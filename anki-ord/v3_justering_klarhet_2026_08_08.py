# -*- coding: utf-8 -*-
"""Justerar tre kort där föregående omskrivning bytte tydlighet mot exakthet.

Adams instruktion 2026-08-08: korten ska vara enkla att förstå enligt
Adam-tal. Teknisk precision som gör kortet svårare att minnas är fel
prioritering i ett deck vars syfte är återkallning, inte facklitteratur.
"""
import apply_flerbetydelse as af
from ankiconnect import invoke
import config

B = '<font color="#3498db">%s</font>'

KORT = [
    # Var: "Äggstock, den honliga könskörteln" -- fackspråk, sämre att minnas.
    ("ovarium", "Organet där ägg bildas hos honor", "formell",
     ["äggstock"],
     f"{B % 'Ovarierna'} frisätter ett ägg i månaden."),

    # Var: verbbetydelsen tillagd -- utlöste cirkularitetsvarning och tillförde lite.
    ("tjära", "Svart, tjock massa som utvinns ur trä eller kol", "vardaglig",
     ["beck", "bitumen"],
     f"Fiskarna brukade bränna {B % 'tjära'} för att täta båtarna."),

    # Var: "vittrat på plats utan att ha transporterats" -- onödigt tungt.
    ("eluvial", "Som vittrat sönder på platsen där det ligger", "formell",
     ["vittringsbildad"],
     f"Jordarten var {B % 'eluvial'} och hade bildats där den låg."),
]


def main():
    for ord_, huvud, reg, syn, ex in KORT:
        nids = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" "Framsida:{ord_}"')
        if not nids:
            print(f"  {ord_}: hittade ingen not")
            continue
        anm = af.apply_card(nids[0], huvudbetydelse=huvud, synonymer=syn,
                            exempelmening=ex, register=reg,
                            mode="sokkoll", escalated=True, ord_=ord_)
        print(f"  {ord_}: ok" + (f"   [anm: {anm}]" if anm else ""))


if __name__ == "__main__":
    main()
