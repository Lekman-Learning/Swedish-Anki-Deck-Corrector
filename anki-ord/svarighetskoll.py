# -*- coding: utf-8 -*-
"""Hittar huvudbetydelser som förklarar ett svårt ord med ett ANNAT svårt ord.

Adams invändning 2026-08-26: "det känns som att Adam-tal inte har blivit så
effektivt att du ibland använder ord som är ålderdomliga i huvudbetydelsen som
skapar mer svårigheter för mig att lära mig kortet."

Mätningen: decket ÄR listan över ord Adam inte kan än. Om en huvudbetydelse
innehåller ett ord som självt är ett uppslagsord i decket, förklaras ett okänt
ord med ett annat okänt ord. Det är kortets grundfel, och det går att mäta
mekaniskt i stället för att bedömas per kort.
"""
import json, re, sys, urllib.request

DECK = "Humanities::Languages::Svenska 10 000"


def ac(action, **params):
    r = urllib.request.urlopen(
        "http://127.0.0.1:8765",
        json.dumps({"action": action, "version": 6, "params": params}).encode(),
        timeout=60)
    d = json.loads(r.read())
    if d.get("error"):
        raise RuntimeError(d["error"])
    return d["result"]


def deckord():
    ids = ac("findNotes", query='deck:"%s"' % DECK)
    ut = set()
    for i in range(0, len(ids), 2000):
        for n in ac("notesInfo", notes=ids[i:i + 2000]):
            w = (n["fields"].get("Framsida", {}).get("value") or "").strip().lower()
            w = re.sub(r"<[^>]+>", "", w).strip()
            if w and " " not in w:
                ut.add(w)
    return ut


STOPP = set("""och eller som en ett den det de i på av till för med om att är var
blir göra något någon man den där när så under över mellan från utan mot vid har
hade kan ska sin sitt sina deras inte bara även samt annat andra alla mycket mer
mest ofta ibland aldrig alltid genom efter före inom utanför""".split())


def main():
    fil = sys.argv[1]
    S = json.load(open(fil, encoding="utf-8"))
    ord_i_deck = deckord()
    print("Uppslagsord i decket: %d\n" % len(ord_i_deck))
    traffar = 0
    for e in S:
        p = e.get("proposed")
        if not p:
            continue
        hb = p.get("huvudbetydelse") or ""
        ren = re.sub(r"<[^>]+>", " ", hb).lower()
        ord_ = re.findall(r"[a-zåäöéü]+", ren)
        egen = e["ord"].lower()
        svara = sorted({w for w in ord_
                        if w in ord_i_deck and w not in STOPP
                        and w != egen and not egen.startswith(w) and len(w) > 3})
        if svara:
            traffar += 1
            print("%-16s %s" % (e["ord"], hb))
            print("%-16s -> SVÅRA ORD I FÖRKLARINGEN: %s\n" % ("", ", ".join(svara)))
    print("=" * 60)
    skrivna = sum(1 for e in S if e.get("proposed"))
    print("%d av %d skrivna kort förklarar ett svårt ord med ett annat deck-ord."
          % (traffar, skrivna))


if __name__ == "__main__":
    main()
