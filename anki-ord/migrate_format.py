"""Engångsmigrering: de 724 kort som redan granskats i det GAMLA formatet
(<ol><li>-definitioner, ingen register-tagg) ska om till Kortformat v2
(Huvudbetydelse fet stil + valfri register-rad), se style_guide.md.

Detta är INTE en blind auto-konvertering. Att slå ihop flera
ordboksliknande <li>-definitioner till en kort, koncis Huvudbetydelse-fras
och att avgöra register kräver samma typ av manuellt omdöme som resten av
granskningsprojektet — bara mekanisk HTML-omstrukturering kan automatiseras
säkert. Detta skript gör bara det mekaniska: hämtar de granskade korten,
parsar det gamla formatet, och skriver ett DRAFT-förslag (huvudbetydelse =
definitionerna hopslagna med " ; " — det är skilda ordboksbetydelser, se
style_guide.md "Separatorer", ändrat 2026-08-05, oförändrat annars) till en sessionsfil
för samma Fas 2/Fas 3-granskningsflöde som redan används
(apply_updates.py). Kort vars definitioner är långa/ordboksartade flaggas
`needs_condensing` — dessa MÅSTE skrivas om för hand till en kort fras,
inte bara joinas rakt av.

Skriver sessions/session_<datum>_migration-format.json (samma
namnmönster/write_session som övriga fetch_*.py-skript).
"""

import argparse

import baksida
import config
from queue_lib import build_tags_by_note, fetch_cards_sorted_by_due, write_session

CONDENSE_WORD_THRESHOLD = 8  # fler ord än detta i en <li> = troligen ordboksstil, inte Adam-tal-fras


def fetch_migrated_cards_sorted():
    """Samma due-sortering som fetch_queue.py/fetch_urgent.py: kort med
    lägst due (schemalagda snarast, dvs Adam ser dem idag/imorgon) kommer
    FÖRST — Adam vill granska/rätta dem han faktiskt möter snart innan
    kort som ligger långt fram. Dedupear på noteId (behåller tidigast due
    om ett kort mot förmodan har flera cards)."""
    query = f'deck:"{config.DECK_NAME}" tag:{config.REVIEWED_TAG_PREFIX}::*'
    cards_info = fetch_cards_sorted_by_due(query, limit=100_000)
    seen_notes = set()
    deduped = []
    for card in cards_info:
        note_id = card["note"]
        if note_id in seen_notes:
            continue
        seen_notes.add(note_id)
        deduped.append(card)
    return deduped, build_tags_by_note(cards_info)


def to_migration_entry(card_info, tags_by_note):
    fields = {name: v["value"] for name, v in card_info["fields"].items()}
    note_id = card_info["note"]
    legacy = baksida.parse_legacy(fields.get(config.FIELD_BAKSIDA, ""))

    definitioner = legacy["definitioner"]
    draft_huvudbetydelse = " ; ".join(definitioner)
    needs_condensing = any(len(d.split()) > CONDENSE_WORD_THRESHOLD for d in definitioner)

    return {
        "noteId": note_id,
        "due": card_info["due"],
        "flagLabel": "migrering-724",
        "ord": fields.get(config.FIELD_ORD, ""),
        "current": legacy,  # gamla formatet, oförändrat — samma nyckel "current" som apply_updates.py förväntar sig
        "needs_condensing": needs_condensing,
        "proposed": {
            "huvudbetydelse": draft_huvudbetydelse,  # DRAFT — kondensera för hand om needs_condensing
            "register": None,  # DRAFT-platshållare — obligatoriskt i slutversionen (style_guide.md,
                                # beslutat 2026-08-04), måste sättas till minst en tagg vid granskning,
                                # inte lämnas null
            "synonymer": legacy["synonymer"],  # redan granskade — rör INTE synonymerna, bara struktur/register
            "synonym_groups": legacy["synonym_groups"],
            "exempelmening": legacy["exempelmening"],
            "bild_html": legacy["bild_html"],
        },
        "tags": tags_by_note.get(note_id, []),
        "approved": False,  # sätts av granskaren, kräver även confidence >=8 för att apply_updates.py ska köra
        "confidence": None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    cards, tags_by_note = fetch_migrated_cards_sorted()
    if not cards:
        print("Inga granskade kort hittades (tag granskad::*) — inget att migrera.")
        return

    queue = [to_migration_entry(c, tags_by_note) for c in cards]
    needs_condensing_count = sum(1 for e in queue if e["needs_condensing"])

    out_path = write_session(queue, name_suffix="_migration-format")
    print(
        f"Skrev {len(queue)} kort till {out_path} "
        f"({needs_condensing_count} flaggade needs_condensing — kräver manuell kondensering, "
        f"resten kan troligen godkännas med draft-huvudbetydelsen oförändrad)."
    )


if __name__ == "__main__":
    main()
