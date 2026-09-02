# -*- coding: utf-8 -*-
"""Batch D: kort 54-75 (ackja .. descendent). Plus tre fix i batch C."""
import io, json, os, sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02_v3-batch.json"
H = '<font color="#3498db">%s</font>'


def kallor(o):
    d = json.load(io.open(os.path.join("uppslag", o + ".json"), encoding="utf-8"))
    u = d.get("urler") or {}
    return " ".join(u[k] for k in ("svenska.se", "synonymer.se", "wiktionary") if u.get(k))


# --- fix i batch C -------------------------------------------------------
REG_FIX = {
 "hermetisk": "fackspråklig (fysik, kemi) i betydelse 1, formell i betydelse 2",
 "ämbete": "formell, ofta i kyrkliga sammanhang",
}
FIX_TILLAT = {
 "upprätta": {"frammande_uppslagsord":
   "Det frammande uppslagsordet ar adjektivet 'upprätt' (staende rak), ett annat lemma "
   "som fritextsokningen drar med sig. Ingenting darifran har anvants; kortets bada "
   "betydelser kommer ur verbet upprättas egna SO-poster."},
}

K = {}

K["ackja"] = (
 "Samisk båtliknande släde, avsedd att dras av ren",
 "neutral, mest historisk",
 ["samisk båtliknande släde"],
 None,
 "De lastade utrustningen i en " + H % "ackja" + " och lät renen dra den över fjället.",
 "till samiskans akja",
 "SO: 'typ av (samisk) slade med batliknande konstruktion' med tillagget 'avsedd att dras "
 "av renar'. BADA leden ar nodvandiga: batformen skiljer ackjan fran andra slädar, och "
 "rendraget forklarar varfor formen ser ut som den gor. SAOL: 'samisk batliknande slade'.")

K["additament"] = (
 "Tillägg eller ändring, särskilt i en skriven handling",
 "formell, ålderdomlig",
 ["tillägg"],
 None,
 "Testamentet kompletterades med ett " + H % "additament" + " några månader före hans död.",
 "latinets additamentum 'tillagg', till addere 'lagga till'",
 "SO: 'tillagg eller andring'. Kort och entydig definition. Ordet ar juridiskt/formellt "
 "och moter nastan bara i skrift, vilket registret markerar; SO:s definition sager inte "
 "det uttryckligen men bruket gor det.")

K["amorin"] = (
 "Kärleksgud avbildad som ett bevingat barn",
 "neutral, konsthistorisk",
 ["kupidon", "kärleksgud"],
 None,
 "Takmålningen var full av " + H % "amoriner" + " som sköt pilar mot varandra.",
 "italienskans amorino, diminutiv av amore 'karlek'",
 "SO: 'karleksgud i ett bevingat barns gestalt'. BARNGESTALTEN ar hela ordet - en amorin "
 "ar inte vilken karleksgud som helst utan just den avbildade som ett litet bevingat barn, "
 "och det ar sa ordet anvands i konsthistoria. 'kupidon' godtas som synonym ur SAOL.")

K["anarki"] = (
 "Frånvaro av styrande makt ; upplösning av samhällsordningen",
 "neutral",
 ["laglöshet", "upplösning av samhällsordningen"],
 None,
 "Efter regimens fall rådde " + H % "anarki" + " i huvudstaden i flera veckor.",
 "grekiskans anarchia 'harskarlosthet', av an- 'utan' och archos 'harskare'",
 "SO: 'franvaro av styrande och kontrollerande makt' plus 'upplosning av "
 "samhallsordningen'. Antalet pa kortet matchar SO:s. SKILJ: anarki som SAKLAGE (kaos) "
 "ar inte samma sak som anarkism, den politiska laran - kortet lar ut det forsta.")

K["antracit"] = (
 "Stenkol med särskilt hög kolhalt",
 "fackspråklig, geologi",
 ["stenkol med hög kolhalt"],
 None,
 "Kaminen eldades med " + H % "antracit" + ", som brinner hetare och renare än vanligt kol.",
 "grekiskans anthrax 'kol'",
 "SO: 'typ av stenkol med hog kolhalt'. HOGA KOLHALTEN ar det enda som skiljer antracit "
 "fran stenkol i allmanhet och maste sta kvar. Ordet anvands ocksa om en morkgra farg, "
 "men den anvandningen saknar ordboksbelagg i de hamtade kallorna och skrivs darfor inte "
 "in.")

K["ballad"] = (
 "Berättande visa i folkvisestil ; sång eller musikstycke i lugn stil",
 "neutral",
 ["medeltida dansvisa", "dikt i folkvisestil"],
 [["medeltida dansvisa", "dikt i folkvisestil"], []],
 "Han avslutade konserten med en långsam " + H % "ballad" + " vid pianot.",
 "provensalskans balada 'dansvisa', till ballar 'dansa'",
 "SO: 'typ av berattande visa' plus 'dikt i folkvisestil' och 'sang el. musikstycke i lugn "
 "stil ibl. av jazzkaraktar'. TVA betydelser pa kortet: den litterara/medeltida och den "
 "moderna musikaliska. Etymologin forklarar forskjutningen - ordet borjade som DANSVISA, "
 "vilket ar varfor en modern ballad ar langsam snarare an berattande.")

K["bane"] = (
 "Orsak till någons död ; den som vållar döden",
 "ålderdomlig, högtidlig",
 ["dråpare", "våldsam död"],
 None,
 "Högmodet blev till slut hans " + H % "bane" + ".",
 None,
 "TVA AV TRE KALLOR: ordet har INGEN SO-artikel (0 def). Betydelsen vilar pa SAOL och "
 "SAOB, som ger 'orsak till ngns dod', 'valdsam dod' och 'drapare'. Ordet lever i nutida "
 "svenska nastan bara i uttrycket 'bli ngns bane', dar det ar orsaken snarare an personen "
 "som avses - darfor star orsaksbetydelsen forst.")

K["belacka"] = (
 "Tala illa om någon bakom hans rygg",
 "formell, ålderdomlig",
 ["förtala", "smäda"],
 None,
 "Han " + H % "belackade" + " sina kollegor i varje samtal han förde med chefen.",
 None,
 "SO: 'tala illa om eller uttrycka sitt (moraliska) ogillande av'. BAKOM RYGGEN star inte "
 "uttryckligen i definitionen men foljer av bruket och av att ordet nastan alltid har en "
 "franvarande person som objekt; det ar preciserat i huvudbetydelsen eftersom ett kort som "
 "bara sa 'tala illa om' inte skulle skilja belacka fran att kritisera oppet. SAOL: "
 "'fortala, smada'.")

K["bestyr"] = (
 "Sysslor och göromål som måste uträttas",
 "neutral, något ålderdomlig; ofta i plural",
 ["syssla"],
 None,
 "Hon hade tusen " + H % "bestyr" + " att hinna med före avresan.",
 None,
 "SO: 'som maste goras' plus 'syssla'. TVANGET ar med i definitionen - ett bestyr ar inte "
 "vad som helst man gor utan nagot som ska uträttas - och star darfor kvar. Ordet moter "
 "nastan alltid i plural, vilket registret markerar.")

K["bevågen"] = (
 "Välvilligt inställd till någon",
 "formell, ålderdomlig",
 ["gunstig", "välvillig"],
 None,
 "Lyckan var honom " + H % "bevågen" + " den dagen.",
 None,
 "SO: 'valvillig till'. SAOL: 'gunstig'. Ordet ar predikativt och kraver ett dativliknande "
 "objekt ('vara ngn bevagen'), vilket ar den enda konstruktion det moter i - "
 "exempelmeningen visar den. Bada synonymerna godtas ur ordbokstexten.")

K["blankvers"] = (
 "Versmått med orimmade rader om fem jambiska takter",
 "fackspråklig, litteraturvetenskap",
 [],
 None,
 "Shakespeares pjäser är till största delen skrivna på " + H % "blankvers" + ".",
 None,
 "TVA AV TRE KALLOR. SO: 'ett versmatt med orimmade jambiska rader med fem takter'. SAOL: "
 "'ett versmatt utan rim och med fem tvastaviga stigande takter per rad' - samma sak med "
 "jamben utskriven som 'tvastavig stigande'. Bada ar hela definitionsstrangar utan kort "
 "synonym, sa faltet lamnas tomt. TRE drag maste sta kvar: orimmat, femtaktigt, jambiskt "
 "- tas nagot bort beskriver definitionen ett annat versmatt.")

K["blott"] = (
 "Bara, endast ; om bara, under förutsättning att ; blottad och oskyddad",
 "ålderdomlig eller högtidlig",
 ["bara", "endast", "enbart"],
 [["bara", "endast", "enbart"], [], []],
 "Han var " + H % "blott" + " sexton år när han skrev sin första symfoni.",
 None,
 "TRE betydelser i SO, av tre olika ordklasser: adverbet 'bara/endast', konjunktionen 'om "
 "bara / under den enda (lattuppfyllda) forutsattningen att', och adjektivet 'oppen eller "
 "oskyddad' (jfr blotta). Att samma form bar tre ordklasser ar sjalva svarigheten med "
 "ordet. Synonymerna galler bara adverbbetydelsen; de tva andra saknar korta belagda "
 "synonymer.")

K["bobin"] = (
 "Spole eller rulle som garn vindas upp på",
 "fackspråklig, textil",
 ["rulle", "spolstomme"],
 None,
 "Tråden matades av från en " + H % "bobin" + " högst upp på maskinen.",
 "franskans bobine 'spole'",
 "SO: 'spolstomme dar garnet vindas upp'. SAOL: 'rulle el. stallning for uppvindning av "
 "garn'. Kallorna skiljer sig: SO sager STOMME (den nakna kärnan), SAOL aven 'stallning'. "
 "Huvudbetydelsen tar den gemensamma karnan - foremalet garnet lindas pa - utan att valja "
 "sida i den detaljen.")

K["bombasm"] = (
 "Uppblåst och anspråksfullt sätt att uttrycka sig",
 "formell, nedsättande",
 ["svulstigt uttryckssätt"],
 None,
 "Talet var ren " + H % "bombasm" + " — många ord, inget innehåll.",
 None,
 "SO: 'sprakligt uttryck som ar ansprakfullt och uppblast'. SAOL: 'svulstigt "
 "uttryckssatt'. NEDSATTANDET ar inbyggt: bombasm ar aldrig ett berom, och det star i "
 "registret. Ordet ar besläktat med bombastisk, som ar det vanligare adjektivet - "
 "substantivet ar det som provas.")

K["bonnett"] = (
 "Styv damhatt med hakband och stort frambrätte",
 "neutral, mest historisk",
 [],
 None,
 "På fotot bär hon en svart " + H % "bonnett" + " knuten under hakan.",
 "franskans bonnet 'mossa, hatta'",
 "SO: 'typ av styv damhatt med hakband'. SAOL preciserar: 'styv hatt med hakband och stort "
 "frambratte sarsk. for kvinnliga fralsningssoldater'. FRAMBRATTET och HAKBANDET ar det "
 "som gor formen igenkannbar och star darfor bada i huvudbetydelsen. Poolen innehaller "
 "bara hela definitionsstrangar, sa synonymfaltet lamnas tomt.")

K["bängel"] = (
 "Ohyfsad och besvärlig pojke",
 "vardaglig, nedsättande",
 ["slyngel", "ohyfsad pojke"],
 None,
 "Ungen var en riktig " + H % "bängel" + " som inte lydde ett ord.",
 None,
 "SO: 'ohyfsad pojke'. SAOL: 'slyngel'. KONET och ALDERN ligger i definitionen - en bangel "
 "ar en pojke, inte vem som helst - och star kvar. Ordet ar nedsattande men inte grovt, "
 "narmast skamtsamt-uppgivet i bruk.")

K["båga"] = (
 "Bluffa eller luras",
 "vardaglig, ålderdomlig",
 ["bluffa", "fuska", "ljuga"],
 None,
 "Han " + H % "bågade" + " sig igenom hela provet utan att ha läst en rad.",
 None,
 "TVA AV TRE KALLOR: ordet har INGEN SO-artikel (0 def). Betydelsen vilar pa SAOL och "
 "SAOB, som ger 'bluffa', 'fuska' och 'ljuga'. Alla tre pekar at samma hall - att skaffa "
 "sig fordel genom att forege nagot man inte har - och tas som synonymer. Ordet ar "
 "nastan utdott i nutida svenska.")

K["bökig"] = (
 "Obekväm och stökig ; rörig och besvärlig att hantera",
 "vardaglig",
 ["obekväm", "rörig", "ostrukturerad"],
 None,
 "Det blev " + H % "bökigt" + " att bära soffan uppför den smala trappan.",
 None,
 "SO ger 'obekvam och stokig' plus 'rorig' och 'ostrukturerad'. TVA praktiskt atskilda "
 "innebordar: nagot som ar fysiskt besvarligt att gora, och nagot som ar oordnat. Bada "
 "moter i vardagsspraket och star pa kortet. Endast SAOL och SO; ordet ar for ungt for "
 "SAOB.")

K["chikan"] = (
 "Skymf och vanheder ; konstgjord kurva på en tävlingsbana ; brist på trumf i kortspel",
 "formell i betydelse 1; betydelse 2 och 3 fackspråkliga",
 ["skymf", "vanheder", "förolämpning", "renons"],
 [["skymf", "vanheder", "förolämpning"], [], ["renons"]],
 "Att bli utesluten ur inbjudan uppfattade han som en medveten " + H % "chikan" + ".",
 "franskans chicane 'trakasseri, spetsfundighet'",
 "TRE betydelser, alla egna SO-huvudbetydelser: 'skam, skymf, vanheder', 'konstgjord kurva "
 "t.ex. pa tavlingsbana for racerbilar' och 'brist pa trumf i kortspel' (= renons). De tre "
 "har inget synligt samband, vilket gor ordet till en typisk provfalla - man kanner igen "
 "racerbanebetydelsen fran sport och gissar fel i en text om harskarteknik.")

K["cistern"] = (
 "Stor cylindrisk behållare för vätska eller gas",
 "neutral",
 [],
 None,
 "Oljan lagrades i en " + H % "cistern" + " på hamnområdet.",
 "latinets cisterna 'vattenbehallare', till cista 'kista, lada'",
 "SO: 'stor (cylindrisk) behallare for vatska eller gas'. SAOL: 'storre behallare for "
 "vatska t.ex. olja'. STORLEKEN ar en del av definitionen i bada kallorna - en cistern ar "
 "aldrig liten. Cylinderformen star inom parentes i SO och ar alltsa typisk men inte "
 "kravd; den behalls utan parentes eftersom den ar vad ordet frammanar. Poolen ger bara "
 "hela definitionsstrangar, sa synonymfaltet lamnas tomt.")

K["dagdrivare"] = (
 "Person som låter tiden gå utan att uträtta något",
 "nedsättande",
 [],
 None,
 "Han kallade dem " + H % "dagdrivare" + " som aldrig gjort ett ärligt dagsverke.",
 None,
 "SO: 'person som later tiden ga utan att utratta ngt'. SAOL: 'person som gar sysslolos'. "
 "Bada ar hela relativsatser utan kort synonym, sa faltet lamnas tomt. NEDSATTANDET ar "
 "inbyggt i ordet men star inte som markning i kallorna; det foljer av att ingen kallar "
 "sig sjalv dagdrivare, och skrivs i registret.")

K["descendent"] = (
 "Ättling i rakt nedstigande led ; i astrologi: det stjärntecken som går ned i horisonten "
 "vid någons födelse",
 "formell, fackspråklig",
 ["ättling"],
 None,
 "Han kunde spåra sig själv som " + H % "descendent" + " till en av de första nybyggarna.",
 "latinets descendens 'nedstigande', till descendere 'stiga ned'",
 "TVA betydelser, bada egna SO-huvudbetydelser: 'attling i rakt nedstigande led' och 'det "
 "stjarntecken som gar ner i horisonten vid en manniskas fodelse'. RAKT NEDSTIGANDE ar "
 "juridiskt precist och maste sta kvar - syskonbarn ar inte descendenter. Motsatsen ar "
 "ascendent, som bar samma tudelning (forfader / uppstigande tecken); etymologin "
 "'nedstigande' forklarar bada betydelserna pa en gang.")


TILLAT = {
 "ballad": {"betydelse_kan_saknas":
   "SO raknar 3: 'typ av berattande visa' plus underbetydelserna 'dikt i folkvisestil' och "
   "'sang el. musikstycke i lugn stil'. De tva forsta ar samma litterara betydelse i tva "
   "formuleringar; kortet slar ihop dem och behaller den moderna musikaliska som egen."},
 "bestyr": {"betydelse_kan_saknas":
   "SO raknar 4: 'som maste goras' och 'syssla' ar samma innebord i tva formuleringar, och "
   "de tva ovriga ar underbetydelser utan egen definition. Ordet har en betydelse."},
 "bevågen": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse."},
 "blott": {"betydelse_kan_saknas":
   "SO raknar 5; tva ar underbetydelser utan egen definition. Kortets tre betydelser "
   "motsvarar SO:s tre riktiga def, en per ordklass (adverb, konjunktion, adjektiv)."},
 "bökig": {"betydelse_kan_saknas":
   "SO raknar 5: tre def varav 'rorig' och 'ostrukturerad' ar samma innebord, plus tva "
   "underbetydelser utan egen definition. Kortets tva betydelser tacker bada de "
   "sarskiljbara innebordarna."},
 "descendent": {"betydelse_kan_saknas":
   "SO raknar 5; tre ar underbetydelser utan egen definition. Kortets tva betydelser "
   "motsvarar SO:s tva riktiga def (slaktled och astrologi)."},
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
print("batch D: %d kort, %d motiveringar, %d fix i batch C" % (n, t, f))
saknas = [o for o in K if not any(e["ord"] == o for e in poster)]
print("ord i K som inte fanns i filen:", saknas or "inga")
