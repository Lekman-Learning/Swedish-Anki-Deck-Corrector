# -*- coding: utf-8 -*-
"""Vad är en sökkoll utan blindgranskning egentligen värd?

Adams fråga 2026-08-11: *"full v3 rätta 10 av de sökkollade korten på is:review
och 10 som är suspended utan någon sökkoll alls så att vi kan se skillnaden och
få en idé av hur pålitliga dessa sökkollade kort utan full v3 egentligen är."*

Frågan är skarp. 618 kort släpptes 2026-08-11 som **provisoriska**: de har en
riktig sökkoll men har aldrig blindgranskats. De ligger i Adams kö och pluggas
varje dag. Om de i praktiken är lika trasiga som de osökkollade korten är
mellansteget värdelöst och de 618 borde spärras. Om de är tydligt bättre är
sökkollen en giltig kvalitetsnivå i sig, och de kan ligga kvar medan kön betas av.

Två armar, tio kort var, dragna slumpmässigt ur samma deck:

    A  PROVISORISKA   tag:v3_provisorisk::* -- sökkollade, i kön, ej blindgranskade
    B  OSÖKKOLLADE    suspenderade is:review helt utan sökverifiering

Armarna hålls i SKILDA sessionsfiler hela vägen, så att verdikten går att
räkna per arm. Slås de ihop går hela poängen förlorad.

Urvalet är slumpmässigt, inte urgency-rankat -- det är avsiktligt. Kvällens
100-kortsbatch var urgency-rankad och gav 42 % underkänt i del 1 mot 12-15 % i
de andra delarna, alltså är rankningen inte neutral. En jämförelse mellan armar
kräver att båda dras på samma sätt, och slumpen är det enda urval som inte
lutar åt något håll.

    python v3_experiment_sokkoll_varde.py --fro 20260811
"""

import argparse
import json
import random
import sys

import config
from ankiconnect import invoke

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DECK = f'deck:"{config.DECK_NAME}"'
SOKVERIF = f"tag:{config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX}::*"

ARMAR = {
    "A-provisorisk": (
        f"{DECK} tag:v3_provisorisk::* -tag:{config.OBEROENDE_TAG_PREFIX}::* "
        f"-tag:v3_pausad::* -tag:v3_underkand::*"
    ),
    "B-osokkollad": (
        f"{DECK} is:review -is:learn is:suspended -{SOKVERIF} "
        f"-tag:v3_pausad::* -tag:v3_underkand::*"
    ),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--antal", type=int, default=10)
    ap.add_argument("--fro", type=int, default=20260811,
                    help="fast frö så urvalet går att återskapa")
    a = ap.parse_args()

    rnd = random.Random(a.fro)
    for namn, fraga in ARMAR.items():
        kort = invoke("findCards", query=fraga)
        print(f"{namn:<16} population: {len(kort)}")
        if len(kort) < a.antal:
            sys.exit(f"För få kort i {namn}: {len(kort)}")
        urval = rnd.sample(sorted(kort), a.antal)
        # kortbyggare --ids-fil vill ha v3_urgency.json-formen. `poang` är
        # meningslöst här (urvalet är slumpat) men fältet läses vid utskrift.
        rader = [{"cardId": c, "ord": "?", "poang": 0} for c in urval]
        utfil = f"experiment_sokkoll_{namn}.json"
        with open(utfil, "w", encoding="utf-8") as f:
            json.dump(rader, f, ensure_ascii=False, indent=1)
        print(f"                 skrev {utfil} ({a.antal} kort, frö {a.fro})")

    print("\nBygg sedan EN session per arm -- de får inte slås ihop:")
    for namn in ARMAR:
        print(f"  python kortbyggare.py --spar omgranskning "
              f"--ids-fil experiment_sokkoll_{namn}.json --antal-ur-fil {a.antal}")


if __name__ == "__main__":
    main()
