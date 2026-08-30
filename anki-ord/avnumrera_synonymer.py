# -*- coding: utf-8 -*-
"""Tar bort numreringen ur synonymfaltet pa redan skrivna kort.

Adams besked 2026-08-30, efter kortet `agnat` ("1. slakting pa manssidan"):
*"inga synonymer ska vara numrerade"*.

`baksida.build()` numrerade tidigare de kvarvarande grupperna nar NAGON
betydelse saknade synonym, sa att kopplingen synonym->betydelse inte foll
bort tyst. Numreringen ar borttagen ur build(); det har skriptet stader upp
de kort som redan bar den.

SAKERHETSREGLER

 * Bara kort dar `parse()` faktiskt hittar v2-strukturen ROrs. Ett kort som
   parsas till tomt skrivs aldrig -- en parse->build-runda pa ett
   legacy-kort hade skrivit over innehallet med ingenting.
 * Bara kort dar SYNONYMFALTET bar siffran. En "1." i exempelmeningen eller
   etymologin ar inte det vi letar efter, och min forsta grova regex
   (`(^|>|\\s)\\d+\\.\\s` over hela baksidan) traffade 213 noter -- fler an de
   som faktiskt hade numrerade synonymer.
 * Torrkorning ar default. `--kor` skriver.
"""
import argparse
import re

import baksida
import config
from ankiconnect import invoke

NUMMER = re.compile(r"(^|;\s*)\d+\.\s")


def synonymrad(raw_html):
    """Raa synonymstrangen ur en v2-baksida, eller None."""
    m = baksida._MAIN_RE.search(raw_html or "")
    return m.group("syn") if m else None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--kor", action="store_true")
    p.add_argument("--visa", type=int, default=10)
    a = p.parse_args()

    nids = invoke("findNotes", query='deck:"%s"' % config.DECK_NAME)
    print("noter i decket: %d" % len(nids))

    traffar = []
    for i in range(0, len(nids), 2000):
        for n in invoke("notesInfo", notes=nids[i:i + 2000]):
            falt = n["fields"]
            raw = (falt.get(config.FIELD_BAKSIDA) or {}).get("value", "")
            rad = synonymrad(raw)
            if not rad or not NUMMER.search(rad):
                continue
            # Ett enda kort (`intim`) bar den kortlivade '·'-formen som
            # build() anvande i nagra timmar 2026-08-30 innan den visade sig
            # bryta rundturen. parse() delar bara pa ';' och ',', sa
            # "privat · 2. nara" blev EN synonym. Normaliseras hit till ';'
            # sa att grupperna kommer tillbaka intakta.
            if "·" in raw:
                raw = raw.replace(" · ", " ; ").replace("·", ";")
            parsed = baksida.parse(raw)
            if not (parsed["huvudbetydelse"] or parsed["synonymer"]):
                print("  HOPPAR (parsas till tomt): %s" % n["noteId"])
                continue
            ny = baksida.build(
                parsed["huvudbetydelse"], synonymer=parsed["synonymer"],
                synonym_groups=parsed["synonym_groups"],
                exempelmening=parsed["exempelmening"],
                register=parsed["register"], etymologi=parsed["etymologi"],
                bild_html=parsed["bild_html"])
            if ny == raw:
                continue
            ord_ = list(falt.values())[0]["value"]
            traffar.append((n["noteId"], ord_, rad.strip(),
                            synonymrad(ny) or "", ny))

    print("kort med numrerad SYNONYMRAD: %d" % len(traffar))
    for _, ord_, fore, efter, _ in traffar[:a.visa]:
        print("   %-22s %-38s -> %s"
              % (re.sub("<[^>]+>", "", ord_)[:22], fore[:38], efter.strip()[:38]))
    if len(traffar) > a.visa:
        print("   ... och %d till" % (len(traffar) - a.visa))

    if not a.kor:
        print("\n(torrkorning -- kor med --kor for att skriva)")
        return

    for nid, _, _, _, ny in traffar:
        invoke("updateNoteFields",
               note={"id": nid, "fields": {config.FIELD_BAKSIDA: ny}})
    print("\nskrivna: %d" % len(traffar))

    kvar = 0
    for i in range(0, len(nids), 2000):
        for n in invoke("notesInfo", notes=nids[i:i + 2000]):
            rad = synonymrad((n["fields"].get(config.FIELD_BAKSIDA) or {}).get("value", ""))
            if rad and NUMMER.search(rad):
                kvar += 1
    print("kort med numrerad synonymrad kvar: %d" % kvar)


main()
