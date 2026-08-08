# -*- coding: utf-8 -*-
"""Slutför v3-passet på de 100 granskade is:new-korten, 2026-08-08.

1. Kortar ner gungfly (spärren gav "13 ord i en betydelse").
2. Registrerar sökkollen på de 77 som klarade granskningen utan omskrivning.
   Innehållet rörs inte -- bara tagg och flagga, alltså kringgås inga
   innehållsspärrar. De 77 identifieras som de första gröna is:new-korten i
   due-ordning, vilket är exakt urvalet som granskades (de 23 omskrivna är
   redan blå och faller därmed bort).
3. Sätter v3_dagsbatch på hela urvalet.
"""
import apply_flerbetydelse as af
from ankiconnect import invoke
import config

B = '<font color="#3498db">%s</font>'
D = f'deck:"{config.DECK_NAME}"'
DAGSBATCH = f"{config.DAGSBATCH_TAG_PREFIX}::2026-08-08"
SOKVERIF = "flerbetydelse_sokverifierad::2026-08-08"


def main():
    # 1. gungfly
    nid = invoke("findNotes", query=f'{D} "Framsida:gungfly"')[0]
    anm = af.apply_card(nid,
                        huvudbetydelse="Flytande växtmatta / Bildligt: osäker grund",
                        synonymer=["flytmatta", "osäker grund"],
                        exempelmening=f"Argumentet vilade på ett {B % 'gungfly'} av lösa antaganden.",
                        register="formell", mode="sokkoll", escalated=True, ord_="gungfly")
    print("gungfly:", anm if anm else "inga anmarkningar")

    # 2. de 77 som klarade granskningen
    ids = invoke("findCards", query=f"{D} is:new -is:suspended flag:3")
    ci = invoke("cardsInfo", cards=ids)
    ci.sort(key=lambda c: c["due"])
    nids, seen = [], set()
    for c in ci:
        if c["note"] not in seen:
            if len(seen) >= 77:
                break
            seen.add(c["note"]); nids.append(c["note"])
    cids = [c["cardId"] for c in ci if c["note"] in seen]
    print(f"godkanda att registrera: {len(nids)} noter / {len(cids)} kort")

    invoke("addTags", notes=nids, tags=SOKVERIF)
    for c in cids:
        invoke("setSpecificValueOfCard", card=c, keys=["flags"],
               newValues=[4], warning_check=True)

    # 3. dagsbatch på hela urvalet
    alla = invoke("findNotes", query=f"{D} tag:{SOKVERIF}")
    invoke("addTags", notes=alla, tags=DAGSBATCH)

    for lbl, q in [
        ("sokverifierad::2026-08-08", f"{D} tag:{SOKVERIF}"),
        ("v3_dagsbatch::2026-08-08", f"{D} tag:{DAGSBATCH}"),
        ("is:new gron kvar", f"{D} is:new -is:suspended flag:3"),
        ("is:new bla", f"{D} is:new -is:suspended flag:4"),
        ("oberoende_verifierad (ska vara 0)", f"{D} tag:{config.OBEROENDE_TAG_PREFIX}::*"),
    ]:
        print(f"{lbl}: {len(invoke('findCards', query=q))}")


if __name__ == "__main__":
    main()
