# Adam-tal — checklista för förenklade definitioner

Detta dokument växer i takt med granskningspassen. Målet är definitioner som
Adam förstår direkt, utan att behöva slå upp fler ord.

## Struktur — icke förhandlingsbart

- **Flaggan är den enda sanningskällan.** Taggar (ai_uncertain, ai_optimized,
  ai_failed, granska_först) är historik, inte fakta. Ett kort kan vara taggat
  ai_uncertain men ha blå flagga — då har Adam redan själv rättat det och det
  är korrekt. Lita alltid på flaggan, aldrig på taggen, vid konflikt.
- **HTML-strukturen i Baksida måste bevaras exakt**: synonymer i blå font
  (`#3498db`), `<br><br>` mellan synonymer och definitionslista, `<ol><li>`
  för definitioner, `<i>` för exempelmeningen, bild sist om den finns.
  `baksida.py` sköter detta automatiskt — skriv aldrig fritext direkt i fältet.
- **Inget fast antal synonymer/definitioner.** Målet är snabb inlärning av
  10 000 ord — varje extra synonym/definition är en sak till att minnas, så
  ta bara med det som faktiskt hjälper. En synonym räcker om ordet bara har
  en riktigt utbytbar. Noll är okej om ordet saknar äkta synonym (skriv bara
  definition + exempel då). Fler än 3 är okej om de är genuint distinkta
  och nyttiga. Tvinga aldrig fram konstlade extra synonymer/definitioner
  för att nå ett målantal — hellre för få än för många.

## Grundregler

- Korta meningar. En tanke per mening.
- Vardagliga ord. Undvik akademiska/latinska synonymer i själva förklaringen
  (även om ordet som förklaras är avancerat).
- Konkret före abstrakt — förklara med ett scenario eller en jämförelse om
  det gör betydelsen tydligare.
- Om ordet har flera betydelser: ta bara med den betydelse som är relevant
  för HP:s ordförståelse (inte en uttömmande ordboksdefinition).
- Definitionen ska kunna läsas högt och förstås direkt, utan omläsning.

## Bevara humor

Vissa kort är skrivna med humor (t.ex. i exempelmeningen) — det hjälper Adam
faktiskt komma ihåg orden. Förenkling till Adam-tal ska INTE platta ut eller
ta bort humorn. Om ett kort redan har ett kul/minnesvärt exempel: behåll
tonen, förenkla bara språket om det behövs. Lägg gärna till humor i nya
förslag där det gör ordet lättare att minnas, så länge det inte gör
betydelsen otydlig.

**Bra mönster**: en konkret, lite absurd karaktär/scen istället för en torr
mening. Exempel — "vitkrage": inte bara "en kontorsarbetare i finkläder",
utan "Jake the narrator, helt deprimerad på sitt kontor" — en person med
namn och känsla fastnar bättre än en generisk beskrivning. Sikta på detta
när ordet tillåter det.

## Bilder

Bilder är personliga minnesknep, inte dekoration. Källor: originalskaparen av
decket, Daniel (som gav Adam det uppdaterade decket), och Adam själv. Vissa
bilder är kopplade till Adams egna känslor/uppfattning om ordet — rör dem
aldrig utan att fråga.

- **Kritik av befintlig bild**: matchar den ordets betydelse och känsla? Om
  den är missvisande eller för generisk (stockfoto-känsla) — flagga och
  föreslå ersättning, men ändra ALDRIG utan Adams godkännande.
- **Ny bild**: föreslå bara om ordet vinner på det (abstrakta ord vinner ofta
  mer på en tydlig karaktär/scen än en bokstavlig illustration). Samma
  princip som humor ovan: en konkret, gärna lite absurd karaktär i en scen
  slår generiska bilder — se "Jake the narrator, deprimerad på sitt kontor"
  för vitkrage.
- Bilden sparas i Anki-media och bäddas in i Baksida FÖRST efter att Adam
  uttryckligen godkänt den specifika bilden (kostar riktiga credits per
  generering — generera inte i blindo).

## Källor för faktakoll

Föredra i denna ordning: **svenska.se** och **synonymer.se** (Adams
godkända källor, alltid först). Bara om ordet/betydelsen inte täcks där,
sök korrekt fakta på annat håll.

## Synonymer kopplade till olika definitioner

Om ett ord har flera definitioner och synonymerna hör till olika
betydelser: gruppera synonymerna per definition, separera grupperna med
mellanslag-semikolon-mellanslag ` ; ` — inte bara `,`. Semikolonet ska ha
SAMMA färg/font som synonymerna (`#3498db`), inte vanlig text. Exempel
(kautschuk, 2 betydelser): `gummi, naturgummi ; radergummi` — gummi/
naturgummi hör till def1 (råämnet), radergummi till def2 (den äldre
betydelsen "radergummi").

## Highlight av ordet i exempelmeningen

Ordet (eller böjningen av det) i exempelmeningen ska ALLTID märkas med
samma blå font som synonymerna: `<font color="#3498db">ordet</font>`.
Inte valfritt — gäller varje nytt/omskrivet exempel.

## Exempelmeningar — alltid bara en

Även vid 2+ definitioner: EN exempelmening per kort, inte en per
betydelse. Tempo vinner över fullständighet — Adam ska hinna igenom
korten i bra takt. Välj den mening som passar bäst för HP-sammanhang
(oftast den vanligaste/mer formella betydelsen).

## Vanliga fällor att undvika

- Att definiera ett ord med ett annat lika svårt ord.
- Cirkeldefinitioner (ordet förklaras med sig självt eller en synonym utan
  extra förklaring).
- För långa definitioner som försöker täcka alla nyanser på en gång.

## Framsidan kan också vara fel

Baksidan är inte den enda platsen ett fel kan sitta. Om ordet på Framsidan
självt är fel — t.ex. saknar ett reflexivt "sig" som behövs (blamera →
blamera sig) eller är felstavat — rätta det också. Kolla alltid mot en
källa (svenska.se/synonymer.se, annars annan lexikal källa) innan du
ändrar Framsida, samma sourcing-regel som för Baksida-fakta.

**Bas-ord och "sig"-form är INTE automatiskt samma kort eller automatiskt
två kort.** Vissa ord finns bara i en form (antingen bara "X" eller bara
"X sig"). Andra ord har både en transitiv/bar form och en genuint skild
reflexiv betydelse (t.ex. "blamera" = skämma ut/misskreditera NÅGON
ANNAN, vs "blamera sig" = göra bort sig SJÄLV — två olika, verifierade
betydelser, se SAOB). Om två separata kort råkar dela nästan samma
Framsida-ord: verifiera i ordbok om båda formerna verkligen är etablerade
och skilda innan du antar att det ena är fel/duplicat. Slå aldrig ihop
eller döper om utan att kolla först.

## Konfidensmärkning (0–10) vid granskning

Varje granskat/godkänt kort ska taggas `konfidens::N` (N = 0–10) utöver
`granskad::<datum>`, som ett mått på hur säker rättningen är:

- **10** = verifierat direkt mot ordbokskälla (svenska.se/synonymer.se/SAOB
  eller likvärdigt), inget tolkningsutrymme.
- **8–9** = ordboksbelagd betydelse, men exempelmening/synonymval eller
  tolkning av en tvetydig tagg (t.ex. fackuttryck som "(geo)") involverar
  eget omdöme.
- **≤7** = mer osäkert — källa svag/otydlig, eller betydelsen är delvis
  gissad. Ett kort på denna nivå ska helst granskas igen innan det anses
  klart, eftersom regeln nedan kräver 100% säkerhet för blå flagga.

Detta ersätter allt tidigare resonemang om procent (100/80/65%) — använd
alltid 0–10-skalan. **Oavsett konfidenssiffra gäller alltid:** flagga
aldrig ett kort blått om du inte är 100% säker på att det är rätt och
bästa varianten — konfidensvärdet är bara ett spår av HUR den säkerheten
uppnåddes, inte en ursäkt för att flagga blått vid osäkerhet.

**Flaggkoppling till konfidens (beslutat 2026-08-04):**

- **9–10 → Blå** (flag:4). Praktiskt taget samma säkerhetsnivå, ingen
  meningsfull skillnad i tillit.
- **8 och därunder → Grön** (flag:3). Betyder "stämmer innehållsmässigt,
  men inte källbelagt till punkt och pricka" — t.ex. egen formulering av
  definition, tolkning av en tvetydig tagg, eller ett löst kopplat
  synonymval. INTE samma sak som fel — bara inte 100%-nivån som krävs för
  blått.
- **OBS — konflikt med existerande grön-användning:** ~84 kort i decket
  var redan flaggade gröna innan detta projekt (se `../CLAUDE.md`,
  "utanför scope, ej nämnt av Adam"). Adam har medvetet valt att återanvända
  grönt ändå för konfidens-8-och-under, trots att det bryter
  en-flagga-en-betydelse-principen för just grönt. Blanda inte ihop: ett
  grönt kort kan antingen vara ett gammalt utanför-scope-kort ELLER ett
  konfidens-8-granskat kort från detta projekt — kolla taggen
  `konfidens::N` för att skilja dem åt.
- Kort med konfidens ≤7 ska INTE flaggas grönt eller blått — de är för
  osäkra för att räknas som klara, håll dem gula/röda tills vidare
  granskning höjer säkerheten.

## Under granskning, kontrollera även

- **Synonymer**: är de faktiskt utbytbara i de flesta sammanhang, eller bara
  besläktade? Ta bort/byt ut perifera synonymer.
- **Exempelmening**: används ordet grammatiskt korrekt och med rätt
  betydelse? Meningen ska göra betydelsen tydligare, inte bara innehålla ordet.
- **Bild**: en del kort har en bild inbäddad sist i Baksida (t.ex. en spade
  för "spade", mer abstrakta bilder för svårare ord). Bilden är ett eget
  hjälpmedel för Adam och ändras/tas ALDRIG bort vid granskning — bara texten
  runt den förenklas vid behov.

(Fyll på med fler specifika exempel/mönster här i takt med att de dyker upp
under granskningspassen.)
