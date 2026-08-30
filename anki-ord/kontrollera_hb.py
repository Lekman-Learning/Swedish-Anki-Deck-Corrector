# -*- coding: utf-8 -*-
"""Jamfor huvudbetydelsen i Anki mot den senaste sessionsfil som skrev ordet.

Bakgrunden: kortet `agnat` visade sig ha huvudbetydelsen
"Slakting pa fadernesidan, SLAKTING PA MANSSIDAN ; att satta bete pa en krok"
i Anki, medan sessionsfilen som skrev det sager
"Slakting pa fadernesidan, ALLTSA VIA MAN ; ...". Adam hade dessutom just
klistrat in den RATTA formen ur sitt eget kort.

Nagonstans mellan sessionsfilen och Anki har alltsa en huvudbetydelse bytt
innehall, och synonymen har krupit in i den. Innan jag gissar vidare om
orsaken vill jag veta OMFATTNINGEN: galler det ett kort eller manga?

Skriptet ar rent lasande.
"""
import glob
import io
import json
import re

import baksida
import config
from ankiconnect import invoke


def sessionsvarden():
    """{ord: (huvudbetydelse, filnamn)} fran den SENAST andrade sessionsfil
    som bar ett forslag for ordet."""
    ut = {}
    for sv in sorted(glob.glob("sessions/*.json")):
        try:
            d = json.load(io.open(sv, encoding="utf-8"))
        except ValueError:
            continue
        if not isinstance(d, list):
            d = d.get("poster") or []
        for p in d:
            if not isinstance(p, dict):
                continue
            v = p.get("proposed")
            if not isinstance(v, dict) or not v.get("huvudbetydelse"):
                continue
            ut[p.get("ord")] = (v["huvudbetydelse"], sv)
    return ut


def main():
    fasit = sessionsvarden()
    print("ord med forslag i nagon sessionsfil: %d" % len(fasit))

    nids = invoke("findNotes", query='deck:"%s"' % config.DECK_NAME)
    olika, lika, saknas = [], 0, 0
    for i in range(0, len(nids), 2000):
        for n in invoke("notesInfo", notes=nids[i:i + 2000]):
            falt = n["fields"]
            ord_ = re.sub("<[^>]+>", "", list(falt.values())[0]["value"]).strip()
            if ord_ not in fasit:
                continue
            raw = (falt.get(config.FIELD_BAKSIDA) or {}).get("value", "")
            hb = baksida.parse(raw)["huvudbetydelse"]
            vantad, sv = fasit[ord_]
            if not hb:
                saknas += 1
            elif hb.strip() == vantad.strip():
                lika += 1
            else:
                olika.append((ord_, vantad, hb, sv))

    print("stammer med sessionsfilen : %d" % lika)
    print("parsas till tomt          : %d" % saknas)
    print("SKILJER SIG               : %d" % len(olika))
    for ord_, vantad, hb, sv in olika[:40]:
        print("\n  %s   (%s)" % (ord_, sv))
        print("    sessionsfil : %s" % vantad)
        print("    Anki        : %s" % hb)
    if len(olika) > 40:
        print("\n  ... och %d till" % (len(olika) - 40))


main()
