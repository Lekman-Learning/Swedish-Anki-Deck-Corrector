# -*- coding: utf-8 -*-
"""Tar bort felaktig sokverifierad-tagg satt 2026-08-08.

FELET: 177 kort taggades flerbetydelse_sokverifierad::2026-08-08 efter att ha
jämförts mot OLD-facit plus egen kunskap. style_guide.md säger att taggen sätts
ENDAST på kort som eskalerats till och bekräftats via RIKTIG sökkoll. Ingen
extern uppslagning gjordes. Taggen var alltså falsk.

Vad som rullas tillbaka:
  - flerbetydelse_sokverifierad::2026-08-08  tas bort
  - v3_dagsbatch::2026-08-08                 tas bort (korten var aldrig en
                                             v3-batch, och taggen utesluter dem
                                             ur kortbyggare.py:s framtida urval)
  - flaggan återställs till grön DÄR kortet saknar annan sokverifierad-tagg

Vad som INTE rullas tillbaka:
  - innehållsomskrivningarna. De rättade verkliga fel (fel synonymer, saknade
    betydelser, cirkulära definitioner) och är förbättringar oavsett vilken
    granskningsnivå de skedde på.
  - flerbetydelse_snabbkoll2::2026-08-08, som apply_card() satte. Den är sann:
    OLD-jämförelse plus egen kunskap ÄR snabbkoll 2.0.
  - kort med sokverifierad::2026-08-07 eller äldre -- de eskalerades på riktigt
    tidigare och behåller blå flagga.
"""
from ankiconnect import invoke
import config

D = f'deck:"{config.DECK_NAME}"'
FALSK = "flerbetydelse_sokverifierad::2026-08-08"
BATCH = f"{config.DAGSBATCH_TAG_PREFIX}::2026-08-08"


def main():
    nids = invoke("findNotes", query=f"{D} tag:{FALSK}")
    print(f"kort med falsk sokverifierad-tagg: {len(nids)}")
    if not nids:
        return

    # Vilka har en ÄLDRE, äkta sokverifierad? De behåller blå flagga.
    akta = set(invoke("findNotes",
                      query=f"{D} tag:flerbetydelse_sokverifierad::* -tag:{FALSK}"))
    print(f"  ...varav med aldre akta sokverifierad: {len(akta)}")

    invoke("removeTags", notes=nids, tags=FALSK)
    invoke("removeTags", notes=nids, tags=BATCH)

    tillbaka = [n for n in nids if n not in akta]
    cids = []
    for n in tillbaka:
        cids += invoke("findCards", query=f"nid:{n}")
    print(f"  ...flaggor att aterstalla till gron: {len(cids)}")
    for c in cids:
        invoke("setSpecificValueOfCard", card=c, keys=["flags"],
               newValues=[3], warning_check=True)

    print("\n--- efter aterstallning ---")
    for lbl, q in [
        ("sokverifierad::2026-08-08 (ska vara 0)", f"{D} tag:{FALSK}"),
        ("v3_dagsbatch::2026-08-08 (ska vara 0)", f"{D} tag:{BATCH}"),
        ("snabbkoll2::2026-08-08 (behalls)", f"{D} tag:flerbetydelse_snabbkoll2::2026-08-08"),
        ("is:new gron", f"{D} is:new -is:suspended flag:3"),
        ("is:new bla", f"{D} is:new -is:suspended flag:4"),
        ("sokverifierad totalt (akta)", f"{D} tag:flerbetydelse_sokverifierad::*"),
    ]:
        print(f"{lbl}: {len(invoke('findCards', query=q))}")


if __name__ == "__main__":
    main()
