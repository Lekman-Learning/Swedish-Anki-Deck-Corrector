# -*- coding: utf-8 -*-
"""Spår A, 35 legacy-kort skrivna om till v2 (2026-08-12, tredje omgången).

Till skillnad från dagens två tidigare omgångar är detta inte omgranskning —
korten har aldrig varit i v2-format. `register` är `None` på alla 35, så hela
registret skrivs här; det finns inget att ärva.

## Vad som faktiskt var fel i legacy-korten

Det dominerande mönstret är **påhittade betydelser**. Legacy-korten har 2–3
`definitioner` var, men SO har oftast bara EN. De extra kom inte från en källa:

* `balalajka` — "en symbol för rysk och östeuropeisk folkmusiktradition"
* `dagsedel` — "Stig Dagermans samling med dagsverser 1944–1954"
* `tomahawk` — "en ryggbiff med ben"
* `kumulation` — en juridisk och en epidemiologisk betydelse
* `homeopati` — "en behandlingsmetod som inte har vetenskapligt stöd"

Ingen av dem finns i SO eller SAOL. De är rimliga påståenden, och två av dem
är till och med sanna om världen — men de är inte betydelser hos ordet, och
ett kort som lär in dem lär in fel svar på tentafrågan "vad betyder X".

## Tre rena sakfel

* **`eventuell`** — synonymen *sannolik*. Eventuell betyder MÖJLIG; sannolik
  betyder trolig. Kortets exempelmening innehöll dessutom inte ordet alls
  ("Det är möjligt att det regnar imorgon").
* **`nativ`** — exemplet var "Det är en nativ talare av det språket", alltså
  engelskans *native speaker*. Svenskans `nativ` betyder "som finns färdig i
  naturen" (SO) och används om metaller och material, inte om människor.
* **`vederlägga`** — synonymen *förneka*. Att förneka är att säga emot; att
  vederlägga är att BEVISA att något är fel. Skillnaden är hela ordet.

## Synonymer som var snävare eller vidare än ordet

Samma testfamilj som gårdagens `affix`/*förstavelse*:

* `cysta`/*tumör* — en cysta är en vätskefylld blåsa, en tumör är en
  cellnybildning. Inte samma sak, och `follikel` är något tredje.
* `alveol`/*lungblåsa* — lungblåsan är EN sorts alveol; tandhålan är en annan.
* `tomahawk`/*yxa*, `budgetering`/*redovisning*, `homeopati`/*pseudovetenskap*
  — vidare, fel axel, respektive ett omdöme om saken snarare än en synonym.

`bryn` fick sin ögonbryn-synonym struken av en annan anledning: den är
**cirkulär** och skulle blockeras av den hårda regeln sedan i morse.

## Tre kort där uppslagsordet inte är uppslagsordet

`vara främmande för` och `till förfång` är fraser — svenska.se:s fritextsökning
returnerar grannartiklar med HTTP 200, så ortografifiltret sorterar bort allt.
Grundorden `främmande` och `förfång` slogs därför upp separat och står som
källa. `förfång` gav SAOL "avbräck; nackdel" med exemplet *till förfång för
ngn/ngt* — alltså precis frasen.

Kvar efter rättning står sex hårda förgranskningsflaggor, alla i samma familj
och alla kontrollerade för hand: `nödsakad` (grannen *nödsakas*), `bryn`
(*bryna*) och `våras` (*sol-och-våra*) får varsin främmande träff av
fritextsökningen, men innehållet här är läst genom ortografifiltret och kommer
bara från rätt uppslag. `till förfång` får dessutom
`register_motsager_markning` för märkningen *vardagligt* — den märkningen
tillhör en av de 47 grannartiklarna, inte `förfång`, som saknar märkning helt.

**`filia` pausas.** SO, SAOL och SAOB saknar uppslagsordet helt, syn.se är tom
och Wiktionary har bara latinets *dotter*. Kortets påstådda betydelse
(dotterförsamling inom frikyrkor och ordenssällskap) har alltså inget stöd i
någon av källorna. Att skriva det ändå vore att gissa och sedan tagga gissningen
som full v3. Samma beslut som `ytong` 2026-08-11.
"""

import json
import sys
import urllib.parse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FARG = "#3498db"
SVENSKA = "https://svenska.se/api/msearch?ord={}"
SESSION = "sessions/session_2026-08-12_v3-batch.json"
PAUSAS = {"filia"}


def h(o):
    return f'<font color="{FARG}">{o}</font>'


K = {
    # kort vars källa är ett ANNAT uppslagsord än framsidan (fraser)
    "vara främmande för": "främmande",
    "till förfång": "förfång",
}

KORT = {
    "alveol": {
        "hb": "liten hålighet i kroppsvävnad, som lungblåsan eller tandhålan",
        "reg": "fackspråklig, neutral, medicin",
        "syn": [],
        "ex": f"Syret går över i blodet nere i lungornas {h('alveoler')}.",
        "skal": "SO och SAOL har EN betydelse: 'hålighet i organisk vävnad'. "
                "Legacy delade upp den i lungor/övriga organ, vilket inte är två "
                "betydelser utan två exempel. Synonymlistan tömd: lungblåsa och "
                "tandhåla är SPECIALFALL av alveol (hyponymer), och 'hålighet' "
                "ensamt är vidare — en alveol är alltid liten och i vävnad.",
    },
    "apostel": {
        "hb": "en av Jesu tolv lärjungar som spred kristendomen ; ivrig "
              "förkunnare av en lära eller rörelse",
        "reg": "neutral, neutral, religion ; neutral, neutral",
        "grupper": [["Jesu sändebud"], ["förkunnare", "missionär"]],
        "ex": f"Han blev en {h('apostel')} för den nya kostläran och predikade "
              f"den överallt.",
        "skal": "SAOL ger den religiösa betydelsen, SO den bildliga ('person som "
                "gör stora insatser för att sprida en lära eller en rörelse') — "
                "två skilda betydelser, nu åtskilda. Legacy hade 'predikanter' i "
                "pluralform mitt i en singularlista.",
    },
    "balalajka": {
        "hb": "ryskt stränginstrument med trekantig resonanslåda och lång hals",
        "reg": "neutral, neutral, musik",
        "syn": [],
        "ex": f"Han knäppte vant på sin {h('balalajka')} och snart dansade hela "
              f"sällskapet.",
        "skal": "Legacys andra betydelse ('en symbol för rysk och östeuropeisk "
                "folkmusiktradition') finns inte i någon källa — det är en "
                "association, inte en betydelse. Instrumentet har ingen synonym.",
    },
    "blåsyra": {
        "hb": "mycket giftig, lättflyktig syra som luktar bittermandel",
        "reg": "fackspråklig, neutral, kemi",
        "syn": ["cyanvätesyra", "cyanväte"],
        "ex": f"Vid brand i plast kan farlig {h('blåsyra')} frigöras i röken.",
        "skal": "SO taggar cyanvätesyra som SYN:synonym och SAOL glossar ordet "
                "rakt av med 'cyanväte' — båda alltså källornas egna likhetstecken.",
    },
    "dagsedel": {
        "hb": "kraftig örfil",
        "reg": "vardaglig, neutral",
        "syn": ["örfil", "snyting", "hurring"],
        "ex": f"Han delade ut en {h('dagsedel')} mitt framför kamerorna.",
        "skal": "SO: 'kraftig örfil', märkt vardagligt och något ålderdomligt. "
                "Legacys två andra betydelser (daglig rapport om dagsverke; Stig "
                "Dagermans dagsverser) saknas i både SO och SAOL.",
    },
    "fång": {
        "hb": "så mycket man kan bära i famnen ; juridiskt förvärv av äganderätt "
              "; smärtsam hovinflammation hos häst och nötkreatur",
        "reg": "neutral, neutral ; formell, neutral, juridik ; fackspråklig, "
               "neutral, medicin",
        "syn": ["famn", "förvärv"],
        "ex": f"Hon kom in med ett stort {h('fång')} nyklippta rosor.",
        "skal": "SO har två uppslag: 'full famn' + 'det att bli ägare till något' "
                "(märkt juridik, SYN:synonym = förvärv) och ett eget uppslag för "
                "djursjukdomen. Legacy saknade exempelmening helt.",
    },
    "fåraktig": {
        "hb": "lätt enfaldig, med ett hjälplöst dumt uttryck",
        "reg": "neutral, nedsättande",
        "syn": ["enfaldig", "fånig", "töntig"],
        "ex": f"När läraren ställde frågan log han bara {h('fåraktigt')} och sa "
              f"ingenting.",
        "skal": "SO 'lätt enfaldig', SAOL 'mjäkig, töntig'. 'Dum' ströks som för "
                "vitt — fåraktig handlar om det hjälplösa uttrycket, inte om "
                "intelligens i allmänhet. 'Uttryckslös' är fel axel.",
    },
    "homeopati": {
        "hb": "alternativ läkemetod med kraftigt utspädda doser av det som "
              "orsakar besväret",
        "reg": "neutral, neutral, medicin",
        "syn": [],
        "ex": f"Kritiker menar att {h('homeopati')} saknar vetenskapligt stöd helt.",
        "skal": "SO beskriver principen (små doser av det som i stora doser ger "
                "sjukdomen). Synonymlistan tömd: alternativmedicin och "
                "komplementärmedicin är ÖVERORDNADE begrepp — homeopati är en av "
                "många — och 'pseudovetenskap' är ett omdöme om metoden, inte en "
                "synonym till ordet.",
    },
    "lända": {
        "hb": "leda till ett visst resultat, oftast i uttryck som lända till heder",
        "reg": "högtidlig, neutral",
        "syn": ["leda till", "medföra", "åstadkomma"],
        "ex": f"Att du plöjt hela kursboken kommer att {h('lända')} dig till heder.",
        "skal": "SO 'föra' med underbetydelsen 'ge anledning till viss bedömning', "
                "märkt ålderdomligt eller högtidligt. 'Bidra till' ströks: det "
                "anger ett delbidrag, lända anger hela följden.",
    },
    "meningsutbyte": {
        "hb": "ömsesidigt utbyte av åsikter, ofta skiljaktiga",
        "reg": "neutral, neutral",
        "syn": ["åsiktsutbyte", "ordväxling"],
        "ex": f"Ett fritt {h('meningsutbyte')} är själva poängen med en demokrati.",
        "skal": "SO: 'ömsesidigt framförande av (skiljaktiga) åsikter' — "
                "ömsesidigheten är kärnan. 'Samtal' ströks som för vitt; ett "
                "samtal behöver inte innehålla åsikter alls.",
    },
    "nödsakad": {
        "hb": "tvingad av svåra omständigheter",
        "reg": "formell, neutral",
        "syn": ["tvungen", "nödgad", "föranlåten"],
        "ex": f"Efter branden var familjen {h('nödsakad')} att flytta till en "
              f"annan stad.",
        "skal": "SO ordagrant. Legacys 'pressad' ströks — pressad är ett tillstånd, "
                "nödsakad är ett tvång att handla.",
    },
    "prejudikat": {
        "hb": "dom som blir norm för hur liknande fall ska avgöras",
        "reg": "formell, neutral, juridik",
        "syn": ["precedensfall", "normerande rättsfall"],
        "ex": f"Högsta domstolens avgörande blev ett {h('prejudikat')} för alla "
              f"liknande mål.",
        "skal": "SO: 'dom eller myndighetsbeslut som kan komma att utgöra norm "
                "för liknande fall'. Legacys 'domslut' och 'rättsavgörande' är "
                "vidare — varje dom är ett domslut, men bara en normbildande dom "
                "är ett prejudikat. 'Vägledning' är vidare igen.",
    },
    "tomahawk": {
        "hb": "stridsyxa hos Nordamerikas urfolk",
        "reg": "neutral, neutral",
        "syn": ["indianyxa"],
        "ex": f"Hans {h('tomahawk')} var en familjeklenod som gått i arv i "
              f"generationer.",
        "skal": "SO och SAOL har bara vapnet. Köttstycket (ryggbiff med ben) finns "
                "i verkligheten men i ingen av källorna, och 'yxa'/'hacka' är "
                "överordnade begrepp.",
    },
    "vara främmande för": {
        "hb": "inte alls kunna tänka sig något ; sakna all erfarenhet av något",
        "reg": "neutral, neutral",
        "syn": ["ta avstånd från", "vara obekant med"],
        "ex": f"Att fuska på provet {h('är främmande för')} henne.",
        "skal": "Frasen har inget eget uppslagsord — svenska.se:s fritextsökning "
                "gav noll ortografiträffar. Grundordet `främmande` slogs därför "
                "upp separat: SO ger adjektivet 'ny och fortfarande obekant' med "
                "underbetydelsen 'som tar avstånd', och synonymer.se listar "
                "uttrycket med betydelsen 'Inte kunna tänka sig något'. Legacys "
                "'ogilla' ströks — man kan ogilla något man är väl bekant med.",
    },
    "rata": {
        "hb": "välja bort något för att man tycker det är för dåligt",
        "reg": "neutral, neutral",
        "syn": ["försmå", "kassera", "utdöma"],
        "ex": f"Han {h('ratade')} alla förslagen och krävde att vi började om.",
        "skal": "SO: 'bedöma som för dålig och därför inte vilja ha' — värderingen "
                "är inbyggd i ordet, och det är den legacy tappade ('välja bort' "
                "ensamt kan vara helt neutralt). Legacy saknade exempelmening.",
    },
    "till förfång": {
        "hb": "till skada eller nackdel för någon",
        "reg": "formell, negativ",
        "syn": ["till avbräck", "till men"],
        "ex": f"Bristande rutiner var honom {h('till förfång')} när kraven ökade.",
        "skal": "Frasen slås inte upp — svenska.se returnerade 30 grannartiklar "
                "(bill, dill, förfina …) och noll ortografiträffar. Grundordet "
                "`förfång` slogs upp separat: SAOL ger 'avbräck; nackdel' med "
                "exemplet *till förfång för ngn/ngt*, alltså exakt frasen. Legacy "
                "saknade exempelmening och stavade 'nackedel'.",
    },
    "biltog": {
        "hb": "som är fredlös och står utanför lagens skydd",
        "reg": "ngt ålderdomlig, neutral, historia",
        "syn": ["fredlös", "fågelfri"],
        "ex": f"Efter dråpet förklarades han {h('biltog')} och tvingades gömma "
              f"sig i skogen.",
        "skal": "SO 'som står utanför lagen', märkt ålderdomligt; SAOL glossar "
                "med just fredlös och fågelfri. 'Utstött' ströks — det är socialt, "
                "biltog är juridiskt.",
    },
    "bryn": {
        "hb": "långsmalt gränsområde, som kanten av en skog ; ögonbryn",
        "reg": "neutral, neutral",
        "syn": ["kant", "rand"],
        "ex": f"Rådjuret stod stilla i {h('brynet')} mellan åkern och skogen.",
        "skal": "SO: 'långsmalt gränsområde' med underbetydelsen ögonbryn. "
                "Synonymen 'ögonbryn' kan INTE stå kvar — den innehåller "
                "uppslagsordet och bryter mot den hårda cirkularitetsregeln sedan "
                "i morse. 'Område' ströks som för vitt: ett bryn är alltid smalt "
                "och alltid en gräns.",
    },
    "budgetering": {
        "hb": "planering av hur pengarna ska fördelas under en period",
        "reg": "neutral, neutral, ekonomi",
        "syn": [],
        "ex": f"Efter en noggrann {h('budgetering')} hade hon råd med både hyra "
              f"och kurslitteratur.",
        "skal": "SAOL har uppslagsordet men ingen gloss; Wiktionary 'det att "
                "budgetera'. 'Redovisning' ströks — det är motsatt riktning i "
                "tiden, en redovisning beskriver pengar som redan är spenderade.",
    },
    "cysta": {
        "hb": "sjuklig vätskefylld blåsa i kroppen",
        "reg": "fackspråklig, neutral, medicin",
        "syn": ["vätskefylld blåsa"],
        "ex": f"Läkaren tömde {h('cystan')} på handleden med en tunn nål.",
        "skal": "SO 'sjuklig blåsformig bildning i kroppen', SAOL 'vätskefylld "
                "blåsa i kroppen'. 'Tumör' ströks: en tumör är en cellnybildning, "
                "en cysta är ett hålrum med vätska. 'Follikel' är en normal "
                "struktur, inte något sjukligt.",
    },
    "efterräkning": {
        "hb": "obehaglig påföljd av något man själv ställt till med",
        "reg": "neutral, lätt negativ",
        "syn": ["påföljd", "efterspel", "vidräkning"],
        "ex": f"Festen var rolig, men {h('efterräkningen')} kom med hyran i "
              f"månadsskiftet.",
        "skal": "SO och SAOL: 'obehaglig påföljd'. Legacys 'konsekvens/följd' är "
                "neutrala — obehagligheten är inbyggd i ordet, precis som i "
                "SAOL:s exempel 'klara sig undan efterräkningar'. Legacys andra "
                "betydelse (elräkning i efterhand) finns inte i källorna.",
    },
    "eventuell": {
        "hb": "som kanske kommer att inträffa",
        "reg": "neutral, neutral",
        "syn": ["möjlig"],
        "ex": f"Ta med paraply för {h('eventuellt')} regn på vägen hem.",
        "skal": "SAKFEL RÄTTAT: synonymen 'sannolik' betyder TROLIG, alltså över "
                "50 % — eventuell säger bara att något är möjligt. Legacys "
                "exempelmening innehöll dessutom inte ordet alls ('Det är möjligt "
                "att det regnar imorgon').",
    },
    "festong": {
        "hb": "flätat band av blommor och frukter, ofta som ornament",
        "reg": "fackspråklig, neutral, konst",
        "syn": ["girland", "blomsterslinga"],
        "ex": f"Över porten satt en {h('festong')} av snidade blommor och frukter.",
        "skal": "SO 'flätat band av blommor och frukter', SAOL 'slinga av blommor "
                "och blad som ornament' — ornamentet är huvudsaken, inte något "
                "man bär. Legacys 'krans' ströks: en krans är sluten, en festong "
                "hänger i en båge.",
    },
    "förseelse": {
        "hb": "lindrigare brott eller regelbrott",
        "reg": "neutral, neutral",
        "syn": ["felsteg", "försyndelse", "överträdelse"],
        "ex": f"Han slapp undan med böter eftersom {h('förseelsen')} var liten.",
        "skal": "SO och SAOL: 'lindrigare brott'. 'Lindrigt brott' som synonym "
                "ströks — det upprepar bara huvudbetydelsen ordagrant.",
    },
    "kompatibel": {
        "hb": "möjlig att få att fungera ihop med något annat",
        "reg": "neutral, neutral, IT",
        "syn": [],
        "ex": f"Den gamla skrivaren är inte längre {h('kompatibel')} med min dator.",
        "skal": "SO 'möjlig att samordna och få att överensstämma', märkt 'särsk. "
                "data.' — därav IT-domänen. 'Överensstämmande' ströks: två saker "
                "kan fungera ihop utan att vara lika.",
    },
    "kumulation": {
        "hb": "successiv anhopning, att något samlas på hög",
        "reg": "formell, neutral",
        "syn": ["anhopning", "hopning"],
        "ex": f"En {h('kumulation')} av små misstag ledde till slut till haveriet.",
        "skal": "SAOL har uppslagsordet utan gloss; syn.se ger anhopning, hopning, "
                "samling. Legacys juridiska och epidemiologiska betydelser finns "
                "inte i någon källa — de är rimliga men obelagda.",
    },
    "kuva": {
        "hb": "tvinga någon till underkastelse ; slå ner en känsla eller ett uppror",
        "reg": "neutral, neutral",
        "syn": ["betvinga", "kväsa", "undertrycka"],
        "ex": f"Regimen försökte {h('kuva')} varje protest med hårda straff.",
        "skal": "SO 'tvinga till underkastelse' med underbetydelsen 'slå ner'. "
                "Legacys 'applicera tryck på något för att ändra dess form' är "
                "fel ord — det är att kuva ihop med KUVERT/kupa, inte kuva.",
    },
    "måttlös": {
        "hb": "som går långt utöver rimliga gränser",
        "reg": "neutral, lätt negativ",
        "syn": ["omåttlig", "hejdlös"],
        "ex": f"Hans {h('måttlösa')} skryt gjorde att ingen orkade lyssna.",
        "skal": "SO 'som går utöver rimliga gränser'. SO taggar hejdlös och "
                "omåttlig som JFR:cohyponym. Legacys 'oändlig' ströks — måttlös "
                "är ett omdöme om att gränsen passerats, oändlig är en storlek.",
    },
    "nativ": {
        "hb": "som finns färdig i naturen ; om metall: gedigen och ren",
        "reg": "fackspråklig, neutral",
        "grupper": [["naturlig"], ["gedigen"]],
        "ex": f"Guld förekommer {h('nativt')} i naturen och behöver inte "
              f"framställas.",
        "skal": "SAKFEL RÄTTAT: legacys exempel var 'Det är en nativ talare av "
                "det språket' — engelskans *native speaker*, inte svenska. SO ger "
                "'som förekommer färdig i naturen' (märkt vetenskapliga och "
                "tekniska sammanhang) och SAOL 'om metall: gedigen'. SO taggar "
                "konstgjord och syntetisk som MOTSATS:antonym, vilket bekräftar "
                "axeln. 'Inhemsk' ströks — det är engelskans betydelse.",
    },
    "oratorisk": {
        "hb": "som rör talekonsten ; vältalig på ett högtravande sätt",
        "reg": "formell, neutral ; formell, lätt negativ",
        "grupper": [["retorisk"], ["högtravande", "deklamatorisk"]],
        "ex": f"Hans {h('oratoriska')} förmåga vann omröstningen trots svaga "
              f"argument.",
        "skal": "SO har två betydelser och den andra bär en värdering "
                "('vältalig på ett HÖGTRAVANDE sätt') — därav två register. "
                "Legacys 'talarkonstnärlig' finns inte som ord.",
    },
    "preludium": {
        "hb": "kortare musikstycke som inleder ett större verk ; inledning eller "
              "förberedelse till något",
        "reg": "neutral, neutral, musik ; formell, neutral",
        "grupper": [["förspel"], ["förberedelse"]],
        "ex": f"Konserten öppnade med ett stilla {h('preludium')} på orgel.",
        "skal": "SO: 'kortare musikstycke som spelas som inledning'; SAOL har "
                "dessutom den överförda 'förberedelse; inledning'. SO taggar "
                "postludium som JFR:cohyponym — efterspelet, alltså motstycket.",
    },
    "sinologi": {
        "hb": "vetenskapen om Kinas språk, historia och kultur",
        "reg": "fackspråklig, neutral",
        "syn": [],
        "ex": f"Hon läste {h('sinologi')} i Uppsala och bodde ett år i Peking.",
        "skal": "SO 'vetenskapen om Kina', SAOL 'vetenskapen om kinesiska språket "
                "och kulturen'. Synonymlistan tömd — legacys 'Kinas vetenskap', "
                "'kinesisk forskning' och 'sino-studier' är inga svenska ord, de "
                "är konstruerade på plats.",
    },
    "vederlägga": {
        "hb": "bevisa att ett påstående är felaktigt",
        "reg": "formell, neutral",
        "syn": ["motbevisa", "gendriva"],
        "ex": f"Det tog forskarna tio år att {h('vederlägga')} teorin.",
        "skal": "SAKFEL RÄTTAT: 'förneka' är att säga emot, 'vederlägga' är att "
                "BEVISA att något är fel — man kan förneka utan ett enda argument. "
                "SO taggar gendriva som SYN:synonym. 'Refutera' ströks som "
                "främmande i svenskan.",
    },
    "våras": {
        "hb": "bli vår ; börja gå mot bättre tider",
        "reg": "neutral, neutral",
        "syn": ["ljusna"],
        "ex": f"Det börjar {h('våras')} för vinylskivan, som säljer i stora "
              f"upplagor igen.",
        "skal": "SO 'bli vår' med underbetydelsen 'bli bättre tider'; SAOL ger "
                "vändningen 'det våras för ngn/ngt'. Synonymen 'ljusna' hör till "
                "den bildliga betydelsen; den bokstavliga har ingen — 'bli vår' "
                "vore bara huvudbetydelsen om igen.",
    },
}


def main():
    poster = json.load(open(SESSION, encoding="utf-8"))
    kvar = [p for p in poster if p["ord"] not in PAUSAS]
    pausade = [p["ord"] for p in poster if p["ord"] in PAUSAS]

    saknar = [p["ord"] for p in kvar if p["ord"] not in KORT]
    if saknar:
        sys.exit(f"saknar rättelse för: {', '.join(saknar)}")

    for p in kvar:
        o = p["ord"]
        r = KORT[o]
        p["proposed"] = {
            # Versal begynnelsebokstav är husstilen i decket -- kontrollerat mot
            # tolv redan godkända full v3-kort (beprövad, bonitet, otolog ...).
            # Skrivs här i stället för i varje post, så den inte kan glömmas
            # bort på ett enstaka kort och ge en osynlig stilavvikelse.
            "huvudbetydelse": r["hb"][0].upper() + r["hb"][1:],
            "synonymer": r.get("syn", [s for g in r.get("grupper", []) for s in g]),
            "synonym_groups": r.get("grupper"),
            "exempelmening": r["ex"],
            "register": r["reg"],
            "etymologi": None,
        }
        p["approved"] = True
        # Källan är uppslagsordet som FAKTISKT slogs upp -- för fraserna är det
        # grundordet, inte framsidan. Att peka på framsidans egen msearch hade
        # sett korrekt ut och ändå inte varit den källa innehållet kom ifrån.
        p["sokkoll"] = {
            "kalla": SVENSKA.format(urllib.parse.quote(K.get(o, o))),
            "slutsats": r["skal"],
        }
        p.pop("applicerad", None)

    json.dump(kvar, open(SESSION, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"fyllde {len(kvar)} poster.")
    if pausade:
        print(f"UTESLUTNA (pausas separat): {', '.join(pausade)}")


if __name__ == "__main__":
    main()
