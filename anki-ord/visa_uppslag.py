# -*- coding: utf-8 -*-
"""Skriver ut det som faktiskt far anvandas nar ett kort skrivs -- och inget annat.

BAKGRUND. Batch 6 (2026-08-25) hade 24 harda anmarkningar, tio av dem
`synonym_utan_ordboksbelagg`. Jag hade tagit synonymer ur synonymer.se:s
redaktionella lista i stallet for ur SO/SAOL. Jag strok synonymerna och kom till
noll flaggor -- men tva kort underkandes anda, for att fororeningen satt kvar i
BETYDELSERNA. `jasig` fick '(vardagligt) mallig och overlagsen' ur synonymer.se
nar SAOL sager 'fin, flott'.

Slutsatsen: sa lange synonymer.se syns i utskriften lacker den in. Den har
visaren skriver darfor ALDRIG ut synonymer.se. Behovs den nagon gang far den
lasas medvetet ur uppslag/<ord>.json, inte av misstag mitt i skrivandet.

VAD SOM VISAS, och varfor just det:

* SO:s RASTRUKTUR, inte sammandraget. Sammandraget plattar ut posterna och
  dubbelraknar underbetydelser, vilket gav falska `betydelse_kan_saknas` i batch
  4-6. Rastrukturen visar exakt en huvudbetydelse med sina underbetydelser, och
  en underbetydelse vars `definition` ar None ar en anvandningsutvidgning -- inte
  en betydelse som saknas.
* Varje lemma for sig. `mor` (adjektiv) och `mo` (substantiv) ar skilda
  uppslagsord som delar grundform. Blandas de ihop ser kortet ut att sakna
  betydelser det inte ska ha.
* SAOL:s definition ORDAGRANT, med semikolon kvar. SAOL:s `;` skiljer
  betydelser, och spaerren raknar dem inte -- `mor` underkandes i batch 6 for att
  SAOL:s tredje led ('bildl. foglig') foll bort.
* Bruklighetskommentarer per betydelse, sa att registret kan lasas ur ratt niva.
* `definitionstillagg` inom <<dubbla vinkelparenteser>>. Faltet bar OBLIGATORISK
  kontext och ar inte valfritt: SO definierar `afficiera` som 'utova (skadlig)
  inverkan pa' med tillagget 'om sjukdom'. Kortet underkandes 2026-08-25 for
  att tillagget inte syntes i utskriften. Samma sak fallde `negligera`.

ANVANDNING
    python visa_uppslag.py ord1 ord2 ...
    python visa_uppslag.py --fil sessions/session_2026-08-25_v3-batch2.json
    python visa_uppslag.py --fil <sessionsfil> --fran 0 --antal 20
"""
import argparse
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HAR = os.path.dirname(os.path.abspath(__file__))
# Matchar slaupp.py:s filnamnssanering.
OTILLATNA = re.compile(r'[\\/:*?"<>|]')
TAGG = re.compile(r"<[^>]+>")


def _ren(t):
    """SO bakar in <a href=...>-lankar i definitionstexten."""
    return TAGG.sub("", t or "").strip()


def _las(ord_):
    f = os.path.join(HAR, "uppslag", OTILLATNA.sub("_", ord_) + ".json")
    if not os.path.exists(f):
        return None
    try:
        return json.load(open(f, encoding="utf-8"))
    except Exception:
        return None


def visa(ord_):
    d = _las(ord_)
    print("=" * 4, ord_)
    if d is None:
        print("   UPPSLAG SAKNAS -- kor slaupp.py forst")
        return
    if d.get("uppslagsform") and d["uppslagsform"] != ord_:
        print("   uppslagsform i kallan:", d["uppslagsform"])
    print("   traffar:", ",".join(d.get("uppslagsordstraffar") or []) or "INGA")

    ratt = d.get("svenska_se_ratt") or {}

    # Utan exakt uppslagsordstraff ar allt som kommer tillbaka fuzzy-brus:
    # `ortodenti` gav 30 lemman fran `ortodox` till `orda`. Att skriva ut dem
    # ar inte bara onodigt utan aktivt skadligt -- nagon av dem SER ut att
    # passa, och da skrivs kortet ur fel artikel. Visa bara narmaste tre och
    # sag rakt ut att ordet inte finns.
    if not (d.get("uppslagsordstraffar") or []):
        print("   *** INGEN EXAKT UPPSLAGSORDSTRAFF ***")
        print("   Ordet finns inte som uppslagsord. Trolig orsak: felstavning,")
        print("   bojd form, eller ord som ordbockerna saknar.")
        narmaste = []
        for k in ("so", "saol"):
            for h in (ratt.get(k) or {}).get("hits", {}).get("hits", [])[:3]:
                lem = h["_source"].get("ortografi") or h["_source"].get("lemma")
                if lem and lem not in narmaste:
                    narmaste.append(lem)
        print("   narmaste lemman i kallan:", ", ".join(narmaste[:5]) or "inga")
        print("   ATGARD: ratta Framsida via proposed_ord, eller pausa kortet.")
        print()
        return

    # --- SO, rastruktur, ett lemma i taget -------------------------------
    hits = (ratt.get("so") or {}).get("hits", {}).get("hits", [])
    if not hits:
        print("   SO: inga traffar")

    # Flerordsuttryck far exakt uppslagsordstraff men slapper anda igenom
    # fuzzy-bruset: `fa gehor for` gav 30 lemman, fran `-talig` till `for`
    # som preposition. Behall bara lemman som faktiskt ar ett ord i sokordet,
    # och tak pa fyra. Utan det dranks den relevanta artikeln.
    delar = set(ord_.lower().split())
    relevanta = [h for h in hits
                 if (h["_source"].get("ortografi") or "").lower() in delar
                 or (h["_source"].get("ortografi") or "").lower() == ord_.lower()]
    if relevanta and len(relevanta) < len(hits):
        dolda = len(hits) - len(relevanta)
        hits = relevanta
        print("   (%d fuzzy-lemman dolda -- de ar inte ord i uppslaget)" % dolda)
    if len(hits) > 4:
        print("   (visar 4 av %d lemman)" % len(hits))
        hits = hits[:4]

    for h in hits:
        s = h["_source"]
        print("   SO-LEMMA %s (%s)" % (s.get("ortografi"), s.get("ordklass")))
        for hb in s.get("huvudbetydelser", []):
            bk = hb.get("bruklighetskommentar")
            am = hb.get("ämnesområden")
            rad = "      DEF: " + _ren(hb.get("definition"))
            # definitionstillagg bar OBLIGATORISK kontext, inte en parentes
            # man kan hoppa over: `afficiera` ar 'utova skadlig inverkan pa'
            # OM SJUKDOM. Kortet underkandes 2026-08-25 for att det saknades.
            if hb.get("definitionstillägg"):
                rad += "  <<" + _ren(hb["definitionstillägg"]) + ">>"
            if bk:
                rad += "   [brukl: %s]" % bk
            if am:
                rad += "   [amne: %s]" % ", ".join(am)
            print(rad)
            for ex in (hb.get("exempel") or [])[:2]:
                print("           ex: " + _ren(ex.get("text")))
            for ub in hb.get("underbetydelser", []):
                ud = _ren(ub.get("definition"))
                ubk = ub.get("bruklighetskommentar")
                utl = ub.get("definitionstillägg")
                tillagg = ("  <<" + _ren(utl) + ">>") if utl else ""
                if not ud:
                    # Ingen egen definition = anvandningsutvidgning, INTE en
                    # betydelse som saknas pa kortet.
                    print("        under: (ingen egen definition -- utvidgning)"
                          + tillagg + ("   [brukl: %s]" % ubk if ubk else ""))
                else:
                    print("        under: " + ud + tillagg
                          + ("   [brukl: %s]" % ubk if ubk else ""))
                for ex in (ub.get("exempel") or [])[:1]:
                    print("             ex: " + _ren(ex.get("text")))
            if hb.get("etymologi"):
                for e in hb["etymologi"]:
                    print("      etym: " + _ren(e.get("text") if isinstance(e, dict) else e))

    # --- SAOL, ordagrant, semikolon kvar ---------------------------------
    saol_hits = (ratt.get("saol") or {}).get("hits", {}).get("hits", [])
    if len(saol_hits) > 4:
        saol_hits = saol_hits[:4]
    for h in saol_hits:
        s = h["_source"]
        for hb in s.get("huvudbetydelser", []):
            rad = "   SAOL: " + _ren(hb.get("definition"))
            if hb.get("bruklighetskommentar"):
                rad += "   [brukl: %s]" % hb["bruklighetskommentar"]
            print(rad)
            print("         ^ semikolon skiljer BETYDELSER -- ta med alla led")
    print()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ord", nargs="*")
    p.add_argument("--fil", help="sessionsfil att lasa ord ur")
    p.add_argument("--fran", type=int, default=0)
    p.add_argument("--antal", type=int)
    a = p.parse_args()

    ord_lista = list(a.ord)
    if a.fil:
        poster = json.load(open(a.fil, encoding="utf-8"))
        ord_lista += [e["ord"] for e in poster]
    ord_lista = ord_lista[a.fran:]
    if a.antal:
        ord_lista = ord_lista[:a.antal]

    for o in ord_lista:
        visa(o)


if __name__ == "__main__":
    main()
