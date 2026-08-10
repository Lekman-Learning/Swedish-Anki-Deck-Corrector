# -*- coding: utf-8 -*-
"""Rättar felstavade uppslagsord på FRAMSIDAN.

`applicera` skriver bara baksidan, av god anledning: framsidan är det ord
kortet handlar om, och att ändra den tyst vore att byta ut kortet mot ett
annat. Därför ligger den här rättelsen i en egen fil, med kravet att varje
ändring ska vara belagd — den felstavade formen ska ge NOLL träffar i
källorna och den rättade ska finnas i SO.

2026-08-10: `in media res` gav noll träffar i svenska.se, synonymer.se och
wiktionary. Den korrekta latinska formen är `in medias res` (ackusativ
plural, 'in i sakerna'), som finns i SO med betydelsen 'omedelbart in i
ämnet', belagd sedan 1884. Kortet lärde alltså ut en felstavning.

Batchfilens `ord`-fält uppdateras samtidigt, så att blindgranskaren får se
det rättade ordet — annars skulle den (helt riktigt) underkänna kortet för
att uppslagsordet inte finns.
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ankiconnect import invoke      # noqa: E402

HAR = os.path.dirname(os.path.abspath(__file__))
FIL = os.path.join(HAR, "sessions", "session_2026-08-10_v3-omgranskning-nya3.json")

RATTELSER = {1780080619842: ("in media res", "in medias res")}


def main():
    for nid, (fel, ratt) in RATTELSER.items():
        n = invoke("notesInfo", notes=[nid])[0]
        nu = n["fields"]["Framsida"]["value"].strip()
        if nu == ratt:
            print("%-16s redan rättad." % ratt)
            continue
        if nu != fel:
            print("AVBRYTER: framsidan på %d är '%s', väntade '%s'." % (nid, nu, fel))
            return 1
        invoke("updateNoteFields", note={"id": nid, "fields": {"Framsida": ratt}})
        print("%-16s -> %s   (nid %d)" % (fel, ratt, nid))

    d = json.load(open(FIL, encoding="utf-8"))
    kort = d["kort"] if isinstance(d, dict) and "kort" in d else d
    bytta = 0
    for e in kort:
        r = RATTELSER.get(e["noteId"])
        if r and e["ord"] == r[0]:
            e["ord"] = r[1]
            bytta += 1
    json.dump(d, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("batchfilen: %d uppslagsord bytta." % bytta)
    return 0


if __name__ == "__main__":
    sys.exit(main())
