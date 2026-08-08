# -*- coding: utf-8 -*-
"""Markerar de kort som skrevs om 2026-08-08 UTAN riktig sökkoll som
hög prio för v3-omgranskning (Adams begäran samma dag).

VILKA: kort som bär `flerbetydelse_granskad::2026-08-08` (satt av
apply_card()) men saknar sökverifierad-tagg helt. De fick sitt innehåll
omskrivet under det pass där 177 kort felaktigt taggades sökverifierade,
och innehållsändringarna behölls vid rollbacken -- men ingen uppslagning
gjordes. De ligger alltså i Adams aktiva kö med text jag skrivit och
ingen källa bakom sig.

VARFÖR BARA 46 OCH INTE 177: rollbacken tog bort taggen från 177 kort,
men bara 73 av dem hade skrivits via apply_card() och därmed fått ett
`::2026-08-08`-spår i Anki (27 med äkta sökkoll, 46 utan). Resten
taggades av ad-hoc-script som anropade addTags direkt och lämnade inget
spår -- de går bara att återskapa ur ordlistorna i v3_omskrivning_*.py.
Lärdomen är densamma som för register och Adam-tal: spårbarhet måste
sitta i skrivvägen, inte i ett script som råkar köras.

Taggen ändrar URVALET, inte bara utseendet: kortbyggare.hamta_pool()
hämtar prio-märkta kort före den vanliga due-ordningen, i båda spåren.
"""
import config
from ankiconnect import invoke

D = f'deck:"{config.DECK_NAME}"'
FRAGA = (f"{D} tag:flerbetydelse_granskad::2026-08-08 "
         f"-tag:{config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX}::*")


def main():
    nids = invoke("findNotes", query=FRAGA)
    print(f"Kandidater: {len(nids)}")
    if not nids:
        return

    # Kontrollera INNAN taggning att urvalet är det jag tror: inget kort
    # får ha en sökverifierad-tagg av något datum, och alla ska vara v2.
    info = invoke("notesInfo", notes=nids)
    fel = []
    for n in info:
        taggar = n.get("tags", [])
        ord_ = n["fields"][config.FIELD_ORD]["value"]
        if any(t.startswith(f"{config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX}::")
               for t in taggar):
            fel.append(f"{ord_}: har ändå en sökverifierad-tagg")
        if config.FORMAT_TAG_V2 not in taggar:
            fel.append(f"{ord_}: saknar {config.FORMAT_TAG_V2}")
    if fel:
        print("AVBRYTER, urvalet stämmer inte:")
        for f in fel[:10]:
            print(f"  {f}")
        return

    invoke("addTags", notes=nids, tags=config.PRIO_TAG_HOG)

    efter = invoke("findNotes", query=f"{D} tag:{config.PRIO_TAG_HOG}")
    print(f"Taggade {config.PRIO_TAG_HOG}: {len(efter)}")
    print("\nOrden, i könordning:")
    for i, n in enumerate(invoke("notesInfo", notes=nids)):
        print(f"  {i + 1:>2}. {n['fields'][config.FIELD_ORD]['value']}")

    # Ligger de i den aktiva kön eller är de suspenderade? Avgör vilket
    # spår som plockar upp dem.
    for lbl, q in [
        ("i spår B (aktiv kö, ej blindverifierad)",
         f'{D} -is:suspended tag:{config.FORMAT_TAG_V2} '
         f'-tag:{config.OBEROENDE_TAG_PREFIX}::* -tag:{config.DAGSBATCH_TAG_PREFIX}::* '
         f'tag:{config.PRIO_TAG_HOG}'),
        ("suspenderade (utanför spår B)", f"{D} is:suspended tag:{config.PRIO_TAG_HOG}"),
        ("blockerade av v3_dagsbatch-taggen",
         f"{D} tag:{config.PRIO_TAG_HOG} tag:{config.DAGSBATCH_TAG_PREFIX}::*"),
    ]:
        print(f"{lbl}: {len(invoke('findNotes', query=q))}")


if __name__ == "__main__":
    main()
