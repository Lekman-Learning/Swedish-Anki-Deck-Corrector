"""Heuristisk skanning: hittar kort där synonymerna troligen avslöjar en
GÖMD andra betydelse som saknas i Huvudbetydelse (se style_guide.md,
"Dold andra betydelse", beslutat 2026-08-05 efter "konglomerat"-fallet —
Huvudbetydelse hade bara företagsbetydelsen, synonymerna hörde till den
allmänna "hopgyttring"-betydelsen).

Rent mekanisk kan inte avgöra OM synonymerna faktiskt hör till en annan
betydelse (kräver ordboks-koll), bara flagga KANDIDATER för manuell
granskning: kort där Huvudbetydelse saknar ` ; ` (bara en betydelse angiven)
men har >= MIN_SYNONYMER synonymer OCH inga synonym_groups redan — fler
synonymer än så är ett svagt tecken på att de kan spänna över mer än en
betydelse.

Ändrar inget. Skriver sessions/session_<datum>_flera-betydelser-scan.json.
"""

import config
from ankiconnect import invoke
import baksida
from queue_lib import build_tags_by_note, fetch_cards_sorted_by_due, write_session

MIN_SYNONYMER = 3


def main():
    query = f'deck:"{config.DECK_NAME}" tag:{config.REVIEWED_TAG_PREFIX}::*'
    cards = fetch_cards_sorted_by_due(query, limit=100_000)  # sorterat på due (lägst/snarast först)
    seen_notes = set()
    tags_by_note = build_tags_by_note(cards)

    candidates = []
    total_scanned = 0
    for card in cards:
        note_id = card["note"]
        if note_id in seen_notes:
            continue
        seen_notes.add(note_id)
        total_scanned += 1

        fields = {name: v["value"] for name, v in card["fields"].items()}
        raw = fields.get(config.FIELD_BAKSIDA, "")
        parsed = baksida.parse(raw)
        if not parsed["huvudbetydelse"]:
            continue  # inte v2-format än, hoppa

        already_split = ";" in parsed["huvudbetydelse"] or parsed["synonym_groups"]
        if already_split:
            continue

        if len(parsed["synonymer"]) >= MIN_SYNONYMER:
            candidates.append({
                "noteId": note_id,
                "due": card["due"],
                "ord": fields.get(config.FIELD_ORD, ""),
                "current": parsed,
                "tags": tags_by_note.get(note_id, []),
                "proposed": None,
                "approved": False,
                "note_till_granskare": "kandidat — kolla om alla synonymer hör till SAMMA betydelse, annars dela upp Huvudbetydelse/synonymer med ' ; ' (se style_guide.md 'Flerbetydelse-genomgång')",
            })

    print(f"{total_scanned} granskade kort skannade, {len(candidates)} kandidater hittade (sorterat på due).")
    if candidates:
        out = write_session(candidates, "_flera-betydelser-scan")
        print(f"Skrev till {out}")


if __name__ == "__main__":
    main()
