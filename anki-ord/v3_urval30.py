# -*- coding: utf-8 -*-
import random, re
from ankiconnect import invoke
import config
D = f'deck:"{config.DECK_NAME}"'
def strip(h):
    h = re.sub(r"<br\s*/?>", "\n", h); h = re.sub(r"<[^>]+>", "", h).replace("&nbsp;", " ")
    return [r.strip() for r in h.split("\n") if r.strip()]
nids = invoke("findNotes", query=f"{D} tag:flerbetydelse_snabbkoll2::2026-08-08 -tag:flerbetydelse_sokverifierad::2026-08-08")
random.seed(30)
urval = random.sample(nids, min(30, len(nids)))
info = invoke("notesInfo", notes=urval)
print(f"urval: {len(info)} av {len(nids)} granskade i natt\n")
for i, x in enumerate(sorted(info, key=lambda n: n["noteId"]), 1):
    rader = strip(x["fields"]["Baksida"]["value"])
    ord_ = strip(x["fields"]["Framsida"]["value"])[0]
    huvud = rader[0] if rader else ""
    ant = huvud.count("/") + 1
    print(f'{i}. {ord_}  [{ant} bet] :: {huvud}')
