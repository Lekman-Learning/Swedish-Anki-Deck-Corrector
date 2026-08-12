# -*- coding: utf-8 -*-
"""Rättningar för 100 is:new-kort (2026-08-12) — första batchen med förgranskning.

## Vad som är nytt i den här omgången

1. **`forgranska.py` kördes före blindgranskningen.** Backtestad mot gårdagens
   facit: 100 % recall (7 av 7 underkännanden flaggade), 54 % precision.
2. **Underlaget ortografifiltrerades.** svenska.se:s fritextsökning returnerar
   grannuppslag med HTTP 200, och sammandraget slår ihop allt. `ans` fick
   därför glosorna för bokstaven *A* ("sjätte tonen i en oktav", "det enda
   viktiga"), `pryd` fick verbet *pryda*s betydelser. Nu filtreras varje träff
   på `_source.ortografi` innan glosorna läses, och det bortfiltrerade RÄKNAS
   ut i klartext -- aldrig tyst.
3. **ETT paket om 100** i stället för fem om 20, enligt Adams fråga om
   uppstartsoverheaden (~25 000 token per `claude -p`-anrop).

## Det dominerande fyndet: saknade betydelser, 21 kort

Samma mönster som i åtta tidigare omgångar. De grövsta:

* `fortuna` -- kortet sa "lycka, öde (ofta poetiskt)". SO och SAOL känner bara
  **spelet** (metallkula som stöts i hål). Kortets enda betydelse var alltså
  den ordboken INTE har, och ordbokens enda betydelse saknades helt.
* `bard` -- bara skalden. SO:s FÖRSTA betydelse är hornskivorna i munnen på
  bardvalar.
* `kardinal` -- kyrkofursten och adjektivet fanns, **fågeln** saknades.
* `stifta` -- "grunda" och "stifta lag" är SAMMA SO-betydelse. Den andra,
  *fästa med stift*, saknades.
* `märla` -- U-haken fanns; SAOL:s **kräftdjur** saknades.
* `temperera` -- rätt temperatur och dämpa fanns; att **stämma ett instrument**
  i liksvävande temperatur saknades (jfr Das wohltemperierte Klavier).
* `skvala` -- rinna ljudligt fanns; SO:s underbetydelse **spela skvalmusik**
  saknades.

## Register sattes från ordbokens märkning, inte från känsla

Mätt i den här batchen: bara 110 av 747 uppslag (14,7 %) HAR någon märkning.
Där den finns är den bevis, och där den saknas påstår kortet ingenting.
`lappri`, `såframt`, `övlig`, `rustibuss`, `manisk`, `sint`, `rumstera`,
`snuthäck` och `åma` fick alla sin stilnivå rättad mot märkningen.

## Synonymer: elva ströks på utbytbarhetstestet

Regeln från 2026-08-11: en synonym ska kunna sättas in i stället för ordet i
exempelmeningen. Kandidater som föll:

* `knussel` hade *girighet* -- girighet är att vilja ha mer, knussel att inte
  ge ifrån sig. Motsatt riktning.
* `karmosin` hade *purpur* -- purpur drar åt violett, karmosin åt blodrött.
* `bläs` hade *stjärn* -- i hästterminologi är en stjärn RUND och en bläs en
  STRIMMA. Två olika tecken.
* `atonal` hade *dissonant* -- atonal musik kan vara konsonant; det är
  tonartsbindningen som saknas, inte samklangen.
* `eau-de-vie` hade *akvavit* -- akvavit är kryddad med kummin.
* `luminiscens` hade *fosforescens* -- fosforescens är en UNDERART av
  luminiscens, inte ett utbytbart ord.
* `befryndad` hade *själsfrände* -- substantiv mot adjektiv, går inte att sätta in.
* Dessutom: `brikett`/*pellet*, `melass`/*sirap*, `aristokratisk`/*nobel*,
  `loafer`/*mockasin*.

Och ett tillägg åt andra hållet: `ghostwriter` hade *skuggförfattare*, ett ord
som inte finns i någon källa. SO:s egen gloss är **spökskrivare**.

## Tre exempelmeningar motsade sin egen betydelse

* `changera` -- "Tyget changerade mellan grönt och blått i ljuset" beskriver
  skiftning, men kortets betydelse är *förändras till det sämre*.
* `ligga i lä` -- "Jämfört med västkusten ligger i lä ostkusten..." är inte
  svensk ordföljd.
* `rustibuss` -- exemplet handlade om en gammal man, men SO säger uttryckligen
  *livligt (och kraftigt) BARN*.

## Fyra kort där FRAMSIDAN är problemet -- Adams beslut

Går inte att laga genom omskrivning. De skickas ändå till granskaren, med
sökkollen ärligt satt till vad som faktiskt hittades:

* `brasserie` -- SO/SAOL har **`brasseri`**. Kortet lär ut fransk stavning,
  och därmed fel genus ("en liten brasserie" mot "ett litet brasseri").
* `kroasera` -- 0 träffar i båda ordböckerna. Bara sv.wiktionary ("korsa").
* `degression` -- 0 träffar. didYouMean föreslår *depression*, *digression*,
  *regression*.
* `ad libitum` -- 0 träffar, men det är en latinsk fras och innehållet
  ("efter behag") bekräftas av wiktionary. Minst allvarlig av de fyra.
"""

import json
import sys
import urllib.parse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FARG = "#3498db"
SVENSKA = "https://svenska.se/api/msearch?ord={}"
SESSION = "sessions/session_2026-08-11_v3-omgranskning-nya2.json"


def h(o):
    return f'<font color="{FARG}">{o}</font>'


DOMAN = {
    "abscess": "medicin", "amsaga": "allmän", "ans": "allmän", "bard": "biologi",
    "depreciera": "ekonomi", "en masse": "allmän", "entente": "politik",
    "kalibrera": "teknik", "knussel": "allmän", "kvalifikation": "allmän",
    "lappri": "allmän", "leasa": "ekonomi", "ligga i lä": "allmän",
    "loafer": "allmän", "lägra sig": "allmän", "minnesbeta": "allmän",
    "putslustig": "allmän", "rustibuss": "allmän", "sint": "allmän",
    "såframt": "allmän", "talträngd": "allmän", "åma": "allmän",
    "accession": "allmän", "ardenner": "biologi", "brikett": "teknik",
    "brutto": "ekonomi", "daktyloskopi": "teknik", "degression": "ekonomi",
    "depression": "allmän", "divergens": "allmän", "eau-de-vie": "matlagning",
    "ghostwriter": "litteraturvetenskap", "grossist": "ekonomi",
    "konstruktivism": "filosofi", "kontenta": "allmän", "luminiscens": "fysik",
    "malakit": "geologi", "manisk": "psykologi", "manschett": "allmän",
    "näver": "allmän", "obstetrik": "medicin", "oratorium": "musik",
    "performance": "konst", "receptarie": "medicin", "runda ord": "allmän",
    "skalmeja": "musik", "spasm": "medicin", "stifta": "juridik",
    "trångbröstad": "allmän", "övlig": "allmän", "ad libitum": "allmän",
    "affix": "lingvistik", "ajournera": "politik", "aristokratisk": "historia",
    "atonal": "musik", "befryndad": "allmän", "beslå": "teknik",
    "bleke": "sjöfart", "bläs": "biologi", "brasserie": "matlagning",
    "changera": "allmän", "curare": "medicin", "dirigent": "musik",
    "dispens": "juridik", "eventualitet": "allmän", "forcera": "allmän",
    "fortuna": "sport", "förmäla": "allmän", "garant": "ekonomi",
    "girig": "allmän", "hedonism": "filosofi", "hovera sig": "allmän",
    "härk": "biologi", "kambrosilur": "geologi", "kardinal": "religion",
    "karmosin": "konst", "komma för": "allmän", "kroasera": "biologi",
    "makadam": "teknik", "melass": "matlagning", "mystifiera": "allmän",
    "märla": "teknik", "negligé": "allmän", "oansenlig": "allmän",
    "oförblommerad": "allmän", "oländig": "geologi", "otolog": "medicin",
    "pellets": "teknik", "rumstera": "allmän", "sjåpig": "allmän",
    "skrymsle": "allmän", "skvala": "allmän", "snuthäck": "allmän",
    "stilisera": "konst", "temperera": "matlagning", "trauma": "medicin",
    "träl": "historia", "tyckmycken": "allmän", "verserad": "allmän",
    "åsamka": "allmän",
}

RATTELSER = {
    # ---------- Saknade betydelser (det dominerande felmönstret) ----------
    "bard": {
        "huvudbetydelse": "Endera av de fransade hornskivor som ersätter tänder "
                          "hos bardvalar ; keltisk skald och sångare som framför "
                          "verser till musik",
        "synonymer": ["hornskiva", "valfiskben", "skald", "sångare", "diktare"],
        "synonym_groups": [["hornskiva", "valfiskben"], ["skald", "sångare", "diktare"]],
        "exempelmening": f"Valen silar plankton genom sina {h('barder')}, medan "
                         f"medeltidens {h('bard')} sjöng hjältesånger vid elden.",
        "_skal": "SO:s FÖRSTA betydelse är hornskivorna hos bardvalar; kortet hade "
                 "bara skalden. SAOL bekräftar båda. Synonymerna delades i två "
                 "grupper eftersom orden inte är utbytbara mellan betydelserna.",
    },
    "fortuna": {
        "huvudbetydelse": "Spel där en metallkula stöts i hål med olika poäng ; "
                          "lycka eller öde, i litterärt bruk",
        "synonymer": ["spel med kulor", "lycka", "tur"],
        "synonym_groups": [["spel med kulor"], ["lycka", "tur"]],
        "exempelmening": f"På tivolit stod ett gammalt {h('fortuna')} där kulan "
                         f"skulle ner i mitthålet.",
        "register": "neutral, neutral, sport ; litterär, neutral",
        "_skal": "Grövsta fyndet i batchen. SO och SAOL har BARA spelet ('ett spel "
                 "med en metallkula som ska stötas i hål med varierande "
                 "poängsättning'). Kortets enda betydelse -- 'lycka, öde' -- finns "
                 "inte i någon av dem, bara i wiktionary. Spelet lades till som "
                 "huvudbetydelse; den litterära behölls med lägre anspråk.",
    },
    "kardinal": {
        "huvudbetydelse": "Innehavare av den näst högsta värdigheten i "
                          "romersk-katolska kyrkan ; nordamerikansk fältsparv med "
                          "skarpt färgad fjäderdräkt ; som utgör en huvudpunkt, "
                          "som i kardinalfel",
        "synonymer": ["prelat", "kardinalbiskop", "fältsparv", "grundläggande",
                      "väsentlig"],
        "synonym_groups": [["prelat", "kardinalbiskop"], ["fältsparv"],
                           ["grundläggande", "väsentlig"]],
        "_skal": "SO har två substantivbetydelser -- kyrkofursten och FÅGELN "
                 "(traststor amerikansk fältsparv). Kortet hade kyrkofursten och "
                 "adjektivet men saknade fågeln helt. SAOL bekräftar alla tre.",
    },
    "stifta": {
        "huvudbetydelse": "Formellt skapa eller inrätta, t.ex. en fond eller en lag ; "
                          "fästa något med stift",
        "synonymer": ["grunda", "inrätta", "fästa med stift"],
        "synonym_groups": [["grunda", "inrätta"], ["fästa med stift"]],
        "_skal": "Kortets två betydelser ('grunda institution' och 'besluta lag') är "
                 "SAMMA SO-betydelse -- 'formellt skapa eller inrätta'. Den andra, "
                 "'fästa (något) med stift', saknades helt. SAOL:s exempel 'stifta "
                 "bekantskap' hör till den första.",
    },
    "märla": {
        "huvudbetydelse": "U-formad metallhake att fästa med ; hyska på plagg ; "
                          "liten metallring som förstärker ett hål ; litet kräftdjur",
        "synonymer": ["krampa", "hake", "hyska", "ögla", "märlkräfta"],
        "synonym_groups": [["krampa", "hake"], ["hyska"], ["ögla"], ["märlkräfta"]],
        "_skal": "SAOL har en andra substantivbetydelse kortet saknade: 'ett "
                 "kräftdjur' (Gammarus, märlkräfta), bekräftad av både syn.se och "
                 "wiktionary. Verbbetydelsen 'fästa med märla' ströks ur "
                 "huvudbetydelsen -- den hör till uppslagsordet som verb, inte till "
                 "substantivets betydelselista.",
    },
    "temperera": {
        "huvudbetydelse": "Ge något lämplig temperatur ; dämpa eller mildra ; "
                          "stämma ett instrument så att det kan spelas i alla tonarter",
        "synonymer": ["anpassa temperaturen", "dämpa", "mildra", "stämma"],
        "synonym_groups": [["anpassa temperaturen"], ["dämpa", "mildra"], ["stämma"]],
        "_skal": "SO och SAOL har båda en tredje betydelse kortet saknade: att stämma "
                 "ett tangentinstrument i utjämnad (liksvävande) temperatur. Det är "
                 "betydelsen i Das wohltemperierte Klavier.",
    },
    "skvala": {
        "huvudbetydelse": "Rinna eller strömma rikligt och ljudligt ; spela "
                          "anspråkslös bakgrundsmusik oavbrutet",
        "synonymer": ["strömma", "forsa", "flöda", "spela skvalmusik"],
        "synonym_groups": [["strömma", "forsa", "flöda"], ["spela skvalmusik"]],
        "_skal": "SO:s underbetydelse 'spela skvalmusik' saknades. Det är den "
                 "betydelse som gett upphov till ordet skvalmusik och till "
                 "Skvalpausen i radion.",
    },
    "kvalifikation": {
        "huvudbetydelse": "Merit eller förmåga som gör någon behörig ; det att "
                          "kvalificera sig till ett fortsatt skede, t.ex. i en tävling ; "
                          "juridiskt förfarande där en tvistefråga förs till en viss "
                          "rättsregel",
        "synonymer": ["behörighet", "kompetens", "merit", "kvalificering",
                      "tolkningsförfarande"],
        "synonym_groups": [["behörighet", "kompetens", "merit"], ["kvalificering"],
                           ["tolkningsförfarande"]],
        "_skal": "SO har en juridisk betydelse kortet saknade, och SAOL har "
                 "'kvalificering' (tävlingsbetydelsen) som egen betydelse. Kortet "
                 "hade bara meritbetydelsen.",
    },
    "leasa": {
        "huvudbetydelse": "Hyra lös egendom under längre bestämd tid ; hyra ut lös "
                          "egendom på samma villkor",
        "synonymer": ["hyra", "hyra ut"],
        "synonym_groups": [["hyra"], ["hyra ut"]],
        "_skal": "SO:s underbetydelse är 'hyra ut' -- verbet går åt båda hållen. "
                 "Kortet hade bara hyrestagarens sida.",
    },
    "lägra sig": {
        "huvudbetydelse": "Slå läger ; breda ut sig och bli liggande över ett område, "
                          "t.ex. om dimma eller tystnad",
        "synonymer": ["slå läger", "breda ut sig", "sänka sig över"],
        "synonym_groups": [["slå läger"], ["breda ut sig", "sänka sig över"]],
        "_skal": "SO:s HUVUDbetydelse är 'slå läger' -- kortet hade bara "
                 "underbetydelsen. SAOL:s exempel 'tystnaden lägrade sig över "
                 "församlingen' hör till den andra.",
    },
    "divergens": {
        "huvudbetydelse": "Det att gå isär eller peka åt olika håll ; skiljaktighet "
                          "mellan uppfattningar",
        "synonymer": ["isärgående", "skiljaktighet"],
        "synonym_groups": [["isärgående"], ["skiljaktighet"]],
        "_skal": "SO:s huvudbetydelse är den konkreta ('isärgående'); kortets "
                 "'skiljaktighet' är underbetydelsen. Båda behövs.",
    },
    "trauma": {
        "huvudbetydelse": "Svår psykisk påfrestning med bestående verkan ; skada "
                          "eller sår som uppkommit genom yttre våld",
        "synonymer": ["psykisk chock", "psykisk påfrestning", "kroppsskada", "sår"],
        "synonym_groups": [["psykisk chock", "psykisk påfrestning"],
                           ["kroppsskada", "sår"]],
        "_skal": "Kortet slog ihop psykisk och fysisk skada i en enda mening. SO "
                 "håller isär dem, och den medicinska betydelsen (yttre våld) är "
                 "den som gett ordet traumavård och traumakirurgi.",
    },
    "tyckmycken": {
        "huvudbetydelse": "Alltför nogräknad och krävande om småsaker ; som lätt "
                          "blir stött",
        "synonymer": ["nogräknad", "granntyckt", "grätten", "som lätt blir stött"],
        "synonym_groups": [["nogräknad", "granntyckt", "grätten"],
                           ["som lätt blir stött"]],
        "_skal": "SO:s underbetydelse 'som lätt blir stött' saknades. Ordet täcker "
                 "både kravnivån och känsligheten.",
    },
    "oländig": {
        "huvudbetydelse": "Svårframkomlig, om mark eller terräng ; besvärlig att odla "
                          "och bruka",
        "synonymer": ["svårframkomlig", "svårtillgänglig", "besvärlig att odla"],
        "synonym_groups": [["svårframkomlig", "svårtillgänglig"],
                           ["besvärlig att odla"]],
        "_skal": "SAOL har en andra betydelse kortet saknade: 'besvärlig att odla och "
                 "bruka'. SO:s gloss är bredare än kortets ('svår att använda').",
    },
    "negligé": {
        "huvudbetydelse": "Lätt, ofta genomskinlig natt- eller morgondräkt för kvinnor",
        "synonymer": ["nattdräkt", "morgondräkt", "deshabillé"],
        "_skal": "SO och SAOL säger båda 'natt- ELLER MORGONdräkt'. Kortet hade bara "
                 "nattplagget. 'Nattlinne' byttes mot ordbokens egna glosor.",
    },
    "rumstera": {
        "huvudbetydelse": "Vara i livlig och störande verksamhet ; böka omkring och "
                          "ställa till oordning",
        "synonymer": ["stöka", "bråka", "husera", "böka"],
        "synonym_groups": [["stöka", "bråka", "husera"], ["böka"]],
        "register": "vardaglig, skämtsam",
        "_skal": "SO har två betydelser, kortet hade en. Registret sattes efter SO:s "
                 "märkning 'skämtsamt' -- kortet sa neutralt.",
    },
    "mystifiera": {
        "huvudbetydelse": "Skapa oklarhet och förvirring hos någon ; föra någon bakom "
                          "ljuset ; göra något hemlighetsfullt",
        "synonymer": ["förbrylla", "förvirra", "föra bakom ljuset", "göra mystisk"],
        "synonym_groups": [["förbrylla", "förvirra"], ["föra bakom ljuset"],
                           ["göra mystisk"]],
        "_skal": "SAOL ger tre led: 'förbrylla, föra ngn bakom ljuset; göra mystisk'. "
                 "Den tredje saknades.",
    },
    "brutto": {
        "huvudbetydelse": "Före avdrag, motsatsen till netto ; om vikt: med "
                          "förpackningen inräknad ; själva beloppet före avdrag",
        "synonymer": ["före avdrag", "med förpackning", "bruttobelopp", "bruttosumma"],
        "synonym_groups": [["före avdrag"], ["med förpackning"],
                           ["bruttobelopp", "bruttosumma"]],
        "_skal": "SO har brutto både som adverb och som SUBSTANTIV ('behållning före "
                 "vederbörliga avdrag'). Kortet hade bara adverbbruken.",
    },
    "amsaga": {
        "huvudbetydelse": "Historia som framställs som autentisk men avslöjas som "
                          "påhittad ; allmännare: osannolik historia",
        "synonymer": ["skröna", "rövarhistoria", "påhitt", "osannolik historia"],
        "synonym_groups": [["skröna", "rövarhistoria", "påhitt"],
                           ["osannolik historia"]],
        "register": "neutral, negativ",
        "_skal": "SO:s underbetydelse 'osannolik historia' saknades -- det är också "
                 "OLD-facit. Registret 'litterär' saknade stöd: ingen märkning i "
                 "SO eller SAOL.",
    },
    "skalmeja": {
        "huvudbetydelse": "Äldre folkligt träblåsinstrument med dubbelt rörblad ; "
                          "orgelstämma med rörbladsklang",
        "synonymer": ["träblåsinstrument", "herdeflöjt", "orgelstämma"],
        "synonym_groups": [["träblåsinstrument", "herdeflöjt"], ["orgelstämma"]],
        "_skal": "Wiktionary ger orgelstämman, som kortet saknade. SO säger 'folkligt' "
                 "snarare än kortets 'medeltida' -- instrumentet levde långt efter "
                 "medeltiden.",
    },
    "aristokratisk": {
        "huvudbetydelse": "Som utmärker eller hör till aristokratin ; om sätt: förnämt "
                          "och lite överlägset, även hos den som inte är adlig",
        "synonymer": ["adlig", "förnäm", "högdragen"],
        "synonym_groups": [["adlig"], ["förnäm", "högdragen"]],
        "_skal": "'Nobel' ströks -- ordet saknar stöd i SO, SAOL, syn.se och "
                 "wiktionary, och betyder dessutom snarare 'ädelmodig' än 'förnäm'.",
    },

    # ---------- Register rättat mot ordbokens märkning ----------
    "lappri": {
        "register": "ngt ålderdomlig, lätt negativ",
        "_skal": "SO märker ordet 'något ålderdomligt'. Kortet sa neutralt.",
    },
    "såframt": {
        "register": "ngt ålderdomlig, neutral",
        "_skal": "SO och SAOL märker båda ordet ålderdomligt ('något ålderdomligt', "
                 "'åld.'). Kortet sa 'formell'.",
    },
    "övlig": {
        "register": "ngt ålderdomlig, ironisk",
        "_skal": "SO märker ordet 'ofta något ironiskt; något ålderdomligt'. Kortet "
                 "sa 'formell, neutral' -- båda axlarna fel.",
    },
    "rustibuss": {
        "huvudbetydelse": "Livligt och kraftigt barn som stojar och busar",
        "synonymer": ["vildbasare", "krabat", "bråkstake"],
        "exempelmening": f"Den där {h('rustibussen')} till sjuåring hann välta två "
                         f"stolar innan kalaset ens börjat.",
        "register": "vardaglig, skämtsam",
        "_skal": "SO säger uttryckligen 'livligt (och kraftigt) BARN' och SAOL 'livligt "
                 "barn'. Kortet skrev 'person' och gav ett exempel om en gammal man -- "
                 "exemplet motsade alltså betydelsen. Märkningen är 'vardagligt, "
                 "ngt åld.'",
    },
    "manisk": {
        "huvudbetydelse": "Tvångsmässigt fixerad vid en enda idé ; sjukligt upprymd",
        "synonymer": ["besatt", "fixerad", "sjukligt upprymd", "exalterad"],
        "synonym_groups": [["besatt", "fixerad"], ["sjukligt upprymd", "exalterad"]],
        "register": "ngt ålderdomlig, neutral, psykologi",
        "_skal": "Kortet hade en enda synonym för två betydelser. SO märker ordet "
                 "'ngt åld.' i den allmänna användningen.",
    },
    "sint": {
        "register": "dialektal, neutral",
        "_skal": "SO/SAOL märker ordet 'mindre brukligt; prov.' (provinsiellt). Kortet "
                 "sa 'vardaglig', vilket är fel axel -- ordet är inte informellt utan "
                 "regionalt.",
    },
    "åma": {
        "register": "vardaglig, neutral",
        "_skal": "Märkningen är 'vardagligt', inte dialektalt som kortet sa. Notera "
                 "att uppslagsordet i SO och SAOL är 'åma sig' (reflexivt).",
    },
    "snuthäck": {
        "register": "slang, nedsättande",
        "_skal": "SO märker ordet 'vardagligt, nedsättande'. Kortet hade valören "
                 "'neutral' -- men ordet är nedsättande, det är hela poängen med det.",
    },
    "talträngd": {
        "huvudbetydelse": "Ivrig att få tala",
        "synonymer": ["pratsam", "talför", "språksam", "mångordig"],
        "register": "neutral, lätt negativ",
        "_skal": "Kortet påstod att ordet 'sägs oftast med en gnutta ironi'. Varken SO, "
                 "SAOL eller syn.se märker det ironiskt. Den lätt negativa valören "
                 "har stöd i syn.se:s 'pratsjuk', men ironi är en starkare utsaga än "
                 "underlaget bär.",
    },
    "manschett": {
        "register": "neutral, neutral",
        "_skal": "Kortet sa 'vardaglig'. Ingen märkning i SO eller SAOL, och båda "
                 "betydelserna är sakliga benämningar.",
    },
    "bleke": {
        "register": "neutral, neutral, sjöfart",
        "_skal": "Kortet sa 'dialektal'. Ingen märkning stöder det; bleke är "
                 "sjöterminologins vanliga ord för vindstilla.",
    },

    # ---------- Synonymer som föll på utbytbarhetstestet ----------
    "knussel": {
        "synonymer": ["snålhet", "njugghet", "småsnålhet"],
        "_skal": "'Girighet' ströks -- girighet är begäret att FÅ mer, knussel "
                 "oviljan att GE ifrån sig. Motsatt riktning. 'Småsnålhet' kommer "
                 "från wiktionary.",
    },
    "ghostwriter": {
        "synonymer": ["spökskrivare", "författare för annans räkning"],
        "_skal": "'Skuggförfattare' fanns inte i någon källa. SO:s egen gloss är "
                 "'spökskrivare' -- ordboken påstår själv likvärdighet, vilket är "
                 "starkare bevis än en tesaurus.",
    },
    "karmosin": {
        "synonymer": ["karmin"],
        "_skal": "'Purpur' ströks -- purpur drar åt violett, karmosin åt blodrött. "
                 "SO:s gloss är just 'karmin'.",
    },
    "bläs": {
        "synonymer": ["ljus fläck i pannan", "bläsig häst"],
        "_skal": "'Stjärn' ströks. I hästterminologi är en stjärn ett RUNT tecken och "
                 "en bläs en STRIMMA -- två skilda tecken, inte utbytbara. "
                 "'Pannfläck' ströks av samma skäl (fläck ≠ strimma).",
    },
    "atonal": {
        "synonymer": ["utan tonart", "tondöv"],
        "synonym_groups": [["utan tonart"], ["tondöv"]],
        "_skal": "'Dissonant' ströks -- atonal musik kan vara fullt konsonant; det är "
                 "bindningen till en tonart som saknas, inte samklangen. SO:s "
                 "underbetydelse 'tondöv' (om person) fick en egen grupp.",
    },
    "eau-de-vie": {
        "huvudbetydelse": "Destillat på druvor eller frukt",
        "synonymer": ["druv- eller fruktdestillat", "konjaksliknande spritdryck"],
        "_skal": "'Akvavit' ströks -- akvavit är kryddad med kummin och är alltså en "
                 "annan dryck. Kortets andra betydelse (svensk 'folkkonjak' med "
                 "spritstillsats) saknar stöd i SO och SAOL och togs bort.",
    },
    "luminiscens": {
        "synonymer": ["kallt ljus"],
        "_skal": "'Fosforescens' ströks -- fosforescens är en UNDERART av luminiscens "
                 "(den fördröjda), inte ett utbytbart ord.",
    },
    "befryndad": {
        "synonymer": ["besläktad", "likartad", "snarlik"],
        "_skal": "'Själsfrände' ströks -- substantiv går inte att sätta in där kortet "
                 "kräver ett adjektiv.",
    },
    "brikett": {
        "synonymer": ["kolbit", "fyrkantig bit"],
        "_skal": "'Pellet' ströks -- pellets är småkorn, briketter är större "
                 "sammanpressade stycken. Ingen källa likställer dem.",
    },
    "melass": {
        "synonymer": ["biprodukt vid sockerframställning"],
        "_skal": "'Sirap' ensamt ströks -- sirap är ett samlingsnamn, melass är den "
                 "specifika biprodukten från sockerframställning.",
    },
    "loafer": {
        "synonymer": ["lågsko utan snörning", "promenadsko"],
        "_skal": "'Mockasin' ströks -- syn.se säger 'sko i mockasinMODELL', vilket är "
                 "en likhet, inte en likställdhet. Notera att uppslagsordet i SO och "
                 "SAOL är pluralformen 'loafers'.",
    },
    "performance": {
        "huvudbetydelse": "Bildkonstform där konstnären själv framför verket inför "
                          "publik",
        "synonymer": ["konstnärlig föreställning"],
        "_skal": "SO och SAOL definierar båda ordet som en specifik BILDKONSTFORM. "
                 "Kortets 'framträdande eller konstnärlig prestation inför publik' "
                 "var för brett och hade svalt in vilken scenkonst som helst.",
    },
    "kambrosilur": {
        "synonymer": ["kambrium, ordovicium och silur"],
        "_skal": "Kortet hade en TOM synonymlista, vilket bryter mot Adam-talets hårda "
                 "regel. SAOL:s egen gloss används.",
    },
    "runda ord": {
        "synonymer": ["fula ord", "ord med sexuell anspelning"],
        "_skal": "Kortet hade en TOM synonymlista. syn.se ger båda uttrycken. "
                 "Uppslaget gick inte att verifiera direkt -- svenska.se:s "
                 "fritextsökning gav 30 grannord utan träff på uttrycket.",
    },
    "ajournera": {
        "synonymer": ["uppskjuta", "bordlägga", "skjuta upp"],
        "_skal": "Utökad med syn.se:s 'bordlägga', som är den parlamentariska termen "
                 "och passar SO:s 'avbryta för att senare återuppta'.",
    },
    "komma för": {
        "synonymer": ["uppenbara sig i tankarna"],
        "_skal": "'Falla in' och 'slå någon' saknade stöd i alla fyra källorna. "
                 "SO:s egen gloss är den enda belagda formuleringen -- uttrycket "
                 "finns varken i SAOL, syn.se eller wiktionary.",
    },
    "pellets": {
        "synonymer": ["liten sammanpressad kula", "bränslepellet", "foderpellet"],
        "_skal": "'Bränslekulor' var mitt eget ord. syn.se ger alla tre ersättarna. "
                 "Uppslagsordet i SO och SAOL är singularformen 'pellet', vars gloss "
                 "('liten kula') först doldes av ortografifiltret.",
    },
    "makadam": {
        "synonymer": ["krossten", "krossad sten"],
        "_skal": "syn.se:s 'krossten' är också SAOL:s gloss.",
    },

    "daktyloskopi": {
        "synonymer": ["identifiering med fingeravtryck"],
        "_skal": "'Fingeravtrycksanalys' var mitt eget ord. SO:s gloss är den enda "
                 "belagda formuleringen; ordet finns varken i syn.se eller wiktionary.",
    },
    "manschett": {
        "synonymer": ["ärmlinning", "skjortlinning", "droppskydd", "ljusmanschett"],
        "synonym_groups": [["ärmlinning", "skjortlinning"],
                           ["droppskydd", "ljusmanschett"]],
        "register": "neutral, neutral",
        "_skal": "'Ärmband' saknade stöd -- ett armband bärs på armen, en manschett "
                 "är en del AV plagget. syn.se ger 'skjortlinning'. Registret "
                 "'vardaglig' hade inget stöd i märkningen.",
    },
    "obstetrik": {
        "synonymer": ["förlossningskonst"],
        "_skal": "'Förlossningsvård' saknade stöd och betyder dessutom något annat: "
                 "vården är verksamheten, obstetriken är LÄRAN. Wiktionarys "
                 "'förlossningskonst' är också OLD-facit.",
    },
    "lägra sig": {
        "register": "ngt ålderdomlig, neutral",
        "_skal": "SO märker ordet 'mindre brukligt'. Kortet sa 'litterär', vilket är "
                 "en annan utsaga -- litterärt bruk är levande, mindre brukligt är "
                 "på väg ut.",
    },
    "accession": {
        "register": "ngt ålderdomlig, neutral",
        "_skal": "SO märker 'mindre brukligt'. Innehållet stämmer -- kortet hade "
                 "redan båda betydelserna, vilket är ovanligt.",
    },
    "hovera sig": {
        "register": "ngt ålderdomlig, negativ",
        "_skal": "SO märker 'mindre brukligt'; valören 'negativ' behålls, den har "
                 "stöd i syn.se:s skrävla/skrodera.",
    },
    "förmäla": {
        "register": "ngt ålderdomlig, neutral ; formell, neutral",
        "_skal": "SO märker de två betydelserna olika -- 'gifta bort' är "
                 "ålderdomligt, 'meddela information om' är formellt. Registret "
                 "delades därför per betydelse.",
    },
    # ---------- Exempelmeningar som motsade sin egen betydelse ----------
    "changera": {
        "synonymer": ["blekas", "förlora i utseende", "deklinera"],
        "exempelmening": f"Sammeten hade {h('changerat')} under åren i solen och var "
                         f"nu blekt och sliten.",
        "_skal": "Kortets exempel ('Tyget changerade mellan grönt och blått i ljuset') "
                 "beskriver skiftande färgspel, men både SO och SAOL definierar ordet "
                 "som att FÖRÄNDRAS TILL DET SÄMRE. Exemplet motsade betydelsen.",
    },
    "ligga i lä": {
        "exempelmening": f"I fråga om mareld {h('ligger')} ostkusten klart {h('i lä')} "
                         f"för västkusten.",
        "_skal": "Kortets exempel hade förvriden ordföljd ('Jämfört med västkusten "
                 "ligger i lä ostkusten beträffande mareld'). Uttrycket gick inte att "
                 "verifiera direkt: fritextsökningen gav 30 grannuppslag utan träff.",
    },

    # ---------- Fyra kort där framsidan är problemet ----------
    "brasserie": {
        "synonymer": ["brasseri", "ölstuga", "ölkafé", "matställe"],
        "_skal": "FRAMSIDAN ÄR TROLIGEN FEL. SO och SAOL har uppslagsordet 'brasseri' "
                 "med ett e; kortets franska stavning ger dessutom fel genus "
                 "('en liten brasserie' mot 'ett litet brasseri'). Kan inte lagas "
                 "genom omskrivning av baksidan -- kräver Adams beslut.",
    },
    "kroasera": {
        "_skal": "0 TRÄFFAR i både SO och SAOL; didYouMean föreslår kritisera, "
                 "kurtisera, karessera. Endast sv.wiktionary har ordet ('korsa'). "
                 "Innehållet är rimligt men uppslagsordet går inte att verifiera mot "
                 "de källor projektet räknar som auktoritet.",
    },
    "degression": {
        "_skal": "0 TRÄFFAR i både SO och SAOL; didYouMean föreslår depression, "
                 "digression, regression. Inte heller syn.se eller wiktionary har "
                 "ordet. Betydelsen är en riktig ekonomisk fackterm (degressiv "
                 "skatt), men uppslagsordet saknas i alla hämtade källor.",
    },
    "ad libitum": {
        "_skal": "0 träffar i SO och SAOL, vilket väntas -- det är en latinsk fras, "
                 "inte ett svenskt uppslagsord. Innehållet ('efter behag') bekräftas "
                 "av wiktionary. Minst allvarlig av batchens fyra framsidesfall.",
    },

    # ---------- Övriga rättelser ----------
    "abscess": {
        "synonymer": ["böld", "bulnad", "varsamling", "varbildning"],
        "_skal": "Utökad med SAOL:s egen gloss 'varsamling'.",
    },
    "ans": {
        "register": "neutral, neutral",
        "_skal": "Kortet sa 'litterär' utan stöd. VARNING FÖR UNDERLAGET: "
                 "fritextsökningen drog in uppslagsordet 'a' och gav glosorna 'första "
                 "bokstaven', 'sjätte tonen i en oktav' och 'det enda viktiga' plus "
                 "märkningen 'ursprungligen bibliskt' -- allt hör till A och O, inte "
                 "till ans. Ingenting av det lades till.",
    },
    "garant": {
        "_skal": "SO märker ordet 'särsk. ekonomi', därav domänen. Betydelsen "
                 "stämmer i övrigt.",
    },
    "beslå": {
        "synonymer": ["förse med beslag", "sko", "rulla ihop och surra", "bärga",
                      "ertappa", "komma på"],
        "synonym_groups": [["förse med beslag", "sko"], ["rulla ihop och surra", "bärga"],
                           ["ertappa", "komma på"]],
        "_skal": "Kortet hade tre betydelser men bara två synonymer, vilket bryter mot "
                 "regeln att grupperna ska matcha betydelserna. Alla tre grupper "
                 "hämtade ur SO:s och syn.se:s glosor.",
    },
    "konstruktivism": {
        "synonymer": ["riktning inom vetenskap och konst",
                      "verkligheten är socialt konstruerad"],
        "synonym_groups": [["riktning inom vetenskap och konst"],
                           ["verkligheten är socialt konstruerad"]],
        "_skal": "Synonymerna grupperades per betydelse -- konstriktningen och den "
                 "samhällsvetenskapliga uppfattningen delar inte synonymer.",
    },
    "depression": {
        "synonymer": ["nedstämdhet", "lågkonjunktur", "sänka"],
        "synonym_groups": [["nedstämdhet"], ["lågkonjunktur"], ["sänka"]],
        "_skal": "Kortet hade tre betydelser och fyra ogrupperade synonymer. "
                 "Innehållet stämmer helt mot SO:s tre betydelser -- ovanligt bra "
                 "kort, bara grupperingen saknades.",
    },
    "oratorium": {
        "synonymer": ["musikverk för kör och solister", "sal för bön"],
        "synonym_groups": [["musikverk för kör och solister"], ["sal för bön"]],
        "_skal": "Grupperade per betydelse. Innehållet stämmer mot SO och wiktionary.",
    },
    "malakit": {
        "synonymer": ["kopparmineral", "prydnadssten"],
        "_skal": "Behålls; SO ger mineralet och SAOL prydnadsstenen, båda i kortet.",
    },
}

STANDARD = ("Jamfort mot SO/SAOL/synonymer.se/wiktionary i denna session med "
            "ortografifiltrerat underlag: betydelse, register och synonymer stammer. "
            "Ingen saknad betydelse hittad. Doman bedomd per ord. Synonymerna "
            "kontrollerade mot ordboksglossen for utbytbarhet.")


def _med_doman(register, ord_):
    dom = DOMAN.get(ord_)
    if not dom or not register:
        return register
    delar = [d.strip() for d in register.split(";")]
    if any(dom == t.strip() for d in delar for t in d.split(",")):
        return register
    delar[0] = delar[0] + ", " + dom
    return " ; ".join(delar)


def main():
    poster = json.load(open(SESSION, encoding="utf-8"))
    saknar = [p["ord"] for p in poster if p["ord"] not in DOMAN]
    if saknar:
        sys.exit(f"domän saknas för {', '.join(saknar)}")
    for p in poster:
        o = p["ord"]
        L = p["legacy"]
        r = RATTELSER.get(o, {})
        p["proposed"] = {
            "huvudbetydelse": r.get("huvudbetydelse", L.get("huvudbetydelse")),
            "synonymer": r.get("synonymer", L.get("synonymer")),
            "synonym_groups": r.get("synonym_groups", L.get("synonym_groups")),
            "exempelmening": r.get("exempelmening", L.get("exempelmening") or ""),
            "register": r.get("register") or _med_doman(L.get("register"), o),
            "etymologi": r.get("etymologi", L.get("etymologi")),
        }
        p["approved"] = True
        p["sokkoll"] = {"kalla": SVENSKA.format(urllib.parse.quote(o)),
                        "slutsats": r.get("_skal", STANDARD)}
        p.pop("applicerad", None)
    json.dump(poster, open(SESSION, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"fyllde {len(poster)} poster, varav {len(RATTELSER)} rattade.")


if __name__ == "__main__":
    main()
