# -*- coding: utf-8 -*-
"""Av de 430 etymologierna utan a/a/o -- hur manga star pa kort JAG skrivit?

De flesta av de 430 ar rent latinska/grekiska/franska rader hamtade ur SO
och alltsa korrekta. Risken sitter i de rader jag sjalv formulerat, alltsa
kort med en v3_granskad-tagg.
"""
import re

import baksida
import config
from ankiconnect import invoke

nids = invoke("findNotes", query='deck:"%s"' % config.DECK_NAME)
traff = []
for i in range(0, len(nids), 2000):
    for n in invoke("notesInfo", notes=nids[i:i + 2000]):
        if not any(t.startswith("v3_granskad") for t in n["tags"]):
            continue
        raw = (n["fields"].get(config.FIELD_BAKSIDA) or {}).get("value", "")
        e = baksida.parse(raw).get("etymologi") or ""
        if e and not any(c in e for c in "åäöÅÄÖ"):
            ord_ = re.sub("<[^>]+>", "",
                          list(n["fields"].values())[0]["value"]).strip()
            traff.append((n["noteId"], ord_, e))

print("v3-kort med etymologi utan a/a/o: %d\n" % len(traff))
for nid, o, e in traff:
    print("%-8s %-20s %s" % (nid, o, e[:130]))
