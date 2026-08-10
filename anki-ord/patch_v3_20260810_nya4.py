# -*- coding: utf-8 -*-
"""v3-omgranskning av 50 kort ur is:new, fjärde omgången 2026-08-10.

**Första batchen där registret sätts på fullständigt underlag.** `slaupp.py`
skriver sedan i kväll ut SO:s `bruklighetskommentar` på en egen BRUK-rad.
Elva av de 50 orden visade sig ha en uttrycklig stilmarkering — uppgifter som
hade varit osynliga i alla tidigare batchar:

    komma på skam         ursprungligen bibliskt; något ålderdomligt
    ligga i lä            sjö.
    benägen               särsk. i vissa formelartade fraser
    gump                  vardagligt
    kajka                 vardagligt
    kardinal              särsk. i vetenskapliga el. tekniska sammanhang
    officiös              mindre brukligt
    samma skrot och korn  vardagligt
    snöd                  något ålderdomligt; åld.
    uppknäppt             vard.
    värv                  något ålderdomligt utom i ett par uttryck

Utgångsläget i batchen: **36 av 50 kort stod som `formell`** (72 %) och bara
fyra hade båda axlarna ifyllda.

## Innehållsfel (8 substantiella)

  komma på skam  FEL BETYDELSE. Kortet: "bli förödmjukad, avslöjad i sitt fel".
                 Uttrycket handlar inte om en person utan om en FÖRVÄNTAN:
                 något visar sig inte hålla. SO ger "inte uppfyllas",
                 Wiktionary "visa sig vara fel" — *farhågorna kom på skam*.
  triera         TVÅ ORD IHOPBLANDADE. Kortets andra betydelse, "prioritera
                 skadade efter allvarlighet", är *triage* — ett annat ord.
                 *Triera* betyder rensa och sortera säd, inget annat.
  hypotek        FEL LED. Kortet: "lån med fastighet som säkerhet". SO: hypotek
                 ÄR säkerheten/panten, inte lånet.
  brikett        FÖR SNÄVT. Kortet sa "bit bränsle". SO: sammanpressat stycke
                 av pulvriserat ämne — bränsle är ett användningsområde, inte
                 definitionen.
  snöd           ÖVERTOLKAT. Kortet: "ohederlig och präglad av vinningslystnad"
                 — det är frasen *snöd vinning* inläst i ordet. SO: "simpel".
  kajka          FEL ELEMENT. Kortet: "segla eller GÅ planlöst omkring". SO:
                 förflytta sig PÅ VATTNET utan mål.
  mystifiera     FEL RIKTNING. Kortet: "göra något gåtfullt". SO: skapa
                 oklarhet och förvirring HOS NÅGON; SAOL: föra ngn bakom ljuset.
  gump           FÖR SNÄVT. Kortet: "bakdel på ett djur". SO markerar även
                 "äv. om ryggslutet hos människa".

Plus tio saknade bibetydelser: exekvera (musik), intuitiv (lätt att förstå),
dussin (*det går tretton på dussinet*), bläs (hästen själv), kardinal
(adjektivet i *kardinalfel*), sjok (bildligt), sporadisk (spatialt),
formalitet (ren formalitet = avgjort på förhand), patriark (vördnadsvärd
åldring), befryndad (andlig släktskap).

## Misslyckade uppslagningar, utskrivna

  gyrometer          svenska.se gav träff men INGEN definition — varken SO
                     eller SAOL. Kortets innehåll är alltså obelagt.
  vinna laga kraft   frasen föll tillbaka på fritextsökning (returnerade
                     *laga* och *instinkt*). Slogs om under *laga kraft*.
  samma skrot och korn / komma på skam / ligga i lä — samma fallback, men SO
                     gav ändå idiomets betydelse i sin lista.
  triera             ingen SO- eller SAOL-artikel; bara synonymer.se och
                     Wiktionary, som är eniga.
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HAR = os.path.dirname(os.path.abspath(__file__))
FIL = os.path.join(HAR, "sessions", "session_2026-08-10_v3-omgranskning-nya4.json")
B = '<font color="#3498db">%s</font>'


def kalla(o):
    import urllib.parse
    q = urllib.parse.quote(o)
    return ("https://svenska.se/api/msearch?ord=%s "
            "https://www.synonymer.se/sv-syn/%s "
            "https://sv.wiktionary.org/wiki/%s" % (q, q, q))


R = {
"formalitet": ("Fastställd regel som måste följas för att något ska vara giltigt ; äv. om social umgängesregel ; äv. om något som i praktiken är avgjort på förhand",
  "neutral, neutral", ["formsak", "regelfråga", "teknikalitet"],
  "Utmanaren var så överlägsen att finalen blev en ren %s." % (B % "formalitet"),
  "till latin forma´lis; jfr formalisera",
  "SAKNAD BETYDELSE. SO ger tre skikt och kortet slog ihop de två första. Det som saknades är den vanligaste användningen i dag: *en ren formalitet* om något vars utgång redan är given. Registret `formell` ströks — SO markerar ingenting."),

"brikett": ("Sammanpressat stycke av pulvriserat eller fibrigt material, ofta bränsle",
  "neutral, neutral", ["pellet", "kolbit"],
  "De halvt uppbrända %s pyrde." % (B % "briketterna"),
  "av franska briquette, diminutiv av brique 'tegelsten'; samma ursprung som bricka",
  "FÖR SNÄVT. Kortet skrev 'kompakt, formpressad bit bränsle'. SO säger 'sammanpressat stycke av pulvriserat ämne' och SAOL 'pulver- el. fibermaterial' — bränsle är det vanligaste användningsområdet, inte definitionen. Det finns briketter av torv, sågspån och metallspån."),

"exekvera": ("Utföra eller verkställa, t.ex. en dom ; äv. om att framföra ett musikstycke",
  "formell, neutral", ["verkställa", "fullgöra", "framföra"],
  "Verket %s av radions symfoniorkester." % (B % "exekverades"),
  "av latin ex´sequi 'fullfölja', till seq´ui 'följa'; jfr sekvens",
  "SAKNAD BETYDELSE. SO markerar *äv. med avseende på musikstycke* med språkprovet ovan. Kortet hade bara den juridiska. Etymologin ('fullfölja') förklarar båda."),

"gallicism": ("Ord eller uttryck i ett icke-franskt språk som är påverkat av franskan",
  "fackspråklig, neutral, lingvistik", ["franskt lånord", "fransk språkegenhet"],
  "Hans tal var bemängt med %s." % (B % "gallicismer"),
  "till latin gall´icus 'gallisk, från Gallien'",
  "Innehållet stämde. Preciserat att ordet förutsätter ett *icke-franskt* mottagarspråk (SAOL:s egen formulering) — en gallicism i franskan är en omöjlighet. Registret ändrat till fackspråklig med domänen lingvistik."),

"gyrometer": ("Instrument som mäter rotationshastighet", "fackspråklig, neutral, teknik",
  ["rotationsmätare"],
  "%s registrerade hur snabbt farkosten roterade." % (B % "Gyrometern"),
  None,
  "UPPSLAGNING MISSLYCKADES. svenska.se gav en träff men **ingen definition** — varken SO eller SAOL har någon artikel, och varken synonymer.se eller Wiktionary hade ordet. Kortets innehåll är alltså obelagt i alla tre källorna och står kvar oförändrat i sak. Det stämmer med allmän teknisk användning (jfr *gyroskop*), men det är en härledning, inte ett belägg."),

"halvfabrikat": ("Industriprodukt som inte har förädlats slutgiltigt utan kräver vidare bearbetning",
  "neutral, neutral, ekonomi", ["mellanprodukt", "mellanvara", "ämne"],
  "Fabriken säljer %s vidare till monteringsindustrin." % (B % "halvfabrikat"),
  None,
  "SO: 'industriprodukt som inte slutgiltigt förädlats'. Innehållet stämde. Värt att notera att ordet i vardagligt tal oftast avser färdigmat — den betydelsen finns INTE i SO eller SAOL, och kortet har därför inte fått den. Registret `formell` ströks."),

"hypotek": ("Värdehandling eller pantsatt egendom som lämnas som säkerhet till en kreditgivare — panten, inte lånet",
  "fackspråklig, neutral, ekonomi", ["pant", "inteckning", "säkerhet"],
  "Många av gårdarna tyngdes svårt av %s." % (B % "hypotek"),
  "av grekiska hypothe´ke 'underlag; pant'",
  "FEL LED. Kortet skrev 'lån med fastighet som säkerhet'. SO säger tvärtom: hypotek ÄR värdehandlingen som lämnas som säkerhet, alternativt den pantsatta egendomen — alltså panten, inte krediten. Skillnaden syns i SO:s eget språkprov: gårdarna *tyngdes av* hypotek. Etymologin bekräftar: grekiskans ord för 'pant'."),

"intuitiv": ("Som bygger på omedelbar känsla i stället för medvetet resonemang ; äv. om något som är lätt att förstå utan förklaring",
  "neutral, neutral", ["instinktiv", "omedelbar", "lättbegriplig"],
  "Ett %s användargränssnitt kräver ingen manual." % (B % "intuitivt"),
  None,
  "SAKNAD BETYDELSE. SO markerar *äv. utvidgat* med betydelsen 'som är lätt att förstå' och språkprovet ovan. Det är i särklass den vanligaste användningen i dag — *intuitivt gränssnitt*, *intuitiv design* — och kortet hade den inte alls."),

"komma på skam": ("Om en förväntan, farhåga eller förutsägelse: visa sig inte hålla, inte uppfyllas",
  "ngt ålderdomlig, neutral", ["visa sig vara fel", "inte infrias"],
  "Alla farhågor om regn %s." % (B % "kom på skam"),
  "till fornsvenska skam 'blygsel; förtret'; uttrycket är ursprungligen bibliskt",
  "FEL BETYDELSE RÄTTAD. Kortet skrev 'bli förödmjukad, avslöjad i sitt fel', alltså om en PERSON. Uttrycket handlar om en förväntan: SO ger 'inte uppfyllas' och Wiktionary 'visa sig vara fel'. Det som kommer på skam är farhågan, profetian eller kritiken — inte den som bar den. Registret satt utifrån SO:s `bruklighetskommentar`: *ursprungligen bibliskt, något ålderdomligt*."),

"ligga i lä": ("Vara underlägsen någon i en jämförelse",
  "neutral, neutral", ["vara underlägsen", "ligga efter", "komma till korta"],
  "Jämfört med västkusten %s ostkusten beträffande mareld." % (B % "ligger i lä"),
  "till lä 'skydd mot vinden'; jfr isländska hlé; besläktat med ljum",
  "Innehållet stämde mot SO ('vara underlägsen'). Registret `formell` ströks. SO:s BRUK-markering *sjö.* gäller grundordet **lä** i sjöfartsbetydelsen (läsidan av ett fartyg), inte det bildliga uttrycket — därför sätts ingen sjöfartsdomän på kortet. Etymologin visar bilden: den som ligger i lä ligger i vindskugga bakom någon annan."),

"malakit": ("Grönt kopparmineral som även används som prydnadssten",
  "neutral, neutral, geologi", ["kopparmineral", "prydnadssten"],
  "Skrinet var inlagt med polerad %s." % (B % "malakit"),
  "bildning till grekiska malakh´e 'malva' — efter växtens gröna blad",
  "Kompletterat. SO ger 'ett grönt kopparmineral', SAOL 'en prydnadssten' — de två källorna beskriver samma sten från olika håll, och kortet hade bara mineralsidan. Etymologin tillagd: uppkallad efter malvans gröna blad."),

"maskopi": ("Hemligt samförstånd mellan två eller flera parter, ofta i syfte att skada någon annan",
  "neutral, negativ", ["hemligt samförstånd", "konspiration", "sammansvärjning"],
  "Delar av regeringen stod i %s med militären." % (B % "maskopi"),
  "av lågtyska matschopie, nederländska maatschappij 'kamratskap; bolag'",
  "SO och SAOL ger båda 'hemligt samförstånd'. Innehållet stämde. Registret `negativ` saknade stilnivå. Ordet förekommer i praktiken bara i frasen *stå/vara i maskopi med* — utskrivet i exemplet."),

"triera": ("Rensa och sortera säd", "fackspråklig, neutral, jordbruk",
  ["rensa säd", "sortera säd"],
  "Kornet %s före sådd." % (B % "trierades"),
  None,
  "TVÅ ORD IHOPBLANDADE. Kortets andra betydelse, 'prioritera skadade efter allvarlighet', är **triage** — ett helt annat ord, från franskans *triage* i sjukvårdssammanhang. *Triera* betyder rensa och sortera säd, och ingenting annat. UPPSLAGNING OFULLSTÄNDIG: varken SO eller SAOL har artikel för ordet; underlaget är synonymer.se ('rensa (säd)') och Wiktionary ('rensa och sortera säd'), som är eniga."),

"vinna laga kraft": ("Om en dom eller ett beslut: bli slutgiltigt och inte längre gå att överklaga",
  "fackspråklig, neutral, juridik", ["bli slutgiltig", "stadfästas"],
  "Domen %s efter tre veckor." % (B % "vann laga kraft"),
  None,
  "UPPSLAGNING MISSLYCKADES FÖRST. Sökning på hela frasen fick svenska.se att falla tillbaka på fritextsökning och returnera artiklarna för *laga* och *instinkt*. Ordet slogs om under **laga kraft**, där SO ger 'som fått laga kraft' (*en kraftvunnen dom*) och synonymer.se 'stadfästelse, rättslig giltighet'. Innehållet stämde."),

"adhesiv": ("Vidhäftande — som har att göra med adhesion", "fackspråklig, neutral",
  ["vidhäftande", "självklistrande"],
  "Ett %s och elastiskt bandage." % (B % "adhesivt"),
  None,
  "SO: 'som har att göra med adhesion', med markeringen *spec. medicin*; SAOL: 'vidhäftande'. Innehållet stämde. Registret ändrat från `formell` till `fackspråklig` — ordet är en fackterm, inte ett byråkratiskt ordval. Kortets 'klibbig' ströks: adhesion är vidhäftning mellan olika material, inte klibbighet."),

"arkivalier": ("Handlingar och dokument som förvaras i ett arkiv — används i plural",
  "formell, neutral", ["arkivhandlingar", "urkunder", "akter"],
  "Oersättliga %s förstördes i branden." % (B % "arkivalier"),
  "av danska arkivalier eller tyska Archivalien; bildat till arkiv",
  "SO: 'dokument som förvaras i arkiv'. Innehållet stämde. Tillagt att ordet i praktiken bara används i plural — det är den upplysning som gör ordet användbart och den saknades."),

"befryndad": ("Som står i släktskapsförhållande ; särskilt bildligt: andligt besläktad, av samma anda",
  "formell, neutral", ["besläktad", "likartad", "själsfrände"],
  "Diktarna uppfattar sig ibland som %s med filosoferna." % (B % "befryndade"),
  "fornsvenska befrundadher; till frände",
  "SAKNAD ANVÄNDNING. SO markerar *särsk. bildligt i fråga om andlig släktskap* — och det är den användning man faktiskt möter, som i SO:s eget språkprov ovan. Kortets 'besläktad, nära förbunden' täckte den bokstavliga men inte att den bildliga dominerar."),

"benägen": ("Som har en inre tendens att handla på visst sätt ; äv. välvilligt intresserad, i formelartade fraser",
  "neutral, neutral", ["böjd", "fallen för", "välvillig"],
  "Artikeln publiceras med %s bistånd av upphovsrättshavaren." % (B % "benäget"),
  "fornsvenska benäghin, eg. 'böjd'; till lågtyska nigen 'böja sig'; jfr niga",
  "Ett av få kort som redan hade båda SO-betydelserna. SO:s `bruklighetskommentar` för den andra är *särsk. i vissa formelartade fraser* — därför är exemplet bytt till just en sådan (*benäget bistånd*, *till benäget påseende*), som är där man faktiskt möter den betydelsen. Registret `formell` ströks."),

"bevekelsegrund": ("Underliggande, ofta känslobaserat motiv för ett handlande",
  "formell, neutral", ["motiv", "drivfjäder", "skäl"],
  "Man undrar vilka hans %s är för att hjälpa dem." % (B % "bevekelsegrunder"),
  None,
  "SO: 'underliggande motiv'. Innehållet stämde. Preciserat med Wiktionarys tillägg att motivet ofta är känslobaserat — det är skillnaden mot ett rent *skäl*, och den gör ordet värt att kunna."),

"bläs": ("Ljus, långsträckt strimma på framsidan av huvudet, särskilt på häst ; äv. om hästen som har en sådan",
  "neutral, neutral", ["pannfläck", "stjärn"],
  "En fux med vit %s." % (B % "bläs"),
  "germanskt ord av osäkert ursprung; besläktat med blossa",
  "SAKNAD BETYDELSE. SAOL ger två: märket OCH hästen själv ('häst med bläs'), vilket även Wiktionary bekräftar. Kortet hade bara märket. Etymologin (besläktat med *blossa*) förklarar bilden: en ljus fläck som lyser."),

"bryologi": ("Läran om mossor", "fackspråklig, neutral, biologi",
  ["mosslära"],
  "Han disputerade i %s." % (B % "bryologi"),
  "till grekiska bry´on 'mossa' och log´os '(en) lära'",
  "SO och SAOL är eniga. Innehållet stämde. Registret ändrat till fackspråklig med domänen biologi, och etymologin tillagd — den gör ordet härledbart i stället för att behöva memoreras."),

"desorienterad": ("Som har mist förmågan att orientera sig eller överblicka sammanhang",
  "neutral, neutral", ["vilsen", "förvirrad", "bortkommen"],
  "När läraren började med logiska symboler kände sig flera av eleverna %s." % (B % "desorienterade"),
  "till latin dis´- 'bort' och orientera",
  "SO: 'som mist förmågan att överblicka sammanhang'. Innehållet stämde. Exemplet bytt till SO:s egna, som visar att ordet inte bara gäller att gå vilse geografiskt utan även att tappa tråden i ett resonemang. Registret `formell` ströks."),

"dussin": ("Grupp om tolv stycken ; i uttrycket *det går tretton på dussinet*: det finns väldigt många, ofta med bibetydelse av medelmåttighet",
  "neutral, neutral", ["tolvtal", "tolv stycken"],
  "En kriminalroman som det går tretton på %s av." % (B % "dussinet"),
  "fornsvenska dusen; av lågtyska dosin; ytterst av latin duod´ecim 'tolv'; jfr duodecimalsystem",
  "SAKNAD BETYDELSE. SO ger utöver antalet även idiomet *det går tretton på dussinet*, med markeringen *ofta i uttryck för medelmåttighet*. Kortet hade bara 'tolv stycken', vilket gör ordet trivialt — det är idiomet som är värt ett kort. Registret `vardaglig` ströks; SO markerar ingenting."),

"eldfängd": ("Som lätt börjar brinna ; bildligt: hetsig, som lätt brusar upp",
  "neutral, neutral", ["lättantändlig", "hetlevrad", "snarstucken"],
  "Han har ett %s humör." % (B % "eldfängt"),
  "svensk dialekt eldfäng, eg. 'som fattas av elden'; jfr fåfäng",
  "Båda SO-betydelserna fanns redan. Synonymerna kompletterade så att även den bildliga sidan får sina — kortet hade bara 'lättantändlig' trots att det listade två betydelser. Registret `formell` ströks."),

"fotsid": ("Som når ända ner till fötterna", "neutral, neutral",
  ["hellång", "sid"],
  "En %s morgonrock." % (B % "fotsid"),
  None,
  "SO och SAOL är eniga. Innehållet stämde. Kortets synonym *ankellång* ströks — den anger en kortare längd än fotsid och är alltså inte utbytbar. Registret `formell` ströks."),

"frondör": ("Person som öppet gör motstånd mot ledningen inom sin egen organisation",
  "formell, neutral, politik", ["oppositionsman", "rebell", "revoltör"],
  "%s i partiet hotade att splittra riksdagsgruppen." % (B % "Frondörerna"),
  "av franska frondeur; efter Fronden, upproren mot kungamakten under Ludvig XIV",
  "PRECISERAT. Kortets 'person som gör motstånd mot makten' är för brett — en frondör opponerar sig inifrån, mot sin egen ledning, vilket SO:s språkprov visar (frondörerna *i partiet*). En demonstrant är inte en frondör. Etymologin tillagd; den förklarar ordet."),

"förargligt": ("Som orsakar lättare irritation", "neutral, lätt negativ",
  ["irriterande", "förtretligt", "retsamt"],
  "Det var %s att vi missade bussen." % (B % "förargligt"),
  None,
  "SO: 'som orsakar lättare irritation'. Innehållet stämde. Registret `vardaglig` ströks — SO markerar ingenting — och valören sänktes från `negativ` till `lätt negativ`: SO:s definition säger uttryckligen *lättare* irritation, vilket är hela skillnaden mot *upprörande*."),

"försmädlig": ("Överlägset spydig eller hånfull ; äv. om händelse: retsamt förarglig",
  "neutral, negativ", ["hånfull", "spydig", "maliciös"],
  "Vi missade bussen precis, %s nog." % (B % "försmädligt"),
  "bildning till smäda",
  "Båda SO-betydelserna fanns redan — ett av få kort där så var fallet. Registret `negativ` saknade stilnivå. Exemplet bytt till SO:s egna, som visar den andra betydelsen (om en händelse, inte om en person), eftersom den är svårare att gissa sig till."),

"fösa": ("Driva något framför sig så att det rör sig åt visst håll ; äv. om människor som behandlas som viljelösa",
  "neutral, neutral", ["driva", "mota", "valla"],
  "Vakterna %s bort åskådarna." % (B % "föste"),
  "av oklart ursprung",
  "SAKNAD ANVÄNDNING. SO markerar *äv. med avseende på människor som behandlas som passiva el. viljelösa* — och det är den användningen som bär ordets ton. Kortet nämnde bara djur och föremål. Registret `vardaglig` ströks."),

"gump": ("Bakdel, särskilt på fågel ; äv. om ryggslutet på en människa",
  "vardaglig, neutral", ["bakdel", "stjärt", "stuss"],
  "Stenskvättans lysande vita %s." % (B % "gump"),
  "svensk dialekt gump; troligen ursprungligen 'något runt och välvt'",
  "FÖR SNÄVT + REGISTER. Kortet sa 'bakdel på ett djur'. SAOL preciserar *hos fågel* och SO markerar *äv. om ryggslutet hos människa* (SO:s eget språkprov: *hon har blivit tung i gumpen*). Registret sattes utifrån SO:s `bruklighetskommentar`: **vardagligt** — kortet sa `formell`, alltså precis fel."),

"invektiv": ("Förolämpande ord, skällsord", "formell, neutral",
  ["skällsord", "smädelse", "tillmäle"],
  "Artikeln innehöll ingen egentlig kritik, mest bara en samling %s." % (B % "invektiv"),
  "av franska invective; av medeltidslatin invecti´va (ora´tio) 'smädande tal'",
  "PRECISERAT. SO säger 'förolämpande **ord**' — kortets 'uttalande' är fel enhet; ett invektiv är ett enskilt ord, inte en replik. Valören satt till neutral: ordet BETECKNAR skällsord men är självt en bokstavlig fackterm, precis som *okvädinsord*."),

"kajka": ("Förflytta sig planlöst på vattnet, ro eller segla utan mål",
  "vardaglig, neutral", ["driva", "kava", "ro planlöst"],
  "Ligga och %s i en eka." % (B % "kajka"),
  "via svensk-estniska dialekter av estniska kaikuma 'vackla; gunga'",
  "FEL ELEMENT + REGISTER. Kortet skrev 'segla eller **gå** planlöst omkring'. SO är entydig: *förflytta sig på vattnet* utan mål. Man kajkar inte på land. Registret sattes utifrån SO:s `bruklighetskommentar`: **vardagligt** — kortet sa `vardaglig` redan, men valören saknades."),

"kardinal": ("Innehavare av den näst högsta värdigheten i romersk-katolska kyrkan ; som adjektiv: som utgör en av de viktigaste eller fasta punkterna, som i *kardinalfel*",
  "neutral, neutral, religion", ["kyrkofurste", "prelat", "grundläggande"],
  "%s samlades i Rom för att välja ny påve." % (B % "Kardinalerna"),
  "av medeltidslatin cardina´lis, till car´do 'dörrtapp; huvudpunkt'",
  "SAKNAD ORDKLASS. SO har fyra betydelser under uppslagsordet; kortet hade bara prästen. Den viktigaste som saknades är **adjektivet** — det som gör *kardinalfel*, *kardinaldygd* och *kardinalpunkt* begripliga. Etymologin binder ihop dem: *cardo* är dörrtappen som allt vrider sig kring, alltså huvudpunkten. Fågelbetydelsen utelämnad som perifer."),

"karess": ("Smekning, ömhetsbetygelse", "litterär, positiv",
  ["smekning", "ömhetsbetygelse", "smek"],
  "Han mötte hennes hand med en %s." % (B % "karess"),
  "av franska caresse; till latin ca´rus 'kär'",
  "SAOL: 'smekning'. Innehåll och register (`litterär, positiv`) stämde båda redan — synonymer.se markerar ordet '(litt.)', vilket bekräftar stilnivån. UPPSLAGNING OFULLSTÄNDIG: SO saknar artikel för ordet."),

"konstruktivism": ("Konstnärlig och arkitektonisk riktning som uppstod i Ryssland kring 1920 ; inom samhällsvetenskap: uppfattningen att verkligheten är socialt konstruerad",
  "fackspråklig, neutral, filosofi", ["konstruktionism", "socialkonstruktivism"],
  "Den bärande tanken i social %s är att vi alla är sociala varelser." % (B % "konstruktivism"),
  None,
  "Båda SO-betydelserna fanns redan. Preciserat att konstriktningen är rysk och kring 1920 (SO: belagt 1925), eftersom ordet annars är svårt att placera. Registret ändrat från `formell` till `fackspråklig` med domänen filosofi. UPPSLAGNING OFULLSTÄNDIG: synonymer.se saknade ordet."),

"kvalifikation": ("Egenskap eller merit som gör någon lämplig eller behörig för en uppgift",
  "neutral, neutral", ["behörighet", "kompetens", "merit"],
  "Båda de sökande hade tillräckliga %s." % (B % "kvalifikationer"),
  None,
  "SO: 'förmåga', SAOL: 'nödvändiga förutsättningar; meriter'. Innehållet stämde. Registret `formell` ströks — ordet förekommer i vanliga platsannonser. SO:s andra betydelse (ett juridiskt tolkningsförfarande) är utelämnad som alltför specialiserad; den möter man inte utanför rättsvetenskapen."),

"laktos": ("Mjölksocker — en disackarid av glukos och galaktos",
  "fackspråklig, neutral, kemi", ["mjölksocker"],
  "Mjölken är fri från %s." % (B % "laktos"),
  "till latin la´c 'mjölk' och ändelsen -os, som markerar sockerarter",
  "SO och SAOL säger båda 'mjölksocker'. Innehållet stämde. Den kemiska sammansättningen tillagd ur Wiktionary, och etymologin — ändelsen *-os* återkommer i *glukos*, *fruktos*, *sackaros* och gör hela gruppen igenkännlig."),

"mystifiera": ("Skapa oklarhet och förvirring hos någon ; äv. föra någon bakom ljuset",
  "neutral, neutral", ["förbrylla", "förvirra", "föra bakom ljuset"],
  "Ett uttalande som snarare %s än klargjorde situationen." % (B % "mystifierade"),
  "av franska mystifier",
  "FEL RIKTNING. Kortet skrev 'göra något gåtfullt och oklart' — som om objektet vore saken. SO säger 'skapa oklarhet och förvirring **hos**', alltså hos en person, och SAOL lägger till 'föra ngn bakom ljuset'. Man mystifierar sin publik, inte sitt ämne."),

"näver": ("Bark av björk, använd som material", "neutral, neutral",
  ["björkbark", "björknäver"],
  "Korgen var flätad av %s." % (B % "näver"),
  "fornsvenska näver; av ovisst ursprung",
  "SO och SAOL säger båda 'bark av björk'. Innehållet stämde. Registret `formell` ströks — näver är ett vardagligt hantverksord, belagt sedan 1300-talet."),

"officiös": ("Halvofficiell — som förmedlar en myndighets uppfattning utan att vara formellt bindande",
  "formell, neutral", ["halvofficiell"],
  "Regeringsorganet och andra officiella och %s organ." % (B % "officiösa"),
  "av franska officieux; av latin officio´sus 'tjänstaktig', till offic´ium 'tjänst'",
  "SO och SAOL säger båda 'halvofficiell'. Innehållet stämde, och preciseras här med vad halvofficiell innebär. SO:s `bruklighetskommentar` är **mindre brukligt** — det är en frekvensuppgift, inte en stilnivå, så registret står kvar som `formell`, men sällsyntheten är värd att känna till."),

"oratorium": ("Stort dramatiskt musikverk för kör, solister och orkester, oftast över religiöst ämne ; äv. bönesal eller bönkapell",
  "formell, neutral, musik", ["körverk", "bönekapell"],
  "Haydns %s Skapelsen." % (B % "oratorium"),
  "av medeltidslatin orato´rium 'bönsal', till latin ora´re 'bedja'",
  "Båda betydelserna fanns redan. Preciserat att verket oftast har religiöst ämne (SAOL: 'större sakralt musikverk'), vilket också förklarar kopplingen till bönesalen — etymologin visar att musikformen är uppkallad efter rummet den framfördes i. Domänen `musik` satt."),

"patriark": ("Stamfader eller en släkts överhuvud ; vördnadsvärd åldring ; titel för en högt uppsatt kyrklig ledare, särskilt i ortodoxa kyrkor",
  "formell, neutral", ["stamfader", "familjeöverhuvud", "kyrkofurste"],
  "%s i Moskva ledde gudstjänsten." % (B % "Patriarken"),
  "fornsvenska patriarke; av grekiska patriar´khes 'stamfader'; jfr monark, pater",
  "SAKNAD BETYDELSE. SO har fyra; kortet hade två och saknade 'vördnadsvärd åldring' — den betydelse man möter i *byns patriark*, utan vare sig släktskap eller kyrka inblandad. Etymologin tillagd."),

"samma skrot och korn": ("Av samma sort, oftast med underförstått nedsättande innebörd",
  "vardaglig, negativ", ["av samma sort", "lika usla", "likadana"],
  "De två ministrarna var av %s." % (B % "samma skrot och korn"),
  "efter tyska Schrot und Korn (ca 1740); i myntsammanhang var skrotet myntets totalvikt och kornet dess halt av ädelmetall",
  "Innehåll och register stämde båda. Det stora tillägget är etymologin, som gör uttrycket begripligt i stället för godtyckligt: *skrot* och *korn* är myntningstermer — totalvikten respektive ädelmetallhalten. Två mynt av samma skrot och korn var alltså identiska ända in i legeringen. UPPSLAGNING: frasen föll tillbaka på fritextsökning, men SO gav ändå idiomets betydelse ('vara av samma (dåliga) sort') och synonymer.se 'själsligen lika, lika usla'."),

"sinnebild": ("Företeelse som på ett koncentrerat sätt ger uttryck för en annan — en symbol",
  "formell, neutral", ["symbol", "inkarnation", "personifikation"],
  "Den sönderbombade kyrkan stod som en %s för krigets vansinne." % (B % "sinnebild"),
  "efter tyska Sinnbild",
  "SO: 'företeelse som på ett koncentrerat sätt ger uttryck för viss annan företeelse'. Innehållet stämde. Preciserat att det är *koncentrationen* som skiljer en sinnebild från vilken symbol som helst — sinnebilden är det renodlade exemplet på något."),

"sjok": ("Stort, sammanhängande stycke ; äv. bildligt om stora mängder av något",
  "neutral, neutral", ["stycke", "flak", "klump"],
  "Stora %s av information rullade förbi på skärmen." % (B % "sjok"),
  "svensk dialekt sjok, troligen variant till slok 'stycke av något helt'; till sloka",
  "SAKNAD BETYDELSE. SO markerar *äv. bildligt* med språkprovet *stora sjok av information*. Kortet hade bara det fysiska stycket. Kortets 'ofta oformlig' ströks — det står inte i någon källa; SO betonar i stället att stycket är stort och sammanhängande. Registret `vardaglig` ströks."),

"snöd": ("Simpel, lumpen — särskilt i uttrycket *för snöd vinnings skull*",
  "ngt ålderdomlig, negativ", ["simpel", "lumpen", "tarvlig"],
  "Han övergav henne för %s vinnings skull." % (B % "snöd"),
  "fornsvenska snöþer 'bar; öde; usel'; germanskt ord med grundbetydelsen 'avskuren; naken'",
  "ÖVERTOLKAT. Kortet skrev 'ohederlig och präglad av vinningslystnad' — det är frasen *snöd vinning* inläst i själva ordet. SO säger bara 'simpel' och SAOL 'simpel, lumpen'; vinningslystnaden ligger i *vinning*, inte i *snöd*. Registret sattes utifrån SO:s `bruklighetskommentar`: **något ålderdomligt**, och SAOL:s *åld.* — kortet sa `litterär`."),

"sovra": ("Sortera bort de mindre användbara delarna ur något",
  "neutral, neutral", ["gallra", "sålla", "utmönstra"],
  "En författare måste kunna %s i stoffet." % (B % "sovra"),
  "av lågtyska suvern 'rena; sovra'; nära besläktat med tyska sauber 'ren'",
  "SO och SAOL är ordagrant eniga. Innehållet stämde. Preciserat att man sovrar **ur** något — verbet tar det man rensar i, inte det man kastar. Registret `formell` ströks."),

"sporadisk": ("Som förekommer bara vid enstaka tillfällen ; äv. bara på enstaka platser",
  "neutral, neutral", ["enstaka", "oregelbunden", "spridd"],
  "%s notiser i tidningen om olyckan." % (B % "Sporadiska"),
  "ur grekiska sporadikos´ 'strövis förekommande'; besläktat med spor",
  "SAKNAD BETYDELSE. SO ger två: den tidsmässiga (enstaka tillfällen) och den **rumsliga** (enstaka platser) — *en väst med små blommor sporadiskt ditsydda*. Kortet hade bara den tidsmässiga. Kortets synonym *sällsynt* ströks: sporadisk handlar om oregelbundenhet, inte om låg frekvens; något kan vara sporadiskt och ändå vanligt."),

"uppknäppt": ("Vars knappar inte är knäppta ; bildligt: glatt avspänd och pratsam",
  "vardaglig, neutral", ["oknäppt", "uppsluppen", "avspänd"],
  "Det %s sällskapet vid bordet bredvid skrattade högt." % (B % "uppknäppta"),
  None,
  "Båda SO-betydelserna fanns redan. Registret bekräftat mot SO:s `bruklighetskommentar` **vard.** — som gäller just den bildliga betydelsen. Kortets synonymer var en blandning av båda betydelsernas; de är nu ordnade så att den bokstavliga kommer först."),

"värv": ("Målinriktad verksamhet, uppdrag eller syssla", "ngt ålderdomlig, neutral",
  ["uppdrag", "syssla", "förrättning"],
  "Efter välförrättat %s smakade det bra med en kopp kaffe." % (B % "värv"),
  "fornsvenska värf; av lågtyska werf 'förehavande; yrke'; till värva",
  "REGISTER RÄTTAT MOT KÄLLAN. SO:s `bruklighetskommentar` lyder **något ålderdomligt utom i ett par uttryck** — kortet sa `litterär`. Preciseringen spelar roll: ordet är på väg ut, men lever kvar i *efter välförrättat värv* och *i sitt dagliga värv*, och det är där man möter det. Exemplet är nu SO:s egna."),
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
