"""Snabbkoll 2.0 på HELA den kvarvarande suspenderade Blå Nya-poolen
(2026-08-07) -- ersätter snabbkoll2_blanya.py, som bara matchade redan
v2-formaterade flag:4-kort. Denna version breddar queryn till alla
suspenderade is:new-kort oavsett flagga/format, eftersom testbatcharna
2026-08-07 visade att stora delar av den kvarvarande poolen fortfarande
ligger i det gamla <ol><li>-formatet, aldrig migrerat till v2.

Samma bygglogik som snabbkoll2.py/snabbkoll2_gamla.py (OLD-decket som
facit + egen kunskap, sökkoll bara vid eskalering i --mode snabbkoll2;
riktig sökkoll på varje kort i --mode sokkoll -- själva applicerings-
lägesskillnaden hanteras av apply_flerbetydelse.py, inte här).

Nytt jämfört med tidigare poolbyggare: "format_bug_hints" per kort --
mjuka varningsflaggor (inte auto-fixar) baserat på buggmönster som
hittades i testbatcharna: engelska textläckor, fabricerade
tredjedefinitioner och nästan-dubblettdefinitioner kräver fortfarande
manuell läsning, men "exempel_saknar_ordet"/"tom_exempelmening"/
"mojlig_dubblett"/"legacy_format" kan flaggas mekaniskt för att styra
var granskaren (jag) lägger extra uppmärksamhet.
"""

import argparse
import datetime
import json
import os
import re

import baksida
import config
from ankiconnect import invoke
from queue_lib import build_tags_by_note, fetch_cards_sorted_by_due
from snabbkoll2 import build_old_lookup


def find_bla_nya_cards(limit):
    query = (
        f'deck:"{config.DECK_NAME}" is:new is:suspended '
        f'-tag:{config.FLERBETYDELSE_TAG_PREFIX}::*'
    )
    return fetch_cards_sorted_by_due(query, limit)


def _strip_html(s):
    if not s:
        return ""
    return re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ").strip()


def compute_format_bug_hints(ord_, current, is_legacy):
    hints = []
    if is_legacy:
        hints.append("legacy_format")

    raw_ex = current.get("exempelmening") or ""
    ex = _strip_html(raw_ex)
    if not ex:
        hints.append("tom_exempelmening")
    else:
        # Substrängkollen missar böjda former ("beslå" -> "beslogs"), så den
        # ger falsklarm snarare än falsknegativ -- den är ett tips, inte en
        # spärr, och får stå kvar som sådan.
        if ord_ and ord_.strip().lower() not in ex.lower():
            hints.append("exempel_saknar_ordet")
        # Den EGENTLIGA regeln (style_guide.md, "Highlight av ordet i
        # exempelmeningen": "Inte valfritt") kontrollerades inte alls
        # tidigare -- ett kort kunde ha ordet i meningen men omarkerat och
        # ändå se rent ut. Se "fantomsmärta", som hittades manuellt.
        if config.SYNONYM_COLOR not in raw_ex:
            hints.append("saknar_highlight")

    if is_legacy:
        defs = current.get("definitioner") or []
        prefixes = [_strip_html(d)[:15].lower() for d in defs if _strip_html(d)]
        if len(prefixes) >= 2 and len(set(prefixes)) < len(prefixes):
            hints.append("mojlig_dubblett")

    return hints


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
    matched, unmatched, legacy_count = 0, 0, 0
    for c in cards:
        fields = {name: v["value"] for name, v in c["fields"].items()}
        raw = fields.get(config.FIELD_BAKSIDA, "")
        ord_ = fields.get(config.FIELD_ORD, "")

        parsed = baksida.parse(raw)
        is_v2 = bool(parsed["huvudbetydelse"] or parsed["synonymer"] or parsed["exempelmening"])
        if is_v2:
            current = parsed
            current_format = "v2"
        else:
            current = baksida.parse_legacy(raw)
            current_format = "legacy"
            legacy_count += 1

        old_match = old_lookup.get(ord_.strip().lower())
        if old_match:
            matched += 1
        else:
            unmatched += 1

        hints = compute_format_bug_hints(ord_, current, current_format == "legacy")

        entries.append({
            "noteId": c["note"],
            "ord": ord_,
            "current": current,
            "current_format": current_format,
            "old_facit": old_match,
            "tags": tags_by_note.get(c["note"], []),
            "format_bug_hints": hints,
            "proposed": None,
            "approved": False,
        })

    today = datetime.date.today().isoformat()
    sessions_dir = os.path.join(os.path.dirname(__file__), "sessions")
    os.makedirs(sessions_dir, exist_ok=True)
    out_path = os.path.join(sessions_dir, f"session_{today}_snabbkoll2-blanya-v2.json")
    n = 2
    while os.path.exists(out_path):
        out_path = os.path.join(sessions_dir, f"session_{today}_snabbkoll2-blanya-v2-batch{n}.json")
        n += 1
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"Skrev {len(entries)} kort till {out_path}")
    print(f"OLD-matchning: {matched} av {len(entries)} ({matched / len(entries):.0%})")
    print(f"Utan OLD-matchning (kollas ändå via egen kunskap / skippas): {unmatched}")
    print(f"Legacy-format (kräver full v2-migrering): {legacy_count}")
    with_hints = sum(1 for e in entries if e["format_bug_hints"])
    print(f"Kort med minst en format_bug_hint: {with_hints}")


if __name__ == "__main__":
    main()
