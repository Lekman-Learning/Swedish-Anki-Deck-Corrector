# -*- coding: utf-8 -*-
"""Adam-tal-rattelser efter svarighetskoll pa v3-batch100.

Regeln: ett svart ord i forklaringen byts mot en KORT FRAS pa enklare
svenska -- aldrig mot en synonym, eftersom en synonym bara flyttar
svarigheten. Falska traffar (vardagsord som rakar finnas i decket)
skrivs anda om nar omskrivningen ar gratis.
"""
import io
import json

FIL = "sessions/session_2026-08-28_v3-batch100.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}

NY = {
    # "mytologi" -> vardagssvenska
    "cyklop": "I de grekiska sagorna: en jätte med ett enda öga mitt i "
              "pannan ; dykarmask som täcker både ögon och näsa",
    # "aktning" -> "hedra"
    "defilera": "Marschera förbi någon förnäm i ordnade led för att hedra "
                "den personen ; bildligt: ta sig i mål med så stor ledning "
                "att det kan ske i lugn och ro",
    # "förmer" -> "bättre"
    "fjär": "Som håller andra på avstånd med en min av att vara bättre än de",
    # "kungöra" -> "meddela"
    "promulgera": "Officiellt meddela att en lag som redan är beslutad nu "
                  "ska börja gälla",
    # "trål" -> "stort släpnät"
    "varp": "I vävning: trådarna som spänns upp på längden i väven och som "
            "de andra trådarna vävs in tvärs igenom ; hög av värdelöst berg "
            "som kastats undan vid gruvbrytning ; draglina till ett stort "
            "släpnät eller till ett mindre ankare",
    # "församling" -> utskrivet (ordet star kvar som synonym, dar det hor hemma)
    "socken": "Det äldsta lokala området på landsbygden: en kyrka med de "
              "människor som hörde till den, och förr också indelningen för "
              "allt lokalt styre",
    # "nära" -> "tätt intill"
    "allitteration": "Att flera betonade ord tätt intill varandra börjar med "
                     "samma ljud, som i \"hals över huvud\"",
    # "tillkännage" -> "berätta om"
    "eklatera": "Offentligt berätta om något som varit privat, framför allt "
                "en förlovning",
    # "satt" -> "använd"
    "fingerad": "Påhittad och använd i stället för det verkliga, för att "
                "dölja vem eller vad det egentligen gäller",
    # "nära" -> "tätt"
    "kalkera": "Kopiera en bild genom att lägga genomskinligt papper över "
               "och rita av linjerna ; bildligt: härma ett verk så tätt att "
               "det blir en avbild",
    # "ämbete" -> "tjänst"
    "patriarkat": "Samhällsskick där fadern eller männen har makten i "
                  "familjen och samhället ; en kyrklig patriarks tjänst, "
                  "eller det område han styr över",
    # "podium" -> "upphöjning"
    "pult": "Liten upphöjning med notställ, som en dirigent står på ; också "
            "om notstället ensamt",
    # "förakt" + "narr" -> utskrivet
    "spe": "Hån: att skratta ut någon för att visa att man ser ner på "
           "personen ; i uttrycket \"in spe\": blivande, ännu inte men snart",
    # "anatomi" -> bort (forsta halvan sager redan samma sak)
    "zootomi": "Läran om hur djurens kroppar är byggda",
    # "stäv" -> "skrov"
    "åmning": "Sifferskalan målad på fartygets skrov, som visar hur djupt "
              "det ligger i vattnet",
}

for ord, bet in NY.items():
    e = BY[ord]
    gammal = e["proposed"]["huvudbetydelse"]
    assert len(bet.split(" ; ")) == len(gammal.split(" ; ")), ord
    e["proposed"]["huvudbetydelse"] = bet

# anlopa: "hamn" ar flaggat men behalls -- se not nedan.
BY["anlöpa"]["sokkoll"]["slutsats"] += (
    " ADAM-TAL: svarighetskollen flaggar 'hamn' som deck-ord. Det ar "
    "behallet: hamn ar A1-svenska och gar inte att skriva om utan att "
    "forklaringen blir langre och samre. Flaggan ar en falsk traff.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("rattade %d kort" % len(NY))
