# -*- coding: utf-8 -*-
"""Spar A batch 2026-09-05, del 1 (ord 1-8). Sokkoll via slaupp.py."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-05_v3-batch.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"abbedissa": dict(
  hb="Kvinna som är chef för ett nunnekloster",
  reg="neutral, neutral, religion",
  grp=[["föreståndarinna"]],
  ex="%s ledde klostrets systrar i den dagliga bönen." % B("Abbedissan"),
  sl="SO: 'kvinnlig föreståndare för nunnekloster', en betydelse, inget "
     "definitionstillägg. SAOL: 'föreståndarinna för kloster' — föreståndarinna "
     "inleder ledet (enda ordet i det), alltså belagd. Legacys andra definition "
     "var bara en omskrivning av samma betydelse. Etymologin (fornsvenska "
     "abbatissa, av medeltidslatin) säger bara att ordet är gammalt, hjälper "
     "inte betydelsen -- utelämnad."),

"bussarong": dict(
  hb="Ett löst skjortliknande plagg med öppning vid halsen -- ursprungligen "
     "sjömanskläder, i dag ett bredare ord för sådana plagg",
  reg="neutral, neutral",
  grp=[["≈≈ skjorta"]],
  ex="Han bar en blå %s med öppen krage till jobbet." % B("bussarong"),
  sl="SO: 'ett skjortliknande överdragsplagg' med definitionstillägget "
     "'ursprungligen för sjömän; numera ofta allmännare om löst sittande plagg "
     "med sprund i halsen' -- båda delarna i tillägget med i huvudbetydelsen. "
     "SAOL: 'blusliknande överdragsplagg', samma betydelse. Inget enskilt ord "
     "inleder ett led som är utbytbart (adjektiv+substantiv-fraser, inget "
     "fristående ord), så synonymen sätts som kategori ur kortets egen "
     "definition. Legacys 'blåblus'/'arbetsblus'/'överdragsplagg' är inte "
     "belagda som fullt utbytbara ord."),

"fibromyalgi": dict(
  hb="En sjukdom som ger ständig smärta i muskler och senor, vanligast hos "
     "kvinnor som kan få barn",
  reg="fackspråklig, neutral, medicin",
  grp=[["≈≈ sjukdom"]],
  ex="Hennes %s gjorde att hon vaknade öm i hela kroppen varje morgon." % B("fibromyalgi"),
  sl="SO: '(tillstånd av) kronisk smärta i muskler och senfästen' med tillägget "
     "'som främst drabbar kvinnor i fertil ålder' -- båda med i huvudbetydelsen. "
     "SAOL: 'en sjukdom med bl.a. muskelvärk', samma betydelse. Inget enskilt "
     "ord i källorna inleder ett led som är utbytbart, så synonymen sätts som "
     "kategori (≈≈ sjukdom, ur SAOL:s eget 'en sjukdom'). Legacys "
     "'tillstånd'/'muskelvärk'/'trötthet' är inte belagda som fulla synonymer."),

"specificera": dict(
  hb="Beskriva något i detalj i stället för bara ungefär ; i en räkning: ange "
     "exakt vad varje belopp gäller",
  reg="neutral, neutral ; neutral, neutral, ekonomi",
  grp=[["≈≈ beskrivning"], ["ange"]],
  ex="Han fick %s exakt vilka ändringar han ville ha i avtalet." % B("specificera"),
  sl="SO ger TVÅ: huvudbetydelsen 'ge närmare beskrivning av (något)' och en "
     "underbetydelse (typ 'spec.') med EGEN definition: 'ange vad olika belopp "
     "i en uppställning utgör betalning för' -- en riktig andra betydelse, inte "
     "bara en utvidgning (samma princip som kompendium samma dag). SAOL: "
     "'noggrant räkna upp el. förteckna, noga ange' (en betydelse, komma "
     "skiljer omformuleringar av samma sak). 'ange' inleder SO:s "
     "underbetydelse ordagrant och är alltså belagd för betydelse två. Inget "
     "ord inleder ett led för första betydelsen (SAOL har de framförställda "
     "orden 'noggrant'/'noga' först i sina led, inte glosan själv), så "
     "synonymen sätts som kategori (≈≈ beskrivning) ur kortets egen "
     "definition för den betydelsen."),

"utlåta": dict(
  ordfix="utlåta sig",
  hb="Säga vad man tycker om något offentligt, ofta med kritik",
  reg="formell, neutral",
  grp=[["yttra sig", "ge sin bedömning"]],
  ex="Rektorn %s skarpt om lärarnas nya schema." % B("utlät sig"),
  sl="Framsidan 'utlåta' saknar exakt SO/SAOL-träff (traffar=saob) -- "
     "SO och SAOL har BARA 'utlåta sig' (reflexivt) som eget uppslagsord, "
     "bekräftat genom ny sökning på den formen (traffar=saol,so). Framsidan "
     "rättad via proposed_ord, matchar SO:s ortografi exakt -- legacy hade "
     "redan 'utlåta sig' i sin egen exempelmening trots att Framsidan saknade "
     "'sig', vilket avslöjade felet. SO: 'yttra sig' med tillägget 'ofta på "
     "ett kritiskt sätt', tillägget med i huvudbetydelsen. SAOL: 'yttra sig, "
     "ge sin bedömning' -- komma skiljer omformuleringar av samma betydelse, "
     "båda inleder egna led och är belagda."),

"antiklerikal": dict(
  hb="Motståndare till kyrkan och dess makt i samhället",
  reg="neutral, neutral, religion",
  grp=[["≈≈ motståndare"]],
  ex="Han kallade sig %s och vägrade gå i kyrkan." % B("antiklerikal"),
  sl="SO: 'som är motståndare till kyrkan', en betydelse -- SO:s eget "
     "ämnesområdestagg 'relig.' på ordledsposten bekräftar domänen. SAOL har "
     "bara en korshänvisning till anti- + klerikal, ingen egen definitionstext "
     "att belägga synonymer mot. Inget enskilt ord inleder ett led som är "
     "utbytbart, så synonymen sätts som kategori (≈≈ motståndare) ur kortets "
     "egen definition, som ordagrant följer SO:s formulering. Legacys "
     "'prästfientlig'/'kyrkofientlig' är inte belagda."),

"geschwint": dict(
  hb="Snabbt och utan ansträngning",
  reg="vardaglig, neutral",
  grp=[["snabbt"]],
  ex="Hon sprang %s upp för trapporna innan bussen skulle gå." % B("geschwint"),
  sl="SO: 'snabbt och lätt' [vardagligt]. SAOL: identisk text [vard.]. En "
     "betydelse; frasen delas inte av komma/semikolon så 'snabbt' inleder "
     "hela ledet och är belagd. Legacys andra definition var bara en "
     "omskrivning av samma betydelse."),

"kompendium": dict(
  hb="Kort sammanfattning av ett ämne, ofta för högskolestudier ; en "
     "kortfattad lärobok ; (på en kamera) skydd mot motljus",
  reg="neutral, neutral ; neutral, neutral ; fackspråklig, neutral, teknik",
  grp=[["sammandrag"], ["≈≈ lärobok"], ["motljusskydd"]],
  ex="Han läste igenom hela %s kvällen före tentan." % B("kompendiet"),
  sl="SO: huvudbetydelsen 'sammandrag av utförlig framställning' med tillägget "
     "'särsk. i samband med (högre) undervisning', plus en underbetydelse "
     "(typ 'spec.') med EGEN definition: 'kortfattad läro- eller handbok' -- "
     "behandlad som riktig andra betydelse, samma princip som specificera "
     "samma dag. SAOL bekräftar samma tvådelning ('sammandrag; kortfattad "
     "handbok') OCH ger en tredje, HELT orelaterad betydelse: 'motljusskydd på "
     "filmkamera' -- en äkta homonym som saknades helt i legacy-innehållet. "
     "'sammandrag' inleder SAOL:s första led (belagd, betydelse 1). 'handbok' "
     "föregås av 'kortfattad' i båda källorna (ingen egen synonymglosa), så "
     "betydelse 2 får en kategori (≈≈ lärobok) ur kortets egen definition. "
     "'motljusskydd' inleder SAOL:s tredje betydelse ordagrant (belagd, "
     "betydelse 3)."),
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
    ordkalla = f.get("ordfix") or e["ord"]
    e["sokkoll"] = {"kalla": U(ordkalla), "slutsats": f["sl"]}
    if f.get("ordfix"):
        e["proposed_ord"] = f["ordfix"]
    if f.get("till"):
        e["forgranska_tillat"] = f["till"]
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("godkande %d kort" % n)
