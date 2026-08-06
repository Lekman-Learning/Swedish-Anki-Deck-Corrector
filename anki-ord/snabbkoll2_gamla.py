"""Snabbkoll 2.0 på den gamla poolen: 1880 kort granskade med den GAMLA,
rent minnesbaserade snabbkollen (`flerbetydelse_snabbkoll::*`) innan
snabbkoll 2.0 fanns (2026-08-06, se style_guide.md "Flerbetydelse-
genomgång"). A/B-testet visade att den gamla snabbkollen missade 8,75% av
felen -- dessa kort har alltså inte fått en tillförlitlig kontroll än.

322 av de 1880 har redan fått en riktig sökkoll (`flerbetydelse_
sokverifierad::*`) trots att de aldrig körts igenom snabbkoll2.py --
de behöver INTE köras om (Adam 2026-08-06). Kvar: 1558 kort som varken
har snabbkoll2- eller sökverifierad-taggen.

Samma bygglogik som snabbkoll2.py (OLD-decket som facit + egen kunskap,
sökkoll bara vid eskalering) -- bara frågan (queryn) skiljer sig.
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

OLD_SNABBKOLL_TAG = config.FLERBETYDELSE_SNABBKOLL_TAG_PREFIX
NEW_SNABBKOLL_TAG = config.FLERBETYDELSE_SNABBKOLL2_TAG_PREFIX
SOKVERIFIERAD_TAG = config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX


def find_gamla_snabbkollade_cards(limit):
    query = (
        f'deck:"{config.DECK_NAME}" tag:{OLD_SNABBKOLL_TAG}::* -is:suspended '
        f'-tag:{NEW_SNABBKOLL_TAG}::* -tag:{SOKVERIFIERAD_TAG}::*'
    )
    return fetch_cards_sorted_by_due(query, limit)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=config.DEFAULT_BATCH_SIZE)
    args = parser.parse_args()

    cards = find_gamla_snabbkollade_cards(args.batch_size)
    if not cards:
        print("Inga gamla snabbkollade kort kvar utan snabbkoll2/sökverifiering.")
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
    out_path = os.path.join(sessions_dir, f"session_{today}_snabbkoll2-gamla-pool.json")
    n = 2
    while os.path.exists(out_path):
        out_path = os.path.join(sessions_dir, f"session_{today}_snabbkoll2-gamla-pool-batch{n}.json")
        n += 1
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"Skrev {len(entries)} kort till {out_path}")
    print(f"OLD-matchning: {matched} av {len(entries)} ({matched / len(entries):.0%})")
    print(f"Utan OLD-matchning (kollas ändå via egen kunskap / skippas): {unmatched}")


if __name__ == "__main__":
    main()
