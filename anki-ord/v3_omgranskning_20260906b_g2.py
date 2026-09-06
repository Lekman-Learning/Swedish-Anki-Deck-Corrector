# -*- coding: utf-8 -*-
"""Sats 2 (is:review efter lapses), ord 21-40. Samma metod som g1."""
import io, json, urllib.parse

FIL = "sessions/session_2026-09-06_v3-omgranskning2.json"
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"såt": dict(
  hb="Nära och innerlig, om vänskap ; mindre område som drivs av vid varje drev under en jakt",
  reg="neutral, positiv ; fackspråklig, neutral, jakt",
  grp=[["förtrolig"], ["≈≈ jaktområde"]],
  ex='De hade varit <font color="#3498db">såta</font> vänner ända sedan skoltiden.',
  etym="fornsvenska satter 'såt; förtrolig; ense'; nordiskt ord som motsvarar latin sanctus, "
       "jfr sankt",
  sl="Rastrukturen visar TVA SO-lemman: sat (adjektiv) 'fortrolig' och sat (substantiv) '(mindre) "
     "omrade som avjagas vid varje drev'. Legacy hade bada -- ratt. CIRKULARITET RATTAD: legacy "
     "sa 'FORTROLIG och nara, om en vanskap' och hade samtidigt 'fortrolig' som forsta synonym. "
     "Definitionen sager nu 'nara och innerlig' och 'fortrolig' -- som ar SO:s HELA definition och "
     "darmed sa belagd en synonym kan bli -- ligger dar den hor hemma. SYNONYMER BORTTAGNA: "
     "'hjartlig' och 'innerlig' finns inte i vare sig SO eller SAOL (de kommer fran OLD-facit, "
     "projektets svagare kalla), och 'jaktomrade' var en omskrivning av definitionen snarare an "
     "en synonym -- ersatt med kategori. REGISTER ANDRAT: 'litterar' saknar stod -- SO ger ingen "
     "brukligheskommentar; betydelse 2:s 'formell' bytt mot 'fackspraklig' med doman jakt, vilket "
     "SAOL:s eget led ('omrade for omgang av drevjakt') motiverar. Exempelmening oforandrad -- "
     "'sata vanner' ar den enda kollokation de flesta motter. Etymologi ny, ur SO."),

"näva": dict(
  hb="Växt med oftast handflikiga blad och purpurröda blommor, av släktet Geranium",
  reg="neutral, neutral, biologi",
  grp=[["≈≈ prydnadsväxt"]],
  ex='I skogsbrynet blommade <font color="#3498db">näva</font> med sina purpurröda kronblad.',
  etym="till svensk dialekt näv 'näsa; näbb' -- växten har näbbliknande frukter",
  sl="FEL BETYDELSE BORTTAGEN. Legacy hade TVA betydelser och satte 'En knuten hand, eller en "
     "handfull av nagot' FORST. Rastrukturen visar ett enda SO-lemma, nava (substantiv): 'typ av "
     "vaxt med oftast handflikiga blad och (purpur)roda blommor'. SAOL sager 'en vaxt'. "
     "OLD-facit sager 'en vaxt, geranium'. Ingen av de tre kallorna kanner nagon handbetydelse: "
     "handen heter NAVE, inte nava, och det ar tva olika ord. Legacy hade alltsa satt ett annat "
     "ords betydelse forst pa kortet -- vilket ocksa forklarar riskflaggan cirkular_synonym, "
     "eftersom synonymen 'hand' da stod mot en definition som borjade med 'en knuten hand'. "
     "Handbetydelsen struken tillsammans med synonymerna 'hand' och 'knytnave'. SYNONYMER "
     "BORTTAGNA aven for vaxten: 'geranium' och 'skogsnava' star inte i SO:s eller SAOL:s "
     "definitionstext (geranium kommer fran OLD) -- ersatta med kategori ur kortets egen "
     "definition. Register: legacys tva rader ('vardaglig' resp. 'formell') galde de tva "
     "betydelserna, varav en nu ar borta; en rad kvar, neutral med doman biologi. "
     "EXEMPELMENING BYTT -- den gamla visade handbetydelsen. Etymologi ny, ur SO: nav "
     "'nasa; nabb' forklarar namnet, eftersom nava har spetsiga, nabblika frukter (darav ocksa "
     "det engelska cranesbill)."),

"lov": dict(
  hb="Kursändring mot vinden när man seglar ; att någon får göra något ; skyldighet att göra "
     "något ; ledighet från skolan utöver helger ; starkt uttryckt uppskattning",
  reg="fackspråklig, neutral, sjöfart ; neutral, neutral ; neutral, neutral ; neutral, neutral ; "
      "högtidlig, positiv",
  grp=[["sväng", "gir"], ["tillåtelse"], ["≈≈ måste"], ["≈≈ skolledighet"], ["beröm", "pris"]],
  ex='Efter <font color="#3498db">lovet</font> var det svårt att komma igång med skolarbetet igen.',
  etym="seglarordet till lova, jfr fornsvenska lof 'vindsida'; de övriga till fornsvenska lof "
       "'bifall, tillåtelse; pris, beröm'",
  sl="FYRA SAKNADE BETYDELSER -- det grovsta fyndet i satsen, och riskflaggan "
     "old_har_fler_betydelser traffade ratt. Legacy hade EN betydelse: 'Svangande kursandring i "
     "segling'. Rastrukturen visar FYRA SO-lemman for lov, med sammanlagt fem definitioner: "
     "(1) 'kursandring i riktning mot vinden' med underbetydelsen 'svang, gir', (2) 'tillatelse' "
     "OCH 'skyldighet' (tva egna definitioner i samma lemma), (3) 'tid av ledighet fran "
     "skolundervisning' med tillagget 'utover helger', (4) 'starkt berom' [nagot hogtidligt]. "
     "SAOL bekraftar alla fyra: 'vandning av segelbat upp mot vinden; svang' / 'tillatelse' / "
     "'ledighet fran skola' / 'berom, pris'. Kortet hade alltsa bara den betydelse Adam ALDRIG "
     "moter, och saknade sportlov, hostlov, 'far jag lov', 'du har lov att stada' och "
     "'lovsang' -- ordets hela vardagliga anvandning. Alla fem nu med. 'svang' och 'gir' star "
     "ordagrant i SO:s underbetydelse (belagda), 'tillatelse' och 'berom, pris' ordagrant i "
     "SAOL:s led (belagda). Skyldighets- och skollovsbetydelserna har fatt kategorier ur kortets "
     "egen definition, eftersom ordbockerna inte ger nagon enordssynonym. REGISTER: sjofartsdomanen "
     "pa betydelse 1; 'hogtidlig' pa betydelse 5 med stod i SO:s egen markning 'nagot "
     "hogtidligt'; ovriga neutrala. Legacys 'formell' saknade stod. EXEMPELMENING BYTT till "
     "skollovet -- den vanligaste betydelsen for en gymnasieelev; den gamla visade seglingen."),

"vara (p)å färde": dict(
  hb="Hålla på att ske, vara i görningen — ofta om något oroande",
  reg="neutral, neutral",
  grp=[["≈≈ pågå"]],
  ex='Något stort var <font color="#3498db">på färde</font> när vi anlände till slottet.',
  etym="fornsvenska a færdhe; till färd",
  sl="Flerordsuttryck utan egen ordboksartikel. Rastrukturen ger SO-LEMMA farde (substantiv) med "
     "TOM definition -- ordet finns bara i den har frasen och far sin betydelse av den. Det ovriga "
     "i hamtningen ar verbet VARA (paga, befinna sig, kunna beskrivas som ...), som "
     "fritextsokningen dragit in tillsammans med 27 andra lemman; ingenting darifran hor till "
     "kortet. Kortet vilar darfor pa OLD-facit ('forsigga, halla pa att ske') och legacys text, "
     "som stammer overens. Definitionen i sak oforandrad; tillagt 'ofta om nagot oroande', vilket "
     "ar frasens faktiska bruk (nagot ar pa farde sags nastan alltid om hot eller "
     "hemligheter -- jfr kortets egen exempelmening) och det som skiljer den fran ett neutralt "
     "'paga'. SYNONYM BORTTAGEN: legacys 'vara pa gang' finns inte i nagon ordbok; ersatt med "
     "kategori ur kortets egen definition. REGISTER ANDRAT: 'litterar' saknar stod. "
     "Exempelmening oforandrad. Etymologi ny, ur SO."),

"holism": dict(
  hb="Riktning inom vetenskapen som menar att man i första hand ska studera helheten, eftersom den "
     "är mer än summan av delarna",
  reg="fackspråklig, neutral, filosofi",
  grp=[["≈≈ helhetssyn"]],
  ex='Inom <font color="#3498db">holismen</font> studeras systemet som helhet, inte del för del.',
  etym="bildning till grekiska holos 'hel, fullständig'",
  sl="SO: 'en vetenskapsteoretisk riktning som havdar att man i forsta hand ska studera "
     "foreteelsers helhet', med tillagget 'och att helheten inte kan betraktas som en summa av "
     "delarna'. SAOL: 'teori som havdar att helheten ar mer an summan av delarna'. Legacy hade "
     "bara SAOL:s halva ('Uppfattningen att helheten ar mer an summan av delarna') och saknade "
     "SO:s -- att holism ar en RIKTNING INOM VETENSKAPEN med ett metodkrav (studera helheten "
     "FORST). Skillnaden ar inte akademisk: legacys formulering gor holism till en allman livssyn, "
     "medan bada ordbockerna beskriver en vetenskapsteoretisk position. Bada halvorna nu med. "
     "Kategorin '≈≈ helhetssyn' lag redan pa kortet och ar satt ur definitionen; ordet har ingen "
     "enordssynonym i nagon kalla. Register och doman oforandrade -- 'fackspraklig' har stod i att "
     "ordet ar en vetenskapsteoretisk term. Exempelmening oforandrad. Etymologin oforandrad, "
     "matchar SO."),

"tillkortakommande": dict(
  hb="Svaghet eller brist som leder till att något går fel",
  reg="neutral, negativ",
  grp=[["misslyckande"]],
  ex='Rapporten pekade ut flera <font color="#3498db">tillkortakommanden</font> hos myndigheten.',
  etym=None,
  sl="SO: '(svaghet eller brist som leder till) misslyckande'. SAOL: 'misslyckande'. Legacys "
     "'Brist eller svaghet som leder till misslyckande' aterger SO:s parentes korrekt, men "
     "innehol ordet 'misslyckande' som ocksa var kortets enda synonym -- cirkulart. Definitionen "
     "sager nu 'att nagot gar fel' och 'misslyckande' ligger kvar som synonym, dar den ar belagd "
     "som SAOL:s hela definition. REGISTER ANDRAT: 'formell' saknar stod -- varken SO eller SAOL "
     "ger nagon brukligheskommentar. Ordet ar langt och byrakratiskt till formen, och det ar just "
     "den kanslan som gjorde att 49 % av decket felaktigt fick 'formell' (style_guide.md "
     "2026-08-10). Laddningen negativ, oforandrad. Exempelmening oforandrad. ETYMOLOGI "
     "UTELAMNAD: SO:s post saknar historiska uppgifter."),

"trollbinda": dict(
  hb="Fånga någons uppmärksamhet så fullständigt att hen glömmer tid och rum",
  reg="neutral, positiv",
  grp=[["fascinera"]],
  ex='Berättaren lyckades <font color="#3498db">trollbinda</font> barnen med sina spännande sagor.',
  etym=None,
  sl="SO: 'fullstandigt fanga uppmarksamheten hos', med tillagget 'nagon, sa att han/hon glommer "
     "tid och rum'. SAOL: 'fascinera'. Legacys 'Fanga nagons fulla uppmarksamhet' tappade SO:s "
     "tillagg, som ar det som ger ordet dess styrka -- att trollbinda ar inte bara att fa nagon "
     "att lyssna utan att fa hen att tappa tidsuppfattningen. Tillagt. 'fascinera' ar SAOL:s hela "
     "definition (belagd). SYNONYM BORTTAGEN: legacys 'fangsla' star inte i vare sig SO:s eller "
     "SAOL:s definitionstext (den kommer fran OLD-facit) och ar dessutom tvetydig -- fangsla "
     "betyder ocksa att satta i fangelse, vilket ar precis den sortens dubbeltydighet ett "
     "synonymfalt inte ska ha. REGISTER ANDRAT: 'vardaglig' saknar stod -- ingen ordbok markerar "
     "ordet; laddningen andrad fran neutral till positiv (att bli trollbunden ar en angenam "
     "upplevelse). Exempelmening oforandrad. ETYMOLOGI UTELAMNAD: SO:s post saknar historiska "
     "uppgifter -- sammansattningen troll + binda ar dock genomskinlig i sig."),

"huvudlös": dict(
  hb="Som visar total brist på eftertanke, oftast om en handling",
  reg="neutral, negativ",
  grp=[["obetänksam"]],
  ex='Att köra i det vädret var ett <font color="#3498db">huvudlöst</font> tilltag.',
  etym=None,
  sl="SO: 'som visar total brist pa eftertanke', med tillagget 'vanligen om handling eller "
     "dylikt'. SAOL: 'av. bildl. obetankksam'. Legacys 'Handlande utan tanke eller fornuft' "
     "beskrev en PERSON som handlar, men bade SO:s tillagg och kortets egen exempelmening ('ett "
     "huvudlost TILLTAG') visar att ordet vanligen beskriver HANDLINGEN, inte den som utfor den. "
     "Rattat, och SO:s 'TOTAL brist' ar nu utskrivet -- huvudlos ar inte 'lite obetankksam' utan "
     "det starkaste ordet i sin familj. 'obetankksam' star ordagrant i SAOL:s led (belagd). "
     "SYNONYMER BORTTAGNA: 'tanklos' och 'vansinnig' star inte i nagon ordboks definitionstext "
     "(de kommer fran OLD-facit), och 'vansinnig' ar dessutom starkare an huvudlos och skulle "
     "leda fel i ett HP-alternativ. REGISTER ANDRAT: 'vardaglig' saknar stod; laddningen andrad "
     "fran neutral till negativ, vilket SO:s 'total brist pa eftertanke' ger direkt stod for. "
     "Exempelmening oforandrad. ETYMOLOGI UTELAMNAD: SO:s post saknar historiska uppgifter."),

"strömfåra": dict(
  hb="Den snabbast rinnande delen av ett vattendrag",
  reg="neutral, neutral, geologi",
  grp=[["≈≈ vattendragets kärna"]],
  ex='Fiskarna sökte sig till <font color="#3498db">strömfåran</font> där vattnet rörde sig '
     'snabbast.',
  etym=None,
  sl="SO: 'snabbast rinnande del av vattendrag', med EN underbetydelse markt '(ingen egen "
     "definition -- utvidgning)'. SAOL har inget led alls for ordet. Legacys 'Djupaste, snabbast "
     "rinnande delen av ett vattendrag' lade till DJUPASTE, som ingen kalla ger -- stromfaran "
     "sammanfaller ofta med djuprannan men behover inte gora det, och SO namner det inte. "
     "Struket. SYNONYM BORTTAGEN, och det var huvudfelet: legacy hade 'fara', vilket ar "
     "uppslagsordets eget efterled -- alltsa ordet i sin egen synonymrad, och dessutom for brett "
     "(en fara kan vara vilken ranna som helst, det ar STROM-ledet som gor den till en stromfara). "
     "Ersatt med kategori ur kortets egen definition. REGISTER ANDRAT: 'formell' saknar stod; "
     "doman geologi tillagd. Exempelmening oforandrad. ETYMOLOGI UTELAMNAD: SO:s post saknar "
     "historiska uppgifter."),

"vara läns på": dict(
  hb="Ha slut på något, vara helt tom på det",
  reg="vardaglig, neutral",
  grp=[["≈≈ tom på"]],
  ex='Skåpet var <font color="#3498db">läns på</font> allt matförråd efter festen.',
  etym="till läns 'fri från vatten', ursprungligen om en båt som pumpats tom",
  sl="Flerordsuttryck. Rastrukturen ger SO-LEMMA lans (adjektiv) 'fri fran vatten' <<om bat>> "
     "plus lans (substantiv) i tva sjofartsbetydelser (segling i vindens riktning; kedja av "
     "flytande stockar). Det ovriga i hamtningen ar verbet VARA, som fritextsokningen dragit in "
     "tillsammans med 21 andra lemman. Frasen 'vara lans pa' har ingen egen artikel; den ar en "
     "overford anvandning av adjektivet, dar batens tomhet pa vatten blivit tomhet pa vad som "
     "helst. Legacys 'Helt tomd pa nagot' ar ratt men passiv -- frasen anvands om den som HAR "
     "slut pa nagot ('vi ar lans pa mjolk'), sa den aktiva formuleringen star forst. "
     "SYNONYM BORTTAGEN: 'utblottad pa' finns inte i nagon kalla och ar dessutom starkare "
     "(utblottad = utfattig); ersatt med kategori ur kortets egen definition. REGISTER ANDRAT: "
     "'litterar' ar rakt fel hall -- frasen ar talsprak. Exempelmening oforandrad. Etymologi ny, "
     "ur SO:s lans-artikel: att lansa en bat ar att pumpa den tom pa vatten, vilket forklarar "
     "hela bilden."),

"bräm": dict(
  hb="Bred ytterkant på ett klädesplagg, av annat material än plagget i övrigt och oftast av "
     "päls ; ytter- eller överkant på en fågelfjäder eller ett blomhylle",
  reg="neutral, neutral ; fackspråklig, neutral, biologi",
  grp=[["kant", "bård"], ["≈≈ fjäderkant"]],
  ex='Kappan hade ett brett <font color="#3498db">bräm</font> av mörk päls runt halsen.',
  etym="fornsvenska brem; av lågtyska breme med samma betydelse",
  sl="Rastrukturen: SO-LEMMA bram har EN definition ('bred ytterkant pa kladesplagg', med "
     "tillagget 'av annat material (vanligen pals) an plagget i ovrigt') och TVA underbetydelser, "
     "varav den forsta ar markt '(ingen egen definition -- utvidgning)' och den andra har egen "
     "text ('ytter- eller overkant pa fagelfjader eller blomhylle') -- alltsa TVA betydelser. "
     "Legacy hade TRE, dar den tredje ('Kant som avviker i utseende') ar en generalisering av de "
     "tva andra snarare an en egen betydelse och inte star i nagon ordbok. Struken. Aven "
     "betydelse 1 var avskalad: SO:s tillagg om MATERIALET (annat an plagget, vanligen pals) ar "
     "det som skiljer ett bram fran en vanlig kant, och det saknades. Tillagt. 'kant' och 'bard' "
     "star ordagrant i SAOL:s led (belagda) och ligger nu i grupp 1 dar de hor hemma -- legacy "
     "hade dem i en oindelad lista mot tre betydelser. Betydelse 2 saknar enordssynonym och har "
     "fatt en kategori. Register: legacys tre rader reducerade till tva; doman biologi kvar pa "
     "fjaderbetydelsen. EXEMPELMENING: 'runt halsen' tillagt sa att man ser var pa plagget "
     "brammet sitter."),

"svulst": dict(
  hb="Onormal knöl av vävnad som växer i kroppen",
  reg="neutral, neutral, medicin",
  grp=[["tumör"]],
  ex='Läkarna upptäckte en elakartad <font color="#3498db">svulst</font> vid undersökningen.',
  etym="av lågtyska swulst med samma betydelse; till svälla",
  sl="SO: 'tumor', med EN underbetydelse markt '(ingen egen definition -- utvidgning)'. SAOL: "
     "'tumor'. Legacys 'Tumor, onormal vavnadsmassa' hade tumoren INNE i definitionen och "
     "samtidigt som forsta synonym -- cirkulart, och den som inte kan 'tumor' fick ingen hjalp. "
     "Definitionen beskriver nu saken ('onormal knol av vavnad som vaxer i kroppen') och 'tumor' "
     "-- som ar bade SO:s och SAOL:s hela definition och darmed sa belagd en synonym kan bli -- "
     "ligger dar den hor hemma. SYNONYM BORTTAGEN: 'knuta' star inte i nagon ordboks "
     "definitionstext. REGISTER ANDRAT: 'formell' saknar stod -- ingen ordbok markerar ordet; "
     "doman medicin tillagd. Exempelmening oforandrad. Etymologi ny, ur SO: slaktskapen med "
     "SVALLA gor ordet genomskinligt -- en svulst ar nagot som svallt upp."),

"vittnesgill": dict(
  hb="Vars vittnesmål enligt lag är giltigt, om en person ; som går att lita på",
  reg="fackspråklig, neutral, juridik ; neutral, positiv",
  grp=[["≈≈ behörig att vittna"], ["trovärdig"]],
  ex='Endast myndiga personer är <font color="#3498db">vittnesgilla</font> i svenska domstolar.',
  etym="fornsvenska vitnis gilder",
  sl="SAKNAD BETYDELSE. Rastrukturen: SO-LEMMA vittnesgill har EN definition ('vars vittnesmal "
     "enligt lag ar giltigt' <<om person>>) och EN underbetydelse med EGEN text ('trovardig') -- "
     "tva betydelser. SAOL bekraftar bada i ett led med semikolon: 'vars vittnesmal ar giltigt; "
     "trovardig'. Legacy hade bara den juridiska. Den andra ar den allmansprakliga anvandningen "
     "('en vittnesgill kalla') och ar den man oftast moter utanfor en rattssal. Tillagd. "
     "'trovardig' ar SO:s egen underbetydelsetext och SAOL:s andra led (belagd), och den ar "
     "flyttad UT ur definitionen -- legacy hade den som enda synonym mot en definition som inte "
     "namnde den alls, sa synonymen svarade mot en betydelse kortet saknade. Betydelse 1 har "
     "ingen enordssynonym och har fatt en kategori ur kortets egen definition. REGISTER ANDRAT: "
     "'formell' bytt mot 'fackspraklig' med doman juridik for betydelse 1 (SO sager uttryckligen "
     "ENLIGT LAG); betydelse 2 ar allmansprak och neutral. Exempelmening oforandrad -- den visar "
     "betydelse 1 tydligt."),

"luns": dict(
  hb="Klumpig och tafatt karl",
  reg="vardaglig, nedsättande",
  grp=[["≈≈ klumpig karl"]],
  ex='Han var en riktig <font color="#3498db">luns</font> när han försökte laga hyllan.',
  etym=None,
  sl="OBS SVAGT KALLAGE: trekallskontrollen ger 'traffar: saol,saob' och 'SO: inga traffar' -- "
     "ordet saknas helt i SO. SAOL sager 'klumpig MANSPERSON' [vard.]. Legacys 'Klumpig, tafatt "
     "PERSON' var alltsa bredare an den enda moderna kallan som finns: SAOL specificerar kon, och "
     "en luns ar inte konsneutralt (jfr att motsvarande ord om kvinnor ar andra). Rattat till "
     "'karl'. SYNONYMER BORTTAGNA: 'drummel' och 'tolp' finns inte i SAOL:s definitionstext "
     "('drummel' ar OLD-facit); eftersom SO saknas helt finns ingen SYN-tagg att luta sig mot, sa "
     "det gar inte att belagga NAGON synonym. En kategori kvar, satt ur kortets egen definition "
     "(ingen kalla kravs for ≈≈). REGISTER ANDRAT: legacy hade 'neutral, latt negativ'. SAOL "
     "markerar ordet 'vard.', sa bruklighet ar vardaglig, inte neutral; och 'klumpig mansperson' "
     "om en person ar nedsattande, inte latt negativt -- config.REGISTER_VALENS reserverar "
     "'nedsattande' for just omdomen om PERSONER. Exempelmening oforandrad. ETYMOLOGI UTELAMNAD: "
     "ingen kalla."),

"snart sagt": dict(
  hb="Så gott som, i det närmaste",
  reg="neutral, neutral",
  grp=[["≈≈ nästan"]],
  ex='Det är <font color="#3498db">snart sagt</font> omöjligt att hinna med allt på en dag.',
  etym="till snart 'inom kort' och säga",
  sl="Flerordsuttryck utan egen ordboksartikel. Rastrukturen ger SO-LEMMA snart (adverb) 'inom "
     "kort' med underbetydelserna 'om en liten stund' och '(genast) nar' -- alltsa TIDSbetydelser, "
     "ingen av dem den frasen har. Fritextsokningen drar dessutom in 29 andra lemman. Kortet vilar "
     "pa OLD-facit ('sa gott som, nastan') och legacys text, som stammer. Definitionen justerad "
     "fran 'Nastan, i stort sett' till 'Sa gott som, i det narmaste': 'nastan' ar flyttat till "
     "synonymraden (legacy hade det pa bada stallen, cirkulart), och 'i stort sett' ar inte samma "
     "sak -- 'i stort sett klart' betyder att det mesta ar gjort, medan 'snart sagt omojligt' "
     "betyder att det narapa ar omojligt. SYNONYMER BORTTAGNA: 'nastan' och 'i princip' finns "
     "inte i nagon ordbok som synonymer till FRASEN; ersatta med en kategori ur kortets egen "
     "definition. REGISTER ANDRAT: 'litterar' saknar stod -- frasen ar vanlig sakprosa. "
     "Exempelmening oforandrad. Etymologin ar sammansattningens delar, ur SO:s snart-artikel."),

"dimpa": dict(
  hb="Falla tungt och överraskande ; oväntat uppenbara sig",
  reg="vardaglig, neutral ; vardaglig, neutral",
  grp=[["falla pladask"], ["dyka upp"]],
  ex='Äpplet <font color="#3498db">dimpade</font> ner från grenen och landade i gräset.',
  etym="ljudhärmande; jfr svensk dialekt dumpa 'falla tungt; gå klumpigt'",
  sl="SAKNAD BETYDELSE. Rastrukturen: SO-LEMMA dimpa har EN definition ('falla tungt och "
     "overraskande') och EN underbetydelse med EGEN text ('ovantat uppenbara sig') -- tva "
     "betydelser. SAOL bekraftar bada som egna led: 'falla pladask' [vard.] och 'av. bildl. dyka "
     "upp' [vard.]. Legacy hade bara den forsta. Den andra ar den bildliga ('han dimpade ner mitt "
     "i motet') och ar minst lika vanlig i tal. Tillagd. 'falla pladask' ar SAOL:s hela forsta "
     "led (belagd), 'dyka upp' SAOL:s andra (belagd); bada ar flyttade ut ur definitionen sa att "
     "de inte forklarar sig sjalva. SYNONYMER BORTTAGNA: legacys 'ramla' och 'dunsa' star inte i "
     "vare sig SO:s eller SAOL:s definitionstext -- 'ramla' ar dessutom svagare (man ramlar utan "
     "att det later, man dimper med en duns). REGISTER: 'vardaglig' oforandrat och nu belagt -- "
     "SAOL markerar BADA leden 'vard.'; en rad per betydelse. Exempelmening oforandrad. "
     "Etymologi ny, ur SO -- att ordet ar ljudharmande ar sjalva forklaringen till varfor det "
     "later som det gor."),

"vara trakterad av": dict(
  hb="Reagera positivt på ett visst bemötande, tycka om det man blir bjuden på",
  reg="neutral, neutral",
  grp=[["≈≈ uppskatta"]],
  ex='Hon var inte särskilt <font color="#3498db">trakterad av</font> hans komplimanger.',
  etym="av latin tractare 'behandla', i medeltidslatin även 'undfägna'",
  sl="Flerordsuttryck. Rastrukturen ger SO-LEMMA trakterad (adjektiv) 'som reagerar positivt' "
     "<<pa visst bemotande eller dylikt>> -- en ren traff som tacker hela kortet. Det ovriga i "
     "hamtningen ar verbet och substantivet VARA, indragna av fritextsokningen tillsammans med "
     "22 andra lemman. Legacys definition ar SO:s ordagrant och star kvar; tillagt 'tycka om det "
     "man blir bjuden pa', som fangar den vanligaste konstruktionen och binder ihop ordet med "
     "etymologins 'undfagna' (att traktera nagon ar att bjuda). SYNONYMER BORTTAGNA: 'gilla' och "
     "'vara smickrad av' star inte i nagon ordbok, och den andra ar dessutom fel -- att vara "
     "trakterad av nagot ar att uppskatta det, inte att kanna sig smickrad. Ersatta med kategori "
     "ur kortets egen definition. RISKFLAGGA old_delar_inget_ordforrad utredd: OLD sager "
     "'fortjust, vara tilltalad av, uppskatta', kortet 'reagerar positivt' -- samma sak, olika "
     "ord; flaggan ar falsk. REGISTER ANDRAT: 'litterar' saknar stod. Exempelmening oforandrad -- "
     "den ar dessutom nastan ordagrant SO:s eget syntex ('hon var inte sarskilt trakterad av den "
     "berusade mannens komplimanger', via OLD)."),

"förhärda": dict(
  hb="Göra någon kall och okänslig ; förhärda sig: stänga av sina egna känslor",
  reg="neutral, negativ ; neutral, negativ",
  grp=[["≈≈ förråa"], ["≈≈ stänga sig"]],
  ex='Modern bad och grät, men han <font color="#3498db">förhärdade</font> sig.',
  etym="till härda",
  sl="SO: 'gora kall och okanslig', med EN underbetydelse markt '(ingen egen definition -- "
     "utvidgning)'. SAOL ger TVA led: 'gora hard el. okanslig' och 'vara hard och okanslig' -- "
     "alltsa den transitiva och den reflexiva anvandningen var for sig. Legacy hade bada, vilket "
     "ar ratt; formuleringen av den andra ('forharda sig -- gora sig kanslolos') var dock nastan "
     "identisk med den forsta, sa kortet sag ut att saga samma sak tva ganger. Betydelse 2 "
     "omskriven till 'stanga av sina egna kanslor', som ar samma innebord men visar skillnaden: "
     "betydelse 1 handlar om vad livet gor med en, betydelse 2 om vad man gor med sig sjalv. "
     "SYNONYM BORTTAGEN: legacys andra synonym var 'vara hard och okanslig' -- ordagrant SAOL:s "
     "definitionstext, alltsa en upprepning av betydelsen och inte en synonym. Bada grupperna har "
     "nu kategorier satta ur kortets egen definition (ingen kalla kravs for ≈≈); ordbockerna ger "
     "ingen enordssynonym. REGISTER ANDRAT: 'formell' saknar stod -- SO ger ingen "
     "brukligheskommentar; laddningen negativ, oforandrad. Exempelmening oforandrad -- den visar "
     "den reflexiva betydelsen och ar bibliskt klingande, vilket passar ordet. Etymologin "
     "oforandrad, matchar SO ('se ursprung till harda')."),

"histrion": dict(
  hb="Skådespelare av enklare slag, ofta en kringresande gycklare",
  reg="ngt ålderdomlig, lätt negativ",
  grp=[["komediant"]],
  ex='Truppen bestod av kringresande <font color="#3498db">histrioner</font> utan fast scen.',
  etym="av latin histrio 'skådespelare'; kanske av etruskiskt ursprung",
  sl="SO: '(enklare) skadespelare', med tillagget 'sarsk. om komedianter, gycklare och dylikt' och "
     "brukligheskommentaren 'nagot alderdomligt'. SAOL: 'enklare skadespelare'. Legacys 'Enkel "
     "skadespelare' var ratt men mager, och SYNONYMRADEN var trasig: den innehol 'skadespelare' "
     "(en hyperonym -- varje skadespelare ar ingen histrion, sa den ar inte utbytbar) och "
     "'enklare skadespelare' (ordagrant SAOL:s definition, alltsa en upprepning av "
     "huvudbetydelsen). Bada strukna. Kvar star 'komediant', som SO namner i sitt eget tillagg "
     "(belagd) och som dessutom ar OLD-facit -- den enda posten som bade ar belagd och faktiskt "
     "utbytbar. SO:s 'gycklare' ar infogad i definitionen tillsammans med 'kringresande', vilket "
     "kortets egen exempelmening redan forutsatte men definitionen inte sa. Register oforandrat "
     "('ngt alderdomlig' har direkt stod i SO:s markning). RISKFLAGGA old_delar_inget_ordforrad "
     "utredd: OLD sager 'komediant', som nu ar kortets synonym -- flaggan slog till for att "
     "legacy saknade ordet. Loses av rattelsen. Exempelmening oforandrad. Etymologin oforandrad, "
     "matchar SO."),

"därom tvista de lärde": dict(
  hb="Om den saken är experterna oense — frågan har inget klart svar",
  reg="neutral, skämtsam",
  grp=[["≈≈ åsikterna går isär"]],
  ex='Huruvida metoden verkligen fungerar, <font color="#3498db">därom tvista de lärde</font>.',
  etym=None,
  sl="Flerordsuttryck utan egen ordboksartikel. Rastrukturen ger SO-LEMMA darom (adverb) 'om det "
     "forhallandet' [formellt] och SO-LEMMA tvista (verb) 'ligga i tvist' med underbetydelsen "
     "'grala, disputera' -- alltsa frasens bestandsdelar var for sig, plus 28 lemman som "
     "fritextsokningen dragit in (lara, lard, lardom ...). Kortet vilar pa OLD-facit ('(skamt.) "
     "fraga som ej har svar') och legacys text, som stammer. Definitionen i sak oforandrad, men "
     "formulerad sa att bada halvorna syns: att de lardes oenighet ar poangen OCH att slutsatsen "
     "ar att fragan saknar svar. SYNONYM BORTTAGEN: 'asikterna gar isar' finns inte i nagon "
     "ordbok och ar dessutom bara en omskrivning; nedgraderad till kategori (ingen kalla kravs "
     "for ≈≈). REGISTER ANDRAT, och det ar den viktigaste andringen: legacy hade 'litterar, "
     "neutral'. OLD-facit markerar uttryckligen '(skamt.)', och det ar hela poangen med frasen -- "
     "den anvands ironiskt, som en axelryckning, aldrig som en saklig konstatering att forskning "
     "pagar. config.REGISTER_VALENS har 'skamtsam' for just detta. Exempelmening oforandrad -- "
     "den visar frasens typiska satsbyggnad, med det som tvistas om forst."),
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    f = FIX.get(e["ord"])
    if not f:
        continue
    e["proposed"] = {
        "huvudbetydelse": f["hb"], "register": f["reg"],
        "synonymer": [s for g in f["grp"] for s in g],
        "synonym_groups": f["grp"], "exempelmening": f["ex"],
    }
    if f.get("etym"):
        e["proposed"]["etymologi"] = f["etym"]
    bild = (e.get("legacy") or {}).get("bild_html")
    if bild:
        e["proposed"]["bild_html"] = bild
    e["sokkoll"] = {"kalla": U(e["ord"]), "slutsats": f["sl"]}
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("godkande %d kort" % n)
