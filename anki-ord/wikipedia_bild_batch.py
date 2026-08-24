"""Retroaktivt batch-script (Adams beslut 2026-08-19): hämtar KANDIDATBILDER
(inte applicerade bilder) från Wikipedia/Commons för kort som redan är
v3-klara (`tag:granskad::*` ELLER `tag:v3_granskad::*`) men saknar bild.

Bygger bara en KÖ, samma tvåstegsmönster som resten av projektet
(fetch_*.py bygger, apply_*.py skriver) -- se `wikipedia_bild_apply.py` för
steget som faktiskt sparar en bild till Anki. Anledningen till att detta
INTE är ett enda script: `wikipedia_bild.hamta_kandidat()` returnerar bara
vad som finns, aldrig en bedömning av om bilden faktiskt matchar ordets
relevanta betydelse (se den modulens docstring och det experiment som
motiverar det: "övertyga" gav Wikipedia-artikeln "Retorik", "bottna i" gav
en bild av den svenska orten Bottna -- båda tekniskt "träffar", båda fel).
Den bedömningen görs av en granskare (Claude, med Adams uttryckliga mandat
2026-08-19) som läser `extract`/`beskrivning` mot kortets Huvudbetydelse
INNAN något appliceras.

Körs i litet, kontrollerbart format -- samma "validera i litet format"-
kultur som snabbkoll2.py/fetch_queue.py (`--batch-size`, default litet här
eftersom varje kort kostar ett nätverksanrop och Adam ska hinna granska
kvaliteten innan en full körning).
"""

import argparse
import datetime
import json
import os

import baksida
import config
import wikipedia_bild as wb
from ankiconnect import invoke

DEFAULT_BATCH_SIZE = 20  # litet med flit -- se docstring ovan


def hamta_bildlosa_v3_kort(limit, offset=0):
    """v3-klara kort (granskad::* ELLER v3_granskad::*) som saknar bild i
    Baksida. Sorterat på due (lägst först) -- samma prioritering som
    fetch_queue.py, kort Adam ser snarast granskas/kompletteras först.
    `offset` låter en senare körning hoppa förbi redan behandlade kort utan
    att behöva ett separat exkluderingsfilter."""
    query = (
        f'deck:"{config.DECK_NAME}" '
        f'(tag:{config.REVIEWED_TAG_PREFIX}::* OR tag:{config.V3_TAG_PREFIX}::*)'
    )
    card_ids = invoke("findCards", query=query)
    if not card_ids:
        return []
    cards_info = invoke("cardsInfo", cards=card_ids)
    cards_info.sort(key=lambda c: c["due"])

    resultat = []
    for c in cards_info:
        fields = {name: v["value"] for name, v in c["fields"].items()}
        raw = fields.get(config.FIELD_BAKSIDA, "")
        parsed = baksida.parse(raw)
        if parsed["bild_html"]:
            continue  # hård regel: rör aldrig kort som redan har bild
        resultat.append((c, fields, parsed))
        if len(resultat) >= offset + limit:
            break
    return resultat[offset:offset + limit]


def bygg_kandidatko(batch_size, offset=0):
    kort = hamta_bildlosa_v3_kort(batch_size, offset=offset)
    entries = []
    hittade, ej_hittade = 0, 0
    for card_info, fields, parsed in kort:
        ord_ = fields.get(config.FIELD_ORD, "")
        kandidat = None
        fel = None
        try:
            kandidat = wb.hamta_kandidat(ord_)
        except Exception as exc:
            fel = str(exc)
        if kandidat:
            hittade += 1
        else:
            ej_hittade += 1
        entries.append({
            "noteId": card_info["note"],
            "ord": ord_,
            "huvudbetydelse": parsed["huvudbetydelse"],
            "kandidat": kandidat,
            "hamtningsfel": fel,
            # Fylls i av granskaren (Claude/Adam) EFTER manuell jämförelse
            # av kandidat mot huvudbetydelse -- se modulens docstring.
            # Aldrig auto-godkänt av detta script.
            "godkand": None,
            "motivering": None,
            "applicerad": False,
        })
    return entries, hittade, ej_hittade


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--offset", type=int, default=0,
                         help="hoppa förbi de N först due-sorterade bildlösa v3-korten")
    args = parser.parse_args()

    entries, hittade, ej_hittade = bygg_kandidatko(args.batch_size, offset=args.offset)

    today = datetime.date.today().isoformat()
    sessions_dir = os.path.join(os.path.dirname(__file__), "sessions")
    os.makedirs(sessions_dir, exist_ok=True)
    out_path = os.path.join(sessions_dir, f"session_{today}_wikipedia-bilder.json")
    n = 2
    while os.path.exists(out_path):
        out_path = os.path.join(sessions_dir, f"session_{today}_wikipedia-bilder-batch{n}.json")
        n += 1
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"Skrev {len(entries)} kort till {out_path}")
    print(f"Kandidat hittad: {hittade}")
    print(f"Ingen kandidat (förväntat för abstrakta ord/verb/idiom): {ej_hittade}")
    print("Granska varje kandidat mot huvudbetydelse innan wikipedia_bild_apply.py körs.")


if __name__ == "__main__":
    main()
