# -*- coding: utf-8 -*-
"""Ta bort `v3_underkand::<datum>` från kort som senare blivit godkända.

## Varför filen finns

Ett kort som underkänns taggas `v3_underkand::<datum>`, rödflaggas och
spärras. När det sedan skrivs om och GODKÄNNS av en ny blindgranskning får
det `oberoende_verifierad::<datum>` — men den gamla underkänd-taggen ligger
kvar. Kortet är då märkt både godkänt och underkänt samtidigt.

**Det är inte kosmetiskt.** `v3_invariant.py` UNDANTAR kort med
`v3_underkand::*` från regeln att full v3 ska vara blått och aktivt, eftersom
underkända kort medvetet ska förbli röda och spärrade. Ett kort med båda
taggarna faller därför ur invariantens kontroll helt: det syns varken som
rätt eller som fel. Invariantens rad "Undantagna" växte från 38 till 66 på
ett dygn utan att någon underkännande faktiskt kvarstod.

Mätt 2026-08-12: **66 kort** i decket bar båda taggarna.

## Regeln

Ta bort `v3_underkand::Y` endast när kortet har ett `oberoende_verifierad::X`
med **X >= Y**. Domen ska alltså vara senare än underkännandet. Ett kort som
underkänts EFTER sitt godkännande rörs inte — där är underkännandet det
färska beskedet.

## Var fixen egentligen hör hemma

I `kortgranskare.py slapp`, som är det som sätter `oberoende_verifierad`. Den
borde ta bort underkänd-taggen i samma andetag. Det här scriptet är
städningen av det som redan hunnit uppstå.

    python rensa_inaktuella_underkand.py            # visa vad som skulle göras
    python rensa_inaktuella_underkand.py --skriv    # gör det
"""
import argparse
import re
import sys

import config
from ankiconnect import invoke

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

UNDERKAND = "v3_underkand"
_DATUM = re.compile(r"::(\d{4}-\d{2}-\d{2})$")


def _datum(tagg):
    m = _DATUM.search(tagg)
    return m.group(1) if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skriv", action="store_true",
                    help="utför ändringen (utan flaggan visas bara vad som skulle ske)")
    a = ap.parse_args()

    q = (f'deck:"{config.DECK_NAME}" tag:{config.OBEROENDE_TAG_PREFIX}::* '
         f'tag:{UNDERKAND}::*')
    ids = invoke("findNotes", query=q)
    if not ids:
        print("Inga kort bär både godkänd- och underkänd-tagg.")
        return 0

    att_rensa, behalls = [], []
    for n in invoke("notesInfo", notes=ids):
        taggar = n.get("tags") or []
        godk = max((_datum(t) for t in taggar
                    if t.startswith(config.OBEROENDE_TAG_PREFIX + "::")), default="")
        gamla = [t for t in taggar
                 if t.startswith(UNDERKAND + "::") and _datum(t) <= godk]
        farska = [t for t in taggar
                  if t.startswith(UNDERKAND + "::") and _datum(t) > godk]
        ord_ = n["fields"][config.FIELD_ORD]["value"]
        if farska:
            behalls.append((ord_, godk, farska))
        elif gamla:
            att_rensa.append((n.get("noteId") or n.get("id"), ord_, godk, gamla))

    print(f"{len(ids)} kort bär båda taggarna.")
    print(f"  {len(att_rensa)} har ett godkännande som är SENARE — taggen är inaktuell")
    print(f"  {len(behalls)} har ett underkännande som är senare — rörs INTE")
    for ord_, godk, farska in behalls:
        print(f"    behålls: {ord_} (godkänd {godk}, underkänd {', '.join(farska)})")

    if not a.skriv:
        for _, ord_, godk, gamla in att_rensa[:15]:
            print(f"    skulle rensa: {ord_:<20} {' '.join(gamla)}  (godkänd {godk})")
        if len(att_rensa) > 15:
            print(f"    ... och {len(att_rensa) - 15} till")
        print("\nKör med --skriv för att utföra.")
        return 0

    for note_id, ord_, godk, gamla in att_rensa:
        for t in gamla:
            invoke("removeTags", notes=[note_id], tags=t)
    print(f"\nRensade {len(att_rensa)} kort. Kör nu `python v3_invariant.py --fixa`"
          f" — de omfattas av invarianten igen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
