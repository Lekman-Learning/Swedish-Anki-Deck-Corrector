# -*- coding: utf-8 -*-
"""Lägger forgranska_tillat på verifierade falsklarm i grupp 1 (2026-09-05)."""
import io, json
FIL = "sessions/session_2026-09-05_v3-omgranskning-repetition.json"

TILLAT = {
"gå i clinch": {
    "frammande_uppslagsord": (
        "Flerordsuttryck -- svenska.se:s fritextsökning på 'gå i clinch' matchar "
        "delorden 'gå' (ett av svenskans mest polysema verb) och 'clinch' separat "
        "och drar in tiotals orelaterade lemman (bli medlem, acceptera, dö, avlida, "
        "gånggrift ...). Grundordet 'clinch' har en egen, ren SO/SAOL-artikel "
        "(kontrollerad separat via visa_uppslag/uppslag/gå i clinch.json) som ger "
        "hela innehållet på kortet. Samma dokumenterade mönster som 'kärringen mot "
        "strömmen'/'tjo och tjim' (se CLAUDE.md 2026-08-19)."),
    "betydelse_kan_saknas": (
        "Sammandragets 'def'-lista för detta uppslag är kontaminerad av 'gå' "
        "(['bli medlem', 'acceptera', '1grav 1'] -- inget av detta handlar om "
        "clinch). Kontrollerat mot RÅSTRUKTUREN (visa_uppslag.py): SO-lemmat "
        "'clinch' har EN huvudbetydelse ('ömsesidig fastlåsning av armar under "
        "boxningsmatch') plus en utvidgning UTAN egen definition ('äv. bildligt i "
        "uttryck för intellektuell (när)kamp, konfrontation eller dylikt') -- alltså "
        "EN sann betydelse, inte tre. Kortets enda huvudbetydelse täcker den. Samma "
        "regel som 'flirta'-fallet 2026-08-25: ett hårt flagg viftas bort mot "
        "råstrukturen, aldrig mot sammandraget."),
    "synonym_utan_stod": (
        "Sammandragets 'exempel'-fält för detta uppslag är också kontaminerat av "
        "'gå med'/'gå på' (SO: 'gå med i en förening'; SAOL: 'gå med på ngt') -- "
        "ingen av dessa rader handlar om clinch, så den automatiska stödkontrollen "
        "ser fel underlag. Den RIKTIGA källan (uppslag/gå i clinch.json, "
        "svenska_se_ratt.saol, lemma 'clinch') har exempelfältet "
        "{'text': 'gå i clinch med', 'parafras': 'gå i närkamp med'} -- SAOL:s egen "
        "parafras för hela idiomet. 'närkamp' är alltså direkt källbelagt, bara i "
        "ett fältformat (exempel.parafras på ett flerordsuttryck) som "
        "sammandraget/kontrollen inte fångar upp."),
    "synonym_utan_ordboksbelagg": (
        "Samma grund som synonym_utan_stod ovan: SAOL:s exempel/parafras för "
        "'gå i clinch med' -> 'gå i närkamp med' belägger 'närkamp' direkt, men "
        "sitter i ett fält (exempel.parafras på flerordsuttrycket 'clinch') den "
        "automatiska kontrollen inte läser. Verifierat manuellt mot rådata i "
        "uppslag/gå i clinch.json."),
},
"nexus": {
    "betydelse_kan_saknas": (
        "Dubbelräkning i sammandraget, samma buggklass som 'flirta' 2026-08-25: "
        "SO:s underbetydelse ('spec. språkvetenskap' / fulltext 'språklig "
        "förbindelse mellan två begrepp som förutsätter varandra') räknas EN gång "
        "i def-listan (fullt utskriven) och EN gång till i underbetydelser-listan "
        "(som korttaggen 'spec. språkvetenskap') -- alltså 3 i sammandraget för "
        "samma 2 verkliga betydelser. Kontrollerat mot RÅSTRUKTUREN "
        "(visa_uppslag.py): SO har en huvudbetydelse ('förbindelse') plus EN "
        "underbetydelse med egen definition ('språklig förbindelse mellan två "
        "begrepp som förutsätter varandra') -- två sanna betydelser, exakt vad "
        "kortet redan har."),
},
"prognos": {
    "betydelse_kan_saknas": (
        "Kontrollerat mot RÅSTRUKTUREN (visa_uppslag.py): SO har EN "
        "huvudbetydelse ('förutsägelse om kommande utveckling eller förlopp') "
        "plus en underbetydelse UTAN egen definition (typ: 'ibland äv. om "
        "individuella framtidsutsikter, särsk. i juridiska sammanhang') -- en "
        "utvidgning av samma grundbegrepp till en persons framtidsutsikter, inte "
        "en egen betydelse (jfr style_guide.md: 'Underbetydelser UTAN egen "
        "definition är utvidgningar, INTE egna betydelser'). Sammandragets "
        "'underbetydelser'-lista räknar ändå in denna korta typtext som en andra "
        "betydelse, vilket ger den falska siffran 2. SAOL har bara EN definition, "
        "ingen semikolon. En sann betydelse, matchar kortet."),
},
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    t = TILLAT.get(e["ord"])
    if not t:
        continue
    e["forgranska_tillat"] = {**(e.get("forgranska_tillat") or {}), **t}
    n += 1

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("uppdaterade", n, "poster med forgranska_tillat")
