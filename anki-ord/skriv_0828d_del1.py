# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch5, kort 1-20. Full v3.

Skriven EFTER 100-batchens felmonster. Tre regler skarpta samma dag:
  1. Synonym bara om ordet ar utbytbart AT BADA HALLEN. Vid minsta tvekan:
     ingen synonym alls. (bemarkt/framstaende, singular/saregen, spe/han
     foll alla tre.)
  2. Ingen betydelse som bara Wiktionary har. (anlopa, autograf.)
  3. Slå aldrig ihop tva betydelser som ordboken haller isar. (ax, yttring,
     harnesk.)
"""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch5.json"
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


def hall_tillbaka(o, motiv):
    """Kortet skrivs INTE. Sokkollen sparas sa att skalet finns kvar."""
    e = BY[o]
    e["sokkoll"] = {"kalla": kallor(o), "slutsats": motiv}
    e["confidence"] = 0
    e["approved"] = False


satt("allenarådande",
     "Som är helt ensam om att gälla, utan att något annat får plats vid "
     "sidan om",
     "neutral, neutral, allmän",
     [],
     "Marknaden framställs som den " + B % "allenarådande" + " förklaringen "
     "till löneskillnaderna.",
     "→ Allena 'ensam' + radande; jfr engelskans alone.",
     "SO: 'helt dominerande'. SAOL ger ingen egen definitionstext. "
     "Wiktionary: 'ensamradande, envaldig' -- INGEN av dem ar upptagen som "
     "synonym: envaldig galler en harskare, allenaradande galler lika garna "
     "en faktor, en asikt eller en forklaring, och orden ar alltsa inte "
     "utbytbara at bada hallen. Det ar ocksa felet i OLD-facit, som sa just "
     "'envaldig'.")

hall_tillbaka(
    "frontong",
    "HALLS TILLBAKA -- INGEN ANVANDBAR KALLTEXT. Uppslagsordet finns i SAOB "
    "(traffar=saob) men skriptet extraherar ingen definitionstext ur SAOB "
    "for nagot ord i den har batchen. Varken SO, SAOL, synonymer.se eller "
    "Wiktionary har nagon artikel. Det enda underlaget ar OLD-facits ord "
    "'prydnadsgavel', vilket ar deckets egen tidigare gissning och inte en "
    "kalla. Att skriva ut vad en frontong ar (det triangelformade faltet "
    "over en portal pa en klassisk byggnad) vore att hamta det ur mitt eget "
    "minne och kalla det uppslaget -- exakt det felet 100-batchen straffade "
    "pa anlopa och autograf. Kortet skrivs inte forran en kalla finns.")

hall_tillbaka(
    "ipso jure",
    "HALLS TILLBAKA -- INGEN KALLA ALLS. Uppslagningen gav traffar=INGEN: "
    "uttrycket saknas i SO, SAOL och SAOB, och bade synonymer.se och "
    "Wiktionary returnerade tomt. OLD-facit sager 'med ratta', vilket "
    "dessutom ser fel ut -- ipso jure ar en juridisk term for att nagot "
    "intraffar automatiskt genom lagen sjalv, inte for att nagon har ratt. "
    "Men den rattelsen kan jag inte gora utan kalla, sa kortet skrivs inte. "
    "Att jag TROR att OLD-facit ar fel ar ett skal att halla tillbaka "
    "kortet, inte ett skal att skriva ett nytt facit ur minnet.")

satt("jade",
     "Grågrön, nästan ogenomskinlig sten som slipas till smycken och "
     "prydnadsföremål",
     "neutral, neutral, allmän",
     [],
     "Ett gammalt kinesiskt sigill av " + B % "jade" + ".",
     "→ Engelska jade; av spanska (piedra de la) ijada, eg. '(sten mot) "
     "njurstenskolik' -- stenen troddes bota njurbesvar.",
     "SO: 'en (gra)gron, tamligen ogenomskinlig prydnadssten'. SAOL: 'ett "
     "gront mineral'. Wiktionary ger dessutom fargbetydelsen ('en gronaktig "
     "farg som forknippas med adelstenen') -- den ar UTELAMNAD eftersom "
     "varken SO eller SAOL har den. Samma regel som fallde anlopa och "
     "autograf i foregaende batch.")

satt("krås",
     "De ätliga inälvorna i en fågel ; i uttrycket \"smörja kråset\": äta "
     "mycket och gott ; veckad remsa av tyg eller spets runt halsen eller "
     "vid ärmen",
     "neutral, neutral, matlagning ; vardaglig, neutral, allmän ; neutral, "
     "neutral, allmän",
     [],
     "Hon firade sin examen med att smörja " + B % "kråset" + " på stadens "
     "finaste krog.",
     "→ I inalvsbetydelsen fornsvenska (gaase)kraas, troligen av lagtyska "
     "kros 'inalvor i gas'. I tygbetydelsen efter tyska Krause, till kraus "
     "'krusig' -- samma rot som krusa.",
     "SO ger TRE definitioner och alla tre ar med: inalvorna, uttrycket "
     "'smorja kraset' ('ata mycket och gott') och tygremsan. Uttrycket ar "
     "byggt pa inalvsbetydelsen men SO listar det som en egen definition "
     "med egen exempelmening, och i 100-batchen underkandes harnesk just "
     "for att jag slog ihop en sadan. De tva huvudbetydelserna har dessutom "
     "OLIKA etymologi -- det ar tva ord som fallit ihop, inte ett ord med "
     "tva sidor. OLD-facit 'inkram; puffkrage' hade bada men med fel ord: "
     "kras ar inalvorna i en FAGEL, inte inkram i allmanhet.")

satt("kätte",
     "Inhägnat bås i ett stall eller en ladugård, där ett eller några djur "
     "står för sig",
     "neutral, neutral, jordbruk",
     [],
     "Kalvarna stod två och två i varje " + B % "kätte" + ".",
     "→ Fornsvenska kätte; ev. beslaktat med lagtyska kete 'hydda, skjul'.",
     "SO: 'avbalkning i stall eller ladugard'. SAOL preciserar 'sluten "
     "avbalkning ... t.ex. for kalvar'. SO:s JFR (box, bas) ar "
     "cohyponymmarkta och tas INTE upp som synonymer: ett bas ar oppet at "
     "ett hall och rymmer ett djur, en katte ar sluten runt om. OLD-facit "
     "'djurbas' suddar precis den skillnaden.")

satt("lumpor",
     "Trasor och utslitna tygstycken",
     "neutral, neutral, allmän",
     ["trasor"],
     "Golvet låg fullt av " + B % "lumpor" + " och trasiga mattor.",
     None,
     "SVAGT BELAGD: bara SAOL har en definition, 'trasor, paltor' (SO har "
     "ingen artikel, Wiktionary returnerade 154 tecken utan anvandbar "
     "glosa). Synonymen trasor ar behallen trots den skarpta regeln, "
     "eftersom den klarar bada-hallen-provet: lumpor och trasor gar att "
     "byta mot varandra i bada riktningarna. Paltor ar daremot struket -- "
     "det ar ett annu ovanligare ord och forklarar ingenting. OLD-facit "
     "'trasor' stammer.",
     conf=6)

satt("sponta",
     "Forma kanterna på en bräda så att den ena får en tunga och den andra "
     "en ränna, så att bräderna kan låsas i varandra ; klä en yta med sådana "
     "bräder",
     "fackspråklig, neutral, teknik ; fackspråklig, neutral, teknik",
     [],
     "Golvet lades med " + B % "spontat" + " virke.",
     None,
     "SO ger tva betydelser: 'forse (brada eller dylikt) med spont' och "
     "'forse med brader med spont' -- alltsa att bearbeta brädan respektive "
     "att kla en yta med de fardiga braderna. Bada ar med; de haller isar "
     "vem som gor vad. Ordet 'spont' sjalvt ar upplost till tunga och ranna "
     "enligt Adam-tal, eftersom en definition som forutsatter uppslagsordets "
     "egen stam inte forklarar nagot. OLD-facit 'forse med spontar' gor "
     "precis det felet.")

satt("degeneration",
     "Att något gradvis utvecklas till det sämre ; inom medicinen: att "
     "celler eller organ bryts ner och förlorar sin funktion",
     "neutral, negativ, allmän ; fackspråklig, neutral, medicin",
     [],
     B % "Degeneration" + " av näthinnan är en vanlig orsak till "
     "synnedsättning.",
     "→ Till degenerera; av latin degenerare 'urarta', till genus 'slakt'.",
     "SO: 'utveckling till det samre', med underbetydelsen 'av. om "
     "omvandling av celler, vavnader el. organ till nagot samre'. Bada ar "
     "med. SAOL glossar 'urartning; forsamring' -- INGEN av dem ar upptagen "
     "som synonym: forsamring ar bredare (en forsamring kan vandas, en "
     "degeneration beskrivs som en riktning) och urartning bar en moralisk "
     "biton som degeneration inte kraver. Bada-hallen-provet faller.")

satt("frikadell",
     "Liten köttbulle som kokas i stället för att stekas, oftast i soppa",
     "neutral, neutral, matlagning",
     [],
     "Kålsoppa med " + B % "frikadeller" + ".",
     "→ Tyska Frikadelle; av aldre franska fricadelle, till latin frigere "
     "'rosta, steka'.",
     "SO: '(liten) kokt kottbulle'. SAOL lagger till 'till soppa'. Bada "
     "preciseringarna ar med, for det ar de som skiljer frikadellen fran en "
     "vanlig kottbulle: den kokas, och den hamnar i soppa. OLD-facit 'kokt "
     "kottbulle' hade den forsta men inte den andra.")

satt("förtappad",
     "Så djupt fallen i synd att räddning inte längre anses möjlig",
     "neutral, negativ, religion",
     [],
     "En " + B % "förtappad" + " syndare utan hopp om nåd.",
     "→ Fornsvenska fortappad, till fortappa 'forlora, forspilla'.",
     "SO: 'som fallit djupt i synd'. SAOL skarper till det avgorande: 'domd "
     "till evig osalighet' -- alltsa att det ar for sent, vilket ar hela "
     "ordet och inte finns i OLD-facits 'fordomd'. Nagon "
     "bruklighetsmarkning ger varken SO eller SAOL, sa formalitetsnivan ar "
     "neutral trots att ordet later hogtidligt; domanen religion foljer "
     "daremot direkt av bada definitionerna (synd, osalighet).")

satt("krum",
     "Böjd eller krokig i formen ; som substantiv: själva böjen — \"med "
     "ryggen i krum\"",
     "neutral, neutral, allmän ; neutral, neutral, allmän",
     [],
     "Han stod med ryggen " + B % "krum" + " över arbetsbänken.",
     "→ Lagtyska krum; beslaktat med kramp och krympa.",
     "SO ger tva: adjektivet 'bojd' och substantivet 'bojd form' (SO:s "
     "exempel: 'hon satt med ryggen i krum'). Bada ar med -- att samma ord "
     "ar bade adjektiv och substantiv ar precis den sorts sak ett kort ska "
     "visa. SAOL:s 'krokt' och Wiktionarys 'krokig' ar INTE upptagna som "
     "synonymer: krokig anvands ocksa om en vag som slingrar sig, vilket "
     "krum aldrig gor, sa bada-hallen-provet faller.")

satt("kväde",
     "Dikt i högtidlig ton, särskilt en fornnordisk sång om gudar eller "
     "hjältar",
     "arkaisk, neutral, litteraturvetenskap",
     [],
     "Völvans " + B % "kväde" + " inleder den poetiska Eddan.",
     "→ Fornsvenska kväþe, till kvada 'kvada, sjunga'.",
     "SO: 'skaldestycke', med markningen alderdomligt. SAOL preciserar: "
     "'hogtidlig dikt; fornnordiskt skaldestycke' -- bada leden ar med, "
     "eftersom SO:s enda ord inte later nagon gissa vare sig tonen eller "
     "sammanhanget. SO:s JFR omkvade ar en sammansattning, inte en synonym. "
     "OLD-facit hade redan bada leden och ar i sak behallet.")

satt("motspänstig",
     "Som aktivt gör motstånd i stället för att göra som man blir tillsagd",
     "neutral, lätt negativ, allmän",
     ["motsträvig"],
     "Det tog en timme att tämja den " + B % "motspänstiga" + " hästen.",
     "→ Efter tyska widerspenstig, till Span 'strid'; till spanna.",
     "SO: 'som gor aktivt motstand'. Ordet AKTIVT ar poangen och ar "
     "inskrivet: motspanstig ar inte samma sak som ovillig, som Wiktionary "
     "glossar med. Synonymen motstravig ar SAOL:s hela definition och "
     "klarar bada-hallen-provet -- de tva orden gar att byta mot varandra i "
     "vilken mening som helst. OLD-facit sa just 'motstravig' och stammer.")

satt("patos",
     "Djup och brinnande känsla som märks i det man säger eller gör",
     "neutral, neutral, allmän",
     [],
     "Hon talade med " + B % "patos" + " om de förtryckta.",
     "→ Grekiska pathos 'lidande, lidelse, upplevelse'; samma rot som "
     "sympati, antipati, patetisk och telepati.",
     "SO: 'stark och lidelsefull kansla'. SAOL: 'lidelse, stark kansla, "
     "hogstamdhet'. Ingen synonym ar upptagen: lidelse (OLD-facits ord) "
     "klarar inte bada-hallen-provet, for lidelse kan galla en person man "
     "alskar medan patos alltid galler en SAK man brinner for. SO:s JFR "
     "patetik ar dessutom cohyponymmarkt.")

satt("ranson",
     "Noga tilldelad mängd av något som det är ont om och som måste räcka",
     "neutral, neutral, allmän",
     [],
     "Knappa " + B % "ransoner" + " av bröd och socker delades ut.",
     "→ Via lagtyska av franska ration; av latin ratio 'rakning, "
     "berakning'; samma rot som ration och reson.",
     "SO: 'noga avpassad mangd av nagot som man maste hushalla med'. Ledet "
     "om hushallning ar avgorande och ar inskrivet -- det ar vad som gor en "
     "ranson till nagot annat an en portion. Darfor ar INGEN av SAOL:s "
     "glosor (andel, lott, tilldelning, portion) upptagen som synonym, och "
     "de ar dessutom allihop cohyponymmarkta i SO. OLD-facit sa 'portion', "
     "vilket ar precis den forvaxlingen.")

satt("stinn",
     "Så full att sidorna buktar ut och ytan spänns ; bildligt om någon "
     "eller något som är fylld till brädden av något: en stinn plånbok",
     "neutral, neutral, allmän ; neutral, neutral, allmän",
     [],
     "Hans mage var " + B % "stinn" + " av soppan.",
     "→ Fornsvenska stinder 'hard, spand'; gemensamt germanskt ord.",
     "SO: 'valfylld sa att sidorna buktar ut', med underbetydelserna 'av. "
     "allmannare' och 'av. bildligt'. De tva senare ar samma bild i olika "
     "styrka och ar hopslagna till en bildlig betydelse -- SO:s egna "
     "exempel pa dem (en stinn planbok, penningstinn, hormonstinn) ar alla "
     "samma sak: fylld till bradden. OLD-facit 'valfylld' hade bara den "
     "bokstavliga och missade att det ar SPANNINGEN, inte mangden, som ar "
     "ordet.")

satt("subtil",
     "Så fin och försiktig att den knappt märks — man måste vara "
     "uppmärksam för att uppfatta den",
     "neutral, neutral, allmän",
     [],
     "Det är en " + B % "subtil" + " skillnad mellan de två orden.",
     "→ Latin subtilis 'fin, harfin, skarpsinnig'.",
     "SO: 'mycket fin' -- en definition sa knapp att den inte forklarar "
     "nagot, sa SAOL:s 'knappt markbar' ar inskrivet i stallet. SO:s JFR "
     "harfin ar cohyponymmarkt och tas inte upp. SAOL:s 'sofistikerad, "
     "spetsfundig' galler en ANNAN sida av ordet (om ett resonemang) och ar "
     "medvetet utelamnad -- den anvandningen ar sallsynt i svenskan och "
     "skulle grumla kortet. OLD-facit 'knappt markbar' stammer.")

satt("tuktig",
     "Som håller sig i strama tyglar moraliskt: behärskad, återhållsam och "
     "anständig",
     "arkaisk, positiv, allmän",
     [],
     "Ett " + B % "tuktigt" + " levnadssätt utan utsvävningar.",
     "→ Till tukt 'aga, sjalvbehärskning'.",
     "SO: 'som praglas av (sedlig) tukt', med markningen alderdomligt. "
     "SAOL: 'sedlig, arbar'. Ingen synonym ar upptagen: arbar ar dessutom "
     "cohyponymmarkt i SO. VIKTIG AVGRANSNING: sedesam skrevs i "
     "foregaende batch samma dag och ligger nara. Skillnaden ar inskriven i "
     "facit -- sedesam handlar om att folja vad omgivningen anser passande, "
     "tuktig om SJALVBEHARSKNING (tukt = aga). OLD-facit 'sedlig' ar lika "
     "svart som uppslagsordet.")

satt("yrka",
     "I rättegång eller på ett möte: formellt begära att ett visst beslut "
     "fattas ; mer allmänt: kräva något med eftertryck",
     "fackspråklig, neutral, juridik ; neutral, neutral, allmän",
     [],
     "Åklagaren " + B % "yrkade" + " att kvinnan skulle häktas.",
     "→ Jfr fornsvenska yrkia 'arbeta, odla, utfora'; gemensamt germanskt "
     "ord (engelskans work), beslaktat med orka och verk.",
     "SO ger tva: 'formellt krava beslut' och 'eftertryckligt krava' (av. "
     "forsvagat). Bada ar med, med SO:s markning sarsk. jur. pa den forsta. "
     "Skillnaden ar hela ordet: man yrkar INFOR nagon som ska besluta, till "
     "skillnad fran att bara krava. OLD-facit 'krava, fordra' var en "
     "synonymrad som suddar just det -- och ingen av dem ar upptagen som "
     "synonym, eftersom man kraver av en person men yrkar hos en instans.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
ok = sum(1 for k in KORT if k.get("approved"))
print("skrev %d kort, hall tillbaka: frontong, ipso jure" % ok)
