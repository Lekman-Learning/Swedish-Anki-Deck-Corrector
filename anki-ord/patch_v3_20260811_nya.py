# -*- coding: utf-8 -*-
"""v3-omgranskning av 50 kort ur is:new, 2026-08-11.

**Batchen där uppslagsverktyget själv visade sig ha ett hål.** `slaupp.py`s
`sammandrag` slår ihop *alla* fuzzy-träffar från svenska.se i ett fält. För
långa, ovanliga ord spelar det ingen roll — de har bara en träff. För korta ord
och flerordsuttryck blir sammandraget en blandning av flera uppslagsord:

    tes              -> 'tes' OCH 'te'      (njutningsdryck av tebusken)
    brasserie        -> 'brasseri', 'brass', 'brasse', 'brassa'
    black om foten   -> 'black', 'fot', 'om' -- var för sig
    ge sig till tåls -> 'tåls', 'ge sig', 'tåla sig'

Tre av de 50 hade INGEN exakt uppslagsordsträff alls, och deras "tre källor"
var därför en illusion: källan fanns, men handlade delvis om ett annat ord.
Samma felklass som stökiometri-nollan och den falska AnkiConnect-negativen --
**ett mätvärde som ser giltigt ut men mäter fel sak.** Den här omgången är
skriven mot exakt uppslagsordsmatchning i stället för mot sammandraget.

De tre lösta för hand ur råträffarna:
  brasserie        SO/SAOL har den svenska stavningen 'brasseri'
  black om foten   SO: 'black' = hämmande faktor; SAOL: 'black' = klossformad
                   fotboja i äldre tid -- vilket ÄR uttryckets bild
  ge sig till tåls SO definierar 'tåla sig' som just 'ge sig till tåls',
                   bruklighetskommentar **vardagligt**

## Innehållsfel (13 substantiella)

  finkel        FEL HUVUDBETYDELSE. Kortet: "illasmakande biprodukt vid
                spritdestillering" -- det är finkelolja, SO:s ANDRA betydelse.
                Huvudbetydelsen är brännvinet självt: "brännvin som inte är
                renat" (SO), "ofullständigt renat brännvin" (SAOL).
  förbigå       OBELAGD BETYDELSE. Kortet hade "överträffa". Ingen av SO, SAOL,
                synonymer.se eller Wiktionary ger den betydelsen.
  genes         SAKNAD BETYDELSE. Kortet hade "ursprung"; SO ger "uppkomst
                ELLER UTVECKLING".
  elevation     SAKNAD BETYDELSE. Bara höjd/vinkel på kortet; SO ger även
                "upplyftning" (kalken i mässan, danspartner i balett).
  anstränga     SAKNAD BETYDELSE. Bara den reflexiva; SO ger först den
                transitiva -- man anstränger ögonen, personalen, en växel.
  lågmäld       SAKNAD BETYDELSE. Bara om person; SO:s första betydelse gäller
                det som SÄGS -- ett lågmält sorl, en lågmäld kritik.
  probera       SAKNAD BETYDELSE. Fackbetydelsen "fastställa halten av guld,
                silver eller platina i" saknades helt.
  parafras      SAKNAD BETYDELSE. Musikbetydelsen (fri bearbetning av känd
                melodi) saknades; SO och SAOL har den båda.
  kvadrant      SAKNAD BETYDELSE. Cirkelsektorn (en fjärdedels cirkel) saknades
                mellan koordinatsystemet och mätinstrumentet.
  mistlur       SAKNAD BETYDELSE. SO markerar "ofta bildligt" -- *furiren hade
                röst som en mistlur*.
  fullmakt      SAKNAD BETYDELSE. Även om själva dokumentet, inte bara rätten.
  ömka          SAKNAD BETYDELSE. Den reflexiva (ömka sig = beklaga sig).
  duffel        FÖR BRETT. Kortet gav "tjockt ylletyg" som egen betydelse; SO
                och SAOL ger bara plagget. Tyget är etymologi, inte en
                nuvarande svensk betydelse.

## Registerfel (9) -- BRUK-raden fortsätter leverera

  förmodligen   "vardaglig" -> neutral. Ingen källa markerar ordet alls.
  sauna         "vardaglig" -> neutral. SO och SAOL ger bara "bastu".
  villervalla   "vardaglig" -> neutral. Ingen bruklighetskommentar i någon källa.
  kurtisera     "formell" -> ngt ålderdomlig. SO: "mest vid beskrivning av äldre
                förhållanden", SAOL: "åld."
  pilt          "litterär" -> ngt ålderdomlig. SO: "något ålderdomligt", SAOL: "åld."
  vidlåda       "litterär" -> ngt ålderdomlig. SO: "något ålderdomligt".
  minuskel      "formell" -> fackspråklig/historia. SO: "mest vid beskrivning av
                äldre förhållanden", SAOL: "liten bokstav i äldre texter".
  genes         "formell" -> fackspråklig. SO: "i vetenskapliga sammanhang".
  elevation     "formell" -> fackspråklig. SO: "i vissa fackspråk".

## Synonymfel (3)

  karmosin      ORDKLASS. Adjektivet "mörkröd" som synonym till ett substantiv.
  körna         CIRKULÄR. "markera med körnare" innehöll uppslagsordets stam.
  affix         "prefix/suffix" var en enda sträng med snedstreck, och missade
                infix (SAOL: "prefix el. suffix el. infix").

## Registertaggarna är en fast lista, inte fritext

Första körningen skrev 41 av 50; nio vägrades av `config.REGISTER_FORMALITY`.
Jag hade hittat på "vetenskaplig", "ålderdomlig" och "historisk". Listan har
"fackspråklig", "ngt ålderdomlig" och en separat domänaxel med "historia" --
och domänen heter "lingvistik", inte "språkvetenskap". Spärren hade rätt: ett
fritt formulerat register går inte att filtrera på i Anki senare.

## Skrivfel (1)

  förmodligen   Exempelmeningen hade "försent" i ett ord. Ska vara "för sent".
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

"genes": ("Uppkomst eller utveckling — hur något har vuxit fram",
  "fackspråklig, neutral", ["uppkomst", "ursprung", "utveckling"],
  "Läkarna försökte förstå sjukdomens %s." % (B % "genes"),
  "av franska genèse; av grekiska génesis 'uppkomst; ursprung' — samma rot som i genus, genetisk och genealogi",
  "SAKNAD BETYDELSE + REGISTER. Kortet hade bara 'ursprung, hur något har uppstått'. SO ger **uppkomst ELLER UTVECKLING** — det är ett förlopp, inte bara en startpunkt, och det är därför ordet lever i sammansättningar som fylogenes och ontogenes. Registret rättat mot SO:s bruklighetskommentar **i vetenskapliga sammanhang**; kortet sa 'formell'."),

"affix": ("Betydelsebärande orddel som fästs före, efter eller inuti ordets kärna",
  "fackspråklig, neutral, lingvistik", ["förstavelse", "ändelse"],
  'Ordet "betalning" har två %s: "be-" och "-ning".' % (B % "affix"),
  "till latin affixus 'fästad', av affigere 'fästa vid' — samma rot som fix, prefix och suffix",
  "SYNONYM + PRECISERING. Kortets synonym var strängen 'prefix/suffix' — två ord hopklistrade med snedstreck, vilket inte fungerar som utbytbar synonym. Kortet missade dessutom **infix** (SAOL: 'prefix el. suffix el. infix'), alltså orddelar som stoppas in mitt i ordet. Definitionen är nu SO:s, som täcker alla tre lägena."),

"anstränga": ("Hårt utnyttja förmågan hos någon eller något ; äv. energiskt inrikta sina egna krafter",
  "neutral, neutral", ["belasta", "pressa", "sträva"],
  "Korrekturläsning %s ögonen." % (B % "anstränger"),
  "av tyska anstrengen, till strengen 'spänna, strama åt' — jfr sträng",
  "SAKNAD BETYDELSE. Kortet hade bara den reflexiva användningen (*anstränga sig*). SO listar den **transitiva först**: man anstränger ögonen, personalen, en telefonväxel. Exempelmeningen är nu SO:s egen och visar just den, eftersom det var den som saknades."),

"borgensman": ("Person som går i borgen för någon annans lån eller skuld",
  "fackspråklig, neutral, juridik", ["garant", "löftesman"],
  "Hans pappa gick in som %s för lånet." % (B % "borgensman"),
  "fornsvenska borghana man, 'borgens man'",
  "Innehållet stämde med SO och SAOL. Synonymen **löftesman** tillagd — den är den etablerade juridiska motsvarigheten och står i både SAOL och synonymer.se. Registret preciserat till juridik."),

"elevation": ("Höjdriktning eller höjd över horisonten ; äv. upplyftning av ett föremål",
  "fackspråklig, neutral", ["höjdvinkel", "lyftning"],
  "Upp till en %s på 45 grader växer skottvidden." % (B % "elevation"),
  "av latin elevatio 'lyftning', till elevare 'lyfta'",
  "SAKNAD BETYDELSE + REGISTER. Kortet hade bara höjd och pjäsvinkel. SO ger även **upplyftning** — av kalken och patenen i den katolska mässan, och av den kvinnliga danspartnern i klassisk balett. Registret rättat mot SO:s **i vissa fackspråk**; det förklarar också varför ordet betyder olika saker i artilleri, kyrka och balett."),

"finkel": ("Ofullständigt renat brännvin ; äv. om finkeloljan som ger det dess skarpa smak",
  "vardaglig, negativ", ["dunder", "hembränt"],
  "Det hembrända luktade skarpt av %s." % (B % "finkel"),
  "förkortning av lågtyska finkeljochen, troligen till fünkeln (slang) 'bränna' och hebreiska jajin 'vin'",
  "FEL HUVUDBETYDELSE. Kortet sa 'illasmakande biprodukt vid spritdestillering' — det är **finkelolja**, som SO listar som ordets ANDRA betydelse. Huvudbetydelsen är själva drycken: 'brännvin som inte är renat' (SO), 'ofullständigt renat brännvin' (SAOL). Kortet hade alltså gjort underbetydelsen till huvudsak."),

"förbigå": ("Lämna utan uppmärksamhet, hoppa över ; äv. undgå någons uppmärksamhet",
  "formell, neutral", ["förbise", "utelämna", "hoppa över"],
  "Han %s vid utnämningen." % (B % "förbigicks"),
  None,
  "OBELAGD BETYDELSE BORTTAGEN. Kortet hade **överträffa** som andra betydelse. Ingen av SO, SAOL, synonymer.se eller Wiktionary känner den — ordet betyder att gå förbi någon i mening 'förbise', inte att prestera bättre. Ersatt med SO:s faktiska andrabetydelse, *undgå uppmärksamheten hos* (*något hade förbigått henne*)."),

"förmodligen": ("Med rätt hög sannolikhet",
  "neutral, neutral", ["sannolikt", "troligen"],
  "Han kommer %s för sent igen." % (B % "förmodligen"),
  None,
  "REGISTER + SKRIVFEL. Kortet märkte ordet **vardaglig**; varken SO eller SAOL ger någon bruklighetskommentar alls, så det är neutralt — det används i myndighetstext lika gärna som i tal. Exempelmeningen hade dessutom *försent* i ett ord; korrekt svenska är **för sent** i två."),

"karmosin": ("Starkt rött färgämne ; äv. om den djupt röda färgen självt",
  "formell, neutral", ["karmin", "purpur"],
  "Sammeten lyste i djup %s." % (B % "karmosin"),
  "via medeltidslatin av arabiska qirmizî 'scharlakansfärgad' — samma ursprung som karmin",
  "SYNONYMFEL (ordklass). Kortet hade adjektivet *mörkröd* som synonym till ett substantiv — *en djup mörkröd* går inte att säga. SO ger 'karmin'; SAOL och Wiktionary 'ett rött färgämne', utvunnet ur en sköldlus. Ordet betecknar alltså i första hand **ämnet**, i andra hand nyansen."),

"körna": ("Göra en liten fördjupning i metall som märker ut var borren ska sättas",
  "fackspråklig, neutral, teknik", ["punktmarkera", "slå märke i"],
  "Han %s plåten innan han borrade hålet." % (B % "körnade"),
  "till körnare, verktyget som används",
  "CIRKULÄR SYNONYM. Kortets enda synonym var *markera med körnare* — den innehåller uppslagsordets egen stam och förklarar därför ingenting för den som inte redan vet vad en körnare är. Utbytt mot två som står på egna ben. Definitionen preciserad med **varför** man körnar: borren glider annars."),

"luminiscens": ("Ljusstrålning från ett ämne som inte är upphettat",
  "fackspråklig, neutral, fysik", ["kallt ljus", "fosforescens"],
  "Maneterna lyste med en svag %s i det mörka vattnet." % (B % "luminiscens"),
  "till latin lumen 'ljus'",
  "Innehållet stämde. Definitionen är nu SO:s ordagranna, eftersom kontrasten är hela poängen: ljus **utan** hög temperatur, till skillnad från glödljus. Fluorescens och fosforescens är två underarter."),

"mastig": ("Väl tilltagen — om mat mättande, om annat omfattande och tung",
  "vardaglig, neutral", ["bastant", "diger", "dryg"],
  "En %s film på fem timmar." % (B % "mastig"),
  "av lågtyska mastig 'välfödd; tjock', till Mast 'gödning av kreatur'",
  "BREDDAD. Kortet band ordet till mat ('tung och mättande'). SO:s definition är bara **väl tilltagen** — en film, en rapport eller en räkning kan vara mastig. Registret bekräftat mot SAOL:s **vard.**"),

"mistlur": ("Signalapparat som varnar sjöfarten vid dimma ; äv. bildligt om en dov, dånande röst",
  "neutral, neutral", ["mistsignal", "tyfon"],
  "Furiren hade röst som en %s." % (B % "mistlur"),
  "till mist 'dimma' och lur",
  "SAKNAD BETYDELSE. SO markerar **ofta bildligt** och ger exemplet *furiren hade röst som en mistlur*. Den bildliga användningen är minst lika vanlig som den bokstavliga i modern svenska, och saknades helt. Exempelmeningen är nu SO:s egen."),

"mondial": ("Som omfattar hela världen",
  "formell, neutral", ["världsomfattande", "global"],
  "Klimatfrågan är ett %s problem." % (B % "mondialt"),
  "av franska mondial, till monde 'värld'; till latin mundus 'värld; universum'",
  "Innehållet stämde med SO och SAOL. Etymologin tillagd — den gör ordet lättare att minnas via *monde*, som många känner igen ur *le monde*."),

"monsieur": ("Fransk artighetstitel för en man — herr, herre",
  "formell, neutral", ["herr", "herre"],
  'Kyparen bugade: "Varsågod, %s."' % (B % "monsieur"),
  "av franska monsieur, egentligen 'min herre'",
  "Innehållet stämde. Etymologin tillagd: ordet är *mon sieur*, 'min herre' — vilket förklarar varför det böjs som det gör och varför pluralen är *messieurs*."),

"toastmaster": ("Person som utbringar skålar och presenterar talarna vid en större fest",
  "neutral, neutral", ["ceremonimästare", "festmarskalk"],
  "Han har varit %s på flera bröllop." % (B % "toastmaster"),
  "av engelska toastmaster, till toast 'skål' och master — jfr mästare",
  "PRECISERAD. Kortet sa 'person som leder ett festligt tillfälle', vilket lika gärna beskriver en konferencier. SO är specifik: det är den som **utbringar skålarna och anmäler talarna**. Synonymen 'konferencier' är därför inte utbytbar och har ersatts av ceremonimästare och festmarskalk."),

"andefattig": ("Som präglas av brist på idéer och skaparförmåga",
  "formell, negativ", ["själlös", "idéfattig"],
  "Talet var långt och %s." % (B % "andefattigt"),
  "efter tyska geistesarm med samma betydelse",
  "Innehållet stämde. Synonymerna skärpta: kortets *tråkig* och *livlös* är för allmänna — andefattig handlar specifikt om **avsaknad av idéer**, inte om att något är trist. SAOL ger 'själlös, utan idéer'."),

"anhang": ("Obestämd, tvivelaktig grupp som följer och stöder en viss person",
  "neutral, negativ", ["följe", "pack"],
  "Ledaren kom insläntrande med hela sitt %s." % (B % "anhang"),
  "av tyska Anhang, till hängen 'hänga' — jfr anhängare och bihang",
  "Registret bekräftat mot SO:s bruklighetskommentar **nedsättande** — kortet hade redan rätt där. Definitionen preciserad: det avgörande ordet i SO är *tvivelaktig*, alltså inte vilket följe som helst."),

"beslå": ("Förse med metallbeslag ; rulla ihop och surra fast ett segel ; oemotsägligt ertappa någon",
  "fackspråklig, neutral", ["ertappa", "överdra"],
  "Han %s med att ha fuskat på provet." % (B % "beslogs"),
  "fornsvenska besla; av lågtyska beslan — se slå",
  "Alla tre betydelserna fanns och stämmer mot SO. Preciserat att den första gäller **metall** (SO markerar 'mest teknik') och att segelbetydelsen är att *rulla ihop och binda fast* — kortet sa bara 'fästa ett segel', vilket är något annat än att bärga det."),

"black om foten": ("Något som hindrar en från att komma framåt — en hämmande börda",
  "neutral, neutral", ["hämsko", "belastning"],
  "De gamla skulderna blev en %s för hela satsningen." % (B % "black om foten"),
  "en *black* var en klossformad fotboja som i äldre tid sattes på fångar och hästar för att hindra dem från att rymma",
  "KÄLLA REDD UT FÖR HAND. Uppslaget gav ingen exakt träff på uttrycket — verktyget slog i stället upp *black*, *fot* och *om* var för sig, vilket blandade in längdmåttet fot och hästfärgen black. Ur råträffarna: SO ger 'black' = **hämmande faktor**, SAOL 'black' = **klossformad fotboja i äldre tid**. Det andra är uttryckets bild och nu dess etymologi — det gör uttrycket begripligt i stället för godtyckligt. Registret rättat från 'litterär' till neutral: uttrycket är fullt gångbart i dagens svenska."),

"brasserie": ("Enklare restaurang av fransk typ, ofta med ölservering",
  "neutral, neutral", ["bistro", "matservering"],
  "De åt lunch på en liten %s i Paris." % (B % "brasserie"),
  "av franska brasserie 'bryggeri, restaurang', till brasser 'brygga' — därav ölen",
  "KÄLLA REDD UT FÖR HAND. Ingen exakt träff på den franska stavningen; SO och SAOL har ordet som **brasseri**, och verktyget drog annars in *brass*, *brasse* och *brassa*. SAOL:s tillägg **med ölservering** är värt att ha kvar, för det är det som skiljer en brasserie från en bistro — och etymologin (bryggeri) förklarar varför."),

"duffel": ("Knälångt ytterplagg av grovt ylletyg, ofta med kapuschong",
  "neutral, neutral", ["ytterrock", "kappa"],
  "Han tog på sig sin gamla %s innan han gick ut i snön." % (B % "duffel"),
  "av engelska duffle coat; till Duffel, en stad i Belgien där tyget vävdes",
  "FÖR BRETT. Kortet gav två betydelser: tyget och plagget. SO ger bara **plagget** ('ett knälångt ytterplagg av grovt ylletyg') och SAOL bara 'en typ av ytterrock med kapuschong'. Tyget är ordets ursprung, inte en nuvarande svensk betydelse — det hör hemma i etymologiraden, där det nu ligger."),

"fullmakt": ("Formellt utfärdad rätt att utöva någon annans lagliga rättigheter ; äv. om själva dokumentet",
  "fackspråklig, neutral, juridik", ["bemyndigande", "mandat"],
  "Hon hade %s i fickan." % (B % "fullmakten"),
  "fornsvenska fulmakt; av lågtyska vulmacht — till full och makt",
  "SAKNAD BETYDELSE. Kortet beskrev bara **rätten**. SO markerar uttryckligen 'äv. om motsvarande dokument', och det är den betydelsen man använder dagligdags — *skriva en fullmakt*, *ha fullmakten i fickan*. Synonymen 'behörighet att företräda' var en omskrivning, inte en synonym; utbytt mot bemyndigande och mandat."),

"förmäla": ("Meddela eller omtala ; äv. ålderdomligt gifta bort",
  "ngt ålderdomlig, neutral", ["omtala", "förtälja"],
  "Vad som sedan hände %s inte historien." % (B % "förmäler"),
  "av lågtyska vormälen 'lova bort' — jfr gemål och giftermål",
  "Båda betydelserna fanns och stämmer. Registret samlat: kortet hade 'litterär ; arkaisk' i två led, SO ger **ålderdomligt** respektive **formellt**. Exempelmeningen är nu SO:s egen, eftersom *historien förmäler* är det enda sammanhang där ordet fortfarande möts i praktiken."),

"ge sig till tåls": ("Hålla sig lugn och vänta tålmodigt",
  "vardaglig, neutral", ["bärga sig", "tåla sig"],
  "Du får %s — paketet kommer i morgon." % (B % "ge dig till tåls"),
  None,
  "KÄLLA REDD UT FÖR HAND. Ingen exakt träff på uttrycket; verktyget drog in *tåls*, *ge sig* och *ge till*. Ur råträffarna: SO definierar uppslagsordet **tåla sig** som just 'ge sig till tåls', med bruklighetskommentaren **vardagligt** — vilket bekräftar kortets register. Synonymen 'vänta tålmodigt' var en omskrivning av definitionen; utbytt mot bärga sig och tåla sig, som båda är riktiga synonymer."),

"hedonism": ("Filosofisk riktning som ser lusten och njutningen som livets högsta värde",
  "formell, neutral", ["njutningslära", "lyckofilosofi"],
  "Hans %s gjorde att han alltid valde det bekväma." % (B % "hedonism"),
  "till grekiska hedoné 'njutning; nöje'",
  "PRECISERAD. Kortet sa 'livssyn' — SO och SAOL är tydliga med att det är en **filosofisk riktning**, en genomtänkt lära och inte bara en läggning. Wiktionary noterar att ordet numera även används allmänt om en njutningslysten livsstil, vilket är den betydelse exempelmeningen visar."),

"injektera": ("Spruta in ett ämne ; särskilt pumpa in material i berg eller betong för att täta eller förstärka",
  "fackspråklig, neutral", ["spruta in", "täta"],
  "Berggrunden %s med cementbruk innan tunneln sprängdes." % (B % "injekterades"),
  "av engelska inject 'spruta in' — jfr injicera",
  "ORDNING RÄTTAD. Kortet satte den medicinska betydelsen först. SO ger **enbart** byggnadsbetydelsen (förstärka eller täta jord och berggrund); SAOL har den medicinska. Uppdelningen är verklig: om kroppen säger man normalt *injicera*, om berg *injektera*. Exempelmeningen visar nu den betydelse SO faktiskt listar."),

"kotteri": ("Mindre, slutet sällskap med stark sammanhållning mot omvärlden",
  "formell, negativ", ["klick", "krets"],
  "Beslutet togs av ett litet %s inom styrelsen." % (B % "kotteri"),
  "av franska coterie, ursprungligen 'torpare under samma egendom', till fornfranska cote 'koja'",
  "Innehållet stämde. Definitionen är nu SO:s ordagranna — det avgörande ledet är **mot omvärlden**, alltså att slutenheten är riktad utåt och inte bara en följd av att gruppen är liten."),

"kurtisera": ("Uppvakta och flörta med",
  "ngt ålderdomlig, neutral", ["uppvakta", "flörta med"],
  "Han %s henne i bersån." % (B % "kurtiserade"),
  "av franska courtiser 'göra någon sin kur', till cours 'hov'",
  "REGISTER RÄTTAT MOT KÄLLAN. Kortet sa 'formell'. SO:s bruklighetskommentar lyder **mest vid beskrivning av äldre förhållanden** och SAOL märker ordet **åld.** — det är alltså inte högtidligt utan gammaldags, vilket är en annan sak. Man kurtiserar i en berså, inte i ett protokoll."),

"kvadrant": ("En fjärdedel av ett koordinatsystem ; en fjärdedels cirkel ; äldre instrument för att mäta stjärnors höjd",
  "fackspråklig, neutral", ["cirkelfjärdedel", "höjdmätare"],
  "Första %s avgränsas av x- och y-axelns positiva delar." % (B % "kvadranten"),
  "av latin quadrans 'fjärdedel' — jfr kvader och kvadrat",
  "SAKNAD BETYDELSE. Kortet hade koordinatsystemet och instrumentet men hoppade över den geometriska mittbetydelsen: **en sektor som utgör en fjärdedel av en cirkel**. Den binder ihop de två andra — instrumentet heter kvadrant just för att det är format som en fjärdedels cirkel. Synonymen 'sektor' var för vid (en sektor kan ha vilken vinkel som helst)."),

"laminera": ("Bygga upp i skikt ; särskilt limma en skyddande plastfolie på",
  "fackspråklig, neutral", ["skiktlimma", "plasta in"],
  "Ett %s bokomslag håller betydligt längre." % (B % "laminerat"),
  "se laminat",
  "BREDDAD. Kortet gav bara plastfolien. SO:s första betydelse är **utföra i form av laminat** och SAOL 'bygga upp el. tillverka av flera skikt' — därför talar man om laminerat järn och laminerat trä, som inte har någon plast alls. Plastningen är specialfallet, inte definitionen."),

"lågmäld": ("Som framförs med låg röst ; om person: som talar tyst, försynt och diskret",
  "neutral, neutral", ["dämpad", "försynt"],
  "Ett %s sorl hördes från salen." % (B % "lågmält"),
  "till låg och mäla 'tala' — jfr fåmäld",
  "SAKNAD BETYDELSE + REGISTER. Kortet beskrev bara personen. SO:s **första** betydelse gäller det som sägs: ett lågmält sorl, en lågmäld konversation, en lågmäld kritik — och den bildliga användningen (*en lågmäld skildring*) bygger på just den. Registret rättat från 'vardaglig' till neutral; ingen källa markerar ordet."),

"minuskel": ("Liten bokstav, gemen — särskilt i äldre handskrifter",
  "fackspråklig, neutral, historia", ["gemen", "liten bokstav"],
  "Texten skrevs helt i %s, utan en enda versal." % (B % "minuskler"),
  "av latin minuscula littera 'ganska liten bokstav', till minusculus 'något mindre'",
  "REGISTER RÄTTAT. Kortet sa 'formell'. SO:s bruklighetskommentar är **mest vid beskrivning av äldre förhållanden** och SAOL definierar rakt av 'liten bokstav i äldre texter'. Ordet är alltså paleografiskt — i vanlig text säger man gemen. Motsatsen är versal (majuskel)."),

"mättsam": ("Som man blir mätt av",
  "neutral, neutral", ["mättande", "matig"],
  "Pannkakorna var goda och %s." % (B % "mättsamma"),
  None,
  "Innehållet stämde. Definitionen är nu SO:s ordagranna, som är kortare och tydligare än kortets 'ger en känsla av fullhet'. Synonymen *matig* tillagd ur synonymer.se — den är vanligare i tal och fångar samma sak."),

"oförblommerad": ("Som framförs utan omskrivningar, rakt på sak",
  "formell, neutral", ["oförtäckt", "osminkad"],
  "Han uttalade sin %s mening om de höga skatterna." % (B % "oförblommerade"),
  "till förblomma 'linda in i vackra ord', till blomma i betydelsen 'utsmyckning'",
  "Innehållet stämde. Etymologin tillagd, och den är ovanligt användbar här: att *förblomma* var att pryda ut med blomsterspråk, så oförblommerad betyder ordagrant **utan blomsterspråk**. Det gör ordet begripligt i stället för bara långt."),

"oredlig": ("Som inte följer moraliskt godtagbara metoder",
  "formell, negativ", ["ohederlig", "bedräglig"],
  "Han dömdes för %s förfarande med bolagets pengar." % (B % "oredligt"),
  "fornsvenska oredheliker; till redlig 'rättrådig'",
  "PRECISERAD. Kortet sa 'ohederlig, laglös'. **Laglös** är fel led — oredlighet handlar om moral och metod, inte om att stå utanför lagen; SO: 'som inte följer (moraliskt) godtagbara metoder'. Ordet lever framför allt i juridikens *oredlighet mot borgenärer*, där just förfarandet är det klandervärda."),

"parafras": ("Fri omskrivning av en text med det ursprungliga innehållet bevarat ; äv. fri bearbetning av en känd melodi",
  "formell, neutral", ["omskrivning", "omdiktning"],
  'Eyvind Johnsons "Strändernas svall" är en %s på Odysséen.' % (B % "parafras"),
  "av grekiska paraphrasis 'omskrivning'",
  "SAKNAD BETYDELSE. Kortet hade bara textbetydelsen. Både SO och SAOL ger även **musikbetydelsen** — en fri bearbetning av en känd melodi — och SO noterar att ordet används likadant inom bildkonsten. Det avgörande ledet i definitionen är att innehållet **bevaras**; annars är det inte en parafras utan en ny text."),

"pilt": ("Liten pojke",
  "ngt ålderdomlig, neutral", ["gosse", "parvel"],
  "En %s i sjömanskostym stod på bryggan." % (B % "pilt"),
  "fornsvenska pilter; av osäkert ursprung",
  "REGISTER RÄTTAT. Kortet sa 'litterär'. SO:s bruklighetskommentar är **något ålderdomligt** och SAOL märker **åld.** Skillnaden spelar roll: litterär betyder att ordet hör hemma i skriven stil, ålderdomlig att det hör hemma i en annan tid. Pilt möts i sagor och äldre text, inte i modern skönlitteratur."),

"probera": ("Pröva ; särskilt fastställa halten av guld, silver eller platina i något",
  "fackspråklig, neutral", ["pröva", "haltbestämma"],
  "Guldsmeden %s ringen för att fastställa halten." % (B % "proberade"),
  "fornsvenska probera; av latin probare 'pröva; godkänna' — jfr prov",
  "SAKNAD BETYDELSE. Kortet hade bara 'pröva, testa', vilket gör ordet till en onödig synonym till *prova*. Både SO och SAOL ger fackbetydelsen: **fastställa ädelmetallhalt**. Det är den som motiverar att ordet finns — därav proberguld, probersten och Probermästaren. Exempelmeningen visade tidigare en kock som smakade soppa, alltså just den betydelse där ordet är överflödigt."),

"representativ": ("Som utgör ett typiskt och lämpligt exempel på något ; äv. om person: som på ett värdigt sätt kan företräda",
  "formell, neutral", ["typisk", "belysande"],
  "Undersökningen byggde på ett %s urval av befolkningen." % (B % "representativt"),
  "till representera; av latin repraesentare 'göra närvarande'",
  "Båda betydelserna fanns och stämmer. Noterat att SO markerar **något ålderdomligt** för den andra betydelsen (*en representativ dam*) — den första, om urval och exempel, är fullt levande och är den Adam möter i statistik och på HP."),

"sauna": ("Bastu",
  "neutral, neutral", ["bastu", "badstuga"],
  "De avslutade träningen med en stund i %s." % (B % "saunan"),
  "av finska sauna med samma betydelse",
  "REGISTER RÄTTAT. Kortet märkte ordet **vardaglig**; varken SO eller SAOL ger någon bruklighetskommentar — båda översätter rakt av till 'bastu'. Om något är *sauna* den mer högtidliga eller finskklingande varianten, inte den vardagligare."),

"självskriven": ("Som obestridligen har eller kommer att få en viss funktion",
  "formell, neutral", ["självklar", "given"],
  "Han var den %s efterträdaren på ordförandeposten." % (B % "självskrivne"),
  "till själv och skriven, egentligen 'inskriven av sig själv'",
  "Innehållet stämde. Definitionen är nu SO:s, som är precisare än 'självklar, given': ordet handlar specifikt om att **inneha eller få en funktion eller plats**, inte om självklarheter i allmänhet. Man är självskriven till ett uppdrag — ett faktum kan inte vara självskrivet."),

"sjåpig": ("Överdrivet rädd eller blyg, ofta på ett tillgjort sätt",
  "vardaglig, negativ", ["pjoskig", "pryd"],
  "Han var alltid %s när det gällde att gå till doktorn." % (B % "sjåpig"),
  None,
  "Innehållet och registret stämde — SAOL märker **vard.** och kortet hade rätt. Synonymen 'tillgjort blyg' var en upprepning av definitionen; utbytt mot *pjoskig* och *pryd*, som är riktiga synonymer och täcker ordets två sidor (rädslan respektive tillgjordheten)."),

"tes": ("Påstående om ett sakförhållande som i princip går att bevisa eller vederlägga",
  "formell, neutral", ["lärosats", "påstående"],
  "Han drev %s att kapitalismen och socialismen närmar sig varandra." % (B % "tesen"),
  "via latin av grekiska thesis 'uppställning; sättande' — jfr antites, hypotes och syntes",
  "Innehållet stämde. Preciserat att det avgörande är att påståendet ska gå att **pröva** — en tes som inte kan vederläggas är ingen tes. I filosofiska sammanhang står den mot sin antites, vilket etymologin gör synlig. (Uppslaget drog även in ordet *te*; den träffen är bortsorterad.)"),

"transparent": ("Genomskinlig ; bildligt om verksamhet: öppen för insyn",
  "neutral, neutral", ["genomskinlig", "öppen"],
  "Företaget lovade en %s redovisning av alla kostnader." % (B % "transparent"),
  "till latin transparere 'skina igenom' — jfr transparang",
  "Innehållet stämde med SO:s två betydelser. Preciserat att den andra är **bildlig** och gäller insyn i verksamhet — det är den betydelsen som dominerar i dagens svenska och den enda som förekommer i myndighets- och företagsspråk."),

"uppbjuda": ("Ta fram och utnyttja allt man har av en förmåga",
  "formell, neutral", ["mobilisera", "uppamma"],
  "Han fick %s hela sin viljestyrka." % (B % "uppbjuda"),
  None,
  "Innehållet stämde. Definitionen skärpt mot SO: det ligger ett **lyckas** i ordet — man uppbjuder sina sista krafter och får fram dem. Ordet används nästan uteslutande om inre resurser (krafter, viljestyrka, tålamod), vilket exempelmeningen nu visar."),

"vidlåda": ("Sitta fast vid ; oftast bildligt: vara förknippad med som en brist",
  "ngt ålderdomlig, neutral", ["häfta vid", "vara behäftad med"],
  "De brister som %s systemet måste åtgärdas." % (B % "vidlåder"),
  "fornsvenska vidherludha; till låda 'fastna'",
  "REGISTER + PRECISERING. Kortet sa 'litterär'; SO:s bruklighetskommentar är **något ålderdomligt**. Viktigare: SO markerar 'ofta bildligt', och den bildliga användningen har nästan alltid **negativ** laddning — det är brister och osäkerheter som vidlåder något, sällan förtjänster."),

"villervalla": ("Tillstånd av fullständig oordning",
  "neutral, neutral", ["virrvarr", "oreda"],
  "I den allmänna %s lyckades gärningsmannen undkomma." % (B % "villervallan"),
  "äldre även villevalla; troligen bildat till vill 'vilsen', av samma typ som virrvarr",
  "REGISTER. Kortet märkte ordet **vardaglig**; ingen av SO, SAOL eller Wiktionary ger någon bruklighetskommentar. Etymologin tillagd — ordet är en s.k. reduplikation, samma ordbildning som *virrvarr* och *mischmasch*, vilket förklarar varför det låter som det gör."),

"ändamålsenlig": ("Som lämpar sig väl för sitt ändamål",
  "formell, neutral", ["lämplig", "funktionell"],
  "För fjällvandring behövs %s klädsel." % (B % "ändamålsenlig"),
  None,
  "Innehållet stämde. Synonymen *praktisk* ströks: en sak kan vara praktisk utan att passa sitt syfte, och ändamålsenlig utan att vara bekväm — ordet mäter **passform mot ett syfte**, inte behändighet. Ersatt med funktionell."),

"ömka": ("Känna eller uttrycka medlidande med ; äv. reflexivt: beklaga sig",
  "ngt ålderdomlig, neutral", ["beklaga", "tycka synd om"],
  "Han ville ha hjälp, men han ville inte bli %s." % (B % "ömkad"),
  "fornsvenska ömka; till öm i den äldre betydelsen 'olycklig' — jfr ynka",
  "SAKNAD BETYDELSE. Kortet hade bara den transitiva. SO ger även den **reflexiva**: *de ömkade sig över släktingens olycksöde* — alltså att beklaga sig, inte att tycka synd om någon annan. De två drar åt olika håll och blandas lätt ihop. Exempelmeningen är SO:s egen och visar att ordet oftast möts i passiv form."),

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
