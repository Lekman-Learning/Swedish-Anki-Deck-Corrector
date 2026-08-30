# -*- coding: utf-8 -*-
"""Skriver ut varje fynd fran aao_koll.py MED omgivande text.

Utan kontext gar traffarna inte att doma: `krogar`, `salar` och `isar` ar
riktiga svenska ord som bara saknas i uppslagskorpusen, medan `skamtare`
och `anvandning` ar akta fel. Bara meningen avgor vilket.
"""
import io
import json
import re

import config
from ankiconnect import invoke

fynd = json.load(io.open("aao_fynd.json", encoding="utf-8"))
nids = sorted({f["noteId"] for f in fynd})
noter = {}
for i in range(0, len(nids), 500):
    for n in invoke("notesInfo", notes=nids[i:i + 500]):
        noter[n["noteId"]] = n

for f in fynd:
    n = noter[f["noteId"]]
    raw = n["fields"][f["falt"]]["value"] or ""
    txt = re.sub("<[^>]+>", " ", raw).replace("&nbsp;", " ")
    txt = re.sub(r"\s+", " ", txt)
    i = txt.lower().find(f["fel"].lower())
    utdrag = txt[max(0, i - 55):i + len(f["fel"]) + 55]
    print("%-18s %-9s %-14s -> %-22s | ...%s..."
          % (f["ord"][:18], f["falt"][:9], f["fel"],
             ", ".join(f["forslag"])[:22], utdrag))
