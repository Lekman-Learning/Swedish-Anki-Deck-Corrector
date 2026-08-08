# -*- coding: utf-8 -*-
import re
from ankiconnect import invoke
import config
D = f'deck:"{config.DECK_NAME}"'
def strip(h):
    h = re.sub(r"<br\s*/?>", " ~ ", h)
    h = re.sub(r"<[^>]+>", "", h).replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", h).strip()
ids = invoke("findCards", query=f"{D} is:new -is:suspended flag:3")
ci = invoke("cardsInfo", cards=ids)
ci.sort(key=lambda c: c["due"])
nids, seen = [], set()
for c in ci:
    if c["note"] not in seen:
        seen.add(c["note"]); nids.append(c["note"])
    if len(nids) >= 100: break
info = invoke("notesInfo", notes=nids)
old = {}
for x in info:
    f = strip(x["fields"]["Framsida"]["value"])
    o = invoke("findNotes", query=f'deck:"Humanities::Languages::Svenska OLD" "Framsida:{f}"')
    old[f] = strip(invoke("notesInfo", notes=[o[0]])[0]["fields"]["Baksida"]["value"])[:70] if o else "-"
for i, x in enumerate(info, 1):
    f = strip(x["fields"]["Framsida"]["value"])
    print(f'{i}. {f} :: {strip(x["fields"]["Baksida"]["value"])}')
    print(f'   FACIT: {old[f]}')
