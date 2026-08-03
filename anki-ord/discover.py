"""Fas 0 — engångskörning för att bekräfta deck-namn, fältnamn och
flagg-mappning mot en riktig, öppen Anki-instans. Redan körd och bekräftad
för Adams deck 2026-08-03 (se config.py). Kör igen om decket/mallen ändras.
"""

import baksida
import config
from ankiconnect import invoke


def main():
    version = invoke("version")
    print(f"AnkiConnect version: {version}\n")

    fields = invoke("modelFieldNames", modelName=config.MODEL_NAME)
    print(f"Fält i {config.MODEL_NAME}: {fields}\n")

    print("Kort per flagga i decket:")
    for flag in range(0, 8):
        card_ids = invoke(
            "findCards", query=f'deck:"{config.DECK_NAME}" flag:{flag}'
        )
        print(f"  flag:{flag} -> {len(card_ids)} kort")

    print("\nExempel-parsning av ett rött kort:")
    red_notes = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" flag:{config.FLAG_ROD}')
    if red_notes:
        info = invoke("notesInfo", notes=red_notes[:1])[0]
        raw = info["fields"][config.FIELD_BAKSIDA]["value"]
        print(f"  Ord: {info['fields'][config.FIELD_ORD]['value']}")
        print(f"  Parsed: {baksida.parse(raw)}")


if __name__ == "__main__":
    main()
