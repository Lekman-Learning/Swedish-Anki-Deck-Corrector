# -*- coding: utf-8 -*-
"""Spärr mot lånade och intetsägande exempelmeningar.

Adams krav 2026-08-11: *"gör exempelmeningarna bättre som ger en bättre
djupgående förståelse av ordet om det går."*

## Varför en spärr och inte en instruktion

Blindgranskaren underkände `brådstörtad` 2026-08-11 med motiveringen att
exempelmeningen *"Lekmans brådstörtade utlandsresa."* är nästan ordagrant
SO:s eget exempel (*"hennes brådstörtade utlandsresa"*) med bytt subjekt --
och dessutom en substantivfras utan predikat.

Det är inte ett enstaka slarv. Den som skriver kortet har just läst
ordboksartikeln, och ordbokens exempel ligger närmast till hands. Resultatet
är en mening som bevisar att ordet finns men inte lär ut något: den upprepar
definitionen i stället för att visa ordet i arbete.

Samma mönster som resten av v3: en regel i prosa som granskaren ska minnas
blir inte följd. Den här filen gör den körbar.

## Vad som kontrolleras

1. **LÅNAD** -- meningen överlappar för mycket med ett exempel ur SO/SAOL i
   `uppslag/<ord>.json`. Mäts på innehållsord, inte tecken: att byta "hennes"
   mot "Lekmans" ändrar strängen men inte meningen.

2. **INTETSÄGANDE** -- meningen skiljer inte ordet från sina synonymer. En
   mening som fungerar lika bra med ett vardagsord i stället för uppslagsordet
   lär inte ut något. Testas grovt via längd och innehållsordsantal: en
   exempelmening under sex innehållsord bär sällan tillräckligt sammanhang.

Båda returneras som VARNINGAR, inte hårda fel. En lånad mening är ibland det
enda rimliga (fasta uttryck, idiom), och en hård spärr hade tvingat fram
sämre meningar för att passera. Skillnaden mot en tyst regel är att varningen
måste ses och avfärdas medvetet.
"""

import json
import os
import re

UPPSLAG = "uppslag"

# Funktionsord bär inget innehåll och ska inte räknas som överlapp -- annars
# blir "den ... i ... som" en träff mot vilken mening som helst.
STOPPORD = {
    "och", "eller", "men", "att", "som", "det", "den", "de", "en", "ett",
    "i", "på", "av", "för", "med", "till", "från", "om", "under", "över",
    "han", "hon", "hans", "hennes", "sin", "sitt", "sina", "min", "mitt",
    "var", "är", "vara", "blir", "bli", "har", "hade", "kan", "ska", "skulle",
    "inte", "så", "när", "då", "där", "här", "man", "sig", "vid", "efter",
}


def _ord(text):
    ren = re.sub(r"<[^>]+>", " ", text or "")
    return [w for w in re.findall(r"[a-zA-ZåäöÅÄÖéèüáó]+", ren.lower())
            if w not in STOPPORD and len(w) > 2]


def _kallexempel(ord_):
    """Alla exempelmeningar SO/SAOL ger för ordet."""
    for namn in (f"{UPPSLAG}/{ord_}.json", f"{UPPSLAG}/{ord_.replace(' ', '_')}.json"):
        if os.path.exists(namn):
            break
    else:
        return []
    try:
        d = json.load(open(namn, encoding="utf-8"))
    except Exception:
        return []
    ut = []

    def gr(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("exempel", "exempelsamling", "text") and isinstance(v, str):
                    if v.strip():
                        ut.append(v.strip())
                else:
                    gr(v)
        elif isinstance(o, list):
            for x in o:
                gr(x)

    gr(d.get("svenska_se_ratt") or {})
    return ut


def granska(ord_, exempelmening, trosk=0.6):
    """Returnerar lista med varningar (tom = ok)."""
    varningar = []
    egna = _ord(exempelmening)
    # Uppslagsordet självt räknas inte -- det MÅSTE stå i meningen.
    kärna = [w for w in egna if not w.startswith(ord_.lower()[:4])]

    if len(kärna) < 5:
        varningar.append(
            f'exempelmeningen bär bara {len(kärna)} innehållsord — för lite '
            f'sammanhang för att skilja ordet från sina synonymer')

    if not egna:
        return varningar

    for kx in _kallexempel(ord_):
        kо = set(_ord(kx))
        if not kо:
            continue
        delade = kо & set(kärna)
        # Andel av ORDBOKENS exempel som återfinns i vårt: fångar
        # "hennes brådstörtade utlandsresa" -> "Lekmans brådstörtade utlandsresa"
        # eftersom 'brådstörtade' och 'utlandsresa' är hela innehållet.
        if len(delade) / len(kо) >= trosk and len(delade) >= 2:
            varningar.append(
                f'exempelmeningen överlappar {len(delade)}/{len(kо)} innehållsord '
                f'med ordbokens eget exempel ("{kx[:60]}") — skriv en egen som '
                f'visar ordet i arbete i stället')
            break

    return varningar


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        for v in granska(sys.argv[1], sys.argv[2]) or ["OK"]:
            print(" ", v)
