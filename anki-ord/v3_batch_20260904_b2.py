# -*- coding: utf-8 -*-
"""Spar A batch 2026-09-04, del 2 (ord 14-25). Sokkoll via slaupp.py."""
import io, json
FIL = "sessions/session_2026-09-04_v3-batch.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: f"https://svenska.se/api/msearch?ord={o}"

FIX = {
"hårklyveri": dict(
  hb="Att gräla om en skillnad som är för liten för att spela roll",
  reg="neutral, lätt negativ",
  grp=[["≈≈ pedanteri"]],
  ex="Diskussionen om kommatecknet blev rent %s." % B("hårklyveri"),
  sl="SO: 'meningslöst exakt utläggning eller analys av något i grunden trivialt'. SAOL: "
     "'meningslöst exakt analys'. En betydelse. Inget ord i SO/SAOL inleder ett eget led, "
     "så synonymen sätts som kategori."),

"logi": dict(
  hb="Tak över huvudet för en kortare tid",
  reg="neutral, neutral",
  grp=[["husrum"]],
  ex="Priset inkluderar resa, mat och %s." % B("logi"),
  sl="SO: 'tillfällig bostad'. SAOL: 'husrum' — inleder ledet, alltså belagd synonym. "
     "Cirkulärflaggan på kortet åtgärdad.",
  till={"betydelse_kan_saknas": "SAOL:s andra post ('huvudbyggnad pa herrgard') ar ett "
        "annat lemma; SO:s under saknar egen definition."}),

"obändig": dict(
  hb="Går inte att tygla eller trycka ner",
  reg="neutral, neutral",
  grp=[["våldsam","vild"]],
  ex="Hon hade en %s vilja att vinna." % B("obändig"),
  sl="SO: 'som inte låter sig påverkas och undertryckas'. SAOL: 'svår att tygla el. "
     "behärska, våldsam, vild' — våldsam och vild inleder egna led."),

"synkron": dict(
  hb="Sker samtidigt ; går i exakt samma takt och fas",
  reg="neutral, neutral ; fackspråklig, neutral, teknik",
  grp=[["samtidig"],["≈≈ i fas"]],
  ex="Ljudet låg inte %s med bilden." % B("synkront"),
  sl="SO: 'samtidig' plus underbetydelsen 'som alltid motsvarar en bestämd fas i visst "
     "förlopp' — den har egen definition och är alltså en riktig andra betydelse. SAOL: "
     "'samtidig' (belagd)."),

"workshop": dict(
  hb="Träff där en liten grupp jobbar praktiskt och delar kunskap med varandra",
  reg="neutral, neutral",
  grp=[["kollokvium","≈≈ möte"]],
  ex="Vi drar igång en %s om studieteknik på lördag." % B("workshop"),
  sl="SO: 'möte där en mindre grupp deltagare delar med sig av sina kunskaper eller "
     "erfarenheter'. SAOL avslutar med 'kollokvium', som inleder eget led och därmed är "
     "belagd. En betydelse — kortets 'arbetstemadag' i OLD-facit är ingen gångbar svenska."),

"asocial": dict(
  hb="Bryter mot samhällets grundregler ; vill inte umgås med andra",
  reg="neutral, negativ ; neutral, neutral",
  grp=[["avvikande"],["≈≈ tillbakadragen"]],
  ex="Han blev alltmer %s och slutade svara i telefon." % B("asocial"),
  sl="SO ger TVÅ: 'som bryter mot grundläggande samhällsnormer' och underbetydelsen 'som "
     "inte tycker om att umgås med andra människor' (egen definition). SAOL: 'avvikande "
     "från samhällets normer' — avvikande belagd. De två betydelserna är olika laddade: "
     "den första är negativ, den andra bara beskrivande."),

"entrecote": dict(
  hb="Skiva nötkött från ryggen, mitt på djuret",
  reg="neutral, neutral, matlagning",
  grp=[["≈≈ köttbit"]],
  ex="Han beställde %s med bearnaise." % B("entrecote"),
  sl="SO: '(maträtt av) skiva nötkött från ryggraden vid djurets mittparti'. SAOL: 'stycke "
     "av mellanrev'. En betydelse; inget enskilt ord är belagt som synonym."),

"formulera": dict(
  hb="Sätta ord på något så att det blir tydligt",
  reg="neutral, neutral",
  grp=[["uttrycka"]],
  ex="Han hade svårt att %s vad som störde honom." % B("formulera"),
  sl="SO: 'ge (tydlig) språklig form åt'. SAOL: 'uttrycka i ord' — uttrycka inleder ledet "
     "och är belagd. En betydelse."),

"friställa": dict(
  hb="Säga upp folk, sagt på ett snyggare sätt ; göra något ledigt att använda",
  reg="neutral, eufemistisk ; fackspråklig, neutral",
  grp=[["≈≈ avskeda"],["≈≈ frigöra"]],
  ex="Fabriken %s fyrtio anställda i våras." % B("friställde"),
  sl="SO ger TVÅ: 'säga upp från arbete p.g.a. brist på arbetstillfällen' med märkningen "
     "[ofta ett slags förskönande omskrivning], och 'göra ledig för användning'. "
     "Märkningen är skäl nog att sätta valören eufemistisk — det är hela poängen med ordet."),

"förtrolig": dict(
  hb="Öppen och tillitsfull mot någon ; sagt i förtroende",
  reg="neutral, neutral ; neutral, neutral",
  grp=[["intim"],["≈≈ konfidentiell"]],
  ex="De satt i ett %s samtal i timmar." % B("förtroligt"),
  sl="SO: 'vänskapligt öppen och tillitsfull' plus underbetydelsen 'som lämnas i "
     "förtroende' (egen definition). SAOL: 'som sker i förtroende, intim' — intim inleder "
     "eget led."),

"förtäckt": dict(
  hb="Halvt dolt, sagt utan att sägas rakt ut",
  reg="neutral, neutral",
  grp=[["dold"]],
  ex="Det var ett %s hot." % B("förtäckt"),
  sl="SO: 'halvt dold eller outsagd'. SAOL: 'dold' — belagd. En betydelse."),

"hänförande": dict(
  hb="Så vackert eller bra att man tappar hakan",
  reg="litterär, positiv",
  grp=[["≈≈ förtjusande"]],
  ex="Utsikten från toppen var %s." % B("hänförande"),
  sl="SO: 'som väcker stark och oemotståndlig förtjusning'. SAOL:s poster ('räkna till', "
     "'fascinera') hör till lemmat HÄNFÖRA, inte hänförande — används därför inte som "
     "belägg. En betydelse."),
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
    if (e["legacy"] or {}).get("bild_html"):
        e["proposed"]["bild_html"] = e["legacy"]["bild_html"]
    e["sokkoll"] = {"kalla": U(e["ord"]), "slutsats": f["sl"]}
    if f.get("till"):
        e["forgranska_tillat"] = f["till"]
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"godkande {n} kort")
