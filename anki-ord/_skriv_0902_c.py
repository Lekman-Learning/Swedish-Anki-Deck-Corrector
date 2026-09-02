# -*- coding: utf-8 -*-
"""Batch C: kort 34-53 (garva .. overdadig). Plus registerfixet i batch B."""
import io, json, os, sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02_v3-batch.json"
H = '<font color="#3498db">%s</font>'


def kallor(o):
    d = json.load(io.open(os.path.join("uppslag", o + ".json"), encoding="utf-8"))
    u = d.get("urler") or {}
    return " ".join(u[k] for k in ("svenska.se", "synonymer.se", "wiktionary") if u.get(k))


K = {}

K["garva"] = (
 "Bereda hud till läder ; skratta",
 "neutral i betydelse 1, vardaglig i 2",
 ["bereda hud till läder", "skratta"],
 [["bereda hud till läder"], ["skratta"]],
 "Vi " + H % "garvade" + " så vi fick ont i magen.",
 None,
 "TVA helt oslaktade betydelser i SO: 'bereda (hud) till lader genom behandling med vissa "
 "amnen' och 'skratta' (vardagligt). De har inget semantiskt samband alls, vilket ar just "
 "varfor ordet ar en fraga vard - man traffar pa skratt-betydelsen dagligen och "
 "garvnings-betydelsen aldrig, och blandar darfor ihop dem pa prov.")

K["hermetisk"] = (
 "Fullständigt lufttät ; om framställning: sluten och otillgänglig",
 "formell",
 ["lufttät", "otillgänglig"],
 [["lufttät"], ["otillgänglig"]],
 "Texten var " + H % "hermetisk" + " — jag läste den tre gånger utan att förstå poängen.",
 "efter Hermes Trismegistos, den mytiske forfattaren till alkemiska skrifter",
 "SO ger tva huvudbetydelser: 'fullstandigt lufttat' och 'otillganglig'. Den andra ar den "
 "bildliga och den som moter i text om sprak och konst. Bada tas med; den konkreta star "
 "forst eftersom den forklarar bilden - en hermetisk text ar sluten pa samma satt som en "
 "lufttat behallare.")

K["idiom"] = (
 "Fast uttryck vars betydelse inte går att räkna ut ur de ingående orden ; särspråk inom "
 "ett större språkområde",
 "fackspråklig, språkvetenskap",
 ["särspråk"],
 None,
 "Uttrycket \"kasta yxan i sjön\" är ett " + H % "idiom" + " — orden var för sig säger ingenting om att ge upp.",
 "grekiskans idioma 'sarart', till idios 'egen'",
 "TVA betydelser i SO, bada egna huvudbetydelser: 'fast uttryck vars innebord inte framgar "
 "av de ingaende ordens betydelser' och sprakbetydelsen 'sarsprak'. SO ger sjalv exemplet "
 "'kasta yxan i sjon', som anvands i exempelmeningen. Antalet pa kortet matchar SO:s.")

K["knapphändig"] = (
 "Alltför kortfattad, som ger färre uppgifter än man behöver",
 "neutral",
 ["fåordig", "kortfattad"],
 None,
 "Rapporten var så " + H % "knapphändig" + " att ingen förstod vad som faktiskt hänt.",
 None,
 "SO: 'som ar i minsta laget' plus 'faordig, kortfattad'. OTILLRACKLIGHETEN ar poangen: "
 "knapphandig ar inte beromande som 'kortfattad' kan vara, utan sager att det saknas "
 "nagot. 'i minsta laget' i SO bar den bedomningen och skrivs darfor ut som 'alltfor' "
 "i huvudbetydelsen.")

K["kommitté"] = (
 "Grupp personer som tillsatts för att utföra en bestämd uppgift",
 "formell",
 ["arbetsgrupp", "nämnd", "utskott"],
 None,
 "En " + H % "kommitté" + " tillsattes för att utreda frågan och kom med sitt betänkande ett år senare.",
 "franskans comite, av engelskans committee, till commit 'anfortro'",
 "SO: 'samling personer som ar tillsatta for att utfora viss uppgift'. SAOL: 'arbetsgrupp "
 "utsedd att handha en uppgift', plus 'namnd' och 'utskott' som likvardiga. TILLSATT-ledet "
 "ar avgorande: en kommitte bildas inte spontant utan utses av nagon, och det skiljer den "
 "fran en grupp i allmanhet.")

K["konsolidera"] = (
 "Säkra något genom att förstärka dess inre struktur ; om företag: stärka den ekonomiska "
 "ställningen",
 "formell",
 ["säkra", "förstärka"],
 [["säkra"], ["förstärka"]],
 "Partiet använde året till att " + H % "konsolidera" + " sin ställning i väljargrupper det redan hade.",
 "latinets consolidare 'gora fast', till solidus 'fast, hel'",
 "SO ger tva huvudbetydelser: 'sakra genom att forbattra den inre strukturen' och "
 "'forstarka den ekonomiska stallningen (for visst foretag)'. Den andra ar en tillampning "
 "av den forsta pa ekonomi, men SO ger den egen status och den ar den vanligaste i "
 "nyhetstext, sa bada star pa kortet. INRE-ledet ar det som skiljer konsolidera fran att "
 "bara vaxa: man befaster det man redan har.")

K["konststycke"] = (
 "Handling som kräver särskild skicklighet",
 "neutral",
 [],
 None,
 "Att få ihop schemat utan en enda krock var ett litet " + H % "konststycke" + ".",
 None,
 "SO: 'som fordrar sarskild skicklighet'. SAOL: 'som kraver stor skicklighet'. Bada ar "
 "relativsatser utan kort synonym, sa synonymfaltet lamnas tomt. Ordet anvands ofta "
 "ironiskt ('inget storre konststycke'), men den anvandningen har inget ordboksbelagg och "
 "skrivs darfor inte in i betydelsen.")

K["labil"] = (
 "Vars tillstånd ändras vid minsta påverkan ; om person: som lätt växlar sinnesstämning",
 "neutral; personbetydelsen ofta med negativ ton",
 ["ostadig", "vacklande", "osäker"],
 None,
 "Blandningen är kemiskt " + H % "labil" + " och måste förvaras kallt.",
 "latinets labilis 'som latt glider', till labi 'glida, falla'",
 "SO ger tva huvudbetydelser: 'vars lage eller tillstand forandras vid minsta paverkan' "
 "och 'som latt vaxlar sinnestillstand'. Bada star pa kortet - den fysiska forklarar den "
 "psykologiska. MINSTA PAVERKAN ar precisionen: labil ar inte samma sak som ostadig i "
 "allmanhet, det ar kansligheten for smaa storningar som ar poangen. Motsatsen ar stabil.")

K["omen"] = (
 "Ovanlig händelse som tolkas som ett förebud om något kommande",
 "neutral, något högtidlig",
 ["förebud", "varsel"],
 None,
 "Att korpen satte sig på taket togs som ett dåligt " + H % "omen" + ".",
 "latinets omen 'forebud, jartecken'",
 "SO: 'ovanlig handelse eller foreteelse som tolkas som forebud'. TOLKAS ar det viktiga "
 "ledet: ett omen ar inte en handelse som ar ett forebud, utan en som NAGON laser som ett "
 "forebud. Det star darfor kvar i huvudbetydelsen. 'forebud' och 'varsel' godtas bada ur "
 "ordbokstexten.")

K["parant"] = (
 "Som har ett elegant och välvårdat yttre",
 "neutral, något ålderdomlig",
 ["klädsam", "stilig"],
 None,
 "Hon kom i en " + H % "parant" + " kappa som fick alla att vända sig om.",
 "franskans parant, till parer 'smycka'",
 "SO: 'som har ett elegant och valvardat yttre'. SAOL: 'kladsam, stilig'. Ordet anvands "
 "bade om personer och om plagg; SAOL:s 'kladsam' pekar pa plagget, SO:s definition pa "
 "bararen. Bada anvandningarna ryms i huvudbetydelsen utan att delas upp, eftersom det ar "
 "samma egenskap sedd fran tva hall.")

K["sarkastisk"] = (
 "Präglad av bitande och hånfull ironi",
 "neutral",
 [],
 None,
 "Kommentaren var så " + H % "sarkastisk" + " att ingen vågade svara.",
 "grekiskans sarkazein 'bita i kottet, hana'",
 "SO: 'praglad av sarkasm'. Den definitionen ar CIRKULAR - den forklarar ordet med sitt "
 "eget substantiv och duger inte pa ett kort. Huvudbetydelsen ar darfor upplost till vad "
 "sarkasm ar: bitande, hanfull ironi. Av samma skal lamnas synonymfaltet tomt: 'praglad av "
 "sarkasm' ar poolens enda post och skulle bli en cirkular synonym. Etymologin ('bita i "
 "kottet') bar samma bild och forklarar 'bitande'.")

K["satirisk"] = (
 "Som angriper missförhållanden genom att förlöjliga dem",
 "neutral",
 [],
 None,
 "Programmet var " + H % "satiriskt" + " och drev med samtliga riksdagspartier.",
 "latinets satira, ursprungligen 'blandad ratt', sedan blandad diktform",
 "SO: 'som utnyttjar satirens verkningsmedel' - liksom sarkastisk en cirkular definition "
 "som forklarar ordet med sitt eget substantiv. Huvudbetydelsen loser upp den till vad "
 "satirens verkningsmedel ar: forlojligande i syfte att angripa. Synonymfaltet lamnas tomt "
 "av samma skal. SKILJ FRAN sarkastisk: satir angriper missforhallanden, sarkasm angriper "
 "en person.")

K["spatiös"] = (
 "Med stora mellanrum mellan bokstäver eller rader ; rymlig",
 "fackspråklig i betydelse 1, typografi",
 ["rymlig"],
 None,
 "Sättningen var " + H % "spatiös" + " och gjorde att texten tog dubbelt så många sidor.",
 "latinets spatiosus 'rymlig', till spatium 'rum, avstand'",
 "SO ger tva huvudbetydelser: 'forsedd med stora mellanrum' och 'rymlig'. Den forsta ar "
 "typografisk och den som ordet faktiskt moter i, den andra ar den allmanna. Bada star pa "
 "kortet. Etymologin binder ihop dem: spatium ar bade avstand och rum.")

K["tjusa"] = (
 "Väcka ett starkt och lustfyllt intresse hos någon",
 "neutral, något ålderdomlig",
 ["bedåra", "förtrolla", "hänföra"],
 None,
 "Utsikten " + H % "tjusade" + " honom så mycket att han glömde bort tiden.",
 None,
 "SO: 'vacka kanslor av lustbetonat intresse hos'. LUSTBETONAT ar precisionen: att tjusa "
 "ar inte att intressera i allmanhet utan att vacka ett njutningsfyllt intresse. SAOL ger "
 "'bedara, fortrolla, hanfora' som likvardiga alternativ, alla tre tagna som synonymer. "
 "Ordet har en trollformels-klang kvar (jfr fortrolla), vilket registret markerar.")

K["underkyld"] = (
 "Om vätska: som är under fryspunkten men ändå inte har stelnat till is",
 "fackspråklig, fysik och meteorologi",
 [],
 None,
 "Regnet var " + H % "underkylt" + " och frös till is i samma ögonblick det träffade vägen.",
 None,
 "TVA AV TRE KALLOR: uppslagningen fick inte full trekallstackning for det har ordet. "
 "SO: 'som inte stelnar till is trots att temperaturen ar under fryspunkten'. Definitionen "
 "ar en hel relativsats utan kort synonym, sa synonymfaltet lamnas tomt. PARADOXEN ar hela "
 "ordet - under noll men anda flytande - och maste sta kvar i huvudbetydelsen for att "
 "kortet ska betyda nagot.")

K["upprätta"] = (
 "Skapa eller inrätta något ; återställa någons anseende efter orättvisa beskyllningar",
 "formell",
 ["skapa", "återställa"],
 [["skapa"], ["återställa"]],
 "Domen " + H % "upprättade" + " honom efter tjugo år av misstankar.",
 None,
 "SO ger flera betydelser; kortet bar de tva som ar praktiskt atskilda och som ordet "
 "faktiskt moter i: 'ge existens at / skapa' (upprätta ett register, en handling) och "
 "'aterstalla anseendet hos (nagon) genom friande fran orattvisa beskyllningar'. Den andra "
 "ar den som ar svarast och som ett prov skulle fraga om, och star darfor i "
 "exempelmeningen. ORATTVISA-ledet ar obligatoriskt: man upprattas inte fran en riktig "
 "anklagelse.")

K["utopi"] = (
 "Föreställning om ett idealsamhälle som inte går att förverkliga",
 "neutral",
 ["dröm", "ouppnåeligt samhällsideal"],
 None,
 "Planen är en " + H % "utopi" + " — den förutsätter att ingen någonsin handlar i eget intresse.",
 "grekiskans ou 'icke' och topos 'plats', alltsa 'ingenstansland'; myntat av Thomas More 1516",
 "SO: 'forestallning om ett (ouppnaeligt) idealtillstand'. OUPPNAELIGHETEN star inom "
 "parentes i SO men ar inte valfri - den ar vad som skiljer en utopi fran ett mal, och "
 "SAOL bekraftar den med 'ouppnaeligt samhallsideal' och 'drom som inte kan forverkligas'. "
 "Den star darfor utan parentes i huvudbetydelsen. Etymologin sager samma sak: platsen "
 "som inte finns.")

K["ynklig"] = (
 "Så eländig att den väcker medlidande eller förakt",
 "neutral, nedsättande",
 ["ömklig"],
 None,
 "Försöket var så " + H % "ynkligt" + " att det var pinsamt att se på.",
 None,
 "SO: 'vard beklagande eller forakt'. DUBBELHETEN ar poangen: ynklig kan vacka bade "
 "medlidande och forakt, och vilket det blir avgors av sammanhanget. Bada leden star "
 "darfor i huvudbetydelsen - ett kort som bara sa 'omklig' skulle tappa foraktet, som ar "
 "den vanligare tonen i nutida bruk. SAOL: 'omklig'.")

K["ämbete"] = (
 "Högre statlig eller kyrklig befattning med en särskild, självständig funktion",
 "formell",
 [],
 None,
 "Han tillträdde sitt " + H % "ämbete" + " i januari och avgick redan i maj.",
 None,
 "SO: 'hogre statlig (eller kyrklig) befattning som har sarskild, sjalvstandig funktion'. "
 "SAOL: 'viktig offentlig el. kyrklig befattning'. SJALVSTANDIGHETEN ar det som skiljer ett "
 "ambete fran en anstallning: ambetet bar en egen befogenhet, inte en delegerad. Poolen "
 "innehaller bara fragment av definitionsstrangen ('hogre', 'sjalvstandig', 'viktig'), "
 "inga hela synonymer, sa faltet lamnas tomt.")

K["överdådig"] = (
 "Slösande rik och påkostad ; storartad ; dumdristig",
 "neutral; betydelse 3 ålderdomlig",
 ["slösande rik", "storartad", "ypperlig", "dumdristig"],
 [["slösande rik"], ["storartad", "ypperlig"], ["dumdristig"]],
 "De bjöd på en " + H % "överdådig" + " middag med sju rätter och tre sorters vin.",
 None,
 "TRE betydelser ur SO:s fyra def: 'praglad av overdad / slosande rik', 'storartad, "
 "ypperlig' och 'dumdristig'. Den tredje ar den overraskande och den aldsta - overdad "
 "betydde ursprungligen overmod, inte lyx. Den tas med eftersom den ar helt osynlig fran "
 "de tva andra och ar precis den sorts betydelse ett prov fragar om.")


TILLAT = {
 "tala med kluven tunga": {"register_motsager_markning":
   "Markningen 'historiskt' kommer fran ett av de INGAENDE orden i fritextsokningen "
   "(lemmat 'med' som substantiv, dvs. skenan pa en slade), inte fran uttrycket. "
   "Flerordsuttryck saknar egen artikel och drar med sig grannlemmans markningar. "
   "Uttrycket sjalvt ar fullt levande och registret 'neutral, bildlig' ar korrekt."},
 "garva": {"betydelse_kan_saknas":
   "SO raknar 4; de tva extra ar underbetydelser utan egen definition. Kortets tva "
   "betydelser motsvarar SO:s tva riktiga def."},
 "hermetisk": {"betydelse_kan_saknas":
   "SO:s tredje post ar en underbetydelse utan egen definition. Kortets tva betydelser "
   "motsvarar SO:s konkreta och bildliga huvudbetydelse."},
 "knapphändig": {"betydelse_kan_saknas":
   "SO:s poster ar 'som ar i minsta laget' och 'faordig, kortfattad' - tva formuleringar "
   "av samma otillracklighet, inte tva betydelser. Kortet slar ihop dem medvetet."},
 "kommitté": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse."},
 "konsolidera": {"betydelse_kan_saknas":
   "SO:s tredje post ar en underbetydelse utan egen definition. Kortets tva betydelser "
   "motsvarar SO:s tva riktiga def."},
 "konststycke": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse."},
 "labil": {"betydelse_kan_saknas":
   "SO raknar 5; tre ar underbetydelser utan egen definition. Kortets tva betydelser "
   "motsvarar SO:s tva riktiga def (fysisk och psykologisk)."},
 "omen": {"betydelse_kan_saknas":
   "SO:s tva extra poster ar underbetydelser utan egen definition. Ordet har en betydelse."},
 "parant": {"betydelse_kan_saknas":
   "SO:s tva extra poster ar underbetydelser utan egen definition. Ordet har en betydelse; "
   "anvandningen om bade person och plagg ryms i den."},
 "spatiös": {"betydelse_kan_saknas":
   "SO:s tredje post ar en underbetydelse utan egen definition. Kortets tva betydelser "
   "motsvarar SO:s tva riktiga def."},
 "tjusa": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse."},
 "upprätta": {"betydelse_kan_saknas":
   "SO raknar 7. Kortet bar de tva betydelser som ar praktiskt atskilda och som ordet "
   "moter i ('inratta' och 'aterstalla anseendet'); ovriga poster ar underbetydelser utan "
   "egen definition eller nara varianter av inratta-betydelsen."},
 "ynklig": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse, "
   "vars dubbla ton (medlidande/forakt) star utskriven."},
 "ämbete": {"betydelse_kan_saknas":
   "SO:s tva extra poster ar underbetydelser utan egen definition. Ordet har en betydelse."},
 "överdådig": {"betydelse_kan_saknas":
   "SO raknar 6: fyra def varav tva ar nara varianter av lyx-betydelsen ('praglad av "
   "overdad' och 'slosande rik'), plus tva underbetydelser utan egen definition. Kortets "
   "tre betydelser tacker samtliga sarskiljbara innebordar."},
}


poster = json.load(io.open(FIL, encoding="utf-8"))
n = t = 0
for e in poster:
    d = K.get(e["ord"])
    if d:
        hb, reg, syn, grp, ex, etym, slut = d
        e["proposed"] = {"huvudbetydelse": hb, "register": reg, "synonymer": syn,
                         "synonym_groups": grp, "exempelmening": ex, "etymologi": etym}
        e["sokkoll"] = {"kalla": kallor(e["ord"]), "slutsats": slut}
        e["approved"] = True
        n += 1
    if e["ord"] in TILLAT:
        e.setdefault("forgranska_tillat", {}).update(TILLAT[e["ord"]])
        t += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("batch C: %d kort, %d poster med motivering" % (n, t))
saknas = [o for o in K if not any(e["ord"] == o for e in poster)]
print("ord i K som inte fanns i filen:", saknas or "inga")
