# -*- coding: utf-8 -*-
"""Hittar ord dar a/o skrivits i stallet for a/a/o -- avdiakritiserad svenska.

VARFOR. Adam 2026-08-30: kortet `skurril` hade etymologin
"scurra 'dagdrivare, skamtare'". Ordet ar `skamtare`. Jag skriver ASCII i
kodkommentarer for att slippa konsolproblem i Windows, och den vanan har
lackt in i innehallet som skrivs till Anki. Ett kort som lar ut en
felstavning ar samre an inget kort.

METOD. Korpusen ar `uppslag/*.json` -- 2 977 uppslagningar mot svenska.se,
alltsa riktig svenska med korrekta diakriter. Ur den byggs:

    RIKTIGA   alla ordformer som faktiskt forekommer
    VIKT      vikt(ord utan diakriter) -> {former MED diakriter}

Ett token flaggas nar BADA galler:
    1. det ar rent ASCII och dess viktade form har en akta a/a/o-variant
    2. tokenet sjalvt finns INTE i korpusen som eget ord

Regel 2 ar det som haller nere falsklarmen: `har`, `for`, `far`, `mot`,
`vara` ar alla riktiga svenska ord och flaggas darfor aldrig, aven om de
OCKSA ar viktade former av `har`/`for`/`far`/`mot`/`vara`.

BEGRANSNINGEN som foljer av det maste sagas hogt: skriptet kan INTE hitta
ett fel dar den avdiakritiserade formen rakar vara ett annat riktigt ord.
Skriver jag "for" nar jag menar "for" ser det ut som datidsformen av `fara`.
Sadana fel maste hittas med ogonen.
"""
import glob
import io
import json
import re
import sys

import config
from ankiconnect import invoke

ORD = re.compile(r"[a-zA-ZåäöÅÄÖéèüáàçñ]{3,}")
VIKT_KARTA = {"å": "a", "ä": "a", "ö": "o", "Å": "A", "Ä": "A", "Ö": "O"}


def vikt(s):
    return "".join(VIKT_KARTA.get(c, c) for c in s)


def bygg_korpus():
    riktiga = set()
    vikter = {}

    def gav(v):
        if isinstance(v, str):
            for m in ORD.finditer(v):
                w = m.group(0).lower()
                riktiga.add(w)
                if any(c in w for c in "åäö"):
                    vikter.setdefault(vikt(w), set()).add(w)
        elif isinstance(v, dict):
            for x in v.values():
                gav(x)
        elif isinstance(v, list):
            for x in v:
                gav(x)

    for fn in glob.glob("uppslag/*.json"):
        try:
            gav(json.load(io.open(fn, encoding="utf-8")))
        except ValueError:
            continue
    return riktiga, vikter


def main():
    riktiga, vikter = bygg_korpus()
    print("korpus: %d ordformer, %d viktade a/a/o-nycklar"
          % (len(riktiga), len(vikter)))

    nids = invoke("findNotes", query='deck:"%s"' % config.DECK_NAME)
    print("noter i decket: %d" % len(nids))

    fynd = []
    for i in range(0, len(nids), 2000):
        for n in invoke("notesInfo", notes=nids[i:i + 2000]):
            falt = n["fields"]
            ord_ = re.sub("<[^>]+>", "",
                          list(falt.values())[0]["value"]).strip()
            for namn, f in falt.items():
                txt = re.sub("<[^>]+>", " ", f["value"] or "")
                txt = txt.replace("&nbsp;", " ")
                for m in ORD.finditer(txt):
                    t = m.group(0)
                    tl = t.lower()
                    if any(c in tl for c in "åäö"):
                        continue
                    if tl in riktiga:
                        continue
                    kand = vikter.get(tl)
                    if not kand:
                        continue
                    fynd.append({"noteId": n["noteId"], "ord": ord_,
                                 "falt": namn, "fel": t,
                                 "forslag": sorted(kand)})

    print("\nTRAFFAR: %d i %d noter"
          % (len(fynd), len({f["noteId"] for f in fynd})))
    from collections import Counter
    c = Counter((f["fel"].lower(), ", ".join(f["forslag"])) for f in fynd)
    for (fel, forslag), n in c.most_common(60):
        print("  %4d  %-24s -> %s" % (n, fel, forslag))
    if len(c) > 60:
        print("  ... och %d fler unika ord" % (len(c) - 60))

    json.dump(fynd, io.open("aao_fynd.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("\nskrev aao_fynd.json")


main()
