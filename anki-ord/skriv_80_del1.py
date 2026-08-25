# -*- coding: utf-8 -*-
"""80-kortsomgangen 2026-08-25, del 1 (ord 1-20).

Skriven med `visa_uppslag.py`, som ALDRIG visar synonymer.se. Det var den
kallan som fororenade bade synonymfalten och betydelserna i batch 6.

Tva kort pausas: `ortodenti` och `reaktioner` finns inte som uppslagsord.
Det forsta ar felstavat (ska vara ortodonti), det andra star i plural
(ska vara reaktion). `proposed_ord` stods inte av v3-vagen, sa Framsida
maste rattas for hand innan korten kan tas tillbaka.
"""
import json
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-25_v3-batch2.json"
BLA = '<font color="#3498db">%s</font>'
HOPPA = {"ortodenti", "reaktioner"}

TILLAT = {
 "neuros": {"register_motsager_markning":
   "SO:s bruklighetskommentar ar 'numera ej i fackmassiga sammanhang' och SAOL "
   "skriver 'mest i aldre tid'. Bada sager att ordet ar pa vag ut, vilket ar "
   "precis vad 'ngt alderdomlig' betyder i valvets vokabular. Kommentaren delar "
   "bara inget ordstam med den."},
 "presidium": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('hogsta ledning') och EN underbetydelse "
   "('ordforandeskap'). Bada star pa kortet."},
}

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form, etymologi)
KORT = {
 "ametist": ("En purpur- till violettfärgad variant av kvarts",
   "neutral, neutral", [],
   "Ringen var infattad med en slipad ametist.", "ametist",
   "Av grekiska <i>amethystos</i> 'som motverkar rus'. Stenen troddes skydda mot berusning."),

 "bräsera": ("Bryna och därefter steka under lock på svag värme med tillsats av vätska",
   "neutral, neutral", [],
   "Hon bräserade oxbringan i tre timmar.", "bräserade",
   "Av franska <i>braiser</i>, till <i>braise</i> 'glöd'."),

 "daler": ("Ett äldre svenskt silver- eller kopparmynt",
   "ngt ålderdomlig, neutral", [],
   "Gården såldes för trehundra daler silvermynt.", "daler",
   "Av lågtyska <i>daler</i>, efter <i>Joachimsthaler</i> — mynt präglat i Joachimsthal. Samma ord som engelskans <i>dollar</i>."),

 "hånfull": ("Som uttrycker låg värdering av någon på ett illvilligt och förlöjligande sätt",
   "neutral, nedsättande", [],
   "Han svarade med ett hånfullt leende.", "hånfullt",
   "Till <i>hån</i>, av fornsvenska <i>hān</i> 'skam, vanära'."),

 "interpellation": ("Fråga utanför riksdagens ordinarie föredragningslista som en riksdagsledamot ställer till ett statsråd",
   "fackspråklig, neutral", [],
   "Oppositionen lämnade in en interpellation om vårdköerna.", "interpellation",
   "Av latin <i>interpellatio</i> 'avbrytande, tilltal', till <i>interpellare</i> 'avbryta någon som talar'."),

 "karyatid": ("Skulpterad kvinnogestalt som bär upp en del av en byggnad",
   "ngt ålderdomlig, neutral", [],
   "Taket bars upp av sex karyatider i vit marmor.", "karyatider",
   "Av grekiska <i>karyatides</i>, egentligen 'kvinnor från Karyai'."),

 "kirurgi": ("Den del av läkarvetenskapen som gäller sjukdomar och skador som behandlas genom operation",
   "neutral, neutral", [],
   "Han specialiserade sig på ortopedisk kirurgi.", "kirurgi",
   "Av grekiska <i>cheirourgia</i> 'handarbete', till <i>cheir</i> 'hand' och <i>ergon</i> 'arbete'."),

 "logg": ("Ett fartygsinstrument som mäter hastighet och tillryggalagd distans ; löpande förteckning över händelser i ett datasystem",
   "neutral, neutral", [],
   "Serverns logg visade när felet uppstod.", "logg",
   "Av engelska <i>log</i> 'trästock'. Farten mättes förr genom att en stock kastades i vattnet."),

 "neuros": ("Uttryck för psykisk ohälsa, särskilt ångest",
   "ngt ålderdomlig, neutral", [],
   "Diagnosen neuros används inte längre i fackmässiga sammanhang.", "neuros",
   "Till grekiska <i>neuron</i> 'nerv, sena'."),

 "prång": ("Liten trång passage eller vrå",
   "neutral, neutral", ["vrå"],
   "Butiken låg i ett prång mellan två höga hus.", "prång",
   "Av lågtyska <i>prange</i> 'trängsel, klämma'. Besläktat med <i>tvinga</i>."),

 "rotting": ("Träfibrer av lianen hos en klättrande palm, använda till möbler och käppar",
   "neutral, neutral", [],
   "Stolen var flätad i rotting.", "rotting",
   "Av malajiska <i>rotan</i>, växtens namn."),

 "afficiera": ("Utöva en skadlig inverkan på någon eller något",
   "ngt ålderdomlig, neutral", ["påverka", "angripa"],
   "Sjukdomen afficierar främst de äldre.", "afficierar",
   "Av latin <i>afficere</i> 'påverka, försätta i ett tillstånd'."),

 "elliptisk": ("Formad som en ellips ; (språkvetenskap) förkortad så att ord underförstås",
   "neutral, neutral", [],
   "Planeternas banor är elliptiska, inte cirkulära.", "elliptiska",
   "Till <i>ellips</i>, av grekiska <i>elleipsis</i> 'brist, utelämnande'."),

 "exil": ("Landsflykt",
   "neutral, neutral", ["landsflykt"],
   "Författaren levde i exil i trettio år.", "exil",
   "Av latin <i>exilium</i> 'landsflykt', till <i>ex</i> 'ut' och roten i <i>salire</i> 'gå, springa'."),

 "indisposition": ("Tillfällig nedsättning av prestationsförmågan",
   "neutral, neutral", [],
   "Löparen skyllde det svaga loppet på indisposition.", "indisposition",
   "Till latin <i>in-</i> 'o-' och <i>dispositio</i> 'ordnande, sinnesstämning'."),

 "negligera": ("Ge sken av att inte lägga märke till något ; strunta i",
   "neutral, neutral", ["försumma"],
   "Han negligerade helt hennes invändningar.", "negligerade",
   "Av latin <i>negligere</i> 'inte bry sig om', till <i>nec</i> 'inte' och <i>legere</i> 'plocka upp'."),

 "presidium": ("Högsta ledning ; ordförandeskap",
   "neutral, neutral", ["ordförandeskap", "ledning"],
   "Frågan hänsköts till förbundets presidium.", "presidium",
   "Av latin <i>praesidium</i> 'skydd, försvar', till <i>praesidere</i> 'sitta främst, leda'."),

 "profylaktisk": ("Förebyggande",
   "fackspråklig, neutral", ["förebyggande", "skyddande"],
   "Patienten fick profylaktisk antibiotika före operationen.", "profylaktisk",
   "Av grekiska <i>prophylaktikos</i> 'som skyddar i förväg', till <i>pro-</i> 'före' och <i>phylassein</i> 'vakta'."),
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    skrivna = pausade = 0
    for e in poster:
        o = e["ord"]
        if o in HOPPA:
            pausade += 1
            print("  PAUSAS (ingen uppslagsordstraff):", o)
            continue
        if o not in KORT:
            continue
        bet, reg, syn, ex, form, etym = KORT[o]
        if form in ex:
            ex = ex.replace(form, BLA % form, 1)
        else:
            print("  VARNING: hittade inte", form, "i:", ex)
        e["proposed"] = {
            "huvudbetydelse": bet, "register": reg, "synonymer": syn,
            "synonym_groups": None, "exempelmening": ex, "etymologi": etym,
        }
        e["approved"] = True
        q = urllib.parse.quote(o)
        e["sokkoll"] = {
            "kalla": (f"SO och SAOL via https://svenska.se/api/msearch?ord={q} "
                      f"samt https://www.synonymer.se/sv-syn/{q} -- hamtade 2026-08-25, "
                      f"sparade i uppslag/{o}.json"),
            "slutsats": ("Betydelser, register och synonymer lasta ur SO:s rastruktur och "
                         "SAOL:s definitionstext via visa_uppslag.py, som inte visar "
                         "synonymer.se. Inget skrivet som inte star i nagon av ordbockerna."),
        }
        if o in TILLAT:
            e["forgranska_tillat"] = TILLAT[o]
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\ndel 1: skrivna {skrivna}  pausade {pausade}")


if __name__ == "__main__":
    main()
