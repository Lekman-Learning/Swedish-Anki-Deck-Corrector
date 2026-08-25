# -*- coding: utf-8 -*-
"""100-kortsomgangen 2026-08-25 (batch3), del 4 (ord 61-80).

Kallor lasta via visa_uppslag.py -- SO:s rastruktur och SAOL ordagrant,
aldrig synonymer.se. Etymologier ur SO:s historiskaUppgifter.
"""
import json
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-25_v3-batch3.json"
BLA = '<font color="#3498db">%s</font>'

TILLAT = {
 "illegitim": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('som inte erkanns av lagen el. av "
   "allmannare moralregler') och EN underbetydelse MED egen definition ('fodd "
   "utom aktenskapet', markt alderdomligt). Bada star pa kortet."},
 "intressent": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('person eller grupp som gjort ekonomisk "
   "satsning') och EN underbetydelse MED egen definition ('som AVSER att gora "
   "ekonomisk satsning'). Bada star pa kortet."},
 "kongruens": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('fullstandig overensstammelse i storlek "
   "och form'), EN underbetydelse UTAN egen definition, och EN underbetydelse MED "
   "egen definition ('overensstammelse i bojning mellan bestamning och "
   "huvudord'). Bada de definierade star pa kortet."},
 "klamra": {
   "betydelse_kan_saknas":
   "SO har EN huvudbetydelse for lemmat `klamra`: 'hafta med klammer'. SAOL:s "
   "andra led ('angsligt halla sig kvar') ar det reflexiva `klamra sig fast`. "
   "Bada star pa kortet eftersom SAOL for dem under samma uppslagsord.",
   "frammande_uppslagsord":
   "Det dolda fuzzy-lemmat ar `klammer`, substantivet verbet ar bildat till."},
 "lealös": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('slapp i lederna') och EN underbetydelse "
   "MED egen definition ('som har svag karaktar'). Bada star pa kortet."},
 "libation": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('dryckesoffer', i religiosa sammanhang) "
   "och EN underbetydelse MED egen definition ('dryckeslag', skamtsamt el. "
   "hogtidligt). Bada star pa kortet, precis som i SAOL."},
 "likvidera": {"betydelse_kan_saknas":
   "SO har TRE huvudbetydelser ('avveckla som ekonomisk enhet', 'betala skuld', "
   "'gora slut pa') plus underbetydelsen '(lata) avliva'. Alla fyra star pa "
   "kortet."},
 "lavoar": {"betydelse_kan_saknas":
   "SO har EN huvudbetydelse ('storre och finare tvattstall'). SAOL:s andra led "
   "('modernt tvattstall') ar markt 'finl.', alltsa finlandssvenskt bruk av samma "
   "ord -- en regional anvandning, inte en andra betydelse i rikssvenskan."},
 "härbärgera": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('uplata plats at nagon') och EN "
   "underbetydelse UTAN egen definition, alltsa en anvandningsutvidgning."},
 "kapson": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('stark grimma for dressyr av hast') och "
   "EN underbetydelse UTAN egen definition."},
 "knusslig": {"betydelse_kan_saknas":
   "SO definierar cirkulart ('som knusslar'). SAOL ger 'smasnal', vilket ar den "
   "enda raka definitionstexten kallorna erbjuder, och den star pa kortet."},
 "mo": {
   "betydelse_kan_saknas":
   "SO har TVA huvudbetydelser ('grusig, torr slattmark' och 'en kornig "
   "jordart'). Bada star pa kortet, precis som i SAOL.",
   "frammande_uppslagsord":
   "Det dolda fuzzy-lemmat ar ett annat ord som rakar stavas likadant."},
 "kamarilla": {"register_motsager_markning":
   "SO:s markning ar 'vanligen nedsattande', SAOL:s 'ofta nedsatt.'. Kortets "
   "register har just 'nedsattande' i valenspositionen. Flaggan slar pa "
   "reservationerna 'vanligen' och 'ofta', inte pa markningen sjalv."},
 "klamra_reg": {},
}
TILLAT.pop("klamra_reg")

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form, etymologi)
KORT = {
 "genmäla": ("Svara, och därvid ofta ge uttryck för en avvikande åsikt",
   "formell, neutral", ["svara"],
   "Han genmälde att siffrorna inte stämde.", "genmälde",
   "Till <i>genmäle</i>, av <i>gen-</i> 'emot' och <i>mäla</i> 'säga'."),

 "hamstra": ("Samla förråd av varor som det väntas bli brist på, ofta utan hänsyn till det allmänna bästa",
   "neutral, nedsättande", [],
   "Folk började hamstra jäst och mjöl.", "hamstra",
   "Av tyska <i>hamstern</i>, till <i>hamster</i>."),

 "härbärgera": ("Upplåta plats åt någon, för övernattning eller liknande",
   "formell, neutral", ["hysa", "inhysa"],
   "Klostret härbärgerade resenärer över natten.", "härbärgerade",
   "Fornsvenska <i>härbärghera</i>."),

 "illegitim": ("Som inte erkänns av lagen eller av allmänna moralregler ; (ålderdomligt) född utom äktenskapet",
   "formell, negativ", ["olaglig", "oberättigad"],
   "Maktövertagandet betraktades som illegitimt.", "illegitimt",
   "Av latin <i>illegitimus</i>, till <i>in-</i> 'o-' och <i>legitim</i>."),

 "ingress": ("Inledning till en framställning, särskilt till en tidningsartikel och då ofta typografiskt markerad",
   "fackspråklig, neutral", ["inledning"],
   "Ingressen ska sammanfatta hela artikeln.", "Ingressen",
   "Av latin <i>ingressus</i> 'ingång, inträdande', till <i>ingredi</i> 'gå in'."),

 "intressent": ("Person eller grupp som gjort en ekonomisk satsning ; person eller grupp som avser att göra en sådan satsning",
   "fackspråklig, neutral", ["delägare"],
   "Flera intressenter hade anmält sig till budgivningen.", "intressenter",
   ""),

 "kamarilla": ("Inre krets av personer som påverkar en statschefs beslut utan att tillhöra regeringen",
   "formell, nedsättande", [],
   "Kungen styrdes av en kamarilla av gamla vänner.", "kamarilla",
   "Av spanska <i>camarilla</i>, till <i>camara</i> 'rum, kammare'."),

 "kapson": ("Stark grimma för dressyr av häst",
   "fackspråklig, neutral", [],
   "Hon longerade hästen i kapson.", "kapson",
   "Av lågtyska <i>kapsun</i>, via franska av italienska <i>cavezzone</i>, till latin <i>caput</i> 'huvud'."),

 "klamra": ("Häfta samman med klammer ; (om att klamra sig fast) ängsligt hålla sig kvar",
   "neutral, neutral", [],
   "Barnet klamrade sig fast vid sin mamma.", "klamrade",
   ""),

 "knusslig": ("Småsnål",
   "vardaglig, nedsättande", ["småsnål", "snål"],
   "Han var knusslig med både beröm och pengar.", "knusslig",
   ""),

 "kohandel": ("Politisk uppgörelse där båda parter offrar principer för praktiska fördelar",
   "neutral, nedsättande", [],
   "Budgeten var resultatet av en ren kohandel.", "kohandel",
   "Efter tyska <i>Kuhhandel</i> med samma betydelse."),

 "konfundera": ("Göra någon förvirrad så att det märks",
   "ngt ålderdomlig, neutral", ["förbrylla"],
   "Frågan konfunderade honom fullständigt.", "konfunderade",
   "Av latin <i>confundere</i> 'sammangjuta, förvirra'. Besläktat med <i>konfys</i>."),

 "kongruens": ("Fullständig överensstämmelse i storlek och form ; överensstämmelse i böjning mellan bestämning och huvudord",
   "fackspråklig, neutral", ["överensstämmelse"],
   "Trianglarna uppvisar kongruens.", "kongruens",
   "Av latin <i>congruentia</i>, till <i>congruere</i> 'stämma överens'."),

 "korrodera": ("Vara utsatt för korrosion, frätas sönder",
   "fackspråklig, neutral", [],
   "Rören hade korroderat inifrån.", "korroderat",
   "Ur latin <i>corrodere</i> 'gnaga sönder'."),

 "lavoar": ("Större och finare tvättställ, ursprungligen ett bord för löst handfat och vattenkanna",
   "ngt ålderdomlig, neutral", ["kommod"],
   "I hörnet stod en lavoar av marmor.", "lavoar",
   "Av franska <i>lavoir</i> 'tvättstuga, tvättkar', till latin <i>lavare</i> 'tvätta'."),

 "lealös": ("Slapp i lederna ; som har svag karaktär",
   "vardaglig, nedsättande", [],
   "Han hängde lealös över stolsryggen.", "lealös",
   "Dialektalt <i>lealös</i>, till <i>led</i> och <i>-lös</i>."),

 "libation": ("Dryckesoffer i religiösa sammanhang ; (skämtsamt) dryckeslag",
   "litterär, neutral", [],
   "Kvällen slutade i en långdragen libation.", "libation",
   "Av latin <i>libatio</i> med samma betydelse."),

 "ligist": ("Medlem av en samhällsfarlig ungdomsgrupp som vandaliserar snarare än ägnar sig åt organiserad brottslighet",
   "neutral, nedsättande", [],
   "Ligister hade slagit sönder busskuren.", "Ligister",
   "Till <i>liga</i>."),

 "likvidera": ("Avveckla som ekonomisk enhet ; betala en skuld ; göra slut på ; låta avliva",
   "formell, neutral", ["avveckla", "avrätta"],
   "Bolaget likviderades efter konkursen.", "likviderades",
   "Av senlatin <i>liquidare</i> 'göra flytande', till <i>liquidus</i> 'flytande, klar'."),

 "mo": ("Grusig, torr slättmark, ofta bevuxen med tall ; en kornig jordart på gränsen till sand",
   "fackspråklig, neutral", [],
   "Tallskogen växte på torr mo.", "mo",
   "Fornsvenska <i>mo(r)</i> 'sandhed'. Av omdiskuterat ursprung."),
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    skrivna = 0
    for e in poster:
        o = e["ord"]
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
                         "synonymer.se. Etymologin hamtad ur SO:s historiskaUppgifter; "
                         "tom dar SO saknar faltet. Inget skrivet som inte star i "
                         "nagon av ordbockerna."),
        }
        if o in TILLAT:
            e["forgranska_tillat"] = TILLAT[o]
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"del 4: skrivna {skrivna}")


if __name__ == "__main__":
    main()
