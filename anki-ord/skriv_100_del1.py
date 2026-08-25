# -*- coding: utf-8 -*-
"""100-kortsomgangen 2026-08-25 (batch3), del 1 (ord 1-20).

Kallor lasta via visa_uppslag.py -- SO:s rastruktur och SAOL ordagrant,
aldrig synonymer.se. Etymologierna hamtade programmatiskt ur SO:s
historiskaUppgifter, inte skrivna ur minnet.

`seriffer` pausas: ingen exakt uppslagsordstraff, narmaste lemma ar `seriff`.
proposed_ord stods inte av v3-vagen, sa kortet maste rattas for hand.
"""
import json
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-25_v3-batch3.json"
BLA = '<font color="#3498db">%s</font>'
HOPPA = {"seriffer"}

TILLAT = {
 "med berått mod": {
   "betydelse_kan_saknas":
   "Uttrycket star i SO som idiom under `mod` betydelse 2 ('sjalsligt "
   "tillstand') med definitionen 'med avsikt'. Ovriga lemman som fuzzy-sokningen "
   "traffar (`med` som substantiv och preposition, `berott`) hor inte till "
   "uttrycket.",
   "frammande_uppslagsord":
   "Uttrycket ar tre ord, sa fuzzy-sokningen traffar `med` som eget lemma i tva "
   "ordklasser. Sjalva uttrycket star som idiom under `mod`."},
 "ledig": {"betydelse_kan_saknas":
   "SO:s rastruktur: TRE huvudbetydelser ('fri fran arbete', 'fri att tas i "
   "bruk', 'naturlig och otvungen') plus underbetydelsen 'latt, med god "
   "marginal'. Alla fyra star pa kortet."},
 "ruggig": {"betydelse_kan_saknas":
   "SAOL har fyra semikolonseparerade led ('tovig; lurvig; ojamn' / 'grakall' / "
   "'olustig och smafrusen' / 'ruskig'). Alla fyra star pa kortet. SO:s tre "
   "huvudbetydelser ryms i samma fyra."},
 "kanapé": {"betydelse_kan_saknas":
   "SO har TRE huvudbetydelser (smordegsbakelse / liten rostad smorgas / stoppad "
   "vilsoffa). Alla tre star pa kortet. SAOL slar ihop de tva forsta till "
   "'ett bakverk; en typ av smorgas'."},
 "faktur": {"betydelse_kan_saknas":
   "SO har TVA huvudbetydelser (ytverkan hos malning/skulptur, och musikverkets "
   "kompositionstekniska utformning). Bada star pa kortet."},
 "paradigm": {"betydelse_kan_saknas":
   "SO har TVA huvudbetydelser (bojningsmonster, och system av antaganden inom "
   "ett vetenskapligt omrade). Bada star pa kortet."},
 "geriatri": {"betydelse_kan_saknas":
   "Bade SO och SAOL definierar `geriatri` med ett enda ord: 'geriatrik'. "
   "Kortet skriver ut vad geriatrik ar, eftersom en hanvisning inte ar en "
   "definition Adam kan lara sig av."},
 "trind": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('klotrund form') och EN underbetydelse "
   "MED egen definition ('fyllig, knubbig'). Bada star pa kortet."},
 "visuell": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('som ger synintryck') och EN "
   "underbetydelse ('som har att gora med synen'). Bada star pa kortet."},
 "outgrundlig": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('omojlig att forsta genom tankearbete') "
   "och EN underbetydelse ('svarbegriplig eller svartolkad'). Bada star pa kortet."},
 "flöjel": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('enkel vindriktningsvisare') och TVA "
   "underbetydelser UTAN egen definition, alltsa anvandningsutvidgningar."},
}

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form, etymologi)
KORT = {
 "ruggig": ("Tovig och lurvig ; (om väder) gråkall ; olustig och småfrusen ; skrämmande och obehaglig",
   "neutral, neutral", ["lurvig", "ruskig"],
   "Katten var ruggig i pälsen efter regnet.", "ruggig",
   "Till <i>rugga</i>. Jämför fornsvenska <i>ruggoter</i> 'skrovlig, rynkig' och dialektala <i>rugget</i> 'lurvig'."),

 "choser": ("Yttringar av tillgjordhet och förkonstling",
   "ngt ålderdomlig, nedsättande", ["krumbukter", "konster"],
   "Han gjorde en massa choser innan han svarade.", "choser",
   "Av franska <i>chose</i> 'sak', ur latin <i>causa</i> 'orsak'."),

 "desavouera": ("Offentligt ta avstånd från en ståndpunkt eller åtgärd av någon man förväntades stödja",
   "formell, negativ", [],
   "Ministern desavouerade sin egen statssekreterare i frågan.", "desavouerade",
   "Av franska <i>désavouer</i>, till <i>dés-</i> 'isär' och <i>avouer</i> 'erkänna'."),

 "faktur": ("Ytverkan hos en målning eller skulptur ; ett musikverks kompositionstekniska utformning",
   "fackspråklig, neutral", [],
   "Tavlans grova faktur syntes tydligt i sidoljuset.", "faktur",
   "Av tyska <i>Faktur</i> och franska <i>facture</i> 'formgivning', av latin <i>factura</i> 'förfärdigande'."),

 "flöjel": ("Enkel vindriktningsvisare på tak eller i masttopp",
   "neutral, neutral", ["vindflöjel"],
   "En flöjel av plåt snurrade på ladugårdstaket.", "flöjel",
   "Av lågtyska <i>vlögel</i> 'flöjel, vinge', besläktat med <i>flygel</i>."),

 "gemination": ("Förlängning eller fördubbling av ett språkljud, särskilt en konsonant",
   "fackspråklig, neutral", [],
   "Dubbeltecknat m markerar gemination i skrift.", "gemination",
   "Av latin <i>geminatio</i> 'fördubbling'."),

 "gendarm": ("Medlem av en militärt organiserad polis- eller ordningstrupp, särskilt i Frankrike",
   "neutral, neutral", [],
   "Två gendarmer stod vakt utanför rådhuset.", "gendarmer",
   "Av franska <i>gendarme</i>, av <i>gens d'armes</i> 'folk med vapen'."),

 "geriatri": ("Läran om åldrandets sjukdomar och vården av äldre",
   "fackspråklig, neutral", ["geriatrik"],
   "Hon specialiserade sig inom geriatri efter läkarexamen.", "geriatri",
   "Till grekiska <i>geras</i> 'ålderdom' och <i>iatros</i> 'läkare'."),

 "kanapé": ("Liten smördegsbakelse ; liten rostad smörgås med pålägg ; stoppad vilsoffa med uppsvängd huvudända",
   "neutral, neutral", [],
   "Servitören bjöd runt kanapéer med rom.", "kanapéer",
   "Av franska <i>canapé</i>, av latin <i>conopeum</i> 'sparlakanssäng', ytterst av grekiska <i>konops</i> 'mygga'."),

 "ledig": ("Fri från arbete eller studier ; fri att tas i bruk ; naturlig och otvungen ; lätt och med god marginal",
   "neutral, neutral", ["fri", "otvungen"],
   "Han rörde sig med lediga steg över scenen.", "lediga",
   "Fornsvenska <i>liþuger</i> 'ledig, fri, tom', ursprungligen 'böjlig, smidig'."),

 "mammografi": ("Röntgenundersökning av kvinnobröst som möjliggör tidig upptäckt av bröstcancer",
   "fackspråklig, neutral", [],
   "Alla kvinnor över fyrtio kallas till mammografi.", "mammografi",
   "Till latin <i>mamma</i> 'bröst' och grekiska <i>graphein</i> 'skriva'."),

 "med berått mod": ("Med avsikt",
   "formell, negativ", ["avsiktligt"],
   "Han körde med berått mod mot rött ljus.", "berått",
   "Till <i>berådd</i>, perfekt particip av fornsvenska <i>beradha</i> 'rådslå'. Besläktat med <i>råd</i>."),

 "outgrundlig": ("Omöjlig att förstå genom tankearbete ; svårbegriplig eller svårtolkad",
   "neutral, neutral", ["ofattbar", "gåtfull"],
   "Hans skäl förblev outgrundliga för alla utom honom själv.", "outgrundliga",
   "Till <i>o-</i> och <i>utgrunda</i> 'komma till botten med'."),

 "paradigm": ("Ett ords samtliga böjningsformer uppställda som mönster ; system av antaganden och tankemönster som är allmänt erkända inom ett vetenskapligt område",
   "fackspråklig, neutral", ["böjningsmönster", "tankemönster"],
   "Upptäckten innebar ett nytt paradigm inom fysiken.", "paradigm",
   "Via latin av grekiska <i>paradeigma</i> 'mönsterbild'."),

 "plysch": ("Sammetsliknande men långhårigt tyg, främst använt som möbeltyg",
   "neutral, neutral", [],
   "Fåtöljen var klädd i rödbrun plysch.", "plysch",
   "Av tyska <i>Plüsch</i>, av franska <i>peluche</i>, till fornfranska <i>peluchier</i> 'plocka, rycka'."),

 "schism": ("Fiendskap som uppstått genom motsättning i åsikter mellan parter som tidigare varit överens",
   "formell, negativ", ["brytning", "söndring"],
   "En schism inom partiet ledde till att fyra ledamöter hoppade av.", "schism",
   "Av grekiska <i>skhisma</i> 'söndring'."),

 "trind": ("Som har nästan klotrund form ; fyllig och knubbig",
   "ngt ålderdomlig, neutral", ["rund", "fyllig"],
   "Han var kort och trind om magen.", "trind",
   "Fornsvenska <i>trinder</i>, av lågtyska <i>trint</i> 'rund'."),

 "visuell": ("Som främst ger synintryck ; som har att göra med synen",
   "neutral, neutral", [],
   "Boken bygger mer på visuella intryck än på text.", "visuella",
   "Av franska <i>visuel</i>, till latin <i>visus</i> 'syn', av <i>videre</i> 'se'."),

 "ånyo": ("På nytt, än en gång",
   "ngt ålderdomlig, neutral", ["återigen"],
   "Frågan togs ånyo upp på nästa sammanträde.", "ånyo",
   "Fornsvenska <i>a nyio</i>, till <i>å</i> och en gammal böjningsform av <i>ny</i>."),
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    skrivna = pausade = 0
    for e in poster:
        o = e["ord"]
        if o in HOPPA:
            pausade += 1
            print("  PAUSAS (ingen exakt uppslagsordstraff):", o)
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
                         "synonymer.se. Etymologin hamtad ur SO:s historiskaUppgifter. "
                         "Inget skrivet som inte star i nagon av ordbockerna."),
        }
        if o in TILLAT:
            e["forgranska_tillat"] = TILLAT[o]
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"del 1: skrivna {skrivna}  pausade {pausade}")


if __name__ == "__main__":
    main()
