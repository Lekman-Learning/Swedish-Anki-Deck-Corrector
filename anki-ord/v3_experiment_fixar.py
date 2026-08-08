# -*- coding: utf-8 -*-
"""Rättar de två kort där snabbkoll flaggade och sökkoll bekräftade, 2026-08-08.

Del av det kontrollerade experimentet: 30 kort snabbkollades, 8 av dem
sökkollades sedan för att mäta vad snabbkoll missade.

RESULTAT
  4 kort som snabbkoll GODKÄNDE, sökkollade: 0 missar
    (lågmäld, furste, sekret, minuskel -- alla bekräftade)
  2 kort som snabbkoll FLAGGADE, sökkollade: 2 av 2 flaggor korrekta
    blamera   ordboken ger REFLEXIVT "blamera sig = skämma ut sig" som
              huvudanvändning; kortet sa "skämma ut någon annan".
    gästspel  används bildligt långt utanför teatern ("kortare gästspel
              som företagare och rådgivare"); kortet låste det vid uppträdande.

SLUTSATS: sökkoll gav ingen mätbar vinst över snabbkoll på ORÖRDA kort.
Dess två träffar tidigare samma dag (likvid, tjära) var båda betydelser
Claude själv tagit bort vid omskrivning. Sökkollens värde ligger alltså i
att granska granskaren, inte kortet. n=4 på den avgörande delen -- riktning,
inte resultat.
"""
import apply_flerbetydelse as af
from ankiconnect import invoke
import config

B = '<font color="#3498db">%s</font>'

KORT = [
    ("blamera", "Skämma ut sig själv genom en dumhet", "formell",
     ["göra bort sig", "dumma sig", "trampa i klaveret"],
     f"Han {B % 'blamerade'} sig fullständigt under presentationen.",
     "SO/SAOB via svenska.se — reflexivt 'blamera sig: skämma ut sig, göra sig "
     "löjlig'. Från franskans blâmer via ty. blamieren, ca 1870. Hämtad 2026-08-08."),

    ("gästspel", "Kort framträdande på främmande scen / Tillfälligt inhopp i vilken roll som helst",
     "formell", ["inhopp", "tillfälligt engagemang"],
     f"Hans {B % 'gästspel'} som rådgivare varade bara ett halvår.",
     "NE + Tyda — 'besök av teatersällskap från annat håll; tillfälligt "
     "framträdande', samt bildligt: 'kortare gästspel som företagare och "
     "rådgivare'. Hämtad 2026-08-08."),
]


def main():
    for ord_, huvud, reg, syn, ex, kalla in KORT:
        nid = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" "Framsida:{ord_}"')[0]
        anm = af.apply_card(nid, huvudbetydelse=huvud, synonymer=syn,
                            exempelmening=ex, register=reg,
                            mode="sokkoll", escalated=True, ord_=ord_, kalla=kalla)
        print(f"OMSKRIVET  {ord_}" + (f"   [anm: {anm}]" if anm else ""))

    for ord_, kalla in [
        ("lågmäld", "SAOB/Tyda — 'talar el. uppträder med dämpad röst, utan att söka "
                    "uppmärksamhet'. Hämtad 2026-08-08."),
        ("furste", "Wikipedia/SAOB — 'suverän monark av lägre rang'; vidare 'monarkisk "
                   "härskare av vilken rang som helst'. Hämtad 2026-08-08."),
        ("sekret", "SAOB — 'kroppsvätska som avsöndras', synonymt med utsöndring. "
                   "Hämtad 2026-08-08."),
        ("minuskel", "Tyda/NE — paleografins term för 'liten bokstav', motsats versal. "
                     "Hämtad 2026-08-08."),
    ]:
        nid = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" "Framsida:{ord_}"')[0]
        af.apply_pass(nid, mode="sokkoll", escalated=True, kalla=kalla)
        print(f"BEKRAFTAT  {ord_}")


if __name__ == "__main__":
    main()
