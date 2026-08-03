"""Engångsverktyg: sök blåa kort efter kända, återkommande felaktiga
synonymer (Adam har identifierat mönstret manuellt, definitionerna stämmer
alltid men vissa synonymer är fel). Läsande sökning, ändrar inget.
"""

import sys

import config
from ankiconnect import invoke

SUSPECT_SYNONYMS = ["allsmäktig", "alrådande", "allrådande"]


def main():
    terms = sys.argv[1:] if len(sys.argv) > 1 else SUSPECT_SYNONYMS
    total_ids = set()
    for term in terms:
        query = f'deck:"{config.DECK_NAME}" flag:{config.FLAG_BLA} "{term}"'
        card_ids = invoke("findCards", query=query)
        print(f'"{term}" -> {len(card_ids)} blåa kort')
        total_ids.update(card_ids)

    print(f"\nTotalt unika blåa kort med minst en misstänkt synonym: {len(total_ids)}")


if __name__ == "__main__":
    main()
