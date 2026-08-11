# -*- coding: utf-8 -*-
"""v3-omgranskning av 50 kort ur is:new, 2026-08-11 batch 1.

Andra batchen med BRUK-raden. **Fjorton av 50 ord** har en uttrycklig
stilmarkering i SO — mot elva i går. Utgångsläget var återigen `formell`:
**27 av 50 kort** (54 %).

    furste       mest historiskt        kortet sa: litterär
    resolvera    något ålderdomligt     kortet sa: formell
    betuttad     vardagligt; något nedsättande   kortet sa: vardaglig, POSITIV
    bliga        vard.                  kortet sa: vardaglig, negativ  (rätt)
    catgut       delvis historiskt      kortet sa: formell
    endräkt      något högtidligt       kortet sa: litterär
    förpakta     åld.                   kortet sa: formell
    försträcka   något ålderdomligt     kortet sa: formell
    gällen       prov.; åld.            kortet sa: formell
    hiva         särsk. sjö.            kortet sa: vardaglig
    lumpen       vard.                  kortet sa: negativ ; vardaglig
    rangera      mindre brukligt        kortet sa: formell
    echaufferad  något högtidligt       kortet sa: formell
    emedan       något formellt         kortet sa: litterär

## Innehållsfel (7 substantiella)

  socialisera   TVÅ FEL I ETT KORT. Kortet: "lära sig ett samhälles normer ;
                umgås". SO:s FÖRSTA betydelse är 'överföra i samhällets ägo',
                alltså förstatliga — den saknades helt. Och "umgås" är engelskans
                *socialize*; SO har den inte.
  resolvera     ANGLICISM. Kortet: "lösa ett problem". SO ger 'besluta' och
                'officiellt meddela'. Att lösa ett problem är engelskans
                *resolve*, inte svenskans resolvera.
  försträcka    OBELAGD BETYDELSE. Kortet: "skada en muskel". Varken SO eller
                SAOL har den; båda ger bara penningbetydelsen.
  formidabel    ETYMOLOGI SOM BETYDELSE. Kortet: "(ålderdomligt) fruktansvärd
                och skräckinjagande". SO:s andra betydelse är 'mycket svår'.
                Skräcken sitter i ordets ursprung (latin *formidare* 'frukta'),
                inte i dess svenska betydelse. Samma fel som *oratorium*
                ("bönsal") i går.
  eldprov       FEL LED SOM HUVUDBETYDELSE. Kortet inledde med gudsdomen med
                glödande järn. SO markerar den som *ursprungligen* — alltså
                etymologi. Huvudbetydelsen är 'avgörande, svårt prov'.
  beklagligtvis OBEGRIPLIG TEXT. Kortet: "Tyvärr, till leda". "Till leda"
                betyder 'ända till utleda' och hör inte hemma här alls.
  sarv          FEL MÄRKNING. Kortet kallade renbetydelsen "dialektal". SO har
                två skilda uppslagsord: ett samiskt lån (*sarves*, hanren) och
                ett svenskt dialektord (karpfisken). Det är homografer, inte en
                huvudbetydelse med en dialektal bibetydelse.

Plus fem saknade bibetydelser: furste ('djävulen', som i *mörkrets furste*),
kråma sig ('bete sig inställsamt'), restituera ('betala tillbaka'), lumpen
('obetydlig' + 'kasserade textilvaror'), stadgad ('mogen, sansad').

## Misslyckade uppslagningar

  ha skygglappar  frasen föll tillbaka på fritextsökning och gav artiklarna för
                  *ha* och *torr*. Slogs om under **skygglappar**, där SO ger
                  både den bokstavliga betydelsen och markeringen *ofta bildligt
                  i uttryck för vägran att inse något*.
  förpakta        ingen SO-artikel; bara SAOL ('arrendera ut', åld.).
  beklagligtvis / lättledd / vördnad   ingen SAOL-artikel.

## Synonymfältet — gårdagens svaga punkt

Blindgranskaren fällde fem kort i går enbart på synonymer. Två regler tillämpas
därför här: **inga överordnade begrepp** (en malakit är inte synonym med
"kopparmineral") och **ingen ordklassblandning** (ett substantiv kan inte vara
synonym till ett adjektiv). Dessutom har synonymer.se-listorna ett skräpvärde,
"tillbaka i grottekvarnen", som är sidnavigering och inte ett ord — det är
bortsorterat.
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HAR = os.path.dirname(os.path.abspath(__file__))
FIL = os.path.join(HAR, "sessions", "session_2026-08-11_v3-omgranskning-nya.json")
B = '<font color="#3498db">%s</font>'


def kalla(o):
    import urllib.parse
    q = urllib.parse.quote(o)
    return ("https://svenska.se/api/msearch?ord=%s "
            "https://www.synonymer.se/sv-syn/%s "
            "https://sv.wiktionary.org/wiki/%s" % (q, q, q))


R = {
"eldprov": ("Avgörande och svårt prov", "neutral, neutral",
  ["prövning", "pärs", "avgörande prov"],
  "Premiären blev ett %s för hela ensemblen." % (B % "eldprov"),
  "ursprungligen om gudsdom: den anklagade skulle bevisa sin oskuld genom att gå genom eld utan att brännas",
  "FEL LED SOM HUVUDBETYDELSE. Kortet inledde med 'prov med glödande järn som skulle bevisa oskuld'. SO markerar den betydelsen som *ursprungligen* — den är alltså ordets historia, inte vad det betyder i dag. Huvudbetydelsen enligt både SO och SAOL är 'avgörande, svårt prov'. Gudsdomen har flyttats till etymologiraden, där den hör hemma och fortfarande gör ordet minnesvärt."),

"agglomerera": ("Hopa samman delar till en enda massa eller kropp",
  "fackspråklig, neutral, teknik", ["hopa", "koncentrera", "gyttra ihop"],
  "Partiklarna %s till större klumpar." % (B % "agglomererade"),
  "se ursprung till agglomerat",
  "SO: 'hopa samman delar till en massa el. kropp', med två fackmarkeringar — *spec. sociologi* om bebyggelse och *spec. teknik* om träfibrer. Innehållet stämde. Registret ändrat från `formell` till `fackspråklig`: ordet förekommer inte utanför facktext."),

"botanisera": ("Samla in och undersöka växter ; bildligt: leta och välja bland ett större utbud",
  "neutral, neutral", ["samla växter", "leta", "ströva bland"],
  "Han %s bland antikvariatets hyllor." % (B % "botaniserade"),
  None,
  "Båda SO-betydelserna fanns redan — den bildliga är markerad *ofta bildligt* och är den man oftast möter. Preciserat att det bildliga inte bara är att strosa utan att *välja bland* (SO: 'välja (bland), undersöka'). Registret `formell` ströks."),

"furste": ("Person i regentställning, särskilt över ett furstendöme ; äv. om medlem av regentfamilj ; i uttrycket *mörkrets furste*: djävulen",
  "ngt ålderdomlig, neutral, historia", ["regent", "monark", "härskare"],
  "Mörkrets %s frestade honom." % (B % "furste"),
  "fornsvenska förste; av lågtyska vurste, eg. 'den förste'; jfr först",
  "SAKNAD BETYDELSE + REGISTER. SO ger tre skikt och kortet hade två; det som saknades är 'djävulen', som lever kvar i *mörkrets furste*. Registret sattes utifrån SO:s `bruklighetskommentar` **mest historiskt** och SAOL:s 'mest i äldre tid' — kortet sa `litterär`. Etymologin visar att en furste helt enkelt var 'den förste'."),

"ha skygglappar": ("Vägra se annat än sitt eget perspektiv",
  "neutral, negativ", ["vara trångsynt", "blunda för verkligheten"],
  "Ledningen %s och missade hela marknadsskiftet." % (B % "hade skygglappar"),
  "skygglappar är de utstående lappar på ett betsel som hindrar hästen från att se åt sidan; efter tyska Scheuklappe",
  "UPPSLAGNING MISSLYCKADES FÖRST. Sökning på hela frasen fick svenska.se att falla tillbaka på fritextsökning och returnera artiklarna för *ha* och *torr*. Ordet slogs om under **skygglappar**, där SO ger den bokstavliga betydelsen och markerar *ofta bildligt i uttryck för vägran att inse något*. Innehållet stämde; registret saknade stilnivå. Bilden bakom uttrycket står nu på etymologiraden."),

"kråma sig": ("Stolt och kokett vrida på kroppen för att visa upp sig ; äv. bete sig inställsamt",
  "neutral, lätt negativ", ["stoltsera", "brösta sig", "göra sig till"],
  "Han %s framför spegeln." % (B % "kråmade sig"),
  "jfr svensk dialekt krumma 'kröka'; nära besläktat med krum",
  "SAKNAD BETYDELSE. SO ger utöver poserandet även 'bete sig inställsamt' — att kråma sig FÖR någon. Kortet hade bara den första. Registret `skämtsam` var en valör utan stilnivå; båda axlarna skrivs nu ut, och valören är lätt negativ snarare än skämtsam: den som kråmar sig beskrivs med ett visst förakt."),

"matrona": ("Äldre, ofta fyllig och värdig gift kvinna", "neutral, skämtsam",
  ["husmoder", "äldre dam"],
  "Hon tronade vid bordsänden som en riktig %s." % (B % "matrona"),
  "av latin matro´na 'husfru', till ma´ter 'moder'; besläktat med matris",
  "SO: 'äldre (gift) kvinna', SAOL preciserar 'fyllig och värdig'. Innehållet stämde. SO ger ingen `bruklighetskommentar`, så `litterär` ströks som obelagt — men valören `skämtsam` behålls, eftersom SAOL:s 'fyllig' och synonymernas 'kraftig äldre dam' visar att ordet inte är neutralt beskrivande."),

"ouvertyr": ("Inledande orkesterstycke till en opera eller ett större verk ; äv. fristående konsertstycke ; bildligt: upptakt",
  "formell, neutral, musik", ["inledningsstycke", "förspel", "preludium"],
  "Kvällens %s var av Rossini." % (B % "ouvertyr"),
  "av franska ouverture 'början', till ouvrir 'öppna'",
  "SAKNAD BETYDELSE. SO ger tre: operaouvertyren, den fristående konsertouvertyren och den bildliga upptakten (*ouvertyren till kriget*). Kortet hade bara den första. Etymologin ('öppna') binder ihop alla tre."),

"resolvera": ("Besluta eller bestämma ; äv. officiellt meddela ett beslut",
  "ngt ålderdomlig, neutral", ["besluta", "bestämma", "avgöra"],
  "Styrelsen %s att ärendet skulle bordläggas." % (B % "resolverade"),
  "via tyska av latin resol´vere 'upplösa', dvs. upplösa varje tvivel; jfr resolut, absolut",
  "ANGLICISM BORTTAGEN. Kortets första betydelse var 'lösa ett problem' — det är engelskans *resolve*. SO ger 'besluta' och 'officiellt meddela'; svenskan har inte lösningsbetydelsen. Registret sattes utifrån SO:s `bruklighetskommentar` **något ålderdomligt**; kortet sa `formell`. Etymologin förklarar bron: att resolvera är att lösa upp tvivlet genom ett beslut."),

"restituera": ("Återställa i rätt skick ; äv. betala tillbaka",
  "formell, neutral, ekonomi", ["återställa", "återbetala", "återlämna"],
  "Beloppet %s till köparen." % (B % "restituerades"),
  "av latin restitu´ere 'återställa'; jfr konstituera, statuera",
  "SAKNAD BETYDELSE. SO ger två och markerar den andra *spec. ekonomi*: att betala tillbaka, som i restituerad tull eller skatt. Kortet hade bara 'återställa, ge tillbaka' och missade därmed den användning man faktiskt möter i text."),

"socialisera": ("Överföra i samhällets ägo eller under samhällets kontroll ; äv. fostra någon in i ett samhälles normer",
  "formell, neutral, politik", ["förstatliga", "nationalisera", "fostra in"],
  "Regeringen ville %s bankerna." % (B % "socialisera"),
  "till social",
  "TVÅ FEL I SAMMA KORT. (1) SO:s FÖRSTA betydelse är 'överföra i samhällets ägo eller ställa under samhällets kontroll' — alltså förstatliga, ordets politiska huvudbetydelse. Den saknades helt på kortet. (2) Kortets andra betydelse, 'umgås', är engelskans *socialize*; varken SO eller SAOL har den på svenska. Struken. Kvar blir SO:s andra betydelse, 'uppfostra och anpassa till visst beteendemönster', som kortet hade i formen 'lära sig ett samhälles normer'."),

"stadgad": ("Fastställd i lag eller föreskrift ; äv. om person: stadig, mogen och sansad",
  "formell, neutral", ["fastställd", "föreskriven", "sansad"],
  "Avgiften är %s i förordningen." % (B % "stadgad"),
  "fornsvenska staþhga; till stadga",
  "SAKNAD BETYDELSE. SAOL ger både 'föreskriva' och 'göra stadig', och synonymlistan bekräftar den andra sidan: *mogen, sansad, stadig*. Kortet hade bara den juridiska. Skillnaden syns i *stadgad avgift* mot *en stadgad karl*."),

"tiptop": ("I bästa skick, av högsta klass", "vardaglig, positiv",
  ["förstklassig", "perfekt", "finfin"],
  "Lägenheten var i %s skick." % (B % "tiptop"),
  "av engelska tiptop; till tipp och topp",
  "SO: 'som är av högsta klass eller i bästa skick'. Innehållet stämde, liksom registret. Etymologin tillagd — ordet är ett engelskt lån och stavas även *tipptopp*, vilket SAOL noterar."),

"antibiotika": ("Läkemedel som dödar eller hämmar bakterier",
  "fackspråklig, neutral, medicin", ["bakteriedödande medel", "penicillin"],
  "Läkaren skrev ut %s mot infektionen." % (B % "antibiotika"),
  "modern bildning till anti- och grekiska bi´os 'liv'; jfr biologi",
  "SO: 'ämne som dödar eller hämmar bakterier'. Innehållet stämde. Värt att notera att *antibiotika* är plural — singularformen är **antibiotikum**, vilket SAOL anger och kortet inte nämnde. Etymologin ('mot liv') tillagd."),

"autonom": ("Som har hög grad av oberoende och styr sig själv ; äv. om fordon: som kan framföras utan förare",
  "neutral, neutral", ["självständig", "oberoende", "självstyrande"],
  "En %s region med eget parlament." % (B % "autonom"),
  "av grekiska auton´omos 'självstyrande'; till auto- och nom´os 'sed; lag'",
  "SAKNAD BETYDELSE. SO ger flera skikt, och det som saknades är det som ordet numera oftast används om: **självkörande fordon** (SAOL: 'självkörande'). SO:s politiska betydelse preciseras dessutom som *begränsat* självbestämmande — en autonom region är inte självständig. Registret `formell` ströks."),

"aviarium": ("Stor flygbur eller byggnad för fågelhållning",
  "fackspråklig, neutral, biologi", ["fågelhus", "voljär"],
  "Djurparkens nya %s rymmer trettio arter." % (B % "aviarium"),
  "av latin avia´rium, till av´is 'fågel'",
  "SO: 'stor flygbur för fåglar', med tillägget *äv. om anläggning för fågelhållning i större skala*. Innehållet stämde. Registret ändrat till fackspråklig — ordet förekommer i praktiken bara i djurpark- och zoologisammanhang."),

"beklagligtvis": ("Vilket är beklagligt — tyvärr", "formell, lätt negativ",
  ["tyvärr", "dessvärre", "olyckligtvis"],
  "%s kunde ärendet inte behandlas i tid." % (B % "Beklagligtvis"),
  None,
  "OBEGRIPLIG TEXT BORTTAGEN. Kortet löd 'Tyvärr, till leda'. *Till leda* betyder 'ända till utleda' och har ingenting med ordet att göra — det ser ut som en avhuggen eller hopblandad rad. SO ger 'vilket är beklagligt'. UPPSLAGNING OFULLSTÄNDIG: SAOL saknar artikel för ordet."),

"betryckt": ("Som känner djup nedstämdhet ; äv. om något som vållar nedstämdhet",
  "formell, negativ", ["nedstämd", "beklämd", "modfälld"],
  "Stämningen var %s efter beskedet." % (B % "betryckt"),
  None,
  "SO ger två riktningar: den som ÄR nedstämd och det som VÅLLAR nedstämdhet (*betryckta omständigheter*). Kortet hade bara den första. Synonymen *förtvivlad* ströks — den är för stark; SO:s ord är 'nedstämd', inte förtvivlad. Registret `negativ` saknade stilnivå."),

"betuttad": ("Förtjust i någon, vanligen med erotisk innebörd",
  "vardaglig, lätt negativ", ["förtjust i", "betagen", "förälskad"],
  "Han var alldeles %s i grannflickan." % (B % "betuttad"),
  "svensk dialekt betuttad 'förlägen; rådvill'; av oklart ursprung",
  "VALÖREN VAR FEL ÅT ANDRA HÅLLET. Kortet sa `positiv`. SO:s `bruklighetskommentar` lyder **vardagligt; något nedsättande** — att kalla någon betuttad är att göra sig lite lustig över förälskelsen. Kortets andra betydelse ('förlägen och rådvill') är inte en svensk bibetydelse utan ordets DIALEKTALA URSPRUNG; den har flyttats till etymologiraden."),

"bliga": ("Titta ihållande och på ett dumt sätt, oftast på en person",
  "vardaglig, negativ", ["glo", "stirra", "blänga"],
  "Sluta %s på folk." % (B % "bliga"),
  "fornsvenska bligha; till en germansk ordstam med betydelsen 'glänsa'",
  "SO: 'titta ihållande, vanligen på en person och på ett dumt sätt'. Innehåll och register stämde båda — registret bekräftat mot SO:s `bruklighetskommentar` **vard.** Preciserat att det dumma ligger i ordet, inte bara varaktigheten; det är skillnaden mot att bara titta länge."),

"catgut": ("Kirurgisk sytråd, ofta tillverkad av fårtarm",
  "ngt ålderdomlig, neutral, medicin", ["kirurgisk sytråd", "tarmsträng"],
  "Såret syddes med %s." % (B % "catgut"),
  "av engelska catgut, till cat 'katt' och gut 'tarm' — trots namnet aldrig av katt",
  "REGISTER RÄTTAT. SO:s `bruklighetskommentar` lyder **delvis historiskt** och SAOL skriver 'förr anv. inom medicinen' — kortet sa `formell`. Materialet är i stort sett utfasat. Etymologin tillagd med sin motsägelse: ordet betyder 'kattarm' men materialet kom från får och get."),

"debitera": ("Påföra någon en kostnad", "formell, neutral, ekonomi",
  ["fakturera", "påföra", "belasta"],
  "Konsulten %s tio timmar." % (B % "debiterade"),
  "av franska débiter 'anteckna som skuld'; till latin de´bitum 'skuld'",
  "SO: 'påföra (någon) en kostnad'. Innehållet stämde. Motsatsen **kreditera** framgår av synonymer.se och är värd att känna till som par. Etymologin ('skuld') tillagd."),

"detaljhandel": ("Handel med varor för försäljning direkt till slutkonsumenter, vanligen i små kvantiteter",
  "formell, neutral, ekonomi", ["minuthandel", "återförsäljning"],
  "%s står för en tredjedel av branschens omsättning." % (B % "Detaljhandeln"),
  None,
  "SO: 'handel med varor för försäljning till de slutliga konsumenterna'. Innehållet stämde. Preciserat att det gäller små kvantiteter (SO:s eget tillägg) — det är kvantiteten och slutkunden tillsammans som skiljer detaljhandel från **partihandel**, som är motsatsen."),

"echaufferad": ("Varm och röd i ansiktet, oftast av stark sinnesrörelse",
  "högtidlig, neutral", ["upphettad", "röd i ansiktet", "upphetsad"],
  "Han kom in %s efter grälet." % (B % "echaufferad"),
  "till franska échauffer 'värma'; jfr chaufför, kalfaktor",
  "PRECISERAT. Kortet sa 'upphetsad eller uppvärmd', vilket missar var värmen syns: SO säger **varm och röd i ansiktet**, vanligen p.g.a. sinnesrörelse. Registret sattes utifrån SO:s `bruklighetskommentar` **något högtidligt**; kortet sa `formell`. Etymologin binder ihop ordet med *chaufför* — den som eldade."),

"emedan": ("Av den orsaken att — eftersom", "formell, neutral",
  ["eftersom", "därför att", "alldenstund"],
  "Mötet ställdes in %s ordföranden var sjuk." % (B % "emedan"),
  "fornsvenska ä mäþan, till ä 'alltid' och medan",
  "SO: 'av den orsaken att'. Innehållet stämde. Registret sattes utifrån SO:s `bruklighetskommentar` **något formellt** — kortet sa `litterär`, vilket antyder skönlitterär stil; ordet hör snarare hemma i myndighetstext och juridik. Etymologin är upplysande: *emedan* betydde ursprungligen 'alltid medan', alltså en tidsangivelse som glidit över i orsak."),

"endräkt": ("Enighet och sämja", "högtidlig, positiv",
  ["enighet", "sämja", "samförstånd"],
  "Efter förhandlingen rådde %s i gruppen." % (B % "endräkt"),
  "av lågtyska endracht, till over en dragen 'vara ense', eg. 'bära jämnt'; jfr dra, dräkt",
  "SO och SAOL är eniga. Innehållet stämde. Registret sattes utifrån SO:s `bruklighetskommentar` **något högtidligt** — kortet sa `litterär`. Etymologin är fin och gör ordet minnesvärt: att dra jämnt, alltså bära bördan lika."),

"etologi": ("Läran om djurens beteende och orsakerna till det",
  "fackspråklig, neutral, biologi", ["beteendelära"],
  "Han forskar i %s vid universitetet." % (B % "etologi"),
  "till grekiska eth´os 'sed, vana' och log´os '(en) lära'",
  "SO: 'läran om djurens beteende och orsakerna till det'. Innehållet stämde. Kortets synonym *beteendevetenskap* ströks — den är ett **överordnat** begrepp som även omfattar människan, och blindgranskaren fällde i går fyra kort på just den sortens synonym. Registret ändrat till fackspråklig med domänen biologi."),

"formidabel": ("Mycket stor och imponerande ; äv. mycket svår",
  "formell, neutral", ["kolossal", "imponerande", "väldig"],
  "Uppgiften var %s men inte omöjlig." % (B % "formidabel"),
  "av franska formidable 'fruktansvärd; imponerande'; av latin formida´re 'frukta'",
  "ETYMOLOGI SOM BETYDELSE. Kortet gav 'fruktansvärd och skräckinjagande' som en ålderdomlig bibetydelse. SO:s andra betydelse är 'mycket **svår**'. Skräcken sitter i ordets ursprung — latinets *formidare*, 'frukta' — inte i dess svenska betydelse, och den står nu på etymologiraden. Det är samma fel som *oratorium* ('bönsal') i gårdagens batch, och nu tredje gången jag gör det."),

"förpakta": ("Arrendera ut mark eller en verksamhet mot ersättning",
  "arkaisk, neutral", ["arrendera ut"],
  "Godset %s till en storbonde." % (B % "förpaktades"),
  None,
  "UPPSLAGNING OFULLSTÄNDIG: SO saknar artikel för ordet; underlaget är SAOL ('arrendera ut') och synonymer.se, som hänvisar vidare till *arrendera*. Registret sattes utifrån SAOL:s markering **åld.** — kortet sa `formell`. Ordet är i praktiken ute ur bruk och möts bara i historisk text."),

"försträcka": ("Låna ut pengar eller andra värden mot skyldighet att lämna tillbaka lika mycket av samma slag",
  "ngt ålderdomlig, neutral, ekonomi", ["låna ut", "förskottera"],
  "Han %s henne tusen kronor till hyran." % (B % "försträckte"),
  "av lågtyska vorstrecken 'sträcka fram'",
  "OBELAGD BETYDELSE BORTTAGEN. Kortets andra betydelse, 'skada en muskel', finns varken i SO eller SAOL — båda ger uteslutande penningbetydelsen. Preciserat vad SO faktiskt säger, och det är en juridiskt viktig nyans: låntagaren ska lämna tillbaka *lika mycket av samma slag*, inte samma föremål. Registret sattes utifrån SO:s `bruklighetskommentar` **något ålderdomligt**."),

"gällen": ("Halvsur — om mjölk och mjölkprodukter som börjat surna",
  "dialektal, lätt negativ", ["halvsur", "surnad"],
  "Mjölken smakade %s." % (B % "gällen"),
  "svensk dialekt gällen; ev. till galla",
  "REGISTER RÄTTAT. Kortet sa `formell` och skrev in dialektaliteten i själva definitionstexten i stället för i registerfältet — alltså rätt information på fel plats, där varken lint eller statistik hittar den. SO:s `bruklighetskommentar` är **prov.** och SAOL:s **åld.** Registret är nu `dialektal`, och definitionen har renodlats."),

"gästspel": ("Tillfälligt framträdande av en artist utanför sin egen scen ; bildligt: kort och tillfällig insats i vilket sammanhang som helst",
  "neutral, neutral", ["inhopp", "tillfälligt engagemang"],
  "Hans tid som minister blev ett kort %s." % (B % "gästspel"),
  None,
  "Båda SO-betydelserna fanns redan. Preciserat att den bokstavliga betydelsen även gäller en annan scen på hemorten än den man är fast engagerad vid — det är SO:s egen avgränsning. Exemplet bytt till den bildliga användningen, som är den man oftast möter i tidningstext. Registret `formell` ströks."),

"helgjuten": ("Gjuten i ett enda stycke ; bildligt: som utgör en väl avvägd, harmonisk helhet",
  "formell, positiv", ["gedigen", "enhetlig", "helstöpt"],
  "En %s insats av hela laget." % (B % "helgjuten"),
  None,
  "SAKNAD BETYDELSE. SO ger den bokstavliga gjutbetydelsen först och markerar den harmoniska som *särskilt bildligt*. Kortet hade bara den bildliga ('solid och väl sammanhållen') — vilket gör ordet svårare att minnas, eftersom det är gjutbilden som förklarar det. Synonymen *solid* ströks: den beskriver hållfasthet, inte harmoni."),

"hiva": ("Förflytta tyngre last med en svängande rörelse ; vardagligt: kasta eller slänga",
  "neutral, neutral, sjöfart", ["vinda upp", "hissa", "slänga"],
  "De %s ombord de sista säckarna." % (B % "hivade"),
  "svensk dialekt hiva; av engelska heave; samma ord som häva",
  "Båda betydelserna fanns redan. SO:s `bruklighetskommentar` är **särsk. sjö.**, vilket kortet inte visade — domänen `sjöfart` är nu satt. Preciserat att grundbetydelsen inbegriper svängrörelsen och ofta en vinsch; det är den som skiljer *hiva* från att bara lyfta."),

"infiltration": ("Omärkligt eller gradvis inträngande av främmande element — i en organisation, en organism eller i marken",
  "formell, neutral", ["inträngning", "innästling"],
  "%s av regnvatten i marken tar flera dygn." % (B % "Infiltration"),
  "till infiltrera",
  "SAKNAD BETYDELSE. SO ger tre användningar: organisationen (ofta bildligt, i syfte att spionera), organismen (medicinskt) och **vattnets nedträngande i marken** — den sista är en hydrologisk fackterm som kortet inte hade. Kortet nämnde två av tre."),

"lumpen": ("Som handlar taktlöst och svekfullt, gemen ; äv. obetydlig ; som substantiv, vardagligt: värnplikten",
  "neutral, negativ", ["gemen", "usel", "tarvlig"],
  "Det var ett %s sätt att behandla en vän." % (B % "lumpet"),
  "av tyska Lumpen- 'ynklig'; till lump",
  "SAKNAD BETYDELSE. SO ger flera skikt; kortet hade det gemena och värnplikten men missade **'obetydlig'** (*en lumpen slant*), som är en helt annan sorts nedvärdering — inte moralisk utan storleksmässig. SO:s `bruklighetskommentar` **vard.** gäller värnpliktsbetydelsen, inte adjektivet; därför står stilnivån som neutral med den vardagliga användningen utskriven i definitionen."),

"lättledd": ("Som alltför lätt låter sig påverkas, ofta i fel riktning",
  "neutral, lätt negativ", ["lättpåverkad", "osjälvständig", "eftergiven"],
  "En %s ung man i fel sällskap." % (B % "lättledd"),
  None,
  "PRECISERAT. Kortet sa 'lätt att påverka eller övertala', vilket låter neutralt. SO lägger till två saker som ändrar tonen: *alltför* lätt, och *ofta i fel riktning*. Ordet är alltså inte beskrivande utan värderande, och valören saknades helt. UPPSLAGNING OFULLSTÄNDIG: SAOL saknar artikel."),

"pejorativ": ("Nedsättande — om ord eller tonfall ; äv. som substantiv: ett ord med nedsättande innebörd",
  "fackspråklig, neutral, lingvistik", ["nedsättande", "förklenande", "nedvärderande"],
  "Ordet används numera nästan alltid %s." % (B % "pejorativt"),
  "bildning till latin pei´or 'sämre'",
  "SAKNAD ORDKLASS. SO ger både adjektivet och substantivet ('ord med nedsättande innebörd'). Kortet hade bara adjektivet. Valören satt till neutral: *pejorativ* BETECKNAR nedsättande språk men är självt en neutral språkvetenskaplig term — samma distinktion som gjordes för *invektiv* och *okvädinsord*."),

"pläd": ("Mindre, lättare filt som används utan lakan, särskilt vid vila dagtid",
  "neutral, neutral", ["filt", "resfilt"],
  "Hon drog %s över benen i soffan." % (B % "plädet"),
  "av engelska plaid; identiskt med iriska ploid 'filt'",
  "PRECISERAT. Kortets 'mjuk, lätt filt' missar det som faktiskt definierar en pläd enligt SO: att den används **utan mellanliggande lakan**, särskilt vid annan vila än nattsömn. Det är därför man har pläd i soffan och filt i sängen. Registret `vardaglig` ströks."),

"rakryggad": ("Rak i ryggen ; bildligt: ärlig och karaktärsfast",
  "neutral, positiv", ["principfast", "karaktärsfast", "hederlig"],
  "Hon var %s nog att erkänna misstaget." % (B % "rakryggad"),
  None,
  "Båda SO-betydelserna fanns i sak. Den bokstavliga har lagts till uttryckligen — den är förutsättningen för bilden, och SO markerar dessutom att ordet *någon gång* används om möbler. Registret `positiv` saknade stilnivå."),

"rangera": ("Placera järnvägsvagnar i viss ordning ; äv. hänföra något till en viss grupp eller plats på en skala",
  "neutral, neutral, teknik", ["växla", "ordna", "inordna"],
  "Vagnarna %s på bangården." % (B % "rangerades"),
  "av franska ranger; till rang; jfr derangera",
  "PRECISERAT. Kortet sa 'ordna i en viss ordning ; flytta godsvagnar' — men järnvägsbetydelsen är SO:s **första** och mest levande, medan den allmänna ordningsbetydelsen bär SO:s `bruklighetskommentar` **mindre brukligt**. Ordningen är alltså omvänd mot kortets. Etymologin kopplar ordet till *rang* och *derangera*."),

"residera": ("Ha sin bostad eller sina lokaler på en viss plats — vanligen om betydelsefull person eller ståndsmässig bostad",
  "formell, neutral", ["ha sitt residens", "bo", "vistas"],
  "Landshövdingen %s på slottet." % (B % "residerar"),
  "av latin reside´re 'bli sittande; bosätta sig'; jfr presidera, konservera",
  "PRECISERAT. Kortet sa 'vara bosatt, hålla till på en plats' — vilket gör ordet utbytbart mot *bo*, och det är det inte. SO:s avgränsning är att det gäller **betydelsefulla personer respektive ståndsmässiga bostäder**, och SO markerar att ordet *ibland* används något skämtsamt om vanliga människor. Just den avgränsningen är hela poängen med ordet."),

"resonans": ("Svängning som uppkommer genom påverkan av en annan svängning med nästan samma frekvens ; bildligt: gensvar och förståelse",
  "fackspråklig, neutral, fysik", ["medsvängning", "genklang", "gensvar"],
  "Förslaget fick ingen %s hos väljarna." % (B % "resonans"),
  "till latin resona´re 'genljuda'; jfr assonans, dissonans, sonor",
  "Båda betydelserna fanns redan. Den fysikaliska har preciserats — det avgörande är att frekvenserna är *nästan lika*, vilket är hela mekanismen, och det stod inte på kortet. Domänen `fysik` satt."),

"sammelsurium": ("Oordnad och brokig blandning av vitt skilda saker",
  "vardaglig, negativ", ["virrvarr", "röra", "mischmasch"],
  "Lådan var ett %s av verktyg, kvitton och gamla nycklar." % (B % "sammelsurium"),
  "av tyska Sammelsurium, skämtsam bildning till lågtyska sammelsur 'röra; surnad mat'; till samla och sur",
  "SO: 'total oordning'. Innehållet stämde. Preciserat att det inte bara är oordning utan att sakerna är **vitt skilda** — det är skillnaden mot vanligt stök. Etymologin är rolig och gör ordet minnesvärt: 'insamlad surmat'."),

"sarv": ("Mörtliknande karpfisk med hög, hoptryckt kropp och röda fenor ; separat ord av samiskt ursprung: hanren, rentjur",
  "neutral, neutral, biologi", ["karpfisk", "rentjur"],
  "%s känns igen på de klarröda fenorna." % (B % "Sarven"),
  "fisken: svensk dialekt sarv ; renen: av samiska sarves",
  "FEL MÄRKNING. Kortet kallade renbetydelsen '(dialektalt)'. SO har **två skilda uppslagsord**: renen kommer av samiskans *sarves*, fisken av ett svenskt dialektord. De är homografer med olika ursprung, inte en huvudbetydelse med dialektal bibetydelse. Fiskbetydelsen är dessutom den vanligare och står nu först. Kortets 'liten sötvattensfisk' preciserat till SO:s egen beskrivning."),

"skriftställare": ("Person som yrkesmässigt ägnar sig åt författarskap, vanligen på relativt anspråkslös nivå",
  "ngt ålderdomlig, neutral", ["författare", "skribent", "publicist"],
  "Han försörjde sig som %s och översättare." % (B % "skriftställare"),
  "efter tyska Schriftsteller; till skrift och ställa 'avfatta'",
  "PRECISERAT, OCH ÅT ANDRA HÅLLET ÄN KORTET. Kortet sa 'författare, särskilt av **seriösa** texter'. SO säger tvärtom: *vanligen på relativt anspråkslös nivå*. Ordet är alltså en lätt nedgradering i förhållande till *författare*, inte en uppgradering — det är precis den sortens nyans ett kort ska bära. Ingen `bruklighetskommentar` finns, men SAOL:s korta 'författare' plus tyskan bakom ordet motiverar `ngt ålderdomlig`."),

"synagoga": ("Judisk gudstjänstlokal", "neutral, neutral, religion",
  ["bönehus", "judisk helgedom"],
  "Församlingen samlades i %s på fredagskvällen." % (B % "synagogan"),
  "av grekiska synagoge´ 'samlingsplats; församling'",
  "SO och SAOL är ordagrant eniga. Innehållet stämde. Registret `formell` ströks — ordet är helt vanligt. Etymologin tillagd: ordet betyder 'samlingsplats', vilket är samma bild som i *kyrka* (av grekiskans 'som hör Herren till') och *moské* ('plats att böja sig')."),

"vördnad": ("Djup högaktning och respekt", "formell, positiv",
  ["respekt", "aktning", "högaktning"],
  "Han talade om sin läromästare med stor %s." % (B % "vördnad"),
  None,
  "SO: 'högaktning och respekt'. Innehållet stämde. Kortets synonym *beundran* ströks ur definitionen: man kan beundra utan att vörda, och vördnad rymmer ett drag av underordning som beundran inte har. Registret `positiv` saknade stilnivå. UPPSLAGNING OFULLSTÄNDIG: SAOL saknar artikel."),

"öda": ("Låta något gå förlorat i onödan — särskilt om tid, kraft eller andra abstrakta tillgångar",
  "ngt ålderdomlig, negativ", ["förslösa", "förspilla", "slösa"],
  "Han %s sina bästa år på det projektet." % (B % "ödde"),
  "fornsvenska öþa; till öde; jfr föröda, ödsla",
  "PRECISERAT. SO markerar att ordet gäller *konkreta el. (vanligen) abstrakta* tillgångar — det är oftast tid och kraft man öder, inte pengar. Där ligger skillnaden mot [[ödsla]], som står i samma batch. Ingen `bruklighetskommentar`, men ordet är belagt sedan fornsvenskan och är i dag klart mindre brukligt än *slösa*."),

"ödsla": ("Slösa med en tillgång, konkret eller abstrakt",
  "neutral, negativ", ["slösa", "förspilla", "misshushålla"],
  "Sluta %s med varmvattnet." % (B % "ödsla"),
  "bildning till fornsvenska ödha 'föröda'; till öde",
  "SO: 'slösa med konkret el. abstrakt tillgång'. Innehållet stämde. **Ordet står medvetet mot [[öda]] i samma batch**: båda går tillbaka på fornsvenskans *öda*, men ödsla är det vanligare och bredare ordet och används lika gärna om vatten som om tid. Registret `negativ` saknade stilnivå."),
}


def main():
    d = json.load(open(FIL, encoding="utf-8"))
    kort = d["kort"] if isinstance(d, dict) and "kort" in d else d
    n, saknas = 0, []
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
    print("UTAN FÖRSLAG: %s" % (", ".join(saknas) if saknas else "-"))


if __name__ == "__main__":
    main()
