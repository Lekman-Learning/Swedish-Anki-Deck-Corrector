# -*- coding: utf-8 -*-
"""Spar A batch 2026-09-04, del 8 (ord 85-99, utom vederkvickande som pausas)."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-04_v3-batch.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"omlott": dict(
  hb="Så att den ena kanten ligger över den andra",
  reg="neutral, neutral",
  grp=[["≈≈ överlappande"]],
  ex="Hon knäppte kappan %s över bröstet." % B("omlott"),
  sl="SO: 'med en kant något överskjutande en annan' (adverb). SAOL har uppslagsordet men "
     "ingen definitionstext. En betydelse. Inget ledinledande enskilt ord finns, så kategorin "
     "tas ur kortets egen definition. Legacys synonymer ('lott', 'föremål', 'delvis') hörde "
     "inte ihop med ordet alls."),

"otit": dict(
  hb="Inflammation i örat",
  reg="fackspråklig, neutral, medicin",
  grp=[["öroninflammation"]],
  ex="Barnet fick %s och skrek av öronvärk hela natten." % B("otit"),
  sl="SO: 'öroninflammation'. SAOL: 'öroninflammation' — hela definitionen, alltså belagd. En "
     "betydelse. Legacys 'örsprång' och 'öronvärk' är symtom, inte samma sak som "
     "inflammationen."),

"patella": dict(
  hb="Det lilla runda benet framför knäleden",
  reg="fackspråklig, neutral, medicin",
  grp=[["knäskål"]],
  ex="Han spräckte sin %s i fallet nedför trappan." % B("patella"),
  sl="SO: 'knäskål'. SAOL: 'knäskål' — hela definitionen, alltså belagd. En betydelse. Legacys "
     "'knäleden' är leden, inte benet — sakligt fel synonym."),

"påföra": dict(
  hb="Skriva upp en avgift eller en skuld på någon",
  reg="formell, neutral, ekonomi",
  grp=[["föra upp"]],
  ex="Kommunen %s fastigheten nya avgifter." % B("påförde"),
  sl="SO: 'föra upp på skuldräkning för någon el. något'. SAOL: 'föra upp på skuldräkning för "
     "ngn el. ngt' — 'föra upp' inleder ledet i båda källorna och är belagd. En betydelse. "
     "Legacys exempelmening saknade highlight helt."),

"recitera": dict(
  hb="Läsa upp en dikt högt och med känsla",
  reg="neutral, neutral, konst",
  grp=[["deklamera"]],
  ex="Hon brukade %s Fröding för barnbarnen." % B("recitera"),
  sl="SO: 'konstnärligt läsa upp skönlitterär text'. SAOL: 'läsa upp konstnärlig text, "
     "deklamera' — deklamera inleder ett eget led och är belagd. En betydelse."),

"rehabilitera": dict(
  hb="Ge upprättelse åt någon som blivit orättvist utpekad ; träna upp någon till ett normalt liv efter sjukdom eller fängelse ; ta revansch och tvätta bort en dålig insats",
  reg="neutral, positiv ; neutral, neutral, medicin ; neutral, neutral, sport",
  grp=[["återupprätta"], ["återanpassa"], ["revanschera sig"]],
  ex="Många av offren för förtrycket kom senare att %s." % B("rehabiliteras"),
  sl="SO ger TVÅ huvudbetydelser: 'ge upprättelse åt person, åskådning m.m. som varit "
     "undertryckt' och 'återanpassa (sjuk, funktionshindrad eller kriminellt belastad person) "
     "till ett normalt liv'. SAOL har TRE lemman och lägger till en tredje: 'ta revansch, "
     "revanschera sig'. Kortet hade två, hopslagna. Återupprätta, återanpassa och revanschera "
     "sig inleder alla egna led och är belagda."),

"rådbråka": dict(
  hb="Tala eller skriva ett språk så illa att det knappt går att förstå ; anstränga hjärnan hårt ; misshandla och tilltyga svårt ; (historiskt) avrätta genom att krossa den dömde på ett hjul",
  reg="neutral, lätt negativ ; neutral, neutral ; neutral, negativ ; arkaisk, negativ, historia",
  grp=[["förvränga"], ["anstränga"], ["mörbulta"], ["≈≈ avrätta"]],
  ex="Turisten %s svenskan så att ingen förstod vad han ville ha." % B("rådbråkade"),
  sl="SO ger TVÅ huvudbetydelser — 'avrätta (dödsdömd person) genom att låta vederbörande "
     "krossas av ett tungt hjul' [historiskt] och 'utsätta (någons kropp) för svåra "
     "påfrestningar' — plus underbetydelsen 'anstränga något, särsk. hjärnan', som har EGEN "
     "definition. SAOL lägger dessutom till språkbetydelsen: 'mörbulta; misshandla; hårt "
     "anstränga sin hjärna; förvränga ord; tala el. skriva ett språk knaggligt'. Kortet hade "
     "bara avrättningen och misshandeln — den i dag klart vanligaste betydelsen (rådbråka "
     "svenskan) saknades helt. Ordningen följer faktisk användning, inte SO:s "
     "artikelordning. Förvränga, anstränga och mörbulta inleder egna led och är belagda."),

"sarkofag": dict(
  hb="Praktfull stenkista att lägga en död i",
  reg="neutral, neutral, historia",
  grp=[["≈≈ stenkista"]],
  ex="En grekisk inskription prydde sidan av %s." % B("sarkofagen"),
  sl="SO: 'fristående, rikt utsmyckad gravkista, ofta i sten och med skulpturer'. SAOL: "
     "'praktfull likkista av sten'. En betydelse. Båda leden inleds av adjektiv, så inget "
     "enskilt ord är belagt — kategorin tas ur kortets egen definition."),

"sefyr": dict(
  hb="Mild vind från väster",
  reg="högtidlig, positiv",
  grp=[["västanvind"]],
  ex="En mild %s drog in över trädgården vid solnedgången." % B("sefyr"),
  sl="SO: 'vind från väster' [något högtidligt]. SAOL: 'västanvind' [högt.] — hela "
     "definitionen, alltså belagd. En betydelse, och markeringen står i registret."),

"siren": dict(
  hb="Apparat som tjuter högt för att varna ; sagoväsen med kvinnohuvud och fågelkropp som lockade sjöfarare i döden",
  reg="neutral, neutral, teknik ; neutral, neutral, historia",
  grp=[["≈≈ larmapparat"], ["≈≈ sagoväsen"]],
  ex="%s tjöt över hela staden när larmet gick." % B("Sirenerna"),
  sl="SO ger TVÅ huvudbetydelser: 'apparat som kan avge starka, utdragna eller upprepade "
     "ljudsignaler' och 'ett antikt sagoväsen med en kvinnas huvud och i övrigt en FÅGELS "
     "kropp, som med sin sång troddes locka sjöfarare i fördärvet'. SAOL har samma två. "
     "Legacys synonymer ('sjöjungfru', 'havsgudinna') är sakligt fel — sirenen har fågelkropp, "
     "inte fiskstjärt — och hörde dessutom bara till den andra betydelsen medan "
     "huvudbetydelsen var apparaten. Legacys exempelmening var avhuggen mitt i ('Tjutet från "
     "sirenerna på ta.'). Leden inleds av 'apparat som' respektive 'ett antikt', så "
     "kategorierna tas ur kortets egna betydelser."),

"sistliden": dict(
  hb="Som var senast, den nyss gångna",
  reg="högtidlig, neutral",
  grp=[["≈≈ senaste"]],
  ex="Beslutet fattades den sjätte %s februari." % B("sistlidne"),
  sl="SO: 'närmast föregående (i tiden)' [något högtidligt]. SAOL har uppslagsordet men ingen "
     "definitionstext. En betydelse, markeringen står i registret. SO:s led inleds av "
     "'närmast', så inget enskilt ord är belagt — kategorin tas ur kortets egen definition."),

"strass": dict(
  hb="Glittrande glas som får se ut som ädelstenar i smycken",
  reg="neutral, neutral",
  grp=[["≈≈ glitterglas"]],
  ex="Klänningen var besatt med %s och paljetter." % B("strass"),
  sl="SO: 'ett starkt brytande, blyhaltigt glas som används till smycken el. som dekoration på "
     "kläder'. SAOL: 'ljusbrytande blyglas till smycken'. En betydelse. Båda leden inleds av "
     "adjektiv, så kategorin komprimeras ur kortets egen definition. Legacys 'glas' och "
     "'smycken' är för vida respektive fel sak."),

"vittja": dict(
  hb="Tömma en fälla eller ett nät på fångst ; stjäla ur någons fickor",
  reg="neutral, neutral, jakt ; neutral, negativ",
  grp=[["tömma"], ["stjäla"]],
  ex="Fiskarna hade %s sina ryssjor redan tidigt på morgonen." % B("vittjat"),
  sl="SO: 'tömma (fångstredskap) på innehåll' plus underbetydelsen 'stjäla', som har EGEN "
     "definition och alltså är en riktig andra betydelse — den saknades på kortet. SAOL: 'ta "
     "hand om fångsten i nät el. snara; stjäla ur fickor e.d.' — samma två. Tömma inleder "
     "SO:s led och stjäla är hela underbetydelsens definition, båda belagda."),

"ömsevis": dict(
  hb="Om vartannat, först det ena och sedan det andra",
  reg="neutral, neutral",
  grp=[["växelvis"]],
  ex="Hon var %s glad och sorgsen hela kvällen." % B("ömsevis"),
  sl="SO: 'växelvis'. SAOL: 'växelvis' — hela definitionen, alltså belagd. En betydelse. "
     "Legacys 'alternerande' saknar ordboksbelägg."),
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
