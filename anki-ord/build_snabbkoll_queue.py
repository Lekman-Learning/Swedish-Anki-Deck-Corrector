"""Engångshjälp: bygger en färsk kö för flerbetydelse-snabbkollen (se
style_guide.md, "Flerbetydelse-genomgång") av de kandidater
`scan_multiple_meanings.py` redan hittat (994 st,
sessions/session_2026-08-05_flera-betydelser-scan.json), MINUS de som redan
fått `flerbetydelse_granskad::*` sen scanningen kördes. Kollar mot riktiga
Anki-taggar live, inte mot de gamla batch1/2/3-filerna (som kan vara
inaktuella). Delar upp resten i filer om max --chunk-size (default 300,
samma stil som tidigare batchar) så en granskningsomgång kan appliceras
löpande utan att tappa allt vid en eventuell krasch.

Skriver sessions/session_<datum>_flerbetydelser-snabbkoll-batchN.json.
"""

import argparse
import datetime
import json
import os

import config
from ankiconnect import invoke

SCAN_FILE = os.path.join(os.path.dirname(__file__), "sessions", "session_2026-08-05_flera-betydelser-scan.json")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunk-size", type=int, default=300)
    args = parser.parse_args()

    with open(SCAN_FILE, "r", encoding="utf-8") as f:
        candidates = json.load(f)

    note_ids = [c["noteId"] for c in candidates]
    already_tagged = set(invoke(
        "findNotes",
        query=f'deck:"{config.DECK_NAME}" tag:{config.FLERBETYDELSE_TAG_PREFIX}::*',
    ))

    remaining = [c for c in candidates if c["noteId"] not in already_tagged]
    print(f"{len(candidates)} kandidater totalt, {len(already_tagged & set(note_ids))} redan flerbetydelse_granskad, {len(remaining)} kvar att snabbkolla.")

    if not remaining:
        return

    today = datetime.date.today().isoformat()
    sessions_dir = os.path.join(os.path.dirname(__file__), "sessions")
    for i in range(0, len(remaining), args.chunk_size):
        chunk = remaining[i:i + args.chunk_size]
        n = i // args.chunk_size + 1
        out_path = os.path.join(sessions_dir, f"session_{today}_flerbetydelser-snabbkoll-batch{n}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(chunk, f, ensure_ascii=False, indent=2)
        print(f"Skrev {len(chunk)} kort till {out_path}")


if __name__ == "__main__":
    main()
