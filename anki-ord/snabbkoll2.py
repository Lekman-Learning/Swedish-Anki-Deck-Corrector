"""Snabbkoll 2.0 (2026-08-06): ersätter det rent minnesbaserade snabbkoll-
läget (som A/B-testet samma dag visade INTE mätbart sänker felfrekvensen,
se style_guide.md "Två tillitsnivåer") med en riktig, men billig, källkoll:
Svenska OLD-decket ("Humanities::Languages::Svenska OLD", ~9800 kort, Adam
bedömer det som nästan 100% korrekt) som facit, jämfört mot v2-kortet.

Till skillnad från sökkoll (WebSearch/WebFetch mot svenska.se etc., dyrt i
tid/tokens) är OLD-uppslaget ett lokalt AnkiConnect-anrop -- i praktiken
gratis och direkt. Granskaren (Claude) jämför sedan v2-kortets huvud-
betydelse/synonymer/exempelmening/register mot OLD-kortets innehåll OCH
egen språkkunskap, precis som vid sökkoll.

Bygger en kö av kort som ALDRIG granskats (ingen flerbetydelse_granskad-tag
alls) tillsammans med eventuell OLD-matchning, för manuell genomgång.
Kort utan OLD-matchning flaggas separat ("old_match": null) -- enligt Adam
(2026-08-06) skippas dessa för nu snarare än att blockera hela flödet.
"""

import argparse
import datetime
import json
import os

import baksida
import config
from ankiconnect import invoke
from queue_lib import build_tags_by_note, fetch_cards_sorted_by_due

OLD_DECK = "Humanities::Languages::Svenska OLD"
FRONT_KEYS = ["Framsida", "Front"]
BACK_KEYS = ["Baksida", "Back"]


def build_old_lookup():
    old_nids = invoke("findNotes", query=f'deck:"{OLD_DECK}"')
    old_info = invoke("notesInfo", notes=old_nids)
    lookup = {}
    for n in old_info:
        fkey = next((k for k in FRONT_KEYS if k in n["fields"]), None)
        bkey = next((k for k in BACK_KEYS if k in n["fields"]), None)
        if not fkey or not bkey:
            continue
        front = n["fields"][fkey]["value"].strip().lower()
        lookup[front] = n["fields"][bkey]["value"]
    return lookup


def find_unreviewed_cards(limit):
    query = (
        f'deck:"{config.DECK_NAME}" tag:{config.FORMAT_TAG_V2} -is:suspended '
        f'-tag:{config.FLERBETYDELSE_TAG_PREFIX}::*'
    )
    return fetch_cards_sorted_by_due(query, limit)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=30)
    args = parser.parse_args()

    cards = find_unreviewed_cards(args.batch_size)
    if not cards:
        print("Inga ogranskade v2-kort kvar.")
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
    out_path = os.path.join(sessions_dir, f"session_{today}_snabbkoll2-test.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"Skrev {len(entries)} kort till {out_path}")
    print(f"OLD-matchning: {matched} av {len(entries)} ({matched / len(entries):.0%})")
    print(f"Utan OLD-matchning (kollas ändå via egen kunskap / skippas): {unmatched}")


if __name__ == "__main__":
    main()
