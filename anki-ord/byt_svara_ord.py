# -*- coding: utf-8 -*-
"""Hämtar, för varje drabbat kort, det svåra ordets EGEN huvudbetydelse ur decket.

Adams idé 2026-08-26: "vi byter ut alla komplexa ord i huvudbetydelsen mot
förklaringen av det ordet". Den går att göra, för förklaringen finns redan —
varje svårt ord är självt ett kort.

Skriptet gör INTE bytet automatiskt. Naiv substitution ger obrukbar text:
  frestad  = "Benägen eller lockad att handla på ett visst sätt"
  benägen  = "Som har en inre tendens att handla på visst sätt"
  -> "Som har en inre tendens att handla på visst sätt eller lockad att
      handla på ett visst sätt"   <- dubblerat och sämre

Det skriptet gör är att lägga fram underlaget: kortets text, det svåra ordet,
och det ordets egen definition. Omskrivningen görs sedan för hand, en fras i
taget, med betydelsen bevarad.
"""
import json, re, sys, urllib.request

DECK = "Humanities::Languages::Svenska 10 000"


def ac(action, **params):
    r = urllib.request.urlopen(
        "http://127.0.0.1:8765",
        json.dumps({"action": action, "version": 6, "params": params}).encode(),
        timeout=180)
    d = json.loads(r.read())
    if d.get("error"):
        raise RuntimeError(d["error"])
    return d["result"]


def clean(s):
    return re.sub(r"<[^>]+>", " ", s or "").replace("&nbsp;", " ").strip()


def hb(n):
    b = n["fields"].get("Baksida", {}).get("value") or ""
    m = re.search(r"<b>(.*?)</b>", b, re.S)
    return re.sub(r"\s+", " ", clean(m.group(1))) if m else ""


def main():
    ids = ac("findNotes", query='deck:"%s"' % DECK)
    ns = []
    for i in range(0, len(ids), 1000):
        ns += ac("notesInfo", notes=ids[i:i + 1000])
    definition = {}
    for n in ns:
        w = clean(n["fields"].get("Framsida", {}).get("value")).lower()
        d = hb(n)
        if w and d:
            definition[w] = d

    traff = json.load(open("svarighet_live_traffar.json", encoding="utf-8"))
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    slut = int(sys.argv[2]) if len(sys.argv) > 2 else 15

    ut = []
    for t in traff[start:slut]:
        rader = []
        for sv in t["svara"]:
            rader.append((sv, definition.get(sv, "(saknar eget kort med definition)")))
        ut.append({"ord": t["ord"], "nu": t["huvudbetydelse"], "svara": rader})

    for u in ut:
        print("### %s" % u["ord"])
        print("   NU: %s" % u["nu"])
        for sv, d in u["svara"]:
            print("   %-16s = %s" % (sv, d))
        print()
    print("Visade %d av %d träffar." % (len(ut), len(traff)))


if __name__ == "__main__":
    main()
