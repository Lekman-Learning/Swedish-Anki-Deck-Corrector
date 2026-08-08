# -*- coding: utf-8 -*-
"""Avgränsar exakt vilka kort som rördes 2026-08-08 utan riktig sökkoll.

De 177 falskt taggade korten går INTE att hitta på snabbkoll2-taggen: en
del av dem taggades direkt via addTags i ad-hoc-script, inte via
apply_card(), och fick därför aldrig snabbkoll2-taggen. Det här scriptet
mäter varje kandidatmängd istället för att gissa vilken som är rätt.
"""
import config
from ankiconnect import invoke

D = f'deck:"{config.DECK_NAME}"'
SOK = "flerbetydelse_sokverifierad"
FRAGOR = [
    ("granskad::2026-08-08 totalt", f"{D} tag:flerbetydelse_granskad::2026-08-08"),
    ("  därav äkta sökverifierade", f"{D} tag:flerbetydelse_granskad::2026-08-08 tag:{SOK}::2026-08-08"),
    ("  därav UTAN sökkoll (botchade)", f"{D} tag:flerbetydelse_granskad::2026-08-08 -tag:{SOK}::*"),
    ("snabbkoll2::2026-08-08", f"{D} tag:flerbetydelse_snabbkoll2::2026-08-08"),
    ("granskad::08-08 + äldre äkta sökkoll", f"{D} tag:flerbetydelse_granskad::2026-08-08 tag:{SOK}::* -tag:{SOK}::2026-08-08"),
    ("gröna is:new (arbetslistan)", f"{D} is:new -is:suspended flag:3"),
    ("v3_granskad (nya taggen)", f"{D} tag:{config.V3_TAG_PREFIX}::*"),
]
for namn, q in FRAGOR:
    print(f"{namn:<40}: {len(invoke('findNotes', query=q))}")

print("\nFörsta 20 botchade, i könordning:")
nids = invoke("findNotes",
              query=f"{D} tag:flerbetydelse_granskad::2026-08-08 -tag:{SOK}::*")
for n in invoke("notesInfo", notes=nids[:20]):
    print(f"  {n['noteId']}  {n['fields'][config.FIELD_ORD]['value']}")
