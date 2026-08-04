"""Daglig granskningskö: kort som kommer snarast, oavsett vilken av de gamla
batch-filerna de råkar tillhöra.

Två grupper, i Ankis egen due-ordning (samma ordning Adam faktiskt möter
korten i):
1. Redan sedda kort (learning/review, ej suspenderade) — sorterade på due,
   dvs de som schemalagts snarast (oftast idag/imorgon).
2. Helt nya, aldrig visade kort (is:new) — sorterade på köposition, dvs de
   NÄSTA Adam introduceras för. Antal styrs som standard av deckets egen
   "nya kort/dag"-gräns (hämtas live via getDeckConfig) så urvalet matchar
   vad Adam faktiskt kommer se samma dag.

Suspenderade (Låst) kort exkluderas härifrån — de är per definition inte på
väg att visas förrän de avsuspenderas manuellt, hör hemma i de vanliga
batch-filerna istället.

Exkluderar alltid redan granskad::*-taggade kort (samma säkerhetsspärr som
fetch_queue.py) — kör man detta dagligen täcker varje körning bara det som
tillkommit/blivit aktuellt sen sist, ingen dubbelgranskning.

Skriver sessions/session_<datum>_urgent.json.
"""

import argparse

import config
from ankiconnect import invoke
from queue_lib import build_tags_by_note, fetch_cards_sorted_by_due, to_queue_entry, write_session


def new_cards_per_day():
    conf = invoke("getDeckConfig", deck=config.DECK_NAME)
    return conf["new"]["perDay"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seen-limit", type=int, default=200)
    parser.add_argument(
        "--new-limit",
        type=int,
        default=None,
        help="default: deckets nya-kort/dag-gräns (getDeckConfig, hämtas live)",
    )
    args = parser.parse_args()

    new_limit = args.new_limit if args.new_limit is not None else new_cards_per_day()

    seen_query = (
        f'deck:"{config.DECK_NAME}" (is:learn OR is:review) -is:suspended -is:new '
        f'-tag:{config.REVIEWED_TAG_PREFIX}::*'
    )
    new_query = (
        f'deck:"{config.DECK_NAME}" is:new -tag:{config.REVIEWED_TAG_PREFIX}::*'
    )

    seen_cards = fetch_cards_sorted_by_due(seen_query, args.seen_limit)
    new_cards = fetch_cards_sorted_by_due(new_query, new_limit)

    all_cards = seen_cards + new_cards
    if not all_cards:
        print("Inga akuta kort kvar (utanför redan granskade).")
        return

    tags_by_note = build_tags_by_note(all_cards)
    queue = [to_queue_entry(c, tags_by_note, "urgent-sedda") for c in seen_cards]
    queue += [to_queue_entry(c, tags_by_note, "urgent-nya") for c in new_cards]

    out_path = write_session(queue, name_suffix="_urgent")
    print(f"Skrev {len(queue)} kort ({len(seen_cards)} sedda, {len(new_cards)} nya) till {out_path}")


if __name__ == "__main__":
    main()
