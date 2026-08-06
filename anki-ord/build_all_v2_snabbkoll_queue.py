"""Engångshjälp (2026-08-06, tredje passet): Adam vill snabbkolla ALLA 3144
v2, ej suspenderade kort mot de 4 breddade kriterierna (huvudbetydelse
korrekt/tydlig, synonymer passar, exempelmening passar, ingen dold/saknad
betydelse) + OLD-decket som jamforelsefacit — inte bara de som aldrig fatt
en flerbetydelse-koll. Motiverat av "vrak"-fallet: det kortet hade redan
bade granskad:: och flerbetydelse_snabbkoll::-taggar och hade anda en
riktig lucka (saknad isbetydelse) som bara syntes vid en riktig sokkoll.

Ingen tag-filtrering har alltsa - kon ar HELA v2/ej-suspenderad-poolen.

Delar upp i filer om max --chunk-size (default 450, storre an tidigare
300 for att halla ner antalet parallella topp-niva-agenter — lardom fran
kraschen 2026-08-05 dar for manga parallella agenter (varav flera spawnade
egna under-agenter) trotte sessionens API-grans).

Skriver sessions/session_<datum>_alla-v2-snabbkoll-batchN.json.
"""

import argparse
import datetime
import json
import os

import config
from ankiconnect import invoke
import baksida
from queue_lib import build_tags_by_note, fetch_cards_sorted_by_due, write_session


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunk-size", type=int, default=450)
    args = parser.parse_args()

    query = f'deck:"{config.DECK_NAME}" tag:{config.FORMAT_TAG_V2} -is:suspended'
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
            continue

        candidates.append({
            "noteId": note_id,
            "due": card["due"],
            "ord": fields.get(config.FIELD_ORD, ""),
            "current": parsed,
            "tags": tags_by_note.get(note_id, []),
            "proposed": None,
            "approved": False,
            "note_till_granskare": (
                "BRED SNABBKOLL: kolla (1) ar Huvudbetydelsen korrekt/tydlig, "
                "(2) passar synonymerna, (3) passar exempelmeningen, "
                "(4) saknas nagon betydelse. Jamfor ocksa mot Svenska OLD-decket "
                "(samma ord) som ett andra facit -- om de INTE stammer overens, "
                "titta noggrannare. Om kortet redan har en bild: bild_html ska "
                "ALLTID kopieras oforandrat om inget nytt uttryckligen laggs till."
            ),
        })

    print(f"{len(candidates)} v2, ej suspenderade kort totalt (hela poolen, ingen tag-filtrering).")
    if not candidates:
        return

    today = datetime.date.today().isoformat()
    sessions_dir = os.path.join(os.path.dirname(__file__), "sessions")
    for i in range(0, len(candidates), args.chunk_size):
        chunk = candidates[i:i + args.chunk_size]
        n = i // args.chunk_size + 1
        out_path = os.path.join(sessions_dir, f"session_{today}_alla-v2-snabbkoll-batch{n}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(chunk, f, ensure_ascii=False, indent=2)
        print(f"Skrev {len(chunk)} kort till {out_path}")


if __name__ == "__main__":
    main()
