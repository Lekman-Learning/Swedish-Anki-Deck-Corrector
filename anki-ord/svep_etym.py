# -*- coding: utf-8 -*-
"""Alla etymologirader i decket som saknar a/a/o helt.

Bredare an aao_koll.py, som bara ser ord vars diakritiska form RAKAR finnas
i uppslagskorpusen. En etymologi utan en enda diakrit ar inte i sig ett fel
-- rent latinska rader ar normala -- men listan ar kort nog att lasa.
"""
import re

import baksida
import config
from ankiconnect import invoke

nids = invoke("findNotes", query='deck:"%s"' % config.DECK_NAME)
n_etym = 0
tomma = []
for i in range(0, len(nids), 2000):
    for n in invoke("notesInfo", notes=nids[i:i + 2000]):
        raw = (n["fields"].get(config.FIELD_BAKSIDA) or {}).get("value", "")
        etym = baksida.parse(raw).get("etymologi") or ""
        if not etym:
            continue
        n_etym += 1
        if not any(c in etym for c in "åäöÅÄÖ"):
            ord_ = re.sub("<[^>]+>", "",
                          list(n["fields"].values())[0]["value"]).strip()
            tomma.append((n["noteId"], ord_, etym))

print("kort med etymologi: %d" % n_etym)
print("utan en enda a/a/o: %d\n" % len(tomma))
for nid, ord_, e in tomma:
    print("%-8s %-20s %s" % (nid, ord_, e[:150]))
