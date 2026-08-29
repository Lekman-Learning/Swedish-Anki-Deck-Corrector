# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch7, 20 kort. Full v3.

Reglerna som gäller, alla ur dagens 19 underkännanden:

1. SLÅ ALDRIG IHOP två betydelser som SO eller SAOL håller isär. Bevisbördan
   ligger hos mig för att de är samma, inte hos ordboken för att de är olika.
2. Synonym bara om ordet är utbytbart ÅT BÅDA HÅLLEN och inte är JFR-markerat
   i SO. En ordboksglosa är ofta en förklaring, inte ett utbytbart ord.
3. Ingen betydelse som bara Wiktionary har.
4. Facit styrs av definitionen — aldrig av etymologin eller av en synonym.
5. ETYMOLOGIFÄLTET RENDERAS PÅ KORTET och skrivs med full svenska. Bara
   sokkoll-slutsatsen är intern och får vara ASCII. Formerna på källspråken
   (fornsvenska, lågtyska, latin) behåller sin egen stavning.
"""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch7.json"
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


satt("glossarium",
     "Ordlista där svåra eller främmande ord förklaras eller översätts, ofta "
     "sist i en bok",
     "neutral, neutral, litteraturvetenskap",
     [],
     "Utgåvan har ett " + B % "glossarium" + " över alla fornsvenska ord.",
     "→ Medeltidslatin glossarium; till glosa.",
     "SO: 'ordsamling med oversattningar eller forklaringar'. SAOL: 'aldre "
     "ordlista med forklaringar'. SO:s JFR (lexikon, ordbok, ordlista) ar "
     "cohyponymmarkta och tas INTE upp som synonymer -- ett glossarium ar "
     "just den lilla ordlistan som hor till EN text, inte en fristaende "
     "ordbok, och det ar den skillnaden som gor ordet svart. OLD-facit "
     "'ordforteckning' suddar den.")

satt("skolios",
     "Sjuklig krökning av ryggraden åt sidan",
     "fackspråklig, neutral, medicin",
     ["snedrygg"],
     "Hon opererades för svår " + B % "skolios" + " som tonåring.",
     "→ Grekiska skolios 'krokig'.",
     "SO: 'sjuklig krokning i sidled av ryggraden', SYN-markt mot snedrygg "
     "-- darav synonymen, som ar den starkaste beviskategorin och klarar "
     "bada-hallen-provet. SO:s JFR kyfos ar cohyponym: kutryggighet, alltsa "
     "krokning BAKAT i stallet for i sidled, och den kontrasten ar just vad "
     "'i sidled' i facit bar. OLD-facit 'snedhet hos rygg' sager inte att "
     "det ar sjukligt eller at vilket hall.")

satt("bokstavstrogen",
     "Som följer förlagan ord för ord ; om en tolkning av en helig skrift: "
     "som tar texten precis som den står, utan att tolka den bildligt",
     "neutral, neutral, allmän ; neutral, neutral, religion",
     [],
     "En " + B % "bokstavstrogen" + " översättning som offrar flytet för "
     "exaktheten.",
     None,
     "SO ger TVA betydelser: 'som ord for ord overensstammer med forlaga' "
     "och 'praglad av bokstavstro' (SO:s exempel: en bokstavstrogen "
     "bibelsyn). Bada ar med, och de ar skilda: den forsta galler en "
     "oversattning eller en avskrift, den andra en hallning till en helig "
     "text. Belaggen ligger 32 ar isar (1881, 1913). OLD-facit 'ordagrann' "
     "tackte bara den forsta.")

satt("camembert",
     "Mjuk fransk dessertost med vit mögelhinna på utsidan",
     "neutral, neutral, matlagning",
     [],
     "En mogen " + B % "camembert" + " som rinner ut på tallriken.",
     "→ Franska camembert, efter Camembert, en stad i Normandie.",
     "SO: 'en fransk dessertost av vitmogeltyp'. SAOL: 'en dessertost'. "
     "Wiktionary preciserar 'mjuk' och 'med vitmogel', vilket ar med. "
     "OLD-facit 'vitmogelost' ar ratt men sager inte att den ar fransk "
     "eller mjuk -- och vitmogel ensamt skiljer den inte fran brie.")

satt("klenod",
     "Föremål som är så värdefullt att man vaktar det ; bildligt om en "
     "person som är ovärderlig för sin omgivning",
     "neutral, positiv, allmän ; neutral, positiv, allmän",
     [],
     "Familjebibeln var den förnämsta " + B % "klenoden" + " i dödsboet.",
     "→ Fornsvenska klenodh 'smycke'; av lågtyska kleinode, till kleine i "
     "betydelsen 'fin, sirlig'; samma rot som klen.",
     "SO: 'sarskilt vardefullt foremal', med underbetydelsen 'av. bildligt "
     "om person' (SO:s exempel: hans gamla hushallerska var en verklig "
     "klenod). Bada ar med -- personbetydelsen skulle ha fallit bort vid en "
     "hopslagning, och den ar den enda av de tva som anvands i talsprak. "
     "SAOL:s 'dyrbarhet' ar INTE upptaget som synonym: en dyrbarhet ar dyr, "
     "en klenod behover inte vara det (familjebibeln ar vardelos pa "
     "auktion). OLD-facit 'nagot vardefullt, dyrgrip' gjorde den "
     "forvaxlingen.")

satt("klåfingrig",
     "Som inte kan låta bli att peta på saker ; bildligt: som inte kan låta "
     "bli att ändra och lägga sig i sådant som inte angår en",
     "neutral, lätt negativ, allmän ; neutral, lätt negativ, allmän",
     [],
     "En " + B % "klåfingrig" + " lärare som rättade alldeles för mycket i "
     "uppsatserna.",
     "→ Till klå 'klia' och finger — fingrarna som kliar av lust att röra.",
     "SO: 'som inte kan lata bli att peta pa allt', med underbetydelsen "
     "'av. bildligt' (SO:s exempel: den klafingriga lararen). Bada ar med. "
     "Wiktionary skriver ut den bildliga: 'som lagger sig i saker for "
     "mycket'. OLD-facit 'som petar pa allt' hade bara den bokstavliga -- "
     "och det ar den bildliga som moter en i text om chefer och politiker.")

satt("kuperad",
     "Om landskap: fullt av höjder och dalar ; om djur: som fått en stor del "
     "av svansen eller öronen avskurna ; om kortlek: delad i två högar före "
     "given ; inom vården: om ett sjukdomsförlopp som avbrutits i tid",
     "neutral, neutral, allmän ; neutral, neutral, allmän ; neutral, "
     "neutral, allmän ; fackspråklig, neutral, medicin",
     [],
     "En boxer med " + B % "kuperad" + " svans.",
     "→ Franska couper 'skära av'; samma rot som kupé och kupp.",
     "SO ger FYRA betydelser: 'som har manga hojder och dalar', 'skara av "
     "en stor del av', 'lyfta av ovre halvan av' (kortleken) och 'forhindra "
     "eller avbryta ett sjukdomsforlopp'. Alla fyra ar med. SAOL bekraftar "
     "de tre forsta ('backig, kullig | stubba svans | blanda kortlek'). "
     "Frestelsen att sla ihop svans och kortlek ar stor -- bada handlar om "
     "att skara/dela -- men SO haller dem isar och det ar ordbokens "
     "avvagning som galler. SO:s JFR (backig, kullig) ar cohyponymmarkta. "
     "OLD-facit 'backig' tackte EN av fyra.")

satt("pascha",
     "Förr i Osmanska riket: titel för en hög ämbetsman ; i dag nästan alltid "
     "bildligt: person som låter andra passa upp på sig",
     "neutral, neutral, historia ; neutral, nedsättande, allmän",
     [],
     "Sedan han blev avdelningschef har han blivit en riktig " +
     B % "pascha" + ".",
     "→ Turkiska pasha.",
     "SO ger tva: '(titel for) person med hog befattning inom "
     "ambetsmannahierarkin' (markning: historiskt) och 'person som kraver "
     "uppassning eller betjaning av omgivningen' (markning: nedsattande, "
     "numera vanligen bildligt). Bada ar med, med respektive markning i "
     "registret. SO noterar ocksa att sammansattningen hederspascha har "
     "POSITIV vardering -- det ar en sammansattning och inte med har. "
     "OLD-facit 'uppassad person' hade bara den bildliga och missade "
     "titeln, som ar ordets ursprung.")

satt("selektiv",
     "Som bygger på ett noggrant urval i stället för att ta allt ; ironiskt "
     "om minne eller uppfattning: som bara plockar upp det som passar en "
     "själv",
     "fackspråklig, neutral, allmän ; neutral, ironisk, allmän",
     [],
     "Han har ett påfallande " + B % "selektivt" + " minne när det gäller "
     "egna löften.",
     "→ Till selektion; av latin seligere 'välja ut'.",
     "SO: 'som grundas pa noggrant utvaljande', med underbetydelserna "
     "'spec. av. i fraga om utvaljande som grundar sig pa valbestamda "
     "(matbara) egenskaper' och 'ibland ironiskt, med antydan om att "
     "utvaljandet styrs av nagons egna syften' (SO:s exempel: ett selektivt "
     "minne). Den ironiska ar en egen betydelse med egen laddning och ar "
     "med; den mattekniska underbetydelsen ar samma sak som huvudbetydelsen "
     "med en precisering och ar inte skild ut. SO markerar generell som "
     "MOTSATS, alltsa antonym. SAOL:s 'utvaljande; sarskiljande' ar inte "
     "upptaget som synonym -- de ar particip av verbet, inte utbytbara mot "
     "adjektivet. OLD-facit sa just 'utvaljande'.")

satt("adonis",
     "Ovanligt vacker ung man ; ibland nedsättande om en man som är mån om "
     "sitt utseende och charmar kvinnor ; en växt i ranunkelsläktet",
     "högtidlig, positiv, allmän ; neutral, nedsättande, allmän ; "
     "fackspråklig, neutral, biologi",
     [],
     "Han såg ut som en " + B % "adonis" + " men hade ingenting att säga.",
     "→ Efter Adonis, i grekisk myt en skön yngling som älskades av "
     "Afrodite.",
     "SO ger TRE betydelser: 'bildskon yngling' (markning: nagot "
     "hogtidligt), 'pigtjusare' (ibland nedsattande) och 'typ av "
     "ranunkelvaxt'. Alla tre ar med. SAOL bekraftar den forsta och "
     "vaxten. De tva forsta ligger nara varandra men har OLIKA laddning -- "
     "den forsta ar berom, den andra kan vara ett gliring -- och SO skiljer "
     "dem, sa de star som tva. OLD-facit 'vacker yngling' hade en av tre.")

satt("apologi",
     "Skrift eller tal som argumenterar till försvar för en person, en lära "
     "eller ett handlande",
     "formell, neutral, allmän",
     [],
     "Hennes memoarer är egentligen en enda lång " + B % "apologi" + ".",
     "→ Grekiska apologia 'försvarstal'.",
     "SO: 'argumenterande forsvar', med underbetydelsen 'av. om liknande "
     "inlagg eller dylikt' -- den ar samma sak i en annan form och ar inte "
     "skild ut. SAOL: 'forsvar; forsvarstal, forsvarsskrift'. Ordet "
     "ARGUMENTERANDE ar avgorande och ar med: en apologi ar inte att bara "
     "forsvara sig utan att lagga fram skal. OLD-facit 'forsvarstal' "
     "utesluter skriften, som ar den vanligaste formen (SO:s eget exempel "
     "handlar om memoarer).")

satt("astigmatism",
     "Fel i en lins som gör att bilden blir suddig, vanligast som ett fel i "
     "ögats hornhinna",
     "fackspråklig, neutral, medicin",
     [],
     "Konstnären El Greco tros ha lidit av " + B % "astigmatism" + ".",
     "→ Grekiska a- 'icke' och stigme 'punkt' — strålarna samlas inte i en "
     "punkt.",
     "SO: 'ett avbildningsfel hos en lins eller en spegel'. SAOL: "
     "'bristande sammanbrytning av ljusstralar genom lins(er), t.ex. i "
     "ogat'. Wiktionary: 'gor att en bild blir oklar'. Facit ar byggt av "
     "alla tre: felet, foljden (suddig bild) och det vanligaste stallet "
     "(ogat). Ordet 'hornhinna' ar med eftersom det ar dar felet nastan "
     "alltid sitter -- SAOL sager 'i ogat', vilket ar oprecist. OLD-facit "
     "'brytningsfel, t.ex i ogat' stammer i sak.")

satt("damejeanne",
     "Stor bukig glasflaska, ofta klädd i flätad korg för att tåla "
     "transport",
     "neutral, neutral, allmän",
     [],
     "Vinet jäste i en " + B % "damejeanne" + " i källaren.",
     "→ Franska dame-jeanne, troligen skämtsamt 'fru Johanna' — flaskans "
     "form liknades vid en bastant kvinna.",
     "SO: 'stor bukig glasflaska'. SAOL lagger till 'i korg ofta for "
     "transport av vin' och Wiktionary 'med skydd av flatverk' -- bada "
     "preciseringarna ar med, eftersom korgen ar det som skiljer en "
     "damejeanne fran vilken stor flaska som helst. SO:s JFR butelj ar "
     "jamforelsemarkt. OLD-facit 'stor korgflaska' hade korgen men inte "
     "att den ar av glas och bukig.")

satt("expropriera",
     "Tvinga en ägare att sälja sin mark eller egendom till staten eller "
     "kommunen, mot ersättning",
     "fackspråklig, neutral, juridik",
     [],
     "Gården " + B % "exproprierades" + " på 1960-talet och nu går "
     "motorvägen tvärs över ägorna.",
     "→ Till latin ex 'från' och proprius 'egen, tillhörig någon privat'; "
     "samma rot som proper.",
     "SO:s definition ar cirkular: 'utfora expropriation av'. SAOL ger "
     "innehallet: 'tvangsinlosa egendom (for statens el. kommuns rakning)', "
     "och facit ar byggt darifran enligt Adam-tal. ERSATTNINGEN ar med "
     "eftersom den ar det juridiska kannetecknet -- expropriation ar inte "
     "konfiskation. OLD-facit 'tvangsinkopa egendom' vander pa rollerna: "
     "det ar staten som koper, agaren som tvingas salja.")

satt("försynt",
     "Som håller sig i bakgrunden och inte tar plats på andras bekostnad ; "
     "också om en handling som görs på det sättet",
     "neutral, positiv, allmän ; neutral, positiv, allmän",
     [],
     "Ett " + B % "försynt" + " påpekande som ingen behövde ta illa upp av.",
     None,
     "SO: 'som tonar ner den egna personligheten', med underbetydelsen 'av. "
     "om handling eller dylikt' (SO:s exempel: ett forsynt papekande, en "
     "forsynt knackning pa dorren). Bada ar med. Wiktionary lagger till 'pa "
     "ett tilltalande satt', vilket motiverar den positiva valensen. SO:s "
     "JFR (diskret, modest, timid) ar cohyponymmarkta och tas INTE upp: "
     "timid ar radsla, forsynthet ar hansyn, och det ar precis den sortens "
     "narsynonym som satter dit folk. OLD-facit 'hansynsfull, blygsam, "
     "diskret' var en sadan rad.")

satt("lapidarstil",
     "Den knappa stil som användes i inskrifter huggna i sten ; kortfattat "
     "men träffande sätt att uttrycka sig",
     "fackspråklig, neutral, historia ; neutral, positiv, "
     "litteraturvetenskap",
     ["stenstil"],
     "Han skrev i en " + B % "lapidarstil" + " där varje mening bar sin "
     "egen tyngd.",
     "→ Till latin lapis 'sten'.",
     "SO ger tva: '(stil som anvandes pa) inskrift i sten' (markning: mest "
     "historiskt) och 'kortfattat men traffande uttryckssatt'. Bada ar med "
     "-- den andra ar den enda som anvands i dag, men den forsta forklarar "
     "VARFOR stilen ar knapp: det kostar att hugga i sten. Stenstil ar "
     "SYN-markt i SO och duger darfor som synonym. OLD-facit sa just "
     "'stenstil', vilket ar ratt men lika ovanligt som uppslagsordet.")

satt("manipulera",
     "Hantera ett föremål eller en apparat med skickliga händer ; styra "
     "människor i en riktning de inte märker, med dolda knep",
     "neutral, neutral, allmän ; neutral, negativ, allmän",
     [],
     "Väljarna " + B % "manipuleras" + " lätt av smarta politiker.",
     "→ Franska manipuler 'bearbeta, hantera'; till latin manipulus "
     "'handfull', till manus 'hand'; samma rot som manikyr.",
     "SO ger tva: 'hantera (apparat eller dylikt) kansligt' och 'otillborligt "
     "styra (manniskor) med hjalp av diskreta knep'. Bada ar med, och det ar "
     "en verklig fälla: den forsta ar helt NEUTRAL (SO:s exempel: han stod "
     "och manipulerade med laset) medan den andra ar klart negativ. "
     "Belaggen ligger over hundra ar isar (1845, 1950). OLD-facit "
     "'paverka' tackte varken den ena eller den andra -- det saknar bade "
     "handerna och ohederligheten.")

satt("meander",
     "Kraftig slinga i ett vattendrag, som floden själv format genom att "
     "gröpa ur ytterkurvan ; bård i form av ett labyrintliknande band, känd "
     "från grekisk konst",
     "fackspråklig, neutral, geologi ; fackspråklig, neutral, konst",
     [],
     "Floden slingrar sig i breda " + B % "meandrar" + " över slätten.",
     "→ Efter Maiandros, grekiskt namn på en starkt slingrande flod i Mindre "
     "Asien.",
     "SO ger tva helt oberoende betydelser: 'kraftigt markerad slinga i "
     "flodlopp' och 'ornament i form av labyrintliknande band'. Bada ar med "
     "-- ornamentet skulle ha fallit bort vid en hopslagning, och det ar "
     "det man moter pa grekiska vaser och i arkitektur. HUR slingan bildas "
     "kommer fran Wiktionary ('erosion i ytterkurvorna') och ar med "
     "eftersom SO:s ord ensamt inte forklarar nagot. SO:s JFR alagreck ar "
     "cohyponym. OLD-facit 'flodslinga' hade en av tva.")

satt("sekretess",
     "Att uppgifter enligt beslut eller lag inte får lämnas ut ; skyldigheten "
     "för den som fått veta något att inte föra det vidare",
     "fackspråklig, neutral, juridik ; fackspråklig, neutral, juridik",
     [],
     "Kuratorn ålades " + B % "sekretess" + " om allt som sagts i rummet.",
     "→ Äldre franska secretesse, till secret 'hemlig'; samma rot som "
     "sekret och sekretion.",
     "SO ger tva: 'pabjudet hemlighallande' och 'tystnadsplikt'. Bada ar "
     "med, och skillnaden ar vem regeln traffar: den forsta galler "
     "UPPGIFTEN (den ar hemligstamplad), den andra PERSONEN (hen far inte "
     "beratta). SAOL bekraftar bada. OLD-facit 'tystnadsplikt' hade bara "
     "den andra -- alltsa halva ordet, och det ar den forsta som avses nar "
     "nagot 'belaggs med sekretess'.")

satt("spinal",
     "Som har med ryggmärgen eller ryggraden att göra",
     "fackspråklig, neutral, medicin",
     [],
     B % "Spinal" + " muskelatrofi är en ärftlig sjukdom i ryggmärgen.",
     "→ Latin spina 'ryggrad, tagg'.",
     "SO: 'som har att gora med ryggmarg eller ryggrad'. SAOL: 'ryggmargs-, "
     "ryggrads-'. Bada leden ar med -- OLD-facit 'har att gora med ryggrad' "
     "utelamnade RYGGMARGEN, som ar det ordet oftast syftar pa i medicinska "
     "sammansattningar (spinal anestesi, spinal muskelatrofi). Ryggraden ar "
     "benet, ryggmargen ar nerven inuti, och sammanblandningen ar hela "
     "svarigheten.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("skrev %d kort" % sum(1 for k in KORT if k.get("approved")))
