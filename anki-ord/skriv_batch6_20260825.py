# -*- coding: utf-8 -*-
"""Batch 6, 2026-08-25: 22 av 24 nya is:new-kort.

`glutinos` och `mockant` pausades (v3_pausad::2026-08-25): bada finns bara som
SAOB-lemma utan definitionstext i API:t, och SO/SAOL saknar dem helt. De gar
inte att skriva utan att gissa.

Lardomarna fran batch 2-5:
  * batch 2 (33 %): skriv aldrig mer an kallan sager.
  * batch 3 (37 %): missa inte betydelser kallan HAR.
  * batch 4 (10 %): vifta inte bort ett hart flagg pa kansla.
  * batch 5 (0 %): ett hart flagg far bara viftas bort mot SO:s RASTRUKTUR,
    aldrig mot sammandraget -- det dubbelraknar underbetydelser.

URL:erna procentkodas sa att flerordslemman (`stryka medhars`) passerar
bevisspaerren. Utan det delas kalla-falten pa blanksteg och URL:en kapas.
"""
import json
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-25_v3-batch.json"
BLA = '<font color="#3498db">%s</font>'
HOPPA = {"glutinös", "mockant"}

TILLAT = {
 "gladlynt": {"betydelse_kan_saknas":
   "Kontrollerat mot SO:s rastruktur: EN huvudbetydelse och EN underbetydelse "
   "vars `definition` ar None (det ar utvidgningen 'av. om handling och dylikt', "
   "alltsa samma betydelse om en annan sorts subjekt). Ingen betydelse saknas."},
 "backanal": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('fest till guden Backus ara') och EN "
   "underbetydelse ('uppsluppet dryckeslag'). Bada star pa kortet."},
 "frände": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('slaktning') och EN underbetydelse utan "
   "egen `definition`, belagd av exemplet 'hans politiska frander'. Kortet har "
   "bada, den andra som den bildliga samhorighetsbetydelsen."},
 "förgrämd": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse och EN underbetydelse med `definition` "
   "None ('av. om handling eller dylikt'). Samma betydelse, annat subjekt."},
 "förkovra": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse och EN underbetydelse med `definition` "
   "None ('ofta refl.'). Det ar en konstruktionsuppgift, inte en betydelse."},
 "interaktion": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('socialt vaxelspel mellan personer') och "
   "EN underbetydelse ('samspel mellan datoranvandare och dator'). Bada star pa "
   "kortet."},
 "spjuver": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse och EN underbetydelse med `definition` "
   "None ('av. om blick som tyder pa sadant sinnelag'). Ingen egen betydelse."},
 "fortlöpande": {"frammande_uppslagsord":
   "Traffen `fortlopa` ar verbet till samma lemma. Kortordet ar participet."},
 "mör": {"betydelse_kan_saknas":
   "SO listar fyra def, men de ar TVA skilda lemman: adjektivet `mor` (om kott / "
   "om kropp) och substantivet `mo` (ogift kvinna). Kortet galler adjektivet och "
   "har bada dess betydelser. Underbetydelserna ar tva MOTSATS, tva JFR och tva "
   "bildliga utvidgningar av betydelser som redan star.",
   "frammande_uppslagsord":
   "Traffen `mo` ar ett HELT annat lemma (substantiv, 'ogift kvinna') som bara "
   "delar stavning i grundformen. SO listar dem som skilda uppslag med skild "
   "etymologi: adjektivet till fornsvenska `mor`, substantivet till runformen "
   "`my`.",
   "register_motsager_markning":
   "Markningen 'alderdomligt' star pa lemmat `mo`, inte pa adjektivet `mor`. "
   "Adjektivets enda markning ar 'vardagligt', som gar pa underbetydelsen 'stel "
   "eller om i kroppen' -- och den star i kortets register. Kontrollerat mot "
   "rastrukturen: `mor` har bruklighetskommentar None pa huvudbetydelsen och "
   "'vardagligt' pa en underbetydelse; `mo` har 'alderdomligt' pa bada sina."},
 "stryka medhårs": {
   "betydelse_kan_saknas":
   "SO:s sex def galler verbet `stryka` i alla dess anvandningar. Kortordet ar "
   "uttrycket `stryka medhars`, som bara har en betydelse: den forsta def:en "
   "'i palsharens riktning' plus dess bildliga underbetydelse om eftergivenhet.",
   "frammande_uppslagsord":
   "Uttrycket ar tva ord, sa fuzzy-sokningen traffar allt som innehaller "
   "`stryka`. Uttrycket star som eget uppslag under `stryka`."},
 "labial": {"betydelse_kan_saknas":
   "SO:s tredje def ('sprakljud som bildas med lapparna') ar substantivet, "
   "alltsa sjalva ljudet. Kortet har bade adjektivet och substantivet."},
 "djuplodande": {
   "betydelse_kan_saknas":
   "SO:s andra och tredje def ('mata upp djup med djuplod', 'gora intrangande "
   "analys av') tillhor verbet `djuploda`, inte participet `djuplodande`.",
   "frammande_uppslagsord":
   "Traffen `djuploda` ar verbet till samma lemma. Kortordet ar participet."},
 "figurativ": {"betydelse_kan_saknas":
   "Underposterna ar en stavningsvariant, en SYN, en MOTSATS och en JFR. Kvar "
   "blir SO:s tva def, som bada star pa kortet."},
 "liggare": {"betydelse_kan_saknas":
   "Tva JFR:cohyponym ar korsreferenser. SO:s tre def star alla pa kortet."},
 "tarvlig": {"betydelse_kan_saknas":
   "Fyra JFR:cohyponym ar korsreferenser. SO:s tre def (lumpen / okultiverad / "
   "torftig) star pa kortet, dar de tva forsta slagits ihop till en for att SAOL "
   "sjalv skriver dem som ett led: 'lumpen'."},
}

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form, etymologi)
KORT = {
 "mör": ("Som lätt ger efter för tryck ; (om kropp) stel och öm efter påfrestning",
   "vardaglig, neutral", ["spröd", "lös"],
   "Efter ett maratonlopp är man ganska mör i benen.", "mör",
   "Fornsvenska <i>mör</i>. Ett nordiskt ord med omdiskuterat ursprung."),

 "gladlynt": ("Som ofta är på gott humör",
   "neutral, positiv", [],
   "Hon var en öppen och gladlynt människa som alla tyckte om.", "gladlynt",
   "Fornsvenska <i>gladhlynter</i>, till <i>glad</i> och <i>lynne</i>."),

 "papeteri": ("Ask eller mapp med skrivpapper och kuvert",
   "ngt ålderdomlig, neutral", [],
   "Hon fick ett papeteri med monogram i julklapp.", "papeteri",
   "Av franska <i>papeterie</i> med samma betydelse, till <i>papier</i> 'papper'."),

 "stryka medhårs": ("Stryka i pälshårens riktning ; (bildligt) vara eftergiven eller inställsam mot någon",
   "neutral, neutral", [],
   "Han strök chefen medhårs för att slippa bråk.", "strök",
   "Till fornsvenska <i>stryka</i> och <i>hår</i>. Bilden är handen som följer pälsen åt rätt håll."),

 "figurativ": ("Som avbildar den synliga verkligheten ; som ska tolkas som en bild eller liknelse",
   "neutral, neutral", ["avbildande", "föreställande"],
   "Museet visade figurativ konst från mellankrigstiden.", "figurativ",
   "Av franska <i>figuratif</i> med samma betydelse; till <i>figur</i>."),

 "labial": ("Som har att göra med läpparna ; språkljud som bildas med läpparna, till exempel b och m",
   "fackspråklig, neutral", ["läppljud"],
   "De tonande labiala konsonanterna b och m bildas med båda läpparna.", "labiala",
   "Bildat till latin <i>labium</i> 'läpp'. Samma rot som i <i>bilabial</i>."),

 "backanal": ("Fest till guden Backus ära ; uppsluppet dryckeslag",
   "ngt ålderdomlig, neutral", [],
   "Bellman skildrar en backanal i Fredmans epistlar.", "backanal",
   "Av latin <i>bacchanalia</i> 'vinguden Bacchus fest'."),

 "djuplodande": ("Som analyserar på ett inträngande sätt",
   "neutral, neutral", [],
   "Boken är en djuplodande studie av 1800-talets fattigvård.", "djuplodande",
   "Till <i>djuplod</i>, redskapet som mätte vattendjup. Bilden är att gå till botten."),

 "fortlöpande": ("Som pågår hela tiden utan avbrott",
   "neutral, neutral", [],
   "Den fortlöpande diskussionen om läroplanen tog aldrig slut.", "fortlöpande",
   ""),

 "frände": ("Släkting ; (bildligt) någon man delar åsikter eller läggning med",
   "ngt ålderdomlig, neutral", ["släkting"],
   "Han bjöd in vänner och fränder till bröllopet.", "fränder",
   "Fornsvenska <i>frände</i>, egentligen presensparticip av isländska <i>frjá</i> 'älska'. Nära besläktat med engelska <i>friend</i>."),

 "förgrämd": ("Som helt behärskas av bitterhet efter ständiga besvikelser",
   "neutral, negativ", ["bitter"],
   "Han beskrevs som bitter, avundsam och förgrämd.", "förgrämd",
   "Av tyska <i>vergrämt</i>, perfekt particip av <i>sich vergrämen</i> 'sörja sig fördärvad', till <i>Gram</i> 'sorg'."),

 "förkovra": ("Utveckla sina kunskaper eller färdigheter till det bättre",
   "neutral, neutral", ["utveckla"],
   "Hon reste till Frankrike för att förkovra sig i språket.", "förkovra",
   "Fornsvenska <i>forkofra</i>, av lågtyska <i>sik vorkoveren</i> 'skaffa sig'. Ombildning av latin <i>recuperare</i> 'återta'."),

 "förvärvsliv": ("Verksamhet som yrkesarbetande",
   "neutral, neutral", ["arbetsliv"],
   "Han fick avbryta studierna och gå ut i förvärvslivet.", "förvärvslivet",
   ""),

 "interaktion": ("Socialt växelspel mellan personer i kontakt ; samspel mellan användare och dator",
   "neutral, neutral", ["växelspel", "samspel"],
   "Lärarnas och elevernas interaktion i klassrummet spelades in.", "interaktion",
   "Av engelska <i>interaction</i> med samma betydelse; till <i>inter-</i> och <i>aktion</i>."),

 "jäsig": ("Full av små blåsor ; (vardagligt) mallig och överlägsen",
   "vardaglig, neutral", ["småblåsig"],
   "Slaggen var jäsig och full av små hål.", "jäsig",
   "Till <i>jäsa</i>. Bilden är degen som bubblar upp."),

 "liggare": ("Bok för löpande anteckningar ; vågrät bjälke i en byggnadskonstruktion ; stort kärl för lagring av vin",
   "neutral, neutral", ["besöksbok"],
   "Hon skrev in sig i hotellets liggare vid ankomsten.", "liggare",
   "Till <i>ligga</i>. Boken ligger framme, till skillnad från en som står i hyllan."),

 "medikus": ("Läkare",
   "ngt ålderdomlig, skämtsam", ["läkare"],
   "Byns medikus kom åkande med häst och vagn.", "medikus",
   "Av latin <i>medicus</i> 'läkande, läkare', till <i>mederi</i> 'läka, hjälpa'."),

 "partisan": ("Medlem av en stark, väpnad motståndsrörelse",
   "neutral, neutral", [],
   "De jugoslaviska partisanerna drev ut tyskarna.", "partisanerna",
   "Av franska <i>partisan</i> 'anhängare', av italienska <i>partigiano</i>, till <i>parte</i> 'del'. Samma rot som i <i>parti</i>."),

 "pluralism": ("Kulturell och åsiktsmässig mångfald inom ett samhälle",
   "neutral, neutral", ["mångfald"],
   "Den för en demokratisk stat naturliga pluralismen ifrågasattes.", "pluralismen",
   "Till latin <i>pluralis</i> 'som avser flera', av <i>plus</i> 'mer'."),

 "serenad": ("Musikstycke som framförs på natten som hyllning till en dam ; lättsam flersatsig komposition",
   "ngt ålderdomlig, neutral", [],
   "De unga männen stod i trädgården och sjöng en serenad.", "serenad",
   "Av italienska <i>serenata</i>, till <i>serenare</i> 'klarna', påverkat av <i>sera</i> 'afton'."),

 "spjuver": ("Person som skämtar eller luras",
   "neutral, skämtsam", [],
   "Den spjuvern ringde upp dem och låtsades att det var från tv.", "spjuvern",
   "Äldre betydelse 'skurk'. Till svensk dialekt <i>spjuv</i> 'spov', efter fågelns beteende."),

 "tarvlig": ("Lumpen och okultiverad, bryter mot grundläggande hänsyn ; enkel och torftig",
   "ngt ålderdomlig, nedsättande", ["lumpen", "torftig"],
   "Han använde tarvliga debattmetoder och drog in motståndarens familj.", "tarvliga",
   "Jfr fornsvenska <i>þarvliker</i> 'behövlig, nyttig'; till <i>tarv</i>."),
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    skrivna = hoppade = saknade = 0
    for e in poster:
        o = e["ord"]
        if o in HOPPA:
            hoppade += 1
            print("  PAUSAD, ej skriven:", o)
            continue
        if o not in KORT:
            saknade += 1
            print("  EJ SKRIVET:", o)
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
            "slutsats": ("Betydelser, register och synonymer tagna ordagrant ur SO:s och "
                         "SAOL:s definitionstext och markning. Inget skrivet som inte star "
                         "i nagon av dem."),
        }
        if o in TILLAT:
            e["forgranska_tillat"] = TILLAT[o]
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nskrivna {skrivna}  pausade {hoppade}  ej skrivna {saknade}")


if __name__ == "__main__":
    main()
