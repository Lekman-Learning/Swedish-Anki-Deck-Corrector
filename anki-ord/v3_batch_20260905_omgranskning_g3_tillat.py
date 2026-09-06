# -*- coding: utf-8 -*-
"""Lägger forgranska_tillat på verifierade falsklarm i grupp 3 (2026-09-05)."""
import io, json
FIL = "sessions/session_2026-09-05_v3-omgranskning-repetition.json"

TILLAT = {
"narr": {
    "betydelse_kan_saknas": (
        "Kontrollerat mot RÅDATA: den 'extra' tredje posten i sammandragets def-lista "
        "('få någon/något att framstå som löjlig') kommer från SO:s IDIOM-fält 'göra "
        "narr av någon/något', inte en egen betydelse av substantivet 'narr' -- "
        "sammandraget flätar in idiombetydelser i samma lista som huvudbetydelser. Två "
        "sanna betydelser (löjlig person / hovnarr), matchar kortet exakt."),
},
"profetia": {
    "betydelse_kan_saknas": (
        "Kontrollerat mot RÅDATA: den 'extra' andra posten i sammandragets def-lista "
        "('en förutsägelse som slår in (delvis) just därför att någon uttalar den') "
        "kommer från SO:s IDIOM-fält 'en självuppfyllande profetia', inte en egen "
        "betydelse av ordet 'profetia' -- samma kontamineringsmönster som 'narr' i denna "
        "omgång. Underbetydelsen ('numera ofta om förutsägelse i allmänhet') saknar egen "
        "definition -- en utvidgningsnot, inte en ny betydelse (och matchar redan "
        "kortets 'ofta med religiös grund'-formulering, som redan behandlar religiös "
        "grund som vanlig men inte obligatorisk). En sann betydelse, matchar kortet."),
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
