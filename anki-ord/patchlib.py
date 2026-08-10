"""Delad byggkod för dagsbatcherna 2026-08-10 och framåt.

Fram till 2026-08-09 fick varje batch en egen kopia av samma `main()`. Det gick
så länge batcherna var få, men kopiorna hann glida isär: indenteringsbuggen i
`patch_so_batch9.py` (tilldelningen hamnade utanför loopen, så bara sista
nyckeln applicerades) fanns bara i EN av kopiorna och gick därför inte att
upptäcka genom att jämföra dem. En delad funktion har den egenskapen att en
rättning gäller alla batcher.

Kalla-fältet byggs härifrån och innehåller ALLA TRE källorna (Adams krav
2026-08-10). Formen måste matcha det `slaupp.py` skriver bevisrader för, annars
vägrar spärren skriva kortet -- vilket är meningen: en `kalla` som pekar på en
hämtning som inte gjorts ska inte gå igenom.
"""
import json
import os
import urllib.parse

import baksida

KO = "sessions/_dagens_142.json"


def kallor(ord_, *extra):
    """De tre standardkällorna för ett ord, plus eventuella extra URL:er.

    `extra` används för idiom: svenska.se tar bara enstaka uppslagsord, så
    'ett kok stryk' beläggs via grundordet `kok` -- där SO faktiskt har
    uttrycket som exempel. URL:en pekar då på det ord som verkligen hämtades,
    inte på idiomet, eftersom spärren jämför mot verkliga hämtningar."""
    k = urllib.parse.quote(ord_)
    return " ".join([
        f"https://svenska.se/api/msearch?ord={k}",
        f"https://www.synonymer.se/sv-syn/{k}",
        f"https://sv.wiktionary.org/wiki/{k}",
        *extra,
    ])


def grundord(ord_):
    """Kalla för ett idiom som belagts via sitt grundord."""
    k = urllib.parse.quote(ord_)
    return (f"https://svenska.se/api/msearch?ord={k} "
            f"https://www.synonymer.se/sv-syn/{k} "
            f"https://sv.wiktionary.org/wiki/{k}")


def bygg(P, mal, ko=KO):
    """P: {ord: (kalla, slutsats, ändringar)} -> sessionsfil."""
    bas = {e["ord"]: e for e in json.load(open(ko, encoding="utf-8"))}
    ut, saknade = [], []
    for ord_, (kalla, slutsats, andr) in P.items():
        e = bas.get(ord_)
        if e is None:
            saknade.append(ord_)
            continue
        p = baksida.parse(e["baksida"])
        proposed = {
            "huvudbetydelse": p["huvudbetydelse"],
            "register": p["register"],
            "synonymer": p["synonymer"],
            "synonym_groups": p["synonym_groups"],
            "exempelmening": p["exempelmening"],
            "etymologi": p["etymologi"],
            # Bilden ska ALLTID följa med uttryckligen. Saknas nyckeln tolkade
            # den gamla applicera() det som "radera", och tre kort (oknytt,
            # damast, köl) förlorade sina bilder 2026-08-10. Anroparen är
            # numera defensiv, men rätt värde ska ändå skickas härifrån.
            "bild_html": p["bild_html"],
        }
        for f_, v in andr.items():
            proposed[f_] = v
        # synonym_groups vinner tyst över synonymer i build(). Lämnas en gammal
        # gruppering kvar när betydelsen eller synonymerna ändrats, skrivs de
        # nya synonymerna aldrig ut -- det hände på `bonitet` 2026-08-09 och
        # syntes först när kortet lästes tillbaka ur Anki.
        if ("huvudbetydelse" in andr or "synonymer" in andr) \
                and "synonym_groups" not in andr:
            proposed["synonym_groups"] = None
        ut.append({
            "noteId": e["note"], "ord": ord_,
            "legacy": None, "proposed": proposed,
            "sokkoll": {"kalla": kalla, "slutsats": slutsats},
            "approved": True, "applicerad": False,
            "oforandrad": not andr,
        })
    os.makedirs("sessions", exist_ok=True)
    json.dump(ut, open(mal, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(ut)} poster -> {mal}")
    if saknade:
        print("SAKNAS i dagens kö:", saknade)

    # BEVISKONTROLL REDAN HÄR, inte först vid skrivningen. Tre gånger under
    # 2026-08-10 filtrerades slaupp.py:s utdata genom sed/head för att spara
    # kontext, och bevisraderna åkte med -- spärren vägrade då korten, helt
    # riktigt, men först efter att hela batchen skrivits färdigt. Att upptäcka
    # det här i stället kostar en sekund och sparar ett helt varv.
    try:
        import sokkoll_verifiering as sv
        bevis = sv.samla_bevis()
        obelagda = [e["ord"] for e in ut
                    if not sv.granska_kalla(e["sokkoll"]["kalla"], bevis)[0]]
        if obelagda:
            print(f"VARNING: {len(obelagda)} kort saknar bevisad hämtning och "
                  f"kommer att vägras: {', '.join(obelagda[:12])}")
            print("  Kör om slaupp.py med --tyst (utan sed/head) så att "
                  "bevisraderna når transkriptet.")
        else:
            print(f"Beviskontroll: alla {len(ut)} kort har bevisad hämtning.")
    except Exception as exc:                       # spärren är inte valfri,
        print(f"(beviskontroll kunde inte köras: {exc})")   # men bygget stoppas
    return ut                                      # inte av att FÖRhandsvisa den


def kontrollera(mal):
    """Läser tillbaka de skrivna korten UR ANKI och jämför fält för fält.

    Detta steg finns för att `applicerad: True` inte är ett bevis på att
    innehållet hamnade rätt -- indenteringsbuggen 2026-08-09 skrev synonymerna
    men aldrig huvudbetydelsen, och varje post var ändå markerad som
    applicerad. Det enda som duger är att läsa kortet som det faktiskt ligger."""
    from ankiconnect import invoke
    import config
    poster = [e for e in json.load(open(mal, encoding="utf-8"))
              if e.get("applicerad")]
    if not poster:
        print("Inga applicerade poster att kontrollera.")
        return []
    live = {n["noteId"]: n for n in
            invoke("notesInfo", notes=[e["noteId"] for e in poster])}
    avvikelser = []
    for e in poster:
        p = baksida.parse(live[e["noteId"]]["fields"][config.FIELD_BAKSIDA]["value"])
        pr = e["proposed"]
        for f in ("huvudbetydelse", "register", "etymologi"):
            if (p[f] or None) != (pr.get(f) or None):
                avvikelser.append((e["ord"], f, pr.get(f), p[f]))
        if set(p["synonymer"]) != set(pr.get("synonymer") or []):
            avvikelser.append((e["ord"], "synonymer",
                               pr.get("synonymer"), p["synonymer"]))
        if pr.get("bild_html") and not p["bild_html"]:
            avvikelser.append((e["ord"], "bild", "fanns", "BORTA"))
    print(f"Kontrollerade {len(poster)} kort mot Anki: "
          f"{len(avvikelser)} avvikelser")
    for o, f, v, l in avvikelser[:20]:
        print(f"  {o}.{f}: väntat {v!r} -> live {l!r}")
    return avvikelser
