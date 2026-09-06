# -*- coding: utf-8 -*-
"""Svarighetskollen: 7 kort forklarade ett svart ord med ett annat deck-ord.

Regeln (kortbyggare._ADAMTAL, skarpt 2026-08-26): inget ord i huvudbetydelsen
far sjalvt vara ett uppslagsord i decket, och noll traffar ar kravet -- inte en
ambition. Rattat med KORTA FRASER, aldrig genom att byta det svara ordet mot en
enklare synonym (svenskan har nastan inga exakta synonymer, och bytet tranar
precis det fel HP:s ORD-del straffar).

Plus den sista harda forgranskningsanmarkningen for belagga.
"""
import io, json

FIL = "sessions/session_2026-09-06_v3-omgranskning.json"

HB = {
 # 'pragel' och 'stilfull' ut. SO:s eget 'fornamt' far bara definitionen.
 "mondän": "Förnämt fin, på det sätt som hör den stora världen till",
 # 'just' ut -- ordet fyllde ingen funktion.
 "avpassa": "Ge något rätt storlek, mängd eller form för det den ska användas till",
 # 'overlatelse' ut, ersatt med korta fraser som sager samma sak.
 "cession": "En långivares överföring av sin fordran till någon annan, utan att "
            "låntagaren behöver vara med ; att en stat lämnar över ett landområde "
            "till en annan ; konkurs",
 # 'tacka' och 'pafoljd' ut. SO:s egen parentes '<<t.ex. straff el. avgift>>'
 # gav ersattningen for den senare.
 "belägga": "Lägga ett skyddande lager över en yta ; ta upp platsen i något så att "
            "den är upptagen ; genom beslut förena med en avgift eller ett förbud, "
            "till exempel skatt ; göra fast ett tåg om en knap ; visa med fakta att "
            "något stämmer ; visa att ett ord har funnits i språket vid en viss tid",
 # 'ihallande' ut.
 "mola": "Göra dovt ont som håller i sig länge, utan att svida till",
 # 'forbehall' ut.
 "obetingad": "Som sker av sig själv utan att ha lärts in, till exempel en reflex ; "
              "helt utan villkor eller krav",
 # 'cylindrisk' ut.
 "svängtapp": "Kort rund axel som något annat kan svänga runt",
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    pr = e.get("proposed")
    if not pr:
        continue
    if e["ord"] in HB:
        pr["huvudbetydelse"] = HB[e["ord"]]
        n += 1
    if e["ord"] == "belägga":
        # Synonymgrupp 1 folide definitionens 'tacka', som nu ar borta.
        pr["synonym_groups"][0] = ["≈≈ skyddande lager"]
        pr["synonymer"] = [s for g in pr["synonym_groups"] for s in g]
        e["forgranska_tillat"] = {"betydelse_kan_saknas": (
            "Kortet har nu SEX betydelser, tagna direkt ur rastrukturen: SO-LEMMA "
            "belagga har FEM definitioner ('forse med tackande lager', 'ta upp plats "
            "i', 'genom stadgande forena med viss pafoljd', 'gora fast', 'ange fakta "
            "som stoder') plus EN underbetydelse med egen definitionstext ('pavisa "
            "forekomst av'). Det ar sex sanna betydelser och kortet har alla sex. "
            "Sammandragets sjunde post ar SAOL:s 'belasta', som inte ar en sjunde "
            "betydelse utan SAOL:s formulering av SO:s tredje ('genom stadgande "
            "forena med viss pafoljd') -- den star redan pa kortet, och 'belasta' "
            "ligger som synonym till just den betydelsen. Sex ar taket for vad ett "
            "kort rimligen kan bara, och har sammanfaller det med vad ordboken "
            "faktiskt har.")}

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("omskrivna huvudbetydelser: %d" % n)
