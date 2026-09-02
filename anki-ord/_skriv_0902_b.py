# -*- coding: utf-8 -*-
"""Batch B: kort 19-33 (stangel .. fiffa upp). Index 18 (strog) hoppas over.

Synonymerna ar valda ENDAST ur _pool.py:s lista over vad forgranska godtar.
Tom lista dar poolen bara innehaller hela definitionsstrangar -- det ar
godkant och normalfallet.
"""
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

K["stängel"] = (
 "Stam på en ört, som bär en eller flera blommor",
 "neutral",
 ["bladlös stjälk"],
 None,
 "Blomman satt högst upp på en lång, tunn " + H % "stängel" + ".",
 None,
 "SO: 'stam pa ort' med tillagget 'som bar en el. flera blommor (och hogblad)'. SAOL: "
 "'bladlos stjalk'. Kallorna kompletterar varandra: SO sager vad stangeln BAR, SAOL att "
 "den saknar blad. Bada dragen star i huvudbetydelsen. 'stam' ensamt tas inte som synonym "
 "- en stam pa ett trad ar ingen stangel; det ar ORT-ledet som gor definitionen.")

K["tala med kluven tunga"] = (
 "Säga en sak men mena en annan, eller säga olika saker till olika personer",
 "neutral, bildlig",
 [],
 None,
 "Ledningen " + H % "talade med kluven tunga" + " — ett budskap till personalen, ett annat till ägarna.",
 None,
 "FLERORDSUTTRYCK. Ingen av kallorna har uttrycket som eget uppslagsord; sokningen "
 "returnerar i stallet de fyra ingaende orden (tala, med, kluven, tunga) med sammanlagt 9 "
 "betydelser, samtliga irrelevanta - inklusive 'typ av plattfisk' och 'skena pa "
 "transportmedel'. Den enda posten som ror uttrycket ar SO:s 'kluven' i betydelsen "
 "'vacklande nar det galler att ta stallning'. Betydelsen ar darfor byggd pa idiomets "
 "etablerade innebord med stod av just den posten, och synonymfaltet lamnas TOMT hellre "
 "an att fyllas med ett ord fran fel lemma.")

K["trema"] = (
 "Två punkter satta över en vokal för att visa att den ska uttalas för sig, som i franskans ë",
 "fackspråklig, språkvetenskap",
 [],
 None,
 "Namnet Noël skrivs med " + H % "trema" + " för att e:et inte ska smälta ihop med o:et.",
 "grekiskans trema 'hål, öppning'",
 "SO: 'ett uttalstecken i form av tva punkter som satts over den ena av tva angransande "
 "vokaltecken for att markera att de ska uttalas var for sig', med tillagget att det "
 "forekommer bl.a. i franskan (som i 'e'). SAOL: 'tva punkter satta over vokal forekommande "
 "bl.a. i franska'. Bada ar hela definitionsstrangar utan kort synonym, sa synonymfaltet "
 "lamnas tomt. FUNKTIONEN (att hindra diftong) ar det som gor kortet anvandbart och star "
 "darfor i huvudbetydelsen, inte bara formen.")

K["vresig"] = (
 "Om träd: låg och krokig i stammen ; om person: irriterad och ovänlig",
 "neutral",
 ["knotig", "irriterad", "tvär"],
 [["knotig"], ["irriterad", "tvär"]],
 "Han svarade " + H % "vresigt" + " och gick därifrån utan att säga vad som var fel.",
 None,
 "TVA betydelser, bada egna huvudbetydelser i SO: 'som har lag, krokig stam' om trad, och "
 "'irriterad och ovanlig' med tillagget 'ofta p.g.a. outtalat missnoje'. SAOL markerar "
 "domanen explicit i bada: 'om trad: forvriden, knotig' och 'om person: butter, tvar'. "
 "Domanmarkeringarna star kvar i huvudbetydelsen eftersom ordet annars ser ut att kunna "
 "anvandas om vad som helst. Tillagget 'outtalat missnoje' ar poangen med personbetydelsen: "
 "vresighet ar irritation som inte sags rakt ut.")

K["adressat"] = (
 "Den som en försändelse är riktad till; även den som ett budskap vänder sig till",
 "formell",
 [],
 None,
 "Brevet kom i retur eftersom " + H % "adressaten" + " hade flyttat.",
 "till adressera, av franskans adresser 'rikta'",
 "SO: 'person som en forsandelse ar riktad till', med underbetydelsen 'person som nagon "
 "eller nagot vander sig till eller riktar sig mot'. SAOL upprepar huvudbetydelsen "
 "ordagrant. Underbetydelsen ar en utvidgning fran postforsandelser till budskap i "
 "allmanhet och vags in i huvudbetydelsen. Poolen innehaller bara hela definitionsstrangar "
 "('person som...'), sa synonymfaltet lamnas tomt - 'mottagare' vore rimligt men star inte "
 "i nagon ordbokstext.")

K["definitiv"] = (
 "Slutgiltig och inte längre möjlig att ändra ; som verkligen är fallet",
 "neutral; betydelse 2 vardaglig",
 ["slutgiltig", "bestämd", "absolut"],
 [["slutgiltig", "bestämd"], ["absolut"]],
 "Beslutet är " + H % "definitivt" + " och går inte att överklaga.",
 "latinets definitivus 'avgorande', till definire 'avgransa, bestamma'",
 "SO ger tva huvudbetydelser: 'slutgiltig' och 'som verkligen ar', den senare med "
 "underbetydelsen 'absolut, verkligen' markerad vardagligt. SAOL: 'slutgiltig; bestamd'. "
 "Den vardagliga forstarkande anvandningen ('det ar definitivt sa') ar en egen betydelse i "
 "SO och tas darfor med, med registret utskrivet.")

K["direktiv"] = (
 "Anvisning uppifrån om hur ett bestämt uppdrag ska utföras",
 "formell",
 ["anvisning", "riktlinje", "föreskrift"],
 None,
 "Han fick tydliga " + H % "direktiv" + " om vad rapporten skulle innehålla.",
 "latinets directivus, till dirigere 'rikta, styra'",
 "SO: 'anvisning om sattet att utfora visst uppdrag' med tillagget 'fran overordnad, "
 "myndighet eller dylikt'. Tillagget ar obligatoriskt: ett direktiv kommer UPPIFRAN, och "
 "utan det ledet blir ordet utbytbart mot vilket rad som helst. SAOL: 'riktlinje, "
 "anvisning, foreskrift' - tre likvardiga alternativ atskilda av komma, alla tre tagna "
 "som synonymer.")

K["divergera"] = (
 "Avlägsna sig från varandra ; om åsikter: gå isär ; i matematik: sakna gränsvärde",
 "formell; betydelse 3 fackspråklig",
 ["gå isär", "skilja sig åt", "vara olika"],
 None,
 "Deras uppfattningar om orsaken " + H % "divergerar" + " kraftigt.",
 "latinets divergere 'boja at olika hall', av dis- 'isar' och vergere 'luta'",
 "SO ger tva huvudbetydelser plus en underbetydelse: 'avlagsna sig fran varandra' (ofta "
 "successivt, spec. om stralar), underbetydelsen 'vara olika', och 'sakna gransvarde' om "
 "matematisk serie. Alla tre star pa kortet eftersom de ar praktiskt atskilda: den forsta "
 "ar fysisk, den andra abstrakt om asikter, den tredje en fackterm. Motsatsen konvergera "
 "finns i poolen ('inte konvergera') och bekraftar axeln.")

K["drakonisk"] = (
 "Ytterligt sträng, om straff, lagar eller regler",
 "formell",
 ["sträng"],
 None,
 "Skolan införde " + H % "drakoniska" + " regler om mobiltelefoner.",
 "efter Drakon, athensk lagstiftare pa 600-talet f.Kr., vars lagar var okant harda",
 "SO: 'ytterligt strang'. FORSTARKNINGEN ar hela ordet - drakonisk ar inte samma sak som "
 "strang, det ar strang bortom rimlighet, och etymologin sager varfor. Bara 'strang' "
 "godtas som synonym ur ordbokstexten; forstarkningsledet 'ytterligt' star i "
 "huvudbetydelsen i stallet. Poolens tredje post ('ytterligt 1strang 1') ar ett "
 "formateringsartefakt med kvarlamnade siffror och anvands inte.")

K["durkdriven"] = (
 "Erfaren och förslagen, med kunskap om alla knep inom sitt område",
 "neutral, ofta med en antydan om slughet",
 ["fullfjädrad", "erfaren"],
 None,
 "En " + H % "durkdriven" + " förhandlare hade sett fällan direkt.",
 None,
 "SO: 'erfaren och med kunskap om alla knep inom visst omrade' samt en andra betydelse "
 "'tekniskt skicklig'. KNEP-ledet ar det som skiljer durkdriven fran enbart erfaren och "
 "star darfor i huvudbetydelsen; utan det blir kortet en synonym till 'rutinerad', vilket "
 "det inte ar. Den tekniska betydelsen utelamnas medvetet - se motiveringen.")

K["dynamik"] = (
 "Inneboende kraft och förmåga till förändring i ett skeende ; läran om hur krafter "
 "påverkar rörelse ; skiftningar i tonstyrka som musikaliskt uttrycksmedel",
 "neutral; betydelse 2 och 3 fackspråkliga",
 ["samspel av krafter"],
 None,
 "Gruppens " + H % "dynamik" + " ändrades helt när den nya chefen kom.",
 "grekiskans dynamis 'kraft, formaga'",
 "TRE betydelser, alla SO:s egna huvudbetydelser: 'inneboende formaga till (positiv) "
 "forandring', 'vetenskapen om krafters inverkan pa rorelser' och 'tonstyrkans skiftningar "
 "som musikaliskt uttrycksmedel'. Antalet pa kortet (3) matchar SO:s antal (3), sa "
 "ingen motivering behovs. Endast 'samspel av krafter' finns som kort synonym i "
 "ordbokstexten; ovriga poolposter ar hela definitionsstrangar.")

K["enkelspårig"] = (
 "Som har bara ett spår ; om person: ensidig och oförmögen att se andra möjligheter",
 "neutral; betydelse 2 bildlig",
 ["ensidig", "ytlig"],
 [["ensidig"], ["ensidig", "ytlig"]],
 "Hans " + H % "enkelspåriga" + " sätt att resonera gjorde diskussionen kort.",
 None,
 "SO: 'som har bara ett spar' plus den bildliga 'ensidig'. SAOL markerar den andra "
 "uttryckligen 'bildl. ensidig'. Bada tas med eftersom den bildliga ar den som faktiskt "
 "anvands om personer och ar den ett prov skulle frag om; den konkreta jarnvagsbetydelsen "
 "star forst eftersom den forklarar bilden.")

K["falang"] = (
 "Riktning eller gruppering inom ett parti ; ben i ett finger eller en tå",
 "neutral; betydelse 2 fackspråklig, anatomi",
 ["riktning", "grupp inom parti", "ben i finger eller tå"],
 [["riktning", "grupp inom parti"], ["ben i finger eller tå"]],
 "Partiets konservativa " + H % "falang" + " röstade emot förslaget.",
 "grekiskans phalanx, den tatslutna stridsformationen i antikens Grekland",
 "TVA betydelser, bada egna huvudbetydelser i SO: 'ben i finger el. ta' och 'riktning inom "
 "politiskt parti'. Den politiska star forst pa kortet eftersom den ar den vanliga i "
 "allman text; den anatomiska ar en fackterm. Etymologin binder ihop dem: den grekiska "
 "phalanx var en sluten formation, och bada betydelserna handlar om en avgransad enhet i "
 "en storre helhet.")

K["fashionabel"] = (
 "Förnäm och lyxig, på ett sätt som följer modet i societeten",
 "neutral, något ålderdomlig",
 ["förnäm", "fin", "societetsmässig"],
 None,
 "De åt på en " + H % "fashionabel" + " restaurang där ingen rätt hade pris i menyn.",
 "engelskans fashionable 'modern, pa modet'",
 "SO: 'fornam och lyxig'. SAOL kompletterar med 'fin, hogmodern, societetsmassig'. "
 "SOCIETETS-ledet ar det som skiljer fashionabel fran bara dyr: ordet handlar om vad ett "
 "visst skikt anser vara ratt, inte om pris, och det star darfor i huvudbetydelsen. "
 "'hogmodern' utelamnas som synonym trots att det finns i poolen - det bar en "
 "teknik-association pa nutida svenska som ordet inte har.")

K["fiffa upp"] = (
 "Snygga upp något snabbt och ytligt",
 "vardaglig",
 ["snygga upp", "göra fin"],
 None,
 "Han hann " + H % "fiffa upp" + " lägenheten en halvtimme innan gästerna kom.",
 None,
 "SO: 'gora fin'. SAOL: 'snygga upp'. Bada ar korta och godtas som synonymer. YTLIGHETEN "
 "ligger inte i ordbokstexten men i uttryckets bruk (jfr 'fiffa upp fasaden') och skrivs "
 "ut i huvudbetydelsen som en precisering, inte som en ny betydelse - att fiffa upp ar "
 "inte att renovera.")


TILLAT = {
 "tala med kluven tunga": {
  "betydelse_kan_saknas":
   "SO:s 9 poster kommer fran de FYRA ingaende orden (tala, med, kluven, tunga), inte fran "
   "uttrycket - dar ingar 'typ av plattfisk' och 'skena pa transportmedel'. Flerordsuttryck "
   "far ingen egen artikel och gar genom fritextsokningen. Uttrycket har en betydelse.",
  "frammande_uppslagsord":
   "Samtliga traffar ar de ingaende orden. Inget innehall fran dem har anvants utom SO:s "
   "'kluven' i betydelsen 'vacklande nar det galler att ta stallning', som ar den enda "
   "posten som faktiskt ror uttrycket."},
 "vresig": {"betydelse_kan_saknas":
   "SO:s tredje post ar en underbetydelse utan egen definition (utvidgning) under "
   "personbetydelsen. Kortets tva betydelser motsvarar SO:s tva riktiga def och SAOL:s "
   "tva domanmarkerade huvudbetydelser."},
 "adressat": {"betydelse_kan_saknas":
   "SO:s andra post ar underbetydelsen 'person som nagon eller nagot vander sig till', "
   "dvs. samma begrepp utvidgat fran postforsandelse till budskap. Kortets huvudbetydelse "
   "bar bada leden."},
 "definitiv": {"betydelse_kan_saknas":
   "SO raknar 5, men underbetydelsen 'absolut, verkligen' ar den vardagliga forstarkningen "
   "som redan star som kortets andra betydelse. Ovriga poster saknar egen definition."},
 "divergera": {"betydelse_kan_saknas":
   "SO raknar 5; kortet bar tre praktiskt atskilda betydelser (fysisk, om asikter, "
   "matematisk). De ovriga posterna ar markorer utan egen definition."},
 "drakonisk": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse."},
 "durkdriven": {"betydelse_kan_saknas":
   "SO:s andra betydelse ar 'tekniskt skicklig', som ar en aldre och i nutida svenska "
   "sallsynt anvandning - ordet moter i praktiken bara i knep-betydelsen. Utelamnas "
   "medvetet: kortet ska lara ut den anvandning Adam faktiskt trafar pa."},
 "enkelspårig": {"betydelse_kan_saknas":
   "SO:s tredje post ar en underbetydelse utan egen definition. Kortets tva betydelser "
   "motsvarar SO:s konkreta och bildliga huvudbetydelse."},
 "fashionabel": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse."},
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
print("batch B: %d kort, %d med motivering" % (n, t))
saknas = [o for o in K if not any(e["ord"] == o for e in poster)]
print("ord i K som inte fanns i filen:", saknas or "inga")
