# -*- coding: utf-8 -*-
"""Lägger forgranska_tillat på verifierade falsklarm i grupp 2 (2026-09-05)."""
import io, json
FIL = "sessions/session_2026-09-05_v3-omgranskning-repetition.json"

TILLAT = {
"rekrytera": {
    "betydelse_kan_saknas": (
        "Kontrollerat mot RÅSTRUKTUREN (visa_uppslag.py): SO:s enda underbetydelse "
        "('ursprungligen i militära sammanhang') saknar egen definition -- en not om "
        "ordets HISTORISKA ursprung (att det en gång användes mest militärt, nu "
        "allmänt), inte en andra betydelse. Sammandraget räknar in denna "
        "ursprungskommentar som betydelse, vilket ger den falska siffran 2. En sann "
        "betydelse, matchar kortet."),
},
"a och o": {
    "frammande_uppslagsord": (
        "Flerordsuttryck utan egen SO/SAOL-artikel -- fritextsökningen matchar bara "
        "enskilda bokstavsartiklar (a, o, A-lag, A-dur, o-ring ...), 51 helt "
        "orelaterade lemman. Grundordens artiklar ger ingenting om uttrycket."),
    "betydelse_kan_saknas": (
        "Sammandragets def/underbetydelser för detta uppslag kommer helt från "
        "kontamination (bl.a. 'tilde' och 'von oben', se frammande_uppslagsord) -- "
        "ingen av de 3 räknade posterna handlar om 'a och o'. Den RIKTIGA källan är "
        "Wiktionary ('det viktigaste; det essentiella') plus synonymer.se:s "
        "redaktionella lista ('början och slutet, det viktigaste, det väsentliga, "
        "alfa, och, omega') -- en sann betydelse, matchar kortet."),
    "synonym_utan_ordboksbelagg": (
        "'_ordboksbelagg' scannar bara SO/SAOL:s sammandrag, som för detta uppslag är "
        "kontaminerat brus (se ovan) och alltså strukturellt inte KAN belägga något "
        "här. Den riktiga källan är Wiktionary: 'det viktigaste; det essentiella' -- "
        "'det viktigaste' är ordagrant Wiktionarys egen definitionstext. Bekräftas "
        "dessutom av synonymer.se:s REDAKTIONELLA lista (inte Användarnas bidrag): "
        "'... det viktigaste, det väsentliga ...'. Samma typ av strukturellt "
        "blindmönster som 'gå i clinch'/'närkamp' i grupp 1 -- källan finns, bara "
        "utanför de fält kontrollen läser."),
},
"ackumulera": {
    "betydelse_kan_saknas": (
        "Kontrollerat mot RÅSTRUKTUREN: SO:s underbetydelse är märkt 'i perfekt "
        "particip ofta' och ger bara ordet 'sammanlagd' -- det är particip-/"
        "adjektivformen av SAMMA grundbetydelse ('ackumulerad summa' = 'sammanlagd "
        "summa'), inte en ny betydelse av verbet. Sammandraget räknar in både "
        "particip-ordet och dess 'i perfekt particip'-tagg som separata poster, "
        "vilket ger den falska siffran 3. En sann betydelse, matchar kortet."),
},
"crescendo": {
    "betydelse_kan_saknas": (
        "Kontrollerat mot RÅSTRUKTUREN: substantivbetydelsens enda underbetydelse "
        "är märkt 'äv. bildligt' UTAN egen definition (bara ett syntex: 'applåderna "
        "och skratten steg till ett crescendo') -- en bildlig UTVIDGNING av samma "
        "begrepp (en stigande höjdpunkt) till icke-musikaliska sammanhang, inte en "
        "tredje betydelse med eget innehåll. Två sanna betydelser (adverb + "
        "substantiv), matchar kortet."),
},
"deja vu": {
    "frammande_uppslagsord": (
        "Den enda 'främmande' träffen är 'déjà vu' -- samma ord som uppslagsordet, "
        "bara med franska diakriter. Stam-jämförelsen i _samma_uppslag känner inte "
        "igen accenttecken, så identiskt ord räknas som ett annat uppslagsord."),
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
