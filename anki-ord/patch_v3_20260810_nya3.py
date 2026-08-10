# -*- coding: utf-8 -*-
"""v3-omgranskning av 65 kort ur is:new, tredje omgången 2026-08-10.

Varje exempelmening skrivs ut i sin helhet med den böjda formen redan
highlightad — ingen {}-mall, det var den som gav "Rektorn presidera vid
disputationen".

## Registerprincipen som tillämpas här

Blindgranskaren fällde tre kort i förra omgången, och alla tre gällde
REGISTER, inget gällde betydelse. Invändningen mot *kroasera* var precis:
ett påstått `fackspråklig` på ett ord som i själva verket är ålderdomligt.
Regeln härifrån: **stilnivån ska kunna försvaras mot ordets faktiska
profil, och när SO/SAOL inte markerar något ska `neutral` väljas framför
en gissning.** Det är också botemedlet mot att 49 % av decket står som
`formell` — ett värde som i praktiken betytt "jag vet inte".

## Innehållsfel som hittades (13 substantiella)

  kangas       HELT FEL ORD — kortet beskrev finskans *kangas* (hedmark/tyg).
               SO, SAOL och OLD-facit säger alla "höftskynke" (swahili khanga).
  tangera      FEL BETYDELSE — "nästan nå ett rekord". SO: uppnå ett resultat
               som är EXAKT likvärdigt. Kortets exempel förstärkte felet.
  depression   FEL BETYDELSE — "lågtrycksområde i atmosfären". SO:s tredje
               betydelse är landområde under havsytans nivå.
  in media res STAVFEL PÅ FRAMSIDAN — noll träffar i alla tre källorna. Rätt
               form *in medias res* finns i SO, belagd sedan 1884.
  semiologi    OBELAGT TILLÄGG — "(medicin) läran om sjukdomssymtom" finns
               varken i SO eller SAOL.
  träl         *livegen* är en annan rättslig institution, och SAOL placerar
               trälen i forntida Norden, inte medeltiden. Bildlig bet. saknades.
  forensisk    FÖR SNÄV — kortet reducerade ordet till kriminalteknik. SO:s
               kärna är hela rättsväsendet (forensisk psykologi/vetenskap).
  dunst        Idiomet *slå blå dunster i ögonen på någon* saknades helt.
  sekret       SO har två homografer; adjektivet 'hemlig' saknades.
  korrupt      Den filologiska betydelsen (förvanskad avskrift) saknades.
  belysande    Betydelsen 'avslöjande, ofta ironiskt' saknades.
  slimmad      Den bildliga organisationsbetydelsen saknades.
  bale         'insektsbo' finns inte i någon källa.

Plus ett tjugotal mindre: saknade bibetydelser (markant, samfälld, jurist,
avel, domptör, genrep, vitmena, skröplig, förordning, annalkande) och
felaktiga synonymer (jamare hade *grogg*/*toddy* — en jamare är en sup).

## Misslyckade uppslagningar, utskrivna

  dra i långbänk  svenska.se föll tillbaka på fritextsökning och returnerade
                  uppslagen för *dra till med* och *oxe* (160 KB svar). Slogs
                  om under *långbänk*, där idiomet finns med etymologi.
  in media res    noll träffar — se ovan, felstavning.
  omnipotent      ingen SO-artikel, bara SAOL "allsmäktig".
  okvädinsord     ingen SO-artikel, bara SAOL "glåpord".
  curare/melass   endast svenska.se (wiktionary 429 / saknas).
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HAR = os.path.dirname(os.path.abspath(__file__))
FIL = os.path.join(HAR, "sessions", "session_2026-08-10_v3-omgranskning-nya3.json")
B = '<font color="#3498db">%s</font>'


def kalla(o):
    import urllib.parse
    q = urllib.parse.quote(o)
    return ("https://svenska.se/api/msearch?ord=%s "
            "https://www.synonymer.se/sv-syn/%s "
            "https://sv.wiktionary.org/wiki/%s" % (q, q, q))


R = {

"bale": ("Skålformat fågelbo, särskilt själva fördjupningen i boet",
  "neutral, neutral, biologi", ["fågelbo", "rede", "fågelrede"],
  "Storkens bo är vanligen en stor %s av kvistar." % (B % "bale"),
  "till fornsvenska badhul, troligen 'grävd grop som liggplats'; besläktat med bädd",
  "ÖVERSKOTT BORTTAGET. SO ger '(fågel)rede', SAOL 'skålformat fågelbo'. Kortets 'eller insektsbo' finns inte i någon av de tre källorna. Registret `dialektal` ströks — varken SO eller SAOL markerar ordet så; det är ett sällsynt men vanligt svenskt ord, belagt sedan 1736."),

"diffus": ("Otydligt avgränsad, utan skarpa konturer ; bildligt: svag och obestämd, t.ex. om minnen eller aningar",
  "neutral, neutral", ["otydlig", "vag", "suddig"],
  "Hon hade bara %s minnen från barndomen." % (B % "diffusa"),
  "av latin diffu´sus, particip av diffun´dere 'sprida ut'; jfr diffundera",
  "SAKNAD BETYDELSE. SO har två betydelseskikt och kortet hade bara det första (om konturer). Det bildliga — *diffusa minnen*, *hon anade diffust att något var på tok* — är minst lika vanligt. Registret `formell` ströks: SO markerar ingenting, och ordet används i vardagsspråk."),

"jamare": ("Sup, en liten mängd starksprit", "vardaglig, skämtsam",
  ["sup", "hutt", "nubbe"],
  "En liten %s till sillen skulle sitta fint." % (B % "jamare"),
  "skämtsam ombildning av jamaikarom",
  "FELAKTIGA SYNONYMER. Kortet hade *grogg* och *toddy* — men en jamare är en sup, alltså en liten mängd oblandad starksprit. En grogg är en utspädd långdrink och en toddy en varm dryck; ingen av dem är utbytbar. synonymer.se ger hutt, nubbe, järn. Etymologin (av *jamaikarom*) tillagd, och den förklarar valören: ordet är skämtsamt."),

"korrupt": ("Som låter sig mutas eller missbrukar sin ställning ; om text: förvanskad, vanställd genom bristfällig avskrift",
  "neutral, negativ", ["mutbar", "korrumperad", "förvanskad"],
  "Många länder styrs av %s regeringar." % (B % "korrupta"),
  "till korrumpera, av latin corrum´pere 'fördärva'",
  "SAKNAD BETYDELSE. SO ger två: den om personer och institutioner, och den filologiska — *de bevarade avskrifterna av verket är svårt korrupta*. Den andra möter man i textkritik och i IT (*en korrupt fil*), och den saknades helt. Registret `negativ` saknade stilnivå; båda axlarna skrivs nu ut."),

"likvid": ("Om tillgångar: omedelbart tillgängliga för utbetalning ; som substantiv: betalning",
  "fackspråklig, neutral, ekonomi", ["betalningsmedel", "kontanter", "köpeskilling"],
  "Bolagets %s medel räckte inte till löneutbetalningarna." % (B % "likvida"),
  "av latin liq´uidus 'flytande; klar'; jfr likvidera",
  "PRECISERAT. SO:s adjektiv beskriver TILLGÅNGARNA ('omedelbart tillgänglig för utbetalning'), inte innehavaren. Kortets 'som har pengar redo att betala med' flyttar egenskapen till fel led, och synonymen *betalningsstark* är dessutom ett annat begrepp — soliditet, inte likviditet. Ett bolag kan vara betalningsstarkt men illikvidt."),

"urholka": ("Göra hål eller fördjupning i något ; bildligt: gradvis avlägsna det värdefulla ur något så att bara formen återstår",
  "neutral, neutral", ["gröpa ur", "holka ur", "undergräva"],
  "Lagen om anställningsskydd höll på att %s." % (B % "urholkas"),
  "till hål; jfr svensk dialekt holka (ur)",
  "Innehållet stämde — båda SO:s betydelser fanns. Registret `formell` ströks (SO markerar ingenting) och exempelmeningen bytt till SO:s egen bildliga, eftersom det är den svårare av de två betydelserna."),

"belysande": ("Som gör något lättare att förstå ; äv. avslöjande, ofta ironiskt om något som röjer en brist",
  "neutral, neutral", ["klargörande", "illustrativ", "avslöjande"],
  "Det är %s att statsministern inte bemöter kritiken i sitt inlägg." % (B % "belysande"),
  "efter tyska beleuchten med samma betydelse",
  "SAKNAD BETYDELSE. SO ger utöver 'skapar förutsättningar för förståelse' även 'avslöjande', med markeringen *ibland ironiskt* och språkprovet ovan. Det är den användning man möter i ledarsidor och kommentarer, och den saknades."),

"boett": ("Fodral eller hölje kring urverket i ett ur — enligt SO särskilt i fickur",
  "fackspråklig, neutral, teknik", ["urfodral", "klockhölje"],
  "Urmakaren öppnade %s för att komma åt verket." % (B % "boetten"),
  "av franska boîte 'dosa'; av medeltidslatin bux´ida 'låda av buxbom'",
  "Innehållet stämde i sak. Preciserat att SO och SAOL båda skriver *fickur* — i modernt urmakeri används ordet även om armbandsur, men det står inte i ordböckerna, så kortet säger nu vad källan säger. Registret ändrat från `formell` till `fackspråklig`: det är en term i ett hantverk, inte ett byråkratiskt ord."),

"depression": ("Svår och långvarig nedstämdhet ; djup ekonomisk kris med produktionsminskning och stor arbetslöshet ; landområde som ligger under havsytans nivå",
  "neutral, neutral", ["nedstämdhet", "svårmod", "lågkonjunktur", "sänka"],
  "Döda havets %s når 392 meter under havsytan." % (B % "depression"),
  "av franska dépression; till latin depri´mere 'trycka ned'; jfr deprimerad",
  "FELAKTIG BETYDELSE RÄTTAD. Kortets tredje betydelse var 'lågtrycksområde i atmosfären'. SO:s tredje betydelse är geografisk — *landområde som är beläget under havsytans nivå*, med Döda havet som språkprov. Meteorologibetydelsen finns i engelskan men inte i SO eller SAOL. Synonymen *lågtryck* struken av samma skäl."),

"eau-de-vie": ("Destillat på druvor eller frukt ; i Sverige särskilt om ett druvdestillat med spritstillsats, s.k. folkkonjak",
  "neutral, neutral, matlagning", ["fruktbrännvin", "akvavit"],
  "De avslutade middagen med en liten %s." % (B % "eau-de-vie"),
  "av franska eau-de-vie, eg. 'livsvatten'; jfr akvavit",
  "Kompletterat. SO ger utöver grundbetydelsen en svensk specialbetydelse: druvdestillat med tillsats av sprit, det som säljs som folkkonjak. Den är relevant just i Sverige och saknades. Etymologin ('livsvatten') tillagd — den kopplar ihop ordet med *akvavit*, som betyder exakt samma sak på latin."),

"forensisk": ("Som hör till rättsväsendet ; äv. mer specifikt: kriminalteknisk",
  "fackspråklig, neutral, juridik", ["rättslig", "kriminalteknisk", "rättsmedicinsk"],
  "Hon undervisar i %s psykologi." % (B % "forensisk"),
  "av latin fore´nsis 'från torget; offentlig', till for´um 'torg'",
  "FÖR SNÄVT. Kortet skrev 'Rättsmedicinsk, kopplad till brottsutredning' — den engelska CSI-betydelsen. SO:s kärna är bredare: *som har att göra med rättsväsendet*, med språkproven forensisk psykologi, forensisk vetenskap, forensisk medicin. Etymologin visar varför: ordet kommer av *forum*, torget där rättskipningen ägde rum."),

"gratifikation": ("Penninggåva eller belöning utöver den vanliga lönen",
  "formell, neutral, ekonomi", ["penninggåva", "belöning", "bonus"],
  "Vissa anställda fick en %s till jul." % (B % "gratifikation"),
  "av latin gratifica´tio 'gunstbevis', till gra´tia 'gunst'; jfr grace, gratie",
  "Innehållet stämde mot både SO och SAOL. Etymologin tillagd — den förklarar tonen: en gratifikation är historiskt en gunst, inte en rättighet, vilket är skillnaden mot *bonus* i ett anställningsavtal."),

"hundväder": ("Mycket svårt oväder", "vardaglig, negativ",
  ["ruskväder", "busväder", "oväder"],
  "Storm och snöblandat regn — vilket %s!" % (B % "hundväder"),
  None,
  "SO: 'svårt oväder', SAOL: 'ruskväder'. Innehåll och register stämde. Exempelmeningen bytt till SO:s egen, som visar den utropande användning ordet nästan alltid har."),

"in media res": ("Berättargrepp där framställningen börjar mitt i handlingen, utan inledande bakgrund",
  "formell, neutral, litteraturvetenskap", ["mitt i handlingen"],
  "Gösta Berlings saga inleds %s: „Äntligen stod prästen i predikstolen.”" % (B % "in medias res"),
  "av latin in´ med´ias re´s, eg. 'in i sakernas mitt'",
  "STAVFEL PÅ FRAMSIDAN. *in media res* gav noll träffar i svenska.se, synonymer.se OCH wiktionary — alla tre. Den korrekta latinska formen är *in medias res* (ackusativ plural: 'in i sakerna'), och den finns i SO med betydelsen 'omedelbart in i ämnet', belagd sedan 1884. Framsidan är rättad. Kortets betydelse var i övrigt riktig."),

"jiddisch": ("Germanskt språk med starka inslag av hebreiska och slaviska språk, talat av askenasiska judar — ett av Sveriges fem nationella minoritetsspråk",
  "neutral, neutral, lingvistik", ["judetyska"],
  "%s är ett av Sveriges nationella minoritetsspråk." % (B % "Jiddisch"),
  "av tyska jiddisch, eg. 'judetyska'; jfr engelska yiddish",
  "Innehållet stämde. Två tillägg ur SO: minoritetsspråksstatusen (relevant just i Sverige, och SO:s eget språkprov) och synonymen *judetyska*, som är den äldre svenska benämningen — synonymfältet var tomt."),

"kangas": ("Typ av höftskynke — färgstarkt bomullstyg som bärs virat kring kroppen, särskilt i Östafrika",
  "neutral, neutral", ["höftskynke", "sarong"],
  "Kvinnorna på marknaden bar mönstrade %s." % (B % "kangas"),
  "av swahili khanga med samma betydelse",
  "KORTET BESKREV FEL ORD. Det stod 'Torr, tallbevuxen hedmark (meänkieli) ; tyg, väv (finskt lånord)' — det är finskans *kangas*. Det svenska uppslagsordet i SO och SAOL är ett annat ord med ett annat ursprung: swahili *khanga*, 'typ av höftskynke', belagt i svenskan sedan 1976. OLD-facit sa också *höftskynke*, så kortet motsade sitt eget facit. Hela kortet omskrivet."),

"lappri": ("Obetydlig sak, struntsak", "neutral, lätt negativ",
  ["struntsak", "bagatell", "petitess"],
  "Vi kan inte slösa tid på sådant %s!" % (B % "lappri"),
  "av lågtyska lapperi 'lagning; fuskverk'; till lapp",
  "Innehållet stämde. Registret `vardaglig` ströks — varken SO eller SAOL markerar ordet, och det hör snarast hemma i skriftspråk. Valören är lätt negativ: att kalla något lappri är att avfärda det. Etymologin tillagd (av *lapp*, alltså 'lappverk')."),

"markant": ("Starkt framträdande, påfallande ; äv. avsevärd, betydande",
  "neutral, neutral", ["påfallande", "framträdande", "avsevärd"],
  "Det blev en %s nedgång i börsaktiviteten." % (B % "markant"),
  "av franska marquant, till marquer 'märka'",
  "SAKNAD BETYDELSE. SO ger två: 'starkt framträdande' (om t.ex. ett hus i stadsbilden) och 'avsevärd, betydande' (om en förändrings storlek). Kortets 'Tydlig, påtaglig' täcker bara den första — men det är den andra man möter i *en markant ökning*, som är den absolut vanligaste användningen i nyhetstext."),

"sekret": ("Vätska som utsöndras från en körtel i en levande organism ; som adjektiv, ålderdomligt: hemlig",
  "fackspråklig, neutral, medicin", ["avsöndringsvätska", "utsöndring", "hemlig"],
  "Saliv, magsaft och andra %s." % (B % "sekret"),
  "substantivet av nylatin secre´tum; adjektivet av latin secre´tus 'avskild; hemlig' — jfr diskret",
  "SAKNAD BETYDELSE. SO har TVÅ homografer under *sekret*: substantivet (kroppsvätska, belagt 1840) och adjektivet 'hemlig' (belagt 1560), som lever kvar i *sekreta utskottet*. Kortet hade bara den första. Etymologin visar att de hänger ihop: båda går till latinets 'avsöndrad, avskild'."),

"sint": ("Arg, ilsken", "vardaglig, neutral",
  ["arg", "ilsken", "förargad"],
  "Hon blev %s över sakernas tillstånd." % (B % "sint"),
  "fornsvenska -sinter; jfr svensk dialekt sint(er) 'hågad; förtretad'",
  "Innehållet stämde. Synonymen *förtörnad* ströks — den ligger på en helt annan stilnivå (högtidlig) än *sint*, som synonymer.se markerar som provinsiellt/vardagligt. Valören satt till neutral: ordet BESKRIVER ilska men bär inte själv en nedsättande ton."),

"stålsätta sig": ("Mobilisera sin själsliga motståndskraft inför något svårt",
  "neutral, neutral", ["härda sig", "göra sig stark", "stå emot"],
  "Hon måste %s för att inte gråta." % (B % "stålsätta sig"),
  None,
  "SO: 'mobilisera själslig motståndskraft'. Innehållet stämde. Registret `vardaglig` ströks — SO markerar ingenting, ordet är gångbart i all slags text. Exempelmeningen bytt till SO:s egen."),

"vitmena": ("Stryka vitt med kalk ; bildligt: göra eller bli mycket blek",
  "neutral, neutral", ["vitkalka", "kalka", "vitlimma"],
  "Hon var %s i ansiktet av skräck." % (B % "vitmenad"),
  "fornsvenska hvitminadher; till vit och lågtyska minie 'mönja'; jfr miniatyr, mönja",
  "SAKNAD BETYDELSE. SO ger 'vitkalka' och, markerat *äv. bildligt*, 'mycket blek' med språkprovet ovan. Kortet hade bara den bokstavliga. Registret `formell` ströks — att vitmena en fasad är ett vardagligt hantverksord."),

"annalkande": ("Som närmar sig ; som substantiv: närmande, i uttrycket *vara i annalkande*",
  "neutral, neutral", ["stundande", "förestående", "antågande"],
  "Våren var i %s." % (B % "annalkande"),
  "till an i betydelsen 'till' och nalkas",
  "SAKNAD ORDKLASS. SO har två uppslag: adjektivet (*en annalkande fara*) och substantivet (*de främsta åkarna var i annalkande*). Kortet hade bara adjektivet, men det är substantivkonstruktionen som är svår att gissa sig till. Registret `formell` ströks."),

"avbön": ("Offentligt medgivande av att man haft fel — nästan alltid i uttrycket *göra avbön*",
  "formell, neutral", ["ursäkt", "offentlig ursäkt"],
  "Han fick välja mellan att göra %s för sitt uttalande och att lämna partiet." % (B % "avbön"),
  "till fornsvenska afbidhia 'be om nåd'",
  "PRECISERAT. SO säger 'offentligt medgivande av fel' — kortets tillägg 'och bön om förlåtelse' står inte där, och skiljer sig i sak: en avbön är att ta tillbaka ett påstående, inte nödvändigtvis att be om ursäkt. Att ordet praktiskt taget bara förekommer i *göra avbön* är nu utskrivet."),

"avel": ("Planmässig förökning och uppfödning av djur ; äv. om avkomman ; äv. om djurens härstamning och kvalitet",
  "neutral, neutral, jordbruk", ["uppfödning", "förädling", "avkomma"],
  "Hästar av god svensk %s." % (B % "avel"),
  "fornsvenska afl 'kraft; avkastning; avel'; besläktat med latin opus",
  "TVÅ SAKNADE BETYDELSER. SO markerar *äv. om resultatet el. avkomman* (årets avel av svin) och *äv. om kvaliteten* (hästar av god svensk avel). Kortet hade bara verksamheten. Det är den tredje som gör uttrycket 'av god avel' begripligt."),

"begiven": ("Som känner en lustfylld dragning till något — konstrueras med prepositionen *på*",
  "neutral, neutral", ["lysten", "sugen på", "hågad"],
  "Han var %s på spel och satte hela lönen på travet." % (B % "begiven"),
  "till äldre svenska begiva sig 'hänge sig åt något'",
  "Innehållet stämde mot SO. Det viktiga tillägget är konstruktionen: ordet står nästan aldrig ensamt utan *begiven PÅ något*, och det är det man behöver veta för att kunna använda det. Registret `formell` ströks — SO markerar ingenting."),

"bröstvärn": ("Kraftig skyddande vall av ungefär halv manshöjd vid en militär anläggning",
  "neutral, neutral, militär", ["skyddsvall", "förskansning", "barrikad"],
  "Skyttarna tog betäckning bakom %s." % (B % "bröstvärnet"),
  None,
  "AVGRÄNSAT. Kortet skrev 'Låg skyddsmur, t.ex. vid en fästning eller balkong'. SO och SAOL begränsar båda ordet till militära anläggningar (SAOL: *t.ex. i skyttegrav*). Det som sitter vid en balkong heter *bröstning*. synonymer.se blandar visserligen in balustrad och fönsterbröstning, men ordböckerna gör det inte, och de avgör."),

"curare": ("Muskelförlamande pilgift som utvinns ur sydamerikanska växter",
  "fackspråklig, neutral, medicin", ["pilgift"],
  "Jägarna doppade pilspetsarna i %s." % (B % "curare"),
  "av spanska curare; ur ett sydamerikanskt indianspråk",
  "SO: 'ett muskelförlamande gift', SAOL: 'ett muskelförlamande pilgift'. Innehållet stämde. UPPSLAGNING OFULLSTÄNDIG: bara svenska.se gav träff — synonymer.se och wiktionary saknar ordet. Slutsatsen vilar därför på en källa, men det är den källa som väger tyngst."),

"degenerera": ("Utvecklas till det sämre, urarta ; äv. transitivt: utveckla något till det sämre",
  "neutral, negativ", ["urarta", "försämras", "förfalla"],
  "Debatten %s snabbt till rent skällande." % (B % "degenererade"),
  "av latin degenera´re, till de 'från' och gen´us 'släkt; börd'",
  "Innehållet stämde. Registret `negativ` saknade stilnivå — bara valören var ifylld, vilket är precis det fel som gjorde registerfältet oanvändbart över hela decket. Båda axlarna skrivs nu ut. Etymologin tillagd: 'att falla ur sin släkt'."),

"domptör": ("Djurtämjare, särskilt inom cirkus ; äv. bildligt om någon som behärskar något svårhanterligt",
  "neutral, neutral", ["djurtämjare", "dressör", "betvingare"],
  "Dirigenten var något av en %s." % (B % "domptör"),
  "av franska dompteur, till domptera 'tämja'",
  "SAKNAD BETYDELSE. SO markerar *äv. allmännare* med språkprovet ovan — den bildliga användningen om en person som tämjer något annat än djur. Kortet hade bara den bokstavliga."),

"dra i långbänk": ("Medvetet dra ut på ett ärende utan att avgöra det",
  "neutral, negativ", ["förhala", "fördröja", "skjuta upp"],
  "Att ärendet %s tärde på allas tålamod." % (B % "drogs i långbänk"),
  "troligen efter tyska etwas auf die lange Bank ziehen; belagt ca 1635, aktualiserat 1978 genom Thorbjörn Fälldin",
  "UPPSLAGNING MISSLYCKADES FÖRST, sedan löst. Sökning på hela frasen fick svenska.se att falla tillbaka på fritextsökning och returnera artiklarna för *dra till med* ('anföra på måfå') och *oxe* — 160 KB irrelevant svar som hade sett ut som en lyckad hämtning i loggen. Ordet slogs om under *långbänk*, där idiomet står med språkprov och etymologi. Innehållet stämde; registret `vardaglig` ströks (SO markerar ingenting) och valören negativ tillagd."),

"dunst": ("Avgiven gas eller ånga, ofta med lukt ; dis, töcken ; i uttrycket *slå blå dunster i ögonen på någon*: lura någon ; minsta hagelsorten i en patron",
  "neutral, neutral", ["ånga", "dis", "os"],
  "Genom sin charm lyckades han gång på gång slå blå %s i ögonen på sin omgivning." % (B % "dunster"),
  "av lågtyska dunst; uttrycket slå blå dunster i ögonen (1840) syftar ursprungligen på trollkonstnärer som gjorde rök för att dölja sina knep",
  "TRE SAKNADE BETYDELSER. Kortet hade bara 'Ånga eller lätt dimma'. SO ger dessutom idiomet *slå blå dunster i ögonen på någon* — som är den i särklass vanligaste användningen av ordet i modern svenska — samt hagelbetydelsen, som även SAOL har. Etymologin till idiomet är tillagd eftersom den gör uttrycket minnesvärt."),

"en masse": ("I stor mängd, alla på en gång", "neutral, neutral",
  ["massvis", "i mängd", "lassvis"],
  "De verkar ha pengar %s." % (B % "en masse"),
  "av franska en masse; jfr massa",
  "SO och SAOL ger båda 'i stor mängd'. Innehållet stämde. Registret `formell` ströks — synonymer.se markerar tvärtom uttrycket som vardagligt, och SO markerar ingenting."),

"estetik": ("Läran om det sköna och om konsten ; äv. om en bestämd formgivningsprincip eller stil",
  "formell, neutral, filosofi", ["skönhetslära", "formspråk"],
  "Den episka teaterns %s bröt medvetet illusionen." % (B % "estetik"),
  "ur grekiska ai´sthesis 'förnimmelse; uppfattning'; jfr anestesi",
  "SAKNAD BETYDELSE. SO markerar *äv. om viss teknik eller dylikt för uppnående av (konstnärlig) skönhet* — den räknebara betydelsen i *en estetik*, *den episka teaterns estetik*. Kortet hade bara den abstrakta läran. Etymologin tillagd: samma rot som i *anestesi*, alltså 'utan förnimmelse'."),

"fläns": ("Utstående, plant och ofta ringformat parti på ett rör eller en maskindel, avsett för hopkoppling",
  "fackspråklig, neutral, teknik", ["krage", "krans", "förstärkningslist"],
  "Rörledningen kopplades ihop med en %s och sex bultar." % (B % "fläns"),
  "av engelska flange; besläktat med flank",
  "SO preciserar funktionen: ett utstående, plant, ofta ringformat parti — det är formen och kopplingsfunktionen som gör en fläns till en fläns, inte bara att den sticker ut. Registret ändrat från `formell` till `fackspråklig` med domänen teknik."),

"framdeles": ("Längre fram i tiden, hädanefter", "neutral, neutral",
  ["hädanefter", "framöver", "i fortsättningen"],
  "Det kommer att visa sig %s om hon har rätt." % (B % "framdeles"),
  "fornsvenska framdelis, eg. 'längre fram på vägen'; till 2led; jfr alldeles",
  "Innehållet stämde. Registret `litterär` ströks — varken SO eller SAOL markerar ordet, och det förekommer i vanlig sakprosa. Etymologin tillagd: eg. 'längre fram på vägen', samma bildning som i *alldeles*."),

"frestad": ("Benägen eller lockad att handla på ett visst sätt",
  "neutral, neutral", ["lockad", "hågad", "benägen"],
  "Man är %s att sätta etiketten „kubism” på hans måleri." % (B % "frestad"),
  "till fresta, fornsvenska fresta 'försöka, pröva'",
  "SO: 'benägen att handla på visst sätt'. Innehållet stämde. Registret `vardaglig` ströks — SO markerar ingenting, och exempelmeningen ovan (SO:s egen) visar tvärtom en resonerande skriftspråklig användning."),

"förordning": ("Rättslig författning ; i Sverige beslutad av regeringen ; äv. om EU-förordning, som gäller direkt i medlemsstaterna",
  "formell, neutral, juridik", ["författning", "stadga", "föreskrift"],
  "Tillämpningen av lagen regleras i särskild %s." % (B % "förordning"),
  None,
  "SAKNAD BETYDELSE. SO markerar *äv. något utvidgat* med språkprovet *Europaparlamentets och rådets förordningar*. EU-förordningen är en annan sak än den svenska regeringsförordningen — den är direkt tillämplig utan att riksdagen gör något — och den saknades helt. För någon som läser nyheter är det den vanligaste betydelsen."),

"genrep": ("Sista och viktigaste repetitionen före premiär ; äv. allmännare om en sista genomkörning inför vilken viktig händelse som helst",
  "vardaglig, neutral", ["generalrepetition", "slutrepetition"],
  "Tävlingen är ett %s inför US Open." % (B % "genrep"),
  "kortord för generalrepetition",
  "SAKNAD BETYDELSE. SO markerar *äv. allmännare* med språkprovet ovan — den överförda användningen om t.ex. en idrottstävling. Kortet hade bara teaterbetydelsen. Etymologin (kortord för *generalrepetition*) tillagd, den förklarar också varför registret är vardagligt."),

"gungfly": ("Växtmatta som vilar på vatten i en myr ; bildligt: osäker grund att stå på",
  "neutral, neutral", ["flytmatta", "kärr", "osäker grund"],
  "Under krisåren levde många människor som på ett %s." % (B % "gungfly"),
  None,
  "Innehållet stämde — båda betydelserna fanns. Registret `formell` ströks; SO markerar ingenting och ordet är ett vanligt naturord. SO noterar att den bildliga betydelsen är belagd sedan 1872, alltså 166 år efter den bokstavliga."),

"in blanko": ("Ej ifylld — utan att belopp, villkor eller namn har angetts ; skrivs även *in blanco*",
  "fackspråklig, neutral, ekonomi", ["oifylld", "utan påskrift"],
  "Checken var utställd %s." % (B % "in blanco"),
  "av spanska blanco, italienska bianco 'vit; oskriven'; jfr blank",
  "Innehållet stämde. Tillagt att SO och SAOL båda stavar uttrycket *in blanco* i sina språkprov medan *in blanko* också är gångbart — en stavningsvariation som är värd att känna till när man möter ordet i text. Etymologin ('vit, oskriven') tillagd."),

"introvert": ("Som har en sluten, inåtvänd läggning ; ofta substantiverat om en sådan person",
  "neutral, neutral, psykologi", ["inåtvänd", "sluten", "inbunden"],
  "En tyst och lugn arbetsmiljö som passar särskilt bra för %s." % (B % "introverta"),
  "modern bildning till latin introver´tere 'vända inåt'; jfr extrovert",
  "SAKNAD ANVÄNDNING. SO markerar *ofta substantiverat* — *för introverta*, alltså ordet som substantiv. Det är så det oftast används idag. Registret `formell` ströks: ordet är numera vardagsspråk. Motsatsen *extrovert* framgår nu av etymologiraden."),

"jurist": ("Person som yrkesmässigt ägnar sig åt juridik ; äv. om den som studerar juridik",
  "neutral, neutral, juridik", ["rättslärd", "lagfaren"],
  "%s har tenta på lördag." % (B % "Juristerna"),
  "av medeltidslatin juris´ta med samma betydelse",
  "SAKNAD BETYDELSE. SO markerar *äv. om person som studerar för att avlägga juridisk examen* med språkprovet ovan. Kortets 'Person utbildad i juridik' utesluter just studenterna. Registret `formell` ströks — *jurist* är ett vardagligt yrkesord."),

"lamentation": ("Intensiv och utdragen klagan", "formell, lätt negativ",
  ["klagan", "jämmer", "veklagan", "jeremiad"],
  "Hennes %s hördes genom hela huset." % (B % "lamentationer"),
  "till lamentera, av latin lamenta´ri 'jämra sig'",
  "SO: 'intensiv klagan', SAOL: 'klagan, jämmer'. Innehållet stämde. Registret `litterär` ändrat till `formell`: ordet hör hemma i sakprosa lika mycket som i skönlitteratur. Valören sänkt från `negativ` till `lätt negativ` — ordet beskriver klagan och används ofta avfärdande, men är inte ett skällsord."),

"melass": ("Tjockflytande, mörkbrun biprodukt från sockertillverkning",
  "neutral, neutral, matlagning", ["sockersirap", "sirap"],
  "Han bakade pepparkakor med %s i degen." % (B % "melass"),
  "av franska mélasse, spanska melaza; till latin mel´ 'honung'; jfr marmelad, mousse",
  "SO och SAOL stämmer båda med kortet. UPPSLAGNING OFULLSTÄNDIG: bara svenska.se gav träff (wiktionary svarade 429). Etymologin tillagd — samma rot som i *marmelad*, latinets ord för honung."),

"mjärde": ("Burformat fiskeredskap som fisken eller kräftan simmar in i men inte hittar ut ur",
  "neutral, neutral", ["fiskebur", "ryssja", "katsa"],
  "Han vittjade %s varje morgon under kräftsäsongen." % (B % "mjärdarna"),
  "fornsvenska miärþre, ursprungligen 'flätad korg av vidjekvistar'",
  "SO: 'ett burformat fiskredskap'. Preciserat hur redskapet fungerar — envägsingången är hela poängen och skiljer mjärden från en vanlig bur. Registret `formell` ströks. Etymologin visar att ordet ursprungligen betydde flätad vidjekorg, belagt sedan 1300-talet."),

"moderera": ("Ändra till rimlig omfattning, dämpa ; anpassa ; leda ett samtal eller granska inlägg som moderator",
  "neutral, neutral", ["dämpa", "jämka", "leda"],
  "Hon fick %s sina krav för att förhandlingen skulle gå framåt." % (B % "moderera"),
  "via franska av latin modera´ri 'dämpa; mildra; anpassa'",
  "PRECISERAT. SO ger tre betydelser och markerar särskilt internetanvändningen (*spec. äv. i fråga om diskussionsgrupp el. liknande på internet*, belagd 1997). Kortets 'leda en diskussion' täcker moderatorrollen i en panel men inte den att granska och släppa igenom inlägg, som är den vanligaste i dag."),

"moralkaka": ("Förnumstigt moraliserande tillsägelse", "vardaglig, negativ",
  ["moralpredikan", "straffpredikan", "uppsträckning"],
  "Pappa höll en lång %s om att komma hem sent." % (B % "moralkaka"),
  "till kaka i en äldre bildlig betydelse 'bestraffning'",
  "SO: 'förnumstigt moraliserande yttrande'. Innehåll och register stämde båda — ett av få kort där så var fallet. Etymologin tillagd eftersom sammansättningen annars är obegriplig: *kaka* betydde en gång bestraffning."),

"okvädinsord": ("Skällsord, förolämpande tillmäle ; skrivs även *okvädingsord*",
  "formell, neutral", ["skällsord", "glåpord", "tillmäle", "invektiv"],
  "Han slungade %s efter bilen som körde iväg." % (B % "okvädinsord"),
  None,
  "UPPSLAGNING OFULLSTÄNDIG: SO har ingen artikel för ordet — bara SAOL ('glåpord') och synonymer.se. Wiktionary kallar formen *okvädinsord* en stavningsvariant av *okvädingsord*, och SAOL listar båda; det står nu på kortet. Valören satt till neutral: ordet BETECKNAR skällsord men är inte självt ett skällsord — den distinktionen saknades när fältet bara sa `negativ`."),

"omnipotent": ("Allsmäktig, med obegränsad makt", "formell, neutral",
  ["allsmäktig", "allrådande"],
  "Gud beskrivs i klassisk teologi som %s." % (B % "omnipotent"),
  None,
  "UPPSLAGNING OFULLSTÄNDIG: SO saknar artikel för ordet; underlaget är SAOL ('allsmäktig'), synonymer.se och wiktionary, som alla ger samma betydelse. Registret `litterär` ändrat till `formell` — ordet hör hemma i teologi och psykoanalys, inte i skönlitterär stil. Ingen etymologi anges eftersom ingen av de tillgängliga källorna gav en."),

"passpoal": ("Remsa eller snöre som sytts fast som prydnad längs kanten på ett klädesplagg eller en möbel",
  "fackspråklig, neutral", ["kantremsa", "prydnadssnodd", "galon"],
  "Klänningen hade smala %s av nappa längs ärmarna." % (B % "passpoaler"),
  "av franska passepoil, till passer 'dra igenom' och poil 'ludd på tyg'",
  "PRECISERAT. Kortets 'Smal, upphöjd kant' beskriver resultatet men inte vad saken är: enligt SO en påsydd remsa eller ett snöre. SAOL lägger till att den även förekommer på möbler. Registret ändrat från `formell` till `fackspråklig` — det är en sömnadsterm."),

"pro forma": ("Enbart på formella grunder, för syns skull",
  "formell, neutral", ["för formens skull", "för syns skull", "sken-"],
  "En verksamhet som bara %s sorterade under utrikesdepartementet." % (B % "pro forma"),
  "av latin pro fo´rma 'för formens skull'",
  "SO och SAOL stämmer båda med kortet. Exempelmeningen bytt till SO:s egen, som visar den byråkratiska användningen tydligare än kortets mötesexempel. Etymologin tillagd."),

"prångla": ("Sälja eller göra sig av med något tvivelaktigt — nästan alltid *prångla ut* något eller *prångla på* någon något",
  "neutral, negativ", ["schackra", "kursa", "lura på"],
  "Han greps för att ha %s falska sedlar." % (B % "prånglat ut"),
  "till äldre svenska pranga 'schackra'; jfr pracka på",
  "PRECISERAT. Kortets 'Sälja på ohederligt sätt' stämmer, men SO visar att ordet i praktiken alltid bär en partikel: *prångla ut* (falska sedlar, noveller) eller *prångla på* någon något. Utan partikeln är ordet knappt användbart, och det stod inte på kortet. Registret `negativ` saknade stilnivå."),

"samfälld": ("Som utförs eller ägs av flera parter tillsammans ; äv. enhällig",
  "formell, neutral, juridik", ["gemensam", "förenad", "enhällig"],
  "Förslaget möttes av %s kritik." % (B % "samfälld"),
  "fornsvenska samfälder, till samfälla sik 'förena sig; komma överens'",
  "SAKNAD BETYDELSE. SAOL ger 'gemensam; enhällig' och SO:s eget språkprov är *en samfälld kritik mot förslaget* — där betyder ordet enhällig, inte samägd. Kortet hade bara ägandebetydelsen, som är den juridiska (samfällighet, samfällt bo)."),

"semiologi": ("Läran om tecken och deras betydelse — detsamma som semiotik",
  "fackspråklig, neutral, lingvistik", ["semiotik", "teckenlära"],
  "Kursen i %s handlade om hur reklam skapar mening." % (B % "semiologi"),
  "till grekiska semei´on 'tecken' och log´os '(en) lära'",
  "OBELAGT TILLÄGG BORTTAGET. Kortet hade '(medicin) läran om sjukdomssymtom' som en andra betydelse, med synonymerna *symtomlära* och *symtomatologi*. Varken SO eller SAOL känner den betydelsen — SO säger bara 'semiotik'. Betydelsen finns i engelsk och fransk medicinsk terminologi, men enligt valvets källhierarki avgör SO och SAOL vad ordet betyder på svenska i dag. Struken."),

"sibylla": ("Kvinna vars uppgift är att förutsäga kommande händelser — i antiken en sierska knuten till ett orakel",
  "formell, neutral, historia", ["sierska", "spåkvinna", "profetissa"],
  "Kungen rådfrågade den delfiska %s innan slaget." % (B % "sibyllan"),
  "av latin sibyll´a 'spåkvinna; sierska'",
  "SO: 'kvinna med uppgift att göra förutsägelser', SAOL preciserar 'forntida grekisk sierska'. Innehållet stämde. Registret `litterär` ändrat till `formell` med domänen historia — ordet är en historisk term, inte ett stilgrepp. UPPSLAGNING OFULLSTÄNDIG: wiktionary svarade 429."),

"skröplig": ("Som har svag hälsa, orkeslös ; äv. om föremål eller företeelse: svag och dålig",
  "neutral, lätt negativ", ["bräcklig", "orkeslös", "skraltig"],
  "De rodde ut i en gammal %s båt." % (B % "skröplig"),
  "fornsvenska skröpeliker; till svensk dialekt skryp 'odryg; svag'",
  "SAKNAD BETYDELSE. SO markerar *äv. om föremål* (en gammal skröplig båt) och *äv. om abstrakt företeelse*. Kortet hade bara hälsobetydelsen, och dess exempel handlade också bara om en människa. Registret `negativ` saknade stilnivå och var dessutom för starkt: att kalla någon skröplig är beskrivande och medlidsamt, inte nedsättande."),

"slimmad": ("Figursydd, tätt åtsittande ; bildligt: nedbantad och mer effektiv, om en organisation eller verksamhet",
  "neutral, neutral", ["figursydd", "insvängd", "nedbantad"],
  "Ledningen ville skapa en %s organisation." % (B % "slimmad"),
  "av engelska slimmed, till slim 'smal'",
  "SAKNAD BETYDELSE. SO markerar *äv. bildligt* med språkproven *en slimmad förvaltning*, *skapa en slimmad organisation*. Kortet hade bara klädbetydelsen. Den bildliga är den man möter i affärs- och nyhetstext och är svårare att gissa sig till."),

"subvention": ("Ekonomiskt understöd, ofta men inte nödvändigtvis från staten",
  "formell, neutral, ekonomi", ["bidrag", "understöd", "prisstöd"],
  "%s till jordbruket skars ned." % (B % "Subventionerna"),
  "av franska subvention; till latin subveni´re 'bistå'",
  "PRECISERAT. SO skriver '(statligt) ekonomiskt understöd' — parentesen betyder att statligt är det vanliga men inte en del av definitionen. Kortets 'Statligt ekonomiskt stöd' gjorde det till ett villkor, vilket utesluter t.ex. EU-subventioner och korssubventionering inom ett företag."),

"suterräng": ("Våning som helt eller delvis ligger under markytan, oftast i en sluttning",
  "neutral, neutral, teknik", ["källarvåning", "sluttningsvåning"],
  "Tvättstugan låg i %s." % (B % "suterrängen"),
  "av franska souterrain, till sous 'under' och terräng",
  "SO: 'våning helt eller delvis under jordytan'. Innehållet stämde. Sluttningen tillagd eftersom det är den som skiljer en suterrängvåning från en vanlig källare — den har fönster i markplan på ena sidan. Etymologin ('under marken') tillagd."),

"säter": ("Fäbod, fäbodvall — plats dit boskapen fördes för sommarbete",
  "neutral, neutral, jordbruk", ["fäbod", "fäbodvall", "betesvall"],
  "Boskapen fördes till %s så snart snön hade gått bort." % (B % "sätern"),
  "fornsvenska säter, ursprungligen 'uppehållsort'; besläktat med sitta",
  "TVÅ OBELAGDA PÅSTÅENDEN BORTTAGNA. Kortet skrev 'Fäbod i fjällen' — varken SO ('fäbod') eller SAOL ('fäbodvall') begränsar ordet till fjällen; fäbodar fanns i hela skogsbygden. Registret `dialektal` ströks av samma skäl: ingen av källorna markerar det. Etymologin visar att ordet betydde 'uppehållsort', besläktat med *sitta* — därav alla ortnamn på -säter."),

"tangera": ("Om linje eller plan: röra vid en kurva i en punkt utan att skära den ; snudda vid, lätt vidröra ; bildligt: gränsa till, antydningsvis beröra ; uppnå ett resultat som är exakt likvärdigt med ett tidigare",
  "neutral, neutral", ["snudda vid", "gränsa till", "vara tangent till"],
  "Han %s världsrekordet på hundra meter." % (B % "tangerade"),
  "av latin tan´gere 'vidröra'; jfr intakt, kontakt, takt, taxera",
  "FELAKTIG BETYDELSE RÄTTAD, och det är den allvarligaste i batchen. Kortet skrev 'nästan nå (t.ex. ett rekord)' och exemplifierade med *Löpningen tangerade nästan hans personbästa*. SO säger raka motsatsen: 'uppnå resultat som är exakt likvärdigt med' — att tangera ett rekord är att TANGERA det, alltså nå exakt samma siffra, inte att komma i närheten. Kortet lärde ut fel. Dessutom saknades den matematiska grundbetydelsen (tangent), som är den som förklarar alla de andra."),

"träl": ("Person som berövats rätten att bestämma över sig själv och tvingas arbeta åt någon annan, särskilt i det forntida Norden ; bildligt: någon som är tvingad till mycket hårt arbete eller starkt beroende av något",
  "neutral, neutral, historia", ["slav", "ofri"],
  "Han levde som en %s under sitt spelberoende." % (B % "träl"),
  "fornsvenska þräl; nordiskt ord av osäkert ursprung",
  "TVÅ FEL. (1) Kortet skrev 'Livegen slav' — livegenskap är en annan rättslig institution, där den ofrie är bunden till jorden men inte ägd som lös egendom. SO säger 'berövats rätten att bestämma över sig själv'. (2) 'under medeltiden' — SAOL placerar trälen *särsk. i det forntida Norden*, alltså vikingatiden; träldomen avskaffades i Sverige 1335. Dessutom saknades den bildliga betydelsen (*syndens träl*, *en träl under lasten*), som är den enda levande i dag."),

"utopist": ("Person som hyser utopiska idéer om ett idealsamhälle",
  "neutral, lätt negativ", ["drömmare", "idealist", "visionär"],
  "Han avfärdades som en naiv %s av sina kollegor." % (B % "utopist"),
  None,
  "SO: 'person som hyser utopiska idéer'. Innehållet stämde. Registret `formell` ströks — ordet används i vanlig debatt. Valören `lätt negativ` tillagd: ordet är oftast en avfärdning, vilket SO:s eget språkprov (*Fourier, en av de stora utopisterna*) inte visar men den vanliga användningen gör. Ingen etymologi anges — SO ger ingen för avledningen."),

"viskös": ("Som har hög viskositet, trögflytande",
  "fackspråklig, neutral, fysik", ["trögflytande", "seg", "tjockflytande"],
  "Sirapen var så %s att den knappt rann ur flaskan." % (B % "viskös"),
  None,
  "SO: 'som har stor viskositet', SAOL: 'seg; trögflytande'. Innehållet stämde. Registret ändrat från `formell` till `fackspråklig` med domänen fysik — ordet är en fysikalisk term, inte ett byråkratiskt ordval. SO ger ingen etymologi."),
}

# Framsidan på ett kort är felstavad och måste rättas separat: applicera rör
# bara baksidan. Se patch_v3_20260810_framsida.py.
FRAMSIDA_RATTAS = {"in media res": "in medias res"}


def main():
    d = json.load(open(FIL, encoding="utf-8"))
    kort = d["kort"] if isinstance(d, dict) and "kort" in d else d
    n = 0
    saknas = []
    for e in kort:
        r = R.get(e["ord"])
        if not r:
            saknas.append(e["ord"])
            continue
        hb, reg, syn, ex, etym, slutsats = r
        e["proposed"] = {"huvudbetydelse": hb, "register": reg, "synonymer": syn,
                         "synonym_groups": None, "exempelmening": ex,
                         "etymologi": etym}
        e["sokkoll"] = {"kalla": kalla(e["ord"]), "slutsats": slutsats}
        e["approved"] = True
        e.pop("applicerad", None)
        n += 1
    json.dump(d, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("skrev förslag för %d av %d kort" % (n, len(kort)))
    if saknas:
        print("UTAN FÖRSLAG: %s" % ", ".join(saknas))
    else:
        print("alla kort har förslag.")


if __name__ == "__main__":
    main()
