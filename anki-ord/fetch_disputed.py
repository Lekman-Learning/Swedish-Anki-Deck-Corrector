"""Hittar kort Adam manuellt bestrider EFTER granskning: han flaggar ett
redan granskad::*-taggat kort rött i riktiga Anki (röd är annars "ledig"
på granskade kort — bara blå/grön används för klara kort, se
style_guide.md "Flaggkoppling till konfidens"). Detta är Adams eget
lås-/markeringssystem: ingen kod behövs för att sätta det, bara ett
skript som hittar dem igen, eftersom fetch_queue.py annars exkluderar
alla granskad::*-taggade kort blint.

Skriver sessions/session_<datum>_bestridda.json, samma format/flöde
(Fas 2/Fas 3) som övriga fetch_*.py.
"""

import config
from queue_lib import build_tags_by_note, fetch_cards_sorted_by_due, to_queue_entry, write_session


def main():
    query = (
        f'deck:"{config.DECK_NAME}" flag:{config.FLAG_ROD} '
        f'tag:{config.REVIEWED_TAG_PREFIX}::*'
    )
    cards = fetch_cards_sorted_by_due(query, limit=100_000)
    if not cards:
        print("Inga bestridda kort hittade (inget granskat kort är rödflaggat just nu).")
        return

    tags_by_note = build_tags_by_note(cards)
    entries = [to_queue_entry(c, tags_by_note, "bestridd") for c in cards]
    out = write_session(entries, "_bestridda")
    print(f"Skrev {len(entries)} bestridda kort till {out}")


if __name__ == "__main__":
    main()
