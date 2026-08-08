# -*- coding: utf-8 -*-
"""Listar röda suspenderade kort med deras nuvarande innehåll."""
import re

import baksida
import config
from ankiconnect import invoke

ids = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" is:suspended flag:1')
print(f"Röda suspenderade: {len(ids)}\n")
info = invoke("notesInfo", notes=ids[:20])
rensa = lambda s: re.sub(r"<[^>]+>", " ", s or "").replace("&nbsp;", " ").strip()
for n in info:
    ord_ = n["fields"][config.FIELD_ORD]["value"]
    raw = n["fields"][config.FIELD_BAKSIDA]["value"]
    p = baksida.parse(raw)
    if not p["huvudbetydelse"]:
        p = baksida.parse_legacy(raw)
        hb = " | ".join(rensa(d) for d in (p.get("definitioner") or []))
        fmt = "legacy"
    else:
        hb = p["huvudbetydelse"]
        fmt = "v2"
    print(f"{n['noteId']}  {ord_!r}  [{fmt}]  bild={bool(p.get('bild_html'))}")
    print(f"   HB : {hb[:110]}")
    print(f"   SYN: {p.get('synonymer')}")
    print(f"   EX : {rensa(p.get('exempelmening'))[:90]}")
    print(f"   TAG: {n.get('tags')}\n")
