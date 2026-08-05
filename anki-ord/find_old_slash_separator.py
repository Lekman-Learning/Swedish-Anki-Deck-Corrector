"""Engångshjälp: hittar v2-kort där Huvudbetydelse innehåller ` / ` (kan vara
den korrekta användningen -- omformuleringar av SAMMA betydelse -- eller den
gamla, felaktiga användningen för att separera FAKTISKT SKILDA betydelser,
se baksida.py build()-docstring "huvudbetydelse-separatorer" och Adams
"tillgå"-fynd 2026-08-05. Ändrar inget, bara listar kandidater för manuell
granskning (samma mönster som scan_multiple_meanings.py).

Skriver sessions/session_<datum>_gammal-slash-separator.json.
"""

import config
from queue_lib import build_tags_by_note, fetch_cards_sorted_by_due, write_session
import baksida

QUERY = f'deck:"{config.DECK_NAME}" tag:{config.FORMAT_TAG_V2} -is:suspended'


def main():
    cards = fetch_cards_sorted_by_due(QUERY, limit=100_000)
    tags_by_note = build_tags_by_note(cards)
    seen = set()
    candidates = []
    for card in cards:
        note_id = card["note"]
        if note_id in seen:
            continue
        seen.add(note_id)
        fields = {name: v["value"] for name, v in card["fields"].items()}
        raw = fields.get(config.FIELD_BAKSIDA, "")
        parsed = baksida.parse(raw)
        if " / " in parsed["huvudbetydelse"]:
            candidates.append({
                "noteId": note_id,
                "ord": fields.get(config.FIELD_ORD, ""),
                "current": parsed,
                "tags": tags_by_note.get(note_id, []),
                "proposed": None,
                "approved": False,
                "note_till_granskare": "kandidat -- avgor om / separerar SAMMA betydelse (ratt, ror ej) eller FAKTISKT SKILDA betydelser (fel, byt till ;)",
            })

    print(f"{len(seen)} v2-kort skannade, {len(candidates)} med ' / ' i Huvudbetydelse.")
    if candidates:
        out = write_session(candidates, "_gammal-slash-separator")
        print(f"Skrev {out}")


if __name__ == "__main__":
    main()
