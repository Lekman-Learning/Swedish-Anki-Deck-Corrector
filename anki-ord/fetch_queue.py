"""Fas 1 — hämtar ett granskningspass:
1. röda kort (fel innehåll)
2. gula kort (osäkert innehåll)
3. blåa kort (innehållet stämmer, men kan vara dåligt skrivet/Adam-tal)
Inom varje flagg-nivå: kort Adam redan sett (learning/review) före aldrig
visade (new) kort, sorterat efter Ankis due-position inom varje grupp — Adam
vill rätta det han redan pluggar innan nytt material.
Upp till --batch-size (default config.DEFAULT_BATCH_SIZE), exkluderar kort
som redan taggats granskad::* i en tidigare omgång.
Skriver sessions/session_<datum>.json.
"""

import argparse

import config
from queue_lib import (
    build_tags_by_note,
    fetch_cards_prioritized,
    to_queue_entry,
    write_session,
)

TIERS = [
    (config.FLAG_ROD, "röd"),
    (config.FLAG_GUL, "gul"),
    (config.FLAG_BLA, "blå"),
]


def build_query(flag_number):
    return (
        f'deck:"{config.DECK_NAME}" flag:{flag_number} '
        f'-tag:{config.REVIEWED_TAG_PREFIX}::*'
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=config.DEFAULT_BATCH_SIZE)
    args = parser.parse_args()

    queue = []
    counts = {}

    for flag_number, label in TIERS:
        remaining = args.batch_size - len(queue)
        if remaining <= 0:
            break
        cards = fetch_cards_prioritized(build_query(flag_number), remaining)
        tags_by_note = build_tags_by_note(cards)
        entries = [to_queue_entry(c, tags_by_note, label) for c in cards]
        queue.extend(entries)
        counts[label] = len(entries)

    if not queue:
        print("Inga kort kvar att granska (utanför redan granskade).")
        return

    out_path = write_session(queue)
    summary = ", ".join(f"{n} {label}" for label, n in counts.items() if n)
    print(f"Skrev {len(queue)} kort ({summary}) till {out_path}")


if __name__ == "__main__":
    main()
