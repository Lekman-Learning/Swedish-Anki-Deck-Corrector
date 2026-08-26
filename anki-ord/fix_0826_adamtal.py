# -*- coding: utf-8 -*-
"""Rättar huvudbetydelser som förklarar ett svårt ord med ett annat svårt ord.

Adams invändning 2026-08-26. Mätt med svarighetskoll.py: 12 av 44 kort använde
ett ord som SJÄLVT är ett uppslagsord i decket. Plus fem sammansättningar som
checken inte fångar (efterskänkning, lystringssignal, hålighet, prydnadsband,
själslig) men som är lika svåra.

Regeln som gäller framåt: förklaringen ska ligga en nivå UNDER ordet. Om ett ord
i huvudbetydelsen självt är ett kort i decket, är kortet fel skrivet.
"""
import json

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}

NY = {
    # --- fångade av svarighetskoll.py ---
    "disputation": "Mötet där en doktorand offentligt försvarar sin forskning mot en utsedd kritiker",
    "i onåd": "Att inte längre vara omtyckt av den som bestämmer",
    "obstruktion": "Att med flit sinka eller sabotera något ; något som täpper till",
    "ympa": "Sätta in en kvist från en växt i stammen på en annan så att den växer fast ; vaccinera",
    "anslå": "Ge pengar till ett bestämt ändamål ; sätta upp ett meddelande ; träffa med slag",
    "drastisk": "Kraftig och långtgående ; chockerande rakt på sak",
    "tentakel": "Smal, rörlig arm som djur känner och griper med ; utsträckt arm av någon som i "
                "hemlighet söker inflytande",
    "anglofil": "Person som älskar England och allt engelskt",
    "appell": "Vädjan om att någon ska göra något ; överklagan till högre domstol ; signal som får "
              "en hund att lyda",
    "avlat": "Att katolska kyrkan tar bort ett straff för synder, ofta mot betalning",
    "bemyndiga": "Ge någon rätt att handla eller besluta i ens ställe",
    "bravera": "Skryta och göra sig märkvärdig med det man gjort",
    # --- inte fångade (sammansättningar), men lika svåra ---
    "grav": "Grävd grop i marken där en död läggs ; allvarlig, med svåra följder",
    "girland": "Band av blommor eller löv som hängs upp som prydnad i mjuka bågar",
    "anfäktelse": "Inre oro eller plåga som gnager ; frestelse",
    "saxa": "Ställa i kors, om vartannat ; klippa ut ur en tidning för att citera",
    "attribut": "Typisk egenskap eller sak man känner igen någon på ; ord som bestämmer ett substantiv",
    "betvingande": "Som bryter ner allt motstånd och tvingar fram beundran",
    "amplitud": "Hur långt något svänger ut från sitt viloläge",
    "vidmakthålla": "Se till att något fortsätter finnas eller gälla",
}

n = 0
for o, hb in NY.items():
    if BY[o]["proposed"]["huvudbetydelse"] != hb:
        BY[o]["proposed"]["huvudbetydelse"] = hb
        BY[o]["sokkoll"]["slutsats"] += (
            " OMSKRIVEN 2026-08-26 efter Adams invändning att huvudbetydelserna använt för svåra "
            "ord. Betydelsen är oförändrad; formuleringen ligger nu en nivå under uppslagsordet.")
        n += 1

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Skrev om %d huvudbetydelser." % n)
