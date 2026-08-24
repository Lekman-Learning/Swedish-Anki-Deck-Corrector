"""Applicerar GODKÄNDA Wikipedia/Commons-bildkandidater (byggda av
wikipedia_bild_batch.py, granskade för hand) till riktiga Anki-kort.

Samma säkerhetsmönster som apply_updates.py: skriver bara kort med
`godkand: true`, kastar aldrig hela batchen på ett enskilt fel. Läser ALLTID
`bild_html` från kortets LIVE Baksida-fält direkt innan skrivning och
vägrar skriva om något redan finns där -- inte bara vid frågetillfället i
batch-scriptet (kortet kan ha fått en bild manuellt mellan de två stegen).
Det är samma "hårda regel" Adam gav uttryckligen: rör aldrig ett kort som
redan har bild.

Varje sparad bild loggas i sin helhet (ord, noteId, källa, käll-URL, licens)
till `bild_kallor.jsonl` -- samma logg-per-rad-format som
`sokkoll_kallor.jsonl` använder för sökkoll-källor, så bildkällor är lika
spårbara i efterhand.
"""

import argparse
import datetime
import json
import os

import baksida
import config
import images
import wikipedia_bild as wb
from ankiconnect import invoke, AnkiConnectError

BILD_KALLOR_LOG = os.path.join(os.path.dirname(__file__), "bild_kallor.jsonl")


def _logga_kalla(rad):
    with open(BILD_KALLOR_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(rad, ensure_ascii=False) + "\n")


def apply_single(entry, torr=False):
    note_id = entry["noteId"]
    ord_ = entry["ord"]
    kandidat = entry.get("kandidat")

    if not entry.get("godkand"):
        return False, "hoppade över (ej godkänd av granskaren)"
    if not kandidat:
        return False, "hoppade över (godkand=true men ingen kandidat -- inkonsekvent post)"

    # HÅRD REGEL (Adams krav 2026-08-19): läs LIVE-innehållet, inte det som
    # låg i sessionsfilen när batchen byggdes -- kortet kan ha ändrats sedan
    # dess. Rör aldrig ett kort som redan har bild.
    live = invoke("notesInfo", notes=[note_id])
    if not live:
        return False, "hoppade över (noteId hittades inte i Anki)"
    live_baksida = live[0]["fields"].get(config.FIELD_BAKSIDA, {}).get("value", "")
    parsed = baksida.parse(live_baksida)
    if parsed["bild_html"]:
        return False, "hoppade över (kortet har redan fått en bild sedan batchen byggdes)"

    if torr:
        return True, f"(torrkörning) skulle hämta {kandidat['bild_url']}"

    try:
        b64, content_type = wb.hamta_bilddata_base64(kandidat["bild_url"])
    except Exception as exc:
        return False, f"hoppade över (kunde inte ladda ner bilden: {exc})"

    filnamn = wb.filnamn_for(ord_, kandidat["bild_url"], content_type)
    try:
        stored_name = images.store_new(filnamn, b64)
    except AnkiConnectError as exc:
        return False, f"hoppade över (kunde inte spara till Anki-media: {exc})"

    ny_bild_html = images.img_tag(stored_name)
    ny_baksida = baksida.build(
        huvudbetydelse=parsed["huvudbetydelse"],
        synonymer=parsed["synonymer"],
        synonym_groups=parsed["synonym_groups"],
        exempelmening=parsed["exempelmening"],
        register=parsed["register"],
        etymologi=parsed["etymologi"],
        bild_html=ny_bild_html,
    )
    invoke("updateNoteFields", note={"id": note_id, "fields": {config.FIELD_BAKSIDA: ny_baksida}})

    _logga_kalla({
        "datum": datetime.date.today().isoformat(),
        "noteId": note_id,
        "ord": ord_,
        "kalla_typ": kandidat["kalla_typ"],
        "titel": kandidat.get("titel"),
        "bild_url": kandidat["bild_url"],
        "sidurl": kandidat.get("sidurl"),
        "licens": kandidat.get("licens"),
        "sparad_som": stored_name,
        "motivering": entry.get("motivering"),
    })

    entry["applicerad"] = True
    return True, f"klart ({stored_name})"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("session_file")
    parser.add_argument("--torr", action="store_true", help="visa vad som skulle hända, skriv inget")
    args = parser.parse_args()

    with open(args.session_file, "r", encoding="utf-8") as f:
        queue = json.load(f)

    for entry in queue:
        ok, message = apply_single(entry, torr=args.torr)
        status = "OK" if ok else "SKIP"
        print(f"[{status}] {entry['ord']}: {message}")

    if not args.torr:
        with open(args.session_file, "w", encoding="utf-8") as f:
            json.dump(queue, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
