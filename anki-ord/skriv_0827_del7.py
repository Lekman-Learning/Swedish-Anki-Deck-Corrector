# -*- coding: utf-8 -*-
"""Batch 2026-08-27, kort 69-70. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-27_v3-batch.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
KALLA = ("SO och SAOL via https://svenska.se/api/msearch?ord=%s "
         "(hamtat 2026-08-27, HTTP 200)")
B = '<font color="#3498db">%s</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, tillat=None, conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": None, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": KALLA % urllib.parse.quote(o),
                    "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("äska",
     "Formellt begära något, oftast pengar från en myndighet ; "
     "rund ask av tunt trä, som man förr förvarade småsaker i",
     "formell, neutral ; ngt ålderdomlig, neutral, historia",
     ["begära", "anhålla om"],
     "Institutionen " + B % "äskade" + " 1,3 miljoner i anslag för ny utrustning.",
     "→ Fornsvenska äskia 'kräva'. Samma ord som engelskans ask.",
     "SAOL: 'begara, anhalla om | rund el. oval ask av span' -- bada "
     "synonymerna leder var sitt led i den forsta betydelsen. 🔴 TVA HELT "
     "SKILDA ORD delar form: verbet (av lagtyska eschen 'fordra') och "
     "substantivet (av ask(tra)). Etymologierna ar oberoende. Verbet lever i "
     "myndighetssprak ('aska medel'), substantivet ar historiskt.",
     tillat={"betydelse_kan_saknas":
             "SO:s 3 poster ar 2 betydelser (verbet och asken) plus 'spec. "
             "(mer konkret)' -- en precisering av verbet, inte en tredje "
             "betydelse."})

satt("översiggiven",
     "Utom sig av förtvivlan",
     "ngt ålderdomlig, negativ",
     ["förtvivlad", "utom sig"],
     "Han kastade sig " + B % "översiggiven" + " på soffan och grät.",
     "→ Fornsvenska ivirgiva sik 'misströsta' — att ha gett upp sig själv.",
     "SAOL: 'fortvivlad, utom sig' -- bada synonymerna leder var sitt led. "
     "SO: 'ytterligt fortvivlad', markt 'nagot alderdomligt'. Ordet ar "
     "starkare an 'ledsen' -- 'ytterligt' i SO:s definition ar poangen. "
     "Etymologin forklarar formen direkt (over sig given = uppgiven).")

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Totalt godkanda kort nu: %d" % sum(1 for k in KORT if k.get("approved")))
