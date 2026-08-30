# -*- coding: utf-8 -*-
"""Skriver ut hela etymologiraden for varje kort dar aao_koll.py flaggat ett
ord i just den raden.

Skalet: detektorn ser bara de ord som RAKAR finnas i uppslagskorpusen med
diakriter. `dyslexi` flaggades pa 'daligt' men bar ocksa 'svart' (svart),
och `eufemism` bar bade 'for' och 'sprak'. Att ratta ord for ord hade
lamnat kvar halva felet -- hela raden maste skrivas om.
"""
import io
import json
import re

import baksida
import config
from ankiconnect import invoke

fynd = json.load(io.open("aao_fynd.json", encoding="utf-8"))
nids = sorted({f["noteId"] for f in fynd})
for i in range(0, len(nids), 500):
    for n in invoke("notesInfo", notes=nids[i:i + 500]):
        raw = (n["fields"].get(config.FIELD_BAKSIDA) or {}).get("value", "")
        etym = baksida.parse(raw).get("etymologi") or ""
        if not etym:
            continue
        if any(c in etym for c in "åäö"):
            markering = " "
        else:
            markering = "!"
        ord_ = re.sub("<[^>]+>", "",
                      list(n["fields"].values())[0]["value"]).strip()
        print("%s %-8s %-20s %s" % (markering, n["noteId"], ord_, etym))
