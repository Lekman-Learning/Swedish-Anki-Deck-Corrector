# -*- coding: utf-8 -*-
"""Märker kvällens 77 sökkollade kort med v3_dagsbatch::2026-08-08.

Adam 2026-08-08: kort som granskats med v3 ska vara v3-märkta.

Två taggar markerar v3, och de påstår olika saker:

  v3_dagsbatch::<datum>       spårar VILKEN BATCH kortet kom i. Beskrivande,
                              inget kvalitetspåstående. Korten nedan kördes
                              i en batch 2026-08-08 -- taggen är sann.

  oberoende_verifierad::<d>   påstår att kortet klarat BLIND andragranskning.
                              Sätts INTE här: samma agent skrev och granskade,
                              paket-steget hoppades över. Att sätta den vore
                              falskt i exakt den kolumn v3 vilar på.

Korten har alltså 3 av v3:s 4 steg: facit-jämförelse mot Svenska OLD,
sökkoll, och omskrivning genom spärrarna. Det som saknas är verdiktsteget.
"""
from ankiconnect import invoke
import config

TAGG = f"{config.DAGSBATCH_TAG_PREFIX}::2026-08-08"
D = f'deck:"{config.DECK_NAME}"'


def main():
    nids = invoke("findNotes",
                  query=f'{D} tag:flerbetydelse_sokverifierad::2026-08-08')
    print(f"kort att marka: {len(nids)}")
    if not nids:
        return
    invoke("addTags", notes=nids, tags=TAGG)

    for lbl, q in [
        (f"{TAGG}", f"{D} tag:{TAGG}"),
        ("v3_dagsbatch::* totalt", f"{D} tag:{config.DAGSBATCH_TAG_PREFIX}::*"),
        ("oberoende_verifierad::* (ska vara 0)",
         f"{D} tag:{config.OBEROENDE_TAG_PREFIX}::*"),
    ]:
        print(f"{lbl}: {len(invoke('findCards', query=q))}")


if __name__ == "__main__":
    main()
