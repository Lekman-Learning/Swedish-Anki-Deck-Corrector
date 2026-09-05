# -*- coding: utf-8 -*-
"""Spar B omgranskning, repetition4 (25 kort). Sokkoll via slaupp.py --tyst
(kort direkt + grundorden last/stapel/rulle/rulla for idiomen)."""
import io, json, urllib.parse

FIL = "sessions/session_2026-09-05_v3-omgranskning-repetition4.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)
W = lambda o: "https://sv.wiktionary.org/wiki/%s" % urllib.parse.quote(o)

FIX = {

"ansätta": dict(
  hb="Plåga eller pressa någon hårt ; (fackspråk) montera fast något, eller börja spela en ton",
  reg="litterär, negativ ; fackspråklig, neutral",
  grp=[["bestorma"], ["börja"]],
  sl="SO ger TVÅ huvudbetydelser: '(hårt) pröva motståndsförmågan hos <någon>' (belagt SAOL "
     "'bestorma') och 'placera <något där det passar och kan fästas>' [i fackspråk] med "
     "underbetydelsen 'börja' [musik, språkvetenskap] -- SAOL bekräftar med semikolon: "
     "'bestorma; börja'. Legacy hade bara den första betydelsen (plåga/besvära/tränga in på, "
     "riskflaggan 'dold_betydelse' hade rätt). 'bestorma' och 'börja' inleder sina SAOL-led, "
     "alltså belagda; 'besvära' och 'tränga in på' saknade belägg och är strukna.",
  till={"betydelse_kan_saknas": "SO:s underbetydelse 'börja' (musik/språkvetenskap) är en "
        "nyans av samma fackspråksbetydelse som redan täcks av kortets andra del "
        "('montera fast något, eller börja spela en ton') -- skrivna ihop i stället för som "
        "en tredje ' ; '-del, för att hålla kortet kort."}),

"bli vid sin läst": dict(
  hb="Hålla sig till sitt eget kompetensområde och inte lägga sig i annat",
  reg="litterär, neutral",
  grp=[["≈≈ hålla sig till sitt"]],
  etym="Från ordspråket 'skomakare, bliv vid din läst' -- läst är skomakarens formmall för skor.",
  sl="SO:s idiom 'skomakare, bliv vid din läst' ger 'håll dig till den (livs)uppgift du har "
     "fått', vilket matchar kortets huvudbetydelse och old_facit exakt. Ingen dold betydelse. "
     "De tre gamla synonymerna var bara omskrivningar av definitionen utan egen ordbokskälla "
     "-- ersatta med en enda ≈≈-kategori (tillåten utan källa för idiom, style_guide 2026-08-29). "
     "Etymologi tillagd: bron mellan bokstavlig läst (skoform) och den bildliga betydelsen."),

"briljera": dict(
  hb="Visa upp enastående skicklighet och göra starkt intryck",
  reg="formell, positiv",
  grp=[["glänsa", "excellera", "utmärka sig"]],
  sl="SO: 'utmärka sig genom att tydligt visa sin skicklighet' -- en betydelse, matchar kortet. "
     "SAOL: 'glänsa, pråla' (komma = samma betydelse, inte skilda). Alla tre synonymer "
     "('glänsa','excellera','utmärka sig') står i synonymer.se:s redaktionella lista, och "
     "'utmärka sig' inleder dessutom SO:s egen definition. Kortet stämmer, oförändrat."),

"fajans": dict(
  hb="Tennglaserat lergods, eller ett föremål gjort av det",
  reg="neutral, neutral",
  grp=[["glaserat lergods", "majolika"]],
  etym="Efter den italienska staden Faenza, där lergodset ursprungligen tillverkades.",
  sl="SO: 'typ av (tenn)glaserat lergods' med definitionstillägg 'el. föremål av lergods' -- "
     "kortet saknade den tillagda betydelsen (fajans = både materialet OCH föremål gjorda av "
     "det). 'dekorerat' i legacy stod inte i någon källa, struket. Register ändrat "
     "formell->neutral: SO ger ingen brukl.-markering, och ett sällsynt men annars vanligt "
     "substantiv (jfr taverna/divan) ska vara neutralt, inte formellt. Synonymer 'glaserat "
     "lergods' (=SO:s egen definitionstext) och 'majolika' båda redaktionella på "
     "synonymer.se; bar 'lergods' struket som för bred hyperonym (all keramik, inte bara "
     "tennglaserad). Etymologi: platsnamnet Faenza gör ordet självförklarande."),

"gå av stapeln": dict(
  hb="Äga rum eller starta, om ett större evenemang",
  reg="neutral, neutral",
  grp=[["äga rum", "starta"]],
  etym="Från skeppsbyggeri, där ett nybygge gled av stapeln vid sjösättningen.",
  sl="SO:s idiom ger EN betydelse: 'äga rum' <om större evenemang>, matchar kortet. "
     "'arrangeras' i legacy saknade belägg (varken SO eller synonymer.se); bytt mot 'starta', "
     "som står i synonymer.se:s redaktionella lista. Register ändrat formell->neutral (ingen "
     "SO-markering, uttrycket är lika naturligt i tal som skrift). Den bokstavliga "
     "sjösättningsbetydelsen är inte längre en levande användning -- flyttad från parentes i "
     "huvudbetydelsen till etymologin, som style_guide.md föreskriver för idiom av den typen "
     "(jfr 'le i mjugg')."),

"leva rullan": dict(
  hb="Festa och leva vilt ; bråka och föra oväsen",
  reg="vardaglig, skämtsam ; vardaglig, negativ",
  grp=[["festa", "rumla", "svira"], ["≈≈ bråka"]],
  sl="SO:s idiomartikel för 'rullan' ger TVÅ idiombetydelser för 'leva rullan': "
     "'föra ett utsvävande liv' (vardagligt, ex. 'de åkte till Ibiza och levde rullan') OCH "
     "'väsnas och bråka' (vardagligt, ex. 'de två männen levde rullan på bussen ... polisen "
     "omhändertog dem'). Legacy hade bara den första betydelsen, dessutom mjukad till "
     "'festa och ha det roligt, ofta med dans' -- 'dans' var inte belagt någonstans, struket. "
     "Synonymer 'festa','rumla','svira' matchar old_facit och synonymer.se:s redaktionella "
     "lista exakt. Andra betydelsen saknar sourced synonym helt (synonymer.se ger bara "
     "festbetydelsen) -- fick en ≈≈-kategori ur kortets egen definition."),

"ruelse": dict(
  hb="Djup ånger och samvetskval över något man gjort fel",
  reg="ngt ålderdomlig, negativ",
  grp=[["djup ånger", "samvetskval", "självanklagelse"]],
  sl="SO: 'ånger och samvetskval' [brukl: något ålderdomligt]. SAOL: 'djup ånger' [åld.]. "
     "Kortets betydelse stämmer. Register ändrat litterär->ngt ålderdomlig för att matcha "
     "SO/SAOL:s uttryckliga bruklighetsmärkning (litterär är fel axel-värde -- ordet är "
     "daterat, inte bara bokspråkligt). Alla tre synonymer bekräftade i synonymer.se:s "
     "redaktionella lista ('självanklagelser' pluralform av 'självanklagelse')."),

"ryd": dict(
  hb="Uppodlad mark eller glänta skapad genom skogsröjning",
  reg="dialektal, neutral",
  grp=[["≈≈ röjd mark"]],
  sl="SO och SAOL har INGEN egen artikel för 'ryd' (bara SAOB-metadata utan definitionstext, "
     "0 träffar). Wiktionary bekräftar dock betydelsen 'röjd mark', vilket matchar kortets "
     "innehåll och old_facit ('röjning i skogen') exakt -- kortet stämmer sakligt. Eftersom "
     "ingen ordbok ger ett enskilt synonymord (synonymer.se saknar helt uppslag) nedgraderades "
     "de tre osourced synonymerna ('röjning','hygge','skogsglänta') till en enda "
     "≈≈-kategori hämtad ur kortets egen, källbekräftade definition.",
  till={"uppslagsord_saknas": "SO/SAOL saknar egen artikel (0 träffar, bara SAOB-metadata "
        "utan definitionstext). Wiktionary ger dock 'röjd mark', som matchar kortets "
        "innehåll -- se sokkoll."}),

"skyla": dict(
  hb="Dölja eller täcka över något ; (jordbruk) stapla skördad säd i skylar för att torka",
  reg="litterär, neutral ; fackspråklig, neutral, jordbruk",
  grp=[["dölja", "hölja"], ["≈≈ sätta i skylar"]],
  sl="SO ger TVÅ HELT SKILDA HOMOGRAFER: skyla(1) 'dölja' <vanligen med hjälp av något "
     "täckande> och skyla(2) 'anordna i skylar' (stapla säd i kärvestackar). SAOL bekräftar "
     "med två separata rader: 'hölja; dölja' respektive 'sätta i skyl'. Legacy hade bara "
     "homograf 1 -- den andra, jordbruksbetydelsen, saknades helt. 'förkläda' i legacy-"
     "synonymerna saknade belägg (varken SO eller SAOL), bytt mot 'hölja' som SAOL faktiskt "
     "ger. Andra betydelsen saknar ett fristående synonymord i källorna (SAOL:s gloss ÄR "
     "hela definitionen) -- fick en ≈≈-kategori.",
  till={"betydelse_kan_saknas": "Räknat rätt är det två SKILDA homografer (verb 'dölja' och "
        "verb 'anordna i skylar') -- båda nu med i kortets ' ; '-uppdelning, matchar SO:s "
        "råstruktur."}),

"slentrian": dict(
  hb="Gammal vana man följer utan att tänka efter eller ifrågasätta",
  reg="vardaglig, lätt negativ",
  grp=[["gammal vana", "vanemässighet", "vanetänkande"]],
  sl="SO: 'mekanisk vanemässighet <som (enligt talaren) bör ifrågasättas>' -- en betydelse. "
     "'Slentrian' är ett SUBSTANTIV, men legacys huvudbetydelse var skriven som en VERBFRAS "
     "('Göra något av ren vana...') -- omskriven till substantivform ('Gammal vana...'), "
     "samma buggtyp som 'ocker' i en tidigare granskning. 'rutinmässighet' i legacy saknade "
     "belägg; bytt mot 'vanemässighet', som är SO:s eget ord. 'gammal vana' och "
     "'vanetänkande' bekräftade i synonymer.se:s redaktionella lista."),

"slik": dict(
  hb="Sådan, av det slaget",
  reg="ngt ålderdomlig, neutral",
  grp=[["sådan", "dylik", "liknande"]],
  sl="SO: 'sådan' [brukl: ålderdomligt]. SAOL: 'sådan' [åld.]. Kortets betydelse stämmer. "
     "Register ändrat litterär->ngt ålderdomlig för att matcha källornas uttryckliga "
     "bruklighetsmärkning. Alla tre synonymer bekräftade i synonymer.se:s redaktionella "
     "lista."),

"tankesmedja": dict(
  hb="Grupp eller organisation som utvecklar idéer och påverkar politiska beslut",
  reg="neutral, neutral",
  grp=[["idéfabrik", "expertgrupp", "hjärntrust"]],
  sl="SO: 'särskild grupp som gör djupgående analyser <och t.ex. utformar ideologi el. "
     "handlingsprogram>' -- en betydelse, matchar kortet (riskflaggan 'dold_betydelse' var "
     "falsklarm, bara en betydelse finns). Ingen av legacys synonymer ('opinionsbildare', "
     "'idégrupp','forum') stod i någon källa -- 'forum' är dessutom fel begrepp (en "
     "diskussionsplats, inte en analysproducerande organisation). Ersatta med "
     "'idéfabrik','expertgrupp','hjärntrust', alla i synonymer.se:s redaktionella lista. "
     "Register ändrat formell->neutral, ingen SO-markering finns."),

"tinga": dict(
  hb="Förhandsbeställa eller boka något",
  reg="formell, neutral",
  grp=[["beställa", "förhandsbeställa", "reservera"]],
  sl="SO: 'i förväg försäkra sig om <någon vara, tjänst eller dylikt>'. SAOL: 'beställa i "
     "förväg'. Kortets betydelse stämmer. Men 'tinga' är ett VERB och legacys synonymlista "
     "hade 'förhandsbokning' (substantiv) och 'reserv' (substantiv) -- fel ordklass. Bytt mot "
     "verbformerna 'förhandsbeställa' och 'reservera', båda i synonymer.se:s redaktionella "
     "lista tillsammans med 'beställa'."),

"varda": dict(
  hb="Bli eller uppstå (ålderdomligt)",
  reg="arkaisk, neutral",
  grp=[["bli"]],
  sl="SO och SAOL ger båda bara 'bli' -- inget annat ord är belagt. Kortets betydelse och "
     "register (arkaisk stämmer med SAOL:s [åld., prov.], helt ur bruk i dagligt tal) är "
     "korrekta, oförändrade. 'uppstå' och 'förvandlas till' i legacy-synonymerna saknade "
     "belägg (varken SO, SAOL eller synonymer.se ger något annat ord än 'bli') och drar "
     "betydelsen snävare/vidare än originalet -- strukna, bara det exakta 'bli' kvar."),

"beträngd": dict(
  hb="I svårigheter, pressad",
  reg="litterär, negativ",
  grp=[["nödställd", "i knipa", "i trångmål"]],
  sl="SO: 'som är i svårigheter' med underbetydelsen 'som kännetecknas av trångmål' -- samma "
     "kärnbetydelse, ingen dold andra betydelse. Matchar old_facit 'i knipa'. 'pressad' i "
     "legacy-synonymerna saknade belägg; bytt mot 'i knipa' och 'i trångmål' (SO:s egen "
     "underbetydelse), båda i synonymer.se:s redaktionella lista tillsammans med 'nödställd' "
     "(=SAOL:s exakta gloss)."),

"handgrepp": dict(
  hb="Särskilt sätt eller trick för att göra något med händerna",
  reg="vardaglig, neutral",
  grp=[["grepp", "metod", "tillvägagångssätt"]],
  sl="SO: 'särskilt sätt att gripa och behandla (något) med handen' + utvidgningen "
     "'tillvägagångssätt' (SAOL: 'äv. metod' -- en användningsutvidgning, inte en skild "
     "betydelse). Kortet fångar redan båda nyanserna. 'knep' i legacy saknade belägg; bytt "
     "mot 'grepp','metod','tillvägagångssätt', alla i synonymer.se:s redaktionella lista."),

"prosa": dict(
  hb="Skriven eller talad text som inte följer versmått, till skillnad från poesi",
  reg="neutral, neutral, litteraturvetenskap",
  grp=[["obunden stil", "text i fri form"]],
  sl="SO: '(skrift)språklig framställningsform som inte är bunden av metriska regler', "
     "MOTSATS:antonym till 'vers'. SAOL breddar med 'skrift el. tal' -- kortets 'skriven "
     "eller talad' stämmer. Legacys synonymer 'berättande text' och 'skriven text' var för "
     "SNÄVA/fel: prosa definieras av FORMEN (inte bunden av versmått), inte av att texten är "
     "berättande -- en teknisk rapport är också prosa. Bytt mot 'obunden stil' och 'text i "
     "fri form', båda i synonymer.se:s redaktionella lista (OBS: samma lista listar "
     "'poesi'/'vers' som 'synonymer' -- det är SO:s uttryckliga ANTONYM, plockade inte med "
     "dem). Domän litteraturvetenskap tillagd: SO klassar ordet bland dramatik/epik/lyrik."),

"skålla": dict(
  hb="Koka snabbt i hett vatten ; bränna sig eller något med hett vatten ; en tunn metallplatta "
     "som skydd eller beslag, t.ex. på en sko",
  reg="vardaglig, neutral ; vardaglig, negativ ; neutral, neutral",
  grp=[["koka", "skölja i kokande vatten"], ["bränna"], ["beslag", "skoning"]],
  sl="SO ger TVÅ HELT SKILDA HOMOGRAFER: skålla (verb) 'skölja över med kokhet vätska så att "
     "skal, hår eller fjädrar lossnar' + underbetydelsen 'skada genom översköljning med "
     "kokhet vätska' (matchar legacys två verbbetydelser), OCH skålla (substantiv) 'tunn "
     "(metall)platta <vanligen anv. som beslag el. skoning>' -- en tredje betydelse, helt "
     "annan ordklass, som saknades i kortet. SAOL bekräftar strukturen. Synonymer per "
     "betydelse hämtade ur synonymer.se:s redaktionella lista ('koka','skölja i kokande "
     "vatten','bränna' för verbet, 'beslag','skoning' för substantivet)."),

"auktor": dict(
  hb="Upphovsman till ett verk ; den som först gav en organism dess vetenskapliga namn",
  reg="litterär, neutral ; fackspråklig, neutral, biologi",
  grp=[["upphovsman", "författare"], ["≈≈ namngivare"]],
  sl="SO: 'upphovsman <till litterärt el. annat konstnärligt verk>' + underbetydelsen "
     "'person som först publicerat det vetenskapliga namnet på en organism' -- kortet "
     "fångar redan båda betydelserna korrekt. old_facit '(lit.) upphovsman' bekräftar "
     "litterär register för första betydelsen -- ändrat från 'formell' till 'litterär' för "
     "att matcha. 'upphovsman' och 'författare' båda i SAOL:s definition ('författare; "
     "upphovsman'). Etymologin (latin auctor, till augere 'öka') var redan korrekt, "
     "oförändrad."),

"bigami": dict(
  hb="Att vara gift med två personer samtidigt",
  reg="fackspråklig, neutral, juridik",
  grp=[["tvegifte"]],
  sl="SO och SAOL ger identisk definition: 'det att samtidigt vara gift med TVÅ personer' -- "
     "legacys 'mer än en person' var för brett (det skulle inkludera polygami med tre eller "
     "fler, ett annat begrepp). Rättat till exakt 'två'. Domän juridik tillagd: bigami är "
     "specifikt ett brott, inte allmänt ordförråd. 'tvegifte' matchar både SO och SAOL "
     "exakt, oförändrad."),

"brumbjörn": dict(
  hb="Vresig, grinig person",
  reg="vardaglig, skämtsam",
  grp=[["tvärvigg", "bitvarg"]],
  sl="SO har ingen egen artikel (0 träffar), SAOL ger 'vresig man' [vard.]. Kortets "
     "kärnbetydelse och register stämmer. Domänfältet 'ämnesområden: psykol.' i SAOL:s "
     "råtext ignorerad medvetet -- style_guide.md/CLAUDE.md dokumenterar att SAOL:s "
     "ämnesområden-fält felaktigt märkt vardagliga känsloord som psykologi tidigare "
     "(betuttad m.fl.), så det räknas inte som domänbelägg. 'tvärvigg' och 'bitvarg' båda "
     "bekräftade i synonymer.se:s redaktionella lista och matchar old_facit."),

"föhn": dict(
  hb="Varm, torr vind på läsidan av en bergskedja, särskilt i Alperna",
  reg="neutral, neutral",
  grp=[["varm fallvind"]],
  sl="SO: 'varm torr vind som uppträder på läsidan av bergskedja <särsk. i Alperna>' -- "
     "definitionstillägget 'särskilt i Alperna' saknades i legacy, tillagt. Register ändrat "
     "formell->neutral (ingen SO-markering, ett naturfenomen-substantiv som andra ska vara "
     "neutrala). Synonymen 'fallvind' i legacy var för bred (kalla fallvindar finns också) "
     "-- bytt mot synonymer.se:s exakta redaktionella gloss 'varm fallvind'. 'fön' och "
     "'föhnvind' uteslutna som cirkulära (samma ord, bara stavnings-/sammansättningsvariant)."),

"herbarium": dict(
  hb="Vetenskaplig samling av torkade, pressade växter",
  reg="fackspråklig, neutral, biologi",
  grp=[["växtsamling", "pressade växter"]],
  sl="SO: 'samling av torkade och pressade växter'. SAOL: 'samling av pressade växter'. "
     "Kortet stämmer. Register ändrat formell->fackspråklig+biologi (ordet hör till "
     "botaniken, inget SO-belägg för 'formell'/byråkratiskt). 'växtsamling' matchar SO "
     "nästan ordagrant, 'pressade växter' tillagd, båda i synonymer.se:s redaktionella "
     "lista."),

"kokard": dict(
  hb="Rosett eller emblem som bärs på en huvudbonad",
  reg="neutral, neutral",
  grp=[["bandrosett", "märke"]],
  sl="SO: 'liten rund platta eller rosett <t.ex. på studentmössa>' -- kortets generalisering "
     "till 'huvudbonad' är rimlig (SO:s 'studentmössa' är bara ETT exempel, inte en "
     "avgränsning). Register ändrat formell->neutral (ingen SO-markering). 'bandrosett' "
     "matchar SAOL/old_facit exakt; 'märke' tillagd, båda i synonymer.se:s redaktionella "
     "lista ('emblem' fanns bara i Användarnas bidrag, alltså inte belagt som synonym -- "
     "ordet får ändå stå kvar i själva definitionen, precis som style_guide tillåter, men "
     "inte i synonymfältet)."),

"revalvera": dict(
  hb="Skriva upp värdet på en valuta (motsats: devalvera)",
  reg="fackspråklig, neutral, ekonomi",
  grp=[["skriva upp valutan", "uppvärdera"]],
  sl="SO och SAOL: 'skriva upp värdet av <valuta>' -- kortet stämmer exakt, motsatsparet "
     "devalvera/revalvera korrekt. Register ändrat formell->fackspråklig+ekonomi (specifik "
     "ekonomisk fackterm). 'höja valutakursen' i legacy bytt mot det mer precisa "
     "'uppvärdera' (synonymer.se, redaktionell); 'devalvera'/'depreciera' i samma lista är "
     "ANTONYMER (motsatt betydelse) och plockades uttryckligen INTE med."),

}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    f = FIX.get(e["ord"])
    if not f:
        continue
    legacy = e.get("legacy") or {}
    e["proposed"] = {
        "huvudbetydelse": f["hb"],
        "register": f["reg"],
        "synonymer": [s for g in f["grp"] for s in g],
        "synonym_groups": f["grp"],
        "exempelmening": legacy.get("exempelmening", ""),
    }
    if f.get("etym"):
        e["proposed"]["etymologi"] = f["etym"]
    if legacy.get("bild_html"):
        e["proposed"]["bild_html"] = legacy["bild_html"]
    kallor = "svenska.se (SAOL/SO/SAOB) %s ; synonymer.se %s" % (
        U(e["ord"]), "https://www.synonymer.se/sv-syn/%s" % urllib.parse.quote(e["ord"]))
    if e["ord"] == "ryd":
        kallor += " ; wiktionary %s" % W("ryd")
    e["sokkoll"] = {"kalla": kallor, "slutsats": f["sl"]}
    if f.get("till"):
        e["forgranska_tillat"] = f["till"]
    e["approved"] = True
    n += 1

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("godkande %d kort" % n)
