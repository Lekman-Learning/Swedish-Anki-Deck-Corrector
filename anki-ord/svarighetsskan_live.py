# -*- coding: utf-8 -*-
"""Skannar LIVE-korten i Anki efter cirkelproblemet: en huvudbetydelse som
förklarar ett svårt ord med ett annat ord som självt är ett kort i decket.

Adams prioritering 2026-08-26: svarighetskoll.py är mer relevant för de kort han
FAKTISKT studerar än för den suspenderade batchen. De suspenderade gör ingen
skada medan de väntar; ett dåligt kort i den aktiva kön kostar varje dag.
"""
import json, re, sys, urllib.request, collections

DECK = "Humanities::Languages::Svenska 10 000"
FULLV3 = ("tag:kortformat::v2 tag:flerbetydelse_granskad::* "
          "tag:flerbetydelse_sokverifierad::* tag:v3_granskad::* "
          "tag:oberoende_verifierad::* -(tag:v3_underkand* OR tag:v3_pausad::*)")


def ac(action, **params):
    r = urllib.request.urlopen(
        "http://127.0.0.1:8765",
        json.dumps({"action": action, "version": 6, "params": params}).encode(),
        timeout=120)
    d = json.loads(r.read())
    if d.get("error"):
        raise RuntimeError(d["error"])
    return d["result"]


def notes(query):
    ids = ac("findNotes", query=query)
    ut = []
    for i in range(0, len(ids), 1000):
        ut += ac("notesInfo", notes=ids[i:i + 1000])
    return ut


def framsida(n):
    w = (n["fields"].get("Framsida", {}).get("value") or "").strip()
    return re.sub(r"<[^>]+>", "", w).strip().lower()


def huvudbetydelse(n):
    """Huvudbetydelsen är den feta texten först i Baksida-bloben."""
    b = n["fields"].get("Baksida", {}).get("value") or ""
    m = re.search(r"<b>(.*?)</b>", b, re.S)
    if not m:
        return ""
    return re.sub(r"<[^>]+>", " ", m.group(1)).strip()


STOPP = set("""och eller som en ett den det de i på av till för med om att är var
blir göra något någon man den där när så under över mellan från utan mot vid har
hade kan ska sin sitt sina deras inte bara även samt annat andra alla mycket mer
mest ofta ibland aldrig alltid genom efter före inom utanför sig ett sitt vara
ha kunna vilja skola vilken vad hur vem""".split())


def main():
    alla = notes('deck:"%s"' % DECK)
    deckord = {framsida(n) for n in alla}
    deckord = {w for w in deckord if w and " " not in w and len(w) > 3}
    print("Uppslagsord i decket: %d" % len(deckord))

    v3 = notes('deck:"%s" (%s)' % (DECK, FULLV3))
    aktiva = notes('deck:"%s" -is:suspended (%s)' % (DECK, FULLV3))
    aktiv_ids = {n["noteId"] for n in aktiva}
    print("Full v3 totalt: %d   varav osuspenderade (studeras): %d\n"
          % (len(v3), len(aktiva)))

    traff = []
    for n in v3:
        hb = huvudbetydelse(n)
        if not hb:
            continue
        egen = framsida(n)
        ord_ = re.findall(r"[a-zåäöéü]+", hb.lower())
        svara = sorted({w for w in ord_
                        if w in deckord and w not in STOPP and w != egen
                        and not egen.startswith(w) and not w.startswith(egen)})
        if svara:
            traff.append((egen, hb, svara, n["noteId"] in aktiv_ids))

    aktiva_traff = [t for t in traff if t[3]]
    print("=" * 68)
    print("RESULTAT")
    print("  full v3-kort med minst ett svårt ord i huvudbetydelsen : %d av %d  (%.0f %%)"
          % (len(traff), len(v3), 100.0 * len(traff) / max(1, len(v3))))
    print("  varav i den AKTIVA kön (studeras nu)                   : %d av %d  (%.0f %%)"
          % (len(aktiva_traff), len(aktiva), 100.0 * len(aktiva_traff) / max(1, len(aktiva))))

    # hur svårt är det att laga? antal svåra ord per kort
    fordelning = collections.Counter(len(t[2]) for t in traff)
    print("\n  Antal svåra ord per drabbat kort:")
    for k in sorted(fordelning):
        print("    %d ord: %4d kort" % (k, fordelning[k]))

    # vilka ord är värst - de återkommer och kan fixas i klump
    vanliga = collections.Counter()
    for _, _, sv, _ in traff:
        vanliga.update(sv)
    print("\n  Vanligaste problemorden (samma ord i många kort = fixas i klump):")
    for w, c in vanliga.most_common(25):
        print("    %-18s %d kort" % (w, c))

    with open("svarighet_live_traffar.json", "w", encoding="utf-8") as f:
        json.dump([{"ord": a, "huvudbetydelse": b, "svara": c, "aktiv": d}
                   for a, b, c, d in traff], f, ensure_ascii=False, indent=1)
    print("\n  Full lista: svarighet_live_traffar.json")


if __name__ == "__main__":
    main()
