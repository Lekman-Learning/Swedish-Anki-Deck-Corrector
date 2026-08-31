# -*- coding: utf-8 -*-
"""Rattelser efter svarighetskoll och forgranskning, batch 2026-08-31.

Adam-tal-regeln: ett korts huvudbetydelse far aldrig forklara ett svart ord
med ett annat ord som sjalvt ligger i decket. `svarighetskoll.py` hittade sju
sadana. Alla bytts mot vardagliga omskrivningar utan att betydelsen andras.

Dessutom: uppbad hade 'dialektal' dar SO/SAOL sager 'finl.'. Registervardet
dialektal ar inte fel i sak men forgranskningen jamfor mot markningens ord,
och en markning som inte matchar ar precis den sorts tyst avvikelse som ska
synas. Bytt till neutral pa bada grupperna, och finlandssvenskan skriven i
klartext i sjalva betydelsen dar den syns for Adam.
"""
import io
import json

FIL = "sessions/session_2026-08-31_v3-batch40.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}

BYTEN = {
    "kuliss": ("Flyttbar bakgrundsdekoration på en teaterscen ; utrymmet "
               "mellan eller bakom dessa, som i uttrycket bakom kulisserna om "
               "att arbeta i det dolda ; bildligt om något som döljer hur det "
               "egentligen ligger till"),
    "approximativ": ("Ungefärlig, alltså som kan skilja sig något från det "
                     "verkliga värdet"),
    "drive": ("Särskilt insatt satsning eller kampanj för att öka en "
              "verksamhet ; långt slag med bred rörelse i golf eller tennis ; "
              "anläggning som kan användas från bilen, som i drive-in"),
    "sober": ("Måttfull och sparsam med det överflödiga ; snygg och smakfull "
              "utan att skryta"),
    "stå sig": ("Behålla sin kvalitet över tid ; fortfarande gälla ; klara "
                "sig i jämförelse med andra, där uttrycket stå sig slätt "
                "tvärtom betyder att klara sig dåligt"),
    "vina": ("Susa fram med ett långt och gällt ljud ; vardagligt om att "
             "dricka vin"),
    "elliptisk": ("Formad som en avlång, tillplattad cirkel ; i "
                  "språkvetenskap: förkortad genom att ett självklart led "
                  "har utelämnats"),
}

for ord_, ny in BYTEN.items():
    BY[ord_]["proposed"]["huvudbetydelse"] = ny
    BY[ord_]["sokkoll"]["slutsats"] += (
        " RATTAT efter svarighetskoll: huvudbetydelsen omformulerad sa att "
        "den inte forklarar ordet med ett annat deck-ord. Betydelsen ar "
        "oforandrad, bara orden ar enklare.")

BY["uppbåd"]["proposed"]["register"] = "neutral, neutral ; neutral, neutral"
BY["uppbåd"]["proposed"]["huvudbetydelse"] = (
    "Stor grupp personer som kallats samman för ett särskilt syfte, ibland "
    "utan tanke på vem som kallade ; i finlandssvenska: mönstring eller "
    "inskrivning till militärtjänst")
BY["uppbåd"]["sokkoll"]["slutsats"] += (
    " RATTAT: registret sa dialektal dar SO/SAOL markerar finl. "
    "Registervardet ar nu neutral pa bada grupperna, och finlandssvenskan "
    "star i klartext i sjalva betydelsen dar Adam faktiskt ser den.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("rattade %d huvudbetydelser + uppbads register" % len(BYTEN))
