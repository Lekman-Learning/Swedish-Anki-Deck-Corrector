# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch2, kort 1-25. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch2.json"
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


satt("ad notam",
     "Lägga något på minnet och rätta sig efter det",
     "ålderdomlig, neutral",
     [],
     "Han fick ta kritiken " + B % "ad notam" + " och ändra sitt sätt att "
     "leda mötena.",
     "→ Latin ad notam 'till anteckning' — något man för in i minnet.",
     "SO: 'som foreskrift'. Wiktionary ger uttrycket: 'ta ad notam: lagga "
     "pa minnet, ratta sig efter'. OLD-facit 'lagga pa minnet' stammer och "
     "ar behallet i sak. Legacys synonymer (nota, nata, notat) ar strukna "
     "-- de ar ljudlika ord, inte utbytbara mot uttrycket. Ordet anvands i "
     "praktiken bara i frasen 'ta ad notam'.")

satt("angöra",
     "Om fartyg: lägga till vid en hamn eller brygga ; sikta in sig mot land "
     "för att få reda på var man befinner sig",
     "fackspråklig, neutral, sjöfart ; fackspråklig, neutral, sjöfart",
     [],
     "Färjan " + B % "angjorde" + " Helsingborg strax före midnatt.",
     None,
     "SO ger tre betydelser: '(lata) ga in i', '(lata) lagga till vid' och "
     "'ta sakra siktmarken av'. De tva forsta ar samma handling och slas "
     "ihop; den tredje ar navigationsbetydelsen och behalls separat. SAOL "
     "bekraftar 'lagga till vid brygga, ga in i hamn'. Inga synonymer "
     "belagda i SO/SAOL:s definitionstext.")

satt("avslå",
     "Säga nej till en ansökan eller ett förslag ; slå tillbaka ett anfall",
     "neutral, neutral ; neutral, neutral",
     ["avvisa", "förkasta"],
     "Nämnden " + B % "avslog" + " hans ansökan utan att ange något skäl.",
     None,
     "SO: 'forklara (ansokan eller dylikt) inte beviljad' samt 'prestera "
     "tillrackligt forsvar mot'. SAOL: 'inte bevilja'. Bada betydelserna "
     "behalls -- forsvarsbetydelsen ar den som overraskar. 'avvisa' och "
     "'forkasta' star som JFR i SO och ar utbytbara i forsta betydelsen. "
     "'avstyrka' ar struket: att avstyrka ar att rekommendera avslag, inte "
     "att besluta det -- olika roller.")

satt("barbarisk",
     "Så grym och hänsynslös att det bryter mot de mest grundläggande "
     "reglerna för hur människor ska behandla varandra",
     "neutral, negativ",
     [],
     "Attacken fördömdes som " + B % "barbarisk" + " av samtliga partier.",
     None,
     "SO: 'som bryter mot grundlaggande regler for mansklig samlevnad'. "
     "SAOL: 'ra, ohyfsad'. SO:s definition ar den starkare och den som "
     "anvands i dag -- SAOL:s 'ohyfsad' underdriver. JFR i SO: "
     "'ociviliserad', 'ra' -- bada strukna som synonymer eftersom de ar "
     "svagare an barbarisk och inte utbytbara i exemplet.")

satt("befaren",
     "Om sjöman: som har gjort långa resor till sjöss och därför kan yrket",
     "fackspråklig, neutral, sjöfart",
     ["berest"],
     "Bara " + B % "befarna" + " matroser fick plats i besättningen.",
     None,
     "SO: 'som har gjort langre resor', med exemplen 'befaren jungman; "
     "befaren matros; befaren maskinpersonal' -- alla sjofartstermer. SAOL "
     "ger 'berest' direkt i definitionstexten, darfor belagd synonym. "
     "Ordet ar en formell grad i handelsflottan (motsats: obefaren), inte "
     "ett allmant omdome om nagon som rest mycket.")

satt("fäbod",
     "Enkel gård i skogen eller fjällen dit man förde djuren på sommaren för "
     "att de skulle få beta",
     "neutral, neutral, historisk",
     [],
     "På " + B % "fäboden" + " gjorde de ost och smör hela sommaren.",
     None,
     "SO: 'anlaggning for utnyttjande under sommaren av betesmarker pa "
     "langre avstand fran lantgarden', markt 'mest historiskt'. SAOL "
     "bekraftar. Wiktionarys 'litet skjul for boskap' ar for snavt -- en "
     "fabod ar en anlaggning dar folk bodde och arbetade, inte ett skjul. "
     "Definitionen ar skriven med korta vardagsord eftersom 'betesmark' "
     "och 'anlaggning' bada ligger over uppslagsordets niva.")

satt("grumlig",
     "Så full av små partiklar att man inte kan se igenom ; bildligt: oklar "
     "och tveksam",
     "neutral, neutral ; neutral, negativ",
     ["grumsig", "oklar"],
     "Vattnet i brunnen blev " + B % "grumligt" + " efter regnet.",
     None,
     "SO: 'fordunklad eller ogenomskinlig pa grund av (riklig) forekomst av "
     "sma partiklar', med explicit 'av. bildligt' for betydelsen 'oklar, "
     "tvivelaktig'. SAOL: 'inte klar, grumsig; av. bildl.' -- 'grumsig' "
     "star darmed i SAOL:s definitionstext. 'oklar' tacker den bildliga "
     "betydelsen. Motsatsen 'klar' finns som MOTSATS i SO.")

satt("gräsrötter",
     "De vanliga medlemmarna i en rörelse eller ett parti, till skillnad "
     "från de som bestämmer",
     "vardaglig, neutral, politik",
     [],
     "Beslutet måste förankras hos " + B % "gräsrötterna" + " innan det "
     "går igenom.",
     "→ Efter engelskans grass roots — det som växer underifrån.",
     "Uppslagsformen 'grasrotter' gav INGEN traff i SO/SAOL/SAOB -- ordet "
     "ar plural. Slog darfor upp grundformen 'grasrot' separat (samma "
     "datum, HTTP 200): SO 'vanlig, enkel manniska', SAOL 'sarsk. bildl. "
     "vanlig manniska i mots. till makthavare', bruk 'vardagligt; sarsk. i "
     "politiska sammanhang'. SO:s exempel star i plural: 'beslutet maste "
     "forankras hos grasrotterna'. Etymologin ar med for att den gor ordet "
     "sjalvforklarande.",
     extra=("https://svenska.se/api/msearch?ord=gr%C3%A4srot",))

satt("hallstämpel",
     "Tydligt märke som visar vem som ligger bakom något",
     "neutral, neutral",
     ["kännemärke"],
     "Tavlan bär en stor konstnärs " + B % "hallstämpel" + ".",
     "→ Ursprungligen stämpeln som hallrätten satte på granskade varor.",
     "SO: 'kannetecken', med tillagget 'ursprungligen om stampel pa "
     "felfria varor som granskats av hallratt'. SAOL: 'kannemarke, pragel' "
     "-- 'kannemarke' darmed belagd i definitionstexten. Etymologin ar "
     "medtagen eftersom ordet annars ar ogenomskinligt: 'hall' syftar pa "
     "hallratten, inte pa en hall. Nutidsbetydelsen ar bildlig, belagd "
     "sedan 1835.")

satt("kortsynt",
     "Som bara tänker på det som händer snart och struntar i vad som kommer "
     "sedan",
     "neutral, negativ",
     [],
     "Att spara in på underhållet var " + B % "kortsynt" + " och kostade "
     "dubbelt så mycket några år senare.",
     None,
     "SO: 'som bara tar hansyn till den narmaste framtiden', med "
     "'nagon gang av. om person'. SAOL: 'som bara planerar pa kort sikt'. "
     "Ordet handlar INTE om synen -- narsynt ar det medicinska ordet. Den "
     "forvaxlingen ar sannolikt den vanligaste och ar skalet att "
     "definitionen sager 'tanker', inte 'ser'.")

satt("medelst",
     "Med hjälp av",
     "ålderdomlig, neutral",
     ["genom"],
     "Han dömdes för bedrägeri " + B % "medelst" + " urkundsförfalskning.",
     None,
     "SO: 'med hjalp av', bruk 'nagot alderdomligt'. SAOL identisk: 'med "
     "hjalp av'. JFR i SO: 'genom' -- belagd och utbytbar. Ordet lever i "
     "praktiken kvar i juridiskt sprak, vilket exempelmeningen speglar "
     "(SO:s eget exempel ar 'bedrageri medelst urkundsforfalskning').")

satt("skäkta",
     "Pil till armborst ; rensa bort de hårda delarna ur lin eller hampa",
     "ålderdomlig, neutral, historisk ; fackspråklig, neutral",
     [],
     B % "Skäktan" + " träffade skölden med en smäll.",
     None,
     "SO ger tre skilda betydelser: 'armborstpil med brett blad', 'slakta "
     "(kreatur) genom skaktning' och 'rensa bort vedartade delar fran'. De "
     "tva forsta och tredje ar OLIKA ord med olika ursprung (SAOB skiljer "
     "dem at). Slaktbetydelsen ar utelamnad: den ar en religios fackterm "
     "(judisk ritualslakt) och skulle krava egen forklaring for att inte "
     "missforstas. Pilbetydelsen ar den som star forst i bade SO och SAOL.")

satt("stetoskop",
     "Instrument som läkaren lyssnar på hjärta och lungor med",
     "neutral, neutral, medicin",
     [],
     "Läkaren satte " + B % "stetoskopet" + " mot hans bröst och bad honom "
     "andas djupt.",
     "→ Grekiska stethos 'bröst' och skopein 'se' — att undersöka bröstet.",
     "SO: 'ett medicinskt instrument for avlyssning av hjarta och lungor'. "
     "SAOL i det narmaste ordagrant samma. Definitionen ar omskriven till "
     "'lyssnar pa' i stallet for 'avlyssning', eftersom avlyssning i "
     "modern svenska starkast associerar till telefonavlyssning. "
     "Etymologin ar medtagen for att den forklarar varfor ett "
     "lyssnarinstrument har ett namn som betyder 'se'.")

satt("tjuga",
     "Gaffel med långt skaft som man lyfter hö med ; vardagligt: "
     "tjugokronorssedel",
     "neutral, neutral ; vardaglig, neutral",
     ["hötjuga"],
     "Han lyfte höet upp på vagnen med en " + B % "tjuga" + ".",
     None,
     "SO ger bada: 'hogaffel' och 'tjugokronorssedel' (den senare markt "
     "vardagligt, belagd sedan 1990). SAOL identisk. JFR i SO: 'hotjuga' "
     "-- belagd synonym for forsta betydelsen. 'Hogaffel' ar undviket i "
     "huvudbetydelsen eftersom det sjalvt ar ett ovanligt ord; en kort "
     "fras ('gaffel med langt skaft som man lyfter ho med') ar tydligare "
     "utan att tappa precision.")

satt("trivsam",
     "Som gör att man känner sig hemma och mår bra",
     "neutral, positiv",
     ["mysig", "gästvänlig"],
     "De hittade en liten " + B % "trivsam" + " restaurang i en gränd.",
     None,
     "SO: 'som vacker kanslor av trevnad och valbefinnande'. SYN i SO: "
     "'gastvanlig', 'mysig' -- bada explicit markta som synonymer och "
     "darmed belagda. Definitionen ar omskriven till vardagsord eftersom "
     "'trevnad' och 'valbefinnande' bada ligger over uppslagsordets niva. "
     "Ordet bildat till 'trivas', vilket gor etymologi overflodig.")

satt("anemisk",
     "Som har för lite blod eller för få röda blodkroppar ; bildligt: blek "
     "och utan kraft",
     "fackspråklig, neutral, medicin ; neutral, negativ",
     ["blodfattig"],
     "Uppsättningen fick svidande kritik för sin " + B % "anemiska" +
     " regi.",
     None,
     "SO: 'som har att gora med anemi', 'som lider av anemi' och -- markt "
     "'av. bildligt' -- 'uddlos, farglos'. SAOL: 'blodfattig; bildl. blek, "
     "ointressant', vilket belagger 'blodfattig' som synonym. De tva "
     "medicinska betydelserna slas ihop; den bildliga behalls separat "
     "eftersom den ar den som dyker upp i text utanfor varden. Ordet "
     "'anemi' undviks i definitionen -- det forklarar inte, det upprepar.")

satt("bevista",
     "Vara på plats vid något som anordnas",
     "formell, neutral",
     ["närvara"],
     "Allmänheten har rätt att " + B % "bevista" + " domstolens "
     "förhandlingar.",
     None,
     "SO: 'vara narvarande vid'. SAOL: 'narvara vid' -- 'narvara' darmed "
     "belagd i definitionstexten. Ordet forvaxlas latt med 'besoka', men "
     "bevista anvands om arrangemang man ar publik vid (premiar, "
     "forhandling, gudstjanst), inte om platser man beger sig till. "
     "Definitionen sager darfor 'nagot som anordnas'.")

satt("budget",
     "Plan över vilka pengar som finns och vad de ska gå till under en viss "
     "tid",
     "neutral, neutral",
     [],
     "Kommunen lade en stram " + B % "budget" + " för nästa år.",
     None,
     "SO: 'plan med angivande av tillgangliga medel och deras fordelning pa "
     "olika poster under viss tid'. SAOL: 'plan over beraknade inkomster "
     "och utgifter t.ex. for ett ar'. Definitionen ar omskriven till "
     "vardagsord. SO:s andra betydelse ('lagpris-', som forled i "
     "sammansattningar: budgethotell) ar utelamnad -- den ar inte ett "
     "sjalvstandigt ord utan ett prefixbruk.")

satt("erotisk",
     "Som har med kärlek och lust mellan människor att göra",
     "neutral, neutral",
     [],
     "Utställningen visade " + B % "erotisk" + " konst från 1700-talet.",
     None,
     "SO: 'som har att gora med erotik' samt 'som har starka sexuella "
     "behov' (om person). Den andra betydelsen ar sallsynt i nutida bruk "
     "och utelamnad. JFR i SO: 'amoros' -- struket som synonym, det ar "
     "betydligt ovanligare an erotisk och skulle forklara latt med svart. "
     "Definitionen anvander 'karlek och lust' i stallet for 'erotik', "
     "eftersom ordet inte far sta i sin egen forklaring.")

satt("malign",
     "Om sjukdom eller tumör: elakartad och farlig",
     "fackspråklig, neutral, medicin",
     ["elakartad"],
     "Provet visade att tumören var " + B % "malign" + ".",
     "→ Latin malus 'ond' — motsatsen benign kommer av bonus 'god'.",
     "SO: 'som utvecklas pa elakartat satt', bruk 'med.'. SAOL: "
     "'elakartad' -- belagd synonym. MOTSATS i SO: 'benign'. Etymologin ar "
     "med eftersom paret malign/benign blir sjalvforklarande av den (ond/"
     "god) och benign annars ar latt att blanda ihop. Wiktionarys "
     "'illvillig, illasinnad' ar en allmansprakig bibetydelse som inte "
     "star i SO och darfor inte tas med.")

satt("provisorisk",
     "Som ska fungera tills vidare, tills något bättre kommer på plats",
     "neutral, neutral",
     ["tillfällig"],
     "De satte upp ett " + B % "provisoriskt" + " tak av presenning över "
     "hålet.",
     None,
     "SO: 'som avses fungera under en overgangstid'. SAOL: 'enbart "
     "gallande for tillfallet el. tills vidare'. JFR i SO: 'tillfallig', "
     "'interimistisk'. 'tillfallig' behalls som synonym; 'interimistisk' "
     "ar struket -- det ar ett ovanligare ord an provisorisk och bryter "
     "regeln att inte forklara svart med svart.")

satt("reflektera",
     "Tänka igenom något ordentligt ; om ljus eller ljud: kastas tillbaka "
     "från en yta",
     "neutral, neutral ; fackspråklig, neutral",
     ["begrunda", "spegla"],
     "Hon bad studenterna " + B % "reflektera" + " över texten innan "
     "seminariet.",
     None,
     "SO ger bada huvudbetydelserna: '(noga) tanka igenom' och "
     "'aterkasta'. SAOL: 'aterkasta, aterspegla' samt 'tanka, eftersinna'. "
     "JFR i SO: 'begrunda', 'fundera', 'spegla'. 'begrunda' och 'spegla' "
     "behalls, en per betydelse, grupperade i samma ordning. Tankbetydelsen "
     "star forst eftersom den ar den vanligaste i lopande text.")

satt("stötvis",
     "Som kommer i korta ryck med uppehåll emellan",
     "neutral, neutral",
     [],
     "Hans andning blev " + B % "stötvis" + " och ytlig.",
     None,
     "SO: 'som sker eller kommer i stotar', med exemplet 'hans stotvisa "
     "andhamtning'. INGEN traff i SAOL eller Wiktionary -- ordet ar belagt "
     "endast via SO (belagt sedan 1866). Definitionen undviker ordet "
     "'stot' eftersom det ar samma ord som ska forklaras; 'korta ryck med "
     "uppehall emellan' sager samma sak utan cirkularitet.")

satt("anfang",
     "Stor utsmyckad begynnelsebokstav i början av ett kapitel ; den yta "
     "längst ner som ett valv vilar på",
     "fackspråklig, neutral, typografi ; fackspråklig, neutral, byggnad",
     [],
     "Varje kapitel inleddes med ett rikt utsirat " + B % "anfang" + ".",
     "→ Tyska Anfang 'början' — bokstaven som börjar texten.",
     "SO ger bada: 'storre, rikt utsmyckad begynnelsebokstav' och 'en "
     "valvbages nedersta begransningsyta'. SAOL bekraftar bada. JFR i SO: "
     "'impost', 'slutsten' -- bada strukna, de ar andra byggnadsdelar, "
     "inte synonymer. Etymologin ar med for att den gor typografiska "
     "betydelsen sjalvforklarande. De tva betydelserna delar ursprung men "
     "SAOB skiljer dem at som separata artiklar.")

satt("anlete",
     "Ansikte",
     "högtidlig, neutral",
     ["ansikte"],
     "Ett leende lyste upp hans " + B % "anlete" + ".",
     None,
     "SO: 'ansikte', med tillagget 'ofta i religiosa sammanhang' och bruk "
     "'nagot hogtidligt'. SAOL: 'ansikte'. Rakt synonympar -- ordet ar en "
     "stilniva, inte en betydelseskillnad. Lever framst kvar i uttrycket "
     "'i sitt anletes svett' och i religiost sprak ('infor Guds anlete'). "
     "Belagt sedan forra halften av 1300-talet.")

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("skrev %d av %d kort" % (sum(1 for k in KORT if k.get("proposed")),
                               len(KORT)))
