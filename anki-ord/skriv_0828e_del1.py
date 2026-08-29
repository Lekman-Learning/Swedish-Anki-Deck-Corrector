# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch6, kort 1-20. Full v3.

Skriven efter 138 kort och 13 underkannanden samma dag. Den harda regeln
som kom ur dem: SLA ALDRIG IHOP TVA BETYDELSER SOM SO ELLER SAOL HALLER
ISAR. Sex av de tretton felen var hopslagningar, och i fyra av dem hade jag
skrivit ut i sokkollen att jag slog ihop -- dokumentationen gjorde felet
sparbart, inte mindre fel. Bevisbordan ligger hos mig for att tva betydelser
ar samma, inte hos ordboken for att de ar olika.

Ovriga regler: synonym bara om ordet ar utbytbart at BADA hallen och inte ar
JFR-markt i SO; ingen betydelse som bara Wiktionary har; facit styrs av
definitionen, aldrig av etymologin eller av en synonym.
"""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch6.json"
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


satt("diminutiv",
     "Mycket liten ; om en ordform: som uttrycker att något är litet ; som "
     "substantiv: själva ordet som bildats för att beteckna en mindre "
     "variant, som \"cigarett\" av cigarr",
     "neutral, neutral, allmän ; fackspråklig, neutral, lingvistik ; "
     "fackspråklig, neutral, lingvistik",
     [],
     "\"Cigarett\" är egentligen ett " + B % "diminutiv" + " som betyder "
     "\"liten cigarr\".",
     "→ Latin diminutivus, till diminuere 'minska'.",
     "SO ger TRE betydelser och alla ar med: adjektivet 'mycket liten' "
     "(SO:s exempel: ett diminutivt hakskagg), den sprakvetenskapliga "
     "'som uttrycker forminskning' (tyskans -chen, -lein) och "
     "substantivet, sjalva forminskningsordet. SAOL bekraftar alla tre. "
     "OLD-facit 'forminskningsord' hade bara den tredje -- den vanligaste "
     "anvandningen i vanlig text ar daremot den forsta, och den saknades.")

satt("dyslexi",
     "Varaktig nedsättning av förmågan att läsa och skriva, som gäller just "
     "det och inte är en allmän inlärningssvårighet",
     "fackspråklig, neutral, medicin",
     [],
     "Med gott stöd kan personer med " + B % "dyslexi" + " minska sina "
     "svårigheter.",
     "→ Grekiska dys- 'daligt, svart' och lexis 'ord, tal'.",
     "SO: 'specifika las- och skrivsvarigheter'. Ordet SPECIFIKA ar hela "
     "termen och ar utskrivet i facit: det ar det som skiljer dyslexi fran "
     "las- och skrivsvarigheter i allmanhet. SAOL: 'nedsattning av las- och "
     "skrivformagan'. Wiktionary lagger till 'varaktigt', som ar med. "
     "Ordblindhet ar JFR-markt i SO och tas INTE upp som synonym -- det ar "
     "ett aldre ord for ungefar samma sak, men SO:s egen markning racker "
     "inte som synonymbelagg (samma regel som fallde spe).")

satt("epitet",
     "Beskrivande ord man sätter på någon eller något, ofta värderande ; "
     "inom grammatiken: ett ord som ansluter direkt till namnet utan paus, "
     "som \"kung\" i \"kung Karl\"",
     "neutral, neutral, allmän ; fackspråklig, neutral, lingvistik",
     [],
     "Hon beskrev honom med mindre smickrande " + B % "epitet" + ".",
     "→ Grekiska epitheton 'tillagg'.",
     "SO ger tva: '(karakteriserande) beteckning' och 'attribut som "
     "omedelbart och utan paus ansluter sig till huvudordet'. Bada ar med. "
     "Att anvandningen ofta ar VARDERANDE foljer av bada SO:s exempel "
     "(mindre smickrande epitet; oformtjant med epitetet rasister) men ar "
     "skrivet som 'ofta', inte som regel, eftersom SAOL:s exempel (Lange "
     "Jan, kung Karl) ar neutrala. SO:s JFR (attribut, apposition) ar "
     "cohyponymer. OLD-facit 'namntillagg' tacker bara den grammatiska.")

satt("gondol",
     "Långsmal, flatbottnad venetiansk båt med uppåtböjda stävar, som förs "
     "fram med en åra i aktern ; korgen eller hytten som hänger under en "
     "luftballong ; fristående försäljningsdisk i en butik där varorna "
     "ligger öppet framme",
     "neutral, neutral, allmän ; fackspråklig, neutral, teknik ; "
     "fackspråklig, neutral, ekonomi",
     [],
     B % "Gondolen" + " stötte nästan i marken, så de måste kasta ballast.",
     "→ Italienska gondola; ursprunget ar omdiskuterat, ev. till "
     "dialektens gondola 'gunga, rulla'.",
     "SO ger TRE betydelser och SAOL bekraftar alla tre: baten, "
     "ballongkorgen och butiksdisken. Alla ar med -- butiksbetydelsen ar "
     "den helt oformodade och skulle ha fallit bort utan uppslagning. "
     "OLD-facit 'langsmal kanalbat' hade bara den forsta. Wiktionarys "
     "fjarde ('hytt for passagerare i en linbana') ar UTELAMNAD: den saknas "
     "i bade SO och SAOL, och en Wiktionary-egen betydelse fallde bade "
     "anlopa och autograf tidigare i dag. Exempelmeningen ar SO:s egen och "
     "illustrerar ballongbetydelsen, eftersom baten redan ar valkand.")

satt("kapellmästare",
     "Titeln på den som leder ett musikkapell ; mer allmänt: den som leder "
     "en orkester",
     "fackspråklig, neutral, musik ; neutral, neutral, musik",
     [],
     "Han var " + B % "kapellmästare" + " vid hovet i över tjugo år.",
     None,
     "SO: '(titel for) dirigent for musikkapell', med underbetydelsen 'av. "
     "allmannare: orkesterledare'. Bada ar med, och skillnaden ar att den "
     "forsta ar en TITEL med formell stallning medan den andra bara "
     "beskriver vad nagon gor. OLD-facit 'ledare for musikkar' missar "
     "titeldelen och byter dessutom kapell mot kar, som ar nagot annat.")

satt("koncept",
     "Utkast till en längre text ; i uttrycket \"tappa koncepterna\": komma "
     "av sig och förlora fattningen ; grundidé för en ny produkt eller "
     "verksamhet, med de bärande dragen bestämda",
     "ngt ålderdomlig, neutral, allmän ; vardaglig, neutral, allmän ; "
     "neutral, neutral, ekonomi",
     [],
     "Ett beprövat " + B % "koncept" + " som fungerat i tjugo länder.",
     "→ Latin conceptum 'det sammanfattade', till concipere 'sammanfatta, "
     "avfatta'; samma rot som koncipiera.",
     "SO ger TRE betydelser: textutkastet (SO:s markning: nagot "
     "alderdomligt), uttrycket 'tappa koncepterna' och den moderna "
     "produktbetydelsen (belagd forst 1983, mot 1527 for den forsta). Alla "
     "tre ar med. Uttrycket ar en egen definition i SO med egen "
     "exempelmening, inte en underbetydelse -- att sla ihop det med "
     "textbetydelsen vore precis felet som fallde harnesk tidigare i dag. "
     "OLD-facit 'manuscript; ide' hade tva av tre och missade uttrycket, "
     "som ar den enda av de tre en modern lasare mater i talsprak.")

satt("kristyr",
     "Glasyr av äggvita och florsocker, som används för att dekorera "
     "bakverk",
     "neutral, neutral, matlagning",
     [],
     "De dekorerade pepparkakshuset med " + B % "kristyr" + ".",
     "→ Ovisst ursprung; troligen bildat i analogi med glasyr.",
     "SO: 'glasyr av aggvita och florsocker'. SAOL: 'sockerglasyr till "
     "tartor'. Bada leden ar med: VAD den bestar av (SO) och VAD den "
     "anvands till (SAOL). OLD-facit 'sockerglasyr' sager inte vad som "
     "skiljer kristyr fran vilken glasyr som helst -- aggvitan.")

satt("mangold",
     "Odlad beta som man äter bladen av, ungefär som spenat",
     "neutral, neutral, biologi",
     [],
     "Röd " + B % "mangold" + " med kraftiga stjälkar.",
     "→ Tyska Mangold; av ovisst ursprung.",
     "SO: 'en odlad beta vars blast anvands som spenat'. Ordet 'blast' ar "
     "utbytt mot 'bladen' enligt Adam-tal -- blast ar minst lika ovanligt "
     "som uppslagsordet. SAOL sager bara 'en vaxt och gronsak', vilket inte "
     "hjalper nagon. OLD-facit 'en spenatgronsak' antyder felaktigt att det "
     "AR en sorts spenat; det ar en beta.")

satt("oantastlig",
     "Så väl gjord att det inte går att rikta minsta kritik mot den",
     "neutral, positiv, allmän",
     ["oklanderlig"],
     "Hans resonemang var logiskt " + B % "oantastligt" + ".",
     None,
     "SO: 'som inte ger skal for minsta kritik'. SAOL:s hela definition ar "
     "'oklanderlig' -- darav synonymen, som klarar bada-hallen-provet: de "
     "tva orden gar att byta mot varandra i vilken mening som helst, och "
     "SO markerar inte oklanderlig som JFR. OLD-facit 'felfri, perfekt' ar "
     "for starkt: oantastlig sager att ingen KAN klandra, inte att allt ar "
     "perfekt -- ett resonemang kan vara oantastligt och anda leda fel.")

satt("postmodernism",
     "Riktning inom konst och litteratur som växte fram som en reaktion mot "
     "modernismen",
     "fackspråklig, neutral, konst",
     [],
     "Byggnaden räknas som ett tidigt exempel på " + B % "postmodernism" +
     ".",
     "→ Till post- 'efter' och modernism.",
     "SO: 'en konstnarlig stilriktning som praglas av reaktion mot "
     "modernismen'. SAOL: 'en stromning inom konsten och litteraturen som "
     "utgor en reaktion mot modernismen'. OLD-facit 'ny fas efter det "
     "moderna' ar fel i sak: forleden post- betyder visserligen 'efter', "
     "men bada ordbockerna definierar ordet som en REAKTION MOT, inte som "
     "nasta steg i samma riktning. Facit ar omskrivet.")

satt("profetera",
     "Framföra ett budskap man säger sig ha fått från Gud ; försvagat i "
     "modern svenska: förutsäga vad som kommer att hända",
     "neutral, neutral, bibliskt ; neutral, neutral, allmän",
     [],
     "Ekonomerna " + B % "profeterade" + " om en krasch som aldrig kom.",
     "→ Fornsvenska prophetera; till profet.",
     "SO ger tva: 'upptrada som religios forkunnare' (markning: sarsk. "
     "bibliskt) och 'forutspa, forutsaga' (numera vanligen forsvagat). Bada "
     "ar med, med SO:s egen notering om att den andra ar den vanliga i dag "
     "-- darav exempelmeningen. OLD-facit 'sprida religiosa asikter' ar fel "
     "i sak: en profet sprider inte sina egna asikter utan framfor ett "
     "budskap han sager sig ha FATT, och den skillnaden ar hela ordet.")

satt("recession",
     "Period när ekonomin krymper i stället för att växa — en mildare "
     "nedgång än en depression",
     "fackspråklig, neutral, ekonomi",
     [],
     "Landet gick in i " + B % "recession" + " efter ett år av fallande "
     "efterfrågan.",
     "→ Engelska recession; samma rot som recess.",
     "SO: 'mildare lagkonjunktur'. SAOL: 'avmattning av den ekonomiska "
     "aktivitetsnivan'. SO markerar depression som JFR:cohyponym -- det ar "
     "alltsa INTE en synonym utan den starkare graden, och just den "
     "kontrasten ar vad SO:s ord 'mildare' bygger pa, sa den ar utskriven i "
     "facit. OLD-facit 'tillbakagang' ar for brett och sager ingenting om "
     "att det galler ekonomin.")

satt("supera",
     "Äta ett sent kvällsmål",
     "neutral, neutral, allmän",
     [],
     "De " + B % "superade" + " på en flott restaurang efter teatern.",
     None,
     "SO och SAOL ger bada exakt samma tva ord: 'ata supe'. Den "
     "definitionen forutsatter att man redan kan ordet supe, och ar darfor "
     "utskriven enligt Adam-tal -- ett facit som innehaller uppslagsordets "
     "egen stam forklarar ingenting. Ingen bruklighetsmarkning finns i "
     "nagondera ordboken, sa registret ar neutralt trots att ordet kanns "
     "gammaldags; en markning far inte hittas pa. OLD-facit 'ata "
     "kvallsmat' stammer men missar att malet ar SENT, vilket ar vad supe "
     "betyder.")

satt("tjusig",
     "Elegant och vacker att se på ; om något som ger status: flott och "
     "eftertraktat ; ibland om en handling: fin och beundransvärd",
     "neutral, positiv, allmän ; neutral, positiv, allmän ; neutral, "
     "positiv, allmän",
     [],
     "Det var " + B % "tjusigt" + " av honom att ta på sig skulden.",
     None,
     "SO: 'elegant och vacker', med underbetydelserna 'av. om foreteelse "
     "som ger status eller dylikt' (SO:s exempel: ett tjusigt jobb i "
     "filmbranschen) och 'ibland av. for att beskriva goda inre "
     "karaktarsegenskaper' (SO:s exempel: det var tjusigt av honom att ta "
     "pa sig skulden). Alla tre ar med -- den tredje ar en HELT annan sak "
     "an de tva forsta, eftersom den inte handlar om utseende alls, och "
     "OLD-facit 'behagfull' tackte bara den forsta. SO:s JFR (grann, "
     "stilig) ar cohyponymer.")

satt("undfå",
     "Ta emot något som ges en, särskilt något andligt",
     "högtidlig, neutral, religion",
     [],
     "Man " + B % "undfår" + " syndernas förlåtelse genom tron.",
     "→ Fornsvenska untfa; efter lagtyska untfan 'ta emot'.",
     "SO: '(fa) ta emot', med markningen hogtidligt; sarsk. i religiosa "
     "sammanhang -- darav bade registret och domanen, och bada SO:s exempel "
     "ar religiosa (undfa det heliga dopet; undfa syndernas forlatelse). "
     "SAOL markar ald. OLD-facit sa '(rel.) mottaga', vilket ar ratt men "
     "'mottaga' ar lika hogtidligt som uppslagsordet.")

satt("annullera",
     "Förklara att ett beslut, ett avtal eller en bokning inte längre "
     "gäller",
     "neutral, neutral, juridik",
     [],
     "Årsmötet " + B % "annullerade" + " styrelsens beslut.",
     "→ Latin annullare 'forinta', till nullus 'ingen'; samma rot som "
     "noll.",
     "SO: 'forklara (beslut, kontrakt eller dylikt) ogiltigt'. SAOL: "
     "'forklara ogiltig, upphava'. Upphava ar INTE upptaget som synonym: "
     "det ar JFR-markt i SO, och orden klarar inte bada-hallen-provet -- "
     "man upphaver en lag men annullerar den inte, man annullerar en "
     "bokning men upphaver den inte. OLD-facit sa just 'upphava'.")

satt("betagande",
     "Så vacker eller charmerande att man inte kan värja sig",
     "neutral, positiv, allmän",
     [],
     "Hennes sång var helt " + B % "betagande" + ".",
     "→ Till betaga, fornsvenska betaka; efter lagtyska benemen, till "
     "nemen 'ta' -- nagot som TAR en.",
     "SO: 'som vacker oemotstandlig fortjusning'. VIKTIG AVGRANSNING: SO:s "
     "uppslag blandar in betydelser som hor till VERBET betaga ('fa nagon "
     "att forlora', 'overvaldiga', SAOL:s 'ta ifran' -- SO:s exempel "
     "'publikens missnoje betog honom lusten att fortsatta'). Uppslagsordet "
     "har ar adjektivet betagande, inte verbet betaga, sa de betydelserna "
     "ar INTE med. Det ar inte en hopslagning av tva betydelser utan en "
     "avgransning till ratt uppslagsord -- de star under samma artikel i "
     "SO men ar olika ordklasser. OLD-facit 'fortjusande' stammer.")

satt("eklog",
     "Dikt om herdar och deras liv ; mer allmänt: dikt som målar upp ett "
     "idylliskt liv på landet",
     "fackspråklig, neutral, litteraturvetenskap ; fackspråklig, neutral, "
     "litteraturvetenskap",
     [],
     "Vergilius " + B % "ekloger" + " är genrens förebild.",
     "→ Grekiska ekloge 'urval, citat'.",
     "SO: 'herdedikt', med underbetydelsen 'av. om dikt som skildrar "
     "idylliskt lantligt liv'. Bada ar med -- den andra ar vidare och "
     "kraver inga herdar alls. SAOL bekraftar: 'herdedikt, idyll i aldre "
     "litteratur'. OLD-facit 'herdedikt' ar SO:s ord men lika svart som "
     "uppslagsordet, och tackte bara den forsta betydelsen.")

satt("homogen",
     "Sammansatt av delar som är likadana rakt igenom ; ibland med "
     "bibetydelsen att helheten därför håller jämn och god kvalitet",
     "neutral, neutral, allmän ; neutral, positiv, allmän",
     [],
     "Ett " + B % "homogent" + " försvar utan svaga punkter.",
     "→ Grekiska homogenes 'av samma art', till homo- 'samma' och genos "
     "'art, slag'.",
     "SO: 'sammansatt av alltigenom likartade bestandsdelar', med "
     "underbetydelsen 'ibland med bibetydelse av god kvalitet eller "
     "dylikt' (SO:s exempel: ett homogent forsvar utan svaga punkter). Bada "
     "ar med. SO markerar heterogen som MOTSATS -- alltsa antonym, inte "
     "synonym. Enhetlig ar JFR-markt i SO och tas darfor inte upp som "
     "synonym trots att det ar SAOL:s hela definition; det ar samma "
     "avvagning som fallde spe tidigare i dag. OLD-facit sa 'enhetlig'.")

satt("krackelera",
     "Ge glasyr eller glas ett nät av fina sprickor ; om en yta: spricka "
     "upp i ett sådant nät ; bildligt om en fasad eller en bild av något: "
     "börja spricka och falla isär",
     "fackspråklig, neutral, konst ; neutral, neutral, allmän ; neutral, "
     "neutral, allmän",
     [],
     "Den äldre Sverigebilden har " + B % "krackelerat" + ".",
     "→ Franska craqueler, till craquer 'knaka'; nara beslaktat med "
     "kracka.",
     "SO ger 'ge (glasyr eller glas) ett nat av fina sprickor' och "
     "'spricka', med underbetydelsen 'av. bildligt'. Tre led i facit: det "
     "AVSIKTLIGA (krackelerat porslin ar en teknik, inte en skada), det som "
     "HANDER av sig sjalvt, och det bildliga -- SO:s enda bildliga exempel "
     "ar behallet som exempelmening eftersom det ar den anvandning en "
     "lasare faktiskt moter. OLD-facit 'spricka' hade bara den andra, "
     "vilket gor att den avsiktliga tekniken ser ut som en olycka.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("skrev %d kort" % sum(1 for k in KORT if k.get("approved")))
