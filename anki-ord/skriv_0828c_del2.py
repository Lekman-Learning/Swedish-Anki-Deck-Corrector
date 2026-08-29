# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch100, kort 26-50. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch100.json"
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


# --- rattelse av del1: SO markte harnesk 'alderdomligt', inte 'nagot' ---
BY["harnesk"]["proposed"]["register"] = (
    "arkaisk, neutral, historia ; neutral, neutral, allmän ; "
    "fackspråklig, neutral, geologi")

satt("missanpassad",
     "Som inte har lyckats finna sig till rätta bland andra människor, i "
     "skolan eller i samhället",
     "neutral, lätt negativ, allmän",
     [],
     "De svårt " + B % "missanpassade" + " ungdomarna sökte sig till "
     "extrema grupper.",
     None,
     "SO: 'illa anpassad till (den sociala) omgivningen'. VIKTIG RATTELSE: "
     "OLD-facit sa 'ouppfostrad', vilket ar fel ord. Ouppfostrad handlar om "
     "uppforande och om vad nagon lart sig hemma; missanpassad handlar om "
     "att inte fungera i sitt sammanhang, och sager ingenting om skuld "
     "eller uppfostran. Facit ar omskrivet.")

satt("socken",
     "Det äldsta lokala området på landsbygden: en kyrka med sin församling, "
     "som förr också var indelningen för allt lokalt styre",
     "ngt ålderdomlig, neutral, historia",
     ["församling"],
     "En liten by i Oderljunga " + B % "socken" + ".",
     "→ Fornsvenska sokn, bildat till soka -- omradet vars folk sokte sig "
     "till samma kyrka.",
     "SO: 'forsamling', SAOL: 'forsamling pa landsbygden', bada med "
     "markningen nagot alderdomligt. Synonymen forsamling ar sjalva "
     "definitionstexten. SAOL listar aven en helt orelaterad betydelse "
     "('socka') -- den ar medvetet utelamnad eftersom den bara ar en "
     "stavningsvariant och skulle grumla kortet. OLD-facit 'aldre "
     "landsindelning' missar att det var kyrkan som definierade omradet.")

satt("valeriana",
     "En hög ört med små vita eller ljusrosa blommor i yviga knippen ; det "
     "lugnande medel som utvinns ur dess rot",
     "neutral, neutral, biologi ; neutral, neutral, medicin",
     ["vänderot"],
     "Hon tog " + B % "valeriana" + " för att kunna somna.",
     "→ Medeltidslatin valeriana; ursprunget ar omdiskuterat.",
     "SO: 'en hog, grenad ort ...', med underbetydelserna 'av. om det "
     "nervlugnande medlet' och 'av. om det slakte som orten tillhor'. SAOL "
     "ger bara medlet: 'preparat av vanderot som lugnande medel'. Bade "
     "vaxten och medlet ar med; slaktbetydelsen ar utelamnad som ren "
     "botanisk teknikalitet. Synonymen vanderot star i SAOL:s "
     "definitionstext (det ar samma vaxt pa svenska), inte bara som JFR i "
     "SO. OLD-facit 'nervlugnande lakevaxt' slog ihop vaxten och medlet.")

satt("varseblivning",
     "Att lägga märke till något med sinnena och göra det till en upplevelse "
     "; inom psykologin: samma sak, men om det som sker inne i en själv",
     "neutral, neutral, allmän ; fackspråklig, neutral, psykologi",
     [],
     "Det lilla barnets " + B % "varseblivning" + " av världen förändras "
     "snabbt.",
     None,
     "SO: 'det att bli varse nagot', med en sarskild psykologisk betydelse "
     "om iakttagande av egna inre skeenden. Bada ar med. SO:s JFR "
     "perception ar cohyponymmarkt och tas darfor INTE upp som synonym, "
     "trots att Wiktionary glossar orden mot varandra -- regeln ar att bara "
     "SO:s eller SAOL:s definitionstext eller en SYN-markning duger som "
     "synonymbevis. OLD-facit 'sinnesuppfattning' ar rimligt men doljer att "
     "ordet betecknar sjalva handelsen, inte formagan.")

satt("ax",
     "Toppen på ett sädesstrå, där kornen sitter tätt samlade ; den "
     "utskjutande delen av en nyckel som griper in i låset ; vardagligt: "
     "acceleration hos ett fordon",
     "neutral, neutral, allmän ; neutral, neutral, teknik ; vardaglig, "
     "neutral, allmän",
     [],
     "Tunga, gyllene " + B % "ax" + " vajade över åkern.",
     "→ Fornsvenska ax; ur en indoeuropeisk ordgrupp med betydelsen 'vass, "
     "spetsig'.",
     "SO ger fem betydelser; tre ar sarskilda ord i praktiken och ar med: "
     "sadesaxet, nyckelaxet och den vardagliga accelerationsbetydelsen "
     "(SO:s markning: vardagligt). Den botaniska definitionen "
     "('blomstallning med oskaftade blommor pa lang huvudaxel') ar samma "
     "sak som sadesaxet, bara fackligare formulerad, och ar hopslagen. "
     "Uttrycket 'fran ax till limpa' ar SO:s egen underbetydelse men ar ett "
     "idiom och hor hemma pa ett eget kort, inte i facit har. OLD-facit "
     "'sadesax' hade bara en av tre.")

satt("bemärkt",
     "Känd och respekterad för att ha uträttat något ovanligt bra",
     "neutral, positiv, allmän",
     ["framstående", "uppmärksammad"],
     "Hon har gjort sig " + B % "bemärkt" + " inom genforskningen.",
     None,
     "SO: 'kand for framstaende egenskaper'. SAOL: 'uppmarksammad, "
     "framstaende' -- bada synonymerna star darmed i definitionstexten. "
     "OLD-facit 'kand och framstaende' stammer; facit ar bara skarpt sa "
     "att det framgar att det ar prestationen som gjort personen kand, "
     "inte kandisskapet i sig.")

satt("efterkomma",
     "Göra det som någon med rätt att bestämma har begärt eller befallt",
     "formell, neutral, allmän",
     ["hörsamma"],
     "Företaget vägrade " + B % "efterkomma" + " myndighetens krav.",
     None,
     "SO:s hela definition ar ett ord: 'horsamma' -- darfor ar det upptaget "
     "som synonym (definitionstext, inte JFR). SO:s markning: formellt. "
     "OLD-facit 'lyda' ar nara men for brett: man efterkommer en begaran "
     "eller ett krav, inte en person, och det ar just den skillnaden mot "
     "'lyda' som gor ordet svart.")

satt("falsett",
     "Det höga, tunna röstläge som ligger ovanför den vanliga rösten och som "
     "framför allt män kan sjunga eller tala i",
     "neutral, neutral, musik",
     [],
     "Han var så upprörd att rösten gick upp i " + B % "falsett" + ".",
     "→ Italienska falsetto, eg. 'falsk rost', till falso 'falsk'.",
     "SO: 'hogt rostlage med tunn klangfarg', med underbetydelsen 'spec. om "
     "avsiktligt hogt rostlage, hos tenorer'. SAOL: 'ett sangsatt med hoga "
     "toner'. OLD-facit 'hogt tonlage' ar for brett -- en sopran sjunger "
     "hogt utan att sjunga i falsett; det avgorande ar att rosten byter "
     "karaktar och blir tunn.")

satt("illuminera",
     "Lysa upp något festligt med många ljus ; måla in färglagda bilder och "
     "bokstäver i en handskriven bok",
     "neutral, neutral, allmän ; fackspråklig, neutral, konst",
     ["eklärera"],
     "Hela parken var " + B % "illuminerad" + " inför nationaldagen.",
     "→ Latin illuminare 'lysa upp', till lumen 'ljus'.",
     "SO ger tva betydelser: 'festligt lysa upp' och 'forse (handskrift) "
     "med farglagda illustrationer'. Bada med. Eklarera ar SYN-markt i SO "
     "och duger darfor som synonym. OLD-facit 'upplysa' ar missvisande pa "
     "svenska: upplysa betyder i forsta hand 'informera', och det ar "
     "precis den forvaxlingen som gor ordet fardigt att gora fel pa.")

satt("infria",
     "Se till att ett löfte eller en förväntan verkligen blir av",
     "neutral, neutral, allmän",
     ["uppfylla", "förverkliga"],
     "Spelaren har ännu inte " + B % "infriat" + " förväntningarna.",
     "→ Till fri i betydelsen 'befriad'; aldre aven 'betala, fullgora'.",
     "SO: 'forverkliga'. SAOL: 'uppfylla'. Bada synonymerna ar sjalva "
     "definitionstexten. OLD-facit 'forverkliga' stammer men sager inte VAD "
     "man forverkligar -- infria tar nastan alltid ett lofte, ett krav "
     "eller en forvantan som objekt, och det ar den begransningen som ar "
     "svar.")

satt("offert",
     "Ett prisförslag som en säljare lämnar till en kund på en bestämd vara "
     "eller tjänst ; också själva papperet där förslaget står",
     "neutral, neutral, ekonomi ; neutral, neutral, ekonomi",
     ["anbud"],
     "Begär in " + B % "offerter" + " från minst tre olika firmor.",
     "→ Franska offerte, italienska offerta; till offerera.",
     "SO: 'erbjudande av tjanst eller vara till visst pris', SYN-markt mot "
     "anbud, med underbetydelsen 'av. om motsvarande dokument'. SAOL: "
     "'anbud'. Bada betydelserna ar med, och anbud ar synonym pa SYN-grund "
     "och inte JFR-grund. OLD-facit 'anbud; kostnadsforslag' var en ren "
     "synonymrad utan forklaring.")

satt("oförarglig",
     "Som inte gör någon upprörd eller illa berörd, trots att man kunde ha "
     "väntat sig det",
     "neutral, neutral, allmän",
     ["harmlös", "oskyldig"],
     "Ett helt " + B % "oförargligt" + " skämt som ingen kunde ta illa upp "
     "av.",
     None,
     "SO: 'som inte orsakar nagon irritation eller skada', med tva "
     "SYN-markningar: harmlos och oskyldig. Bada ar alltsa SYN-belagda och "
     "inte bara JFR. Wiktionary skarper poangen: 'trots att det kunde "
     "forvantas' -- det ledet ar inskrivet i facit, eftersom det ar det som "
     "skiljer oforarglig fran ett neutralt 'oskadligt'. OLD-facit "
     "'harmlos, beskedlig' var en synonymrad; beskedlig ar dessutom "
     "obelagt i SO och SAOL och ar struket.")

satt("rauk",
     "Hög stenpelare vid stranden som blivit kvar när havet nött bort det "
     "mjukare berget runt omkring",
     "neutral, neutral, geologi",
     [],
     "Gotlands berömda " + B % "raukar" + " står kvar i vattenbrynet.",
     "→ Gotlandsk dialekt rauk; samma rot som rok.",
     "SO: 'pelarformig rest av hardare berggrund'. SAOL: 'strandpelare pa "
     "Gotland'. Facit forklarar HUR de bildas, eftersom det ar det som gor "
     "ordet begripligt -- OLD-facit 'strandpelare' ar ett lika ovanligt ord "
     "som uppslagsordet och forklarar ingenting.")

satt("renhårig",
     "Som spelar med öppna kort och behandlar andra rättvist",
     "neutral, positiv, allmän",
     ["hygglig", "pålitlig"],
     "Han var " + B % "renhårig" + " nog att erkänna att han hade fel.",
     None,
     "SO: 'rattvis och arlig'. SAOL: 'hygglig, palitlig' -- darifran "
     "synonymerna, ur definitionstexten. SO:s JFR juste ar cohyponymmarkt "
     "och raknas inte. Ingen bruklighetsmarkning finns i SO eller SAOL, sa "
     "registret ar neutralt trots att ordet kanns talsprakligt -- en "
     "markning far inte hittas pa. OLD-facit hade bade facit och en "
     "synonymrad ('just, schysst, palitlig'); just och schysst ar obelagda "
     "i SO/SAOL och ar strukna.")

satt("spjäll",
     "Vridbar skiva i ett rör eller en skorsten som man stryper eller "
     "släpper på draget med ; motsvarande skiva som reglerar hur mycket luft "
     "som går in i en motor",
     "neutral, neutral, teknik ; fackspråklig, neutral, teknik",
     [],
     "Med stängt " + B % "spjäll" + " håller kakelugnen värmen hela natten.",
     "→ Fornsvenska spiäld, grundbetydelse 'kluvet trastycke'; beslaktat "
     "med spalt.",
     "SO: 'anordning for reglering av luft- eller gasstrommar i en "
     "skorstenskanal', med underbetydelsen 'av. om liknande anordning i "
     "forgasare'. Bada med. OLD-facit 'reglerande lucka' ar for vagt -- en "
     "lucka oppnas och stangs, ett spjall stalls i lagen daremellan, och "
     "det ar hela funktionen. Wiktionarys 'revbensspjall' ar ett annat ord "
     "med annat ursprung och ar inte med.")

satt("överläggning",
     "Formellt samtal där parterna går igenom en fråga tillsammans innan "
     "något beslutas",
     "neutral, neutral, allmän",
     [],
     "Parterna återupptar " + B % "överläggningarna" + " på måndag.",
     None,
     "SO: 'det att overlagga' -- en definition som forutsatter att man "
     "redan kan verbet, sa facit ar utskrivet. SO:s JFR (debatt, "
     "diskussion, forhandling) ar cohyponymmarkta och tas inte upp som "
     "synonymer: en debatt har publik, en forhandling har motstridiga krav, "
     "en overlaggning har varken del. OLD-facit 'diskussion' suddar just "
     "den skillnaden.")

satt("absolutism",
     "Att helt avstå från alkohol ; styrelseskick där all makt är samlad hos "
     "en enda person",
     "neutral, neutral, allmän ; neutral, neutral, politik",
     ["helnykterhet", "envälde"],
     B % "Absolutismen" + " i Frankrike nådde sin höjdpunkt med Ludvig XIV.",
     "→ Till absolut, i betydelsen 'obegransad, oinskrankt'.",
     "SO ger tva helt oberoende betydelser: 'total avhallsamhet fran bruk "
     "av alkohol' och 'koncentration av politisk makt till en person'. SAOL "
     "sammanfattar dem som 'helnykterhet' och 'envalde' -- darav bada "
     "synonymerna, ur definitionstexten. SO:s JFR (nykterism, envalde) "
     "hade inte rackt som belagg for envalde, men SAOL ger det i "
     "definitionen. OLD-facit hade bada betydelserna men bara som "
     "stickord.")

satt("allitteration",
     "Att flera betonade ord nära varandra börjar med samma ljud, som i "
     "\"hals över huvud\"",
     "fackspråklig, neutral, litteraturvetenskap",
     ["uddrim"],
     B % "Allitterationen" + " är den fornnordiska diktningens främsta "
     "kännetecken.",
     "→ Franska allittération; till latin ad 'till' och littera 'bokstav'; "
     "samma rot som litteratur.",
     "SO: 'typ av rim som innebar att tryckstarka ord som star nara "
     "varandra borjar pa vokal eller samma konsonant'. Uddrim ar SYN-markt "
     "och duger som synonym; inrim ar JFR-markt (det ar motsatsen, rim "
     "inne i raden) och tas inte upp. OLD-facit 'begynnelserim' ar korrekt "
     "men lika svart som uppslagsordet.")

satt("alstring",
     "Att skapa något, särskilt konstnärligt ; också om det som skapats",
     "högtidlig, neutral, allmän ; högtidlig, neutral, allmän",
     [],
     "Pristagarens flödande lyriska " + B % "alstring" + " sträcker sig över "
     "fyra decennier.",
     None,
     "SO: 'skapande verksamhet', med underbetydelsen 'av. om resultatet'. "
     "Bada med -- det ar just tvetydigheten mellan handlingen och "
     "resultatet som gor ordet svart. SO:s markning: nagot hogtidligt. "
     "OLD-facit 'skapande' hade bara handlingen.")

satt("anatema",
     "Ett hårt och högtidligt fördömande, ursprungligen kyrkans beslut att "
     "stänga ute någon ur församlingen",
     "högtidlig, negativ, allmän",
     ["bannlysning", "förkastelsedom"],
     "Han utslungade ett " + B % "anatema" + " över hela normupplösningen.",
     "→ Grekiska anathema 'nagot som ar vigt at en gud' -- alltsa "
     "avskilt fran det vanliga livet.",
     "SO: 'kraftigt fordomande', med markningen nagot hogtidligt. SAOL: "
     "'bannlysning, forkastelsedom' -- darifran bada synonymerna, ur "
     "definitionstexten. Facit tar med bade den moderna, varldsliga "
     "anvandningen (SO:s exempel handlar om social orattvisa) och det "
     "kyrkliga ursprunget, eftersom OLD-facit 'bannlysning' bara gav det "
     "senare och darfor blir fel i de flesta moderna belagg.")

satt("anlöpa",
     "Om fartyg: gå in i en hamn och lägga till för ett kortare uppehåll ; "
     "om metall: mörkna eller få en hinna på ytan när den värms eller utsätts "
     "för luft",
     "fackspråklig, neutral, sjöfart ; fackspråklig, neutral, teknik",
     [],
     "Fartyget " + B % "anlöpte" + " Marseilles hamn tidigt på morgonen.",
     "→ Efter lagtyska anlopen, tyska anlaufen; samma rot som lopa.",
     "SO och SAOL ger bara sjofartsbetydelsen ('lagga till i' / 'lagga i "
     "land vid el. i'). Metallbetydelsen ('belaggas med rost eller arg, "
     "andra farg') star hos Wiktionary och ar en verklig fackterm inom "
     "metallbearbetning (anlopt stal). Den ar med, men markt som svagare "
     "belagd: den vilar pa EN kalla, inte pa SO. OLD-facit 'inkomma till "
     "hamns' ar ratt i sak men missar att uppehallet ar kort och planerat.",
     conf=7)

satt("autograf",
     "Namnteckning som en känd person skrivit för hand åt en beundrare ; "
     "också om annat som någon skrivit med egen hand",
     "neutral, neutral, allmän ; fackspråklig, neutral, allmän",
     [],
     "Stjärnorna skrev " + B % "autografer" + " för brinnande livet.",
     "→ Grekiska autographos, till auto- 'sjalv' och graphein 'skriva'.",
     "SO: 'egenhandig namnteckning'. SAOL preciserar: 'ofta av kand "
     "person' -- den preciseringen ar hela ordet och ar inskriven. "
     "Wiktionary ger dessutom den vidare betydelsen 'egenhandig "
     "handskrift', som ar med som andra betydelse. SO:s JFR signatur ar "
     "cohyponymmarkt och tas inte upp som synonym -- OLD-facit sa just "
     "'signatur', vilket ar for brett: vem som helst har en signatur, men "
     "bara den beromdes ar en autograf.")

satt("beriden",
     "Som sitter till häst i tjänsten, om polis eller soldat",
     "neutral, neutral, allmän",
     ["ridande"],
     "Den " + B % "beridna" + " gränspolisen patrullerade längs floden.",
     "→ Efter tyska beritten med samma betydelse.",
     "SO: 'utrustad med hast'. SAOL: 'ridande' -- darifran synonymen, ur "
     "definitionstexten. Wiktionary preciserar 'som rider pa hast i "
     "tjanst', och bada SO:s exempel (granspolis, hogvakt) galler tjanst. "
     "OLD-facit 'till hast' stammer men ar sa kort att det inte skiljer "
     "beriden fran 'ridande' i allmanhet.")

satt("beväring",
     "Förr: de yngsta årsklasserna av värnpliktiga soldater ; i "
     "finlandssvenska: en enskild soldat som gör sin värnplikt ; i "
     "vapensköldar: ett djurs klor, tänder och tunga",
     "ngt ålderdomlig, neutral, militär ; neutral, neutral, militär ; "
     "fackspråklig, neutral, historia",
     [],
     "Han exercerade " + B % "beväring" + " vid Svea livgarde.",
     "→ Till bevara i den aldre betydelsen 'utrusta med vapen'.",
     "SO ger tre betydelser: kollektivet av yngre varnpliktiga (markning: "
     "nagot alderdomligt), den enskilda varnpliktige (markning: finl., "
     "alltsa finlandssvenska) och den heraldiska ('ett djurs delar i en "
     "vapenskold'). Alla tre ar med. OLD-facit 'varnpliktig soldat' slog "
     "ihop de tva forsta och missade att svenskan i forsta hand anvander "
     "ordet om HELA argangen, inte om en person -- det ar den skillnaden "
     "som gor ordet svart.")

satt("boricka",
     "Åsna",
     "arkaisk, neutral, allmän",
     ["åsna"],
     "Bonden lastade sin " + B % "boricka" + " med tunga säckar.",
     "→ Franska bourrique 'asna'; av spanska borrico; ytterst av senlatin "
     "burricus 'liten fuxrod hast'.",
     "SO och SAOL ger bada exakt ett ord: 'asna', med markningen "
     "alderdomligt. Har finns ingenting att forklara ett steg neroat -- "
     "asna ar redan sa enkelt det gar, och att skriva ut mer skulle vara "
     "att hitta pa. Kortet ar alltsa avsiktligt ett rent glosekort. "
     "OLD-facit 'asna' stammer exakt.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("skrev %d kort" % sum(1 for k in KORT if k.get("approved")))
