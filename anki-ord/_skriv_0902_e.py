# -*- coding: utf-8 -*-
"""Batch E: kort 76-95 (disponent .. insistera). Plus tre fix i batch D."""
import io, json, os, sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02_v3-batch.json"
H = '<font color="#3498db">%s</font>'


def kallor(o):
    d = json.load(io.open(os.path.join("uppslag", o + ".json"), encoding="utf-8"))
    u = d.get("urler") or {}
    return " ".join(u[k] for k in ("svenska.se", "synonymer.se", "wiktionary") if u.get(k))


REG_FIX = {
 "blott": "ålderdomlig utom i vissa uttryck",
 "chikan": "något ålderdomlig; betydelse 2 och 3 fackspråkliga",
}
FIX_TILLAT = {
 "bestyr": {"frammande_uppslagsord":
   "Det frammande uppslagsordet ar verbet 'bestyra' (ombesorja), som fritextsokningen drar "
   "med sig. Substantivet bestyr har egna SO-poster och inget innehall fran verbet har "
   "anvants."},
}

K = {}

K["disponent"] = (
 "Person i ledande ställning i affärsvärlden, ofta chef för ett industriföretag",
 "neutral, mest historisk",
 ["förvaltare", "person med chefsfunktion"],
 None,
 "Hans farfar var " + H % "disponent" + " vid bruket i trettio år.",
 "till disponera, av latinets disponere 'ordna, forfoga over'",
 "SO: 'person i ledande stallning i affarsvarlden'. SAOL ger ocksa 'forvaltare av "
 "bostadsfastighet'. Titeln ar i praktiken historisk - den bars av bruksledningar och "
 "moter idag mest i aldre text och slaktforskning, vilket registret markerar.")

K["driftkucku"] = (
 "Person som andra ständigt driver med",
 "vardaglig",
 ["person som andra driver med"],
 None,
 "Han blev klassens " + H % "driftkucku" + " redan första veckan.",
 None,
 "SO: 'person som ofta utsatts for forlojligande skamt'. SAOL: 'person som andra driver "
 "med'. UPPREPNINGEN ar en del av betydelsen - en driftkucku ar inte den som blir "
 "utskrattad en gang utan den som standigt ar mal, och 'ofta'/'standigt' star darfor kvar.")

K["ekipera"] = (
 "Utrusta någon med kläder",
 "formell, ålderdomlig",
 ["utrusta"],
 None,
 "Han lät " + H % "ekipera" + " sig från topp till tå inför bröllopet.",
 "franskans equiper 'utrusta', ursprungligen om att rusta ett fartyg",
 "SO: 'utrusta med klader'. KLADERNA ar hela inskrankningen: att ekipera ar inte att "
 "utrusta i allmanhet. Etymologin ar tvartom vidare (att rusta ett fartyg), vilket "
 "forklarar varfor ordet kanns storslaget for en sa vardaglig sak.")

K["eloge"] = (
 "Uttalat beröm, ofta inför andra",
 "neutral",
 ["beröm", "lovord"],
 None,
 "Hon fick en " + H % "eloge" + " av chefen inför hela avdelningen.",
 "franskans eloge 'lovtal', av grekiskans eulogia 'lovprisning'",
 "SO: 'uppskattande omnamnande'. OMNAMNANDET ar poangen - en eloge sags UT, garna offentligt, "
 "till skillnad fran uppskattning man bara kanner. 'berom' och 'lovord' godtas ur SAOL.")

K["enständig"] = (
 "Envist ihärdig, som inte ger sig",
 "ålderdomlig",
 ["enträgen", "ihärdig"],
 None,
 "Han var " + H % "enständig" + " i sitt krav och släppte det aldrig.",
 None,
 "TVA AV TRE KALLOR: ordet har INGEN SO-artikel (0 def) och saknades dessutom pa "
 "synonymer.se. Betydelsen vilar pa SAOL och SAOB, som ger 'entragen' och 'iharding'. "
 "Bada pekar at samma hall - uthallighet i ett krav - och tas som synonymer.")

K["fallenhet"] = (
 "Medfödd förmåga eller benägenhet för något",
 "neutral",
 ["anlag", "benägenhet"],
 None,
 "Hon hade en tydlig " + H % "fallenhet" + " för språk redan som barn.",
 None,
 "SO: 'medfodd formaga'. MEDFODDHETEN ar det avgorande ledet - fallenhet ar inte inlard "
 "skicklighet utan en anlagsmassig lattnad, och utan det ledet blir ordet utbytbart mot "
 "'formaga'. SAOL: 'anlag, benagenhet'.")

K["federalism"] = (
 "Statsskick där makten är delad mellan en centralmakt och delstater",
 "fackspråklig, statsvetenskap",
 ["förbundssystem"],
 None,
 "USA:s " + H % "federalism" + " ger delstaterna egen lagstiftande makt.",
 "latinets foedus 'forbund'",
 "TVA AV TRE KALLOR (synonymer.se saknade artikel). SO: 'statsskick som kannetecknas av "
 "maktdelning mellan centralmakt och delstater'. SAOL: 'forbundssystem som "
 "organisationsform for stat t.ex. i USA'. MAKTDELNINGEN ar karnan - en federation ar inte "
 "bara en sammanslutning utan en dar bada nivaerna har egen, grundlagsskyddad makt.")

K["fejka"] = (
 "Utge något för att vara äkta fast det inte är det",
 "vardaglig",
 ["förfalska", "låtsa", "hitta på"],
 None,
 "Han " + H % "fejkade" + " ett intyg för att slippa provet.",
 "engelskans fake",
 "SO: 'felaktigt utge (nagot) for att vara akta'. AVSIKTEN ar inbyggd: att fejka ar inte "
 "att ha fel utan att medvetet framstalla nagot falskt som akta. SAOL ger 'forfalska', "
 "'latsa' och 'hitta pa' som likvardiga.")

K["force majeure"] = (
 "Yttre, övermäktig omständighet som gör det omöjligt att fullgöra ett avtal",
 "fackspråklig, juridik",
 [],
 None,
 "Leverantören åberopade " + H % "force majeure" + " när hamnen stängdes av strejken.",
 "franskan, ordagrant 'overmaktig kraft'",
 "SO: 'yttre omstandighet som gor det omojligt att fullgora ett avtal'. SAOL skarper till "
 "'overmaktiga omstandigheter'. BADA leden behovs: omstandigheten maste vara BADE yttre "
 "(utanfor partens kontroll) och overmaktig (inte bara besvarlig). Bada kallorna ger hela "
 "definitionsstrangar utan kort synonym, sa faltet lamnas tomt.")

K["fylogeni"] = (
 "En arts eller artgrupps utvecklingshistoria",
 "fackspråklig, biologi",
 [],
 None,
 "Kladogrammet visar valarnas " + H % "fylogeni" + " tillbaka till landlevande förfäder.",
 "grekiskans phylon 'stam, slakte' och genesis 'uppkomst'",
 "TVA AV TRE KALLOR (synonymer.se saknade artikel). SO och SAOL sager samma sak: 'en arts "
 "eller artgrupps utvecklingshistoria'. Poolen innehaller bara hela definitionsstrangar, "
 "sa synonymfaltet lamnas tomt. SKILJ FRAN ontogeni, som ar den enskilda individens "
 "utveckling - det ar den forvaxling ett prov skulle testa.")

K["fäderne"] = (
 "Faderns sida av släkten",
 "formell, ålderdomlig",
 [],
 None,
 "Gården hade gått i arv på " + H % "fädernet" + " i fem generationer.",
 None,
 "SO: 'faderns sida (av en viss persons slakt)'. Ordet moter nastan bara i bestamd form "
 "och i fasta uttryck ('pa fadernet', 'arv och eget'), vilket exempelmeningen visar. "
 "Poolen ger bara fragment ('faderns') och hela definitionsstrangen, sa synonymfaltet "
 "lamnas tomt. Motsatsen ar moderne.")

K["förkomma"] = (
 "Gå förlorad genom slarv eller vårdslöshet",
 "formell",
 ["försvinna", "komma bort"],
 None,
 "Handlingarna hade " + H % "förkommit" + " någonstans i posthanteringen.",
 None,
 "SO: 'ga forlorad genom slarv'. SLARVET ar med i definitionen - nagot som forkommer har "
 "inte stulits eller forstorts utan tappats bort, och ordet bar darfor en antydan om "
 "vardslos hantering. Ordet anvands nastan bara i perfekt particip ('forkommen', "
 "'har forkommit').")

K["förställa"] = (
 "Förändra sitt utseende eller sin röst för att vilseleda ; låtsas vara någon annan",
 "formell",
 ["göra sig oigenkännlig", "låtsas vara någon annan"],
 None,
 "Han " + H % "förställde" + " rösten i telefon så att ingen skulle känna igen honom.",
 None,
 "SO ger tva huvudbetydelser: 'forandra (en persons kannetecken) i vilseledande syfte' och "
 "'gora sig oigenkannlig'. VILSELEDANDET ar obligatoriskt - att forstalla ar aldrig "
 "neutral forandring. SKILJ FRAN 'forestalla', som ar ett annat ord och den vanligaste "
 "forvaxlingen.")

K["galej"] = (
 "Uppsluppet festande",
 "vardaglig, ålderdomlig",
 ["festande"],
 None,
 "Hela kvarteret var ute på " + H % "galej" + " efter segern.",
 None,
 "SO: 'uppsluppet festande'. Ordet moter nastan bara i uttrycket 'vara/ga ut pa galej', "
 "vilket exempelmeningen visar. UPPSLUPPENHETEN skiljer galej fran fest i allmanhet och "
 "star kvar i huvudbetydelsen.")

K["gniden"] = (
 "Överdrivet snål",
 "vardaglig, nedsättande",
 ["snål", "gnidig"],
 None,
 "Han var för " + H % "gniden" + " för att ens bjuda på kaffe.",
 None,
 "SO ger flera poster; den levande betydelsen ar 'snal', med SAOL:s 'gnidig' som variant. "
 "OVERDRIFTEN ar det som gor ordet nedsattande - gniden ar inte sparsam utan snal bortom "
 "det rimliga - och star darfor i huvudbetydelsen. Bilden bakom ordet ar den som gnider "
 "mynten mellan fingrarna.")

K["goutera"] = (
 "Uppskatta och tycka om",
 "formell, något ålderdomlig",
 ["gilla", "uppskatta", "tycka om"],
 None,
 "Publiken " + H % "gouterade" + " inte skämtet.",
 "franskans gouter 'smaka, njuta av', till latinets gustare",
 "SO: 'uppskatta'. SAOL: 'gilla, tycka om'. Ordet anvands sarskilt ofta NEKANDE ('inte "
 "goutera'), vilket exempelmeningen visar - det ar den konstruktion man faktiskt moter. "
 "Etymologin (att smaka) forklarar varfor ordet har en ton av forfinad bedomning.")

K["grift"] = (
 "Grav",
 "ålderdomlig, högtidlig",
 ["grav"],
 None,
 "Han lades i sina fäders " + H % "grift" + ".",
 None,
 "SO och SAOL ger bada enbart 'grav'. Ordet ar helt utdott i vardagsprosan och lever kvar "
 "i sammansattningar och fasta uttryck (griftefrid, griftetal), vilket ar dar man faktiskt "
 "moter det. Poolens post '1grav 1' ar ett formateringsartefakt med kvarlamnade siffror; "
 "den rena formen 'grav' anvands.")

K["hugskott"] = (
 "Plötslig och tillfällig idé utan större värde",
 "neutral, något nedsättande",
 ["plötslig idé"],
 None,
 "Planen var ett " + H % "hugskott" + " som han glömde bort redan nästa dag.",
 None,
 "SO: 'tillfallig ide eller tanke utan storre varde'. SAOL: 'plotslig ide'. BADE "
 "plotsligheten och VARDELOSHETEN ar med i kallorna, och det ar den senare som gor ordet "
 "nedsattande: ett hugskott ar inte en insikt utan ett infall.")

K["index"] = (
 "Tal som sätts i relation till ett grundtal för att möjliggöra jämförelser ; förteckning "
 "över huvudpunkter ; nedsänkt tecken som skiljer bokstäver åt",
 "fackspråklig",
 ["jämförelsetal", "förteckning"],
 [["jämförelsetal"], ["förteckning"], []],
 "Konsumentprisindex steg med två procent, medan lönerna följde ett annat " + H % "index" + ".",
 "latinets index 'angivare, visare', till indicare 'peka ut'",
 "SO ger fem huvudbetydelser. Kortet bar de TRE som ar praktiskt atskilda och som ordet "
 "faktiskt moter i: statistiktalet, forteckningen (register) och det matematiska "
 "nedsankta tecknet. Etymologin ('visare') ar den gemensamma namnaren - alla tre PEKAR UT "
 "nagot. De ovriga SO-posterna ('avlasningsmarke pa en skala', 'tal som anger "
 "karakteristisk egenskap') ar specialfall av statistiktalet.")

K["insistera"] = (
 "Envist hålla fast vid ett krav eller ett påstående",
 "formell",
 ["envisas"],
 None,
 "Hon " + H % "insisterade" + " på att få se originalhandlingen.",
 "latinets insistere 'sta pa, halla fast vid'",
 "TVA AV TRE KALLOR (wiktionary gav HTTP 429 aven vid omkorning). SO ger tva poster: "
 "'envisas med att havda' och 'envisas med att krava'. De ar samma handling riktad mot "
 "tva olika objekt - en asikt respektive ett krav - och slas darfor ihop till en "
 "betydelse pa kortet, med bada objekten utskrivna.")


TILLAT = {
 "ekipera": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse."},
 "eloge": {"betydelse_kan_saknas":
   "SO:s tva extra poster ar underbetydelser utan egen definition. Ordet har en betydelse."},
 "fäderne": {"betydelse_kan_saknas":
   "SO:s extra poster ar 'foraldra-' som forled och en underbetydelse utan egen "
   "definition. Ordet har en betydelse."},
 "förställa": {"betydelse_kan_saknas":
   "SO:s tredje post ar en underbetydelse utan egen definition. Kortets tva betydelser "
   "motsvarar SO:s tva riktiga def."},
 "gniden": {"betydelse_kan_saknas":
   "SO raknar 4, men posterna ar varianter av samma snalhet ('snal', 'gnidig') plus "
   "underbetydelser utan egen definition. Ordet har en levande betydelse."},
 "index": {"betydelse_kan_saknas":
   "SO raknar 7. Kortet bar de tre praktiskt atskilda betydelserna; ovriga poster ar "
   "specialfall av statistiktalet ('avlasningsmarke pa en skala', 'tal som anger "
   "karakteristisk egenskap') eller underbetydelser utan egen definition."},
 "insistera": {"betydelse_kan_saknas":
   "SO:s tva def ar 'envisas med att havda' och 'envisas med att krava' - samma handling "
   "mot tva objekt, medvetet sammanslagna med bada objekten utskrivna. Tredje posten "
   "saknar egen definition."},
}


poster = json.load(io.open(FIL, encoding="utf-8"))
n = t = f = 0
for e in poster:
    o = e["ord"]
    if o in REG_FIX:
        e["proposed"]["register"] = REG_FIX[o]
        f += 1
    if o in FIX_TILLAT:
        e.setdefault("forgranska_tillat", {}).update(FIX_TILLAT[o])
        f += 1
    d = K.get(o)
    if d:
        hb, reg, syn, grp, ex, etym, slut = d
        e["proposed"] = {"huvudbetydelse": hb, "register": reg, "synonymer": syn,
                         "synonym_groups": grp, "exempelmening": ex, "etymologi": etym}
        e["sokkoll"] = {"kalla": kallor(o), "slutsats": slut}
        e["approved"] = True
        n += 1
    if o in TILLAT:
        e.setdefault("forgranska_tillat", {}).update(TILLAT[o])
        t += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("batch E: %d kort, %d motiveringar, %d fix" % (n, t, f))
saknas = [o for o in K if not any(e["ord"] == o for e in poster)]
print("ord i K som inte fanns:", saknas or "inga")
