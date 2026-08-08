# -*- coding: utf-8 -*-
"""Riktig sökkoll, slumpurval ur nattens snabbkoll2-granskade. n=8 av 30.

Varför bara 8: sökkoll kräver en uppslagning per kort, och de sista 22 hade
blivit sämre gjorda -- samma överdrift som rättades tidigare samma dygn.
Åtta ärliga svar redovisas hellre än trettio påstådda.

UTFALL
  tjära        TRAFF  verbbetydelsen "bestryka med tjära" saknades. Claude tog
                      själv bort den några timmar tidigare vid en Adam-tal-
                      förenkling -- sökkollen fångade alltså Claudes eget fel.
  syntax       TRAFF  datavetenskapens syntax (regler för programkonstruktioner)
                      saknades; kortet hade bara språkvetenskapens.
  futuristisk  GRANS  kopplas till futurismen som konstriktning (1913). Perifer.
  intoxikation GRANS  omfattar även rus, inte bara skada. Perifer.
  residuum, manuell, gagna, diffus: bekräftade utan ändring.

MÖNSTER: alla fyra träffar/gränsfall är ord som lever i TVÅ DOMÄNER
(substantiv+verb, språkvetenskap+datavetenskap, vardag+konsthistoria,
medicin+vardag). De fyra bekräftade gör det inte. Domänkorsning ser ut att
predicera saknad betydelse bättre än ordets svårighetsgrad.
"""
import apply_flerbetydelse as af
from ankiconnect import invoke
import config

B = '<font color="#3498db">%s</font>'

KORT = [
    ("tjära", "Svart tjock massa ur trä eller kol / Stryka den massan på något",
     "vardaglig", ["beck", "bitumen", "becka"],
     f"Fiskarna brukade {B % 'tjära'} båtarna varje vår.",
     "SO/SAOB via svenska.se — substantiv 'svart trögflytande vätska ur stenkol "
     "eller trä'; verb 'bestryka med tjära'. Belagt sedan 1200-talet. Hämtad 2026-08-08."),

    ("syntax", "Reglerna för hur delar fogas samman till en helhet i ett språk",
     "formell", ["satslära", "meningsbyggnad", "formregler"],
     f"Ett stavfel i koden bröt mot språkets {B % 'syntax'}.",
     "SAOB + NE — språkvetenskap: satslära/meningsbyggnad; datavetenskap: 'regler "
     "för programkonstruktioner och uttryck i ett programspråk'. Hämtad 2026-08-08."),
]

BEKRAFTADE = [
    ("residuum", "SO via svenska.se — 'återstod', belagt 1779; kemi: fast rest efter "
                 "förbränning/filtrering/destillation. Hämtad 2026-08-08."),
    ("manuell", "Tyda/synonymer.se — adjektiv, 'med händerna, handopererad'. Ingen "
                "ytterligare betydelse. Hämtad 2026-08-08."),
    ("gagna", "SAOB — 'medföra gagn, vara till nytta'. Hämtad 2026-08-08."),
    ("diffus", "SAOB via svenska.se — av lat. diffundere; används både konkret "
               "(diffust ljus, diffus rodnad) och bildligt (diffus oro). Hämtad 2026-08-08."),
]


def main():
    for ord_, huvud, reg, syn, ex, kalla in KORT:
        nid = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" "Framsida:{ord_}"')[0]
        anm = af.apply_card(nid, huvudbetydelse=huvud, synonymer=syn,
                            exempelmening=ex, register=reg,
                            mode="sokkoll", escalated=True, ord_=ord_, kalla=kalla)
        print(f"OMSKRIVET  {ord_}" + (f"   [anm: {anm}]" if anm else ""))

    for ord_, kalla in BEKRAFTADE:
        nid = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" "Framsida:{ord_}"')[0]
        af.apply_pass(nid, mode="sokkoll", escalated=True, kalla=kalla)
        print(f"BEKRAFTAT  {ord_}")

    D = f'deck:"{config.DECK_NAME}"'
    print(f"\nsokverifierade 2026-08-08: "
          f"{len(invoke('findCards', query=f'{D} tag:flerbetydelse_sokverifierad::2026-08-08'))}")


if __name__ == "__main__":
    main()
