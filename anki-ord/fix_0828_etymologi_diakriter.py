# -*- coding: utf-8 -*-
"""Aterstaller a/a/o i etymologifaltet pa dagens tre batchar.

FELET. Jag skriver sokkoll-slutsatserna i ren ASCII med flit -- de ar interna
och laser aldrig av Adam. Men samma vana lackte in i ETYMOLOGI-faltet, som
INTE ar internt: det renderas pa kortets baksida. Resultatet ar felstavad
svenska pa ett svenskt ordforradsdeck -- 'lagtyska' for 'lagtyska', 'beslaktat'
for 'beslaktat', 'nara' for 'nara'.

Blindgranskaren hittade det pa ETT kort (formaten: 'ordagrant "mata fel"' dar
det ska sta 'mata fel' -- mata och mata ar olika ord, sa etymologin blev
obegriplig i stallet for klargorande). Kontrollen visade 47 kort med samma
fel, spridda over alla tre batcharna. 138 av dem ar redan slappta till Adams
ko.

VAD SOM INTE RORS. Fornsvenska, lagtyska, latinska och franska former ar
korrekta som de star -- 'liuster', 'thruga', 'vormeten', 'calx' ska INTE fa
diakriter. Bara de SVENSKA orden i forklaringstexten rattas. Darfor ordlista
med ordgranser, inte en generell teckenersattning.
"""
import io
import json
import re

# Bara svenska forklaringsord. Formerna pa kallspraken lamnas ororda.
ORD = {
    "lagtyska": "lågtyska",
    "hogtyska": "högtyska",
    "islandska": "isländska",
    "gronlandska": "grönländska",
    "beslaktat": "besläktat",
    "slakt": "släkt",
    "nara": "nära",
    "aldre": "äldre",
    "aven": "även",
    "alltsa": "alltså",
    "fran": "från",
    "darfor": "därför",
    "daremot": "däremot",
    "sjalv": "själv",
    "sjoman": "sjöman",
    "manniska": "människa",
    "nagot": "något",
    "fullgora": "fullgöra",
    "utfora": "utföra",
    "gora": "göra",
    "foda": "föda",
    "forinta": "förinta",
    "dolja": "dölja",
    "gomma": "gömma",
    "spoke": "spöke",
    "overskatta": "överskatta",
    "anstranga": "anstränga",
    "trastycke": "trästycke",
    "tradstam": "trädstam",
    "tradstammar": "trädstammar",
    "inalvor": "inälvor",
    "inalvsbetydelsen": "inälvsbetydelsen",
    "kada": "kåda",
    "kortelsvulst": "körtelsvulst",
    "glansande": "glänsande",
    "smasak": "småsak",
    "utplanad": "utplånad",
    "tillganglig": "tillgänglig",
    "talt": "tält",
    "sparlakanssang": "sparlakanssäng",
    "fornamst": "förnämst",
    "fornamste": "förnämste",
    "rakning": "räkning",
    "berakning": "beräkning",
    "stota": "stöta",
    "ljudharmande": "ljudhärmande",
    "gnagga": "gnägga",
    "efterrattlig": "efterrättlig",
    "rattar": "rättar",
    "lopa": "löpa",
    "karls": "kärls",
    "hart": "hårt",
    "val": "väl",
    "hal": "häl",
    "natt": "nätt",
    "mata": "mäta",
    "tra": "trä",
    "at": "åt",
    "ar": "är",
    "pa": "på",
}
MONSTER = re.compile(r"\b(%s)\b" % "|".join(sorted(ORD, key=len, reverse=True)))

# Tva ord som bara ar fel i EN viss etymologi -- ordlistan far inte trafffa
# dem generellt ('gas' och 'am' ar riktiga svenska ord i andra sammanhang).
SARFALL = {
    "krås": [("'inalvor i gas'", "'inälvor i gås'")],
    "åmning": [("till am.", "till åm.")],
}

FILER = [
    "sessions/session_2026-08-28_v3-batch100.json",
    "sessions/session_2026-08-28_v3-batch5.json",
    "sessions/session_2026-08-28_v3-batch6.json",
]

andrade = []
for fil in FILER:
    KORT = json.load(io.open(fil, encoding="utf-8"))
    for k in KORT:
        p = k.get("proposed") or {}
        e = p.get("etymologi")
        if not e:
            continue
        ny = MONSTER.sub(lambda m: ORD[m.group(1)], e)
        for gammalt, ratt in SARFALL.get(k["ord"], []):
            ny = ny.replace(gammalt, ratt)
        if ny != e:
            p["etymologi"] = ny
            andrade.append((k["ord"], e, ny))
    json.dump(KORT, io.open(fil, "w", encoding="utf-8"), ensure_ascii=False,
              indent=1)

for ord_, gammalt, ny in andrade:
    print("%-16s %s" % (ord_, ny))
print("\n%d etymologifalt rattade" % len(andrade))
