# -*- coding: utf-8 -*-
"""Arbetsbatch 2026-09-02c, kort 34-66.

NY REGEL, ur blindgranskningens andra omgang (9 underkanda av 50): en
INNEHALLSBARANDE underbetydelse raknas som en betydelse. `vakuum`,
`psykos` och `erovring` foll alla pa att SO:s "av. bildligt" utelamnats --
granskaren kallade den bildliga anvandningen "mycket vanlig" och krav den
som egen rad. Min generella motivering om att underbetydelser inte ar
betydelser holl alltsa inte, och den ska inte upprepas.

Gransen gar vid INNEHALL, inte vid rubrik: "av. bildligt" med exempel ar
en betydelse, bara "av." eller "spec." ar det inte. Och en betydelse som
bara finns i en FAST FRAS ar fortfarande ingen betydelse hos ordet -- det
var vad `koloss` och `profetia` foll pa i samma omgang.
"""
import io, json, sys
import _hjalp_0902b as HJ

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02c_v3-batch.json"
H = HJ.H

K = {
 "plektrum": (
  "Liten tunn skiva som man knäpper strängarna med",
  "neutral, neutral, musik", ["liten skiva som strängarna på vissa stränginstrument slås an med"],
  [["liten skiva som strängarna på vissa stränginstrument slås an med"]],
  "Gitarristen tappade sitt %s mitt i solot men fortsatte spela med fingrarna." % (H % "plektrum"),
  "En betydelse. Synonymraden var tom och är fylld ur poolen."),

 "prestanda": (
  "Hur mycket något klarar av att prestera",
  "neutral, neutral", ["prestationsförmåga", "prestationer"],
  [["prestationsförmåga", "prestationer"]],
  "Bilens %s imponerade på testförarna." % (H % "prestanda"),
  "SO:s andra post, 'åligganden', är den ursprungliga latinska betydelsen "
  "(det som bör fullgöras) och används inte i modern svenska; den är "
  "utelämnad. Etymologin visar varifrån den kommer."),

 "prisma": (
  "Genomskinlig kropp med raka sidor som bryter ljuset",
  "fackspråklig, neutral, fysik", ["ljusbrytande kropp av denna form"],
  [["ljusbrytande kropp av denna form"]],
  "Spektroskopet använde ett %s för att dela upp ljuset." % (H % "prisma"),
  "En betydelse. Synonymraden var tom och är fylld ur poolen. SO:s "
  "grundbetydelse är den rent geometriska kroppen; kortet leder med den "
  "optiska, som är den Adam möter."),

 "promotion": (
  "Högtidlig ceremoni där doktorsbevis delas ut ; åtgärder för att få en vara såld",
  "formell, neutral ; fackspråklig, neutral, ekonomi",
  ["högtidlig ceremoni varvid bevis på doktorsvärdighet delas ut", "≈≈ säljfrämjande"],
  [["högtidlig ceremoni varvid bevis på doktorsvärdighet delas ut"], ["≈≈ säljfrämjande"]],
  "%s i universitetets aula samlade årets alla nya doktorer." % (H % "Promotionen"),
  "Kortet hade båda betydelserna men fem synonymer i EN grupp, varav bara "
  "en har belägg. Grupperna är nu delade per betydelse."),

 "saldo": (
  "Det som finns kvar på ett konto när allt räknats ihop",
  "neutral, neutral, ekonomi", ["skillnad mellan debet och kredit"],
  [["skillnad mellan debet och kredit"]],
  "Efter lönen kom in hade han äntligen ett positivt %s på kontot." % (H % "saldo"),
  "En betydelse. Synonymraden var tom och är fylld ur poolen."),

 "sexualitet": (
  "Allt som har med kroppens lust och samliv att göra",
  "neutral, neutral", ["≈≈ könsdrift"], [["≈≈ könsdrift"]],
  "Skolan fick en öppnare syn på %s under 1970-talet." % (H % "sexualitet"),
  "En betydelse. Synonymraden var tom; poolen ger bara SO:s definition "
  "ordagrant, så kategorin används."),

 "absorbera": (
  "Suga upp något ; ta in och förstå ; helt uppta någons intresse",
  "neutral, neutral, kemi ; neutral, neutral ; neutral, neutral",
  ["suga upp", "förstå och tillgodogöra sig", "lägga beslag på intresse el. krafter"],
  [["suga upp"], ["förstå och tillgodogöra sig"], ["lägga beslag på intresse el. krafter"]],
  "Växternas rötter kan %s näringsämnen från jorden." % (H % "absorbera"),
  "RÄTTAT: kortet hade två av SO:s tre betydelser. Den som saknades är "
  "'förstå och tillgodogöra sig' -- att absorbera kunskap -- och den är "
  "vanlig i studiesammanhang."),

 "amfibie": (
  "Djur som lever både på land och i vatten ; farkost som går både på land och i vatten",
  "neutral, neutral, biologi ; neutral, neutral, teknik",
  ["ett groddjur", "farkost som kan framföras både till lands och till sjöss"],
  [["ett groddjur"], ["farkost som kan framföras både till lands och till sjöss"]],
  "Jättesalamandern är en av världens största %s." % (H % "amfibier"),
  "Kortet hade båda betydelserna. Andra gruppen stod utan synonym och har "
  "fått poolens egen."),

 "anstucken": (
  "Till hälften övertygad om en tvivelaktig lära",
  "ngt ålderdomlig, lätt negativ", ["påverkad av ett (tvivelaktigt) tänkesätt"],
  [["påverkad av ett (tvivelaktigt) tänkesätt"]],
  "Var den gamle finansmannen nazistiskt %s?" % (H % "anstucken"),
  "En betydelse. 'påverkad' ensamt saknar belägg och är för brett -- ordet "
  "bär alltid att det man påverkats av är tvivelaktigt. Etymologin "
  "förklarar bilden: ansticka betydde 'smitta'."),

 "astronomisk": (
  "Som hör till astronomin ; ofattbart stor",
  "fackspråklig, neutral, fysik ; vardaglig, neutral",
  ["≈≈ stjärnkunnig", "mycket stor"], [["≈≈ stjärnkunnig"], ["mycket stor"]],
  "Priserna på bostäder i innerstaden hade nått %s nivåer." % (H % "astronomiska"),
  "Kortet hade båda betydelserna men stod utan synonymer. Den andra "
  "betydelsen -- den bildliga om ofattbart stora tal -- är den Adam möter "
  "oftast och den enda som dyker upp utanför fackspråk."),

 "atrofi": (
  "Att en kroppsdel tynar bort och krymper av att inte användas",
  "fackspråklig, neutral, medicin", ["förtvining"], [["förtvining"]],
  "Efter tre månader i gips syntes tydlig %s i vadmuskeln." % (H % "atrofi"),
  "En betydelse. 'förtvining' är SO:s egen. Huvudbetydelsen säger nu VARFÖR "
  "-- av att inte användas -- vilket är det som gör ordet begripligt."),

 "avträda": (
  "Lämna ifrån sig sina rättigheter till något ; gå sin väg från ett rum",
  "formell, neutral, juridik ; ngt ålderdomlig, neutral",
  ["lämna ifrån sig", "avlägsna sig (gående)"],
  [["lämna ifrån sig"], ["avlägsna sig (gående)"]],
  "Sverige fick %s sina baltiska besittningar 1721." % (H % "avträda"),
  "Kortet hade båda betydelserna. Första gruppen stod utan synonym."),

 "banal": (
  "Så vanlig och uttjatad att den inte säger något",
  "neutral, negativ", ["alldaglig", "sliten", "platt"],
  [["alldaglig", "sliten", "platt"]],
  "Han tyckte manuset var %s och fullt av utslitna klyschor." % (H % "banalt"),
  "En betydelse. Alla tre synonymerna finns i poolen. Etymologin är värd "
  "att ha: franskans banal betydde ursprungligen 'påbjuden till allmänt "
  "bruk' -- alltså gemensam, därav vanlig, därav intetsägande."),

 "belysning": (
  "Ljus från lampor i stället för från dagen ; det att göra ett sammanhang tydligt ; själva lamporna",
  "neutral, neutral ; formell, neutral ; vardaglig, neutral",
  ["ljusförhållanden", "åskådligt klarläggande", "≈≈ armatur"],
  [["ljusförhållanden"], ["åskådligt klarläggande"], ["≈≈ armatur"]],
  "Den svaga %s i källaren gjorde det svårt att läsa." % (H % "belysningen"),
  "Kortet hade två betydelser. SO:s underbetydelse 'äv. konkret om lampor "
  "och dylikt' bär eget innehåll -- det är ju den man köper i butiken -- "
  "och är tillagd som tredje."),

 "blackout": (
  "Kortvarig medvetslöshet ; att omdömet plötsligt slås ut",
  "vardaglig, neutral ; vardaglig, neutral",
  ["kort medvetslöshet", "plötslig förlust av omdömesförmågan"],
  [["kort medvetslöshet"], ["plötslig förlust av omdömesförmågan"]],
  "Piloten tros ha drabbats av en %s vid spakarna." % (H % "blackout"),
  "Kortet hade två betydelser men den andra var formulerad som 'minneslucka, "
  "ofta i samband med alkohol'. SO:s andra betydelse är bredare: det är "
  "OMDÖMET som slås ut, inte bara minnet. 'svimning' saknar belägg."),

 "demobilisera": (
  "Ta en armé ur beredskap och skicka hem soldaterna",
  "formell, neutral, militär", ["hemförlova soldater"], [["hemförlova soldater"]],
  "Kåren skulle transporteras hem och %s efter kriget." % (H % "demobiliseras"),
  "En betydelse. 'avmobilisera' saknar ordboksbelägg och förklarar dessutom "
  "ordet med nästan samma ord. Poolens 'hemförlova soldater' säger vad som "
  "faktiskt händer."),

 "deportera": (
  "Tvinga bort någon till en avlägsen plats",
  "formell, negativ, juridik", ["förvisa till avlägsen plats"],
  [["förvisa till avlägsen plats"]],
  "På 1800-talet %s England förbrytare till Australien." % (H % "deporterade"),
  "En betydelse. 'förvisa' ensamt saknar belägg. Valören satt till negativ "
  "-- deportation är ett tvångsmedel, och ordet bär den laddningen."),

 "diskotek": (
  "Lokal där man dansar till inspelad musik ; en samling grammofonskivor",
  "ngt ålderdomlig, neutral ; ngt ålderdomlig, neutral",
  ["danslokal med inspelad musik", "skivsamling"],
  [["danslokal med inspelad musik"], ["skivsamling"]],
  "Ungdomarna gick på %s varje fredag för att dansa till sent på natten." % (H % "diskotek"),
  "Kortet hade båda betydelserna. 'danslokal' ensamt saknar belägg och är "
  "bytt mot poolens fullständiga form. Etymologin förklarar den andra "
  "betydelsen: -tek betyder förvaringsrum, som i bibliotek."),

 "donera": (
  "Ge bort något större till ett gott ändamål",
  "neutral, neutral", ["skänka", "ge till allmännyttigt ändamål"],
  [["skänka", "ge till allmännyttigt ändamål"]],
  "Hon %s hela sin porslinssamling till museet." % (H % "donerade"),
  "En betydelse. Båda synonymerna finns i poolen."),

 "eminens": (
  "Titel för en katolsk kardinal ; person som styr i det tysta utan att synas",
  "formell, neutral, religion ; litterär, neutral",
  ["kardinal", "≈≈ maktspelare"], [["kardinal"], ["≈≈ maktspelare"]],
  "Ers %s mottog delegationen i audiensen." % (H % "eminens"),
  "RÄTTAT: kortet ledde med 'upphöjdhet, förnämlighet' -- en betydelse SO "
  "inte har. SO ger två: titeln för kardinal, och den skenbart "
  "betydelselösa men inflytelserika personen (den grå eminensen). "
  "'förnämlighet' och 'högvördighet' saknar båda belägg."),

 "eruption": (
  "Utbrott där material sprutar ut ur jordens inre ; häftigt utbrott av känslor",
  "fackspråklig, neutral, geologi ; litterär, neutral",
  ["vulkaniskt utbrott", "≈≈ känsloutbrott"],
  [["vulkaniskt utbrott"], ["≈≈ känsloutbrott"]],
  "En serie våldsamma %s skakade marken runt vulkanen." % (H % "eruptioner"),
  "SO:s underbetydelse 'äv. bildligt om utbrott av andligt slag (vanligen "
  "av vrede men äv. av skaparkraft)' bär eget innehåll och är tillagd som "
  "egen betydelse. 'utbrott' ensamt saknar belägg."),

 "essentiell": (
  "Så viktig att det inte går utan ; livsnödvändig för kroppen",
  "formell, neutral ; fackspråklig, neutral, medicin",
  ["väsentlig", "livsviktig"], [["väsentlig"], ["livsviktig"]],
  "De ställdes inför %s frågor om liv och död." % (H % "essentiella"),
  "SO har två betydelser. Den andra är den medicinska -- essentiella "
  "aminosyror och fettsyror, alltså sådana kroppen inte kan bilda själv. "
  "Kortet slog ihop dem; nu står de var för sig."),

 "eufori": (
  "Stark känsla av lycka och upprymdhet",
  "formell, positiv", ["lyckokänsla", "förhöjt stämningsläge"],
  [["lyckokänsla", "förhöjt stämningsläge"]],
  "Löparna kände total %s när de äntligen korsade mållinjen." % (H % "eufori"),
  "En betydelse. 'upprymdhet' saknar belägg som fristående synonym och är "
  "bytt mot poolens 'förhöjt stämningsläge'."),

 "evident": (
  "Så tydlig att den inte går att ifrågasätta",
  "formell, neutral", ["uppenbar", "obestridlig"], [["uppenbar", "obestridlig"]],
  "Han skriver så snårigt att budskapet inte är omedelbart %s." % (H % "evident"),
  "En betydelse. Båda synonymerna finns i poolen. Kortet var redan korrekt."),

 "evolution": (
  "Långsam förändring av arter över mycket lång tid",
  "fackspråklig, neutral, biologi", ["levande organismers förändring över lång tid enl. darwins lära"],
  [["levande organismers förändring över lång tid enl. darwins lära"]],
  "Under %s utvecklade vissa djur ett inre skelett." % (H % "evolutionen"),
  "SO:s definition är bara 'utveckling', men SAOL ger den biologiska. "
  "Underbetydelsen 'spec. i politiska sammanhang' gäller evolution som "
  "motsats till revolution -- gradvis förändring i stället för omvälvning -- "
  "och är en användning av samma grundbetydelse."),

 "exceptionell": (
  "Som är ett tydligt undantag från det vanliga",
  "formell, neutral", ["högst ovanlig", "undantagsvis förekommande"],
  [["högst ovanlig", "undantagsvis förekommande"]],
  "Hon var en %s begåvning redan som barn." % (H % "exceptionell"),
  "En betydelse. Båda synonymerna finns i poolen."),

 "fascination": (
  "Intensivt intresse för något ; förmågan att väcka sådant intresse",
  "litterär, neutral ; litterär, neutral",
  ["intensivt intresse", "egenskapen att väcka intensivt intresse"],
  [["intensivt intresse"], ["egenskapen att väcka intensivt intresse"]],
  "Han läste boken med stor %s." % (H % "fascination"),
  "RÄTTAT: SO har två betydelser -- känslan hos den som betraktar OCH "
  "egenskapen hos det som betraktas. Kortet hade bara den första. "
  "'tjusning' saknar belägg."),

 "flaggskepp": (
  "Fartyg som befälhavaren styr flottan från ; det främsta i en grupp",
  "neutral, neutral, sjöfart ; neutral, neutral",
  ["≈≈ amiralsfartyg", "bildl. viktigaste produkt el. avdelning"],
  [["≈≈ amiralsfartyg"], ["bildl. viktigaste produkt el. avdelning"]],
  "Elbilen var företagets nya %s inom hållbar mobilitet." % (H % "flaggskepp"),
  "Kortet hade båda betydelserna. 'amiralsskepp' och 'paradnummer' saknar "
  "belägg. Registret ändrat från vardaglig till neutral."),

 "flott": (
  "Elegant och påkostad ; smält djurfett som man steker i",
  "vardaglig, positiv ; neutral, neutral, matlagning",
  ["fin", "stilig", "smält djurfett"],
  [["fin", "stilig"], ["smält djurfett"]],
  "Han klädde sig i en %s kostym för bröllopet." % (H % "flott"),
  "Kortet hade båda betydelserna. 'elegant', 'snygg', 'ister' och "
  "'stekfett' saknar belägg och är utbytta mot poolens egna. SO:s tredje "
  "post ('som helt bärs av vatten') är ett HOMONYM -- flott som i flytande "
  "-- och hör inte hit."),

 "grammatik": (
  "Reglerna för hur ord och meningar byggs i ett språk ; lärobok i de reglerna",
  "neutral, neutral, lingvistik ; neutral, neutral",
  ["språklära", "≈≈ lärobok"], [["språklära"], ["≈≈ lärobok"]],
  "Han satt uppe hela natten och pluggade %s inför tentan." % (H % "grammatik"),
  "SO:s två definitioner är samma sak i äldre och modern tappning. "
  "Underbetydelsen 'äv. om motsvarande lärobok' bär eget innehåll -- boken "
  "är ett fysiskt föremål, inte ett regelsystem -- och står som egen "
  "betydelse. 'syntax' är struket: syntax är en DEL av grammatiken."),

 "haiku": (
  "Japansk kortdikt på tre rader",
  "fackspråklig, neutral, litteraturvetenskap", ["en typ av japansk kortdikt"],
  [["en typ av japansk kortdikt"]],
  "En %s fångar ett ögonblick i naturen med bara några få ord." % (H % "haiku"),
  "En betydelse. Kortet sade '17 stavelser', vilket är sant för japanskan "
  "men inte för svenska haiku -- SO nämner det inte, och SAOL säger bara "
  "treradig. Formuleringen är därför bytt mot det källorna faktiskt ger."),

 "höfta": (
  "Gissa fram ett svar utan säkert underlag",
  "vardaglig, neutral", ["bestämma på ett ungefär", "skatta"],
  [["bestämma på ett ungefär", "skatta"]],
  "Han visste inte hur man skriver ett kåseri, så det var bara att %s." % (H % "höfta"),
  "SO:s två definitioner är samma handling -- att arbeta på känn och att "
  "göra en snabb uppskattning. 'gissa' och 'måfå' saknar belägg; 'måfå' är "
  "dessutom inget verb."),

 "imitativ": (
  "Som går ut på att härma något",
  "formell, neutral", ["efterliknande"], [["efterliknande"]],
  "Barnen lärde sig språket med en %s metod, genom att härma vuxna." % (H % "imitativ"),
  "En betydelse. 'efterliknande' finns i poolen."),
}


poster = json.load(io.open(FIL, encoding="utf-8"))
n, obelagda = 0, []
for e in poster:
    d = K.get(e["ord"])
    if not d:
        continue
    hb, reg, syn, grp, ex, slut = d
    pool = set(HJ.synpool(e["ord"]))
    for s in syn:
        if not s.startswith("≈") and s not in pool:
            obelagda.append((e["ord"], s))
    e["proposed"] = {"huvudbetydelse": hb, "register": reg, "synonymer": syn,
                     "synonym_groups": grp, "exempelmening": ex,
                     "etymologi": HJ.etym(e["ord"])}
    e["sokkoll"] = {"kalla": HJ.kallor(e["ord"]), "slutsats": slut}
    e["approved"] = True
    n += 1

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Skrev %d kort." % n)
print("(min egen poolkontroll ar strangare an forgranskas -- kor forgranska.py)")
print("utanfor min pool:", obelagda or "inga")
