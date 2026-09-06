# -*- coding: utf-8 -*-
"""Spar A batch 2026-09-05, del 1 (ord 0-7). Sokkoll via slaupp.py."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-05_v3-batch4.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"catering": dict(
  hb="Leverans av färdiglagad mat, till exempel till fester eller flygresor",
  reg="neutral, neutral",
  grp=[["≈≈ matleverans"]],
  ex="Företaget ordnade %s till bröllopet." % B("catering"),
  sl="SO: 'leverans av färdiglagad mat' <<till passagerarflygplan, privata fester m.m.>> "
     "(definitionstillägg medtaget). SAOL: 'leverans av färdig mat till beställarens egna "
     "lokaler' -- ingen enskild synonymglosa inleder ledet, så kategori sätts ur kortets "
     "egen definition. En betydelse."),

"förrättning": dict(
  hb="Arbetsuppgift som hör till en tjänst, särskilt inom det offentliga ; (om kroppen) naturlig funktion",
  reg="formell, neutral, juridik ; neutral, eufemistisk",
  grp=[["tjänsteärende", "tjänstegöromål"], ["funktion"]],
  ex="Lantmätaren var ute på %s hela dagen för att mäta upp den nya tomtgränsen." % B("förrättning"),
  sl="SO: 'göromål som enligt bestämmelserna ingår i arbetsuppgifterna för viss tjänst' "
     "<<särsk. om uppgift inom ramen för offentlig tjänst>> (definitionstillägg medtaget), "
     "plus underbetydelsen 'äv. funktion' (syntex 'kroppens förrättningar') som HAR egen "
     "definition (länkordet 'funktion' utgör hela ledet) och alltså är en riktig andra "
     "betydelse -- den saknades helt i legacy. SAOL: 'tjänstegörmål, tjänsteärende' -- båda "
     "inleder ledet, belagda."),

"heresi": dict(
  hb="Uppfattning eller lära som avviker från den som anses rätt, till exempel inom vetenskapen",
  reg="neutral, negativ",
  grp=[["kätteri", "irrlära"]],
  ex="Att ifrågasätta den rådande teorin sågs av kollegorna som ren %s." % B("heresi"),
  sl="SO: 'lära som avviker från den påbjudna' [brukl: i vetenskapliga sammanhang] -- "
     "bruklighetsmarkeringen visar att ordet i praktiken används brett, inte bara "
     "kyrkligt/religiöst, så domän sätts inte. SAOL: 'kätteri, irrlära' -- båda inleder "
     "ledet, belagda. En betydelse."),

"huckle": dict(
  hb="Enkel sjal som knyts runt huvudet",
  reg="ngt ålderdomlig, neutral",
  grp=[["huvudduk", "huvudkläde"]],
  ex="Gummorna hade %s på huvudet på väg till kyrkan." % B("huckle"),
  etym="Sammandragning av ordet 'huvudkläde', belagt sedan 1655.",
  sl="SO: '(enklare) sjal som knyts runt huvudet', syntex 'gummor i hucklen på väg till "
     "kyrkan' -- daterat/traditionellt bruk, registret satt ngt ålderdomlig. SAOL: "
     "'huvudduk, huvudkläde' -- båda inleder ledet, belagda. Etymologi (SO): sammandragning "
     "av 'huvudkläde', belagt sedan 1655 -- bär betydelsen direkt. En betydelse."),

"inkubationstid": dict(
  hb="Tiden mellan att man smittas av något och att sjukdomen bryter ut",
  reg="fackspråklig, neutral, medicin",
  grp=[["≈≈ tidsperiod"]],
  ex="Giftet sprider sig under en %s på ungefär tolv dagar." % B("inkubationstid"),
  sl="SO: 'tiden mellan inträngandet av smittämne i organismen och de första "
     "sjukdomsyttringarna', syntex 'giftet sprider sig under en inkubationstid av ca 12 "
     "dagar' (anpassad till exempelmening). SAOL: 'tiden mellan nedsmittning och sjukdomens "
     "utbrott'. Ingen enskild synonymglosa inleder ledet i någon källa, så kategori sätts ur "
     "kortets egen definition. En betydelse."),

"trall": dict(
  hb="Enkel, glad melodi ; invand vana som lätt blir slentrian ; spjälgolv som lyfter fötterna ovanför ett vått golv",
  reg="neutral, neutral ; neutral, lätt negativ ; neutral, neutral",
  grp=[["låt", "visa"], ["≈≈ vana"], ["spjälgaller", "spjälgolv"]],
  ex="Han gnolade en enkel %s medan han diskade." % B("trall"),
  sl="SO ger homograf 1 med TVÅ huvudbetydelser: 'enkel, glad melodi' och 'invant sätt att gå "
     "tillväga eller bete sig' <<ofta med bibetydelse av slentrian>> (definitionstillägg "
     "medtaget som negativ valör). Homograf 2: 'lös spjälbotten på golv som skyddar mot "
     "direkt kontakt med vatten' <<anv. på fartyg, i tvättrum och i andra våta utrymmen>> "
     "(kontext medtagen), med en underbetydelse UTAN egen definition (utvidgning till "
     "trädgårdsdäck, räknas inte som egen betydelse). SAOL bekräftar med EN post, två "
     "huvudbetydelser: 'melodi, låt, visa' (exempel 'enligt den vanliga trallen' = 'på det "
     "vanliga sättet', vilket bekräftar habit-betydelsen som en utvidgning av samma ord) och "
     "'spjälgaller; spjälgolv' -- alla inleder egna led, belagda. Legacys 'låt; gammal vana' "
     "saknade helt spjälgolv-betydelsen, tillagd. 'vana' i mellersta betydelsen är en "
     "kategori ur kortets egen definition, ingen ordbokskälla ger ett fristående synonymord "
     "för just den nyansen."),

"ökänd": dict(
  hb="Känd av alla för att vara dålig, i moraliskt avseende",
  reg="neutral, negativ",
  grp=[["beryktad", "illa känd"]],
  ex="Han var en %s bedragare som lurat hundratals människor." % B("ökänd"),
  sl="SO: 'allmänt känd för sina dåliga egenskaper' <<i moraliskt el. liknande avseende>> "
     "(definitionstillägg medtaget). SAOL: 'beryktad, illa känd' -- båda inleder ledet, "
     "belagda. En betydelse."),
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
