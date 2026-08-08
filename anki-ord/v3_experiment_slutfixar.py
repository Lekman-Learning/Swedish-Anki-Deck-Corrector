# -*- coding: utf-8 -*-
"""Kontrollerat experiment 2026-08-08: snabbkoll vs sökkoll på samma kort.

UPPLÄGG: 30 orörda gröna is:new-kort snabbkollades (kort + OLD-facit + egen
kunskap). Verdikten skrevs ner FÖRE någon uppslagning. Därefter sökkollades
16 av dem mot ordbok för att mäta vad snabbkoll missade.

RESULTAT (n=16)
  Snabbkoll GODKÄNDE 10 av dessa -> 1 missad betydelse (10 %)
      eldprov   ordboken ger den historiska betydelsen GUDSDOM (bära glödande
                järn för att bevisa oskuld). Kortet hade bara den bildliga.
  Snabbkoll FLAGGADE 6 -> 5 korrekta, 1 falskt larm (83 %)
      blamera      reflexivt "blamera sig" är huvudanvändningen.  RATT
      gastspel     används bildligt långt utanför teatern.         RATT
      lotsa        sjöfartsbetydelsen är ordets kärna.             RATT
      ouvertyr     bildligt "upptakt" saknades.                    RATT
      duffel       är ett TYG och en VÄSKA, inte bara en rock.     RATT
      okvadinsord  stavningen var korrekt -- äldsta formen,
                   finns i SAOL och SAOB.                          FALSKT LARM

SLUTSATS: snabbkoll 2.0 är bättre än väntat men inte fullgod. Den missar
ungefär var tionde betydelse, och den missar dem tyst. Dess egna flaggor är
däremot pålitliga (83 %), vilket gör den användbar som TRIAGE: det den
flaggar är nästan alltid värt en sökkoll, men det den godkänner är inte
garanterat rent.

Jämför tidigare samma dag: på kort Claude REDAN SKRIVIT OM hittade sökkoll
2 av 6 fel -- och båda var betydelser Claude själv raderat. Sökkollens värde
är alltså högst på omskrivna kort, lägre på orörda.
"""
import apply_flerbetydelse as af
from ankiconnect import invoke
import config

B = '<font color="#3498db">%s</font>'

KORT = [
    ("eldprov", "Prov med glödande järn som skulle bevisa oskuld / Avgörande prövning",
     "litterär", ["gudsdom", "avgörande prov", "hård prövning"],
     f"Första matchen blev ett riktigt {B % 'eldprov'} för den unge målvakten.",
     "SO via svenska.se + Tyda — ursprungligen gudsdom: 'en oskyldigt anklagad "
     "skadades inte av eld eller glödande järn'; i modern tid överförd betydelse "
     "'hård prövning, avgörande test'. Hämtad 2026-08-08."),

    ("duffel", "Tjockt ylletyg / Ytterrock av det tyget",
     "formell", ["ylletyg", "ytterrock"],
     f"Han tog på sig sin gamla {B % 'duffel'} innan han gick ut i snön.",
     "SO/SAOL via svenska.se + historiskaord.se — efter staden Duffel i Belgien: "
     "tyget (grovt tjockt ylletyg), rocken och väskan. Belagt sedan 1950-talet ur "
     "eng. duffle coat. Hämtad 2026-08-08."),
]

BEKRAFTADE = [
    ("okvädinsord", "SAOL/SAOB + Isof frågelådan — okvädinsord är den ÄLDSTA formen och "
                    "fullt korrekt; okvädingsord och okvädningsord är senare, "
                    "regelbundnare bildningar. Ingen ändring behövs. Hämtad 2026-08-08."),
    ("pultron", "SO/SAOB — 'fegis, person som lätt skräms av hot eller fara'. Från fra. "
                "poltron, it. poltrone. Hämtad 2026-08-08."),
    ("sjok", "SAOL/Tyda — 'lager av något mjukt', 'klumpigt stycke'. Belagt sedan 1847. "
             "Hämtad 2026-08-08."),
    ("kråma sig", "SAOL via svenska.se — reflexivt 'göra sig till, brösta sig, stoltsera, "
                  "kokettera'. Hämtad 2026-08-08."),
    ("estetik", "NE + Wikipedia — filosofisk gren om konst, smak och det sköna; av gre. "
                "aisthesis 'sinnesintryck'. Egen disciplin sedan Baumgarten 1735. "
                "Hämtad 2026-08-08."),
    ("rangera", "SO/SAOB — 'ordna, ställa i ordning'; järnväg: placera vagnar i viss "
                "ordning. Från ty. rangieren, belagt 1664. Hämtad 2026-08-08."),
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
