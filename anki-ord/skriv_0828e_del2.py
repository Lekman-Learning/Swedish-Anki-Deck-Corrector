# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch6, kort 21-40. Samma skarpta regler som del1."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch6.json"
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
    e = BY[o]
    e["sokkoll"] = {"kalla": kallor(o), "slutsats": motiv}
    e["confidence"] = 0
    e["approved"] = False


satt("omfång",
     "Hur stor plats en yta eller en kropp tar upp ; också om andra mätbara "
     "utsträckningar, som en rösts omfång ; mer abstrakt: hur långt något "
     "sträcker sig",
     "neutral, neutral, allmän ; neutral, neutral, allmän ; neutral, "
     "neutral, allmän",
     [],
     "Skadeverkningarnas " + B % "omfång" + " stod klart först efter flera "
     "veckor.",
     "→ Tyska Umfang; samma rot som fang.",
     "SO: '(storleken av den) del av rummet en yta eller en kropp upptar', "
     "med underbetydelserna 'av. i fraga om andra matbara utstrackningar' "
     "och 'av. mer abstrakt'. Alla tre ar med. SO:s JFR (omfattning, "
     "utstrackning, volym) ar cohyponymmarkta och tas INTE upp som "
     "synonymer -- OLD-facit sa 'storlek och omfattning', vilket ar just en "
     "sadan synonymrad, och den suddar att omfang i grunden handlar om PLATS "
     "i rummet.")

satt("plottrig",
     "Full av småsaker som inte hänger ihop, så att helheten blir svår att "
     "uppfatta",
     "neutral, lätt negativ, allmän",
     [],
     "En faktaspäckad men lite " + B % "plottrig" + " bok.",
     None,
     "SO: 'som bestar av en mangd smadetaljer utan klart sammanhang'. SAOL: "
     "'som saknar helhet, alltfor sonderstyckad'. SO:s JFR (oredig, rorig) "
     "ar cohyponymmarkta och tas inte upp. OLD-facit sa 'rorig', vilket ar "
     "for brett: ett rum kan vara rorigt utan att besta av smadetaljer, och "
     "det ar antalet SMA delar utan sammanhang som ar plottrigt.")

satt("ranglig",
     "Som inte sitter väl ihop och därför vinglar ; om en person: lång och "
     "smal utan stadga i kroppen",
     "neutral, lätt negativ, allmän ; neutral, lätt negativ, allmän",
     [],
     "En " + B % "ranglig" + " stol som knakade vid minsta rörelse.",
     None,
     "SO ger tva: 'som inte sitter val ihop och darfor ar ostadig' och "
     "'lang och skranglig' (av. om person). Bada ar med -- den andra "
     "handlar inte om att nagot ar daligt hopsatt utan om kroppsform, och "
     "de har ingenting med varandra att gora utom bilden av ostadighet. "
     "SAOL:s hela definition ar 'skranglig'; det ordet ar INTE upptaget som "
     "synonym eftersom det bara tacker den andra betydelsen och alltsa inte "
     "klarar bada-hallen-provet. OLD-facit 'ostadig' tackte bara den "
     "forsta.")

satt("robust",
     "Som tål påfrestningar utan att gå sönder ; om ett system: driftsäkert, "
     "fungerar även när något går fel ; om en person: som inte tar illa vid "
     "sig av motgångar ; om ett sätt eller en jargong: grov och utan "
     "förfining",
     "neutral, positiv, allmän ; fackspråklig, positiv, teknik ; neutral, "
     "positiv, allmän ; neutral, lätt negativ, allmän",
     [],
     "Han har en " + B % "robust" + " personlighet och orättvis kritik biter "
     "inte på honom.",
     "→ Latin robustus, till robur 'hart tra, styrka'.",
     "SO ger 'som tal pafrestningar val' och 'driftsaker' som SKILDA "
     "definitioner, plus underbetydelserna 'sarsk. om person, av. sjalsligt' "
     "och 'av. om handling eller dylikt, med tonvikt pa den laga graden av "
     "forfining'. Alla fyra ar med. Frestelsen att sla ihop de tva forsta "
     "ar stor -- de later lika -- men de ar olika: en kokssoffa TAL slag, "
     "ett system FUNGERAR trots fel. Sex hopslagningar underkandes tidigare "
     "i dag och regeln ar nu att ordbokens uppdelning galler. Den fjarde "
     "betydelsen ar dessutom den enda med negativ laddning (SO:s exempel: "
     "en robust jargong), vilket OLD-facit 'kraftig och stadig' helt "
     "missade.")

satt("skurril",
     "Komisk på ett grovt och plumpt sätt",
     "ngt ålderdomlig, lätt negativ, allmän",
     [],
     B % "Skurrila" + " skämt som fick halva publiken att resa sig.",
     "→ Latin scurrilis 'narraktig', till scurra 'dagdrivare, skamtare'.",
     "SO: 'komisk pa ett grovt satt', med markningen ngt ald. SAOL: 'grovt "
     "gycklande, plump, vulgar'. SO:s JFR burlesk ar cohyponymmarkt och tas "
     "INTE upp som synonym -- OLD-facit listade det forst i en synonymrad "
     "('burlesk, gycklande, plump, vulgar, ra'), men burlesk ar en "
     "konstform med overdrivna kontraster medan skurril beskriver grovhet. "
     "Ingen av de fem ar upptagen.")

satt("sträva",
     "Anstränga sig målmedvetet för att nå något ; ta sig fram med möda ; om "
     "något högt: sträcka sig uppåt ; som substantiv: snedställt stöd som "
     "stöttar en lutande vägg",
     "neutral, neutral, allmän ; neutral, neutral, allmän ; litterär, "
     "neutral, allmän ; fackspråklig, neutral, teknik",
     [],
     "Tornspiran " + B % "strävar" + " mot himlen.",
     "→ I verbbetydelsen lagtyska streven 'sticka upp, anstranga sig'; "
     "samma rot som streber. Substantivet av tyska Strebe.",
     "SO ger FYRA betydelser: 'anstranga sig for att uppna', 'ta sig fram "
     "med anstrangning', 'peka' (av. i fraga om tankt rorelse -- SO:s "
     "exempel: tornspiran stravar mot himlen) och substantivet 'snedstallt "
     "stod'. Alla fyra ar med. SAOL bekraftar tre av dem. OLD-facit "
     "'arbeta' tackte en enda, och missade bade den fysiska rorelsen, den "
     "bildliga och hela substantivet -- som dessutom har egen etymologi och "
     "alltsa ar ett annat ord.")

satt("utläggning",
     "Att placera ut något, som minor eller kablar ; en lång och utförlig "
     "redogörelse i tal eller skrift",
     "fackspråklig, neutral, teknik ; neutral, neutral, allmän",
     [],
     "Hon höll en lång " + B % "utläggning" + " om riskerna med alkohol.",
     None,
     "SO ger tva helt oberoende betydelser: 'det att placera ut nagot' "
     "(SO:s exempel: utlaggning av minor) och 'langre, noggrann "
     "framstallning'. Bada ar med. SAOL har bara den forsta "
     "('utplacering'), Wiktionary bada. OLD-facit 'redogorelse, kommentar' "
     "hade bara den andra -- och 'kommentar' ar for kort: poangen med en "
     "utlaggning ar att den ar LANG.")

satt("agentur",
     "Att företräda ett annat företags ekonomiska intressen, till exempel "
     "genom att sälja dess varor ; också om företaget som gör det",
     "neutral, neutral, ekonomi ; neutral, neutral, ekonomi",
     [],
     "De tog över " + B % "agenturen" + " för färjeleden.",
     "→ Till agent, av latin agere 'satta i rorelse, handla'.",
     "SO: 'verksamhet som ekonomisk representant', med underbetydelsen 'av. "
     "om motsvarande organisation'. Bada ar med -- ordet betecknar bade "
     "SYSSLAN och FORETAGET, och SO:s tva exempel visar just det ('handel "
     "med klader i agentur' mot 'lata en agentur ta over verksamheten'). "
     "OLD-facit 'foretradare at foretag' hade bara organisationen, och "
     "beskriver dessutom en person snarare an ett foretag.")

satt("aktualisera",
     "Få en fråga att bli angelägen igen så att den måste tas upp",
     "neutral, neutral, allmän",
     [],
     "Storbranden " + B % "aktualiserar" + " personalbristen inom "
     "brandförsvaret.",
     "→ Franska actualiser; till aktuell.",
     "SO:s hela definition ar 'gora aktuell' -- ett facit som bygger pa "
     "uppslagsordets egen stam och darfor ar utskrivet enligt Adam-tal. "
     "SAOL ger 'gora aktuell, uppdatera' med KOMMA, inte semikolon: det ar "
     "tva glosor for samma betydelse, inte tva betydelser, sa kortet har "
     "bara en. Ingen synonym ar upptagen: uppdatera galler en uppgift som "
     "blivit foraldrad, aktualisera galler en fraga som blivit angelagen "
     "igen. OLD-facit sa 'gora aktuell' och forklarar ingenting.")

satt("alias",
     "Även kallad — sätts mellan någons riktiga namn och ett påhittat ; som "
     "substantiv: det påhittade namnet i sig",
     "neutral, neutral, allmän ; neutral, neutral, allmän",
     [],
     "Polisen gick ut med det " + B % "alias" + " mannen använt på internet.",
     "→ Latin alias 'vid annat tillfalle'.",
     "SO ger tva: adverbet 'aven kallad' (SO:s exempel: klassens skrack "
     "alias Lillen) och substantivet 'fingerat namn'. Bada ar med -- de ar "
     "olika ordklasser och anvands helt olika, vilket OLD-facit ('annat "
     "namn') doljer genom att bara ge substantivet. SO:s JFR tacknamn ar "
     "jamforelsemarkt och tas inte upp; ett tacknamn ar dessutom nagot man "
     "doljer sig bakom, ett alias behover inte dolja nagot.")

satt("avvika",
     "Ändra riktning och lämna den utstakade vägen ; i hemlighet ge sig av "
     "från en plats man ska vara på ; tydligt skilja sig från det vanliga "
     "eller väntade",
     "neutral, neutral, allmän ; neutral, neutral, allmän ; neutral, "
     "neutral, allmän",
     [],
     "Två interner " + B % "avvek" + " från fängelset under permissionen.",
     "→ Fornsvenska afvika.",
     "SO ger TRE betydelser: 'andra sin fardriktning', 'i hemlighet lamna, "
     "rymma' och 'klart skilja sig' (av. bildligt). Alla tre ar med. "
     "OLD-facit 'skilja sig' hade bara den tredje och missade helt "
     "rymningsbetydelsen, som ar den enda dar ordet ar en fackterm "
     "(kriminalvard, sjukvard) och den som mest sannolikt dyker upp i en "
     "text utan att lasaren forstar den. Exempelmeningen ar darfor vald "
     "till den.")

satt("bagatellisera",
     "Låtsas som att något viktigt bara är en småsak",
     "neutral, lätt negativ, allmän",
     [],
     "Man bör inte " + B % "bagatellisera" + " miljöproblemen.",
     "→ Till bagatell, av franska bagatelle 'smasak'.",
     "SO och SAOL ger ordagrant samma definition: 'forringa betydelsen av'. "
     "Forringa ar INTE upptaget som synonym: man kan forringa nagons insats "
     "utan att latsas att den ar en smasak, sa orden klarar inte "
     "bada-hallen-provet. Wiktionarys 'avfarda som oviktigt; anse vara en "
     "bagatell' ligger nara facit och stodjer formuleringen. OLD-facit "
     "'forringa' ar just den synonymen.")

satt("benign",
     "Om en tumör eller sjuklig förändring: som utvecklas på ett ofarligt "
     "sätt",
     "fackspråklig, neutral, medicin",
     ["godartad"],
     "Vårtan visade sig vara " + B % "benign" + ".",
     "→ Latin benignus, till bene 'val' och gignere 'foda, frambringa'.",
     "SO: 'som utvecklas pa godartat satt', med markningen med. SAOL:s hela "
     "definition ar 'godartad' -- darav synonymen, som klarar "
     "bada-hallen-provet inom medicinen och inte ar JFR-markt. SO markerar "
     "malign som MOTSATS, alltsa antonym: det ar det ordet man ska halla "
     "isar benign fran, och de skiljs bara av tre bokstaver. OLD-facit "
     "'godartad' stammer exakt.")

satt("besjälad",
     "Helt uppfylld av en känsla eller en vilja ; om naturen eller döda "
     "ting: framställd som om den hade en själ",
     "litterär, neutral, allmän ; litterär, neutral, litteraturvetenskap",
     [],
     "Hon var " + B % "besjälad" + " av en vilja att hjälpa sina "
     "medmänniskor.",
     "→ Efter tyska beseelen; till sjal.",
     "SO ger 'uppfylla' och 'ge sjal at, formanskliga', med underbetydelsen "
     "'av. bokstavligt med avseende pa doda ting' (SO:s exempel: den "
     "besjalade naturen hos de romantiska diktarna). Bada betydelserna ar "
     "med. SAOL:s 'passionerat engagerad' bekraftar den forsta. OLD-facit "
     "'inspirerad, eldad; sjalfull' var en synonymrad, och ingen av de tre "
     "ar upptagen -- sjalfull beskriver den som HAR sjal, besjalad den som "
     "FYLLTS av nagot.")

satt("bondsk",
     "Som har drag som kännetecknar bönder och deras kultur — enkel och "
     "jordnära",
     "neutral, neutral, allmän",
     [],
     "Möbler i en enkel, " + B % "bondsk" + " stil.",
     None,
     "SO: 'som har egenskaper som kannetecknar bonder eller bonders "
     "kultur'. Ingen bruklighets- eller valensmarkning finns, sa registret "
     "ar neutralt trots att ordet KAN anvandas nedsattande -- SO:s tva "
     "exempel ar en neutral mobelstil och ett 'troskyldigt och lite "
     "bondskt' svar, alltsa inte entydigt negativa, och en laddning far "
     "inte hittas pa. OLD-facit 'lantlig' ar for brett: lantligt handlar om "
     "landsbygden, bondskt specifikt om bonder.")

satt("deklassera",
     "Trycka ner någon till en lägre samhällsställning",
     "neutral, negativ, allmän",
     [],
     "Genom faderns konkurs blev familjen " + B % "deklasserad" + ".",
     "→ Franska déclasser, till dé- 'itu' och classe 'klass'.",
     "SO och SAOL ger ordagrant samma definition: 'ge lagre rang el. "
     "status'. Ordet 'samhallsstallning' kommer fran Wiktionary "
     "('nedsatta; flytta ned i en lagre samhallsstallning') och ar med "
     "eftersom bade SO:s och SAOL:s enda exempel handlar om social klass, "
     "inte om rang i en organisation. OLD-facit 'nedsatta socialt' sager "
     "samma sak.")

satt("drittel",
     "Träkärl av sammanfogade stavar som förr användes för att förvara smör "
     "; också om det rymdmått ett sådant kärl rymde",
     "neutral, neutral, historia ; neutral, neutral, historia",
     [],
     "Smöret packades i en " + B % "drittel" + " för export till England.",
     "→ Danska drittel; av tyska Drittel 'tredjedel'.",
     "SO: 'storre laggkarl for forvaring av smor', markning: mest "
     "historiskt. SAOL ger TVA: 'tunna for forpackning av smor' OCH 'en "
     "volymenhet for smor' -- alltsa bade karlet och mattet, och bada ar "
     "med. Wiktionary bekraftar bada och lagger till att karlet var av bok "
     "och anpassat for den engelska marknaden, vilket exempelmeningen "
     "speglar. Ordet 'laggkarl' ar utskrivet enligt Adam-tal.")

satt("eufemism",
     "Mildare ord som man sätter i stället för ett som känns obehagligt "
     "eller grovt",
     "fackspråklig, neutral, lingvistik",
     [],
     "\"Den lede\" är en " + B % "eufemism" + " för \"fan\".",
     "→ Grekiska euphemismos 'anvandning av ett vackert ord for en dalig "
     "sak', till eu 'god' och pheme 'ord, sprak'.",
     "SO: 'forskonande omskrivning'. SAOL: 'mildrande el. forskonande "
     "uttryck'. Bada leden -- att det MILDRAR och att det ersatter nagot "
     "obehagligt -- ar med, eftersom SO:s ord 'forskonande' ensamt later "
     "som om det handlade om att gora nagot vackert i allmanhet. SO:s JFR "
     "noaord ar cohyponymmarkt (ett noaord ar en eufemism av vidskeplig "
     "orsak, alltsa en underart). OLD-facit 'forskonande omskrivning' ar "
     "SO:s ord rakt av.")

satt("fog",
     "Ställe där två delar i en konstruktion satts ihop ; i uttrycket "
     "\"knaka i fogarna\": vara nära att brista ; fullgott skäl — \"med "
     "fog\" ; i grammatiken: ljudet eller bokstaven som binder ihop två led "
     "i ett sammansatt ord",
     "neutral, neutral, teknik ; neutral, neutral, allmän ; neutral, "
     "neutral, allmän ; fackspråklig, neutral, lingvistik",
     [],
     "Deras äktenskap knakar i " + B % "fogarna" + ".",
     "→ Skarvbetydelsen av lagtyska voge, till vogen 'foga'. Skalbetydelsen "
     "fornsvenska fogh 'det som ar till pass' -- ett annat ord med annan "
     "historia; samma rot som ofog.",
     "SO ger TRE definitioner plus en underbetydelse, och alla fyra ar med: "
     "skarven, uttrycket 'knaka i fogarna' (SO:s egen definition 'vara nara "
     "att brista'), 'fullgott skal' och 'av. om sammanbindande ljud el. "
     "bokstav' (foge-s). VIKTIGT: skarven och skalet ar TVA OLIKA ORD med "
     "skilda etymologier som fallit ihop i stavning -- det ar utskrivet i "
     "etymologin, eftersom en lasare annars forsoker hitta ett samband som "
     "inte finns. OLD-facit 'skarv; bra skal' hade tva av fyra.")

hall_tillbaka(
    "bulbus",
    "HALLS TILLBAKA -- INGEN KALLA ALLS. Uppslagningen gav traffar=INGEN: "
    "ordet saknas i SO, SAOL och SAOB, och bade synonymer.se och "
    "Wiktionary returnerade tomt. OLD-facit sager 'knol'. Bulbus ar latin "
    "och anvands i svensk anatomi (bulbus oculi = ogongloben, bulbus "
    "olfactorius = luktbulben), men INGEN av de uppslagna kallorna sager "
    "det -- att skriva ut det vore att hamta ur eget minne och kalla det "
    "uppslaget. Tredje kortet i dag som halls tillbaka av samma skal "
    "(se frontong, ipso jure). Kortet skrivs inte forran en fackordbok "
    "slagits upp.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("skrev %d kort, haller tillbaka bulbus"
      % sum(1 for k in KORT if k.get("approved")))
