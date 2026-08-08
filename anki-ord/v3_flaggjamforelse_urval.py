# -*- coding: utf-8 -*-
"""Urval för flaggjämförelsen: håller grön och blå så lika som möjligt
i allt UTOM det som ska mätas.

Frågan: bär flaggan information? Blå betyder "eskalerad till och bekräftad
via riktig sökkoll", grön betyder "klarade v3-snabbkollen mot OLD-facit
utan eskalering". Om en ny, oberoende sökkoll hittar lika många fel i
båda grupperna säger flaggan ingenting.

Båda grupperna dras ur samma aktiva nya-kö, i due-ordning, så skillnaden
mellan dem är verifieringsdjupet -- inte hur svåra orden är eller när
Adam möter dem.
"""
import re

import baksida
import config
from ankiconnect import invoke
from snabbkoll2 import build_old_lookup

D = f'deck:"{config.DECK_NAME}"'
rensa = lambda s: re.sub(r"<[^>]+>", " ", s or "").replace("&nbsp;", " ").strip()


def las(query, n):
    cids = invoke("findCards", query=query)
    if not cids:
        return []
    info = invoke("cardsInfo", cards=cids)
    info.sort(key=lambda c: c["due"])
    return invoke("notesInfo", notes=[c["note"] for c in info[:n]])


def visa(rubrik, notes, old):
    print(f"\n{'=' * 70}\n{rubrik}\n{'=' * 70}")
    for n in notes:
        ord_ = n["fields"][config.FIELD_ORD]["value"]
        p = baksida.parse(n["fields"][config.FIELD_BAKSIDA]["value"])
        facit = rensa(old.get(ord_.strip().lower()))
        print(f"\n{n['noteId']}  {ord_}")
        print(f"  HB   : {p['huvudbetydelse']}")
        print(f"  REG  : {p['register']}")
        print(f"  SYN  : {p['synonymer']}  grupper={p['synonym_groups']}")
        print(f"  EX   : {rensa(p['exempelmening'])}")
        print(f"  ETY  : {p['etymologi']}")
        print(f"  BILD : {bool(p['bild_html'])}")
        print(f"  OLD  : {facit[:150] if facit else '(ingen matchning)'}")


def main():
    for lbl, q in [
        ("prio-korten (46) som är gröna", f"{D} tag:{config.PRIO_TAG_HOG} flag:3"),
        ("prio-korten (46) som är blå", f"{D} tag:{config.PRIO_TAG_HOG} flag:4"),
        ("blå + äkta sökkoll 2026-08-08",
         f"{D} flag:4 tag:{config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX}::2026-08-08"),
        ("gröna i aktiva nya-kön", f"{D} is:new -is:suspended flag:3"),
        ("blå i aktiva nya-kön", f"{D} is:new -is:suspended flag:4"),
    ]:
        print(f"{lbl:<45}: {len(invoke('findCards', query=q))}")

    old = build_old_lookup()
    gron = las(f"{D} is:new -is:suspended flag:3 tag:{config.PRIO_TAG_HOG}", 5)
    bla = las(f"{D} is:new -is:suspended flag:4 "
              f"tag:{config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX}::2026-08-08", 5)
    visa("GRÖNA (snabbkollade mot OLD, aldrig sökkollade)", gron, old)
    visa("BLÅ (eskalerade till riktig sökkoll 2026-08-08)", bla, old)


if __name__ == "__main__":
    main()
