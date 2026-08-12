# -*- coding: utf-8 -*-
"""Deterministisk förkontroll: kortets INNEHÅLL mot det som faktiskt hämtades.

## Varför filen finns

`baksida.validate_adamtal()` kollar FORM (tom exempelmening, saknad highlight,
grupper som inte matchar betydelser). Ingenting kollar innehållet mot källan
förrän blindgranskaren gör det -- för hand, mot betalning, sist i kedjan.

Mätt 2026-08-11: av 25 underkännanden i en batch om 100 var 10 synonymfel och
flera av resten var fel som SYNS I DEN HÄMTADE DATAN. Tre exempel, alla
verifierade i `uppslag/`:

    ganglie   SO 0 träffar, SAOL 0 träffar   -- uppslagsordet finns inte
    pryd      hits = [pryd (adj), pryda (verb)] -- glosorna blandar två ord
    oval      popularity_count 9673, märkning [] -- ingen fackterm, ändå
              satte jag domänen "matematik"

Alla tre går att fånga med ett villkor var. Varje fel som fångas här är ett
kort granskaren slipper underkänna OCH ett kort jag slipper göra om -- det är
därför den här kontrollen både höjer kvaliteten och sänker kostnaden.

## Vad den INTE är

Den dömer inte. Den flaggar, så att felen rättas innan det dyra steget körs.
En flagga kan vara falsk (homografer är legitima, `oval` är både adjektiv och
substantiv) -- därför skiljer scriptet på HÅRD och MJUK precis som
`lint_adamtal.py`, och massfixar aldrig.

**Regellogik för FORM bor i `baksida.py` och får inte dupliceras hit.** Det
här scriptet äger bara innehåll-mot-källa, en dimension baksida inte kan se
eftersom den aldrig får uppslagsdatan.

    python forgranska.py sessions/<fil>.json
    python forgranska.py sessions/<fil>.json --bara-hard
    python forgranska.py sessions/<fil>.json --json ut.json
"""
import argparse
import json
import os
import re
import sys
from collections import Counter

import baksida
import config

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HAR = os.path.dirname(os.path.abspath(__file__))

HARDA = (
    "uppslagsord_saknas",
    "frammande_uppslagsord",
    "synonym_utan_stod",
    "register_motsager_markning",
)
MJUKA = (
    "betydelse_kan_saknas",
    "doman_utan_stod",
    "uppslag_saknas",
)

# Underbetydelselistan innehåller maskinmarkörer som inte är betydelser.
_EJ_BETYDELSE = re.compile(r"^(SYN|JFR|ANT|SE):", re.I)

# "neutral"/"allmän" påstår ingenting och kan aldrig motsäga en märkning.
_NEUTRALA = {"neutral", "allmän", "allman", ""}

# MÄTT 2026-08-12, och det avgjorde regelns utformning: av 747 uppslag har
# bara 110 (14,7 %) någon SO-märkning alls. Den första versionen av den här
# kontrollen flaggade "stilnivå utan märkning" och slog därför ut på 19 av 20
# kort i backtestet -- den mätte frånvaro av data, inte fel i kortet.
#
# Rätt riktning är den omvända: flagga när ordboken FAKTISKT säger något och
# kortet säger något annat. Då är tystnad tystnad, och utsaga är bevis.
_MARKNING_NEUTRAL = re.compile(
    r"^(särsk|äv|ibland|vanligen|spec|numera|ofta|i sht|jfr|se|ursprungligen"
    r"|sammanfattande|eg|urspr)\b", re.I)

# Ordbokens etikett och valvets registerord är samma utsaga med olika ord.
# Utan den här tabellen slog regeln ut på `sint`, vars märkning är "prov."
# medan kortet -- korrekt -- säger "dialektal".
_MARKNING_LIKA = {
    "prov": "dialektal", "provinsiellt": "dialektal", "dial": "dialektal",
    "mindre brukligt": "ålderdomlig", "åld": "ålderdomlig",
    "ålderdomligt": "ålderdomlig", "vard": "vardaglig", "vardagligt": "vardaglig",
    "nedsätt": "nedsättande", "skämtsamt": "skämtsam", "ironiskt": "ironisk",
    "formellt": "formell", "litt": "litterär", "språkv": "lingvistik",
    "sjö": "sjöfart", "geol": "geologi", "vulg": "vulgär",
}

# Popularitetsgräns: över detta är ordet för vanligt för att rimligen bära en
# fackspråklig domän utan att ordboken märkt det som fackterm. 9673 (oval)
# ligger över; äkta facktermer i decket ligger typiskt en tiopotens lägre.
POPULARITET_VARDAGSORD = 5000


def _uppslag(ord_):
    f = os.path.join(HAR, "uppslag", ord_ + ".json")
    if not os.path.exists(f):
        return None
    try:
        return json.load(open(f, encoding="utf-8"))
    except Exception:
        return None


def _hits(u, kalla):
    try:
        return u["svenska_se_ratt"][kalla]["hits"]["hits"]
    except Exception:
        return []


def _ortografier(u, kalla):
    ut = []
    for h in _hits(u, kalla):
        o = (h.get("_source") or {}).get("ortografi")
        if o:
            ut.append(str(o))
    return ut


def _popularitet(u):
    """Högsta popularity_count bland träffarna -- ordets vanlighet."""
    pop = []
    for kalla in ("so", "saol"):
        for h in _hits(u, kalla):
            p = (h.get("_source") or {}).get("popularity_count")
            if isinstance(p, int):
                pop.append(p)
    return max(pop) if pop else None


def _so(u, falt):
    try:
        return u["sammandrag"]["svenska_se"]["so"].get(falt) or []
    except Exception:
        return []


def _saol(u, falt):
    try:
        return u["sammandrag"]["svenska_se"]["saol"].get(falt) or []
    except Exception:
        return []


def _kallord(u):
    """Alla ord som förekommer i NÅGON hämtad källa -- stödunderlaget.

    Gloser, exempel, syn.se och wiktionary slås ihop till en påse. En synonym
    som inte finns någonstans i den påsen har inget hämtat stöd alls.
    """
    bitar = []
    for f in ("def", "underbetydelser", "exempel", "jfr"):
        bitar += [str(x) for x in _so(u, f)] + [str(x) for x in _saol(u, f)]
    try:
        avd = u["sammandrag"]["synonymer_se"].get("avdelningar") or {}
        for lista in avd.values():
            bitar += [str(x) for x in lista]
    except Exception:
        pass
    try:
        bitar += [str(x) for x in (u["sammandrag"]["wiktionary"].get("definitioner") or [])]
    except Exception:
        pass
    text = " ".join(bitar).lower()
    return set(re.findall(r"[a-zåäöéèü]+", text)), text


def _stam(ord_):
    """Grov stamning: klipp vanliga svenska ändelser så att böjda former matchar."""
    o = ord_.lower().strip()
    for e in ("ande", "ende", "aste", "are", "ade", "ing", "en", "et", "er",
              "or", "ar", "as", "an", "a", "t", "s"):
        if len(o) - len(e) >= 4 and o.endswith(e):
            return o[: -len(e)]
    return o


def _har_stod(syn, kallpase, kalltext):
    """Finns synonymen i det hämtade underlaget, direkt eller som stam?"""
    s = re.sub(r"<[^>]+>", "", str(syn or "")).strip().lower()
    if not s:
        return True  # tom synonym är baksidas regel, inte vår
    if s in kalltext:
        return True
    delar = re.findall(r"[a-zåäöéèü]+", s)
    if not delar:
        return True
    # Flerordssynonym: räcker att huvudordet har stöd.
    for d in delar:
        if d in kallpase:
            return True
        st = _stam(d)
        if len(st) >= 4 and any(k.startswith(st) for k in kallpase):
            return True
    return False


def _samma_uppslag(traff, ord_):
    """Är träffens uppslagsord samma ord, eller bara en formvariant av det?

    svenska.se listar reflexiva och avledda former som EGNA uppslagsord:
    `ajournera` ger även `ajournera sig`, `kardinal` ger `kardinal-`,
    `pellets` ger `pellet`. Sådana är inte solvens-fällan -- de hör till
    samma ord. Det som ska fångas är `pryd` -> `pryda` och `ans` -> `a`,
    alltså träffar på ett ANNAT lexem.
    """
    a, b = traff.lower().strip(" -"), ord_.lower().strip(" -")
    if a == b:
        return True
    for suffix in (" sig", " ut", " av", " om"):
        if a == b + suffix or b == a + suffix:
            return True
    # Singular/plural och bestämd form av samma ord (pellets/pellet).
    kort, lang = sorted((a, b), key=len)
    return lang.startswith(kort) and lang[len(kort):] in ("s", "n", "t", "en", "et", "er")


def _riktiga_underbetydelser(u):
    return [x for x in _so(u, "underbetydelser")
            if isinstance(x, str) and not _EJ_BETYDELSE.match(x.strip())]


def granska_post(p):
    """Returnerar lista med (regel, detalj) för en post."""
    fel = []
    ord_ = (p.get("ord") or "").strip()
    pr = p.get("proposed") or {}
    if not pr:
        return fel

    u = _uppslag(ord_)
    if u is None:
        fel.append(("uppslag_saknas", f"ingen uppslag/{ord_}.json -- kör slaupp.py"))
        return fel

    # 1. Uppslagsordet finns inte alls (ganglie).
    so_h, saol_h = _hits(u, "so"), _hits(u, "saol")
    if not so_h and not saol_h:
        dym = []
        for kalla in ("so", "saol"):
            try:
                for f in u["svenska_se_ratt"][kalla].get("didYouMean") or []:
                    t = f.get("text") if isinstance(f, dict) else str(f)
                    if t and t not in dym:
                        dym.append(t)
            except Exception:
                pass
        fel.append(("uppslagsord_saknas",
                    "0 träffar i SO och SAOL"
                    + (f" -- menade du: {', '.join(dym[:3])}?" if dym else "")))

    # 2. Glosorna kommer delvis från ett ANNAT uppslagsord (pryd -> pryda).
    frammande = set()
    for kalla in ("so", "saol"):
        for o in _ortografier(u, kalla):
            if not _samma_uppslag(o, ord_):
                frammande.add(o)
    if frammande:
        # Flerordsuttryck går alltid genom fritextsökningen och drar då med sig
        # tiotals grannord (solvens-fällan). Visa några och räkna resten -- hela
        # listan är brus, men ANTALET säger hur illa förorenat underlaget är.
        vis = sorted(frammande)[:6]
        mer = f" (+{len(frammande) - len(vis)} till)" if len(frammande) > len(vis) else ""
        fel.append(("frammande_uppslagsord",
                    f"{len(frammande)} främmande uppslagsord i träffarna: "
                    f"{', '.join(vis)}{mer} -- glosor kan höra till fel ord"))

    # 3. SO har fler betydelser än kortet.
    antal_so = len(_so(u, "def")) + len(_riktiga_underbetydelser(u))
    antal_kort = len(baksida.betydelser(pr.get("huvudbetydelse") or ""))
    if antal_so and antal_kort and antal_so > antal_kort:
        fel.append(("betydelse_kan_saknas",
                    f"SO har {antal_so} betydelser/underbetydelser, kortet har "
                    f"{antal_kort}"))

    # 4. Synonymer utan stöd i något hämtat underlag.
    kallpase, kalltext = _kallord(u)
    if kallpase:
        utan = [s for s in (pr.get("synonymer") or []) if not _har_stod(s, kallpase, kalltext)]
        if utan:
            fel.append(("synonym_utan_stod",
                        f"saknar stöd i hämtad källa: {', '.join(map(str, utan))}"))

    # 5. Ordboken HAR märkt ordet, men kortets register nämner inte märkningen.
    reg = str(pr.get("register") or "").lower()
    markning = [str(x) for x in _so(u, "märkning")] + [str(x) for x in _saol(u, "märkning")]
    # Fältet `märkning` innehåller ibland en hel definitionsfras i stället för
    # en stiletikett ("sammanfattande benämning på kambrium, ordovicium och
    # silur"). En sådan kan inte motsägas av ett register. Etiketter är korta.
    sagande = [m for m in markning
               if not _MARKNING_NEUTRAL.match(m.strip()) and len(m.strip()) <= 30]
    for m in sagande:
        lag = m.lower().strip(" .")
        likvärdig = _MARKNING_LIKA.get(lag)
        if likvärdig and _stam(likvärdig)[:5] in reg:
            continue
        kärna = [w for w in re.findall(r"[a-zåäöéèü]{4,}", lag)
                 if w not in ("sammanhang", "brukligt", "dylikt")]
        kärna += [_MARKNING_LIKA[w] for w in kärna if w in _MARKNING_LIKA]
        if kärna and not any(_stam(w)[:5] in reg for w in kärna):
            fel.append(("register_motsager_markning",
                        f"SO/SAOL märker ordet {m!r} men kortets register säger "
                        f"{pr.get('register')!r}"))

    # 6. Fackspråklig domän på ett vardagsord som ordboken inte märkt som fackterm.
    pop = _popularitet(u)
    for grupp in [g.strip() for g in reg.split(";") if g.strip()]:
        delar = [d.strip() for d in grupp.split(",")]
        doman = delar[2] if len(delar) > 2 else ""
        if doman and doman not in _NEUTRALA and not markning:
            if pop is not None and pop > POPULARITET_VARDAGSORD:
                fel.append(("doman_utan_stod",
                            f"domän {doman!r} men popularitet {pop} och ingen "
                            f"märkning i SO/SAOL"))
    return fel


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fil")
    ap.add_argument("--bara-hard", action="store_true")
    ap.add_argument("--json")
    a = ap.parse_args()

    d = json.load(open(a.fil, encoding="utf-8"))
    poster = d["poster"] if isinstance(d, dict) and "poster" in d else d

    rapport, rakning = [], Counter()
    for p in poster:
        fel = granska_post(p)
        if a.bara_hard:
            fel = [f for f in fel if f[0] in HARDA]
        if fel:
            rapport.append({"ord": p.get("ord"), "noteId": p.get("noteId"),
                            "fel": [{"regel": r, "detalj": t} for r, t in fel]})
        for r, _ in fel:
            rakning[r] += 1

    print("=" * 74)
    print(f"FÖRGRANSKNING  {os.path.basename(a.fil)}  --  {len(poster)} poster, "
          f"{len(rapport)} med anmärkning")
    print("=" * 74)
    for grupp, namn in ((HARDA, "HÅRD"), (MJUKA, "MJUK")):
        rader = [(r, n) for r, n in rakning.most_common() if r in grupp]
        if rader:
            print(f"\n[{namn}]")
            for r, n in rader:
                print(f"  {n:4d}  {r}")
    for post in rapport:
        print(f"\n  {str(post['ord']).upper()}")
        for f in post["fel"]:
            märke = "!!" if f["regel"] in HARDA else "  "
            print(f"    {märke} {f['regel']}: {f['detalj']}")

    if a.json:
        json.dump(rapport, open(a.json, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        print(f"\nSkrev {a.json}")

    hard = sum(n for r, n in rakning.items() if r in HARDA)
    print(f"\n{hard} hårda anmärkningar -- rätta dem INNAN blindgranskningen.")


if __name__ == "__main__":
    main()
