# -*- coding: utf-8 -*-
"""Mekanisk förgranskning av gröna kort inför v3 — sorterar fram det som behöver ögon.

Bakgrund: granskningen av 100 kort 2026-08-08 visade att den dominerande
bristen är CIRKULARITET -- synonymen upprepar ett ord ur definitionen. ~60 %
av korten hade det. Den bristen går att hitta utan omdöme, till skillnad från
sakfel och saknade betydelser.

Skriptet räknar därför fram tre signaler per kort och skriver ut korten
sorterade efter hur mycket de behöver granskas. Det ERSÄTTER inte granskningen
-- det bestämmer bara ordningen och sparar ögon till det som kräver dem.

  CIRKULÄR      synonym delar ordstam med definitionen. Grad 2 = alla
                synonymer gör det (kortet lär ingenting), grad 1 = någon.
  FACITGLAPP    kortets definition delar ingen ordstam med OLD-facit.
                Betyder inte fel -- betyder att de säger olika saker, alltså
                värt att titta på. Fångade förtecken, gungfly och upphov.
  INGET FACIT   ingen motsvarighet i OLD. v3 kräver eskalering.

Användning:
    python v3_lint_gron.py            # alla gröna is:new
    python v3_lint_gron.py --alla     # även is:review
"""
import argparse
import re
import sys

from ankiconnect import invoke
import config

STOPP = {
    "och", "eller", "som", "att", "det", "den", "ett", "en", "för", "med",
    "till", "från", "utan", "något", "någon", "man", "sig", "är", "inte",
    "har", "kan", "vid", "över", "under", "efter", "genom", "sin", "sitt",
    "ofta", "t.ex", "dvs", "mycket", "helt", "mer", "bara", "annan", "andra",
}


def strip_html(h):
    h = re.sub(r"<br\s*/?>", "\n", h)
    h = re.sub(r"<[^>]+>", "", h).replace("&nbsp;", " ")
    return h.strip()


def stammar(text):
    """Grova ordstammar: gemener, 6 tecken, stoppord bort. Fångar böjningar."""
    ord_ = re.findall(r"[a-zåäöéA-ZÅÄÖ]+", (text or "").lower())
    return {o[:6] for o in ord_ if len(o) > 3 and o not in STOPP}


def dela_baksida(b):
    """Baksidan är rader: huvudbetydelse, (register), synonymer, exempel."""
    rader = [r.strip() for r in strip_html(b).split("\n") if r.strip()]
    if not rader:
        return "", [], ""
    huvud = rader[0]
    syn, ex = [], ""
    for r in rader[1:]:
        if r.startswith("(") and r.endswith(")"):
            continue
        # Skilj synonymrad från exempelmening. Idiom saknar ofta synonymer
        # helt, och utan den här kontrollen lästes exemplet som synonym --
        # vilket blåste upp cirkularitetssiffran (exemplet innehåller ju
        # alltid uppslagsordet). Exempel = hel mening: många ord och
        # meningsskiljetecken.
        ar_mening = (len(r.split()) > 5 and re.search(r"[.!?]\s*$", r)) or "?" in r
        if ar_mening:
            if not ex:
                ex = r
        elif not syn:
            syn = [s.strip() for s in re.split(r"[,;/]", r) if s.strip()]
    return huvud, syn, ex


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--alla", action="store_true")
    a = p.parse_args()

    D = f'deck:"{config.DECK_NAME}"'
    q = f"{D} flag:3 -is:suspended" if a.alla else f"{D} is:new -is:suspended flag:3"
    nids = invoke("findNotes", query=q)
    print(f"granskar {len(nids)} grona kort\n")

    info = []
    for i in range(0, len(nids), 500):
        info.extend(invoke("notesInfo", notes=nids[i:i + 500]))

    rader = []
    for x in info:
        ord_ = strip_html(x["fields"]["Framsida"]["value"])
        huvud, syn, ex = dela_baksida(x["fields"]["Baksida"]["value"])
        hs = stammar(huvud)

        traffar = sum(1 for s in syn if stammar(s) & hs)
        cirk = 2 if syn and traffar == len(syn) else (1 if traffar else 0)

        o = invoke("findNotes",
                   query=f'deck:"Humanities::Languages::Svenska OLD" "Framsida:{ord_}"')
        if o:
            fac = strip_html(invoke("notesInfo", notes=[o[0]])[0]["fields"]["Baksida"]["value"])
            glapp = 0 if (stammar(fac) & hs) else 1
        else:
            fac, glapp = "", 2   # inget facit = eskalering

        poang = cirk * 2 + glapp * 3
        rader.append((poang, cirk, glapp, ord_, huvud, ", ".join(syn), fac[:60]))

    rader.sort(key=lambda r: -r[0])
    ettiketter = {0: "-", 1: "delvis", 2: "HELT"}
    glapp_txt = {0: "-", 1: "GLAPP", 2: "INGET FACIT"}

    print(f"{'poang':>5}  {'cirkular':8} {'facit':12} ord")
    print("-" * 78)
    for poang, cirk, glapp, ord_, huvud, syn, fac in rader:
        if poang == 0:
            continue
        print(f"{poang:>5}  {ettiketter[cirk]:8} {glapp_txt[glapp]:12} {ord_}")
        print(f"           def: {huvud}")
        print(f"           syn: {syn}")
        if fac:
            print(f"           fac: {fac}")

    rena = sum(1 for r in rader if r[0] == 0)
    print(f"\n=== {rena} kort utan anmarkning, {len(rader) - rena} flaggade ===")


if __name__ == "__main__":
    sys.exit(main())
