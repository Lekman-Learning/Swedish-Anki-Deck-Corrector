"""Daglig/återkommande hämtning av nästa skiva suspenderade, ogranskade Blå
Nya-kort (se suspend_unreviewed_new.py), due-sorterat -- samma könordning
Adam möter dem i när de släpps in. Skriver sessions/session_<datum>_bla-nya-
nasta.json för Fas 2-granskning. apply_updates.py avsuspenderar varje kort
automatiskt när det appliceras, så granskning + applicering av denna fil ÄR
"släppet" -- inget separat unsuspend-steg behövs.

Default batch-size = config.DEFAULT_BATCH_SIZE (100), Adam nämnde 110-200/
dag som riktvärde -- justera med --batch-size vid behov.
"""

import argparse

import config
from queue_lib import build_tags_by_note, fetch_cards_sorted_by_due, to_queue_entry, write_session

QUERY = f'deck:"{config.DECK_NAME}" is:new -tag:{config.FORMAT_TAG_V2}'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=config.DEFAULT_BATCH_SIZE)
    args = parser.parse_args()

    cards = fetch_cards_sorted_by_due(QUERY, args.batch_size)
    if not cards:
        print("Inga ogranskade Blå Nya-kort kvar (hela poolen klar).")
        return

    tags_by_note = build_tags_by_note(cards)
    entries = [to_queue_entry(c, tags_by_note, "blå-nya") for c in cards]
    out_path = write_session(entries, "_bla-nya-nasta")
    print(f"Skrev {len(entries)} kort till {out_path}")


if __name__ == "__main__":
    main()
