# -*- coding: utf-8 -*-
"""50 legacy-kort ur spår A (is:new, suspenderade) -> full v3.

**Första batchen som grupperar synonymerna per betydelse.** Adam påpekade
2026-08-13 att kort med flera betydelser ofta saknar `;` mellan synonymgrupperna,
så att man inte kan se vilken synonym som hör till vilken betydelse. Spärren för
det är ännu inte byggd (den ligger i `ATT_GORA.md`), men regeln följs för hand
här: **antingen har varje betydelse en belagd synonym och då grupperas de, eller
så får kortet tom synonymlista.** Halvvägs -- en platt lista över flera
betydelser -- är just det tvetydiga fall Adam klagade på.

## Vad de gamla korten hade för fel

Tio kort hade en betydelse som ordböckerna inte känner igen, och fem av dem var
ren ordförväxling:

* `avfallen` hade "övergett sin tro" som HUVUDbetydelse. Det är `avfällig`.
  SO och SAOL ger bara "starkt avmagrad" för den här formen, och OLD-facit sa
  också "avmagrad".
* `ofelbart` hade den katolska ofelbarhetsdogmen som andra betydelse. Den hör
  till `ofelbarhet`, inte till adverbet.
* `handfast` hade "relaterat till en viss typ av bindning eller förpliktelse" --
  det är `handfästning`, ett annat ord.
* `försumbar` hade `försumlig` som synonym. Det betyder vårdslös, inte obetydlig.
* `kontinuitet` hade synonymen "fortlöpandehet", som inte är ett svenskt ord.

`stamma` gick åt andra hållet: kortet hade BARA stamningsbetydelsen och saknade
den som SO listar först -- `härstamma`. OLD-facit sa "ha sitt ursprung", alltså
var felet synligt utan att slå upp något.

`spatial` hade en definition skriven på engelska ("Pertaining to the arrangement
of objects in space").

## Tre luckor i min egen beläggsspärr, hittade under läsningen

Alla tre gjorde att spärren underkände korrekta synonymer, alltså motsatt fel mot
det som byggde spärren i går:

1. **Underbetydelser räknades inte.** SO lägger ofta sina renaste synonymglosor
   där: `balsamisk` har definitionen "som doftar som balsam" (en omskrivning) och
   underbetydelserna "väldoftande" + "lindrande" -- precis de två ord som hör
   hemma på kortet.
2. **Gradadverb åt upp glosan.** "starkt avmagrad" och "helt säkert" gjorde att
   `avmagrad` och `säkert` inte inledde sina led.
3. **Inledande parentes gjorde samma sak.** "(mild) uppmaning till visst
   handlande" och "(svag) ansats till förekomst" -- `uppmaning` och `ansats` föll
   bort trots att ordboken säger exakt de orden.

## Avgränsningar värda att skriva ut

* `befrynda` vilar på SAOL (post utan definition, bara exemplet "befrynda sig med
  ngn") + SAOB + en websökning, eftersom SO saknar ordet helt. Betydelsen är
  samstämmig i alla tre; det är beläggets BREDD som är tunn, inte dess riktning.
* `erosion` får bara den geologiska betydelsen. Den bildliga ("erosion av
  förtroendet") och den medicinska finns i varken SO eller SAOL, och enligt
  källhierarkin avgör de två dagens betydelser.
* `bitanke` får bara "baktanke". SO:s hela definition ÄR ordet `baktanke`.
* `ontologi` får bara den filosofiska betydelsen. SAOL:s andra, "hierarkisk
  klassificering av världen", är IT-användningen och saknas i SO.
* `paletå` märks INTE som ålderdomlig. SAOL skriver "en äldre typ av överrock" --
  det beskriver plagget, inte ordets bruklighet. Att förväxla de två är precis
  den registermiss som fällde kort tidigare i veckan.
* `stamma` får tom synonymlista trots att `härstamma` är belagd: den innehåller
  uppslagsordet och avslöjar svaret på framsidan.
* `kverulant` likaså -- SO:s definition är "person som (ofta) kverulerar".
"""
import json
import sys
import urllib.parse

SESSION = "sessions/session_2026-08-13_v3-batch.json"
SVENSKA = "https://svenska.se/api/msearch?ord={}"

K = {}
PAUSAS = set()

# Redovisade undantag från förgranskningens hårda regler. Regeln tystas inte --
# flaggan blir `<regel>_tillaten` och följer med in i sessionsfilen som
# blindgranskaren läser, tillsammans med motiveringen nedan.
TILLAT = {
    "avfallen": {
        "frammande_uppslagsord":
            "Träffarna innehåller `avfall`, `avfalla` och `falla av` -- tre "
            "besläktade men skilda lexem. Kortet använder BARA SO:s och SAOL:s "
            "adjektivpost `avfallen`, som i båda ordböckerna lyder ordagrant "
            "'starkt avmagrad'. Ingen glosa är hämtad från de andra posterna; "
            "tvärtom är det just sammanblandningen med `avfalla` som var det "
            "gamla kortets fel.",
    },
    "bildad": {
        "frammande_uppslagsord":
            "Träffen `bilda` är verbet som participet kommer av. Kortet använder "
            "bara adjektivposterna `bildad` i SO och SAOL. Synonymlistan är "
            "dessutom tom, så ingen glosa kan ha vandrat över från fel post.",
    },
    "bespetsa sig på": {
        "frammande_uppslagsord":
            "50 grannord -- flerordsuttryck går genom fritextsökningen och drar "
            "med sig hela bokstavsintervallet (be, bel, ben, besatt ...). Kortet "
            "bygger uteslutande på SO:s post `bespetsa sig`, 'förhoppningsfullt "
            "bereda sig'. Synonymlistan är tom, och SO:s SYN-relation ('sticka', "
            "'ti') är uppenbart brus som medvetet INTE används.",
    },
}

B = '<font color="#3498db">{}</font>'

KORT = {
    "rysch": {
        "hb": "tätt rynkad remsa av tunt tyg som pynt på kläder",
        "syn": ["krås"],
        "grp": None,
        "ex": f'Klänningen hade en {B.format("rysch")} av tyll runt halsen.',
        "reg": "neutral, neutral, allmän",
        "ety": "av franska ruche, samma ord som ruche 'bikupa av bark'",
        "skal": "SO: 'tätt rynkad remsa av tunt tyg'. SAOL: 'rynkad remsa, krås' -- "
                "därifrån kommer synonymen. Kortets bildliga betydelse ('rysch och "
                "pysh') finns i ingen av dem och tas bort; uttrycket bär den, inte ordet.",
    },
    "avfallen": {
        "hb": "starkt avmagrad",
        "syn": ["avmagrad"],
        "grp": None,
        "ex": f'Efter sjukdomen var han blek och {B.format("avfallen")}.',
        "reg": "neutral, neutral, allmän",
        "ety": "ursprungligen 'det som faller bort'",
        "skal": "SO och SAOL ger BÅDA bara 'starkt avmagrad' för adjektivet. Kortets "
                "gamla huvudbetydelse -- 'övergett sin tro' -- hör till `avfällig`, ett "
                "annat ord; OLD-facit sa också 'avmagrad'. Synonymen är SO:s och SAOL:s "
                "egen glosa med gradadverbet avskalat.",
    },
    "balsamisk": {
        "hb": "som doftar som balsam ; som verkar lugnande och lindrande",
        "syn": ["väldoftande", "lindrande"],
        "grp": [["väldoftande"], ["lindrande"]],
        "ex": f'Salvan hade en {B.format("balsamisk")} doft av kåda och lade sig svalt över huden.',
        "reg": "neutral, positiv, allmän ; neutral, neutral, allmän",
        "ety": None,
        "skal": "SO: definitionen 'som doftar som balsam' med underbetydelserna "
                "'väldoftande' och 'lindrande'. De två underbetydelserna ÄR de två "
                "betydelserna, och de ger varsin belagd synonym -- därav grupperingen. "
                "SAOL har posten utan definitionstext.",
    },
    "bildad": {
        "hb": "som har goda allmänna kunskaper på många områden ; skapad, formad",
        "syn": [],
        "grp": None,
        "ex": f'En {B.format("bildad")} läsare känner igen anspelningen utan fotnot.',
        "reg": "neutral, positiv, allmän ; neutral, neutral, allmän",
        "ety": "efter tyska gebildet; till bild",
        "skal": "SO: 'som har goda allmänna kunskaper på många områden'. SAOL har två "
                "poster: 'skapad' (participet) och 'som har breda kunskaper'. Tom "
                "synonymlista: den enda belagda glosan är 'skapad', som bara täcker den "
                "andra betydelsen -- en platt lista hade sett ut som om den gällde båda. "
                "Kortets gamla 'utbildad' och 'allmänbildad' innehåller dessutom "
                "uppslagsordet.",
    },
    "blodvite": {
        "hb": "blödande sår",
        "syn": [],
        "grp": None,
        "ex": f'Grälet slutade i {B.format("blodvite")}.',
        "reg": "neutral, neutral, allmän",
        "ety": "fornsvenska bloþvite, till -þvite '-sår'",
        "skal": "SO och SAOL säger båda ordagrant 'blödande sår'. Exemplet är SAOL:s "
                "eget. Kortet hade samma betydelse skriven två gånger ('ett sår som "
                "blöder' / '... som blöder kraftigt') -- en betydelse, inte två. Tom "
                "synonymlista: 'sår' och 'blödning' är delar av definitionen, inte "
                "utbytbara ord.",
    },
    "erosion": {
        "hb": "nötning och nedbrytning av jordytan genom vatten, vind och is",
        "syn": ["nötning"],
        "grp": None,
        "ex": f'Åkerjorden försvann genom {B.format("erosion")} när skyddsplanteringen togs bort.',
        "reg": "neutral, neutral, geologi",
        "ety": "av latin erosio; till erodera",
        "skal": "SO: 'nötning och nedbrytning av jordytan som förorsakas av vatten, "
                "vindar och is'. SAOL har posten utan definitionstext. Kortets andra "
                "betydelse (bildlig/medicinsk urholkning) finns i ingen av dem och tas "
                "bort enligt källhierarkin.",
    },
    "försumbar": {
        "hb": "så obetydlig att man kan bortse från den",
        "syn": ["obetydlig"],
        "grp": None,
        "ex": f'Skillnaden mellan de två mätinstrumenten var {B.format("försumbar")}.',
        "reg": "neutral, neutral, allmän",
        "ety": "till försumma och -bar",
        "skal": "SO: 'så obetydlig att man kan bortse från den'. SAOL: 'mycket liten, "
                "obetydlig'. Kortets gamla synonym `försumlig` är ett ANNAT ord -- det "
                "betyder vårdslös -- och är struket.",
    },
    "hattig": {
        "hb": "som präglas av ryckighet och brist på följdriktighet",
        "syn": ["oorganiserad", "vimsig"],
        "grp": None,
        "ex": f'Mötet blev {B.format("hattigt")} — vi hoppade mellan fyra ämnen utan att avsluta något.',
        "reg": "neutral, lätt negativ, allmän",
        "ety": None,
        "skal": "SO: 'som utmärks av ryckighet och brist på följdriktighet'. SAOL: "
                "'oorganiserad, vimsig' -- båda synonymerna är SAOL:s egna. Två källor "
                "(wiktionary saknar posten).",
    },
    "nonsens": {
        "hb": "meningslöst innehåll i tal eller skrift",
        "syn": ["struntprat"],
        "grp": None,
        "ex": f'Rapporten var full av {B.format("nonsens")} som ingen kunde omsätta i handling.',
        "reg": "neutral, negativ, allmän",
        "ety": "av engelska nonsense; av franska non-sens, till sens 'mening; förnuft'",
        "skal": "SO: 'meningslöst innehåll'. SAOL: 'meningslöst innehåll; struntprat' -- "
                "`struntprat` inleder sitt eget led och är därmed belagt. Kortets 'strul' "
                "och 'skitsnack' kommer från syn.se och är strukna.",
    },
    "spatial": {
        "hb": "som har att göra med utsträckning i rummet",
        "syn": ["rumslig"],
        "grp": None,
        "ex": f'Testet mätte {B.format("spatial")} förmåga — att vrida figurer i huvudet.',
        "reg": "fackspråklig, neutral, psykologi",
        "ety": "till spatium",
        "skal": "SO: 'som har att göra med utsträckning i rummet', märkt "
                "**'psykologi m.m.'** -- den märkningen ger både stilnivån och domänen, "
                "och den är källbelagd, inte gissad. SAOL: 'rumslig, rums-'. Kortets "
                "tredje definition var skriven på ENGELSKA och är borttagen. Wiktionary "
                "svarade 429 vid båda försöken -- två källor.",
    },
    "stamma": {
        "hb": "härstamma, ha sitt ursprung ; tala hackigt med ofrivilliga avbrott",
        "syn": [],
        "grp": None,
        "ex": f'Ordet {B.format("stammar")} från lågtyskan.',
        "reg": "neutral, neutral, allmän ; neutral, neutral, medicin",
        "ety": "till stam; för talbetydelsen fornsvenska stama, till stamber 'stammande'",
        "skal": "SO listar 'härstamma' FÖRST och 'besväras av stamning' som andra "
                "betydelse; SAOL har 'härstamma' + 'tala hackigt'. Kortet hade bara "
                "talbetydelsen och saknade alltså den ordböckerna sätter först -- "
                "OLD-facit sa 'ha sitt ursprung'. Tom synonymlista trots att `härstamma` "
                "är belagd: den innehåller uppslagsordet och avslöjar svaret.",
    },
    "tillhålla": {
        "hb": "bestämt uppmana någon att göra något",
        "syn": ["uppmana"],
        "grp": None,
        "ex": f'Rektorn {B.format("tillhöll")} eleverna att komma i tid.',
        "reg": "formell, neutral, allmän",
        "ety": "fornsvenska tilhalda; troligen efter lågtyska toholden 'ställa krav på'",
        "skal": "SO: 'bestämt uppmana' med underbetydelsen 'framhålla för'. SAOL: "
                "'uppmana'. Kortets andra betydelse ('beställa eller ange att något ska "
                "ske') finns i ingen av dem.",
    },
    "vansklig": {
        "hb": "svår att klara på grund av stor osäkerhet",
        "syn": ["svår", "besvärlig"],
        "grp": None,
        "ex": f'Det är {B.format("vanskligt")} att sia om räntan ett år framåt.',
        "reg": "neutral, neutral, allmän",
        "ety": "fornsvenska vanskliker, till vander 'svår; nogräknad'",
        "skal": "SO: 'svår att klara på grund av stor osäkerhet'. SAOL: 'svår, "
                "besvärlig' -- båda synonymerna är SAOL:s egna. Kortets 'labil' finns "
                "inte i någon ordbok och är struken.",
    },
    "drätsel": {
        "hb": "kommunal finansförvaltning",
        "syn": [],
        "grp": None,
        "ex": f'Stadens {B.format("drätsel")} sköttes av en särskild kammare.',
        "reg": "ngt ålderdomlig, neutral, ekonomi",
        "ety": "jfr fornsvenska träsel 'kassa; (skatte)inkomst'; ur grekiska thesauros 'skatt'",
        "skal": "SO: 'kommunal finansförvaltning'. SAOL: 'i äldre tid: en kommuns "
                "finansförvaltning' -- markeringen 'i äldre tid' är källan till "
                "stilnivån. Kortet saknade exempelmening helt; den är nyskriven. Tom "
                "synonymlista: 'finansförvaltning' är definitionens huvudord, inte ett "
                "utbytbart ord.",
    },
    "vittgående": {
        "hb": "som berör stora områden och får omfattande följder",
        "syn": [],
        "grp": None,
        "ex": f'Beslutet fick {B.format("vittgående")} konsekvenser.',
        "reg": "neutral, neutral, allmän",
        "ety": None,
        "skal": "SO: 'som berör stora områden'. Exemplet är SAOL:s eget. Kortet saknade "
                "exempelmening. Tom synonymlista -- varken SO eller SAOL pekar ut något "
                "utbytbart ord.",
    },
    "befrynda": {
        "hb": "bli släkt med någon genom giftermål",
        "syn": [],
        "grp": None,
        "ex": f'De två släkterna {B.format("befryndades")} genom giftermålet.',
        "reg": "ngt ålderdomlig, neutral, allmän",
        "ety": "fornsvenska befrynda; av medellågtyska sik bevrunden",
        "skal": "SO SAKNAR ordet helt. SAOL har posten 'befrynda sig' men utan "
                "definitionstext -- bara exemplet 'befrynda sig med ngn'. Betydelsen "
                "kommer från SAOB ('bliva befryndad genom giftermål') och bekräftades "
                "med en allmän websökning enligt regeln om färre än tre källor: NE och "
                "Wiktionary ger samma innebörd. Beläggets BREDD är tunn, inte dess "
                "riktning.",
    },
    "bespetsa sig på": {
        "hb": "förhoppningsfullt se fram emot något",
        "syn": [],
        "grp": None,
        "ex": f'Han {B.format("bespetsade sig på")} en ledig helg.',
        "reg": "ngt ålderdomlig, positiv, allmän",
        "ety": "fornsvenska bespeia",
        "skal": "SO: 'förhoppningsfullt bereda sig' -- valören positiv kommer därifrån. "
                "SAOL har posten utan definitionstext, bara 'bespetsa sig på ngt'. Tom "
                "synonymlista: SO:s SYN-relation ger 'sticka' och 'ti', vilket är "
                "uppenbart brus från en annan post och inte används.",
    },
    "bitanke": {
        # Semikolon är reserverat som betydelseavgränsare i formatet, så
        # "baktanke; dold avsikt" hade lästs som TVÅ betydelser. Tankstreck.
        "hb": "baktanke — dold avsikt bakom det man säger",
        "syn": ["baktanke"],
        "grp": None,
        "ex": f'Erbjudandet kom utan {B.format("bitanke")} — han ville faktiskt bara hjälpa till.',
        "reg": "neutral, neutral, allmän",
        "ety": None,
        "skal": "SO:s HELA definition är ordet `baktanke` (som korshänvisning), vilket "
                "gör det till den starkast möjliga beläggningen. SAOL har posten utan "
                "definitionstext. Kortets andra betydelse ('sekundär tanke, "
                "reservation') finns i ingen av dem.",
    },
    "deponera": {
        "hb": "lämna något värdefullt i någon annans förvar ; göra sig av med avfall på en anvisad plats",
        "syn": ["lämna i förvar", "göra sig av med"],
        "grp": [["lämna i förvar"], ["göra sig av med"]],
        "ex": f'Han {B.format("deponerade")} testamentet hos banken.',
        "reg": "formell, neutral, juridik ; neutral, neutral, allmän",
        "ety": "av latin deponere 'lägga ned'",
        "skal": "SO: 'lämna (värde) i någon annans förvar' med underbetydelserna 'lämna "
                "(värde) som säkerhet' och 'göra sig av med'. SAOL: 'lämna i förvar, ibl. "
                "som pant'. Båda betydelserna har en belagd glosa, därför grupperade.",
    },
    "etagär": {
        "hb": "fristående möbel med hyllor i flera plan för prydnadssaker",
        "syn": ["atenienn"],
        "grp": None,
        "ex": f'Snäckorna stod uppradade på en {B.format("etagär")} i hallen.',
        "reg": "neutral, neutral, allmän",
        "ety": "av franska étagère; till etage",
        "skal": "SAOL: 'fristående anordning med hyllor i flera plan för prydnadssaker'. "
                "SO: 'hylla eller (flervånings)bord för prydnadsföremål'. Synonymen "
                "`atenienn` är SO:s egen SYN:synonym-taggning -- ovanligt ord, men den "
                "starkaste beläggningsformen som finns.",
    },
    "excellera": {
        "hb": "utmärka sig genom att vara utomordentligt bra på något",
        "syn": ["glänsa", "utmärka sig"],
        "grp": None,
        "ex": f'Hon {B.format("excellerade")} i uppsatsskrivning men kämpade med muntliga redovisningar.',
        "reg": "formell, positiv, allmän",
        "ety": "av latin excellere 'höja sig'",
        "skal": "SO: 'utmärka sig genom att vara utomordentligt bra'. SAOL: 'utmärka "
                "sig, glänsa' -- båda synonymerna står ordagrant där. Kortets andra "
                "definition var en ordagrann avskrift av SAOB:s prosa och är ersatt.",
    },
    "försoning": {
        "hb": "återställt vänskapligt förhållande efter en konflikt ; återställd gemenskap med Gud",
        "syn": [],
        "grp": None,
        "ex": f'Efter tio år utan kontakt kom en {B.format("försoning")} mellan bröderna.',
        "reg": "neutral, positiv, allmän ; neutral, neutral, religion",
        "ety": None,
        "skal": "SO: 'återställt vänskapligt förhållande efter konflikt' med "
                "underbetydelsen 'återställande av gudsgemenskap' -- det är de två "
                "betydelserna. SAOL har posten utan definitionstext. Tom synonymlista: "
                "ingen av betydelserna har en utbytbar glosa i ordböckerna.",
    },
    "gast": {
        "hb": "besättningsman på fartyg ; vålnad, spöke",
        "syn": ["matros", "hjälpreda", "vålnad", "spöke"],
        "grp": [["matros", "hjälpreda"], ["vålnad", "spöke"]],
        "ex": f'Som {B.format("gast")} på skutan skötte han storseglet.',
        "reg": "neutral, neutral, sjöfart ; neutral, neutral, allmän",
        "ety": "sjömansordet av lågtyska/nederländska gast, samma ord som gäst; "
               "spökordet av fornsvenska gaster, troligen av frisiska gast '(ond) ande' "
               "— jfr engelska ghost",
        "skal": "SO har två poster: 'besättningsman på fartyg' och 'vålnad'. SAOL: "
                "'matros; hjälpreda på segelbåt' och 'spöke'. Alla fyra synonymerna är "
                "ordböckernas egna och fördelas per betydelse. Etymologin är ovanligt "
                "värd att ha här: de två betydelserna har helt SKILDA ursprung, ordet är "
                "två ord som råkat sammanfalla.",
    },
    "handfast": {
        "hb": "som utstrålar kraft och orubblighet",
        "syn": ["stabil", "pålitlig"],
        "grp": None,
        "ex": f'Han gav ett {B.format("handfast")} intryck och tog kommandot direkt.',
        "reg": "neutral, positiv, allmän",
        "ety": None,
        "skal": "SO: 'som utstrålar kraft och orubblighet' med underbetydelsen 'som "
                "tycks mycket påtaglig' -- en nyans av samma betydelse, inte en andra. "
                "SAOL: 'stabil, pålitlig'. Kortets andra betydelse ('en viss typ av "
                "bindning eller förpliktelse') hör till `handfästning`, ett annat ord, "
                "och exempelmeningen handlade om filmen *Harald Handfaste*.",
    },
    "humaniora": {
        "hb": "humanistiska vetenskaper och läroämnen",
        "syn": [],
        "grp": None,
        "ex": f'Hon läste {B.format("humaniora")} — litteraturvetenskap och idéhistoria.',
        "reg": "neutral, neutral, allmän",
        "ety": "av latin humaniora (studia), eg. 'de mänskligare studierna'",
        "skal": "SO: 'humanistiska vetenskaper'. SAOL: 'humanistiska vetenskaper el. "
                "läroämnen'. Kortet hade samma sak i tre definitioner. Tom "
                "synonymlista: 'humanistiska ämnen' är definitionen omskriven, inte en "
                "synonym.",
    },
    "inflika": {
        "hb": "skjuta in ett ord eller en kommentar i ett samtal",
        "syn": ["skjuta in"],
        "grp": None,
        "ex": f'Hon {B.format("inflikade")} att siffran var två år gammal.',
        "reg": "neutral, neutral, allmän",
        "ety": "efter tyska einflicken",
        "skal": "SO:s hela definition är korshänvisningen `skjuta in`. SAOL: 'skjuta in "
                "ord i ett samtal'. Kortets 'kommentera' och 'lägga till' är syn.se-ord "
                "utan ordboksstöd och är strukna.",
    },
    "inkråm": {
        "hb": "inre, mjukare delen av ett bröd ; innanmäte av fågel eller fisk ; ett bolags tillgångar och skyldigheter",
        "syn": [],
        "grp": None,
        "ex": f'Köparen tog över {B.format("inkråmet")} men lämnade kvar bolagets historik.',
        "reg": "neutral, neutral, matlagning ; neutral, neutral, matlagning ; neutral, neutral, ekonomi",
        "ety": "till fornsvenska krumma, krome; av lågtyska krome 'inkråm'",
        "skal": "SO: 'inre, mjukare delar av bröd' med underbetydelserna 'innanmäte av "
                "fågel eller fisk' och 'ett bolags tillgångar och skyldigheter'. SAOL "
                "bekräftar de två första. Tom synonymlista: bara den andra betydelsen "
                "har en belagd glosa (`innanmäte`), och en platt lista hade sett ut som "
                "om den gällde alla tre. Två källor -- wiktionary saknar posten.",
    },
    "inrådan": {
        "hb": "mild uppmaning till ett visst handlande",
        "syn": ["uppmaning"],
        "grp": None,
        "ex": f'På läkarens {B.format("inrådan")} slutade han röka.',
        "reg": "formell, neutral, allmän",
        "ety": "till råda",
        "skal": "SO: '(mild) uppmaning till visst handlande' -- `uppmaning` är belagt "
                "när den inledande parentesen skalas av. SAOL har posten utan "
                "definitionstext, bara 'på min inrådan'. Kortets 'begäran' är en annan "
                "sak: en inrådan är ett råd, inte ett krav.",
    },
    "instinktiv": {
        "hb": "som styrs av instinkter snarare än av eftertanke",
        "syn": ["oreflekterad", "omedveten"],
        "grp": None,
        "ex": f'Hans {B.format("instinktiva")} reaktion var att backa ett steg.',
        "reg": "neutral, neutral, allmän",
        "ety": None,
        "skal": "SO: 'som styrs av instinkter'. SAOL: 'av inre drift, oreflekterad, "
                "omedveten' -- båda synonymerna står där ordagrant.",
    },
    "kandera": {
        "hb": "överdra med ett hölje av socker",
        "syn": [],
        "grp": None,
        "ex": f'Violerna var {B.format("kanderade")} och knastrade av socker.',
        "reg": "fackspråklig, neutral, matlagning",
        "ety": None,
        "skal": "SAOL: 'överdra med sockerglasyr'. SO: 'låta (sockerlösning eller honung) "
                "kristallisera' med underbetydelsen 'överdra med en hinna av "
                "sockerglasyr' -- samma handling sedd från två håll, alltså en betydelse. "
                "Tom synonymlista: `glasera` finns inte i någon av ordböckernas texter.",
    },
    "kontinuitet": {
        "hb": "fortlöpande sammanhang utan avbrott ; det att svara mot en sammanhängande helhet",
        "syn": [],
        "grp": None,
        "ex": f'Bytet av lärare mitt i terminen bröt {B.format("kontinuiteten")} i undervisningen.',
        "reg": "neutral, neutral, allmän ; fackspråklig, neutral, matematik",
        "ety": "av franska continuité; till latin continuus 'sammanhängande; oavbruten'",
        "skal": "SO har TVÅ betydelser: 'fortlöpande sammanhang' och 'det att vara "
                "(eller svara mot) en sammanhängande helhet', den senare märkt "
                "**'matematik'**. Kortet hade bara den första -- och dess påstådda "
                "matematikbetydelse ('en funktion som alltid har ett definierat värde') "
                "var dessutom fel definition på kontinuitet. SAOL: 'oavbrutet "
                "sammanhang'. Kortets 'fortlöpandehet' är inte ett svenskt ord. Tom "
                "synonymlista: `sammanhang` bär bara halva innebörden -- det är just det "
                "oavbrutna som ÄR kontinuitet.",
    },
    "kverulant": {
        "hb": "person som ständigt klagar och söker fel",
        "syn": [],
        "grp": None,
        "ex": f'Föreningens protokoll bar spår av en enda envis {B.format("kverulant")}.',
        "reg": "neutral, negativ, allmän",
        "ety": None,
        "skal": "SO: 'person som (ofta) kverulerar'. SAOL har posten utan "
                "definitionstext. Tom synonymlista: den enda belagda glosan innehåller "
                "uppslagsordet, och kortets 'missnöjesapostel' och 'klagofigur' finns i "
                "ingen ordbok.",
    },
    "lapsus": {
        "hb": "fel som beror på rent förbiseende",
        "syn": ["felsägning", "felskrivning"],
        "grp": None,
        "ex": f'Att kalla honom vid fel namn var en ren {B.format("lapsus")}.',
        "reg": "formell, neutral, allmän",
        "ety": "av latin lapsus 'glidande; snavande; fall'",
        "skal": "SO: 'fel som beror på rent förbiseende'. SAOL: 'fel genom förbiseende, "
                "felsägning, felskrivning' -- de två synonymerna är SAOL:s egna och "
                "preciserar dessutom vad ordet faktiskt används om.",
    },
    "mission": {
        "hb": "verksamhet för att sprida en religion ; officiellt, ofta diplomatiskt uppdrag ; större uppgift som kräver personligt engagemang",
        "syn": [],
        "grp": None,
        "ex": f'Hans {B.format("mission")} var att få alla barn i byn till skolan.',
        "reg": "neutral, neutral, religion ; formell, neutral, politik ; neutral, neutral, allmän",
        "ety": "av latin missio 'sändning; avsändande', till mittere 'sända'",
        "skal": "SO har tre betydelser: 'verksamhet för utbredning av religion', "
                "'officiellt (diplomatiskt) uppdrag' och 'större uppgift som kräver "
                "personligt engagemang'. Kortet hade bara två och saknade den "
                "diplomatiska. Tom synonymlista: bara den andra betydelsen har en belagd "
                "glosa (`uppdrag`).",
    },
    "ofelbart": {
        "hb": "helt säkert, utan undantag",
        "syn": ["säkert"],
        "grp": None,
        "ex": f'Felparkering leder {B.format("ofelbart")} till böter.',
        "reg": "neutral, neutral, allmän",
        "ety": None,
        "skal": "SAOL har adverbet: 'helt säkert', med exemplet som används här. "
                "Kortets andra betydelse -- påvens ofelbarhet -- hör till `ofelbarhet`, "
                "inte till adverbet, och kortets synonymer var adjektivformer (`osviklig`, "
                "`felfri`) som inte kan bytas mot ett adverb.",
    },
    "ontologi": {
        "hb": "läran om vad som finns och hur verkligheten är beskaffad",
        "syn": [],
        "grp": None,
        "ex": f'Frågan om tal existerar oberoende av oss är {B.format("ontologi")}, inte matematik.',
        "reg": "fackspråklig, neutral, filosofi",
        "ety": "till grekiska on (genitiv ontos) '(det) varande' och logos '(en) lära'",
        "skal": "SO: 'läran om de begrepp och kategorier man behöver för att beskriva "
                "och förklara verkligheten'. SAOL: 'vetenskapen om det varandes väsen'. "
                "SAOL:s andra betydelse -- 'hierarkisk klassificering av världen' -- är "
                "IT-användningen och saknas i SO; den tas inte in. Kortets tredje "
                "betydelse blandade ihop ontologi med det ontologiska gudsbeviset.",
    },
    "paletå": {
        "hb": "rak eller svagt insvängd herröverrock utan skärp",
        "syn": [],
        "grp": None,
        "ex": f'Han hängde av sig {B.format("paletån")} i tamburen.',
        "reg": "neutral, neutral, allmän",
        "ety": "av franska paletot 'ytterrock'; av äldre engelska paltok 'kort rock'",
        "skal": "SO: 'typ av rak eller svagt insvängd herröverrock utan skärp'. "
                "**Registret är medvetet neutralt.** SAOL skriver 'en äldre typ av "
                "överrock', men det beskriver PLAGGET, inte ordets bruklighet -- att "
                "läsa det som en ålderdomsmarkering är exakt den registermiss som fällt "
                "kort tidigare i veckan. Två källor.",
    },
    "pompös": {
        "hb": "som präglas av upphöjd prakt ; högtravande och uppblåst",
        "syn": ["ståtlig", "praktfull", "högtravande", "uppblåst"],
        "grp": [["ståtlig", "praktfull"], ["högtravande", "uppblåst"]],
        "ex": f'Talet var {B.format("pompöst")} och sade till slut ingenting.',
        "reg": "neutral, neutral, allmän ; neutral, negativ, allmän",
        "ety": "av franska pompeux; till pomp",
        "skal": "SO: 'som präglas av upphöjd prakt' med underbetydelsen 'högtravande, "
                "uppblåst'. SAOL delar upp det likadant: 'ståtlig, praktfull; "
                "högtravande, uppblåst' -- semikolonet i SAOL markerar just gränsen "
                "mellan de två betydelserna, så grupperingen följer källan direkt. "
                "Valören skiljer sig mellan dem, vilket är hela poängen med ordet.",
    },
    "potpurri": {
        "hb": "doftblandning av torkade blad i en kruka ; musikstycke hopfogat av flera kända melodier ; brokig blandning av lite av varje",
        "syn": [],
        "grp": None,
        "ex": f'Konserten avslutades med ett {B.format("potpurri")} ur tre operetter.',
        "reg": "neutral, neutral, allmän ; neutral, neutral, musik ; neutral, neutral, allmän",
        "ety": "av franska pot-pourri, ursprungligen 'maträtt av allehanda ingredienser', "
               "till pot 'kruka' och pourri 'rutten'",
        "skal": "SO har musikbetydelsen FÖRST och doftblandningen som andra; SAOL har "
                "'blandning, lite av varje' samt musikstycket. Kortet hade bara doft- "
                "och den allmänna betydelsen och saknade musikbetydelsen, som är den "
                "ordböckerna sätter först. Tom synonymlista: `blandning` täcker bara den "
                "tredje betydelsen.",
    },
    "påtaglig": {
        "hb": "tydligt märkbar",
        "syn": ["tydlig", "uppenbar"],
        "grp": None,
        "ex": f'Det fanns en {B.format("påtaglig")} spänning i rummet redan innan mötet började.',
        "reg": "neutral, neutral, allmän",
        "ety": None,
        "skal": "SO: 'tydligt märkbar' (ordagrant OLD-facit). SAOL: 'tydlig, uppenbar; "
                "åskådlig; förnimbar' -- båda synonymerna är SAOL:s egna.",
    },
    "raspig": {
        "hb": "som ger ifrån sig ett lätt skrapande ljud",
        "syn": [],
        "grp": None,
        "ex": f'Rösten var {B.format("raspig")} efter en hel dag i telefon.',
        "reg": "neutral, neutral, allmän",
        "ety": None,
        "skal": "SO: 'som ger ifrån sig ett lätt skrapande ljud'. SAOL har posten utan "
                "definitionstext. Tom synonymlista: kortets 'skrovlig', 'hes' och 'grov' "
                "kommer från syn.se -- och `skrovlig` är dessutom fel dimension, ordet "
                "handlar om LJUD, inte om yta.",
    },
    "rännil": {
        "hb": "liten ström av vätska",
        "syn": [],
        "grp": None,
        "ex": f'En {B.format("rännil")} av smält snö sökte sig ner för backen.',
        "reg": "neutral, neutral, allmän",
        "ety": "fornsvenska rännil; till ränna i den äldre betydelsen 'rinna'",
        "skal": "SO: 'liten ström av vätska'. SAOL: 'litet vattenflöde'. Tom "
                "synonymlista: kortets 'kanal' och 'dike' är ANLÄGGNINGAR -- en rännil är "
                "vätskan själv, inte fåran den går i. Kortets andra och tredje betydelse "
                "beskrev just fåror och är borttagna.",
    },
    "sakteliga": {
        "hb": "långsamt och gradvis",
        "syn": ["långsamt", "efter hand"],
        "grp": None,
        "ex": f'Isen släppte {B.format("sakteliga")} sitt grepp om sjön.',
        "reg": "neutral, neutral, allmän",
        "ety": "fornsvenska saktelika",
        "skal": "SO: 'med låg fart'. SAOL: 'långsamt, efter hand' -- båda synonymerna "
                "står ordagrant där.",
    },
    "stagnera": {
        "hb": "gradvis upphöra att utvecklas i positiv riktning",
        "syn": ["avstanna"],
        "grp": None,
        "ex": f'Försäljningen {B.format("stagnerade")} efter tre år av stadig tillväxt.',
        "reg": "neutral, negativ, allmän",
        "ety": "av latin stagnare 'stå stilla', till stagnum 'stillastående vatten'",
        "skal": "SO: 'gradvis upphöra att utvecklas i positiv riktning'. SAOL: "
                "'avstanna i utveckling'. Kortets 'förslappas' finns i ingen ordbok.",
    },
    "streber": {
        "hb": "person som är helt inriktad på att göra karriär",
        "syn": ["karriärist", "uppåtsträvare"],
        "grp": None,
        "ex": f'Han fick snabbt rykte om sig att vara en {B.format("streber")} som tog åt sig äran för andras arbete.',
        "reg": "neutral, nedsättande, allmän",
        "ety": "av tyska Streber, till streben 'sträva'",
        "skal": "SO: 'person som är helt inriktad på att arbeta hårt och göra karriär'. "
                "SAOL: 'uppåtsträvare, karriärist' -- båda synonymerna är SAOL:s egna. "
                "Valören är **nedsättande**, inte bara negativ: SO märker ordet "
                "'nedsättande' och SAOL 'nedsätt.'. Jag satte först 'negativ' på egen "
                "bedömning; förgranskningen fångade det mot märkningen.",
    },
    "säteri": {
        "hb": "huvudgård i ett frälsegods",
        "syn": ["sätesgård", "herrgård"],
        "grp": None,
        "ex": f'Familjen ägde ett {B.format("säteri")} med allé och två flyglar.',
        "reg": "neutral, neutral, historia",
        "ety": "bildning till det äldre sätesgård",
        "skal": "SO: 'huvudgård i frälsegods', med `sätesgård` taggat SYN:synonym -- "
                "starkaste beläggningsformen. SAOL: 'sätesgård; herrgård'. Kortets "
                "'lantgård' är fel: ett säteri definieras av skattefriheten, inte av "
                "storleken.",
    },
    "tariff": {
        "hb": "förteckning över gällande priser och avgifter",
        "syn": ["taxa"],
        "grp": None,
        "ex": f'Elbolaget höjde sin {B.format("tariff")} vid årsskiftet.',
        "reg": "formell, neutral, ekonomi",
        "ety": "via italienska av arabiska tarîf 'kungörande; taxa'",
        "skal": "SO: 'förteckning över gällande priser och avgifter'. SAOL: 'lista över "
                "satser för avgifter el. varupriser, taxa'. Kortets andra betydelse "
                "('en avgift eller betalning') är fel riktning -- tariffen är LISTAN, "
                "inte den enskilda avgiften.",
    },
    "tilde": {
        "hb": "tecknet ~",
        "syn": [],
        "grp": None,
        "ex": f'Spanskans {B.format("tilde")} är det som skiljer n från ñ.',
        "reg": "fackspråklig, neutral, lingvistik",
        "ety": "av spanska tilde; av latin titulus 'inskrift; överskrift'",
        "skal": "SO och SAOL säger båda bara 'tecknet ~'. Kortets två definitioner var "
                "vaga omskrivningar av samma sak. Tom synonymlista -- ett tecken har "
                "inget utbytbart ord. Två källor.",
    },
    "tillstymmelse": {
        "hb": "svag ansats till att något finns",
        "syn": ["ansats", "tecken"],
        "grp": None,
        "ex": f'Det fanns inte en {B.format("tillstymmelse")} till bevis i utredningen.',
        "reg": "neutral, neutral, allmän",
        "ety": "troligen sammanhängande med dialektalt stumn 'trädstubbe'",
        "skal": "SO: '(svag) ansats till förekomst' -- `ansats` är belagt när parentesen "
                "skalas av. SAOL: 'ansats, tecken till ngt'. Kortets 'insinuation' och "
                "'allusion' betyder något helt annat (antydan om NÅGOT, inte spår AV "
                "något) och är strukna.",
    },
    "verbalisera": {
        "hb": "uttrycka i ord",
        "syn": ["uttrycka"],
        "grp": None,
        "ex": f'Han hade svårt att {B.format("verbalisera")} vad som gjorde honom orolig.',
        "reg": "formell, neutral, allmän",
        "ety": "efter engelska verbalize",
        "skal": "SO och SAOL säger båda ordagrant 'uttrycka i ord'. Två källor -- "
                "wiktionary saknar posten.",
    },
}


def main():
    data = json.load(open(SESSION, encoding="utf-8"))
    poster = data["poster"] if isinstance(data, dict) else data

    kvar = [p for p in poster if p["ord"] not in PAUSAS]
    pausade = [p["ord"] for p in poster if p["ord"] in PAUSAS]

    saknar = [p["ord"] for p in kvar if p["ord"] not in KORT]
    if saknar:
        sys.exit(f"saknar rättelse för: {', '.join(saknar)}")

    for p in kvar:
        o = p["ord"]
        r = KORT[o]
        p["proposed"] = {
            "huvudbetydelse": r["hb"][0].upper() + r["hb"][1:],
            "synonymer": r["syn"],
            "synonym_groups": r.get("grp"),
            "exempelmening": r["ex"],
            "register": r["reg"],
            "etymologi": r.get("ety"),
        }
        p["approved"] = True
        if o in TILLAT:
            p["forgranska_tillat"] = TILLAT[o]
        p["sokkoll"] = {
            "kalla": SVENSKA.format(urllib.parse.quote(K.get(o, o))),
            "slutsats": r["skal"],
        }
        p.pop("applicerad", None)

    if isinstance(data, dict):
        data["poster"] = kvar
        ut = data
    else:
        ut = kvar
    json.dump(ut, open(SESSION, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    tomma = sum(1 for p in kvar if not p["proposed"]["synonymer"])
    grupperade = sum(1 for p in kvar if p["proposed"]["synonym_groups"])
    flerbet = sum(1 for p in kvar if ";" in p["proposed"]["huvudbetydelse"])
    print(f"fyllde {len(kvar)} poster -- {tomma} med tom synonymlista, "
          f"{grupperade} med grupperade synonymer av {flerbet} flerbetydelsekort.")
    if pausade:
        print(f"UTESLUTNA (pausas separat): {', '.join(pausade)}")


if __name__ == "__main__":
    main()
