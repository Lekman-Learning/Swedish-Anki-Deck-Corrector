# -*- coding: utf-8 -*-
"""Synonymkandidater rangordnade efter hur starkt belägget är.

## Varför filen finns

Blindgranskningen 2026-08-11 underkände 25 av 100 kort. **10 av de 25 föll på
SYNONYMERNA**, inte på betydelsen — den enskilt största felkategorin i
omgången. Exempel: `entomologi` hade *insektologi* (ett ord som inte finns),
`hortonom` hade *landskapsarkitekt* (ett annat yrke), `abstrahera` hade
*avskilja* (latinsk etymologi, inte svensk betydelse).

Adams förslag var att hämta de bästa synonymerna från synonymer.se. Det
mättes mot de tio fallen och **fungerar inte**: syn.se INNEHÖLL den underkända
synonymen i 5 av 10 fall (`bortklemad` → *ouppfostrad*, *klemig*; `bemänga` →
*späda*, *tillsätta*; `barm` → *bringa*, *famn*; `kommissarie` → *ombud*;
`abstrahera` → *avskilja*), hade rätt svar i 3 och ingenting alls i 2.

Orsaken är strukturell och inte ett kvalitetsfel hos sajten: **synonymer.se är
en tesaurus.** En tesaurus listar ord i samma betydelseområde. Ett kort
behöver ord som går att BYTA UT. `barm` och `famn` hör ihop; de är inte
utbytbara. `bemänga` och `späda` handlar båda om att blanda — åt motsatt håll.

## Vad filen gör i stället

Rangordnar kandidater efter belägg, starkast först:

    ORDBOKSGLOSS  SO:s och SAOL:s egna definitioner, när de är korta nog att
                  fungera som gloss. Detta är det STARKASTE belägget som
                  finns: ordboken påstår själv att uttrycken är likvärdiga.
                  SAOL säger rakt ut att en kväkare är "medlem av den
                  religiösa rörelsen Vännernas samfund" -- en korrekt synonym
                  som fanns tillgänglig hela tiden medan kortet i stället fick
                  den påhittade stavningen *kvekare*.

    TESAURUS      synonymer.se:s redaktionella avdelningar. KANDIDATER, inte
                  facit. Var och en måste klara utbytbarhetstestet nedan.

Filen väljer inte åt granskaren. Den lägger fram underlaget med belägget
utskrivet, så att valet går att göra och går att granska i efterhand.

## Utbytbarhetstestet

Det testet var vad blindgranskaren faktiskt tillämpade, och det vi saknade:

    Går synonymen att sätta in i stället för ordet i exempelmeningen
    utan att meningen ändras?

*Ouppfostrad* klarar inte det mot "en bortklemad unge" — en unge kan vara
bortskämd utan att vara ouppfostrad. Testet går mot SO:s definition, som
redan hämtas för varje ord.

    python synonymforslag.py ord1 ord2 ...
    python synonymforslag.py --sessionsfil sessions/<fil>.json
"""

import argparse
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HAR = os.path.dirname(os.path.abspath(__file__))
UPPSLAG = os.path.join(HAR, "uppslag")

ANVANDARAVDELNING = "användarnas bidrag"

# Samma skräp som slaupp.py filtrerar vid hämtning. Upprepat HÄR eftersom
# uppslag/ innehåller filer som sparades FÖRE den fixen -- 727 stycken
# 2026-08-11. Utan det här filtret läser den här filen tillbaka just den
# sidfotslänk som nyss togs bort ur inhämtningen.
_EJ_SYNONYM = ("tillbaka i grottekvarnen", "motsatsord", "användarnas bidrag",
               "synonymer", "andra ord", "korsord")

# En gloss som är längre än så här är en definition att läsa, inte ett ord att
# sätta in i en mening. Gränsen är satt så att SAOL:s "medlem av den religiösa
# rörelsen Vännernas samfund" (46 tecken) ryms -- den är lång men fungerar som
# synonym, och den är exakt det slags svar som saknades på `kväkare`.
GLOSSTAK = 55

# Definitionsinledningar som gör glossen till en beskrivning i stället för en
# utbytbar synonym. "som avviker från det typiska" kan inte ersätta `atypisk`
# i en mening; "avvikande" kan.
_BESKRIVANDE = re.compile(r"^(som|vilken|där|när|det att|en person som)\b", re.I)

# Bruklighets- och omfångskvalifikatorer är INTE glosor. `barm` gav annars
# SAOL:s "särsk. hos kvinnor" som synonymkandidat -- en precisering av den
# föregående definitionen, inte ett ord som kan ersätta `barm` i en mening.
_KVALIFIKATOR = re.compile(
    r"^(särsk|äv|ibland|vanligen|spec|numera|förr|ofta|bildl|i sht|jfr|se)\b\.?",
    re.I)


def _txt(v):
    if isinstance(v, str):
        return re.sub(r"<[^>]+>", "", v).strip()
    if isinstance(v, list):
        return " | ".join(x for x in (_txt(i) for i in v) if x)
    return ""


def _las(ord_):
    f = os.path.join(UPPSLAG, ord_.replace(" ", "_") + ".json")
    if not os.path.exists(f):
        return None
    try:
        return json.load(open(f, encoding="utf-8"))
    except Exception:
        return None


def _rensa(t, ord_):
    t = " ".join(t.split()).strip(" .;:,")
    lag = t.lower()
    if not t or lag == ord_.lower():
        return None
    if lag in _EJ_SYNONYM or "grottekvarnen" in lag:
        return None
    return t


def ordboksglosor(data, ord_):
    """SO:s och SAOL:s definitioner, delade till gloss-storlek."""
    ut = []
    sv = (data.get("sammandrag") or {}).get("svenska_se") or {}
    for bok in ("so", "saol"):
        d = sv.get(bok) or {}
        if not isinstance(d, dict):
            continue
        for rad in (d.get("def") or []):
            # '|' skiljer SO:s huvudbetydelser, ';' och ',' delbetydelser.
            for bit in re.split(r"[|;]", _txt(rad)):
                b = _rensa(bit, ord_)
                if not b or len(b) > GLOSSTAK or _KVALIFIKATOR.match(b):
                    continue
                beskrivande = bool(_BESKRIVANDE.match(b))
                ut.append((b, bok.upper(), beskrivande))
    # Behåll ordningen men ta bort dubbletter (SO och SAOL säger ofta samma sak).
    sedda, unika = set(), []
    for b, bok, beskr in ut:
        if b.lower() in sedda:
            continue
        sedda.add(b.lower())
        unika.append((b, bok, beskr))
    return unika


def tesauruskandidater(data, ord_):
    """synonymer.se:s redaktionella avdelningar — kandidater, inte facit."""
    syn = ((data.get("sammandrag") or {}).get("synonymer_se")) or {}
    ut = []
    for namn, innehall in (syn.get("avdelningar") or {}).items():
        lag = namn.lower()
        if ANVANDARAVDELNING in lag:
            continue
        # Motsatsavdelningen är farligast av allt att kopiera rakt av: den
        # innehåller ord som betyder TVÄRTOM. `framfusig` gav annars *försynt*
        # och *taktfull* som synonymkandidater. Ett kort med en antonym som
        # synonym lär ut motsatsen till det som står i huvudbetydelsen.
        if "motsats" in lag or "antonym" in lag:
            continue
        for x in (innehall if isinstance(innehall, list) else [innehall]):
            for bit in re.split(r"[,;|]", _txt(x)):
                b = _rensa(bit, ord_)
                if b and b.lower() not in {y.lower() for y in ut}:
                    ut.append(b)
    return ut


def rapport(ord_):
    data = _las(ord_)
    rader = [f"### {ord_}"]
    if not data:
        rader.append("   [ingen sparad uppslagning — kör slaupp.py först]")
        return "\n".join(rader)

    glosor = ordboksglosor(data, ord_)
    kandidater = tesauruskandidater(data, ord_)

    if glosor:
        rader.append("   ORDBOKSGLOSS (starkast belägg — ordboken påstår likvärdighet):")
        for b, bok, beskr in glosor:
            markering = "  [beskrivande — omformulera till utbytbar form]" if beskr else ""
            rader.append(f"      {bok:<5} {b}{markering}")
    else:
        rader.append("   ORDBOKSGLOSS: (ingen tillräckligt kort definition)")

    if kandidater:
        rader.append("   TESAURUS (kandidater — testa utbytbarhet var för sig):")
        rader.append("      " + ", ".join(kandidater))
    else:
        rader.append("   TESAURUS: (inget redaktionellt innehåll)")

    if not glosor and not kandidater:
        rader.append("   ⚠ INGEN GRUND — sätt inga synonymer på det här kortet.")
    return "\n".join(rader)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ord", nargs="*")
    ap.add_argument("--sessionsfil")
    a = ap.parse_args()

    ord_lista = list(a.ord)
    if a.sessionsfil:
        d = json.load(open(a.sessionsfil, encoding="utf-8"))
        poster = d["poster"] if isinstance(d, dict) and "poster" in d else d
        ord_lista += [p.get("ord") if isinstance(p, dict) else p for p in poster]
    if not ord_lista:
        print(__doc__)
        return 1
    for o in ord_lista:
        print(rapport(o))
    return 0


if __name__ == "__main__":
    sys.exit(main())
