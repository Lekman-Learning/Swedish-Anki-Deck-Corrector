"""bristlista_bygg.py -- bygger om tre_kallor_saknas.json ur uppslagsfilerna.

Behövs efter parallella hämtningar (`hamta_parallellt.py`): varje `slaupp.py`
läser bristlistan, ändrar den och skriver tillbaka vid avslut, så den sista
processen skriver över de andras rader. Uppslagsfilerna själva är sanningen --
varje fil bär `kallor_med_innehall` -- så listan går att räkna fram exakt.

    python bristlista_bygg.py            # skriver tre_kallor_saknas.json
    python bristlista_bygg.py --visa     # räknar bara, rör inget
"""
import argparse
import json
import os
import time
from collections import Counter

HAR = os.path.dirname(os.path.abspath(__file__))
UPPSLAG = os.path.join(HAR, "uppslag")
BRISTLISTA = os.path.join(HAR, "tre_kallor_saknas.json")
ALLA = ("svenska.se", "synonymer.se", "wiktionary")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--visa", action="store_true")
    a = ap.parse_args()

    idag = time.strftime("%Y-%m-%d")
    brist, rakning = {}, Counter()
    filer = [f for f in os.listdir(UPPSLAG) if f.endswith(".json")]
    for f in filer:
        try:
            u = json.load(open(os.path.join(UPPSLAG, f), encoding="utf-8"))
        except Exception:
            rakning["olasbar"] += 1
            continue
        har = list(u.get("kallor_med_innehall") or [])
        rakning[f"{len(har)} källor"] += 1
        if len(har) < 3:
            brist[u.get("ord", os.path.splitext(f)[0])] = {
                "har": har,
                "saknar": [k for k in ALLA if k not in har],
                "sedd": idag,
            }

    print(f"uppslagsfiler: {len(filer)}")
    for k in sorted(rakning):
        print(f"  {k}: {rakning[k]}")
    print(f"ofullständiga: {len(brist)}")

    if a.visa:
        return
    json.dump(brist, open(BRISTLISTA, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"skrev {BRISTLISTA}")


if __name__ == "__main__":
    main()
