# -*- coding: utf-8 -*-
"""Retroaktiv märkning av kort som redan underkänts i blindgranskningen.

Fram till 2026-08-10 gjorde `verdikt` ingenting alls med underkända kort utom
att skriva en loggrad. Spärren finns nu i koden, men de kort som dömdes INNAN
dess ligger fortfarande omärkta i den aktiva kön. Den här filen efterhandsmärker
dem, en gång.

Ett kort räknas som underkänt om dess SENASTE dom är "underkand" -- flera kort
har dömts om efter rättning, och ett kort som först föll och sedan godkändes
ska självklart inte suspenderas. Loggen läses därför i ordning och sista
verdiktet vinner.
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config                      # noqa: E402
from ankiconnect import invoke     # noqa: E402

LOGG = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "oberoende_granskningar.jsonl")


def main():
    sista = {}
    for rad in open(LOGG, encoding="utf-8"):
        rad = rad.strip()
        if not rad:
            continue
        d = json.loads(rad)
        sista[d["noteId"]] = d          # senare rader skriver över tidigare

    underkanda = [d for d in sista.values() if d["verdikt"] == "underkand"]
    if not underkanda:
        print("inga kort med underkänt som senaste dom.")
        return 0

    nids = [d["noteId"] for d in underkanda]
    print("%d kort har UNDERKÄNT som senaste dom:" % len(nids))
    for d in sorted(underkanda, key=lambda x: x["ord"]):
        print("   %-18s %s" % (d["ord"], (d.get("anmarkning") or "")[:78]))

    idag = __import__("datetime").date.today().isoformat()
    invoke("addTags", notes=nids, tags="v3_underkand::%s" % idag)

    kort_ids = []
    for i in range(0, len(nids), 50):
        bit = nids[i:i + 50]
        kort_ids.extend(invoke("findCards",
                               query=" OR ".join("nid:%d" % n for n in bit)))
    for c in kort_ids:
        invoke("setSpecificValueOfCard", card=c, keys=["flags"],
               newValues=[config.FLAG_ROD], warning_check=True)
    invoke("suspend", cards=kort_ids)

    print("\n%d noter taggade v3_underkand::%s" % (len(nids), idag))
    print("%d kort rödflaggade och suspenderade." % len(kort_ids))
    print("Arbetslista framöver:  tag:v3_underkand*")
    return 0


if __name__ == "__main__":
    sys.exit(main())
