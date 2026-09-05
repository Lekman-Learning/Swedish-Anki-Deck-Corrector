# -*- coding: utf-8 -*-
"""Spar A batch 2026-09-05, batch2, grupp 1 (ord 0-7). Sokkoll via slaupp.py."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-05_v3-batch2.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"blast": dict(
  hb="Blad och stjälkar som sitter kvar ovanpå en rotfrukt, till exempel potatis",
  reg="neutral, neutral",
  grp=[["≈ bladverk"]],
  ex="Efter skörden plöjdes %s ner i åkern." % B("blasten"),
  sl="SO: 'blad och stjälkar av rotfrukt'. SAOL: identisk text, en betydelse. Inget "
     "enskilt ord i källorna inleder ett eget led, så närmaste ord tas ur "
     "synonymer.se (redaktionellt: 'bladverk'), märkt ≈. Legacys exempelmening "
     "påstod att potatisblast användes som djurfoder -- växtdelen innehåller solanin "
     "och är giftig för djur, ett sakfel i legacy-innehållet. Bytt mot en neutral "
     "mening om att plöja ner den."),

"bouquet": dict(
  hb="Den speciella doften och smaken hos till exempel ett vin eller en konjak",
  reg="neutral, positiv",
  grp=[["≈ arom"]],
  ex="Sommelieren beskrev vinets fylliga %s av mogna bär." % B("bouquet"),
  sl="SO: 'karakteristisk (angenäm) doft och smak <<särsk. hos vin och konjak>>' -- "
     "definitionstillägget om vin/konjak är med. SAOL: 'doft hos vin', samma betydelse. "
     "'Arom' är SO:s JFR:cohyponym (inte SYN), märkt ≈. Valör positiv eftersom SO själv "
     "skriver 'angenäm'."),

"ciceron": dict(
  hb="En kunnig person som visar besökare runt bland sevärdheter eller andra spännande platser",
  reg="neutral, neutral",
  grp=[["vägvisare", "guide"]],
  ex="Sällskapets %s berättade ivrigt om varje staty på torget." % B("ciceron"),
  sl="SO-lemma 'ciceron': 'person som sakkunnigt förevisar sevärdheter <<el. andra "
     "intressanta företeelser>>' -- definitionstillägget är med. Underbetydelsen (om "
     "reseskildrare) saknar egen definition, en utvidgning. SAOL: 'vägvisare, guide' -- "
     "båda inleder ledet, belagda. OBS: samma sökning ger också en HELT ANNAN SAOL-lemma "
     "'cicero' ('en stilgrad', boktryckarstil) vars BESTÄMDA form råkar stavas 'ciceron' "
     "-- samma inflektionskrock som te/tes och gem/gemen (se CLAUDE.md 2026-08-11). "
     "Deckets uppslagsord 'ciceron' är obestämd form och matchar bara guide-lemmat, inte "
     "stilgrads-lemmat (vars obestämda form är 'cicero'), så stilgraden hör inte hemma "
     "på kortet."),

"spröd": dict(
  hb="Går lätt sönder, till exempel för att den är luftig eller torr ; (bildligt, om person) verkar bräcklig och svag",
  reg="neutral, neutral ; neutral, neutral",
  grp=[["≈ skör"], ["≈ svag"]],
  ex="Det gamla brevpapperet var så %s att det gick sönder i händerna." % B("sprött"),
  sl="SO ger TVÅ: huvudbetydelsen 'som lätt bryts eller trycks sönder <<p.g.a. luftig "
     "struktur eller dylikt>>' (definitionstillägg med) och underbetydelsen 'ofta "
     "bildligt om person: som ger intryck av att vara lätt och svag' -- den HAR egen "
     "definition, alltså en riktig andra betydelse (legacy hade bara en, cirkulärt "
     "definierad med 'sprödhet'). SAOL saknar egen definitionstext för spröd. SO:s "
     "jfr-ord (bräcklig, mör, skör) är JFR:cohyponym, inte SYN -- 'skör' klarar "
     "insättningstestet bäst, märkt ≈. 'Svag' till andra betydelsen från synonymer.se "
     "(redaktionellt), märkt ≈."),

"ödslig": dict(
  hb="Ligger öde och känns tomt och övergivet",
  reg="neutral, lätt negativ",
  grp=[["öde", "obebodd"]],
  ex="Det gamla, %s slottet ekade tomt när vinden for genom salarna." % B("ödsliga"),
  sl="SO: 'som är eller ligger 2öde <<och därmed ger en känsla av övergivenhet>>' -- "
     "definitionstillägget om känslan av övergivenhet är med. Underbetydelsen ('äv. "
     "bildligt') saknar egen definition, en utvidgning. SAOL: 'öde, obebodd' -- båda "
     "inleder egna led, belagda. Valör lätt negativ eftersom SO:s eget exempel "
     "('tillvaro allt ensammare och ödsligare') visar en melankolisk bibetydelse."),

"förklenande": dict(
  hb="Talar nedsättande om något eller någon för att få det att verka sämre än det är",
  reg="neutral, negativ",
  grp=[["nedsättande"]],
  ex="Han talade förklenande om kollegans insats, som om den inte betydde något." ,
  sl="SO: 'nedsättande' -- hela definitionen är ordet 'nedsättande', som alltså inleder "
     "(=utgör) ledet och är fullt belagt. SAOL-artikeln som hittas ('med förtal "
     "förringa') hör till grundverbet 'förklena', inte till presensparticipet "
     "'förklenande' som eget uppslagsord -- använd inte den som egen källa för "
     "adjektivet, bara som stöd för att betydelsen hänger ihop. En betydelse."),

"notorisk": dict(
  hb="Känd av alla för att göra dåliga eller tvivelaktiga saker, om och om igen",
  reg="neutral, negativ",
  grp=[["ökänd"]],
  ex="Han var en notorisk skolkare som aldrig dök upp på lektionerna.",
  sl="SO: en betydelse, 'som uppmärksammas på grund av (moraliskt) tvivelaktiga "
     "handlingar eller egenskaper', underbetydelsen ('äv. om handling') saknar egen "
     "definition. SAOL skriver 'allbekant; otvivelaktig; ökänd' som TRE semikolon-"
     "skilda glosor för samma SAOL-lemma -- testat i egen mening ('en notorisk "
     "lögnare'): bara 'ökänd' håller ('en ökänd lögnare' fungerar), 'allbekant'/"
     "'otvivelaktig' känns ålderdomliga/fel nyans där ('en allbekant lögnare' känns "
     "konstigt) och utelämnas. Ökänd är dessutom SO:s JFR:cohyponym."),

"nyansera": dict(
  hb="Visa på fler fina skillnader i något, till exempel en beskrivning eller en känsla ; mjuka upp ett tidigare uttalande, oftast för att dämpa det",
  reg="neutral, neutral ; neutral, neutral",
  grp=[["≈ fördjupa"], ["förändra", "modifiera"]],
  ex="Historikern nyanserade sin bild av kriget genom att lyfta fram flera perspektiv.",
  sl="SO ger TVÅ under samma lemma 'nyansera': huvudbetydelsen 'åstadkomma finare "
     "skiftningar i <<någon framställning etc., särsk. med avseende på begrepp, "
     "känslor eller dylikt>>' (tillägget med) och underbetydelsen MED EGEN definition "
     "'förändra, modifiera <<vanligen i dämpande riktning>>' -- en riktig andra "
     "betydelse (legacy hade bara den första). Den reflexiva 'nyansera sig' är ett "
     "SKILT SO-lemma (eget l_nr) och hör inte hit. SAOL: 'ge nyanser; framställa el. "
     "utforma med nyanser; förändra, modifiera' -- sista ledet ('förändra, modifiera') "
     "svarar mot andra betydelsen, båda orden belagda. Ingen enda-ords-synonym till "
     "första betydelsen inleder ett led; 'fördjupa' tas från synonymer.se "
     "(redaktionellt), märkt ≈."),
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
