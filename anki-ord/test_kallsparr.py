# -*- coding: utf-8 -*-
"""Verifierar källspärren: sökkoll utan kalla=... ska vägras."""
import apply_flerbetydelse as af
from ankiconnect import invoke
import config

nid = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" "Framsida:diffus"')[0]

print("1. sokkoll UTAN kalla -- ska kasta AssertionError")
try:
    af._tag_and_flag(nid, "sokkoll", True, "2026-08-08", kalla=None, ord_="diffus")
    print("   MISSLYCKADES: spadde igenom utan kalla!")
except AssertionError as e:
    print(f"   OK, vagrades: {str(e)[:90]}...")

print("2. snabbkoll2 utan kalla -- ska funka (ingen sokkoll pastas)")
try:
    af._tag_and_flag(nid, "snabbkoll2", False, "2026-08-08",
                     has_old_match=True, ord_="diffus")
    print("   OK, gick igenom")
except Exception as e:
    print(f"   OVANTAT FEL: {type(e).__name__}: {e}")
