# -*- coding: utf-8 -*-
"""Bevisar att prio-taggen ändrar URVALET, inte bara sorteringen.

Anropar kortbyggare.hamta_pool() direkt -- den skriver aldrig till Anki
(taggningen sker i main()), så det här är en ren torrkörning.
"""
import config
import kortbyggare
from ankiconnect import invoke

for spar, antal in (("omgranskning", config.OMGRANSKNING_STORLEK),
                    ("nya", config.DAGSBATCH_STORLEK)):
    cards = kortbyggare.hamta_pool(antal, spar)
    nids = [c["note"] for c in cards]
    prio = set(invoke("findNotes",
                      query=f'deck:"{config.DECK_NAME}" tag:{config.PRIO_TAG_HOG}'))
    traffar = [n for n in nids if n in prio]
    print(f"{spar:<13} hämtade {len(cards):>3} kort, varav {len(traffar):>2} prio")
    if traffar:
        forsta = [n in prio for n in nids[:len(traffar)]]
        print(f"              prio ligger först: {all(forsta)}")
