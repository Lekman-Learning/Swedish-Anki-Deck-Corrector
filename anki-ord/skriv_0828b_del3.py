# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch2, kort 51-75. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch2.json"
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


satt("humifiera",
     "Om växtdelar: brytas ner och bli till mull",
     "fackspråklig, neutral, biologi",
     [],
     "Torven bestod av växtrester som ännu inte hunnit " + B % "humifieras" +
     ".",
     "→ Latin humus 'jord' — samma ord som i humus och exhumera.",
     "OFULLSTANDIG KALLBILD: uppslagsordskollen gav traff ENDAST i SAOB -- "
     "ordet saknas i bade SO och SAOL, och svenska.se:s sammandrag var "
     "tomt. Hamtade darfor SAOB-artikeln direkt (saob.se/artikel/"
     "?seek=humifiera, HTTP 200): 'HUMIFIERA ... (i fackspr.) forvandla "
     "till mull l. mullartad substans', publicerad 1932, med belagg fran "
     "Hygiea 1857 om 'ej fullt humifierade vaxtdelar'. SAOB anger aven "
     "sammansattningen humifieringsgrad. Definitionen ar skriven passivt "
     "(brytas ner) eftersom det ar sa ordet faktiskt anvands.",
     extra=("https://www.saob.se/artikel/?seek=humifiera",),
     conf=7)

satt("i tid och otid",
     "Alltför ofta och även när det inte passar",
     "neutral, negativ",
     [],
     "Han drog samma historia " + B % "i tid och otid" + " tills ingen "
     "orkade lyssna.",
     None,
     "Hela frasen gav INGEN traff som uppslagsord i SO/SAOL/SAOB -- "
     "uttryck star sallan som egna lemman. Slog darfor upp grundordet "
     "'otid' separat (samma datum, HTTP 200, traffar i saol, so, saob): "
     "SO 'vid felaktig eller olamplig tidpunkt', med 'i tid och otid' och "
     "'i otid' listade som just de uttryck ordet forekommer i. Wiktionary "
     "ger frasen direkt: 'alltid, alltfor ofta'. Definitionen slar ihop "
     "bada: det ar bade frekvensen och olampligheten som ligger i "
     "uttrycket.",
     extra=("https://svenska.se/api/msearch?ord=otid",))

satt("insulär",
     "Som hör till en ö ; bildligt: avskärmad från intryck utifrån",
     "fackspråklig, neutral ; formell, negativ",
     [],
     "Han beskrev 1800-talets svenska kulturliv som " + B % "insulärt" +
     " och självupptaget.",
     "→ Latin insula 'ö' — samma rot som i isolera.",
     "SO: 'som avser eller ar typisk for en o' samt -- markt 'av. "
     "bildligt' -- 'avskild fran yttre (intellektuella) impulser'. SAOL: "
     "'o-; provinsiell'. Bada betydelserna behalls; den bildliga ar den "
     "som faktiskt dyker upp i text. Etymologin ar med eftersom "
     "slaktskapen med 'isolera' gor bada betydelserna sjalvforklarande pa "
     "en gang.")

satt("kartig",
     "Om frukt: omogen ; om person: kaxig och uppkäftig",
     "vardaglig, neutral ; vardaglig, negativ",
     [],
     "När det väl var dags för operation var hon inte lika " + B % "kartig" +
     " längre.",
     None,
     "SO ger bada: 'omogen' och 'kaxig', bruk 'vardagligt'. SAOL har bara "
     "fruktbetydelsen: 'om frukt el. bar: omogen'. Wiktionary bara "
     "personbetydelsen: 'uppkaftig, kaxig'. Bada behalls darfor, med "
     "kallorna sammanlagda. JFR i SO: 'stursk' -- struket som synonym, det "
     "ar ovanligare an kartig sjalvt. Betydelserna hanger ihop: en kart ar "
     "en omogen frukt.")

satt("kofferdist",
     "Sjöman i handelsflottan ; fartyg i handelsflottan",
     "ålderdomlig, neutral, sjöfart ; ålderdomlig, neutral, sjöfart",
     [],
     "Han mönstrade på som " + B % "kofferdist" + " och seglade på "
     "Sydamerika.",
     None,
     "SO ger bada: 'sjoman vid handelsflottan' och 'handelsfartyg', bruk "
     "'alderdomligt'. SAOL bekraftar bada i omvand ordning. Att samma ord "
     "betecknar bade manniskan och fartyget ar ordets sardrag och skalet "
     "att bada betydelserna behalls. Till 'kofferdi', aldre benamning pa "
     "handelssjofart. Belagt sedan 1883.")

satt("kommod",
     "Låg möbel med tvättfat, från tiden före rinnande vatten",
     "neutral, neutral, historisk",
     [],
     "I hörnet stod en " + B % "kommod" + " med porslinsfat och kanna.",
     "→ Franska commode 'bekväm' — möbeln som gjorde tvättandet enkelt.",
     "SO: 'lagt skap med tvattfat', med 'av. om skapliknande tvattstall', "
     "bruk 'mest historiskt'. SAOL: 'skapliknande tvattstall'. "
     "Definitionen lagger till 'fran tiden fore rinnande vatten' eftersom "
     "mobeln annars ar obegriplig -- det ar bruket, inte formen, som "
     "forklarar den. Wiktionarys andra betydelse ('langsmal byra') ar en "
     "senare betydelseglidning och utelamnad.")

satt("konfektion",
     "Tillverkning av och handel med färdigsydda kläder",
     "fackspråklig, neutral",
     [],
     "Han var grosshandlare i tyger och " + B % "konfektion" + ".",
     "→ Latin conficere 'färdigställa' — samma rot som i konfekt.",
     "SO: '(handel med eller tillverkning av) fabrikssydda klader'. SAOL: "
     "'fabriksmassig tillverkning av klader; handel med fardigsydda "
     "fabriksgjorda klader'. Ordet betecknar motsatsen till skraddarsytt. "
     "Etymologin ar med for slaktskapen med konfekt, som ar oantad och "
     "gor ordet minnesvart (bada ar nagot 'fardigstallt').")

satt("kreation",
     "Plagg eller modell skapad av en modeskapare",
     "formell, neutral, mode",
     [],
     "Tidningen visade de senaste " + B % "kreationerna" + " från Paris.",
     None,
     "SO: 'modeskapelse' samt 'tolkning (av teaterroll)', bruk 'mindre "
     "brukligt'. SAOL har bara 'modeskapelse'. Modebetydelsen behalls "
     "ensam -- teaterbetydelsen ar markt mindre bruklig i SO och saknas "
     "helt i SAOL. VARNING mot forvaxling: ordet betyder INTE 'skapelse' i "
     "allman mening pa svenska, trots att engelskans creation gor det. Det "
     "ar en snavare modeterm.")

satt("malström",
     "Kraftig virvel i vattnet ; bildligt: något som drar med sig allt",
     "neutral, neutral ; neutral, negativ",
     ["virvelström"],
     "En " + B % "malström" + " av tankar for runt i huvudet på honom.",
     "→ Nederländska maalstroom, till malen 'virvla'.",
     "SO: 'kraftig virvelstrom', med 'av. bildligt' och exemplet 'en "
     "malstrom av tankar jagade runt i hjarnan'. SAOL: 'valdsam "
     "virvelstrom' -- 'virvelstrom' darmed belagd i definitionstexten. "
     "Bada betydelserna behalls; den bildliga far exempelmeningen eftersom "
     "det ar sa ordet oftast anvands i lopande text.")

satt("nubb",
     "Kort spik med platt huvud",
     "neutral, neutral",
     [],
     "Hon fäste tyget mot ryggstödet med " + B % "nubb" + ".",
     None,
     "SO: 'liten spik', med 'av. kollektivt' -- ordet anvands ofta utan "
     "plural-s ('med nubb'), vilket exempelmeningen foljer. SAOL: 'liten "
     "spik'. Wiktionary preciserar: 'kortare spik med platt huvud', vilket "
     "ar tagit in i definitionen eftersom det platta huvudet ar det som "
     "skiljer nubb fran stift. Inte att forvaxla med 'nubbe' (snaps), som "
     "ar ett annat ord.")

satt("osteoporos",
     "Benskörhet — skelettet blir poröst och går lätt av",
     "fackspråklig, neutral, medicin",
     ["benskörhet"],
     "Hon fick behandling mot " + B % "osteoporos" + " efter höftfrakturen.",
     "→ Grekiska osteon 'ben' och poros 'por' — ben fullt av hål.",
     "SO: 'benskorhet'. SAOL identisk. INGEN traff i SAOB -- ordet ar "
     "relativt sent (belagt sedan 1884). 'benskorhet' ar belagd synonym "
     "och star i definitionen, men foljs av en forklaring eftersom "
     "benskorhet i sig inte sager vad som faktiskt hander. Etymologin gor "
     "termen genomskinlig och ar darfor med.")

satt("pannå",
     "Inramat fält i en vägg eller dörr ; skiva som är preparerad att måla "
     "på",
     "fackspråklig, neutral, konst ; fackspråklig, neutral, konst",
     [],
     "Konstnären målade motivet på en " + B % "pannå" + " av ek i stället "
     "för på duk.",
     "→ Franska panneau — nära släkt med panel.",
     "SO ger bada: 'avgransat falt i panel, vagg eller dorr, som omges av "
     "nagon inramning' och 'skiva (av tra, papp eller dylikt) som ar "
     "preparerad for konstnarlig malning'. SAOL bekraftar bada. "
     "Wiktionary-hamtningen gav forst HTTP 429 och kordes om (HTTP 200) "
     "men gav inget innehall. JFR i SO: 'dorrspegel' -- struket, det ar "
     "en specifik sorts panna, inte en synonym.")

satt("patina",
     "Grön hinna som lägger sig på koppar med tiden ; vackert slitage som "
     "visar ålder",
     "neutral, neutral ; neutral, positiv",
     [],
     "Stadskärnan hade fått en " + B % "patina" + " som ingen nybyggnation "
     "kan härma.",
     None,
     "SO: 'gronfargad oxidbelaggning pa yta av kopparlegering' samt -- "
     "markt 'ofta bildligt' -- 'utseende som (pa ett tilltalande satt) "
     "vittnar om hog alder'. SAOL: 'oxidbelaggning pa kopparforemal; yta "
     "som aldrats vackert'. Bada betydelserna behalls. Det POSITIVA i den "
     "bildliga betydelsen ar avgorande: patina ar inte forfall, det ar "
     "slitage som klar ett foremal. Ordet ar oraknebart.")

satt("proselyt",
     "Nyvunnen anhängare av en tro eller en åsikt",
     "formell, neutral, religion",
     [],
     "Rörelsen skickade ut sina ivrigaste " + B % "proselyter" + " för att "
     "värva fler.",
     None,
     "SO: '(ny)vunnen anhangare av viss tro eller asikt', bruk 'ibland "
     "nagot ironiskt'. SAOL: 'nyvunnen anhangare'. Det avgorande i ordet "
     "ar NY -- en proselyt ar en nyomvand, inte vilken anhangare som "
     "helst, och nyomvanda beskrivs ofta som overdrivet ivriga (darav "
     "ironin SO noterar). Exempelmeningen bar den nyansen. Grekiska "
     "proselytos 'nykomling'.")

satt("ringhet",
     "Att vara liten och betydelselös",
     "ålderdomlig, neutral",
     [],
     "Boken är en samling tankar som jag i min " + B % "ringhet" + " har "
     "skrivit ner.",
     None,
     "SO: 'litenhet och obetydlighet' samt 'min obetydliga person', bruk "
     "'nagot alderdomligt'. INGEN traff i SAOL:s definitionstext utover "
     "hanvisning. Ordet lever i praktiken bara kvar i den sjalvutplanande "
     "frasen 'i min ringhet', som SO listar som eget exempel och som "
     "exempelmeningen darfor bygger pa. JFR i SO: 'ringa'. Belagt sedan "
     "1526.")

satt("seckla",
     "Dregla",
     "dialektal, neutral",
     ["dregla"],
     "Barnet låg och " + B % "secklade" + " i sömnen.",
     None,
     "SO: 'dregla', bruk 'dialektalt'. SAOL: 'dregla', bruk 'prov.' "
     "(provinsiellt). Wiktionary: 'dregla'. Alla tre kallor ger exakt "
     "samma enda ord -- ovanligt entydigt. Rakt synonympar; ordet ar en "
     "dialektal variant utan egen betydelsenyans. Belagt sedan 1677.")

satt("seeda",
     "Placera de bästa deltagarna så att de inte möts tidigt i en turnering",
     "fackspråklig, neutral, sport",
     [],
     "Förra årets segrare " + B % "seedades" + " som etta i turneringen.",
     "→ Engelska seed 'så, strö ut' — de bästa sprids i lottningen.",
     "SO: 'placera i rangordning efter formodad skicklighet' samt 'placera "
     "bland favoriterna'. SAOL: 'rangordna tavlande efter skicklighet; "
     "placera de basta i olika grupper'. INGEN traff i Wiktionary. "
     "Definitionen bygger pa SAOL:s andra led ('i olika grupper') eftersom "
     "det ar SYFTET som gor ordet begripligt -- man seedar for att de "
     "basta inte ska sla ut varandra i forsta omgangen, inte bara for att "
     "rangordna.")

satt("spaljé",
     "Glest galler av spjälor som växter får klättra på",
     "neutral, neutral",
     [],
     "Vinrankorna klättrade uppför " + B % "spaljén" + " längs husväggen.",
     None,
     "SO: 'stallning med spjalor eller nat till stod for hoga vaxter'. "
     "SAOL: 'spjalverk till stod for vaxter'. Wiktionary ger aven "
     "betydelsen 'hack (dubbel rad av soldater)' -- utelamnad, den saknas "
     "i bade SO och SAOL och ar en fransk militarterm. Via franska av "
     "italienska spalliera, till spalla 'skuldra'.")

satt("stenografi",
     "Snabbskrift där varje ljud skrivs med ett enkelt tecken",
     "fackspråklig, neutral",
     [],
     "Sekreteraren tecknade ner hela förhöret i " + B % "stenografi" + ".",
     "→ Grekiska stenos 'trång' och graphein 'skriva' — hoptryckt skrift.",
     "SO: 'ett system for snabbskrift dar varje bokstav i alfabetet "
     "motsvaras av ett lattskrivet tecken'. SAOL: 'typ av snabb handskrift "
     "med spec. tecken, delvis for hela ord'. Definitionen sager 'ljud' "
     "snarare an 'bokstav' -- SAOL:s tillagg om hela ord visar att "
     "systemet inte ar en ren bokstavsersattning. JFR i SO: "
     "'stenografera'.")

satt("telepati",
     "Tankeöverföring mellan människor utan något känt sätt att kommunicera",
     "neutral, neutral",
     ["tankeöverföring"],
     "Det verkade råda någon slags " + B % "telepati" + " mellan tvillingarna.",
     "→ Grekiska tele- 'fjärran' och pathos 'känsla' — känsla på avstånd.",
     "SO: 'overforing av tankar eller kanslor (fran en person till en "
     "annan) utan hjalp av kanda kommunikationsmedel'. SAOL: "
     "'tankeoverforing, tankelasning' -- 'tankeoverforing' darmed belagd "
     "synonym. Den avgorande delen av definitionen ar 'utan kanda "
     "kommunikationsmedel'; utan den blir ordet bara 'att forsta "
     "varandra'.")

satt("utkomst",
     "Det man försörjer sig på",
     "formell, neutral",
     ["uppehälle"],
     "Många sökte sin " + B % "utkomst" + " i grannländerna under krisåren.",
     None,
     "SO: 'mojlighet att fortjana pengar till sitt uppehalle'. SAOL: "
     "'bargning, uppehalle' -- 'uppehalle' darmed belagd synonym. JFR i "
     "SO: 'naring'. Wiktionarys ovriga betydelser ('avfard, avsked' samt "
     "'resultat, framgang') ar aldre och saknas i SO/SAOL -- utelamnade. "
     "Definitionen ar kortad till vardagssprak: forsorjning ar vad ordet "
     "handlar om.")

satt("vandel",
     "Hur någon lever sitt liv, sett ur moralisk synvinkel",
     "formell, neutral",
     ["levnadssätt"],
     "Tjänsten krävde att den sökande förde en hederlig " + B % "vandel" +
     ".",
     None,
     "SO: 'satt att leva sitt liv'. SAOL: 'uppforande, levnadssatt' -- "
     "'levnadssatt' darmed belagd. JFR i SO: 'leverne', 'uppforande'. "
     "Definitionen lagger till 'ur moralisk synvinkel' eftersom ordet "
     "nastan alltid star ihop med ett omdome ('hederlig vandel', "
     "'tvivelaktig vandel') och anvands i lagtext om lamplighetsprovning. "
     "Lever ocksa kvar i uttrycket 'handel och vandel'.")

satt("via",
     "Genom en plats på vägen ; med hjälp av någon eller något som "
     "förmedlar",
     "neutral, neutral ; neutral, neutral",
     [],
     "Hon fick veta det " + B % "via" + " en gemensam vän.",
     "→ Latin via 'väg' — samma ord som i viadukt och trivial.",
     "SO ger bada: 'langs en vag som loper genom' och 'genom formedling "
     "av, med hjalp av', den senare markt 'av. abstrakt'. SAOL: 'genom, "
     "over, forbi'. Wiktionary-hamtningen gav forst HTTP 429 och kordes om "
     "(HTTP 200). Den abstrakta betydelsen ar i dag den vanligaste och far "
     "exempelmeningen. JFR i SO: 'forbi', 'genom', 'over'.")

satt("väderbiten",
     "Solbränd och fårad i ansiktet av att ha varit mycket ute",
     "neutral, neutral",
     [],
     "En gammal " + B % "väderbiten" + " fiskare satt och lagade nät på "
     "bryggan.",
     None,
     "SO: 'solbrand och farad', med 'av. om foremal som utsatts for mycket "
     "sol och vind'. SAOL: 'farad i ansiktet'. Definitionen slar ihop "
     "bada och lagger till orsaken, eftersom ordet inte betyder "
     "solbrand i allmanhet utan barn av lang utomhusvistelse. "
     "Foremalsbetydelsen ('en vaderbiten gammal kyrka') ar utelamnad som "
     "mindre vanlig. Belagt sedan 1734.")

satt("välsituerad",
     "Som har det gott ställt ekonomiskt",
     "formell, neutral",
     ["välbärgad"],
     "Familjen var " + B % "välsituerad" + " och bodde i ett stort hus vid "
     "havet.",
     None,
     "SO: 'valbargad'. SAOL: 'valbestalld, formogen'. 'valbargad' ar SO:s "
     "hela definition och darmed belagd synonym, men duger inte som "
     "huvudbetydelse -- valbargad ar ett lika ovanligt ord. Definitionen "
     "sager darfor 'har det gott stallt ekonomiskt' med vardagsord. "
     "Wiktionary: 'smatt formogen'. Belagt sedan 1897.")

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("skrev %d av %d kort" % (sum(1 for k in KORT if k.get("proposed")),
                               len(KORT)))
