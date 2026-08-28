# -*- coding: utf-8 -*-
"""Spar B (omgranskning), 2026-08-28: 20 kort.

OBS: kortbyggaren skriver ut "dessa kort ligger REDAN i Adams ko". Det ar
FALSKT for den har batchen -- kontrollmatning via cardsInfo visar att alla 20
ar SUSPENDERADE review-kort. Se CLAUDE.md-avsnittet om spar B:s foraldrade
varning.
"""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-omgranskning.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
KALLA = ("SO och SAOL via https://svenska.se/api/msearch?ord=%s "
         "(hamtat 2026-08-28, HTTP 200)")
B = '<font color="#3498db">%s</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, grupper=None, tillat=None,
         conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": grupper, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": KALLA % urllib.parse.quote(o),
                    "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("allestädes",
     "Överallt — numera nästan bara i uttrycket \"allestädes närvarande\"",
     "ngt ålderdomlig, neutral",
     ["överallt"],
     "Enligt läran är Gud " + B % "allestädes" + " närvarande, i varje rum och "
     "på varje plats samtidigt.",
     None,
     "SO och SAOL ger bada 'overallt', och SO markerar uttryckligen "
     "**alderdomligt** -- kortet hade 'litterar', vilket ar en annan sak: "
     "litterart ar levande men skriftligt, alderdomligt ar pa vag ur bruket. "
     "Rattat. Wiktionary lagger till den upplysning som saknades helt: ordet "
     "lever i praktiken bara i frasen 'allestades narvarande'. Det star nu i "
     "huvudbetydelsen, for utan det ar kortet svarare att anvanda an att "
     "forsta. Synonymerna 'varhelst' och 'alla stallen' star i ingen kalla "
     "-- strukna.")

satt("attest",
     "Skriftligt intyg om något ; påskrift som godkänner att en räkning får "
     "betalas",
     "formell, neutral ; formell, neutral, ekonomi",
     ["intyg"],
     "Hon fick en " + B % "attest" + " från läkaren på att hon varit sjuk.",
     None,
     "🔴 TVA FEL. (1) SPRAKFEL I EXEMPLET: kortet skrev 'Han fick ETT attest' "
     "-- attest ar ett EN-ord (SAOL: attesten, attester). Ett kort som lar in "
     "fel genus ar samre an inget kort. Exempelmeningen ar omskriven. "
     "(2) SAKNAD BETYDELSE: SO ger 'skriftligt intyg', men SAOL ger ocksa "
     "'godkannande, paskrift' -- attestera en faktura ar den vanligaste "
     "anvandningen i svenskt arbetsliv och saknades helt. Tillagd. "
     "'bevis' och 'dokument' ar strukna: de star i ingen kalla och ar "
     "dessutom overordnade termer, inte synonymer.")

satt("förnuftsvidrig",
     "Som går rakt emot vad som är rimligt att tänka",
     "neutral, negativ",
     [],
     "Att skära ner på forskningen mitt under en pågående epidemi framstod "
     "som ett " + B % "förnuftsvidrigt" + " beslut.",
     None,
     "SO: '(hoggradigt) fornuftsstridig'. SAOL har inget eget "
     "definitionstext. SO satter INGEN bruklighetsmarkering, sa kortets "
     "'litterar' saknar belagg -- rattat till neutral enligt config.py:s "
     "regel att neutral ar det normala fallet och inte ett misslyckande. "
     "Synonymerna 'orimlig', 'ologisk' och 'irrationell' star i ingen kalla "
     "som SYN:synonym -- strukna. Huvudbetydelsen undviker medvetet "
     "'fornuft', eftersom en definition som innehaller uppslagsordets eget "
     "forled inte forklarar nagot.")

satt("gemytlig",
     "Vänlig och godmodig på ett sätt som gör alla omkring en avspända ; om "
     "en tillställning: trivsam och otvungen",
     "neutral, positiv ; neutral, positiv",
     ["godmodig", "småtrevlig"],
     "Det var en " + B % "gemytlig" + " stämning kring bordet hela kvällen.",
     None,
     "SO: 'som upptrader trevligt och vanligt och darigenom sprider en god "
     "stamning omkring sig', med 'av. om handling och dylikt'. SAOL: "
     "'godmodig, fryntlig, smatrevlig' -- godmodig och smatrevlig star i "
     "SAOL:s definitionstext och ar belagda. 'mysig' och 'trivsam' star i "
     "ingen kalla -- strukna. Registret 'vardaglig' saknade belagg (varken "
     "SO eller SAOL markerar det) och ar rattat till neutral. Betydelse tva "
     "(om tillstallning, inte person) fanns antydd men inte utskriven.")

satt("klosett",
     "Toalett med spolning",
     "neutral, neutral",
     ["toalett"],
     "Det gamla huset hade fortfarande utedass i stället för " + B % "klosett"
     + ".",
     "→ Engelska water closet, av closet 'kammare' — samma latinska rot "
     "(claudere 'stänga') som i kloster.",
     "SO: '(spolbar) anordning for utrattande av naturbehov'. SAOL: "
     "'toalett' -- SAOL:s hela definition och darmed belagd som synonym. "
     "'WC' ar struken: SO listar wc som JFR:cohyponym, alltsa ett "
     "sidoordnat begrepp, inte en synonym. 'avtrade' star i ingen kalla och "
     "ar dessutom motsatsen till en klosett (utedass utan spolning). "
     "Registret 'formell' var fel -- klosett ar inte byrakratsprak utan ett "
     "daterat vardagsord. Rattat till neutral. Etymologin ar med for att "
     "den forklarar varfor ordet ser ut som det gor.")

satt("medfaren",
     "Sliten och skadad av att ha hanterats ovarsamt — nästan alltid med "
     "\"illa\" framför",
     "neutral, lätt negativ",
     ["sliten"],
     "Väggen pryddes av en illa " + B % "medfaren" + " tapet full av rispor "
     "och fuktfläckar.",
     None,
     "SO: 'som visar spar av ovarsam anvandning', markerat SYN:synonym mot "
     "sliten -- sliten ar darmed belagd. SAOL: 'sliten, skadad'. 'harjad' "
     "och 'nott' star i ingen kalla -- strukna. Registret 'vardaglig' "
     "saknade belagg och ar rattat. Tillagt i huvudbetydelsen: ordet star "
     "nastan alltid efter 'illa' -- bade SO:s och kortets egen exempelmening "
     "gor det, men kortet sa det inte.")

satt("memento",
     "Varnande påminnelse — något som får en att tänka på vad som kan gå "
     "illa",
     "högtidlig, neutral",
     ["påminnelse", "varning"],
     "Hennes alltför tidiga död blev ett " + B % "memento" + " för dem alla.",
     "→ Latin memento 'kom ihåg!' — släkt med minne.",
     "🔴 EXEMPELMENINGEN ILLUSTRERADE FEL SAK. Kortet hade 'Det var ett "
     "memento fran hans farfar: \"Var alltid snall mot andra.\"' -- det ar "
     "ett gott rad, inte ett memento. SO sager 'VARNANDE paminnelse', och "
     "SO:s eget exempel ar 'hennes for tidiga dod var ett memento for dem "
     "alla'. Utan varningen ar ordet bara en synonym for paminnelse, vilket "
     "det inte ar. Exempel och huvudbetydelse omskrivna. SO markerar "
     "'nagot hogtidligt' -- kortet hade 'litterar'. Rattat. SAOL: "
     "'paminnelse, varning', bada belagda. 'erinring' star i ingen kalla.")

satt("odiös",
     "Så motbjudande att man känner avsky",
     "ngt ålderdomlig, negativ",
     ["förhatlig", "olidlig"],
     "Hans " + B % "odiösa" + " sätt att tala om kollegorna gjorde honom "
     "impopulär.",
     "→ Latin odium 'hat'.",
     "SO: 'forhatlig', markerat **mindre brukligt** -- kortet hade "
     "'litterar', vilket sager att ordet lever. Det gor det knappt. Rattat "
     "till ngt alderdomlig. SAOL: 'forhatlig, olidlig' -- bada belagda. "
     "'motbjudande' och 'avskyvard' kommer fran Wiktionary och star i "
     "varken SO eller SAOL som synonymer -- strukna (motbjudande anvands "
     "daremot i huvudbetydelsen, dar det ar en forklaring och inte ett "
     "paastaende om synonymi).")

satt("skärmytsling",
     "Kort och begränsad strid mellan små styrkor ; bildligt: kortare gräl "
     "eller ordväxling",
     "neutral, neutral ; neutral, neutral",
     [],
     "En " + B % "skärmytsling" + " mellan regeringen och oppositionen "
     "avslutade debatten.",
     None,
     "SAKNAD BETYDELSE, deckets dominerande fel. SO: 'mindre strid' med "
     "'av. bildligt', och SO:s eget exempel ar 'en skarmytsling mellan "
     "regeringen och oppositionen'. Kortet hade bara den militara "
     "betydelsen. Tillagd, och exempelmeningen bytt till den bildliga "
     "eftersom det ar den vanligaste i dagens text. Kortet pastod ocksa "
     "'ofta ovantad' -- det star i ingen kalla och ar struket. Registret "
     "'formell' saknade belagg. 'sammandrabbning' och 'mindre kamp' star i "
     "ingen kalla; 'mindre strid' ar SO:s definitionsord och skulle bli "
     "cirkulart.")

satt("vankelmod",
     "Oförmåga att bestämma sig, som gör andra oroliga",
     "neutral, negativ",
     [],
     "Regeringens " + B % "vankelmod" + " inför nedskärningarna oroade "
     "marknaden.",
     "→ Lågtyska wankel 'ostadig' och mod i den äldre betydelsen 'sinne'.",
     "SO: 'orosskapande obeslutsamhet' -- ordet **orosskapande** ar inte "
     "utsmyckning, det ar det som skiljer vankelmod fran vanlig tvekan, och "
     "kortet ('osakerhet och tveksamhet infor ett beslut') hade tappat det. "
     "Tillagt. SAOL: 'obeslutsamhet'. Synonymerna ar strukna: "
     "'obeslutsamhet' ar SAOL:s definitionsord och blir cirkulart, "
     "'beslutsangest' och 'tvekan' star i ingen kalla och 'beslutsangest' "
     "ar dessutom en kansla hos den som tvekar, medan vankelmod beskrivs "
     "utifran.")

satt("ymnig",
     "Som kommer i stora mängder, nästan mer än man behöver",
     "neutral, neutral",
     ["riklig"],
     "Det föll ett " + B % "ymnigt" + " snöfall över staden hela natten.",
     None,
     "SO: 'flodande riklig'. SAOL: 'riklig' -- SAOL:s hela definition och "
     "darmed belagd. 'flodande riklig' som synonym var SO:s definition "
     "avskriven ordagrant, vilket gor synonymraden till en upprepning av "
     "huvudbetydelsen; struken. 'overflodande' och 'yppig' star i ingen "
     "kalla -- strukna (yppig betyder dessutom nagot annat om kroppar). "
     "Registret 'litterar' saknade belagg i bada ordbockerna.")

satt("attribuera",
     "Peka ut vem som troligen skapat ett verk som saknar signatur",
     "fackspråklig, neutral",
     ["hänföra"],
     "Målningen har " + B % "attribuerats" + " till Rembrandt.",
     "→ Latin attribuere 'tilldela' — samma rot som attribut.",
     "SO: 'ange sasom troligen skapad av'. SAOL: 'hanfora ngt anonymt till "
     "ngn som upphovsman' -- hanfora star i SAOL:s definitionstext och ar "
     "belagd. tillskriva ar SO:s JFR:cohyponym och ar inte inskriven. "
     "ANDRING: domanen 'konst' ar borttagen. SO markerar inget "
     "amnesomrade, och enligt CLAUDE.md-regeln fran 2026-08-11 far en doman "
     "inte hittas pa ur exempelmeningen -- det var precis sa 'betuttad' "
     "blev psykologi. Att SO:s enda exempel rakar vara en malning racker "
     "inte.")

satt("deodorant",
     "Medel som tar bort eller döljer dålig lukt",
     "neutral, neutral",
     [],
     B % "Deodorant" + " finns bland annat som spray och roll-on.",
     "→ Latin de 'bort' och odor 'lukt' — samma rot som odör.",
     "SO: 'medel for avlagsnande eller undertryckande av obehaglig lukt'. "
     "Kortet snavade betydelsen till 'medel mot KROPPSLUKT' -- SO sager "
     "obehaglig lukt i allmanhet, och deodorant anvands aven om t.ex. "
     "rumsdeodorant. Vidgat till SO:s formulering. Synonymen 'deo' ar "
     "struken: den ar en verklig vardaglig kortform men star i varken SO "
     "eller SAOL, och synonymsparren (2026-08-12) kraver att ordboken sjalv "
     "sager det.")

satt("kofångare",
     "Stötfångare på bilens fram- eller baksida",
     "ngt ålderdomlig, neutral",
     ["stötfångare"],
     "Bilens " + B % "kofångare" + " låg krossad på vägbanan efter olyckan.",
     "→ Engelska cow-catcher, om plogen framför amerikanska ånglok som "
     "sköt undan boskap från spåret.",
     "SO: 'stotfangare', markerat **nagot alderdomligt** -- kortet hade "
     "'vardaglig'. Det ar inte samma sak: vardagligt ar levande talsprak, "
     "alderdomligt ar pa vag ut. Rattat. SAOL: 'framre el. bakre stotskydd "
     "pa bil'. stotfangare ar SO:s hela definition och darmed belagd. "
     "Etymologin ar tillagd for att den forklarar det annars obegripliga "
     "ordledet 'ko-' -- den kommer fran SO:s egen etymologirad "
     "(engelska cow-catcher).")

satt("betänkande",
     "Grundligt övervägande — ofta i \"utan betänkande\", alltså utan att "
     "tveka ; skriftlig rapport med resultatet av en utredning",
     "formell, neutral ; formell, neutral, politik",
     ["övervägande"],
     "Utredningens " + B % "betänkande" + " sänds nu ut på remiss.",
     None,
     "SO: '(grundligt) overvagande' och 'skriftlig redogorelse for "
     "resultatet av utredning'. (SO:s tredje post, 'overvaga grundligt', ar "
     "verbet BETANKA och hor till ett annat uppslagsord -- utelamnad.) "
     "SAOL bekraftar bada. Kortet skrev betydelse ett som 'tvekan innan "
     "beslut' -- det ar en omvandning: sjalva ordet betyder overvagandet, "
     "och tvekan kommer bara fran frasen 'utan betankande'. Omskrivet sa "
     "att bade ordet och frasen framgar. 'utlatande' ar struket (SO:s "
     "JFR:cohyponym); 'rapport' ar en overordnad term, inte en synonym.")

satt("entresol",
     "Låg mellanvåning inskjuten mellan två vanliga våningar",
     "neutral, neutral",
     ["halvvåning"],
     "Hotellet hade en " + B % "entresol" + " mellan första och andra "
     "våningen.",
     "→ Franska entre 'mellan' och sol 'golv'.",
     "SO: 'lag mellanvaning'. SAOL: 'lag mellanvaning, halvvaning' -- "
     "halvvaning star i SAOL:s definitionstext och ar belagd. 'mezzanin' ar "
     "struken: SO listar den som JFR:cohyponym, alltsa ett narliggande men "
     "skilt begrepp. Registret 'formell' saknade belagg i bada ordbockerna "
     "-- rattat till neutral.")

satt("isomorf",
     "Som har exakt samma form eller uppbyggnad som något annat",
     "fackspråklig, neutral",
     [],
     "De två kristallstrukturerna är " + B % "isomorfa" + " och har samma "
     "geometriska mönster.",
     "→ Grekiska isos 'lika' och morphe 'form'.",
     "SO: 'som har samma form eller struktur', med heteromorf markerat som "
     "MOTSATS:antonym. SAOL ger ingen egen definitionstext. Synonymen "
     "'likformig' ar struken: den star i ingen kalla, och likformig betyder "
     "dessutom nagot svagare -- isomorfi kraver strukturell identitet, inte "
     "bara likhet. Registret 'formell' var fel ordaxel (byrakratsprak) och "
     "ar bytt till fackspraklig.")

satt("polygami",
     "Äktenskap där en person är gift med flera samtidigt ; utvidgat: att "
     "leva med flera partner samtidigt",
     "neutral, neutral ; neutral, neutral",
     ["månggifte"],
     B % "Polygami" + " är lagligt i vissa länder.",
     None,
     "SO: 'aktenskapsform som innebar att en make/maka ar gift med fler an "
     "en person', markerat SYN:synonym mot manggifte, plus 'av. utvidgat om "
     "andra parforhallanden'. Den utvidgade betydelsen saknades i kortet "
     "och ar tillagd -- den ar den vanligaste i dagens text. 'flergifte' ar "
     "struket: star i ingen kalla. ⚠️ bigami och monogami ar SO:s "
     "JFR:cohyponym och ska INTE blandas ihop -- bigami ar specifikt tva.")

satt("resolut",
     "Kraftfull och bestämd i sitt handlande",
     "neutral, positiv, allmän",
     ["beslutsam", "rask"],
     "Hon tog " + B % "resolut" + " initiativet när de andra tvekade.",
     None,
     "SO: 'kraftfull och bestamd', med 'av. om handling eller dylikt'. "
     "SAOL: 'beslutsam, rask' -- bada synonymerna star i SAOL:s "
     "definitionstext och ar belagda. INGEN ANDRING behovdes: kortet stamde "
     "mot bada ordbockerna, registret var rimligt satt och exempelmeningen "
     "ar SO:s egen. Kortet gar igenom omgranskningen for att fa "
     "oberoende_verifierad, inte for att det var trasigt.")

satt("sörja",
     "Blöt, smutsig blandning av snö, lera och vatten ; känna sorg efter "
     "någon som dött ; sörja för: se till att något blir gjort",
     "vardaglig, neutral ; neutral, neutral ; formell, neutral",
     [],
     "Efter regnet var grusvägen en enda " + B % "sörja" + ".",
     None,
     "SAKNAD BETYDELSE. SO ger fem poster: 'smutsig blandning av vatska och "
     "smapartiklar', 'kanna stark sorg over', 'kanna sorg over forlusten "
     "av', 'vara ledsen eller dyster' och **'ta ansvar'** (sorja for). "
     "Kortet hade tva av dem och missade helt 'sorja for' -- den vanligaste "
     "anvandningen i skriven text vid sidan av sorgbetydelsen, och en HP "
     "provar garna just den. Tillagd. De tre sorgvarianterna ar slagna "
     "ihop till en, eftersom skillnaden mellan dem ar grad, inte betydelse. "
     "Synonymerna ar strukna: 'slask' och 'begrata' ar SO:s JFR:cohyponym, "
     "'modd' star i ingen kalla, och 'grata' ar sakligt fel -- man kan "
     "sorja utan att grata.",
     tillat={"betydelse_kan_saknas":
             "SO:s fem poster ar tre linjer: sorjan (substantivet), sorgen "
             "(tre gradskillnader av samma sak) och sorja for. Kortet ger "
             "alla tre."})

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Skrev %d kort." % sum(1 for k in KORT if k.get("approved")))
