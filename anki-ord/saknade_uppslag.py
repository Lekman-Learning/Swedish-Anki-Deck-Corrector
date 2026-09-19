"""saknade_uppslag.py -- listar deckets ord som saknar uppslag/<ord>.json.

Kräver att Anki är igång med AnkiConnect (samma krav som resten av projektet).
Resultatet är en enkel JSON-lista som `slaupp.py --fil` äter direkt, tänkt att
köras på en annan maskin (EliteBook) medan stationära datorn gör annat.

    python saknade_uppslag.py                    # skriver saknade_uppslag.json
    python saknade_uppslag.py --ut listan.json --antal 2000
"""
import argparse
import json
import os
import re
import urllib.request

import config

HAR = os.path.dirname(os.path.abspath(__file__))
UPPSLAG = os.path.join(HAR, "uppslag")
OTILLATNA = re.compile(r'[\\/:*?"<>|]')


def anki(action, **params):
    ra = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request("http://127.0.0.1:8765", data=ra,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        svar = json.load(r)
    if svar.get("error"):
        raise RuntimeError(svar["error"])
    return svar["result"]


def har_uppslag(ord_):
    return os.path.exists(os.path.join(UPPSLAG, OTILLATNA.sub("_", ord_) + ".json"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ut", default="saknade_uppslag.json")
    p.add_argument("--antal", type=int, help="ta bara de N första (för ett testpass)")
    p.add_argument("--deck", default=config.DECK_NAME)
    a = p.parse_args()

    nids = anki("findNotes", query=f'deck:"{a.deck}"')
    print(f"noter i decket: {len(nids)}")
    orden, tomma = [], 0
    for i in range(0, len(nids), 500):
        for n in anki("notesInfo", notes=nids[i:i + 500]):
            o = (n["fields"].get(config.FIELD_ORD, {}).get("value") or "").strip()
            if o:
                orden.append(o)
            else:
                tomma += 1

    unika = sorted(set(orden))
    saknas = [o for o in unika if not har_uppslag(o)]
    if a.antal:
        saknas = saknas[:a.antal]

    json.dump(saknas, open(a.ut, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"unika ord:        {len(unika)}   (tomma framsidor: {tomma})")
    print(f"har uppslag:      {len(unika) - len([o for o in unika if not har_uppslag(o)])}")
    print(f"SAKNAR uppslag:   {len(saknas)}  -> {a.ut}")
    print(f"\nKör sedan, gärna på den andra datorn:\n  python slaupp.py --fil {a.ut}")


if __name__ == "__main__":
    main()
