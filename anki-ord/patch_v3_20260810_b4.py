"""Batch 4, 2026-08-10 — 20 kort.

Tre sakfel hittade, varav ett som gjorde kortet direkt vilseledande:
`ornera` hade en exempelmening som beskrev fel handling ("ornerade lägenheten
med blommor"), `amsaga` hade ett stavfel i själva definitionen, och `prelat`
bar en registeretikett som ingen källa stöder.

Etymologin ger fyra oväntade par: brutto↔brutal, sufflett↔sufflé,
topografi↔utopi, gedigen↔dejlig.
"""
import patchlib as pl

MAL = "sessions/session_2026-08-10_v3-tre-kallor-b4.json"
P = {}


def lagg(ord_, slutsats, kalla=None, **andr):
    P[ord_] = (kalla or pl.kallor(ord_), slutsats, andr)


lagg("aristokratisk",
     "TVÅ BRUK, INTE ETT. SO skiljer på 'som **utmärker** aristokrati' "
     "(hållningen: 'aristokratisk arrogans', 'hennes aristokratiska "
     "uppträdande') och, neutralt, 'som **har att göra med** aristokrati' "
     "('aristokratiska miljöer'). Kortets 'Som tillhör adeln, förnäm' slog "
     "ihop dem, och tappade därmed att ordet oftast beskriver ett SÄTT hos "
     "någon som inte behöver vara adlig alls. Etymologin är dessutom en av de "
     "mest upplysande i decket.",
     huvudbetydelse="Som hör till adeln ; om sätt: förnämt och lite "
                    "överlägset — även hos den som inte är adlig",
     synonymer=["adlig", "förnäm", "högdragen", "nobel"],
     etymologi="Grekiska aristos 'bäst' + kratos 'makt' — de bästas välde.")

lagg("högfärdig",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'som uppträder med en känsla av att vara "
     "förmer än andra' — kortet stämmer ordagrant. Belagt sedan 1385, alltså "
     "ett av deckets äldsta ord. Ordet är genomskinligt när man delar det: "
     "hög + färd, där **färd betyder 'uppträdande'** i gammal svenska (samma "
     "led som i *ofärd* och *välfärd*).",
     etymologi="hög + färd, där färd betyder 'uppträdande' — som i välfärd.")

lagg("gedigen",
     "TRE BETYDELSER, KORTET HADE TVÅ. SO ger 'fri från inblandning av annat "
     "material' (metallen), 'kraftig och stabil' (stenhuset) och 'grundlig, "
     "pålitlig' (utbildningen). Kortets 'solid och av hög kvalitet' täcker "
     "två av tre men suddar ut skillnaden mellan att något är STABILT och att "
     "det är GRUNDLIGT gjort. Etymologin är oväntad: tyska *gediegen* till "
     "*gedeihen* 'trivas, frodas' — släkt med **dejlig**. Det gediget gjorda "
     "är alltså det som fått växa färdigt.",
     huvudbetydelse="Om metall: ren och oblandad ; om saker: kraftig och "
                    "stabil ; om arbete: grundligt och pålitligt gjort",
     synonymer=["solid", "fullvärdig", "grundlig", "pålitlig"],
     etymologi="Tyska gedeihen 'frodas' — det som fått växa färdigt. Släkt "
               "med dejlig.")

lagg("komma för",
     "BEKRÄFTAT, INGEN ÄNDRING. SO: 'uppenbara sig för (någon) i tankarna', "
     "med exemplet 'det kom för honom att han hade sett henne förut' — vilket "
     "är nästan ordagrant kortets exempelmening. Belagt sedan 1691. "
     "ENDAST EN KÄLLA: varken synonymer.se eller Wiktionary har uttrycket. "
     "Rödflaggas enligt Adams regel 2026-08-10.")

lagg("sufflett",
     "ETYMOLOGIN GER ETT PAR ATT MINNAS. SO: 'upp- och nedfällbart "
     "skyddstak', SAOL preciserar 'på bil el. barnvagn' — kortet har båda. "
     "Ursprunget är franskans *souffler* '**blåsa upp**', vilket gör "
     "sufflett och **sufflé** till samma ord: båda är något som blåses upp.",
     etymologi="Franska souffler 'blåsa upp' — samma ord som sufflé.")

lagg("korus",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'samtidigt ljudande av flera röster', med "
     "exemplet 'alla barnen svarade i korus'. Kortet stämmer. Ordet är "
     "latinets *chorus* 'kör' — **samma ord som kor** (platsen i kyrkan där "
     "kören stod) och **korum** (militär andakt).",
     etymologi="Latin chorus 'kör' — samma ord som kor i en kyrka.")

lagg("ans",
     "KORTET VAR FÖR SNÄVT. Det sa 'skötsel och vård av något, **t.ex. "
     "utseendet**'. SO ger bara 'omsorgsfull vård', och dess enda exempel "
     "handlar om MARK: 'utan ans blir den ljuvaste idyll snart vildmark'. "
     "Ordet används mest om trädgård, djur och gröda — inte främst om "
     "utseendet. Kortets exempelmening (välvårdat skägg) är fortfarande "
     "riktig, men definitionen skulle inte peka bort från huvudbruket. "
     "Etymologin är kort och räcker: ans hör till **ansa**.",
     huvudbetydelse="Omsorgsfull vård och skötsel — oftast av mark, djur "
                    "eller växter",
     synonymer=["skötsel", "vård", "omvårdnad", "ansning"],
     etymologi="Hör till verbet ansa.")

lagg("fonetik",
     "EN SYNONYM SOM ÄR FEL SAK. Kortet har 'ljudlära', vilket går an. Men "
     "synonymer.se listar även **fonologi** som synonym, och det är fel — SO "
     "har fonologi under JFR, inte som liktydigt. Skillnaden är precis den "
     "sortens sak som testas: **fonetik studerar ljuden fysiskt, fonologi "
     "studerar hur ett språk använder dem för att skilja ord åt.** Den "
     "gränsdragningen skrivs in i definitionen i stället för att lämnas "
     "outsagd. Etymologin (grekiska phone 'ljud') står inte i SO, som bara "
     "säger 'till fonetisk' -- den är hämtad ur Wiktionarys uppslag och "
     "märks ut här som just det.",
     huvudbetydelse="Läran om språkljuden som fysiska ljud — till skillnad "
                    "från fonologi, som handlar om hur språket använder dem",
     synonymer=["ljudlära"],
     etymologi="Grekiska phone 'ljud, röst' — samma ord som i telefon.")

lagg("blindskrift",
     "BEKRÄFTAT, INGEN ÄNDRING. SO: 'skriftsystem med särskilt alfabet som "
     "kan urskiljas med känseln', JFR brailleskrift och punktskrift — exakt "
     "kortets två synonymer. Belagt sedan 1873. Ingen etymologi i SO, och "
     "ordet behöver ingen: det är genomskinligt sammansatt.")

lagg("såframt",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'såvida', SAOL: 'om, såvida'. "
     "synonymer.se märker ordet **(åld.)**, vilket motiverar att kortet inte "
     "är märkt vardagligt. Ursprunget är fornsvenska *sva framt*, "
     "ursprungligen '**så långt**' — alltså 'så långt som det gäller att…'. "
     "Belagt sedan 1373.",
     etymologi="Fornsvenska sva framt, 'så långt' — så långt som det gäller "
               "att något stämmer.")

lagg("sondera",
     "BEKRÄFTAT + ETYMOLOGI. SO ger tre bruk, kortet har de två som betyder "
     "något: sonden och det bildliga utforskandet. SO daterar dem: "
     "sond-betydelsen 1704, den bildliga **1811** — det bildliga bruket är "
     "alltså yngre, vilket förklarar varför 'sondera terrängen' känns som ett "
     "lån från medicinen. Det är precis vad det är. "
     "TVÅ KÄLLOR: Wiktionary strypte anropet — rödflaggas för omprövning.",
     etymologi="Av franska sonder, till sond — det bildliga bruket 'sondera "
               "terrängen' är lånat från läkarens sond.")

lagg("amsaga",
     "STAVFEL I DEFINITIONEN, OCH EN ETYMOLOGI SOM FÖRKLARAR ALLT. Kortet sa "
     "'**Pahittad**' — ett å saknades i själva definitionen. Rättat. "
     "Ursprunget är ordet som gör resten begriplig: amsaga var från början "
     "*ammsaga*, till **amma** — en historia man berättar för små barn. "
     "Därav både 'påhittad' och den nedlåtande tonen. SO ger dessutom "
     "gränsdragningen: historien '**framställs som autentisk** men avslöjas "
     "som påhittad', vilket kortet redan fångade.",
     huvudbetydelse="Påhittad historia som sprids som om den vore sann",
     synonymer=["skröna", "rövarhistoria", "myt", "påhitt"],
     etymologi="Ursprungligen ammsaga — en historia man berättar för små barn.")

lagg("prelat",
     "REGISTERETIKETTEN 'IRONISK' ÄR OBELAGD. Kortet var märkt 'formell, "
     "**ironisk**'. Ingen av källorna antyder ironi: SO ger '(hederstitel "
     "för) förtjänt katolsk präst' och SAOL detsamma. Ordet kan användas "
     "ironiskt, men det kan nästan alla titlar — det gör inte ironin till en "
     "egenskap hos ordet. Struken. Kortets synonym 'biskop' är dessutom fel "
     "sort: en prelat KAN vara biskop men behöver inte vara det. "
     "Etymologin: medeltidslatin *praelatus* 'framlyft', till *praeferre* "
     "'föredra' — **samma rot som preferera**.",
     register="formell",
     synonymer=["kyrkofurste", "högt uppsatt präst"],
     etymologi="Latin praelatus 'framlyft', till praeferre 'föredra' — samma "
               "rot som preferera.")

lagg("dalt",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'överdriven omsorg', JFR **pjosk** — "
     "kortets första synonym, belagd. SO:s exempel ('daltet med "
     "ungdomsbrottslingarna') visar att ordet nästan alltid används "
     "anklagande, vilket kortets register redan fångar. Ordet hör till "
     "**dalta**. Belagt först 1919, alltså ungt.",
     etymologi="Hör till verbet dalta.")

lagg("fördärvlig",
     "BEKRÄFTAT. SO: 'som medför stor skada eller olycka', SAOL: "
     "'fördärvbringande'. Kortet stämmer. SO:s exempel 'spritens fördärvliga "
     "inverkan' visar det typiska bruket: ordet fästs oftast vid en VANA "
     "eller ett INFLYTANDE, inte vid en enskild händelse — vilket kortets "
     "exempelmening om spelberoende också gör. Belagt sedan 1442.",
     etymologi="Till fördärv — det som leder någon i fördärvet.")

lagg("topografi",
     "BEKRÄFTAT + ETYMOLOGI MED ETT ORD ADAM KAN. SO ger kortets två "
     "betydelser: beskrivningen och själva terrängförhållandena. Ursprunget "
     "är grekiska *topos* 'plats' + *graphein* 'skriva' — och **samma topos "
     "finns i utopi**, som ordagrant betyder 'ingen plats'.",
     etymologi="Grekiska topos 'plats' + graphein 'skriva' — samma topos som "
               "i utopi, 'ingen plats'.")

lagg("ornera",
     "EXEMPELMENINGEN BESKREV FEL HANDLING. Kortet hade 'Hon **ornerade "
     "lägenheten med blommor och konstverk** inför festen' — men ornera "
     "betyder att smycka en YTA med inarbetat mönster, inte att inreda ett "
     "rum. SO: 'ornamentera', SAOL: 'pryda, utsira', och SO:s enda exempel är "
     "'vackert **ornerade bårder**'. Att ställa blommor i en lägenhet är att "
     "dekorera, inte att ornera. Ny exempelmening som visar rätt handling. "
     "Etymologin: latin *ornare* 'pryda' — samma ord som **ornament**.",
     huvudbetydelse="Smycka en yta med inarbetat mönster — möts oftast som "
                    "ornerad",
     exempelmening='Dörrposten var rikt <font color="#3498db">ornerad</font> '
                   'med slingrande rankor.',
     etymologi="Latin ornare 'pryda' — samma ord som ornament.")

lagg("brutto",
     "BEKRÄFTAT + EN ETYMOLOGI SOM ÄR SVÅR ATT TRO. SO: 'före vederbörliga "
     "avdrag', med motsatsen **netto** — kortet har den, vilket är rätt: "
     "paret är hela poängen. Ursprunget är italienskans *brutto*, "
     "egentligen '**rå, smutsig**', av latin *brutus* — alltså **samma ord "
     "som brutal**. Bruttovikten är varan i sitt råa skick, förpackning och "
     "allt.",
     etymologi="Italienska brutto 'rått, oputsat' — samma ord som brutal. "
               "Bruttovikt är varan i råskick.")

lagg("pistong",
     "BEKRÄFTAT + ETYMOLOGI. SO och SAOL ger båda bara 'kolv'. Kortet stämmer "
     "och förklarar dessutom var den sitter, vilket källorna inte gör. "
     "Ursprunget: italienska *pistare* '**stampa**' — kolven stampar i "
     "cylindern. Nära besläktat med **pistill**, mortelstöten.",
     etymologi="Italienska pistare 'stampa' — kolven stampar. Släkt med "
               "pistill.")

lagg("signera",
     "BEKRÄFTAT + ETYMOLOGI SOM BINDER IHOP FLERA ORD. SO: 'sätta sin "
     "signatur på'. Ursprunget är latin *signare* 'märka', till *signum* "
     "'tecken' — **samma rot som insignier, signal och resignera**. Att "
     "resignera är ordagrant att 'skriva av sig' något.",
     etymologi="Latin signum 'tecken' — samma rot som signal och insignier.")


if __name__ == "__main__":
    pl.bygg(P, MAL)
