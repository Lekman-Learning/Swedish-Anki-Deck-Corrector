"""Batch 8, 2026-08-10 — de sista 25 korten i dagens kö.

De flesta av de här korten fick sitt innehåll rättat 2026-08-09. Dagens
tillägg är därför nästan uteslutande etymologin — och den är ovanligt stark i
just den här gruppen: `deadline` var en gräns fångar sköts vid om de korsade
den, `huldra` betyder 'hon som döljer sig', `slapstick` är namnet på en
verklig rekvisita, och `bonitet` visar sig vara samma ord som **bonus**.

Tre uttryck har bara synonymer.se som källa (`loafer`, `lägga sordin på`,
`ad interim`) och rödflaggas.
"""
import patchlib as pl

MAL = "sessions/session_2026-08-10_v3-tre-kallor-b8.json"
P = {}


def lagg(ord_, slutsats, kalla=None, **andr):
    P[ord_] = (kalla or pl.kallor(ord_), slutsats, andr)


lagg("nota bene",
     "BEKRÄFTAT + ETYMOLOGI. SO och SAOL ger båda 'märk väl'. Ursprunget är "
     "latinets *nota bene*, ordagrant '**märk väl**', till *notare* — samma "
     "ord som **notera**. Förkortningen **nb** finns med i synonymer.se och "
     "är den form man oftast möter.",
     etymologi="Latin nota bene, 'märk väl' — samma notare som i notera. "
               "Förkortas nb.")

lagg("överreklamerad",
     "BEKRÄFTAT. SO: 'framställd som bättre än den/det är', med två exempel "
     "som visar båda polerna: 'filmen var klart överreklamerad' och 'utsikten "
     "var **inte** överreklamerad'. Den nekande formen är vanlig och värd att "
     "känna igen. synonymer.se ger de moderna motsvarigheterna **hajpad** och "
     "**upphaussad**. Ingen etymologi i SO; ordet är genomskinligt sammansatt.",
     synonymer=["hajpad", "upphaussad", "överskattad"])

lagg("slapstick",
     "ETYMOLOGIN ÄR EN RIKTIG REKVISITA. SO: 'komedi eller fars med snabbt "
     "tempo och avancerad situationskomik'. Ordet kommer av engelskans *slap* "
     "'slag' + *stick* 'käpp' — **slapsticken var ett verkligt föremål**: två "
     "ihopsatta trälister som gav en hög smäll utan att göra ont, använda i "
     "commedia dell'arte. Genren är uppkallad efter sitt tillhygge.",
     synonymer=["fars", "buskis", "situationskomik"],
     etymologi="Engelska slap 'slag' + stick 'käpp' — en riktig rekvisita: "
               "två trälister som smällde högt utan att göra ont.")

lagg("ingenium",
     "ETYMOLOGIN BINDER IHOP TRE ORD, OCH LÖSER EN TVIST. SO: '(skapande) "
     "begåvning', SAOL: 'förstånd, begåvning'. Ursprunget är latin *ingenium* "
     "'natur; begåvning' — **samma ord som geni och ingenjör**. Det är också "
     "svaret på den blinda granskarens invändning 2026-08-09: granskaren nådde "
     "bara SAOB och menade att ordet var för snävt beskrivet. Med SO framme "
     "syns att '**skapande**' hör till kärnan, inte är ett tillägg.",
     synonymer=["begåvning", "snille", "skaparkraft"],
     etymologi="Latin ingenium 'medfödd begåvning' — samma ord som geni och "
               "ingenjör.")

lagg("dispasch",
     "BEKRÄFTAT + ETYMOLOGI. SO och SAOL ger båda bara 'haveriutredning'. "
     "Ordet är sjörättens term för uppgörelsen efter ett sjöhaveri: vem som "
     "ska betala vad. Ursprunget: italienska *dispaccio* '**avgörande, "
     "beslut**' — dispaschen ÄR avgörandet.",
     etymologi="Italienska dispaccio 'avgörande' — dispaschen är själva "
               "avgörandet efter ett sjöhaveri.")

lagg("håvor",
     "BEKRÄFTAT + ETYMOLOGI SOM FÖRKLARAR VARFÖR ORDET BARA FINNS I PLURAL. "
     "SO: 'gåvor', med de fasta uttrycken '**Guds håvor**' och '**lyckans "
     "håvor**'. Ordet är plural av fornsvenskans *hava*, av lågtyska *have* "
     "'**egendom**' — **samma ord som ha**. Håvor är alltså ordagrant 'det "
     "man har', vilket förklarar att formen alltid är plural.",
     etymologi="Plural av gammalt hava, 'egendom' — samma ord som ha. Därför "
               "bara i plural.")

lagg("deadline",
     "ETYMOLOGIN ÄR MÖRKARE ÄN MAN TROR. SO: 'bestämd tidpunkt när något "
     "senast måste vara avslutat', JFR **tidsgräns**. Ursprunget enligt SO: "
     "engelska *dead-line*, egentligen '**dödslinje**', **ursprungligen om en "
     "linje i ett fängelseområde** — fångar som passerade den blev skjutna. "
     "Ordet har alltså inte med 'sista tidpunkt' att göra från början, utan "
     "med en gräns man inte överlever att korsa.",
     etymologi="Engelska dead-line, 'dödslinje' — en linje i ett fängelse "
               "som fångar sköts för att korsa.")

lagg("besynnerlig",
     "BEKRÄFTAT + ETYMOLOGI. SO ger kortets två betydelser: 'svår att förstå "
     "sig på' och, om person, 'något tokig'. Ursprunget är oväntat: lågtyska "
     "*besunderlik*, **besläktat med sönder** och med **synnerlig** — "
     "grundbetydelsen är 'sär-skild, avskild från mängden'. Det som är "
     "besynnerligt är alltså det som skiljer ut sig, inte det som är fel.",
     etymologi="Släkt med sönder och synnerlig — grundbetydelsen är "
               "'avskild från mängden'.")

lagg("hurtbulle",
     "BEKRÄFTAT + ETYMOLOGI. SO: '(överdrivet) hurtig och **sportig** person'. "
     "Ordet är helt enkelt *hurtig* + *bulle*, där bulle används som "
     "nedlåtande personbeteckning (jfr *sötnos*, *pucko*). synonymer.se ger "
     "en lång rad belagda alternativ, av vilka **friskus** och "
     "**frisksportare** är de mest användbara.",
     synonymer=["friskus", "frisksportare", "hurtfrisk person"],
     etymologi="hurtig + bulle, där bulle är en nedlåtande personbeteckning.")

lagg("ad interim",
     "RÖDFLAGGAS — BARA EN KÄLLA. Varken SO, SAOL eller Wiktionary har "
     "uppslaget; bara synonymer.se, som ger 'tills vidare'. Kortets definition "
     "stämmer med det, och latinet är genomskinligt: *ad interim* 'för "
     "mellantiden'. Men enligt Adams regel 2026-08-10 ska ett kort med en enda "
     "källa märkas ut i stället för att framstå som fullbelagt.",
     etymologi="Latin ad interim, 'för mellantiden'. Förkortas a.i.")

lagg("abstrakt",
     "BEKRÄFTAT + ETYMOLOGI SOM ÄR EN BILD. SO ger fyra nyanser, alla med "
     "samma kärna: 'som inte kan uppfattas med sinnena', med MOTSATSEN "
     "**konkret**. Ursprunget: latin *abstractus* '**fråndragen, avskild**', "
     "till *abstrahera* — det abstrakta är det man dragit bort från det "
     "konkreta. Bilden av att DRA BORT egenskaper tills bara begreppet är "
     "kvar är hela ordet.",
     etymologi="Latin abstractus 'fråndragen' — man drar bort det konkreta "
               "tills bara begreppet är kvar.")

lagg("anvisa",
     "TVÅ BETYDELSER, OCH DEN ANDRA ÄR MYNDIGHETSSPRÅK. SO ger 'ge upplysning "
     "om' OCH '**bevilja**' ('anvisa medel'). Den andra är den man möter i "
     "budgettexter och är en helt annan handling än den första. SO:s exempel "
     "'hon blev **anvisad plats** längst bak' visar dessutom det passiva "
     "bruket, där ordet betyder 'tilldela'.",
     huvudbetydelse="Visa var något finns eller hur man ska gå till väga ; i "
                    "myndighetsspråk: bevilja eller tilldela, som i 'anvisa "
                    "medel'",
     synonymer=["hänvisa", "tilldela", "bevilja", "anslå"],
     etymologi="Efter tyska anweisen — samma visa som i att visa vägen.")

lagg("avhysa",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'tvinga att flytta från sin bostad', med den "
     "vidare betydelsen om tillfälliga uppehållsplatser ('ockupanterna "
     "avhystes'). JFR **vräka**. Ursprunget säger precis vad ordet gör: "
     "fornsvenska *afhysa* '**skilja från hus och gård**' — av + **hysa**, "
     "alltså motsatsen till att hysa någon.",
     etymologi="av + hysa — fornsvenskans 'skilja från hus och gård'. "
               "Motsatsen till att hysa någon.")

lagg("variabel",
     "BEKRÄFTAT — OCH EN BETYDELSE SOM ÄR ROLIG ATT KUNNA. SO ger de "
     "matematiska bruken och MOTSATSEN **konstant**, men också: "
     "'**stjärna med föränderlig ljusstyrka**'. En variabel är alltså också "
     "ett astronomiskt objekt. SO listar dessutom ordet både som substantiv "
     "och adjektiv, vilket kortet bör spegla.",
     huvudbetydelse="Storhet som kan anta olika värden — motsatsen till en "
                    "konstant ; som adjektiv: föränderlig",
     synonymer=["föränderlig storhet", "växlande", "skiftande"],
     etymologi="Till variera, av latin variare 'växla'.")

lagg("reservat",
     "BEKRÄFTAT + ETYMOLOGI. SO ger kortets båda betydelser (naturen och det "
     "avsatta området för en minoritet) och lägger till en tredje: '**äv. om "
     "område med värdefull äldre bebyggelse**', alltså kulturreservat. "
     "Ursprunget: latin *reservare* '**spara undan**' — **samma ord som "
     "reserv**. Ett reservat är något undanlagt.",
     etymologi="Latin reservare 'spara undan' — samma ord som reserv.")

lagg("beprövad",
     "BEKRÄFTAT — OCH ETT SKÄMTSAMT BRUK SOM ÄR VÄRT ATT KÄNNA. SO: 'som har "
     "prövats med framgång under tillräcklig tid', men noterar 'äv. "
     "skämtsamt' med det lysande exemplet '**generaler av beprövad "
     "oduglighet**'. Ordet kan alltså vändas ironiskt, vilket kortet inte "
     "visade. SO ger också den fasta frasen 'enligt **vetenskap och beprövad "
     "erfarenhet**', som är juridisk term inom vården.",
     huvudbetydelse="Har prövats med framgång under lång tid — kan vändas "
                    "ironiskt: 'av beprövad oduglighet'",
     etymologi="Till pröva; jfr tyska erprobt.")

lagg("förhala",
     "BEKRÄFTAT. SO ger kortets båda betydelser: 'försöka fördröja' och "
     "sjötermen. En sak preciseras: SO säger att sjöbetydelsen även används "
     "reflexivt om personer ('**förhala sig** in till kajen'), där personen "
     "tänks representera fartyget. Kortet är i övrigt oförändrat.",
     etymologi="Samma ord i båda betydelserna — att hala, dra i något.")

lagg("bonitet",
     "ETYMOLOGIN LÖSER ETT PROBLEM SOM STÅTT KVAR SEDAN I GÅR. SO och SAOL "
     "ger BARA 'grad av avkastningsförmåga' — kreditvärdighetsbetydelsen, som "
     "kortet burit, finns i en av fem källor och inte i någon av "
     "Akademiens. Den stryks nu. Ursprunget förklarar båda bruken: tyska "
     "*Bonität*, till latin *bonus* '**god**' — **samma ord som bonus**. "
     "Bonitet är helt enkelt 'godhetsgrad', vilket kan gälla mark lika väl "
     "som en gäldenär. Den gamla synonymen *bördighet* var obelagd och "
     "hängde kvar via synonym_groups; den försvinner med samma ändring.",
     huvudbetydelse="Markens grad av avkastningsförmåga",
     synonymer=["avkastningsförmåga", "godhetsgrad"],
     etymologi="Latin bonus 'god' — samma ord som bonus. Bonitet är "
               "godhetsgrad.")

lagg("bilateral",
     "BEKRÄFTAT + SYSKONORDEN. SO: 'som innefattar två parter', JFR "
     "**multilateral** (flera) och **unilateral** (ensidig). De tre hör ihop "
     "och är lättare som grupp än var för sig; kortet nämnde dem inte. "
     "Ursprunget: *bi-* 'två' + latin *latus* '**sida**' — samma *latus* som "
     "i *lateral* och *kollateral*.",
     huvudbetydelse="Som gäller två parter — jämför unilateral (en) och "
                    "multilateral (flera)",
     etymologi="bi- 'två' + latin latus 'sida'.")

lagg("loafer",
     "RÖDFLAGGAS — BARA EN KÄLLA. Varken SO, SAOL eller Wiktionary har "
     "uppslaget; bara synonymer.se, som ger 'sko i mockasinmodell, lågsko "
     "utan snörning, promenadsko'. Kortets definition stämmer med det. "
     "Etymologin (engelska *loafer* 'dagdrivare') är allmänt känd men står "
     "inte i någon av de tre källorna och skrivs därför inte in som belagd.",
     synonymer=["mockasin", "lågsko utan snörning", "promenadsko"])

lagg("lägga sordin på",
     "RÖDFLAGGAS — BARA EN KÄLLA. Uttrycket saknas i SO, SAOL och Wiktionary; "
     "synonymer.se ger bara 'förstämma'. Innehållet är ändå härledbart ur "
     "**sordin**, dämparen man sätter på ett stråk- eller blåsinstrument för "
     "att dämpa ljudet — att lägga sordin på något är att dämpa stämningen. "
     "Det skrivs in som etymologi eftersom det gör uttrycket begripligt, med "
     "noteringen att belägget är svagt.",
     etymologi="En sordin är dämparen man sätter på ett instrument — att "
               "lägga sordin på är att dämpa.")

lagg("revy",
     "ETYMOLOGIN KNYTER IHOP ALLA TRE BETYDELSERNA. Kortet fick sin tredje "
     "betydelse (den militära förbimarschen) 2026-08-09 efter den blinda "
     "granskningen. Nu syns varför de tre hör ihop: franska *revue* "
     "'**återblick, översikt**', till *revoir*, latin *revidere* '**återse**' "
     "— **samma ord som revidera**. Föreställningen, artikeln och "
     "förbimarschen är alla former av att se något passera i översikt. Det "
     "är också ursprunget till uttrycket 'passera revy'.",
     etymologi="Franska revue 'återblick', av latin revidere 'återse' — samma "
               "ord som revidera. Därav 'passera revy'.")

lagg("civiliserad",
     "BEKRÄFTAT + ETYMOLOGI. SO ger fyra betydelser; kortets två motsvarar de "
     "två första i den ordning som är rätt för HP. Ursprunget: franska "
     "*civiliser* 'införa ordnat samhällsskick', till **civil**, av latin "
     "*civis* '**medborgare**' — samma ord som i *civil* och *stad*. Att "
     "civilisera är ordagrant att göra till stadsbo. SO:s motsatsord är värda "
     "att känna: **barbarisk, primitiv, ociviliserad**.",
     etymologi="Till civil, av latin civis 'medborgare' — att civilisera är "
               "ordagrant att göra till stadsbo.")

lagg("vedervåga",
     "BEKRÄFTAT, MEN KÄLLÄGET SKA SYNAS. Bara SAOL har uppslaget ('sätta på "
     "spel; våga sig på'); SO saknar det helt, och synonymer.se märker ordet "
     "**(mindre brukl.)**. Kortets båda bruk fick sin form 2026-08-09 efter "
     "den blinda granskningen, och står fast. Etymologin: *veder-* är samma "
     "förled som i **vedergällning** och betyder 'mot' — att vedervåga är att "
     "våga något mot en risk.",
     etymologi="veder- betyder 'mot', som i vedergällning — att våga något "
               "mot en risk.")

lagg("huldra",
     "ETYMOLOGIN ÄR PERFEKT FÖR VÄSENDET. SO: 'ett mytologiskt kvinnligt "
     "(skogs)väsen med förmåga att utöva **farlig lockelse**' — faran är del "
     "av definitionen, vilket är lätt att tappa. Ursprunget: dansk-norska "
     "*huldre*, egentligen '**någon som döljer sig**', besläktat med "
     "**hölja**. Huldran är alltså 'hon som gömmer sig' — precis det ett "
     "skogsväsen gör.",
     huvudbetydelse="Kvinnligt skogsväsen i folktron som lockar till sig "
                    "människor — lockelsen är farlig",
     synonymer=["skogsrå", "skogsfru", "vittra"],
     etymologi="Norska huldre, 'någon som döljer sig' — släkt med hölja.")


if __name__ == "__main__":
    pl.bygg(P, MAL)
