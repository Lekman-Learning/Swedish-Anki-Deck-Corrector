# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch6, kort 41-60. Samma skarpta regler som del1."""
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


satt("fotogenisk",
     "Som tar sig bra ut på bild, även när personen inte är särskilt vacker "
     "i verkligheten",
     "vardaglig, positiv, allmän",
     [],
     "Hon är inte särskilt söt men hon har ett " + B % "fotogeniskt" +
     " utseende.",
     "→ Till foto och grekiskans -genes 'som ger upphov till'.",
     "SO: 'som tar sig bra ut pa fotografier', med markningen vard. Ledet "
     "'aven nar personen inte ar sarskilt vacker' star inte i definitionen "
     "men ar SO:s ENDA exempelmening, ordagrant -- det ar alltsa belagt och "
     "ar hela poangen med ordet: fotogenisk och vacker ar inte samma sak. "
     "OLD-facit 'som blir bra pa bild' ar SAOL:s ord och missar just det.")

satt("förmäten",
     "Som ställer krav långt över vad man har täckning för ; också om "
     "själva kravet eller handlingen",
     "neutral, negativ, allmän ; neutral, negativ, allmän",
     [],
     "Han är " + B % "förmäten" + " nog att tro att han kan bestämma över "
     "dem.",
     "→ Lagtyska vormeten, eg. particip av sik vormeten 'overskatta sig' -- "
     "ordagrant 'mata fel'.",
     "SO: 'som framfor alltfor oblyga krav eller ansprak', med "
     "underbetydelsen 'av. om handling och dylikt' (SO:s exempel: deras "
     "formatna krav). Bada ar med. SO:s JFR (ansprakfull, pretentios) ar "
     "cohyponymmarkta och tas INTE upp som synonymer -- OLD-facit "
     "'overmodig; ansprakfull' var just en sadan rad, och den missar att "
     "formatenhet handlar om att KRAVA nagot man inte har tackning for, "
     "inte om sjalvbild i allmanhet. Etymologin ar med for att den gor "
     "ordet genomskinligt.")

satt("gerilla",
     "Väpnad grupp utanför den reguljära armén som slåss i små enheter med "
     "snabba överfall",
     "neutral, neutral, militär",
     [],
     B % "Gerillan" + " gjorde en hastig attack och försvann sedan "
     "spårlöst.",
     "→ Spanska guerilla, diminutiv till guerra 'krig' -- alltsa 'litet "
     "krig'.",
     "SO: 'icke-reguljara militara trupper som arbetar i sma enheter'. "
     "SAOL: 'forband som for partisankrig'. SO:s JFR partisan ar "
     "cohyponymmarkt. OLD-facit 'motstandsrorelse' ar for brett och delvis "
     "fel: en motstandsrorelse behover varken vara vapnad eller organiserad "
     "i militara enheter, och det ar just de tva dragen som definierar en "
     "gerilla.")

satt("gourmet",
     "Person som är kunnig om mat och lägger stor vikt vid kvalitet och "
     "smak",
     "neutral, neutral, allmän",
     [],
     "En " + B % "gourmet" + " som reser långt för en enda måltid.",
     "→ Franska gourmet; av fornfranska gromet 'vinhandlardrang'.",
     "SO: 'person som lagger stor vikt vid god mat'. SAOL: 'finsmakare; "
     "vin- och matkannare'. INGEN synonym ar upptagen, trots att SO har en "
     "SYN-markering i uppslaget: markeringarna kommer i ordningen "
     "SYN, JFR, JFR mot listan lackergom, finsmakare, gourmand, och det gar "
     "inte att sakert lasa ut VILKET av de tre som ar SYN-markt. En "
     "oklar markering duger inte som belagg. VIKTIG FALLA: gourmand (SO:s "
     "JFR) ar den vanligaste forvaxlingen -- en gourmand ater MYCKET, en "
     "gourmet ater VAL.")

satt("hälare",
     "Person som köper stöldgods och säljer det vidare",
     "neutral, negativ, juridik",
     [],
     B % "Hälaren" + " dömdes hårdare än tjuven som utfört inbrottet.",
     "→ Tyska Hehler, till hehlen 'dolja, gomma'.",
     "SO:s hela definition ar 'person som gjort sig skyldig till haleri' -- "
     "cirkulart for den som inte redan kan ordet haleri, och darfor "
     "utskrivet enligt Adam-tal. Innehallet kommer fran Wiktionary: 'person "
     "som koper och saljer stoldgods'. SAOL har ingen artikel. OLD-facit "
     "'tjuvgodskopare' ar ratt i sak men missar VIDAREFORSALJNINGEN, som ar "
     "det brottet bestar i -- den som koper stoldgods for eget bruk ar "
     "ocksa halare, men det ar handeln lagen siktar pa.")

satt("ity att",
     "Därför att — ett gammalt sätt att inleda en förklaring",
     "arkaisk, neutral, allmän",
     [],
     "Hon avstod från att uppträda " + B % "ity att" + " hennes sångröst var "
     "minimal.",
     "→ Till ty i den aldre betydelsen 'darfor'.",
     "SO: 'av den anledningen (att)', med markningen alderdomligt; SAOL: "
     "'darfor att', markt ald. NOT OM UPPSLAGNINGEN: sokningen drog med sig "
     "artikeln for subjunktionen ATT (basala subjunktioner, 'att du inte "
     "skams!') -- den har ingenting med uttrycket att gora och ar inte "
     "anvand. Bara den forsta definitionen och SO:s exempelmening hor till "
     "ity att. OLD-facit 'darfor att, eftersom' stammer.")

satt("jokk",
     "Bäck eller å i fjällen",
     "dialektal, neutral, allmän",
     [],
     "De vadade över " + B % "jokken" + " där vattnet gick till knäna.",
     "→ Samiska jokk 'forsande vattendrag'.",
     "SO: 'fjallback', SAOL: 'back, a sarsk. i Lappland', med markningen "
     "prov. (provinsiellt) -- darav registret dialektal. Bada kallorna ar "
     "med: SO begransar till fjallen, SAOL till Lappland och tillater bade "
     "back och a. OLD-facit 'fjallback' ar SO:s ord men utesluter a:ar, som "
     "SAOL tar med.")

satt("katamaran",
     "Båt med två smala skrov som sitter ihop ovanför vattenytan",
     "neutral, neutral, sjöfart",
     [],
     B % "Katamaranen" + " går snabbare än en enskrovsbåt av samma storlek.",
     "→ Via engelskan av tamil kattumaram, till kattu 'binda' och maram "
     "'tradstam' -- hopbundna tradstammar.",
     "SO: 'typ av bat som bestar av tva smala skrov som ar parallellt "
     "forbundna over vattenlinjen'. Att skroven sitter ihop OVANFOR vattnet "
     "ar det avgorande och ar med -- OLD-facit 'tvadelad bat' later som en "
     "bat som gatt sonder. Snabbheten kommer fran SAOL ('snabbgaende bat "
     "med tva skrov') och ar exempelmeningens grund. SO:s JFR trimaran ar "
     "cohyponym: samma sak med tre skrov.")

satt("kommissionär",
     "Person eller firma som köper och säljer i eget namn men för någon "
     "annans räkning ; tjänsteman som mot arvode utför ärenden åt "
     "allmänheten ; ledamot av EU-kommissionen",
     "fackspråklig, neutral, ekonomi ; fackspråklig, neutral, juridik ; "
     "neutral, neutral, politik",
     [],
     "Sveriges " + B % "kommissionär" + " fick ansvaret för handelsfrågor.",
     "→ Franska commissionnaire; till kommission.",
     "SO ger TRE betydelser och SAOL bekraftar alla tre: handelsombudet, "
     "tjanstemannen och EU-ledamoten (SO: 'sarsk. om ledamot av "
     "EU-kommissionen, ett av EU:s viktigaste organ'). Alla ar med. "
     "OLD-facit 'ombud, mellanhand' var en synonymrad som tackte den forsta "
     "och missade EU-betydelsen helt -- den enda av de tre en lasare "
     "faktiskt moter i en nyhetstext i dag, och darfor vald till "
     "exempelmening. Ledet 'i eget namn men for annans rakning' ar den "
     "juridiska karnan i kommission och skiljer kommissionaren fran ett "
     "vanligt ombud.")

satt("kräslig",
     "Överdådigt läcker och yppig, om mat eller ett liv i lyx",
     "neutral, neutral, allmän",
     [],
     "En " + B % "kräslig" + " måltid med sju rätter och vin till varje.",
     None,
     "SVAGT BELAGD: SO har ingen artikel. SAOL ger 'lacker; overdadig' och "
     "Wiktionary 'overdadig, yppig; lacker; forfinad' -- facit ar byggt av "
     "de ord bada kallorna delar. Ingen bruklighetsmarkning finns hos SAOL, "
     "sa registret ar neutralt trots att ordet ar sallsynt; att SAOL har "
     "ordet alls betyder att det raknas till nutida svenska, till skillnad "
     "fran misskundsam tidigare i dag. OLD-facit 'vacker, utsokt, "
     "overdadig' innehaller 'vacker', som saknas i bada kallorna och ar "
     "struket.",
     conf=7)

satt("memoarer",
     "Samlade nedtecknade minnen från någons eget liv",
     "neutral, neutral, litteraturvetenskap",
     [],
     "Han satt i tio år och skrev sina " + B % "memoarer" + ".",
     "→ Franska mémoire 'minne'; av latin memoria; samma rot som memorera "
     "och promemoria.",
     "NOT OM UPPSLAGNINGEN: sokningen pa pluralformen 'memoarer' gav "
     "traffar=INGEN i samtliga kallor -- ordboken indexerar singularformen. "
     "En SEPARAT uppslagning pa 'memoar' gjordes darfor (svenska.se HTTP "
     "200, traffar=saol,so,saob) och ar underlaget: SO och SAOL ger bada "
     "'samlade levnadsminnen', Wiktionary '(bok dar en person berattar "
     "sina) levnadsminnen'. Ordet 'levnadsminnen' ar utskrivet enligt "
     "Adam-tal. SO:s JFR sjalvbiografi ar cohyponymmarkt och tas inte upp: "
     "en sjalvbiografi tacker hela livet i sammanhang, memoarer ar "
     "nedslag. OLD-facit 'nedtecknade levn.minnen' stammer.")

satt("måndagsexemplar",
     "Exemplar av en vara som råkat bli slarvigt tillverkat",
     "vardaglig, negativ, allmän",
     [],
     "Hans nya bil verkade vara ett " + B % "måndagsexemplar" + ".",
     None,
     "SO: 'slarvigt tillverkat exemplar', med markningen vard. SAOL: "
     "'daligt exemplar'. Wiktionary lagger till 'produkt med "
     "produktionsfel'. Ordet 'rakat' ar med for att markera att det galler "
     "ett ENSKILT exemplar ur en i ovrigt bra serie -- det ar hela "
     "skillnaden mot en dalig produkt, och OLD-facit 'dalig vara' suddar "
     "den. Namnets ursprung (tanken att varor tillverkade pa mandagar blir "
     "samre) star INTE i nagon av kallorna och ar darfor inte inskrivet som "
     "etymologi.")

satt("nitid",
     "Liten, prydlig och tydlig — särskilt om handstil",
     "ngt ålderdomlig, positiv, allmän",
     [],
     "Hon skrev med en " + B % "nitid" + " handstil som gick att läsa på "
     "långt håll.",
     "→ Latin nitidus 'blank, glansande'; samma rot som netto och natt.",
     "SO: 'liten och prydlig'. SAOL: 'prydlig och tydlig'. Bada kallorna "
     "bidrar med ett eget led -- SO:s 'liten' och SAOL:s 'tydlig' -- och "
     "bada ar med, eftersom ingendera ensam ar tillracklig. SO:s markning: "
     "mindre brukligt. Wiktionary preciserar 'i sht om handstil', vilket ar "
     "med. OLD-facit 'prydlig' tackte en tredjedel.")

satt("odör",
     "Lukt, oftast obehaglig",
     "neutral, lätt negativ, allmän",
     [],
     "Det förekom ofta en svag " + B % "odör" + " av sopor i trapphuset.",
     "→ Franska odeur 'lukt, doft'; av latin odor; samma rot som "
     "deodorant.",
     "SO: '(otrevlig) lukt' -- parenteserna ar SO:s egna och betyder att "
     "obehaget ar det VANLIGA men inte tvingande, vilket facit speglar med "
     "'oftast'. SO:s JFR stank ar cohyponymmarkt och tas inte upp: en stank "
     "ar alltid stark och alltid obehaglig, en odor kan vara svag (SO:s "
     "eget exempel). OLD-facit 'lukt, stank' gav bada ytterligheterna och "
     "traffade darfor ingen av dem.")

satt("preciös",
     "Överdrivet förfinad och tillgjord i sitt sätt eller sitt språk ; "
     "historiskt: medlem av en fransk litterär krets under barocken som "
     "odlade just en sådan förfining",
     "ngt ålderdomlig, lätt negativ, allmän ; fackspråklig, neutral, "
     "litteraturvetenskap",
     [],
     "Uppsatsen var något " + B % "preciös" + " och omständlig.",
     "→ Franska précieux 'dyrbar'; samma rot som preciosa.",
     "SO ger tva betydelser: 'overdrivet forfinad' och 'medlem av en fransk "
     "litterar riktning under barocken, som efterstravade spraklig "
     "forfining'. Bada ar med -- den andra ar en person, inte en egenskap, "
     "och skulle ha fallit bort vid en hopslagning. SAOL bekraftar bada "
     "('forkonstlad, overforfinad | precios person'). SO:s markning: ald. "
     "SO:s JFR forkonstlad ar cohyponymmarkt. OLD-facit 'tillgjord, "
     "konstlad' tackte bara den forsta.")

satt("struma",
     "Sjuklig förstoring av sköldkörteln",
     "fackspråklig, neutral, medicin",
     [],
     "Vissa former av " + B % "struma" + " förebyggs genom att jod tillsätts "
     "i salt.",
     "→ Latin struma 'kortelsvulst'.",
     "SO: 'forstoring av skoldkorteln'. SAOL: 'en sjukdom med forstoring av "
     "skoldkorteln'. Ordet SJUKLIG kommer fran Wiktionary och SAOL:s "
     "'sjukdom' och ar med, eftersom skoldkorteln kan vaxa av naturliga "
     "skal utan att det ar struma. Att svullnaden syns pa halsen ar allmant "
     "kant men star inte i nagon av kallorna och ar darfor INTE inskrivet. "
     "OLD-facit 'sjukdom i skoldkortlen' ar for brett -- struma ar en "
     "sarskild forandring, inte vilken skoldkortelsjukdom som helst.")

satt("teknikalitet",
     "Teknisk detalj inom ett fackområde ; också om en ren formalitet som "
     "avgör en sak trots att den saknar betydelse i sak",
     "neutral, neutral, allmän ; neutral, neutral, juridik",
     [],
     "Vi kan inte här gå in på alla lagstiftningens " + B % "teknikaliteter"
     + ".",
     "→ Efter engelska technicality; till teknik.",
     "SO: 'fackmassig finess'. SAOL ger TVA led atskilda med semikolon: "
     "'teknisk detalj; formalitet' -- alltsa tva betydelser, och bada ar "
     "med. Den andra ar den som anvands i uttryck som 'friad pa en "
     "teknikalitet' och ar helt franvarande hos SO. OLD-facit 'detalj; "
     "formalitet' hade bada men utan att saga vilket omrade det galler.")

satt("transversal",
     "I matematiken: linje som skär två eller flera andra linjer ; som "
     "adjektiv: tvärgående",
     "fackspråklig, neutral, matematik ; fackspråklig, neutral, allmän",
     [],
     B % "Transversalen" + " skär de båda parallella linjerna i var sin "
     "punkt.",
     "→ Till latin transversus 'vand pa tvaren'.",
     "SO ger tva: substantivet 'linje som skar tva eller flera andra "
     "linjer' (markning: matematik) och adjektivet 'transversell', dvs. "
     "tvargaende (markning: mindre brukligt). Bada ar med -- de ar olika "
     "ordklasser. OLD-facit 'tvargaende' hade bara adjektivet och missade "
     "substantivet, som ar den betydelse ordet nastan alltid har i text.")

satt("tålig",
     "Om en person: som uthärdar smärta eller besvär utan att klaga ; som "
     "står ut med besvärliga människor utan att bli irriterad ; om ett "
     "material eller en sak: som klarar påfrestningar utan att ta skada",
     "neutral, positiv, allmän ; neutral, positiv, allmän ; neutral, "
     "neutral, teknik",
     [],
     "Hon var " + B % "tålig" + " och rörde inte en min trots smärtorna.",
     "→ Fornsvenska tholugher; till tala.",
     "SO ger TRE betydelser: 'som kan uthärda pafrestningar utan att klaga' "
     "(om en person och egen smarta), 'som kan uthärda ooonskade "
     "foreteelser utan att bli irriterad' (om andra manniskor -- SO:s "
     "exempel: han var forbluffande talig mot barnen) och 'som motstar "
     "pafrestningar utan att ta skada' (om saker). Alla tre ar med. De tva "
     "forsta later lika men ar olika: den ena handlar om vad man star ut "
     "med SJALV, den andra om vad man star ut med hos ANDRA. Belaggen "
     "skiljer dem med 567 ar (1320 mot 1887). OLD-facit "
     "'motstandskraftig' tackte bara den tredje.")

satt("åthävor",
     "Synliga gester och rörelser i sättet att uppträda ; ofta om ett sätt "
     "som märks alltför mycket",
     "neutral, neutral, allmän ; neutral, lätt negativ, allmän",
     [],
     "Han lämnade mötet under stora " + B % "åthävor" + ".",
     "→ Fornsvenska athäva 'uppforande, beteende', till hava sik at 'bete "
     "sig'; samma rot som ha och havd.",
     "SO: 'iakttagbart satt att bete sig', med underbetydelsen 'ofta om "
     "alltfor markbart satt att bete sig'. Bada ar med, och skillnaden "
     "syns i SO:s tva exempel: 'foredomligt lugnt och UTAN athavor' mot "
     "'lamnade motet UNDER STORA athavor'. Ordet ar alltsa neutralt i sig "
     "men bar oftast en overdrift. SO:s JFR later ar cohyponymmarkt. "
     "OLD-facit 'maner, later; gester' var en synonymrad; ingen av de tre "
     "ar upptagen.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("skrev %d kort totalt" % sum(1 for k in KORT if k.get("approved")))
