# -*- coding: utf-8 -*-
"""Spar B (omgranskning), session_2026-09-06_v3-omgranskning.json, ord 1-20.

Urval: suspenderade is:review-kort rangordnade efter lapses -- Adam har glomt
dem 3-7 ganger och de ligger anda suspenderade, sa repetitionen han redan
betalat for ar inlast. Sokkoll via
    python slaupp.py --fil rep40_ord.json --antal 40 --tyst
kord i sessionens eget transkript (bevisrader SVENSKA_SE_HAMTAD och
UPPSLAGSORD for alla 40 orden).
"""
import io, json, urllib.parse

FIL = "sessions/session_2026-09-06_v3-omgranskning.json"
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"ömma för": dict(
  hb="Känna starkt med någon som har det svårt, och vilja skydda",
  reg="neutral, positiv",
  grp=[["ömka", "tycka synd om"]],
  ex='Hon kunde inte låta bli att <font color="#3498db">ömma för</font> den ensamma hunden.',
  etym="till öm, fornsvenska ömber 'usel; ömtålig; medlidsam' -- den som ömmar känner sig själv "
       "ömtålig inför någon annans nöd",
  sl="SO har ingen egen verbpost for 'omma for' utan for adjektivet om, dar en av betydelserna ar "
     "'som har och uttrycker varma, vardande och beskyddande kanslor' -- alltsa INTE bara "
     "medlidande utan ocksa varme och beskyddarinstinkt. SAOL listar frasen 'omma for (ngn)' som "
     "eget exempel. Legacys 'Hysa medkansla for' var CIRKULART: synonymlistan innehol exakt samma "
     "fras ('hysa medkansla for'), sa kortet forklarade ordet med sig sjalvt. Dessutom ar 'hysa' "
     "sjalvt ett svart ord. Omskrivet till 'Kanna starkt med ... och vilja skydda', som tar med "
     "bade medkanslan och SO:s beskyddarnyans. 'omka' och 'tycka synd om' star bada i "
     "synonymer.se (belagda, och ingen av dem forekommer i huvudbetydelsen). REGISTER ANDRAT: "
     "'litterar' var en gissning -- varken SO eller SAOL ger nagon brukligheskommentar, och "
     "SAOL:s exempel ar rak prosa. Neutral bruklighet, positiv laddning (kanslan ar varm). "
     "Etymologin ny, ur SO:s historiska uppgifter for om."),

"lovvärd": dict(
  hb="Som förtjänar beröm",
  reg="neutral, positiv",
  grp=[["berömvärd", "erkännansvärd"]],
  ex='Det var ett <font color="#3498db">lovvärt</font> försök, även om det inte lyckades.',
  etym="fornsvenska lofvärdher; till lov 'beröm' och värd",
  sl="SO: 'som fortjanar berom' -- legacys huvudbetydelse matchar ordagrant, oforandrad. SO:s "
     "underbetydelser bar tva SYN:synonym-taggar. 'beromvard' och 'erkannansvard' star bada i "
     "synonymer.se (belagda). SYNONYM BORTTAGEN: legacy hade 'prisvard', som i modern svenska "
     "framfor allt betyder 'vard sitt pris' (om varor) -- inte utbytbart mot lovvard i 'ett "
     "lovvart forsok'. Kvar star tva som ar det. REGISTER ANDRAT: 'litterar' saknar stod -- "
     "varken SO eller SAOL markerar ordet, och SO:s egna exempel ('ett lovvart forsok', 'lovvarda "
     "ambitioner') ar vanlig sakprosa. Laddningen ar daremot klart positiv, inte neutral. "
     "Exempelmeningen matchar SO:s eget syntex 'ett lovvart forsok', oforandrad. Etymologi ny, "
     "ur SO."),

"mondän": dict(
  hb="Fin och elegant på ett sätt som hör den stora världen och societeten till",
  reg="neutral, positiv",
  grp=[["fashionabel", "världsvan"]],
  ex='En <font color="#3498db">mondän</font> badort lockade societeten varje sommar.',
  etym="av franska mondain, till monde 'värld' -- alltså 'som hör (den stora) världen till'",
  sl="SO: 'fornamt elegant'. SAOL: 'fin, elegant, av vard'. OLD-facit: 'fin och elegant (med "
     "pragel av stora varlden)'. Legacys 'Varldsvan och elegant' tappade det som SAOL:s 'av vard' "
     "och OLD:s 'stora varlden' bada pekar pa: mondan handlar inte om att ha rest mycket utan om "
     "att hora till en fin, internationell societet. Tillagt. 'fashionabel' och 'varldsvan' star "
     "bada i synonymer.se (belagda). REGISTER ANDRAT: 'formell' saknar stod -- ingen av "
     "ordbockerna ger brukligheskommentar (jfr style_guide.md 2026-08-10: 49 % av decket "
     "felaktigt 'formell'). Ordet ar dessutom klart positivt laddat, inte neutralt. "
     "Exempelmeningen matchar SO:s eget syntex 'en mondan badort', oforandrad. Etymologi ny, ur "
     "SO -- monde 'varld' forklarar direkt varfor ordet betyder vad det betyder."),

"krösus": dict(
  hb="Väldigt rik person",
  reg="vardaglig, neutral",
  grp=[["mångmiljonär", "penningmagnat"]],
  ex='Efter försäljningen av bolaget var han en <font color="#3498db">krösus</font> som kunde '
     'köpa vad han ville.',
  etym="av grekiska Kroisos, namnet på en sagolikt rik kung i Lydien på 500-talet f.Kr.",
  sl="FAKTAFEL RATTAT. Legacy: 'Mycket rik men SNAL person', med synonymerna 'stormrik snaljap' "
     "och 'girigbuk'. SO sager bara 'mycket rik person' (vardagligt). SAOL: 'rik person' (vard.). "
     "synonymer.se: 'stormrik person, penningmagnat, rikeman, mangmiljonar, miljardar, kapitalist, "
     "magnat' -- inte ett enda ord om snalhet. Tva av tre kallor motsager alltsa legacy; bara "
     "OLD-facit ('mycket snal samt rik person') stoder det, och OLD ar projektets svagare kalla. "
     "Aven namnet bakom ordet talar emot: Kroisos var ordsprakligt RIK, inte girig. Snalheten "
     "struken ur bade definition och synonymer. EXEMPELMENING BYTT: den gamla ('trots att han "
     "levde sparsamt') byggde hela sin poang pa snalheten och skulle ha lart in felet igen. Ny "
     "mening visar rikedomen ensam. Register 'vardaglig' oforandrat -- bade SO och SAOL markerar "
     "det. Etymologi ny, ur SO."),

"marodör": dict(
  hb="Hänsynslös person som härjar och förstör, ofta en soldat som lämnat ledet för att röva",
  reg="neutral, negativ",
  grp=[["skadegörare", "plundrare"]],
  ex='Byn hade länge plågats av en <font color="#3498db">marodör</font> som stal boskap på natten.',
  etym="av franska maraudeur, till marauder 'stryka omkring och plundra' -- ursprungligen om "
       "soldater som lämnade ledet för att röva på egen hand",
  sl="SO: 'hansynslos skadegorare'. SAOL: 'plundrare, skadegorare'. Legacy hade bara 'Hansynslos "
     "plundrare' -- SMALARE an SO, som satter SKADEGORARE som huvudord. Skillnaden ar inte "
     "kosmetisk: SO:s eget exempel ar 'fotbollens marodorer', alltsa huliganer som forstor utan "
     "att plundra nagot. Definitionen breddad till 'harjar och forstor' med plundringen kvar som "
     "det vanliga specialfallet. Bada synonymerna star ordagrant i SAOL:s led (belagda). "
     "RISKFLAGGA old_delar_inget_ordforrad utredd: OLD sager 'skadegorare', vilket ar exakt SO:s "
     "huvudord -- flaggan slog till for att LEGACY saknade det ordet, inte for att OLD ar fel. "
     "Rattelsen loser flaggan. Etymologin (ny, ur SO) ar sjalv minneshjalpen: en marodor ar "
     "ursprungligen soldaten som gar ifran truppen for att stjala."),

"vidtaga": dict(
  hb="Sätta igång och genomföra något, till exempel en åtgärd ; ta vid direkt efter något annat",
  reg="neutral, neutral ; ngt ålderdomlig, neutral",
  grp=[["genomföra", "företa"], ["ta vid"]],
  ex='Efter branden beslöt kommunen att <font color="#3498db">vidtaga</font> skärpta '
     'brandskyddsåtgärder.',
  etym="fornsvenska vidhertaka 'ta vid, börja'; till vid och taga",
  sl="SO ger tva betydelser: 'utgora omedelbar fortsattning' och 'paborja och genomfora'. Legacy "
     "hade bada -- ratt, oforandrat i sak. 'genomfora' star ordagrant i SAOL:s led (belagd), "
     "'foreta' i synonymer.se (belagd), 'ta vid' i SAOL:s eget exempel 'milsvida skogar vidtar el. "
     "TAR VID norr om byn' (belagd). SYNONYM BORTTAGEN: legacys 'tillgripa' har en negativ klang "
     "(tillgripa vald, tillgripa nagons egendom) som vidtaga saknar -- inte utbytbart i 'vidtaga "
     "atgarder'. REGISTER: SAOL markerar det andra ledet 'el. ald.', sa betydelse 2 far 'ngt "
     "alderdomlig'; betydelse 1 ar omarkerad i bada ordbockerna och blir neutral. Legacys enda rad "
     "'formell, neutral' tackte dessutom tva betydelser -- nu en rad per betydelse. Etymologi ny, "
     "ur SO: vidhertaka 'ta vid' visar att bada betydelserna kommer ur samma bild."),

"asketisk": dict(
  hb="Som helt avstår från nöjen och lever mycket strängt och enkelt ; mycket sparsam och avskalad",
  reg="neutral, neutral ; neutral, neutral",
  grp=[["avhållsam", "försakande"], ["spartansk", "avskalad"]],
  ex='Munken levde <font color="#3498db">asketiskt</font> i en kal cell utan minsta bekvämlighet.',
  etym=None,
  sl="SO ger tva betydelser: 'som helt avstar fran njutningar' och 'mycket sparsam' (den senare "
     "aven bildligt, om stil). Legacy hade bada -- ratt. SPRAK: legacys 'njutning' bytt mot "
     "'nojen' (enklare, samma sak i sammanhanget). 'avhallsam' star i synonymer.se OCH ar "
     "OLD-facit (belagd), 'spartansk' i synonymer.se (belagd). 'forsakande' och 'avskalad' lag "
     "redan pa kortet. SYNONYMER GRUPPERADE: legacy hade sex synonymer i EN oindelad lista mot tva "
     "betydelser -- 'spartansk, aterhallsam, forsakande' hor till betydelse 1-2 och 'avskalad, "
     "sparsmakad, nedtonad' till betydelse 2, men utan gruppering gick det inte att se vilken som "
     "var vilken. Nu tva grupper, tva synonymer var. REGISTER: legacy hade EN rad ('neutral') mot "
     "tva betydelser -- nu en rad per betydelse. Ingen av ordbockerna markerar bruklighet. "
     "ETYMOLOGI UTELAMNAD: SO:s post for asketisk saknar historiska uppgifter, och asket slogs "
     "inte upp i den har omgangen -- ingen kalla, alltsa ingen etymologi (hellre tom an gissad). "
     "Exempelmening ny (munk i kal cell) -- konkret bild for betydelse 1."),

"lake": dict(
  hb="Saltlösning som mat läggs i för att hålla sig ; en gulbrun sötvattensfisk i torskfamiljen "
     "med brett huvud och stor mun",
  reg="neutral, neutral, mat ; neutral, neutral, biologi",
  grp=[["saltlag", "saltlake"], ["≈≈ torskfisk"]],
  ex='Gurkorna fick ligga en vecka i <font color="#3498db">lake</font> innan de var färdiga.',
  etym="fornsvenska lake 'saltlake', troligen av lågtyska lake; fisknamnet är ett annat ord, "
       "fornsvenska laki av ovisst ursprung",
  sl="SO ger tva betydelser: 'koksaltlosning for lakning eller konservering av livsmedel' och 'en "
     "gulbrun torskfisk med langstrackt kropp, brett huvud och stor mun'. Legacy hade bada, men "
     "fiskbeskrivningen var bara 'en sotvattenslevande torskfisk' -- SO:s sardrag (gulbrun, brett "
     "huvud, stor mun) ar just det som gor att man kan se fisken framfor sig, tillagt. 'saltlake' "
     "star ordagrant i SAOL:s led (belagd), 'saltlag' i synonymer.se (belagd). Fisken har ingen "
     "enordssynonym i nagon kalla -- kategori '≈≈ torskfisk' satt ur kortets egen definition "
     "(ingen kalla kravs for ≈≈). SYNONYM BORTTAGEN: legacys 'marinad' ar inte samma sak -- en "
     "marinad ar kryddad och ofta sur, en lake ar saltlosning; ingen kalla ger det. "
     "EXEMPELMENING BYTT: legacys 'Fisken lag i lake innan den roktes' anvander bada betydelserna "
     "pa en gang och gor kortet tvetydigt just dar det ska vara tydligt. Ny mening (gurkor) visar "
     "betydelse 1 rent. Register 'formell' struket, ingen ordbok markerar ordet; domaner tillagda. "
     "Etymologi ny, ur SO -- viktigt att de tva betydelserna ar TVA OLIKA ORD som rakat mota "
     "varandra, inte en betydelseutveckling."),

"endiv": dict(
  hb="Besk och knaprig bladgrönsak som liknar en avlång sallad",
  reg="neutral, neutral, mat",
  grp=[["≈≈ salladsgrönsak"]],
  ex='Salladen fick en besk och fräsch ton av <font color="#3498db">endiv</font>.',
  etym="fornsvenska endivia; via italienska endivia av arabiskt ursprung",
  sl="SO: 'en besk, sprod, avlang salladsliknande gronsak'. Legacy hade bara 'Bladgronsak som "
     "liknar sallad' -- alla tre sardragen som skiljer endiv fran vanlig sallad (BESK, SPROD, "
     "AVLANG) saknades, och utan dem ar definitionen sann men oanvandbar: den passar lika bra pa "
     "ruccola eller mangold. Tillagda. RISKFLAGGA old_delar_inget_ordforrad utredd: OLD sager 'ett "
     "slags salladsvaxt', kortet sa 'bladgronsak ... sallad' -- ingen konflikt, bara olika ord for "
     "samma sak; flaggan ar falsk har. Trekallskontrollen visar att endiv bara finns i svenska.se "
     "(ingen traff i synonymer.se) -- det finns alltsa INGEN belagd ordbokssynonym, sa kategori "
     "'≈≈ salladsgronsak' satt ur kortets egen definition (ingen kalla kravs for ≈≈). Legacys "
     "'bladgronsak' som synonym var cirkular, samma ord som i definitionen. REGISTER ANDRAT: "
     "'vardaglig' saknar stod -- varken SO eller SAOL markerar ordet; domanen mat tillagd. "
     "Exempelmening ny, byggd pa SO:s eget sardrag 'besk'. Etymologi ny, ur SO."),

"skult": dict(
  hb="Huvudets översta, välvda del",
  reg="vardaglig, neutral",
  grp=[["hjässa", "skalle"]],
  ex='Han tryckte ner mössan över <font color="#3498db">skulten</font>.',
  etym="svensk dialekt skult; troligen besläktat med skalle",
  sl="SO: 'huvudets oversta, valvda del' (vardagligt) -- kortets definition satt nu ordagrant "
     "efter SO. CIRKULARITET RATTAD: legacy sa 'Hjassa, huvudets oversta del' OCH hade 'hjassa' "
     "som enda synonym -- ordet forklarades alltsa med sin egen synonym, och den som inte kan "
     "'hjassa' fick ingen hjalp alls. 'hjassa' flyttad till synonymfaltet dar den hor hemma; "
     "definitionen star kvar pa egna ben. 'hjassa' och 'skalle' star bada ordagrant i SAOL:s led "
     "(belagda). REGISTER ANDRAT: legacy hade 'litterar' -- rakt fel hall. BADE SO och SAOL "
     "markerar ordet vardagligt, och SO:s eget exempel ('tryckte ner mossan over skulten') ar "
     "talsprak. Exempelmening ar just det syntexet, oforandrad. Etymologi ny, ur SO -- "
     "slaktskapen med 'skalle' ar sjalv minneshjalpen."),

"grand": dict(
  hb="Mycket litet korn eller smula av något ; medlem av den högsta spanska adeln",
  reg="neutral, neutral ; neutral, neutral, historia",
  grp=[["dammkorn", "smolk"], ["≈≈ adelsman"]],
  ex='Det fanns knappt ett <font color="#3498db">grand</font> damm kvar på den nypolerade möbeln.',
  etym="fornsvenska grand 'smula; gruskorn'",
  sl="SO: 'liten partikel', med det bibliska uttrycket 'se grandet i sin broders oga men inte "
     "bjalken i sitt eget' och den nekande anvandningen 'inte ett dugg' som underbetydelser. SAOL: "
     "'dammkorn, smolk'. Legacy hade bade partikelbetydelsen och den spanska adelstiteln -- den "
     "senare star inte i den hamtade SO/SAOL-posten men bekraftas av OLD-facit ('manlig spansk "
     "hogadel'), sa den star kvar. SPRAK: legacys 'Mycket liten mangd av nagot' var fel sorts ord "
     "-- ett grand ar ett KORN, nagot rakningsbart (darav 'ett grand'), inte en mangd. Rattat. "
     "'dammkorn' och 'smolk' star bada ordagrant i SAOL:s led (belagda). Adelstiteln har ingen "
     "belagd enordssynonym -- legacys 'spansk hogadel' var en omskrivning av definitionen, inte en "
     "synonym; ersatt med kategori '≈≈ adelsman' (ingen kalla kravs). REGISTER: legacys 'litterar' "
     "saknar stod och tackte dessutom tva betydelser -- nu en rad per betydelse, domanen historia "
     "pa adelstiteln. Exempelmening oforandrad. Etymologi ny, ur SO."),

"avpassa": dict(
  hb="Ge något rätt storlek, mängd eller form för just det den ska användas till",
  reg="neutral, neutral",
  grp=[["anpassa", "lämpa"]],
  ex='Läroböcker som är speciellt <font color="#3498db">avpassade</font> för vuxenundervisningen.',
  etym=None,
  sl="SO: 'ge en lamplig utformning eller utstrackning' -- EN betydelse. Legacys 'Anpassa eller "
     "justera nagot for att PASSA en viss situation' innehol uppslagsordets eget huvudled, alltsa "
     "ordet i sin egen definition. Omskrivet utan det: 'ratt storlek, mangd eller form'. "
     "RISKFLAGGA old_har_fler_betydelser utredd: OLD-facit klumpar ihop 'ratta, anpassa' med tva "
     "exempelmeningar ('Avpassa saltet i soppan', 'Avpassa farten efter vaglaget') utan separator "
     "-- det SER ut som flera betydelser men ar SO:s enda betydelse med tva olika objekt (mangd "
     "resp. utstrackning), vilket ar exakt vad SO:s 'utformning ELLER utstrackning' tacker. Ingen "
     "saknad betydelse; bada objekttyperna nu namnda i definitionen ('storlek, mangd eller form'). "
     "'anpassa' och 'lampa' star bada i synonymer.se (belagda). SYNONYM BORTTAGEN: 'justera' ar "
     "snavare (finjustera nagot befintligt) och tacker inte SO:s 'ge en utformning'. REGISTER "
     "ANDRAT: 'formell' saknar stod -- varken SO eller SAOL markerar ordet. Exempelmeningen ar "
     "SO:s eget syntex, oforandrad. ETYMOLOGI UTELAMNAD: SO:s post saknar historiska uppgifter, "
     "ingen kalla att ha."),

"snaskig": dict(
  hb="Kladdig och äcklig att ta i ; om reportage: som rotar närgånget i andras privatliv",
  reg="vardaglig, negativ ; vardaglig, negativ, journalistik",
  grp=[["kladdig", "sölig"], ["snuskig"]],
  ex='Toaletten på macken var riktigt <font color="#3498db">snaskig</font>.',
  etym="till snaska 'äta sötsaker med smackande ljud'",
  sl="SO ger tva betydelser: 'solig och kladdig' och 'som innebar otillborligt rotande i "
     "manniskors intima liv' (den senare bildligt, med syntexet 'ett snaskigt reportage om "
     "filmstjarnans karleksaffarer'). Legacy hade bada -- ratt. 'kladdig' och 'solig' star bada i "
     "synonymer.se (belagda, och 'solig' inleder SO:s definition ordagrant), 'snuskig' ordagrant i "
     "SAOL:s led (belagd). SYNONYMER GRUPPERADE OCH EN UTBYTT: legacys tre synonymer lag i EN "
     "oindelad lista mot tva betydelser -- 'grisig' hor till betydelse 1 och 'skvallrig' till "
     "betydelse 2, men utan gruppering syntes det inte. Nu tva grupper. 'skvallrig' utbytt mot "
     "'snuskig': skvaller kan vara ofarligt, medan SO:s 'OTILLBORLIGT rotande i INTIMA liv' ar "
     "just det snuskiga. REGISTER: vardaglig oforandrat, men laddningen andrad fran neutral till "
     "negativ -- bada betydelserna ar klart nedsattande (SO: 'otillborligt'). Domanen journalistik "
     "pa betydelse 2, ur SO:s eget syntex. Exempelmeningen matchar SO:s syntex 'toaletten var "
     "ganska snaskig', oforandrad. Etymologi ny, ur SO ('till snaska')."),

"vidja": dict(
  hb="Lång och böjlig kvist, ofta av vide, som man kan fläta med",
  reg="neutral, neutral",
  grp=[["≈ spö"]],
  ex='Hon flätade en korg av <font color="#3498db">vidja</font>.',
  etym="fornsvenska viþia; besläktat med vide, med grundbetydelsen 'flätning'",
  sl="SO: 'lang och bojlig kvist'. SAOL: 'bojlig gren ofta av vide, mjukt spo'. Legacy hade "
     "'Bojlig kvist, t.ex. fran vide, anvand till flatning' -- i sak ratt; SO:s 'LANG' tillagt "
     "(det ar langden som gor att den gar att flata med, jfr SO:s eget uttryck 'smal som en "
     "vidja'), och 't.ex.' ersatt med 'ofta' som SAOL har. SYNONYM NEDGRADERAD: legacy hade 'spo' "
     "OMARKERAT, alltsa som fullt utbytbart -- men ett spo ar ett tillskuret redskap att sla med, "
     "en vidja ar kvisten pa busken; de ar INTE utbytbara ('hon flatade en korg av spo' gar inte). "
     "Nedgraderat till '≈ spo', narmaste befintliga ord, belagt i SAOL:s led 'mjukt spo' och i "
     "synonymer.se. REGISTER ANDRAT: 'litterar' saknar stod -- varken SO eller SAOL markerar "
     "ordet. Exempelmening oforandrad. Etymologi ny, ur SO -- 'flatning' som grundbetydelse ar "
     "sjalv minneshjalpen, och slaktskapen med 'vide' forklarar SAOL:s 'ofta av vide'."),

"åtbörd": dict(
  hb="Rörelse med kroppen som visar vad man känner eller tänker",
  reg="neutral, neutral",
  grp=[["gest", "tecken"]],
  ex='Han gjorde en hotfull <font color="#3498db">åtbörd</font> med näven.',
  etym="till fornsvenska atbära sik 'bära sig åt' -- alltså hur man bär sig åt med kroppen",
  sl="SO: '(kropps)rorelse som uttrycker kansla eller tanke'. Legacy hade bara 'Gest som "
     "uttrycker en kansla' -- tva fel pa en rad. For det forsta saknades TANKE, som star jamsides "
     "med kanslan i SO:s definition (en atbord kan lika garna betyda 'kom hit' som 'jag ar arg'). "
     "For det andra var 'gest' bade definitionens huvudord och kortets forsta synonym -- "
     "cirkulart, och den som inte kan 'gest' fick ingen hjalp. Definitionen star nu pa vardagsord "
     "('rorelse med kroppen som visar vad man kanner eller tanker') och 'gest' ligger dar den hor "
     "hemma, bland synonymerna. 'gest' star ordagrant i SAOL:s led (belagd), 'tecken' i "
     "synonymer.se (belagd). REGISTER ANDRAT: 'litterar' saknar stod -- ingen av ordbockerna "
     "markerar ordet, och SO:s eget syntex ('en hotfull atbord med naven') ar vanlig prosa. "
     "Exempelmeningen ar just det syntexet, oforandrad. Etymologi ny, ur SO: 'bara sig at' visar "
     "att ordet ar helt genomskinligt sa fort man ser det."),

"skrodera": dict(
  hb="Tala stort och överdrivet om sina egna bedrifter",
  reg="neutral, negativ",
  grp=[["skryta", "skrävla"]],
  ex='Han satt och <font color="#3498db">skroderade</font> om sommarens fiskafängen.',
  etym="troligen ombildning av svensk dialekt skroa 'bullra; skryta'",
  sl="SO: 'skryta'. SAOL: 'skryta, skravla'. Legacy sa 'Skryta stort' OCH hade 'skryta' som "
     "forsta synonym -- cirkulart pa samma satt som skult och atbord: definitionen BESTOD av "
     "synonymen. Omskrivet till 'Tala stort och overdrivet om sina egna bedrifter', som beskriver "
     "handlingen i stallet for att namna den; 'skryta' ligger kvar bland synonymerna dar den ar "
     "belagd (ordagrant SO:s hela definition). 'skravla' star ordagrant i SAOL:s led (belagd). "
     "REGISTER ANDRAT: legacy hade 'vardaglig' -- men VARKEN SO ELLER SAOL ger nagon "
     "brukligheskommentar for skrodera (till skillnad fran t.ex. skult, dar bada markerar "
     "vardagligt). Utan stod blir bruklighet neutral. Laddningen daremot andrad fran neutral till "
     "negativ: att skrodera ar inget berom, och SO:s eget syntex ('satt och skroderade om "
     "sommarens fiskafangen') ar mild spott. Exempelmeningen ar det syntexet, oforandrad. "
     "Etymologi ny, ur SO -- 'bullra' fangar ljudet i ordet."),

"oför": dict(
  hb="Som inte kan röra sig eller arbeta på grund av en kroppsskada",
  reg="ålderdomlig, neutral",
  grp=[["vanför", "ofärdig"]],
  ex='Efter skadan var han <font color="#3498db">oför</font> till allt kroppsarbete.',
  etym="fornsvenska oför 'ofarbar; ur stånd att röra sig'; till o- och -för",
  sl="BETYDELSEFEL RATTAT. Legacy: 'Oformogen, oduglig till nagot' -- alltsa allman oduglighet. "
     "SO sager 'vanfor' (alderdomligt), SAOL 'fysiskt funktionshindrad' (ald.), OLD-facit "
     "'vanfor'. Alla tre kallorna menar KROPPSLIG oformaga, inte oduglighet i allmanhet. "
     "Skillnaden ar avgorande for HP:s ORD-del: 'ofor' i ett provsvar handlar om kroppen, och "
     "legacys bredare definition skulle ha gjort ett fel alternativ ('oduglig', 'inkompetent') "
     "lockande. Rattat. 'vanfor' ar SO:s hela definition (belagd), 'ofardig' star i synonymer.se "
     "(belagd). SYNONYM BORTTAGEN: 'oduglig' bar just det fel som rattas har. REGISTER: legacys "
     "'arkaisk' bytt mot 'alderdomlig' -- samma sak, men det ar den term bade SO ('alderdomligt') "
     "och SAOL ('ald.') anvander och den som star pa ovriga kort i decket. Exempelmeningen ('ofor "
     "till allt KROPPSARBETE') beskrev redan den rattade betydelsen och behovde inte andras -- den "
     "var bevisligen mer ratt an definitionen ovanfor den. Etymologi ny, ur SO: 'ur stand att rora "
     "sig' ar den rattade betydelsen ordagrant."),

"gå med håven": dict(
  hb="Samla in pengar eller bidrag ; försöka locka fram beröm om sig själv",
  reg="neutral, neutral ; neutral, lätt negativ",
  grp=[["≈≈ samla in pengar"], ["fiska efter beröm"]],
  ex='Ungdomsorkestern har <font color="#3498db">gått med håven</font> för att kunna åka på ett '
     'musikläger.',
  etym="till håv, som förutom fiskredskapet också är den nätförsedda skaftpåse kollekten samlades "
       "in med i kyrkan -- att gå med håven är att gå runt med den",
  sl="SAKNAD BETYDELSE. SO:s post for hav ger TVA idiomatiska betydelser for 'ga med haven': "
     "'forsoka fa bidrag' OCH 'forsoka locka fram vanligt omdome om sig sjalv'. Legacy hade bara "
     "den andra ('Tigga om berom eller komplimanger'). Den forsta ar inte en utvidgning utan en "
     "egen betydelse med eget syntex i SO: 'ungdomsorkestern har gatt med haven for att kunna aka "
     "pa ett musiklager' -- dar handlar det om pengar, inte om berom. Tillagd som betydelse 1 "
     "(SO:s egen ordning). Betydelse 1 har ingen belagd synonym; kategori '≈≈ samla in pengar' "
     "satt ur kortets egen definition (ingen kalla kravs for ≈≈). 'fiska efter berom' for "
     "betydelse 2 star i synonymer.se (belagd). REGISTER: legacys 'litterar' saknar stod; frasen "
     "ar vanligt talsprak. Neutral for insamlingen, latt negativ for beromfisket (som ar mild "
     "kritik). EXEMPELMENING BYTT till SO:s eget syntex for den NYA betydelsen -- den gamla visade "
     "bara betydelse 2. Etymologi ny, ur SO:s underbetydelse 'av. om liknande anordning for "
     "insamling av kollekt vid gudstjanst' -- den forklarar hela bilden: kyrkhaven pa skaft som "
     "gick runt bankraderna. OBS vid granskning: hamtningen for 'ga med haven' innehaller aven "
     "SAOL-material for 'ga pa' (fortsatta, bli lurad av, kosta) -- en artefakt av frassokningen, "
     "inte betydelser hos den har frasen, och lamnad utanfor kortet."),

"agn": dict(
  hb="De torra skalen kring sädeskorn som skiljs bort när säden tröskas ; ätbart bete på kroken "
     "vid fiske",
  reg="neutral, neutral, lantbruk ; neutral, neutral, fiske",
  grp=[["fröskal", "blomfjäll"], ["bete", "lockbete"]],
  ex='Nu gäller det att skilja <font color="#3498db">agnarna</font> från vetet.',
  etym="fornsvenska aghn; gemensamt germanskt ord, besläktat med grekiska akhne 'agnar' och med ax",
  sl="SO ger tva betydelser: 'skarm- och blomfjall (kring frukt) hos sad, som skiljs bort vid "
     "troskning' och 'atbart lockbete (pa krok) vid fiske'. Legacy hade bada -- ratt. SPRAK: "
     "legacys 'Det torra skalet runt ett sadeskorn' stod i singular, men agnar upptrader nastan "
     "alltid i plural (OLD-facit markerar 'ofta plur.', och SO:s eget uttryck ar 'skingras som "
     "agnar for vinden'); satt i plural. Dessutom saknades TROSKNINGEN, som ar hela poangen med "
     "ordet -- det ar darfor agnar ar sinnebilden for det vardelosa som blaser bort. Tillagt. "
     "'froskal' och 'blomfjall' star bada i SAOL/synonymer.se (belagda), 'bete' och 'lockbete' "
     "likasa. SYNONYM BORTTAGEN: legacys 'fiskbete' finns inte i nagon kalla som eget ord; 'bete' "
     "gor samma jobb och ar belagt. REGISTER ANDRAT: 'formell' saknar stod; domaner (lantbruk, "
     "fiske) tillagda, en per betydelse. Exempelmeningen ('skilja agnarna fran vetet') ar det "
     "bibliska uttryck SO sjalv markerar som 'ursprungligen bibliskt' -- den starkaste "
     "minneskroken som finns for ordet, oforandrad. Etymologi ny, ur SO: slaktskapen med 'ax' "
     "binder ihop betydelse 1 med nagot Adam redan kan."),

"förfara": dict(
  hb="Handla eller bete sig på ett visst sätt i en bestämd situation",
  reg="neutral, neutral",
  grp=[["gå till väga", "agera"]],
  ex='Instruktionen beskriver hur man ska <font color="#3498db">förfara</font> vid eldsvåda.',
  etym="jfr fornsvenska forfara 'försvinna; förstöra; försiggå; erfara'; till för- och fara",
  sl="SO: 'ga till vaga' -- EN betydelse. Legacy sa 'Ga till vaga pa ett visst satt' OCH hade 'ga "
     "till vaga' som enda synonym -- cirkulart: definitionen VAR synonymen, sa kortet gav noll "
     "information at den som inte redan kunde frasen. Definitionen omskriven till 'Handla eller "
     "bete sig pa ett visst satt i en bestamd situation'; 'ga till vaga' ligger kvar som synonym, "
     "dar den ar belagd som SO:s hela definition. 'agera' star i synonymer.se (belagd). REGISTER "
     "ANDRAT: 'formell' saknar stod -- varken SO eller SAOL ger nagon brukligheskommentar. Ordet "
     "KANNS byrakratiskt, och det ar precis den sortens kansla som gjorde att 49 % av decket "
     "felaktigt fick 'formell' (style_guide.md 2026-08-10); utan ordbokskommentar blir det "
     "neutral. Exempelmeningen ar SO:s eget syntex ('en instruktion om hur man ska forfara i "
     "handelse av eldsvada'), oforandrad. Etymologin lag redan pa kortet, matchar SO, oforandrad."),
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
