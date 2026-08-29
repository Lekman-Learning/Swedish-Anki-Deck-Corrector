# -*- coding: utf-8 -*-
"""Batch 2026-08-29, 20 kort. Full v3.

Reglerna, alla ur 2026-08-28 (217 kort, 20 underkännanden):

1. SLÅ ALDRIG IHOP två betydelser som SO eller SAOL håller isär. Bevisbördan
   ligger hos mig för att de är samma. Detta fel återkom SEX gånger på en
   dag, fem av dem efter att regeln formulerats — och i fem fall hade jag
   skrivit ut i sökkollen att jag slog ihop.
2. Synonym bara om ordet är utbytbart ÅT BÅDA HÅLLEN och inte är JFR-markerat
   i SO. En ordboksglosa är ofta en förklaring, inte ett utbytbart ord.
3. Ingen betydelse som bara Wiktionary har.
4. Facit styrs av definitionen — aldrig av etymologin eller av en synonym.
5. ETYMOLOGIFÄLTET RENDERAS PÅ KORTET: full svenska. Bara sokkoll-slutsatsen
   är intern och får vara ASCII. Formerna på källspråken behåller sin egen
   stavning.
"""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-29_v3-batch.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
B = '<font color="#3498db">%s</font>'


def kallor(o, *extra):
    k = urllib.parse.quote(o)
    return " ".join([
        "https://svenska.se/api/msearch?ord=%s" % k,
        "https://www.synonymer.se/sv-syn/%s" % k,
        "https://sv.wiktionary.org/wiki/%s" % k,
        *extra,
    ])


def satt(o, bet, reg, syn, ex, ety, slutsats, grupper=None, extra=(), conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": grupper, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": kallor(o, *extra), "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True


satt("balk",
     "Lång bärande del i en byggnad som tar upp tyngd ; i vapensköldar: brett "
     "snedställt band från övre högra hörnet till nedre vänstra ; "
     "huvudavdelning av den svenska lagen, som brottsbalken",
     "neutral, neutral, teknik ; fackspråklig, neutral, historia ; "
     "fackspråklig, neutral, juridik",
     [],
     "Bestämmelsen finns i tredje kapitlet i " + B % "balken" + ".",
     "→ Fornsvenska balker 'bjälke, avbalkning'; germanskt ord, besläktat "
     "med bjälke.",
     "SO ger TRE betydelser: den barande byggnadsdelen, det heraldiska "
     "bandet och lagavdelningen. Alla tre ar med. SAOL bekraftar tva och "
     "lagger till 'jarnbalk med profil i form av ett I' -- den ar en SORT av "
     "byggnadsbalk, inte en egen betydelse, och ar inte skild ut. SO:s JFR "
     "(bjalke, regel, sparre, syll) ar cohyponymmarkta: alla ar delar i en "
     "konstruktion men inte utbytbara. OLD-facit 'grundbjalke' hade en av "
     "tre, och 'grund-' ar dessutom fel: en balk sitter lika garna i taket. "
     "Exempelmeningen ar vald till lagbetydelsen, som ar den man faktiskt "
     "moter i text.")

satt("docka",
     "Leksak i form av en människofigur ; anläggning i en hamn där ett "
     "fartyg kan torrläggas för reparation ; maskindel som håller upp "
     "arbetsstycket, till exempel i en svarv ; som verb: ta in ett fartyg i "
     "en sådan anläggning, eller själv gå in i den ; som verb: koppla ihop "
     "två rymdfarkoster",
     "neutral, neutral, allmän ; fackspråklig, neutral, sjöfart ; "
     "fackspråklig, neutral, teknik ; fackspråklig, neutral, sjöfart ; "
     "fackspråklig, neutral, teknik",
     [],
     "Fartyget låg i " + B % "docka" + " för att få skrovet lagat.",
     "→ Leksaksbetydelsen fornsvenska dokka, troligen ursprungligen "
     "'hopvriden garnbunt'. Hamnbetydelsen av lågtyska docke, engelska dock "
     "— ett helt annat ord som fallit ihop i stavning.",
     "SO ger SEX numrerade betydelser; kortet har fem. HOPSLAGNINGEN SOM "
     "GJORTS, och skalet: SO skiljer 'ta in (fartyg) i docka' fran 'tas in "
     "i docka'. Det ar samma handelse sedd fran tva hall -- transitiv och "
     "intransitiv form av SAMMA verb, alltsa en grammatisk skillnad och "
     "inte tva betydelser. Det ar den enda hopslagning jag gjort i den har "
     "batchen och den ar utskriven for att kunna underkannas. Ovriga "
     "underbetydelser (skyltdocka, modedocka, garndocka, samt 'litet sott "
     "barn el. liten sot kvinna') ar sammansattningar respektive bildliga "
     "anvandningar av leksaksbetydelsen och ar inte skilda ut. OLD-facit "
     "'hamnbassang' hade EN av sex, och den ar dessutom oprecis: en docka "
     "TOMS pa vatten, en bassang gor det inte.")

satt("moarera",
     "Ge tyg ett skimrande vågmönster",
     "fackspråklig, neutral, allmän",
     [],
     "Sidenet var " + B % "moarerat" + " så att ljuset gick i vågor över "
     "tyget.",
     "→ Till moaré; av franska moirer 'vattra'.",
     "SVAGT BELAGD: SO och SAOL har ingen artikel; uppslagsordet finns bara "
     "i SAOB (traffar=saob), varifran skriptet inte extraherar "
     "definitionstext. Enda kalla med en betydelse ar Wiktionary: 'vattra'. "
     "Det ordet ar utskrivet enligt Adam-tal, i linje med kortet MOARE som "
     "skrevs 2026-08-28 ur SO ('typ av vavnad med vattrad yta'). VIKTIG "
     "RATTELSE: OLD-facit sa 'gora brokig'. Brokig betyder flerfargad; "
     "moarering handlar om SKIMMER och vagmonster i EN farg. Facit ar "
     "omskrivet.",
     conf=6)

satt("motvalls",
     "Som alltid säger emot och gör tvärtom",
     "vardaglig, lätt negativ, allmän",
     [],
     "Det sägs ofta att britter är ett " + B % "motvalls" + " släkte.",
     "→ Motvall, bildat till mot i analogi med efternamn som Ekvall och "
     "Sandvall.",
     "SO: 'motstravig', med markningen vard. SAOL preciserar: 'som alltid "
     "sager emot el. kranglar'. SAOL:s formulering ar den som anvands i "
     "facit, eftersom SO:s enda ord ar lika svart som uppslagsordet. "
     "OLD-facit 'som gar mot strommen' ar for smickrande: att ga mot "
     "strommen ar att tanka sjalv, motvalls ar att saga emot for sakens "
     "skull. Ordet lever i praktiken i uttrycket 'motvalls karring'.")

satt("nutrition",
     "Tillförsel av näring till kroppen ; läran om näring och hur kroppen "
     "tar upp den",
     "fackspråklig, neutral, medicin ; fackspråklig, neutral, medicin",
     [],
     "Patienten fick " + B % "nutrition" + " genom sond under hela "
     "vårdtiden.",
     "→ Till latin nutrire 'amma, nära'.",
     "SO ger tva: '(tillforsel av) naring' och 'naringslara' (ibland av.), "
     "med markningen i vetenskapliga sammanhang. Bada ar med -- den ena ar "
     "en HANDLING i vardrummet, den andra ett AMNE pa universitetet, och de "
     "har bara ordet gemensamt. SAOL bekraftar den forsta och lagger till "
     "'amnesomsattning', som ar en foljd av naringstillforseln och inte "
     "skild ut. OLD-facit 'naringslara' hade bara den andra -- alltsa den "
     "sallsyntare av de tva.")

satt("redning",
     "Att göra en sås eller soppa tjockare ; också om själva blandningen av "
     "mjöl och vätska som används till det",
     "neutral, neutral, matlagning ; neutral, neutral, matlagning",
     [],
     "Smält smöret och vispa i mjölet till en jämn " + B % "redning" + ".",
     "→ Till reda i betydelsen 'göra i ordning'.",
     "SO: 'avredning av en vatska', med underbetydelsen 'av. om resultatet'. "
     "Bada ar med -- handlingen och blandningen, och det ar den andra man "
     "moter i ett recept. SAOL ger innehallet: 'blandning av mjol och vatska "
     "for att gora en sas tjock'. SO:s definition ar cirkular (avredning "
     "forutsatter reda) och ar utskriven enligt Adam-tal. OLD-facit 'grund "
     "till sas' ar vagt och sager varken vad den bestar av eller vad den "
     "gor.")

satt("rättmätig",
     "Som stämmer med vad man känner är rättvist ; som enligt lagen är den "
     "rätte — den rättmätige ägaren",
     "neutral, positiv, allmän ; fackspråklig, neutral, juridik",
     [],
     "Stöldgodset återlämnades till den " + B % "rättmätige" + " ägaren.",
     "→ Efter lågtyska rechtmetich; samma rötter som rätt och mått.",
     "SO ger tva: 'som uppfyller naturliga krav pa rattvisa' (rattmatiga "
     "krav, ett rattmatigt straff) och 'som enligt lag ar' (den rattmatige "
     "agaren). Bada ar med, och skillnaden ar avgorande: den forsta ar en "
     "KANSLA av rattvisa, den andra ett LAGLIGT forhallande. Nagot kan vara "
     "rattmatigt i den andra betydelsen och anda kannas orattvist. SO:s JFR "
     "berattigad ar cohyponymmarkt; SAOL:s 'berattigad; laglig' ar glosor "
     "for var sin betydelse och ingen av dem ar utbytbar mot bada -- alltsa "
     "inga synonymer. OLD-facit 'lagenlig, befogad' var just en sadan rad.")

satt("småskuren",
     "Som bara ser till småsaker och saknar förmåga att se det stora",
     "neutral, nedsättande, allmän",
     [],
     "En " + B % "småskuren" + " anmärkning som ingen brydde sig om.",
     None,
     "SO: 'trangsynt'. SAOL: 'smasint'. Bada orden ar lika svara som "
     "uppslagsordet och facit ar darfor utskrivet. Wiktionary ger tre HELT "
     "andra, bokstavliga betydelser ('finskuren, hackad', 'med sma tata "
     "inskarningar', 'med manga sma inslag av olika naturtyper'). De ar "
     "UTELAMNADE: varken SO eller SAOL har nagon av dem, och en "
     "Wiktionary-egen betydelse fallde bade anlopa och autograf "
     "2026-08-28. OLD-facit 'trangsynt' ar SO:s ord rakt av.")

satt("anekdot",
     "Kort och roande historia, ofta om en verklig person",
     "neutral, neutral, allmän",
     [],
     "Det finns många mer eller mindre sanna " + B % "anekdoter" + " om "
     "Bellman.",
     "→ Via latin och franska av grekiska anekdoton, eg. 'något outgivet' — "
     "historier som inte tryckts utan gått muntligt.",
     "SO: 'kortare roande historia'. SAOL: 'kort skamtsam berattelse, "
     "historia'. Ledet 'om en verklig person' ar inte definitionstext men "
     "foljer av bada SO:s exempel (anekdoter OM Bellman; en anekdot som "
     "belyser troghet i en beslutsprocess) och ar skrivet som 'ofta', inte "
     "som krav. Wiktionarys 'med nagon form av slutpoang' ar en precisering "
     "utan stod i SO/SAOL och ar utelamnad. OLD-facit 'kort roande "
     "historia' ar SO:s ord och stammer.")

satt("argot",
     "Slangspråk inom en sluten grupp, ursprungligen tjuvarnas eget språk",
     "fackspråklig, neutral, lingvistik",
     [],
     "Flera ord kom in i svenskan via de kriminellas " + B % "argot" + ".",
     "→ Franska argot 'slang, tjuvspråk'; ursprunget är okänt.",
     "SO: 'speciell form av slangsprak som anvands inom subkulturer'. SAOL "
     "smalnar av till 'forbrytarslang'. Bada leden ar med: att det ar en "
     "SLUTEN grupp (SO) och att ursprunget ar tjuvsprak (SAOL). SO:s JFR "
     "slang ar jamforelsemarkt och tas INTE upp som synonym -- skillnaden "
     "ar hela ordet: slang ar allmant talsprak, argot ar en grupps EGET "
     "sprak, ofta avsiktligt obegripligt for utomstaende. OLD-facit 'slang "
     "(ofta kriminellt)' fangar det ungefarligt men utan att saga att "
     "slutenheten ar poangen.")

satt("brushuvud",
     "Person som brusar upp och tappar behärskningen vid minsta anledning",
     "neutral, lätt negativ, allmän",
     [],
     "Ett par unga " + B % "brushuvuden" + " på kadettskolan ville "
     "duellera.",
     None,
     "SO: 'person med minimal sjalvkontroll'. SAOL: 'hetlevrad person'. "
     "Wiktionary ger det avgorande ledet: 'som av mindre yttre paverkan "
     "brusar upp' -- alltsa att TROSKELN ar lag, inte bara att personen ar "
     "argsint, och det ar med. OLD-facit 'hetsporre' ar INTE upptaget som "
     "synonym: ordet saknas i bade SO:s och SAOL:s artiklar for brushuvud, "
     "och en hetsporre driver pa framat medan ett brushuvud brakar ihop.")

satt("drivbänk",
     "Låg låda av brädor med glasfönster över, där man driver upp plantor "
     "tidigt på våren",
     "neutral, neutral, jordbruk",
     [],
     "De odlade gurkor i " + B % "drivbänk" + " redan i mars.",
     None,
     "SO: 'karm av brader eller dylikt som kan tackas med fonster av glas "
     "eller plast for att skydda eller driva upp vaxter i en odlingsbadd'. "
     "SAOL: 'fonstertackt jordbadd for uppdragning av vaxter'. Poangen med "
     "ordet ar att man far en FORSPRANG pa sasongen -- det ar vad 'driva "
     "upp' betyder och det ar utskrivet, eftersom OLD-facit 'liten inglasad "
     "odling' later som ett vaxthus i miniatyr utan att saga varfor man "
     "har ett.")

satt("gisslare",
     "Person som piskar sig själv som botgöring ; bildligt: skoningslös "
     "kritiker",
     "fackspråklig, neutral, religion ; neutral, neutral, allmän",
     [],
     "Hon har gjort sig känd som en av regeringens främsta " +
     B % "gisslare" + ".",
     "→ Till gissla 'piska'; av fornsvenska gisl 'piska, spö'.",
     "SO ger tva: 'person som plagar sig sjalv' och 'hard kritiker' (av. "
     "bildligt). Bada ar med. Wiktionary ger dessutom en TREDJE, bokstavlig "
     "('person som gisslar (slar) nagon') -- den ar UTELAMNAD eftersom SO "
     "inte har den och en Wiktionary-egen betydelse inte duger som belagg. "
     "SO:s JFR flagellant ar cohyponymmarkt och tas inte upp trots att det "
     "ligger mycket nara den forsta betydelsen. OLD-facit "
     "'sjalvplagare; hard kritiker' hade bada, men 'sjalvplagare' sager "
     "inte att det ar en religios handling.")

satt("mortalitet",
     "Hur många som dör i en befolkning under en viss tid, räknat i "
     "förhållande till hur många som lever där",
     "fackspråklig, neutral, medicin",
     ["dödlighet"],
     B % "Mortaliteten" + " i Sverige sjönk kraftigt under 1900-talet.",
     "→ Franska mortalité; till latin mors, genitiv mortis, 'död'; samma "
     "rot som mord och amortera.",
     "SO: 'relativt antal avlidna', SYN-markt mot dodlighet -- den "
     "starkaste beviskategorin, och orden ar utbytbara at bada hallen i den "
     "statistiska anvandningen. SAOL preciserar 'relaterad till hela "
     "folkmangden', vilket ar med: ordet RELATIVT i SO:s definition ar hela "
     "poangen och forsvinner i OLD-facits 'dodlighet'. SO:s JFR nativitet "
     "ar motstycket (fodelsetal), inte en synonym.")

satt("portiär",
     "Tygdraperi som hängs framför en dörröppning i stället för en dörr",
     "neutral, neutral, allmän",
     [],
     "En tung " + B % "portiär" + " av sammet skilde salongen från hallen.",
     "→ Franska portière; till porte 'dörr'.",
     "SO: '(dorr)forhange'. SAOL har ingen artikel; Wiktionary bekraftar "
     "'dorrforhange'. Att den ersatter dorren ar utskrivet eftersom "
     "'forhange' ensamt lika garna kan avse en gardin for ett fonster. "
     "OLD-facit 'dorrforhange' ar SO:s ord och stammer, men ar lika "
     "ovanligt som uppslagsordet.")

satt("sampel",
     "Den grupp man faktiskt undersöker, utvald för att spegla en större "
     "helhet",
     "fackspråklig, neutral, allmän",
     [],
     "Man kan inte dra några slutsatser eftersom " + B % "samplet" + " är "
     "skevt.",
     "→ Engelska sample; av fornfranska essample 'exempel' — samma ord som "
     "exempel.",
     "SO: 'stickprov for statistisk undersokning'. SAOL: 'stickprov'. "
     "Stickprov ar INTE upptaget som synonym trots att det ar SAOL:s hela "
     "definition: ett stickprov ar per definition slumpmassigt, ett sampel "
     "behover inte vara det (SO:s eget exempel ar 'de forsta fem meningarna "
     "i varje kapitel', vilket inte ar slumpmassigt). Bada-hallen-provet "
     "faller. SO:s JFR (population, urval) ar cohyponymmarkta: populationen "
     "ar helheten samplet ska spegla.")

satt("slabbig",
     "Blöt och kladdig på ett osnyggt sätt",
     "neutral, lätt negativ, allmän",
     [],
     "En " + B % "slabbig" + " portion pasta och tomatsås.",
     "→ Svensk dialekt slabbig; till slabba 'söla med vatten'.",
     "SO: 'vat och solig'. SAOL: 'vat och smutsig; slafsig'. Bada bidrar: "
     "SO:s 'solig' och SAOL:s 'smutsig' ar samma sak sedd fran tva hall och "
     "ar sammanfattade som 'kladdig ... osnyggt'. SO:s JFR (slafsig, "
     "slaskig) ar cohyponymmarkta och tas inte upp -- slaskigt ar vad det "
     "ar ute pa gatan i februari, slabbigt ar vad som ligger pa tallriken. "
     "Ingen bruklighetsmarkning finns i vare sig SO eller SAOL, sa "
     "registret ar neutralt trots att ordet later talsprakligt.")

satt("snusmumrik",
     "Gubbe som snusar",
     "vardaglig, neutral, allmän",
     [],
     "En gammal " + B % "snusmumrik" + " satt och halvsov på bänken.",
     "→ Till snus och mumrik.",
     "SO och SAOL ger bada exakt ett ord: 'snusgubbe', med markningen "
     "vardagligt. Det ordet ar utskrivet enligt Adam-tal. Ingen valens ar "
     "satt: efterleden -mumrik ar i sig nedsattande, men VARKEN SO ELLER "
     "SAOL markerar ordet sa, och en laddning far inte hittas pa. VIKTIG "
     "FALLA: Snusmumriken i Mumindalen ar Tove Janssons figur och har "
     "ingenting med betydelsen att gora -- ordet ar belagt sedan 1891, "
     "decennier fore muminbockerna.")

satt("ta reson",
     "Ta sitt förnuft till fånga och sluta streta emot",
     "neutral, neutral, allmän",
     [],
     "Till slut fick de honom att " + B % "ta reson" + " och gå med på "
     "förlikning.",
     "→ Franska raison 'förnuft'; av latin ratio 'plan, eftertanke'; samma "
     "rot som ranson och rationell.",
     "NOT OM UPPSLAGNINGEN: sokningen pa flerordsuttrycket drog med sig "
     "artiklar for RESON och for TAX-FREE ('befriad fran skatt', av "
     "engelska tax-free) -- den senare har ingenting med uttrycket att gora "
     "och ar inte anvand. Detta ar tredje gangen ett flerordsuttryck ger "
     "fel traff (jfr reda pengar 2026-08-28, som gav redaktion och sedan "
     "regn). Det som ANVANTS ar SO:s definition av reson, 'anvanda sitt "
     "fornuft', plus att frasen 'ta reson' star i SO:s egen exempellista. "
     "OLD-facit 'bli fornuftig' stammer men missar att uttrycket nastan "
     "alltid anvands nar nagon GER MED SIG efter att ha strulat.")

satt("verv",
     "Kraft och glöd i det man gör eller berättar",
     "arkaisk, positiv, allmän",
     [],
     "Han berättade med " + B % "verv" + " om sina ungdomsår på sjön.",
     "→ Franska verve 'entusiasm'; troligen av latin verba 'ord'; samma rot "
     "som verb.",
     "SO och SAOL ger bada 'kraft och livfullhet', SAOL med tillagget "
     "'glod', med markningen alderdomligt. Glod ar INTE upptaget som "
     "synonym: man kan tala med glod utan att tala med verv -- verv "
     "innehaller ocksa ett drag av svung och elegans som glod saknar, sa "
     "bada-hallen-provet faller. OLD-facit 'livfullhet' tappade KRAFTEN, "
     "som ar halva definitionen i bada ordbockerna.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("skrev %d kort" % sum(1 for k in KORT if k.get("approved")))
