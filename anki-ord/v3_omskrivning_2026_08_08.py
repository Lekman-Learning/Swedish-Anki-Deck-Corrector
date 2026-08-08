# -*- coding: utf-8 -*-
"""v3-omskrivning av de gröna korten introducerade 2026-08-08.

Går genom apply_card() så att validate_register() och validate_adamtal()
faktiskt körs -- direkta AnkiConnect-skrivningar hade kringgått spärrarna,
vilket är precis vad v3 finns för att förhindra.

mode="sokkoll", escalated=True: varje kort här har fått en riktig
källkontroll (OLD-facit där det fanns, annars dubbelkollat mot egen
kunskap enligt Adams instruktion 2026-08-08 om att kompensera för
saknat facit).

OBS: oberoende_verifierad sätts INTE. Samma agent har skrivit och
granskat, alltså är den blinda andragranskningen inte gjord. Att sätta
taggen hade varit en lögn i just den kolumn v3 bygger på.
"""
import sys

import apply_flerbetydelse as af
from ankiconnect import invoke
import config

BLA = '<font color="#3498db">%s</font>'

KORT = [
    # (ord, huvudbetydelse, register, synonymer, exempelmening_html)
    ("erforderlig", "Som krävs för ett visst syfte", "formell",
     ["nödvändig", "obligatorisk", "påkallad"],
     f"Han saknade den {BLA % 'erforderliga'} utbildningen för tjänsten."),

    ("vertebrat", "Djur med ryggrad — fisk, groddjur, kräldjur, fågel eller däggdjur", "formell",
     ["ryggradsdjur"],
     f"Fiskar, fåglar och däggdjur är alla {BLA % 'vertebrater'}."),

    ("gagna", "Vara till fördel för någon eller något", "formell",
     ["gynna", "främja", "tjäna"],
     f"Ett gott samarbete {BLA % 'gagnar'} båda företagen."),

    ("kiropraktik", "Manuell behandling av rygg och leder genom ledjustering", "formell",
     ["manuell terapi", "ledbehandling"],
     f"Hon provade {BLA % 'kiropraktik'} för sin långvariga ryggvärk."),

    ("toujours", "Alltid, jämt", "litterär",
     ["alltid", "jämt", "ständigt"],
     f"Hon var {BLA % 'toujours'} lika elegant, oavsett tillfälle."),

    ("gloriös", "Full av ära och glans", "litterär",
     ["ärorik", "strålande", "lysande"],
     f"Laget firade en {BLA % 'gloriös'} seger i finalen."),

    ("förvärva", "Få något i sin ägo / Tillägna sig något abstrakt, som kunskap eller erfarenhet", "formell",
     ["anskaffa", "erhålla", "tillägna sig"],
     f"Hon {BLA % 'förvärvade'} flytande franska under sina år i Lyon."),

    ("beskärm", "Beskydd under någons omsorg", "arkaisk",
     ["värn", "hägn", "beskydd"],
     f"Barnen växte upp under sin farmors {BLA % 'beskärm'}."),

    ("vestal", "Prästinna i Vestas tempel, bunden vid kyskhetslöfte / Bildligt: kysk kvinna", "litterär",
     ["prästinna", "kysk kvinna"],
     f"{BLA % 'Vestalerna'} vaktade den heliga elden i Rom."),

    ("bryderi", "Villrådighet inför ett svårt val", "formell",
     ["villrådighet", "huvudbry", "bekymmer"],
     f"Han stod i stort {BLA % 'bryderi'} över vilket jobb han skulle ta."),

    ("brevledes", "Med brev som medel för kontakt", "litterär",
     ["per brev", "skriftligen", "per post"],
     f"De höll kontakten {BLA % 'brevledes'} under kriget."),
]


def main():
    ok, fel = [], []
    for ord_, huvud, reg, syn, ex in KORT:
        try:
            nids = invoke("findNotes",
                          query=f'deck:"{config.DECK_NAME}" "Framsida:{ord_}"')
            if not nids:
                fel.append((ord_, "hittade ingen not"))
                continue
            anm = af.apply_card(
                nids[0],
                huvudbetydelse=huvud,
                synonymer=syn,
                exempelmening=ex,
                register=reg,
                mode="sokkoll",
                escalated=True,
                ord_=ord_,
            )
            ok.append((ord_, anm))
        except Exception as e:
            fel.append((ord_, f"{type(e).__name__}: {e}"))

    print(f"=== SKRIVNA: {len(ok)} ===")
    for o, anm in ok:
        print(f"  {o}" + (f"   [mjuka anmärkningar: {anm}]" if anm else ""))
    print(f"=== FEL: {len(fel)} ===")
    for o, m in fel:
        print(f"  {o}: {m}")
    return 0 if not fel else 1


if __name__ == "__main__":
    sys.exit(main())
