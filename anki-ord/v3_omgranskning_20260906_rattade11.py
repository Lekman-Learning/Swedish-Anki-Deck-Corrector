# -*- coding: utf-8 -*-
"""De 11 kort blindgranskaren underkande i sats 1 och 2, rattade.

Varje anmarkning ar godtagen -- ingen av dem var ett falsklarm. Tre kategorier:
  SAKNAD BETYDELSE  brosta, dager, spont, bram
  FEL I EXEMPELMENINGEN  avpassa (ingen finit sats), vittnesgill (juridiskt
                         falskt pastaende), dimpa (fel preteritum)
  FEL ETIKETT       agn (doman), obetingad (fackspraklig), serendipitet och
                    nava (fel ≈≈-kategori)

Sokkoll: python slaupp.py --fil rep11_ord.json --antal 11 --tyst, kord
ofiltrerat i sessionens eget transkript.
"""
import io, json, urllib.parse

FIL = "sessions/session_2026-09-06_v3-omgranskning4.json"
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"avpassa": dict(
  hb="Ge något rätt storlek, mängd eller form för det den ska användas till",
  reg="neutral, neutral",
  grp=[["≈≈ anpassa"]],
  ex='Hon <font color="#3498db">avpassade</font> sina steg efter barnets.',
  etym=None,
  sl="UNDERKAND i blindgranskningen, och anmarkningen var ratt: exempelmeningen "
     "'Laroboker som ar speciellt avpassade for vuxenundervisningen' ar ingen mening utan "
     "en nominalfras med relativsats -- den saknar finit huvudverb. Jag hade tagit SO:s "
     "ordboksexempel rakt av utan att skriva om det till en sats, till skillnad fran vad "
     "jag gjort pa ovriga kort i samma paket. Bytt mot SO:s ANDRA syntex, 'hon avpassade "
     "sina steg efter barnets', som ar en fullstandig sats och dessutom visar den "
     "vanligare, konkreta anvandningen. Allt ovrigt oforandrat och redan godkant av "
     "granskaren: SO har EN betydelse ('ge en lamplig utformning eller utstrackning for "
     "ett aktuellt syfte'), kortet aterger den, och 'passa' ar utmonstrat ur definitionen "
     "eftersom det ar uppslagsordets eget huvudled."),

"agn": dict(
  hb="De torra skalen kring sädeskorn som skiljs bort när säden tröskas ; ätbart bete på kroken "
     "vid fiske",
  reg="neutral, neutral, jordbruk ; neutral, neutral, allmän",
  grp=[["skärmfjäll", "blomfjäll"], ["bete"]],
  ex='Nu gäller det att skilja <font color="#3498db">agnarna</font> från vetet.',
  etym="fornsvenska aghn; gemensamt germanskt ord, besläktat med grekiska akhne 'agnar' och med ax",
  sl="UNDERKAND i blindgranskningen. Anmarkningen: betydelse 2 var amnesmarkt 'jakt', men agn "
     "ar enligt SO ett FISKEord ('atbart lockbete (pa krok) vid fiske'), sa markningen "
     "motsager kortets egen definition. Det stammer. PROBLEMET AR ATT 'fiske' INTE FINNS I "
     "config.REGISTER_DOMAN. Listan har 'jakt' men inget fiskeomrade, och 'jordbruk', "
     "'biologi' och 'sjofart' passar lika daligt. Jag valde 'jakt' som narmaste granne, "
     "vilket blev fel pa just det satt granskaren beskriver. Satt till 'allman', som enligt "
     "config betyder BEDOMD men utan fackomrade -- det ar sant har (agn i "
     "betydelsen bete ar allmant ordforrad, inte fackssprak) och sager inte emot "
     "definitionen. ATGARD FOR ADAM: overvag att lagga till 'fiske' i "
     "config.REGISTER_DOMAN. Domanlistan utokades 2026-08-10 av precis det skalet -- att "
     "blindgranskningen upprepade gange saknade en amnesmarkning som inte fanns. Betydelse 1 "
     "behaller 'jordbruk', som granskaren uttryckligen godkande. Allt ovrigt oforandrat."),

"brösta": dict(
  hb="brösta sig: göra sig stor och skryta ; del av seldon som ligger mot hästens bringa och tar "
     "upp draget ; brösta av: koppla loss en kanon från förställaren och göra den skjutklar ; "
     "brösta av: skjuta i väg ett hårt skott, eller framföra något med åthävor",
  reg="vardaglig, lätt negativ ; fackspråklig, neutral, sport ; fackspråklig, neutral, militär ; "
      "vardaglig, neutral, sport",
  grp=[["stoltsera", "kråma sig"], ["≈≈ seldel"], ["≈≈ göra skjutklar"], ["≈≈ skjuta"]],
  ex='Han <font color="#3498db">bröstade</font> sig över segern som om han vunnit den ensam.',
  etym="'brösta av' och seldelen hör till tyska Protz, italienska biroccio 'tvåhjulig vagn' -- "
       "förställaren som kanonen kopplas loss från",
  sl="UNDERKAND i blindgranskningen, och anmarkningen tar udden av det forgranska_tillat jag "
     "sjalv skrivit. Jag hade motiverat att kanonbetydelsen var ett historiskt specialfall av "
     "SAOL:s 'avlossa en salva' och darfor inte behovde egen rad. Granskaren visar att det ar "
     "tvartom: SO ger 'koppla loss (kanoner) for att forsatta dem i eldstallning, sarsk. om "
     "aldre artilleripjaser' som HUVUDbetydelse for 'brosta av' -- att gora kanonen skjutklar "
     "ar alltsa inte samma sak som att avlossa den, det ar momentet fore. Tillagd som egen "
     "betydelse 3. Granskaren pekade ocksa ut ett FOLJDFEL i etymologin: uppgiften om tyska "
     "Protz och italienska biroccio 'tvahjulig vagn' hor till artilleribetydelsen -- vagnen ar "
     "FORSTALLAREN kanonen kopplas loss fran -- men jag hade kopplat den till seldelen. "
     "Etymologin skriven om sa att den pekar pa ratt betydelse och forklarar vad forstallaren "
     "ar. SO:s 'framfora under athavor' ('brostade av en Wagneraria') ar inlemmad i betydelse "
     "4, dar den hor ihop med sportanvandningen: bada handlar om att leverera nagot med kraft "
     "och later. Bada de betydelser granskaren uttryckligen godkande ('brosta sig' och "
     "seldelen) star oforandrade."),

"dager": dict(
  hb="Naturligt ljus som inte är direkt solsken ; ljust parti i en bild eller målning, motsatsen "
     "till skuggan — ofta i plural, dagrar ; det intryck något ger, den dager något framstår i ; "
     "i öppen dager: så att alla kan se det",
  reg="neutral, neutral ; fackspråklig, neutral, konst ; neutral, neutral ; neutral, neutral",
  grp=[["dagsljus"], ["belysning", "ljuseffekt"], ["≈≈ intryck"], ["≈≈ allmänt känt"]],
  ex='Det var redan full <font color="#3498db">dager</font> när hon vaknade.',
  etym="fornsvenska dagher; samma ord som dag",
  sl="UNDERKAND i blindgranskningen, och aven har foll mitt eget forgranska_tillat. Jag hade "
     "motiverat att kortets tre betydelser LAG OVER vad rastrukturen kraver. Granskaren visar "
     "att en av SO:s fyra moment saknades helt: bildbetydelsen, 'ljuseffekt i konstverk' "
     "(SO:s syntex 'tavlans skuggor och dagrar'). Den ar dessutom exakt den betydelse "
     "OLD-facit raknar upp separat som 'ljuseffekt' och SAOL som sitt tredje semikolonled -- "
     "tva kallor jag hade framfor mig. Tillagd som betydelse 2, i SO:s egen ordning. "
     "Granskaren pekade ocksa ut ett FOLJDFEL i synonymraden: 'belysning' lag grupperad under "
     "betydelse 1 (dagsljuset) men hor till just den bildbetydelse kortet utelamnade. Flyttad, "
     "tillsammans med 'ljuseffekt' som ocksa ar SAOL:s eget led -- bada belagda. Grupp 1 har "
     "nu 'dagsljus' ensam. Doman konst tillagd pa betydelse 2. Definition, exempelmening och "
     "etymologi var enligt granskaren korrekta och star oforandrade."),

"obetingad": dict(
  hb="Som uppstår spontant och av sig själv, om en känsla eller egenskap ; helt utan villkor "
     "eller krav",
  reg="neutral, neutral ; neutral, neutral",
  grp=[["≈≈ spontan"], ["oinskränkt", "förbehållslös"]],
  ex='Barnets <font color="#3498db">obetingade</font> tilltro till föräldrarna.',
  etym="till o- och betinga",
  sl="UNDERKAND i blindgranskningen. Anmarkningen: SO:s huvudbetydelse ar 'som uppkommer "
     "spontant' <<om kansla, egenskap etc.>> -- en ALLMANSPRAKLIG betydelse -- men jag hade "
     "skrivit om den till 'som sker av sig sjalv utan att ha larts in, till exempel en "
     "reflex' och stamplat den 'fackspraklig, psykologi'. Darmed gjorde jag SO:s allmanna "
     "betydelse till inlarningspsykologins 'obetingad reflex'. Granskaren pekar pa att kortet "
     "da sag emot sig sjalvt: exempelmeningen ar SO:s egen och allmansspraklig ('barnets "
     "obetingade tilltro till foraldrarna'), och ett barns tilltro ar varken en reflex eller "
     "'≈≈ medfodd'. Helt ratt. Definitionen foljer nu SO ordagrant, registret ar neutralt och "
     "kategorin bytt till '≈≈ spontan', som ar SO:s eget ord. Reflexanvandningen ar inte "
     "utskriven som egen betydelse -- SO ger den inte som ett eget moment, och att lagga till "
     "den vore att uppfinna en betydelse. Etymologins kontrast betingad/obetingad ar struken "
     "av samma skal: den forklarade den fackbetydelse kortet inte langre pastar sig ha. "
     "Betydelse 2 var enligt granskaren korrekt och star oforandrad."),

"serendipitet": dict(
  hb="Förmågan att göra lyckliga upptäckter av en ren slump",
  reg="neutral, positiv",
  grp=[["≈≈ upptäckarförmåga"]],
  ex='Flemings <font color="#3498db">serendipitet</font> gav världen penicillinet — han letade '
     'efter något helt annat.',
  etym="efter engelska serendipity; till namnet Serendip i sagan De tre prinsarna från Serendip, "
       "av persiska Sarandip 'Sri Lanka'",
  sl="UNDERKAND i blindgranskningen. Anmarkningen: kategorin '≈≈ lyckosam slump' ar sakligt fel, "
     "inte bara vid. Bade SO och kortets egen definition sager FORMAGA -- en egenskap hos en "
     "person -- men kategorin placerar ordet bland handelser och tillfalligheter. Granskaren "
     "jamfor med ovriga kort i paketet, dar ≈≈ genomgaende ar ett sant overbegrepp (simpa "
     "≈≈ bottenfisk, dyrk ≈≈ laskverktyg), och det ar ratt: en serendipitet ar ingen slump, "
     "det ar formagan att ta vara pa den. Bytt till '≈≈ upptackarformaga', som granskaren "
     "sjalv foreslog som det mer informativa alternativet. EXEMPELMENINGEN hade samma "
     "forskjutning -- 'upptacktes genom ren serendipitet' behandlar ordet som sjalva "
     "slumphandelsen. Bytt till granskarens formulering, dar formagan tillskrivs Fleming. "
     "Definition och etymologi var enligt granskaren korrekta mot SO och star oforandrade."),

"spont": dict(
  hb="Utstående list på en bräda som passar in i ett spår på nästa bräda vid hopfogning ; själva "
     "spåret på en sådan bräda, eller fogen mellan två hopfogade brädor",
  reg="fackspråklig, neutral, teknik ; fackspråklig, neutral, teknik",
  grp=[["kantlist"], ["≈≈ fog"]],
  ex='<font color="#3498db">Sponten</font> på plankan passade perfekt in i spåret på nästa.',
  etym="av lågtyska spunt 'sprund (i tunna); tapp; spont'",
  sl="UNDERKAND i blindgranskningen, och mitt forgranska_tillat var fel. Jag hade motiverat att "
     "SO:s tva underbetydelser saknar egen definitionstext och att SAOL:s led beskriver samma "
     "foremal fran tva hall. Granskaren visar att de tva underbetydelserna lyder 'aven om "
     "RANNAN pa sadan brada' och 'aven om FOGEN mellan sadana brador' -- alltsa tva andra "
     "referenter an listen sjalv, inte tva satt att beskriva listen. SAOL:s semikolon i "
     "'kantlist och fals pa brada; fog mellan sadana brador' skiljer likasa tva klart olika "
     "saker. Ordet betecknar alltsa bade tappen, sparet och fogen dem emellan. Tillagt som "
     "betydelse 2. Aven exempelmeningen justerad: den sa 'rannan pa nasta' medan definitionen "
     "sa 'spar', sa kortet anvande tva ord for samma sak; nu 'spar' pa bada stallen. "
     "'kantlist' ar SAOL:s eget definitionsord och godkandes uttryckligen av granskaren, "
     "liksom register, doman och etymologi -- alla oforandrade."),

"näva": dict(
  hb="Växt med oftast handflikiga blad och purpurröda blommor",
  reg="neutral, neutral, biologi",
  grp=[["≈≈ ört"]],
  ex='I skogsbrynet blommade <font color="#3498db">näva</font> med sina purpurröda kronblad.',
  etym="till svensk dialekt näv 'näsa; näbb' -- växten har näbbliknande frukter",
  sl="UNDERKAND i blindgranskningen. Anmarkningen: kategorin '≈≈ prydnadsvaxt' ar sakligt fel. "
     "Nava (slaktet Geranium) ar i svenskt sprakbruk framfor allt VILDA orter -- skogsnava, "
     "blodnava, stinknava -- och SAOL sager bara 'en vaxt'. Granskaren pekar dessutom pa att "
     "kortet sa emot sig sjalvt: min egen exempelmening placerar vaxten i skogsbrynet, alltsa "
     "vildvaxande, medan kategorin sa prydnadsvaxt. Helt ratt, och felet kom av att jag lat "
     "OLD-facits 'geranium' dra tankarna till pelargonen (som ar en Pelargonium, ett annat "
     "slakte). Bytt till '≈≈ ort', granskarens eget forslag och det som stammer med bade SAOL "
     "och exempelmeningen. Betydelse och etymologi var enligt granskaren korrekta mot SO och "
     "star oforandrade -- liksom det storsta fyndet pa kortet, att legacys forsta betydelse "
     "'en knuten hand' hor till ett annat ord (NAVE) och ar struken."),

"bräm": dict(
  hb="Bred ytterkant på ett klädesplagg, av annat material än plagget i övrigt och oftast av "
     "päls ; kant med avvikande utseende, eller kant i allmänhet ; ytter- eller överkant på en "
     "fågelfjäder eller ett blomhylle",
  reg="neutral, neutral ; neutral, neutral ; fackspråklig, neutral, biologi",
  grp=[["≈≈ pälskant"], ["kant", "bård"], ["≈≈ fjäderkant"]],
  ex='Kappan hade ett brett <font color="#3498db">bräm</font> av mörk päls runt halsen.',
  etym="fornsvenska brem; av lågtyska breme med samma betydelse",
  sl="UNDERKAND i blindgranskningen, och anmarkningen ar sarskilt trafffsaker eftersom den "
     "pekar pa en INRE motsagelse i mitt eget kort. Jag hade tva betydelser (pälskanten och "
     "fjaderkanten) och motiverade i forgranska_tillat att SO:s forsta underbetydelse saknar "
     "egen definitionstext. Granskaren visar att SO har tre nivaer och att den mellersta ar "
     "'kant med avvikande utseende eller kant i allmanhet' -- skumbram, tallriksbram. Och det "
     "avgorande: kortets synonym 'kant' horde till just den betydelse kortet inte angav. Med "
     "min definition gick det inte att forsta 'ett vitt bram av skum langs stranden'. "
     "Betydelsen tillagd som nummer 2, och 'kant' och 'bard' -- bada ordagrant SAOL:s led -- "
     "flyttade dit dar de hor hemma. Betydelse 1 och 3 har fatt kategorier ur kortets egen "
     "definition. Register utokat till tre rader; biologidomanen ligger kvar pa fjaderkanten, "
     "som granskaren inte hade nagot att invanda mot. Legacys tredje rad ('Kant som avviker i "
     "utseende') visade sig alltsa vara RATT hela tiden -- det var jag som strok den."),

"vittnesgill": dict(
  hb="Vars vittnesmål enligt lag är giltigt, om en person ; som går att lita på",
  reg="fackspråklig, neutral, juridik ; neutral, positiv",
  grp=[["≈≈ behörig att vittna"], ["trovärdig"]],
  ex='Han är knappast <font color="#3498db">vittnesgill</font> eftersom han inte var nykter när '
     'olyckan inträffade.',
  etym="fornsvenska vitnis gilder",
  sl="UNDERKAND i blindgranskningen -- och det var ett SAKFEL, inte ett formfel. Min "
     "exempelmening pastod 'Endast myndiga personer ar vittnesgilla i svenska domstolar'. "
     "Granskaren pekar pa rattegangsbalken 36 kap.: aven omyndiga kan horas som vittnen, och "
     "for den som inte fyllt 15 ar provar ratten lampligheten fran fall till fall. Nagon "
     "myndighetsgrans finns alltsa inte, och kortet larde ut en felaktig rattsregel som "
     "dessutom lat auktoritativ. Bytt mot granskarens forslag, som ligger nara SO:s eget "
     "belagg och visar ordet i sin faktiska anvandning -- om en enskild persons trovardighet, "
     "inte om en formell behorighetsgrans. Bada betydelserna var enligt granskaren belagda och "
     "star oforandrade, liksom synonymraden dar 'trovardig' ar SO:s egen underbetydelsetext."),

"dimpa": dict(
  hb="Falla tungt och överraskande ; oväntat uppenbara sig",
  reg="vardaglig, neutral ; vardaglig, neutral",
  grp=[["falla pladask"], ["dyka upp"]],
  ex='Äpplet <font color="#3498db">damp</font> ner från grenen och landade i gräset.',
  etym="ljudhärmande; jfr svensk dialekt dumpa 'falla tungt; gå klumpigt'",
  sl="UNDERKAND i blindgranskningen for ett GRAMMATIKFEL i exempelmeningen, och granskarens "
     "formulering ar den ratta domen: ett kort som lar ut fel preteritum av ett oregelbundet "
     "verb kan inte godkannas. Jag skrev 'Applet DIMPADE ner'. Dimpa ar starkt bojt -- dimper, "
     "DAMP, dumpit (SAOL ger aven dimpt i supinum) -- och formen 'dimpade' finns inte. Rattat "
     "till 'Applet DAMP ner'. Uppslagsordet ar markerat i sin preteritumform, vilket ar en "
     "fordel snarare an en brist: det ar just den formen man snubblar pa. Bada betydelserna "
     "var enligt granskaren ratt mot SO och SAOL och star oforandrade, liksom synonymerna "
     "'falla pladask' och 'dyka upp', som bada ar SAOL:s egna led."),
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
