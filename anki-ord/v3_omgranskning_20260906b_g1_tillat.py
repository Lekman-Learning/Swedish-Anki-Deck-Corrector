# -*- coding: utf-8 -*-
"""Rattelser och verifierade falsklarm for sats 2, ord 1-20.

En andring i sak (kollekt delas i tva betydelser), en pausning
(spelevinker saknas helt i SO och SAOL) och atta motiverade undantag,
vart och ett provat mot rastrukturen.

Lardom fran sats 1: blindgranskaren underkande brosta och dager DAR JAG
SKRIVIT forgranska_tillat -- mina motiveringar var fel, inte flaggorna.
Darfor ar defaulten har att LAGGA TILL betydelsen nar den ar verklig, och
undantag skrivs bara nar rastrukturen visar att posten saknar egen
definitionstext eller hor till ett annat lemma.
"""
import io, json

FIL = "sessions/session_2026-09-06_v3-omgranskning2.json"

poster = json.load(io.open(FIL, encoding="utf-8"))

T = {
 "dåd": {"betydelse_kan_saknas": (
   "Kontrollerat i RAFILEN (uppslag/dad.json), inte bara i visa_uppslag: SO:s enda "
   "huvudbetydelse ar 'konkret, skadlig handling'. Den enda underbetydelsen har INGEN "
   "definition -- bara en formkommentar med texten 'i sammansattn.', alltsa en "
   "upplysning om ordbildning (illdad, terrordad, stordad), inte en betydelse. SAOL har "
   "likasa ett enda led, 'klandervard garning'. En betydelse ar ratt. Vard att notera: "
   "SO listar idiomet 'bista nagon med rad och dad', som ar den enda ovriga anvandning "
   "dar ordet inte ar negativt -- det ar sannolikt darifran legacys felaktiga 'bragd, "
   "stor bedrift' kom. Idiomet ar dock bundet till just den frasen och ar ingen "
   "sjalvstandig betydelse hos ordet.")},

 "likare": {"betydelse_kan_saknas": (
   "Rastrukturen: SO-LEMMA likare har EN definition ('normalmatt som andra matt jamfors "
   "med', med tillagget 'och justeras efter') och EN underbetydelse med egen "
   "definitionstext ('erkand forebild eller auktoritet') -- tva betydelser. SAOL:s enda "
   "led ('normalmatt som andra matt kan justeras efter') ar samma sak som SO:s forsta och "
   "ar det tredje som rakningen kommer at. Kortet har bada de sanna betydelserna; den "
   "tredje raden legacy hade ('Mattstock i sammansattningar') ar struken just for att den "
   "inte ar en betydelse.")},

 "boken": {
  "frammande_uppslagsord": (
   "De fyra doljda lemmana ar abc-bok, bok, e-bok och sciencefictionbok -- alltsa "
   "substantivet BOK i bestamd form respektive sammansattningar. Uppslagsordet ar "
   "adjektivet 'boken' ('mer an overmogen', om frukt), ett helt annat ord som rakar "
   "sammanfalla med bokens bestamda form. Ingen glosa pa kortet kommer fran "
   "bok-lemmana: hela innehallet ar hamtat ur SO-LEMMA boken (adjektiv) och SAOL:s "
   "'halvskamd'."),
  "betydelse_kan_saknas": (
   "Rakningen pa sju ar summan av bok-lemmanas betydelser (skrift, trad, e-bok, abc-bok "
   "...), se ovan. SO-LEMMA boken (adjektiv) har EN definition, 'mer an overmogen' <<om "
   "frukt>>, utan underbetydelser, och SAOL ett enda led, 'halvskamd'. En betydelse ar "
   "ratt.")},

 "snärj": {
  "frammande_uppslagsord": (
   "Det doljda lemmat ar VERBET snarja, som uppslagsordet snarj ar bildat till (SO:s "
   "etymologi: 'till 1snarja 3'). Det ar ordets ursprung, inte ett frammande ord, men "
   "dess betydelser (trassla in, forvirra, fanga djur) ar verbets och hor inte pa "
   "substantivkortet."),
  "betydelse_kan_saknas": (
   "Rakningen pa sex innefattar verbet snarjas led (se ovan). For SUBSTANTIVET snarj ger "
   "SO en betydelse ('jakt', vardagligt) och SAOL tva semikolonseparerade led ('snar' och "
   "'jakt, sja'). Kortet har bada SAOL:s -- snarbetydelsen ar den som legacy saknade och "
   "hela skalet till att kortet skrivits om.")},

 "kurra": {"betydelse_kan_saknas": (
   "Rastrukturen visar tva SO-lemman. kurra (substantiv) har EN definition, 'arrest'. "
   "kurra (verb) har EN definition, 'ge ifran sig ett ganska ljust, dampat bullrande "
   "ljud', plus TVA underbetydelser som bada ar markta '(ingen egen definition -- "
   "utvidgning)' -- de ar SAOL:s 'kuttra' och 'om katt: spinna', alltsa samma ljud fran "
   "andra ljudkallor, inte nya betydelser. Tva sanna betydelser, vilket ar vad kortet "
   "har.")},

 "inrättning": {"betydelse_kan_saknas": (
   "Rastrukturen: SO-LEMMA inrattning har TVA definitioner ('(del av) organisation som (i "
   "fasta lokaler) utfor viss typ av tjanster at allmanheten' och 'foremal eller detalj "
   "med viss funktion'). Den forsta bar EN underbetydelse markt '(ingen egen definition "
   "-- utvidgning)', som ar det tredje som rakningen kommer at. Tva sanna betydelser, "
   "vilket ar vad kortet har.")},

 "intagande": {
  "frammande_uppslagsord": (
   "De tva doljda lemmana ar verbet INTA och partikelverbet TA IN, som adjektivet "
   "'intagande' ar presensparticip till. Deras betydelser (lagga in, satta sig i "
   "besittning av, storma) ar verbets. Kortets innehall kommer uteslutande ur SO-LEMMA "
   "intagande (adjektiv) 'som vinner spontan sympati' och SAOL:s 'behaglig, "
   "charmerande'."),
  "betydelse_kan_saknas": (
   "Rakningen pa sex ar verbet intas led (se ovan). SO-LEMMA intagande (adjektiv) har EN "
   "definition utan underbetydelser, och SAOL ett led med tva synonymer i samma "
   "betydelse. En betydelse ar ratt."),
  "register_motsager_markning": (
   "Brukligheskommentaren 'nagot formellt' sitter pa VERBET inta, inte pa adjektivet "
   "intagande (se frammande_uppslagsord ovan) -- att 'inta en maltid' ar formellt sager "
   "ingenting om huruvida ett intagande leende ar det. Varken SO-LEMMA intagande eller "
   "SAOL:s 'behaglig, charmerande' bar nagon brukligheskommentar alls, sa neutral "
   "bruklighet ar ratt. Laddningen positiv har direkt stod i bada ('sympati', "
   "'behaglig').")},

 "spont": {"betydelse_kan_saknas": (
   "Rastrukturen: SO-LEMMA spont har EN definition ('utstaende parti pa brada, planka "
   "eller dylikt som vid sammanfogning fors in i en ranna pa en annan brada') och TVA "
   "underbetydelser, bada markta '(ingen egen definition -- utvidgning)'. SAOL:s led "
   "'kantlist och fals pa brada; fog mellan sadana brador' beskriver samma foremal fran "
   "tva hall (listen respektive fogen den bildar) -- kortets definition tacker bada "
   "genom att namna bade listen och rannan den passar i. En betydelse ar ratt.")},
}

# kollekt delas i tva betydelser -- se motivering i slutsatsen nedan.
KOLLEKT = dict(
  hb="Insamling av pengar för välgörenhet vid en gudstjänst ; själva pengarna som samlas in",
  reg="neutral, neutral, religion ; neutral, neutral, religion",
  grp=[["insamling"], ["≈≈ insamlade pengar"]])

n_t = n_p = 0
for e in poster:
    o = e["ord"]
    pr = e.get("proposed")
    if o in T:
        e["forgranska_tillat"] = T[o]
        n_t += 1

    if o == "kollekt" and pr:
        pr["huvudbetydelse"] = KOLLEKT["hb"]
        pr["register"] = KOLLEKT["reg"]
        pr["synonym_groups"] = KOLLEKT["grp"]
        pr["synonymer"] = [s for g in KOLLEKT["grp"] for s in g]
        e["sokkoll"]["slutsats"] += (
            " ANDRAT EFTER FORGRANSKNING: jag hade slagit ihop insamlingen och pengarna till "
            "EN betydelse med motiveringen att SO:s underbetydelse saknar egen definitionstext. "
            "Aterstalt till TVA, som legacy hade. Skalet: i sats 1 underkande blindgranskaren "
            "bade brosta och dager pa exakt den sortens hopslagning, och 'ta upp kollekt' "
            "(handlingen) och 'kollekten racker till en ny orgel' (pengarna) ar tva olika "
            "referenter, inte tva satt att uttrycka samma sak. Nar tvekan rader ar det billigare "
            "att ha betydelsen an att sakna den.")

    # spelevinker pausas: uppslagsordet finns inte i SO eller SAOL.
    if o == "spelevinker":
        e["approved"] = False
        e["pausad_forgranska"] = (
            "uppslagsord_saknas: 0 traffar i SO och SAOL. Trekallskontrollen ger 'traffar: saob' "
            "-- ordet finns bara i den historiska ordboken. Forgranskningen foreslar SPELEVINK, "
            "och det ar sannolikt det ratta: 'spelevink' ar den gangse formen, 'spelevinker' ser "
            "ut som en pluralform eller en felaktig sammandragning som fastnat i decket. Att byta "
            "sjalva uppslagsordet ar inte en granskningsatgard utan ett beslut om vad kortet ska "
            "handla om -- det ar Adams. Kortet ligger kvar suspenderat tills dess. "
            "(OLD-facit finns: '(vard.) upptagsmakare, gamang, filur', sa betydelsen ar inte i "
            "tvivel -- bara ordformen.)")
        n_p += 1

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("tillat: %d, pausade: %d" % (n_t, n_p))
