# -*- coding: utf-8 -*-
"""Spar B (omgranskning), session_2026-09-06_v3-omgranskning.json, ord 21-40.

Samma urval och samma sokkoll som g1: bevisraderna for alla 40 orden star i
sessionens eget transkript (slaupp.py --fil rep40_ord.json --antal 40 --tyst).
"""
import io, json, urllib.parse

FIL = "sessions/session_2026-09-06_v3-omgranskning.json"
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"förevändning": dict(
  hb="Påhittat eller obetydligt skäl som skjuts fram för att dölja det verkliga",
  reg="neutral, negativ",
  grp=[["svepskäl", "undanflykt"]],
  ex='Telefonsamtalet gav honom en <font color="#3498db">förevändning</font> att lämna mötet.',
  etym="till äldre förevända 'anföra som skäl'; av tyska vorwenden med samma betydelse",
  sl="SO: 'anfort men i sammanhanget betydelselost skal for visst handlande'. SAOL: 'ogiltigt skal "
     "som anfors t.ex. for franvaro'. Legacys 'Falskt eller obetydligt skal som doljer den "
     "verkliga anledningen' traffar ratt i sak. Justerat pa en punkt: SO:s poang ar att skalet "
     "ANFORS -- det sags hogt, det ar inte bara en privat tanke -- sa 'skjuts fram' har ersatt det "
     "passiva 'som doljer'. 'falskt' bytt mot 'pahittat' (enklare, samma sak). 'svepskal' och "
     "'undanflykt' star bada i synonymer.se (belagda), och 'svepskal' ar dessutom OLD-facit. "
     "Register oforandrat: ingen ordbok ger brukligheskommentar, och laddningen ar klart negativ "
     "(SAOL: 'OGILTIGT skal'). Exempelmeningen ar SO:s eget syntex, oforandrad. Etymologi ny, "
     "ur SO -- 'forevanda' = 'vanda fram', alltsa halla nagot framfor sig, vilket ar precis "
     "bilden."),

"pracka": dict(
  hb="Lura eller tvinga på någon något hen inte vill ha ; en andfågel med lång hals och smal, "
     "svagt uppåtböjd näbb",
  reg="vardaglig, negativ ; neutral, neutral, biologi",
  grp=[["truga på", "lura på"], ["småskrake"]],
  ex='Försäljaren <font color="#3498db">prackade</font> på henne en ny dammsugare.',
  etym="verbet av lågtyska pracken 'tigga'; fågelnamnet är ett annat ord, en ljudhärmande bildning",
  sl="SAKNAD BETYDELSE, och det var HUVUDBETYDELSEN som saknades. Legacy hade BARA fageln ('en "
     "aldre, dialektal benamning pa sjofageln smaskrake'). SO ger tva: fageln OCH 'lura eller "
     "tvinga (nagon) att ta emot eller kopa', med syntexet 'forsaljaren prackade pa henne en ny "
     "dammsugare'. SAOL har over huvud taget INTE fageln -- bara verbet ('truga pa, lura pa', med "
     "konstruktionen 'pracka pa ngn ngt'). synonymer.se ger bada men lagger verbgruppen under "
     "'(vard.)'. Verbet ar alltsa det som tva av tre kallor prioriterar och det enda en modern "
     "lasare motter; det star nu forst. Fageln kvar som betydelse 2. Bada verbsynonymerna star "
     "ordagrant i SAOL:s led (belagda); 'smaskrake' ar OLD-facit och star i synonymer.se "
     "('smaskrak'). REGISTER: verbet vardagligt (synonymer.se:s '(vard.)') och negativt laddat "
     "(att bli prackad pa nagot ar inget man vill); fageln neutral med doman biologi. Legacys "
     "'dialektal' galler pa sin hojd fageln och saknar stod aven dar. EXEMPELMENING BYTT till "
     "SO:s eget syntex for den nya betydelsen -- den gamla ('Prackan simmar graciost pa sjon') "
     "visade bara fageln. Etymologi ny, ur SO, som ger tva skilda ursprung: verbet ur lagtyska "
     "pracken 'tigga', fagelnamnet ljudharmande. Att det ar tva olika ord ar sjalva forklaringen "
     "till varfor kortet kanns sa spretigt."),

"skvattram": dict(
  hb="Lågväxt, starkt doftande buske på myrar, med många små vita blommor",
  reg="neutral, neutral, biologi",
  grp=[["getpors"]],
  ex='Doften av <font color="#3498db">skvattram</font> låg tung över myren.',
  etym="troligen bildat till svensk dialekt skvattra 'stänka, plaska'; av ljudhärmande ursprung",
  sl="SO: 'en risartad, starkt doftande myrvaxt med talrika, vita blommor', med en "
     "SYN:synonym-taggad underbetydelse (getpors). Legacys 'En starkt doftande myrvaxt med vita "
     "blommor' var ratt men tappade tva av SO:s sardrag: RISARTAD (det ar en lag buske, inte en "
     "ort) och TALRIKA (blommorna sitter manga ihop). Bada tillagda -- 'risartad' omskrivet till "
     "'lagvaxt ... buske', som ar samma sak i Adam-tal. 'getpors' ar SO:s egen SYN-taggade "
     "korshanvisning och OLD-facit (belagd, oforandrad). Trekallskontrollen visar att skvattram "
     "saknas i synonymer.se -- getpors ar alltsa den enda belagda synonymen som finns, och den ar "
     "fullt utbytbar (samma vaxt, Rhododendron tomentosum). Register och doman oforandrade; ingen "
     "ordbok ger brukligheskommentar. Exempelmening oforandrad -- doften ar det enda de flesta "
     "nagonsin motter av vaxten och darmed ratt minneskrok. Etymologin lag redan pa kortet, "
     "matchar SO, oforandrad."),

"kutting": dict(
  hb="Liten tunna av trä ; i uttrycket vända på kuttingen: se saken från motsatt håll",
  reg="dialektal, neutral ; neutral, neutral",
  grp=[["kagge"], ["≈≈ kasta om perspektivet"]],
  ex='Skolan har vänt på <font color="#3498db">kuttingen</font> och byggt färre lärosalar men '
     'fler grupprum.',
  etym="troligen bildat till kotte",
  sl="SO ger tva betydelser: 'mindre (tra)tunna' (dialektalt) och idiomet 'anlagga ett motsatt "
     "perspektiv'. Legacy hade bada -- ratt. SYNONYM BORTTAGEN: legacy hade 'kagge, LITEN TUNNA' "
     "-- den andra var ordagrant kortets egen definition, alltsa ingen synonym alls utan en "
     "upprepning. Struken; 'kagge' star kvar och ar belagd ordagrant i SAOL:s led ('liten tunna, "
     "kagge') och i synonymer.se. Betydelse 2 ar ett idiom utan enordssynonym -- kategorin "
     "'≈≈ kasta om perspektivet' lag redan pa kortet och ar satt ur definitionen (ingen kalla "
     "kravs for ≈≈), oforandrad. REGISTER: 'dialektal' pa betydelse 1 har stod i SO:s egen "
     "markning 'dialektalt'; betydelse 2 (idiomet) ar omarkerad i SO och blir neutral -- legacys "
     "andra rad sa redan det. Exempelmeningen ar SO:s eget syntex, nedkortat. Etymologin lag "
     "redan pa kortet, matchar SO, oforandrad."),

"cession": dict(
  hb="En långivares överlåtelse av sin fordran till någon annan, utan att låntagaren behöver vara "
     "med ; en stats överlåtelse av ett landområde till en annan stat ; konkurs",
  reg="fackspråklig, neutral, juridik ; fackspråklig, neutral, politik ; fackspråklig, neutral, "
      "juridik",
  grp=[["≈≈ fordringsöverlåtelse"], ["≈≈ landavträdelse"], ["konkurs", "bankrutt"]],
  ex='Banken genomförde en <font color="#3498db">cession</font> av lånefordringarna till ett '
     'inkassobolag.',
  etym="av latin cessio 'avträdande'",
  sl="TVA SAKNADE BETYDELSER -- riskflaggan dold_betydelse traffade ratt. SO ger TRE: 'en "
     "borgenars overlatelse av fordran till ny person utan galdenarens samtycke', 'overlatelse av "
     "territorium fran en stat till en annan' och 'konkurs'. Legacy hade bara den forsta. SAOL "
     "bekraftar den tredje explicit ('overlatelse av fordran utan galdenars medverkan; KONKURS'), "
     "och OLD-facit sager bara ett enda ord: 'konkurs'. Det forklarar ocksa riskflaggan "
     "old_delar_inget_ordforrad -- OLD och kortet delade inget ordforrad darfor att de beskrev "
     "OLIKA BETYDELSER, inte for att nagon av dem var fel. Bada tillagda. SPRAK: legacys "
     "'borgenars' och 'galdenarens' ar sjalva uppslagsord i decket och bryter mot regeln att "
     "forklaringen ska ligga en niva under uppslagsordet; utbytta mot 'langivare' och 'lantagare'. "
     "Betydelse 1 och 2 har ingen belagd enordssynonym -- kategorier satta ur kortets egen "
     "definition (ingen kalla kravs for ≈≈). 'konkurs' och 'bankrutt' for betydelse 3 star bada i "
     "synonymer.se (belagda), och 'konkurs' ar dessutom SO:s hela definition. REGISTER: alla tre "
     "ar fackspraklig; domanerna skiljer dem at (juridik, politik, juridik). Legacys enda rad "
     "'formell, neutral' tackte tre betydelser. Exempelmeningen visar betydelse 1, oforandrad. "
     "Etymologi ny, ur SO -- 'avtradande' ar den gemensamma karnan i alla tre betydelserna, vilket "
     "gor kortet till en helhet i stallet for tre losa fakta."),

"genever": dict(
  hb="Nederländskt brännvin kryddat med enbärsolja",
  reg="neutral, neutral, mat",
  grp=[["≈ brännvin"]],
  ex='Han hällde upp en <font color="#3498db">genever</font> ur det bukiga lerkruset.',
  etym="av nederländska jenever 'enbär; genever', ytterst till latin juniperus 'enbuske' -- samma "
       "ord som gett engelskans gin",
  sl="SO: 'ett brannvin som kryddats med enbarsolja'. SAOL: 'ett NEDERLANDSKT enbarsbrannvin'. "
     "Legacys 'Enbarskryddat brannvin' tappade harkomsten, som SAOL satter forst och som ar det "
     "enda som skiljer genever fran andra enbarsbrannvin -- tillagd. SO:s precisering 'enbarsOLJA' "
     "(inte enbaren sjalva) ocksa med. SYNONYM NEDGRADERAD: legacy hade 'brannvin' OMARKERAT, "
     "alltsa som fullt utbytbart -- men allt brannvin ar inte genever; ordet ar en overordnad "
     "kategori, inte en synonym. Nedgraderat till '≈ brannvin', narmaste befintliga ord, belagt i "
     "synonymer.se (som ger just och endast 'brannvin'). REGISTER ANDRAT: 'vardaglig' saknar stod "
     "-- varken SO eller SAOL markerar ordet; doman mat tillagd. EXEMPELMENING BYTT: legacys "
     "'Genever skapades ursprungligen av nederlandarna' ar en encyklopedisk uppgift, inte en "
     "mening som visar ordet i bruk. Den nya bygger pa SO:s eget syntex 'genever tappat pa "
     "lerkrus' -- lerkruset ar dessutom den bild man faktiskt ser genever i. Etymologi ny, ur SO, "
     "inklusive SO:s egen hanvisning till gin: att genever och gin ar samma ord binder ihop ett "
     "okant ord med ett Adam redan kan."),

"korollarium": dict(
  hb="Sats som följer självklart av ett större bevisat påstående, utan att behöva bevisas för sig",
  reg="fackspråklig, neutral, matematik",
  grp=[["följdsats", "konklusion"]],
  ex='Pythagoras sats är ett teorem, och flera <font color="#3498db">korollarier</font> följer '
     'direkt ur det.',
  etym="av latin corollarium 'liten belöning; tillfogad följdsats', till corolla 'liten krans' -- "
       "något man får på köpet",
  sl="SO: 'sats som uppenbart foljer av ett (storre) teorem' (filosofi, matematik). SAOL: "
     "'foljdsats'. Legacys 'Logisk foljdsats som direkt foljer av ett tidigare bevisat pastaende' "
     "var CIRKULAR: 'foljdsats' var bade definitionens huvudord och kortets enda synonym. "
     "Definitionen star nu pa egna ben ('Sats som foljer sjalvklart av ett storre bevisat "
     "pastaende') och 'foljdsats' ligger bland synonymerna dar den ar belagd ordagrant i SAOL:s "
     "led. Tillagt ur SO: 'UTAN ATT BEHOVA BEVISAS FOR SIG' -- SO:s 'uppenbart' ar just det som "
     "gor ett korollarium till ett korollarium och inte till ytterligare ett teorem. 'konklusion' "
     "star i synonymer.se (belagd). REGISTER: legacys 'formell' bytt mot 'facksprakligt' med "
     "doman matematik, vilket har FAKTISKT stod -- SO ger brukligheskommentaren 'filosofi, "
     "matematik' och SAOL 'mat.'. EXEMPELMENING RATTAD: legacy hade 'flera KOROLLARIUM', fel "
     "numerus; ratt plural ar korollarier. Aven 'fran det' bytt mot 'ur det' (idiomatiskt for "
     "harledning). Etymologi ny, ur SO -- 'liten krans' som man far pa kopet forklarar varfor "
     "ordet betyder en sats man far gratis."),

"brösta": dict(
  hb="brösta sig: göra sig stor och skryta ; del av seldon som ligger mot hästens bringa och tar "
     "upp draget ; brösta av: skjuta i väg ett hårt skott",
  reg="vardaglig, lätt negativ ; fackspråklig, neutral, hästsport ; vardaglig, neutral, sport",
  grp=[["stoltsera", "kråma sig"], ["≈≈ seldel"], ["≈≈ skjuta"]],
  ex='Han <font color="#3498db">bröstade</font> sig över segern som om han vunnit den ensam.',
  etym="seldelen och 'brösta av' hör till tyska Protz, italienska biroccio 'tvåhjulig vagn'",
  sl="SAKNAD BETYDELSE, och aterigen den vanligaste. Legacy hade BARA seldelen ('Seldel som ligger "
     "mot hastens bringa och tar upp draget'). Men OLD-facit sager ett enda ord: 'STOLTSERA', och "
     "synonymer.se inleder hela sin lista med 'brosta sig, stoltsera, skryta, krama sig, yvas, "
     "vara stolt, satta nasan i vadret'. Tva kallor ger alltsa den reflexiva betydelsen, som "
     "legacy saknade helt -- vilket ocksa forklarar riskflaggan old_delar_inget_ordforrad: OLD och "
     "kortet beskrev olika betydelser. Tillagd, och satt FORST: det ar den enda av de tre en "
     "modern lasare motter utanfor en travbana. SO ger dessutom en tredje, 'framfora' med "
     "markningen 'vardagligt; sarsk. sport' och syntexet 'NN brostade av en rokare' (fotboll) -- "
     "SAOL bekraftar med 'avlossa en salva'. Tillagd som betydelse 3. SO:s kanonbetydelse ('koppla "
     "loss kanoner for att forsatta dem i eldstallning') ar den historiska formen av samma sak och "
     "har inte fatt egen rad. 'stoltsera' och 'krama sig' star bada i synonymer.se (belagda); "
     "betydelse 2 och 3 saknar enordssynonym och har fatt kategorier ur kortets egen definition "
     "(ingen kalla kravs for ≈≈). REGISTER: legacys 'formell' saknar stod; betydelse 1 och 3 ar "
     "vardagliga (synonymer.se resp. SO:s 'vardagligt'), betydelse 2 fackspraklig. EXEMPELMENING "
     "BYTT: legacys 'Kusken kontrollerade att brostat satt ratt' visade bara betydelse 2 och hade "
     "dessutom en form ('brostat') som inte ar uppslagsordet. Ny mening visar betydelse 1. "
     "ETYMOLOGI: SO:s uppgift (tyska Protz, 'tvahjulig vagn') galler vagnen och darmed betydelse 2 "
     "och 3 -- det star uttryckligen i etymologifaltet, sa att den inte lases som forklaring till "
     "'brosta sig'. Nagon kalla for det senare ledets ursprung hamtades inte i den har omgangen "
     "och har darfor lamnats outsagd."),

"dager": dict(
  hb="Naturligt ljus som inte är direkt solsken ; det intryck något ger — den dager något "
     "framstår i ; i öppen dager: så att alla kan se det",
  reg="neutral, neutral ; neutral, neutral ; neutral, neutral",
  grp=[["dagsljus", "belysning"], ["≈≈ intryck"], ["≈≈ allmänt känt"]],
  ex='Det var redan full <font color="#3498db">dager</font> när hon vaknade.',
  etym="fornsvenska dagher; samma ord som dag",
  sl="SO: '(naturligt) ljus som inte utgors av direkt solstralning', med tre underbetydelser som "
     "har egen definitionstext: 'av. om motsvarande atergivning i bild', 'av. bildligt, spec. i "
     "uttryck for det intryck nagot gor' och 'spec. av. i ett uttryck for att nagot blir (allmant) "
     "kant' -- den sista ar 'i oppen dager'. Legacy hade tva av dessa (ljuset och intrycket) men "
     "SAKNADE 'i oppen dager', som ar det uttryck ordet oftast dyker upp i i modern text. Tillagt. "
     "BETYDELSE 1 PRECISERAD: legacy sa bara 'Dagsljus', men SO:s definition ar snavare an sa -- "
     "dager ar ljus som INTE ar direkt solstralning (det diffusa ljuset, jfr SO:s egna exempel "
     "'rummets skumma dager', 'den vackra dagern efter solnedgangen'). Skillnaden ar hela poangen "
     "med att ordet finns vid sidan av 'dagsljus'. 'dagsljus' och 'belysning' star bada ordagrant "
     "i SAOL:s led (belagda) och ligger i grupp 1; de ovriga tva betydelserna saknar "
     "enordssynonym och har kategorier ur kortets egen definition. SO:s fjarde underbetydelse "
     "(dager i bild, jfr SAOL:s 'ljuseffekt' och SO:s 'tavlans skuggor och dagrar') ar en "
     "fackanvandning inom maleri av samma ljusbetydelse och har inte fatt egen rad. REGISTER: "
     "legacys 'litterar' saknar stod -- ingen av ordbockerna markerar ordet; tre rader nu, en per "
     "betydelse. Exempelmeningen ar SO:s eget syntex 'det var full dager', oforandrad. "
     "Etymologi ny, ur SO."),

"belägga": dict(
  hb="Täcka en yta med ett lager ; ta upp platsen i något så att den är upptagen ; visa med fakta "
     "att något stämmer ; genom beslut förena med en påföljd, till exempel skatt eller förbud",
  reg="neutral, neutral ; neutral, neutral ; neutral, neutral ; fackspråklig, neutral, juridik",
  grp=[["täcka", "överdra"], ["≈≈ uppta"], ["styrka", "bevisa"], ["ålägga", "påföra"]],
  ex='Sjukhuset var <font color="#3498db">belagt</font> till bristningsgränsen.',
  etym="fornsvenska beläggia 'omge; täcka'; av lågtyska beleggen med samma betydelse",
  sl="SAKNAD BETYDELSE -- riskflaggan old_har_fler_betydelser traffade ratt. SO ger sex "
     "betydelser: 'forse med tackande lager', 'TA UPP PLATS I', 'genom stadgande forena med viss "
     "pafoljd', 'gora fast', 'ange fakta som stoder' och 'pavisa forekomst av'. Legacy hade tre "
     "(tacka, styrka, alagga) och saknade 'ta upp plats i' -- den betydelse ordet oftast har i "
     "vardagen ('sjukhuset var belagt', 'alla fonsterborden var belagda', 'en belagd plats'). SAOL "
     "har den som sitt andra led. Tillagd som betydelse 2. SO:s 'gora fast' (sjofartsordet, "
     "belagga en trosse) och skillnaden mellan 'ange fakta som stoder' och 'pavisa forekomst av' "
     "(den senare ar sprakvetenskapens 'ordet ar belagt fran 1600-talet' -- SO markerar den "
     "sarskilt) har inte fatt egna rader; fyra betydelser ar taket for vad ett kort kan bara, och "
     "de fyra som star ar de Adam faktiskt motter. 'tacka' och 'overdra' star bada i "
     "synonymer.se (belagda), 'bevisa' inleder SAOL:s forsta led ordagrant, 'styrka' star i "
     "synonymer.se. 'alagga' och 'pafora' lag redan pa kortet. Betydelse 2 saknar enordssynonym "
     "som inte ar cirkular ('uppta' ar SAOL:s eget led men ligger for nara definitionen) -- "
     "kategori satt ur kortets egen text. SYNONYMER GRUPPERADE: legacy hade sex synonymer i EN "
     "oindelad lista mot tre betydelser, sa det gick inte att se vilken som horde vart. Nu fyra "
     "grupper. REGISTER: legacys 'formell' saknar stod for de tre forsta; den juridiska "
     "betydelsen har daremot SO:s egen markning 'ofta juridik'. EXEMPELMENING BYTT till SO:s eget "
     "syntex for den NYA betydelsen -- den gamla visade en betydelse kortet redan hade. "
     "Etymologi ny, ur SO."),

"pagod": dict(
  hb="Östasiatiskt tempel byggt som ett fristående torn",
  reg="neutral, neutral, religion",
  grp=[["≈ tempelbyggnad"]],
  ex='En japansk <font color="#3498db">pagod</font> reste sig bland trädtopparna.',
  etym="av portugisiska pagode, ytterst till sanskrit bhagavat 'helig'",
  sl="SO: 'typ av osterlandsk tempelbyggnad i form av ett FRISTAENDE TORN'. SAOL: 'en typ av "
     "tempelbyggnad som ar vanlig i OSTASIEN'. Legacys 'Osterlandskt tempeltorn' var kort men "
     "tappade bada precisionerna: att tornet star fritt (SO) och att det ar Ostasien, inte "
     "'Osterlandet' i allmanhet (SAOL). Bada tillagda. SYNONYMER NEDGRADERADE: legacy hade "
     "'tempel' och 'tempelbyggnad' OMARKERADE, alltsa som fullt utbytbara -- men varje tempel ar "
     "inte en pagod; orden ar overordnade kategorier. Det ar precis den sortens fel HP:s ORD-del "
     "straffar. Ett kvar, nedgraderat till '≈ tempelbyggnad', narmaste befintliga ord, belagt i "
     "synonymer.se. REGISTER ANDRAT: 'vardaglig' saknar stod -- varken SO eller SAOL markerar "
     "ordet; doman religion tillagd. Exempelmeningen matchar SO:s eget syntex 'en japansk pagod', "
     "oforandrad. Etymologi ny, ur SO -- att ordet kom till Europa via portugisiska sjofarare och "
     "ytterst betyder 'helig' pa sanskrit ar bade sant och latt att minnas."),

"exstirpera": dict(
  hb="Ta bort något ur kroppen genom en operation",
  reg="fackspråklig, neutral, medicin",
  grp=[["skära bort", "operera bort"]],
  ex='Läkarna fick <font color="#3498db">exstirpera</font> tumören helt.',
  etym="av latin exstirpare 'utrota; utplåna', till stirps 'stam; rot' -- att dra upp med roten",
  sl="SO: 'genom operation avlagsna'. SAOL: 'operera bort svulst'. Legacys 'Kirurgiskt avlagsna' "
     "var ratt i sak men CIRKULAR mot sin egen synonymlista, dar forsta posten var 'avlagsna "
     "kirurgiskt' -- alltsa samma tva ord i omvand ordning. Definitionen omskriven till vardagsord "
     "('Ta bort nagot ur kroppen genom en operation'); den cirkulara synonymen struken. 'skara "
     "bort' och 'operera bort' star bada i synonymer.se (belagda), och 'operera bort' ar dessutom "
     "SAOL:s eget led. REGISTER: 'formell' bytt mot 'fackspraklig' med doman medicin -- ordet "
     "anvands inte i formell svenska i allmanhet utan uteslutande i medicinskt fackssprak, vilket "
     "bade SO:s syntex ('radikalt exstirperad tjocktarmscancer') och synonymer.se:s markning "
     "'med.' visar. Exempelmeningen matchar SO:s syntex 'exstirpera en tumor', oforandrad. "
     "Etymologi ny, ur SO -- 'stirps' = rot ger bilden av att dra upp med roten, vilket ar exakt "
     "vad SAOL:s 'operera bort svulst' innebar."),

"gensträvig": dict(
  hb="Som gör motstånd och inte vill lyda",
  reg="neutral, lätt negativ",
  grp=[["motsträvig", "motspänstig"]],
  ex='Hästen var <font color="#3498db">gensträvig</font> och vägrade gå in i transporten.',
  etym="till gen- 'mot, emot' och sträva -- alltså 'som strävar emot'",
  sl="SO: 'motstravig'. SAOL: 'motstravig'. OLD-facit: 'trotsig, motspanstig'. Legacys 'Som gor "
     "motstand och inte vill lyda' star kvar oforandrad -- den ar en riktig forklaring i "
     "Adam-tal, inte en synonym, och den tacker bade ordbockernas 'motstravig' och OLD:s "
     "'trotsig'. RISKFLAGGA old_delar_inget_ordforrad utredd: OLD sager 'trotsig, motspanstig' och "
     "kortet 'gor motstand och inte vill lyda' -- ingen konflikt, bara olika ord for samma sak; "
     "flaggan ar falsk har. 'motstravig' ar bade SO:s och SAOL:s hela definition (belagd, lag "
     "redan pa kortet), 'motspanstig' ar OLD-facit och star i synonymer.se (belagd, tillagd -- "
     "kortet hade bara EN synonym, och tva ger battre grepp om ordet). Register oforandrat: ingen "
     "ordbok ger brukligheskommentar, laddningen ar latt negativ. Exempelmening oforandrad -- "
     "hasten som vagrar ar den tydligaste bilden av att strava emot. ETYMOLOGI OMSKRIVEN: legacy "
     "hade 'till gen- 1 och 1sträva', dar siffrorna ar SO:s interna hanvisningsnummer och inte "
     "sager en lasare nagonting (samma fel som homofons 'se ursprung till 2homofon 1', ratttat "
     "2026-09-05). Utskrivet till 'gen- mot, emot' + strava, med den genomskinliga "
     "sammansattningen 'som strävar emot' -- vilket gor ordet sjalvforklarande."),

"mola": dict(
  hb="Göra dovt och ihållande ont, utan att svida till",
  reg="neutral, neutral",
  grp=[["småvärka", "molvärka"]],
  ex='Det <font color="#3498db">molade</font> i tanden hela natten.',
  etym="jfr svensk dialekt mola; av omdiskuterat ursprung",
  sl="SO: 'ihallande smavarka'. SAOL: 'smavarka'. Legacys 'Varka dovt och ihallande' var CIRKULAR: "
     "'varka' var bade definitionens huvudverb och kortets forsta synonym. Definitionen omskriven "
     "till 'Gora dovt och ihallande ont, UTAN ATT SVIDA TILL' -- den sista bestamningen ar tillagd "
     "for att skilja molande fran skarp smarta, vilket ar hela skalet till att ordet finns "
     "(jfr SO:s syntex 'en molande vark'). 'smavarka' ar SO:s och SAOL:s eget led (belagd), "
     "'molvarka' star i synonymer.se (belagd). SYNONYM BORTTAGEN: 'gnaga' finns visserligen i "
     "synonymer.se men beskriver en annan kansla (gnagande = natande, ofta bildligt om oro) och ar "
     "inte utbytbart i 'det molade i tanden'. REGISTER ANDRAT: 'vardaglig' saknar stod -- varken "
     "SO eller SAOL ger nagon brukligheskommentar. SO:s 'av. bildligt' (syntex: 'en molande "
     "kansla av tomhet') ar en utvidgning UTAN egen definitionstext och ar darfor inte en andra "
     "betydelse -- kortet har medvetet kvar en betydelse. Exempelmeningen ar SO:s eget syntex "
     "'det molade i tanden', oforandrad. Etymologin lag redan pa kortet, matchar SO, oforandrad."),

"obetingad": dict(
  hb="Som sker av sig själv utan att ha lärts in, till exempel en reflex ; helt utan villkor eller "
     "förbehåll",
  reg="fackspråklig, neutral, psykologi ; neutral, neutral",
  grp=[["≈≈ medfödd"], ["ovillkorlig", "förbehållslös"]],
  ex='Barnets <font color="#3498db">obetingade</font> tilltro till föräldrarna.',
  etym="till o- och betinga -- en betingad reflex är inlärd, en obetingad är det inte",
  sl="SAKNAD BETYDELSE, och SO satter den FORST. SO ger tva: 'som uppkommer spontant' och "
     "'absolut, oinskrankt'. Legacy hade bara den andra ('Helt utan villkor eller forbehall, "
     "absolut'). SO:s forsta ar psykologins term -- den obetingade reflexen, den man fods med till "
     "skillnad fran den betingade som lars in (Pavlovs hundar). Tillagd som betydelse 1. Att den "
     "saknades ar allvarligt just for HP: 'obetingad reflex' ar ett staende uttryck i "
     "gymnasiebiologi och psykologi, och ett kort som bara ger 'ovillkorlig' gor det uttrycket "
     "obegripligt. Betydelse 1 har ingen belagd enordssynonym -- kategori '≈≈ medfodd' satt ur "
     "kortets egen definition (ingen kalla kravs for ≈≈). 'ovillkorlig' och 'forbehallslos' star "
     "bada i synonymer.se (belagda), och 'forbehallslos' ar dessutom SAOL:s hela definition och "
     "OLD-facit. SYNONYM BORTTAGEN: legacys 'absolut' stod ordagrant i definitionen och var darmed "
     "en upprepning, inte en synonym. REGISTER: betydelse 1 fackspraklig med doman psykologi; "
     "betydelse 2 neutral (legacys 'formell' saknar stod i bada ordbockerna). Exempelmeningen ar "
     "SO:s eget syntex och visar betydelse 2, oforandrad -- SO:s syntex for betydelse 1 ('en "
     "bestammelse med obetingad giltighet') hor egentligen till betydelse 2 den ocksa, sa "
     "ordboken erbjuder ingen battre. Etymologi ny: sammansattningen (o- + betinga) ar "
     "genomskinlig, och kontrasten betingad/obetingad reflex ar sjalva nyckeln till den nya "
     "betydelse 1."),

"agrar": dict(
  hb="Som har med jordbruk att göra, eller är präglad av jordbruk ; person som driver jordbrukets "
     "intressen i politiken",
  reg="neutral, neutral, lantbruk ; neutral, neutral, politik",
  grp=[["jordbruks-", "lantbruks-"], ["bondepolitiker"]],
  ex='Sverige var fram till 1900-talet i grunden ett <font color="#3498db">agrart</font> samhälle.',
  etym="av latin agrarius 'som hör till jordbruket', till ager 'åker'",
  sl="SAKNAD BETYDELSE. SO ger fyra led: 'som har att gora med jordbruk', 'dominerad av jordbruk', "
     "'PERSON SOM REPRESENTERAR JORDBRUKSINTRESSEN' och 'jordbrukare'. Legacy hade bara "
     "adjektivet ('Som hor till jordbruket'). Substantivbetydelsen ar ingen utvidgning utan en "
     "egen ordklass med egen definitionstext, och SAOL bekraftar den som eget led ('foresprakare "
     "for jordbruksintressen'); synonymer.se inleder rentav hela sin lista med 'bondepolitiker'. "
     "Tillagd. Adjektivets tva SO-led ('har att gora med' resp. 'dominerad av') ar samma betydelse "
     "med olika styrka och star pa en rad, med bada varianterna namnda ('har med jordbruk att "
     "gora, eller ar praglad av'). RISKFLAGGA old_delar_inget_ordforrad utredd: OLD sager "
     "'jordbruksanknuten', kortet 'hor till jordbruket' -- samma sak, olika ord; flaggan ar falsk. "
     "'jordbruks-' och 'lantbruks-' lag redan pa kortet och star ordagrant i SAOL:s led (belagda); "
     "'bondepolitiker' star i synonymer.se (belagd). REGISTER ANDRAT: 'formell' saknar stod -- "
     "varken SO eller SAOL markerar ordet; domaner (lantbruk, politik) tillagda, en per "
     "betydelse. Exempelmeningen matchar SO:s syntex 'det gamla agrara samhallet', oforandrad. "
     "Etymologi ny, ur SO -- 'ager' = aker ar samma rot som i agronom och areal."),

"strimmig": dict(
  hb="Försedd med smala, ofta oregelbundna ränder",
  reg="neutral, neutral",
  grp=[["strimmad", "≈ randig"]],
  ex='Katten var grå och <font color="#3498db">strimmig</font> över ryggen.',
  etym=None,
  sl="SO: 'forsedd med (oregelbundna) smala rander' -- legacys huvudbetydelse matchar ordagrant "
     "inklusive parentesens 'oregelbundna' (kortet har 'ofta oregelbundna', vilket ar precis vad "
     "SO:s parentes betyder). Oforandrad. SYNONYMER RATTADE, och det ar hela andringen: legacy "
     "hade EN post, '≈≈ randig' -- alltsa markt som KATEGORI. Det ar fel niva pa tva satt. For det "
     "forsta ar 'randig' inget kategoriord utan ett vanligt, fullt existerande svenskt adjektiv, "
     "sa markningen ska vara '≈' (narmaste befintliga ord), inte '≈≈'. For det andra fanns hela "
     "tiden en riktig, fullt utbytbar synonym att ha: 'strimmad', som star i synonymer.se allra "
     "forst i listan. Den star nu omarkerad (fullt utbytbar, belagd), med '≈ randig' efter -- "
     "randig ar narapa men inte samma sak, eftersom randigt normalt betyder REGELBUNDNA rander "
     "medan SO uttryckligen sager 'oregelbundna' om strimmigt. Aven '≈ randig' ar belagd i "
     "synonymer.se. Register oforandrat; ingen ordbok ger brukligheskommentar. Exempelmeningen "
     "matchar SO:s eget syntex 'en strimmig katt', oforandrad. ETYMOLOGI UTELAMNAD: SO:s post "
     "saknar historiska uppgifter, ingen kalla att ha."),

"svängtapp": dict(
  hb="Kort cylindrisk axel som något annat kan svänga runt",
  reg="fackspråklig, neutral, teknik",
  grp=[["pivå", "axeltapp"]],
  ex='Luckan satt på en <font color="#3498db">svängtapp</font> och kunde fällas åt båda hållen.',
  etym=None,
  sl="SO: 'tappliknande konstruktion som nagot kan svanga kring', med en SYN:synonym-taggad "
     "underbetydelse. ORDET I SIN EGEN DEFINITION: legacy sa 'TAPPliknande del som nagot kan "
     "svanga runt' -- bade 'tapp' och 'svanga' ur uppslagsordet svangTAPP, sa den som inte redan "
     "visste vad en tapp ar fick ingen hjalp. Omskrivet till 'Kort cylindrisk axel', som beskriver "
     "saken i stallet for att namna den. SYNONYM UPPGRADERAD: legacy hade '≈≈ vridpunkt', alltsa "
     "en KATEGORI satt ur kortets egen text -- men det fanns hela tiden en belagd, fullt utbytbar "
     "synonym: 'piva', som ar bade SO:s egen SYN-taggade korshanvisning, OLD-facit (som sager "
     "just och endast 'piva') och forsta posten i synonymer.se. Kategorin ersatt med 'piva' plus "
     "'axeltapp' (ocksa synonymer.se, belagd). Det loser aven riskflaggan "
     "old_delar_inget_ordforrad: OLD sa 'piva' och kortet sa 'vridpunkt' -- de delade inget "
     "ordforrad darfor att kortet undvek det ord bada ordbockerna anvander. Register och doman "
     "oforandrade (ordet ar rent tekniskt fackssprak). Exempelmening oforandrad. ETYMOLOGI "
     "UTELAMNAD: SO:s post saknar historiska uppgifter."),

"hedendom": dict(
  hb="Religiös tro helt utan samband med kristendom, judendom och islam ; ibland: att helt sakna "
     "religion",
  reg="neutral, neutral, religion ; neutral, neutral, religion",
  grp=[["paganism"], ["religionslöshet", "ateism"]],
  ex='Forntida <font color="#3498db">hedendom</font> präglades av dyrkan av många gudar.',
  etym="fornsvenska hedhindomber",
  sl="SAKNAD BETYDELSE. SO ger tva: 'religios tro helt utan samband med kristen, judisk och "
     "muslimsk tradition' och -- 'nagon gang spec.' -- 'ATEISM'. Legacy hade bara den forsta. Den "
     "andra bekraftas starkt fran andra hallet: OLD-facit sager ett enda ord, 'RELIGIONSLOSHET', "
     "och synonymer.se avslutar sin lista med 'ateism, gudsforneklse, religionsloshet'. Det "
     "forklarar riskflaggan old_delar_inget_ordforrad -- OLD beskrev den betydelse kortet saknade. "
     "Tillagd, med SO:s reservation 'ibland' kvar i texten eftersom betydelsen ar ovanligare an "
     "den forsta. SPRAK: legacys 'de abrahamitiska (kristendom, judendom, islam)' -- 'abrahamitisk' "
     "ar ett svarare ord an uppslagsordet sjalvt och bryter mot regeln att forklaringen ska ligga "
     "en niva under. Struket; de tre religionerna namns nu direkt, som SO gor. Aven legacys 'ofta "
     "med manga gudar' struket ur definitionen -- SO har det inte, och det ar inte sant om all "
     "hedendom (t.ex. animism); manggudadyrkan finns kvar i exempelmeningen dar den hor hemma som "
     "typfall. 'paganism' lag redan pa kortet och star i synonymer.se (belagd). "
     "'religionsloshet' och 'ateism' star bada i synonymer.se (belagda), och 'ateism' ar SO:s hela "
     "definition av betydelse 2. Register: ingen ordbok ger brukligheskommentar; doman religion pa "
     "bada. Exempelmeningen behallen for betydelse 1 -- SO:s eget syntex ('hedendomen i det "
     "moderna valfardssamhallet') visar visserligen den nya betydelsen men ar sa kortfattat att "
     "det inte gar att avgora ur meningen sjalv vilken betydelse som avses. Etymologi ny, ur SO."),

"libretto": dict(
  hb="Texten till en opera eller operett — sångtexten och handlingen, inte musiken",
  reg="neutral, neutral, musik",
  grp=[["operatext", "librett"]],
  ex='<font color="#3498db">Librettot</font> till operan var skrivet av en känd poet.',
  etym="av italienska libretto, egentligen 'liten bok'; till latin liber 'bok', samma ord som i "
       "exlibris",
  sl="SO: 'text till opera ELLER OPERETT'. SAOL: 'text till opera el. operett'. Legacy hade bara "
     "'Text till en opera' -- operetten saknades, trots att BADA ordbockerna namner den "
     "uttryckligen och att ordet anvands lika sjalvklart om bada. Tillagd. Ocksa tillagt: vad "
     "librettot INTE ar. Att det galler sangtexten och handlingen men inte musiken ar den enda "
     "sak man behover veta for att inte blanda ihop libretto med partitur, och ingen av "
     "definitionerna sager det rakt ut. 'operatext' lag redan pa kortet och star i synonymer.se "
     "(belagd); 'librett' star ocksa dar (belagd) och ar den forsvenskade formen -- vard att ha "
     "med eftersom den dyker upp i aldre text. REGISTER ANDRAT: 'formell' saknar stod -- varken "
     "SO eller SAOL markerar ordet; doman musik tillagd. Exempelmening oforandrad. Etymologi ny, "
     "ur SO inklusive SO:s egen hanvisning till exlibris: 'liten bok' forklarar ordet direkt "
     "(librettot delades ut som ett litet hafte till publiken), och kopplingen till liber/exlibris "
     "binder det till nagot Adam kanner igen."),
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    f = FIX.get(e["ord"])
    if not f:
        continue
    e["proposed"] = {
        "huvudbetydelse": f["hb"], "register": f["reg"],
        "synonymer": [s for g in f["grp"] for s in g],
        "synonym_groups": f["grp"], "exempelmening": f["ex"],
    }
    if f.get("etym"):
        e["proposed"]["etymologi"] = f["etym"]
    bild = (e.get("legacy") or {}).get("bild_html")
    if bild:
        e["proposed"]["bild_html"] = bild
    e["sokkoll"] = {"kalla": U(e["ord"]), "slutsats": f["sl"]}
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("godkande %d kort" % n)
