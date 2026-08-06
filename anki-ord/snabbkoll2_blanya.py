"""Snabbkoll 2.0 på Blå Nya-poolen: blå (flag:4), v2-formaterade kort som
fortfarande är is:new -- Adam har alltså aldrig ens sett dem i Anki än --
och som saknar all flerbetydelse-koll (2026-08-06, se style_guide.md
"Flerbetydelse-genomgång"). 311 kort i poolen vid start.

Samma bygglogik som snabbkoll2.py/snabbkoll2_gamla.py (OLD-decket som
facit + egen kunskap, sökkoll bara vid eskalering) -- bara frågan
(queryn) skiljer sig: här är flag:4 + is:new explicita krav, till
skillnad från snabbkoll2.py som tar alla ogranskade v2-kort oavsett flagga
eller new/learning/review-status.
"""

import argparse
import datetime
import json
import os

import baksida
import config
from ankiconnect import invoke
from queue_lib import build_tags_by_note, fetch_cards_sorted_by_due
from snabbkoll2 import build_old_lookup

FLERBETYDELSE_TAG = config.FLERBETYDELSE_TAG_PREFIX


def find_bla_nya_cards(limit):
    query = (
        f'deck:"{config.DECK_NAME}" flag:4 is:new -is:suspended '
        f'tag:{config.FORMAT_TAG_V2} -tag:{FLERBETYDELSE_TAG}::*'
    )
    return fetch_cards_sorted_by_due(query, limit)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=config.DEFAULT_BATCH_SIZE)
    args = parser.parse_args()

    cards = find_bla_nya_cards(args.batch_size)
    if not cards:
        print("Inga blå nya kort kvar utan flerbetydelse-koll.")
        return

    old_lookup = build_old_lookup()
    tags_by_note = build_tags_by_note(cards)

    entries = []
    matched, unmatched = 0, 0
    for c in cards:
        fields = {name: v["value"] for name, v in c["fields"].items()}
        raw = fields.get(config.FIELD_BAKSIDA, "")
        ord_ = fields.get(config.FIELD_ORD, "")
        parsed = baksida.parse(raw)

        old_match = old_lookup.get(ord_.strip().lower())
        if old_match:
            matched += 1
        else:
            unmatched += 1

        entries.append({
            "noteId": c["note"],
            "ord": ord_,
            "current": parsed,
            "old_facit": old_match,
            "tags": tags_by_note.get(c["note"], []),
            "proposed": None,
            "approved": False,
        })

    today = datetime.date.today().isoformat()
    sessions_dir = os.path.join(os.path.dirname(__file__), "sessions")
    os.makedirs(sessions_dir, exist_ok=True)
    out_path = os.path.join(sessions_dir, f"session_{today}_snabbkoll2-blanya.json")
    n = 2
    while os.path.exists(out_path):
        out_path = os.path.join(sessions_dir, f"session_{today}_snabbkoll2-blanya-batch{n}.json")
        n += 1
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"Skrev {len(entries)} kort till {out_path}")
    print(f"OLD-matchning: {matched} av {len(entries)} ({matched / len(entries):.0%})")
    print(f"Utan OLD-matchning (kollas ändå via egen kunskap / skippas): {unmatched}")


if __name__ == "__main__":
    main()
