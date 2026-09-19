"""laga_brister.py -- hämtar om ord som fick färre än tre källor.

Hör ihop med `hamta_parallellt.py`. Mätt 2026-09-20 på samma ordlista:

| Läge | Ord med alla tre källorna |
|---|---|
| Sekventiellt (1 process) | **15 av 15 (100 %)** |
| 3 processer | 33 av 38 (87 %) |
| 6 processer | 78 av 106 (74 %) |

Bortfallet är inte att orden saknas: `absurd` fick bara två källor parallellt
och alla tre vid omhämtning. Det är Wikimedias strypning (HTTP 429), som
`slaupp.py`s egen kommentar redan dokumenterar -- och en strypning ser ut som
ett saknat uppslag. Därför: hämta snabbt parallellt, laga sedan i ETT spår.

    python laga_brister.py               # alla uppslag med <3 källor
    python laga_brister.py --antal 200   # ta 200 åt gången
    python laga_brister.py --visa        # lista bara, hämta inget
"""
import argparse
import json
import os
import re
import subprocess
import sys

HAR = os.path.dirname(os.path.abspath(__file__))
UPPSLAG = os.path.join(HAR, "uppslag")
OTILLATNA = re.compile(r'[\\/:*?"<>|]')
# Flerordsuttryck står sällan i ordböckerna. De ska inte hämtas om i all
# evighet, så de hoppas över om de redan har noll källor.
FLERORD = re.compile(r"[ ()]")


def ofullstandiga():
    ut = []
    for f in os.listdir(UPPSLAG):
        if not f.endswith(".json"):
            continue
        try:
            u = json.load(open(os.path.join(UPPSLAG, f), encoding="utf-8"))
        except Exception:
            continue
        har = u.get("kallor_med_innehall") or []
        ord_ = u.get("ord") or os.path.splitext(f)[0]
        if len(har) < 3 and not (FLERORD.search(ord_) and not har):
            ut.append((ord_, har))
    return sorted(ut)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--antal", type=int)
    ap.add_argument("--visa", action="store_true")
    a = ap.parse_args()

    lista = ofullstandiga()
    print(f"ofullständiga uppslag: {len(lista)}")
    if a.visa:
        for o, har in lista[:60]:
            print(f"  {o}: {har}")
        return
    orden = [o for o, _ in lista][:a.antal] if a.antal else [o for o, _ in lista]
    if not orden:
        return
    fil = os.path.join(HAR, "_laga.json")
    json.dump(orden, open(fil, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"hämtar om {len(orden)} ord i ETT spår (ingen parallellitet)")
    subprocess.run([sys.executable, "-X", "utf8", "slaupp.py", "--fil", fil, "--tyst"], cwd=HAR)
    kvar = ofullstandiga()
    print(f"\nefter: {len(kvar)} ofullständiga (var {len(lista)})")
    print("Kör sedan:  python bristlista_bygg.py")


if __name__ == "__main__":
    main()
