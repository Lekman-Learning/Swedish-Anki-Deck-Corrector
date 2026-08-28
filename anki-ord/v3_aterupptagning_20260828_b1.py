# -*- coding: utf-8 -*-
"""11 kortfixar 2026-08-28 (kördes som 'spår C', som visade sig
vara dubbelarbete -- spår B täckte redan poolen efter fixen 2026-08-11). Sökkoll gjord via slaupp.py 2026-08-28 —
bevisraderna SVENSKA_SE_HAMTAD ligger i transkriptet."""
import io, json

FIL = "sessions/session_2026-08-28_v3-aterupptagning.json"
BLA = '<font color="#3498db">%s</font>'
U = lambda o: f"https://svenska.se/api/msearch?ord={o}"

FIX = {
"adekvat": dict(
  hb="Passar precis för det som krävs",
  reg="formell, neutral",
  syn=["passande","lämplig","träffande"],
  ex="Hon fick %s vård direkt när hon kom in." % (BLA % "adekvat"),
  etym="av latin adaequare 'göra lika med' — det ska matcha kravet, inte bara räcka till",
  slutsats="SO: 'som motsvarar givna krav'. SAOL: 'fullt motsvarig, träffande, riktig'. "
           "Kortets synonym 'tillräcklig' är FEL — adekvat handlar om att passa kravet, "
           "inte om mängd. Struken. En betydelse, riskflaggan var falsklarm."),

"asketisk": dict(
  hb="Avstår helt från njutning och lever strängt ; mycket sparsam och avskalad i stilen",
  reg="neutral",
  grp=[["spartansk","återhållsam","försakande"],["avskalad","sparsmakad","nedtonad"]],
  ex="Han levde %s i ett rum utan möbler." % (BLA % "asketiskt"),
  slutsats="SO ger TVÅ betydelser: 'som helt avstår från njutningar' och 'mycket sparsam' "
           "(om uttrycksmedel — SO-ex: 'den asketiska inredningen'). Kortet hade bara den "
           "första. Riskflaggan dold_betydelse var korrekt."),

"brandtal": dict(
  hb="Eldande tal som ska få en grupp att agera",
  reg="neutral",
  syn=["stridsrop","appell","agitationstal"],
  ex="Ordföranden höll ett %s mot nedskärningarna." % (BLA % "brandtal"),
  slutsats="SO: 'tal som är avsett att egga till handling'. SAOL: 'engagerat, agitatoriskt "
           "tal'. Kortet stämde. En betydelse — riskflaggan var falsklarm. Oförändrat i sak."),

"cynism": dict(
  hb="Misstro mot att människor menar väl ; ett yttrande som visar den misstron",
  reg="neutral",
  grp=[["människoförakt","illusionslöshet"],["elakhet","hån"]],
  ex="Hans %s om vänskap gjorde alla tysta." % (BLA % "cynism"),
  slutsats="SO ger TVÅ: 'cynisk inställning' och 'yttrande som vittnar om cynisk "
           "inställning' (SO-ex: 'hans cynismer om den starkares rätt' — räknebart). "
           "Kortet hade bara hållningen. Riskflaggan korrekt."),

"dubiös": dict(
  hb="Tvivelaktig och går inte riktigt att lita på ; skum och ljusskygg om person eller ställe",
  reg="neutral",
  grp=[["tvivelaktig","osäker"],["skum","suspekt","ljusskygg"]],
  ex="Erbjudandet kändes %s redan från början." % (BLA % "dubiöst"),
  slutsats="SO skiljer på påstående ('vars sanningsvärde kan ifrågasättas') och person/plats "
           "(SO-ex: 'en dubiös figur', 'en något dubiös nattklubb'). Delat i två — HP testar "
           "just den skillnaden."),

"extempore": dict(
  hb="Utan förberedelse, rakt ur stunden",
  reg="formell",
  syn=["oförberett","improviserat"],
  ex="Hon fick tala %s när huvudtalaren uteblev." % (BLA % "extempore"),
  etym="latin ex tempore, 'ur stunden' — du tar det på rak arm",
  slutsats="SO: 'oförberett'. SAOL: 'oförberett, på rak arm'. Kortet stämde; en betydelse, "
           "riskflaggan falsklarm. Etymologin tillagd — den gör ordet självförklarande."),

"förleda": dict(
  hb="Locka någon att göra något dumt ; få någon att tro något felaktigt",
  reg="neutral",
  grp=[["lura","narra","locka"],["vilseleda","missleda"]],
  ex="Reklamen %s honom att köpa hela paketet." % (BLA % "förledde"),
  etym="egentligen 'leda vilse'",
  slutsats="SO ger TVÅ: 'locka till felaktigt beteende' och 'ge felaktig uppfattning' "
           "(SO-ex: 'man ska inte förledas att tro på politiker'). Kortet hade bara "
           "handlingen, inte trons-betydelsen."),

"granntyckt": dict(
  hb="Överdrivet kräsen och petig med hur saker ska vara",
  reg="neutral, lite ålderdomlig",
  syn=["kräsen","nogräknad","petig"],
  ex="Vi kan sova på golvet, jag är inte så %s." % (BLA % "granntyckt"),
  slutsats="SO: 'överdrivet kräsen och noggrann'. Kortets avgränsning 'särskilt med mat' "
           "finns INTE i någon källa — SO:s eget exempel handlar om boende och komfort "
           "('vi kan bo på vandrarhem'). Påhittad begränsning, struken."),

"kongenial": dict(
  hb="Stämmer helt i anda och avsikt med någon eller något annat",
  reg="formell",
  syn=["själsbesläktad","samstämd"],
  ex="Översättningen var %s med originalet." % (BLA % "kongenial"),
  slutsats="SO: 'som överensstämmer med någons eller någots anda och avsikter'. SAOL: "
           "'själsligt befryndad'. Kortets 'med originalet' var för smalt — ordet används "
           "även om personer. Breddat."),

"meddelsam": dict(
  hb="Berättar gärna och öppet om sig själv och vad han vet",
  reg="neutral",
  syn=["öppenhjärtig","pratsam","frispråkig"],
  ex="Efter en kopp kaffe blev han förvånansvärt %s." % (BLA % "meddelsam"),
  slutsats="SO: 'som gärna meddelar sig med andra', JFR öppenhjärtig. Kortets 'pratsam' "
           "missar kärnan: det handlar om att DELA MED SIG, inte om att prata mycket. "
           "Skärpt."),

"mossbelupen": dict(
  hb="Helt övervuxen av mossa ; hopplöst gammalmodig",
  reg="neutral",
  grp=[["mossbevuxen","mosstäckt"],["föråldrad","antikverad","unken"]],
  ex="Han drog samma %s vits varje jul." % (BLA % "mossbelupna"),
  slutsats="SO ger TVÅ: 'helt täckt av mossa' och 'helt föråldrad'. SAOL likaså "
           "('mossbevuxen; bildl. helt föråldrad'). Kortet hade bara den bildliga. "
           "Riskflaggan korrekt."),
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    f = FIX.get(e["ord"])
    if not f:
        continue
    prop = {
        "huvudbetydelse": f["hb"],
        "register": f["reg"],
        "synonymer": f.get("syn") or [s for g in f["grp"] for s in g],
        "synonym_groups": f.get("grp"),
        "exempelmening": f["ex"],
    }
    if f.get("etym"):
        prop["etymologi"] = f["etym"]
    if (e["legacy"] or {}).get("bild_html"):
        prop["bild_html"] = e["legacy"]["bild_html"]   # bevaras oförändrad
    e["proposed"] = prop
    e["sokkoll"] = {"kalla": U(e["ord"]), "slutsats": f["slutsats"]}
    e["approved"] = True
    n += 1

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"markerade {n} kort som godkända i {FIL}")
