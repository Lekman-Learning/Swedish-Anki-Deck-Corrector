"""Fas 3 — skriver godkända ändringar från en sessionsfil tillbaka till Anki:
uppdaterar Baksida-fältet (via baksida.build, bevarar ev. bild oförändrad),
flyttar kortets flagga till blå, taggar granskad::datum.

Körs antingen kort-för-kort under passet (apply_single, anropad från
granskningsflödet i Fas 2) eller batchat i slutet via main().

OBS: setSpecificValueOfCard för att sätta flaggan kräver en tillräckligt ny
AnkiConnect-version. Verifierad tillgänglig i Adams installation 2026-08-03.
"""

import argparse
import datetime
import json

import baksida
import config
from ankiconnect import invoke, AnkiConnectError


def apply_single(entry):
    note_id = entry["noteId"]
    proposed = entry["proposed"]
    if not entry.get("approved") or not proposed:
        return False, "hoppade över (ej godkänt)"

    current = entry["current"]
    new_baksida = baksida.build(
        synonymer=proposed.get("synonymer", current["synonymer"]),
        definitioner=proposed.get("definitioner", current["definitioner"]),
        exempelmening=proposed.get("exempelmening", current["exempelmening"]),
        # bild_html sätts explicit i proposed (av images.py/Fas 2) om Adam
        # godkänt en ny/ändrad bild, annars rörs den befintliga bilden aldrig
        bild_html=proposed.get("bild_html", current["bild_html"]),
        synonym_groups=proposed.get("synonym_groups"),
    )
    invoke(
        "updateNoteFields",
        note={"id": note_id, "fields": {config.FIELD_BAKSIDA: new_baksida}},
    )

    today = datetime.date.today().isoformat()
    invoke("addTags", notes=[note_id], tags=f"{config.REVIEWED_TAG_PREFIX}::{today}")

    try:
        card_ids = invoke("findCards", query=f"nid:{note_id}")
        for card_id in card_ids:
            invoke(
                "setSpecificValueOfCard",
                card=card_id,
                keys=["flags"],
                newValues=[config.FLAG_BLA],
                warning_check=True,
            )
    except AnkiConnectError as exc:
        return True, f"fält+tagg uppdaterat, men flaggan kunde INTE sättas automatiskt ({exc}) — sätt till blå manuellt"

    return True, "klart"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("session_file", help="sökväg till sessions/session_<datum>.json")
    args = parser.parse_args()

    with open(args.session_file, "r", encoding="utf-8") as f:
        queue = json.load(f)

    for entry in queue:
        ok, message = apply_single(entry)
        status = "OK" if ok else "SKIP"
        print(f"[{status}] {entry['ord']}: {message}")

    with open(args.session_file, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
