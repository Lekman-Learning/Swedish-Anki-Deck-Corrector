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

    confidence = entry.get("confidence")
    if confidence is None or confidence <= 7:
        return False, "hoppade över (konfidens saknas eller <=7 — inte redo, se style_guide.md)"

    current = entry["current"]
    register = proposed.get("register", current.get("register"))
    warnings = baksida.validate_register(register)
    if warnings:
        return False, f"hoppade över (ogiltig register-tagg: {'; '.join(warnings)})"

    new_baksida = baksida.build(
        huvudbetydelse=proposed.get("huvudbetydelse", current.get("huvudbetydelse", "")),
        synonymer=proposed.get("synonymer", current["synonymer"]),
        exempelmening=proposed.get("exempelmening", current["exempelmening"]),
        register=register,
        # bild_html sätts explicit i proposed (av images.py/Fas 2) om Adam
        # godkänt en ny/ändrad bild, annars rörs den befintliga bilden aldrig
        bild_html=proposed.get("bild_html", current["bild_html"]),
        synonym_groups=proposed.get("synonym_groups"),
    )

    fields = {config.FIELD_BAKSIDA: new_baksida}
    proposed_ord = entry.get("proposed_ord")
    if proposed_ord and proposed_ord != entry["ord"]:
        # Framsidan kan också vara fel (felstavning, saknat "sig" osv), se
        # style_guide.md "Framsidan kan också vara fel" — rättas bara om
        # proposed_ord explicit satts under granskningen.
        fields[config.FIELD_ORD] = proposed_ord

    invoke("updateNoteFields", note={"id": note_id, "fields": fields})

    today = datetime.date.today().isoformat()

    # Tar bort ev. tidigare granskad::/konfidens::-taggar innan nya läggs
    # till, annars kan ett kort som granskas om (t.ex. vid v2-migreringen)
    # sluta med motsägelsefulla taggar, typ konfidens::10 OCH konfidens::9
    # samtidigt (upptäckt 2026-08-04 under pilottest av 5 migrerade kort).
    old_tags = [
        t for t in entry.get("tags", [])
        if t.startswith(f"{config.REVIEWED_TAG_PREFIX}::") or t.startswith("konfidens::")
    ]
    if old_tags:
        invoke("removeTags", notes=[note_id], tags=" ".join(old_tags))

    # Flaggkoppling beslutad 2026-08-04 (style_guide.md): 9-10 -> Blå,
    # <=8 -> Grön. <=7 hanteras redan ovan (skippas helt, inte redo).
    flag = config.FLAG_BLA if confidence >= 9 else config.FLAG_GRON
    tags_to_add = f"{config.REVIEWED_TAG_PREFIX}::{today} konfidens::{confidence} {config.FORMAT_TAG_V2}"
    extra_tags = entry.get("extra_tags")
    if extra_tags:
        tags_to_add += " " + " ".join(extra_tags)
    invoke("addTags", notes=[note_id], tags=tags_to_add)

    try:
        card_ids = invoke("findCards", query=f"nid:{note_id}")
        for card_id in card_ids:
            invoke(
                "setSpecificValueOfCard",
                card=card_id,
                keys=["flags"],
                newValues=[flag],
                warning_check=True,
            )
    except AnkiConnectError as exc:
        return True, f"fält+tagg uppdaterat, men flaggan kunde INTE sättas automatiskt ({exc}) — sätt manuellt"

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
