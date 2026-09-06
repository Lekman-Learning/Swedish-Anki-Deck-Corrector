# -*- coding: utf-8 -*-
"""Spar B (omgranskning), repetition3, 2026-09-05. Sokkoll via slaupp.py,
verifierat ord for ord mot SO/SAOL:s ravdata (uppslag/<ord>.json) och
old_facit. Se sokkoll.slutsats per post for motivering."""
import io, json

FIL = "sessions/session_2026-09-05_v3-omgranskning-repetition3.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % o

FIX = {

# ---------------------------------------------------------------- ANDRADE
"demolera": dict(
  hb="Slå sönder eller förstöra ett större föremål helt och hållet",
  reg="vardaglig, negativ",
  grp=[["förstöra", "rasera", "riva"]],
  ex='Bilen blev helt %s vid krocken.' % B("demolerad"),
  etym="av latin demoli´ri med samma betydelse, till de 'ned' och moli´ri 'bygga; upprätta'",
  sl="SO: 'helt förstöra <<(större) föremål eller dylikt>>' — definitionstillägget "
     "('större föremål') var uteslutet i legacy och är obligatorisk kontext (utan den "
     "låter det som att man kan demolera vad som helst, t.ex. ett papper). Tillagt. "
     "SAOL: 'riva, rasera' — båda inleder egna led, belagda. 'förstöra' inleder SO:s "
     "definition, också belagt. En betydelse."),

"torsion": dict(
  hb="Vridning som gör att den ena änden av ett långsträckt föremål vänds åt ett annat "
     "håll än den andra",
  reg="fackspråklig, neutral, fysik",
  grp=[["≈≈ vridning"]],
  ex="Ingenjören beräknade axelns %s innan den sattes i drift." % B("torsion"),
  etym="av franska torsion med samma betydelse; till latin torque´re 'vrida'; jfr "
       "ursprung till distorsion, tordera, tortyr, tvär",
  sl="SO har EN huvudbetydelse ('formförändring hos (långsträckt) kropp när den ena "
     "ändan vrids i förhållande till den andra' [brukl: fysik, teknik]) med en "
     "underbetydelse 'spec. medicin' (torsion av navelsträngen) som saknar EGEN "
     "definition — en utvidgning, inte en andra betydelse. Legacy hade felaktigt gjort "
     "utvidgningen till en egen registrerad betydelse med eget register/synonymgrupp. "
     "Slagit ihop till en betydelse. Kategorin '≈≈ vridning' hämtad ur kortets egen "
     "definition, kräver ingen källa."),

"vakuum": dict(
  hb="Ett utrymme helt utan luft — används också bildligt om ett tomrum där något som "
     "borde finnas saknas",
  reg="neutral, neutral",
  grp=[["lufttomt rum", "tomrum"]],
  ex="Man kan skapa ett %s genom att pumpa ut all luft ur en behållare." % B("vakuum"),
  etym="av latin vac´uum med samma betydelse, till vac´uus 'tom; ledig'; jfr ursprung "
       "till vakant",
  sl="SO har EN huvudbetydelse ('fullständigt tomrum <<särsk. med tanke på frånvaro av "
     "luft>>') med en underbetydelse 'äv. bildligt' (maktvakuum, känslomässigt vakuum) "
     "utan egen definition — en utvidgning. Legacy hade gjort den till en egen "
     "registrerad betydelse med eget register/synonymgrupp; slagit ihop till en. SAOL "
     "bekräftar: 'lufttomt rum; tomrum; äv. bildl.' — samma mönster, tredje ledet är en "
     "bruksnot utan egen synonym. Registret 'fackspråklig' på förra kortet stämde inte "
     "heller: SO ger ingen bruklighetskommentar för ordet (till skillnad från t.ex. "
     "torsion), så det är allmänt ordförråd. Synonymerna 'lufttomt rum' och 'tomrum' "
     "inleder varsitt led i SAOL, belagda."),

"avnämare": dict(
  hb="Mottagare av en vara — ofta ett företag som köper in råvaror eller halvfabrikat "
     "för att bearbeta eller sälja dem vidare",
  reg="formell, neutral, ekonomi",
  grp=[["mottagare"]],
  ex="Livsmedelsindustrin är en %s av jordbruksprodukter." % B("avnämare"),
  sl="SO: 'mottagare av vara <<särsk. råvara el. halvfabrikat för försäljning el. "
     "vidare förädling>>' — definitionstillägget var uteslutet i legacy ('Mottagare "
     "eller köpare av en vara' är för allmänt, säger inget om den industriella "
     "kontexten som gör ordet meningsfullt). Tillagt. SAOL: 'mottagare av vara el. "
     "annan nyttighet' — 'mottagare' inleder båda definitionerna, belagt. 'köpare' och "
     "'konsument' stod i legacy men inleder inget led i SO/SAOL och är dessutom inte "
     "fullt utbytbara (en avnämare kan vara mottagare utan att vara slutkonsument) — "
     "borttagna, 'mottagare' räcker som belagd synonym."),

"blekfet": dict(
  hb="Blek i ansiktet och lite uppsvälld och slapp att se på",
  reg="vardaglig, lätt negativ",
  grp=[["uppsvälld", "≈ plussig", "≈ pösig"]],
  ex="Han hade ett %s ansikte efter sjukdomen." % B("blekfet"),
  sl="SO: 'som är blek och gör ett slappt, uppsvällt intryck <<om person, ansikte el. "
     "kropp>>' — TVÅ egenskaper (blek OCH slappt/uppsvällt intryck). Legacy hade bara "
     "'blek och uppsvälld', halva definitionen — 'slapp' saknades helt. Tillagt. "
     "'uppsvälld' matchar SO:s 'uppsvällt' rakt av, belagt. SAOL saknar egen "
     "definitionstext för ordet. 'plussig' och 'pösig' finns bara i synonymer.se "
     "(redaktionell avdelning, https://www.synonymer.se/sv-syn/blekfet) — inte i "
     "SO/SAOL:s definitionstext — märkta ≈. old_facit ('plussig') bekräftar valet."),

"fibrös": dict(
  hb="Uppbyggd av sega fibrer eller bindväv",
  reg="fackspråklig, neutral, biologi",
  grp=[["fibrig", "trådig"]],
  ex="Köttbiten var seg och %s, full av senor som var svåra att tugga." % B("fibrös"),
  sl="Innehållet stämmer redan (SO: 'som består av (rikligt förekommande) bindväv'; "
     "SAOL breddar till 'fibrig, trådig' — bägge inleder egna led, belagda; exemplet "
     "med senor/bindväv i kött matchar SO exakt). Enda felet var registret: 'formell' "
     "användes för 'ovanligt/tekniskt klingande ord' — precis den felanvändning "
     "config.py varnar för. Ordet är fackspråkligt (medicin/biologi), inte "
     "byråkratiskt. Rättat till fackspråklig + domän biologi. Synonymen 'fintrådig' "
     "stod inte i SO/SAOL och är struken (fibrig/trådig räcker och är belagda)."),

"virtuos": dict(
  hb="Som visar enastående skicklighet inom sitt område ; Person med enastående "
     "skicklighet, ofta inom musik",
  reg="neutral, positiv ; neutral, positiv",
  grp=[["skicklig"], ["≈≈ skicklig person"]],
  ex="Den unga %s pianisten fick hela konsertsalen att resa sig i stående ovationer." % B("virtuosa"),
  sl="SO har TVÅ separata lemman för virtuos: adjektiv ('som visar enastående "
     "skicklighet <<särsk. vid (det tekniska) utövandet av en konst>>') och substantiv "
     "('person som visar enastående skicklighet <<särsk. inom musiken ... men äv. "
     "allmännare>>'). Legacy hade bara adjektivbetydelsen — substantivbetydelsen "
     "(en virtuos = en person) saknades helt, tillagd. SAOL bekräftar båda: "
     "'enastående skicklig' / 'tekniskt överlägset skicklig konstnär'. Register "
     "'formell' var fel av samma skäl som fibrös — bytt till neutral. 'skicklig' "
     "inleder SAOL:s definition, belagt; andra gruppen är en kategori hämtad ur "
     "kortets egen definition."),

"böjd": dict(
  hb="Krökt eller vriden i formen ; Benägen eller villig att göra något",
  reg="neutral, neutral ; vardaglig, neutral",
  grp=[["krökt"], ["benägen", "villig"]],
  ex="Jag är %s att instämma i vad du säger." % B("böjd"),
  sl="SAOL: 'krökt; bildl. benägen' — SEMIKOLON skiljer BETYDELSER, och legacy hade "
     "bara den bildliga ('benägen eller villig'), inte den bokstavliga fysiska "
     "betydelsen (krökt/böjd i formen). SO:s DEF för adjektivet 'böjd' är en "
     "korshänvisning till 'benägen', vilket bara täcker halva SAOL-posten. Tillagt "
     "den bokstavliga betydelsen. 'krökt' inleder SAOL:s första led, belagt. "
     "'benägen'/'villig' oförändrade från legacy (benägen är SO:s egen "
     "korshänvisning)."),

"hövisk": dict(
  hb="Artigt, belevat och fint uppträdande, gärna på ett ridderligt sätt — särskilt om "
     "kärlek: byggd på beundran och tillbakahållen sexualitet, inte på det köttsliga",
  reg="litterär, positiv",
  grp=[["ärbar", "taktfull", "ridderlig"]],
  ex="Han bugade sig %s och höll upp dörren åt henne." % B("hövisk"),
  sl="SO har EN huvudbetydelse ('artig och taktfull på ett förfinat och elegant sätt') "
     "med en underbetydelse ('ofta spec. i fråga om kärleksförhållande som präglas av "
     "tillbedjan och nedtoning av det sexuella') UTAN egen definition — en utvidgning "
     "av samma grundbetydelse, inte en andra betydelse. Legacy hade gjort den till en "
     "egen registrerad betydelse ('litterär, ömsint') med eget register. Slagit ihop "
     "till EN betydelse som nämner båda nyanserna, matchar SO:s råstruktur. SAOL: "
     "'ärbar, taktfull; ridderlig' — alla tre inleder egna led, belagda och "
     "oförändrade."),

"katjon": dict(
  hb="Positivt laddad jon",
  reg="fackspråklig, neutral, kemi",
  grp=[["positiv jon"]],
  ex="Natriumkatjonen Na+ är en vanlig %s i saltlösningar." % B("katjon"),
  sl="Innehållet stämmer (SO: 'positivt laddad jon <<som vid elektrolys eller dylikt "
     "vandrar till katoden>>'; SAOL detsamma). Enda felet var registret: 'formell' "
     "för ett rent kemibegrepp, samma felanvändning som fibrös/virtuos. Rättat till "
     "fackspråklig + domän kemi."),

"lagg": dict(
  hb="Flat stekpanna för plättar ; Stav i ett träkärl ; Kant/övergångszon vid en "
     "högmosse ; En skida, mest använt i plural (laggar)",
  reg="vardaglig, neutral ; vardaglig, neutral ; formell, neutral ; dialektal, "
      "neutral, sport",
  grp=[["stekpanna", "plättsats"], ["tunnstav"], ["mosskant"], ["skida"]],
  ex="Hon värmde upp %s innan hon började grädda pannkakorna." % B("laggen"),
  sl="SAOL listar FYRA separata huvudbetydelser för lagg: 'stav till träkärl', 'flat "
     "panna för gräddning av pannkakor o.d.', 'kant av mosse' OCH 'skida' (med "
     "formkommentaren 'mest i pl.'). Legacy hade bara tre — skida (dialektalt ord för "
     "skidor, laggar) saknades helt, trots att SAOL:s egna ämnesområden bekräftar det "
     "('geol., geogr., sport, matlagn.' — fyra domäner för fyra betydelser). Tillagt "
     "som fjärde betydelse, domän sport, formalitet dialektal (regionalt/ålderdomligt "
     "ord för skidor). 'skida' inleder SAOL:s fjärde led, belagt."),

"resolut": dict(
  hb="Bestämd och snabb att agera, särskilt i en svår situation",
  reg="neutral, positiv, allmän",
  grp=[["beslutsam", "rask"]],
  ex="Hon tog %s initiativet när de andra tvekade." % B("resolut"),
  sl="SO: 'kraftfull och bestämd <<särsk. i situation som fordrar snabb handling>>' — "
     "definitionstillägget (kravet på SNABB handling i en svår situation) var "
     "uteslutet i legacy ('kraftfull och bestämd i sitt handlande' säger inget om "
     "tempo eller svårighet). Tillagt. SAOL: 'beslutsam, rask' — båda inleder egna "
     "led, belagda och oförändrade från legacy."),

"rosa": dict(
  hb="Ljust röd eller skär färg ; Berömma och prisa",
  reg="vardaglig, neutral ; neutral, positiv",
  grp=[["skär"], ["berömma", "prisa"]],
  ex="Hon svepte in sig i en varm %s morgonrock innan kaffet var klart." % B("rosa"),
  sl="SO har två helt skilda lemman (adjektiv 'ljust röd', verb 'ge beröm'), redan "
     "korrekt fångade som två betydelser i legacy. Två fixar: (1) registret var EN "
     "gemensam rad för båda betydelserna trots att de är olika ordklasser med olika "
     "valör — delat upp per betydelse, verbet fick valören 'positiv' (att berömma är "
     "en positivt laddad handling). (2) synonymen 'skär (färg)' hade en onödig "
     "parentes klistrad på — SAOL:s ord är bara 'skär', förenklat. 'berömma' matchar "
     "SO:s 'ge beröm', 'prisa' står ordagrant i SAOL: 'lovorda, prisa' — båda belagda."),

"sofism": dict(
  hb="Skenbart logiskt men egentligen felaktigt resonemang",
  reg="fackspråklig, neutral, filosofi",
  grp=[["spetsfundighet", "felslut"]],
  ex="Att hävda att alla hundar är djur, därför är alla djur hundar, är en %s." % B("sofism"),
  sl="Definitionen stämmer mot SO ('yttrande som skenbart är egendomligt eller "
     "orimligt men i verkligheten kan bevisas genom någon typ av logiskt resonemang "
     "<<och som framförs i syfte att briljera, provocera eller dylikt>>') och matchar "
     "kortets egen exempelmening (en ogiltig syllogism som LÅTER logisk). Två fixar: "
     "registret 'formell' bytt till fackspråklig + domän filosofi (samma "
     "felanvändningsmönster som fibrös/katjon/virtuos — ordet är en logik-/"
     "retorikterm, inte byråkratspråk). Synonymen 'skenargument' stod inte i SAOL — "
     "bytt mot 'felslut', som inleder SAOL:s andra led ('spetsfundighet; avsiktligt "
     "felslut') och alltså är belagt. Ingen semikolon-betydelse: SO har bara EN "
     "huvudbetydelse för ordet, så SAOL:s två ord räknas som två synonymer för samma "
     "betydelse (jfr korrosions 'rostning; frätning' för en och samma delbetydelse)."),

"solvens": dict(
  hb="God betalningsförmåga",
  reg="formell, neutral, ekonomi",
  grp=[["betalningsförmåga", "≈ kreditvärdighet"]],
  ex="Bolagets %s var stark trots konjunkturnedgången." % B("solvens"),
  sl="SAKFEL: legacy hade en andra 'betydelse' ('tråd med ögla för varptrådar i "
     "vävstol') som INTE hör till solvens alls — det är en definition av det HELT "
     "ANDRA, orelaterade ordet 'solv' (en väv-/vävstolsterm), som bara råkade följa "
     "med i svenska.se:s fuzzy-sökning på 'solvens' eftersom orden delar "
     "bokstavsprefix. Samma kontamineringsfälla som drabbat flerordsuttryck tidigare "
     "i projektet, fast här på ett enskilt ord. SO/SAOL har bara EN betydelse för "
     "solvens: '(god) betalningsförmåga'. Den fabricerade andra betydelsen, dess "
     "register och synonymen 'solv' borttagna helt. 'betalningsförmåga' inleder "
     "definitionen, belagt. 'kreditvärdighet' är inte ordagrant i SO/SAOL men är en "
     "etablerad nära synonym inom ekonomi — märkt ≈."),

"stab": dict(
  hb="Personal som biträder en ledare eller chef",
  reg="formell, neutral, militär",
  grp=[["medarbetare", "≈ ledningsgrupp"]],
  ex="Generalen konsulterade sin %s innan operationen påbörjades." % B("stab"),
  sl="Innehållet stämmer (SO: 'personal som biträder militär chef' med utvidgningen "
     "'äv. om annan (biträdande) personal', t.ex. 'presidentens stab', 'restaurangens "
     "stab av kypare' — bekräftar att kortets bredare definition, som redan gäller "
     "'en ledare eller chef' i allmänhet, är rätt). SAOL: 'personal som biträder "
     "militär chef; samling medarbetare' — 'medarbetare' inleder andra ledet, belagt. "
     "'ledningsgrupp' stod i legacy men inleder inget led och är inte fullt utbytbart "
     "(en ledningsgrupp FATTAR beslut, en stab BITRÄDER en chef) — märkt ≈."),
}

# --------------------------------------------------------------- OFORANDRADE
UNCHANGED_SL = {
"korrosion": "Legacy stämmer redan mot SO:s TVÅ huvudbetydelser: 'metallförstöring "
    "genom kemisk inverkan av vätskor eller gaser <<som t.ex. bildar rost på järn och "
    "ärg på koppar>>' och 'nötning och avslipning av fast berggrund genom yttre "
    "krafter <<särsk. partiklar som transporteras av vind, vatten el. is>>' — rätt "
    "antal betydelser, rätt register per betydelse (kemi/geologi), rätt domänuppdelning. "
    "SAOL: 'rostning; frätning' — båda inleder egna led och är korrekt kopplade till "
    "första betydelsen. Andra gruppen '≈≈ nednötning' är en kategori hämtad ur "
    "kortets egen definition, kräver ingen källa. Exempelmeningen matchar första "
    "betydelsen. Oförändrat.",
"inbäddad journalist/reporter": "Fritextsökningen på frasen kontaminerades kraftigt "
    "(matchade 'journalist', 'reporter', 'bädda in' m.fl. som separata artiklar), men "
    "den relevanta träffen finns: SO:s artikel för 'bädda in' har en underbetydelse "
    "'spec. äv. med avseende på krigskorrespondenter som färdas tillsammans med "
    "framryckande trupper' med exemplet 'den amerikanska armén bäddade in journalister "
    "i vissa förband i Irak' — matchar kortets definition exakt, och old_facit "
    "('vederbörande som följer ett förband') bekräftar. 'krigskorrespondent' är ordagrant "
    "SO:s egen term för fenomenet. Oförändrat.",
"sila mygg och svälja kameler": "Biblisk idiom (Matt 23:24), ingen egen SO/SAOL-artikel "
    "för hela uttrycket (fritextsökningen kontaminerades av kamel/sila/svälja var för "
    "sig). old_facit bekräftar exakt betydelsen: '(ursp. bibl.) haka upp sig på "
    "småsaker o missa större...'. Kortets definition ('Ägna sig åt petiga detaljer och "
    "missa det som verkligen är viktigt') matchar. Idiom får ingen ≈≈-kategori (hela "
    "uttrycket bär betydelsen), men de tre synonymfraserna är paraforsomskrivningar av "
    "definitionen, inte påstådda ordboksbelägg — godtagbart för ett idiom utan egen "
    "artikel. Oförändrat.",
"attribuera": "SO: 'ange såsom troligen skapad av <<viss upphovsman; med avseende på "
    "skrift, konstverk och dylikt>>' — matchar kortets definition. SAOL: 'hänföra ngt "
    "anonymt till ngn som upphovsman' — 'hänföra' inleder ledet, kortets enda synonym "
    "är alltså belagd. Exempelmeningen (målning attribuerad till Rembrandt) matchar "
    "definitionstillägget (konstverk). Oförändrat.",
"longör": "SO: 'utdraget, föga underhållande avsnitt <<av skildring, föreställning "
    "eller dylikt>>' — matchar kortets 'Tråkigt, utdraget avsnitt i en bok eller "
    "film'. SAOL: 'långrandigt avsnitt t.ex. i bok el. skådespel' — 'långrandighet' är "
    "nominaliseringen av SAOL:s eget adjektiv 'långrandigt', belagd. Exempelmeningen "
    "matchar. Oförändrat.",
"osökt": "SO ger adverb ('fullkomligt naturligt <<utan att man behöver göra någon "
    "ansträngning>>') och adjektiv ('fullkomligt naturlig') — samma innehåll, bara "
    "olika ordklass, inte två skilda betydelser. Kortets definition ('Helt naturligt, "
    "utan ansträngning') fångar definitionstillägget fullt ut. SAOL: 'som faller sig "
    "naturlig' — 'naturligt' belagt av båda källorna. Exempelmeningen matchar. "
    "Oförändrat.",
"tjudra": "SO: 'binda med tjuder', med utvidgningen 'binda fast' (samma synonym som "
    "kortet redan har, direkt ur SO:s egen text) och en bildlig utvidgning ('skolan "
    "får inte tjudra elevernas fantasi') utan egen definition. Kortets 'Binda fast ett "
    "djur med rep eller kedja' är en rimlig konkretisering av tjuder (en tjuderlina "
    "ÄR ett rep/en kedja) och matchar exemplet (hästar). Oförändrat.",
"blidväder": "SO: 'väderlek under vintern som kännetecknas av temperatur (strax) över "
    "fryspunkten' — matchar kortets 'Mild vinterväderlek strax över nollan' nästan "
    "ordagrant. SAOL detsamma. old_facit ('tö') bekräftar synonymerna "
    "mildväder/töväder. Exempelmeningen matchar. Oförändrat.",
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n_fix = n_unchanged = n_pause = 0
for e in poster:
    ord_ = e["ord"]

    if ord_ == "enligt/efter konstens alla regler":
        # Traffar for bade "enligt/efter konstens alla regler" (med slash) OCH
        # for den fria formen "efter konstens alla regler" ar noll pa BADE
        # SO, SAOL och SAOB -- kontrollerat direkt i uppslagsfilerna
        # (svenska_se_ratt.{so,saol,saob} tomma), plus Wiktionary "finns: false"
        # och synonymer.se HTTP 404. De "traffar" slaupp.py rapporterade for
        # friformen ar kontaminering (efter/konst/regel som egna artiklar,
        # inte frasen sjalv) -- samma monster som "karringen mot strommen"/
        # "trojansk hast" i tidigare batchar. Ingen kalla finns att stodja
        # kortet mot. Rors INTE, rapporteras for paus.
        e["pausad"] = "inget_uppslagsord_i_so_saol"
        n_pause += 1
        continue

    f = FIX.get(ord_)
    if f:
        e["proposed"] = {
            "huvudbetydelse": f["hb"],
            "register": f["reg"],
            "synonymer": [s for g in f["grp"] for s in g],
            "synonym_groups": f["grp"],
            "exempelmening": f["ex"],
            "etymologi": f.get("etym", e["legacy"].get("etymologi")),
        }
        if e["legacy"].get("bild_html"):
            e["proposed"]["bild_html"] = e["legacy"]["bild_html"]
        e["sokkoll"] = {"kalla": U(ord_), "slutsats": f["sl"]}
        e["approved"] = True
        n_fix += 1
        continue

    sl = UNCHANGED_SL.get(ord_)
    if sl:
        leg = e["legacy"]
        e["proposed"] = {
            "huvudbetydelse": leg["huvudbetydelse"],
            "register": leg["register"],
            "synonymer": leg["synonymer"],
            "synonym_groups": leg.get("synonym_groups"),
            "exempelmening": leg["exempelmening"],
            "etymologi": leg.get("etymologi"),
        }
        if leg.get("bild_html"):
            e["proposed"]["bild_html"] = leg["bild_html"]
        e["sokkoll"] = {"kalla": U(ord_), "slutsats": sl}
        e["approved"] = True
        n_unchanged += 1
        continue

    print("VARNING: inget beslut for", ord_)

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"Andrade: {n_fix}   Oforandrade (verifierade): {n_unchanged}   Pausade: {n_pause}")
