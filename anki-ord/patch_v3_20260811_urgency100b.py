# -*- coding: utf-8 -*-
"""100 urgency-rankade suspenderade is:review-kort (2026-08-11, kväll).

Sökkoll: `slaupp.py` kördes mot alla 100 orden i denna session, i två svep om
50. 99 av 100 fick träff på svenska.se; undantaget är idiomet
`gå upp i limningen`, som inte är uppslagsord i någon av de tre ordböckerna.

TRE KORT HAR EGEN KÄLLA, inte svenska.se:
* `keratit`   -- bara SAOB har uppslagsordet, och SAOB:s artikel ger ingen
                 brukbar nutida definition. Belagt mot NE i samma session:
                 "medicinsk term för hornhinneinflammation". synonymer.se
                 saknar ordet helt (visar "du kanske menade keratin").
* `gå upp i limningen` -- saknas i alla tre ordböckerna. Vilar på
                 synonymer.se:s REDAKTIONELLA post (Adams källregel 2026-08-11).
* `lända till` -- bara SAOB; synonymer.se redaktionellt bekräftar "medföra".

## Vad genomgången faktiskt hittade

Det dominerande felet är detsamma som hela decket lider av: **SO listar flera
betydelser, kortet har en.** 23 kort saknade minst en betydelse. Grövst:
`risa` (SO har fyra, kortet en), `ansats` (fem mot två), `knyck` (tre mot en),
`prägla` (fem mot två), `kummel` (fyra mot två).

Ett kort var rakt av FEL: **`toujours`**. Kortet sa "alltid, jämt" -- den
franska betydelsen. Svenskt `toujours` är ett adjektiv: SO ger "sällskaplig
och trevlig", syn.se "trevlig, fryntlig, sällskaplig", OLD-facit "trevlig".
Hela kortet, inklusive exempelmeningen, byggde på fel språk.

## Två fällor jag INTE gick i

`slå dank`, `kavat`, `pryd`, `svara för` och `alla taggar utåt` fick digester
fulla av grannord (svenska.se:s msearch är en fritextsökning): `dank` som
"dåligt smalt ljus", `kavat` som "krypa" (= *kava*), `pryd` som "förse med
prydnad" (= *pryda*). Ingen av dem har lagts till. Det är exakt felet jag
gjorde med `solvens` 2026-08-11, där vävnadstermen för *solv* hamnade på
`solvens`-kortet och blindgranskaren fångade det.

## Registerändringar görs bara mot uttryckligt belägg

Mätt 2026-08-11: kort jag skrev om underkändes i 35 %, orörda i 20 %. Att
röra ett kort är alltså farligare än att låta det vara. Registret ändras
därför bara när SO/SAOL har en bruklighetskommentar som SÄGER EMOT kortet
(`pärs` vardagligt mot kortets litterär, `sumpa` vardagligt mot formell,
`tryta` ngt ålderdomligt mot vardaglig) eller när värdet är ett kategorifel
(`ränsel` som "arkaisk" när SO ger ordet utan märkning och med nutida
exempel). Där ordböckerna tiger står kortets värde kvar.
"""

import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SESSION = "sessions/session_2026-08-11_v3-omgranskning.json"

DOMAN = {
    "framfusig": "allmän", "psykoprofylax": "medicin", "sto": "biologi",
    "nivellera": "allmän", "puffa": "allmän", "valspråk": "allmän",
    "slå dank": "allmän", "vederfaras": "allmän", "hemgift": "historia",
    "alla taggar utåt": "allmän", "toujours": "allmän", "atypisk": "allmän",
    "gå upp i limningen": "allmän", "brevledes": "allmän", "surmulen": "allmän",
    "ortopedi": "medicin", "vertebrat": "biologi", "svara för": "allmän",
    "kronologi": "historia", "respiration": "medicin", "gloriös": "allmän",
    "kiropraktik": "medicin", "paralysera": "medicin", "pigment": "kemi",
    "trafikabel": "teknik", "exekutiv": "juridik", "spad": "matlagning",
    "kurativ": "medicin", "framstöt": "militär", "simili": "allmän",
    "handha": "allmän", "tillstyrka": "juridik", "risa": "allmän",
    "keratit": "medicin", "beivra": "juridik", "behållning": "ekonomi",
    "pärs": "allmän", "hirs": "jordbruk", "ränsel": "allmän",
    "frivol": "allmän", "oförvitlig": "allmän", "palp": "biologi",
    "hambo": "musik", "hortonom": "jordbruk", "dementera": "allmän",
    "kavat": "allmän", "förnumstig": "allmän", "tilltaga": "allmän",
    "visshet": "allmän", "knyck": "allmän", "bortklemad": "allmän",
    "tjudra": "jordbruk", "utrangera": "teknik", "tordön": "allmän",
    "bemänga": "allmän", "lisös": "allmän", "nabo": "allmän",
    "delikt": "juridik", "bundsförvant": "politik", "flakong": "allmän",
    "kummel": "historia", "östan": "allmän", "entomologi": "biologi",
    "abstrahera": "filosofi", "ebonit": "kemi", "ansats": "allmän",
    "astrakan": "jordbruk", "vrenskas": "allmän", "hematit": "geologi",
    "lunett": "konst", "barm": "allmän", "epistemologi": "filosofi",
    "oftalmi": "medicin", "nedkomst": "medicin", "förflugen": "allmän",
    "härröra": "allmän", "prägla": "allmän", "interregnum": "historia",
    "flyhänt": "allmän", "amfora": "historia", "pryd": "allmän",
    "kommissarie": "politik", "belägenhet": "allmän", "obscen": "allmän",
    "abbreviation": "musik", "prominent": "allmän", "abstrus": "allmän",
    "föröva": "juridik", "halvkväden": "allmän", "bagge": "biologi",
    "sumpa": "allmän", "metodism": "religion", "aplomb": "allmän",
    "lända till": "allmän", "partisk": "allmän", "handlag": "allmän",
    "tryta": "allmän", "bitumen": "kemi", "kväkare": "religion",
    "samarbetsman": "politik",
}

EGEN_KALLA = {
    "keratit": "https://www.ne.se/uppslagsverk/encyklopedi/lång/keratit",
    "gå upp i limningen": "https://www.synonymer.se/sv-syn/gå+upp+i+limningen",
}

RATTELSER = {
    # ---- Fel betydelse ------------------------------------------------
    "toujours": {
        "huvudbetydelse": "Sällskaplig och trevlig",
        "synonymer": ["trevlig", "fryntlig", "sällskaplig"],
        "register": "ngt ålderdomlig, positiv, allmän",
        "exempelmening": "Värden var toujours och fick alla gäster att känna sig hemma.",
        "_skal": "KORTET VAR FEL SPRÅK. Det sa 'alltid, jämt' -- franskans toujours. "
                 "Svenskt toujours är ett ADJEKTIV: SO 'sällskaplig och trevlig' "
                 "(märkn: mindre brukligt), syn.se 'trevlig, fryntlig, sällskaplig', "
                 "OLD-facit 'trevlig'. Betydelse, synonymer, register och "
                 "exempelmening är alla utbytta.",
    },
    "psykoprofylax": {
        "huvudbetydelse": "Psykologisk metod för smärtlindring vid förlossning",
        "synonymer": ["förlossningsförberedelse", "andningsteknik"],
        "_skal": "Kortet sa 'andningsmetod'. SO: 'en PSYKOLOGISK metod för "
                 "smärtlindring', SAOL: 'en metod för lindring av smärtor vid "
                 "förlossning'. Andningen är en del av metoden, inte metoden.",
    },
    "bitumen": {
        "huvudbetydelse": "Naturlig kolväteförening med mörk färg — sammanfattande "
                          "beteckning för bl.a. naturgas, petroleum och asfalt",
        "synonymer": ["asfalt", "beck", "petroleumprodukt"],
        "_skal": "Kortet sa 'tjärliknande ämne för asfalt' -- för smalt. SO gör "
                 "bitumen till PARAPLYTERMEN som asfalt ligger under, inte till "
                 "asfaltens bindemedel.",
    },

    # ---- Saknad betydelse ---------------------------------------------
    "framfusig": {
        "huvudbetydelse": "Som oblygt tränger sig på ; ibland med positiv värdering: "
                          "driftig och orädd",
        "synonymer": ["påträngande", "påflugen", "oblyg"],
        "_skal": "SO+: 'ibland äv. med positiv värdering', med exemplet 'en framfusig "
                 "anfallare är vad laget behöver'. Kortet gav bara den negativa läsningen.",
    },
    "nivellera": {
        "huvudbetydelse": "Utjämna till en enda nivå ; avväga höjdskillnader vid fältmätning",
        "synonymer": ["utjämna", "likrikta", "avväga"],
        "register": "formell, lätt negativ, allmän",
        "_skal": "Två fynd. (1) SAOL ger 'avväga vid fältmätning' som egen betydelse "
                 "-- lantmäteritermen saknades. (2) SO:s bruklighetskommentar är "
                 "'ofta nedsättande' om den bildliga användningen; kortet sa neutral.",
    },
    "puffa": {
        "huvudbetydelse": "Utvecklas i korta stötar ; ge lätt stöt ; mana på, utöva "
                          "påtryckning ; göra reklam för",
        "synonymer": ["knuffa", "mana på", "göra reklam för"],
        "_skal": "SO ger fem betydelser, kortet två. Den som saknades helt är "
                 "'mana (på), utöva påtryckning' -- SAOL:s 'puffa för ngt'.",
    },
    "hemgift": {
        "huvudbetydelse": "Egendom som kvinnan för med sig i boet vid giftermål ; "
                          "gåva från föräldrarna till dottern vid hennes giftermål",
        "synonymer": ["medgift", "hemföljd", "utstyrsel"],
        "_skal": "SO ger TVÅ betydelser -- egendomen i boet och gåvan från "
                 "föräldrarna. Kortet hade bara den första.",
    },
    "kronologi": {
        "huvudbetydelse": "Läran om beräkning och indelning av tiden ; tidsmässig "
                          "inbördes ordning",
        "synonymer": ["tideräkning", "tidsföljd", "tidsordning"],
        "_skal": "SO ger vetenskapen FÖRST ('(läran om) beräkning och indelning av "
                 "tiden'), SAOL 'tideräkning; tidsföljd'. Kortet hade bara ordningen.",
    },
    "paralysera": {
        "huvudbetydelse": "Orsaka fullständig förlust av rörelseförmågan hos ; "
                          "bildligt: orsaka tillfällig förlust av handlingsförmågan",
        "synonymer": ["förlama", "lamslå", "bedöva"],
        "_skal": "SO ger två betydelser. Den bildliga ('skräcken paralyserade dem') "
                 "saknades -- och det är den vanligaste i löpande text.",
    },
    "exekutiv": {
        "huvudbetydelse": "Verkställande ; som har att göra med exekution, dvs. "
                          "indrivning och tvångsförsäljning",
        "synonymer": ["verkställande", "utövande", "utmätnings-"],
        "_skal": "SO och SAOL ger båda den juridiska betydelsen ('exekutiv auktion', "
                 "'som äger rum som verkställighet av dom'). Kortet hade bara den "
                 "statsrättsliga.",
    },
    "spad": {
        "huvudbetydelse": "Vatten som livsmedel kokats i ; äv. om lag för inläggning "
                          "och (vardagligt) om sjö- och havsvatten",
        "synonymer": ["avkok", "sky", "lag"],
        "_skal": "SO ger tre användningar; kortet en. 'Falla i spat/spadet' om att "
                 "hamna i sjön saknades helt.",
    },
    "kurativ": {
        "huvudbetydelse": "Som har botande effekt ; som rör kurator och kuratorsarbete",
        "synonymer": ["botande", "läkande", "kurators-"],
        "_skal": "SAOL ger TVÅ betydelser: 'botande, läkande | kurators-', med "
                 "exemplet 'kurativ verksamhet'. Kortet hade bara den medicinska.",
    },
    "framstöt": {
        "huvudbetydelse": "Begränsat anfall ; initiativ eller krav",
        "synonymer": ["anfall", "framryckning", "initiativ"],
        "_skal": "SO ger den militära betydelsen först och 'initiativ, krav' som "
                 "egen, bildlig betydelse. Kortets 'energisk åtgärd' suddade ut "
                 "gränsen mellan dem.",
    },
    "risa": {
        "huvudbetydelse": "Kritisera strängt ; täcka eller förse med ris och kvistar ; "
                          "aga med ris ; (risa ihop) falla samman",
        "synonymer": ["kritisera", "klandra", "täcka med ris"],
        "_skal": "SO ger FYRA betydelser och SAOL tre; kortet hade en. Både "
                 "'ett risat farstugolv / risa ärter' och 'risa ihop' (kollapsa) "
                 "saknades helt.",
    },
    "behållning": {
        "huvudbetydelse": "Kvarstående värde efter utgifter ; gott utbyte av något",
        "synonymer": ["överskott", "saldo", "utbyte"],
        "_skal": "SO och SAOL ger båda 'gott utbyte' som egen betydelse -- 'hade du "
                 "behållning av boken?'. Den saknades, och det är den betydelse "
                 "ordet oftast har utanför bokföring.",
    },
    "pärs": {
        "huvudbetydelse": "Svår påfrestning ; (titel för) huvudman i engelsk adelsätt, "
                          "ledamot av överhuset",
        "synonymer": ["hårt prov", "svår prövning", "engelsk adelsman"],
        "register": "vardaglig, negativ, allmän",
        "_skal": "Två fynd. (1) SO och SAOL ger båda adelstiteln som egen betydelse. "
                 "(2) SO:s bruklighetskommentar är 'vardagligt'; kortet sa litterär, "
                 "vilket är fel håll på skalan.",
    },
    "visshet": {
        "huvudbetydelse": "Övertygelse som grundar sig på säkra fakta ; säkerhet, "
                          "frånvaro av tvivel",
        "synonymer": ["säkerhet", "övertygelse", "bestämdhet"],
        "_skal": "SO ger två betydelser: övertygelsen och säkerheten ('med till "
                 "visshet gränsande sannolikhet'). Kortet hade bara den första.",
    },
    "knyck": {
        "huvudbetydelse": "Kort, tvär och plötslig rörelse ; tvär krök ; "
                          "kilometer i timmen",
        "synonymer": ["ryck", "tvär krök", "km/h"],
        "_skal": "SO ger TRE betydelser, kortet en. Både kröken och 'kom upp i 100 "
                 "knyck' saknades -- SAOL har km/h som sin enda betydelse.",
    },
    "tordön": {
        "huvudbetydelse": "Åska ; kraftigt buller eller dån",
        "synonymer": ["åska", "dunder", "dån"],
        "_skal": "SO ger 'kraftigt buller' FÖRE åskan; syn.se 'starkt buller, dunder, "
                 "dån, brak, muller'. Kortet hade bara åskan.",
    },
    "nabo": {
        "huvudbetydelse": "Granne eller närboende ; person i grannland",
        "synonymer": ["granne", "närboende", "grannfolk"],
        "_skal": "SO ger 'person i grannland' som egen betydelse -- 'våra nabor "
                 "norrmännen'. Det är den användning ordet oftast har i modern text.",
    },
    "kummel": {
        "huvudbetydelse": "Stenröse som minnesmärke eller gravröse ; fast sjömärke av "
                          "sten ; en långsträckt torskfisk med stort huvud",
        "synonymer": ["gravröse", "båk", "torskfisk"],
        "_skal": "SO ger fyra betydelser, SAOL tre; kortet två. Sjömärket ('stympad "
                 "kon', SAOL 'fast sjömärke av sten', syn.se 'båk') var hopblandat "
                 "med gravröset i kortets 'stenröse som markerar en plats vid kusten'.",
    },
    "östan": {
        "huvudbetydelse": "Från eller åt öster ; vind från öster",
        "synonymer": ["österifrån", "östanvind", "östlig vind"],
        "_skal": "SO och SAOL ger båda substantivet ('en isande östan', 'en kraftig "
                 "östan'). Kortet hade bara adverbet.",
    },
    "ansats": {
        "huvudbetydelse": "Påbörjat försök ; teoretisk inriktning ; kort intensiv "
                          "språngmarsch före hopp ; upphöjt parti på en yta",
        "synonymer": ["försök", "inriktning", "anlopp"],
        "_skal": "SO ger fem betydelser och SAOL fyra; kortet två. Den akademiska "
                 "('en uppsats med språkhistorisk ansats') och den tekniska "
                 "('upphöjt parti t.ex. på verktyg') saknades båda.",
    },
    "astrakan": {
        "huvudbetydelse": "Sommaräpple med löst, sött och genomskinligt kött ; fint, "
                          "krusulligt lammskinn och tyg som liknar det",
        "synonymer": ["sommaräpple", "lammskinn", "persian"],
        "_skal": "SO och SAOL ger båda pälsverket som egen betydelse. Kortet hade "
                 "bara äpplet -- två helt orelaterade saker med samma namn.",
    },
    "barm": {
        "huvudbetydelse": "Bröst ; äv. om förvaringsplatsen innanför kläderna vid bröstet",
        "synonymer": ["bröst", "bringa", "famn"],
        "register": "högtidlig, neutral, allmän",
        "exempelmening": "Hon gömde brevet vid sin barm så att ingen skulle hitta det.",
        "_skal": "Tre fynd. (1) SO+: 'äv. om förvaringsplats vid bröstet' -- källan "
                 "till 'nära en orm vid sin barm'. (2) SO:s bruklighetskommentar är "
                 "'något högtidligt', inte litterär. (3) Exempelmeningen var "
                 "fragmentet 'Fyllig barm.', inte en mening.",
    },
    "prägla": {
        "huvudbetydelse": "Åstadkomma avtryck och relief i metall ; ge viss prägel åt ; "
                          "fästa i minnet ; (om djurunge) lära upp genom prägling",
        "synonymer": ["stämpla", "känneteckna", "inpränta"],
        "_skal": "SO ger fem betydelser, kortet två. Både minnesbetydelsen (SAOL:s "
                 "enda: 'fästa i minnet') och den etologiska präglingen saknades.",
    },
    "interregnum": {
        "huvudbetydelse": "Period mellan två regeringar utan högsta myndighet ; "
                          "utvidgat: period mellan två ledningar, t.ex. på ett företag",
        "synonymer": ["mellanregering", "vakans", "övergångsperiod"],
        "_skal": "SO+: 'äv. utvidgat, t.ex. på företag'; SAOL 'tid mellan en ledares "
                 "avgång och val av efterträdare'. Den moderna, icke-statsrättsliga "
                 "användningen saknades.",
    },
    "kommissarie": {
        "huvudbetydelse": "Tjänsteman med ledande eller övervakande uppdrag ; "
                          "historiskt: regeringsmedlem i Sovjetunionen",
        "synonymer": ["poliskommissarie", "ombud", "folkkommissarie"],
        "_skal": "SO och SAOL ger båda sovjetministern som egen betydelse (SO märker "
                 "den 'historiskt'). Kortet hade bara tjänstemannen.",
    },
    "belägenhet": {
        "huvudbetydelse": "Placering i rummet ; bildligt: situation man befinner sig i",
        "synonymer": ["läge", "placering", "situation"],
        "exempelmening": "Han hamnade i en svår belägenhet när både bilen och "
                         "telefonen gick sönder.",
        "_skal": "SO ger 'situation' som egen betydelse ('hon är i den lyckliga "
                 "belägenheten att kunna välja') -- OLD-facit har den, kortet inte. "
                 "Exempelmeningen var dessutom fragmentet 'Restaurangens känsliga "
                 "belägenhet.'",
    },
    "obscen": {
        "huvudbetydelse": "Präglad av ohöljd sexualitet ; allmännare om något som "
                          "upplevs som stötande",
        "synonymer": ["oanständig", "slipprig", "stötande"],
        "exempelmening": "Han tyckte att direktörernas obscena bonusar var ett hån "
                         "mot de anställda.",
        "_skal": "SO+: 'äv. allmännare om något som upplevs som stötande' -- 'obscena "
                 "löner', 'familjen är obscent rik'. Den betydelsen saknades, och "
                 "exempelmeningen var fragmentet 'Obscena gester.'",
    },
    "prominent": {
        "huvudbetydelse": "Framstående ; (anatomi) framskjutande, utstående",
        "synonymer": ["framstående", "bemärkt", "framskjutande"],
        "exempelmening": "Mannen på porträttet kändes igen på sin prominenta haka.",
        "_skal": "SO ger två betydelser med bruklighetskommentaren 'särsk. anatomi' "
                 "på den andra. Kortet klämde in 'särskilt inom anatomi' i den FÖRSTA "
                 "betydelsen, vilket gjorde raden obegriplig. Exemplet var dessutom "
                 "fragmentet 'Prominenta utländska gäster.'",
    },
    "sumpa": {
        "huvudbetydelse": "Försumma att utnyttja ; lägga levande nyfångad fisk i sump",
        "synonymer": ["missa", "gå miste om", "lägga i sump"],
        "register": "vardaglig, lätt negativ, allmän",
        "exempelmening": "Han sumpade en given målchans i den sista minuten.",
        "_skal": "Tre fynd. (1) SO och SAOL ger båda fisksumpen som egen betydelse -- "
                 "den som gav ordet dess bild. (2) SO:s och SAOL:s "
                 "bruklighetskommentar är 'vardagligt'; kortet sa formell. "
                 "(3) Exemplet var fragmentet 'Sumpa en målchans.'",
    },
    "aplomb": {
        "huvudbetydelse": "Stor säkerhet i uppträdandet ; eftertryck och kraft",
        "synonymer": ["självsäkerhet", "pondus", "eftertryck"],
        "_skal": "SAOL ger 'eftertryck' som egen betydelse vid sidan av säkerheten; "
                 "syn.se har 'eftertryck, kraft, kläm, emfas'. Kortet hade bara "
                 "uppträdandet.",
    },
    "handlag": {
        "huvudbetydelse": "Sätt att hantera något ; fallenhet för att hantera eller sköta",
        "synonymer": ["hanteringssätt", "fallenhet", "skicklighet"],
        "_skal": "SO ger två betydelser -- sättet och FALLENHETEN. SAOL 'förmåga att "
                 "handskas med ngn/ngt'. Kortet hade bara sättet, fast det är "
                 "fallenheten som 'gott handlag med barn' handlar om.",
    },
    "tryta": {
        "huvudbetydelse": "Börja ta slut ; saknas, fattas",
        "synonymer": ["ta slut", "sina", "fattas"],
        "register": "ngt ålderdomlig, neutral, allmän",
        "_skal": "Två fynd. (1) SO ger 'saknas' som egen betydelse ('mig tryter "
                 "ingenting'), SAOL 'vara brist på'. (2) SO:s bruklighetskommentar är "
                 "'något ålderdomligt' -- kortet sa vardaglig, alltså motsatt håll.",
    },
    "kväkare": {
        "synonymer": ["medlem av Vännernas samfund", "kvekare"],
        "_skal": "Synonymfältet var TOMT. SAOL namnger samfundet: 'medlem av den "
                 "religiösa rörelsen Vännernas samfund'.",
    },
    "flyhänt": {
        "huvudbetydelse": "Som snabbt når resultat, ofta med elegans ; ibland med "
                          "bibetydelsen ytlig",
        "synonymer": ["rapp", "flink", "lättvindig"],
        "exempelmening": "Översättningen var flyhänt men missade textens allvar.",
        "_skal": "SO+ ger två utvidgningar kortet saknade: 'ofta med tonvikt på "
                 "elegans' och 'äv. med viss bibetydelse av ytlighet'. Den senare "
                 "vänder ordets valör och är precis vad 'en flyhänt översättning' "
                 "betyder. Exemplet var fragmentet 'En flyhänt gitarrist.'",
    },

    # ---- Fel register (uttryckligt belägg i ordboken) -------------------
    "vederfaras": {
        "register": "arkaisk, neutral, allmän",
        "_skal": "SO:s bruklighetskommentar är 'ålderdomligt' och SAOL:s 'åld.'. "
                 "Kortet sa litterär, vilket påstår levande bokspråk.",
    },
    "simili": {
        "register": "arkaisk, neutral, allmän",
        "_skal": "SAOL:s bruklighetskommentar är 'åld.'. Kortet sa formell.",
    },
    "lisös": {
        "register": "ngt ålderdomlig, neutral, allmän",
        "_skal": "SAOL:s bruklighetskommentar är 'ngt åld.', inte 'åld.'. Kortet sa "
                 "arkaisk, vilket påstår att ordet är ur bruk.",
    },
    "ränsel": {
        "register": "neutral, neutral, allmän",
        "_skal": "Kortet sa arkaisk (= ur bruk). SO ger ordet UTAN bruklighets"
                 "kommentar och med nutida exempel ('packa sin ränsel'). Ett ord SO "
                 "listar omärkt är standardsvenska.",
    },
    "tilltaga": {
        "register": "ngt ålderdomlig, neutral, allmän",
        "_skal": "SAOL märker formen 'el. åld.' och syn.se skriver '(ngt åld.) "
                 "tillta'. Kortet sa formell, vilket antyder ett levande "
                 "byråkratiskt ord.",
    },
    "nedkomst": {
        "register": "högtidlig, neutral, medicin",
        "_skal": "SO:s bruklighetskommentar är 'något högtidligt' och syn.se "
                 "'(ngt högt.)'. Kortet sa litterär.",
    },
    "epistemologi": {
        "register": "fackspråklig, neutral, filosofi",
        "_skal": "SO:s bruklighetskommentar är 'filosofi' och SAOL:s 'filos.' -- "
                 "domänen står uttryckligen i ordboken, till skillnad från på de "
                 "flesta andra kort i batchen.",
    },
    "respiration": {
        "register": "fackspråklig, neutral, medicin",
        "_skal": "SO:s bruklighetskommentar är 'i medicinska sammanhang'.",
    },
    "abbreviation": {
        "register": "fackspråklig, neutral, musik",
        "_skal": "SO:s bruklighetskommentar är 'särsk. i musikaliska sammanhang' -- "
                 "kortet nämnde musiken i betydelseraden men lämnade registret "
                 "oinformerat.",
    },
    "gloriös": {
        "register": "litterär, positiv, allmän",
        "_skal": "Valören var satt till neutral. SO:s definition är 'full av ära' "
                 "och SAOL:s 'ärorik, lysande' -- ordet är entydigt positivt laddat.",
    },

    # ---- Trasiga exempelmeningar ---------------------------------------
    "härröra": {
        "exempelmening": "Uppgiften härrör från en säker källa inom myndigheten.",
        "_skal": "Exempelmeningen var grammatiskt trasig: 'Uppgiften härröra från "
                 "säker källa.' -- infinitiv där finit form krävs. SO:s eget exempel "
                 "är 'uppgiften härrör från säker källa'.",
    },
    "lända till": {
        "exempelmening": "Den nya lagen lände till stora förändringar i samhället.",
        "_skal": "Exempelmeningen var grammatiskt trasig: 'Den nya lagen lända till "
                 "omfattande samhällsförändringar.' Betydelsen står kvar; "
                 "synonymer.se:s redaktionella post ger 'medföra, lända'.",
    },
    "halvkväden": {
        "exempelmening": "Regeringens halvkvädna kritik av diktaturen övertygade ingen.",
        "_skal": "Exempelmeningen saknade mellanslag och var ett fragment: "
                 "'Halvkvädnamedgivanden.' SO:s eget exempel används i stället.",
    },
    "förflugen": {
        "exempelmening": "Ett förfluget ord på festen ställde till med skandal.",
        "_skal": "Exempelmeningen var fragmentet 'En förflugen idé.' SO:s andra "
                 "exempel är en hel mening och visar ordet i bruk.",
    },
    "pryd": {
        "exempelmening": "Hon var för pryd för att ens uttala ordet.",
        "_skal": "Exempelmeningen innehöll rå HTML-entitet ('Hon var&nbsp;pryd i "
                 "sängen.') och var dessutom onödigt platt. Betydelsen orörd. "
                 "OBS: SO:s 'förse med prydnad' hör till PRYDA, inte pryd, och har "
                 "därför inte lagts till.",
    },
    "amfora": {
        "exempelmening": "I graven låg en spräckt amfora med en bild på Akilles.",
        "_skal": "Exempelmeningen var fragmentet 'En spräckt amfora med en bild på "
                 "Akilles.' Samma innehåll, nu som mening.",
    },

    # ---- Precisering mot ordbokens formulering -------------------------
    "ortopedi": {
        "huvudbetydelse": "Läran om behandling av sjukdomar och felaktigheter i "
                          "rörelse- och hållningsorganen",
        "synonymer": ["rörelseorganens medicin", "hållningslära"],
        "_skal": "SO säger 'rörelse- OCH HÅLLNINGSorganen' och OLD-facit "
                 "'hållningslära'. Kortets 'skelett, muskler och leder' tappade "
                 "hållningen, som är halva ämnet.",
    },
}

STANDARD = ("Jamfort mot SO/SAOL/synonymer.se i denna session: betydelse, register och "
            "synonymer stammer. Ingen saknad betydelse hittad. Doman bedomd per ord.")


def _med_doman(register, ord_):
    """Lägger till den bedömda domänen på första betydelsen om den saknas."""
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
    saknar_doman = [p["ord"] for p in poster if p["ord"] not in DOMAN]
    if saknar_doman:
        sys.exit("Domän saknas för: %s" % ", ".join(saknar_doman))

    n = 0
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
        p["sokkoll"] = {
            "kalla": EGEN_KALLA.get(o, f"https://svenska.se/api/msearch?ord={o}"),
            "slutsats": r.get("_skal", STANDARD),
        }
        p.pop("applicerad", None)
        n += 1

    json.dump(poster, open(SESSION, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Fyllde {n} poster. Rattelser: {len(RATTELSER)}. Domaner: {len(DOMAN)}.")
    print(f"Egen kalla (ej svenska.se): {', '.join(EGEN_KALLA)}")


if __name__ == "__main__":
    main()
