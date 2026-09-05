# -*- coding: utf-8 -*-
"""Spar A batch 2026-09-04, del 6 (ord 61-72). Sokkoll via slaupp.py."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-04_v3-batch.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"eremitage": dict(
  hb="Litet lust- eller jaktslott ; avskild plats där man får vara i fred",
  reg="neutral, neutral ; neutral, neutral",
  grp=[["lustslott"], ["≈≈ tillflykt"]],
  ex="Kungen lät bygga ett %s längst bort i slottsparken." % B("eremitage"),
  sl="SO: 'lust- eller jaktslott'. SAOL: 'plats för avskildhet; lustslott' — semikolonet "
     "skiljer två betydelser, och avskildhetsbetydelsen finns bara i SAOL. Lustslott inleder "
     "SAOL:s andra led och är belagd; för avskildhetsbetydelsen finns inget ledinledande "
     "enskilt ord, så kategorin tas ur kortets egen definition."),

"fraktion": dict(
  hb="Utbrytargrupp inom ett parti ; del som skilts ut ur en kemisk blandning",
  reg="neutral, neutral, politik ; fackspråklig, neutral, kemi",
  grp=[["meningsgrupp"], ["delmängd"]],
  ex="En %s av partiet bröt sig ur och bildade ett eget." % B("fraktion"),
  sl="SO ger TVÅ huvudbetydelser: 'mindre, avgränsad grupp (oppositionella) i politiskt parti' "
     "och 'ämnen som separerats ur en (kemisk) blandning'. SAOL har två lemman: 'meningsgrupp "
     "inom parti' och 'delmängd erhållen vid kemisk fraktionering' — meningsgrupp och "
     "delmängd inleder sina led och är belagda."),

"franchising": dict(
  hb="Rätt att sälja någon annans vara under dennes varumärke",
  reg="neutral, neutral, ekonomi",
  grp=[["försäljarrätt"]],
  ex="Hela hamburgerkedjan drivs på %s av lokala ägare." % B("franchising"),
  sl="SO: 'licens att tillverka eller sälja viss vara eller tjänst, varvid utrustning och "
     "dylikt tillhandahålls av licensgivaren'. SAOL: 'avtalsbunden ensamrätt att tillhandahålla "
     "en vara under samarbete med tillverkaren; försäljarrätt' — försäljarrätt inleder andra "
     "ledet och är belagd. En betydelse."),

"frifräsare": dict(
  hb="Radikal person som säger precis vad den tycker",
  reg="vardaglig, neutral",
  grp=[["≈≈ radikal"]],
  ex="Kulturdebatten behöver några %s som vågar säga emot." % B("frifräsare"),
  sl="SO och SAOL säger båda ordagrant 'frispråkigt radikal person' [vardagligt/vard.]. En "
     "betydelse. Ledet inleds av adverbet 'frispråkigt', så inget enskilt ord är belagt som "
     "synonym — kategorin tas ur kortets egen definition."),

"förege": dict(
  hb="Ange något som sitt skäl",
  reg="formell, neutral",
  grp=[["påstå", "ange"]],
  ex="Han %s sjukdom som skäl för att slippa vittna." % B("föreger"),
  sl="SO: 'anföra som (viktig) faktor'; underbetydelsen saknar egen definition och är en "
     "utvidgning. SAOL: 'ange som viktig faktor, påstå' — ange och påstå inleder egna led och "
     "är belagda. Legacys 'föregiva' är ett eget uppslagsord, inte en synonym att lära in.",
  till={"betydelse_kan_saknas": "SO:s enda underbetydelse saknar egen definition och ar "
        "enligt SO:s rastruktur en utvidgning av huvudbetydelsen, inte en betydelse."}),

"gehenna": dict(
  hb="Helvetet, platsen där de fördömda plågas",
  reg="litterär, negativ, bibliskt",
  grp=[["helvete"]],
  ex="På kyrkmålningen plågades syndarna i det brinnande %s." % B("gehenna"),
  sl="SO: 'helvete' [bibliskt]. SAOL: 'helvete' — hela definitionen, alltså belagd. En "
     "betydelse. Legacys 'underjorden' är den grekiska Hades, en annan föreställning."),

"gemak": dict(
  hb="Praktfullt rum i ett slott",
  reg="ngt ålderdomlig, skämtsam",
  grp=[["praktrum"]],
  ex="Guiden visade oss slottets salar och %s." % B("gemak"),
  sl="SO: 'praktfullt rum' [något ålderdomligt el. skämtsamt] — båda markeringarna står i "
     "registret. SAOL: 'praktrum' — hela definitionen, alltså belagd. En betydelse. Legacys "
     "'budoar' är ett damrum, en annan sak."),

"genesis": dict(
  hb="Det att något uppstår och blir till",
  reg="neutral, neutral",
  grp=[["uppkomst", "ursprung"]],
  ex="Boken följer partiets %s från källarmöte till riksdag." % B("genesis"),
  sl="SO: 'det att komma att existera'. SAOL: 'uppkomst, ursprung' — båda inleder egna led och "
     "är belagda. En betydelse."),

"genre": dict(
  hb="Sorts konst eller berättande med sina egna typiska drag",
  reg="neutral, neutral, konst",
  grp=[["konstart", "sort"]],
  ex="Han har bara spelat komedi, medan hon prövat flera andra %s." % B("genrer"),
  sl="SO: 'typ av (konstnärlig) framställning som kännetecknas av viss uppsättning stildrag "
     "eller innehållsliga faktorer'; de två underbetydelserna saknar egen definition och är "
     "utvidgningar. SAOL: 'slag, sort, konstart; genrebild' — sort och konstart inleder egna "
     "led och är belagda.",
  till={"betydelse_kan_saknas": "SO:s bada underbetydelser saknar egen definition och ar "
        "utvidgningar av samma betydelse. SAOL:s sista led 'genrebild' ar en hanvisning till "
        "ett annat uppslagsord (genrebild = genremalning), inte en egen betydelse hos genre."}),

"gnata": dict(
  hb="Tjata och klaga småaktigt om småsaker, om och om igen",
  reg="vardaglig, negativ",
  grp=[["smågräla", "kälta"]],
  ex="%s inte på barnen jämt och ständigt!" % B("Gnata"),
  sl="SO: 'ständigt kritisera på ett småaktigt sätt, ofta om mindre allvarliga saker'. SAOL: "
     "'ständigt smågräla, kälta' [vard.] — smågräla och kälta inleder egna led och är belagda. "
     "En betydelse."),

"gästabud": dict(
  hb="Stor fest med mycket mat och många inbjudna",
  reg="ngt ålderdomlig, neutral",
  grp=[["≈≈ fest"]],
  ex="Birger Magnusson bjöd sina bröder på ett %s som slutade i tragedi." % B("gästabud"),
  sl="SO: 'fest med riklig förtäring och många inbjudna' [något ålderdomligt]. SAOL: 'måltid "
     "med åtskilliga gäster'. En betydelse. Båda definitionerna är fraser utan ett "
     "ledinledande enskilt ord, så kategorin tas ur kortets egen definition — legacys "
     "'bankett' och 'kalas' saknar ordboksbelägg."),

"harka": dict(
  hb="Kratta, både redskapet och att kratta med det",
  reg="dialektal, neutral",
  grp=[["kratta"]],
  ex="Han tog fram %s och drog ihop höstlöven på gräsmattan." % B("harkan"),
  sl="SO saknar uppslagsordet. SAOL har TVÅ homografer, båda märkta [prov.]: substantivet "
     "harka 'kratta' och verbet harka 'kratta' — samma glosa för båda, därför skrivs de som "
     "en betydelse som uttryckligen täcker både redskapet och handlingen. Legacys andra "
     "definition ('ålfiskeredskap med långa, tätt sittande taggar') har inget stöd i SO eller "
     "SAOL och är struken. Legacys exempelmening var dessutom grammatiskt fel ('Han användes "
     "harken') och saknade highlight."),
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    f = FIX.get(e["ord"])
    if not f:
        continue
    e["proposed"] = {"huvudbetydelse": f["hb"], "register": f["reg"],
                     "synonymer": [s for g in f["grp"] for s in g],
                     "synonym_groups": f["grp"], "exempelmening": f["ex"]}
    if f.get("etym"):
        e["proposed"]["etymologi"] = f["etym"]
    if (e["legacy"] or {}).get("bild_html"):
        e["proposed"]["bild_html"] = e["legacy"]["bild_html"]
    e["sokkoll"] = {"kalla": U(e["ord"]), "slutsats": f["sl"]}
    if f.get("till"):
        e["forgranska_tillat"] = {**(e.get("forgranska_tillat") or {}), **f["till"]}
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("godkande %d kort" % n)
