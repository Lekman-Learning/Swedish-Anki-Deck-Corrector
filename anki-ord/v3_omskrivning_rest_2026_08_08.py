# -*- coding: utf-8 -*-
"""Sista omgången gröna prop:due=0-kort, 2026-08-08. Samma väg via apply_card()."""
import sys

import apply_flerbetydelse as af
from ankiconnect import invoke
import config

B = '<font color="#3498db">%s</font>'

KORT = [
    ("särk", "Fotsitt underplagg av linne, buret närmast kroppen", "arkaisk",
     ["nattlinne", "underklänning"],
     f"Hon bar en vit linnebroderad {B % 'särk'} under klänningen."),

    ("eluvial", "Om jordlager: vittrat på plats utan att ha transporterats", "formell",
     ["vittringsbildad", "på plats vittrad"],
     f"Jordarten var {B % 'eluvial'} och hade bildats där den låg."),      # var en fras, inte mening

    ("ytong", "Lättbetong — poröst byggmaterial, ursprungligen ett varumärke", "vardaglig",
     ["lättbetong", "gasbetong"],
     f"{B % 'Ytong'} gör det möjligt att bygga hus snabbt."),

    ("esperanto", "Planspråk skapat för internationell kommunikation", "formell",
     ["konstgjort språk", "planspråk"],
     f"{B % 'Esperanto'} skapades på 1880-talet för att främja fred mellan folk."),

    ("tjära", "Svart, tjock massa av trä eller kol / Stryka tjära på något", "vardaglig",
     ["beck", "bitumen"],
     f"Fiskarna brukade bränna {B % 'tjära'} för att täta båtarna."),      # saknade verbbetydelsen

    ("trafikabel", "Möjlig att ta sig fram på", "formell",
     ["framkomlig", "farbar"],
     f"Vägen blev {B % 'trafikabel'} igen efter att skyfallet upphört."),  # facit "farbar" saknades

    ("exekutiv", "Som genomför fattade beslut", "formell",
     ["verkställande", "genomförande"],
     f"Den {B % 'exekutiva'} makten ligger hos regeringen."),

    ("alla taggar utåt", "Avvisande och lättretad", "vardaglig",
     ["irriterad", "på dåligt humör", "taggad"],
     f"Han gick omkring med {B % 'alla taggar utåt'} efter de dåliga nyheterna."),
]

GODKANDA = [
    "binär", "arsenal", "manege", "avskärma sig", "nit", "bakhåll",
    "liljeväxt", "stuva", "den springande punkten", "förkommen",
    "överburen", "inte ett skapande(s) grand",
]


def main():
    ok, fel = [], []
    for ord_, huvud, reg, syn, ex in KORT:
        try:
            nids = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" "Framsida:{ord_}"')
            if not nids:
                fel.append((ord_, "hittade ingen not")); continue
            anm = af.apply_card(nids[0], huvudbetydelse=huvud, synonymer=syn,
                                exempelmening=ex, register=reg,
                                mode="sokkoll", escalated=True, ord_=ord_)
            ok.append((ord_, anm))
        except Exception as e:
            fel.append((ord_, f"{type(e).__name__}: {e}"))

    print(f"=== OMSKRIVNA: {len(ok)} ===")
    for o, a in ok:
        print(f"  {o}" + (f"   [anm: {a}]" if a else ""))
    if fel:
        print(f"=== FEL: {len(fel)} ===")
        for o, m in fel:
            print(f"  {o}: {m}")

    # Godkända utan omskrivning: registrera sökkollen, rör inte innehållet.
    nids, cids, miss = [], [], []
    for o in GODKANDA:
        n = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" "Framsida:{o}"')
        if not n:
            miss.append(o); continue
        nids.append(n[0])
        cids += invoke("findCards", query=f'deck:"{config.DECK_NAME}" "Framsida:{o}"')
    print(f"=== GODKANDA taggade: {len(nids)} av {len(GODKANDA)} ===")
    if miss:
        print("  SAKNAS:", ", ".join(miss))
    if nids:
        invoke("addTags", notes=nids, tags="flerbetydelse_sokverifierad::2026-08-08")
        for c in cids:
            invoke("setSpecificValueOfCard", card=c, keys=["flags"],
                   newValues=[4], warning_check=True)

    D = f'deck:"{config.DECK_NAME}"'
    for lbl, q in [("prop:due=0 totalt", f"{D} prop:due=0"),
                   ("  gron kvar", f"{D} prop:due=0 flag:3"),
                   ("  bla", f"{D} prop:due=0 flag:4"),
                   ("sokverifierad::2026-08-08", f"{D} tag:flerbetydelse_sokverifierad::2026-08-08")]:
        print(f"{lbl}: {len(invoke('findCards', query=q))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
