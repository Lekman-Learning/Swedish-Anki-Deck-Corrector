"""Engångsrättning (2026-08-21): Adam pekade på att det ska vara ett
Enter-mellanrum (blankrad, <br><br>) mellan antingen exempelmeningen eller
den etymologiska raden och bilden. `baksida.build()` skriver redan alltid
<br><br> -- kontrollerat mot hela decket, 2 747 av 2 852 bildkort har det
rätt. De återstående 105 är ÄLDRE kort skrivna innan konventionen fanns
(2026-08-07) eller handredigerade i efterhand (samma sorts kort som
`kornett`) -- ingen kod i repot skriver längre den trasiga varianten.

Rör BARA kort med exakt EN bild. Kort med flera bilder (som `kornett`,
Adam rättar den för hand just nu) hoppas över helt -- att röra ett kort
någon aktivt redigerar samtidigt är precis den typ av krock `bildskydd.py`
finns för att undvika.

Läser LIVE-innehållet direkt innan skrivning (samma mönster som
wikipedia_bild_apply.py) -- inte ett snapshot från en tidigare körning.

Körs: python patch_bild_mellanrum.py --torr     (visa vad som skulle ändras)
      python patch_bild_mellanrum.py             (skriv på riktigt)
"""

import argparse
import re

import config
from ankiconnect import invoke

_IMG_RE = re.compile(r"<img[^>]*>")
_TRAILING_BR_RE = re.compile(r"(?:<br>\s*)*$")


def hitta_kandidater(deck):
    note_ids = invoke("findNotes", query=f'deck:"{deck}"')
    info = invoke("notesInfo", notes=note_ids)
    kandidater = []
    for n in info:
        bak = n["fields"].get(config.FIELD_BAKSIDA, {}).get("value", "")
        antal_bilder = len(_IMG_RE.findall(bak))
        if antal_bilder != 1:
            continue
        idx = bak.find("<img")
        head = bak[:idx]
        m = _TRAILING_BR_RE.search(head)
        br_antal = m.group(0).count("<br>") if m else 0
        if br_antal != 2:
            kandidater.append(n["noteId"])
    return kandidater


def rätta_ett(note_id, torr):
    live = invoke("notesInfo", notes=[note_id])
    if not live:
        return False, "hoppade över (noteId hittades inte)"
    bak = live[0]["fields"].get(config.FIELD_BAKSIDA, {}).get("value", "")
    ord_ = live[0]["fields"].get(config.FIELD_ORD, {}).get("value", "")

    antal_bilder = len(_IMG_RE.findall(bak))
    if antal_bilder != 1:
        return False, f"hoppade över (nu {antal_bilder} bilder, inte längre 1 -- rörs inte)"

    idx = bak.find("<img")
    head, svans = bak[:idx], bak[idx:]
    ny_head = _TRAILING_BR_RE.sub("<br><br>", head)
    if ny_head == head:
        return False, "redan rätt (ändrades av något annat sedan skanningen)"

    ny_bak = ny_head + svans
    if torr:
        return True, f"(torrkörning) {ord_!r}: skulle rätta mellanrummet"

    invoke("updateNoteFields", note={"id": note_id, "fields": {config.FIELD_BAKSIDA: ny_bak}})
    return True, f"{ord_!r}: rättat"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--torr", action="store_true", help="visa vad som skulle hända, skriv inget")
    parser.add_argument("--deck", default=config.DECK_NAME)
    args = parser.parse_args()

    kandidater = hitta_kandidater(args.deck)
    print(f"{len(kandidater)} kort med exakt en bild saknar korrekt <br><br>-mellanrum.\n")

    ok_antal, skip_antal = 0, 0
    for note_id in kandidater:
        ok, meddelande = rätta_ett(note_id, args.torr)
        status = "OK" if ok else "SKIP"
        print(f"[{status}] {note_id}: {meddelande}")
        if ok:
            ok_antal += 1
        else:
            skip_antal += 1

    ord_ = "skulle rättas" if args.torr else "rättade"
    print(f"\n{ok_antal} kort {ord_}, {skip_antal} överhoppade.")


if __name__ == "__main__":
    main()
