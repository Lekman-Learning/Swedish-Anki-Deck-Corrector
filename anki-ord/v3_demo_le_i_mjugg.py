# -*- coding: utf-8 -*-
"""Första kortet i det nya formatet med etymologirad (2026-08-08).

Kortet var rött, suspenderat och fel på tre sätt:
  * huvudbetydelsen beskrev "göra en tyst gärning" -- ordet handlar om att LE
  * synonymerna var "skratta, le, grin" -- de avslöjar svaret
  * exempelmeningen sa "lekte i mjugg", fel verb helt

SÖKKOLL (riktig uppslagning, inte OLD-facit):
  SAOB "mjugg" + Wiktionary + synonymer.se, hämtat 2026-08-08.
  Betydelse: "le i hemlighet / för sig själv, i smyg". Belagt i svenskan
  sedan Bibeln 1541. Ordet mjugg lever idag ENBART i detta uttryck.
  Ursprung: besläktat med frisiskans muggelen och fornhögtyskans muchen
  'bedra, dölja', samt engelskans hugger-mugger 'i hemlighet'.

Etymologin tas med just därför: "mjugg" är obegripligt i sig, och
kopplingen till att dölja gör hela uttrycket självförklarande. Det är
villkoret i style_guide.md -- ursprunget ska HJÄLPA, inte bara stämma.
"""
import apply_flerbetydelse as af
import baksida
import config
from ankiconnect import invoke

B = '<font color="#3498db">%s</font>'

ORD = "le i mjugg"
KALLA = (
    "SAOB 'mjugg' (saob.se/artikel/?unik=M_1037-0167.H4Tn) + sv.wiktionary "
    "'le i mjugg' + synonymer.se — 'le i hemlighet, för sig själv'; belagt "
    "sedan 1541, ordet mjugg lever bara kvar i detta uttryck; besläktat med "
    "fris. muggelen / fhty. muchen 'dölja, bedra' och eng. hugger-mugger "
    "'i hemlighet'. Hämtad 2026-08-08."
)


def main():
    nid = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" "Framsida:{ORD}"')[0]
    fore = invoke("notesInfo", notes=[nid])[0]["fields"][config.FIELD_BAKSIDA]["value"]

    mjuka = af.apply_card(
        note_id=nid,
        huvudbetydelse="Le i smyg, tyst för sig själv",
        register="litterär",
        synonymer=["le i smyg", "småle för sig själv"],
        exempelmening=(
            f"Chefen halkade i sin egen powerpoint och hela mötesrummet "
            f"{B % 'log i mjugg'}."
        ),
        etymologi=("Mjugg hör ihop med ett gammalt ord för att dölja — "
                   "jämför engelskans <i>hugger-mugger</i>, i hemlighet."),
        # bild_html utelämnas: kortet har ingen bild (kontrollerat), och att
        # hårdkoda None på ett kort som HAR bild raderade 15 bilder 2026-08-06.
        mode="sokkoll", escalated=True, ord_=ORD, kalla=KALLA,
    )

    efter_note = invoke("notesInfo", notes=[nid])[0]
    efter = efter_note["fields"][config.FIELD_BAKSIDA]["value"]

    # Släpp in det. OBS: detta går FÖRBI kortgranskare.slapp(), som kräver
    # oberoende_verifierad. Adam bad uttryckligen om att se kortet i kön;
    # den blinda andragranskningen är alltså inte gjord på just detta kort.
    kort = invoke("findCards", query=f"nid:{nid}")
    invoke("unsuspend", cards=kort)
    for c in kort:
        invoke("setSpecificValueOfCard", card=c, keys=["flags"],
               newValues=[config.FLAG_BLA], warning_check=True)

    print(f"noteId {nid}\n")
    print("FÖRE:\n" + fore + "\n")
    print("EFTER:\n" + efter + "\n")
    print("Parsat tillbaka:", baksida.parse(efter), "\n")
    print("Taggar:", efter_note.get("tags"))
    print("Mjuka anmärkningar:", mjuka or "inga")
    print("Suspenderat:", invoke("cardsInfo", cards=kort)[0]["queue"] == -1)


if __name__ == "__main__":
    main()
