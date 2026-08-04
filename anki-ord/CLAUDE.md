# anki-ord — System A status (Anki ORD-kortsgranskning)

Se [../CLAUDE.md](../CLAUDE.md) för helheten. Denna fil = teknisk detalj +
exakt var vi står, så en ny chatt kan fortsätta direkt.

## Bekräftat mot riktig, öppen Anki (Fas 0, `discover.py`, klart 2026-08-03)

- Deck: `Humanities::Languages::Svenska 10 000`
- Note type: `Grundläggande-adc63`
- Fält: `Framsida` (ordet), `Baksida` (EN HTML-blob, se `baksida.py`)
- Flaggor: flag:1 = **Röd** (fel) · flag:2 = **Gul** (osäker) · flag:4 =
  **Blå** (stämmer, konfidens 9-10) · flag:3 = **Grön** (dels 84 gamla kort
  utanför scope, dels nya konfidens-≤8-granskade kort sen 2026-08-04 — skilj
  dem åt via tagg `konfidens::N`, se style_guide.md)
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
| `apply_updates.py` | Fas 3 — skriver godkända ändringar (`updateNoteFields` via `baksida.build`, plus `Framsida` om `proposed_ord` satt). Kräver `entry["confidence"]`: ≤7 skippas (ej redo), 8→flagga Grön, 9-10→flagga Blå (fixat 2026-08-04, se style_guide.md — tidigare flaggade koden fellaktigt ALLTID blått oavsett konfidens). Taggar `granskad::<datum>` + `konfidens::N`. `apply_single` per kort under passet, eller batchat i `main()` |
| `style_guide.md` | "Adam-tal"-checklista — struktur, grundregler, bevara humor, bildhantering, vanliga fällor |

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

## Style guide — kärnpunkter (full version i `style_guide.md`)

- Målstruktur 3 synonymer / 2 definitioner, avvikelse OK om ordet motiverar det
- Korta meningar, vardagliga ord, konkret före abstrakt
- Bevara humor i befintliga exempelmeningar — förenkla språk, inte tonen
- Bilder är personliga minnesknep — kritisera/föreslå fritt, ändra ALDRIG
  utan Adams uttryckliga godkännande (kostar credits per generering)
