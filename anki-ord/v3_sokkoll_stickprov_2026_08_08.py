# -*- coding: utf-8 -*-
"""RIKTIG sökkoll — stickprov på 6 kort, 2026-08-08.

Syfte: mäta om sökkoll hittar något som snabbkoll 2.0 (OLD-facit + egen
kunskap) missade. Alla sex hade redan granskats och skrivits om samma dag
under snabbkoll2.

Utfall: 2 av 6 fick nya fynd.
  förtecken  SO/SAOB: musikens förtecken är PRIMÄRbetydelsen, plus
             matematikens plus/minus. Kortet hade ingendera.
  likvid     Ordboken ger BÅDE adjektiv och substantiv. Claudes egen
             omskrivning tidigare samma dag tog bort substantivbetydelsen
             -- sökkollen fångade alltså Claudes fel, inte kortets.
  gungfly, upphov, urholka, neslig: bekräftade, inga ändringar.

Källorna loggas till sokkoll_kallor.jsonl av _logga_kalla().
"""
import apply_flerbetydelse as af
from ankiconnect import invoke
import config

B = '<font color="#3498db">%s</font>'

KORT = [
    ("förtecken",
     "Notskriftstecken som höjer eller sänker en ton / Den prägel något sker under",
     "formell",
     ["prägel", "inriktning", "anstrykning"],
     f"En valkampanj med socialistiska {B % 'förtecken'}.",
     "SO/SAOB via svenska.se — musikens förtecken (♯, ♭, ♮) som primärbetydelse, "
     "bildlig 'utmärkande särpräg', samt matematikens plus/minus. Hämtad 2026-08-08."),

    ("likvid",
     "Betalning vid en affär / Som har pengar redo att betala med",
     "formell",
     ["betalning", "köpeskilling", "betalningsstark"],
     f"Säljaren fick {B % 'likvid'} samma dag som kontraktet skrevs.",
     "SO via svenska.se — substantiv: 'betalning för (större) varuöverlåtelse eller "
     "tjänst'; adjektiv: 'omedelbart tillgänglig för utbetalning'. Hämtad 2026-08-08."),
]

# Bekräftade utan ändring -- taggas ändå som sökverifierade, med källa.
BEKRAFTADE = [
    ("gungfly", "SO via svenska.se — bokstavlig växtmatta på vatten, bildlig sedan 1872 "
                "('ett moraliskt gungfly'). Hämtad 2026-08-08."),
    ("upphov", "SAOB/NE — 'ursprung, första början'; även 'impuls, idé'. Hämtad 2026-08-08."),
    ("urholka", "SO via svenska.se — bokstavlig 'göra fördjupning i', bildlig "
                "'undergräva, försvaga'. Hämtad 2026-08-08."),
    ("neslig", "SAOB via svenska.se — 'som medför skam el. vanära, särskilt om "
               "handlingar och brott'. Hämtad 2026-08-08."),
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
