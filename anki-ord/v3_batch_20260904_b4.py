# -*- coding: utf-8 -*-
"""Spar A batch 2026-09-04, del 4 (ord 37-48, utom apparans som pausas). Sokkoll via slaupp.py."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-04_v3-batch.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"summarisk": dict(
  hb="Tar bara upp huvuddragen ; sker förenklat och snabbt, utan den noggranna prövning som annars krävs",
  reg="neutral, neutral ; neutral, neutral, juridik",
  grp=[["sammandragen", "kortfattad"], ["≈≈ förenklad"]],
  ex="Rapporten gav bara en %s bild av vad som hade hänt." % B("summarisk"),
  sl="SO ger TVÅ: 'som bara tar upp huvuddragen' plus underbetydelsen 'äv. som sker utan "
     "sedvanlig ingående prövning', som har EGEN definition och alltså är en riktig andra "
     "betydelse (summarisk process) — den saknades helt på kortet. SAOL: 'sammandragen; "
     "kortfattad' — båda inleder egna led och är belagda för betydelse ett."),

"tongivande": dict(
  hb="Den som andra rättar sig efter och tar efter",
  reg="neutral, neutral",
  grp=[["ledande"]],
  ex="Hon var %s i debatten och de andra följde snart hennes linje." % B("tongivande"),
  sl="SO: 'som (indirekt) bestämmer inriktningen av åsikter och beteendemönster inom större "
     "grupp, genom att själv utgöra mönster'. SAOL: 'intellektuellt ledande' — ledande inleder "
     "ledet efter restriktionen, alltså belagd. En betydelse."),

"urskulda": dict(
  hb="Försvara någon genom att peka på skäl som gör saken mindre allvarlig",
  reg="neutral, neutral",
  grp=[["rättfärdiga", "ursäkta"]],
  ex="Han försökte %s sin son med att skolan hade svikit honom." % B("urskulda"),
  sl="SO: 'försvara genom att anföra förmildrande omständigheter för viss förseelse eller "
     "dylikt'. Det andra SO-lemmat är den reflexiva formen 'urskulda sig' ('försvara sig …'), "
     "alltså samma betydelse riktad mot en själv, inte en ny betydelse. SAOL: 'försöka "
     "rättfärdiga; ursäkta' — rättfärdiga och ursäkta inleder egna led, alltså belagda."),

"ärbar": dict(
  hb="Som lever efter äldre tiders krav på sexuell moral",
  reg="ngt ålderdomlig, neutral",
  grp=[["dygdig", "sedesam"]],
  ex="På den tiden skulle en %s kvinna aldrig gå ut ensam på kvällen." % B("ärbar"),
  sl="SO: 'som visar god sexualmoral enligt vissa (äldre) föreställningar; mest om kvinna' "
     "[något ålderdomligt]. SAOL: 'sexuellt dygdig, sedesam' — dygdig och sedesam inleder egna "
     "led, alltså belagda. Legacys 'anständig' och 'hederlig' står inte i någon ordbok; "
     "'sedesam' är dessutom SO:s JFR:cohyponym men är belagd via SAOL:s definitionstext."),

"ackuratess": dict(
  hb="Stor noggrannhet, gärna med elegans",
  reg="neutral, positiv",
  grp=[["noggrannhet", "elegans"]],
  ex="Han vek varje skjorta med en %s som gränsade till besatthet." % B("ackuratess"),
  sl="SO: 'stor noggrannhet, vanligen i kombination med viss elegans' — definitionstillägget "
     "gör eleganskomponenten till en del av SAMMA betydelse, inte en andra. SAOL: 'noggrannhet; "
     "elegans' — båda inleder egna led och är belagda."),

"aktris": dict(
  hb="Kvinna som spelar roller på scen eller film",
  reg="neutral, neutral, konst",
  grp=[["skådespelerska"]],
  ex="Den franska %s tackade nej till rollen." % B("aktrisen"),
  sl="SO: 'skådespelerska'. SAOL: 'skådespelerska' — inleder ledet, alltså belagd. En "
     "betydelse. Legacys 'artist' och 'rollinnehavare' saknar ordboksbelägg."),

"alika": dict(
  hb="Den lilla svartgrå kråkfågeln med ljusa ögon",
  reg="dialektal, neutral, biologi",
  grp=[["kaja"]],
  ex="En flock %s lyfte från kyrktornet." % B("alikor"),
  sl="SO: 'kaja' [dialektalt]. SAOL: 'kaja' — inleder ledet, alltså belagd. EN betydelse, och "
     "den är ett SUBSTANTIV för en fågel. Legacy påstod att alika betyder 'berusad' "
     "(synonymer stupfull/full, exempelmening 'Han var alika efter festen') — fel ordklass och "
     "fel betydelse, sannolikt en sammanblandning med uttrycket 'full som en alika'."),

"anbringa": dict(
  hb="Sätta fast något på rätt ställe",
  reg="formell, neutral",
  grp=[["fästa", "placera"]],
  ex="Skylten ska %s väl synligt vid ingången." % B("anbringas"),
  sl="SO: 'placera något där det passar (och kan fästas)'. SAOL: 'fästa, placera' — båda "
     "inleder egna led, alltså belagda. En betydelse. Legacys 'montera' saknar belägg."),

"assonans": dict(
  hb="Ofullständigt rim där bara vokalerna stämmer överens",
  reg="fackspråklig, neutral, litteraturvetenskap",
  grp=[["halvrim"]],
  ex='Orden "orm" och "harm" bildar en %s.' % B("assonans"),
  sl="SO: 'typ av oäkta rim, vanligen med identiska vokaler men bara likartade konsonanter el. "
     "vice versa', med halvrim taggat SYN:synonym — alltså belagd på den starkaste grunden. "
     "SAOL: 'halvrim t.ex. orm: harm'. En betydelse."),

"avhjälpa": dict(
  hb="Få bort eller mildra ett fel eller en brist",
  reg="neutral, neutral",
  grp=[["avlägsna", "lindra"]],
  ex="Felet gick att %s på tio minuter." % B("avhjälpa"),
  sl="SO: 'lindra eller avlägsna fel el. brist' — båda orden inleder egna led. SAOL: "
     "'avlägsna' — belagd. En betydelse. Legacys OLD-facit var en klistrad HTML-blob och "
     "användes inte."),

"avskräde": dict(
  hb="Rester som man vill bli av med",
  reg="neutral, lätt negativ",
  grp=[["avfall"]],
  ex="Hinken med %s stod och stank utanför dörren." % B("avskräde"),
  sl="SO: 'rester eller material som man vill bli av med'. SAOL: 'avfall' — inleder ledet, "
     "alltså belagd. 'skräp' är SO:s JFR:cohyponym och används därför inte. En betydelse."),
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
