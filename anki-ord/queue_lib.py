"""Delad logik för att hämta, sortera och skriva sessionskö-filer. Används av
fetch_queue.py (röd/gul/blå) och fetch_blue_suspects.py (blå med misstänkt
fel synonym).
"""

import datetime
import json
import os

import baksida
import config
from ankiconnect import invoke


def fetch_cards_sorted_by_due(query, limit):
    """Hämtar kort matchande query, sorterat efter Ankis due-position — samma
    ordning korten faktiskt kommer till Adam i Anki (new: köposition,
    review/relearning: schemalagt datum).
    """
    card_ids = invoke("findCards", query=query)
    if not card_ids:
        return []
    cards_info = invoke("cardsInfo", cards=card_ids)
    cards_info.sort(key=lambda c: c["due"])
    return cards_info[:limit]


def fetch_cards_prioritized(query, limit):
    """Som fetch_cards_sorted_by_due, men kort Adam redan sett (learning/
    review/relearning, dvs `-is:new`) kommer alltid före aldrig visade kort
    (`is:new`). Adam vill granska/rätta det han redan håller på att lära sig
    innan nytt material, så han inte lär in fel version av ett ord han redan
    pluggar.
    """
    seen = fetch_cards_sorted_by_due(f"{query} -is:new", limit)
    remaining = limit - len(seen)
    if remaining <= 0:
        return seen
    new = fetch_cards_sorted_by_due(f"{query} is:new", remaining)
    return seen + new


def to_queue_entry(card_info, tags_by_note, flag_label):
    fields = {name: v["value"] for name, v in card_info["fields"].items()}
    raw = fields.get(config.FIELD_BAKSIDA, "")

    # De flesta kort är ännu inte migrerade till v2 (se CLAUDE.md,
    # "Kortformat v2 — pågående migrering") — baksida.parse() matchar bara
    # v2-formatet och returnerar en tom struktur på gamla kort. Utan denna
    # fallback skulle "current" se tomt ut för alla ~1242 ogranskade kort,
    # och granskaren (Fas 2) skulle inte se det befintliga innehållet som
    # referens. Upptäckt 2026-08-04 innan nästa granskningsomgång startade.
    parsed = baksida.parse(raw)
    is_v2 = bool(parsed["huvudbetydelse"] or parsed["synonymer"] or parsed["exempelmening"])
    if not is_v2:
        parsed = baksida.parse_legacy(raw)

    note_id = card_info["note"]
    return {
        "noteId": note_id,
        "flagLabel": flag_label,
        "ord": fields.get(config.FIELD_ORD, ""),
        "current": parsed,  # v2: huvudbetydelse/register/synonymer/exempelmening/bild_html.
                             # legacy (de flesta kort ännu): synonymer/definitioner/exempelmening/bild_html.
        "current_format": "v2" if is_v2 else "legacy",
        "tags": tags_by_note.get(note_id, []),
        "proposed": None,  # fylls i under granskningen i Fas 2: v2-formen (se baksida.build)
        "approved": False,
    }


def build_tags_by_note(cards_info):
    note_ids = list({c["note"] for c in cards_info})
    if not note_ids:
        return {}
    notes_info = invoke("notesInfo", notes=note_ids)
    return {n["noteId"]: n.get("tags", []) for n in notes_info}


def write_session(queue, name_suffix=""):
    if not queue:
        return None
    today = datetime.date.today().isoformat()
    sessions_dir = os.path.join(os.path.dirname(__file__), "sessions")
    os.makedirs(sessions_dir, exist_ok=True)
    out_path = os.path.join(sessions_dir, f"session_{today}{name_suffix}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)
    return out_path
