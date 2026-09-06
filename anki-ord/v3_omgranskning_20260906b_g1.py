# -*- coding: utf-8 -*-
"""Sats 2 (is:review efter lapses), ord 1-20.

Synonymerna ar denna gang hamtade UR RASTRUKTUREN (visa_uppslag.py) -- SO:s
SYN-taggar och SO/SAOL:s definitionstext -- aldrig ur synonymer.se. Dar
ordboken inte namnger nagon synonym star `≈≈ kategori` ur kortets egen
definition. Domanerna ar kontrollerade mot config.REGISTER_DOMAN.
Exempelmeningarna ar fullstandiga satser med finit verb (blindgranskaren
underkande avpassa i sats 1 for ett oomskrivet ordboksfragment).

Sokkoll: python slaupp.py --fil rep40b_ord.json --antal 40 --tyst, kord i
sessionens eget transkript.
"""
import io, json, urllib.parse

FIL = "sessions/session_2026-09-06_v3-omgranskning2.json"
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"gärdsmyg": dict(
  hb="Mycket liten brunspräcklig tätting med kort, uppåtstående stjärt och en snabb, forcerad sång",
  reg="neutral, neutral, biologi",
  grp=[["≈≈ småfågel"]],
  ex='En <font color="#3498db">gärdsmyg</font> hoppade omkring i snåret och letade efter insekter.',
  etym="till gärde och smyga",
  sl="SO: 'en liten brunspracklig tatting med kort uppatstaende stjart', med parentesen 'och en "
     "snabb, forcerad sang med klara toner blandade med surrande drillar'. Legacy sa 'En mycket "
     "liten brunspracklig fagel' -- 'fagel' ar bredare an SO:s TATTING, och sangen saknades helt. "
     "Bada tillagda: gardsmygen ar beromd for att vara en av Sveriges minsta faglar med en av dess "
     "kraftigaste sanger, och den kontrasten ar sjalva minneskroken. SAOL sager bara 'en fagel' och "
     "ger ingen synonym; kategori '≈≈ smafagel' lag redan pa kortet och ar satt ur definitionen "
     "(ingen kalla kravs for ≈≈). Register och doman oforandrade. Exempelmening oforandrad. "
     "Etymologin ('till garde och smyga') forklarar namnet: fageln smyger i snar och "
     "gardsgardar."),

"kollekt": dict(
  hb="Insamling av pengar för välgörenhet vid en gudstjänst, och pengarna som samlas in",
  reg="neutral, neutral, religion",
  grp=[["insamling"]],
  ex='Församlingen tog upp <font color="#3498db">kollekt</font> till de nödställda efter '
     'jordbävningen.',
  etym="av latin collecta 'samlande; samling', till colligere 'samla' -- samma rot som i kollektion",
  sl="SO: 'insamling for valgorande andamal vid gudstjanst', med EN underbetydelse markt '(ingen "
     "egen definition -- utvidgning)' i rastrukturen. Legacy delade upp kortet i TVA betydelser "
     "('Insamling av pengar under en gudstjanst ; pengarna som samlats in'). Enligt projektets "
     "regel ar en utvidgning utan egen definitionstext ingen egen betydelse, sa de tva ar slagna "
     "ihop till en rad dar bada anvandningarna namns ('och pengarna som samlas in'). "
     "'insamling' star ordagrant i SAOL:s led ('insamling av pengar t.ex. vid gudstjanst') och i "
     "SO:s egen definition -- belagd. RISKFLAGGA old_delar_inget_ordforrad utredd: OLD sager "
     "'pengainsamling i kyrkan', kortet 'insamling av pengar ... gudstjanst' -- samma sak, olika "
     "sammansattning; flaggan ar falsk har. Register oforandrat. Exempelmening skarpt till en "
     "fullstandig sats med konkret mottagare. Etymologi ny, ur SO -- colligere 'samla' binder ihop "
     "ordet med kollektion och kollektiv."),

"dyrk": dict(
  hb="Enkelt nyckelliknande verktyg som öppnar ett lås på annat sätt än nyckeln, ofta vid inbrott",
  reg="neutral, neutral",
  grp=[["≈≈ låsverktyg"]],
  ex='Tjuvarna hade använt en <font color="#3498db">dyrk</font> för att ta sig in i lägenheten.',
  etym="av lågtyska dirk med samma betydelse; identiskt med mansnamnet Didrik",
  sl="SO: 'ett enkelt, nyckelliknande verktyg for oppning av las pa annat satt an det normala', "
     "med parentesen 'ofta vid inbrott'. SAOL: 'ett redskap att oppna manga olika las med'. "
     "Legacys 'Verktyg for att olovligen oppna las' hade tva brister: NYCKELLIKNANDE saknades (det "
     "ar det som skiljer en dyrk fran en kofot), och 'olovligen' ar snavare an SO, som sager 'pa "
     "annat satt an det normala' och lagger inbrottet i en parentes -- en lassmed dyrkar ocksa. "
     "Rattat. SYNONYM BORTTAGEN: 'tjuvnyckel' finns inte i vare sig SO eller SAOL; ersatt med "
     "kategori '≈≈ lasverktyg' ur kortets egen definition. RISKFLAGGA old_delar_inget_ordforrad "
     "utredd: OLD sager 'lasverktyg', vilket ar exakt kategorin -- flaggan slog till pa legacys "
     "'tjuvnyckel'. REGISTER ANDRAT: 'vardaglig' saknar stod -- varken SO eller SAOL markerar "
     "ordet. Exempelmening oforandrad. Etymologi ny, ur SO -- att dyrken bar samma namn som "
     "Didrik ar bisarrt nog och darfor latt att minnas."),

"avlatsbrev": dict(
  hb="Dokument från kyrkan i äldre tid som intygade att ett straff för synder var efterskänkt",
  reg="neutral, neutral, historia",
  grp=[["≈≈ kyrkligt intyg"]],
  ex='Den medeltida kyrkan sålde <font color="#3498db">avlatsbrev</font> för stora summor.',
  etym="fornsvenska aflats bref",
  sl="SO: 'dokument som utgor bevis pa erhallen avlat'. SAOL markerar 'i aldre tid'. Legacys "
     "'Dokument som bevisade kopt AVLAT' bryter mot regeln att forklaringen ska ligga en niva "
     "under uppslagsordet: 'avlat' ar uppslagsordets eget forled, alltsa ordet i sin egen "
     "definition, och den som inte vet vad avlat ar far ingen hjalp alls. Utskrivet till vad "
     "avlaten faktiskt var -- ett efterskankt straff for synder. Aven SAOL:s tidsmarkning "
     "('i aldre tid') ar nu med i definitionen. SYNONYM BORTTAGEN: legacys 'intyg' star inte i "
     "nagon ordbok som synonym och ar dessutom for brett (ett intyg kan vara vad som helst); "
     "ersatt med kategori '≈≈ kyrkligt intyg' ur kortets egen definition. REGISTER ANDRAT: "
     "'formell' saknar stod; doman historia tillagd, vilket SAOL:s 'i aldre tid' motiverar. "
     "Exempelmening skarpt ('Medeltida kyrkan salde' -> 'Den medeltida kyrkan salde ... for stora "
     "summor') -- den gamla saknade bestamd artikel och lat som en rubrik."),

"dåd": dict(
  hb="Konkret handling som skadar någon och förtjänar klander",
  reg="neutral, negativ",
  grp=[["klandervärd gärning"]],
  ex='Ingen visste vem som låg bakom <font color="#3498db">dådet</font>.',
  etym="runform taiþir, fornsvenska dadh; gemensamt germanskt ord",
  sl="BETYDELSEN VAR OMVAND. Legacy: 'Bragd, stor bedrift', register 'arkaisk, neutral', "
     "synonymer 'stordad' och 'bravad' -- alltsa genomgaende POSITIVT. SO sager 'konkret, SKADLIG "
     "handling'. SAOL sager 'KLANDERVARD garning'. Bada ordbockerna ar alltsa negativa, och "
     "kortet var positivt: en rakt motsatt betydelse, inte en nyansskillnad. Modernt sprakbruk "
     "bekraftar det utan tvekan -- terrordad, illdad, mordet beskrivs som ett dad, aldrig en "
     "hjaltegarning. (Ordet HAR en alderdomlig positiv anvandning i 'bragder och dad', men den ar "
     "inte den SO och SAOL beskriver, och att lara in den som huvudbetydelse pa ett HP-kort ar "
     "direkt skadligt: 'dad' i ett provsvar ar negativt laddat.) Helt omskrivet. "
     "'klandervard garning' ar SAOL:s hela definition (belagd). Register andrat fran 'arkaisk, "
     "neutral' till 'neutral, negativ' -- ordet ar varken ur bruk eller neutralt. "
     "EXEMPELMENING BYTT: 'Hans dad under kriget blev beromt langt senare' lar in precis det fel "
     "som rattas har. RISKFLAGGA old_saknas: kortet har inget OLD-facit alls, sa den kontrollen "
     "kunde inte fanga felet -- det ar SO och SAOL som gor det."),

"likare": dict(
  hb="Mått som är fastställt som det riktiga och som andra mått jämförs med ; person eller sak som "
     "andra rättar sig efter",
  reg="fackspråklig, neutral, teknik ; neutral, positiv",
  grp=[["normalmått"], ["förebild"]],
  ex='Kilogramprototypen i Paris var länge <font color="#3498db">likare</font> för all vägning i '
     'världen.',
  etym="till äldre lika 'jämka; justera'",
  sl="Rastrukturen: SO-LEMMA likare har EN definition ('normalmatt som andra matt jamfors med', "
     "med tillagget 'och justeras efter') och EN underbetydelse med egen text ('erkand forebild "
     "eller auktoritet') -- alltsa TVA betydelser. Legacy hade TRE: den tredje, 'Mattstock i "
     "sammansattningar', finns inte i vare sig SO eller SAOL och ar dessutom ingen betydelse utan "
     "en anmarkning om ordbildning. Struken. 'normalmatt' star ordagrant i bade SO:s och SAOL:s "
     "definition (belagd) och 'forebild' ordagrant i SO:s underbetydelse (belagd); bada ar "
     "flyttade UT ur huvudbetydelsen sa att de inte forklarar sig sjalva -- definitionen sager nu "
     "'matt som ar faststallt som det riktiga' respektive 'person eller sak som andra rattar sig "
     "efter'. Legacys kategorier '≈≈ forebild' och '≈≈ mattstock' behovs darmed inte: den forsta "
     "var en belagd synonym som markts som kategori i onodan. REGISTER: betydelse 2:s 'formell' "
     "saknar stod och ar bytt mot neutral; laddningen ar positiv (SO sager ERKAND forebild). "
     "EXEMPELMENING BYTT till kilogramprototypen -- den ar den likare de flesta har hort talas om "
     "och binder ihop bada betydelserna."),

"simpa": dict(
  hb="Brokigt färgad bottenlevande rovfisk med brett, platt huvud, taggiga gällock och stora "
     "bröstfenor",
  reg="neutral, neutral, biologi",
  grp=[["≈≈ bottenfisk"]],
  ex='Han drog upp en <font color="#3498db">simpa</font> som spärrade upp sin väldiga mun.',
  etym="fornsvenska simpa; av ovisst ursprung",
  sl="SO: 'typ av brokigt fargad, bottenlevande rovfisk med brett, platt huvud, taggiga gallock "
     "och stora brostfenor', med parentesen 'forekommande i bade salt och sott vatten'. Legacy "
     "hade fyra av de fem sardragen men tappade BROKIGT FARGAD -- det forsta ordet i SO:s "
     "definition och det man ser forst pa fisken. Tillagt. SAOL sager bara 'en fisk' och ger ingen "
     "synonym; kategori '≈≈ bottenfisk' lag redan pa kortet och ar satt ur definitionen. "
     "RISKFLAGGA old_delar_inget_ordforrad utredd: OLD sager 'taggfenig fisk', kortet "
     "'taggiga gallock' -- OLD har blandat ihop gallock med fenor, men det ar OLD som ar oprecist, "
     "inte kortet; SO ar entydig. Flaggan avfardad. Register och doman oforandrade. "
     "EXEMPELMENING BYTT: den gamla ('Han fick upp en simpa med taggiga gallock') upprepade "
     "definitionen ordagrant i stallet for att visa ordet i bruk. Den nya visar den stora munnen, "
     "som foljer av SO:s 'brett, platt huvud'. Etymologin oforandrad, matchar SO."),

"boken": dict(
  hb="Mer än övermogen och nästan skämd, om frukt",
  reg="ngt ålderdomlig, neutral",
  grp=[["halvskämd"]],
  ex='De sista päronen i skålen hade blivit alldeles <font color="#3498db">bokna</font> och '
     'smakade sött men mjäkigt.',
  etym="fornsvenska bokin; svensk dialekt boken 'skämd; skrumpen'; troligen besläktat med baka",
  sl="SO: 'mer an overmogen' <<om frukt>>, med brukligheskommentaren 'nagot alderdomligt'. SAOL: "
     "'halvskamd'. Legacys definition ('Overmogen och nastan skamd, om frukt') var ratt i sak; "
     "SO:s 'MER AN overmogen' ar dock starkare an bara 'overmogen' och ar nu utskrivet. "
     "REGISTER ANDRAT: legacy hade 'dialektal', vilket saknar stod -- SO markerar uttryckligen "
     "'nagot alderdomligt', inte dialektalt, och det ar skillnad: ett dialektord hor till en "
     "plats, ett alderdomligt ord till en tid. (Etymologins 'svensk dialekt boken' galler ordets "
     "URSPRUNG, inte dess nuvarande bruklighet -- sannolikt darifran legacys fel kom.) "
     "'halvskamd' ar SAOL:s hela definition (belagd). SYNONYMER BORTTAGNA: legacys 'overmogen' "
     "stod ordagrant i definitionen (upprepning, inte synonym) och 'mosig' finns inte i nagon "
     "kalla. RISKFLAGGA dold_betydelse utredd: de fyra doljda lemmana ar 'bok' i sina olika "
     "betydelser (skrift, trad, e-bok) -- ett annat ord som rakar sammanfalla i bestamd form, "
     "inte en dold betydelse hos adjektivet boken. Exempelmening oforandrad -- den visar den "
     "bestamda formen 'bokna', som ar den man faktiskt motter."),

"snärj": dict(
  hb="Stress och alldeles för mycket att göra ; snår av hopvuxna grenar",
  reg="vardaglig, lätt negativ ; neutral, neutral",
  grp=[["jäkt", "sjå"], ["snår"]],
  ex='Som ensamstående trebarnsmamma hade hon ett rejält <font color="#3498db">snärj</font>.',
  etym="till snärja; fornsvenska snäria, nära besläktat med snar, snara och snår",
  sl="SAKNAD BETYDELSE. SO ger 'jakt' (vardagligt). SAOL ger TVA semikolonseparerade led: 'snar' "
     "och 'jakt, sja' (vard.). Legacy hade bara jaktbetydelsen. Snarbetydelsen ar inte en "
     "utvidgning utan SAOL:s forsta led och hanger ihop med etymologin (snarja, snara, snar) -- "
     "det ar den konkreta bilden som jaktbetydelsen ar en overford anvandning av. Tillagd. "
     "'jakt' och 'sja' star bada ordagrant i SAOL:s led (belagda), 'snar' likasa. "
     "CIRKULARITET UNDVIKEN: legacy sa 'Stress och JAKT i vardagen' och hade samtidigt 'jakt' som "
     "synonym; definitionen sager nu 'alldeles for mycket att gora' och lamnar jakt at "
     "synonymraden. SYNONYM BORTTAGEN: legacys 'stress' star kvar i definitionen och ar darmed "
     "ingen synonym. REGISTER: 'vardaglig' tillagt for betydelse 1 -- bade SO och SAOL markerar "
     "den; snarbetydelsen ar omarkerad och blir neutral. Exempelmening oforandrad. Etymologi ny, "
     "ur SO -- slaktskapen med snara och snar forklarar bada betydelserna pa en gang."),

"förlägenhet": dict(
  hb="Obehaglig känsla av att skämmas inför andra ; en brydsam situation, till exempel brist på "
     "pengar",
  reg="neutral, neutral ; neutral, neutral",
  grp=[["≈≈ blygsel"], ["brydsam situation"]],
  ex='Hon rodnade av <font color="#3498db">förlägenhet</font> när hon snubblade på scenen.',
  etym=None,
  sl="Rastrukturen: SO-LEMMA forlagenhet har EN definition ('det att vara forlagen') och EN "
     "underbetydelse med egen text ('brydsam situation') -- tva betydelser, vilket ar vad kortet "
     "har. SO:s egen definition ar dock cirkular pa ordbokssatt ('det att vara forlagen'), sa den "
     "gar inte att overta; utskriven till vad kanslan ar. SYNONYMER RATTADE, och det var det "
     "storsta felet: legacy hade 'generad, skamsen, knipa, trangmal' i EN oindelad lista. De tva "
     "forsta ar ADJEKTIV medan uppslagsordet ar ett SUBSTANTIV -- 'hon rodnade av generad' gar "
     "inte att saga, sa de var inte utbytbara alls. Ersatta med kategorin '≈≈ blygsel' for "
     "betydelse 1. 'brydsam situation' ar SO:s egen underbetydelsetext (belagd) och star nu ensam "
     "i grupp 2; 'knipa' och 'trangmal' finns inte i vare sig SO eller SAOL. REGISTER ANDRAT: "
     "'vardaglig' saknar stod och tackte dessutom bada betydelserna -- nu en rad per betydelse, "
     "bada neutrala. Exempelmening oforandrad. ETYMOLOGI UTELAMNAD: SO:s post saknar historiska "
     "uppgifter."),

"kurra": dict(
  hb="Låst rum där någon hålls fången en kortare tid ; ge ifrån sig ett ljust, dämpat bullrande "
     "ljud, som magen gör när man är hungrig",
  reg="vardaglig, neutral ; neutral, neutral",
  grp=[["arrest", "finka"], ["bullra"]],
  ex='Efter slagsmålet fick han sitta natten i <font color="#3498db">kurran</font>.',
  etym="substantivet av omdiskuterat ursprung, kanske svensk dialekt kurra 'koja'; verbet är "
       "ljudhärmande",
  sl="Rastrukturen visar TVA SO-lemman: kurra (substantiv) 'arrest' [vardagligt] och kurra (verb) "
     "'ge ifran sig ett ganska ljust, dampat bullrande ljud'. Legacy hade bada -- ratt. "
     "CIRKULARITET RATTAD: legacy sa 'Vardagligt ord for ARREST eller fangelse' och hade samtidigt "
     "'arrest' som forsta synonym. Definitionen beskriver nu saken ('last rum dar nagon halls "
     "fangen en kortare tid') och 'arrest' ligger dar den hor hemma. Dessutom stod "
     "brukligheskommentaren INNE i definitionen ('Vardagligt ord for ...') -- den hor till "
     "registerfaltet, inte till betydelsen. 'arrest' och 'finka' star bada ordagrant i SAOL:s led "
     "(belagda), 'bullra' i SAOL:s 'bullra i magen' (belagd). SYNONYMER BORTTAGNA: 'hakte' och "
     "'mullra' finns inte i nagon kalla. REGISTER ANDRAT: legacy hade 'slang' for betydelse 1, men "
     "BADE SO och SAOL sager 'vardagligt' respektive 'vard.' -- slang ar ett steg under vardaglig "
     "(config.REGISTER_FORMALITY) och har inget stod. Verbet ar omarkerat i bada ordbockerna och "
     "blir neutralt. Exempelmening oforandrad. Etymologi ny, ur SO, som ger tva skilda ursprung "
     "for de tva orden."),

"obeständig": dict(
  hb="Som förändras och försämras när den utsätts för påverkan",
  reg="neutral, lätt negativ",
  grp=[["≈≈ förgänglig"]],
  ex='Skulpturerna var av gips och andra <font color="#3498db">obeständiga</font> material.',
  etym=None,
  sl="SO: 'som i vissa (vasentliga) avseenden forandras (och forsamras) vid paverkan' -- EN "
     "betydelse. Legacys 'Som forandras och bryts ner nar den utsatts for paverkan' var nara, men "
     "'bryts ner' ar snavare an SO:s 'forsamras': ett obestandigt material behover inte brytas ner "
     "utan kan lika garna blekna, spricka eller andra form. Rattat till SO:s eget ord. "
     "RISKFLAGGA old_delar_inget_ordforrad utredd: OLD sager 'flyktig', vilket ar en ANNAN "
     "betydelse an SO:s -- flyktig handlar om att forsvinna, obestandig om att forandras vid "
     "paverkan. SO och SAOL ger inget stod for flyktighetsbetydelsen, sa den har inte tagits in; "
     "OLD ar projektets svagare kalla och far inte ensam lagga till en betydelse. Kategorin "
     "'≈≈ forganglig' lag redan pa kortet och ar satt ur definitionen (ingen kalla kravs). "
     "REGISTER ANDRAT: 'formell' saknar stod -- SO ger ingen brukligheskommentar; laddningen "
     "mildrad fran negativ till latt negativ (obestandig ar en saklig materialegenskap, inte ett "
     "klander). Exempelmening oforandrad. ETYMOLOGI UTELAMNAD: SO:s post saknar historiska "
     "uppgifter."),

"pondus": dict(
  hb="Naturlig förmåga att inge respekt ; kraft och allvar i det man säger",
  reg="neutral, positiv ; neutral, neutral",
  grp=[["värdighet"], ["eftertryck", "tyngd"]],
  ex='Rektorn var en man med <font color="#3498db">pondus</font>.',
  etym="av latin pondus 'vikt; tyngd' -- samma rot som i pund och pensum",
  sl="Rastrukturen: SO-LEMMA pondus har EN definition ('naturlig formaga att inge respekt') och EN "
     "underbetydelse med egen text ('tyngd, eftertryck') -- tva betydelser, vilket ar vad kortet "
     "har. SPRAK: legacys forsta betydelse ('Naturlig TYNGD som gor att andra lyssnar') anvande "
     "ordet 'tyngd', som ar betydelse 2:s synonym -- de tva betydelserna gled darmed ihop. "
     "Betydelse 1 foljer nu SO ordagrant ('inge respekt') och 'tyngd' finns bara kvar i grupp 2. "
     "'vardighet' och 'eftertryck' star bada ordagrant i SAOL:s led ('vardighet, eftertryck'), "
     "'tyngd' i SO:s underbetydelse -- alla tre belagda. Legacys andra betydelse sa 'EFTERTRYCK i "
     "det man sager' och hade 'eftertryck' som synonym; definitionen sager nu 'kraft och allvar' i "
     "stallet. REGISTER ANDRAT: 'formell' saknar stod for bada betydelserna -- varken SO eller "
     "SAOL markerar ordet. Exempelmening oforandrad -- kort, konkret och visar den vanligaste "
     "betydelsen. Etymologi ny, ur SO: 'vikt; tyngd' forklarar bada betydelserna, och kopplingen "
     "till pund gor det latt att minnas."),

"inrättning": dict(
  hb="Organisation som i egna lokaler utför en viss sorts tjänster åt allmänheten ; föremål eller "
     "detalj med en viss funktion, ofta ett vars inre man inte känner till",
  reg="neutral, neutral ; neutral, neutral",
  grp=[["≈≈ institution"], ["≈≈ anordning"]],
  ex='Kommunen byggde en ny <font color="#3498db">inrättning</font> för äldreomsorg.',
  etym=None,
  sl="Rastrukturen: SO-LEMMA inrattning har TVA definitioner -- '(del av) organisation som (i "
     "fasta lokaler) utfor viss typ av tjanster at allmanheten' (med tillagget 'mest om "
     "samhalleliga organisationer') och 'foremal eller detalj med viss funktion' (med tillagget "
     "'sarsk. om foremal vars inre funktionssatt ar okant el. ointressant'). Legacy hade bada, men "
     "bada var avskalade: 'Organisation eller institution som utfor tjanster' tappade LOKALERNA "
     "och ALLMANHETEN, och 'anordning eller konstruktion for ett visst andamal' tappade SO:s "
     "roligaste och mest anvandbara precisering -- att en inrattning ofta ar just en manick vars "
     "innanmate man inte begriper. Bada tillaggen infogade. SYNONYMER NEDGRADERADE: legacy hade "
     "fyra omarkerade synonymer (institution, anstalt, anordning, konstruktion) i en oindelad "
     "lista. Ingen av dem star i SO:s eller SAOL:s definitionstext, och 'anstalt' ar dessutom "
     "missvisande smalt i modern svenska (fangelse). Ersatta med en kategori per betydelse, satta "
     "ur kortets egen definition. REGISTER ANDRAT: 'formell' saknar stod och tackte tva "
     "betydelser -- nu en rad per betydelse. Exempelmening oforandrad. ETYMOLOGI UTELAMNAD: SO:s "
     "post saknar historiska uppgifter."),

"maka": dict(
  hb="Kvinnlig part i ett äktenskap ; som är lika eller hör samman och bildar ett par ; skjuta "
     "något ett litet stycke åt sidan",
  reg="formell, neutral ; ngt ålderdomlig, neutral ; neutral, neutral",
  grp=[["hustru"], ["≈≈ sammanhörande"], ["flytta", "jämka"]],
  ex='Kan du <font color="#3498db">maka</font> dig lite åt vänster så att alla får plats?',
  etym="adjektivet till fornsvenska maki 'like; kamrat'; verbet av lågtyska maken 'göra, "
       "åstadkomma'",
  sl="Rastrukturen visar TRE SO-lemman: maka (adjektiv) 'som ar lika eller hor samman' [mindre "
     "brukligt utom i vissa uttryck], maka (substantiv) 'kvinnlig part i aktenskap' [nagot "
     "formellt] och maka (verb) 'forskjuta ett litet stycke i sidled'. Legacy hade alla tre -- "
     "ratt. ORDNING ANDRAD: hustrubetydelsen star nu forst, eftersom den ar den enda de flesta "
     "motter. REGISTER RATTAT, och det var huvudfelet: legacy hade EN rad, 'vardaglig, neutral', "
     "for alla tre. SO markerar substantivet 'nagot formellt' -- alltsa raka MOTSATSEN till "
     "vardagligt (man sager 'min fru' i talsprak, 'min maka' i en dodsannons). Adjektivet ar "
     "markt 'mindre brukligt utom i vissa uttryck', vilket narmast motsvarar 'ngt alderdomlig' i "
     "config.REGISTER_FORMALITY; verbet ar omarkerat och neutralt. Nu tre rader. 'hustru' star "
     "ordagrant i SAOL:s led (belagd), 'flytta' och 'jamka' likasa ('flytta, jamka'). Legacys "
     "'matchande' och 'flytta pa sig' finns inte i nagon ordbok; adjektivet har fatt en kategori "
     "ur kortets egen definition. EXEMPELMENING BYTT: legacys 'De har strumporna ar inte maka' "
     "visade den minst brukliga betydelsen; den nya visar verbet, som ar det Adam faktiskt "
     "anvander."),

"serendipitet": dict(
  hb="Förmågan att göra lyckliga upptäckter av en ren slump",
  reg="neutral, positiv",
  grp=[["≈≈ lyckosam slump"]],
  ex='Penicillinet upptäcktes genom ren <font color="#3498db">serendipitet</font> — Fleming letade '
     'efter något helt annat.',
  etym="efter engelska serendipity; till namnet Serendip i sagan De tre prinsarna från Serendip, "
       "av persiska Sarandip 'Sri Lanka'",
  sl="SO: 'formaga att gora lyckliga upptackter av en slump', med tillagget 'ofta forekommande "
     "t.ex. hos uppfinnare'. SAOL: 'formaga att gora vardefulla upptackter av en slump'. Legacys "
     "'Formagan att hitta nagot vardefullt av en slump, utan att ha letat efter det' ar i sak "
     "riktig och nara bada ordbockerna; justerad till SO:s ordval ('gora lyckliga upptackter') och "
     "'en REN slump' for att ta bort tvetydigheten i legacys 'utan att ha letat efter det' -- "
     "poangen ar inte att man inte letade alls, utan att man letade efter nagot annat (som "
     "exempelmeningen visar). Kategorin '≈≈ lyckosam slump' lag redan pa kortet och ar satt ur "
     "definitionen; ordet har ingen enordssynonym i nagon kalla. REGISTER ANDRAT: 'formell' saknar "
     "stod -- varken SO eller SAOL markerar ordet; laddningen positiv, oforandrad. Exempelmening "
     "oforandrad -- penicillinet ar sjalva skolexemplet. Etymologi ny, ur SO: att ordet kommer ur "
     "en persisk saga om tre prinsar som standigt hittade det de inte sokte ar hela forklaringen "
     "till ordet."),

"intagande": dict(
  hb="Som utan ansträngning vinner andras sympati",
  reg="neutral, positiv",
  grp=[["charmerande", "behaglig"]],
  ex='Hennes enkla och <font color="#3498db">intagande</font> väsen gjorde henne omtyckt av alla.',
  etym="fornsvenska intaka 'bemäktiga sig'",
  sl="SO: 'som vinner spontan sympati'. SAOL: 'behaglig, charmerande'. Legacys 'Charmerande, "
     "vinner spontan sympati' var CIRKULAR: 'charmerande' var bade definitionens forsta ord och "
     "kortets forsta synonym. Definitionen star nu ensam ('som utan anstrangning vinner andras "
     "sympati', dar 'utan anstrangning' ar SO:s 'spontan' i Adam-tal) och 'charmerande' ligger dar "
     "den hor hemma. 'charmerande' och 'behaglig' star bada ordagrant i SAOL:s led (belagda). "
     "SYNONYM BORTTAGEN: legacys 'fortjusande' ar OLD-facit men finns inte i vare sig SO eller "
     "SAOL, och ar dessutom starkare an intagande. REGISTER ANDRAT: 'vardaglig' saknar stod -- "
     "varken SO eller SAOL markerar ordet; laddningen andrad fran neutral till positiv, vilket "
     "bade SO ('sympati') och SAOL ('behaglig') ger direkt stod for. Exempelmening oforandrad. "
     "Etymologi ny, ur SO -- 'bemaktiga sig' visar bilden: den intagande personen intar en, som "
     "en fastning."),

"kadrilj": dict(
  hb="Äldre dans där fyra eller flera par dansar mitt emot varandra i livligt tempo ; "
     "ryttaruppvisning där en grupp rider olika turer till musik",
  reg="neutral, neutral, historia ; neutral, neutral, sport",
  grp=[["kontradans"], ["≈≈ ryttaruppvisning"]],
  ex='De dansade <font color="#3498db">kadrilj</font> på slottsbalen med eleganta steg.',
  etym="av franska quadrille, av spanska cuadrilla 'ryttargrupp'; till latin quadrus 'fyrkantig' "
       "-- fyra par i en fyrkant",
  sl="SAKNAD BETYDELSE. SO ger TVA definitioner: 'en kontradans med fyra eller flera par som "
     "dansar mitt emot varandra' (med tillagget 'i livligt tempo; vanlig under 1800-talet') och "
     "'typ av ryttaruppvisning' (med tillagget 'av en grupp som rider ett antal olika turer till "
     "musik'). Legacy hade bara dansen. Ryttaruppvisningen ar ingen utvidgning utan en egen "
     "definition med eget tillagg, och den ar dessutom det som binder ihop ordet med dess "
     "ursprung (spanska cuadrilla = ryttargrupp). Tillagd. Aven dansdefinitionen var for tunn: "
     "legacys 'Aldre gruppdans i par' sager inte det som gor en kadrilj till en kadrilj -- att "
     "paren star MITT EMOT VARANDRA. Tillagt. 'kontradans' star ordagrant i SO:s definition "
     "(belagd) och har flyttats ut ur kortets definition sa att den inte forklarar sig sjalv. "
     "REGISTER ANDRAT: 'litterar' saknar stod -- SO ger ingen brukligheskommentar; domanerna "
     "historia (SO: 'vanlig under 1800-talet') och sport tillagda. Exempelmening oforandrad. "
     "Etymologi ny, ur SO -- 'fyra par i en fyrkant' gor bade namnet och dansformen "
     "sjalvforklarande."),

"spelevinker": dict(
  hb="Lekfull person som gärna hittar på upptåg",
  reg="vardaglig, skämtsam",
  grp=[["≈≈ upptågsmakare"]],
  ex='Han var en riktig <font color="#3498db">spelevinker</font> som alltid fick klassen att '
     'skratta.',
  etym=None,
  sl="OBS SVAGT KALLAGE, och det ar den viktigaste noteringen pa det har kortet. "
     "Trekallskontrollen ger 'traffar: saob' -- alltsa INGEN traff i vare sig SO eller SAOL, bara "
     "i SAOB (den historiska ordboken). Det finns darfor ingen modern ordboksdefinition att stodja "
     "sig pa och ingen belagd synonym. Kortet vilar pa OLD-facit ('(vard.) upptagsmakare, gamang, "
     "filur') plus legacys egen text, som stammer med bada. Definitionen ar i sak oforandrad; "
     "'gillar upptag' bytt mot 'garna hittar pa upptag' (aktivare, samma sak). SYNONYMER "
     "NEDGRADERADE: legacys 'upptagsmakare' och 'skojare' stod omarkerade, alltsa som fullt "
     "utbytbara belagda synonymer -- men ingen ordbok belagger dem. En kategori kvar, satt ur "
     "kortets egen definition (ingen kalla kravs for ≈≈). REGISTER: 'vardaglig' tillagt med stod i "
     "OLD-facits '(vard.)'; laddningen 'skamtsam' oforandrad, vilket 'filur' och 'gamang' "
     "bekraftar. Exempelmening oforandrad. ETYMOLOGI UTELAMNAD: ingen kalla."),

"spont": dict(
  hb="Utstående list på en bräda som passar in i en ränna på nästa bräda vid hopfogning",
  reg="fackspråklig, neutral, teknik",
  grp=[["kantlist"]],
  ex='<font color="#3498db">Sponten</font> på plankan passade perfekt in i rännan på nästa.',
  etym="av lågtyska spunt 'sprund (i tunna); tapp; spont'",
  sl="SO: 'utstaende parti pa brada, planka eller dylikt som vid sammanfogning fors in i en ranna "
     "pa en annan brada, planka eller dylikt'. SAOL: 'kantlist och fals pa brada; fog mellan "
     "sadana brador'. Legacys 'Utstickande FJADER pa en brada' anvande fackordet 'fjader' -- ratt "
     "i snickarsprak (spont och fjader) men obegripligt for den som inte redan kan det, och "
     "dessutom var 'fjader' kortets enda synonym, sa definitionen och synonymen var samma ord. "
     "Utskrivet till SO:s hela bild: listen OCH rannan den passar i, vilket ar det enda som gor "
     "att man forstar vad en spont ar till for. 'kantlist' star ordagrant i SAOL:s led (belagd) "
     "och ar dessutom begripligt utan forkunskaper. RISKFLAGGA old_delar_inget_ordforrad utredd: "
     "OLD sager 'sammanlankande bradlist' -- samma sak som SAOL:s 'kantlist', bara annorlunda "
     "sammansatt; flaggan slog till pa legacys 'fjader'. Loses av rattelsen. REGISTER ANDRAT: "
     "'formell' bytt mot 'fackspraklig' med doman teknik -- ordet ar rent snickeri-fackssprak, "
     "inte formell allmansvenska. EXEMPELMENING: samma mening, men uppslagsordet ar nu markerat "
     "(legacy saknade highlight helt)."),
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
