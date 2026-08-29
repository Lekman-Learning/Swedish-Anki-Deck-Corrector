# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch100, kort 1-25. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch100.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
B = '<font color="#3498db">%s</font>'


def kallor(o, *extra):
    k = urllib.parse.quote(o)
    return " ".join([
        "https://svenska.se/api/msearch?ord=%s" % k,
        "https://www.synonymer.se/sv-syn/%s" % k,
        "https://sv.wiktionary.org/wiki/%s" % k,
        *extra,
    ])


def satt(o, bet, reg, syn, ex, ety, slutsats, grupper=None, extra=(), conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": grupper, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": kallor(o, *extra), "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True


satt("fistel",
     "Onaturlig gång som bildats i kroppen vid sjukdom, mellan två organ "
     "eller ut till huden",
     "fackspråklig, neutral, medicin",
     [],
     "Efter operationen bildades en " + B % "fistel" + " mellan tarmen och "
     "huden.",
     "→ Latin fistula 'rör, pipa' — en gång i kroppen som inte ska finnas.",
     "SO: 'icke-anatomisk kanal i kroppen'. SAOL: 'onaturlig kanal i "
     "kroppen t.ex. fran varharde'. OLD-facit 'onormal kanal i kroppen' "
     "stammer men sager inte att den gar mellan tva stallen -- det ar "
     "poangen med ordet och ar inskrivet. SO:s JFR (tandfistel, tarmfistel) "
     "ar sammansattningar, inte synonymer.")

satt("moaré",
     "Tyg med skimrande vågmönster ; själva vågmönstret",
     "neutral, neutral, allmän ; neutral, neutral, allmän",
     [],
     "Hon bar en klänning i svart " + B % "moaré" + " som skiftade i ljuset.",
     "→ Franska moiré, till moirer 'vattra'; slaktingar med mohair.",
     "SO: 'typ av vavnad med vattrad yta', med underbetydelsen 'av. om "
     "vattrat monster'. SAOL: 'vattrat tyg el. monster'. Bada betydelserna "
     "ar med. Ordet 'vattrad' ar sjalvt for svart och ar ersatt med "
     "'skimrande vagmonster' enligt Adam-tal. OLD-facit 'ett slags "
     "tygmonstereffekt' missar att moare ocksa ar sjalva tyget.")

satt("opinion",
     "Den åsikt som en stor grupp människor delar i en fråga ; också om "
     "själva gruppen som tycker så",
     "neutral, neutral, allmän ; neutral, neutral, allmän",
     ["folkmening"],
     "Det fanns en stark " + B % "opinion" + " mot att lägga ner sjukhuset.",
     "→ Latin opinio 'mening, tro'.",
     "SO: 'gemensam asikt hos storre grupp manniskor', med underbetydelsen "
     "'av. med tanke pa gruppen' (SO:s exempel 'blidka opinionen'). Bada "
     "med. Synonymen folkmening star i SAOL:s definitionstext: 'allman "
     "mening, folkmening'. OLD-facit markte ordet (pol.) -- SO ger ingen "
     "sadan domanmarkning, och opinion anvands lika garna om annat an "
     "politik, sa markningen ar struken.")

satt("praxis",
     "Det sätt något brukar göras på, som blivit den vanliga ordningen utan "
     "att stå skrivet någonstans ; inom juridiken: hur domstolarna faktiskt "
     "brukar döma i liknande fall",
     "neutral, neutral, allmän ; fackspråklig, neutral, juridik",
     ["bruk"],
     "Det är " + B % "praxis" + " att en ordförande som förlorar sin "
     "majoritet avgår.",
     "→ Grekiska praxis 'handling'; samma rot som praktisk.",
     "SO: 'vedertaget handlingsmonster'. SAOL lagger till den juridiska "
     "betydelsen: 'vedertaget bruk; rattssedvanja; praktik'. Synonymen bruk "
     "star i SAOL:s definitionstext. SO:s JFR (bruk 2, sedvanja) ar "
     "cohyponymmarkta och raknas inte som synonymbevis -- bruk kom in via "
     "SAOL, inte via JFR. Ordet 'vedertagen' ar for svart och ar upplost i "
     "klartext.")

satt("sinus",
     "I matematiken: en av grundfunktionerna i trigonometrin, som kopplar "
     "en vinkel till förhållandet mellan två sidor i en rätvinklig triangel "
     "; i kroppen: ett hålrum eller en utbuktning, till exempel bihålorna i "
     "skallbenet",
     "fackspråklig, neutral, matematik ; fackspråklig, neutral, medicin",
     [],
     B % "Sinus" + " för 30 grader är exakt 0,5.",
     "→ Latin sinus 'veck, vik'; samma rot som insinuera.",
     "SO ger tva helt skilda betydelser: 'en grundlaggande trigonometrisk "
     "funktion' och 'utbuktning eller halrum i kroppen'. SAOL bekraftar "
     "bada. OLD-facit hade BARA kroppsbetydelsen ('halrum i kroppen') -- "
     "matematikbetydelsen ar den vanligaste och saknades helt. JFR "
     "(cosinus, tangens) ar cohyponymer, inte synonymer.")

satt("bjärt",
     "Om färg: så stark och skrikig att den sticker i ögonen ; bildligt om "
     "en skillnad: så skarp att den är omöjlig att missa",
     "neutral, neutral, allmän ; neutral, neutral, allmän",
     ["gräll"],
     "Fallskärmsavtalen stod i " + B % "bjärt" + " kontrast till sparkraven "
     "på alla andra.",
     "→ Fornsvenska biärter 'lysande, grann'; gemensamt germanskt ord, "
     "belagt pa runsten fran 1000-talet.",
     "SO ger tva betydelser: 'som framtrader starkt for synsinnet' och "
     "'mycket skarp och tydlig' (ofta bildligt, SO:s exempel 'bjart "
     "kontrast'). Synonymen grall star i SAOL:s definitionstext ('grallt "
     "lysande') -- inte bara som JFR i SO. OLD-facit 'farggrann, grall, "
     "iogonfallande' tackte bara farg och missade den bildliga anvandningen "
     "som ar den vanligaste i skrift.")

satt("akribi",
     "Ytterst noggrann kontroll av varje uppgift och varje hänvisning i "
     "vetenskapligt arbete",
     "formell, neutral, allmän",
     [],
     "En forskare med lysande idéer men bristande " + B % "akribi" + ".",
     "→ Grekiska akribeia 'noggrannhet, punktlighet'.",
     "SO och SAOL ger samma definition: 'vetenskaplig noggrannhet'. SO "
     "markning: formellt -- darav registret. Inga synonymer foreslagna: "
     "noggrannhet ar ett bredare ord (akribi galler specifikt "
     "kallhantering i vetenskapligt arbete), inte utbytbart. OLD-facit "
     "'vetenskaplig noggranhet' var korrekt men felstavat och sager inte "
     "VAD man ar noggrann med.")

satt("alltjämt",
     "Fortfarande, om något som har pågått länge och ännu inte upphört",
     "neutral, neutral, allmän",
     ["fortfarande", "ännu"],
     "Hon bor " + B % "alltjämt" + " kvar i huset hon växte upp i.",
     "→ Fornsvenska alt iämpt 'standigt'; belagt sedan 1484.",
     "SO: 'fortfarande', med SYN-markering mot annu. SAOL: 'fortfarande'. "
     "Bada synonymerna ar alltsa belagda i definitionstexten respektive som "
     "SYN, inte som JFR. Ingen bruklighetsmarkning i SO eller SAOL, sa "
     "registret ar neutralt -- ordet KANNS aldrigt men det ar inte belagt "
     "och far inte hittas pa.")

satt("cyklop",
     "I grekisk mytologi: en jätte med ett enda öga mitt i pannan ; "
     "dykarmask som täcker både ögon och näsa",
     "neutral, neutral, allmän ; neutral, neutral, allmän",
     [],
     "Odysseus lyckades blända " + B % "cyklopen" + " med en glödgad påle.",
     "→ Grekiska kyklops, av kyklos 'cirkel' och ops 'oga'.",
     "SO ger tva betydelser: 'enogd jatte' och 'cyklopoga', dvs. dykmasken "
     "(SO:s exempel: 'setet innehaller cyklop, snorkel och ett par "
     "simfotter'). SAOL bekraftar bada. OLD-facit 'enogd sagojatte' hade "
     "bara den forsta. JFR (gigant, jatte, turs) ar cohyponymer respektive "
     "overordnat ord -- inga synonymer.")

satt("defilera",
     "Marschera förbi någon förnäm i ordnade led för att visa aktning ; "
     "bildligt: ta sig i mål med så stor ledning att det kan ske i lugn och "
     "ro",
     "neutral, neutral, militär ; neutral, neutral, sport",
     [],
     "Trupperna " + B % "defilerade" + " förbi kungens kista.",
     "→ Franska défiler 'ga i rad', till file 'rad'; samma rot som fil.",
     "SO: 'marschera (forbi hogt uppsatt person) som hedersbetygelse', med "
     "underbetydelsen 'av. bildligt, sarsk. i uttryck for overlagsen seger' "
     "(SO:s exempel: 'han var en hel kurva fore och kunde defilera in i "
     "mal'). Bada med. OLD-facit hade bara 'marschera forbi' och missade "
     "att det ska ske INFOR nagon och som hedersbetygelse -- det ar hela "
     "skillnaden mot att bara ga forbi.")

satt("diligens",
     "Täckt hästdragen vagn som förr gick i fast turlista med post och "
     "resenärer",
     "neutral, neutral, historia",
     [],
     "Banditerna rånade " + B % "diligensen" + " på vägen mot Lyon.",
     "→ Franska (voiture de) diligence, ursprungligen 'hastighet' -- "
     "vagnen som gick efter tidtabell; av latin diligentia 'noggrannhet'.",
     "SO: 'tackt hastdragen vagn for befordran av passagerare och post'. "
     "SO:s markning: historiskt -- darav doman historia. OLD-facit "
     "'postvagn' var for smalt: diligensen tog bade post OCH passagerare, "
     "och det ar tidtabellen som skiljer den fran vilken vagn som helst.")

satt("fjär",
     "Som håller andra på avstånd med en min av att vara förmer än de",
     "ngt ålderdomlig, lätt negativ, allmän",
     ["högdragen", "avvisande"],
     "Hon var " + B % "fjär" + " mot alla som försökte närma sig henne.",
     "→ Franska fier 'vild, stolt'; av latin ferus 'vild'.",
     "SO: 'hogdraget avvisande'. SAOL: 'hogdragen; avvisande'. Bada "
     "synonymerna star i definitionstexten. SO:s markning: nagot "
     "alderdomligt -- darav registret. OLD-facit 'stolt och hogdragen' "
     "missar avvisandet, som ar den halva av ordet som handlar om hur man "
     "beter sig mot andra.")

satt("getto",
     "Förr: den avskilda stadsdel dit judar tvingades flytta ; i dag: ett "
     "isolerat och nedgånget bostadsområde där nästan alla tillhör samma "
     "grupp",
     "neutral, neutral, historia ; neutral, nedsättande, allmän",
     [],
     "Upproret i Warszawas " + B % "getto" + " slogs ner efter en månad.",
     "→ Troligen italienska ghetto, efter Ghetto, namnet pa en stadsdel i "
     "Venedig.",
     "SO: '(isolerat och forslummat) stadsomrade med enhetlig befolkning', "
     "med underbetydelsen 'av. nagot utvidgat, enbart med betoning av "
     "social enhetlighet'. SAOL skiljer tydligare pa den historiska judiska "
     "betydelsen och den moderna bildliga -- den uppdelningen ar foljd har. "
     "SO markning: nedsattande, vilket galler den moderna betydelsen. "
     "OLD-facit 'isolerat bostadsomrade' saknade helt den historiska "
     "betydelsen, som ar ordets ursprung.")

satt("inuit",
     "Person som tillhör urbefolkningen på Grönland, i norra Kanada, Alaska "
     "och nordöstra Ryssland",
     "neutral, neutral, allmän",
     [],
     "Många " + B % "inuiter" + " på Grönland lever fortfarande av jakt och "
     "fiske.",
     "→ Inuit ar pluralformen av inuk 'manniska' pa gronlandska.",
     "SO: 'person tillhorande nagon av flera folkgrupper i bl.a. Gronland, "
     "Alaska och Ryssland'. SAOL: 'urinvanare i bl.a. Gronland och Alaska'. "
     "VIKTIG RATTELSE: OLD-facit sa bara 'eskima'. Det ordet undviks i dag "
     "och ar inte det inuiterna sjalva anvander -- det ar precis darfor "
     "ordet inuit finns i sprakbruket. Facit ar helt omskrivet. SO:s JFR "
     "gronlandare ar en cohyponym (en delgrupp), inte en synonym.")

satt("kitt",
     "Seg massa som stelnar och används för att täta springor, till exempel "
     "runt en fönsterruta ; bildligt: det som håller ihop en grupp eller ett "
     "samhälle",
     "neutral, neutral, teknik ; neutral, neutral, allmän",
     [],
     "Religionen var det " + B % "kitt" + " som höll ihop landet.",
     "→ Tyska Kitt; slakt med latin bitumen 'beck'; samma rot som kada.",
     "SO: 'en degartad massa som anvands for tatning och spackling', med "
     "underbetydelsen 'ibland bildligt' -- SO:s enda exempelmening ar just "
     "den bildliga. SAOL: 'en massa for tatning av t.ex. fonster; av. "
     "bildl.' Bada betydelserna ar med. OLD-facit 'tatningsmassa' hade bara "
     "den bokstavliga.")

satt("kursiv",
     "Om text: skriven med bokstäver som lutar åt höger ; om läsning: snabb "
     "och översiktlig, utan att gå in på detaljer ; som substantiv: själva "
     "den högerlutande stilsorten",
     "neutral, neutral, allmän ; neutral, neutral, allmän ; neutral, "
     "neutral, allmän",
     [],
     "Några av uppsatserna på litteraturlistan kan läsas " + B % "kursivt" +
     ".",
     "→ Franska cursif, av medeltidslatin cursivus 'lopande'; till kurs.",
     "SO ger tre betydelser: den lutande stilen (adjektiv), 'som (snabbt) "
     "fangar innehallet i stora drag men inte gar in pa detaljer' (om "
     "lasning), och sjalva tryckstilen (substantiv). SAOL bekraftar alla "
     "tre. OLD-facit 'om lutande text' hade bara den forsta -- "
     "lasbetydelsen ar den som faktiskt satter dit folk, och exempelmeningen "
     "ar vald for att visa den. JFR oversiktlig ar cohyponymmarkt och "
     "raknas inte som synonym.")

satt("promulgera",
     "Officiellt kungöra att en lag som redan är beslutad nu ska börja gälla",
     "fackspråklig, neutral, juridik",
     ["utfärda"],
     "Alla lagar " + B % "promulgeras" + " av presidenten.",
     "→ Latin promulgare 'ansla, kungora'.",
     "SO:s hela definition ar ett enda ord: 'utfarda' -- darfor ar utfarda "
     "upptaget som synonym (det ar definitionstexten, inte en JFR). SAOL "
     "preciserar: 'utfarda en antagen lag'. Domanmarkningen juridik foljer "
     "av SAOL:s begransning till lagar; nagon bruklighetsmarkning finns "
     "inte i SO, sa formalitetsnivan ar satt till fackspraklig och inte "
     "hogtidlig.")

satt("ratificera",
     "Slutgiltigt godkänna ett färdigförhandlat avtal mellan stater, så att "
     "det börjar gälla",
     "fackspråklig, neutral, juridik",
     [],
     "Kongressen vägrade " + B % "ratificera" + " Versaillesfördraget.",
     "→ Medeltidslatin ratificare 'slutgiltigt faststalla'.",
     "SO: 'gora (preliminar internationell overenskommelse) giltig'. SAOL: "
     "'godkanna fordrag'. Poangen som OLD-facit ('godkanna ett avtal') "
     "missar ar att avtalet redan ar forhandlat och undertecknat -- "
     "ratificeringen ar det sista steget som gor det bindande. SO:s JFR "
     "(bekrafta, parafera, stadfasta) ar cohyponymer: parafera ar tvartom "
     "ett TIDIGARE steg i samma kedja, inte ett utbytbart ord.")

satt("toga",
     "Fornromersk dräkt för män: ett stort tygstycke utan ärmar som lindades "
     "runt kroppen",
     "neutral, neutral, historia",
     [],
     "Senatorerna kom till mötet klädda i vita " + B % "togor" + ".",
     "→ Latin toga, till tegere 'tacka'; samma rot som tak.",
     "SO: 'ett fornromerskt armlost plagg for man, som draperades runt "
     "kroppen'. SAOL: 'fornromersk mantel'. SO har en underbetydelse markt "
     "bara 'av.' utan text -- vad den avser gar inte att lasa ut ur "
     "uppslaget, och den ar darfor INTE gissad in i facit. OLD-facit "
     "'svepande drakt' sager inte att det ar romerskt, vilket ar hela "
     "ordet.")

satt("vrensk",
     "Som spjärnar emot och vägrar följa med i stället för att göra som man "
     "blir tillsagd",
     "neutral, lätt negativ, allmän",
     ["motspänstig"],
     "Hästen var " + B % "vrensk" + " och vägrade gå in i transporten.",
     "→ Fornsvenska vrensker 'vrensk, brunstig'; slakt med dialektens "
     "vrina 'gnagga'; troligen ljudharmande.",
     "SO: 'som (ofta) stretar emot'. Synonymen motspanstig ar SAOL:s hela "
     "definition, alltsa definitionstext och inte JFR. Ingen "
     "bruklighetsmarkning i SO eller SAOL trots att ordet ar sallsynt -- "
     "ingen markning ar darfor pahittad. OLD-facit 'motstravig' stammer.")

satt("varp",
     "I vävning: trådarna som spänns upp på längden i väven och som de "
     "andra trådarna vävs in tvärs igenom ; hög av värdelöst berg som "
     "kastats undan vid gruvbrytning ; draglina till trål eller till ett "
     "mindre ankare",
     "fackspråklig, neutral, allmän ; fackspråklig, neutral, geologi ; "
     "fackspråklig, neutral, sjöfart",
     [],
     "Tyget var rött i " + B % "varpen" + " och svart i inslaget.",
     "→ Jfr islandska och norska varp; gemensamt germanskt ord, nara "
     "beslaktat med varpa. I linbetydelsen fornsvenska varp, eg. 'kast'.",
     "SO ger fem betydelser, som SAOL grupperar i tre: vaven, gruvhogen och "
     "linorna/notdragningen. De tre grupperna ar behallna; SO:s "
     "sardelningar av linorna (tral kontra ankare) ar sammanslagna eftersom "
     "det ar samma sak. OLD-facit hade alla tre men bara som stickord "
     "('langsgaende vavtradar; bergrester; draglina') utan forklaring. "
     "Ordet 'vaft' i SO:s exempel ar utbytt mot 'inslag', som ar den "
     "vanligare termen.")

satt("evinnerlig",
     "Som upprepas så länge och så ofta att man tröttnar på det ; också bara "
     "förstärkande: alldeles oerhört",
     "neutral, lätt negativ, allmän ; vardaglig, neutral, allmän",
     ["evig"],
     "Detta " + B % "evinnerliga" + " tjat om att jag ska klippa mig!",
     "→ Jfr fornsvenska ävinnelikher 'evig'; ytterst till gotiska aiws "
     "'tid'; samma rot som evig.",
     "SO: 'som pa ett trottande satt upprepas under mycket lang tid', med "
     "underbetydelsen 'av. allmant forstarkande, ofta i adverbiell "
     "anvandning' (SO:s exempel: 'jag ar sa evinnerligt trott pa alla dessa "
     "dokusapor'). Bada med. Synonymen evig ar SAOL:s forsta "
     "definitionsord. OLD-facit 'evig' fangar inte det avgorande: "
     "evinnerlig bar nastan alltid irritation, evig gor det inte.")

satt("halvpension",
     "Hotellavtal som ger rummet, frukost och en varm måltid till per dag",
     "neutral, neutral, allmän",
     [],
     "Resan kostade 8 000 kronor med " + B % "halvpension" + ".",
     None,
     "SO: 'inackordering som omfattar logi, frukost och ett huvudmal'. "
     "SAOL: 'inkvartering pa hotell e.d. med frukost och ett huvudmal per "
     "dag'. OLD-facit 'hotellerbjudande' sager ingenting om VAD som ingar, "
     "vilket ar hela ordet -- och det ar precis det som skiljer det fran "
     "helpension (SO:s JFR, en cohyponym och inte en synonym).")

satt("harnesk",
     "Den del av en rustning som skyddar bröstet och överkroppen ; i "
     "uttrycket 'gå i harnesk mot': bli stridslysten och helt avvisande mot "
     "något ; i geologin: en blankslipad yta i berget där två block glidit "
     "mot varandra",
     "ngt ålderdomlig, neutral, historia ; neutral, neutral, allmän ; "
     "fackspråklig, neutral, geologi",
     [],
     "Hon gick i " + B % "harnesk" + " mot varje förslag om förändring.",
     "→ Fornsvenska harnesk, av lagtyska harnesch; av fornfranska harnas "
     "'rustning, utrustning'.",
     "SO: '(del av) rustning', med underbetydelsen 'av. bildligt i uttryck "
     "for helt avvisande installning' (SO:s exempel: 'hon ar i harnesk mot "
     "alla nyheter'). SAOL ger dessutom en geologisk betydelse, 'polerad "
     "glidyta', med markningen geol. Alla tre ar med -- den bildliga ar i "
     "praktiken den enda som anvands i dag. SO:s markning alderdomligt "
     "galler rustningsbetydelsen. JFR (brynja, rustning) ar cohyponym "
     "respektive overordnat ord.")

satt("lymfa",
     "Den klara vätska som finns mellan cellerna i kroppen och som fraktar "
     "näring och avfall mellan blodet och vävnaden",
     "fackspråklig, neutral, medicin",
     [],
     B % "Lymfan" + " samlas upp i egna kärl och leds tillbaka till blodet.",
     "→ Latin lympha 'klart vatten'.",
     "SO och SAOL sager nastan ordagrant samma sak: 'vavnadsvatska som "
     "ombesorjer amnesutbytet mellan blodet och cellerna'. OLD-facit "
     "'vavnadsvatska' ar korrekt men sager inte vad den GOR, och "
     "'vavnadsvatska' ar dessutom lika svart som uppslagsordet -- facit ar "
     "darfor omskrivet ett steg neroat enligt Adam-tal.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("skrev %d kort" % sum(1 for k in KORT if k.get("approved")))
