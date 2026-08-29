# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch5, kort 21-40. Full v3. Samma skarpta regler
som del1 -- se dess docstring."""
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


satt("blåställ",
     "Omgång blå överdragskläder som man drar på sig över de vanliga för "
     "kroppsarbete ; bildligt: att kavla upp ärmarna och slita",
     "neutral, neutral, allmän ; neutral, neutral, allmän",
     [],
     "I bortamatchen fick laget dra på sig " + B % "blåstället" + " och "
     "jobba.",
     None,
     "SO: 'omgang blaa overdragsklader for kroppsarbete', med "
     "underbetydelsen 'ofta bildligt i uttryck for hart arbete' -- och SO:s "
     "ENDA exempelmening ar den bildliga (bortamatchen). Bada ar med. "
     "OLD-facit 'arbetsklader' hade bara den bokstavliga och missade "
     "dessutom att plagget dras UTANPA de vanliga klaerna, vilket ar vad "
     "'overdragsklader' betyder. SO:s JFR blaklader ar en sammansattning.")

satt("distorsion",
     "Ledskada som uppstår när en led tvingas röra sig åt fel håll ; "
     "förvrängning av en bild eller ett ljud när det förs över",
     "fackspråklig, neutral, medicin ; fackspråklig, neutral, teknik",
     [],
     "Det var för mycket " + B % "distorsion" + " i högtalarna.",
     "→ Latin distorsio 'vridning isar'; samma rot som torsion.",
     "SO ger tva helt oberoende betydelser: ledskadan och forvrangningen "
     "vid overforing. SAOL bekraftar bada ('forvridning el. forvrangning av "
     "bild el. ljud; vrickning av led'). OLD-facit 'forvrangning' hade bara "
     "den ena -- och det ar den medicinska som ar aldst (belagd 1860 mot "
     "1906). Wiktionarys tredje betydelse (linsfel som gor raka linjer "
     "bojda) ar en underart av forvrangningen och ar inte skild ut.")

satt("entlediga",
     "Skilja någon från en tjänst eller ett uppdrag ; också: bevilja någon "
     "det avsked som hen själv har bett om",
     "formell, neutral, allmän ; formell, neutral, allmän",
     [],
     "Hon " + B % "entledigades" + " på egen begäran från sitt uppdrag.",
     "→ Tyska entledigen, till ledig 'fri'.",
     "SO ger tva: 'avskeda' och 'bevilja avsked eller befrielse', med "
     "markningen nagot formellt. Bada ar med, och skillnaden ar hela "
     "poangen: i den forsta ar det arbetsgivaren som vill bli av med "
     "personen, i den andra ar det personen sjalv som bett om att fa ga. "
     "SO:s tva exempel visar precis det ('p.g.a. forskingring' mot 'pa egen "
     "begaran'). OLD-facit 'avskeda' hade bara den forsta, vilket gor "
     "ordet entydigt negativt -- det ar det inte.")

satt("etyd",
     "Musikstycke skrivet för att öva upp en bestämd teknisk färdighet ; "
     "också om ett sådant stycke som är så krävande att det spelas på "
     "konsert",
     "fackspråklig, neutral, musik ; fackspråklig, neutral, musik",
     [],
     "Hon övade Chopins " + B % "etyder" + " varje morgon.",
     "→ Franska étude 'studie'; av latin studium -- samma ord som studium.",
     "SO: 'musikaliskt ovningsstycke', med underbetydelsen 'av. om tekniskt "
     "kravande konsertstycke'. Bada ar med -- Chopins etyder ar just det "
     "gransfallet, och det ar darfor exempelmeningen ar vald sa. OLD-facit "
     "'ovningsstycke i musik' hade bara den forsta. Ledet 'en bestamd "
     "teknisk fardighet' ar inskrivet eftersom det ar vad som skiljer en "
     "etyd fran vilket ovningsstycke som helst.")

satt("extravagant",
     "Så påkostad och överdådig att den visar upp rikedom ; också om ett "
     "beteende som går långt utöver det vanliga",
     "neutral, neutral, allmän ; neutral, lätt negativ, allmän",
     [],
     "Hans " + B % "extravaganta" + " klädsel drog blickarna till sig.",
     "→ Franska extravagant 'overdriven, besynnerlig'; till extra och latin "
     "vagari 'vandra omkring' -- samma rot som vag och vagabond.",
     "SO: 'som ger intryck av rikedom', med underbetydelsen 'av. om "
     "handling eller dylikt'. Bada ar med. SAOL:s 'overdadig; overdriven' "
     "ar INTE upptagna som synonymer: overdadig sager ingenting om vem som "
     "ser pa, medan SO:s definition uttryckligen handlar om vilket INTRYCK "
     "det ger -- bada-hallen-provet faller. OLD-facit 'overdadig och lyxig' "
     "var en sadan synonymrad.")

satt("frondera",
     "Öppet sätta sig upp mot dem som bestämmer, inifrån den egna gruppen",
     "neutral, neutral, politik",
     [],
     "En fraktion " + B % "fronderade" + " mot partistyrelsen.",
     "→ Franska fronder, eg. 'slunga', till fronde 'en slunga'; av latin "
     "funda 'slunga'.",
     "SO: 'oppet opponera sig'. SAOL: 'opponera, visa missnoje'. Ledet "
     "'inifran den egna gruppen' ar inskrivet ur SO:s exempelmening (en "
     "fraktion mot sin egen partistyrelse) -- det ar vad som skiljer "
     "frondera fran att opponera sig i allmanhet, och just darfor ar "
     "opponera INTE upptaget som synonym trots att det star i bada "
     "definitionerna. OLD-facit sa 'opponera' och gor den forvaxlingen.")

satt("globetrotter",
     "Person som reser runt i världen, ofta och överallt",
     "neutral, neutral, allmän",
     [],
     "Han är en riktig " + B % "globetrotter" + " som varit i över nittio "
     "länder.",
     "→ Engelska globetrotter, till globe 'jordklot' och trot 'trava, "
     "lunka'; samma rot som glob, foxtrot och trottoar.",
     "SO: 'person som reser runt hela jordklotet'. SAOL: 'vittberest "
     "person, jordenruntresenar'. OLD-facit sa 'jordenruntresenar', vilket "
     "ar SAOL:s ord men for smalt: en jordenruntresa ar EN resa, en "
     "globetrotter ar nagon som reser standigt. Ordet ar darfor inte "
     "upptaget som synonym.")

satt("harm",
     "Vrede som väcks av att något är moraliskt orätt",
     "neutral, negativ, allmän",
     ["indignation"],
     "Hans hånfulla ord väckte allmän " + B % "harm" + ".",
     "→ Runform harmi, fornsvenska harmber 'sorg, skada, fortrytelse'; "
     "gemensamt germanskt ord, belagt pa runsten fran 1000-talet.",
     "SO: '(moraliskt betingad) vrede', SYN-markt mot indignation -- den "
     "starkaste beviskategorin, och orden klarar bada-hallen-provet. "
     "Fortrytelse ar daremot bara JFR-markt och tas inte upp. NOT: "
     "fortrytelse skrevs i foregaende batch samma dag och fick ocksa "
     "indignation som synonym (aven dar SYN-markt). Det ar korrekt for bada "
     "-- skillnaden mellan harm och fortrytelse ar att fortrytelse traffar "
     "en sjalv ('till sin stora fortrytelse'), harm traffar en oratt mot "
     "vem som helst. OLD-facit 'ilska' ar for brett: ilska behover ingen "
     "moralisk grund alls.")

satt("implodera",
     "Brista så att väggarna sugs inåt mot mitten i stället för att slungas "
     "utåt ; bildligt om ett system eller en organisation: falla samman "
     "inifrån",
     "fackspråklig, neutral, fysik ; neutral, neutral, allmän",
     [],
     "Östblocket " + B % "imploderade" + " 1989.",
     "→ Engelska implode, bildat efter explodera med latin in 'inat' som "
     "forled.",
     "SO ger tva: 'springa sonder sa att bitarna sugs inat mot ett centrum' "
     "och 'falla samman' (ofta bildligt). Bada ar med. Ledet 'i stallet for "
     "att slungas utat' ar inskrivet eftersom hela ordet bara ar begripligt "
     "i kontrast till explodera -- SO markerar sjalv explodera som JFR. "
     "OLD-facit 'sprangas inat' ar SAOL:s ord och missar den bildliga "
     "anvandningen, som ar den vanligaste i text.")

satt("klassifikation",
     "Indelning av något i grupper efter bestämda kännetecken",
     "neutral, neutral, allmän",
     ["klassificering"],
     "Även i äldre tid fanns en sorts " + B % "klassifikation" + " av "
     "molnen.",
     None,
     "SO:s hela definition ar ett ord: 'klassificering' -- darav synonymen, "
     "som klarar bada-hallen-provet (orden ar utbytbara i vilken mening som "
     "helst). Wiktionary skriver ut vad det innebar: 'indelning i klasser'. "
     "OLD-facit 'sortering' ar INTE upptaget som synonym: man kan sortera "
     "efter storlek utan att skapa nagra klasser, sa sortering ar bade "
     "bredare och gor nagot annat.")

satt("koloratur",
     "Utsmyckning av en sångstämma med snabba löpningar och drillar",
     "fackspråklig, neutral, musik",
     [],
     "Partiet kräver en sopran som behärskar " + B % "koloratur" + ".",
     "→ Italienska coloratura, till latin colorare 'farga' -- sangen "
     "'fargas'; samma rot som kolorera.",
     "SO: 'utsmyckning av sang med drillar och lopningar'. SAOL sager samma "
     "sak. SO:s JFR lopning ar cohyponymmarkt -- det ar en BESTANDSDEL i "
     "koloraturen, inte ett utbytbart ord. OLD-facit "
     "'sangutsmyckning' stammer i sak men sager inte VILKEN sorts "
     "utsmyckning, vilket ar hela termen.")

satt("konvergent",
     "Om strålar eller linjer: riktade mot samma punkt ; bildligt om åsikter "
     "eller utvecklingar: som närmar sig varandra ; inom matematiken: som "
     "har ett gränsvärde",
     "fackspråklig, neutral, fysik ; neutral, neutral, allmän ; "
     "fackspråklig, neutral, matematik",
     [],
     "Ett knippe " + B % "konvergenta" + " ljusstrålar möts i brännpunkten.",
     "→ Till konvergera; av latin convergere 'luta mot varandra'.",
     "SO ger TRE betydelser: 'som ar riktade mot samma punkt' (markning: "
     "spec. fysik), 'som tenderar att sammanfalla' (av. bildligt) och 'som "
     "har gransvarde'. Alla tre ar med -- den matematiska skulle ha fallit "
     "bort om jag slagit ihop den med den forsta, vilket ar precis felet "
     "som fallde ax och yttring i foregaende batch. SO markerar divergent "
     "som MOTSATS; det ordet ar alltsa antonym, inte synonym, och tas inte "
     "upp. OLD-facit 'sammanlopande' ar SAOL:s ord och tacker bara den "
     "forsta.")

satt("lomma",
     "Gå långsamt och tungt, med släpande steg ; ge sig iväg långsamt och "
     "snopet, ofta efter ett nederlag",
     "vardaglig, neutral, allmän ; vardaglig, neutral, allmän",
     [],
     "Hunden " + B % "lommade" + " av när den inte fick något socker.",
     "→ Svensk dialekt loma, lomma; ev. beslaktat med lam.",
     "SO ger tva: 'ga langsamt och nagot lufsigt' och '(snopet) ge sig i "
     "vag'. Bada ar med. Skillnaden ar riktningen -- den forsta beskriver "
     "SATTET att ga, den andra att man LAMNAR platsen, och SO markerar den "
     "andra sarskilt. Ordet 'lufsigt' ar upplost till 'tungt, med slapande "
     "steg' enligt Adam-tal. OLD-facit 'ga langsamt' hade bara den forsta "
     "och missade snopenheten, som ar ordets hela farg.")

satt("nihilism",
     "Uppfattningen att ingenting egentligen finns eller har något värde ; "
     "en hållning som avvisar allt bestående utan att sätta något i stället "
     "; historiskt: en revolutionär rörelse i 1800-talets Ryssland",
     "fackspråklig, neutral, filosofi ; neutral, neutral, allmän ; neutral, "
     "neutral, historia",
     [],
     "Hans totala svartsyn och " + B % "nihilism" + " gjorde honom omöjlig "
     "att diskutera med.",
     "→ Tyska Nihilismus; till latin nihil 'ingenting'.",
     "SO ger TRE betydelser: den filosofiska ('asikten att ingenting "
     "verkligt existerar'), den allmanna ('helt avvisande hallning') och "
     "den historiska ('en revolutionar rysk ytterlighetsrorelse', markning: "
     "historiskt). Alla tre ar med. SAOL bekraftar de tva forsta och lagger "
     "till att det galler 'aven varden och normer' -- det ledet ar "
     "inskrivet. OLD-facit 'fornekande av normer' hade bara halva den "
     "filosofiska betydelsen: nihilismen fornekar i sin starkaste form att "
     "nagot alls EXISTERAR, inte bara att normer galler.")

satt("notabel",
     "Värd att lägga märke till — tillräckligt ovanlig för att nämnas",
     "formell, neutral, allmän",
     [],
     B % "Notabelt" + " är det höga oddset på trean.",
     "→ Franska notable, latin notabilis; till notera.",
     "SO: 'vard att lagga marke till', med markningen formellt. SAOL:s "
     "'marklig; bemarkt, fornam' ar INTE upptagna som synonymer. Bemarkt "
     "skrevs dessutom i foregaende batch samma dag och foll da just pa "
     "synonymfaltet -- skillnaden ar att bemarkt beskriver en PERSON som ar "
     "kand, notabel beskriver en UPPGIFT som ar vard att namna. OLD-facit "
     "'anmarkningsvard' ligger nara men ar starkare: notabelt betyder vart "
     "att namna, anmarkningsvart betyder uppseendevackande.")

satt("orogenes",
     "Bildningen av bergskedjor, när rörelser i jordskorpan pressar upp "
     "berggrunden",
     "fackspråklig, neutral, geologi",
     ["bergskedjebildning"],
     "Vid den senaste stora " + B % "orogenesen" + " bildades Alperna.",
     "→ Grekiska oros 'berg' och genesis 'skapelse'; samma efterled som i "
     "genes.",
     "SO: 'bildning av bergskedjor genom rorelser i jordskorpan'. SAOL:s "
     "hela definition ar 'bergskedjebildning' -- darav synonymen, som "
     "klarar bada-hallen-provet eftersom de betecknar exakt samma "
     "foreteelse. HUR det gar till (rorelser i jordskorpan) ar med, "
     "eftersom SAOL:s ord annars bara byter ett langt ord mot ett annat. "
     "OLD-facit sa just 'bergskedjebildning'.")

satt("sejour",
     "Kortare tid som man tillbringar på ett ställe innan man drar vidare",
     "neutral, neutral, allmän",
     [],
     "Efter " + B % "sejouren" + " i den italienska klubben återvände han "
     "till moderklubben.",
     "→ Franska séjour, till séjourner 'vistas'.",
     "SO: 'kortare, tillfallig vistelse', med noteringen 'ofta i "
     "sportjargong' -- darav exempelmeningen, som ar SO:s egen. Ledet "
     "'innan man drar vidare' ar inskrivet: en sejour ar per definition ett "
     "MELLANSPEL, vilket OLD-facits 'vistelse' inte sager. SAOL:s "
     "'vistelsetid, uppehall' ar darfor inte upptagna som synonymer -- de "
     "saknar bade tidsbegransningen och det tillfalliga.")

satt("suggerera",
     "Påverka någon så att en tanke tas emot utan att prövas ; också: "
     "framkalla en stämning eller känsla hos någon",
     "neutral, neutral, psykologi ; neutral, neutral, allmän",
     [],
     "Dekoren " + B % "suggererade" + " fram den rätta kusliga stämningen.",
     "→ Latin suggerere 'lagga under, bara fram, ingiva'.",
     "SO: 'paverka genom suggestion' -- en definition som forutsatter "
     "uppslagsordets egen stam, sa den ar utskriven. SO:s underbetydelse "
     "'ibland med stark tonvikt pa resultatet' tacker SO:s andra exempel "
     "(dekoren som suggererar fram en stamning) och ar med som egen "
     "betydelse. OLD-facit 'paverka, intala' var en synonymrad; intala ar "
     "obelagt i SO och SAOL och ar struket. SAOL:s 'hypnotiskt paverka' ar "
     "for smalt -- SO:s exempel handlar inte om hypnos.")

satt("tabelras",
     "Att allt sopas bort och man börjar om från noll",
     "ngt ålderdomlig, neutral, allmän",
     [],
     "Reformen innebar " + B % "tabelras" + " med hela det gamla systemet.",
     "→ Franska table rase 'rent bord'; av latin tabula rasa '(vax)tavla "
     "med utplanad skrift' -- samma rot som tavla.",
     "SO: 'total forstorelse', med markningen mindre brukligt; SAOL: "
     "'fullstandig forodelse'. MOTSAGELSE MELLAN KALLOR: Wiktionary ger en "
     "helt annan betydelse -- 'gora rent bord, ata, dricka eller gora slut "
     "pa det som dukats fram'. Den ar INTE med: SO och SAOL ar overens mot "
     "Wiktionary, och samma feltyp (en Wiktionary-egen betydelse) fallde "
     "anlopa och autograf i foregaende batch. Facit foljer SO/SAOL men "
     "skriver ut att det handlar om att sopa bort for att BORJA OM, vilket "
     "etymologin (den utplanade vaxtavlan) gor tydlig.")

satt("ävlan",
     "Ivrig och enträgen strävan efter något",
     "högtidlig, neutral, allmän",
     [],
     "Människans fåfänga " + B % "ävlan" + " efter lycka.",
     None,
     "SO: 'ivrig och angelagen stravan', med markningen hogtidligt; SAOL "
     "markar ald. SAOL:s 'ivrig stravan' sager samma sak. Ordet 'angelagen' "
     "ar utbytt mot 'entragen', som ar vanligare. NOT: SO:s enda "
     "exempelmening ('manniskans fafanga avlan efter lycka') antyder att "
     "stravan ar forgaves, men det star inte i definitionen och ar darfor "
     "INTE inskrivet i facit -- att lasa in en biton ur en exempelmening ar "
     "samma sorts overtolkning som fallde eklatera. OLD-facit 'ivrig "
     "stravan, moda, iver' var en synonymrad; moda och iver ar bredare och "
     "ar strukna.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
ok = sum(1 for k in KORT if k.get("approved"))
print("skrev %d kort totalt (2 halls tillbaka)" % ok)
