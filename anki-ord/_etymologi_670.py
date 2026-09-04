# -*- coding: utf-8 -*-
"""Fyller i saknade etymologier pa full-v3-kort. Se PLAN_etymologi_670.md.

Kopierar SO:s egen etymologistrang ordagrant via HJ.etym(). Ingen
formulering, ingen bedomning -- darfor ingen blindgranskning.

    python _etymologi_670.py --torr     # bygger planen, skriver ingenting
    python _etymologi_670.py            # verifierar allt, skriver sedan
"""
import io, json, os, sys

import config
import _hjalp_0902b as HJ
from ankiconnect import invoke

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

TORR = "--torr" in sys.argv
GRA = "#9e9e9e"


def _uppslagsform(o):
    u = HJ._u(o) or {}
    return (u.get("uppslagsform") or "").strip()


def _etymrader(o):
    u = HJ._u(o)
    if not u:
        return []
    so = ((u.get("sammandrag") or {}).get("svenska_se") or {}).get("so") or {}
    return so.get("etymologi") or []


def main():
    ids = invoke("findNotes", query='tag:oberoende_verifierad deck:"%s"' % config.DECK_NAME)
    noter = invoke("notesInfo", notes=ids)
    print("full v3-kort: %d" % len(noter))

    saknar_fore = 0
    plan = []
    bort = {"fras": 0, "ingen_etym": 0, "flera_rader": 0, "avvikande_lemma": 0}

    for n in noter:
        o = n["fields"][config.FIELD_ORD]["value"].strip()
        b = n["fields"][config.FIELD_BAKSIDA]["value"]
        if GRA in b:
            continue                                    # filter 1
        saknar_fore += 1
        rader = _etymrader(o)
        if not rader:
            bort["ingen_etym"] += 1                     # filter 2
            continue
        if " " in o:
            bort["fras"] += 1                           # filter 3
            continue
        if len(rader) != 1:
            bort["flera_rader"] += 1                    # filter 4
            continue
        uf = _uppslagsform(o)
        if uf and uf != o:
            bort["avvikande_lemma"] += 1                # filter 5
            continue
        plan.append((n["noteId"], o, b, rader[0]))

    print("saknar etymologi: %d" % saknar_fore)
    print("bortfiltrerade  : %s" % bort)
    print("PLANERADE       : %d" % len(plan))

    # ---- verifiering: avviker ETT kort avbryts hela korningen ----
    fel = []
    for nid, o, b, e in plan:
        if b.count("</i>") != 1:
            fel.append((o, "%d st </i>" % b.count("</i>")))
        if GRA in b:
            fel.append((o, "har redan gratt block"))
        if "&" in e or "<" in e:
            fel.append((o, "etymologin innehaller & eller <"))
        if not e.strip():
            fel.append((o, "tom etymologi"))
    if fel:
        print("\nAVBRUTET -- %d kort avviker, INGET skrivet:" % len(fel))
        for o, v in fel[:20]:
            print("   %-24s %s" % (o, v))
        sys.exit(1)
    print("verifiering: alla %d klara" % len(plan))

    print("\nTIO STICKPROV")
    for nid, o, b, e in plan[:10]:
        print("  %-20s -> %s" % (o, e[:90]))

    if TORR:
        print("\n--torr: inget skrivet.")
        return

    # ---- skrivning ----
    uppdrag = []
    for nid, o, b, e in plan:
        i = b.index("</i>") + len("</i>")
        b_ny = b[:i] + '<br><br><font color="%s">&rarr; %s</font>' % (GRA, e) + b[i:]
        uppdrag.append({"id": nid, "fields": {config.FIELD_BAKSIDA: b_ny}})

    for u in uppdrag:
        invoke("updateNoteFields", note=u)
    print("\nSKREV %d kort" % len(uppdrag))

    # ---- lasning tillbaka ----
    noter2 = invoke("notesInfo", notes=ids)
    saknar_efter = sum(1 for n in noter2
                       if GRA not in n["fields"][config.FIELD_BAKSIDA]["value"])
    har = len(noter2) - saknar_efter
    print("efter: saknar %d (fore %d), har gratt block %d"
          % (saknar_efter, saknar_fore, har))
    if saknar_efter != saknar_fore - len(uppdrag):
        print("!! SIFFRAN STAMMER INTE -- utred innan nagot mer skrivs")
        sys.exit(1)
    print("stammer.")


main()
