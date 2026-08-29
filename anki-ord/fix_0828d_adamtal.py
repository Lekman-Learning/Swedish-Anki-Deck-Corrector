# -*- coding: utf-8 -*-
"""Adam-tal-rattelser pa v3-batch5. Kort fras, aldrig synonymbyte."""
import io
import json

FIL = "sessions/session_2026-08-28_v3-batch5.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}

NY = {
    # "ränna" -> "spår"
    "sponta": "Forma kanterna på en bräda så att den ena får en tunga och "
              "den andra ett spår, så att bräderna kan låsas i varandra ; "
              "klä en yta med sådana bräder",
    # "böjd" -> "krökt/kroknar" (bojd ar sjalvt ett deck-ord)
    "krum": "Krokig i formen, som något som har krökt sig ; som substantiv: "
            "själva kröken — \"med ryggen i krum\"",
    # "anständig" + "återhållsam" -> utskrivet
    "tuktig": "Som håller sig i strama tyglar moraliskt: behärskad, sträng "
              "mot sig själv och noga med att inte gå över gränsen",
    # "bevilja" -> "säga ja till"
    "entlediga": "Skilja någon från en tjänst eller ett uppdrag ; också: "
                 "säga ja till det avsked som personen själv har bett om",
    # "färdighet" -> "sak man behöver kunna"
    "etyd": "Musikstycke skrivet för att öva upp en bestämd sak man behöver "
            "kunna på sitt instrument ; också om ett sådant stycke som är så "
            "krävande att det spelas på konsert",
    # "överdådig" -> utskrivet
    "extravagant": "Så påkostad och slösaktig att den visar upp rikedom ; "
                   "också om ett beteende som går långt utöver det vanliga",
    # "enträgen" -> "ihärdig"
    "ävlan": "Ivrig och ihärdig strävan efter något",
}

for ord_, bet in NY.items():
    e = BY[ord_]
    gammal = e["proposed"]["huvudbetydelse"]
    assert len(bet.split(" ; ")) == len(gammal.split(" ; ")), ord_
    e["proposed"]["huvudbetydelse"] = bet

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("rattade %d kort" % len(NY))
