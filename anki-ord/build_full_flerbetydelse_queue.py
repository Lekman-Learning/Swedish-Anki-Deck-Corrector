"""Engångshjälp (2026-08-05, andra passet): Adam bad om att snabbkolla ALLA
kort som inte kollats än, inte bara `scan_multiple_meanings.py`s
heuristik-kandidater (>= 3 synonymer). Bygger kön direkt fran live Anki:
alla v2, ej suspenderade kort som helt saknar `flerbetydelse_granskad::*`
(oavsett synonymantal) — bredare an foregaende pass som bara tackte
scan-filens 994 kandidater.

Delar upp i filer om max --chunk-size (default 300) sa granskningen kan
appliceras lopande utan att tappa allt vid en eventuell krasch.

Skriver sessions/session_<datum>_flerbetydelser-full-batchN.json.
"""

import argparse
import datetime
import os

import config
from ankiconnect import invoke
import baksida
from queue_lib import build_tags_by_note, fetch_cards_sorted_by_due, write_session


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunk-size", type=int, default=300)
    args = parser.parse_args()

    query = (
        f'deck:"{config.DECK_NAME}" tag:{config.FORMAT_TAG_V2} -is:suspended '
        f'-tag:{config.FLERBETYDELSE_TAG_PREFIX}::*'
    )
    cards = fetch_cards_sorted_by_due(query, limit=100_000)
    tags_by_note = build_tags_by_note(cards)

    seen_notes = set()
    candidates = []
    for card in cards:
        note_id = card["note"]
        if note_id in seen_notes:
            continue
        seen_notes.add(note_id)

        fields = {name: v["value"] for name, v in card["fields"].items()}
        raw = fields.get(config.FIELD_BAKSIDA, "")
        parsed = baksida.parse(raw)
        if not parsed["huvudbetydelse"]:
            continue  # inte v2-format, ska inte finnas i denna kö men skydda ändå

        candidates.append({
            "noteId": note_id,
            "due": card["due"],
            "ord": fields.get(config.FIELD_ORD, ""),
            "current": parsed,
            "tags": tags_by_note.get(note_id, []),
            "proposed": None,
            "approved": False,
            "note_till_granskare": (
                "SNABBKOLL (fullstandig svep): kolla om nagon/nagra synonymer hor till en "
                "ANNAN betydelse an Huvudbetydelse. Om ja, dela upp Huvudbetydelse/synonymer "
                "med ' ; ' (se style_guide.md 'Flerbetydelse-genomgang' och 'Dold andra "
                "betydelse'). Om nej, godkann orort med note om att inget dolt hittades."
            ),
        })

    print(f"{len(candidates)} kort utan flerbetydelse_granskad hittade (sorterat pa due).")
    if not candidates:
        return

    today = datetime.date.today().isoformat()
    sessions_dir = os.path.join(os.path.dirname(__file__), "sessions")
    for i in range(0, len(candidates), args.chunk_size):
        chunk = candidates[i:i + args.chunk_size]
        n = i // args.chunk_size + 1
        out_path = os.path.join(sessions_dir, f"session_{today}_flerbetydelser-full-batch{n}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            import json
            json.dump(chunk, f, ensure_ascii=False, indent=2)
        print(f"Skrev {len(chunk)} kort till {out_path}")


if __name__ == "__main__":
    main()
