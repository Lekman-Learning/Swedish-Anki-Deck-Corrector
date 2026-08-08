# -*- coding: utf-8 -*-
import random, re, json
from ankiconnect import invoke
import config
D = f'deck:"{config.DECK_NAME}"'
def strip(h):
    h = re.sub(r"<br\s*/?>", " ~ ", h); h = re.sub(r"<[^>]+>", "", h).replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", h).strip()
nids = invoke("findNotes", query=f"{D} is:new -is:suspended flag:3 -tag:flerbetydelse_snabbkoll2::2026-08-08")
random.seed(2608)
urval = random.sample(nids, 30)
info = invoke("notesInfo", notes=urval)
ut = []
for i, x in enumerate(info, 1):
    o = strip(x["fields"]["Framsida"]["value"])
    b = strip(x["fields"]["Baksida"]["value"])
    f = invoke("findNotes", query=f'deck:"Humanities::Languages::Svenska OLD" "Framsida:{o}"')
    fac = strip(invoke("notesInfo", notes=[f[0]])[0]["fields"]["Baksida"]["value"])[:60] if f else "INGET FACIT"
    ut.append({"n": i, "noteId": x["noteId"], "ord": o})
    print(f"{i}. {o} :: {b}")
    print(f"   FACIT: {fac}")
json.dump(ut, open("experiment30.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
