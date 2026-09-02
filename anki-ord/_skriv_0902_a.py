# -*- coding: utf-8 -*-
"""Skriver kort 0-17 i batchen 2026-09-02.

Kallorna byggs ur uppslag/<ord>.json sa URL:erna inte kan bli feltypade.
"""
import io, json, os, sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02_v3-batch.json"
H = '<font color="#3498db">%s</font>'


def kallor(o):
    d = json.load(io.open(os.path.join("uppslag", o + ".json"), encoding="utf-8"))
    u = d.get("urler") or {}
    return " ".join(u[k] for k in ("svenska.se", "synonymer.se", "wiktionary") if u.get(k))


K = {}

K["absolvera"] = (
 "Fullborda eller avsluta, särskilt en utbildning eller en examen ; ge syndaförlåtelse",
 "mindre brukligt, formell",
 ["fullborda", "avsluta", "ge syndaförlåtelse"],
 [["fullborda", "avsluta"], ["ge syndaförlåtelse"]],
 "Han " + H % "absolverade" + " sin utbildning på tre år i stället för de normala fem.",
 "latinets absolvere 'lösa upp, frigöra', av ab- 'bort' och solvere 'lösa' — samma rot som i absolut",
 "SO ger 'fullborda' om nagon handling, markerat mindre brukligt, med underbetydelsen "
 "'gora fri fran skuld'. SAOL har tva led atskilda av semikolon: 'avsluta, fullborda; "
 "avlagga examen' samt en egen huvudbetydelse 'ge syndaforlatelse'. Tva betydelser alltsa, "
 "inte tre: examensledet ar en tillampning av fullborda, inte nagot eget. "
 "'avlagga' tas INTE med som ensam synonym eftersom SAOL:s led ar 'avlagga examen' - "
 "ordet ensamt betyder inte absolvera.")

K["sanslös"] = (
 "Som har förlorat medvetandet ; som har förlorat all behärskning ; fullkomligt meningslös",
 "neutral i betydelse 1, vardaglig i 2 och 3",
 ["medvetslös", "avsvimmad", "besinningslös", "hejdlös", "meningslös", "vanvettig"],
 [["medvetslös", "avsvimmad"], ["besinningslös", "hejdlös"], ["meningslös", "vanvettig"]],
 "Han låg " + H % "sanslös" + " på golvet i två minuter innan han vaknade.",
 None,
 "SO ger tre huvudbetydelser: 'som har forlorat medvetandet', 'som har forlorat formagan "
 "till beharskning' (vardagligt, vanligen adverbiellt) och 'som saknar mening' (vardagligt). "
 "Alla tre tas med eftersom de ar SO:s egna huvudbetydelser, inte underbetydelser. "
 "synonymer.se stoder uppdelningen: medvetslos/avsvimmad, ohammad/besinningslos/hejdlos och "
 "meningslos/vanvettig ligger i tre tydliga knippen.")

K["bylsig"] = (
 "Om klädesplagg: oformlig och illasittande, så att tyget putar ut i veck och knölar",
 "neutral, något vardaglig",
 ["oformlig", "illasittande", "pösig", "säckig"],
 None,
 "Den " + H % "bylsiga" + " vinterjackan fick honom att se dubbelt så bred ut.",
 None,
 "SO: 'som putar ut i veck eller knolar' med tillagget 'p.g.a. (alltfor) stort omfang'. "
 "SAOL preciserar tillampningen: 'om kladesplagg: oformlig och illasittande'. Tillagget ar "
 "obligatorisk kontext, inte en parentes - ordet anvands om plagg, inte om vad som helst "
 "som putar. En betydelse. Endast SAOL och SO har artikel.")

K["coupe"] = (
 "Efterrätt av glass och frukt, serverad i portionsglas eller i skål på fot",
 "neutral",
 ["fruktefterrätt", "glassefterrätt"],
 None,
 "Till efterrätt blev det en " + H % "coupe" + " med vaniljglass, hallon och grädde.",
 "franskans coupe 'bägare, skål', till couper 'skära'",
 "SO: 'efterratt serverad i portionsglas' med tillagget 'vanligen med glass och frukt som "
 "ingredienser'. SAOL: 'glassefterratt serverad i skal pa fot'. Kallorna skiljer sig pa "
 "karlet (glas mot skal pa fot), sa bada tas med i huvudbetydelsen i stallet for att valja "
 "en och tysta den andra. synonymer.se ger ocksa 'cocktail', vilket INTE tas med - det ar "
 "en annan sak pa svenska och skulle bli missvisande.")

K["digna"] = (
 "Långsamt sjunka ihop under en alltför tung börda ; om bord: bågna av allt som står på det",
 "neutral, något högtidlig",
 ["sjunka samman", "svikta", "segna ned", "bågna"],
 [["sjunka samman", "svikta", "segna ned"], ["bågna"]],
 "Bordet " + H % "dignade" + " under skinkor, sillar och sju sorters kakor.",
 None,
 "SO ger en huvudbetydelse: 'langsamt sjunka ihop' med tillagget 'p.g.a. for stor "
 "pafrestning'. SAOL delar med semikolon i tre led: 'sjunka samman; svikta under en borda; "
 "av. med tonvikt pa overflod'. Det tredje ledet ar overflodsbetydelsen (bordet som dignar), "
 "tillrackligt sarskild for en egen grupp - dar ar ingenting nara att ge vika, tvartom ar "
 "det ett positivt overflod.")

K["endokrin"] = (
 "Som gäller de körtlar vars hormoner går direkt ut i blodet i stället för genom en utförsgång",
 "fackspråklig, medicin",
 ["inresekretorisk", "insöndrande"],
 None,
 "Sköldkörteln är en " + H % "endokrin" + " körtel och skickar sina hormoner rakt ut i blodet.",
 "grekiskans endon 'inuti' och krinein 'avskilja'",
 "SO ger definitionen 'inresekretorisk' och SAOL 'insondrande, inresekretorisk'. RODFLAGGA: "
 "bada definitionerna ar SVARARE an uppslagsordet, vilket bryter mot regeln att forklaringen "
 "ska ligga under ordet - 'inresekretorisk' hjalper ingen som inte redan vet. "
 "Huvudbetydelsen ar darfor omskriven till vad inresekretorisk faktiskt betyder: utsondring "
 "rakt ut i blodet i stallet for genom en gang. Bada ordbokstermerna star kvar som "
 "synonymer. Endast SAOL och SO; ingen SAOB-artikel.")

K["essens"] = (
 "Det innersta och mest väsentliga i något ; koncentrerad lösning av doft- eller smakämnen",
 "neutral",
 ["innersta väsen", "kärnpunkt", "andemening", "extrakt", "koncentrat"],
 [["innersta väsen", "kärnpunkt", "andemening"], ["extrakt", "koncentrat"]],
 "Hela hans invändning kan kokas ned till en mening — det är " + H % "essensen" + " av kritiken.",
 "latinets essentia 'väsen', bildat till esse 'vara'",
 "SO ger tva huvudbetydelser: 'det som utgor karnpunkten' i nagot abstrakt, och "
 "'koncentrerad losning av doft- eller smakamnen'. SAOL bekraftar den andra. VIKTIGT: "
 "sokningen returnerade aven SAOL-rader om 'tonen e sankt med ett halvt tonsteg' och 'det "
 "hogsta kortet i en farg' - de tillhor lemmat ESS, inte essens, och ar uteslutna. "
 "Fuzzy-traffar som ser ut att vara extra betydelser ar den vanligaste vagen till ett fel kort.")

K["expenser"] = (
 "Mindre utgifter och utlägg, särskilt sådana som hör till ett bestämt uppdrag",
 "formell, något ålderdomlig; används i plural",
 ["småutgifter", "utlägg", "omkostnader"],
 None,
 "Han fick ersättning för resan men fick själv stå för sina " + H % "expenser" + ".",
 "latinets expensa 'utgift', till expendere 'väga upp, betala ut'",
 "SO: '(smarre) omkostnader' med tillagget 'sarsk. i samband med visst uppdrag'. SAOL: "
 "'sma utgifter, utlagg'. Bada kallorna bar SMA-heten som en del av betydelsen, inte som "
 "en bisak - ordet betyder inte utgifter i allmanhet. synonymer.se markerar '(pl.)', och "
 "ordet anvands i praktiken bara i plural, vilket star i registret. Endast SAOL och SO.")

K["fiskal"] = (
 "Som rör statens skatter och inkomster ; jurist under domarutbildning, äldre även åklagare",
 "formell, fackspråklig",
 ["fiskalisk", "åklagare", "tjänsteman i hovrätt"],
 [["fiskalisk"], ["åklagare", "tjänsteman i hovrätt"]],
 "Regeringen motiverade höjningen med rent " + H % "fiskala" + " skäl — den behövde pengarna.",
 "latinets fiscus 'korg, statskassa'",
 "Tva SKILDA lemman i SO, inte en betydelse med nyanser: adjektivet 'som har att gora med "
 "statens ekonomiska intressen' och substantivet '(titel for) person med uppgift att beivra "
 "lagovertradelser'. SAOL ger substantivets nutida innebord: 'jurist som genomgar "
 "domarutbildning'. Bada tas med, och substantivets forskjutning fran atalande till "
 "utbildningstitel skrivs ut - den ar sjalva poangen med ordet idag.")

K["habil"] = (
 "Duglig och kompetent, men utan självständighet eller något nyskapande",
 "neutral, ibland något nedsättande",
 ["duglig", "kompetent", "skicklig"],
 None,
 "Framförandet var " + H % "habilt" + " men inte på något sätt överraskande.",
 "franskans habile 'skicklig', av latinets habilis 'lätthanterlig, duglig'",
 "SO:s definition ar 'duglig men foga sjalvstandig eller nyskapande', markerad 'ibland "
 "nagot nedsattande'. INSKRANKNINGEN ar hela ordet: habil ar berom med en broms i. SAOL:s "
 "'duglig, kompetent; skicklig' saknar den nyansen och skulle ensamt ge ett falskt kort - "
 "ett habilt arbete ar inte ett skickligt arbete, det ar ett arbete som duger. "
 "synonymer.se listar bade 'skicklig' och motsatsen 'oduglig', vilket bekraftar att ordet "
 "ligger mitt emellan och att enbart positiva synonymer vore vilseledande.")

K["hypotetisk"] = (
 "Som bygger enbart på ett antagande och inte på något känt faktum",
 "neutral",
 ["antagen", "förmodad", "tänkt", "teoretisk"],
 None,
 "Frågan är rent " + H % "hypotetisk" + " — ingen har föreslagit att det faktiskt ska göras.",
 "grekiskans hypothesis 'antagande, grundval', av hypo- 'under' och tithenai 'sätta'",
 "SO: 'som grundar sig enbart pa antaganden', med underbetydelsen 'som galler eller ar av "
 "vikt bara om vissa forutsattningar uppfylls'. Underbetydelsen ar en anvandning av samma "
 "begrepp (det villkorliga), inte en andra betydelse, sa den vags in i huvudbetydelsen i "
 "stallet for att fa en egen grupp. synonymer.se ger motsatserna 'faktisk, bevisad', "
 "vilket bekraftar att ordets karna ar franvaron av belagg.")

K["kont"] = (
 "Enkel ryggsäck eller ryggkorg, vanligen flätad av näver",
 "mest historisk",
 ["ryggsäck", "ryggkorg", "ränsel", "mes"],
 None,
 "Han bar sin " + H % "kont" + " av näver på ryggen hela vägen upp till fäboden.",
 None,
 "SO: 'enkel ryggsack' med tillagget 'vanligen av flatad naver', markerat 'mest "
 "historiskt'. SAOL: 'korg el. vaska av naver att bara pa ryggen'. Bada kallorna bar "
 "NAVERN som en del av definitionen, inte som en illustration, sa den star kvar i "
 "huvudbetydelsen. SAOL ger bade korg och vaska; darfor 'ryggsack eller ryggkorg' i "
 "stallet for att valja en av dem.")

K["lisma"] = (
 "Uppträda inställsamt på ett alltför genomskinligt sätt",
 "neutral, något ålderdomlig",
 ["fjäska", "ställa sig in", "smickra", "smila"],
 None,
 "Han " + H % "lismade" + " för chefen på ett sätt som fick hela rummet att titta bort.",
 None,
 "SO: 'upptrada installsamt' med tillagget 'pa ett alltfor tydligt satt'. Tillagget ar "
 "obligatoriskt: lisma ar inte neutral installsamhet utan installsamhet som SYNS, och "
 "darfor misslyckas. SAOL: 'stalla sig in, fjaska'. Bada leden tas som synonymer eftersom "
 "SAOL:s komma skiljer likvardiga alternativ, inte betydelser.")

K["periferisk"] = (
 "Som ligger i utkanten och därför är av underordnad betydelse",
 "ålderdomlig; den nutida formen är perifer",
 ["perifer", "marginell", "oväsentlig"],
 None,
 "Invändningen är " + H % "periferisk" + " och rör inte huvudfrågan.",
 "grekiskans periphereia 'omkrets', av peri- 'runt' och pherein 'bära'",
 "TVA AV TRE KALLOR: ordet finns i SAOL och SAOB men har INGEN SO-artikel. "
 "SAOL ger en enda rad: 'perifer'. Betydelsen ar alltsa hamtad ur SAOL:s hanvisning plus "
 "synonymer.se ('perifer, yttre, i utkanten, ovasentlig, marginell, sekundar'), inte ur en "
 "egen definition. Att SO saknar ordet medan SAOL bara hanvisar vidare ar sjalv "
 "informationen: periferisk ar den aldre formen av perifer, och det star i registret.")

K["sakral"] = (
 "Som hör till gudstjänsten och därför omges av vördnad och högtidlighet",
 "formell",
 ["kyrklig", "religiös", "helig", "högtidlig"],
 None,
 "Rummet hade en " + H % "sakral" + " tystnad som ingen ville vara först med att bryta.",
 "latinets sacer 'helig, invigd'",
 "SO: 'forknippad med gudstjanstliv' med tillagget 'och darfor vordad, hogtidlig etc.'. "
 "SAOL: 'religios; hogtidlig' - tva led atskilda av semikolon. Hogtidligheten ar alltsa "
 "inte en bibetydelse utan bars av bada kallorna, och tas darfor in i huvudbetydelsen. "
 "synonymer.se ger motsatserna 'profan, ohelig', vilket bekraftar axeln ordet ligger pa.")

K["saltomortal"] = (
 "Hopp med en hel volt i luften",
 "neutral",
 ["frivolt", "salto", "luftsprång", "volt"],
 None,
 "Hon avslutade friståendet med en " + H % "saltomortal" + " och landade utan ett steg.",
 "italienskans salto mortale 'dödssprång', av salto 'hopp' och mortale 'dödlig'",
 "SO: 'hopp med helomvandning i luften' med tillagget 'sarsk. i cirkus-, gymnastik- och "
 "simhoppssammanhang'. SAOL: 'halsbrytande luftsprang; frivolt'. Sammanhangstillagget ar "
 "en anvandningsuppgift, inte en inskrankning av betydelsen, och foljer darfor inte med i "
 "huvudbetydelsen. Etymologin ar vard att ha kvar: 'dodssprang' forklarar SAOL:s "
 "'halsbrytande'.")

K["serum"] = (
 "Den gulaktiga vätska som blir kvar när blodet stelnat ; läkemedel mot förgiftning "
 "framställt ur sådan vätska ; flytande hudvårdsprodukt som läggs på före krämen",
 "neutral; betydelse 1 och 2 fackspråkliga",
 ["blodvatten", "blodserum", "motgift", "antidot", "hudvårdsprodukt"],
 [["blodvatten", "blodserum"], ["motgift", "antidot"], ["hudvårdsprodukt"]],
 "Läkaren gav honom " + H % "serum" + " mot ormgiftet inom en timme efter bettet.",
 "latinets serum 'vassla, vattnig vätska'",
 "TRE betydelser, alla belagda. SO ger tva huvudbetydelser: 'aggvitehaltig kroppsvatska som "
 "befriats fran fasta partiklar' och 'flytande hudvardsprodukt som appliceras efter "
 "rengoring' med tillagget 'men fore dag- eller nattkram'. SAOL delar i tre: 'en gulaktig "
 "vatska med antikroppar i blodet', 'ett lakemedel framstallt ur blod mot forgiftning' och "
 "'en hudvardsprodukt'. Lakemedelsbetydelsen finns alltsa bara i SAOL men ar en egen "
 "huvudbetydelse dar, sa den tas med. Tredje gruppen bar bara hypernymen 'hudvardsprodukt' "
 "eftersom svenskan saknar en akta synonym - det ar SAOL:s egen formulering ordagrant.")

K["spisa"] = (
 "Äta ; lyssna på musik ; avvisa eller inte gå med på något",
 "ålderdomlig eller skämtsam i betydelse 1, vardaglig i 2",
 ["förtära", "inmundiga", "lyssna på", "avnjuta", "avvisa", "avfärda"],
 [["förtära", "inmundiga"], ["lyssna på", "avnjuta"], ["avvisa", "avfärda"]],
 "Vi satt och " + H % "spisade" + " jazz till långt in på natten.",
 None,
 "TRE betydelser. SO ger 'ata' (alderdomligt el. skamtsamt) med underbetydelsen 'lyssna pa' "
 "musik (vardagligt, nagot alderdomligt). SAOL delar i tre huvudbetydelser: 'ata' (ald.), "
 "'lyssna pa (jazz)musik' (vard.) och 'avvisa, avfarda'. Den tredje finns INTE i SO men "
 "ar en egen huvudbetydelse i SAOL och tas darfor med - 'det spisar jag inte' ar ett "
 "levande uttryck som annars vore obegripligt fran kortet. 'ata' anvands inte som synonym "
 "till sig sjalv; i stallet star SO-nara alternativ ur synonymer.se.")


poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    d = K.get(e["ord"])
    if not d:
        continue
    hb, reg, syn, grp, ex, etym, slut = d
    e["proposed"] = {"huvudbetydelse": hb, "register": reg, "synonymer": syn,
                     "synonym_groups": grp, "exempelmening": ex, "etymologi": etym}
    e["sokkoll"] = {"kalla": kallor(e["ord"]), "slutsats": slut}
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("skrev %d kort" % n)
saknas = [o for o in K if not any(e["ord"] == o for e in poster)]
print("ord i K som inte fanns i filen:", saknas or "inga")
