# -*- coding: utf-8 -*-
"""Adam-tal: tre kort forklarade ett deck-ord med ett annat deck-ord.

Regeln ar att forklaringen ska ligga ETT STEG UNDER uppslagsordet. Botas med
omskrivning till enklare fras -- ALDRIG med synonymbyte, for da flyttas bara
problemet.

  docka     'i en hamn'   -> 'vid vattnet'
  gisslare  'botgoring'   -> 'religiost straff for sina synder'
  ta reson  'streta emot' -> 'ge med sig'
"""
import io
import json

FIL = "sessions/session_2026-08-29_v3-batch.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}

BYTEN = {
    "docka": [("anläggning i en hamn där ett fartyg kan torrläggas",
               "anläggning vid vattnet där ett fartyg kan torrläggas")],
    "gisslare": [("Person som piskar sig själv som botgöring",
                  "Person som piskar sig själv som religiöst straff för sina "
                  "synder")],
    "ta reson": [("Ta sitt förnuft till fånga och sluta streta emot",
                  "Ta sitt förnuft till fånga och ge med sig")],
}

for ord_, par in BYTEN.items():
    p = BY[ord_]["proposed"]
    for gammalt, nytt in par:
        assert gammalt in p["huvudbetydelse"], ord_
        p["huvudbetydelse"] = p["huvudbetydelse"].replace(gammalt, nytt)
    print("%-10s %s" % (ord_, p["huvudbetydelse"]))

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("\n%d kort omskrivna" % len(BYTEN))
