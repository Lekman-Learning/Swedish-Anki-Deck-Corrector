# -*- coding: utf-8 -*-
"""Bevisar att --ordning mognad ändrar URVALET, inte bara sorteringen.

Adams regel 2026-08-30: en full v3-omgång ska börja i de kort han redan
kan (mature eller närmast mature), inte i is:new.

Torrkörning -- hamta_pool() skriver aldrig till Anki (taggningen sker i
main()). Jämför due-urvalet med mognadsurvalet på samma spår och antal.
"""
import kortbyggare

ANTAL = 25

for ordning in ("due", "mognad"):
    cards = kortbyggare.hamta_pool(ANTAL, "omgranskning", ordning=ordning)
    ivl = [c["interval"] for c in cards]
    mature = sum(1 for i in ivl if i >= 21)
    nara = sum(1 for i in ivl if 14 <= i < 21)
    print("ordning=%-8s %3d kort   ivl %3d..%-3d   mature %2d   nara %2d"
          % (ordning, len(cards), max(ivl or [0]), min(ivl or [0]), mature, nara))
    if ordning == "mognad":
        # Fallande ordning ar hela poangen: gar den sonder tyst blir batchen
        # ett godtyckligt urval som bara SER prioriterat ut.
        assert ivl == sorted(ivl, reverse=True), "urvalet ar inte fallande: %r" % ivl
        assert min(ivl) >= 1, "nytt kort (ivl 0) slank igenom prop:ivl>=1"
        print("             fallande: OK   inga ivl=0: OK")
