# -*- coding: utf-8 -*-
"""Spar A batch 2026-09-04, del 3 (ord 25-36). Sokkoll via slaupp.py."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-04_v3-batch.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"inpiskad": dict(
  hb="Så rutinerad i något dåligt att inget längre biter på honom",
  reg="neutral, negativ",
  grp=[["utstuderad", "fullfjädrad"]],
  ex="Han var en %s bedragare som lurat folk i trettio år." % B("inpiskad"),
  sl="SO: 'utstuderad och förhärdad'. SAOL: 'fullfjädrad, utstuderad' — komma, alltså EN "
     "betydelse, och båda orden inleder egna led (belagda). Legacy påstod 'perfekt inlärd "
     "och automatiserad genom upprepad övning' — det är fel ord; inpiskad är förhärdad, "
     "inte inövad."),

"jävig": dict(
  hb="Har egna intressen i saken och får därför inte vara med och avgöra den",
  reg="neutral, neutral, juridik",
  grp=[["obehörig"]],
  ex="Domaren anmälde sig som %s eftersom den åtalade var hans granne." % B("jävig"),
  sl="SO: 'olämplig att delta i juridisk process eller dylikt på grund av (risk för) "
     "partiskhet'. SAOL: 'obehörig på grund av jäv' — obehörig inleder ledet, alltså belagd. "
     "En betydelse; legacys andra definition var en omskrivning av den första."),

"kaplan": dict(
  hb="Präst som är anställd av ett företag, en förening eller en familj ; (förr) präst som hjälpte kyrkoherden",
  reg="neutral, neutral, religion ; arkaisk, neutral, religion",
  grp=[["≈≈ präst"], ["hjälppräst"]],
  ex="Regementets %s höll en kort andakt före utryckningen." % B("kaplan"),
  sl="SO: 'präst som är anställd av institution, organisation eller privatperson' plus "
     "underbetydelsen 'förr äv. hjälppräst', som har EGEN definition och därför är en riktig "
     "andra betydelse. SAOL: 'präst anställd av en institution; hjälppräst i äldre tid' — "
     "hjälppräst inleder andra ledet, alltså belagd."),

"kvistig": dict(
  hb="Full av grenstumpar och därför ojämn ; (vardagligt) svår och krånglig",
  reg="neutral, neutral ; vardaglig, neutral",
  grp=[["≈≈ ojämn"], ["svår", "brydsam"]],
  ex="Plankorna var %s och gick inte att hyvla jämna." % B("kvistiga"),
  sl="SO ger TVÅ: 'full av kvistar' och 'svår att förstå och göra något åt' [vardagligt]. "
     "SAOL har två lemman: 'full av kvistar' och 'svår, brydsam' — svår och brydsam inleder "
     "egna led och är belagda för betydelse två."),

"kynne": dict(
  hb="Den läggning och de drag som är typiska för någon",
  reg="neutral, neutral",
  grp=[["läggning", "sinnelag"]],
  ex="Det svenska %s märks när ingen vill skryta om sig själv." % B("kynnet"),
  sl="SO: 'uppsättning karaktärsdrag hos person el. grupp av personer'; underbetydelsen "
     "('äv. hos djur(art)') saknar egen definition och är en utvidgning. SAOL: 'läggning, "
     "sinnelag; prägel' — läggning och sinnelag inleder egna led, alltså belagda.",
  till={"betydelse_kan_saknas": "SO har EN huvudbetydelse; underbetydelsen 'äv. hos "
        "djur(art)' saknar egen definition och är enligt SO:s råstruktur en utvidgning, "
        "inte en betydelse."}),

"mättad": dict(
  hb="Har tagit upp allt av ett ämne som får plats ; om marknad: redan full av varan ; om färg: djup och kraftig ; full av något bra",
  reg="fackspråklig, neutral, kemi ; neutral, neutral, ekonomi ; neutral, neutral ; neutral, positiv",
  grp=[["fylld"], ["≈≈ full"], ["≈≈ kraftig"], ["≈≈ rik"]],
  ex="Han rörde tills lösningen var %s och saltet la sig på botten." % B("mättad"),
  sl="SO ger FYRA: huvudbetydelsen 'som tillförts största möjliga mängd av något' [fysik, "
     "kemi, meteorologi] plus tre underbetydelser med EGEN definition — 'som har största "
     "möjliga utbud av viss vara' (mättad marknad), 'intensiv och fyllig' om färgton, och "
     "'mycket väl försedd' om abstrakta företeelser. Kortet hade bara den första, skriven "
     "två gånger. SAOL: 'fylld av ngt' — fylld inleder ledet, alltså belagd."),

"ornament": dict(
  hb="Utsmyckning som följer och lyfter fram formen på ett föremål ; liten utsmyckning i en melodi",
  reg="neutral, neutral, konst ; neutral, neutral, musik",
  grp=[["utsirning"], ["≈≈ utsmyckning"]],
  ex="Runstenens %s slingrade sig hela vägen runt kanten." % B("ornament"),
  sl="SO: 'stiliserat prydnadsmönster som utnyttjar och understryker föremåls grundform' "
     "plus underbetydelsen 'äv. bildligt: musikalisk utsmyckning', som har EGEN definition "
     "och alltså är en riktig andra betydelse — den saknades helt på kortet. SAOL: "
     "'utsirning, utsmyckning' — utsirning inleder ledet, alltså belagd."),

"papill": dict(
  hb="Liten vårtlik utväxt på ett organ, till exempel på tungan",
  reg="fackspråklig, neutral, medicin",
  grp=[["≈≈ utväxt"]],
  ex="Tungans %s gör att ytan känns sträv." % B("papiller"),
  sl="SO: 'vårtliknande del av (eller utväxt från) ett organ'. SAOL: 'vårtlik upphöjning el. "
     "utbuktning'. En betydelse. Inget enskilt ord i källorna inleder ett led som är utbytbart "
     "mot papill, så synonymen sätts som kategori ur kortets egen definition."),

"pava": dict(
  hb="Flaska, oftast med sprit i",
  reg="vardaglig, neutral",
  grp=[["flaska"]],
  ex="Han hade en %s i innerfickan hela kvällen." % B("pava"),
  sl="SO: 'flaska, särsk. för sprit' [vardagligt]. SAOL: 'flaska sprit' [vard.] — flaska "
     "inleder ledet, alltså belagd. En betydelse. Legacy hade tappat både spritnyansen och "
     "det vardagliga registret och skrev om ordet som en neutral behållare."),

"rättrådig": dict(
  hb="Gör det som är rätt även när ingen ser på",
  reg="neutral, positiv",
  grp=[["redlig", "rättvis"]],
  ex="En %s domare låter sig aldrig köpas." % B("rättrådig"),
  sl="SO: 'som handlar på ett moraliskt riktigt sätt enligt någon (samhällelig) norm'; "
     "underbetydelsen ('äv. om handling') saknar egen definition. SAOL: 'redlig, rättvis' — "
     "båda inleder egna led. Legacys 'hederlig' och 'redbar' är SO:s JFR:cohyponym, alltså "
     "inte belagda som synonymer.",
  till={"betydelse_kan_saknas": "SO:s enda underbetydelse ('äv. om handling eller dylikt') "
        "saknar egen definition och är en utvidgning av huvudbetydelsen, inte en betydelse."}),

"skral": dict(
  hb="Ganska dålig och klen",
  reg="neutral, lätt negativ",
  grp=[["dålig"]],
  ex="Skörden blev %s efter den torra sommaren." % B("skral"),
  sl="SO: 'ganska dålig'; underbetydelsen 'äv. med tanke på dålig hälsa' saknar egen "
     "definition och är en utvidgning, som täcks av 'klen'. SAOL: 'dålig' — belagd. "
     "'undermålig' i legacy är SO:s JFR:cohyponym, inte en belagd synonym.",
  till={"betydelse_kan_saknas": "SO:s underbetydelse 'äv. med tanke på dålig hälsa' saknar "
        "egen definition; enligt SO:s råstruktur är den en utvidgning av 'ganska dålig' och "
        "täcks av kortets 'klen'."}),

"skröna": dict(
  hb="Uppdiktad historia som berättas för att roa",
  reg="neutral, neutral",
  grp=[["≈≈ historia"]],
  ex="Farfar drog samma %s om jättegäddan varje jul." % B("skröna"),
  sl="SO: 'fantasifull och roande historia'. SAOL: 'fantasifull historia'. En betydelse. "
     "Inget enskilt ord inleder ett led som är utbytbart, så kategorin sätts ur kortets egen "
     "definition. OLD-facits 'lögnaktig historia' är en valörförskjutning — SO betonar det "
     "roande, inte lögnen."),
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
        e["forgranska_tillat"] = f["till"]
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("godkande %d kort" % n)
