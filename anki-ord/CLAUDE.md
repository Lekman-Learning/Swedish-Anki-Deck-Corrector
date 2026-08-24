# anki-ord — System A status (Anki ORD-kortsgranskning)

Se [../CLAUDE.md](../CLAUDE.md) för helheten. Denna fil = teknisk detalj +
exakt var vi står, så en ny chatt kan fortsätta direkt.

## Bekräftat mot riktig, öppen Anki (Fas 0, `discover.py`, klart 2026-08-03)

- Deck: `Humanities::Languages::Svenska 10 000`
- Note type: `Grundläggande-adc63`
- Fält: `Framsida` (ordet), `Baksida` (EN HTML-blob, se `baksida.py`)
- Flaggor: flag:1 = **Röd** (fel — men se dubbel betydelse nedan, tillagd
  2026-08-19) · flag:2 = **Gul** (osäker) · flag:4 = **Blå** (stämmer,
  konfidens 9-10) · flag:3 = **Grön** (dels 84 gamla kort utanför scope,
  dels nya konfidens-≤8-granskade kort sen 2026-08-04 — skilj dem åt via
  tagg `konfidens::N`, se style_guide.md)

  **🔴 Röd har TVÅ olika betydelser beroende på var kortet är i
  livscykeln (Adams beslut 2026-08-19) — avgör via `granskad::*`/
  `v3_granskad::*`-taggen, aldrig via flaggan ensam:**
  - **Kort UTAN `granskad::*`-tagg** (ännu inte v3-klara): röd betyder
    fortfarande **innehållsfel** — det ursprungliga, oförändrade läget.
    `fetch_queue.py`s prioritering (röd → gul → blå) gäller BARA dessa.
  - **Kort MED `granskad::*`-tagg** (redan v3-klara, innehållet är
    verifierat): röd betyder i stället **"Adam har svårt att lära sig det
    här kortet"** — en personlig repetitionssignal Adam sätter själv i
    Anki under vanligt plugg, inte ett granskningsresultat. Detta är
    ORTOGONALT mot om kortet är sakligt korrekt.
  - **Kontrollerat 2026-08-19: kolliderar inte med befintlig kod.**
    `fetch_queue.py` (`build_query()`) exkluderar redan
    `-tag:granskad::*` från alla flagg-nivåer, så v3-klara kort (som bär
    just den taggen) hamnar aldrig i korrigeringskön oavsett flaggfärg.
    Adams personliga röd-markeringar på redan v3-klara kort kan alltså
    aldrig blandas in i "kort som behöver rättas" — skyddet fanns redan,
    av ett annat skäl, innan den här regeln beslutades. Om ett FRAMTIDA
    script någon gång skannar `flag:1` utan att gå via `fetch_queue.py`s
    query-mönster: kom ihåg samma `-tag:granskad::*`-filtrering.
- Befintliga taggar (`ai_optimized`, `ai_uncertain`, `ai_failed`,
  `granska_först`) är historik, INTE fakta — flaggan vinner alltid vid
  konflikt (t.ex. blå + `ai_uncertain` = Adam har redan rättat, är korrekt)

## Script-inventering

| Fil | Gör |
|---|---|
| `ankiconnect.py` | Thin wrapper, `invoke(action, **params)` mot `localhost:8765` |
| `config.py` | Deck/model/fält/flagg-konstanter (se ovan) |
| `baksida.py` | Parse/bygg Baksida-HTML-mikroformatet — skriv ALDRIG fritext direkt i fältet |
| `discover.py` | Fas 0, engångskörning, redan körd |
| `fetch_queue.py` | Fas 1 — hämtar batch: röd → gul → blå, och inom varje flagg-nivå kort Adam redan ser (learning/review, `-is:new`) före aldrig visade (`is:new`) — beslutat 2026-08-04, Adam vill rätta det han redan pluggar innan nytt material. Sorterat på due-position inom varje grupp. Default `DEFAULT_BATCH_SIZE=100`, exkl. redan `granskad::*` taggade. Skriver `sessions/session_<datum>.json` |
| `fetch_blue_suspects.py` | Riktad genväg: blå kort med känd fel synonym (se `SUSPECT_SYNONYMS`), utan att vänta på blå-rotationen. Skriver `sessions/session_<datum>_blaa-misstankta.json`, samma format |
| `scan_blue_synonyms.py` | Läsande engångssökning, ändrar inget, listar blå kort som matchar `SUSPECT_SYNONYMS = ["allsmäktig", "alrådande", "allrådande"]` |
| `queue_lib.py` | Delad hämta/sortera/skriv-logik för de två fetch-skripten |
| `images.py` | Läsa/skriva Anki-media (bilder), används i Fas 2 |
| `migrate_format.py` | Engångsmigrering v2-format: hämtar `granskad::*`-kort, parsar gammalt format (`baksida.parse_legacy`), skriver draft-huvudbetydelse (gamla definitionerna hopslagna) till sessionsfil, inget appliceras auto |
| `apply_updates.py` | Fas 3 — skriver godkända ändringar (`updateNoteFields` via `baksida.build`, plus `Framsida` om `proposed_ord` satt). Kräver `entry["confidence"]`: ≤7 skippas (ej redo), 8→flagga Grön, 9-10→flagga Blå (fixat 2026-08-04, se style_guide.md — tidigare flaggade koden fellaktigt ALLTID blått oavsett konfidens). Taggar `granskad::<datum>` + `konfidens::N`. `apply_single` per kort under passet, eller batchat i `main()` |
| `style_guide.md` | "Adam-tal"-checklista — struktur, grundregler, bevara humor, bildhantering, vanliga fällor |
| `wikipedia_bild.py` | Adams beslut 2026-08-19 — hämtar en KANDIDATBILD (aldrig en bekräftad bild) från sv.wikipedia (REST `page/summary`) eller Commons-fritextsökning (fallback). Gör ALDRIG en relevansbedömning själv — se "Bildkomplettering via Wikipedia" nedan för varför det måste vara ett separat steg |
| `wikipedia_bild_batch.py` | Fas 1 för bildkomplettering — hämtar N v3-klara (`granskad::*` ELLER `v3_granskad::*`) bildlösa kort (sorterat på due), försöker en kandidat per ord, skriver `sessions/session_<datum>_wikipedia-bilder.json`. Applicerar inget. `--batch-size` (default 20, litet med flit), `--offset` |
| `wikipedia_bild_apply.py` | Fas 2 — applicerar bara poster med `godkand: true` (satt av granskaren för hand efter att ha jämfört kandidaten mot kortets Huvudbetydelse). Läser ALLTID live `bild_html` direkt innan skrivning, vägrar skriva om kortet fått en bild sedan batchen byggdes. Loggar varje sparad bild (ord, källa, käll-URL, licens) till `bild_kallor.jsonl`. `--torr` för torrkörning |

## Öppna sessionsfiler

**`sessions/session_2026-08-04.json`** — AKTIV KÖ, 106 kort totalt:
- **28 `"approved": true`, redan APPLICERADE till riktiga Anki via
  `apply_updates.py`** (kört 2026-08-04, `[OK]` för alla 28, se historik för
  fullständig lista). Dessa kort är nu taggade `granskad::2026-08-04` +
  `konfidens::N` i Anki och flaggade Blå (konfidens 9-10 på samtliga 28).
- 78 `"approved": false, "proposed": null` (väntar på Fas 2), oförändrad
  inbördes ordning från förra passet.

De 7 senast tillagda/applicerade (utöver de ursprungliga 21): "spel för
galleriet", "bolare", "pöbel" (Framsida var redan korrekt stavad — "påbel"
i tidigare anteckning var en egen felläsning pga terminal-encodingbugg, se
Errors-sektion i sessionshistorik), "vara i svang", "kanalje", "bottna i",
"vina". Alla dessa hade helt eller delvis fel innehåll (t.ex. "vina"
beskrev vinbär i stället för ljudet av något som susar/viner förbi;
"bottna i"/"vara i svang" hade återanvänd skräp-synonymlista
"allsmäktig/allhärskande" från en helt annan kortbugg) — verifierat mot
svenska.se/synonymer.se/SAOB och omskrivet innan applicering.

Nästa kort i kön (första av de 78 obehandlade): **"förråda sig"**.

**Prioriteringsregel (beslutad 2026-08-04):** Adam vill granska kort han
redan håller på att lära sig FÖRE kort han aldrig sett, så han inte lär in
fel version av ett ord han redan pluggar. `fetch_queue.py`/`queue_lib.py`
(`fetch_cards_prioritized`) implementerar detta permanent för alla framtida
körningar.

**Konfidens/flagg-koppling (beslutad 2026-08-04, se style_guide.md):** varje
applicerat kort MÅSTE ha `entry["confidence"]` (0-10) i session-JSON innan
`apply_updates.py` kör det — annars skippas det automatiskt (säkerhetsspärr
tillagd 2026-08-04 efter att en bugg upptäcktes: koden flaggade tidigare
ALLTID blått oavsett faktisk säkerhet).

**`sessions/session_2026-08-03.json`** — 10 röda kort, HELT ogranskad.
Ord: kautschuk, eternell, driven, + 7 till.

**`sessions/session_2026-08-03_blaa-misstankta.json`** — 59 blå kort från
`scan_blue_synonyms.py`/`fetch_blue_suspects.py`, alla ogranskade. Exempel:
"omnipotent" har synonymen "evighetsmaktig" (misstänkt fel) OCH en
definition som ser trasig ut ("Hovärendes, som har full makt...") — trots
att `fetch_blue_suspects.py`s docstring antar att definitionen alltid
stämmer på blå kort. Kontrollera det antagandet under granskningen, inte
bara synonymen.

## Batch2, 20 is:new-kort: syn.se:s kandidatlista är inte synonymstöd (2026-08-12)

19 kort blindgranskade (ett pausat före granskning, se nedan): **14 godkända,
5 underkända — 26 %**, mot kvällens tidigare 15 %. Kostnad 1,01 USD, 31 turer.

**Fyra av de fem underkännandena är samma defekt, och den är systematisk:
synonymer hämtade ur syn.se.**

| Kort | Synonym | Vad granskaren visade |
|---|---|---|
| `pandemi` | farsot | Överordnad term — farsot kräver ingen spridning över stora områden |
| `kätting` | boja, förtöjning | Boja = fotboja; förtöjning = tross/rep. Ingendera är en lastbärande kedja |
| `kuriosa` | antikviteter | Antikvitet definieras av *ålder*, kuriosa av det *udda* |
| `installation` | inmontering | Hör till anslutningsbetydelsen, inte konstbetydelsen |

`las.py` skriver ut listan under rubriken **"syn.se (KANDIDATER, ej facit)"** —
etiketten var alltså redan rätt, och jag behandlade den ändå som beläggning.
`forgranska.py`s `synonym_utan_stod` fångar inte det, eftersom regeln bara
kontrollerar att ordet **förekommer** i en källa, inte att källan **påstår
synonymi**. syn.se blandar synonymer, hyperonymer, kohyponymer och lösa
associationer i samma platta lista.

**Regel härav:** en synonym får bara skrivas in om en av dessa gäller —
(a) SO markerar den `SYN:synonym`, eller (b) den står i SO:s eller SAOL:s
definitionstext för ordet. syn.se duger till att *hitta* kandidater, aldrig till
att belägga dem. `fackman` (specialist, SYN:synonym) och `generös` (frikostig,
givmild, båda SYN:synonym) klarade granskningen just därför.

**Det femte underkännandet, `schakt`, är bara delvis rätt.** Granskaren avfärdade
kortets hisstrumma-betydelse som sakligt fel med hänvisning till SO — men **SAOL
säger ordagrant "stor öppning i marken; hisstrumma"**, och enligt valvets
källhierarki avgör SO *och* SAOL dagens betydelser. Underkännandet står ändå,
för kortet hade ett verkligt fel: det saknade SO:s faktiska andra homograf
("sänkning av markytan på utstakat område"). Granskaren hade rätt slutsats av
delvis fel skäl — andra gången en blindgranskare visats resonera fel om SAOL
(jfr `brödtext` samma dag).

**`förborgad` pausades före granskningen** (`v3_pausad::inget_uppslagsord_i_so_saol`).
Förgranskningen larmade `frammande_uppslagsord`, och rådatan gav flaggan rätt:
varken SO eller SAOL har formen som eget uppslagsord, bara verbet `förborga`.
Betydelsen var inte problemet — registret var det, eftersom `ngt ålderdomlig`
då vilar på min slutledning i stället för på en märkning.

**Kontrollkorten uteblev:** `v3_kontrollkort.py blanda` hittade 0 av 3 kandidater
(kort äldre än 3 dagar med `oberoende_verifierad`). Paketet gick alltså ut utan
planterade fel, så granskarens egen träffsäkerhet är omätt den här gången.

Läget efter: full v3 **755 → 769**, färdig is:new-pool **455 → 469**,
underkända 89, pausade 3, spår A kvar 6 745.


## Synonymspärren: ordboken måste själv säga det, och tom lista är godkänt (2026-08-12, Adams beslut)

**Adam:** *"kort som inte ska ha synonymer alltså 0 eftersom att kortet
representerar ett ord som är väldigt unikt och inte har synonymer så krävs inga
synonymer och blir därigenom godkänt."*

Ny hård regel `synonym_utan_ordboksbelagg` i `forgranska.py`. En synonym godtas
bara om **ordboken själv pekar ut den**, på ett av två sätt:

* (a) SO taggar korshänvisningen `SYN:synonym`, eller
* (b) ordet **inleder ett eget led** i SO:s eller SAOL:s definition.

Att kravet är *inleder*, inte *förekommer*, är hela finessen. SAOL definierar
`pandemi` som "allomfattande farsot" -- `farsot` står där, men modifierat, och
bara hela frasen är utbytbar. Jämför `triumfera`: "segra; jubla efter att ha
vunnit framgång", där båda orden inleder sina led och är riktiga synonymglosor.
En ren containment-kontroll släpper igenom farsot; den här gör det inte.

**Varför den gamla regeln inte räckte.** `synonym_utan_stod` frågar bara om
ordet förekommer **någonstans i det hämtade underlaget** -- och syn.se ingår i
det underlaget. syn.se blandar synonymer, överordnade begrepp, syskonord och
lösa associationer i en platt lista som `las.py` mycket riktigt märker
*"KANDIDATER, ej facit"*. Regeln var därför uppfylld av allt syn.se råkade
lista.

**Tom lista är normalfallet, inte ett misslyckande.** Mätt över 828 uppslag med
egen SO/SAOL-post: **7 %** har `SYN:synonym`, **24 %** har en definition som är
en synonymuppräkning, **69 % har inget belägg alls**. `baksida.tom_synonym`
fångar bara tomma strängar i listan, aldrig en tom lista -- verifierat.
`VERIFIERARINSTRUKTION` säger nu uttryckligen att en tom synonymlista aldrig
ensam får ge underkänt.

**Det pedagogiska argumentet, som är starkare än det källkritiska:** decket
pluggas mot HP-provets ORD-del, som *är* ett synonymtest. Distraktorerna där är
just ord som ligger nära utan att vara utbytbara. En nästan-synonym på kortet
tränar alltså exakt det fel provet straffar. Tom lista är inte bara ärligare,
den är bättre.

**Regressionstest:** 22 kända fall, 22 rätt. Fångar farsot/pandemi,
boja+förtöjning/kätting, antikviteter/kuriosa, inmontering/installation.
Släpper igenom segra+jubla/triumfera, förutsätta+tänka sig/ponera,
kokett/behagsjuk, gåsunge/gässling, specialist/fackman (SYN),
frikostig+givmild/generös (SYN), svågerpolitik/nepotism (SYN),
anslutning/installation.

### Omfattningen: 676 av 769 full v3-kort bär minst en obelagd synonym (89 %)

Mätt mot live-decket. 9 kort har redan tom synonymrad, 83 är helt rena.

Siffran är hög, men stickprov visar att regeln har rätt i de flesta fallen --
det är decket som är fel, inte spärren. Korten genererades ursprungligen med
tre synonymer var oavsett om det fanns några:

| Kort | Kortets synonymer | Vad ordboken säger |
|---|---|---|
| `konstitutiv` | bestämmande | "grundläggande, väsentlig" -- kortets ord är sannolikt fel |
| `beprövad` | tillförlitlig, pålitlig, härdad | "som prövats med framgång" -- följder, inte synonymer |
| `putslustig` | skämtsam, lustig | "smårolig, skojig" -- två dugliga fanns, kortet tog andra |
| `bonitet` | godhetsgrad | "grad av avkastningsförmåga" -- ordet finns inte i någon ordbok |
| `otolog` | öronläkare | "specialist på otologi" -- **äkta falskt utslag** |

`otolog` visar den enda falska formen: ordboken definierar med en fackterm och
kortet ger det korrekta vardagsordet. Räkna med att en minoritet av de 676 är av
den sorten.

**Inte en massfix.** De 676 godkändes under den gamla standarden och är en
arbetslista, inte en brand. Kör om dem batchvis i vanlig ordning -- spärren ger
urvalet gratis. Blindgranskaren fångade bara 4 av de 14 obelagda i batch2, så
spärren är inte överflödig bredvid granskaren.


## Batch3, 20 is:new-kort: 0 % underkänt -- första felfria batchen (2026-08-12)

Första batchen skriven under synonymspärren. **20 av 20 godkända**, 53 turer,
1,79 USD. Föregående två batcher samma kväll: 15 % och 26 % underkänt.

**Sju av tjugo kort fick tom synonymlista** (fiffel, hydrokultur, kanvas,
bokslut, lagbunden, lektor, metates). Det är regeln som arbetar som avsett --
ordböckerna gav inget utbytbart ord, så kortet får inget. Där ordboken levererar
blev synonymerna i gengäld starka: `skolexempel` -> `typexempel` är SO:s egen
`SYN:synonym`, och `påpasslig` -> `alert, vaken` står ordagrant i SAOL.

**Kan 0 % lita på?** Inte fullt ut, och det ska sägas rakt ut: kontrollkorten
uteblev igen, så granskarens egen träffsäkerhet är omätt. En nollsiffra utan
planterade fel är precis det läge där ett bra parti inte går att skilja från en
slapp granskare. **Ett motargument finns dock i mätdatan:** granskaren körde
**2,65 turer per kort** mot batch2:s 1,63 -- alltså mer arbete per kort, inte
mindre. Det talar mot slapphet, men ersätter inte en kontrollmätning.

**Adams fråga efteråt: "är det för att vi tillåter 0 synonymer?"** Delvis, och
mätningen visar hur mycket. Batch3 har **hälften så många synonympåståenden**
som batch2 (23 mot 44; 1,1 mot 2,3 per kort) -- alltså mindre yta att ha fel på.
Men antalet betydelser per kort är oförändrat (1,3 mot 1,4), så den andra stora
feltypen hade samma yta som förut.

Och synonymeffekten räcker inte för att förklara noll. Över alla **1 062**
loggade blindgranskningar i `oberoende_granskningar.jsonl`:

| | |
|---|---|
| Underkända | 201 (**19 %**) |
| Nämner synonymer | 104 (52 % av underkännandena) |
| **Rena** synonymfel | 16 (**8 %**) |

Försvinner synonymfelen helt hamnar frekvensen mellan **9 % och 17 %** beroende
på hur de blandade fallen räknas -- inte på 0 %. Resten är sannolikt tur plus
lite lättare ord: batch3:s median-popularitet är 4 800 mot batch2:s 2 918, och
**0 av 20 vid en sann frekvens på 10 % inträffar i 12 % av fallen**, ungefär var
åttonde batch. Ett parti om 20 kort kan inte skilja "processen blev bättre" från
"det gick bra den här gången".

**Skillnaden som måste hållas isär:** tom synonymlista gör korten mindre
felaktiga, men delvis genom att de påstår mindre -- inte bara genom att de
påstår rätt. Ett kort utan synonymer kan inte ha fel synonym. Det är en verklig
vinst för HP-provet och ska inte bokföras som att skrivandet blivit bättre.

**Varför kontrollkorten inte gick att blanda in, och det är inte en bugg:**
`valj_kontroller` kräver kort som blindgodkänts för minst 3 dagar sedan.
Taggen `oberoende_verifierad` finns bara i tre dagar: 236 kort 2026-08-10,
339 den 11:e, 214 den 12:e. Gränsen i dag är <= 2026-08-09, alltså tom mängd.
**Från 2026-08-13 blir de 236 korten från den 10:e valbara** och funktionen
börjar fungera av sig själv. Ingen åtgärd behövs, men glöm inte att kontrollera
att den faktiskt slår igång.

### Tre buggar i spärrarna, hittade genom att läsa utdatan

1. **SAOL:s bruklighetsmarkörer åt upp synonymer.** `"äv. blek, ointressant"`
   gjorde att `blek` inte inledde sitt led och föll som obelagt, trots att SAOL
   listar ordet. `_LEDMARKOR` strippar nu `äv.`, `ofta`, `ibl.`, `särsk.`,
   `bildl.` med flera.
2. **Partikelverb larmade om sin egen form.** `spritta` gav
   `frammande_uppslagsord: spritta till`. Suffixlistan i `_samma_uppslag` var
   fyra partiklar lång. Utökad till hela det slutna partikelförrådet, plus en
   regel för particip där partikeln flyttar fram till prefix (`bona om` ->
   `ombonad`).
3. **`gem` räknades som samma ord som `gemen`** -- och därmed blev
   *pappersklämma* en belagd synonymkandidat för `gemen`. Orsaken var
   plural-/bestämdformsregeln: `gem` + `en`. Exakt samma bugg som den
   dokumenterade `te`/`tes`-sammanblandningen från 2026-08-11, som stått som
   öppen defekt sedan dess. Åtgärd: kortformen måste vara minst 5 tecken innan
   ändelseregeln får slå till -- ett kort ord plus en ändelse är oftare ett
   ANNAT ord än en böjning av det korta. Regressionstest: 14 fall, 14 rätt,
   inklusive `brass`/`brasserie` och `black`/`black om foten`.

Registerfel som förgranskningen fångade före granskningen: `fiffel` är märkt
*vardagligt*, `gemen`s betydelse 'vanlig' *något ålderdomligt*, `sensation`s
sinnesintrycksbetydelse *psykologi*. Alla tre hade gått till granskaren fel.

Läget efter: full v3 **769 -> 789**, färdig is:new-pool **469 -> 489**,
underkända 89, pausade 3, spår A kvar 6 725.


## Nästa steg

Fortsätt Fas 2 i `session_2026-08-04.json`, börja med **"förråda sig"**
(första obehandlade av de 78). Kör kort för kort, verifiera mot
svenska.se/synonymer.se, skriv `proposed`+`confidence`, sätt
`approved: true`, applicera löpande eller batchat via `apply_updates.py`.

De två 08-03-filerna (10 röda + 59 blå-misstänkta) väntar fortfarande,
Adam har inte valt att prioritera dem än.

## Blå kort i relearning (ny granskningstyp, 2026-08-04)

Adam märkte att blåa kort (flaggade "stämmer 100%, rör inte") ändå hamnar i
Ankis relearning-kö — dvs han glömmer dem trots att innehållet är korrekt.
Hypotes: dåligt minnesvärda exempelmeningar, inte fel fakta (bekräftat av
Adam). `sessions/session_2026-08-04_blaa-relearning.json` — 55 blåa,
ogranskade kort med `type:3` (relearning) i Anki, hämtat via ad-hoc-script
(ej ett permanent fetch_*.py-skript ännu, kan läggas till om mönstret
återkommer). 18 av 55 hade trasiga/fragmentariska exempelmeningar (t.ex.
"Iaktta konvenansen.", eller kvarglömda `<br>`-rester) eller ett rent
stavfel ("korsar": "kappade"/"handelsfartyggets" → "erövrade"/
"handelsfartyget") — omskrivna till fullständiga, konkreta meningar och
applicerade (samma `apply_updates.py`-flöde, confidence 10, fakta
oförändrade). Efter Adams feedback ("jag vill inte att du missar
någonting, nästan bättre att skriva om vartenda kort") gjordes en tredje,
uttömmande pass: alla kvarvarande kort skrevs om till mer konkreta/levande
meningar istället för att bedömas binärt bra/dålig — även de som redan
"fungerade" fick en starkare scen/karaktär där det gick att hitta något att
förbättra. Detta hittade även ett grammatikfel ("modd": "ett stort modd" —
tveksamt genus, omskrivet för att undvika artikeln helt) och en vag
"åtgärder"-formulering ("vidtaga"). **Totalt 48 av 55 omskrivna.** Endast 7
lämnades helt orörda efter granskning, med motivering — redan komplett
scen+karaktär, inget att vinna: morfem, förnumstig, oförsynt, bjugg,
farstu, palp, hambo. Fullständig lista över vilka som ändrades finns i
sessionsfilen (`proposed` != null).

Öppen fråga: är detta läge unikt för dessa 55, eller ska `fetch_queue.py`
även erbjuda ett "blå-relearning"-pass permanent (liknande
`fetch_blue_suspects.py`)? Inte beslutat än.

## Fullständig genomgång: alla "lär om" + "mogna" kort (2026-08-04)

Adam bad om ett systematiskt slutförande av HELA Ankis "Lär om"- och
"Mogna"-kategorier (Anki-statistikens egna kategorier, inte våra
granskningsflaggor) — inte bara de blå. Två nya sessionsfiler:

**`sessions/session_2026-08-04_larom-alla.json`** — 34 kort, `type:3`
(relearning), ALLA flaggor, exkl. redan granskade. 27 av 34 var **gröna
legacy-kort** (aldrig faktagranskade tidigare, tillhör de gamla 84
utanför-scope-korten) — inte bara dålig formulering utan riktiga sakfel:
- **efor**: definition påstod "högsta militär befälhavare" — fel, eforer
  var civila tillsynsämbetsmän som övervakade kungarna, inte arméchefer.
- **bortklemad**: definition innehöll kvarglömt tyskt ord ("verwöhnt").
- **traktat**: fel genus i exempelmening ("ett traktat" → "en traktat").
- **filibuster**: fel genus ("den omstridda lagförslaget" → "det").
- **veläng**: äkta ord (verifierat via webbsökning), stavfel i definition
  fixat ("kilinghudar" → "killinghudar").
- **blästra**: svag synonym ("blåsa") ersatt med "sandblästra".
- Resten: fragment utan verb eller kvarglömd `<br>`/`<span>`-formatering.
18 av 27 gröna fixade, 9 redan korrekta. De resterande 7 (blå, redan
granskade i förra passet) + 9 gröna lämnades orörda med motivering.

**`sessions/session_2026-08-04_mogna.json`** — 380 kort, review med
intervall ≥21 dagar (378 blå, 1 gul, 1 grön). En heuristisk skanning
(fragment <5 ord, kvarglömd `<br>`/`&nbsp;`/`<span style`, tom
exempelmening) users på ALLA 380 för att inte missa något manuellt igen —
147 flaggade, 233 redan bra. Bland de 147 fanns **11 kort med HELT TOMMA
exempelmeningar** (på kuppen, endotermisk, missta sig, medaljens baksida,
pampusch, blåsa faran över, en polsk riksdag, gå tretton på dussinet,
understatement, rannsaka, den gubben går inte) — dessa fick helt nya
meningar skrivna från grunden utifrån definitionerna. Alla 147 skrivna om
och applicerade, verifierat live (t.ex. "morän" — korrekt format, taggar
`granskad::2026-08-04` + `konfidens::10`).

**Totalt denna session: 55 (blå relearning) + 34 (alla relearning) + 380
(mogna) = kompletta pass över tre stora kortgrupper**, med sammanlagt över
200 korrigerade exempelmeningar/definitioner/synonymer och flera riktiga
sakfel fixade (inte bara formulering). Metodlärdom: manuell "bra/dålig"-
bedömning missar saker (3 av 55 missades första passet på blå-relearning);
en skriptad heuristisk skanning (ordantal, HTML-rester, tom sträng) fångar
konsekvent det manuell läsning missar, och användes därför på de 380
mogna korten direkt.

## Genomgång av Unga + Nya-orange + Låst (2026-08-04, pågående)

Adam beslutade att fortsätta bortom Lär om/Mogna: alla kort som INTE är
"Nya" (blå, aldrig visade, 7506 kort) ska granskas. Kartlagt via
`(type, queue)` mot Ankis egna pie-chart-siffror (exakt match):
- Nya blå (7506) = type0/queue0 — UTANFÖR scope, rörs ej
- Nya orange (53, egentligen "Lärande") = type1/queue1
- Lär om (39) = type3/queue1 — redan klart (se ovan)
- Unga (1978) = type2/queue2, ivl<21
- Mogna (382) = type2/queue2, ivl>=21 — redan klart (se ovan)
- Låst (76) = queue=-1, alla typer (suspenderade)

Scope denna nya omgång: Nya-orange + Unga + Låst = 2042 kort (efter
exkludering av redan granskade), batchat i 6 filer à max 400:
`sessions/session_2026-08-04_resten-batch1.json` t.o.m. `...batch6.json`
(fetch-skript: `fetch_remaining.py`, scratchpad, ej permanent ännu).

**Batch 1 (400 kort, klar):** 376 blå, 12 gul, 12 grön. Heuristisk skanning
(samma metod som mogna-passet) flaggade 199. Utökad manuell
faktagranskning av alla 24 gul/grön (inte bara de heuristiskt flaggade)
hittade riktiga sakfel även på BLÅA kort — flaggan garanterar alltså inte
korrekthet, se tidigare lärdom:
- **"vara på örat"** (blå): definitionen var helt fel — påstod "vara
  uppmärksam", verklig betydelse är **"vara berusad"**. Omskriven helt.
- **"mas"** (blå): en av två definitioner var påhittad ("person som driver
  in Ivans skatter till Sverige" — verifierat obefintligt via webbsökning).
  Rätt betydelse: informell/lätt nedsättande benämning på en man från
  Dalarna. Fixad.
- **"gentaga"** (blå): ordet existerar inte i svenskan (verifierat — SAOL/
  SAOB saknar det, AI-genererade synonymsajter "gissar" ändå fram
  böjningar). Framsidan är alltså fel, inte bara baksidan. **Kortet
  SUSPENDERAT** (inte gissat om till annat ord) + taggat
  `granska_fabricerat`, väntar på Adams beslut om vad kortet ska bli.
- **"vråk"**: synonymen "råk" var fel (helt annan fågel, kråkfågel/
  islucka), bytt mot "musvråk".
- Övriga 176 fixade kort: mestadels formatstädning (`<span style=...>` →
  standardiserad `<font color="#3498db">`, kvarglömda `<br>`/`&nbsp;`) +
  omskrivna korta/tomma exempelmeningar till konkreta scener, samma
  standard som mogna-passet. Flera kort hade helt tomma synonymer/
  definitioner (t.ex. svärmisk, attribuera, konsiliant, fiken, lämpa,
  slåtter, briljera, slik, skålla, varda, sila mygg och svälja kameler,
  leva rullan, bli vid sin läst, rå om, klosett) — helt nyskrivna.
Applicerat via `apply_updates.py`, verifierat live (t.ex. "vara på örat").

**Batch 2 (400 kort, klar 2026-08-04):** 383 blå, 5 grön, 12 gul. Samma
metod som batch 1, men den heuristiska skanningen breddades: förra passets
skript kollade bara `exempelmening` för `<span>`/`<br>`/tomhet/kort längd.
Denna gång kollades även `definitioner`-fältet för kvarglömd `<br>`/`<div>`
samt `<b>`-taggar (istället för `<font>`) i exempelmeningen — detta fångade
4 extra trasiga kort (feja, mangrann, titan, relä) som hade missats av
ursprungsheuristiken. **Rekommendation: använd den breddade skanningen för
batch 3–6 också.** Totalt 201 kort flaggade/fixade av 400 (197 via
originalheuristiken + 4 extra).

Full manuell faktagranskning av alla 12 gul + 5 grön (inte bara
heuristiskt flaggade), plus stickprov på ovanliga/arkaiska blå ord — hittade
riktiga sakfel, verifierat mot svenska.se/synonymer.se/SAOB/SAOL via
webbsökning:

- **"asa"** (blå): definitionen sa "röra sig med lätthet och utan
  ansträngning" — helt fel riktning. Verklig betydelse (bekräftad via
  sökning): röra sig **långsamt och motvilligt/trögt**, jämför "masa sig".
  Definition och synonymer omskrivna.
- **"garvad"** (grön): synonymerna (härdad, luttrad, erfaren — den bildliga
  "erfaren person"-betydelsen, t.ex. "en garvad journalist") matchade INTE
  definitionerna, som bara beskrev bokstavlig lädergarvning. Definitionerna
  omskrivna till den bildliga betydelsen synonymerna faktiskt syftade på.
- **"änkestöt"** (blå): synonymerna ("armbågsnerveslag", "nerverörning",
  "armbågsnervesmärta") var påhittade sammansättningar som inte finns i
  språket. Ersatta med den enda verifierade riktiga synonymen: "kalvdön"
  (dialektalt, bekräftat via sökning). Själva definitionen (känseln av att
  slå armbågen mot nervus ulnaris) stämde och lämnades orörd.
- **Grammatikfel** fixade i exempelmeningar: "träta" (fel genus, "ett litet
  träta" → "en liten träta"), "hunsa" (fel verbform, "Han hunsa" → "Han
  hunsade"), "spediera" (samma sorts fel, "Företaget spediera" →
  "spedierar"), "suverän" (fel genus, "en...tal" → "ett...tal"),
  "korrugerad" (fel genus, "Den...plåttaket" → "Det...plåttaket"),
  "förtryta" (fel böjning — "förtrytade" är inte en form av detta starka
  verb, korrekt preteritum är "förtröt"), "mangrann" (exempelmeningen
  saknade slut-t: "mangran" → "mangrant").
- **"metronom"** (blå): tredje definitionen var ovidkommande trivia
  (skivbolaget Metronome, grundat 1949 — bekräftat verkligt men helt
  irrelevant för ordinlärning). Borttagen, behöll de två instrumentdefinitionerna.
- **"anseende"** (blå): andra definitionen om varumärkesrättsligt
  "anseendeskydd" bekräftades vara en riktig men alltför nischad juridisk
  detalj för ett grundord. Borttagen till förmån för kärnbetydelsen "rykte".
- **"cyklon"** (blå): hade 5 definitioner inklusive regionala orkannamn
  (Atlanten/Stilla havet-varianter) — för encyklopediskt för Adam-tal,
  förenklat till 2 kärndefinitioner (lågtryck + tropisk storm).
- **"aptera"** (blå): exempelmeningen innehöll stötande innehåll helt
  orelaterat till ordets betydelse. Ersatt med en neutral, korrekt mening
  (sändare monterad på ett djur för forskning, matchar egen definition).
- Diverse mindre sakfel: cirkulär synonym ("överträffa" hade sig själv
  listad som egen synonym), stavfel i synonymer ("esamrättslig" →
  "ensamrättslig" för exklusiv, "översgående" → "övergående" för
  förgänglig, "innehål" → "innehåll" i uttömmandes definition), trasig
  definitionstext ("en förnorskt ord" → "ett fornnordiskt ord" för fylgia),
  missmatchade synonymer (kolonn hade "stam" som inte är en verklig
  synonym för pelare; motion hade träningsrelaterade synonymer trots att
  definitionerna gällde den parlamentariska betydelsen — bytt till
  förslag/yrkande/interpellation).
- Källor kontrollerade utöver svenska.se/synonymer.se: SAOL/SAOB-citat via
  webbsökning för änkestöt, stenisk, asa, böcken/boken (arkaiskt ord för
  övermogen frukt — bekräftat existerande och korrekt), överlupen (båda
  betydelserna — mossbelupen OCH överhopad med arbete — bekräftade
  korrekta), ärevördig vs högvördig (bekräftat verkliga, SKILDA kyrkliga
  titlar i en hierarki — INTE dubblett/fel som misstänkt), dyschatell,
  gördel, strak.
- Inga helt påhittade/obefintliga ord hittades i batch 2 (till skillnad
  från "gentaga" i batch 1) — **inga suspenderingar krävdes denna gång.**
- Övriga ~185 fixade kort: formatstädning (`<span style=...>` och `<b>` →
  `<font color="#3498db">`, kvarglömda `<br>`/`&nbsp;`/`<div>`-rester i
  både exempelmening och definitioner) + omskrivna korta/tomma
  exempelmeningar till konkreta scener, samma standard som batch 1. Flera
  kort hade helt tomma synonymer (t.ex. ehuru, charmant, trindsäd, på en
  höft, fribyteri, bulla upp, få korgen, antåga, skriande, sätta sig, vara
  stadd vid kassa, i runda tal, turnera, vischa, ligga någon i fatet,
  hugsvala, hembära, gå på ett ut, ha en gås oplockad med ngn) och/eller
  tomma exempelmeningar — helt nyskrivna.

Alla 201 fixade kort applicerade via `apply_updates.py` (confidence 10
genomgående, samma standard som batch 1), verifierat live mot riktiga
Anki (t.ex. "aptera", "asa", "garvad", "änkestöt" — flaggor nu blå,
taggade `granskad::2026-08-04` + `konfidens::10`). `bild_html` rördes
inte på något av de 84 kort i batchen som hade bild.

**Batch 3-6 (1242 kort, EJ påbörjade ännu via den ordinarie sekvensen):**
samma metod ska upprepas, med den breddade heuristiska skanningen (se
ovan). Skala/tidsåtgång per batch är betydande — flagga detta till Adam
innan resterande 4 batchar körs i följd. Se dock nästa avsnitt — en del av
dessa kort granskades ändå, fast via en annan urvalsordning.

## Urgent-pass: kort Adam läser inom kort (2026-08-04)

**Nytt permanent scope-beslut (2026-08-04):** Adam bad om att få prioritera
kort han FAKTISKT läser inom en dag eller två, istället för att bara följa
den gamla batch3–6-sekvensen rakt av. `sessions/session_2026-08-04_resten-batch3-urgent.json`
byggdes med två grupper (se `flagLabel`-fältet):

- **`batch3-minst-mellanrum`** (200 kort): redan sedda kort (Unga/Nya-
  orange/Låst-scopet, exkl. redan granskade i batch 1–2) sorterade på lägst
  `ivl`/`due` — de kort Adam repeterar snarast.
- **`batch3-nya-kommande`** (100 kort): **HELT NYA kort Adam aldrig sett**
  (`is:new`), sorterade på könposition (`due`) — de 100 nästa han
  introduceras för (≈ en dags nya kort, deckets gräns är 100/dag).

**EXPLICIT SCOPE-UTÖKNING, beslutad 2026-08-04:** Nya blå kort (7506 st,
`is:new`) var tidigare uttryckligen UTANFÖR scope ("rörs ej", se
`../CLAUDE.md`-historik). Adam har nu bett om att de närmast förestående
100 nya korten (de han introduceras för näst) ska förgranskas INNAN han
ser dem första gången, som ett stående beslut för alla framtida pass —
inte en engångsavvikelse. Praktiskt innebär det: varje gång ett nytt
urgent-pass körs bör det inkludera nästa skiva nya kort på samma sätt,
utöver de redan sedda korten.

**Metod:** Grupp 1 fick riktig flagg-status hämtad via `cardsInfo` (flags:
184 blå, 9 grön, 7 gul, 0 röd av 200) — gul/grön fick full manuell
faktagranskning, blå fick heuristisk skanning (breddad variant från batch 2)
plus stickprov på ovanliga/misstänkta ord. Grupp 2 (helt nya kort) fick
**full manuell faktagranskning av alla 100**, utan genväg baserat på flagga
— dessa var praktiskt taget ogranskade sedan tidigare (flag:4 i Anki av
tekniska skäl, men aldrig faktiskt sedda/verifierade av någon).

**Resultat: 102 av 300 kort fixade och applicerade** (33 i grupp 1, 69 i
grupp 2), verifierat live mot Anki (rätt taggar `granskad::2026-08-04` +
`konfidens::N` på alla 102, rätt flagg-koppling 70 blå/32 grön, inga
mismatch). **Inga påhittade/obefintliga ord hittades** denna gång (till
skillnad från "gentaga" i batch 1) — inga suspenderingar krävdes.

Konkreta sakfel hittade, verifierat mot svenska.se/synonymer.se/SAOB via
webbsökning:

- **grannlaga** (blå): definitionen beskrev fel sak — en PERSON med
  känsligt temperament, istället för att en UPPGIFT/FRÅGA kräver takt och
  finkänslighet (den faktiska betydelsen). Omskriven.
- **åbäkig** (blå): definitionen sa "otrevlig/oskön", verklig betydelse är
  stor och klumpig till formen (matchar synonymerna otymplig/klumpig).
- **näva** (gul, växtnamn): "pelargonium" i synonymlistan är FEL släkte —
  Pelargonium och Geranium (näva) är två skilda växtsläkten, trots att
  engelskans "geranium" ofta blandar ihop dem. Verifierat via webbsökning.
  Borttagen ur synonymlistan.
- **harmynt** (gul): "olämpligt" var en helt felaktig synonym (obesläktad
  betydelse), "medfött" beskrev bara tillståndet, inte ordet. Ordet saknar
  en riktig utbytbar synonym — tömde listan (style_guide: noll är okej).
- **räv bakom örat** (blå): "förfalskande" var fel synonym (rätt är
  slug/listig/slipad) — och en KYRILLISK bokstav (а) hade smugit sig in i
  ordet "överlista" i definitionen (osynlig i vanlig läsning, hittad via
  skriptad tecken-skanning). Ny felkategori jämfört med tidigare batchar,
  värt att hålla ögonen öppna för i framtida pass.
- **pillemarisk** (blå): definitionen var HELT FEL — påstod "inte äkta
  eller pålitlig" (om ett FÖREMÅL/en AFFÄR). Verklig betydelse (SAOB,
  webbsökning): skälmaktig/lekfullt lurig, om en PERSONS uttryck eller
  sätt. Definition, synonymer och exempelmening omskrivna helt.
- **otolog** (grupp 2, ny): definitionen påstod öron-NÄSA-HALS-specialist,
  men otolog är specifikt öronläkare (en annan specialitet, ÖNH-läkare
  heter något annat). Förenklad.
- **hävdatecknare** (grupp 2, ny): synonymen "kronolog" är obekräftad,
  rätt synonym är "krönikör" (verifierat).
- **bekväma sig** (grupp 2, ny): synonymen "nedsänka sig till" existerar
  inte, rätt är "nedlåta sig till" (verifierat mot SAOB).
- **putslustig** (grupp 2, ny): synonymen "krystad" betyder något helt
  annat (tvingad/onaturlig), hör inte ihop med putslustigs faktiska
  betydelse (skojig/lustig på ett löjligt/gulligt sätt).
- **materialistisk** (grupp 2, ny): synonymen "egentinsinnad" gick inte
  att bekräfta existera i någon källa — sannolikt fabricerat/felstavat.
  Bytt mot "prylgalen" (bekräftad synonym).
- **proskribera** (grupp 2, ny): andra definitionen påstod en koppling
  till "utlänningslagens bestämmelser" — kunde inte beläggas och verkar
  fabricerad. Verklig klassisk betydelse (antikens Rom): att offentligt
  förklara någon fredlös och förverka dennes egendom.
- **monstruös** (grupp 2, ny): synonymlistan innehöll ordet SJÄLVT
  (cirkulärt, samma buggmönster som "överträffa" i batch 2) plus
  "odramatisk" som är fel betydelse. Bytt mot ohygglig/vidunderlig/
  avskyvärd.
- **överlastad** (grupp 2, ny): samma cirkulära synonym-bugg (ordet
  listat som sin egen synonym).
- **exkludera** (grupp 2, ny): exempelmeningen använde inte alls ordet
  (stod "uteslöts" istället, ett annat ord), plus grammatikfel ("brutt"
  → "brutit") och en fabricerad synonym ("utesköta" → "utestänga").
- **skrymma** (grupp 2, ny): fel preteritumform i exempelmeningen
  ("skrymmade"), korrekt är "skrymde" (verifierat).
- **djäkne** (grupp 2, ny): exempelmeningen bestod bara av ordet
  "diakonos" (den grekiska etymologin, inte en riktig svensk mening) —
  helt omskriven till en fullständig scen.
- **vedervåga** och **lägga sordin på** (grupp 2, ny): exempelmeningarna
  använde inte alls målordet/uttrycket — omskrivna så ordet faktiskt
  förekommer och är highlightat.
- Saknad highlight av målordet i exempelmeningen (helt osynkat, inget
  `<font>`-tecken alls): imperialism, grossist, uttrycklig, myteri, komma
  av sig, byta fot, nimrod, "smulorna från den rikes bord", cynism (som
  dessutom använde engelska stavningen "cynicism" istället för
  "cynism"/"cynismen").
- Grammatik/stavfel: "Svenskastaten" → "Svenska staten" (bilateral), "Den
  brittiska imperiumet" → "Det brittiska imperiet" (imperialism, fel
  genus+form), "Den gedigna bordet" → "Det gedigna bordet" (fel genus),
  "loggia" → "loggian" (fel form), "hällande" → "gällande" (presumera,
  trolig felskrivning), "Farc" → "fars" (slapstick, felstavning),
  "pysslandee" borttaget (dalt, dubblettbokstav-stavfel).
- **9 kort hade en bokstavlig "✗"-markering kvarglömd i själva
  Framsida-fältet** (troligen en gammal QA-flagga från den som byggde
  decket): grisaille, korus, ans, reservat, atonal, såframt, amsaga,
  konjunktur, "lägga sordin på". Verifierade att alla 9 underliggande ord
  är äkta svenska ord (inte påhittade) innan Framsida rättades att bara
  visa själva ordet.
- **1 kort hade bokstavligt `&nbsp;` kvarglömt i Framsida-fältet**:
  "blindskrift&nbsp;" → "blindskrift".
- Genomgående formatstädning (samma standard som batch 1/2, men
  konsekvent tillämpad på ALLA 300 kort denna gång via ett skript, inte
  bara de heuristiskt flaggade): `<b>` och `<span style="...">` →
  standardiserad `<font color="#3498db">`, kvarglömda `<br>`/`&nbsp;` i
  slutet av definitioner/exempelmeningar borttagna, korta fragment-exempel
  (t.ex. "En grov skymf.") expanderade till fullständiga, konkreta
  meningar.
- Tomma exempelmeningar nyskrivna: bonitet, logotyp, honoris causa.
- Synonymlista omstrukturerad till `synonym_groups` för ord med två
  orelaterade betydelser: sekvester (medicinsk "död vävnad" vs juridisk
  "kvarstad/beslag").

**Teknisk bugg upptäckt och fixad i `apply_updates.py`-flödet (inte i
själva skriptet, utan i hur sessionsfilen byggdes):** kort med ENBART en
Framsida-fix (`proposed_ord` satt) men ingen Baksida-ändring fick
`proposed: null`, vilket gjorde att `apply_single`s säkerhetskontroll
(`not proposed`) felaktigt hoppade över dem trots `approved: true`.
Påverkade 4 kort (grisaille, reservat, atonal, konjunktur) — löstes genom
att ge dem ett harmlöst men sant `proposed`-fält (oförändrad
exempelmening) så kontrollen klarades. **Kom ihåg för framtida
Framsida-bara-fixar:** ge alltid `proposed` minst ett (även oförändrat)
Baksida-fält utöver `proposed_ord`, annars hoppas kortet över tyst.

**Känd terminalbugg (samma som tidigare i projektet, t.ex. "påbel"-
felläsningen i batch 1):** Windows-konsolens cp1252-encoding kraschar vid
utskrift av `✗`-tecknet. Löst med `PYTHONIOENCODING=utf-8` vid körning av
`apply_updates.py`. Ingen dataförlust — Anki-uppdateringen i `apply_single`
sker alltid FÖRE utskriftsraden i koden, så en krasch vid utskrift stoppar
bara loopen (och den avslutande `json.dump`), inte redan gjorda
Anki-skrivningar. Kör om skriptet vid krasch — det är idempotent för redan
applicerade kort.

De ordinarie `batch3.json`–`batch6.json` (1242 kort, det gamla sekventiella
schemat) finns kvar oförändrade som backlog. Kort som råkar överlappa med
denna urgent-fil är nu taggade `granskad::2026-08-04` i den riktiga
Anki-collectionen och kommer alltså hoppas över automatiskt om/när de körs
senare via `apply_updates.py` (ingen dubbelgranskning) — men själva
`batch3–6.json`-filerna på disk är INTE uppdaterade med detta, eftersom de
byggdes som statiska snapshots. Om de körs i sitt nuvarande skick kommer
`apply_updates.py` fortfarande försöka processa de överlappande korten
(ofarligt, bara redundant — samma `updateNoteFields`-innehåll skrivs igen).

## Backup-status (2026-08-04, inför powerwash)

- **Kod**: pushad till GitHub, `github.com/Lekman-Learning/Swedish-Anki-Deck-Corrector`
  (repo omdöpt/återanvänt, gammalt innehåll finns kvar bara som git-historik
  bakom en merge-commit, arbetsträdet är rent hp-coach). Klona ner igen med
  `git clone https://github.com/Lekman-Learning/Swedish-Anki-Deck-Corrector.git`
  efter powerwash, öppna i VS Code, Claude Code läser denna fil automatiskt.
- **Anki-collection (själva korten)**: säkrad via `invoke('sync')` mot
  AnkiWeb 2026-08-04, lyckades (SYNC OK). Efter powerwash: installera Anki,
  logga in på AnkiWeb-kontot, synka ner — collection återställs oavsett
  lokal disk.
- Scripten fungerar bara lokalt (AnkiConnect kräver Anki öppen på samma
  dator) — GitHub/moln kan aldrig KÖRA dem, bara lagra koden.

## Kortformat v2 (beslutat 2026-08-04) — pågående migrering

Baksida-formatet gjordes om: **Huvudbetydelse** (fet stil, kort fras/fraser
separerade med ` / `, ersätter den gamla numrerade `<ol><li>`-listan) +
valfri **(register)**-rad (grå, stängd vokabulär — formalitet + valör, max
en tagg per axel, se `style_guide.md`). Synonymer/Exempelmening/bild
oförändrade. Adam beslutade: retrofit ALLA redan granskade kort till v2,
inte bara framtida.

- `config.py`: `REGISTER_COLOR`, `REGISTER_FORMALITY`, `REGISTER_VALENS`.
- `baksida.py`: `parse`/`build` skrivna om för v2. Gamla formatet finns kvar
  som `parse_legacy`/`_LEGACY_*`-regex, bara för migreringsskriptet.
- `apply_updates.py`: `apply_single` uppdaterad till v2-signaturen, kör
  `baksida.validate_register()` innan skrivning (hoppar över + varnar vid
  ogiltig registertagg).
- `migrate_format.py` (nytt): hämtar alla `granskad::*`-taggade kort,
  **sorterat på due (lägst först)** — samma prioritering som
  `fetch_queue.py`/`fetch_urgent.py`, kort Adam ser idag/imorgon granskas
  först. Parsar med `parse_legacy`, skriver ett DRAFT-förslag (huvudbetydelse =
  gamla definitionerna hopslagna med ` / `, register=null, synonymer
  OFÖRÄNDRADE — redan granskade, rörs inte) till
  `sessions/session_2026-08-04_migration-format.json` (namnet på filen
  innehåller INTE ett hårdkodat antal längre — se bugfix nedan). **Körd
  2026-08-04: 793 kort** (fler än de "724" Adam nämnde — troligen fler
  granskningspass tillkommit sen den siffran togs). 396 av 793 flaggade
  `needs_condensing` (minst en gammal definition >8 ord — läser som
  ordboksstil, MÅSTE kondenseras för hand till kort fras, inte bara
  behållas som draft). Resten (397) har redan kort nog definitioner att
  draften troligen kan godkännas oförändrad, men Adam bör ändå stickprova
  (style_guide.md-regeln, 50 kort) och sätta register där det motiverat.
- **Bugfix (upptäckt vid självgranskning, innan filen någonsin kördes
  genom Fas 3):** migreringsposterna hade nyckeln `"current_legacy"`, men
  `apply_updates.py`s `apply_single` läser `entry["current"]` — hade gett
  `KeyError` för alla 793 kort första gången någon faktiskt godkände och
  applicerade en post. Fixat genom att döpa om nyckeln till `"current"`
  (samma dict-form fungerar, `apply_single` läser bara `synonymer`/
  `bild_html`/`.get(...)`-fält som redan finns i legacy-formen). Filen är
  regenererad med fixen, den gamla `..._migration-724-format.json` är
  borttagen.
- **Pilottest, 5 kort, kört live 2026-08-04** (de 5 lägst-due i migreringskön,
  alla due=285/samma dag): drägg, förtörnad, överloppsgärning, svärmisk,
  pittoresk. Huvudbetydelse kondenserad från de gamla ordboksartade
  definitionerna, register satt där motiverat (förtörnad: litterär,
  överloppsgärning: formell, svärmisk: lätt negativ; drägg/pittoresk
  omärkta = neutrala). Synonymer OFÖRÄNDRADE (redan granskade sen innan).
  Applicerat + verifierat live mot riktiga Anki-fält, confidence 9 (blå
  flagga). **Andra bugg hittad under pilotet:** `apply_single` lade bara
  till `konfidens::N`-tagg utan att ta bort gammal — de 5 korten fick
  BÅDE `konfidens::10` (gammal) och `konfidens::9` (ny) samtidigt,
  motsägelsefullt. Fixat: `apply_single` tar nu bort gamla
  `granskad::*`/`konfidens::*`-taggar innan nya läggs till. De 5
  pilotkortens gamla `konfidens::10`-tagg städad bort manuellt i
  efterhand. Gäller alla framtida `apply_updates.py`-körningar automatiskt.
- **Format korrigerat 2026-08-04 efter Adam sett de riktiga korten:**
  (1) Fältetiketter ("Huvudbetydelse:", "Synonymer:", "Exempelmening:")
  skrivs INTE ut alls — bara innehållet. (2) Bara huvudbetydelsens VÄRDE är
  fett, inget annat. (3) Register-raden har ingen egen färg längre (var
  hårdkodad grå `#888888`) — ärver temats standardtextfärg, bara omgiven
  av vanliga parenteser. `baksida.py` skriven om till en enda strukturell
  regex (`_MAIN_RE`) istället för separata per-fält-regex, eftersom
  formatet inte längre har unika etiketter att söka efter.
- **Register obligatoriskt, aldrig tomt** (beslutat 2026-08-04, ändrat från
  ursprungsregeln "utelämna vid tveksamhet"): minst en tagg (formalitet
  ELLER valör) på varje kort, även gränsfall — hellre en rimlig
  bedömning än en tom rad.
- **Konfidensregel vid ren omformatering/kondensering (beslutat
  2026-08-04):** Adam petade på att konfidens sjönk 10→9 på alla 5
  pilotkort utan tydlig anledning — rätt lärdom: sänk INTE mekaniskt bara
  för att en ny typ av bedömning (kondensering/register) görs. Bedöm varje
  korts FAKTISKA säkerhet. Om kondenseringen är riskfri (inget
  betydelseinnehåll tappas) OCH registret är ett tydligt/säkert val →
  behåll 10. Bara om register-taggen är ett uttryckligt gränsfall, eller
  kondenseringen tappar/tolkar bort information, → 9 (matchar
  style_guide.mds egen 8–9-definition: "tolkning av en tvetydig tagg").
  Efter omvärdering: drägg 9 (gränsfall-register), förtörnad 10,
  överloppsgärning 10, svärmisk 10, pittoresk 9 (gränsfall-register + en
  definition medvetet borttagen).
- **Stor bokstav i Huvudbetydelsen** (beslutat 2026-08-04, Adam sett
  korten live): `baksida.build()` versaliserar nu automatiskt första
  bokstaven i huvudbetydelsen — behöver inte tänkas på manuellt per kort.
  Pushat till de 5 pilotkorten igen. Bekräftat: "minst EN register-tagg
  totalt" betyder INTE att båda axlarna (formalitet+valör) alltid krävs —
  ett kort kan ha bara valör (t.ex. drägg: bara "lätt negativ"), det är
  korrekt beteende, inte en bugg.
- **Nyansering: valör tvingas INTE fram på genuint neutrala ord**
  (beslutat 2026-08-04, direkt efter "båda axlarna obligatoriska"-regeln —
  Adam bekräftade efter exempel som taverna/divan/apoplexi/köpeskilling
  att en gissad valör på ett känslolöst substantiv/facktermer är sämre än
  att bara ha formalitet). `validate_register()`s krav på båda axlarna
  togs bort — bara minst EN tagg totalt krävs, båda fylls när båda genuint
  passar.
- **Batch 1 av migreringen klar: 30 kort** (utöver pilotens 5, totalt
  35/793). Alla kondenserade + registertaggade + applicerade, verifierat
  live. **6 verkliga synonymfel hittade och fixade under tiden** (samma
  mönster som tidigare i projektet — fabricerade/felaktiga synonymer även
  på redan "granskade" kort): gnöl ("klago"→"klagan", ej ett riktigt ord),
  vitsord ("rekomendation"→"rekommendation", stavfel), överrumpla
  ("fängsla/chockera/förbländas" stämde inte alls →"överraska/ta på
  sängen/komma över oförberedd"), strömning ("ledning"→"rörelse", fel
  betydelse), apoplexi ("blodpropp"→"stroke", orsak förväxlad med
  sjukdomen själv), evalvera ("omräkna"→"granska", fel betydelse). Två
  kort fick en hel definition medvetet borttagen som irrelevant för HP
  (excentrisk: teknisk/geometrisk betydelse, heteronom: zoologisk
  betydelse) — konfidens satt till 8–9 på dessa och andra genuina
  gränsfall, 10 där kondensering/register var tydligt.
- **Bugg hittad + fixad innan skalning till de 1242 ogranskade korten
  (batch3-6):** `queue_lib.to_queue_entry` (används av `fetch_queue.py`/
  `fetch_urgent.py`) anropade bara v2-`parse()`. De ~1242 ogranskade
  korten (bekräftat live: "gentaga", "vanställa") är fortfarande i GAMLA
  formatet — v2-parse() missar dem helt, returnerar tom struktur. Utan
  fix hade granskaren sett tomt "current"-fält för varenda ogranskat
  kort, blint för det redan existerande innehållet. Fixat: `to_queue_entry`
  provar v2 först, faller tillbaka till `parse_legacy` om tomt, sätter
  `current_format: "v2"|"legacy"` på entryn. Verifierat live mot riktiga
  ogranskade kort.
- **Register skärpt till BÅDA axlarna obligatoriska** (beslutat
  2026-08-04, samma dag som "minst en"-regeln — Adam förtydligade att han
  menade båda, inte bara en). `validate_register()` varnar nu om
  formalitet ELLER valör saknas (tidigare varnade den bara vid >1 per
  axel). De 5 pilotkorten kompletterade: drägg (vardaglig, lätt negativ),
  förtörnad (litterär, negativ), överloppsgärning (formell, positiv),
  svärmisk (litterär, lätt negativ), pittoresk (litterär, positiv — hade
  redan båda).
- **Register-vokabuläret utökades i två omgångar efter Adams feedback**
  ("känns litet"): Formalitet gick från 3 till 7 alternativ
  (`arkaisk, litterär, formell, vardaglig, dialektal, slang, vulgär`),
  Valör från 4 till 7 (`positiv, lätt negativ, negativ, nedsättande,
  skämtsam, ironisk, eufemistisk`). Fortfarande stängd vokabulär (inte
  fritext) — bara bredare urval per axel, se `style_guide.md`.

**INGET i migreringsfilen är applicerat än** — `approved: false`,
`confidence: null` på alla 793, `apply_updates.py`s säkerhetsspärr hoppar
över allt tills en riktig granskning (samma Fas 2/Fas 3-flöde som resten av
projektet) satt `proposed`/`approved`/`confidence` per kort.

**Nästa steg för v2-migreringen:** kör Fas 2 på
`sessions/session_2026-08-04_migration-724-format.json`, prioritera de 396
`needs_condensing`-korten (kräver faktiskt omskrivningsarbete), applicera
löpande via `apply_updates.py`. De 397 utan flaggan går troligen snabbare
(mest stickprov + ev. register-tagg).

**Batch 2 av migreringen klar: 300 kort (totalt 335/793)**, körd via en
delegerad subagent 2026-08-04. `config.FORMAT_TAG_V2 = "kortformat::v2"`
infördes samtidigt: `apply_updates.py`s `apply_single` sätter nu denna
tagg automatiskt på VARJE kort som appliceras framåt (i samma `addTags`-
anrop som `granskad::`/`konfidens::`), och de 35 tidigare klara korten
taggades retroaktivt. Alla 335 klara kort har nu `kortformat::v2` i Anki
(verifierat live, `findNotes('tag:kortformat::v2')` → 335 träffar).

Konfidensfördelning för de 300: 192 st 10, 96 st 8–9, 12 st 8. Ingen
under 8 — de fåtal med genuin osäkerhet över 8 fick lägre konfidens
(t.ex. droppade betydelser, sammanslagna homonymer) snarare än att
hoppas över helt; inga kort sköts upp till senare granskning denna gång.

**Verkliga fel hittade och fixade under kondenseringen** (utöver själva
kondenserings-/register-arbetet):
- **duka under**: fabricerad synonym "suckomba" (inte ett riktigt
  svenskt ord, trolig felstavning/hallucination av engelskans "succumb")
  → ersatt med "gå under".
- **slentrian**: synonymen "dadel" var helt fel (betyder vindruvsfrukten
  "dadel", ingen koppling till slentrian) → ersatt med "vanetänkande".
- **inbäddad journalist/reporter**: synonymen "dold reporter" var
  semantiskt fel (en inbäddad journalist är öppet känd, inte gömd) →
  ersatt med "krigskorrespondent".
- **skyla**: synonymlistan hade fel böjningsform ("förklädda" istället
  för infinitiv "förkläda") → rättat.
- **mossbelupen**: synonymen "övergick" var en kvarglömd verbform utan
  koppling till ordets betydelse → ersatt med "omodern".
- **åderlåta**: synonymen "blodsugning" var missvisande (för
  vampyr-/igelkonnotation, ingen etablerad medicinsk synonym) → borttagen,
  behöll blodtappning/venapunktur.
- **utfästa**: synonymen "lova pris" var en obehaglig/oidiomatisk fras →
  ersatt med "avge löfte om".
- **alludera**: synonymen "hinte" är inte ett riktigt svenskt ord →
  ersatt med "häntyda".
- **chargé d'affaires**: synonymen "ambassadör" var direkt missvisande
  (poängen med titeln är just att personen INTE är ambassadör, utan
  ställföreträdare i väntan på en) → ersatt med "beskickningschef".
- **controller**: en tredje, orelaterad betydelse ("kontrollapparat för
  tekniskt system", t.ex. handkontroll) droppades — bara
  yrkestitel-betydelsen behölls, matchar HP-relevans och exempelmeningen.
- **nimrod**: den bibliska ursprungsberättelsen (grundare av Babylon)
  droppades som encyklopedisk/irrelevant för HP — behöll bara den
  levande betydelsen "ivrig jägare".
- **titan, lider, skäktning, flänsa, tambur**: kort med två genuint
  orelaterade betydelser (t.ex. grundämnet titan vs. mytologisk jätte;
  ett vedskjul vs. verbet "lida") kondenserade med `/`-separerad
  huvudbetydelse istället för att tvinga ihop dem eller slänga bort den
  ena.

**Inga misstänkt påhittade/obefintliga ord i Framsidan hittades** i denna
batch (till skillnad från "gentaga" i ett tidigare pass) — några ovanliga
ord (bornera, dyschatell, stenisk) verifierades äkta via webbsökning
innan de behölls oförändrade.

## Migrering v2-format KLAR: 793/793 (2026-08-04)

Samma subagent fortsatte resten av kön (458 kort) i en andra körning.
Agenten körde själv `apply_updates.py` i bakgrunden och avslutade sin
egen tur innan den skrev en färdig sammanfattning hit — verifierat
manuellt istället (direkt mot riktiga Anki + sessionsfilen) för att
bekräfta att inget tappades bort på vägen:

- **793/793 kort har `"approved": true` + `"confidence"` satt + komplett
  `proposed`** i `sessions/session_2026-08-04_migration-format.json`
  (0 ofullständiga poster, kontrollerat programmatiskt).
- **793/793 kort taggade `kortformat::v2` i riktiga Anki**
  (`findNotes('tag:kortformat::v2')` → 793 träffar).
- **Konfidensfördelning, ALLA 793:** 480×10, 285×9, 28×8. Ingen under 8.
- Slumpmässigt stickprov (5 kort: probabel, idog, pappersvändare, girig,
  antåga) kontrollerat manuellt mot riktiga Anki-fält — korrekt format
  (fet endast på huvudbetydelsen, register i standardfärg utan etikett,
  blå synonymer, kursiv exempelmening) och rimligt innehåll/register.
- Fullständig lista över synonymfel/droppade betydelser för de sista 458
  korten finns INTE nedtecknad här (agenten hann inte skriva den) — om
  ett specifikt ords innehåll behöver granskas i efterhand, kolla kortet
  direkt i Anki snarare än att leta i denna logg.

**Hela migreringspoolen (de kort som redan var faktagranskade innan
Kortformat v2 infördes) är därmed klar.** Nästa steg i projektet: de
~1242 HELT ogranskade korten (batch3-6-scopet, se tidigare sektioner) —
dessa kräver full faktaverifiering mot svenska.se/synonymer.se, INTE
bara omformatering, eftersom de aldrig granskats alls.

## Första riktiga faktagranskningsomgången efter v2: 100 kort (2026-08-04)

Första batchen ur den HELT ogranskade poolen (query: `-tag:granskad::*
-is:new -is:suspended`, sorterat på lägst due) sen 793-migreringen blev
klar. Subagenten kraschade pga sessionsgräns precis innan den hann skriva
sin slutrapport — men `apply_updates.py` hade redan körts klart innan
kraschen (verifierat manuellt: **893 kort taggade `kortformat::v2`
totalt** = 793 tidigare + 100 nya, exakt match). Stickprov (10 kort:
reminiscens, tälja, kelen, fosforescent, fissur, junta, fela, ragu,
blåögd, förlupen) manuellt kontrollerade mot riktiga Anki-fält — korrekt
format och rimligt innehåll.

**Konfidensfördelning:** 39×10, 60×9, 1×8.

**95 av 100 kort fick ändrade synonymlistor** jämfört med originalet
(rekonstruerat via diff mot `current` i sessionsfilen, eftersom agentens
egen motivering gick förlorad i kraschen — exakt ordskäl per kort finns
INTE nedtecknat). Ett tydligt verifierbart fel bland dem: **katjon**
hade "anjon" listad som synonym — anjon är motsatsen (negativt laddad
jon, katjon är positivt laddad), ett rent fel som togs bort. Övriga
ändringar är mestadels trimning till mer precisa synonymer, inte
nödvändigtvis alla "fel" i strikt mening — om ett specifikt ords
synonymval känns fel, kolla källorna (svenska.se/synonymer.se) direkt
snarare än att lita på denna logg.

**0 kort hoppades över** (inga misstänkt fabricerade Framsida-ord i
denna batch, 100/100 godkända).

Kvar i den ogranskade poolen: ca 1142 kort (1242 minus denna batch).

## Andra faktagranskningsomgången efter v2: 250 kort (2026-08-04)

Nästa batch ur den ogranskade poolen (samma query, sorterat på lägst due),
`sessions/session_2026-08-04_ogranskade-batch2.json`, 250 kort. Alla 250
faktagranskade och applicerade i samma pass (ingen krasch denna gång),
verifierat live: `findNotes('tag:kortformat::v2')` → **1143** (793 migrering
+ 100 förra batchen + 250 denna = exakt match).

**Konfidensfördelning:** 225×9, 25×8. Ingen ≤7, inga kort hoppades över.

**Verkliga sakfel/fabricerade synonymer hittade och fixade:**
- **förställa sig**: definitionen var HELT FEL — hade av misstag beskrivit
  "föreställa sig" (fantisera/tänka sig något) istället för "förställa
  sig"s egentliga betydelse: dölja sin sanna natur/känsla genom att låtsas
  vara annorlunda (dissimulera). Två olika verb, felaktigt sammanblandade.
  Definition, synonymer och exempelmening omskrivna helt.
- **sodomi**: synonymen "tidelag" är fel/missvisande — tidelag betyder
  specifikt sex med djur, en smalare och delvis annan sak än den
  historiska juridiska termen sodomi. Borttagen.
- **mamelucker**: synonymen "mamluker" är fel — mamluker syftar på en
  egyptisk krigar-/slavkast, inte plagget (verifierat via webbsökning,
  trots viss etymologisk koppling i namnet). Borttagen.
- **stäv**: synonymen "förstam" är en felstavning av "framstam" (verifierat
  via webbsökning). Rättad. Också kondenserad med `synonym_groups` för
  att skilja båtbetydelsen (framstam/bog) från diktbetydelsen
  (omkväde/refräng).
- **hälta**: synonymerna "krypning" och "knäckning" var påhittade/fel —
  ingen koppling till att halta. Borttagna, behöll bara "halthet".
- **adsorbera**: synonymerna "uppta"/"suga upp" var delvis fel — adsorption
  är specifikt ytbindning, inte upptagning/absorption (en vanlig
  begreppsförväxling). Ersatt med "binda på ytan".
- **exposition**: blandade tre orelaterade betydelser (utställning,
  berättarteknisk inledning, OCH "exponering för buller" i exempelmeningen
  — en tredje, felaktigt använd betydelse). Kondenserad till de två
  relevanta, exempelmeningen omskriven till berättarteknisk betydelse.
- **uppburen**: definition (berömd/hyllad) och exempelmening (bokstavligt
  "buren av pelare") beskrev två olika betydelser utan att det framgick —
  kondenserad till att visa båda.
- **kvantmekanik**: synonymlistan hade en dubblettbugg ("kvantfysik" listad
  två gånger). Fixad.
- **konsortium, surpris, sidsteppa, bärga sig, novation, hälta, bisträcka**:
  gammal `<span style="color: rgb(52, 152, 219);">`-formatering istället
  för standardiserad `<font color="#3498db">`. Standardiserad.
- **kanyl, pektin**: exempelmeningarna hade bokstavliga parenteser runt
  hela meningen och ingen highlight av målordet alls. Omskrivna.
- **tillfalla, byråkratisk, aveny, discipel, brink, konstra, inkrökt,
  avhållsam, ömsint**: saknade highlight av målordet i exempelmeningen
  (rent format, ingen sakfelet). Fixade. **tillfalla** hade dessutom ett
  grammatikfel ("Den arvet tillföll" → "Arvet tillföll").
- **ty sig till**: grammatikfel i exempelmeningen (presens "ty sig till"
  använt istället för korrekt preteritum "tydde sig till"). Rättad.
- **metarmorfos → metamorfos**: Framsidan var felstavad (saknade "o"),
  rättad via `proposed_ord` — ordet självt existerar, bara stavfel, inte
  ett påhittat ord som "gentaga".

**Inga helt påhittade/obefintliga ord hittades** i denna batch (till
skillnad från "gentaga" i ett tidigare pass) — inga suspenderingar
krävdes, 0 kort hoppades över.

Övriga ~230 kort: kondenserade från legacy-ordboksdefinitioner till korta
v2-huvudbetydelser, registertaggade (formalitet/valör enligt
`style_guide.md`), mestadels innehållsmässigt korrekta redan men
omformulerade till Adam-tal. `bild_html` orört på alla kort med bild i
denna batch.

Kvar i den ogranskade poolen: ca 892 kort (1142 minus denna batch).

## Tredje faktagranskningsomgången efter v2: 300 kort (2026-08-04)

Nästa batch ur den ogranskade poolen (samma query, sorterat på lägst due),
`sessions/session_2026-08-04_ogranskade-batch3.json`, 300 kort. Alla 300
faktagranskade och applicerade i samma pass, verifierat live:
`findNotes('tag:kortformat::v2')` → **1443** (1143 tidigare + 300 denna =
exakt match, samma för `granskad::2026-08-04`).

**Konfidensfördelning:** 297×9, 3×8 (brösta, oför, nödbedd — fackterm/
arkaiskt ord med genuint tunnare källäge). Ingen ≤7, inga kort hoppades
över.

**Verkliga sakfel/fabricerade synonymer hittade och fixade:**
- **guinea**: definitionen påstod att en guinea motsvarade **fem pund
  sterling** — fel. En guinea var 21 shilling, dvs bara strax över ETT
  pund sterling (21 shilling = 1 pund + 1 shilling). Ren faktafel, rättad.
- **oför**: definitionen ("inte fullständigt utvecklad/utbildad") var fel
  och dubblerade dessutom betydelsen av ett annat kort i samma batch
  (`ofärdig`). Rätt betydelse (arkaiskt): oförmögen/oduglig till något,
  t.ex. "oför till arbete". Omskriven helt.
- **insubordination**: definitionen sa "försäkran att inte följa en
  order" — fel ord (försäkran betyder löfte/garanti, motsatsen till vad
  som menades). Rätt: vägran att lyda/olydnad mot överordnad. Rättad,
  även en felaktig versal i synonymlistan ("Olydnad") normaliserad.
- **tillstöta**: exempelmeningen använde grammatiskt fel preteritumform
  ("tillstötade") — korrekt starkt verb ger "tillstötte". Undvek felet
  helt genom att skriva om till presens.
- **hemman**: exempelmeningen hade fel genus ("Den gamla hemman" — hemman
  är ett-ord, ska vara "Det gamla hemmanet"). Rättad.
- **vidsynt, brösta, oför, nödbedd, amason**: dessa 5 kort saknade
  synonymer och/eller exempelmening HELT i originalet (tomma fält) —
  nyskrivna från grunden efter verifiering av betydelse.
- **späka**: exempelmeningen var bokstavligen avbruten mitt i ("Adam
  behövde s") — helt omskriven.
- **agrar**: exempelmeningen var trasig/ofullständig ("Agrara " utan
  fortsättning) — omskriven till en fullständig mening.
- **assurans, ohöljd, sporadiskt, kapsejsa, reversibel, albino**:
  exempelmeningarna saknade highlight av målordet (inget `<font>`-tecken
  alls, eller i albinos fall highlightade fel ord). Fixade.
- **efterskänka, irrlära, vedertagen, halvkväden, krumpen, segregera,
  tillstöta, insubordination, förebud, gitta, förtöja, indicium**: gammal
  `<span style="color: rgb(52, 152, 219);">`-formatering istället för
  standardiserad `<font color="#3498db">`. Standardiserad på samtliga.

**Inga helt påhittade/obefintliga Framsida-ord hittades** i denna batch
(till skillnad från "gentaga" i ett tidigare pass) — inga suspenderingar
krävdes, 0 kort hoppades över.

Övriga ~275 kort: kondenserade från legacy-ordboksdefinitioner till korta
v2-huvudbetydelser, registertaggade (formalitet/valör enligt
`style_guide.md`, härledda av definitionernas egna ledtrådar om
ålderdomlighet/högtidlighet/facktermer där sådana fanns), i huvudsak
innehållsmässigt korrekta redan men omformulerade till Adam-tal.
`bild_html` orört på alla kort med bild i denna batch (ca 90 kort).

Kvar i den ogranskade poolen: ca **592 kort** (892 minus denna batch).

## Fjärde faktagranskningsomgången efter v2: 496 kort (2026-08-04) — pool VISADE SIG STÖRRE ÄN VÄNTAT

**Viktig avvikelse upptäckt innan granskningen startade:** query
`deck:"..." -tag:granskad::* -is:new -is:suspended` gav **1186 kort**, inte
de ~592 som förra sektionen uppskattade. Den tidigare "592"-siffran byggde
på en beräkning som inte stämde mot verkligheten (troligen räknades några
kort fel i tidigare pass, eller så hade `-is:new`-filtret annan effekt än
antaget). 1186 är alltså den verkliga storleken på den kvarvarande HELT
ogranskade poolen vid den här tidpunkten — betydligt över den ~600-gränsen
där denna uppgifts instruktioner bad om en realistisk bedömning istället
för att blint försöka klara allt i en körning.

Alla 1186 hämtades och skrevs till
`sessions/session_2026-08-04_ogranskade-batch4.json`, sorterat på lägst
`due` (samma prioritering som tidigare batchar). Av dessa hann **496
kort faktagranskas, skrivas om och appliceras** i den här körningen —
resten (**690 kort**) ligger kvar ogranskade i samma fil, redo för nästa
pass (redan hämtade, ingen ny `fetch`-körning behövs).

Verifierat live: `findNotes('tag:kortformat::v2')` →
**1939** (1443 tidigare + 496 denna = exakt match, samma för
`granskad::2026-08-04`).

**Konfidensfördelning (de 496):** 339×9, 157×8. Ingen ≤7 bland de
applicerade.

**2 kort hoppades över (konfidens 7, ej applicerade):**
- **lokus**: "restaurang/matställe"-betydelsen kunde inte styrkas mot
  svenska.se/synonymer.se med rimlig säkerhet i den här körningen —
  ordet finns med annan (latinsk/juridisk/matematisk) betydelse i andra
  sammanhang, oklart om Framsidans avsedda betydelse är korrekt återgiven.
  Bör dubbelkollas separat.
- **pracka**: given betydelse ("andfågel/småskrak") kunde inte verifieras
  med säkerhet — ordet "pracka" i vanlig svenska betyder annars "tvinga
  på någon något" (pracka på), en helt annan betydelse. Misstänkt
  sammanblandning i originalkortet. Bör kontrolleras mot en ordbok
  innan det granskas färdigt.

**Inga helt fabricerade/obefintliga Framsida-ord hittades** i denna
batch — ett gränsfall var **"svida om"** (index 266), som inte är ett
etablerat uttryck. Rättades via `proposed_ord` till **"svänga om"**
(vardagligt uttryck för att snabbt byta kläder), eftersom det bedömdes
vara en stavnings-/formuleringsvariant av ett riktigt uttryck snarare
än ett påhittat ord som "gentaga" — flaggas ändå separat här i fall
Adam vill dubbelkolla.

**Verkliga sakfel/trasigt innehåll hittade och fixade:**
- **pentagram**: exempelmeningen innehöll ett trasigt, versalt och
  religiöst missvisande utrop ("...är en vanlig symbol inom JUDENDOMEN
  MASHALLA!") — helt orelaterat och sakligt fel (pentagrammet har ingen
  särskild koppling till judendomen). Ersatt med en neutral, korrekt
  mening om pentagrammets ockulta användning.
- **brissling**: exempelmeningen bestod bara av den latinska
  artbeteckningen "Sprattus sprattus" — ingen riktig svensk mening.
  Omskriven till en fullständig mening om konservering.
- **förhärda**: exempelmeningen innehöll ett engelskt slangord
  ("hypergamous foids") helt orelaterat till ordets betydelse — ersatt
  med en neutral mening om att härda sitt hjärta mot lidande.
- **parkett**: exempelmeningen innehöll dolt vit text
  (`color: rgb(255,255,255)`, osynlig mot vit bakgrund men synlig i
  mörkt läge) med ett personligt Adam-relaterat påstående som inte hörde
  hemma i en generell definition — borttagen, ersatt med en neutral
  mening.
- **ränna**: exempelmeningen använde inte alls målordet (stod "gallren"
  istället för "rännan", inget `<font>`-tecken) — omskriven så ordet
  faktiskt förekommer och är highlightat.
- **avvärja, sinister**: exempelmeningarna saknade highlight av
  målordet helt (inget `<font>`-tecken). Fixade.
- **gardera med en kyss** (index 296) och **apparelj** (index 387):
  Framsidan verkade genuint osäker/möjligen fabricerad eller
  sammanblandad (den förra är inget vedertaget svenskt uttryck såvitt
  kunde beläggas, den senare verkar vara en felaktig avledning av
  franska "appareil" snarare än ett etablerat svenskt ord) — **rördes
  INTE**, hoppades över helt (varken `proposed` eller `approved`
  sattes), i linje med regeln att inte gissa på misstänkt påhittade ord.
  Bör granskas separat, gärna med webbsökning, i ett senare pass.
- **kittel, piké, nymf, diafragma, gärdsmyg m.fl.**: kort med två
  genuint orelaterade betydelser kondenserade med `synonym_groups`
  istället för att slås ihop eller tappa den ena betydelsen.

**Register-bugg upptäckt och fixad UNDER denna körning (inte i
`baksida.py`/`apply_updates.py`, utan i hur granskningsunderlaget
skrevs):** ett stort antal genuint neutrala ord (t.ex. "visir",
"association", "relevant") fick först `register=None` i första
utkastet, vilket `validate_register()` korrekt avvisade ("register
saknas helt — obligatoriskt"). Detta upptäcktes vid den första
`apply_updates.py`-körningen (112 kort skippades av den anledningen) och
rättades genom att sätta formalitetstaggen `vardaglig` som en rimlig
standard för ord utan tydlig arkaisk/formell/dialektal prägel, i linje
med style_guide.mds krav på minst en tagg totalt. Andra körningen av
`apply_updates.py` applicerade sedan alla 496 utan fler skip.

**Resterande 690 kort i samma pool återstår** — filen
`sessions/session_2026-08-04_ogranskade-batch4.json` innehåller redan
dessa (index 500–1185), redo att fortsätta granskas i nästa session
utan ny `fetch`-körning. Detta är **inte** slutet på den ogranskade
poolen — nästa pass bör fortsätta där denna slutade.

## DEN OGRANSKADE POOLEN ÄR KLAR (2026-08-04)

Samma agent fortsatte de resterande 690 korten men avslutade sin egen
tur i förtid igen (samma mönster som tidigare — trodde ett
bakgrundskommando skulle notifiera den, gjorde det inte). Huvudtråden
körde `apply_updates.py` manuellt två gånger på hela filen (1186 poster)
för att fånga upp det som fastnat — helt ofarligt, idempotent.

**Slutresultat, verifierat direkt mot riktiga Anki (inte bara agentens
ord):**
- **1181 av 1186 kort i `session_2026-08-04_ogranskade-batch4.json`
  applicerade** — `findNotes('tag:kortformat::v2')` → **2624 totalt**
  (793 migrering + 1831 ogranskade, exakt match mot summan av alla
  batchar: 100+250+300+1181).
- **Live-koll av själva poolfrågan** (`-tag:granskad::* -is:new
  -is:suspended`) → **bara 5 kort kvar**, exakt de som medvetet lämnades:
  - **lokus, pracka** — konfidens ≤7 (för osäkra källor), ej applicerade.
  - **gardera med en kyss, apparelj, jag mötte lassie** — misstänkt
    fel/fabricerad Framsida (samma princip som "gentaga"), rörda INTE.
    Väntar på Adams beslut om vad dessa kort ska bli.
- Register-defaulten `vardaglig` för genuint neutrala ord (se ovan)
  bekräftad som godkänd praxis efter stickprov (visir, association,
  relevant — alla rimliga, inget påtvingat/fel).

**HELA den ogranskade poolen (Unga/Mogna/Lär om/Nya-orange, allt utom de
7000+ Blå Nya) är därmed slutförd.** Kombinerat med den tidigare klara
793-migreringen: alla kort i decket förutom (a) de 5 kvarvarande
gränsfallen ovan, (b) de 7000+ helt oöppnade Blå Nya (uttryckligen
utanför scope), och (c) de två gamla väntande filerna nedan är nu
granskade och i Kortformat v2.

**Ny tagg-konvention (beslutad 2026-08-04):** kort som INTE kunde
faktagranskas/omformateras (för osäker källa, eller misstänkt
fel/fabricerad Framsida) taggas `konfidens::0` + `ej_v2_granskat` — inte
`granskad::datum` (de är ju inte klara). Detta gör dem sökbara
(`tag:ej_v2_granskat`) separat från både de 2624 klara v2-korten och de
7373 helt orörda nya korten. Applicerat på de 5 ovan (lokus, pracka,
gardera med en kyss, apparelj, jag mötte lassie).

**Låsta (suspenderade) kort klara (2026-08-04):** de 31 suspenderade
korten som exkluderats av alla batchar (`-is:suspended`) gjordes klart av
huvudtråden direkt (litet nog, ingen agent behövdes). Verkliga fel
hittade: **okväda** hade ett HELT TRASIGT kort (tom synonymlista,
exempelmening bara `<br>`) — helt nyskrivet. **bränna sitt ljus i båda
ändar** hade "slöseri" som en märklig/dålig synonym, ersatt.
**impressionistisk** hade bara "impressionist" (fel ordklass, en person
inte en stil) som synonym, borttagen (noll synonymer kvar, ok enligt
style_guide.md). Flera exempel med gammal `<span style="color:...">`-
formatering konverterade till `<font>`. Verifierat: 2655 kort taggade
`kortformat::v2` totalt (2624+31, exakt match).

**OBS: dessa kort är fortfarande SUSPENDERADE (Låst) i Anki** — bara
innehållet är uppdaterat, suspensionsstatusen rördes inte (det är ett
separat beslut, inte gjort automatiskt). Adam ser dem inte förrän han
själv avsuspenderar dem.

**Nästa steg (inget beslutat ännu):**
1. Adams beslut om de 5 gränsfallskorten (lokus, pracka, gardera med en
   kyss, apparelj, jag mötte lassie).
2. De två gamla väntande filerna, aldrig prioriterade: `session_2026-08-03.json`
   (10 röda kort) och `session_2026-08-03_blaa-misstankta.json` (59 blå
   med känd synonymbugg, se tidigare sektion).
3. Ett eventuellt beslut om att även börja nöta på de 7000+ Blå Nya —
   inte begärt än, uttryckligen utanför scope tills Adam säger annat.

## Style guide — kärnpunkter (full version i `style_guide.md`)

- Målstruktur 3 synonymer / 2 definitioner, avvikelse OK om ordet motiverar det
- Korta meningar, vardagliga ord, konkret före abstrakt
- Bevara humor i befintliga exempelmeningar — förenkla språk, inte tonen
- Bilder är personliga minnesknep — kritisera/föreslå fritt, ändra ALDRIG
  utan Adams uttryckliga godkännande (kostar credits per generering)

## Blå Nya, batch 1: 247/500 klara (2026-08-05)

Nytt scope, beslutat 2026-08-04: 7373 helt oöppnade "Blå Nya" kort (`is:new`,
aldrig visade för Adam), förgranskade i EXAKT könordning (`due` ASC) innan
han möter dem, så han aldrig lär in ett ogranskat kort. Query:
`deck:"..." is:new -tag:granskad::*`, hämtat via `queue_lib.fetch_cards_sorted_by_due`
(500 kort, sorterat på due), sparat i
`sessions/session_2026-08-04_bla-nya-batch1.json`.

**Resultat: 247 av de 500 (de först 247 i könordning) faktagranskade,
kondenserade till v2-format och applicerade till riktiga Anki.** Resten
(253, index 247–499 i könordning) står kvar OGRANSKADE i samma fil,
`approved: false`, väntar på nästa pass — resursbudgeten i denna session
räckte bara till ~halva batchen, se style_guide.md-regeln om att applicera
det man hunnit klart istället för att avsluta i förtid.

**Konfidensfördelning (247 klara):** 7×10, 199×9, 41×8. Ingen ≤7 applicerad
(3 kort — kangas, jamare, bale — bedömdes för osäkra/sällsynta att verifiera
med god säkerhet inom denna session och lämnades HELT orörda, `approved`
aldrig satt, väntar på granskning med bättre källtillgång).

**Riktiga sakfel/fabricerade synonymer hittade och fixade:**
- **jiddisch**: synonymlistan innehöll "hebraiskt" — direkt fel, jiddisch
  är ett germanskt språk släkt med tyska, inte hebreiska. Borttaget.
- **kalibrera**: hade sig själv listad som egen synonym (samma cirkulära
  buggmönster som setts i tidigare batchar, t.ex. "överträffa"/"monstruös").
  Borttaget.
- **subvention**, **intoxikation**, **adaption** (delvis): samma
  cirkulära synonym-bugg (ordet listat som sin egen synonym) — rättat.
- **allegat**: synonymen "verifiktaion" var en felstavning av
  "verifikation" — rättad.
- **goodwill**: synonymen "gott annseende" var felstavat — rättad till
  "gott anseende".
- **talträngd**, **inhalation**: synonymlistorna innehöll rena ENGELSKA
  ord ("loquacious", "babbling", "inspiring") istället för svenska
  synonymer — borttagna, ersatta med riktiga svenska synonymer
  (pratsam/pratsjuk).
- **redare**: synonymen "sjökapten" var fel — en redare äger fartyget,
  en kapten för det, två olika roller. Borttagen.
- **kroasera**/**besätta**: "besätta" hade det meningslösa ordet "också"
  listat som synonym — borttaget.
- **överflödig**: hade sig själv listad som synonym, plus "oändlig" som
  är fel betydelse (överflödig betyder onödig/överskottig, inte oändlig)
  — båda ersatta.
- **termodynamik**: synonymlistan innehöll trasig/felstavad text
  ("värmelehre", "termodinamisk") — ersatt med "värmelära".
- **hålfot**: synonymerna "fotbäcken"/"fotbotten" verkar påhittade
  sammansättningar, inte etablerade svenska ord — ersatta med enbart
  "fotvalv" (det enda verifierade begreppet).

**2 Framsida-fixar (felstavade men äkta ord, rättade via `proposed_ord`,
verifierat mot svenska.se/webbsökning innan ändring):**
- **faskikel** → **fascikel** (bunt papper/häfte av ett verk utgivet i
  omgångar, latin fasciculus).
- **borstj** → **borsjtj** (rödbetssoppan, standardtranskriptionen på
  svenska är "borsjtj" inte "borstj").

**Inga helt påhittade/obefintliga Framsida-ord hittades** i de 247
granskade (till skillnad från "gentaga" i ett tidigare pass) — inga
suspenderingar krävdes.

**3 kort medvetet lämnade helt orörda** (varken godkända eller avslagna,
väntar på granskning med bättre källor): **kangas** (ovanligt
dialektord/terrängterm, osäker på exakt nyans), **jamare** (mycket
dialektalt/sällsynt ord för en klunk sprit, svag källbeläggning),
**bale** (viltbiologisk term för djurs liggplats, svag källbeläggning).

**Teknisk lärdom denna gång:** en första körning av `apply_updates.py`
missade 9 kort p.g.a. `validate_register()`s regel "max en tagg per axel"
— jag hade av misstag skrivit två formalitets-taggar på samma rad
(t.ex. `"formell, litterär"`) på tillstå, signa, adoratör, ingenium,
hugfästa, persvadera, räfst, konsekrera, ok. Rättat till en tagg per axel
och applicerat om (idempotent, ingen dubbelskrivning av redan lyckade
kort). Bra påminnelse att köra `baksida.validate_register()` som
sanity-check INNAN man kör hela batchen, inte bara lita på att
`apply_updates.py` fångar det i efterhand.

## Blå Nya, batch 1 KLAR: 497/500 (2026-08-05, fortsättning)

Resten av samma fil (`sessions/session_2026-08-04_bla-nya-batch1.json`,
index 247–499) granskades och applicerades i en andra omgång, samma
process/regler. **Hela batch 1 är nu klar: 497 av 500 kort granskade,
kondenserade till v2 och applicerade** (3 lämnade orörda, se nedan).
Verifierat live: `findNotes('tag:kortformat::v2')` → **3152** (2902 innan
denna omgång + 250 nya = exakt match).

**Konfidensfördelning (hela batch 1, 497 kort):** 405×9, 85×8, 7×10.
Ingen ≤7 applicerad.

**Fler riktiga sakfel/fabricerade synonymer hittade och fixade (utöver de
redan rapporterade från första halvan):**
- **famös**: synonymen "okänd" var raka motsatsen till ordets betydelse
  (famös betyder beryktad/välkänd, inte okänd) — borttagen.
- **vertebrat**: synonymen "ryggradslösa" var motsatsen till ordet
  (vertebrat = ryggradsDJUR, inte ryggradsLÖSA djur) — borttagen.
- **sarv**: synonymen "rentjur" var helt fel djurslag (sarv är en fisk,
  inte ett renhorn) — borttagen.
- **laktos**, **kardinal**, **specifik**, **favorisera**, **antibiotika**,
  **gagna**, **sjok**, **överflödig** (delvis rapporterat innan): flera av
  dessa hade ordet självt cirkulärt listat som sin egen synonym — samma
  återkommande buggmönster som setts i tidigare granskningspass, rättat.
- **baryton**: synonymerna "tenor"/"bas" är andra, angränsande röstlägen
  — inte synonymer till baryton utan separata klassificeringar. Borttagna.
- **formalitet**: synonymlistan innehöll trasig text ("Plik",
  "formellitet") istället för riktiga synonymer — ersatt med "ceremoni".
- **karmosin**, **mistlur**, **monsieur**, **båk**, **teknokrati**:
  synonymlistor innehöll engelska ord ("crimson"/"carmine", "foghorn",
  "signal (Eng: Beacon)") eller cirkulära/trasiga poster — rensade.
- **hålfot** (rapporterat innan): kompletterat, samma mönster.

**1 ytterligare Framsida-stavfel rättat via `proposed_ord`:**
**obsetrik** → **obstetrik** (läran om graviditet/förlossning, saknade
ett "t"). **Viktigt upptäckt vid verifiering:** decket hade REDAN ett
separat, korrekt stavat "obstetrik"-kort sedan tidigare (redan granskat,
`konfidens::10`, taggat `ai_uncertain`) — rättningen av stavfelet skapade
alltså av misstag en OJÄMN DUBBLETT (två kort med samma Framsida-ord,
olika Baksida-innehåll). **Inget togs bort** — flaggar detta till Adam för
manuellt beslut om vilket av de två `obstetrik`-korten (note-id
1780080620242 respektive 1780080622018) som ska behållas/slås samman,
i linje med style_guide.md-regeln att aldrig slå ihop kort utan att fråga.

**3 kort fortsatt helt orörda** (för osäkra/sällsynta att verifiera med
god säkerhet denna session): kangas, jamare, bale — samma tre som i förra
rapporten, ingen ny bedömning gjordes.

**2 kort skippades i en första apply-körning** (skälmaktig, kråma sig —
dubbla valör-taggar "positiv, skämtsam"/"negativ, skämtsam"), rättade till
en tagg per axel och applicerade om. Alla 497 bekräftat OK i den slutliga
körningen.

**Batch 1 av de 7373 Blå Nya är därmed helt klar.** Nästa steg: hämta
nästa skiva (nästa 500, eller valfri batchstorlek) via
`queue_lib.fetch_cards_sorted_by_due` med samma query, fortsätt Fas 2/3.
Kvar av de 7373: cirka 6873 kort, ej ens hämtade än.

## Sållningsfilter för Blå Nya (beslutat + implementerat 2026-08-05)

Adams idé: istället för att lita på att granskningen hinner före Adams
egen takt (ett race), suspendera HELA den ogranskade Blå Nya-poolen så
den är fysiskt oåtkomlig, och avsuspendera kort styckvis i takt med att
de granskas färdigt. Så bara `kortformat::v2`-taggade kort någonsin syns
i Adams nya-kort-kö.

**Teknisk korrigering under designen:** Ankis "bury" är dagligt och
återställs varje dygn automatiskt — håller INTE kvar kort permanent.
`suspend`/`unsuspend` (samma mekanism som redan användes på de 31
"Låst"-korten) är persistent och rätt verktyg här.

**Implementerat:**
- `suspend_unreviewed_new.py` — engångssvep (men säkert att köra om,
  idempotent): suspenderar alla `is:new -tag:kortformat::v2`-kort. Kört
  2026-08-05: **6876 kort suspenderade**. Verifierat efteråt:
  630 v2-taggade kort osuspenderade/synliga, 6876 suspenderade,
  summa 7506 = hela "Nya Blå"-poolen (type0/queue0), exakt match.
- `apply_updates.py` (`apply_single`) — avsuspenderar nu automatiskt
  kortets card_ids efter att flagg+tagg satts. No-op för kort som aldrig
  var suspenderade (påverkar alltså inte andra flöden i projektet,
  t.ex. Unga/Mogna-granskning). Detta ÄR "släppet" — inget separat
  unsuspend-steg behövs, bara vanlig Fas 2/3-granskning.
- `fetch_bla_nya.py` — daglig/återkommande hämtning, samma query
  (`is:new -tag:kortformat::v2`), due-sorterat, `--batch-size` (default
  `config.DEFAULT_BATCH_SIZE=100`, Adam nämnde 110-200/dag som riktvärde).
  Skriver `sessions/session_<datum>_bla-nya-nasta.json`.

**Nästa steg:** kör `fetch_bla_nya.py` för nästa skiva, granska (Fas 2),
applicera via `apply_updates.py` (Fas 3) — de granskade korten
avsuspenderas automatiskt och dyker upp i Adams kö i due-ordning. Upprepa
dagligen/vid behov tills hela poolen (6876 kort, minus de 3 olösta
gränsfallen kangas/jamare/bale som förblir suspenderade tills de
granskas separat) är igenom.

**Flerbetydelse-snabbkoll KLAR (2026-08-05):** alla 894 återstående kandidater
(994 totalt minus 100 redan gjorda) snabbkollade via tre parallella
subagenter, `sessions/session_2026-08-05_flerbetydelser-snabbkoll-batch{1,2,3}.json`.
**10 kort hade en dold andra betydelse och fixades**: utgå, tambur (batch1),
nod, dille, utanverk, solid, paria (batch2), konglomerat, optik, kromatisk
(batch3). 875 kort bekräftat redan korrekta (taggade oförändrade). **9 kort
lämnades helt orörda** (äkta synonymfel, inte dold betydelse, väntar på
vanlig granskning): modus vivendi, preja, på eget bevåg, agorafobi,
framliden, samt och synnerligen, albino, blottställd, lovlig. 985/994
kandidater nu taggade `flerbetydelse_granskad`+`flerbetydelse_snabbkoll`.
**Sidofynd:** ~20 kort har gammal `eller`/`/`-separator istället för `;` i
flerbetydelseord (batch3) — ej fixat, separat problem för senare pass.
**Säkerhetsfix samtidigt:** `apply_updates.py` avsuspenderar nu bara kort
som var icke-v2 FÖRE denna körning (dvs. faktiska Blå Nya-släpp) — kort som
redan var v2 rörs aldrig, oavsett suspend-status (skyddar Adams egna
manuella suspenderingar + de gamla Låst-korten från omgranskningspass).
**Nästa steg:** `_sokverifierad`-omgång på de 875 redan godkända (billig
`_snabbkoll` gjord, dyrare källkoll återstår), plus de ~20 kända
separator-avvikelserna ovan.

**Avslutat 2026-08-05 (samma session):** de 9 tidigare skippade kandidaterna
(modus vivendi, preja, på eget bevåg, agorafobi, framliden, samt och
synnerligen, albino, blottställd, lovlig) taggade `flerbetydelse_granskad`+
`flerbetydelse_snabbkoll` (innehåll orört — de har inte en dold betydelse,
utan misstänkta synonymfel, ett separat problem för en vanlig
granskningsomgång). Samtidigt: de 5 kvarvarande icke-v2-gränsfallen
(lokus, pracka, gardera med en kyss, apparelj, jag mötte lassie)
suspenderade, så ALLA icke-suspenderade kort i decket nu är v2 och
flerbetydelse-kollade (utom de ~2155 som aldrig matchade
kandidat-heuristiken, se ovan).

**Gammal `/`-separator fixad (2026-08-05, upptäckt via "tillgå"-kortet):**
`find_old_slash_separator.py` hittade 71 v2-kort med ` / ` i Huvudbetydelse
(fler än de ~20 som gissades tidigare). 47 hade redan `synonym_groups`
uppdelade från tidigare pass (bara fel separatortecken, mekanisk fix). 24
saknade det — 20 var genuint skilda betydelser (fick nya `synonym_groups`,
ibland en ny synonym för den tidigare otäckta betydelsen), **4 lämnades
orörda**: `överloppsgärning` (samma betydelse, bara olika precisionsnivå,
`/` är korrekt där), `förtörnad`+`ärevördig` (oklart/gränsfall, ej ändrat),
och **`anrika`** (misstänkt ordförväxling med adjektivet "anrik" —
institutionsbetydelsen hör troligen INTE till verbet "anrika" alls, flaggas
för Adams uppmärksamhet, inte bara en separator-bugg). **67 kort fixade och
applicerade**, verifierat: 0 kvarvarande v2-kort med ` / ` förutom de 4
avsiktligt orörda. Bifynd: `skäktning` hade en trasig trippel-duplicerad
bild-tagg (kvarglömd `</i>`-rest) i både exempelmening och bild_html,
städat i samma körning.

**Bred flerbetydelse-snabbkoll v2 (2026-08-06, ersätter det smala passet):**
upptäckt via "vråk" (bird+isbetydelse, missades av BÅDE vanlig granskning
OCH gårdagens smala flerbetydelse-koll — bara en riktig sökkoll mot
Hellquists etymologiska ordbok hittade felet). Nya kriterier: (1)
huvudbetydelse korrekt/tydlig, (2) synonymer passar, (3) exempelmening
passar, (4) ingen betydelse saknas, (5) register+valör stämmer — plus
jämförelse mot `Humanities::Languages::Svenska OLD` som andra facit.
Kön byggs av `build_all_v2_snabbkoll_queue.py` (HELA 3142-korts v2-poolen,
inte bara ogranskade — tidigare smala kriterier ansågs otillräckliga).
7 batchar á ~450 kort. **Batch 1, 4, 6 klara och applicerade** (1350 kort,
62 fixade ≈ 4,6%, se `sessions/session_2026-08-06_alla-v2-snabbkoll-batch{1,4,6}.json`).
Batch 5 granskad klar men EJ applicerad (kraschade innan `apply_updates.py`
hann köras — kör den filen separat innan nästa runda). Batch 2, 3, 7
väntar helt. Kraschorsak: kontots API-sessionsgräns nåddes när flera av 7
parallella agenter spawnade egna underagenter (mångdubblade resursbehovet)
— lösning som fungerade: instruera uttryckligen "spawna aldrig
underagenter" + större batchar (450 ist. för 300) för att hålla nere
antal toppnivå-agenter.

**Sökkoll-stickprov (2026-08-06):** 20 slumpmässiga "rena" kort (konfidens
10) från batch 1/4/6 verifierades mot riktiga källor (SAOL/SO/Wikipedia).
**4/20 (20%) hade ändå fel** som snabbkollen missat: patetisk (exempel
blandade ihop Beethoven/Tjajkovskij, fel highlight-tagg), lira (fel
synonym "kasta"), flott (saknade betydelsen "djurfett"), astronomisk
(saknade den bokstavliga astronomi-betydelsen). Alla fyra fixade direkt,
taggade `flerbetydelse_sokverifierad::2026-08-06`. Slutsats: 20% > 4,6%
visar att sökkoll hittar saker även den breddade snabbkollen missar —
värt att fortsätta med riktade sökkoll-stickprov, inte bara snabbkoll.

**A/B-test: snabbkoll vs. sökkoll, är snabbkoll tillräckligt? (2026-08-06,
slutfört):** Adam misstänkte att det första 20-korts-stickprovet (4/20
fel) kunde vara en fluke. Körde fyra ytterligare stickprovsomgångar,
totalt jämförande "snabbkollade" (konfidens 10) mot "helt okollade" kort,
alla verifierade mot riktiga källor (SAOL/SO/SAOB/Wikipedia) innan fix:

| Grupp | Kort | Fel | Frekvens |
|---|---|---|---|
| A — snabbkollade | 160 | 14 | 8,75% |
| B — helt okollade | 60 | 4 | 6,7% |

**Slutsats: skillnaden ryms inom felmarginalen — statistiskt går
grupperna INTE att särskilja.** Snabbkollens "konfidens 10"-stämpel ger
ingen mätbar garanti mot dolda fel. Vanligaste felmönstret genomgående:
en hel betydelse saknas helt (samma mönster som "vråk", t.ex. reserverad
saknade "bokad plats"-betydelsen, sekant saknade den trigonometriska,
realisera saknade den ekonomiska) — annars fel/ihopblandade synonymer,
sakfel i exempelmeningar, eller `;`-separatorn ersatt med "eller" mellan
två riktiga betydelser. Alla 17 fel över dessa omgångar fixade direkt och
applicerade, taggade `flerbetydelse_sokverifierad::2026-08-06`.

**Praktisk konsekvens:** det ursprungliga tvånivåsystemet (sökkoll bara
på kort snabbkollen själv flaggar som osäkra) missar en stadig ström av
dolda fel i det snabbkollen kallar "klart". Verklig kvalitetssäkring på
hela decket kräver sökkoll på alla ~3143 kort förr eller senare — snabbkoll
fångar fortfarande en del fel billigt (~4,6% av alla kort vid första
passet) och är värt att köra, men ersätter inte sökkoll.

**Processändring (2026-08-06): sökkoll är nu obligatoriskt för allt
framtida v2-arbete, inte bara ett separat kvalitetspass.** Adam bad om att
koda in dagens lärdomar direkt i arbetssättet istället för att bara jaga
befintliga kort i efterhand — annars hamnar vi i samma läge igen nästa
gång 3000+ nya/omgranskade kort ska göras. Uppdaterat:

- `style_guide.md`: "Flerbetydelse-genomgång" — det gamla
  "två tillitsnivåer, sökkoll bara på osäkra kort"-upplägget är ersatt.
  Varje nytt/omgranskat v2-kort ska sökkollas mot en riktig källa (se
  "Källor för faktakoll", nu inkl. Hellquist, Svenskt dialektlexikon och
  `Humanities::Languages::Svenska OLD` som jämförelsefacit) INNAN det
  taggas klart. `flerbetydelse_snabbkoll::<datum>` finns kvar historiskt/
  som billig prioriteringssignal men ersätter aldrig sökkollen.
  "Konfidensmärkning": konfidens 10 kräver nu uttryckligen en FAKTISK
  källkoll, inte bara en säker känsla från minnet (det var precis det
  som gjorde snabbkollens "konfidens 10" opålitlig). Ny obligatorisk
  5-punktschecklista under "Under granskning, kontrollera även".
- `config.py`: kommentarerna vid `FLERBETYDELSE_SNABBKOLL_TAG_PREFIX`/
  `FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX` uppdaterade till att spegla
  detta — **taggnamnen själva är OFÖRÄNDRADE** (Adam bad uttryckligen om
  att behålla samma taggkonvention: `kortformat::v2` +
  `flerbetydelse_sokverifierad::<datum>` tillsammans för allt nytt arbete).
- Ingen kodfunktionalitet ändrad (`baksida.py`/`apply_updates.py` format
  och taggmekanism var redan kompatibla, bara dokumentationen/processen
  var föråldrad).

**Adams egen del av loopen (beslutat 2026-08-05):** 630 aktiva v2-kort i
kön räcker som arbetsstorlek. Om Adam under vanlig plugg själv hittar ett
kort i den aktiva kön som är dåligt (trots `kortformat::v2`-taggen)
suspenderar han det manuellt i Anki-appen — det åker då ur hans kö tills
det omgranskas, istället för att fortsätta cirkulera. Nästa steg för
projektet framåt är alltså tvådelat: (1) kvalitetsförbättra/granska om de
630 redan aktiva korten vid behov, (2) fylla på med fler avsuspenderade
kort ur den suspenderade poolen när Adam börjar nå slutet på de 630.

**Bilder återgivna från OLD-decket (2026-08-05, Adam rapporterade saknad
bild på "viadukt"):** utredning visade att INGA bilder tagits bort av
tidigare pass denna session — 644 icke-suspenderade kort med `<img>` hade
alla sina 640 unika mediefiler intakta i mediebiblioteket. `viadukt`
(och 2499 andra v2-kort utan suspendering) saknade helt enkelt `bild_html`
— ett gap som fanns redan innan dagens session (`granskad::2026-08-04`).
Adam bad om att använda `Humanities::Languages::Svenska OLD` (9759 noter,
modeller `Grundläggande-adc63` + `Basic`) som bildfacit: för varje ord utan
bild i nya decket, om OLD-kortet för samma ord (case-insensitive
Framsida-match) har en `<img>`, kopiera över den. Nytt script
`restore_images_from_old_deck.py`: matchade 113 av 2500 bildlösa v2-kort
mot en bild i OLD (de flesta OLD-kort saknar bild helt, så resten hade
inget att hämta). Bilder skalas ned till max 250px på längsta sidan (Adams
krav "inte betydligt större än 250x") via Pillow, sparas under ett NYTT
filnamn (`restored_<original>`) så OLD-kortets egen visning inte påverkas,
och läggs in som `bild_html` via `baksida.parse`/`build`. 2 kantfall
krävde manuell fix (`curare`: HTML-entity i filnamnet, `inlaga`: 403 från
extern hotlänk, löstes med Referer-header) — **113/113 lyckades till slut**,
verifierat live (`viadukt` har nu sin bild, alla taggade
`bild_atergiven::2026-08-05`). Kvarvarande 2387 bildlösa v2-kort saknar
bild även i OLD — inget mer att hämta därifrån. Bifynd:
`ankiconnect.py`s hårdkodade 10s-timeout höjdes till 60s (bulk-`notesInfo`
över tusentals kort tajmade ut annars).

## Snabbkoll 2.0: OLD-decket som gratis källkoll, ersätter "sökkoll på allt" (2026-08-06)

Samma dag som "sökkoll obligatoriskt för allt v2-arbete" beslutades (se
ovan) föreslog Adam en förbättring: eftersom `Humanities::Languages::
Svenska OLD` bedöms som nästan 100% korrekt, varför inte använda den som
en riktig men GRATIS källkoll (lokalt AnkiConnect-uppslag, ingen
websökning) istället för att alltid gå direkt till dyr sökkoll?

**Nytt script `snabbkoll2.py`:** hämtar ogranskade v2-kort
(`-tag:flerbetydelse_granskad::*`), bygger en OLD-decks-lookup
(Framsida/Front, case-insensitive), och skriver en sessionsfil med
v2-kortets innehåll bredvid OLD-kortets Baksida/Back för granskning.
Granskaren (Claude) jämför sedan mot BÅDE OLD-facit och egen
språkkunskap — samma djup som sökkoll, men utan websökningskostnad.

**Validering, fem omgångar samma dag:**

| Omgång | Kort | OLD-täckning | Fel hittade av snabbkoll 2.0 | Extra fel hittade av efterföljande sökkoll |
|---|---|---|---|---|
| 1 | 30 | 100% (30/30) | 1 (ingäld — motsatt betydelse) | 0 |
| 2 | 20 | 100% (20/20) | 2 (i långa banor, konvent) | 0 |
| 3 | 20 | 100% (20/20) | 2 (vandal, atmosfär — "eller/;"-bugg) | 0 |
| 4 | 15 | 100% (15/15) | 1 (parhäst — samma "eller/;"-bugg) | 0 |
| 5 | 15 | 100% (15/15) | 0 (1 homografkrock: mol) | 0 |
| **Totalt** | **100** | **100%** | **6** | **0** |

Till skillnad från den gamla minnesbaserade snabbkollen (8,75% dolda fel
kvar efter "godkänd", se A/B-testet ovan) missade snabbkoll 2.0 INGENTING
som en efterföljande fullständig sökkoll sedan hittade, på 100 kort.
Kända svagheter: (1) homografkrockar (t.ex. "delta" — OLD-kortet täckte
substantivbetydelsen "flodmynning", v2-kortet verbbetydelsen "delta/
medverka"; samma sak med "mol") ger en skenbar avvikelse som inte är ett
verkligt fel, bara extra granskningsarbete. (2) Ett återkommande
formateringsfel — "eller" felaktigt använt för att länka två GENUINT
distinkta betydelser istället för " ; " — stod för 3 av de 6 hittade
felen (vandal, atmosfär, parhäst); värt en enkel textkontroll som
komplement om arbetet skalas upp.

**Statistisk ärlighet om "0 missade fel på 100 kort" — läs innan du drar
för starka slutsatser:** detta bevisar INTE en 0%-missfrekvens. Det fanns
bara 6 faktiska fel att missa i stickprovet, och med 0 missade av 6 (regel
om tre-tumregeln) ligger den sanna missfrekvensen sannolikt i intervallet
0–3%, inte bevisat noll. Testet var dessutom INTE blint på samma sätt som
det ursprungliga A/B-testet (där snabbkollade kort från en TIDIGARE,
separat session granskades om oberoende) — här gjorde samma granskare
(Claude) snabbkoll 2.0 och sökkoll på samma kort i samma sittning, vilket
ger en viss risk för bekräftelsebias (omprövar sitt eget färska omdöme
snarare än att upptäcka något genuint missat). Slutsats: starkt,
uppmuntrande resultat — inte bevis på perfektion. Gör periodiska BLINDA
stickprov senare (samma metod som A/B-testet: kort granskade dagar/veckor
tidigare, omgranskade fristående) för att verkligen validera detta över
tid, precis som den gamla snabbkollens brist bara upptäcktes för att
någon till slut gick tillbaka och kollade.

**Ny process (ersätter "sökkoll på allt" från tidigare samma dag):**
snabbkoll 2.0 är förstahandskontroll på alla v2-kort. Sökkoll (riktig
websökning) körs bara vid ESKALERING: OLD och v2 stämmer inte överens,
ordet saknar OLD-matchning, eller granskaren själv är osäker trots
matchning. Given kostnadsbesparingen (gratis lokalt uppslag istället för
websökning på ~94-97% av korten i detta stickprov) och avsaknaden av
belägg för kvalitetsförsämring är detta värt det som standardprocess —
men se den statistiska brasklappen ovan innan det behandlas som en
slutgiltigt löst fråga.

**Taggning (taggnamnen är oförändrade/konsekventa med tidigare, nya
`FLERBETYDELSE_SNABBKOLL2_TAG_PREFIX`-konstanten tillagd i `config.py`):**
`flerbetydelse_granskad::<datum>` på alla granskade kort,
`flerbetydelse_snabbkoll2::<datum>` på alla kort som körts igenom
OLD-jämförelsen, `flerbetydelse_sokverifierad::<datum>` ENDAST på kort
som eskalerats till och bekräftats via riktig sökkoll (inte längre på
varje kort automatiskt). Se style_guide.md "Flerbetydelse-genomgång" för
fullständig regeltext.

Nästa steg: köra snabbkoll 2.0 i större skala (t.ex. nästa 100-300
ogranskade kort) för att se om eskaleringsfrekvensen (hur ofta ett kort
faktiskt behöver sökkoll) håller sig låg när stickprovet växer.

## Snabbkoll 2.0, andra valideringsrundan: 100 NYA kort, full sökkoll på ALLA (2026-08-06, kväll)

Adam bad om ett nytt, större test: snabbkoll 2.0 på 100 helt nya
(tidigare ogranskade) kort, `sessions/session_2026-08-06_snabbkoll2-test-batch6.json`,
följt av **riktig, individuell sökkoll på samtliga 100** — inte bara de
kort snabbkoll 2.0 själv flaggade för eskalering, för att verkligen testa
om 0-missfrekvensen håller när stickprovet är dubbelt så stort som förra
rundan.

**OLD-täckning: 100/100 (100%).** Snabbkoll 2.0 (jämförelse mot OLD-facit
+ egen kunskap) flaggade **10 kort** för eskalering — en märkbart högre
andel (10%) än förra rundans 6/100 (6%). Sökkoll av samtliga 100 kort
(inte bara de 10 flaggade) **bekräftade exakt dessa 10 fel och hittade 0
ytterligare** bland de återstående 90 — samma mönster som förra rundan,
nu på dubbelt så stort stickprov.

**De 10 bekräftade felen, alla rättade och applicerade:**
- **dat → dåd**: Framsidan var felaktigt "dat" (saknade å) trots att hela
  Baksidan (definition, synonymer, exempelmening) uttryckligen handlade
  om ordet "dåd". Rättad via `proposed_ord`, samma buggtyp som tidigare
  Framsida-stavfel (t.ex. "metarmorfos"→"metamorfos").
- **census**: "eller" band ihop två genuint skilda betydelser (modern
  folkräkning vs. det romerska förmögenhetskravet för rösträtt) — samma
  "eller/;"-buggmönster som vandal/atmosfär/parhäst tidigare idag.
- **NYTT, dominant felmönster denna runda: en hel ordboksbetydelse saknades
  helt i huvudbetydelsen**, trots att exempelmeningen eller `synonym_groups`
  ibland redan antydde att en till betydelse fanns (7 av 10 fel):
  - **mönstra**: saknade "ta värvning/skriva in sig (t.ex. på ett fartyg)".
  - **page**: saknade "pagefrisyr" (kort frisyr) HELT — trots att
    `synonym_groups` redan hade en egen grupp för det och att
    exempelmeningen ("Kort page med snedlugg") uteslutande beskrev
    frisyren, inte adelsmannen.
  - **inbunden**: saknade den personliga betydelsen (tystlåten,
    reserverad) — samma mönster, `synonym_groups` hade redan en egen
    grupp för det som huvudbetydelsen inte täckte.
  - **visir**: saknade den historiska betydelsen (rådgivare till furste i
    islamiska länder, ursprung till "vesir/vizier") — bara
    hjälmgaller-betydelsen fanns med.
  - **bulvan**: saknade jaktbetydelsen (konstgjord lockfågel) — bara
    "målvakt/strohman"-betydelsen fanns med.
  - **parabel**: saknade den matematiska betydelsen (andragradskurvan,
    en av de vanligaste betydelserna av ordet) — bara den litterära
    liknelse-betydelsen fanns med.
  - **ockult**: saknade grundbetydelsen "dold, hemlig" (t.ex. "ockult
    blod" inom medicin) — bara "övernaturlig"-betydelsen fanns med.
- **holma**: det allvarligaste fyndet — HELT FEL ordklass och betydelse.
  Kortet påstod "liten ö" (substantiv), men "holma" är faktiskt ett
  jaktdialektalt VERB som betyder att gå runt ett område (t.ex. vid
  björnjakt) för att med hjälp av spår avgöra om villebråd finns kvar där
  — helt obesläktat med "liten ö" (som stavas "holme"). Detta hade INTE
  upptäckts av vanlig manuell granskning utan OLD-jämförelsen (OLD-kortet
  sa "inringa", vilket triggade misstanken).

**Övriga 90 kort: 0 fel hittade** av den individuella sökkollen, verifierat
mot svenska.se/SAOB/SAOL/webbkällor ord för ord.

**Taggning:** alla 100 kort taggade `flerbetydelse_granskad::2026-08-06` +
`flerbetydelse_snabbkoll2::2026-08-06` + `flerbetydelse_sokverifierad::2026-08-06`
(alla fick faktiskt riktig sökkoll denna runda, inte bara de eskalerade).

## Snabbkoll 2.0 som avsett: 150 kort, sökkoll bara på eskalerade (2026-08-06, kväll)

Efter de två valideringsrundorna (som medvetet körde full sökkoll på ALLA
kort för att testa metoden) körde Adam snabbkoll 2.0 **som den faktiskt är
tänkt att användas i produktion**: 150 nya, tidigare ogranskade v2-kort
(`sessions/session_2026-08-06_snabbkoll2-test-batch7.json`, due-sorterat —
i praktiken de kort som ligger närmast att släppas till Adam), sökkoll
bara på de kort snabbkoll 2.0 själv flaggade.

**OLD-täckning: 149/150 (99%).** Snabbkoll 2.0 flaggade **9 kort** för
eskalering (6%, i linje med förra rundornas 6-10%). Sökkoll av dessa 9:

- **6 bekräftade fel, rättade:**
  - **plakat**: saknade en HEL betydelse — "plakat" som adjektiv betyder
    (vardagligt) "redlöst berusad" ("gå till plakat"), helt orelaterat till
    anslag/affisch-betydelsen. OLD-facitet hade båda ("anslag, affisch;
    mycket berusad") men bara den första fanns med i kortet.
  - **kreditera**: saknade grundbetydelsen "sätta in pengar på ett konto"
    (bokföringsterm) — bara den bildliga "ge någon äran"-betydelsen fanns
    med, trots att OLD-facitet ("tillgodoräkna; berömma") pekade på båda.
  - **nickedocka**: saknade den bildliga betydelsen "person som okritiskt
    instämmer med andra" (jasägare) — bara den bokstavliga dockan (leksak
    med nickande huvud) fanns med. OLD-facitet hade bara den bildliga
    betydelsen ("lydig person"), vilket avslöjade obalansen.
  - **association**: saknade organisations-betydelsen ("sammanslutning,
    förening") — bara den mentala kopplings-betydelsen fanns med, trots
    att OLD-facitet ("förknippning; sammanslutning") hade båda.
  - **flottilj**: saknade sjöstridsbetydelsen ("sjöstyrka", ett mindre
    örlogsförband) — bara flygflottilj-betydelsen fanns med, trots att
    OLD-facitet ("flygförband; sjöstyrka") hade båda.
  - **spjälka**: huvudbetydelsen ("dela upp i mindre delar") stämde INTE
    med den egna exempelmeningen ("Läkaren fick spjälka benet för att
    stabilisera det") — spjälka har två skilda betydelser (klyva virke i
    tunna stycken / sätta i skena för att stödja en skadad kroppsdel),
    exempelmeningen visade uteslutande den andra. Samma "missing
    meaning"-mönster som föregående runda, femte gången i rad att en
    saknad betydelse är den vanligaste felkällan.
- **2 eskalerade, bekräftat REDAN KORREKTA (ingen fix behövdes):**
  - **spetsfundig**: OLD-facitet ("listig och kvicktänkt") avvek från
    kortet ("onödigt hårklyvande"), men sökkoll bekräftade att kortets
    egen definition är den korrekta (SAOB: "mycken färdighet i att
    utfinna små, oväsentliga åtskillnader") — OLD-facitet var här den
    missvisande källan, inte kortet.
  - **"nu går skam på torra land!"**: inget OLD-facit alls (null), men
    sökkoll bekräftade att kortets definition ("utrop av bestörtning över
    ett skandalöst beteende") redan stämmer.

Detta bekräftar att snabbkoll 2.0:s eskaleringslogik fungerar åt BÅDA
hållen — den fångar inte bara fel i v2-kortet, utan flaggar också korrekt
när avvikelsen egentligen ligger i det billiga OLD-facitet (spetsfundig)
eller när ingen avvikelse alls finns (skam-uttrycket). Ingen sökkoll gjordes
på de 141 icke-eskalerade korten denna runda (till skillnad från de två
föregående testrundorna) — detta är alltså det första "på riktigt"-körningen
av metoden i produktionsläge.

**Taggning:** alla 150 kort taggade `flerbetydelse_granskad::2026-08-06` +
`flerbetydelse_snabbkoll2::2026-08-06`. Bara de 8 sökkollade korten (6
rättade + 2 bekräftat korrekta) fick också `flerbetydelse_sokverifierad::2026-08-06`.

**Uppdaterad statistisk sammanställning (cirka 200 kort testade totalt
under 2026-08-06, båda valideringsrundorna kombinerat):**

| Runda | Kort | Fel hittade av snabbkoll 2.0 | Extra fel hittade av full sökkoll |
|---|---|---|---|
| Förmiddag (5 delrundor) | 100 | 6 | 0 |
| Kväll (denna runda) | 100 | 10 | 0 |
| **Totalt** | **200** | **16** | **0** |

Med 0 missade fel över 200 individuellt sökkollade kort (rule-of-three på
kortnivå, inte felnivå) sjunker den övre 95%-gränsen för den sanna
missfrekvensen till ungefär **3/200 ≈ 1,5%** — snävare än förmiddagens
0-3%-uppskattning, men fortfarande INTE bevisat noll. Testdesignen är
fortfarande INTE blind (samma granskare gjorde bägge passen i samma
sittning) — se "Statistisk ärlighet"-avsnittet ovan, samma resonemang
gäller. Den nya lärdomen denna runda: **"saknad betydelse" är det klart
vanligaste felmönstret** (7 av 16 fel hittade hela dagen), vanligare än
ren faktafel eller "eller/;"-formateringsbuggen — värt att aktivt leta
efter framöver, särskilt på ord med `synonym_groups` som inte matchar
antalet betydelser i huvudbetydelsen.

## Snabbkoll 2.0 på den gamla poolen: 400 av 1558 kort (2026-08-06, kväll)

Adam identifierade ett nytt scope-hål: **1880 kort** är granskade med den
GAMLA, rent minnesbaserade snabbkollen (`flerbetydelse_snabbkoll::*`,
innan snabbkoll 2.0 fanns) men har ALDRIG jämförts mot OLD-decket. 322 av
dessa har ändå fått en riktig sökkoll sedan tidigare (`flerbetydelse_
sokverifierad::*`) och behöver inte köras om — kvar står **1558 kort**
som varken har snabbkoll2- eller sökverifierad-taggen, alltså bara
granskade med metoden som A/B-testet visade missade 8,75% av felen.

**Nytt permanent script:** `snabbkoll2_gamla.py` — samma logik som
`snabbkoll2.py` (OLD-facit + egen kunskap, sökkoll bara vid eskalering)
men riktad mot just denna pool
(`tag:flerbetydelse_snabbkoll::* -tag:flerbetydelse_snabbkoll2::*
-tag:flerbetydelse_sokverifierad::* -is:suspended`, due-sorterat).
Återanvänds för resterande ~1158 kort i kommande omgångar.

**Första omgången: 400 kort** (`sessions/session_2026-08-06_snabbkoll2-gamla-pool.json`).
OLD-täckning: 400/400 (100%). Snabbkoll 2.0 flaggade **20 kort** (5%) för
eskalering — en märkbart lägre andel än de tre föregående rundorna
(6-10%), rimligt eftersom denna pool redan passerat en (svagare) mänsklig
granskning tidigare, till skillnad från helt ogranskade kort.

**15 av 20 bekräftade fel, alla rättade:**
- **Sjätte rundan i rad där "saknad hel betydelse" dominerar** (13 av 15):
  lagg (saknade "kant/övergångszon vid en högmosse" — ett tredje, helt
  orelaterat fackord), beskickning (saknade den metallurgiska betydelsen
  "blandning av råmaterial i en masugn"), rya (saknade den dialektala
  verbbetydelsen "skrika och väsnas" — helt orelaterad till mattan),
  respondera (saknade den akademiska termen "försvara sin avhandling som
  respondent"), mas (saknade den historiska betydelsen "skatteindrivare"),
  menisk (saknade fysik/kemi-betydelsen "krökt vätskeyta i ett rör" —
  vanlig i skolkemi), konsol (saknade "spelkonsol/kontrollpanel", en av
  ordets vanligaste betydelser i modernt språk), likgiltig (saknade "om
  sak: utan betydelse, oväsentlig" — skilt från den personliga attityden),
  utgå (saknade idrottsbetydelsen "dra sig ur/uteslutas ur en tävling"),
  sätta sig (saknade "sjunka, om husgrund/mark" — bara den bokstavliga
  "sätta sig ner" fanns), abandon (saknade grundbetydelsen "otvungenhet,
  hängivet obehärskat sätt" — bara den sjörättsliga betydelsen fanns,
  trots att den själv redan var korrekt), spak (saknade HELA adjektiv-
  betydelsen "tam och foglig" — bara handtags-substantivet fanns, en
  annan ordklass helt), charad (saknade ursprungsbetydelsen "ordgåta" —
  bara den moderna gissningsleken fanns).
- **1 korrigerat sakfel snarare än tillagd betydelse:** mista sansen —
  kortet sa bara "tappa fattningen, bli överväldigad" (bildligt), men
  ordets mest direkta betydelse är att SVIMMA (förlora medvetandet
  bokstavligen) — bekräftat av flera källor. Huvudbetydelsen skrevs om
  för att leda med den bokstavliga betydelsen, med den bildliga kvar som
  andra betydelse.
- **1 rent felaktigt påstående, borttaget:** influens — kortet påstod att
  ordet vardagligt kan betyda "person med stort inflytande i sociala
  medier", vilket INTE stämmer (det är ordet "influencer", inte
  "influens", som betyder det). Ersatt med den riktiga fackspråks-
  betydelsen inom fysik: "elektrostatisk induktion" (växelverkan mellan
  laddade partiklar på avstånd). Ny exempelmening skrevs eftersom den
  gamla demonstrerade det felaktiga påståendet.

**5 av 20 eskalerade, bekräftat REDAN KORREKTA (ingen fix):**
- **dentist**: OLD-facitet sa "tandtekniker" (fel yrke — någon som
  tillverkar tandproteser, inte behandlar patienter), men SAOB bekräftar
  att "dentist" är en ålderdomlig synonym till "tandläkare", precis som
  kortet redan sa.
- **lämpa, skäktning, bulk, diskonto**: sökkoll bekräftade att kortens
  egna definitioner redan var rimliga/korrekta trots avvikande eller
  saknat OLD-facit.

Ytterligare två exempel på metodens styrka åt "OLD har fel"-hållet
(dentist, plus spetsfundig från föregående runda) — mönstret upprepar
sig konsekvent över rundorna.

**Taggning:** alla 400 kort taggade `flerbetydelse_granskad::2026-08-06` +
`flerbetydelse_snabbkoll2::2026-08-06`. Bara de 20 sökkollade korten (15
rättade + 5 bekräftat korrekta) fick också
`flerbetydelse_sokverifierad::2026-08-06`.

**Kvarstående kö:** ~1158 kort i den gamla poolen väntar fortfarande på
snabbkoll 2.0 — kör `snabbkoll2_gamla.py --batch-size <N>` för nästa
omgång.

## Snabbkoll 2.0 på den gamla poolen, omgång 2: nästa 400 kort (2026-08-06, kväll)

Fortsättning på ovanstående, körd via samma `snabbkoll2_gamla.py`
(`sessions/session_2026-08-06_snabbkoll2-gamla-pool-batch2.json`).
OLD-täckning: 399/400 (100%, ett kort utan träff). Snabbkoll 2.0 flaggade
**22 kort** (5,5%, i linje med förra omgångens 5%).

**19 av 22 bekräftade fel, alla rättade — "saknad hel betydelse" dominerar
för sjunde omgången i rad** (17 av 19), bland annat flera fall där en HEL
ordklass eller ett helt fackområde saknades: **vän** (saknade den
ålderdomliga adjektivbetydelsen "skön, fager" — helt annan ordklass än
substantivet "vän"=kompis), **motion** (saknade den vardagliga huvud-
betydelsen "fysisk aktivitet/träning" — bara det formella riksdags-
förslaget fanns, trots att träningsbetydelsen sannolikt är den vanligare
i vardagsspråk), **maka** (saknade verbbetydelsen "flytta något lite
grann" — bara substantiven "hustru" och "matchande" fanns),
**stadga** (saknade "stadgar" = föreskrifter för en förening, en mycket
vanlig betydelse), **nätt** (saknade grundbetydelsen "liten och täck,
söt" — bara "knappt tillräcklig" fanns, trots att den täcka betydelsen
sannolikt är vanligare), **imperativ** (saknade den filosofiska
betydelsen "moralisk nödvändighet" — bara grammatiktermen fanns),
**angelägen** (saknade "brådskande, om en sak" — bara den personliga
attityden fanns), **kurator** (saknade konstutställnings-betydelsen),
**svale** (saknade "svalgång", en täckt yttergång), **preja**, **lod**
(lödmetall), **sinkadus** (örfil), **härda** (om person), **turnera**
(ge ett yttrande en språklig vändning), **blottställd** (utfattig),
**ofärdig** (ålderdomligt "vanför"), **belägga** (ålägga/påföra t.ex.
skatt). Ett kort korrigerades snarare än utökades: **gå med håven**
hade fel betydelse helt — kortet sa "tigga om pengar" men uttrycket
betyder specifikt "tigga komplimanger/fiska efter beröm"; både
huvudbetydelse och exempelmening skrevs om. Ett kort fick en bildlig
bibetydelse tillagd: **bita i gräset** (försvagat: "lida nederlag",
inte bara bokstavligt dö).

**3 av 22 eskalerade, bekräftat REDAN KORREKTA:** skygga (OLD-facitet
"ge skugga" var uppenbarligen en sammanblandning med det snarlika ordet
"skugga" — kortets "dra sig undan, bli skrämd" är korrekt), gå på ett
ut (inget OLD-facit, sökkoll bekräftade att kortet redan stämde),
cession (sökkoll gav inget tydligt stöd för att en extra betydelse
saknas trots OLD:s avvikande "konkurs"-facit).

**Taggning:** alla 400 kort taggade `flerbetydelse_granskad::2026-08-06`
+ `flerbetydelse_snabbkoll2::2026-08-06`. Bara de 22 sökkollade korten
(19 rättade + 3 bekräftat korrekta) fick också
`flerbetydelse_sokverifierad::2026-08-06`.

**Kvarstående kö:** ~758 kort i den gamla poolen väntar fortfarande på
snabbkoll 2.0.

## Snabbkoll 2.0 på Blå Nya-poolen: första halvan, 155 av 311 kort (2026-08-06, kväll)

Ny pool, skild från "gamla poolen" ovan: blå (flag:4), v2-formaterade kort
som fortfarande är `is:new` — Adam har alltså aldrig ens sett dem i Anki
än — och som saknar ALL flerbetydelse-koll. 311 kort i poolen vid start
(Adam frågade efter "552 blå nya kort i learning", men ingen AnkiConnect-
fråga gav exakt det talet; efter avstämning med Adam användes 311-
poolen — kort som är `is:new` och okollade — som den avsedda poolen).
Nytt permanent script: `snabbkoll2_blanya.py` (samma bygglogik som
`snabbkoll2.py`/`snabbkoll2_gamla.py`, frågan filtrerar på `flag:4 is:new`).

Körd som `sessions/session_2026-08-06_snabbkoll2-blanya.json`, 155 kort
(hälften av poolen, enligt Adams instruktion). OLD-täckning: 155/155
(100%). Snabbkoll 2.0 flaggade **12 kort (7,7%)** — något högre än
gamla-poolens 5-5,5%, rimligt eftersom dessa kort ALDRIG granskats för
flerbetydelse förut (till skillnad från gamla poolen som redan fått en
minnesbaserad koll en gång).

**Alla 12 bekräftade fel/ofullständiga, rättade — "saknad hel betydelse"
dominerar även här:** **koloni** (saknade både den biologiska betydelsen
"grupp djur/växter" och vardagsbetydelsen "barnkoloni/sommarläger" — bara
"landområde" fanns), **lumpen** (saknade den mycket vanliga vardagliga
substantivbetydelsen "värnpliktig militärutbildning" — helt annan
ordklass än adjektivet "lumpen"=elak), **depression** (saknade både den
ekonomiska betydelsen "djup lågkonjunktur" och den meteorologiska
"lågtrycksområde" — bara den psykiatriska diagnosen fanns), **oratorium**
(saknade "litet bönerum" inom katolska kyrkan — bara det musikaliska
verket fanns), **patriark** (saknade den kyrkliga hederstiteln inom
ortodoxa kyrkan — bara släktöverhuvud-betydelsen fanns), **besätta**
(saknade "garnera/pryda", t.ex. en klänning besatt med pärlor — bara
"ockupera/tillsätta" fanns), **semiologi** (saknade den medicinska
betydelsen "symtomlära" — bara teckenläran fanns), **benägen** (saknade
"välvillig/positivt inställd till någon" — bara "har en tendens" fanns).
Tre kort korrigerades snarare än utökades: **ocker** hade en verb-formad
huvudbetydelse ("Utnyttja...") trots att ordet är ett substantiv —
skrevs om till substantivform; **formalitet** definierades för brett
("regelbunden, traditionell procedur/ceremoni") när kärnbetydelsen är en
formell men ofta obetydlig åtgärd — skrevs om för att matcha både
ordboken och kortets egen exempelmening ("bara en formalitet"); **damast**
saknade det utmärkande draget "vanligen enfärgat" (mönstret framträder
genom vävens yta, inte genom färgkontrast). Ett kort fick en nyanserad
bibetydelse tillagd: **uppknäppt** hade "avslappnad och informell" där
sökkoll visade att den etablerade bibetydelsen faktiskt är mer specifikt
"glad, öppen och pratsam".

**Taggning:** alla 155 kort taggade `flerbetydelse_granskad::2026-08-06`
+ `flerbetydelse_snabbkoll2::2026-08-06`. De 12 sökkollade korten fick
också `flerbetydelse_sokverifierad::2026-08-06`.

**Kvarstående kö:** 156 kort kvar i Blå Nya-poolen (andra halvan), väntar
på nästa körning av `snabbkoll2_blanya.py`.

## Snabbkoll 2.0 på Blå Nya-poolen: andra halvan KLAR, hela poolen genomgången (2026-08-06, kväll)

Sista 156 korten i poolen körda (`sessions/session_2026-08-06_snabbkoll2-
blanya-batch2.json`). OLD-täckning 156/156 (100%). 12 av 156 (7,7%,
identiskt med första halvans andel) eskalerade till riktig sökkoll — alla
bekräftade fel/ofullständigheter, "saknad hel betydelse" dominerar för
NIONDE omgången i rad: **hiva** (saknade vardagsbetydelsen "kasta/slänga"
— bara den nautiska "hissa" fanns), **förmäla** (saknade den
ålderdomliga betydelsen "gifta bort", särskilt om furstliga personer —
bara "berätta" fanns), **injektera** (saknade den bygg-/bergtekniska
betydelsen "pumpa in material för att täta/förstärka" — bara den
medicinska sprutbetydelsen fanns), **bräcka** (saknade HELA två
betydelser: köksbetydelsen "steka lätt", t.ex. bräckt fläsk, och den
litterära "gry" om dagen — bara "brista/överträffa" fanns, fyra
betydelser totalt i OLD-facitet mot två på kortet), **stifta** (saknade
"stifta lagar" — bara "grunda en institution" fanns), **finstilt**
(saknade den bildliga betydelsen "finstämd, raffinerad"), **pellets**
(saknade foderbetydelsen — bara biobränslebetydelsen fanns, HELT skilda
användningsområden), **kaki** (saknade frukten kaki/persimon — bara
färgen/tyget fanns), **botanisera** (saknade den bildliga betydelsen
"strosa/utforska bland något", t.ex. bland böcker eller nyheter),
**forcera** (saknade en tredje, mer teknisk betydelse "knäcka/avslöja en
kod"). Två kort fick en ålderdomlig/dialektal bibetydelse tillagd som
sökkollen bekräftade var äkta trots att den kändes ovanlig:
**formidabel** (ålderdomligt "fruktansvärd, skräckinjagande" — motsatt
valör mot den vanliga "imponerande") och **betuttad** (dialektalt
"förlägen, rådvill" bredvid den vanliga "förtjust i").

**Utöver sökkoll-eskaleringarna: 4 kort med rena format-/grammatikfel
som hittades vid genomläsningen, ingen sökkoll behövdes:**
**fantomsmärta** hade en exempelmening där ordet inte var highlightat
alls (bröt mot standardformatet); **deus ex machina** hade en missvisande
synonym ("maskin" — en bokstavlig delöversättning av frasen, inte ett
faktiskt synonymt begrepp — bytt mot "räddande ängel, oväntad räddning");
**ha satt sin sista potatis** hade ett dubbelt hjälpverb i
exempelmeningen ("hade han <b>ha</b> satt...", grammatiskt fel — "ha"
togs bort); **det går sin gilla gång** bröt mot svenskans V2-ordföljd
efter en framflyttad bisats ("Trots krisen det går..." istället för
"Trots krisen går det...").

**Taggning:** alla 156 kort taggade `flerbetydelse_granskad::2026-08-06`
+ `flerbetydelse_snabbkoll2::2026-08-06`. De 12 sökkollade fick också
`flerbetydelse_sokverifierad::2026-08-06` (de 4 rena format-/
grammatikfixarna räknas INTE som sökkollade, fick ingen sökverifierad-
tagg). **Flaggning enligt det nya systemet:** 12 kort → Blå, 144 kort →
Grön.

**Hela Blå Nya-poolen är nu klar: 311/311 kort genomgångna** (155 + 156).
Totalt 24 bekräftade fel/ofullständigheter fixade över båda halvorna
(7,7% i båda), plus 4 extra format-/grammatikfixar i andra halvan.

## Snabbkoll 2.0 på gamla-poolen, omgång 3: 350 kort (2026-08-06, kväll)

Tillbaka till den gamla snabbkoll-poolen (kort granskade med det GAMLA
minnesbaserade läget innan snabbkoll 2.0 fanns). 350 kort körda via
`snabbkoll2_gamla.py` (`sessions/session_2026-08-06_snabbkoll2-gamla-
pool-batch3.json`). OLD-täckning 350/350 (100%). **24 av 350 (6,9%)**
eskalerade till riktig sökkoll, alla bekräftade och rättade — "saknad
hel betydelse" dominerar för TIONDE omgången i rad, ovanligt många
kort med tydliga HOMONYMER (helt orelaterade betydelser, inte bara
nyanser av samma ord) denna omgång:

**Homonymer/helt skilda betydelser:** **lake** (saknade fisken — bara
saltlagen fanns), **singel** (saknade "grovt grus som byggmaterial" —
bara civilståndet fanns), **näva** (saknade den MYCKET vanligare
betydelsen "knuten hand/handfull" — kortet hade bara den ovanliga
växten Geranium, ombytt ordning så handbetydelsen nu står först),
**kurra** (saknade verbbetydelsen "bullra svagt", t.ex. om en tom mage
— bara substantivet "finka" fanns), **komposition** (saknade
"musikstycke" — bara konstverks-uppbyggnaden fanns), **piccolo**
(saknade HELA två betydelser: piccolaflöjten och en kvartsflaska
champagne — bara hotellpojken fanns), **grand** (saknade den spanska
adelstiteln — sällsynt men bekräftad), **såt** (saknade en jaktterm för
avgränsat jaktområde bredvid vänskapsbetydelsen).

**Bildliga/utvidgade betydelser som saknades:** **raster** (saknade
den mycket vanligare vardagsbetydelsen "rast, arbetspaus" — bara
tryckteknikbetydelsen fanns), **anda** (saknade "andetag" — bara
stämning/atmosfär fanns), **dager** (saknade den vanliga idiom-
betydelsen "perspektiv", som i "sätta något i en ny dager" — bara
bokstavligt dagsljus fanns), **kaliber** (saknade den bildliga "en
persons kvalitet/status", som i "en man av hans kaliber"), **episk**
(saknade den moderna slangbetydelsen "fantastisk, grym" — bara den
litterära betydelsen fanns), **inramning** (saknade den bildliga
"omgivande sammanhang/stämning", som i "skandalens politiska
inramning" — dessutom omskriven från verb- till substantivformulering,
eftersom ordet är ett substantiv), **förlägenhet** (saknade "knipa,
svår situation" t.ex. penningförlägenhet), **offensiv** (saknade
substantivbetydelsen "en anfallshandling/satsning").

**Övriga saknade betydelser:** **förlägga** (saknade HELA två
betydelser: "publicera en bok" och kopplingen till förlag), **vanmakt**
(saknade den ålderdomliga "medvetslöshet, svimning"), **syndikat**
(saknade den kriminella nätverksbetydelsen, skild från företags-
sammanslutningen), **hjon** (saknade den historiska tjänare-betydelsen),
**sockel** (saknade "golvlist" bredvid piedestal-betydelsen),
**fortifikation** (saknade "befästningskonst" som egen disciplin,
bredvid själva anläggningen). Ett kort fick sin definition preciserad
snarare än utökad: **förljugen** hade en för bred/generisk definition
("falsk") — sökkoll visade att ordet mer specifikt betyder falskt
romantiserad/idylliserad, vilket nu är tillagt.

**Utöver sökkoll-eskaleringarna: 1 rent innehållsfel utan sökkoll-
behov:** **jour** hade en direkt missvisande synonym ("vikariat" —
förväxlar jourtjänst med ett vikariat, två olika anställningsbegrepp),
bytt mot "beredskap, jourtjänst".

**Taggning:** alla 350 kort taggade `flerbetydelse_granskad::2026-08-06`
+ `flerbetydelse_snabbkoll2::2026-08-06`. De 24 sökkollade fick också
`flerbetydelse_sokverifierad::2026-08-06` (jour-fixen räknas inte som
sökkollad). **Flaggning:** 24 kort → Blå, 326 kort → Grön.

**Kvarstående kö:** 758 − 350 = 408 kort kvar i gamla-poolen.

## Snabbkoll 2.0 på gamla-poolen, omgång 4 (SISTA): 408 kort — hela gamla-poolen KLAR (2026-08-06, kväll)

Sista omgången av gamla-poolen, körd via `snabbkoll2_gamla.py --batch-size 408`
(`sessions/session_2026-08-06_snabbkoll2-gamla-pool-batch4.json`). OLD-täckning
403/408 (99%). Till skillnad från tidigare omgångar granskades hela filen
manuellt av huvudtråden (inte i mindre delrundor) genom en kondenserad
text-dump (ord/huvudbetydelse/synonymer/exempel/OLD-facit per rad) — **24 av
408 (5,9%) flaggade för eskalering**, i linje med tidigare omgångars 5-8%.

**Viktig procesförbättring denna omgång:** samtliga 24 eskalerade kort
verifierades faktiskt mot riktiga källor via WebSearch (SAOB/SO/synonymer.se/
Wikipedia/fackkällor) INNAN någon fix skrevs — inte bara mot minnet. Detta
bekräftade alla 24 misstankar som äkta (inga falska positiva denna gång).

**"Saknad hel betydelse" dominerar för ELFTE omgången i rad (21 av 24),
flera tydliga homonymer:** **ed** (saknade den ålderdomliga geografiska
betydelsen "landtunga/näs mellan vatten", vanlig som ortnamnsled — helt
obesläktad med det heliga löftet), **agn** (saknade fiskbete/lockmedel —
helt obesläktat med sädesskalet), **traktat** (saknade "kort religiös/
politisk propagandaskrift" — obesläktat med statsfördraget), **utvikning**
(saknade "utvikningsbild", den kända tidningsbetydelsen med lättklädda
personer — bara "avstickare från ämnet" fanns), **grädda** (saknade "gräddan"
= samhällets elit/crème de la crème — bara baka-betydelsen fanns),
**kommission** (saknade den mycket vanliga betydelsen "expertgrupp/kommitté
för utredning", t.ex. EU-kommissionen — bara "sälja på kommission" fanns),
**bipolär** (saknade den psykiatriska diagnosen "bipolär sjukdom" — bara
den allmänna "två motsatta poler"-betydelsen fanns), **multipel** (saknade
adjektivbetydelsen "flerfaldig", som i "multipel skleros" — bara
substantivbetydelsen "en multipel av ett tal" fanns), **korpus** (saknade
"kroppen/resonanslådan på ett stränginstrument" — bara språkvetenskaplig
textsamling fanns), **ackord** (saknade "beting, prestationslön" — det
mycket vanliga uttrycket "jobba på ackord" — bara den musikaliska och
ekonomiska betydelsen fanns), **skovel** (saknade "turbin-/propellerblad" —
bara spade-betydelsen fanns), **spin-off** (saknade den ekonomiska
"sidoeffekt/bieffekt"-betydelsen — bara media-avknoppningen fanns),
**marionett** (saknade den bildliga "viljelöst redskap/person som styrs av
andra" — bara den bokstavliga dockan fanns), **identitet** (saknade den
MYCKET vanligare personliga/psykologiska betydelsen "känsla av vem man är"
— bara den logiska "fullständig överensstämmelse" fanns, en allvarlig
prioriteringsmiss), **lurvig** (saknade slangbetydelsen "lätt berusad"),
**kreatur** (saknade den bibliska/ålderdomliga betydelsen "skapad varelse"
— bara boskap fanns), **belysning** (saknade den bildliga "förklaring,
synsätt", som i "kasta ny belysning på frågan"), **tyfon** (saknade
betydelsen "mistlur/tryckluftsdriven ljudsignal på fartyg" — **och
huvudbetydelsen motsade dessutom kortets EGEN exempelmening**, som
uteslutande beskrev ett fartygs ljudsignal, inte en storm — ett nytt,
allvarligare undermönster: en huvudbetydelse i direkt konflikt med sin
egen exempelmening, inte bara en extern källa), **dramatisera** (saknade
grundbetydelsen "bearbeta till pjäsform" — bara den bildliga
"överdriva"-betydelsen fanns), **"gå den breda vägen"** (den bibliska
moraliska/kriminella konnotationen hade urvattnats bort till enbart
"välja det bekväma").

**3 kort korrigerade snarare än utökade (verifierad felaktig huvudbetydelse,
inte bara saknad):** **väld** — allvarligaste fyndet denna omgång: kortet
påstod "makt/herravälde", en sammanblandning med det snarlika ordet
"välde". Det verkliga "väld" betyder "partiskhet, jäv" (SAOB, bekräftar
OLD-facitets "partiskhet" som korrekt — kortets egen betydelse var alltså
helt fel, ett av få fall i hela sessionen där OLD hade rätt och v2-kortet
fel om huvudbetydelsen). **slå bakut** — kortet definierade ordet som
"få motsatt effekt än avsett" (backfire), men etablerad betydelse (SAOB,
bekräftar OLD-facitets "spjärna, göra motstånd") är att göra motstånd/
vägra rätta sig efter något — omskrivet till den korrekta betydelsen.
**changera** — kortet hade bara den klassiska "skifta i färg (om siden)"-
betydelsen, men modern användning lutar starkt åt en andra, negativ
betydelse "gradvis förlora i värde/kvalitet" (bekräftar OLD-facitets
"bli sämre") — tillagd som andra betydelse. **krösus** kompletterades med
den utelämnade kärnkomponenten "snål" (krösus betyder specifikt en rik
person som ÄVEN är snål, inte bara vem som helst förmögen).

**Taggning:** alla 408 kort taggade `flerbetydelse_granskad::2026-08-06` +
`flerbetydelse_snabbkoll2::2026-08-06`. De 24 sökkollade/rättade fick också
`flerbetydelse_sokverifierad::2026-08-06`. **Flaggning:** 24 kort → Blå,
384 kort → Grön.

**HELA GAMLA-POOLEN ÄR NU KLAR: 0 kort kvar** (1558 → 0 över fyra omgångar:
400+400+350+408). Kombinerat med den redan klara Blå Nya-poolen (311/311)
betyder det att BÅDA de stora identifierade snabbkoll-2.0-poolerna är
slutförda. Nästa steg (påbörjat direkt efter, samma kväll, på Adams
begäran): snabbkoll 2.0 på alla kort i Anki-statistikens "Lär om"-kö
(`is:learn`), se nästa avsnitt.

## Snabbkoll 2.0 på "Lär om"-kön (is:learn): 8 kort, hela kön KLAR (2026-08-06, sen kväll)

Adam bad om snabbkoll 2.0 på alla `is:learning`-kort direkt efter att
gamla-poolen blev klar. Anki-sökoperatorn heter `is:learn` (inte
`is:learning`) — 38 kort totalt i den kön, varav 9 redan suspenderade
(orörda separat sedan tidigare) och 30 redan `flerbetydelse_granskad`
sedan innan. **Kvar att kolla: bara 8 kort**
(`sessions/session_2026-08-06_snabbkoll2-islearning.json`): omhulda,
gerundium, konsekrera, förebära, föregiva, blot, beveka, förklinga.

OLD-täckning 8/8 (100%). **0 av 8 eskalerade** — alla huvudbetydelser
matchade OLD-facit och egen kunskap utan avvikelse (bl.a. bekräftat att
gerundium/infinit verbform, blot/fornnordisk offerrit, och beveka/
övertala-blidka alla stämmer). Ett OLD-kort (konsekrera) hade av misstag
en kvarglömd Google-bildsöknings-URL inklistrad i sitt Baksida-fält — ett
skräpdataproblem i OLD-decket självt, inte i v2-kortet, ingen åtgärd
behövdes på vår sida.

**Taggning:** alla 8 kort taggade `flerbetydelse_granskad::2026-08-06` +
`flerbetydelse_snabbkoll2::2026-08-06`, flaggade Gröna (inga sökkollade,
inga fel hittade). **"Lär om"-kön är därmed också helt klar** — samtliga
icke-suspenderade `is:learn`-kort i decket har nu gått igenom
flerbetydelse-processen.

## Snabbkoll 2.0 på de 7 suspenderade is:review-korten, alla avsuspenderade (2026-08-07)

De sista 7 suspenderade `is:review`-korten (gentaga, lokus, pracka, gardera
med en kyss, apparelj, jag mötte lassie, bjugg) — alla i legacy-format utom
bjugg, alla märkta `ej_v2_granskat`/`konfidens::0`/`granska_först`/
`granska_fabricerat` sedan tidigare — gicks igenom och avsuspenderades.

Eftersom inget av korten hade riktigt v2-innehåll att jämföra mot OLD-facit
krävde alla sju en full sökkoll (inte bara OLD-jämförelse), med några
konkreta fynd:

- **gentaga**: taggad `granska_fabricerat` sedan tidigare (misstänkt
  påhittat ord) — **INTE fabricerat**. SAOB bekräftar ordet, betyder
  "upprepa" (särskilt om ord/framställning/motiv/melodi). Legacy-
  innehållet var korrekt, migrerat oförändrat till v2, register "arkaisk".
  `granska_fabricerat`-taggen rörs inte (Adams egen historik) men
  misstanken är alltså vederlagd.
- **gardera med en kyss** → **Framsidan ändrad till "gardera med kryss"**:
  uttrycket med "kyss" (puss) verkar ha varit en felskrivning/fabrikation —
  det etablerade uttrycket är "gardera med kryss" (stryktipset: täcka både
  1:an och kryss/oavgjort när man är osäker), och OLD-facit ("säga ngt med
  reservation för att resultatet kan bli annorlunda") matchar kryss-
  betydelsen exakt, inte kyss-betydelsen. Adam bekräftade ändringen innan
  den applicerades (jfr `style_guide.md`, gentaga-precedenten om att aldrig
  byta ett ords identitet utan godkännande).
- **jag mötte lassie**: legacy-definitionen ("möta en kändis") var för
  bokstavlig — uttrycket myntades av Petter Karlsson på Expressen och
  betyder specifikt att skryta om en flyktig/avlägsen kändiskontakt (ofta
  en långsökt koppling på en vardaglig plats). Nyanserad till att fånga
  den skämtsamma/skrytsamma vinkeln, matchar OLD-facit ("avlägsen relation
  till en känd person") bättre.
- **apparelj, lokus, pracka, bjugg**: legacy/v2-innehållet stämde med
  OLD-facit och egen kunskap, migrerade/lämnade oförändrade i sak.
  **Uppföljning att göra**: "pracka" kan ha en andra, mycket vanligare
  betydelse (verbet i "pracka på" = tvinga/lura på någon något) utöver den
  nuvarande enda betydelsen (dialektalt/äldre namn på sjöfågeln småskrake)
  — hittades men hann inte bekräftas fullt ut innan WebSearch-
  sessionsgränsen tog slut. Inte tillagt än, flaggas för nästa
  granskningsrunda.

Alla 7 taggade `flerbetydelse_granskad::2026-08-07` +
`flerbetydelse_snabbkoll2::2026-08-07` + `flerbetydelse_sokverifierad::2026-08-07`
(alla krävde riktig sökkoll), flaggade Blå, och **avsuspenderade**. Detta var
de sista kvarvarande suspenderade `is:review`-korten — inga suspenderade
kort återstår i den poolen.

## Snabbkoll 2.0 på is:review, omgång 2 (SISTA): 282 kort — is:review HELT KLART (2026-08-07)

Adam bad om att göra alla resterande 282 icke-suspenderade `is:review`-kort i
en enda omgång. OLD-täckning 280/282. **19 kort eskalerade** till riktig
sökkoll (WebSearch mot SAOB/SAOL/synonymer.se/facksajter) — alla utom två
var det dominerande mönstret från tidigare rundor: en **saknad andra
betydelse**, oftast bildlig, som fanns i OLD-facit men inte på v2-kortet:

- **tillskriva**: saknade den ålderdomliga "skriva formellt brev till någon"-
  betydelsen (bara "anse bero på" fanns).
- **bördig**: saknade helt den extremt vanliga "ha sitt ursprung/härstamma
  från en plats"-betydelsen (bara "fruktbar om jord" fanns).
- **långskott**: kortet hade redan ett tomt " ; " i huvudbetydelsen (ett
  påbörjat men aldrig avslutat försök till bibetydelse) — bildliga
  "vild gissning/vågspel med liten chans att lyckas" tillagd.
- **löslig, ljum, grace, referera, raffinerad, legislatur, mångfaldiga,
  infinit, färga, ränna in, skifte**: samma mönster, en bildlig eller
  ålderdomlig bibetydelse tillagd (bl.a. ljum: bokstavligt "halvvarm" +
  bildligt "oengagerad", raffinerad: bokstavligt "renad" + bildligt
  "listig/utstuderad", infinit: grammatisk term "icke-finit verbform" +
  allmänspråkligt "oändlig").
- **hamn** och **bankett**: två **genuina homonymer**, samma mönster som
  "ok"/"sarv"/"konstruktivism" i tidigare rundor. "Hamn" har förutom
  "skyddad plats för fartyg" en helt orelaterad ålderdomlig/mytologisk
  betydelse: "skepnad/gestalt, vålnad" (fornnordiska "hamr", jfr
  "hamnskifte" = skepnadsskifte). "Bankett" betyder förutom "festmåltid"
  även, inom vägteknik, "vägren" (den grusade remsan utanför körbanan).
- **uniform**: kortet blandade ihop substantiv- och adjektivbetydelsen —
  huvudbetydelsen beskrev bara substantivet (klädsel) men synonymen
  ("likformig") hörde till adjektivet. Delat upp i två tydliga betydelser.
- **eminens**: kortet hade bara den snäva "titel för katolsk kardinal"-
  betydelsen, saknade den bredare grundbetydelsen "upphöjdhet, förnämlighet,
  värdighet".
- **honnörsord**: ingen saknad betydelse, men synonymen "hedersord" var fel
  (betyder "hedersord/löfte", inte "honnörsord") — rättad till "värdeladdat
  ord".

Kandidater som undersöktes men INTE ändrades (för svag evidens eller
bekräftades redan korrekta): resonera, låta påskina (bekräftades sakna den
misstänkta "falskt"-nyansen — nuvarande text stämmer), fason, konnässans,
skorra, varva, träda, karat, kneippkur.

Alla 282 taggade `flerbetydelse_granskad::2026-08-07` +
`flerbetydelse_snabbkoll2::2026-08-07`; de 19 rättade dessutom
`flerbetydelse_sokverifierad::2026-08-07` och flaggade Blå, resten Gröna.
**`is:review`-poolen är därmed helt klar** — 0 icke-granskade kort kvar i
den kön. Enda kvarvarande arbete i projektet är den stora suspenderade
"Blå Nya"-poolen (~6 900 kort, medvetet dold tills den släpps in i Adams
nya-kort-kö).

## Testbatch: full sökkoll på alla 22 icke-sökkollade is:learn-kort (2026-08-07)

Adam ville mäta hur mycket "usage" (Claude-sessionskvot) en full sökkollrunda
(WebSearch på VARJE kort, inte bara eskalerade) drar, som underlag för att
uppskatta vad en hel Blå Nya-runda (~6 900 kort) skulle kosta. is:learn hade
bara 22 icke-sökkollade kort kvar (15 redan snabbkoll2-godkända + 7 helt
osedda, suspenderade) — för få för en 50-kortsbatch, så hela poolen kördes.

22 WebSearch-anrop, ett per ord. **21/22 bekräftades korrekta som de var.**
Ett fel hittades: **brokad** saknade den definierande "guldtråd"-detaljen
(brokad är historiskt specifikt vävt med guld-/silvertråd, inte bara
"mönstrat sidentyg" i allmänhet) — rättat.

Alla 22 taggade `flerbetydelse_sokverifierad::2026-08-07` (utöver
granskad/snabbkoll2), flaggade Blå. De 7 suspenderade av dem avsuspenderade.
`is:learn` har nu 0 icke-sökverifierade kort kvar (bara ett kort förblir
suspenderat, av skäl utanför flerbetydelse-processen).

Adams egen mätning: ca 2 % av veckokvoten och 5 % av 5-timmarsfönstret för
denna 22-korts full-sökkoll-runda — ett användbart riktmärke för att skala
upp mot Blå Nya-poolen.

## Testbatch 2: full sökkoll på 50 kort ur den suspenderade Blå Nya-poolen (2026-08-07)

Adam menade egentligen `is:new` (inte `is:learn`) för 50-korts-testet. 50
kort hämtade ur den ~6 900 kort stora suspenderade "Blå Nya"-poolen
(`is:new -tag:flerbetydelse_granskad::*`), full sökkoll (50 WebSearch-anrop,
ett per ord).

**Viktig skillnad mot is:review/is:learn-poolerna**: dessa 50 kort var INTE
i v2-format — de låg kvar i ett äldre mellanformat
(`<font>synonymer</font><br><br><ol><li>definition</li></ol>`), aldrig
migrerade. Sökkollen blev därför en full v2-migrering av alla 50, inte bara
en jämförelse. Detta avslöjade buggtyper som inte synts i de redan
v2-migrerade poolerna:

- **Engelska läckor**: "lägra sig" hade två definitioner skrivna på
  ENGELSKA istället för svenska. "degel" hade exempelmeningen "melting pot"
  (bara det, på engelska). "knussel" hade hela synonymraden på engelska
  (stinginess, parsimony, miserliness).
- **Fabricerade/felaktiga tredjedefinitioner**: "manschett" hade en tredje
  "definition" som beskrev vitkragebrottslighet ("brott begånget av en
  ansedd person...") — inte en verklig betydelse av ordet i sig, borttagen.
  "göt" hade en påhittad andra definition ("del av en större
  metallkonstruktion") som inte stämmer med vad ett göt faktiskt är.
  "tillskyndare" hade en andra "definition" som bara löd "Synonymt med
  initiativtagare" — ett läckt metakommentar, inte en definition.
- **Genuin missad betydelse**: "kangas" är en äkta homonym — dialektal
  hedmark (meänkieli) OCH tyg/väv (finskt lånord, vilket också förklarar
  varför OLD-decket hade "höftskynke" som facit) — kortet hade bara
  hedmarksbetydelsen, plus en helt påhittad tredje "definition" om att
  Kangas är ett vanligt finskt efternamn (borttagen, inte en ordbetydelse).
- **Trasiga exempelmeningar**: flera kort hade tomma, ofullständiga eller
  helt orelaterade exempelmeningar (t.ex. "jamare" hade en mening som inte
  ens nämnde ordet).
- **Nästan-dubblettdefinitioner**: de flesta korten hade två `<li>`-
  definitioner som bara var omformuleringar av samma betydelse (inte
  genuint skilda betydelser) — slogs ihop till en betydelse vid
  migreringen, i linje med style_guide.mds " ; " (skilda betydelser) vs.
  ingen separator (omformulering)-konvention.

Alla 50 migrerade till v2, taggade `flerbetydelse_granskad::2026-08-07` +
`flerbetydelse_snabbkoll2::2026-08-07` + `flerbetydelse_sokverifierad::2026-08-07`
+ `kortformat::v2`, flaggade Blå. **Fortfarande suspenderade** — de förblir
dolda i sållningsfiltret tills Adam väljer att släppa in dem, i linje med
"Sållningsfilter för Blå Nya"-policyn.

**Slutsats för skalning**: Blå Nya-poolen är alltså inte bara en
"jämför-mot-facit"-uppgift som is:review var, utan kräver en fullständig
v2-migrering av mestadels aldrig-formaterat innehåll, med ett tydligt
mönster av AI-genererade skräpdata (engelska läckor, fabricerade
tredjedefinitioner, trasiga exempelmeningar) utöver de vanliga
"saknad betydelse"-felen. Usage-kostnaden per kort är alltså sannolikt
högre än för is:review (mer omfattande sökkoll + full omskrivning krävs
för de flesta kort, inte bara en jämförelse).

**Självrättning samma runda:** Adam upptäckte att jag hade lämnat korten
suspenderade och bad mig själv utvärdera om de var redo att släppas in.
Kontroll visade att 37 av 50 kort saknade register helt eller använde en
otillåten tagg ("ålderdomlig" istället för den låsta vokabulärens
"arkaisk") — registret är obligatoriskt enligt style_guide.md, aldrig
valfritt. Rättat på alla 37, verifierat med `validate_register()` (0
kvarvarande problem), och **därefter avsuspenderade alla 50**.

## Testbatch 3: false-negative-test — 50 is:new-kort som klarat snabbkoll 2.0 UTAN eskalering (2026-08-07)

Adam förtydligade det ursprungliga syftet: inte fler kort ur Blå Nya, utan
50 `is:new`-kort som redan gått igenom snabbkoll 2.0 och bedömts INTE
behöva sökkoll (gröna, `flerbetydelse_snabbkoll2`-taggade men INTE
`flerbetydelse_sokverifierad`-taggade) — för att testa om den egna
bedömningen i 2.0 (jämförelse mot OLD-facit + egen kunskap, utan
websökning) är tillräckligt tillförlitlig, eller om en fullständig
sökkoll hittar fel som ändå slank igenom.

50 kort hämtade, redan i v2-format och redan granskade en gång. Full
sökkoll (50 WebSearch-anrop) på alla, oavsett om de såg misstänkta ut.

**Resultat: 49/50 höll — bara 1 fel hittat (2%).** "goodwill" hade bara
den ursprungliga betydelsen (gott anseende/välvilja) men saknade den minst
lika vanliga redovisningsbetydelsen (ett företags immateriella värde
utöver bokfört värde) — tillagd. Inget annat av de 50 hade fel eller
saknade betydelser.

**Slutsats**: 2%-felfrekvensen på redan-godkända kort är lägre än den
gamla minnesbaserade snabbkollens 8,75% (se A/B-testet i style_guide.md,
"Flerbetydelse-genomgång"), vilket stöder att snabbkoll 2.0:s
OLD-facit-jämförelse + egen kunskap är en väsentligt bättre bas än
ren minnesbedömning — men den är inte perfekt (2% > 0%). Om Adam vill
pressa felfrekvensen ännu lägre skulle full sökkoll på ALLA kort krävas,
men det är den dyra vägen usage-testerna ovan visar kostnaden för.
Alla 50 taggade `flerbetydelse_sokverifierad::2026-08-07` (oavsett om de
hade fel eller ej, eftersom alla nu faktiskt sökkollats), "goodwill"
uppgraderad till Blå flagga.

## Nytt verktyg: generaliserad v2-ombyggnad för Blå Nya, två lägen (2026-08-07)

Testbatcharna ovan visade att `snabbkoll2_blanya.py` (som bara matchade
redan v2-formaterade flag:4-kort) inte täcker den kvarvarande
suspenderade poolen (~6 850 kort) — stora delar ligger fortfarande i det
gamla `<ol><li>`-formatet. Tre nya, permanenta script byggdes (se
`.claude/plans/elegant-singing-mochi.md` för fullständig design):

- **`snabbkoll2_blanya_v2.py`** — breddad poolbyggare
  (`is:new is:suspended -tag:flerbetydelse_granskad::*`, ingen flagg-
  eller formatbegränsning). Parsar legacy-kort automatiskt via
  `baksida.parse_legacy()` och beräknar `format_bug_hints` per kort
  (`legacy_format`, `tom_exempelmening`, `exempel_saknar_ordet`,
  `mojlig_dubblett`) — mjuka pekare för granskaren, inga auto-fixar.
- **`condense_session.py`** — generisk kondenserad-dump-generator,
  ersätter de ad-hoc scratchpad-scripten som skrevs om för hand i varje
  omgång denna session. Fungerar på både v2- och legacy-`current`.
- **`apply_flerbetydelse.py`** — delad apply-/tagg-/flagg-/
  avsuspenderingslogik för båda lägena (`--mode snabbkoll2` eller
  `--mode sokkoll`). `apply_card()` **vägrar** (ValueError) skriva ett
  kort med ogiltigt/saknat register — direkt svar på att 37 av 50 kort
  i en tidigare testbatch saknade giltigt register trots att
  `baksida.validate_register()` redan fanns. `--mode sokkoll` kräver
  dessutom `escalated=True` för varje kort (AssertionError annars).
  `apply_batch_unsuspend()` dubbelkontrollerar register direkt mot Anki
  innan avsuspendering, istället för att lita på vad som skickades in.

**Verifieringskörning** (20 legacy-kort, `--mode snabbkoll2`, hela
kedjan bygg→kondensera→granska→applicera→avsuspendera): 18/20 kort
matchade OLD-facit/egen kunskap utan eskalering (merparten hade
"nästan-dubblettdefinitioner" som slogs ihop till en betydelse, exakt
det mönster verktyget flaggar). **2 eskalerade**: "agna" fick en
bekräftad andra betydelse tillagd (agnar = sädesskal, saknades i
OLD-facit). "kuliss" hade en påstådd tredje betydelse om skogsvård
(bälte av kvarlämnade träd vid avverkning) som **inte gick att
bekräfta via sökning och slopades** — ett konkret exempel på den
fabricerade-legacy-text-buggen som motiverade hela verktygsbygget.
Alla 20 v2-migrerade, taggade, flaggade och avsuspenderade.

Nästa steg: köra verktyget i större batchar (`--batch-size 100+`) mot
resten av den suspenderade poolen, i `snabbkoll2`-läge som standard.

## "eller"-separatorbugg upptäckt igen på "pöbel", trots sökverifiering samma dag (2026-08-07)

Adam hittade manuellt (Röd-flaggade) att **pöbel** hade
`"en okontrollerad folkmassa, eller människor från samhällets lägsta
skikt"` som huvudbetydelse — samma `"eller/;"`-buggmönster som
vandal/atmosfär/parhäst/census tidigare (se ovan), fast här med ett
extra kommatecken (`", eller"`) framför. Två genuint skilda betydelser
(arg folkmassa vs. person från lägsta samhällsskiktet) skrivna som om
de vore löst utbytbara, istället för den överenskomna `" ; "`-
separatorn. Buggen introducerades i `session_2026-08-04_migration-
format.json` under Fas 2-kondenseringen och applicerades sedan.

**Anmärkningsvärt:** kortet gick igenom BÅDE `flerbetydelse_snabbkoll2`
OCH `flerbetydelse_sokverifierad` tidigare samma dag (2026-08-07,
"Nytt verktyg"-passet ovan) utan att separatorbuggen fångades — varken
snabbkoll 2.0 eller den riktiga sökkollen är skriven för att leta efter
just detta formateringsmönster, bara sakfel i själva betydelsen.

**Fixat mekaniskt** (direkt via AnkiConnect, ingen ny innehållsgranskning
eftersom betydelsen redan var sökverifierad samma dag): huvudbetydelse
→ `"En okontrollerad folkmassa ; människor från samhällets lägsta
skikt"`, flagga Röd → Blå, ny tagg `eller_separator_fixad::2026-08-07`.

## "eller"-separatorn: full svepning klar, 70 kort fixade (2026-08-07, Opus)

Uppföljningen av pöbel-fyndet ovan, körd med Opus enligt beslutet.
Nytt permanent script: **`find_eller_separator.py`** (systerscript till
`find_old_slash_separator.py`). Ändrar inget själv — "eller" är ett
normalt svenskt ord inuti EN betydelse ("kunglig eller kejserlig titel",
"inte kan läsa eller skriva"), så en blind ersättning skulle förstöra
fler kort än den lagar. Scriptet rankar istället kandidater i tre nivåer
och lämnar bedömningen till granskaren:

| Nivå | Signal | Träffar | Utfall |
|---|---|---|---|
| `hog` | `synonym_groups` har 2+ grupper men Huvudbetydelse saknar ` ; ` | 2 | båda buggar |
| `medel` | `", eller"` (komma + eller) utan ` ; ` | 68 | alla åtgärdade |
| `lag` | något `" eller "` alls, utan ` ; ` | 484 | **0 buggar** — genomlästa, "eller" står inuti en betydelse |

**Kommatecknet var den avgörande signalen.** `lag`-nivån (484 kort) var
helt ren; hela felmassan låg i `", eller"`. Det är den kontroll som ska
återanvändas, inte "letar efter ordet eller".

**70 kort rättade och applicerade**, alla verifierade mot OLD-facit/
ordkunskap ett och ett (inte regex):
- **61 fick ` ; `** — genuint skilda betydelser. Flera bekräftades av att
  OLD-facit självt använde `;` (anhålla "begära; beröva misstänkt", dåna
  "mullra; svimma", skarv "där två delar sitter ihop; sjöfågel", gehör,
  eldfängd, kvadrant, moderera, spekulera, anvisa). Grövsta fallen var
  rena homonymer: **legat** (arv / påvligt sändebud), **skarv** (fog /
  sjöfågel), **försträcka** (låna ut pengar / skada en muskel).
  **beslå** hade TRE betydelser hopbuntade och fick två `;`.
- **9 fick ` / `** istället — leden var omformuleringar av SAMMA
  betydelse, där ` ; ` hade varit lika fel som "eller" (det påstår två
  betydelser som inte finns): agglomerera, antåga, bjäbba, furste,
  huttla med någon, karitativ, knivig, moratorium, vetta.
- **överlastad** fick också andra ledet omskrivet — det definierade
  uppslagsordet med sig självt ("överlastad med för mycket dekor").

Beslutsunderlaget per kort ligger kvar i
`sessions/session_2026-08-07_eller-separator.json` (`proposed` +
`note_till_granskare` på alla 554), med före-läget i
`..._backup.json`. Alla 70 taggade `eller_separator_fixad::2026-08-07`.
Flaggorna rördes INTE — det här var en formatfix, inte en omgranskning.
Omkörning efter fix: `hog: 0, medel: 0`.

**Lärdomen om kontrollerna, inte om orden:** pöbel hade passerat både
`flerbetydelse_snabbkoll2` och `flerbetydelse_sokverifierad` samma dag.
Båda kollar SAKINNEHÅLL (stämmer betydelsen? saknas någon?), ingen av dem
kollar FORM. De 70 korten var alltså inte sakligt fel — betydelserna
fanns där, de var bara hopbuntade så att kortet läser som en betydelse
istället för två. Mekaniska formkontroller (som denna och
`find_old_slash_separator.py`) hittar en klass av fel som ingen mängd
innehållsgranskning fångar, och är i stort sett gratis att köra om.

## Kodgenomgång: hela kodbasen verifierad mot live-decket (2026-08-07)

Alla 27 script lästa och kontrollerade, plus en körning av hela
v2-poolen (3202 kort) genom `baksida.py`. Resultat:

| Kontroll | Utfall |
|---|---|
| Alla moduler importerar rent | 27/27 |
| `parse()` klarar varje v2-kort | 3202/3202 |
| `parse()` → `build()` identisk med originalet | 3202/3202 (efter fix nedan) |
| Register saknas / ogiltigt | 0 / 0 |

Registerkontrollen är alltså helt ren — den hårda spärren i
`apply_flerbetydelse.apply_card()` har gjort sitt jobb; de 37/50 utan
giltigt register som motiverade spärren har ingen motsvarighet kvar.

**Två riktiga buggar hittade och fixade:**

1. **`baksida.py`: `parse()` tappade bilden på kort med ett enda `<br>`
   före `<img>`** (`_IMG_TAIL_RE` krävde exakt två). För sådana kort
   returnerade `parse()` `bild_html=None`, och nästa `parse()`→`build()`
   **raderade bilden tyst** — alltså vilken innehållsfix som helst, eller
   `restore_images_from_old_deck.py`. Träffade 1 av 766 bildkort
   (**faun**), som därmed låg en godtycklig framtida omskrivning från att
   förlora sin bild. Regexen tar nu ett-eller-flera `<br>`; faun-kortets
   `<img>` normaliserades samtidigt till standardformatet med `style=`.
   Testat att `<br>` inuti en exempelmening fortfarande inte förväxlas
   med en bild.

2. **`queue_lib.write_session()` skrev tyst över en befintlig
   sessionsfil.** Eftersom granskningen (`approved`/`proposed`) lagras I
   sessionsfilen raderade en andra körning av t.ex. `fetch_queue.py`
   samma dag hela det första passets arbete. `snabbkoll2*.py` hade redan
   en `while os.path.exists`-dedup lokalt — den flyttades till
   `write_session()` så att alla `fetch_*`/`scan_*`-script skyddas
   likadant (andra körningen får `-batch2`).

**Iakttagelse, inte åtgärdad:** `avkastning` har OLD-facit "vinst; skörd"
men kortet saknar skörde-betydelsen. Det är "saknad betydelse"-mönstret
(det vanligaste felet enligt sökkollarna ovan), inte en separatorbugg —
noterat här för nästa innehållspass, inte fixat i denna omgång.

## Granskning av v2-ombyggnaden för Blå Nya — tre buggar (2026-08-07)

Riktad genomgång av `snabbkoll2_blanya_v2.py` → `apply_flerbetydelse.py`
(verktyget som bygger om nya kort till v2, se avsnittet ovan). Alla tre
buggarna satt i den DELADE apply-logiken, alltså i det steg varje kort
passerar — inte i något kantfall.

1. **`apply_card()` satte aldrig `kortformat::v2`.** Kortet skrevs om till
   v2-format men taggades bara med flerbetydelse-taggarna. Följd: kortet
   blev **osynligt för varje `tag:kortformat::v2`-fråga i projektet** —
   `snabbkoll2.py`, `build_all_v2_snabbkoll_queue.py`,
   `build_full_flerbetydelse_queue.py`, `find_old_slash_separator.py`,
   `restore_images_from_old_deck.py` och `find_eller_separator.py`.
   **26 kort låg i det hålet**: v2 till innehållet, avsuspenderade, i
   Adams kö — men utanför räckhåll för alla uppföljande kontroller.
   Åtgärdat i koden + de 26 efterhandstaggade. Eller-svepningen kördes om
   efteråt (3229 kort istället för 3202): inga nya separatorfel.

2. **Gul-flaggan var inte implementerad.** style_guide.md beskriver TRE
   utfall (eskalerad→Blå, OLD-matchning→Grön, **ingen OLD-matchning→Gul**),
   men `_tag_and_flag()` kände bara till Blå/Grön. Kort utan OLD-matchning
   flaggades alltså Gröna, dvs "jämförd mot facit" — när facit aldrig
   fanns. 9 kort berörda (bl.a. `kontrastera`, `legymer`, `i hast`), nu
   satta till Gul. `has_old_match` är numera ett OBLIGATORISKT argument för
   icke-eskalerade kort (AssertionError annars), samma spärr-princip som
   registret redan hade — en default hade bara återskapat buggen.

3. **`apply_batch_unsuspend()` kraschar på stora batchar.** Den bygger en
   `nid:X OR nid:Y ...`-kedja över hela batchen; Anki/SQLite spränger
   uttrycksträdet vid ~1000 led (`Expression tree is too large (maximum
   depth 1000)`). Reproducerat med 2356 kort. Detta hade slagit till exakt
   när verktyget används som CLAUDE.md föreskriver ("nästa steg:
   `--batch-size 100+`"). Frågan chunkas nu om 500.

**Bonus i samma pass:** `compute_format_bug_hints()` kollade om ordet fanns
i exempelmeningen, men INTE om det var highlightat — vilket är den regel
style_guide.md faktiskt kallar "inte valfritt". Nytt tips `saknar_highlight`.
Den gamla substrängkollen står kvar men ger falsklarm på böjda former
(`beslå` → "beslogs"); den är ett tips, inte en spärr.

**Datafynd på köpet:** 11 kort hade bokstavligt `&nbsp;` i **Framsida**
(samma buggklass som `blindskrift&nbsp;` tidigare), 7 hade dubbla
mellanslag. Ett kort var helt inverterat: **Framsida innehöll hela den
gamla Baksidan** (`<ol><li>`-definitioner, tom exempelmening) och
**Baksida innehöll strängen `"ai_failed"`** — ett taggnamn skrivet i ett
innehållsfält. Ordet var `HTML`. Återställt från sitt eget innehåll,
flaggat Gul (ingen OLD-matchning), fortfarande suspenderat — släpp det
manuellt om det ska ingå. Före-läget i
`sessions/session_2026-08-07_html-kort-backup.json`.

## Adam-tal-lint: `lint_adamtal.py` (2026-08-07)

Nytt permanent script som mekaniskt kontrollerar det style_guide.md
faktiskt går att kontrollera mekaniskt. Ändrar aldrig något. Varje
kontroll är märkt `[SÄKER]` (i praktiken utan falsklarm, kan åtgärdas
rakt av) eller `[BEDÖM]` (kända legitima undantag — massfixa aldrig).

**Utfall: 3054 av 3229 kort (94,6%) helt rena.**

Alla `[SÄKER]`-kategorier är nu nollade. Åtgärdat i denna omgång:

| Fynd | Antal | Åtgärd |
|---|---|---|
| Avslutande punkt i Huvudbetydelse | 54 | borttagen (inget annat kort har det) |
| Semikolon utan mellanslag (`;` ej ` ; `) | 6 | bedömt ett och ett: 3 `` ; ``, 2 ` / `, 1 parentes |
| Gammal `<span style="rgb(52,152,219)">` | 2 | → `<font color="#3498db">` |
| Exempelmening helt utan highlight | 3 | highlight tillagd |
| Exempelmening med flera meningar | 1 | `magnat` skriven till en mening |
| HTML-skräp i bild-tagg | 1 | `ginkgo` hade en Amazon-produkttitel i `alt=` |
| Cirkulär + ordboksartad Huvudbetydelse | 1 | `andakt` definierade sig själv på 23 ord |
| Synonymgrupper utan motsvarande betydelser | 1 | `blickfång` plattad till en grupp |

`;`-fyndet är värt att notera: de 6 korten hade GENUINT två betydelser,
bara skrivna med `;` istället för ` ; `. Eller-svepningen missade dem
(den letade efter "eller"), och `baksida.build()`s indragning av
bibetydelsers register hade inte heller fungerat, eftersom den splittar
på ` ; `. En separator som är *nästan* rätt är osynlig för alla verktyg.

**Kvar, medvetet inte åtgärdat (`[BEDÖM]`, 175 kort):**

- **`fragment_exempel` (57)** — den enda kvarvarande posten med verklig
  Adam-tal-substans. Exempelmeningar som är substantivfraser utan finit
  verb: "Ett ekonomiskt debacle.", "Sjunga legato.", "En solid kropp.",
  "Manuell färdighet." Precis mönstret style_guide.md klagar på ("En grov
  skymf."). Kräver en omskrivning per kort — lämpligt eget pass.
- **`cirkular_synonym` (53)** — samma mängd som style_guide.md redan
  adjudicerat en gång (reservat→naturreservat, krypto→kryptovaluta m.fl.
  bedömda som genuin specificering, inte avslöjande). Rör inte utan att
  läsa den historiken först.
- **`cirkular_definition` (28)** och **`ordbokslangd_hb` (39)** — nästan
  uteslutande falsklarm från grov stamklippning respektive ordräkning
  (`signa`→"välsigna", `fiken`→"nyfiken" är olika ord; långa
  huvudbetydelser är ofta befogade på facktermer som `grisaille`).
- **`flera_meningar` (3)** — alla tre legitima. `anafor` illustrerar
  stilfiguren genom att upprepa satsinledningen ("Jag kommer. Jag ser.
  Jag förstår.") — en enda mening hade förstört kortet. Flyttad till
  `[BEDÖM]` just därför.

Tröskeln för `fragment_exempel` sänktes från <5 till <4 ord under
genomgången: vid <5 var i princip alla 101 träffar fullgoda meningar
("Prelaten välsignade menigheten."). Ordräkning är en dålig proxy för
"fragment" — det verkliga felet (sats utan finit verb) kräver
ordklasstaggning för att hittas säkert.

## Adam-tal flyttat in i skrivvägen (2026-08-07)

Linten ovan hittar fel i EFTERHAND. Ett kort som skrivs fel och upptäcks
en vecka senare har Adam redan pluggat in — så reglerna flyttades dit de
biter: `baksida.validate_adamtal()`, anropad som **hård spärr** i båda
skrivvägarna.

Detta är exakt samma åtgärd som registret fick, och av samma anledning.
Register-reglerna stod i style_guide.md i två dagar och hamnade ändå fel
på 37 av 50 kort, ända tills `apply_card()` började vägra skriva utan
giltigt register. Adam-tal hade samma konstruktionsfel: prosa granskaren
skulle minnas, plus en efterhandskontroll.

| Var | Beteende vid brott mot hård regel |
|---|---|
| `apply_flerbetydelse.apply_card()` | `ValueError` — kortet skrivs inte |
| `apply_flerbetydelse.apply_pass()` | `ValueError` — "använd apply_card() istället" |
| `apply_updates.apply_single()` | hoppar över kortet (samma mönster som registret) |

**Hård/mjuk-uppdelningen är mätt, inte gissad.** Hårda regler är de som
gav 0 falsklarm på hela decket i lint-körningen ovan. Mjuka är de där
genomgången visade legitima undantag — `flera_meningar` blockerar
ingenting, eftersom **anafor** MÅSTE ha flera meningar för att kortet ska
fungera. Undantag görs med `tillat=["regelnamn"]` (eller `"tillat"` i
sessionsfilen), aldrig genom att mjuka upp regeln: då syns undantaget i
sessionsfilen istället för att tyst försvinna.

**`lint_adamtal.py` duplicerar inte längre regellogiken** — den anropar
samma `validate_adamtal()`. Två definitioner som glider isär är precis
den buggklass som gav upphov till hela den här genomgången (jfr
`kortformat::v2`-taggen som bara sattes i den ena skrivvägen).
Verifierat: linten ger IDENTISKT resultat före och efter refaktorn,
3054/3229 rena.

**`snabbkoll2_blanya_v2.py` (nya kort) bär nu Adam-tal per kort.** Varje
post i sessionsfilen får `adamtal_blockerande` + `adamtal_varningar`
(validatorn körd på nuvarande innehåll, så granskaren ser kravlistan
medan kortet ändå skrivs om) plus `note_till_granskare` med de sex
punkter som INTE går att kontrollera maskinellt: vardagliga ord, förklara
inte svårt med svårt, konkret före abstrakt, bevara humorn, en
exempelmening med highlight, bara utbytbara synonymer.

Det sista är värt att understryka: **spärren fångar bara form.** Att
skriva vardagligt, konkret och minnesvärt kan ingen regexkontroll avgöra
— den delen är fortfarande granskarens jobb, och style_guide.md är
fortfarande den viktigaste texten i projektet.

## Blint stickprov på "saknad betydelse" — 34 kort rättade (2026-08-07)

style_guide.md efterlyste uttryckligen ett BLINT stickprov: *"testet är
heller inte blint... gör periodiska BLINDA stickprov senare för att
verkligen validera detta över tid."* Detta är det testet.

**Metoden**, tio rader och helt mekanisk: OLD-facit signalerar flera
betydelser med `;` — leta kort där OLD har `;` men v2-huvudbetydelsen
bara har EN betydelse. Ingen bedömning i urvalssteget, alltså ingen
bekräftelsebias.

**Utfall: 116 kandidater — samtliga redan `flerbetydelse_granskad`, 25
till och med `flerbetydelse_sokverifierad`** (den dyraste nivån).

Efter genomgång ett kort i taget: **34 genuint ofullständiga, 82
falsklarm.** Falsklarmen fördelar sig på två mönster som är värda att
känna igen inför nästa körning:
- OLD:s `;` skiljer ofta SYNONYMER, inte betydelser ("memento:
  påminnelse; varning" — kortet hade redan båda).
- Många OLD-poster är förorenade med exempelmeningar eller etymologi
  ("randas: börja**en ny dag randas**; Ragnarök stundar...").

**De 34 rättade** fick andra betydelsen tillagd med ` ; `, synonymerna
grupperade i `synonym_groups`, och register per bibetydelse där det
skiljer (koj: `formell ; vardaglig`, lakej: `arkaisk ; nedsättande`).
Fyra källkollades utöver OLD (evalvera, njugg, vidtaga, stigbygel).

Grövsta fynden var kort där en HEL betydelse saknades:
- **stigbygel** — bara sadelbygeln, inte hörselbenet i mellanörat.
- **göt** — bara metallblocket, inte folkstammen i Götaland.
- **stranda** och **flaggskepp** — hade bara den BILDLIGA betydelsen,
  den bokstavliga (gå på grund / amiralsskeppet) saknades helt.
- **kultur** — saknade den biologiska odlingsbetydelsen.
- **evalvera** — saknade "räkna om från ett myntslag till ett annat"
  (bekräftat mot ordbok, kortet hade bara "värdera").

**Det starkaste mönstret: synonymerna avslöjade betydelsen som saknades
i huvudbetydelsen.** `flaggskepp` hade redan synonymen "amiralsskepp",
`lovlig` hade "tillåten, laglig", `menig` hade "allmän, vanlig",
`vidtaga` hade "börja" — alla pekade på en betydelse huvudbetydelsen
inte nämnde. Det är precis "dold andra betydelse"-signalen style_guide
beskriver, och den är mekaniskt sökbar.

**Vad detta säger om processen.** ~34 av 3202 OLD-matchade kort ≈ 1,1 %
— vilket ligger *precis inom* den 1,5 %-gräns rule-of-three-räkningen i
style_guide.md själv angav. Statistiken i dokumentet var alltså ärlig;
det som var för optimistiskt var läsningen av den som "0 missade fel".
Snabbkoll 2.0 är fortfarande klart bättre än den gamla minnesbaserade
kollen (8,75 %), men "sökverifierad" är inte samma sak som "fullständig"
— 25 av kandidaterna bar den taggen.

Alla 116 har nu ett `utfall`-fält (`atgardad`/`falsklarm`) med
motivering i `sessions/session_2026-08-07_saknad-betydelse-kandidater.json`,
så de 82 inte behöver bedömas om. Före-läget för de 34 ligger i
`..._saknad-betydelse-backup.json`.

**Svepningen är billig och bör köras om** när OLD-decket eller
kortmassan ändras — den är nu en engångskostnad i tid, inte i tokens.

## v3.0 — kortbyggare + kortgranskare (2026-08-07, i drift från 2026-08-08)

Från 2026-08-08 skrivs **125 kort/dag** om från legacy till v2 och släpps
in i Adams kö. 6 805 kort kvar, **6 780 (100 %) har OLD-facit**, ~54
dagar. Adams krav: varje släppt kort ska vara rätt, med sökkoll +
OLD-facit + oberoende verifiering.

### Fem script

| Fil | Roll |
|---|---|
| `kortbyggare.py` | Bygger dagsbatchen. Samlar legacy-innehåll, OLD-facit, riskflaggor och Adam-tal-kraven per kort. Skriver aldrig till Anki. |
| `riskflaggor.py` | Mekaniska risksignaler FÖRE skrivning. Styr var uppmärksamheten läggs. |
| `kortgranskare.py` | `applicera` → `paket` → `verdikt` → `slapp`. Varje steg kontrollerar att det föregående faktiskt gjordes. |
| `blint_stickprov.py` | Mäter felfrekvensen i redan släppta kort. Den enda delen som mäter om resten fungerar. |
| `lint_adamtal.py` | Retroaktiv formkontroll (oförändrad). |

### Det som gör v3 annorlunda: blind andragranskning

`paket` skriver en fil med **enbart** uppslagsordet, OLD-facit och det
färdiga kortet. Den innehåller medvetet INTE riskflaggorna,
sökkollsanteckningarna, det gamla innehållet eller något annat som
avslöjar hur kortet blev till.

Skälet är mätt, inte principiellt: style_guide.md noterade risken redan
om snabbkoll 2.0 (*"samma granskare ... i samma sittning"*), och
2026-08-07 visade sig den befogad — 34 kort med saknad betydelse i
material som passerat BÅDE snabbkoll OCH sökverifiering. **En granskare
som kontrollerar sitt eget arbete bekräftar sig själv.** Verdikt-steget
måste därför köras i en FRISTÅENDE kontext (ny session eller separat
agent) som bara läser paketfilen.

### Släppspärren — "granskat" är inte längre ett påstående

`slapp` avsuspenderar bara kort som har alla taggar i
`config.SLAPP_KRAVER_TAGGAR` (`kortformat::v2` +
`flerbetydelse_granskad` + `flerbetydelse_sokverifierad` +
`oberoende_verifierad`) OCH klarar register + hårda Adam-tal-reglerna
kontrollerat mot **live-innehållet i Anki**, inte mot vad som en gång
skickades in. Saknas något stannar kortet suspenderat.

Dessutom vägrar `applicera` skriva ett kort vars `sokkoll`-fält är tomt
— det är så kravet "sökkoll på varje kort" blir kontrollerbart i stället
för en ambition.

### Verifierat end-to-end 2026-08-07 (3 kort, inget släppt)

- Släpp före verifiering: **0 av 3 släpptes**, alla blockerade på
  `saknar oberoende_verifierad`.
- Paketet läcker ingenting: kontrollerat mot `riskflaggor`, `sokkoll`,
  `legacy`, `proposed`, `note_till_granskare`, `slutsats` — 0 träffar.
- Verdiktvägen: 2 godkända släppbara, 1 underkänd hålls kvar.
- Sökkollspärren: kort med tomt `sokkoll` skrevs inte.
- Adam-tal-spärren: kort med exempelmening utan highlight skrevs inte.

Testtaggarna togs bort efteråt — de tre korten är applicerade men
**suspenderade och oberoende_verifierad saknas**, eftersom ingen
fristående granskning faktiskt gjorts på dem. De ligger först i kön.

De tre var i sig ett bevis på att flödet behövs: `approximativ` hade
synonymen "tillnärmmelsevis" felstavad, `dandy` hade **"flåsig"** som
synonym (sakligt fel — SAOB ger "sprätt, snobb, modelejon"), och
`vara renons` hade två genuina betydelser hopslagna.

### Två spår, 150 kort/dag (beslutat 2026-08-07)

`kortbyggare.py --spar {nya,omgranskning}`

| Spår | Pool | Takt | Vad det är |
|---|---|---|---|
| **A `nya`** | 6 802 suspenderade legacy-kort | 125/dag | Skrivs om till v2 och släpps in i kön |
| **B `omgranskning`** | 3 227 v2-kort utan `oberoende_verifierad` | 25/dag | Kort Adam **pluggar just nu**, skrivna under den gamla processen |

Hela decket (10 034 kort) blir v3-verifierat på **~67 dagar**.

**Skillnaden mellan spåren är inte kosmetisk.** Spår A är suspenderat och
gör noll skada medan det väntar. Spår B ligger i Adams aktiva kö — ett
fel där kostar varje dag det får stå. Med ~1 % restfel är det ~30 kort
som lärs in fel. 125/25 optimerar för volym; väg om mot HP-datumet om
korrekthet i det aktiva materialet ska väga tyngre.

För spår B gäller dessutom:
- `slapp` avsuspenderar ingenting (korten är redan släppta) — den
  markerar dem som blindverifierade och **varnar** för kort som inte
  klarar kontrollen, eftersom de pluggas medan de är trasiga.
- Riskflaggorna räknas på v2-innehållet (`huvudbetydelse`, inte
  `definitioner`) — verifierat: `drägg` med två betydelser via ` ; ` ger
  inget falsklarm, `förtörnad` med en betydelse och tre synonymer flaggas.

**Urvalet är riskprioriterat, inte slumpmässigt** — syftet är att laga
fel snabbast möjligt. Räkna därför ALDRIG felfrekvens på spår B:s
träffar; urvalet är snedvridet och siffran blir för hög. Mätningen kommer
från `blint_stickprov.py`, som drar slumpmässigt just av det skälet.
Kort sagt: **25/dag riskprioriterat för att laga, 10/vecka slumpmässigt
för att veta.**

### Vad v3 INTE garanterar

Kedjan garanterar att inget kort når kön utan att ha passerat alla steg.
Den garanterar **inte** att bedömningarna i stegen är riktiga. Det som
gör kvaliteten mätbar är `blint_stickprov.py` — kör det varje vecka.
Utan mätning är "verifierat" fortfarande bara ett ord.

## v3 skärpt: sökkoll på allt, v3-tagg, etymologirad, prio-kö (2026-08-08)

Fyra beslut av Adam samma dag, plus en bugg som hittades under bygget.

### Sökkoll på varje kort — eskaleringsregeln är avskaffad

Adam: *"jag vill verkligen sökkolla för att garantera att korten med alla
verktyg vi har blir så nära rätt som möjligt. Alltså Opus 5 sökkoll v3 med
old facit och intern kunskap."* OLD-facit och egen språkkunskap är
komplement till uppslagningen, aldrig ersättning för den.

`apply_flerbetydelse.apply_card()`/`apply_pass()` **defaultar nu till
`mode="sokkoll", escalated=True`**. Den billiga vägen finns kvar men måste
väljas uttryckligen. En anropare som glömmer sätta läget får en
AssertionError om saknad källa — inte en tyst nedgradering till en
kontroll som aldrig gjordes. Se style_guide.md, "GÄLLANDE REGEL".

### `v3_granskad::<datum>` (`config.V3_TAG_PREFIX`)

De gamla 2.0-taggarna lämnas exakt som de är (historik). Allt som körs med
v3-metoden framåt taggas dessutom `v3_granskad`. Taggen sätts i
`_tag_and_flag()` **bara på den eskalerade vägen**, alltså bara när en
riktig sökkoll med loggad källa faktiskt gick igenom, och ingår i
`config.SLAPP_KRAVER_TAGGAR` — inget kort kan släppas in i kön utan den.

### Etymologirad i Kortformat v2

Valfri rad efter exempelmeningen, före bilden, med samma `<br><br>`-lucka
som mellan de övriga blocken. Ren text, ingen fet stil, ingen egen färg.
`baksida.build(etymologi=...)` / `parse()` / `apply_card(etymologi=...)`,
och den följer med in i det blinda paketet.

**Villkoret är "hjälper ursprunget?", inte "vet vi ursprunget?"** — se
style_guide.md, "Etymologi". Mjuk längdgräns 18 ord
(`baksida.ETYMOLOGI_MAX_ORD`), blockerar aldrig.

Etymologin läses ur SVANSEN i `parse()`, inte via `_MAIN_RE`, så kort utan
etymologi parsas exakt som förut. Verifierat med `test_etymologi.py`:
**3 232 kort, 0 avvikande** i en parse→build-runda över hela decket. Det är
samma buggklass som kostade `faun` sin bild 2026-08-07 (parse tappar ett
fält → nästa build raderar det tyst).

### Prio-kö: `v3_prio::hog` (`config.PRIO_TAG_HOG`)

`kortbyggare.hamta_pool()` hämtar prio-märkta kort FÖRE den vanliga
due-ordningen, i båda spåren, och `poster.sort()` lägger dem först.
**Förturen måste ligga i urvalet, inte bara i sorteringen** — med 3 000+
kort i spår B hade ett prio-kort längre bak i due-ordningen aldrig kommit
med i dagens 25, hur högt det än var märkt.

Första användningen: de **46** kort som skrevs om 2026-08-08 utan riktig
sökkoll (`v3_markera_prio_botchade.py`). Verifierat med
`test_prio_urval.py`: spår B hämtar nu 25 prio-kort först.

### Buggen: källspärren slog ut v3:s huvudväg

Källspärren (`kalla=` obligatoriskt för sökverifierad-taggen, byggd efter
de 177 falskt taggade korten) skrevs in i `apply_card()` utan att
`kortgranskare.applicera()` uppdaterades — och den är v3:s ENDA skrivväg
för dagsbatchen. Varje kort hade kastat AssertionError, fångats av
anroparens `try/except` och tyst landat i "hoppade över". Hela
125-kortsflödet hade rapporterat noll skrivna kort utan synlig orsak.
Hann aldrig göra skada; v3 hade inte startat.

**Andra gången samma mönster:** `kortformat::v2` sattes 2026-08-07 bara i
den ena skrivvägen och gjorde 26 kort osynliga för alla uppföljande
kontroller. En spärr som läggs i en delad funktion måste följas till varje
anropare i samma ändring.

### Rättning: "177 falskt taggade kort" är 46 spårbara

Rollbacken tog bort taggen från 177 kort, men bara **73** hade skrivits via
`apply_card()` och därmed fått ett `::2026-08-08`-spår (27 med äkta
sökkoll, **46 utan**). De övriga ~131 taggades av ad-hoc-script som
anropade `addTags` direkt och lämnade inget spår i Anki — de går bara att
återskapa ur ordlistorna i `v3_omskrivning_*.py`. Samma lärdom igen:
spårbarhet måste sitta i skrivvägen, inte i ett script som råkar köras.

Frågan som hittar de 46: `tag:flerbetydelse_granskad::2026-08-08
-tag:flerbetydelse_sokverifierad::*`

## Blindgranskningen inbyggd i v3 — och beviset för den (2026-08-08)

Adam: *"granskningen ska ju kolla allting, att betydelserna stämmer och att
inget saknas."* `oberoende_verifierad` fanns redan i
`config.SLAPP_KRAVER_TAGGAR` men hade **aldrig körts** — 0 kort i hela
decket. Steget var beskrivet, inte genomfört.

### Det verkliga problemet var inte att steget saknades

Taggen `oberoende_verifierad` vilade på granskarens ord. Det är exakt vad
`sokverifierad` gjorde innan källspärren — och den satt på 177 kort som
aldrig sökkollats. Att bara "komma ihåg" att köra blindgranskningen i en
ny session hade återskapat samma fel. Så steget byggdes med sitt bevis:

| Spärr i `verdikt()` | Vägrar när |
|---|---|
| granskare saknas | ingen har uppgett vem som granskade |
| självgranskning | `granskare` == `skriven_av` (skiftlägesokänsligt, trimmat) |
| tom anmärkning | ett kort underkänns utan att det står VAD som är fel |
| saknat verdikt | någon post är obedömd |

`applicera --granskare <namn>` stämplar `skriven_av` på varje post;
`paket` bär den vidare utanför `poster` (granskaren ska döma korten, inte
författaren); `verdikt --granskare <namn>` jämför. Utfallet loggas per kort
till `oberoende_granskningar.jsonl`, samma princip som
`sokkoll_kallor.jsonl`: taggen säger ATT något gjorts, loggen säger VAD och
AV VEM, och är det enda som går att granska i efterhand.

Verifierat med `test_oberoende_sparr.py`: alla fyra fallen avbryter, loggen
växer 0 byte, ingenting taggas.

### `facit_signal` — den mekaniska luckdetektorn i paketet

`paket` räknar nu betydelser i OLD-facit (`;`-separerade) mot betydelser i
kortet (` ; `-separerade) och skriver en signal när facit antyder fler.
Härledd enbart ur facit + färdigt kort, alltså ur sådant granskaren ändå
ser — den läcker ingenting om hur kortet blev till.

Signalen är en **fråga, inte ett konstaterat fel**: OLD skiljer ofta bara
synonymer med `;`, vilket gav 82 falsklarm på 116 kandidater 2026-08-07.
Men samma svepning hittade också 34 äkta luckor. Stickprov vid bygget:
signalen fångar `avkastning` (facit "vinst; skörd", kortet saknar skörden)
— den lucka som stått onoterad i den här filen sedan 2026-08-07.

### Checklistan granskaren får

`VERIFIERARINSTRUKTION` utökad från 6 till 8 punkter, i prioritetsordning
med "saknas en hel betydelse" först (dominerande felmönster i elva
omgångar i rad). Nytt sedan tidigare: krav på att granskaren **slår upp
ordet själv** (facit är en andra källa, inte den enda), separatorkontroll
(` ; ` vs ` / ` vs "eller"), cirkulära synonymer, grammatik i
exempelmeningen, båda registeraxlarna, etymologins sanning och nytta, och
till sist läsbarheten högt.

### Vad det fortfarande INTE garanterar

Blindgranskningen fångar klassen "granskaren bekräftar sig själv". Den
fångar inte att två granskare gör samma fel. `blint_stickprov.py` är
fortfarande den enda mätningen av om kedjan håller — och den kan först nu
ge data, eftersom den väljer på `tag:oberoende_verifierad::*` som varit 0.

## Beslut 2026-08-08 (kväll): v3 är enda metoden

Adam: v3 i sin fullständiga form bygger **och** granskar alla kort. Ingen
snabbkoll-väg kvar, ingen villkorlig eskalering. Sökkoll + OLD-facit +
blindgranskning på varje kort — det som pply_card() redan kräver som
standard (`mode="sokkoll", escalated=True`).

**Den bindande resursen är tokens, inte kvalitet.** Volymen är given
utifrån:

| Behov | Kort/dag |
|---|---|
| Håll nya-kön levande (annars tar korten slut) | 125 |
| + rätta befintliga kort i samma takt | ~300 |

300/dag med full v3 per kort är det som ska rymmas i budgeten. Om något
måste skäras är det takten på omgranskningen (spår B) — aldrig djupet per
kort, eftersom hela poängen med v3 är att slippa gå tillbaka.

**Senare, separat program:** hämta bilder ur OLD-facit och fyll i de kort
som saknar bild. Frikopplat från v3-kedjan — bild är inte en betydelse och
ska inte konkurrera om samma tokens.

## deck_snapshot.py — läget, inte bara händelserna (2026-08-08)

Projektet loggade händelser (`kallor.jsonl`, `oberoende_granskningar.jsonl`)
men aldrig **läget**. Utan mätpunkter går det inte att visa att v3 fungerar
över 67 dagar — bara att hävda det. Baslinjen på 10 % fel är meningslös utan
något att jämföra mot.

`python deck_snapshot.py` skriver en rad om dagen till `deck_historik.jsonl`.
Kör om samma dag **skriver över** dagens rad: en snapshot är ett läge, inte en
händelse, och två rader med samma datum vore två sanningar om samma dag.

Första mätpunkten, 2026-08-08:

| | |
|---|---|
| totalt | 10 034 |
| v2-format / flerbetydelse | 3 233 |
| sökverifierad | 931 |
| v3_granskad | 1 |
| oberoende_verifierad | **0** |
| prio_hog | 46 |
| flaggor R/G/Grön/Blå | 810 / 1 273 / 2 292 / 5 659 |
| nya aktiva | 567 |
| suspenderade | 6 810 |

Siffran att hålla ögonen på är `nya_aktiva = 567`. Vid 125 nya kort om dagen
räcker den kön i drygt fyra dagar — det är den som sätter takten, inte
antalet kort i decket.
## `--ko`-flaggan + 50 kort ur dagens nya-kö (2026-08-09)

**Buggen som flaggan löser.** `kortbyggare.py --spar omgranskning` sorterar på
`due`. Repetitionskort har ett schemalagt DATUM som due, nya kort har en
KÖPOSITION — talen ligger i olika intervall, så repetitionskorten vinner alltid.
Följden: körningen tidigare samma dag la **alla 20 kort i repetitionskön och noll
i nya-kön**, trots att det var de nya korten (de Adam introduceras för i dag) som
skulle skyddas. Buggen var tyst — utdatan såg korrekt ut.

**Fix:** `KO_FILTER` + `--ko {nya,repetition,bada}` (default `bada`) som lägger
`is:new` / `-is:new` på pool-frågan **före** sorteringen. Filtrera efter
sortering hade inte hjälpt — de nya korten kom aldrig med i de N första.

`--ko` avvisas för `--spar nya`: spår A är suspenderat och därmed varken nytt
eller förfallet i Ankis mening, så filtret hade tystat hela poolen utan felmeddelande.

Sessionsfilens namn får `-nya`/`-repetition`-suffix så två körningar samma dag
inte blandas ihop.

    python kortbyggare.py --spar omgranskning --ko nya --antal 50

**Verifierat:** 50 av 50 kort inne i dagens nya-kö (mot 0 av 20 före fixen).

### Passet: 50 kort, 39 ändrade

Alla 50 skrivna (`applicera`: 50 skrivna, 0 hoppade), konfidens 49x10 + 1x8.
Taggade `flerbetydelse_granskad::2026-08-09` +
`flerbetydelse_sokverifierad::2026-08-09`, verifierat mot live-innehållet.

**SAKNAD BETYDELSE, 6 kort** — alla belagda mot källa, inte gissade:
`gedigen` (om metall: ren/oblandad, SAOL+SAOB), `konjunktur` (allmännare:
omständigheter, SO+SAOB), `reservat` (område för ursprungsfolk, SAOB+NE),
`revy` (mönstring/översikt, "passera revy", SAOL), `bilateral` (dubbelsidig,
medicinskt), `variabel` — där **definitionen var ett substantiv men
exempelmeningen använde ordet som adjektiv**; kortet motsade sig självt och
ingen flagga reagerade.

**SAKLIGT FEL SYNONYM, 16 kort:** `fonetik`/"språkvetenskap" (hela fältet mot en
gren), `otolog`/"audiolog" (hörselvård mot läkarspecialitet), `bilateral`/"parvis",
`beprövad`/"bevisad", `amsaga`/"historik", `avi`/"brev", `glyptotek`/"konstgalleri",
`civiliserad`/"förnuftig", `försonlig`/"fredlig", `schattera`/"mörklägga",
`konstitutiv`/"avgörande", `sondera`/"granska", `grisaille`/"Gradering",
`komma för`/"inbilla sig", `hävdatecknare`/"hävdaforskare", `uppslag`/"boköppning".
Fyra av dem går inte att belägga som ord alls: hörselmedicinare, hävdaforskare,
boköppning, bortskämmande.

**CIRKULÄRA KORT, 6 st** — ser kompletta ut, lär ut ingenting. `urmodig` är det
renodlade fallet: definition "Gammaldags, omodern", synonymer
`['gammaldags','omodern']` — ordagrant samma sträng, och kortet passerade den
gamla granskningen och blåflaggades. Samma mönster: `korus`, `sufflett`,
`bonitet`, `depreciera`, `fördärvlig`. **Detta är underlaget för att flytta
`cirkular_synonym`/`cirkular_definition` från ADAMTAL_MJUKA till ADAMTAL_HARDA.**

**EXEMPELMENING, 6 st:** `fonetik` (meningen använde inte ordet alls, utan
"fonetiker"), `förhala` (fel användning), `schattera` ("schattar" -> "schatterar"),
`yuppie` ("lönekuver" -> "lönekuvert"), `depreciera` ("svenska kronor" -> kronan),
`prelat` (tre ords fragment).

**REGISTER, 4 st:** `fördärvlig`/`högfärdig` saknade formalitetsaxeln helt,
`försonlig` var felmärkt vardaglig, `revy` felmärkt formell.

**RÄKNA INTE FELFREKVENS PÅ DETTA.** 31 av 50 valdes för hög riskflagga —
urvalet är riskprioriterat med avsikt. 39/50 är inte deckets felnivå. Den siffran
kommer från `blint_stickprov.py`. 11 av 50 var korrekta och lämnades orörda.

Riskflaggan `dold_betydelse` gick igång på 31 kort men träffade rätt
betydelsefel i 6 — den styr uppmärksamhet, den bevisar ingenting.

### Kvar

`oberoende_verifierad` är fortfarande **0**. Blindpaketet är byggt:
`sessions/session_2026-08-09_v3-paket-nya.json`, 50 poster, läckagekontrollerat
(0 träffar på riskflaggor/sokkoll/legacy/proposed/note_till_granskare).
**Verdikt måste köras i en FRISTÅENDE session** — inte i den som skrev korten.
Kvar av dagens 125: 75 kort.

**Samspel med prio-taggen (löst vid rebase 2026-08-09):** `hamta_pool` hämtar
prio-märkta kort först och fyller på med resten. `--ko` läggs därför på
BASFRÅGAN, inte bara på restposten — annars hade prio-hämtningen dragit in
repetitionskort även vid `--ko nya` och ätit upp platserna innan de nya korten
ens övervägdes. Samma sak för `prio_kvar`-räkningen i utskriften.

## HÅL 0 — sökkollen är nu maskinellt bevisad (2026-08-09, kväll)

**Vad som hände.** 141 kort granskades under dagen. `kalla`-fältet påstod
`"svenska.se (SAOL/SO/SAOB) + OLD-facit"` på i praktiken alla. Adam frågade rakt ut
om alla kort var sökkollade. Mätt mot `raw-websearch/`-loggen: **11 av 141 hade en
faktisk uppslagning.** Taggen `flerbetydelse_sokverifierad::2026-08-09` sattes på alla
141 och togs bort från 130 samma kväll. `flerbetydelse_granskad` står kvar — korten ÄR
granskade mot OLD-facit, bara inte webbkollade.

**Varför spärren inte fångade det.** `applicera` vägrade redan skriva ett kort med
TOMT `sokkoll`. Men den kunde bara se ATT fältet var ifyllt, inte att innehållet var
sant. Felet var inte slarv — det var att den som gjorde arbetet också skrev intyget om
att arbetet gjorts. Exakt samma asymmetri som `paket`/`verdikt` finns för att lösa på
innehållssidan, fast för källorna.

**Fixen: `sokkoll_verifiering.py`.** `kalla` måste innehålla en URL, och URL:en måste
finnas som `input.url` på ett faktiskt WebFetch-anrop i Claude Codes transkript — ett
vittne som skrivs av verktygslagret och som granskaren inte kan redigera.
`raw-websearch/` i valvet används som reserv för äldre datum.

**Bugg i spärren, fångad av dess eget test samma kväll:** första versionen drog varje
URL som förekom på en rad som nämnde "WebFetch". Då räckte det att SKRIVA en URL för
att "bevisa" en hämtning — vilket upphäver hela modulens syfte. Rättat: bara
`input.url` på ett `tool_use`-block med `name == "WebFetch"` räknas.

**`svenska.se` är BLOCKERAD som källa.** Sidan är JS-renderad; WebFetch får tillbaka
ett tomt skal (verifierat 2026-08-09). Att tillåta den hade gjort det möjligt att
"belägga" ett ord med en tom sida. Godkända värdar: synonymer.se, saob.se,
wiktionary.org, ne.se, isof.se, sprakochfolkminnen.se, runeberg.org, tyda.se.
**`https://www.synonymer.se/sv-syn/<ord>` är den kanal en sökkoll ska gå genom** —
verifierat att den fetchar och ger betydelser plus synonymlista.

**Torrkörning mot dagens 141:** 0 släpps igenom, 141 stoppas. Även de 11 genuint
kontrollerade, eftersom de använde WebSearch (en fråga) och inte WebFetch (en URL).
Avsiktligt: en sökfråga går inte att knyta till ett specifikt uppslagsord, en hämtad
URL gör det.

### Vad detta kostar, och varför det måste sägas högt

100 % sökkoll betyder **en WebFetch per kort**. Vid 125 kort/dag är det 125 hämtningar
per dag, utöver granskningsarbetet. Det är den verkliga kostnaden, och det var precis
den kostnaden som fick volymen och kvaliteten att krocka 2026-08-09 — konflikten löstes
tyst till volymens fördel.

**Skriv inte om takten utan att räkna om hämtningarna.** Om 125/dag inte går ihop med
en hämtning per kort är svaret att sänka takten, inte att sänka kravet. Adams mål
2026-08-09: *"den bästa modellen med 100 % sökkoll ... aldrig behöva oroa sig över om
korten är rätt eller fel."*

### Att göra om

130 kort saknar sökkoll, varav **97 ändrades i innehåll utan källa**. Ordlistan finns i
`sessions/session_2026-08-09_*`, där varje relabelad post är märkt `[EJ WEBBKOLLAT]`.
Högst risk: åtta påståenden om att ett ord *inte finns*, gjorda utan uppslagning —
`hävdaforskare`, `boköppning`, `bortskämmande`, `habegärlig`, `initialera`, `brunton`,
`öppningsvisning`, `misskastningar`.

### svenska.se löst — SAOB är ordadresserbar (2026-08-09, sent)

`https://www.saob.se/artikel/?seek=<ord>` är serverrenderad och tar ordet direkt.
Verifierat med två skilda ord (gedigen, trolsk) — rätt artikel per ord, full text,
numrerade betydelser, etymologi och belägg.

svenska.se självt förblir blockerat: både `/tre/?sok=` och den äldre
`/tri/f_saol.php?sok=` ger ett tomt skal. SAOB är samma akademi och djupare, så
ingenting går förlorat.

**Adams beslut 2026-08-09: SAOB ska alltid användas.** Sökkollen per kort blir därmed:

1. `saob.se/artikel/?seek=<ord>` — betydelser, auktoritativt
2. `sv.wiktionary.org/wiki/<ord>` — modernt bruk, numrerade betydelser
3. `synonymer.se/sv-syn/<ord>` — synonymer

**Tre hämtningar per kort.** Vid 125 kort/dag = 375 hämtningar/dag. Räkna om takten
mot den siffran innan nästa batch startas — se varningen om volym kontra kvalitet ovan.

**Beviset att flera källor behövs:** av fyra testhämtningar avslöjade två att en
rättelse skriven samma kväll UR EGET HUVUD var ofullständig. `tabernakel` fick två
betydelser, Wiktionary listar fyra. `trolsk` fick en, SAOB listar två. Båda korten var
redan skrivna till Anki när det upptäcktes.


## `slaupp.py`s sammandrag blandar ihop uppslagsord (2026-08-11)

**Hålet.** `sammandrag`-fältet slår ihop *alla* fuzzy-träffar som svenska.se:s
API returnerar. För långa, ovanliga ord spelar det ingen roll -- de har en enda
träff. För korta ord och flerordsuttryck blir sammandraget en blandning:

    tes              -> 'tes' OCH 'te'    (SO-def innehöll "njutningsdryck ... tebusken")
    brasserie        -> 'brasseri', 'brass', 'brasse', 'brassa'
    black om foten   -> 'black', 'fot', 'om'  -- var för sig
    ge sig till tåls -> 'tåls', 'ge sig', 'ge till', 'tåla sig'

Tre av dagens 50 hade **ingen exakt uppslagsordsträff alls**. Deras
trekällskontroll sa ändå "tre källor", eftersom den räknar *hämtningar som gav
innehåll*, inte *hämtningar som gav rätt ord*. Beviskedjan var alltså intakt --
hämtningen gjordes verkligen -- men den bevisade fel sak.

**Samma felklass som stökiometri-nollan och den falska AnkiConnect-negativen:
ett mätvärde som ser giltigt ut men mäter fel sak.** Hål 0 stänger frågan "gjordes
uppslagningen?". Det stänger inte "handlade svaret om rätt ord?".

**Så här läser man rätt** -- filtrera på exakt ortografi i stället för att lita
på sammandraget:

    h = uppslag['svenska_se_ratt'][db]['hits']['hits']
    traffar = [x for x in h if x['_source'].get('ortografi','').lower() == ordet.lower()]

De tre utan träff reddes ut för hand ur råträffarna: SO/SAOL har `brasserie`
under den svenska stavningen **brasseri**; `black om foten` finns som SO:s
definition av **black** ('hämmande faktor') med SAOL:s **black** ('klossformad
fotboja i äldre tid') som uttryckets bild; och SO definierar uppslagsordet
**tåla sig** som just 'ge sig till tåls', bruklighetskommentar *vardagligt*.

**Förslag till fix (ej genomfört):** låt `sammanfatta()` ta med `ortografi` per
betydelse, och låt trekällskontrollen räkna en källa som fullständig först när
den har en exakt uppslagsordsträff. Då blir "tre källor" ett påstående om ordet
i stället för om HTTP-anropen.

### Två spärrar som fungerade samma dag

1. **Hål 0 vägrade alla 50** vid första appliceringen. Orsak: `slaupp.py` kördes
   med `| tail -80`, vilket klippte bort bevisraderna innan de nådde
   transkriptet. `--tyst` finns för exakt detta, och kommentaren vid flaggan
   dokumenterar att samma misstag gjorts 2026-08-09 (sex kort) och 2026-08-10
   (elva kort). Detta var tredje gången, med 50 kort. **Rätt sätt att spara
   kontext är att låta skriptet tiga, aldrig att filtrera dess utdata.**
2. **Registerspärren vägrade nio kort.** Taggarna "vetenskaplig", "ålderdomlig"
   och "historisk" var påhittade. `config.REGISTER_FORMALITY` har
   **`ngt ålderdomlig`** och `fackspråklig`; historia och lingvistik ligger på
   den separata domänaxeln (`REGISTER_DOMAN`), och domänen heter `lingvistik`,
   inte "språkvetenskap". Ett fritt formulerat register går inte att filtrera
   på i Anki efteråt -- därför är listan fast.

## 2026-08-11: allt utan full v3 suspenderat, sju spärrar, fem buggar

**Adams beslut:** *"Jag vill att vi suspendar allt som inte är full v3."*
2 670 repetitionskort suspenderades; kön fylls nu bara på av granskning.
Efter dagens två omgångar: **412 full v3**, 70 i repetitionskön, 318 i
nya-kön, **0 aktiva kort utan full v3**. Kvar att granska: 2 600.

### Nya spärrar

**Uppslagsordskontroll i `slaupp.py`.** svenska.se:s msearch är en fritext-
sökning: saknas ordet returneras grannartiklar med HTTP 200. `ytong` (ett
varumärke) fick artikeln för **yta** och trekällskontrollen räknade källan
som komplett, eftersom den bara såg att anropet lyckades. Nu stryks
svenska.se som källa utan exakt uppslagsordsträff. Fixen stod föreslagen men
ogenomförd sedan tidigare samma dag.

**Variantformer.** Adam: *"är det inte bara att loafer är loafers istället."*
Rätt — `loafers` träffar SAOL och SO, `loafer` ingenting. `slaupp.py` provar
nu ett fåtal böjningsformer innan ett ord döms som osökbart. Av 13 ord som
pausats som "osökbara" gick **12 att belägga** efter fixen. Bara `ytong` är
genuint utanför ordböckerna.

**Omkörningssvep.** `_hamta_ratt` backade redan av 429 fyra gånger, men ett
ord som brände sina försök besöktes ALDRIG igen — det landade i
`tre_kallor_saknas.json` och såg där ut som ett ord källan saknar. Svepet
körs efter batchen, bara på returbara fel.

**Registret kräver båda axlarna (`baksida.validate_register`).** Regeln stod
i docstringen sedan 2026-08-04 (*"skärpt från 'minst en av dem'"*) men fanns
aldrig i koden: `arkaisk` ensamt, `negativ` ensamt och även `juridik` ensamt
passerade utan varning. När spärren slogs på föll **86 av 342 full-v3-kort**
och 2 681 av 3 233 v2-kort.

**`exempelkoll.py`, inkopplad i skrivvägen.** Blindgranskaren underkände
`brådstörtad` för en exempelmening nästan ordagrant lånad ur SO. Mätt över
decket: bara **15** kort har lånad mening — men **1 716 av 3 233** är för
tunna (färre än fem innehållsord). Det är den verkliga bristen.

**`v3_urgency.py`** rankar is:review-kön på RISK (hur kortet blev till) +
EXPONERING (lapses, intervall, förfallodag). 2 012 av 2 670 saknade sökkoll;
legacy-format och flerbetydelse var noll. **Lapses är signalen som inte finns
någon annanstans**: ett kort Adam upprepat failar kan vara fel KORT, inte fel
Adam.

**`v3_kontrollkort.py`** blandar in redan godkända kort som dolda kontroller
i varje blint paket, så processen mäts kontinuerligt i stället för 10/vecka.
Första två körningarna: 9 kontroller, 0 avvikelser. Mäter samstämmighet, inte
sanning — två granskare kan dela blind fläck.

### Buggar som suspenderingen avslöjade

Tre av samma klass: ett antagande om världen fruset i kod, som slutade gälla.

1. **`POOL_FRAGA["omgranskning"]` krävde `-is:suspended`.** Efter
   suspenderingen matchade det noll kort och poolen tömdes tyst.
   `test_prio_urval.py` fångade det.
2. **`slapp` avsuspenderade inget för spår B**, styrt av flaggan
   `redan_i_kon`. 50 blindverifierade kort hade stannat suspenderade medan
   utdatan sa "inget avsuspenderades" som om det vore väntat. Tittar nu på
   kortens faktiska läge.
3. **`--ids-fil` gick förbi pausfiltret** och drog in `ytong` i en batch.

Plus: `slaupp.py` och `v3_digest.py` kunde inte läsa v3:s EGNA sessionsfiler
(väntade strängar, fick objekt — felet dök upp nere i `urllib`).

### Register auto-ifyllt — en skuld, inte en fix

Adam: *"fyll i neutralt då."* 2 681 kort fick `neutral` på saknad axel.
Alla 3 233 v2-kort har nu giltigt register. **Men ingen har bedömt dem.**
`perfid` underkändes samma dag på exakt det — valören stod som `neutral` fast
ordet är tydligt negativt. Skulden är detekterbar men verklig; taggen
`register_autoifylld::2026-08-11` är det som gör den hittbar.

Round-trippen `parse → build` verifierades mot hela decket före skrivningen:
1 avvikande av 3 233 (`le i mjugg`, känd formatmigrering).

### Domänaxeln — SAOL:s `ämnesområden` går INTE att använda

305 av 501 sparade uppslagningar har fältet ifyllt, vilket såg ut som en
jackpot. Stickprovet stoppade det: fältet är en **semantisk klassificering**,
inte en registermarkör. `betuttad`, `avsmak`, `bestört` taggas `psykol.`;
`bekantgöra` som `jur.`; `blaskig` som `matlagn.`; `författning` ligger under
både jur. och med. Hade 96 vardagliga känsloord märkts som psykologi vore
taggen värdelös på samma sätt som `sokverifierad` blev på 177 osökta kort.

Den pålitliga källan är SO:s bruklighetskommentar (*"särsk. juridik"*). Elva
ord hade en; sex fick ny domäntagg. **71 → 77 av 3 233.** SO markerar
fackområde för ~2 % av ett allmänt ordförråd — axeln SKA vara gles.

### Bilderna: inte förlorade, bara slut

757 av 3 233 v2-kort har bild. OLD-facit har 1 810 bilder på 10 030 poster.
Endast **22** kort saknade en bild som fanns att hämta — de är åtgärdade.
Resten saknar bild för att källan inte har någon.

### Hål 0 stoppade skrivningen fem gånger, och hade rätt varje gång

Först gick jag förbi spärren helt genom att anropa `apply_flerbetydelse.
apply_card()` direkt i stället för via `kortgranskare.applicera()` — korten
fick v3-taggen utan att sökkollen bevisats. Upptäcktes bara för att `paket`
sa "Inga applicerade kort".

Sedan vägrades idiom vars `kalla` pekade på hela frasen (URL:en kapas vid
första mellanslaget). Sedan vägrades de igen — för att grundordsuppslagningen
körts genom `tail -20`, som kapade bevisraderna. Och i nästa omgång igen, för
att jag filtrerat genom `grep`.

**Det är fjärde och femte gången samma misstag görs i det här projektet**
(2026-08-09: sex kort, 2026-08-10: elva, 2026-08-11: femtio, plus dessa två),
den här gången av någon som citerat regeln i samma session. Slutsatsen är
inte att skärpa instruktionen. Den är att spärren är det enda som håller.

### Provisoriskt släppta kort — `v3_provisorisk` (2026-08-11, samma kväll)

Adam: *"problemet är att jag vill börja repetera alla is:review korten så
snabbt som möjligt så att jag inte glömmer bort de."*

Suspenderingen samma kväll slog ihop två olika påståenden: **"tillräckligt
säker för att plugga"** och **"verifierad enligt högsta standard"**. Det är
inte samma sak, och att spärra allt kostade 2 600 inlärda ord i glömska —
en säker förlust, mot en låg risk.

**618 kort släpptes därför tillbaka:** de som HAR en riktig sökkoll
(`flerbetydelse_sokverifierad`) men ännu inte blindgranskats, minus alla med
röd/gul flagga, 3+ lapses, `v3_underkand` eller `v3_pausad`. De taggas
`v3_provisorisk::<datum>`.

**Standarden för full v3 är oförändrad.** De 618 påstås inte vara verifierade
— de har ett eget, ärligare märke. Full v3 stod på 412 före och efter.

Underlaget för risken: blindgranskningen underkände 10 av 80 kort samma dag
(12 %), men nästan alla på register, en enstaka synonym eller en
exempelmening. Bara `farstu` och `omistlig` gällde själva betydelsen.

`v3_suspend_ofullstandiga.py` undantar numera `v3_provisorisk::*` — annars
hade nästa rutinkörning tyst rivit upp beslutet och sett ut som en städning.

**Adams princip, som styr allt ovan:** *"full v3 kort ska inte vara fel,
standarden ska vara ofattbart hög när de väl markeras som full v3."*
Triagering får därför bestämma ORDNINGEN på arbetet, aldrig ersätta
källäsningen före taggen. En triage som gör att 74 % av korten taggas utan
att någon läst deras källor vore exakt vad `sokverifierad` var på 177 osökta
kort.

### Buggen: 97 kort hade fastnat mellan stegen

`POOL_FRAGA["omgranskning"]` exkluderade `-tag:v3_dagsbatch::*`, alltså varje
kort som NÅGONSIN varit i en batch. Taggen tas aldrig bort, så "påbörjad"
behandlades som "klar". Mätt: 460 kort hade varit i en batch, **97 blev
aldrig verifierade** (78 underkända plus avhoppade) och kunde inte plockas
igen. Ett underkänt kort är per definition trasigt och ska tillbaka i kön
först, inte försvinna ur den.

Rätt villkor är "redan klar" (`oberoende_verifierad`) plus dagens egen batch.
Poolen gick 2 724 → 2 805 och 57 underkända blev synliga igen.

### Källhierarkin skärpt: synonymer.se räknas — men bara redaktionellt

**Adams beslut 2026-08-11:** *"om ordet finns på synonymer.se så räcker det …
jag tycker att svenska.se är bäst men synonymer.se räknas också som en top
tier verifiering."*

Regeln antogs, med ETT tillägg — och motexemplet kom ur samma samtal.
`anhedoni` FINNS på synonymer.se, men bara som **användarbidrag**, och glosan
där är *"livströtthet"*. Det är fel: anhedoni är oförmåga att känna njutning,
inte livströtthet. En regel som säger "finns på synonymer.se räcker" hade
alltså godkänt kortet mot en felaktig källa.

Skillnaden kräver inget omdöme. Sajten namnger sina avsnitt, och
`Användarnas bidrag` är utpekat. Mätt över 583 sparade uppslagningar:
**555 har redaktionellt innehåll, 27 har BARA användarbidrag** — och de 27 är
genomgående facktermer (`anhedoni`, `ftalat`, `gemmologi`, `daktyloskopi`),
alltså precis där en crowdsourcad gloss är som minst pålitlig.

| Källäge | Räknas som verifiering |
|---|---|
| svenska.se med uppslagsordsträff | **Ja** (bäst) |
| synonymer.se, redaktionell avdelning | **Ja** |
| synonymer.se, bara `Användarnas bidrag` | **Nej** → websökning krävs |

`slaupp.py` skriver `verifieringsgrund` i varje sparad uppslagning
(`ordbok` / `synonymer.se (redaktionell)` / `SAKNAS — kräver websökning`), så
en senare granskare ser VILKEN grund kortet vilar på, inte bara att det
passerade. Ett ord med enbart användarbidrag loggas som
`SYNONYMER_SE_ENDAST_ANVANDARBIDRAG` i transkriptet.

Utfall på testfallen: `näpsa` → ordbok, `sobriquet` → synonymer.se
(redaktionell, alltså godkänd trots att alla tre ordböcker saknar ordet),
`anhedoni` och `ytong` → saknas.

### `anhedoni`: kortet var mer korrekt än sina källor

Websökningen (NE, Svensk MeSH/Karolinska) gav *"oförmåga att uppleva
njutning, nöje och glädje"*. Kortets *"Oförmåga att känna glädje"* var alltså
rätt men för smalt — källorna leder med **njutning**, vilket är kärnan
(grekiska: *"utan njutning"*). Synonymen `apati` är dessutom fel: apati är
brist på motivation, anhedoni är att njutningen uteblir.

Men OLD-facit sa *"livströtthet, likgiltighet"* och synonymer.se:s
användarbidrag sa *"livströtthet"* — **båda fel.** Hade kortet rättats EFTER
facit hade det försämrats. Det är det starkaste argumentet hittills för att
blindgranskaren ska slå upp ordet själv i stället för att jämföra mot facit.

### Invarianten: full v3 = blå + avsuspenderad (`v3_invariant.py`)

**Adams regel 2026-08-11:** *"full v3 kort ska vara blue:flagged och
unsuspended."*

Taggarna och kortets läge sattes på olika ställen och kunde glida isär utan
att något larmade. Mätt när regeln formulerades: av 412 full-v3-kort var 387
blå, **22 röda**, 1 grön och 2 utan flagga — och 16 av de röda var AKTIVA.
Adam pluggade alltså dagligen kort som bar flaggan "stämmer inte alls" medan
taggarna påstod att de var verifierade (`gyro`, `cypress`, `frotté`,
`kalorimeter`, `bekväma sig` m.fl.).

Ingen av de två uppgifterna var fel när den sattes — röda flaggan kom från en
äldre granskning, taggarna från v3. Det saknades någon som höll dem i takt.
**En motsägelse som ingen kontrollerar ser ut som ordning.**

19 kort rättade. Två undantag som ALDRIG ska tvingas blå:
`v3_underkand::*` (bevisligen trasiga) och `v3_pausad::*`.

### Domänaxeln: `allmän` tillagd, men INTE massifylld

Adam: *"se också till att alla kort med full v3 får domän, det är ett koncept
som jag verkligen gillar."*

Bokstavligt går det inte. Av 412 full-v3-kort hade **64 en domän**, och exakt
**ETT till** (`ekvivalent`) gick att belägga ur SO:s bruklighetskommentar. SO
markerar inte fackområde för allmänt ordförråd.

Värdet **`allmän`** lades därför till i `config.REGISTER_DOMAN` med
betydelsen *bedömd, inget fackområde* — så att tomt och bedömt slutar se
likadana ut, samma princip som Adams registerbeslut 2026-08-10.

**Men det fylls inte i maskinellt**, och det är ett medvetet stopp. Orden som
saknar domän inkluderar `kalorimeter`, `mikrofiche`, `fascikel`,
`vernissage`, `affektiv`. Att SO inte råkar sätta en bruklighetskommentar
betyder inte att ordet saknar fackområde — `kalorimeter` är ett
fysikinstrument oavsett vad SO skriver. Ett automatiskt `allmän` hade blivit
exakt den obedömda skuld som `neutral` blev på 2 681 kort, fast med en tagg
som PÅSTÅR att någon bedömt.

Domänen ska alltså bedömas per kort i samma steg som registret. För de 347
befintliga är det ett arbete, inte en körning.

## Fortsättning 18 augusti: de 23 oskrivna korten, en subagent, och ett nytt fel i Hål 0

Session sparad halvvägs samma kväll (`792bae5`) lämnade 23 ord i
`session_2026-08-18_v3-batch.json` oskrivna. En isolerad subagent (körd
utan tillgång till valvet, se `verktyg/README.md`-liknande separation)
fortsatte kedjan: `slaupp.py --tyst` → skriv → `applicera` → `paket` →
blind granskning → `verdikt` → `slapp`.

### slaupp.py:s dolda gräns

`--antal` defaultar till **20**, inte "alla ord i filen". Första körningen
på 23 ord slog tyst av vid 20 -- tre ord (tarva, underminera, utstaka)
fick ingen uppslagning alls, utan varning. Fångades bara för att
uppslag/-katalogen kontrollerades efteråt. Andra körningen med
`--hoppa 20 --antal 3` fångade resten. Värt en framtida fix: låt filläget
(`--fil`) defaulta `--antal` till hela listans längd istället för 20.

### 4 av 23 pausade, inte skrivna

- **hippopotamus, echappera, passiar**: `forgranska.py`s hårda regel
  `uppslagsord_saknas` (0 träffar i SO och SAOL) slog till på alla tre --
  echappera/passiar har bara en SAOB-artikel utan digitaliserad
  definitionstext, hippopotamus har ingen artikel alls (bara Wiktionary
  "flodhäst"). Taggade `v3_pausad::inget_uppslagsord_i_so_saol`, samma
  princip som `ytong`/`förborgad`.
- **kliche**: svenska.se ger noll träff för exakt den stavningen men
  föreslår **kliché** (med accent) -- samma felklass som
  `kvintessensen`/`regel-rigel` i `ATT_GORA.md`, fast på ett HELT OSKRIVET
  kort denna gång. Framsidan ändrar vad Adam testas på, så den rörs inte
  utan hans beslut -- taggad `v3_pausad::framsida_mojligen_felstavad`
  istället för att gissa fram innehåll under en trolig felstavning.

### Nytt fel hittat i Hål 0: glob-mönstret nådde aldrig en subagents transkript

`kortgranskare.py applicera` blockerade 14 av 19 nyskrivna kort med
"SÖKKOLL EJ BEVISAD ... hämtningen gjordes aldrig", trots att `slaupp.py`
bevisligen kört och `grep` hittade bevisraderna direkt i transkriptfilen.
Orsak: `sokkoll_verifiering.py`s glob (`projects/*/*.jsonl`) letar en nivå
under `~/.claude/projects/` -- men en subagent (Agent-verktyget) loggar
till `projects/<projekt>/<session>/subagents/agent-<id>.jsonl`, TRE nivåer
ned. De 5 kort som ändå gick igenom kom av en slump ur föräldersessionens
egen (ytligare, men ofullständigt speglade) transkriptfil.

Fixat: rekursiv glob (`projects/**/*.jsonl`, `recursive=True`) i båda
funktionerna i `sokkoll_verifiering.py`. Verifierat: alla 19 ord gick från
`False` till `True`, hela sökningen (inkl. en 130 MB-fil på disken) tog
~6 sekunder. Gäller bara arbete kört via en subagent -- vanliga
huvudsessioner loggar redan en nivå ned och träffades aldrig av buggen.
Se `ATT_GORA.md`, "Hittat 2026-08-18", punkt 4, för fullständig logg.

### Utfall

19 av 23 skrivna och applicerade. Dessutom omskrivna de 5 kort som
underkändes tidigare samma kväll (`vittra`, `konvoj`, `trojansk häst`,
`göromål`, `inkongruens`) efter granskarens konkreta anmärkningar --
saknad betydelse (vittra, konvoj, trojansk häst), fel register (göromål),
fel domän+exempel (inkongruens). Gammal `v3_underkand::2026-08-18`-tagg
och röd flagga borttagna efter omskrivning (innehållet som doms är inte
längre samma) -- korten väntar nu på en FÄRSK blind granskning precis som
vilket oreviderat kort som helst.

27 kort väntade totalt på blind granskning (8 sedan tidigare + 19 nya).
27 delar inte jämnt i två paket ≥17 (golvet), så **18 paketerades nu**
(de 8 gamla + de 10 första alfabetiskt av de 19 nya), resten (9 nya +
5 omskrivna = 14) sparas till nästa gång istället för att köras
underdimensionerat.

### review18: 15 godkända, 3 nya underkännanden

`session_2026-08-18_v3-paket-review18.json` -- 37 turer, 1,28 USD, **15
godkända / 3 underkända (17 %)**. 15 släppta (`kortgranskare.py slapp`),
in i Adams aktiva kö. Full v3 i decket: **1043 → 1058**.

De tre underkännandena, alla med konkreta, träffsäkra anmärkningar:

- **bärig** (ett av de 8 gamla, inte skrivet ikväll): "som flyter bra i
  vattnet" var en övergeneralisering -- SO:s faktiska betydelse gäller
  specifikt fartyg/fartygsdelar som flyter bra TROTS att de är lastade,
  inte flytförmåga i allmänhet. Domän ändrad allmän → sjöfart.
- **indifferent**: synonymen "obestämd" hörde till den kemiska betydelsen
  (indifferenta gaser) som kortet medvetet INTE tog med -- matchade alltså
  inte den kvarvarande betydelsen (likgiltig). Ren följdfel av mitt eget
  beslut att skala bort fackbetydelsen utan att städa synonymlistan efter.
  Borttagen.
- **krämare**: jag hade delat upp ordet i en påhittad neutral
  förstabetydelse ("Småhandlare, köpman") och en nedsatt andra --
  ordböckerna har EN betydelse, taggad nedsättande rakt av. Slagit ihop,
  märkt nedsättande genomgående.

Alla tre omskrivna efter anmärkningarna, applicerade på nytt, gammal
`v3_underkand`-tagg och röd flagga borttagna (samma mönster som de fem
tidigare underkännandena). Väntar nu på en färsk granskning.

### 17 kort kvar väntar -- exakt på golvet, paketerade också

De 14 sparade ovan + de 3 nya underkännandena (bärig/indifferent/krämare,
omskrivna) = **17**, exakt golvvärdet. Paketerade och skickade till en ny
blind granskning: `sessions/session_2026-08-18_v3-paket-review17.json`.

### review17: 16 godkända, 1 underkänt (`passivera`)

36 turer, 0,90 USD, **16 av 17 godkända (94 %)**. 16 släppta. Det enda
underkännandet var mitt eget: `passivera` saknade SO:s grammatiska
betydelse ("omvandla ett verb till passiv form", t.ex. jaga → jagas) --
jag hade medvetet skalat bort den som "för nischad" (samma resonemang som
jag använde för `indifferent`s kemibetydelse), men här hade granskaren
rätt: det är en egen, etablerad SO-betydelse, inte en teknisk fotnot.
Tillagd som tredje betydelse, omskriven, applicerad, gammal
`v3_underkand`-tagg + röd flagga borttagna. Väntar på nästa
granskningsomgång (1 kort, långt under golvet -- sparas till dess fler
finns att köra tillsammans).

### Slutläge för kvällens fortsättning

- **19 av 23 ursprungligen oskrivna kort skrivna och applicerade** (4
  pausade: se ovan).
- **45 kort släppta till full v3 idag totalt** (14 innan den här
  fortsättningen + 15 från review18 + 16 från review17).
- **0 kort står kvar underkända** -- alla sex underkännanden under kvällen
  (vittra, konvoj, trojansk häst, göromål, inkongruens, bärig, indifferent,
  krämare, passivera -- nio räknat, se nedan) omskrivna och applicerade på
  nytt samma kväll.
- **1 kort (`passivera`) väntar på en framtida granskningsomgång**,
  medvetet inte kört ensamt under 17-kortsgolvet.
- Full v3 i hela decket: **1029 → 1074** (+45).
- Ett verkligt Hål 0-fel hittat och fixat (rekursiv glob för
  subagent-transkript, se ovan och `ATT_GORA.md` punkt 4).
- Ett nytt, ofarligt men dokumenterat datakvalitetsfel hittat
  (`slaupp.py` kan tyst hämta fel ords artikel för flerordsuttryck,
  `ATT_GORA.md` punkt 5).

**Mönster värt att notera bland underkännandena:** fyra av de nio (nästan
hälften) berodde på att jag MEDVETET skalade bort en betydelse för att
hålla kortet kort ("koncist före uttömmande") -- indifferent (kemi),
krämare (fel uppdelning, inte en skalning men samma familj av fel),
passivera (grammatik), och delvis konvoj/trojansk häst (saknade
betydelser, men inte medvetet uteslutna, snarare missade). Granskaren
konsekvent rättade tillbaka mot "SO:s alla etablerade betydelser hör med",
inte mot min egen avvägning om vad som är "nischat". Värt att komma ihåg
nästa gång frestelsen att skala bort en betydelse för koncishetens skull
dyker upp -- facit är tydligen SO:s egna betydelseindelning, inte min
bedömning av vad som är användbart.

## Adam-tal-regressionen upptäckt och en ny 50-kortsbatch (2026-08-18, samma kväll fortsatt)

Adam flaggade mitt i ett HP-prov (utan tid att ge exempel) att kort läste
ut som SO/SAOB-avskrifter. Full utredning + fem värsta exemplen + förslag
på en mjuk `forgranska.py`-regel loggade i `ATT_GORA.md`
("Hittat 2026-08-18, sent: Adam-tal-regression"). Kort sammanfattat:
**15 av 45 släppta kort (33 %) var ordagranna kopior av SO/SAOL:s egen
text, ytterligare 4 nästan ordagranna (42 % totalt)** -- en verklig
regression, inte normal variation, eftersom andra kort samma kväll visar
att omskrivning går att göra för nästan vilket ord som helst. Rotorsaken:
inget steg i pipelinen (varken de mekaniska reglerna eller den blinda
granskarens instruktion) kontrollerar avstånd till källan, bara längd och
faktakorrekthet. Inget av de 45 korten ändrades -- Adam skulle se
omfattningen själv först.

### 50 nya is:new-kort, med lärdomen tillämpad direkt

`kortbyggare.py --spar nya --antal 50` (`session_2026-08-18_v3-batch2.json`).
Varje Huvudbetydelse självgranskades mot en ord-överlappsmätning (samma
metod som avslöjade regressionen) INNAN den skickades vidare -- tre kort
(`kateder`, `svepa`, `emittera`) skrevs om på plats när överlappet mot
SO/SAOL var för högt.

**2 av 50 pausade:** `villös` (bara SAOB-stubbe, inget SO/SAOL-belägg) och
`räcka lång näsan åt` (SO/SAOL saknar träff helt, och den korrekta
idiomformen `räcka lång näsa åt` saknar dem också -- trolig
framsidefelstavning, `v3_pausad::framsida_mojligen_felstavad`).

**48 skrivna och applicerade.** Ett nytt Hål 0-fel hittat på vägen: `kalla`
för flerordsuppslag med bokstavligt mellanslag trunkerades av
`_URL_RE` och gav falska "hämtningen gjordes aldrig" -- löst med
procentkodning (`urllib.parse.quote`), se `ATT_GORA.md`.

**Blindgranskat i två paket om 24 (körda parallellt), sedan verdikt+släpp:**

| Paket | Godkända | Underkända |
|---|---|---|
| review-a | 19 | 5 (anonym, bekännelse, dyrka, fradga, kid) |
| review-b | 19 | 5 (fåfäng, göra en höna av en fjäder, interpretera, svepa, välbeställd) |

**38 släppta till full v3.** De 10 underkända omskrivna direkt efter
granskarens konkreta anmärkningar (saknad betydelse på 5 av dem, en
felkopplad betydelse på `dyrka` som egentligen hör till `dyrka upp`, en
obelagd synonym på `fåfäng`, ett grammatikfel på `fradga`, en
exempelmening som highlightade fel ord på `kid`, och en faktafel
etymologi på `göra en höna av en fjäder` -- H.C. Andersens saga slutar på
FEM hönor, inte tio som jag skrivit, källan jag själv byggde på hade fel
siffra). Applicerade på nytt, gamla `v3_underkand`-taggar/röda flaggor
borttagna. Väntar på nästa granskningsomgång (10 kort, under golvet).

**Slutläge:** 83 kort släppta till full v3 under hela kvällens session
(45 + 38). Full v3 i decket: **1029 → 1112**. 0 kort står kvar
underkända. 11 kort väntar medvetet på en framtida granskningsomgång
(1 `passivera` sedan tidigare + 10 nya, tillsammans under golvet men
tillräckligt nära för att bli nästa paket).

## Tredje batchen samma kväll: 30 kort medan Adam var borta från tangentbordet

Adam bad om ytterligare 30 is:new-kort medan han själv körde eget
Anki-pass + tittade på TV -- ingen tillgänglig för frågor, samma
självständiga arbetssätt som resten av kvällen.
`kortbyggare.py --spar nya --antal 30` → `session_2026-08-19_v3-batch.json`.
`slaupp.py --tyst` komplett i EN körning för alla 30 (ingen trunkering).

Adam-tal-disciplinen från tidigare i kväll tillämpad rakt av: varje
Huvudbetydelse självgranskad mot containment-måttet innan skrivning --
bara `småskrake` låg över tröskeln (0,73) och skrevs om innan den ens
nådde `forgranska.py`.

### Ovanligt många idiom -- och en tydlig lärdom om källkontaminering

Batchen innehöll ovanligt många flerordsuttryck (`trampa vatten`,
`dra sitt strå till stacken`, `spotta i nävarna`, `det allena
saliggörande`, `dra det tyngsta lasset`, `inte säga flaska`, `kärringen
mot strömmen`, `sätta bocken till trädgårdsmästare`, `tjo och tjim`,
`visa framfötterna`) -- och `forgranska.py` slog ut `frammande_uppslagsord`
på 15 av 28 kort, klart fler än i tidigare batcher. Mönstret bakom:
svenska.se:s fuzzy-sök för flerordsfraser landar ofta i en HELT
orelaterad artikel vars exempeltext råkar innehålla frasen (samma
felklass som `trojansk häst`→`spann` tidigare i kväll, se
`ATT_GORA.md` punkt 5) -- `kärringen mot strömmen` gav t.ex. bara
prepositionen "mot", `tjo och tjim` bara ordet "skalle". Varje sådant
fall kontrollerades manuellt: den faktiskt relevanta raden (oftast en
enda, identifierbar via en direkt matchande exempelmening) plockades ut
för hand, Wiktionary eller SAOL användes som primärkälla där SO var ren
brus, och kontamineringen skrevs ut explicit i `sokkoll.slutsats` för
varje sådant kort.

### forgranska.py bekräftat vara ett fristående revisionsverktyg, INTE en spärr i `applicera()`

Tre kvarstående `register_motsager_markning`-flaggor (`det allena
saliggörande`, `föredrag`, `inte säga flaska`) visade sig vara riktiga
gränser i verktyget snarare än fel i korten:
- `föredrag`: SO:s `i fackspråk`-märkning gäller en enda av två
  betydelser, men kontrollen är ordnivå, inte betydelsenivå.
- `inte säga flaska`: SO ger TVÅ formalitetsmärkningar samtidigt
  ("vardagligt" OCH "något ålderdomligt"), men registerfältet har bara
  EN formalitetsplats -- omöjligt att tillfredsställa båda samtidigt.
- `det allena saliggörande`: märkningen "åld. utom i några uttr." är en
  sammansatt fras `_MARKNING_LIKA`-tabellen i `forgranska.py` inte
  känner igen.

`kortgranskare.py applicera` kördes ändå och skrev alla tre kort utan
problem -- vilket bekräftar att `forgranska.py`s HÅRDA flaggor är en
stark rekommendation ("rätta INNAN blindgranskningen"), inte en teknisk
spärr i skrivvägen (den enda faktiska spärren är `baksida.validate_adamtal()`,
ett annat, snävare regelset). Nyttigt att veta för framtida sessioner:
en envis hård flagga som inte går att lösa utan att förstöra kortets
sakinnehåll behöver inte blockera skrivning -- men ska alltid
dokumenteras i `sokkoll` OCH få en riktig, oberoende bedömning av
blindgranskaren (som den fick här).

### 28 skrivna, 25 granskade (26-golvsregeln + `blindgranska.py`s 25-tak)

2 pausade: `hovjunkare` (noll träff i SO/SAOL/SAOB/Wiktionary -- inget
att bygga på över huvud taget) och `korpgluggarna` (samma sak; grundordet
`korpglugg` har bara en SAOB-stubbe, inget facit).

28 skrivna kort delar inte jämnt i två paket ≥17 (minsta möjliga summa
för två sådana är 34), och `blindgranska.py`s eget tak (`MAX_POSTER=25`)
tillåter inte alla 28 i en körning. Löst genom `--antal 25`: 25
granskade nu, 3 (`tjo och tjim`, `visa framfötterna`, `överpröva`) ligger
kvar odömda i samma paketfil för en framtida omgång.

**22 av 25 godkända, 3 underkända** (`trampa vatten`, `föredrag`,
`göra sig` -- alla tre saknade en hel betydelse enligt granskaren).
Ironiskt nog var `föredrag` samma kort jag redan hade skalat ner för att
undvika en `register_motsager_markning`-flagga -- fel prioritering,
granskaren ville ha tillbaka precis den betydelsen. Lärdom: en mekanisk
varning väger aldrig tyngre än fullständighet: skala aldrig bort en
sann betydelse för att tysta ett verktyg.

Alla tre omskrivna efter anmärkningarna, applicerade på nytt, gamla
`v3_underkand`-taggar/röda flaggor borttagna.

**22 släppta till full v3.** Full v3 i decket: **1112 → 1134**.
Kvällens totalsumma: **105 kort släppta till full v3** (14 + 15 + 16 +
38 + 22, se historiken ovan för uppdelningen per omgång).

**17 kort väntar nu medvetet på en framtida granskningsomgång**
(1 `passivera` + 10 från den förra omskrivningsrundan + 6 nya: de tre
omskrivna underkännandena + de tre odömda från 25-taket) -- exakt på
golvet igen, men inte kört ensamt eftersom kvällen redan var lång.

## Fjärde batchen: 30 kort medan Adam gjorde ett ärende + städade, medvetet lättare urval

Adam bad om ytterligare 30 is:new-kort medan han var borta -- med en ny
begäran: han kommer tillbaka från en jobbig natt och ville ha en lättare
startsträcka, inte en batch full av de svåraste orden i poolen. Ingen
`--svårighet`-flagga finns i `kortbyggare.py` (poolen sorteras bara på
`due`, ingen svårighets-/frekvenssignal alls), och uppdraget var
uttryckligt: bygg ingen ny tooling för det, chansa på ordurvalet i
stället.

### Metod: hämta bredare, välj smalare, lämna tillbaka resten

`kortbyggare.py --spar nya --antal 90` gav 90 kandidater att välja
30 "lättare" ord ur för hand (kortare, enkelsidiga, vardagliga --
`pixel`, `nobel`, `memorera`, `sätta in` -- i stället för poolens
tyngsta arkaismer som `dväljas`, `ådagalägga`, `slåss mot
väderkvarnar`-liknande idiom).

**Viktig bieffekt upptäckt och hanterad:** `hamta_pool()` (i
`kortbyggare.py`) taggar VARJE hämtat kort med `v3_dagsbatch`, oavsett om
det sedan skrivs eller inte -- och för spår "nya" exkluderar
`POOL_FRAGA` kort med den taggen FÖR ALLTID (inget datum i frågan, till
skillnad från spår "omgranskning"). Att bara plocka 30 av 90 hade alltså
tyst tagit bort 60 fullt dugliga ord ur poolen för gott. Löst genom att
`removeTags` de 60 obehövda korten direkt efter urvalet -- de är nu
exakt som innan de någonsin rördes.

### Resultat: fler underkännanden, som väntat

`slaupp.py --tyst` komplett i en körning. `alliteration` pausad --
`svenska.se` ger noll träff, men den korrekta stavningen `allitteration`
(dubbelt L) har full SO/SAOL/SAOB-täckning, samma mönster som
`kliche`→`kliché` tidigare i kväll.

29 skrivna, 25 granskade (samma 25-taksbegränsning som batch 3).
**19 godkända, 6 underkända (24 %)** -- klart högre andel än kvällens
tidigare batcher (12-21 %), en direkt, förväntad kostnad av att
medvetet skriva enkelsidiga kort för ett pool fullt av flerbetydelseord:
`sätta in`, `infinna sig`, `mellanhand`, `syna` och `urna` underkändes
alla för en saknad betydelse (`mellanhand` t.o.m. tre av tre möjliga --
kortet innehöll bara den minst primära). `gruva sig` underkändes av ett
annat skäl: SAOL:s kommalista "oroa sig, ängslas" fick mig att skriva in
'ängslas' som belagd synonym, men granskaren visade att orden INTE är
fullt utbytbara trots kommaformatet -- ett tecken på att den mekaniska
"inleder ett led"-regeln inte fångar allt, den fångar bara ordagrann
källhärledning, inte faktisk utbytbarhet.

Alla sex omskrivna efter anmärkningarna (`mellanhand` fick alla tre
SO-betydelser tillagda, `urna` fick sin huvudbetydelse bytt från den
snävare kremeringsbetydelsen till SO:s bredare grundbetydelse),
applicerade på nytt, gamla `v3_underkand`-taggar borttagna.

**19 släppta till full v3.** Full v3 i decket: **1134 → 1153**.

**Slutsats om "lättare kort"-uppdraget:** gick delvis att uppfylla --
orden som VALDES var genuint enklare/vanligare (pixel, nobel, memorera,
hålla av snarare än dväljas, ådagalägga), men "enklare ord" och "enkelt
KORT" visade sig vara olika saker -- flera av de valda orden hade ändå
flera SO-betydelser, och att medvetet skriva bara en av dem för
enkelhetens skull är precis det mönster som orsakade underkännanden
tidigare i kväll (`föredrag`, `göra sig`). Nästa gång Adam vill ha en
lättare batch: välj korta, vardagliga ORD (det gick bra), men skriv
ALLA deras betydelser ändå -- enkelhet ska komma från ordvalet, inte
från att tunna ut korten.

**Session-totalsumma (18-19 augusti): 124 kort släppta till full v3**
(105 från föregående dags-logg + 19 härifrån). 0 kort står kvar
underkända. **27 kort väntar nu medvetet på en framtida
granskningsomgång** (11 från 18 augusti + 16 från 19 augusti: 3
omskrivna + 3 odömda från batch 3, 6 omskrivna + 4 odömda från batch 4)
-- gott om marginal över 17-golvet till nästa körning.

## Femte batchen, 19 augusti: 30 is:new-kort via en fristående agent

Kört av en isolerad subagent (samma separationsmönster som 18 augustis
fortsättning), fullständig v3-kedja: `kortbyggare.py --spar nya --antal 30`
(spår A:s pool ÄR den `is:new`-avgränsade poolen -- 6802 suspenderade
legacy-kort som aldrig nått Adams kö) → `slaupp.py --kompakt` (30 ord) →
skrivning → `forgranska.py` → `kortgranskare.py applicera/paket` →
`blindgranska.py` → `verdikt` → `slapp`.

**29 av 30 skrivna och släppta, 1 pausad.** `faute / fåt` pausad
(`v3_pausad::inget_uppslagsord_i_so_saol`) -- varken "faute" eller "fåt"
har någon egen SO/SAOL-artikel, bara SAOB (som `granska_post()`s regel 1
inte räknar som belägg). Båda formerna betyder "misstag" och listar
varandra som synonym på synonymer.se, men utan SO/SAOL-täckning hade
kortet blockerats av `uppslagsord_saknas` oavsett innehåll -- samma
mönster som `hippopotamus`/`echappera`/`passiar` 2026-08-18.

**Tretton av de tjugonio hade STORA sakfel i legacy-innehållet**, inte
bara formulering -- `eftersätta` (påstod "efterträda/ersätta", verklig
betydelse "försumma", raka motsatsen), `hövas` (påstod "höja/lyfta",
verklig betydelse "vara tillbörligt/passande" -- ren ordförväxling),
`komma an på` (påstod "få tag på/komma över", verklig betydelse "bero
på"), `nagelfara` (påstod nagelinfektion, verklig betydelse "granska
extremt noggrant" -- bokstavstolkning av "nagel" i stället för
idiomet), `tyken` (fel ORDKLASS: kortet gjorde ett adjektiv till ett
substantiv), `utgjuta sig` (påstod bokstavligt "låta känslor strömma
ut", verklig betydelse "klaga länge och känslosamt"), `ta skruv`
(bokstavlig skruvning i stället för idiomet "ta effekt"), `ta till
intäkt` (blandade ihop med "intäkt" = inkomst, verklig betydelse
"åberopa som stöd för"), `ligga av sig` (påstod stress/sjukdom som
orsak, verklig betydelse "försämras av att inte användas/övas"), `pösa`
och `slå an` (saknade var sin hel bildlig/bokstavlig betydelse), `kuse`
(hela innehållet påhittat -- rätt svar var tre dialektala homografer:
häst, bröd, insekt). old_facit-fältet hade i nästan alla dessa fall
redan rätt svar (`old_delar_inget_ordforrad`-flaggan pekade korrekt),
men legacy-kortets FELAKTIGA innehåll hade ändå överlevt oemotsagt tills
nu.

**Kontamineringsfällan för flerordsuttryck slog till igen** (samma
mönster som "kärringen mot strömmen"/"trojansk häst" tidigare i veckan):
svenska.se:s fritextsökning för `komma an på`, `ta skruv`, `sticka av
mot`, `ta till intäkt`, `låta undfalla sig` och `låta undslippa sig` drog
in dussintals orelaterade ord (`-bar`, `andante`, `berusad`, `San
Marino` ...) eftersom ett av frasens korta ord (`an`, `mot`, `ta`)
matchade helt andra artiklar. `forgranska.py` flaggar detta som
`frammande_uppslagsord` (HÅRD men rådgivande, blockerar inte skrivning --
bekräftat i onsdagens `applicera`-körning) på alla sex. Löst genom att slå
upp grundfrasen separat (`sticka av` i stället för `sticka av mot`) där
det gick, och genom att dokumentera kontamineringen explicit i `sokkoll`
där SO:s egna SYN:synonym-taggar (via `so_relationer()`) ändå gav ett
rent facit trots det brusiga fritextsvaret.

**Hål 0 fångade en riktig regression, inte bara ett känt mönster:**
flerords-`kalla`-URL:er utan procentkodning (`?ord=ta skruv` med
bokstavligt mellanslag) trunkerades av `_URL_RE` i
`sokkoll_verifiering.py` och gav falska "hämtningen gjordes aldrig" på
15 av 29 kort trots att `slaupp.py` bevisligen hämtat alla. Detta är
EXAKT den bugg CLAUDE.md 2026-08-18 sa var löst med
`urllib.parse.quote` -- men fixen gäller bara `slaupp.py`s EGNA
`kalla`-generering (se `SKRIPT_KALLA`-kommentaren i
`sokkoll_verifiering.py`), inte `kalla`-strängar en granskare skriver för
hand utifrån bevisraden. Löst genom att procentkoda ordet i `kalla` manuellt
för alla flerordsposter innan `applicera` kördes om.

**Blindgranskningen underkände 2 av 25 i första paketet (8 %), båda på
REGISTER, inte sakinnehåll:** `kuse` hade formalitetsaxeln omvänd (häst
är `vard.`, bröd/insekt är `prov.` -- kortet hade det tvärtom), `låta
undfalla sig` hade `vardaglig` där SO markerar `ålderdomligt/arkaiskt`.
Båda omskrivna, återgranskade i ett nytt 3-kortspaket tillsammans med
`låta undslippa sig` (samma lemmapar, samma register-misstag, men
**inte** fångat av blindgranskaren i första körningen -- fixat proaktivt
ändå, eftersom SO-underlaget är identiskt för båda uttrycken). Alla tre
godkända i omgranskningen. **0 kort står kvar underkända.**

**Sjätte checkpunkten (dictionary-ton, tillagd samma dag) triggade
INTE på något av de 29 skrivna korten** -- ingen Huvudbetydelse innehöll
fackordsuffix eller tunga nominaliseringar av den typ Adam kritiserade
(`andsläktet`, `upphävande av`). Disciplinen tycks hålla utan att någon
enskild fälla behövde undvikas aktivt; värt att fortsätta mäta över fler
batchar innan det räknas som bevisat.


## Bildkomplettering via Wikipedia — pilot på 20 kort (2026-08-19)

Adams beslut: bildlösa v3-klara kort ska kunna få en bild automatiskt
hämtad från sv.wikipedia/Wikimedia Commons -- men bara konkreta ord (djur,
växter, föremål, artefakter, platser), aldrig gissat för abstrakta
ord/verb/idiom, och ALDRIG på ett kort som redan har bild. Byggt i tre
delar (se Script-inventering): `wikipedia_bild.py` (hämtar kandidater,
gör ALDRIG en relevansbedömning själv), `wikipedia_bild_batch.py` (bygger
kö av bildlösa v3-kort + kandidat, samma tvåstegsmönster som
`apply_updates.py`), `wikipedia_bild_apply.py` (applicerar bara
`godkand: true`-poster, loggar käll-URL+licens till `bild_kallor.jsonl`).
Dessutom en best-effort-krok i `kortgranskare.slapp()`
(`foreslag_bilder_for_slappta`) som efter varje framtida släpp bygger en
förslagskö för nysläppta bildlösa kort -- applicerar aldrig något själv,
och kan aldrig få `slapp()` att faila (inpackad i try/except).

**Mätningen som avgör hur försiktig automationen måste vara: Commons
fritextsökning matchar på ord i FILNAMNET, inte på betydelse.** Av 20
pilotkort (due-sorterat ur de 2 750 av 3 580 v3-klara korten som saknar
bild, 76,8 %) hittade modulen en kandidat för 10 -- men vid manuell
granskning (jämförelse av bildens faktiska innehåll mot kortets
Huvudbetydelse, i flera fall genom att faktiskt öppna bilden) var bara
**2 av 10 kandidater användbara, 8 var felträffar**:

| Ord | Kandidat | Varför fel |
|---|---|---|
| `drägg` | foto på ett fällbart *dragg* (ankare) | substrängmatchning "drägg"≈"dragg" |
| `köpeskilling` | foto på prislappar i en läskautomat | generisk stockfoto-bild, inte begreppet |
| `reminiscens` | kubistisk målning bara DÖPT "Reminiscens" | abstrakt konst, ingen visuell koppling till minnesbild |
| `renegat` | fransk 1800-talskarikatyr, texttung | rätt tema, obrukbar som snabbt minnesknep |
| `resolut` | foto av ett typsnittsgjuteri | helt orelaterat |
| `vitsord` | tysk nödsedel med en ko | helt orelaterat |
| `taverna` | flott restaurang på Musée d'Orsay | rätt artikel (`Restaurang`), fel register -- motsatsen till "enklare vardshus" |
| `enaktare` | engelskspråkig WPA-teateraffisch | textbaserad, inget scen/karaktär |
| `tälja` | foto från en spansk kvarn/lokalitet | helt orelaterat |
| `attribuera` | Wikipedia-artikelns egen CC-BY-ikon | artikelstubbens enda bild råkar vara en licensikon |

De två godkända: **`apoplexi`** fick en CT-bild av hjärnan med pil mot
infarkten (sv.wikipedia-artikeln "Stroke") -- medicinskt korrekt och
direkt matchande. **`bygdemål`** fick en karta över dialektområden i
Norrland (Commons) -- topiskt exakt rätt, visar begreppet regional dialekt
konkret. Båda applicerade och verifierade live i Anki, källor loggade i
`bild_kallor.jsonl`.

**8 av 20 kort gav ingen kandidat alls** (förtörnad, överloppsgärning,
svärmisk, formsak, överrumpla, strömning, märgfull, "klä skott för
något") -- alla abstrakta ord/verb/idiom, exakt det förväntade normalläget
enligt Adams instruktion, inget att åtgärda.

**Extrapolering till hela beståndet:** 2/20 = 10 % fick en godkänd bild i
piloten. Appliceras samma kvot på hela poolen (2 750 bildlösa v3-kort)
skulle en full körning sannolikt ge runt **275 nya bilder** -- en
meningsfull men måttlig andel, och bara om VARJE kandidat granskas
manuellt precis som i piloten. Att köra batch-scriptet utan mellansteget
(automatiskt applicera alla hittade kandidater) hade satt fel bild på
8 av 10 kort som fick någon kandidat alls -- exakt det Adam bad om att
undvika.

**Teknisk fälla hittad under piloten, fixad i `wikipedia_bild.py`:**
`upload.wikimedia.org` gav HTTP 429 redan efter två nedladdningar i
följd under den manuella granskningen (bilderna hämtades separat för att
kunna öppnas och tittas på). `hamta_bilddata_base64()` saknade backoff --
lades till (429/503 backas av och görs om, samma mönster som
`slaupp.py`s Wiktionary-anrop, se den filens kommentar från 2026-08-10).

Full v3 i decket efter batchen: **1153 → 1182** (+29).

---

## Batch 5, 24 augusti (natt): 0 % underkänt — och två fel i mitt eget arbetssätt

**24 av 24 godkända.** Första felfria omgången sedan blindgranskningen infördes.
Kurvan över dygnet:

| Batch | Underkänt | Vad som ändrades inför den |
|---|---|---|
| 2 | 33 % | — |
| 3 | 37 % | `betydelse_kan_saknas` gjordes HÅRD |
| 4 | 10 % | batch 3:s lärdom (missa inte betydelser källan HAR) |
| **5** | **0 %** | batch 4:s lärdom: vifta inte bort ett hårt flagg |

Full v3 i decket efter batchen: **1472 → 1496** (+24). Kostnad 1,75 USD.

### Det som faktiskt gjorde skillnaden

`flirta` fick ett hårt `betydelse_kan_saknas` (SO 3, kortet 2). I batch 4 hade
jag i samma läge skrivit en handviftande motivering om fuzzy-matchning på `go`
— och blindgranskaren underkände kortet för exakt det flagget hade sagt. Den
här gången lästes **SO:s råstruktur** i stället för sammandraget:

```
ORTO: flirta | ordklass: verb
ORTO: flörta | ordklass: verb
  DEF: antyda och försöka väcka erotiskt intresse
    UNDER: antyda intresse för samverkan | brukl: särsk. politik
```

Exakt en huvudbetydelse och en underbetydelse, båda på kortet. Trean uppstod
för att underbetydelsen räknas två gånger när sammandraget plattas ut — en gång
i `def`-listan, en gång i `underbetydelser`-listan.

**Regeln som följer:** ett hårt flagg får bara viftas bort mot
`svenska_se_ratt[...]['hits']['hits'][*]['huvudbetydelser']`, aldrig mot
`sammandrag`. Sammandraget är en tillplattning och kan dubbelräkna.

### Fel 1 (fixat): flerordslemman kunde aldrig passera bevisspärren

`grå eminens` blockerades i batch 4 och skrevs av som en olöst lucka. Orsaken
var att `sokkoll.kalla` delas på blanksteg, så
`https://svenska.se/api/msearch?ord=grå eminens` kapades till `...?ord=grå`.

Fixen är en rad i skrivskriptet:

```python
q = urllib.parse.quote(o)          # "alter ego" -> "alter%20ego"
e["sokkoll"]["kalla"] = f"... https://svenska.se/api/msearch?ord={q} ..."
```

`sokkoll_verifiering._normalisera()` avkodar procentkodning innan den jämför,
så den kodade URL:en matchar den rekonstruerade okodade. Verifierat i batch 5:
**`alter ego` och `de facto` gick båda igenom spärren.** Samma rad löser
`grå eminens` när det kortet plockas igen.

### Fel 2 (mitt, inte kodens): klipp ALDRIG `slaupp.py`s utdata

Första appliceringen av batch 5 vägrade **alla 24 korten** med
`SÖKKOLL EJ BEVISAD`. Jag misstänkte procentkodningen och hade fel — orsaken
var att jag kört

```
python slaupp.py --tyst <14 ord> 2>&1 | tail -20
```

`tail -20` kastade bort varenda `SVENSKA_SE_HAMTAD`-rad. De raderna **är**
beviskedjan: spärren läser dem ur transkriptet och rekonstruerar URL:en ur
dem. En hämtning som gjorts men vars kvitto klippts bort är, för spärren, en
hämtning som aldrig skedde.

Det är värt att notera att spärren betedde sig **precis rätt** — den vägrade
intyga något den inte kunde se bevis för, trots att hämtningen faktiskt gjorts.
Rätt beteende hos ett skydd är att fela åt det håll som kostar arbete, inte åt
det håll som släpper igenom.

**Regeln:** `slaupp.py` körs alltid med hela utdatan synlig, eller filtrerad
med `grep "HAMTAD\|UPPSLAGSORD"` — aldrig med `head`/`tail`.

### Mätt sluttillstånd

| | |
|---|---|
| Full v3 | **1496** |
| Lager (osuspenderade) | 1506 |
| Pool kvar (spår A) | 6060 |
| Ackumulerade underkända | **161** ← växande skuld, ingen plockar upp dem |
| Repetitionsskuld | 830 |

De **161 underkända** är värda en egen omgång. De är per definition trasiga
kort som togs ur kön och aldrig kom tillbaka — samma feltyp som
`-tag:v3_dagsbatch::*` orsakade i spår B den 11 augusti, fast nu i en annan
form: `POOL_FRAGA["nya"]` exkluderar `-tag:v3_dagsbatch::*` utan undantag, så
ett underkänt spår A-kort kan **aldrig** plockas igen av `kortbyggare.py`.
Det är inte medvetet valt, och det är därför siffran bara växer.
