# -*- coding: utf-8 -*-
"""50 provisoriska is:review-kort -> full v3.

## Varför just den här poolen

Adam 2026-08-16: *"skriv om 50 av de sökkollade provisoriska v3 korten i
is:review"*. Det vänder prioriteringen från 2026-08-11, där de suspenderade
korten gick först med motiveringen att de var helt osynliga för honom. De 550
provisoriska är motsatsen: de ligger i kön och pluggas varje dag.

Urvalet är rankat med `v3_urgency_provisorisk.py` (ny fil, se dess docstring).
Hela batchen har intervall 1-2 dagar och 2-3 lapses -- alltså kort Adam
faktiskt fastnar på just nu. Det är värt att skriva ut varför det urvalet är
rätt: ett kort med tre lapses tolkas normalt som att HAN inte kan ordet, men i
det här decket är den andra förklaringen minst lika trolig -- att kortet är
fel och att han failar det för att han lärt sig rätt sak.

**Den tolkningen bekräftades.** `jämka`, kortet med flest lapses i hela poolen,
saknade två av SO:s tre betydelser.

## Vad genomgången hittade

**Tretton kort saknade minst en hel betydelse** -- samma dominerande felmönster
som i åtta omgångar i rad:

| Ord | Vad som saknades |
|---|---|
| `jämka` | 'minska i viss utsträckning' (juridiskt) OCH 'avpassa åsikter' |
| `skygga` | 'undvika, vara rädd' OCH 'ge skugga åt' -- FACIT sa `ge skugga` |
| `förlägga` | 'lämna kapital för drivande av rörelse' -- FACIT sa `finansiera` |
| `traktat` | 'avhandling' (Voltaires traktat om toleransen) |
| `hissna` | 'känna stark häpnad' |
| `hädisk` | 'som avviker från allmänt accepterade uppfattningar' |
| `domptera` | 'äv. med avseende på personer' (domptera publiken) |
| `vitter` | 'om verk och tal: skönlitterär' |
| `lokus` | 'bestämd plats' |
| `gästgiveri` | 'verksamhet som gästgivare' |
| `sodomi` | 'analsex' |
| `prosaisk` | SAOL:s 'på prosa, prosa-' |
| `tillgå` | fanns, men ogrupperade synonymer |

**`kerub` hade betydelserna i fel ordning.** Kortet ledde med 'bevingad
väktarängel'. Det är SO:s ANDRA betydelse, märkt "ursprungligen". Den första --
och den enda de flesta möter -- är 'liten, knubbig ängel i barngestalt'. FACIT
sa `änglabarn`. Kortet lärde alltså ut undantaget som huvudregel.

## Fyra rena sakfel

* **`braska`** hade exempelmeningen *"Snön braskar när man går på den kalla
  vintervägen"*, alltså snö som knastrar under fötterna. SO:s definition är
  'vara under fryspunkten' och hela belägget är ordspråket *om Anders braskar,
  julen slaskar* -- det handlar om kylan, inte om ljudet under skorna. FACIT:
  `vara kallt ute`. Exemplet är utbytt mot ordspråket.
* **`tillskriva`** märkte brevbetydelsen "(ålderdomligt)". Varken SO eller SAOL
  märker den; SAOL skriver rakt av 'kontakta med formellt brev'. En påhittad
  bruklighetsmärkning är samma feltyp som `paletå` den 13 augusti.
* **`lägga rabarber på något`** definierades som "olovligen ta något åt sig".
  SO skriver '(hänsynslöst) lägga beslag på något', och det egna exemplet är en
  budgivning på en auktion -- fullt lagligt. Ordet är hänsynslöst, inte olagligt.
* **`korpulent`** sa "kraftigt byggd och överviktig". SO: 'som har stort
  kroppsomfång'. "Kraftigt byggd" antyder muskulös, vilket är fel ord.

## Ett stavfel som stått på ett levande kort

`lysning` hade synonymen **`tilllännagivande`** -- tre l och ett bortfallet k.
Rätt form är `tillkännagivande`.

## Fjorton felaktiga registermärkningar

Den vanligaste var att märka ett ålderdomligt eller vardagligt ord som
`litterär` eller `formell`. Ordböckernas egen märkning gäller:

`snits` (SO: något vardagligt, kortet sa litterär) · `nimrod` (SO: något
högtidligt, kortet sa skämtsam) · `minaret` (omärkt, kortet sa vardaglig) ·
`högmäld` (SAOL: åld., kortet sa formell) · `gästgiveri` (SO: något
ålderdomligt, kortet sa litterär) · `braska` (SO: något ålderdomligt) ·
`sälla` (SO: högtidligt/ålderdomligt) · `njugg` · `konfekt` · `huvudbry` ·
`canasta` · `ockult` · `domptera` · `mista sansen`.

Alla femtio får dessutom **domänaxeln** ifylld enligt Adams regel 2026-08-11 --
poolen hade genomgående tvåaxligt register (`formell, neutral`), vilket är
exakt den registerbrist som gav dem hög rankning i urgency-listan.

## Tre flerordsuttryck med förorenat underlag

Fritextsökningen kan inte slå upp fraser, så svaret gäller huvudordet:

* `mista sansen` fick posterna för **`mista`** och **`sans`** var för sig. Båda
  behövs dock: SO:s `sans` ger *tillstånd av normalt medvetande* OCH *tillstånd
  av lugn och självbehärskning*, och har `mista sansen` som eget exempel. De två
  betydelserna på kortet är alltså belagda, bara inte som en frasartikel.
* `vara på örat` fick **`öra`** och **`örsprång`** -- värk i mellanörat och
  läran om örats sjukdomar. Helt fel spår. Skriven mot allmän websökning enligt
  regeln 2026-08-11; synonymer.se ger `berusad` för just frasen.
* `lägga rabarber på något` fick växten **rabarber**, men här räddade SO
  frasen: dess andra definition ÄR '(hänsynslöst) lägga beslag på något', med
  frasen som eget exempel.

## Etymologier

Trettioett kort får en etymologirad, alla tagna ordagrant ur uppslagets
ETYM-fält. Villkoret är "hjälper ursprunget?", inte "vet vi ursprunget?" -- de
utelämnade är de där ursprunget är ren språkhistorisk trivia.

Den mest användbara är `lägga rabarber på något`: idiomet är en **skämtsam
ombildning av `lägga embargo på`** från 1893. Det förklarar varför en köksväxt
står i ett uttryck om att lägga beslag på saker, och gör frasen möjlig att
minnas i stället för att nöta.

`vitter` är den näst mest användbara: fornsvenska *viter* 'vettig, klok',
besläktat med **veta**. Ordet har alltså ingenting med `vit` att göra, vilket är
den gissning formen inbjuder till.

## Medvetna avgränsningar

Regeln sedan 2026-08-15 är att en betydelse som står i SO eller SAOL kommer med,
och att tveksamma fall löses genom att ta med. Dessa tre står i VARKEN SO eller
SAOL i dagens hämtning och utelämnas därför:

* **`lokus` får inte betydelsen 'toalett'.** Den är välkänd i talspråk och finns
  i SAOB, men varken SO, SAOL eller Wiktionary gav den i dagens svar.
  Källhierarkin låter SO och SAOL avgöra. Noterat här därför att utelämnandet är
  det enda i batchen som riskerar att möta Adam på ett prov.
* **`braska` får inte betydelsen 'skryta, göra väsen av sig'** (braskande
  rubriker). Den finns i etymologiraden som fornsvenska 'bullra; uppträda
  överdådigt', men etymologi är inte en betydelse i dag.
* **`sälla` får inte adjektivbetydelsen 'lycklig, salig'** (de sälla
  jaktmarkerna). Det är ett eget uppslagsord, `säll`, med egen etymologi
  (fornsvenska *säl* mot verbets *sälla sik*) -- samma sak som `divan`/`diva`
  den 15 augusti, inte en andra betydelse hos samma ord.

## Synonymlistorna skrevs om två gånger, och det är det viktigaste i batchen

Första versionen tog synonymerna från **synonymer.se**. `forgranska.py`
underkände då **63 hårda anmärkningar på 50 kort** -- nästan uteslutande
`synonym_utan_ordboksbelagg`. Regeln är strängare än jag antog: en synonym
duger bara om SO själv taggar den `SYN:synonym`, ELLER om den står ordagrant i
SO:s eller SAOL:s definitionstext. Att synonymer.se listar ordet räknas inte.

Det är rätt regel, och skälet syns i utfallet: av `korpulent`s föreslagna
`fet, fyllig, rund` står bara `fetlagd` i SAOL. `fyllig` och `trind` är
synonymer.se:s associationer, inte ordbokens -- och ett kort som lär ut en
association som en betydelse är precis det som gör Adam osäker på provet.

Samtliga listor är därför omskrivna mot `_ordboksbelagg()`s faktiska facit.
Följden är att **femton kort får tom synonymlista**, vilket är normalfallet i
det här decket (69 %) och uttryckligen godkänt. Där ordbokens enda glosa ÄR
definitionen är huvudbetydelsen redan synonymen, och en upprepning på raden
under tillför ingenting.

Ett antal huvudbetydelser är dessutom omformulerade för att de annars hade
innehållit sin egen synonym: `hemman` sa 'jordbruksfastighet' och hade
`jordbruksfastighet` som synonym, `gallup` sa 'opinionsundersökning' likaså.
Omskrivningen gör synonymraden till information i stället för eko.

## Tre registermärkningar som ordboken motsade

`sälla`, `vanmakt` och `kalfatra` fick alla `register_motsager_markning`.
`vanmakt` och `kalfatra` är rättade rakt av. `sälla` går inte att rätta: SO
märker ordet BÅDE 'något högtidligt' OCH 'något ålderdomligt', och den låsta
registervokabulären har en enda stilnivåaxel -- ordet kan inte vara båda. Det
löses med ett motiverat undantag i TILLAT, inte genom att välja bort en av
ordbokens märkningar tyst.
"""
import json
import sys
import urllib.parse

SESSION = "sessions/session_2026-08-16_v3-omgranskning.json"
SVENSKA = "https://svenska.se/api/msearch?ord={}"

# Kortets framsida -> det uppslagsord som faktiskt slogs upp.
K = {}

PAUSAS = set()

TILLAT = {
    "mista sansen": {
        "frammande_uppslagsord":
            "Flerordsfras: fritextsökningen returnerade posterna för `mista` "
            "('förlora ngt man äger') och `sans` var för sig, inte frasen. Båda "
            "behövs och båda bär kortet: SO:s `sans` ger 'tillstånd av normalt "
            "medvetande' OCH 'tillstånd av lugn och självbehärskning', och har "
            "`mista sansen` som eget exempel under den första.",
        "register_motsager_markning":
            "SO:s märkning 'mindre brukligt' gäller `mista` i sin allmänna "
            "betydelse 'förlora', inte frasen. Frasen är levande men "
            "skriftspråklig -- `litterär` ligger närmast i den fasta listan.",
    },
    "vara på örat": {
        "frammande_uppslagsord":
            "Grövsta fallet i batchen: svaret gäller `öra` (hörselorganet, "
            "kärlets öra) och `örsprång` (värk i mellanörat, läran om örats "
            "sjukdomar). Frasen finns inte som uppslagsord i SO eller SAOL. "
            "Skriven mot allmän websökning enligt regeln 2026-08-11: "
            "synonymer.se ger `berusad` för just frasen `vara på örat`, och "
            "ordlista.se beskriver den som vardaglig med typexemplet 'lite på "
            "örat', alltså lätt berusning snarare än kraftig.",
    },
    "lägga rabarber på något": {
        "frammande_uppslagsord":
            "Svaret gäller växten `rabarber` med dess bladskaft och stjälkar. "
            "Här räddar SO ändå frasen: uppslagets andra definition ÄR "
            "'(hänsynslöst) lägga beslag på något', märkt vardagligt, med frasen "
            "som eget exempel och en budgivning på auktion som belägg. "
            "Wiktionary bekräftar med 'lägga beslag på; lägga vantarna på'.",
    },
    "jämka": {
        "frammande_uppslagsord":
            "Enda främmande träffen är `jämka samman`, som är SO:s egen "
            "underrubrik till uppslagsordets tredje betydelse ('avpassa') och "
            "inte ett annat ord. Kortets tredje betydelse bygger just på den.",
    },
    "hissna": {
        "frammande_uppslagsord":
            "SO:s uppslagsord är stavat `hisna` och SO skriver uttryckligen att "
            "den formen är att föredra ('hellre än'). `hissna` är samma ord i "
            "SAOL-stavning, inte ett annat ord. Kortets framsida behålls -- det "
            "är den formen Adam mött -- men synonymlistan är tom eftersom "
            "ordboksbelägget hänger på den andra stavningen.",
    },
    "sälla": {
        "register_motsager_markning":
            "SO ger TVÅ märkningar för samma betydelse: 'något högtidligt' OCH "
            "'något ålderdomligt'. Den låsta registervokabulären har en enda "
            "stilnivåaxel, så båda kan inte skrivas. `högtidlig` väljs eftersom "
            "SO listar den först och eftersom ordet fortfarande är gångbart i "
            "skrift ('sälla sig till oppositionen' är samtida tidningsspråk), "
            "medan `arkaisk` hade påstått att det gått ur bruk.",
        "frammande_uppslagsord":
            "Svaret slår ihop verbet `sälla` ('ansluta sig', fornsvenska sälla "
            "sik, till sälle) med adjektivet `säll` ('lycklig, salig', "
            "fornsvenska säl) -- skilda uppslagsord med skild etymologi och "
            "skilda första belägg (ca 1430 mot ca 1325). Kortet använder bara "
            "verbposten. Samma tvetydighet som `divan`/`diva` den 15 augusti.",
    },
    "färm": {
        "frammande_uppslagsord":
            "SO:s uppslagsord är stavat `ferm`, och exemplet lyder 'det är ferm "
            "betjäning på kinesrestaurangen'. `färm` är samma ord i annan "
            "stavning -- SAOL saknar posten helt, men synonymer.se listar `ferm` "
            "först bland synonymerna till `färm`. Kortets framsida behålls.",
    },
    "braska": {
        "register_motsager_markning":
            "SO märker 'något ålderdomligt', SAOL saknar märkning. Kortet är "
            "märkt `ngt ålderdomlig` efter SO, som är den utförligare posten.",
    },
    "skygga": {
        "frammande_uppslagsord":
            "Svaret blandar verbet `skygga` med adjektivet `skygg` ('som ogärna "
            "umgås med andra människor', 'mycket skygg'). Kortet använder bara "
            "verbposten, som SO ger tre betydelser: rycka kroppen bakåt, "
            "undvika/vara rädd, och ge skugga åt (SAOL: 'ge skugga el. skydd', "
            "märkt åld., med exemplet 'skygga ögonen med handen').",
    },
    "traktat": {
        "frammande_uppslagsord":
            "Svaret drar in verbet `trakta` ('ivrigt försöka uppnå', 'sträva att "
            "skada'), ett eget uppslagsord. Kortet använder bara substantivet, "
            "som SO ger tre betydelser: överenskommelse mellan stater, "
            "avhandling, och uppbygglig religiös småskrift.",
    },
    "konfekt": {
        "frammande_uppslagsord":
            "Svaret listar idiomen `variera konfekten` ('göra något omväxlande') "
            "och `bli lurad på konfekten` som egna betydelser. Det är fasta "
            "uttryck som innehåller ordet, inte betydelser hos substantivet -- "
            "kortet skriver därför en betydelse och lägger idiomet i exemplet.",
    },
}

B = '<font color="#3498db">{}</font>'

KORT = {
    # ---------------------------------------------------------------- 1-10
    "jämka": {
        "hb": "försiktigt maka något till ett lämpligare läge ; minska något i viss utsträckning ; avpassa åsikter efter varandra",
        "syn": ["flytta", "minska", "avpassa", "anpassa"],
        "grp": [["flytta"], ["minska"], ["avpassa", "anpassa"]],
        "ex": f'Hon stannade framför spegeln för att {B.format("jämka")} på hatten.',
        "reg": "neutral, neutral, allmän ; formell, neutral, juridik ; formell, neutral, politik",
        "ety": None,
        "skal": "SO ger TRE betydelser: '(försiktigt eller obetydligt) flytta något "
                "till lämpligare position', 'minska i viss utsträckning' och "
                "'avpassa' med exemplet 'jämka samman olika åsikter'. SAOL: "
                "'anpassa'. Kortet hade bara den första. Samtliga fyra synonymer "
                "står ordagrant i SO:s eller SAOL:s definitionstext; "
                "`sammanjämka` utesluts som cirkulär.",
    },
    "märgfull": {
        "hb": "full av inre kraft och uttrycksfullhet",
        "syn": ["spännande"],
        "grp": None,
        "ex": f'Hennes romaner utmärktes av ett {B.format("märgfullt")} språk.',
        "reg": "litterär, positiv, allmän",
        "ety": None,
        "skal": "SO: 'full av inre kraft och uttrycksfullhet'. SAOL: 'äv. bildl. "
                "färgstark, spännande'. Kortets synonym `spännande` är SAOL:s eget "
                "andraled och står kvar. `kraftfull`, `mustig` och `kärnfull` "
                "prövades men finns bara hos synonymer.se -- de faller på "
                "ordboksbeläggsregeln, och `färgstark` går inte att lyfta ut ur "
                "SAOL:s led 'bildl. färgstark'.",
    },
    "apoplexi": {
        "hb": "slaganfall orsakat av blödning eller propp i hjärnan",
        "syn": ["slaganfall", "hjärnblödning"],
        "grp": None,
        "ex": f'Han drabbades av {B.format("apoplexi")} och förlorade talförmågan.',
        "reg": "fackspråklig, neutral, medicin",
        "ety": "av grekiska apoplexia med samma betydelse",
        "skal": "SO: 'slaganfall'. SAOL: 'slaganfall, hjärnblödning' -- båda inleder "
                "var sitt led och är belagda i ordboken själv. Kortet var redan "
                "riktigt; den röda flaggan hade ingen täckning i underlaget.",
    },
    "korpulent": {
        "hb": "som har stort kroppsomfång",
        "syn": ["fetlagd"],
        "grp": None,
        "ex": f'En värdig och {B.format("korpulent")} gentleman steg ur vagnen.',
        "reg": "formell, eufemistisk, allmän",
        "ety": None,
        "skal": "SO: 'som har stort kroppsomfång'. SAOL: 'fet, fetlagd'. Kortet sa "
                "'kraftigt byggd och överviktig' -- 'kraftigt byggd' antyder "
                "muskulositet, som varken SO eller SAOL stöder. Av kortets tre "
                "synonymer står bara `fetlagd` i en ordbok; `fyllig` och `rund` är "
                "synonymer.se:s associationer. `fet` utgår dessutom för att den "
                "krockar med den eufemistiska valören som är hela poängen med ordet.",
    },
    "tillgå": {
        "hb": "utspela sig på ett visst sätt ; ha möjlighet att använda",
        "syn": ["ske", "förlöpa", "utnyttja"],
        "grp": [["ske", "förlöpa"], ["utnyttja"]],
        "ex": f'Han berättade hur det hela hade {B.format("tillgått")}.',
        "reg": "formell, neutral, allmän",
        "ety": None,
        "skal": "SO: 'utspela sig' och '(ha möjlighet att) utnyttja', med "
                "`ha att tillgå` som eget uttryck. SAOL: 'ske, förlöpa'. Båda "
                "betydelserna fanns redan; ändringen är att synonymerna nu grupperas "
                "per betydelse. `stå till buds` byttes mot SO:s eget `utnyttja`.",
    },
    "prosaisk": {
        "hb": "vardaglig och saklig, utan poetisk lyftning ; skriven på prosa",
        "syn": [],
        "grp": None,
        "ex": f'Hennes något {B.format("prosaiska")} man talade helst om hyra och räkningar.',
        "reg": "litterär, lätt negativ, allmän ; fackspråklig, neutral, litteraturvetenskap",
        "ety": None,
        "skal": "SO: 'vardaglig och saklig', 'äv. med tonvikt på enkelhet och "
                "tristess'. SAOL ger dessutom den bokstavliga betydelsen 'på prosa, "
                "prosa-', som kortet saknade. Tom synonymlista: ordbokens enda "
                "belagda glosor är `vardaglig`, `torr` och `prosa-`, varav de två "
                "första redan står i huvudbetydelsen och den tredje röjer "
                "uppslagsordet.",
    },
    "njugg": {
        "hb": "onödigt sniken och gnidig ; alltför knappt tilltagen",
        "syn": ["snål", "knapp"],
        "grp": [["snål"], ["knapp"]],
        "ex": f'Försäkringsbolagen är {B.format("njugga")} när det gäller skadestånd.',
        "reg": "ngt ålderdomlig, negativ, allmän ; neutral, negativ, allmän",
        "ety": None,
        "skal": "SO: '(onödigt) snål och knusslig'. SAOL: 'snål; knapp' -- två led, "
                "alltså två betydelser, och båda glosorna är ordbokens egna. Kortet "
                "var märkt `vardaglig`, vilket varken SO eller SAOL stöder. "
                "Huvudbetydelsen är omskriven så att `snål` kan stå som synonym i "
                "stället för att upprepa definitionen.",
    },
    "traktat": {
        "hb": "skriftlig överenskommelse mellan stater ; lärd avhandling ; uppbygglig religiös skrift",
        "syn": ["fördrag", "avhandling", "uppbygglig skrift"],
        "grp": [["fördrag"], ["avhandling"], ["uppbygglig skrift"]],
        "ex": f'Länderna undertecknade en {B.format("traktat")} om ömsesidigt bistånd.',
        "reg": "formell, neutral, juridik ; formell, neutral, litteraturvetenskap ; formell, neutral, religion",
        "ety": None,
        "skal": "SO ger TRE betydelser: 'skriftlig överenskommelse mellan stater', "
                "'avhandling' (Voltaires traktat om toleransen) och 'uppbygglig "
                "(religiös) småskrift'. SAOL: 'fördrag | filosofisk småskrift'. "
                "Kortet hade den första och den tredje men saknade "
                "avhandlingsbetydelsen -- den som SO belägger utförligast.",
    },
    "hissna": {
        "hb": "börja känna svindel ; känna stark häpnad",
        "syn": [],
        "grp": None,
        "ex": f'Hon {B.format("hisnade")} när hon fick veta vad hotellsviten kostade.',
        "reg": "litterär, neutral, allmän",
        "ety": None,
        "skal": "SO: '(börja) känna svindel' och 'känna stark häpnad', den andra med "
                "exemplet om hotellsviten. Kortet hade bara svindelbetydelsen. "
                "Exemplet är bytt till häpnadsbelägget, eftersom den betydelsen är "
                "den som saknades. Tom synonymlista -- se TILLAT: uppslagsordet är "
                "stavat `hisna`, så ordboksbelägget kan inte knytas till kortets "
                "framsida.",
    },
    "snits": {
        "hb": "elegant och skickligt utförande",
        "syn": ["elegans", "stil"],
        "grp": None,
        "ex": f'Han hade en sådan {B.format("snits")} i skidåkningen att alla i backen vände sig om.',
        "reg": "vardaglig, positiv, allmän",
        "ety": None,
        "skal": "SO: 'elegans i utförande', märkt 'något vardagligt'. SAOL: 'stil, "
                "elegans', märkt 'vard.' -- BÅDA ordböckerna märker ordet vardagligt, "
                "och kortet sa `litterär`. Det är motsatsen till vad källorna säger. "
                "`piff` utgår: bara synonymer.se har den.",
    },
    # --------------------------------------------------------------- 11-20
    "skov": {
        "hb": "avgränsad period mellan två andra ; uppflammande av ett kroniskt sjukdomstillstånd",
        "syn": ["period", "uppflammande"],
        "grp": [["period"], ["uppflammande"]],
        "ex": f'Manodepressiv sjukdom kännetecknas av återkommande {B.format("skov")}.',
        "reg": "formell, neutral, allmän ; fackspråklig, neutral, medicin",
        "ety": "fornsvenska skof 'stöt, knuff'; till skjuva; jfr uppskov",
        "skal": "SO ger båda betydelserna: 'period som på något sätt är avskild från "
                "den föregående och den efterföljande perioden' och 'uppflammande av "
                "ett (kroniskt) sjukdomstillstånd'. SAOL: 'uppflammande av sjukdom'. "
                "`skede` och `anfall` utgår -- bara synonymer.se har dem. Etymologin "
                "binder ihop ordet med `uppskov`, vilket FACIT själv pekar på.",
    },
    "nimrod": {
        "hb": "ivrig och skicklig jägare",
        "syn": [],
        "grp": None,
        "ex": f'Farfar var en {B.format("nimrod")} som kände varje spår i skogen.',
        "reg": "högtidlig, positiv, jakt",
        "ety": "till Nimrod, namn på skicklig jägare i Gamla testamentet",
        "skal": "SO: 'ivrig och skicklig jägare', märkt 'något högtidligt'. Kortet sa "
                "`skämtsam`, vilket ingen källa stöder -- högtidligt och skämtsamt är "
                "motsatta valörer. Tom synonymlista: `jägare` är hyperonym och står "
                "dessutom redan i definitionen. Etymologin är hela poängen med ordet "
                "och förklarar märkningen.",
    },
    "mista sansen": {
        "hb": "förlora medvetandet ; förlora sitt lugn och sin självbehärskning",
        "syn": [],
        "grp": None,
        "ex": f'Han {B.format("miste sansen")} vid minsta tecken på blod.',
        "reg": "litterär, neutral, allmän",
        "ety": "sans av franska sens 'mening; förnuft'; av latin sensus 'förnimmelse'",
        "skal": "Frasen finns inte som eget uppslagsord, men SO:s `sans` ger båda "
                "betydelserna kortet påstår -- 'tillstånd av normalt medvetande' och "
                "'tillstånd av lugn och självbehärskning' -- och har `mista sansen` "
                "som eget exempel under den första. Tom synonymlista: ordboksbelägget "
                "hör till `mista` och `sans` var för sig, inte till frasen.",
    },
    "sälla": {
        "hb": "ansluta sig till en grupp",
        "syn": ["ansluta sig"],
        "grp": None,
        "ex": f'Hon {B.format("sällade")} sig genast till kamraterna när hon kom in i lokalen.',
        "reg": "högtidlig, neutral, allmän",
        "ety": "fornsvenska sälla sik; till sälle",
        "skal": "SO: 'ansluta sig', märkt både 'något högtidligt' och 'något "
                "ålderdomligt'. Kortet sa `litterär, neutral`. Adjektivbetydelsen "
                "'lycklig, salig' hör till det egna uppslagsordet `säll` och kommer "
                "inte med, se TILLAT.",
    },
    "utpräglad": {
        "hb": "mycket tydlig eller typisk",
        "syn": ["påtaglig"],
        "grp": None,
        "ex": f'Hon är en {B.format("utpräglad")} individualist som aldrig följer strömmen.',
        "reg": "neutral, neutral, allmän",
        "ety": "till ut och prägla",
        "skal": "SO: 'mycket tydlig eller typisk', omärkt. SAOL: 'tydlig, påtaglig'. "
                "Kortet var riktigt; registret ändras från `formell` till `neutral` "
                "eftersom ingen av ordböckerna märker ordet och SO:s sju exempel är "
                "genomgående vardagliga. `påtaglig` är SAOL:s eget andraled och det "
                "enda av kortets synonymförslag som har ordboksbelägg.",
    },
    "fåmäld": {
        "hb": "som ogärna yttrar sig",
        "syn": ["fåordig"],
        "grp": None,
        "ex": f'Statsministern var ytterst {B.format("fåmäld")} efter mötet.',
        "reg": "litterär, neutral, allmän",
        "ety": "till få och mäla; jfr lågmäld, högmäld",
        "skal": "SO: 'som ogärna yttrar sig'. SAOL: 'fåordig'. Kortet var riktigt; "
                "`tystlåten` och `ordknapp` utgår eftersom bara synonymer.se har dem. "
                "Etymologiraden binder ihop ordet med `högmäld`, som ligger i samma "
                "batch -- SO:s egen etymologi hänvisar till -mäld-familjen.",
    },
    "likgiltig": {
        "hb": "helt ointresserad ; som inte förmår väcka något intresse",
        "syn": ["ointresserad", "egal"],
        "grp": [["ointresserad"], ["egal"]],
        "ex": f'Vem av de båda kandidaterna som vinner är i grunden {B.format("likgiltigt")}.',
        "reg": "neutral, negativ, allmän ; neutral, neutral, allmän",
        "ety": "efter tyska gleichgültig med samma betydelse",
        "skal": "SO ger båda betydelserna i kortets ordning, och pekar själv ut "
                "`egal` som jämförelseord till den andra. Exemplet är bytt till den "
                "ANDRA betydelsen, eftersom det är den Adam lär sig sämre: "
                "'likgiltig' om en person är genomskinligt, 'likgiltigt' om ett val "
                "är det inte. FACIT sa just `betydelselös`.",
    },
    "effektuera": {
        "hb": "genomföra en beställning eller ett fattat beslut",
        "syn": ["verkställa", "utföra"],
        "grp": None,
        "ex": f'Lagret lovade att {B.format("effektuera")} beställningen inom två arbetsdagar.',
        "reg": "formell, neutral, ekonomi",
        "ety": None,
        "skal": "SO: 'verkställa', märkt 'något formellt', med 'effektuera en "
                "beställning' som första exempel. SAOL: 'utföra, verkställa'. Båda "
                "synonymerna är ordböckernas egna. Huvudbetydelsen är omskriven till "
                "'genomföra' så att `verkställa` blir information på synonymraden i "
                "stället för en upprepning.",
    },
    "sodomi": {
        "hb": "sexuell handling som förr ansågs avvika från det tillåtna ; analsex",
        "syn": [],
        "grp": None,
        "ex": f'Historiskt förbjöds {B.format("sodomi")} genom sträng lagstiftning.',
        "reg": "arkaisk, neutral, juridik ; ngt ålderdomlig, neutral, allmän",
        "ety": None,
        "skal": "SO ger TVÅ betydelser: 'sexuell handling som förr ansågs avvika från "
                "det tillåtna eller normala' och 'analsex'. Kortet hade bara den "
                "första. Tom synonymlista behålls: den enda ordboksbelagda glosan är "
                "`analsex`, som redan står som andra betydelse.",
    },
    "gästgiveri": {
        "hb": "traditionsrikt matställe och hotell vid allmän väg ; verksamhet som gästgivare",
        "syn": ["gästgivargård", "värdshusrörelse"],
        "grp": [["gästgivargård"], ["värdshusrörelse"]],
        "ex": f'Det berömda {B.format("gästgiveriet")} vid foten av Hallandsåsen.',
        "reg": "ngt ålderdomlig, neutral, historia ; ngt ålderdomlig, neutral, ekonomi",
        "ety": None,
        "skal": "SO ger två betydelser: byggnaden och verksamheten. SAOL har bara den "
                "andra ('värdshusrörelse'). Kortet hade bara byggnaden. Märkningen "
                "'något ålderdomligt' är SO:s egen; kortet sa `litterär`. Båda "
                "synonymerna står i ordbokstexten.",
    },
    # --------------------------------------------------------------- 21-30
    "konfekt": {
        "hb": "utsökta små sötsaker",
        "syn": ["finare godis"],
        "grp": None,
        "ex": f'Det gäller att variera {B.format("konfekten")} så att gästerna inte tröttnar.',
        "reg": "neutral, neutral, matlagning",
        "ety": None,
        "skal": "SO: 'finare sötsaker'. SAOL: 'sötsaker, finare godis'. Kortet sa "
                "`vardaglig`, vilket ingen källa stöder. Exemplet är bytt till SO:s "
                "eget idiom `variera konfekten`, som är den form Adam faktiskt möter "
                "ordet i. `praliner` och `bonbon` utgår -- bara synonymer.se har dem "
                "-- och `konfektyrer` är dessutom cirkulär.",
    },
    "gallup": {
        "hb": "undersökning av åsikter hos ett representativt urval personer",
        "syn": ["opinionsundersökning"],
        "grp": None,
        "ex": f'En {B.format("gallup")} visade att över 90 procent ansåg miljöfrågorna viktiga.',
        "reg": "neutral, neutral, politik",
        "ety": "efter den amerikanske sociologen George Gallup",
        "skal": "SO: 'opinionsundersökning som utförs genom frågor till ett "
                "representativt urval personer'. Kortet sa `vardaglig`; ordet är "
                "omärkt i båda ordböckerna och hör hemma i nyhetsspråk. "
                "Huvudbetydelsen är omskriven så att SO:s egen glosa "
                "`opinionsundersökning` kan stå som synonym i stället för att "
                "upprepas. `gallupundersökning` är cirkulär och utgår.",
    },
    "inbunden": {
        "hb": "obenägen att yttra sig ; om bok: bunden i hårda pärmar",
        "syn": ["sluten", "tyst", "försedd med pärmar"],
        "grp": [["sluten", "tyst"], ["försedd med pärmar"]],
        "ex": f'Efter hustruns död blev han alltmer {B.format("inbunden")}.',
        "reg": "neutral, lätt negativ, allmän ; neutral, neutral, allmän",
        "ety": "jfr fornsvenska inbundin 'innestängd; invecklad'",
        "skal": "SO ger båda betydelserna: 'försedd med pärmar' och 'obenägen att "
                "yttra sig'. SAOL: 'tyst, sluten' -- båda glosorna är alltså "
                "ordbokens egna. Bokbetydelsens enda belagda glosa är SO:s "
                "omskrivning 'försedd med pärmar'; huvudbetydelsen är därför "
                "formulerad om till 'bunden i hårda pärmar' så att raden inte "
                "upprepar sig.",
    },
    "skygga": {
        "hb": "kasta sig bakåt inför något skrämmande ; dra sig undan av rädsla ; skärma av från ljus",
        "syn": ["rycka undan", "undvika", "ge skugga åt"],
        "grp": [["rycka undan"], ["undvika"], ["ge skugga åt"]],
        "ex": f'Vi får inte {B.format("skygga")} för att tala klartext om kostnaderna.',
        "reg": "neutral, neutral, allmän ; neutral, neutral, allmän ; arkaisk, neutral, allmän",
        "ety": "fornsvenska skygga; bildn. till skygg",
        "skal": "SO ger TRE verbbetydelser: 'rycka (kroppen) bakåt eller åt sidan som "
                "reaktion på något skrämmande', 'undvika, vara rädd' (äv. bildligt) "
                "och 'ge skugga åt'. SAOL bekräftar den tredje: 'ge skugga el. "
                "skydd', märkt åld., med exemplet 'skygga ögonen med handen'. Kortet "
                "hade bara den första -- och FACIT pekade uttryckligen på `ge skugga`. "
                "Alla tre synonymer står i SO:s definitionstext; `skygg` utgår som "
                "cirkulär och `sky` saknar ordboksbelägg.",
    },
    "omsider": {
        "hb": "efter viss lång tid",
        "syn": ["slutligen", "med tiden"],
        "grp": None,
        "ex": f'Sent {B.format("omsider")} blev hennes författarskap upptäckt.',
        "reg": "litterär, neutral, allmän",
        "ety": "fornsvenska um sidher; troligen besläktat med sedan",
        "skal": "SO: 'efter viss (lång) tid'. SAOL: 'slutligen; med tiden' -- båda "
                "leden tas som synonymer. Kortet var riktigt. Exemplet är omskrivet "
                "så att den fasta frasen `sent omsider` syns; den är enligt SO den "
                "form ordet nästan alltid uppträder i.",
    },
    "färm": {
        "hb": "snabb och ivrig i sitt utförande",
        "syn": [],
        "grp": None,
        "ex": f'Det är {B.format("färm")} betjäning på restaurangen vid torget.',
        "reg": "ngt ålderdomlig, positiv, allmän",
        "ety": "av franska ferme 'fast; stadig'; av latin firmus; jfr firma",
        "skal": "SO:s uppslagsord är stavat `ferm`: 'snabb och ivrig', 'ofta om "
                "handling eller dylikt'. Kortet sa 'snabb och skicklig' -- SO skriver "
                "ivrig, inte skicklig. SAOL saknar posten helt, vilket motiverar "
                "`ngt ålderdomlig`. Tom synonymlista: ordboksbelägget är knutet till "
                "stavningen `ferm`, se TILLAT.",
    },
    "högmäld": {
        "hb": "som talar med stark och bärande röst",
        "syn": ["högröstad"],
        "grp": None,
        "ex": f'De {B.format("högmälda")} orden från talaren nådde hela salen.',
        "reg": "arkaisk, neutral, allmän",
        "ety": "till hög och mäla; jfr fåmäld, lågmäld",
        "skal": "SAOL: 'högröstad', märkt åld. SO saknar posten helt, vilket i sig "
                "är en bruklighetsuppgift. Kortet sa `formell, neutral`; åld. i SAOL "
                "plus frånvaro i SO ger `arkaisk`. `bullersam` utgår -- bara "
                "synonymer.se har den. Etymologin är samma bildning som `fåmäld` i "
                "denna batch, vars SO-post hänvisar till -mäld-familjen.",
    },
    "hemman": {
        "hb": "gård med tillhörande jord, räknad som en ekonomisk enhet",
        "syn": ["jordbruksfastighet"],
        "grp": None,
        "ex": f'Familjen brukade samma {B.format("hemman")} i fem generationer.',
        "reg": "arkaisk, neutral, jordbruk",
        "ety": "fornsvenska heman 'bostad; gård'; till hember 'hem'",
        "skal": "SO: 'jordbruksfastighet betraktad som ekonomisk enhet', märkt "
                "'numera ej officiell beteckning'. SAOL: 'jordbruksfastighet'. "
                "Huvudbetydelsen är omskriven så att ordbokens egen glosa kan stå på "
                "synonymraden i stället för att upprepas. `bondgård` och "
                "`lantegendom` utgår -- bara synonymer.se har dem.",
    },
    "minaret": {
        "hb": "smalt torn invid en moské, varifrån bönetimmarna ropas ut",
        "syn": [],
        "grp": None,
        "ex": f'{B.format("Minareten")} på den gamla moskén syntes långt bort.',
        "reg": "neutral, neutral, religion",
        "ety": "ur arabiska manara 'fyrtorn; torn vid moské'; till nar 'eld'",
        "skal": "SO: 'torn för böneutrop invid moské'. SAOL: 'smalt torn vid moské "
                "varifrån bönetimmarna utropas'. Kortet sa `vardaglig`, vilket ingen "
                "källa stöder -- ordet är den neutrala fackbeteckningen. Tom "
                "synonymlista: `bönetorn` finns bara hos synonymer.se, och `torn` är "
                "hyperonym. Etymologin förklarar varför ett bönetorn delar ursprung "
                "med ett fyrtorn.",
    },
    "braska": {
        "hb": "vara mycket kallt, under fryspunkten",
        "syn": ["knastra i köld"],
        "grp": None,
        "ex": f'Om Anders {B.format("braskar")}, slaskar julen.',
        "reg": "ngt ålderdomlig, neutral, allmän",
        "ety": "jfr fornsvenska braska 'bullra'; av ljudhärmande ursprung",
        "skal": "SO: 'vara under fryspunkten', märkt 'något ålderdomligt', med "
                "ordspråket 'om Anders braskar, julen slaskar' som enda belägg. SAOL: "
                "'knastra i köld'. FACIT: `vara kallt ute`. Kortets exempel -- 'snön "
                "braskar när man går på den kalla vintervägen' -- läste in ett ljud "
                "under fötterna som ingen källa stöder; det är KYLAN som braskar. "
                "Exemplet är bytt till ordspråket.",
    },
    # --------------------------------------------------------------- 31-40
    "vanmakt": {
        "hb": "känsla av att inte kunna göra något åt saken ; kortvarig förlust av medvetandet",
        "syn": ["oförmåga", "hjälplöshet", "tillfällig medvetslöshet"],
        "grp": [["oförmåga", "hjälplöshet"], ["tillfällig medvetslöshet"]],
        "ex": f'Myndigheternas {B.format("vanmakt")} inför våldet blev alltmer uppenbar.',
        "reg": "litterär, negativ, allmän ; ngt ålderdomlig, neutral, medicin",
        "ety": "fornsvenska vanmakt; till van- och makt",
        "skal": "SO: '(känsla av) oförmåga att företa sig något' och 'tillfällig "
                "medvetslöshet', den andra med belägget 'falla i vanmakt'. SAOL: "
                "'hjälplöshet'. Två ändringar mot kortet: valören på första "
                "betydelsen skärps till `negativ` (SO:s samtliga exempel är 'sorg "
                "och vanmakt', 'ilska och vanmakt'), och SO:s märkning 'något "
                "ålderdomligt' skrivs nu ut i registret -- den saknades och gav en "
                "hård anmärkning i förgranskningen.",
    },
    "förlägga": {
        "hb": "placera på en viss plats ; lägga undan så att det inte kan hittas ; ge ut på sitt förlag ; skjuta till kapital för en rörelse",
        "syn": ["placera", "lägga undan", "ge ut", "lämna kapital"],
        "grp": [["placera"], ["lägga undan"], ["ge ut"], ["lämna kapital"]],
        "ex": f'Författaren har {B.format("förlagt")} handlingen till 1800-talets Indien.',
        "reg": "formell, neutral, allmän ; vardaglig, neutral, allmän ; fackspråklig, neutral, litteraturvetenskap ; fackspråklig, neutral, ekonomi",
        "ety": "fornsvenska forläggia; av lågtyska vorleggen",
        "skal": "SO ger FYRA huvudbetydelser, den sista 'lämna kapital eller lån för "
                "drivande av rörelse'. Kortet hade tre och saknade finansieringen -- "
                "och riskflaggan `old_har_fler_betydelser` plus FACIT (`placera; "
                "slarva bort; publicera; finansiera`) pekade båda på just den. "
                "Samtliga fyra synonymer står i SO:s eller SAOL:s definitionstext; "
                "`slarva bort`, `publicera` och `finansiera` fanns bara hos "
                "synonymer.se och är utbytta mot ordbokens egna formuleringar. "
                "Tids-placeringen ('förlägga handlingen till 1800-talet') behandlas "
                "som en användning av den första betydelsen, eftersom SO markerar den "
                "med 'äv. bildligt'.",
    },
    "kalfatra": {
        "hb": "göra ett fartygs nåt tätt med drev och beck ; syna hårt och kritiskt",
        "syn": ["täta", "nagelfara"],
        "grp": [["täta"], ["nagelfara"]],
        "ex": f'Turerna kring företagsnedläggningen {B.format("kalfatrades")} i medierna.',
        "reg": "arkaisk, neutral, historia ; neutral, negativ, allmän",
        "ety": "av nederländska kalfateren; troligen ur arabiska qafr 'beck'",
        "skal": "SO: 'täta nåten i' (märkt historiskt) och 'strängt och kritiskt "
                "granska'. SAOL: 'täta med drev' och 'nagelfara, granska'. Två "
                "ändringar: den andra betydelsen får valören `negativ` (SO:s 'strängt "
                "och kritiskt' är inte neutralt), och domänen ändras från `sjöfart` "
                "till `historia` eftersom SO:s märkning ordagrant är 'historiskt' -- "
                "sjöfartsdomänen gav en hård anmärkning i förgranskningen. `dreva` "
                "utgår som synonym; bara synonymer.se har den.",
    },
    "tillskriva": {
        "hb": "skriva ett formellt brev till någon ; anse någon vara upphovet till något",
        "syn": ["kontakta", "tillräkna", "tillerkänna"],
        "grp": [["kontakta"], ["tillräkna", "tillerkänna"]],
        "ex": f'Man måste {B.format("tillskriva")} henne ett visst mod.',
        "reg": "formell, neutral, allmän ; formell, neutral, allmän",
        "ety": None,
        "skal": "SO ger brevbetydelsen FÖRST och utan bruklighetsmärkning; SAOL "
                "skriver rakt av 'kontakta med formellt brev' och 'tillerkänna, "
                "tillräkna'. Kortet märkte brevbetydelsen '(ålderdomligt)', vilket "
                "ingen källa stöder -- en påhittad bruklighetsmärkning, samma feltyp "
                "som `paletå` den 13 augusti. SO:s tre senare betydelser slås samman: "
                "de delar glosorna och skiljer sig bara i vad som tillskrivs.",
    },
    "häda": {
        "hb": "uttrycka upprörande ringaktning för något heligt",
        "syn": ["förhåna"],
        "grp": None,
        "ex": f'Hon {B.format("hädade")} Gud genom att uttala förbannelser.',
        "reg": "litterär, negativ, religion",
        "ety": None,
        "skal": "SO: 'uttrycka en upprörande ringaktning för', med 'äv. försvagat och "
                "skämtsamt'. SAOL: 'förhåna ngt heligt' -- den enda ordboksbelagda "
                "synonymen. Den försvagade användningen skrivs inte som egen "
                "betydelse: SO markerar den med 'äv.', inte som eget led. `smäda`, "
                "`vanhelga` och `bespotta` finns bara hos synonymer.se.",
    },
    "domptera": {
        "hb": "med upprepade övningar tvinga ett vilt djur till visst beteende ; behärska och styra en folkmassa",
        "syn": ["tämja", "tvinga"],
        "grp": [["tämja"], ["tvinga"]],
        "ex": f'En artist med en speciell förmåga att {B.format("domptera")} publiken.',
        "reg": "fackspråklig, neutral, allmän ; litterär, neutral, allmän",
        "ety": None,
        "skal": "SO: 'tvinga (vilt djur) till visst beteende genom upprepade "
                "övningar', med 'äv. med avseende på personer' och exemplet om "
                "artisten som dompterar publiken. SAOL: 'tämja djur; äv. bildl.' "
                "Kortet hade bara djurbetydelsen och var dessutom märkt `vardaglig` "
                "-- ordet är en dressyrterm. `dressera`, `kuva` och `tygla` utgår: "
                "bara synonymer.se har dem.",
    },
    "ischias": {
        "hb": "sjukligt tillstånd med smärtor kring höften och ned längs benet",
        "syn": ["nervsmärta"],
        "grp": None,
        "ex": f'{B.format("Ischias")} gjorde det svårt för honom att sitta någon längre stund.',
        "reg": "neutral, neutral, medicin",
        "ety": None,
        "skal": "SO: 'sjukligt tillstånd med smärtor i området kring höfterna och "
                "nedåt benen'. SAOL: 'nervsmärta som strålar ut i ben och fot'. "
                "Kortet var riktigt. Registret ändras från `formell` till `neutral`: "
                "ordet är allmänspråkets ord för besväret, inte fackspråkets "
                "(`ischiasneuralgi`). `höftvärk` utgår -- bara synonymer.se har den.",
    },
    "hädisk": {
        "hb": "som uttrycker hädelse ; som avviker från allmänt accepterade uppfattningar",
        "syn": [],
        "grp": None,
        "ex": f'{B.format("Hädiska")} tankar om att männen i vissa avseenden behandlas sämre än kvinnorna.',
        "reg": "neutral, negativ, religion ; neutral, lätt negativ, allmän",
        "ety": None,
        "skal": "SO ger TVÅ betydelser: 'som uttrycker eller innebär hädelse' och, "
                "'ofta utvidgat', 'som avviker från allmänt accepterade "
                "uppfattningar'. Kortet hade bara den religiösa. Den utvidgade är den "
                "vanligare i modern svenska och har SO:s eget exempel; kortets "
                "exempel är därför bytt till det. Tom synonymlista: bara `blasfemisk` "
                "har ordboksbelägg, och en ensam glosa till den ena av två betydelser "
                "kan inte grupperas.",
    },
    "canasta": {
        "hb": "ett kortspel som spelas med två kortlekar",
        "syn": [],
        "grp": None,
        "ex": f'De spelade {B.format("canasta")} vid köksbordet varje fredagskväll.',
        "reg": "neutral, neutral, sport",
        "ety": "av spanska canasta 'korg'; av grekiska kanastron; jfr kanister",
        "skal": "SO: 'ett kortspel med två kortlekar'. SAOL: 'ett kortspel'. Kortet sa "
                "'kortspel med kombinationer av kort', vilket är innehållslöst -- "
                "alla kortspel har kombinationer. SO:s `två kortlekar` är det enda "
                "som faktiskt skiljer spelet ut. Ordet saknas helt hos synonymer.se.",
    },
    "ockult": {
        "hb": "som har att göra med övernaturliga företeelser ; inte uppenbar för sinnena",
        "syn": ["övernaturlig", "dold", "osynlig"],
        "grp": [["övernaturlig"], ["dold", "osynlig"]],
        "ex": f'Med åren har hans {B.format("ockulta")} intressen blivit allt större.',
        "reg": "neutral, neutral, religion ; fackspråklig, neutral, medicin",
        "ety": "av latin occultus 'fördold; hemlig'",
        "skal": "SO: 'som inte är uppenbar för de fem sinnena eller för vanliga "
                "dödliga', 'som har att göra med övernaturliga företeelser' och, 'äv. "
                "medicin', 'dold, osynlig' (ockulta blödningar). SAOL: "
                "'övernaturlig'. Kortet hade båda betydelserna men märkte den första "
                "`vardaglig`, vilket ingen källa stöder. Alla tre synonymer står i "
                "ordbokstexten; `mystisk` och `fördold` gör det inte.",
    },
    # --------------------------------------------------------------- 41-50
    "kerub": {
        "hb": "liten, knubbig ängel i barngestalt ; ursprungligen: ängel som vaktar paradiset",
        "syn": [],
        "grp": None,
        "ex": f'Takmålningen var full av {B.format("keruber")} som svävade bland molnen.',
        "reg": "neutral, ömsint, konst ; litterär, neutral, bibliskt",
        "ety": "av hebreiska kerub 'högre väsen i nära förbindelse med gudomen'",
        "skal": "ORDNINGEN VAR OMVÄND. SO:s FÖRSTA betydelse är 'liten, knubbig ängel "
                "i barngestalt'; 'ängel som vaktar paradiset' är den andra och märkt "
                "'ursprungligen'. SAOL bekräftar: 'ängel särsk. i barngestalt'. FACIT "
                "sa `änglabarn`. Kortet ledde med undantaget och saknade "
                "huvudregeln -- det lärde alltså ut fel primärbetydelse. Tom "
                "synonymlista: `ängel` är hyperonym och de enda övriga belagda "
                "glosorna är de två definitionerna själva.",
    },
    "armod": {
        "hb": "svår fattigdom",
        "syn": [],
        "grp": None,
        "ex": f'Familjen levde i djupt {B.format("armod")} under krigsvintern.',
        "reg": "litterär, negativ, allmän",
        "ety": "av lågtyska armot; till arm 'fattig'",
        "skal": "SO: 'svår fattigdom', med belägget 'leva i armod'. SAOL: 'djup "
                "fattigdom'. Kortet var riktigt. Tom synonymlista: ordbokens båda "
                "glosor ÄR huvudbetydelsen med utbytt gradadverb, och `misär`, "
                "`torftighet` och `nöd` finns bara hos synonymer.se.",
    },
    "vitter": {
        "hb": "som tycker om och förstår sig på litteratur ; om verk eller tal: lärt skönlitterär",
        "syn": ["litteraturälskande", "skönlitterär"],
        "grp": [["litteraturälskande"], ["skönlitterär"]],
        "ex": f'Ett {B.format("vittert")} sällskap samlades varje torsdag för att diskutera poesi.',
        "reg": "högtidlig, positiv, litteraturvetenskap",
        "ety": "fornsvenska viter 'vettig; klok'; besläktat med veta",
        "skal": "SO ger två betydelser: personen som tycker om litteratur, och 'äv. om "
                "verk, tal och dylikt' ('ett vittert tacktal'). SAOL bekräftar med "
                "två led: 'skönlitterär; litteraturälskande' -- båda synonymerna är "
                "alltså SAOL:s egna. `beläst`, `boksynt` och `kultiverad` finns bara "
                "hos synonymer.se. Etymologin är den mest användbara i batchen: ordet "
                "hör ihop med `veta`, inte med `vit` som formen inbjuder till att "
                "gissa.",
    },
    "huvudbry": {
        "hb": "ansträngning att begripa något, eller det som orsakar den",
        "syn": ["tankemöda"],
        "grp": None,
        "ex": f'De saknade pengarna var ett svårt {B.format("huvudbry")} för henne.',
        "reg": "neutral, lätt negativ, allmän",
        "ety": "till bry i betydelsen 'möda, besvär; oro'",
        "skal": "SO: 'tankemöda', med 'äv. om något som orsakar tankemöda, problem "
                "eller dylikt'. SAOL: 'tankemöda'. Kortet sa `vardaglig`, vilket "
                "ingen källa stöder. Huvudbetydelsen är omskriven så att ordbokens "
                "glosa `tankemöda` kan stå som synonym; `bryderi`, `grubbel` och "
                "`bekymmer` saknar ordboksbelägg.",
    },
    "lokus": {
        "hb": "krog eller enklare restaurang ; en viss angiven punkt",
        "syn": ["matställe", "bestämd plats"],
        "grp": [["matställe"], ["bestämd plats"]],
        "ex": f'Det nya {B.format("lokuset")} vid torget serverar utsökt mat.',
        "reg": "slang, neutral, allmän ; fackspråklig, neutral, allmän",
        "ety": "studentslang; till latin locus 'plats'",
        "skal": "SO ger TVÅ betydelser: 'matställe' och 'bestämd plats'. Kortet hade "
                "bara den första, och riskflaggan `dold_betydelse` pekade på det. "
                "Båda synonymerna är SO:s egna definitioner, så huvudbetydelsen är "
                "omskriven för att inte upprepa dem. Se docstringen om varför "
                "toalettbetydelsen INTE kommer med.",
    },
    "vara på örat": {
        "hb": "vara berusad, oftast lätt",
        "syn": [],
        "grp": None,
        "ex": f'Efter tre öl var han rejält {B.format("på örat")} när han skulle hitta hem.',
        "reg": "vardaglig, skämtsam, allmän",
        "ety": None,
        "skal": "Frasen finns inte i SO eller SAOL; uppslaget gav `öra` och "
                "`örsprång`. Skriven mot allmän websökning enligt regeln 2026-08-11: "
                "synonymer.se ger `berusad` för just `vara på örat`, och ordlista.se "
                "beskriver den som vardaglig med typexemplet 'vi blev lite på örat', "
                "alltså lätt berusning. Kortet var i sak riktigt; ändringen är att "
                "graden och den skämtsamma valören skrivs ut. Tom synonymlista: "
                "ordboksbelägget gäller hörselorganet, inte frasen.",
    },
    "lysning": {
        "hb": "offentligt tillkännagivande i kyrkan om ett planerat giftermål",
        "syn": ["kungörelse"],
        "grp": None,
        "ex": f'Paret tog ut {B.format("lysning")} tre veckor före bröllopet.',
        "reg": "arkaisk, neutral, religion",
        "ety": "fornsvenska lysning, i lysninga dagher 'dag för lysning'",
        "skal": "SO: 'kungörelse i samband med gudstjänst om planerat giftermål', med "
                "belägget 'ta ut lysning'. SAOL: 'mest i äldre tid: tillkännagivande "
                "i kyrkan att ett par planerar att gifta sig'. Kortet hade "
                "STAVFELET `tilllännagivande` (tre l, bortfallet k) i synonymlistan. "
                "Det rätta ordet står nu i huvudbetydelsen i stället, och SO:s egen "
                "glosa `kungörelse` är den enda kvar på synonymraden -- "
                "`äktenskapskungörelse` är en omskrivning utan belägg.",
    },
    "anafor": {
        "hb": "stilistisk upprepning av ett ord i början av flera satser",
        "syn": [],
        "grp": None,
        "ex": f'"Jag kom, jag såg, jag segrade" är en {B.format("anafor")}.',
        "reg": "fackspråklig, neutral, litteraturvetenskap",
        "ety": "av grekiska anaphora 'tillbakasyftning'; jfr metafor",
        "skal": "SO: 'stilistisk upprepning av ord eller fras'. SAOL preciserar: "
                "'retorisk upprepning av ord i början av samordnade satser' -- det "
                "är BÖRJAN som gör figuren till anafor, och den precisionen förs in "
                "i huvudbetydelsen. Exemplet är bytt till Caesars kända trikolon, "
                "som är en riktig anafor och lättare att minnas än kortets "
                "konstruerade mening. Den lingvistiska betydelsen (tillbakasyftande "
                "pronomen) finns i varken SO eller SAOL och kommer inte med.",
    },
    "flottilj": {
        "hb": "förband av stridsflygplan ; förband av lätta örlogsfartyg",
        "syn": [],
        "grp": None,
        "ex": f'Flygvapnets första {B.format("flottilj")} stationerades i Västerås.',
        "reg": "fackspråklig, neutral, militär ; fackspråklig, neutral, sjöfart",
        "ety": "av franska flottille; diminutiv av flota 'flotta'",
        "skal": "SO: 'förband av stridsflygplan', med 'äv. om förband av "
                "krigsfartyg'. SAOL ger båda: 'förband av lätta örlogsfartyg; "
                "fredsförband inom flygvapen'. Kortet var riktigt i sak. Tom "
                "synonymlista: ordbokens enda belagda glosor ÄR de två "
                "definitionerna, och `flygförband`/`sjöstyrka` finns bara hos "
                "synonymer.se. Etymologin förklarar storleken: en flottilj är en "
                "LITEN flotta, vilket skiljer den från `flotta` och `eskader`.",
    },
    "lägga rabarber på något": {
        "hb": "hänsynslöst lägga beslag på något",
        "syn": [],
        "grp": None,
        "ex": f'Det var många på auktionen som ville {B.format("lägga rabarber på")} brevsamlingen.',
        "reg": "vardaglig, lätt negativ, allmän",
        "ety": "skämtsam ombildning av lägga embargo på, belagd sedan 1893",
        "skal": "SO ger frasen som egen definition trots att uppslaget gäller växten: "
                "'(hänsynslöst) lägga beslag på något', märkt vardagligt, med "
                "auktionsexemplet som belägg. Wiktionary: 'lägga beslag på; lägga "
                "vantarna på'. Kortet sa 'olovligen ta något åt sig' -- SO skriver "
                "hänsynslöst, inte olagligt, och SO:s eget exempel är en fullt laglig "
                "budgivning. Tom synonymlista: ordboksbelägget gäller växten "
                "rabarber. Etymologin förklarar varför en köksväxt hamnat i "
                "uttrycket.",
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
    ety = sum(1 for p in kvar if p["proposed"]["etymologi"])
    print(f"fyllde {len(kvar)} poster -- {tomma} med tom synonymlista, "
          f"{grupperade} med grupperade synonymer av {flerbet} flerbetydelsekort, "
          f"{ety} med etymologi.")
    if pausade:
        print(f"UTESLUTNA (pausas separat): {', '.join(pausade)}")


if __name__ == "__main__":
    main()
