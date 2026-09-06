# -*- coding: utf-8 -*-
"""Spar A batch 2026-09-04, del 5 (ord 49-60). Sokkoll via slaupp.py."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-04_v3-batch.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"befogenhet": dict(
  hb="Rätt att fatta vissa beslut eller göra vissa saker",
  reg="neutral, neutral, juridik",
  grp=[["rättighet", "behörighet"]],
  ex="Rektorn hade inte %s att stänga av eleven på egen hand." % B("befogenhet"),
  sl="SO: 'laglig rätt att vidta viss typ av åtgärder inom visst område' [särsk. juridik]. "
     "SAOL: 'rättighet; behörighet; rättmätighet' — rättighet och behörighet inleder egna led "
     "och är belagda. Legacys 'kompetens' och 'mandat' saknar ordboksbelägg."),

"besvärjelse": dict(
  hb="Ordramsa som ska ha övernaturlig kraft ; själva ritualen där man manar fram eller driver bort andar",
  reg="neutral, neutral, religion ; neutral, neutral, religion",
  grp=[["≈≈ ordramsa"], ["≈≈ ritual"]],
  ex="Medicinmannen mumlade sina %s över elden." % B("besvärjelser"),
  sl="SO: '(formelartad) ordramsa som avses ha övernaturlig verkan' plus underbetydelsen "
     "'det att besvärja', som har EGEN definition och alltså är en riktig andra betydelse "
     "(själva handlingen, inte formeln) — den saknades på kortet. Den tredje underbetydelsen "
     "saknar egen definition och är en utvidgning. SAOL: 'formelartad ordramsa som tros ha "
     "övernaturlig verkan' — inget enskilt ord inleder ett utbytbart led, så kategorierna tas "
     "ur kortets egen definition."),

"bienn": dict(
  hb="Om en växt: lever i två år",
  reg="fackspråklig, neutral, biologi",
  grp=[["tvåårig"]],
  ex="Trädgårdsmästaren sådde både ettåriga och %s växter." % B("bienna"),
  sl="SO: 'som lever i två år, om växt'. SAOL: 'tvåårig' — inleder ledet, alltså belagd. En "
     "betydelse. Legacys 'tvåår' och 'tvåårsk' är inga svenska ord."),

"blarr": dict(
  hb="Prat om ingenting",
  reg="vardaglig, lätt negativ",
  grp=[["struntprat"]],
  ex="Mötet blev en timme av rent %s utan ett enda beslut." % B("blarr"),
  sl="SO: 'struntprat' [vardagligt] — struntprat är hela definitionen och därmed belagd. SAOL "
     "saknar uppslagsordet; SO räcker enligt källhierarkin. En betydelse. Legacys 'bladder' "
     "saknar belägg."),

"botanik": dict(
  hb="Läran om växterna",
  reg="neutral, neutral, biologi",
  grp=[["≈≈ växtlära"]],
  ex="Hon läste %s och kunde namnge varje ogräs i rabatten." % B("botanik"),
  sl="SO: 'vetenskapen om växterna'. SAOL: 'vetenskapen om växter'. En betydelse. Inget "
     "enskilt ord i källorna inleder ett utbytbart led (definitionerna är fraser), så "
     "kategorin sätts som en komprimering av kortets egen definition."),

"cellofan": dict(
  hb="Tunn genomskinlig film som man slår in saker i",
  reg="neutral, neutral",
  grp=[["≈≈ omslagsmaterial"]],
  ex="Blombuketten var inslagen i knastrande %s." % B("cellofan"),
  sl="SO: 'en genomskinlig cellulosaplast som används som omslagsmaterial m.m.'. SAOL: 'ett "
     "genomskinligt omslagsmaterial'. En betydelse. Definitionerna är fraser utan ett "
     "utbytbart ledinledande ord, så kategorin tas ur kortets egen definition."),

"delinkvent": dict(
  hb="Person som ska ta sitt straff",
  reg="formell, neutral, juridik",
  grp=[["brottsling"]],
  ex="%s fördes in i rättssalen för att höra domen." % B("Delinkventen"),
  sl="SO: 'person som har att undergå straff'. SAOL: 'brottsling som ska straffas' — "
     "brottsling inleder ledet, alltså belagd. En betydelse."),

"dermatologi": dict(
  hb="Läran om huden och dess sjukdomar",
  reg="fackspråklig, neutral, medicin",
  grp=[["≈≈ hudlära"]],
  ex="Hon specialiserade sig på %s och tog emot patienter med svåra eksem." % B("dermatologi"),
  sl="SO: 'läran om hudsjukdomar'. SAOL: 'vetenskapen om huden och dess sjukdomar'. En "
     "betydelse. Inget enskilt ord inleder ett utbytbart led, så kategorin komprimeras ur "
     "kortets egen definition. Legacys 'dermatoskopi' är en undersökningsmetod, inte ett "
     "kunskapsfält — sakligt fel synonym."),

"distribution": dict(
  hb="Utdelning och utskickning av varor till många mottagare ; hela kedjan som får varan fram till kunden ; hur något är spritt över ett område ; hur ett språkljud eller ord får förekomma i språket",
  reg="neutral, neutral ; neutral, neutral, ekonomi ; neutral, neutral ; fackspråklig, neutral, lingvistik",
  grp=[["≈≈ utdelning"], ["≈≈ varukedja"], ["≈≈ spridning"], ["≈≈ förekomst"]],
  ex="Förlaget sköter %s av boken till alla bokhandlar." % B("distributionen"),
  sl="SO ger FYRA: huvudbetydelsen 'överenskommen eller regelmässig fördelning och "
     "utskickning, särsk. av varor bland många mottagare' plus TRE underbetydelser med EGEN "
     "definition — 'sammanfattningen av alla operationer som syftar till att ställa varor "
     "eller tjänster till konsumenternas förfogande', 'grad av spridning över visst område' "
     "och 'ett eller flera språkelements förekomst och kombinationsmöjligheter inom ett "
     "språksystem'. Kortet hade bara den första. SAOL:s post saknar definitionstext, så "
     "synonymerna sätts som kategorier ur kortets egna betydelser."),

"drasut": dict(
  hb="Lång ung karl",
  reg="vardaglig, nedsättande",
  grp=[["≈≈ karl"]],
  ex="In i köket klev en %s som knappt fick plats under lampan." % B("drasut"),
  sl="SO: '(lång, yngre) mansperson' [nedsättande]. SAOL: 'lång pojke el. man' [vard.]. En "
     "betydelse, och båda markeringarna står i registret. Legacys 'räkel', 'bängel' och "
     "'fyrtorn' saknar ordboksbelägg, så kategorin tas ur kortets egen definition."),

"ekvilibristik": dict(
  hb="Skicklig balanskonst, ofta bildligt om någon som briljerar med sin teknik",
  reg="neutral, positiv",
  grp=[["≈≈ balanskonst"]],
  ex="Pianisten imponerade med sin %s i sista satsen." % B("ekvilibristik"),
  sl="SO: 'det att vara ekvilibristisk' — en cirkulär definition, med syntex 'pianisten "
     "imponerade med sin ekvilibristik' som visar den bildliga användningen. SAOL har "
     "uppslagsordet men ingen definitionstext. Ingen källa ger ett belagt synonymord, så "
     "kategorin komprimeras ur kortets egen definition."),

"entreprenad": dict(
  hb="Åtagande att utföra ett större arbete åt någon mot betalning",
  reg="neutral, neutral, ekonomi",
  grp=[["≈≈ åtagande"]],
  ex="Kommunen lade ut hela skolbygget på %s." % B("entreprenad"),
  sl="SO: 'åtagande att mot viss ersättning utföra större arbetsuppgift, ofta efter "
     "konkurrens'; de tre underbetydelserna saknar egen definition och är utvidgningar. "
     "SAOL: 'arbets- el. leveransbeting av större omfattning' — ledet inleds av en avkortad "
     "sammansättning, alltså inget brukbart synonymord, så kategorin tas ur kortets egen "
     "definition. Legacys 'ackord' och 'avtal' saknar belägg."),
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
