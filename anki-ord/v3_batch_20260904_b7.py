# -*- coding: utf-8 -*-
"""Spar A batch 2026-09-04, del 7 (ord 73-84). Sokkoll via slaupp.py."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-04_v3-batch.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"hexameter": dict(
  hb="Versmått med sex takter på varje rad, känt från de grekiska hjältedikterna",
  reg="fackspråklig, neutral, litteraturvetenskap",
  grp=[["≈≈ versmått"]],
  ex="Iliaden och Odysséen är skrivna på %s." % B("hexameter"),
  sl="SO: 'ett orimmat versmått med sexfotade versrader med omväxlande två- och trestaviga "
     "fallande takter, ursprungligen grekiskt'; underbetydelsen saknar egen definition. SAOL: "
     "'en verstyp med sex trokéer el. daktyler på varje rad'. En betydelse. Inget ledinledande "
     "enskilt ord är utbytbart, så kategorin tas ur kortets egen definition.",
  till={"betydelse_kan_saknas": "SO:s enda underbetydelse saknar egen definition och ar en "
        "utvidgning av huvudbetydelsen, inte en betydelse."}),

"hird": dict(
  hb="Kungens egen skara av livvakter i fornnordisk tid",
  reg="neutral, neutral, historia",
  grp=[["livvakt"]],
  ex="Kungens %s slöt sig tätt kring honom under slaget." % B("hird"),
  sl="SO: 'personlig livvakt för (fornnordisk) kung eller storman'. SAOL: 'i äldre tid i "
     "Norden: livvakt för hövding e.d.' — livvakt inleder ledet efter restriktionen och är "
     "belagd. En betydelse."),

"hytta": dict(
  hb="Byggnad med smältugn för metall eller glas ; översta akterdäcket på ett gammalt segelfartyg ; liten enkel övernattningsstuga i fjällen ; hötta, hota med knuten näve",
  reg="neutral, neutral, teknik ; fackspråklig, neutral, sjöfart ; neutral, neutral ; neutral, negativ",
  grp=[["smältugn"], ["≈≈ akterdäck"], ["≈≈ stuga"], ["hötta"]],
  ex="Järnet smältes fram i %s nere vid forsen." % B("hyttan"),
  sl="SO:s substantivlemma ger TRE huvudbetydelser: 'smältugn för framställning av metall "
     "eller glas', 'högsta akterdäck på äldre segelfartyg' och 'liten, enkel stuga för "
     "övernattning, särsk. om sådan stuga i Norge'. Dessutom finns ett eget VERBLEMMA hytta, "
     "som SO anger som variant av hötta — SAOL har det som homograf 2 med definitionen "
     "'hötta'. Kortet hade bara smältugnen och stugan; akterdäcket och hela verbet saknades. "
     "SAOL: 'byggnad med smältugn' (smältugn inleder ledet, belagd) och 'hötta' (belagd)."),

"istadig": dict(
  hb="Vägrar envist att foga sig ; går inte att få ur fläcken",
  reg="neutral, lätt negativ ; neutral, lätt negativ",
  grp=[["motspänstig", "envis"], ["≈≈ orörlig"]],
  ex="Åsnan blev %s och vägrade ta ett enda steg till." % B("istadig"),
  sl="SO: 'som envist vägrar att foga sig' plus underbetydelsen 'som inte kan förmås att röra "
     "sig ur fläcken el. i önskad riktning', som har EGEN definition och alltså är en riktig "
     "andra betydelse — den saknades på kortet. Den tredje posten saknar definition och är en "
     "utvidgning. SAOL: 'motspänstig, envis' — båda inleder egna led och är belagda."),

"karisma": dict(
  hb="Stark personlig utstrålning som drar till sig andra",
  reg="neutral, positiv",
  grp=[["≈≈ utstrålning"]],
  ex="Talaren hade en %s som fick hela salen att tystna." % B("karisma"),
  sl="SO: 'stark personlig utstrålning som ger förmåga att påverka och fascinera andra "
     "människor'. SAOL: 'personlig utstrålning' — ledet inleds av adjektivet 'personlig', så "
     "inget enskilt ord är belagt; kategorin tas ur kortets egen definition. En betydelse."),

"kujon": dict(
  hb="Feg stackare som aldrig vågar stå upp för något",
  reg="ngt ålderdomlig, nedsättande",
  grp=[["≈≈ fegis"]],
  ex="Han var en %s som lät andra ta smällen." % B("kujon"),
  sl="SO saknar uppslagsordet. SAOL: 'feg person' — ledet inleds av adjektivet 'feg', så inget "
     "enskilt ord är belagt; kategorin komprimeras ur kortets egen definition. En betydelse. "
     "Legacys andra definition ('svag individ som är lätt att manipulera') har inget "
     "ordboksstöd — kujon handlar om feghet, inte om att vara lättpåverkad."),

"käpphäst": dict(
  hb="Barnleksak: en pinne med hästhuvud på ; fråga som någon ständigt återkommer till",
  reg="neutral, neutral ; neutral, lätt negativ",
  grp=[["≈≈ leksak"], ["≈≈ favoritfråga"]],
  ex="Pojken red runt på sin %s i trädgården." % B("käpphäst"),
  sl="SO ger TVÅ huvudbetydelser: 'leksak i form av en käpp med hästhuvud på' och 'fråga som "
     "någon ständigt och gärna återkommer till'. SAOL har två lemman: 'en äldre leksak' och "
     "'ngt man gärna sysslar med och återkommer till'. Leden inleds av artikel respektive "
     "pronomen, så inget enskilt ord är belagt — kategorierna tas ur kortets egna betydelser. "
     "Legacys 'fix idé' är något annat: en tvångstanke, inte ett favoritämne."),

"laborera": dict(
  hb="Utföra försök i ett laboratorium ; pröva sig fram med olika lösningar",
  reg="neutral, neutral ; neutral, neutral",
  grp=[["≈≈ försök"], ["experimentera"]],
  ex="Kemistudenterna %s med syror och baser hela förmiddagen." % B("laborerade"),
  sl="SO: 'utföra laboration' plus underbetydelsen 'göra prov, experimentera', som har EGEN "
     "definition och alltså är en riktig andra betydelse. SAOL: 'utföra naturvetenskapliga "
     "försök i laboratorium; experimentera; arbeta' — experimentera inleder ett eget led och "
     "är belagd för betydelse två."),

"legering": dict(
  hb="Att smälta ihop metaller till ett enda material ; själva materialet som blir resultatet",
  reg="neutral, neutral, teknik ; neutral, neutral, teknik",
  grp=[["≈≈ sammansmältning"], ["metallblandning"]],
  ex="Brons är en %s av koppar och tenn." % B("legering"),
  sl="SO: 'metallblandning som bildar ett enhetligt material' — metallblandning inleder ledet "
     "och är belagd; underbetydelsen saknar egen definition. SAOL: 'det att legera; äv. om "
     "resultatet, t.ex. brons, mässing' — semikolonet skiljer SJÄLVA PROCESSEN från "
     "RESULTATET, alltså två betydelser, och kortet hade bara resultatet. Legacys 'amalgam' är "
     "en särskild kvicksilverlegering, inte en synonym."),

"markis": dict(
  hb="Adelsman i rang mellan hertig och greve ; nedfällbart soltak av tyg över ett fönster",
  reg="neutral, neutral, historia ; neutral, neutral",
  grp=[["≈≈ adelstitel"], ["≈≈ soltak"]],
  ex="%s ärvde godset efter sin far." % B("Markisen"),
  sl="SO ger TVÅ huvudbetydelser: '(titel för) adelsman av hög rang, mellan hertig och greve' "
     "och 'solskydd av tyg som fälls ner framför fönster'. SAOL har två lemman med samma "
     "uppdelning. Leden inleds av '(titel för)' respektive 'nedfällbart', alltså inget belagt "
     "enskilt ord — kategorierna tas ur kortets egna betydelser. Legacys exempelmening hade "
     "fel genus ('sitt markis' — det heter en markis, markisen)."),

"moatjé": dict(
  hb="Den andra i ett par, den man är tillsammans med för kvällen",
  reg="ngt ålderdomlig, neutral",
  grp=[["partner", "motspelare"]],
  ex="Han förde sin %s till bordet." % B("moatjé"),
  sl="SO: 'andra parten i par som tillsammans utför viss aktivitet el. bildar en varaktig "
     "enhet; spec. om (någons) kavaljer respektive dam'. SAOL: 'ngns kavaljer el. dam; "
     "partner, motspelare' — partner och motspelare inleder egna led och är belagda. En "
     "betydelse; SAOL:s led är synonymuppräkningar, inte skilda betydelser."),

"odisputabel": dict(
  hb="Så självklart att ingen kan säga emot",
  reg="högtidlig, neutral",
  grp=[["obestridlig", "oomtvistlig"]],
  ex="Hennes insats den kvällen var av %s betydelse för laget." % B("odisputabel"),
  sl="SO: 'som man inte behöver disputera om' [något högtidligt] — markeringen står i "
     "registret. SAOL: 'obestridlig, oomtvistlig' — båda inleder egna led och är belagda. En "
     "betydelse."),
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
