"""Suspenderar alla ogranskade (icke-kortformat::v2) Blå Nya-kort, så att bara
v2-granskade kort finns kvar i Adams nya-kort-kö. Beslutat 2026-08-05:
"sållningsfilter" istället för att lita på att granskningen hinner före Adams
egen takt — suspend är persistent (till skillnad från Ankis "bury", som
återställs varje dygn), så ett suspenderat kort kan inte nås av misstag.

apply_updates.py avsuspenderar automatiskt varje kort när det granskats
färdigt och taggats kortformat::v2 (se apply_single) — detta skript behöver
alltså bara köras en gång för att lägga grunden, sen sköter granskningsflödet
resten. Säkert att köra om (suspend är idempotent, rör inte redan
suspenderade eller redan v2-taggade kort).
"""

import config
from ankiconnect import invoke

QUERY = f'deck:"{config.DECK_NAME}" is:new -tag:{config.FORMAT_TAG_V2}'


def main():
    card_ids = invoke("findCards", query=QUERY)
    if not card_ids:
        print("Inga ogranskade Blå Nya-kort hittade (redan klart eller redan suspenderade).")
        return

    print(f"Hittade {len(card_ids)} ogranskade Blå Nya-kort. Suspenderar...")
    invoke("suspend", cards=card_ids)
    print(f"Klart — {len(card_ids)} kort suspenderade. De släpps in automatiskt "
          f"i takt med att fetch_bla_nya.py -> apply_updates.py granskar dem.")


if __name__ == "__main__":
    main()
