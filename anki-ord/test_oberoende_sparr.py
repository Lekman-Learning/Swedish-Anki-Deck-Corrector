# -*- coding: utf-8 -*-
"""Verifierar oberoendespärren i kortgranskare.verdikt().

Spärren finns av samma skäl som källspärren: `oberoende_verifierad` vilade
annars på granskarens ord. `sokverifierad` gjorde det, och satt på 177 kort
som aldrig sökkollats.

Kör mot en TEMPORÄR paketfil med ett påhittat noteId -- inget rör Anki,
eftersom varje fall ska AVBRYTA innan addTags nås.
"""
import json
import os
import tempfile

import kortgranskare as kg

FALL = [
    ("granskare saknas helt", {"skriven_av": "A", "granskare": None}, None),
    ("granskaren skrev korten själv", {"skriven_av": "A", "granskare": "A"}, None),
    ("samma namn, annan skiftlägesform", {"skriven_av": "Claude"}, "  claude "),
    ("underkänt utan anmärkning", {"skriven_av": "A", "granskare": "B"}, None),
]


def bygg(meta, verdikt_, anmarkning):
    d = dict(meta)
    d["instruktion"] = "test"
    d["poster"] = [{"noteId": -1, "ord": "testord", "facit": None,
                    "facit_signal": None, "kort": {},
                    "verdikt": verdikt_, "anmarkning": anmarkning}]
    f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                    encoding="utf-8")
    json.dump(d, f, ensure_ascii=False)
    f.close()
    return f.name


def main():
    logg = os.path.join(os.path.dirname(os.path.abspath(__file__)), kg.OBEROENDE_LOGG)
    fore = os.path.getsize(logg) if os.path.exists(logg) else 0

    for i, (namn, meta, arg) in enumerate(FALL):
        # Sista fallet ska passera oberoendekontrollen men falla på anmärkningen.
        underkant = namn.startswith("underkänt")
        sokvag = bygg(meta, "underkand" if underkant else "godkand", None)
        print(f"\n--- {namn}")
        try:
            kg.verdikt(sokvag, arg)
        finally:
            os.unlink(sokvag)

    efter = os.path.getsize(logg) if os.path.exists(logg) else 0
    print(f"\nLoggen växte: {efter - fore} byte (ska vara 0 -- inget fall "
          f"fick tagga något)")


if __name__ == "__main__":
    main()
