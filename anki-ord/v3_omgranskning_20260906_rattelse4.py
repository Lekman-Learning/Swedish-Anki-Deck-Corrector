# -*- coding: utf-8 -*-
"""Registervokabularen ar SLUTEN -- jag hittade pa sex taggar som inte finns.

config.REGISTER_DOMAN och REGISTER_FORMALITY ar listor, inte fritext. De tio
kort som applicera hoppade over hade: mat (-> matlagning), lantbruk (->
jordbruk), fiske (-> jakt), hastsport (-> sport), sprakvetenskap (->
lingvistik), journalistik (-> ingen doman alls, det saknas i listan) samt tva
stilnivaer som inte heller finns: 'alderdomlig' (-> ngt alderdomlig, SAOL:s
{ngt ald.}) och 'mindre brukligt' (-> ngt alderdomlig).
"""
import io, json

FIL = "sessions/session_2026-09-06_v3-omgranskning.json"

REG = {
 "lake":     "neutral, neutral, matlagning ; neutral, neutral, biologi",
 "endiv":    "neutral, neutral, matlagning",
 # SO markerar partikelbetydelsen 'mindre brukligt'; narmaste giltiga stilniva
 # ar 'ngt alderdomlig' (daterat men begripligt) -- ordet lever kvar i
 # bibelcitatet om grandet i sin broders oga.
 "grand":    "ngt ålderdomlig, neutral ; neutral, neutral, historia",
 # 'journalistik' finns inte i REGISTER_DOMAN. Betydelse 2 ar inte heller
 # fackssprak -- den ar vardaglig och allman, sa domanen utgar.
 "snaskig":  "vardaglig, negativ ; vardaglig, negativ",
 # SO: 'alderdomligt', SAOL: 'ald.' -- men ordet ar fortfarande begripligt,
 # alltsa 'ngt alderdomlig', inte 'arkaisk' (som betyder UR BRUK).
 "oför":     "ngt ålderdomlig, neutral",
 "agn":      "neutral, neutral, jordbruk ; neutral, neutral, jakt",
 "genever":  "neutral, neutral, matlagning",
 "brösta":   "vardaglig, lätt negativ ; fackspråklig, neutral, sport ; "
             "vardaglig, neutral, sport",
 "belägga":  "neutral, neutral ; neutral, neutral ; fackspråklig, neutral, juridik ; "
             "fackspråklig, neutral, sjöfart ; neutral, neutral ; "
             "fackspråklig, neutral, lingvistik",
 "agrar":    "neutral, neutral, jordbruk ; neutral, neutral, jordbruk ; "
             "neutral, neutral, politik ; neutral, neutral, jordbruk",
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    pr = e.get("proposed")
    if pr and e["ord"] in REG:
        pr["register"] = REG[e["ord"]]
        n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("rattade register: %d" % n)
