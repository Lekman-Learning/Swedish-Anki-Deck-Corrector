# -*- coding: utf-8 -*-
"""v3-omskrivning: 23 av 100 granskade is:new-kort, 2026-08-08.

Granskade mot Svenska OLD. Tre kategorier åtgärdas:

  SAKFEL/SPRÅKFEL   fel synonym eller fel i svenskan
  SAKNAD BETYDELSE  facit bar en betydelse kortet saknade
  HELT CIRKULÄRT    synonymen var definitionen ordagrant -- kortet lär ingenting

Klarhet före exakthet (Adams regel 2026-08-08): definitionen ska vara den
konkreta formulering man minns, inte den mest tekniskt precisa.
"""
import sys

import apply_flerbetydelse as af
from ankiconnect import invoke
import config

B = '<font color="#3498db">%s</font>'

KORT = [
    # ---------- sakfel / språkfel ----------
    ("voyeur", "Person som i smyg tittar på andras privata stunder", "negativ",
     ["smygtittare", "kikare på andra"],
     f"Grannen visade sig vara en {B % 'voyeur'} som spanade in i fönstren."),   # syn "kikare" = tubkikare, fel

    ("skenhelig", "Låtsas vara bättre än man är", "negativ",
     ["hycklande", "falsk", "skrymtaktig"],
     f"Han höll ett {B % 'skenheligt'} tal om ärlighet."),                        # "later" var felskrivet

    ("humid", "Fuktig i luften", "formell",
     ["fuktig", "rå"],
     f"Klimatet i regnskogen var varmt och {B % 'humidt'}."),                     # var "humid" om neutrum

    # ---------- saknad betydelse (facit bar den) ----------
    ("förtecken", "Tecken på något kommande / Den prägel något sker under", "formell",
     ["varningstecken", "prägel", "inriktning"],
     f"En valkampanj med socialistiska {B % 'förtecken'}."),

    ("gungfly", "Flytande matta av växter på vatten / Bildligt: osäker mark att stå på", "formell",
     ["flytmatta", "osäker grund"],
     f"Argumentet vilade på ett {B % 'gungfly'} av lösa antaganden."),

    ("upphov", "Det något kommer ifrån / Uppslaget till något", "formell",
     ["ursprung", "källa", "uppslag"],
     f"Ryktet hade sitt {B % 'upphov'} i en missuppfattning."),

    ("likvid", "Som har pengar tillgängliga att betala med", "formell",
     ["betalningsstark", "solvent"],
     f"Företaget hade gott om {B % 'likvida'} medel."),                           # def var substantiv, exemplet adjektiv

    # ---------- helt cirkulära ----------
    ("neslig", "Så illa att det drar vanära över någon", "negativ",
     ["skamlig", "förnedrande", "vanhedrande"],
     f"Laget led ett {B % 'nesligt'} nederlag med tio bollar."),

    ("elokvent", "Talar med lätthet och kraft", "positiv",
     ["vältalig", "talför"],
     f"Talaren var {B % 'elokvent'} och fångade hela publiken."),

    ("anletsdrag", "Formen på ett ansikte", "litterär",
     ["ansiktsdrag", "drag"],
     f"Hans {B % 'anletsdrag'} var stränga och orörliga."),

    ("diffus", "Utan skarpa gränser", "formell",
     ["otydlig", "oklar", "vag"],
     f"Beskrivningen av olyckan var väldigt {B % 'diffus'}."),

    ("fägring", "Det vackra hos något", "litterär",
     ["skönhet", "behag", "prakt"],
     f"Poeten hyllade naturens {B % 'fägring'} på våren."),

    ("urholka", "Gröpa ur inifrån / Tära på något tills det inte håller", "formell",
     ["gröpa ur", "försvaga", "underminera"],
     f"Vattnet hade {B % 'urholkat'} stenen under hundratals år."),

    ("modifiera", "Göra mindre ändringar i något", "formell",
     ["ändra", "anpassa", "justera"],
     f"Ingenjörerna {B % 'modifierade'} motorn för bättre bränsleekonomi."),

    ("intoxikation", "Skada av gift eller överdos", "formell",
     ["förgiftning", "överdosering"],
     f"Patienten fördes in med akut {B % 'intoxikation'}."),

    ("bestört", "Slagen av oväntade dåliga nyheter", "negativ",
     ["förskräckt", "chockad", "bragt ur fattningen"],
     f"Hon blev {B % 'bestört'} när hon hörde nyheten."),

    ("förfäkta", "Driva en åsikt trots motstånd", "formell",
     ["hävda", "försvara", "kämpa för"],
     f"Han {B % 'förfäktade'} sin ståndpunkt trots kritiken."),

    ("futuristisk", "Ser ut att höra hemma i framtiden", "formell",
     ["framtidsinriktad", "modernistisk"],
     f"Byggnaden hade en {B % 'futuristisk'} design av glas och stål."),

    ("atypisk", "Följer inte det vanliga mönstret", "formell",
     ["avvikande", "ovanlig", "oregelbunden"],
     f"Symtomen var {B % 'atypiska'} för sjukdomen."),

    ("portabel", "Går lätt att bära med sig", "formell",
     ["bärbar", "flyttbar", "handburen"],
     f"Han köpte en {B % 'portabel'} högtalare till resan."),

    ("bekantgöra", "Låta allmänheten få veta", "formell",
     ["tillkännage", "offentliggöra", "kungöra"],
     f"Företaget {B % 'bekantgjorde'} de nya reglerna för alla anställda."),

    ("manuell", "Gjord med händerna, inte av en maskin", "formell",
     ["handdriven", "icke-automatisk"],
     f"Bilen hade {B % 'manuell'} växellåda."),

    ("verifiera", "Kontrollera att något stämmer mot en källa", "formell",
     ["bekräfta", "styrka", "intyga"],
     f"Han {B % 'verifierade'} uppgifterna innan rapporten skickades."),
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
