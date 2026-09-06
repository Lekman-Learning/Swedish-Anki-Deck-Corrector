# -*- coding: utf-8 -*-
"""Svarighetskollen: 14 av 40 kort forklarade ett svart ord med ett annat deck-ord.

Rattat med korta fraser, aldrig genom att byta det svara ordet mot en enklare
synonym (kortbyggare._ADAMTAL). Nagra av traffarna ar overraskande vardagliga
ord ('nara', 'kall', 'eftersom') -- de star i decket som egna uppslagsord och
raknas darfor, aven nar de knappast ar svara. Regeln ar anda noll traffar, sa
de ar omskrivna.
"""
import io, json

FIL = "sessions/session_2026-09-06_v3-omgranskning2.json"

HB = {
 # 'tatting' och 'forcerad' ut. Precisionen flyttad till en jamforelse i stallet.
 "gärdsmyg": "Mycket liten brunspräcklig fågel med kort, uppåtstående stjärt och en sång som är "
             "förvånansvärt stark för storleken",
 # 'klander' och 'konkret' ut. SO:s 'skadlig handling' star kvar; det klandervarda
 # bars av synonymen 'klandervard garning'.
 "dåd": "Handling som skadar någon eller något",
 # 'skamd' ut.
 "boken": "Mer än övermogen och på väg att bli dålig, om frukt",
 # 'snar' ut ur definitionen -- ordet ar betydelse 2:s synonym och hor darfor hemma
 # pa synonymraden, inte i bada.
 "snärj": "Stress och alldeles för mycket att göra ; tätt hopvuxna buskar och grenar",
 # 'brydsam' ut ur definitionen; ordet star kvar som synonym ('brydsam situation',
 # SO:s egen underbetydelsetext).
 "förlägenhet": "Obehaglig känsla av att skämmas inför andra ; en svår situation, till exempel "
                "brist på pengar",
 # 'sympati' ut.
 "intagande": "Som utan ansträngning får andra att tycka om en",
 # 'upptag' ut. (Kortet ar pausat, men rattas anda sa att det ar redo om Adam
 # beslutar att byta uppslagsordet till 'spelevink'.)
 "spelevinker": "Lekfull person som gärna hittar på bus och skoj",
 # 'ranna' ut.
 "spont": "Utstående list på en bräda som passar in i ett spår på nästa bräda vid hopfogning",
 # 'nara', 'innerlig' och 'drev' ut. 'fortrolig' star kvar som synonym (SO:s hela
 # definition), sa betydelsen gar inte forlorad.
 "såt": "Varm och tillitsfull, om vänskap ; mindre område som jagas av i en omgång",
 # 'geranium' ut ur definitionen -- slaktnamnet star i slutsatsen i stallet.
 "näva": "Växt med oftast handflikiga blad och purpurröda blommor",
 # 'eftersom' ut.
 "holism": "Riktning inom vetenskapen som menar att man i första hand ska studera helheten, "
           "som är mer än summan av delarna",
 # 'tafatt' ut.
 "luns": "Klumpig och fumlig karl",
 # 'kall' ut. SAOL:s 'gora hard el. okanslig' ger ersattningen.
 "förhärda": "Göra någon hård och okänslig ; förhärda sig: stänga av sina egna känslor",
 # 'gycklare' ut.
 "histrion": "Skådespelare av enklare slag, ofta en kringresande komiker",
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    pr = e.get("proposed")
    if pr and e["ord"] in HB:
        pr["huvudbetydelse"] = HB[e["ord"]]
        n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("omskrivna huvudbetydelser: %d" % n)
