"""Separat, litet pass: blåa kort (flag:4, "stämmer i sak") som ändå
innehåller en känd återkommande felaktig synonym (Adam har identifierat
mönstret manuellt — definitionerna stämmer alltid, men vissa synonymer är
fel, t.ex. "allsmäktig"/"allrådande"). Snabb riktad genväg till de värsta
blåa korten, utan att vänta på att de kommer upp i den vanliga blå-rotationen
i fetch_queue.py. Fyll på SUSPECT_SYNONYMS när fler mönster upptäcks.

Skriver sessions/session_<datum>_blaa-misstankta.json — samma format som
fetch_queue.py, apply_updates.py hanterar den utan ändring (flaggan är redan
blå, ingen flagg-ändring sker).
"""

import argparse

import config
from queue_lib import (
    build_tags_by_note,
    fetch_cards_sorted_by_due,
    to_queue_entry,
    write_session,
)

SUSPECT_SYNONYMS = ["allsmäktig", "allrådande"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=config.DEFAULT_BATCH_SIZE)
    args = parser.parse_args()

    terms_query = " OR ".join(f'"{t}"' for t in SUSPECT_SYNONYMS)
    query = f'deck:"{config.DECK_NAME}" flag:{config.FLAG_BLA} ({terms_query}) -tag:{config.REVIEWED_TAG_PREFIX}::*'

    cards = fetch_cards_sorted_by_due(query, args.batch_size)
    tags_by_note = build_tags_by_note(cards)
    queue = [to_queue_entry(c, tags_by_note, "blå (misstänkt synonym)") for c in cards]

    if not queue:
        print("Inga blåa kort med kända misstänkta synonymer kvar (utanför redan granskade).")
        return

    out_path = write_session(queue, name_suffix="_blaa-misstankta")
    print(f"Skrev {len(queue)} misstänkta blåa kort till {out_path}")


if __name__ == "__main__":
    main()
