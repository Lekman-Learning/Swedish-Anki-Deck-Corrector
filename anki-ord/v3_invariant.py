# -*- coding: utf-8 -*-
"""Håller full-v3-kortens LÄGE i takt med deras taggar.

Adams regel 2026-08-11: *"full v3 kort ska vara blue:flagged och unsuspended.
om anhedoni nu är full v3 så ska det inte vara grönt eller suspended."*

## Varför det behövde bli ett skript

Taggarna och kortets läge sattes på olika ställen och kunde glida isär utan
att något larmade. Mätt när regeln formulerades: av 412 full-v3-kort var
**387 blå, 22 röda, 1 grön och 2 utan flagga** -- och 16 av de röda var
AKTIVA, alltså kort Adam pluggade dagligen med en flagga som betyder
"stämmer inte alls" medan taggarna påstod att de var verifierade.

Ingen av de två påståendena var fel när de sattes. Den röda flaggan kom från
en äldre granskning, taggarna från v3. Det som saknades var någon som höll
dem i takt -- och en motsägelse som ingen kontrollerar ser ut som ordning.

## Regeln

Ett kort med alla fem taggarna i `config.SLAPP_KRAVER_TAGGAR` ska vara
**blåflaggat och avsuspenderat** -- MED TVÅ UNDANTAG:

* `v3_underkand::*` -- blindgranskningen har underkänt kortet. Det är
  bevisligen trasigt och ska stanna rött och spärrat tills det rättats.
* `v3_pausad::*` -- ordet går inte att sökkolla (varumärken, facktermer
  utanför ordböckerna). Se v3_pausa.py.

Undantagen är inte kosmetiska: utan dem hade skriptet släppt in kort som en
granskare uttryckligen dömt ut, och gjort dem blå på köpet.

    python v3_invariant.py --torr
    python v3_invariant.py --fixa
"""

import argparse
import sys

import config
from ankiconnect import invoke

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DECK = f'deck:"{config.DECK_NAME}"'
FULL_V3 = " ".join([
    f"tag:{config.FORMAT_TAG_V2}",
    f"tag:{config.FLERBETYDELSE_TAG_PREFIX}::*",
    f"tag:{config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX}::*",
    f"tag:{config.V3_TAG_PREFIX}::*",
    f"tag:{config.OBEROENDE_TAG_PREFIX}::*",
])
UNDANTAG = "(tag:v3_underkand* OR tag:v3_pausad::*)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--torr", action="store_true")
    ap.add_argument("--fixa", action="store_true")
    a = ap.parse_args()
    if not (a.torr or a.fixa):
        sys.exit("Ange --torr eller --fixa.")

    bas = f"{DECK} {FULL_V3} -{UNDANTAG}"
    alla = set(invoke("findCards", query=bas))
    ej_bla = sorted(alla - set(invoke("findCards", query=f"{bas} flag:{config.FLAG_BLA}")))
    susp = sorted(set(invoke("findCards", query=f"{bas} is:suspended")))
    undantagna = invoke("findCards", query=f"{DECK} {FULL_V3} {UNDANTAG}")

    print(f"Full v3, ej undantagna : {len(alla)}")
    print(f"  fel flagga (ej blå)  : {len(ej_bla)}")
    print(f"  suspenderade         : {len(susp)}")
    print(f"Undantagna (underkända/pausade, ska förbli röda+spärrade): {len(undantagna)}")

    if ej_bla:
        info = invoke("cardsInfo", cards=ej_bla[:15])
        noter = {n["noteId"]: n for n in invoke("notesInfo",
                                                notes=[c["note"] for c in info])}
        print("\n  Exempel:")
        for c in info:
            ord_ = noter[c["note"]]["fields"][config.FIELD_ORD]["value"][:22]
            print(f"    {ord_:<24} flagga={c['flags']}  suspenderad={c['queue'] == -1}")

    if a.torr:
        print("\n--torr: inget ändrat.")
        return

    if ej_bla:
        for c in ej_bla:
            invoke("setSpecificValueOfCard", card=c, keys=["flags"],
                   newValues=[config.FLAG_BLA], warning_check=True)
        print(f"\nSatte blå flagga på {len(ej_bla)} kort.")
    if susp:
        invoke("unsuspend", cards=susp)
        print(f"Avsuspenderade {len(susp)} kort.")

    # Verifiera mot Anki i stället för att lita på att anropen lyckades --
    # `setSpecificValueOfCard` rapporterar fel per post, inte via undantag.
    kvar_flagga = len(invoke("findCards", query=f"{bas} -flag:{config.FLAG_BLA}"))
    kvar_susp = len(invoke("findCards", query=f"{bas} is:suspended"))
    if kvar_flagga or kvar_susp:
        sys.exit(f"VARNING: {kvar_flagga} med fel flagga, {kvar_susp} suspenderade kvar.")
    print("Invarianten håller: alla full-v3-kort är blå och aktiva.")


if __name__ == "__main__":
    main()
