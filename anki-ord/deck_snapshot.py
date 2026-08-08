# -*- coding: utf-8 -*-
"""Daglig ögonblicksbild av deckets tillstånd -> deck_historik.jsonl.

Varför: projektet loggar *händelser* (kallor.jsonl, oberoende_granskningar.jsonl)
men aldrig *läget*. Efter 67 dagars v3 går det då inte att visa en kurva, bara
att hävda att det blev bättre. Baslinjen på 10 % fel (2026-08-08) är meningslös
utan mätpunkter att jämföra den mot.

En rad per dag, JSONL, append-only. Kör om samma dag skriver över dagens rad --
en snapshot är läget, inte en händelse, och två rader samma datum vore två
sanningar om samma dag.

    python deck_snapshot.py            # ta dagens snapshot, visa diff mot förra
    python deck_snapshot.py --visa     # visa historiken, skriv ingenting
"""
import json
import os
import sys
from datetime import date

import config
from ankiconnect import invoke

HISTORIK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deck_historik.jsonl")
D = f'deck:"{config.DECK_NAME}"'

# Namn -> Anki-fråga. Ordningen är den de skrivs ut i.
MATT = [
    ("totalt",            ""),
    ("v2_format",         f"tag:{config.FORMAT_TAG_V2}"),
    ("flerbetydelse",     f"tag:{config.FLERBETYDELSE_TAG_PREFIX}::*"),
    ("sokverifierad",     f"tag:{config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX}::*"),
    ("v3_granskad",       f"tag:{config.V3_TAG_PREFIX}::*"),
    ("oberoende",         f"tag:{config.OBEROENDE_TAG_PREFIX}::*"),
    ("prio_hog",          f"tag:{config.PRIO_TAG_HOG}"),
    ("flagga_rod",        f"flag:{config.FLAG_ROD}"),
    ("flagga_gul",        f"flag:{config.FLAG_GUL}"),
    ("flagga_gron",       f"flag:{config.FLAG_GRON}"),
    ("flagga_bla",        f"flag:{config.FLAG_BLA}"),
    ("nya_aktiva",        "is:new -is:suspended"),
    ("suspenderade",      "is:suspended"),
    ("forfallna",         "is:due"),
]


def mat():
    ut = {}
    for namn, fraga in MATT:
        q = D if not fraga else f"{D} {fraga}"
        ut[namn] = len(invoke("findCards", query=q))
    return ut


def las_historik():
    if not os.path.exists(HISTORIK):
        return []
    rader = []
    with open(HISTORIK, encoding="utf-8") as f:
        for rad in f:
            rad = rad.strip()
            if rad:
                try:
                    rader.append(json.loads(rad))
                except ValueError:
                    continue
    return rader


def skriv(rader):
    with open(HISTORIK, "w", encoding="utf-8") as f:
        for r in rader:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def visa_diff(ny, forra):
    bredd = max(len(n) for n, _ in MATT)
    for namn, _ in MATT:
        v = ny["matt"][namn]
        if forra is None:
            print(f"  {namn:<{bredd}} {v:>6}")
            continue
        d = v - forra["matt"].get(namn, 0)
        pil = f"  {d:+d}" if d else ""
        print(f"  {namn:<{bredd}} {v:>6}{pil}")


def main():
    if "--visa" in sys.argv:
        rader = las_historik()
        if not rader:
            print("Ingen historik ännu.")
            return
        for r in rader:
            m = r["matt"]
            print(f"{r['datum']}  totalt={m['totalt']:<5} v3={m['v3_granskad']:<5} "
                  f"oberoende={m['oberoende']:<5} prio={m['prio_hog']:<4} "
                  f"nya_aktiva={m['nya_aktiva']}")
        return

    idag = date.today().isoformat()
    rader = las_historik()
    forra = next((r for r in reversed(rader) if r["datum"] != idag), None)

    ny = {"datum": idag, "matt": mat()}
    rader = [r for r in rader if r["datum"] != idag] + [ny]
    rader.sort(key=lambda r: r["datum"])
    skriv(rader)

    if forra:
        print(f"Snapshot {idag} (diff mot {forra['datum']}):")
    else:
        print(f"Snapshot {idag} -- första mätpunkten, ingen diff att visa:")
    visa_diff(ny, forra)
    print(f"\nSkrivet till {os.path.basename(HISTORIK)} ({len(rader)} mätpunkter).")


if __name__ == "__main__":
    main()
