"""
Anki-Svenska: Kontrollera och uppdatera Anki-kort mot Svenska.se

Kräver:
  - Anki öppet med AnkiConnect-tillägget (addon 2055492159)
  - pip install -r requirements.txt
  - playwright install chromium
  - Ollama igång med: ollama pull llama3.2

Kommandon:
  python main.py --list-decks
  python main.py --deck "McHP Anki" --batch 20 --dry-run
  python main.py --deck "McHP Anki" --batch 20
  python main.py --deck "McHP Anki" --update --batch 10 --dry-run
  python main.py --deck "McHP Anki" --update
"""

import argparse
import json
import sys
from pathlib import Path

from bs4 import BeautifulSoup

try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False
    def tqdm(it, **kwargs):
        print(f"{kwargs.get('desc', '')} ({kwargs.get('total', '?')} kort)...")
        return it

import anki_connect
import svenska_scraper as scraper_mod
import comparator
import synonymer_scraper
import updater

SWE_TAGS = ["swe_ok", "swe_mismatch", "swe_not_found", "swe_unclear", "swe_updated"]


def _strip_html(html: str) -> str:
    return BeautifulSoup(html, "html.parser").get_text(strip=True)


def get_front_word(note: dict) -> str:
    fields = note.get("fields", {})
    for name in ("Framsida", "Front", "Word", "Ord", "Fråga"):
        if name in fields:
            return _strip_html(fields[name]["value"])
    if fields:
        return _strip_html(next(iter(fields.values()))["value"])
    return ""


def get_back_html(note: dict) -> str:
    fields = note.get("fields", {})
    for name in ("Baksida", "Back", "Definition", "Förklaring", "Svar"):
        if name in fields:
            return fields[name]["value"]
    vals = list(fields.values())
    return vals[1]["value"] if len(vals) > 1 else ""


def get_back_field_name(note: dict) -> str:
    fields = note.get("fields", {})
    for name in ("Baksida", "Back", "Definition", "Förklaring", "Svar"):
        if name in fields:
            return name
    vals = list(fields.keys())
    return vals[1] if len(vals) > 1 else ""


def fetch_notes_in_batches(note_ids: list[int]) -> list[dict]:
    notes = []
    for i in range(0, len(note_ids), 100):
        notes.extend(anki_connect.get_notes_info(note_ids[i:i + 100]))
    return notes


def main():
    parser = argparse.ArgumentParser(
        description="Kontrollera och uppdatera Anki-kort mot Svenska.se",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--deck", "-d", help="Namn på Anki-deck")
    parser.add_argument("--update", action="store_true",
        help="Uppdatera kortens innehåll med AI (kräver Ollama)")
    parser.add_argument("--threshold", "-t", type=float, default=0.25,
        help="Likhetströskel 0–1 (standard: 0.25)")
    parser.add_argument("--dry-run", action="store_true",
        help="Visa vad som SKULLE göras, ändra ingenting i Anki")
    parser.add_argument("--batch", "-b", type=int, default=0,
        help="Bearbeta max N kort (0 = alla)")
    parser.add_argument("--no-skip", action="store_true",
        help="Bearbeta alla kort, även redan taggade/uppdaterade")
    parser.add_argument("--list-decks", action="store_true",
        help="Visa alla deck-namn och avsluta")
    parser.add_argument("--show-fields", action="store_true",
        help="Visa fältnamn för de 3 första korten (felsökning)")
    args = parser.parse_args()

    # --- Anslut till Anki ---
    print("Ansluter till Anki...")
    if not anki_connect.ping():
        print("\nFEL: Kan inte ansluta till Anki.")
        print("  1. Öppna Anki")
        print("  2. Installera AnkiConnect (addon: 2055492159)")
        sys.exit(1)
    print("  Ansluten!")

    if args.list_decks:
        for d in sorted(anki_connect.get_deck_names()):
            print(f"  • {d}")
        sys.exit(0)

    if not args.deck:
        parser.error("Ange --deck eller --list-decks")

    # --- Kolla Ollama om --update ---
    if args.update:
        print("Kontrollerar Ollama...")
        try:
            updater.check_ollama()
            print("  Ollama OK!")
        except RuntimeError as e:
            print(f"\nFEL: {e}")
            sys.exit(1)

    # --- Hämta kort ---
    print(f"\nSöker kort i: {args.deck}")
    note_ids = anki_connect.find_notes(args.deck)
    if not note_ids:
        print("Inga kort hittades. Kolla deckets namn med --list-decks")
        sys.exit(1)
    print(f"  {len(note_ids)} kort hittade")

    print(f"  Hämtar kortinnehåll...")
    notes = fetch_notes_in_batches(note_ids)

    if args.show_fields:
        for note in notes[:3]:
            word = get_front_word(note)
            back = _strip_html(get_back_html(note))[:100]
            print(f"\n  Fält: {list(note['fields'].keys())}")
            print(f"  Framsida: {word!r}")
            print(f"  Baksida:  {back!r}")
        sys.exit(0)

    # --- Filtrera taggade ---
    # Vid uppdatering: hoppa över swe_ok (verifierade) och swe_updated (redan uppdaterade)
    # Vid taggning: hoppa över alla swe_*-taggar
    skip_tags = SWE_TAGS if not args.update else ["swe_ok", "swe_updated"]
    if not args.no_skip:
        before = len(notes)
        notes = [n for n in notes if not any(t in n.get("tags", []) for t in skip_tags)]
        if before - len(notes):
            print(f"  Hoppar över {before - len(notes)} redan bearbetade kort")

    if args.batch > 0:
        notes = notes[: args.batch]

    if not notes:
        print("Inga kort kvar att bearbeta.")
        sys.exit(0)

    mode = "UPPDATERAR med AI" if args.update else "KONTROLLERAR"
    print(f"\n{mode}: {len(notes)} kort")
    if args.dry_run:
        print("  [DRY RUN — ingenting sparas i Anki]")

    # =========================================================
    # LÄGE 1: --update  →  skriv om korten med AI
    # =========================================================
    if args.update:
        stats = {"updated": 0, "not_found": 0, "error": 0}
        results_log = []

        iterator = tqdm(notes, desc="Uppdaterar", total=len(notes)) if HAS_TQDM \
                   else tqdm(notes, total=len(notes), desc="Uppdaterar")

        with scraper_mod.SvenskaScraper() as svenska:
            try:
                for i, note in enumerate(iterator):
                    note_id = note["noteId"]
                    word = get_front_word(note)
                    old_back = get_back_html(note)
                    back_field = get_back_field_name(note)

                    if not word or not back_field:
                        stats["error"] += 1
                        continue

                    try:
                        sv_result = svenska.search(word)

                        if not sv_result.get("found"):
                            stats["not_found"] += 1
                            results_log.append({"word": word, "verdict": "not_found"})
                            if not args.dry_run:
                                anki_connect.remove_tags([note_id], " ".join(SWE_TAGS))
                                anki_connect.add_tags([note_id], "swe_not_found")
                            continue

                        syn_text = synonymer_scraper.fetch_synonymer(word)
                        data = updater.extract_card_content(
                            word, sv_result["text"], syn_text
                        )
                        new_back = updater.build_card_back(word, data)

                        # Visa förhandsgranskning för de 3 första korten
                        if i < 3 or args.dry_run:
                            updater.preview_card(word, old_back, new_back)

                        if not args.dry_run:
                            anki_connect.update_note_fields(
                                note_id, {back_field: new_back}
                            )
                            anki_connect.remove_tags([note_id], " ".join(SWE_TAGS))
                            anki_connect.add_tags([note_id], "swe_updated")

                        stats["updated"] += 1
                        results_log.append({"word": word, "verdict": "updated", "new_back": new_back})

                    except Exception as e:
                        msg = f"Fel för '{word[:25]}': {e}"
                        tqdm.write(f"  {msg}") if HAS_TQDM else print(f"  {msg}")
                        stats["error"] += 1

            except KeyboardInterrupt:
                print("\nAvbruten. Sparar cache...")

        print(f"\n{'='*40}")
        print(f"  Uppdaterade:  {stats['updated']}")
        print(f"  Ej hittade:   {stats['not_found']}")
        print(f"  Fel:          {stats['error']}")

    # =========================================================
    # LÄGE 2: bara taggning (utan --update)
    # =========================================================
    else:
        stats = {"ok": 0, "mismatch": 0, "not_found": 0, "unclear": 0, "error": 0}
        results_log = []

        iterator = tqdm(notes, desc="Kontrollerar", total=len(notes)) if HAS_TQDM \
                   else tqdm(notes, total=len(notes), desc="Kontrollerar")

        with scraper_mod.SvenskaScraper() as svenska:
            try:
                for note in iterator:
                    note_id = note["noteId"]
                    word = get_front_word(note)
                    back_html = get_back_html(note)

                    if not word:
                        stats["error"] += 1
                        continue

                    try:
                        sv_result = svenska.search(word)

                        # Hämta synonymer.se som extra källa
                        syn_text = synonymer_scraper.fetch_synonymer(word)

                        result = comparator.compare(
                            back_html, sv_result, args.threshold,
                            synonymer_text=syn_text,
                        )
                        tag = result["tag"]
                        stats[tag.replace("swe_", "")] = stats.get(tag.replace("swe_", ""), 0) + 1

                        results_log.append({
                            "note_id": note_id, "word": word,
                            "verdict": result["verdict"], "score": result["score"],
                            "tag": tag,
                        })

                        if not args.dry_run:
                            anki_connect.remove_tags([note_id], " ".join(SWE_TAGS))
                            anki_connect.add_tags([note_id], tag)

                    except Exception as e:
                        msg = f"Fel för '{word[:25]}': {e}"
                        tqdm.write(f"  {msg}") if HAS_TQDM else print(f"  {msg}")
                        stats["error"] += 1

            except KeyboardInterrupt:
                print("\nAvbruten. Sparar cache...")

        print(f"\n{'='*40}")
        print(f"  Korrekt     (swe_ok):        {stats.get('ok', 0):>5}")
        print(f"  Mismatch    (swe_mismatch):  {stats.get('mismatch', 0):>5}")
        print(f"  Ej hittat   (swe_not_found): {stats.get('not_found', 0):>5}")
        print(f"  Oklart      (swe_unclear):   {stats.get('unclear', 0):>5}")
        print(f"  Fel:                         {stats.get('error', 0):>5}")

    synonymer_scraper.flush_cache()
    Path("results.json").write_text(
        json.dumps(results_log, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\nResultat sparade i results.json")
    if args.dry_run:
        print("[Kör utan --dry-run för att spara till Anki]")


if __name__ == "__main__":
    main()
