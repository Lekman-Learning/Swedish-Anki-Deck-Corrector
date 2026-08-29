# Adam-tal — checklista för förenklade definitioner

Detta dokument växer i takt med granskningspassen. Målet är definitioner som
Adam förstår direkt, utan att behöva slå upp fler ord.

## Adam-tal är numera en SPÄRR, inte bara en checklista (2026-08-07)

De regler nedan som går att avgöra mekaniskt ligger i
`baksida.validate_adamtal()` och **blockerar skrivning** i båda
skrivvägarna — `apply_flerbetydelse.apply_card()`/`apply_pass()` (kastar
`ValueError`) och `apply_updates.apply_single()` (hoppar över kortet).
Ett kort som bryter mot dem går alltså inte att skriva längre.

Bakgrunden är registret: reglerna för det stod i den här filen i två
dagar och hamnade ändå fel på 37 av 50 kort, ända tills kontrollen blev
en hård spärr i skrivvägen. Adam-tal hade exakt samma lucka — prosa som
granskaren skulle minnas, plus `lint_adamtal.py` som körs i efterhand.
Ett kort som skrivs fel och upptäcks en vecka senare har Adam redan
pluggat in.

- **Hårda regler** (`baksida.ADAMTAL_HARDA`) — blockerar. Valda för att
  de mätt 0 falsklarm på hela decket: saknad highlight, tom
  exempelmening, avslutande skiljetecken i Huvudbetydelse, `;` utan
  mellanslag, HTML i Huvudbetydelse, kvarglömd HTML, tom synonym/
  synonymgrupp, synonymgrupper som inte matchar antalet betydelser,
  fler register än betydelser.
- **Mjuka regler** (`baksida.ADAMTAL_MJUKA`) — varnar, blockerar aldrig:
  flera meningar, fragment-exempel, ordbokslängd, cirkulär definition,
  cirkulär synonym, osymmetriska grupper. De har kända legitima undantag
  och att göra dem hårda hade tvingat fram sämre kort.
- **Undantag** görs med `tillat=["regelnamn"]` (eller `"tillat"` i
  sessionsfilen), inte genom att mjuka upp regeln. Då syns undantaget i
  sessionsfilen istället för att försvinna. Kanoniskt exempel: **anafor**,
  vars exempelmening MÅSTE ha flera meningar eftersom kortet illustrerar
  stilfiguren genom att upprepa satsinledningen ("Jag kommer. Jag ser.
  Jag förstår.").

**Resten av den här filen är fortfarande det som betyder mest.** Spärren
fångar bara form. Att skriva vardagligt, konkret och minnesvärt — och att
inte förklara ett svårt ord med ett annat lika svårt — kan ingen
regexkontroll avgöra. `lint_adamtal.py` är den retroaktiva vyn för kort
som skrevs innan spärren fanns; regellogiken bor i `baksida.py`, aldrig
duplicerad.

## Struktur — icke förhandlingsbart

- **Flaggan är den enda sanningskällan.** Taggar (ai_uncertain, ai_optimized,
  ai_failed, granska_först) är historik, inte fakta. Ett kort kan vara taggat
  ai_uncertain men ha blå flagga — då har Adam redan själv rättat det och det
  är korrekt. Lita alltid på flaggan, aldrig på taggen, vid konflikt.
- **HTML-strukturen i Baksida måste bevaras exakt** (Kortformat v2, beslutat
  2026-08-04, ersätter det gamla `<ol><li>`-formatet — se `config.py` för
  fullständig HTML). `baksida.py` sköter detta automatiskt — skriv aldrig
  fritext direkt i fältet.
- **Kortformat v2 (korrigerat 2026-08-04 efter Adams feedback — INGA
  fältetiketter skrivs ut, "Huvudbetydelse:"/"Synonymer:"/"Exempelmening:"
  är bara namnen på koncepten i denna guide, inte text på kortet):**
  - **Huvudbetydelse** — ENDAST detta värde är fett stilat (`<b>`), inget
    annat på kortet är det. Stor bokstav först (`baksida.build()` gör
    detta automatiskt, beslutat 2026-08-04). Så koncist som möjligt,
    vardagligt språk, ingen ordboksstil. Detta ersätter den gamla numrerade
    `<ol><li>`-definitionslistan helt.
    - **Separatorer (ändrat 2026-08-05):** ` ; ` mellan FAKTISKT SKILDA
      betydelser av ordet (t.ex. "gummi ; radergummi" för kautschuk — två
      olika saker ordet kan syfta på). ` / ` mellan olika sätt att UTTRYCKA
      SAMMA betydelse (omformuleringar/synonyma fraser, inte skilda
      betydelser). Semikolonet ska ha SAMMA färg/font som resten av
      Huvudbetydelsen (fet, ingen egen font-tagg). **Tidigare (fram till
      2026-08-04) var detta tvärtom** (`/` = skilda betydelser) — redan
      migrerade kort (793+) kan ha fel tecken enligt den gamla konventionen
      och behöver en genomgång/rättning, ren dokumentändring gör det inte
      automatiskt.
  - **(register)** — OBLIGATORISK rad direkt under Huvudbetydelse, INGEN
    egen färg — ärver temats standardtextfärg (vit i nattläge, svart i
    dagläge), bara inramat i vanliga parenteser för att synas som en egen
    liten rad (beslutat 2026-08-04, ersätter tidigare grå `#888888`-färg
    OCH tidigare "valfri, utelämna vid tveksamhet"-regel — Adam vill alltid
    ha något ifyllt, hellre en gränsfallsbedömning än en tom rad, och vill
    att den ser ut som resten av texten, inte gråtonad). Se
    "Register"-avsnittet nedan för exakt vokabulär och regler.
  - **Synonymer** — oförändrat: blå font (`#3498db`), INTE fet stil,
    valfritt antal (oftast 1–3), bara de som faktiskt är utbytbara. Noll
    är okej.
  - **Exempelmening** — oförändrat: `<i>`, INTE fet stil, målordet
    highlightat i blå font, EN mening per kort (se "Exempelmeningar —
    alltid bara en" nedan).
  - **Etymologi** — VALFRI rad efter exempelmeningen, se "Etymologi" nedan.
  - Bild sist om den finns, oförändrat.

## Etymologi (tillagd 2026-08-08, Adams begäran)

En valfri rad EFTER exempelmeningen, med samma `<br><br>`-lucka som mellan
de andra blocken, och alltid FÖRE bilden. Ren text — ingen fet stil (bara
huvudbetydelsen är fet), ingen egen färg (samma regel som registerraden).
Sätts via `baksida.build(etymologi=...)` / `apply_card(etymologi=...)`,
aldrig som fritext i fältet.

**Villkoret är inte "vet vi ursprunget?" utan "hjälper ursprunget?"**
Etymologin är en till sak att läsa på varje repetition. Den tjänar bara
in den kostnaden när den gör ordet självförklarande — när Adam efteråt
kan härleda betydelsen istället för att minnas den.

- **Ta med** när ursprunget bär betydelsen: *rangera* av ty. *rangieren*
  "ordna i rad"; *eldprov* av gudsdomen där den anklagade bar glödande
  järn; *duffel* efter staden Duffel i Belgien där tyget vävdes.
- **Utelämna** när ursprunget bara är ett faktum: att ett ord kommer från
  latin utan att latinet säger något om betydelsen, eller när kedjan är
  så lång att förklaringen behöver en egen förklaring — det bryter mot
  grundregeln om att aldrig förklara svårt med svårt.
- **Max ~18 ord** (`baksida.ETYMOLOGI_MAX_ORD`). Över det varnar
  `validate_adamtal()` med `etymologi_langd` — en MJUK regel, den
  blockerar inte, eftersom enstaka ord genuint kräver mer. Men behandla
  varningen som att den nästan alltid har rätt.
- **De flesta kort ska sakna etymologi.** Ett kort utan den är aldrig ett
  fel, och den blinda andragranskningen underkänner aldrig på den grunden
  — bara på att en befintlig etymologi är osann eller inte hjälper.
- Etymologin är en påstådd FAKTAUPPGIFT och lyder under samma källkrav
  som resten av kortet: den ska stå i den källa sökkollen loggar, inte
  komma ur minnet. Hellquists *Svensk etymologisk ordbok*
  (runeberg.org/svetym) är förstahandskällan, se "Källor för faktakoll".
- **Synonymraden finns för HP:s ORD-delprov (fastställt 2026-08-29 av Adam):**
  *"målet med synonymerna är att ha de vanligaste synonymerna inför ORD."*
  ORD ger ett ord och fem alternativ, och uppgiften är att välja det som
  *betyder samma sak eller ligger närmast i betydelse*. Fältet ska alltså
  bära **det vanligaste ordet som ligger närmast** — inte nödvändigtvis ett
  ord som är utbytbart åt båda hållen.

  🔴 **Detta upphäver den strängare regeln som gällde 27–28 augusti.** Den
  krävde utbytbarhet åt båda hållen och uteslöt allt SO JFR-markerar, vilket
  fick blindgranskningen att underkänna `bemärkt`/framstående,
  `singulär`/säregen och `spe`/hån. Alla tre står nu med tomt synonymfält.
  Mätt 2026-08-29: **911 av 4 735 v2-kort (19 %) har en tom synonymrad** —
  varje ett av dem är ett kort som inte gör det jobb fältet finns för.

  Gränsen går fortfarande vid **fel betydelse**: `tertial`/kvartal (4 månader
  mot 3) och `jour`/vikariat (två skilda anställningsformer) är riktiga fel,
  för de lär in något osant. Ett närliggande ord är inte samma sak som ett
  felaktigt ord.

- **Inget fast antal synonymer.** Målet är snabb inlärning av 10 000 ord —
  varje extra synonym är en sak till att minnas, så ta bara med det som
  faktiskt hjälper. Ett välvalt ord slår tre medelmåttiga. Fler än 3 är okej
  om de är genuint distinkta och nyttiga. Tvinga aldrig fram konstlade extra
  synonymer för att nå ett målantal — men **noll är numera ett underbetyg,
  inte ett godtagbart utfall**: saknas ett ord helt ska kortet flaggas för
  påfyllning, inte släppas som färdigt.

## Idiom och flerordsuttryck (beslutat 2026-08-24, Adams fynd)

**Adam läste `trampa vatten` och såg att kortet var fel byggt.** Så här såg det ut:

| Fält | Innehåll |
|---|---|
| huvudbetydelse | *"Hålla sig flytande i vattnet genom att röra benen… ; (bildligt) inte komma någon vart"* |
| exempelmening | *"Han trampade vatten medan han väntade på att livräddaren skulle komma."* |
| etymologi | TOMT |
| synonymer | TOMT |

**Exempelmeningen illustrerar den bokstavliga betydelsen** — alltså den enda som
HP:s ORD-del inte testar. Kortets enda exempel lär ut svarsalternativet man ska
undvika. Det är sämre än ett tunt kort; det är ett kort som tränar fel.

Mätt samma dag: **117 av 152 idiomkort (77 %) har tomt etymologifält**, mot 62 %
för enkla ord. För ett idiom kostar det mer, eftersom bilden bakom uttrycket är
själva minneskroken.

### Tre regler för flerordsuttryck

**1. Ordna huvudbetydelsen efter FAKTISK ANVÄNDNING, inte efter bokstavlighet.**
Den vanligaste betydelsen först. För idiom är det nästan alltid den bildliga —
men skriv inte "bildlig först" som mekanisk regel, för det finns uttryck som
oftast används bokstavligt. Adams formulering 2026-08-24: *"efter den mest
använda betydelsen, helst den bildliga för det brukar vara den."*

**2. Behåll den bokstavliga betydelsen, men sist och märkt.**
`trampa vatten` ÄR en verklig simteknik. Att stryka sann information ur ett
referenskort är sämre än att ordna om den, och ordningsföljden gör redan jobbet.

*Undantag:* uttryck där det bokstavliga inte längre är en levande betydelse
(`le i mjugg` — ingen "mjuggar" idag). Där hör bakgrunden bara i etymologin.

**3. Exempelmeningen ska visa den betydelse som står FÖRST.**
Alltid. Ett exempel som illustrerar en annan betydelse än kortets huvudbetydelse
är ett fel, inte en variation.

### Etymologin på idiom: skriv ut BRON

Det räcker inte att ange den bokstavliga handlingen. Det som fastnar är *varför*
bilden ger betydelsen.

| Variant | Duger? |
|---|---|
| *"Från simtekniken att trampa vatten."* | ❌ Bara ett faktum |
| *"Från simtekniken: man rör benen oavbrutet men förflyttar sig inte ur fläcken."* | ✅ Nu syns kopplingen till brist på framsteg |

### Mall

> **Framsida:** trampa vatten
> **Huvudbetydelse:** *(bildligt)* inte komma någon vart, hålla på utan att göra
> framsteg · *(bokstavligt)* hålla sig flytande på stället genom att röra benen
> **Register:** vardaglig (bildligt), sport (bokstavligt)
> **Exempelmening:** *Utredningen har trampat vatten i ett halvår utan att komma
> närmare ett svar.*
> **Etymologi:** Från simtekniken — man rör benen oavbrutet men förflyttar sig
> inte ur fläcken. Bilden är ansträngning utan förflyttning.

⚠️ **De 152 befintliga idiomkorten görs INTE om nu.** 239 av de tomma korten är
redan i Adams rotation; att bygga om inlärda kort är en förbättring, inte en
rättelse. Gäller från nästa batch, plus de osedda korten. Faller ett gammalt
idiomkort återkommande i repetitionen — rätta det då.

## Register — stängd vokabulär (Kortformat v2, beslutat 2026-08-04)

Register-raden taggar HÖGST två oberoende axlar — mer blir övertaggning:

- **Formalitet** (`config.REGISTER_FORMALITY`): `neutral` (vanlig
  standardsvenska — **det normala fallet och det vanligaste rätta svaret**:
  ordet är varken högtidligt eller vardagligt, t.ex. *marinera*, *katedral*,
  *topografi*, *taverna*) / `arkaisk` (ålderdomligt, UR
  BRUK) / `litterär` (poetiskt/bokspråk, LEVANDE men skriftligt-högtidligt —
  skiljer sig från arkaisk genom att fortfarande användas, t.ex. i
  skönlitteratur) / `formell` (byråkratiskt/officiellt) / `vardaglig` /
  `dialektal` (regional variant, t.ex. "kalvdön") / `slang` (under
  vardaglig, gatuspråk) / `vulgär` (svordomar/tabuspråk, grövre än slang).

  > **`formell` betyder byråkratiskt/officiellt — inte "ovanligt" eller
  > "fint".** Testet: skulle ordet se malplacerat ut i ett sms till en
  > kompis *därför att det hör hemma i myndighetsspråk*? Bara då är det
  > `formell`. Ett ord som bara är sällsynt (*taverna*, *divan*) är
  > `neutral`. Före 2026-08-10 saknades `neutral`, och eftersom
  > registerraden aldrig får vara tom hamnade halva decket (49,1 %) på
  > `formell` — inte av slarv, utan för att inget sant alternativ fanns.
  > Se kommentaren i `config.py`.
- **Valör** (`config.REGISTER_VALENS`): `neutral` (**ingen känsloladdning —
  skrivs UT, utelämnas inte**) / `positiv` (genuint lovordande, utöver
  neutralt — t.ex. "hedervärd") / `ömsint` (kärleksfullt: raring, älskling) /
  `skämtsam` (lekfull/rolig ton) / `ironisk` (sarkastisk, ordet
  används för att mena motsatsen — t.ex. "det var ju succé" om ett
  misslyckande) / `eufemistisk` (mildrar en hård verklighet, t.ex. "gå
  bort" för dö) / `lätt negativ` / `negativ` /
  `nedsättande` (starkare än negativ, används om PERSONER — t.ex. ett
  öknamn) / `starkt nedsättande` (SO:s egen gradering, t.ex. *pöbel*).

  > **`neutral` skrivs ut (Adams beslut 2026-08-10).** Tidigare betydde en
  > tom valör "neutral", men ett fält som *aldrig bedömts* såg då exakt
  > likadant ut som ett fält som bedömts till neutral. Samma sorts tysta
  > tvetydighet som `formell`-problemet på den andra axeln.

- **Fackområde** (`config.REGISTER_DOMAN`) — **NY axel 2026-08-10, valfri
  och oftast tom.** Guiden har sedan 2026-08-04 sagt att ämnesdomän är "EN
  EGEN, separat märkning", men den fanns aldrig i koden och användes därför
  aldrig. Blindgranskningen 2026-08-10 saknade den fyra gånger: `beskärm`
  är SO-märkt *"särsk. bibliskt"*, `gensaga` *"särsk. juridik"*, `granulera`
  har en medicinsk betydelse, `bleke` en jordbruksbetydelse — alla fyra fick
  i stället en stilnivå-tagg som inte var sann. Sätt den bara när ordet
  faktiskt hör hemma i ett fackområde.

### `oklart` — flykt-taggen (2026-08-10)

Laglig på **varje** axel när vokabulären genuint inte räcker. Men den är
aldrig tyst: `validate_register()` rapporterar den med prefixet `OKLART:`,
så den går att räkna.

**Poängen är att den är ett mätinstrument, inte en lucka.** En öppen
vokabulär glider isär över 10 000 kort (mätt — det var därför listan låstes).
En låst vokabulär som saknar rätt värde tvingar fram en lögn (mätt — det var
så 49 % blev `formell`). `oklart` är tredje vägen: sann, laglig och räknad.
Återkommer samma skäl på många kort är det **bevis** för att ett nytt värde
behövs — och då växer vokabulären på mätning i stället för på gissning.

Använd den inte av bekvämlighet. `neutral` är nästan alltid det rätta svaret
för ett vanligt ord; `oklart` är för när du genuint inte kan avgöra.

**Regler:**

- Max EN tagg per axel (`(formell, lätt negativ)` OK, `(formell, arkaisk)`
  fel — två formalitets-taggar).
- Använd EXAKT vokabulären ovan, inga synonyma varianter (`högtidlig`,
  `formal`, `bokspråk` osv.) — annars glider taggningen isär över 10 000
  kort/flera granskningspass, samma problem som tidigare setts med
  fabricerade synonymer. `baksida.validate_register()` varnar (kraschar
  inte) vid avvikelse — kör den som sanity check innan applicering.
- Registret gäller den FÖRSTA/vanligaste betydelsen i Huvudbetydelse om
  inget annat anges — lägg inte till flera register-rader för flera
  betydelser.
- **Registerraden är obligatorisk, aldrig helt tom (beslutat 2026-08-04,
  nyanserat samma dag).** Minst EN tagg krävs. Fyll BÅDA axlarna när båda
  genuint passar (t.ex. drägg: vardaglig + lätt negativ — ordet har
  faktiskt både en ton och en bibetydelse). Men tvinga ALDRIG fram en
  gissad tagg på en axel som genuint inte har någon naturlig hemvist —
  vanligast för valör på neutrala substantiv/facktermer (taverna, divan,
  apoplexi, köpeskilling, moratorium, evalvera m.fl.): dessa får bara en
  formalitets-tagg (t.ex. `formell` för köpeskilling), ingen valör, om
  ordet genuint saknar känsloladdning. Vid genuin OSÄKERHET om vilken
  tagg som passar bäst (inte "finns det ens någon"): välj den mest
  försvarbara, hellre en rimlig gissning än att hoppa över — men skilj
  det från fall där ingen tagg alls är sann.

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
- **BUGG hittad 2026-08-06 (kväll), rättad samma dag**: tre fix-script
  (`fix_blanya.py`, `fix_blanya2.py`, `fix_gamla3.py`) hardkodade
  `"bild_html": None` för varje rättat kort utan att kolla om
  originalkortet faktiskt hade en bild — raderade av misstag bilder på
  15 kort (damast, injektera, finstilt, deus ex machina, kaki, raster,
  komposition, förlägga, lake, singel, inramning, kaliber, sockel, näva,
  piccolo), återställda samma kväll. Tidigare fix-script (`fix_batch7.py`,
  `fix_gamla_pool.py`, `fix_gamla_pool_batch2.py`) gjorde rätt genom att
  läsa `bild_html` från sessionsfilens `current`-fält per kort. **Regel
  framåt: varje fix-script MÅSTE läsa `entry["current"]["bild_html"]`
  från sessionsfilen per rättat kort och skicka med det till
  `baksida.build()` — aldrig hardkoda `None`.**

## Källor för faktakoll

Föredra i denna ordning: **svenska.se** (SAOL/SO/SAOB) och **synonymer.se**
(Adams godkända källor, alltid först). Om ordet/betydelsen inte täcks där
(vanligt för ålderdomliga/dialektala ord): Hellquists **Svensk etymologisk
ordbok** (runeberg.org/svetym) och **Svenskt dialektlexikon**
(runeberg.org/dialektl) är bra sekundära källor för att hitta bortglömda/
dialektala bibetydelser — se "vråk"-fallet nedan. Annars valfri korrekt
källa.

**Extra facit (tillagt 2026-08-06): `Humanities::Languages::Svenska OLD`**
— det gamla decket (samma Anki-collection, sök
`deck:"Humanities::Languages::Svenska OLD" Framsida:<ordet>` eller
`Front:<ordet>`, modeller "Grundläggande-adc63"/"Basic"). Slå alltid upp
ordet där och jämför mot v2-kortets Huvudbetydelse INNAN du litar på
kortets nuvarande innehåll — flera riktiga fel (bl.a. "vråk", som saknade
en hel isbetydelse trots att OLD-kortet hade den) hittades bara för att
OLD-decket avslöjade en avvikelse. Stämmer OLD och v2 inte överens: räknas
INTE automatiskt som att OLD har rätt — utred vidare mot en riktig
ordbokskälla innan du ändrar något.

## GÄLLANDE REGEL: sökkoll på varje kort (beslutat 2026-08-08)

Adam: *"jag vill verkligen sökkolla för att garantera att korten med alla
verktyg vi har blir så nära rätt som möjligt. Alltså Opus 5 sökkoll v3 med
old facit och intern kunskap. På detta sättet behöver vi inte gå tillbaka
hela tiden."*

**Detta ersätter eskaleringsregeln nedan.** Allt som skrivs eller
omgranskas från och med nu får en RIKTIG uppslagning — OLD-facit och egen
språkkunskap är komplement till den, aldrig ersättning för den.

- `apply_flerbetydelse.apply_card()`/`apply_pass()` **defaultar till
  `mode="sokkoll", escalated=True`** sedan 2026-08-08. Den billiga vägen
  finns kvar men måste väljas uttryckligen. En anropare som glömmer sätta
  läget får en AssertionError om saknad källa — inte en tyst nedgradering
  till en kontroll som aldrig gjordes.
- `kalla=` är obligatoriskt och loggas per kort i `sokkoll_kallor.jsonl`.
  Taggen `flerbetydelse_sokverifierad` säger bara ATT en sökkoll gjorts;
  filen säger VAD som slogs upp och är det enda som går att granska i
  efterhand. Bakgrunden är dyrköpt: 2026-08-08 sattes taggen på 177 kort
  som bara jämförts mot OLD-decket och granskarens minne. Alla 177
  rullades tillbaka.
- **Namnet:** metoden som jämför mot OLD-facit utan uppslagning heter
  `snabbkoll2` i taggar och kod (taggnamnen ändras aldrig, Adams beslut
  2026-08-06). I löpande text heter den **v3-snabbkoll** — den är ett STEG
  i v3-kedjan, inte en egen version. Skriv inte "snabbkoll 2.0" om det
  arbete som görs i v3.
- **v3-märkning (Adams beslut 2026-08-08):** de gamla 2.0-taggarna lämnas
  exakt som de är — de är historik och beskriver den metod som faktiskt
  användes då. Allt som körs med v3-metoden framåt får dessutom
  `v3_granskad::<datum>` (`config.V3_TAG_PREFIX`). Taggen sätts i
  `_tag_and_flag()` **bara på den eskalerade vägen**, alltså bara när en
  riktig sökkoll med loggad källa faktiskt gick igenom. Ett kort som körts
  på den billiga vägen får ingen v3-tagg, hur v3-lik processen än kändes.
  `v3_granskad` ingår också i `config.SLAPP_KRAVER_TAGGAR`, så inget kort
  kan släppas in i kön utan den.

Motiveringen bakom eskaleringsregeln nedan var kostnad, och mätningarna
som stödde den står kvar för att de fortfarande är sanna om metoden. Det
Adam väger annorlunda är vad ett fel kostar: ett kort som lärs in fel
måste läras om, och den kostnaden betalas varje dag felet får stå.

Det senast mätta (2026-08-08, 30 kort snabbkollade, 16 av dem därefter
sökkollade) stöder valet: bland kort v3-snabbkollen GODKÄNDE hittade
sökkollen ett fel på 1 av 10 — och det missas TYST, ett godkänt kort ser
likadant ut oavsett om det saknar en hel betydelse. Dess egna flaggor var
däremot pålitliga, 5 av 6 rätt. Snabbkollen duger alltså till att styra
uppmärksamhet, inte till att garantera ett kort.

## Flerbetydelse-genomgång (beslutat 2026-08-05, efter "konglomerat"-fallet)

Alla redan granskade kort (3152 st, `granskad::*`) körs igenom en extra
kontroll: saknas en vanlig andra betydelse (se "Dold andra betydelse" ovan)?
`scan_multiple_meanings.py` hittade 994 kandidater (Huvudbetydelse utan ` ; `
men ≥3 synonymer) — körs i omgångar om 333 kort.

- **Ny tagg**: `flerbetydelse_granskad::<datum>` — sätts UTÖVER
  `granskad::<datum>` (uppdateras till dagens datum om kortet ändras) på
  varje kort som gått igenom denna specifika kontroll, oavsett om något
  ändrades. Skiljer "genomgången för denna kontroll" från vanlig
  `granskad::*`, eftersom kortet kan ha granskats en gång innan kontrollen
  fanns. Sätts via `entry["extra_tags"]` i sessionsfilen, plockas upp av
  `apply_updates.py` automatiskt.
- **Snabbkoll 2.0 + villkorlig sökkoll-eskalering (ändrat 2026-08-06,
  ersätter "sökkoll obligatoriskt för allt"-regeln från tidigare samma
  dag).** Bakgrund: ett A/B-test visade att den GAMLA, rent minnesbaserade
  snabbkollen inte höll måttet — 160 "snabbkollade och godkända" kort
  sökkollades i efterhand och 14 av dem (8,75%) hade ändå ett fel
  snabbkollen missat, statistiskt oskiljbart från 60 helt okollade kort
  (4 fel, 6,7%). Det ledde till en tillfällig regel om obligatorisk
  sökkoll på ALLA kort. Den regeln var korrekt givet den gamla snabbkollen,
  men onödigt dyr (websökning för varje enda kort) givet vad som visade
  sig fungera bättre samma dag:

  **Snabbkoll 2.0** jämför kortet mot `Humanities::Languages::Svenska
  OLD`-decket (se "Källor för faktakoll" ovan) — INTE bara minnet, en
  riktig fristående källa, men ett gratis lokalt AnkiConnect-uppslag
  istället för dyr websökning. Verktyg: `snabbkoll2.py` bygger kön och
  hämtar OLD-matchningen automatiskt; granskaren (Claude) jämför sedan
  v2-kortets Huvudbetydelse/synonymer/exempelmening/register mot
  OLD-kortet OCH egen språkkunskap, exakt som vid sökkoll. **Validerat
  2026-08-06 på 100 kort** (fem omgångar, 30+20+20+15+15): snabbkoll 2.0
  hittade 6 fel själv (3 sakfel: ingäld, i långa banor, konvent; 3
  formateringsfel av samma sort — "eller" felaktigt använt för två
  GENUINT distinkta betydelser istället för " ; ": vandal, atmosfär,
  parhäst) — den efterföljande sökkollen av SAMMA 100 kort hittade 0
  ytterligare fel. Till skillnad från gamla snabbkollen missade den
  alltså ingenting sökkoll skulle ha hittat, på det stickprov som
  testats hittills.

  **Andra valideringsrundan, 100 NYA kort (2026-08-06, kväll):** samma
  metod, men denna gång fick ALLA 100 kort en riktig, individuell sökkoll
  (inte bara de snabbkoll 2.0 flaggade), för att testa om 0-missfrekvensen
  håller på ett dubbelt så stort stickprov. Snabbkoll 2.0 flaggade 10 kort
  (10%, högre andel än förra rundans 6%) — sökkollen av samtliga 100
  bekräftade exakt dessa 10 och hittade 0 nya bland de återstående 90.
  **Nytt dominant felmönster upptäckt denna runda:** en hel ordboksbetydelse
  helt frånvarande i Huvudbetydelsen (7 av 10 fel: mönstra, page, inbunden,
  visir, bulvan, parabel, ockult) — ofta trots att `synonym_groups` redan
  hade en egen grupp för den saknade betydelsen, en varningssignal värd
  att aktivt leta efter. Allvarligaste enskilda fyndet: **holma**, där
  kortet påstod fel ORDKLASS OCH betydelse helt (sa "liten ö" när ordet
  faktiskt är ett jaktdialektalt verb för att spåra villebråd) — hittades
  bara tack vare OLD-jämförelsen, inte av vanlig läsning.

  **Statistisk brasklapp — läs innan du litar blint på "0 missade fel":**
  över båda rundorna, 200 kort testade totalt, 16 faktiska fel hittade av
  snabbkoll 2.0 själv, 0 missade av den efterföljande fulla sökkollen.
  Rule-of-three PÅ KORTNIVÅ (0 missar av 200 individuellt sökkollade kort,
  inte 0 av 16 fel) ger en övre 95%-gräns på ungefär 3/200 ≈ 1,5% för den
  sanna missfrekvensen — snävare än efter första rundan, men fortfarande
  INTE bevisat noll. Testet är heller inte blint som det ursprungliga
  A/B-testet (samma granskare gjorde snabbkoll 2.0 och sökkoll på samma
  kort i samma sittning — viss risk för bekräftelsebias). Gör periodiska
  BLINDA stickprov senare (kort granskade dagar/veckor tidigare,
  omgranskade fristående) för att verkligen validera detta över tid.

  **Regel framåt:** kör snabbkoll 2.0 som förstahandskontroll på alla
  v2-kort (nya eller omgranskade). **Eskalera till riktig sökkoll
  (websökning) ENDAST när** (a) OLD-decket och v2-kortet inte stämmer
  överens, (b) ordet saknar OLD-matchning helt, eller (c) granskaren
  själv känner sig osäker trots att OLD och v2 stämmer överens — se
  "ingäld" (OLD sa "inkomster", kortet sa raka motsatsen "penningskuld")
  och "konvent" (kortet saknade en hel betydelse OLD inte ens visade
  tydligt, upptäckt via egen kunskap) som exempel på när eskalering
  behövdes. Kort som klarar snabbkoll 2.0 utan eskalering behöver INTE
  sökkollas ytterligare — det är hela poängen med hybriden.

  **Taggning (håll denna konsekvent, inga nya taggnamn):**
  - `flerbetydelse_granskad::<datum>` — sätts på ALLA kort som gått
    igenom snabbkoll 2.0, oavsett resultat.
  - `flerbetydelse_snabbkoll2::<datum>` — sätts på ALLA kort som
    genomgått OLD-jämförelsen (den nya, källbaserade snabbkollen —
    förväxla inte med gamla `flerbetydelse_snabbkoll::<datum>`, som
    förblir en historisk/legacy-tagg för det äldre minnesbaserade läget).
  - `flerbetydelse_sokverifierad::<datum>` — sätts ENDAST på kort som
    eskalerats till och bekräftats/rättats via riktig sökkoll. Ett kort
    kan alltså ha `flerbetydelse_snabbkoll2` UTAN `flerbetydelse_
    sokverifierad` (klarade OLD-jämförelsen utan eskalering) — det är
    förväntat och räknas som fullgott granskat.

  Konfidens 10 (se "Konfidensmärkning" nedan) kräver fortfarande en
  faktisk källkoll — OLD-decket räknas som en sådan källa, ren
  minneskänsla gör det fortfarande inte.

  **Tredje rundan, 150 kort, metoden körd SOM AVSETT (2026-08-06, kväll):**
  till skillnad från de två valideringsrundorna ovan (som medvetet
  sökkollade ALLA kort) kördes denna gång bara sökkoll på de kort
  snabbkoll 2.0 själv flaggade — den faktiska produktionsprocessen.
  9 av 150 (6%) eskalerades. 6 var genuina fel (plakat, kreditera,
  nickedocka, association, flottilj, spjälka — femte omgången i rad där
  "saknad hel betydelse" är den vanligaste felkällan; spjälka hittades
  för att exempelmeningen motsade den egna Huvudbetydelsen). 2 visade sig
  redan vara korrekta (spetsfundig, "nu går skam på torra land") — i
  spetsfundigs fall var det OLD-facitet som var missvisande, inte kortet,
  vilket visar att eskaleringslogiken fångar avvikelser åt båda hållen
  utan att anta att OLD alltid har rätt. Ingen sökkoll gjordes på de 141
  icke-eskalerade korten. Se `anki-ord/CLAUDE.md` för fullständig lista.

  **Fjärde omgången, den GAMLA snabbkoll-poolen (2026-08-06, kväll):**
  1558 kort granskade med den gamla minnesbaserade snabbkollen (innan
  snabbkoll 2.0 fanns) hade aldrig fått en OLD-jämförelse eller sökkoll.
  Nytt script `snabbkoll2_gamla.py` riktar snabbkoll 2.0 mot just denna
  pool. Första 400-korts omgången: 20 eskalerade (5%, lägre än tidigare
  rundors 6-10%, rimligt eftersom poolen redan sett en svagare mänsklig
  granskning). 15 bekräftade fel rättade — "saknad hel betydelse" är nu
  bekräftat i SEX rundor i rad som det dominerande felmönstret (13 av 15
  denna gång, bl.a. spak som saknade en HEL ordklass/betydelse:
  adjektivet "tam, foglig" fanns inte alls, bara substantivet "handtag").
  5 eskalerade visade sig redan korrekta (dentist, lämpa, skäktning, bulk,
  diskonto) — ytterligare bevis på att eskaleringslogiken fångar fel åt
  båda hållen.

  **Femte omgången, samma pool (2026-08-06, kväll):** ännu 400 kort. 22
  eskalerade (5,5%). 19 bekräftade fel rättade — "saknad hel betydelse"
  dominerar för SJUNDE omgången i rad (17 av 19), flera med en HEL
  ordklass saknad (vän saknade adjektivbetydelsen "skön, fager"; maka
  saknade verbbetydelsen "flytta något lite grann") eller en betydelse
  som sannolikt är VANLIGARE än den som redan fanns på kortet (motion
  saknade "fysisk aktivitet" och hade bara riksdagstermen; nätt saknade
  "liten och täck, söt" och hade bara "knappt tillräcklig"; stadga
  saknade "stadgar" = föreningsföreskrifter). Ett kort ("gå med håven")
  hade helt fel betydelse och korrigerades i grunden — uttrycket betyder
  specifikt "tigga komplimanger", inte generellt "tigga om pengar". 3
  eskalerade bekräftat korrekta, bl.a. skygga där OLD-facitet visade sig
  vara en sammanblandning med det snarlika ordet "skugga". ~758 kort kvar
  i poolen.

  **Sjätte omgången, ny pool — Blå Nya, aldrig sedda kort (2026-08-06,
  kväll):** skild pool från gamla-poolen ovan: blå (flag:4), v2-
  formaterade kort som fortfarande är `is:new` (Adam har aldrig sett dem
  i Anki) och saknar ALL flerbetydelse-koll, 311 kort totalt. Nytt script
  `snabbkoll2_blanya.py`. Första halvan körd, 155 kort. OLD-täckning
  155/155 (100%). 12 eskalerade (7,7%, högre än gamla-poolens 5-5,5% —
  rimligt eftersom denna pool aldrig fått NÅGON tidigare kontroll, till
  skillnad från gamla-poolen som redan haft en minnesbaserad koll). Alla
  12 bekräftade fel/ofullständiga och rättade — "saknad hel betydelse"
  dominerar för ÅTTONDE omgången i rad, flera med ett helt annat
  fackområde eller helt annan ordklass saknad: koloni (saknade både den
  biologiska betydelsen och "barnkoloni"), lumpen (saknade den mycket
  vanliga vardagliga SUBSTANTIVbetydelsen "militärutbildning" — helt
  annan ordklass än adjektivet "elak"), depression (saknade både den
  ekonomiska och meteorologiska betydelsen), oratorium (saknade "litet
  bönerum" inom katolska kyrkan), patriark (saknade den kyrkliga
  hederstiteln), besätta (saknade "garnera/pryda"), semiologi (saknade
  den medicinska "symtomlära"), benägen (saknade "välvillig"-nyansen).
  Två kort korrigerades i grunden snarare än utökades: ocker hade en
  verb-formad Huvudbetydelse trots att ordet är ett substantiv; formalitet
  definierades för brett och matchade inte ens sin egen exempelmening.
  damast saknade det utmärkande draget "vanligen enfärgat". 156 kort kvar
  i Blå Nya-poolen (andra halvan).

  **Andra halvan, 156 kort — hela Blå Nya-poolen (311 kort) nu KLAR
  (2026-08-06, kväll):** 12 av 156 (7,7%, identiskt med första halvans
  andel) eskalerade, alla bekräftade och rättade. Samma mönster: hiva
  (saknade "kasta/slänga"), förmäla (saknade ålderdomliga "gifta bort"),
  injektera (saknade bygg-/bergtekniska "täta/förstärka"), bräcka
  (saknade HELA två betydelser: "steka lätt" och "gry" — fyra betydelser
  i OLD mot två på kortet), stifta (saknade "stifta lagar"), finstilt
  (saknade bildliga "finstämd, raffinerad"), pellets (saknade
  foderbetydelsen), kaki (saknade frukten), botanisera (saknade bildliga
  "utforska bland"), forcera (saknade tekniska "knäcka en kod").
  formidabel och betuttad fick en ovanlig men sökkoll-bekräftad
  ålderdomlig/dialektal bibetydelse tillagd. Utöver detta: 4 rena
  format-/grammatikfel hittade och fixade utan sökkoll (saknad highlight,
  missvisande synonym, dubbelt hjälpverb, fel V2-ordföljd) — se
  `anki-ord/CLAUDE.md` för alla detaljer. Totalt över hela poolen: 24
  sökkoll-bekräftade fel/ofullständigheter (7,7%) + 4 extra formatfixar,
  av 311 kort.

  **Sjunde omgången, tillbaka till gamla-poolen: 350 kort (2026-08-06,
  kväll):** 24 av 350 (6,9%) eskalerade, alla bekräftade och rättade.
  Ovanligt många rena HOMONYMER denna omgång (helt orelaterade
  betydelser, inte bara nyanser): lake (fisken saknades, bara saltlagen
  fanns), singel (grus saknades), näva (den vanliga betydelsen "knuten
  hand" saknades helt — kortet hade bara den sällsynta växten Geranium,
  ordningen byttes så handbetydelsen kommer först), kurra (verb-
  betydelsen "bullra om magen" saknades), piccolo (både flöjten och
  champagneflaskan saknades). Flera bildliga/idiomatiska betydelser
  saknades också: raster (den vanliga "rast, arbetspaus" saknades helt),
  dager ("i en ny dager" = perspektiv), kaliber ("en man av hans
  kaliber" = kvalitet), episk (modern slangbetydelse "grym"),
  inramning ("politisk inramning" = sammanhang, dessutom omskriven från
  verb- till substantivform). Se `anki-ord/CLAUDE.md` för fullständig
  lista (18 kort till). Ett rent synonymfel utan sökkoll-behov: jour
  hade den missvisande synonymen "vikariat" (förväxlar två olika
  anställningsbegrepp). Flaggning: 24 Blå, 326 Gröna. 408 kort kvar i
  gamla-poolen.

  **Nytt flagg-system för flerbetydelse-genomgången (beslutat 2026-08-06,
  kväll, ersätter konfidensbaserad flaggning för DENNA kontroll):**
  istället för att flagga efter en numerisk konfidenssiffra (se
  "Konfidensmärkning" nedan, som fortfarande gäller för Fas 2/den
  ursprungliga sakfels-granskningen) flaggas kort nu efter
  VERIFIERINGSDJUP i flerbetydelse-kontrollen:
  - Eskalerad till och bekräftad/rättad via riktig sökkoll → **flag:4 Blå**
    (`config.FLAG_BLA`).
  - Klarat snabbkoll 2.0 UTAN eskalering, med en OLD-decket-matchning
    → **flag:3 Grön** (`config.FLAG_GRON`).
  - Specialfall: klarat snabbkoll 2.0 UTAN eskalering och UTAN
    OLD-matchning (bara egen kunskap, inget facit alls) → **flag:2
    Orange/Gul** (`config.FLAG_GUL`). Krockar medvetet inte med
    flag:2:s ANDRA betydelse ("osäker, granska" från den ursprungliga
    Fas 2) — Adam bekräftade 2026-08-06 att de gamla orange-korten är
    suspenderade och snabbkollas innan de avsuspenderas, så de två
    betydelserna möts aldrig i praktiken.

  Satt via `setSpecificValueOfCard` (samma AnkiConnect-anrop som
  `apply_updates.py` redan använder för den gamla konfidensflaggningen).
  **Applicerat överallt 2026-08-06:** Blå Nya-omgången (155 kort: 12 Blå,
  143 Gröna, 0 Orange — 100% OLD-täckning) OCH retroaktivt på de tre
  tidigare klara omgångarna (950 kort: 150-korts produktionsomgången +
  800 kort i gamla-poolen) — 50 Blå (sökkollade), 900 Gröna (OLD-matchade,
  ingen eskalering), 0 Orange (samtliga 950 hade OLD-matchning).
- **Symmetriska synonymgrupper**: om ett kort får en andra betydelse
  tillagd, sikta på samma ANTAL synonymer per betydelse — `1 ; 1` eller
  `2 ; 2`, inte `1 ; 3`. Håller korten balanserade/lika snabba att läsa
  oavsett hur många betydelser de har. Inte en hård regel om en betydelse
  genuint saknar en andra utbytbar synonym (hellre `1 ; 1` än en påtvingad
  extra) — men sikta symmetriskt som standard.
- **Register per bibetydelse (ändrat 2026-08-05 v2, ersätter både
  inline-i-fetstil-varianten och den kortlivade två-radersvarianten):**
  registerraden under Huvudbetydelse gäller fortfarande FÖRSTA/vanligaste
  betydelsen (oförändrad regel). Om en TILLAGD andra (eller tredje)
  betydelse har ett ANNAT register än den första: skriv BÅDA registren på
  SAMMA rad, andra registret indraget med `&nbsp;` till ungefär under sin
  betydelses startpunkt i Huvudbetydelse-raden ovanför — inte en ny rad:
  ```
  <b>En våg eller krökning i hår eller ull ; att fjäska och smickra någon underdånigt</b><br>
  (dialektal)                              (vardaglig, negativ)<br>
  <br>
  ...
  ```
  `baksida.build(register=...)` tar en ` ; `-separerad sträng, en del per
  betydelse (`"dialektal ; vardaglig, negativ"`), och räknar ut
  indentering automatiskt (tecken-baserad approximation utifrån
  huvudbetydelsens textlängd — fetstil är inte monospace, blir aldrig
  pixelperfekt, men tillräckligt för att visuellt koppla rätt register
  till rätt betydelse). Om bibetydelsen delar samma register som den
  första: ingen extra registerdel behövs, bara huvudregisterraden gäller
  (se ackreditera: båda betydelserna var `formell`, ingen extra del
  lades till).

## Synonymer kopplade till olika betydelser

Om ett ord har flera betydelser i Huvudbetydelse (separerade med ` ; `) och
synonymerna hör till olika betydelser: gruppera synonymerna i samma
ordning som betydelserna, separera grupperna med mellanslag-semikolon-
mellanslag ` ; ` — inte bara `,`. Semikolonet ska ha SAMMA färg/font som
synonymerna (`#3498db`), inte vanlig text. Exempel (kautschuk, Huvudbetydelse
`naturgummi ; (äldre) radergummi`): `gummi, naturgummi ; radergummi` —
gummi/naturgummi hör till första betydelsen (råämnet), radergummi till
andra (den äldre betydelsen).

- **Undvik cirkulära synonymer (bugg hittad av Adam 2026-08-06, kväll,
  rättad samma kväll):** en synonym som bara är huvudordet plus ett
  prefix/suffix (t.ex. "piccolaflöjt" som synonym för "piccolo",
  "berginjektera" för "injektera", "foderpellets" för "pellets",
  "brottssyndikat" för "syndikat", "tjänstehjon"/"fattighjon" för
  "hjon", "barnkoloni" för "koloni", "lagstifta" för "stifta")
  avslöjar svaret direkt istället för att vara en oberoende ledtråd —
  9 kort hade detta fel efter dagens flerbetydelse-fixar, rättade
  samma kväll. Kolla alltid: innehåller den föreslagna synonymen
  huvudordet (eller en tydlig böjning av det) som substräng? Om ja,
  hitta ett genuint annat ord istället, eller — om inget bra alternativ
  finns — lämna den bibetydelsens synonymgrupp med ETT befintligt ord
  snarare än att tvinga fram ett cirkulärt tillägg (en TOM synonymgrupp
  ger ett formateringsartefakt, `; ` utan text efter — testat och
  bekräftat i `baksida.build()`, så gruppen ska aldrig vara helt tom).
  **Uppföljning samma kväll (efter Adams fråga "behöver jag oroa mig
  över de andra korten?"):** en fullständig, automatiserad genomgång av
  ALLA 93 kort som fixats under dagens sex snabbkoll 2.0-omgångar (inte
  bara de sex senaste) — kollar både bild_html-bevarande och
  substräng-match mellan huvudord och synonym — hittade 4 till: **mas**
  (dalmas, skattmas — båda innehöll "mas"), **rya** (ryamatta → bytt mot
  flossmatta), **konsol** (spelkonsol), **kurator** (curator — den
  engelska kognaten är i praktiken samma ord, avslöjar svaret lika
  mycket som en bokstavlig substräng). Alla rättade. Efter denna
  genomgång: 0 bildproblem, 0 kvarvarande cirkulära synonymer (fyra
  återstående substräng-träffar är false positives — kolonialområde,
  skogsnäva och instifta är genuint fristående etablerade ord som
  fanns på korten INNAN dagens fixar, "sig" i "slå sig ner" är bara
  ett kort, grammatiskt nödvändigt pronomen).

  **Full historisk revision, alla 2601 flerbetydelse_granskad-kort
  (2026-08-06, sent på kvällen, efter Adams fråga "hur långt behöver du
  kolla"):** automatiserad substräng-kontroll körd mot ALLA kort som
  någonsin gått igenom flerbetydelse-processen (inte bara dagens 2537 —
  även 64 kort från 2026-08-05, innan snabbkoll 2.0 fanns). 122 råa
  träffar. De allra flesta var false positives (korta grammatiska ord
  som "sig"/"till"/"för" i flerordsuttryck, eller legitima
  specificitets-tillägg som "kreatur"→"nötkreatur", "vråk"→"musvråk" —
  äkta artnamn/specificering, inte cirkulära). **8 äkta svaga/cirkulära
  synonymer hittade och rättade** (alla i vanliga synonymlistor, inte
  synonym_groups — så bara EN svag synonym bland flera bra togs bort,
  inget ersattes): slapstick (slapstick-humor borttagen), albino
  (albinos borttagen — dessutom hittades "färgblindhet" vara sakligt
  FEL, inte bara cirkulärt: albinism handlar om pigmentbrist, inte
  färgblindhet, borttagen), ehuru (ehuruväl), frilans (frilansare),
  furu (furuträ), väld (välde — nästan identisk stavning), onkologi
  (onkologisk medicin), oför (oförmögen — bara en upprepning av ordets
  egen huvudbetydelse). Resterande ~30 gränsfall (t.ex.
  reservat→naturreservat, krypto→kryptovaluta, borst→borsthår) bedömdes
  tillföra genuin specificering snarare än att avslöja svaret rakt av —
  lämnade orörda, men flagga gärna om något av dem känns fel vid
  granskning.

### `≈` binder till ETT ord, och det ordet star forst (2026-08-29)

Adams fraga: *"vid ljuster ar = tecknet for bade treudd, harpun eller bara
treudd?"* Notationen svarade olika beroende pa vem som last den:

```
Sa renderades raden :  ≈ treudd, harpun
Sa tolkade koden    :  ['≈ treudd', 'harpun']
```

Koden binder `≈` till nasta ord; ogat laser det som att det galler hela
raden. **Regeln ar darfor: ett ord efter `≈`.** Ar narmaste ord anda
ungefarligt tillfor ett andra ungefarligt ord brus, inte precision -- och
det ar just det andra ordet som gor raden dubbeltydig.

Undantaget ar per BETYDELSE, inte per kort. `cyklop` far behalla
`≈ jätte ; undervattensmask`: en enogd jatte ar bara ungefar en "jatte",
men en cyklop AR en dykarmask. Dar ar den forsta betydelsen ungefarlig och
den andra exakt, och ` ; ` haller isar dem.

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

- **10** = FAKTISKT verifierat mot en riktig ordbokskälla (svenska.se/
  synonymer.se/SAOB/Hellquist eller likvärdigt) i just DENNA granskning —
  inget tolkningsutrymme. **En säker känsla från minnet räcker ALDRIG för
  10, oavsett hur strukturerad bedömningen var** (se A/B-testet
  2026-08-06 under "Flerbetydelse-genomgång" — minnesbaserade "konfidens
  10"-bedömningar hade 8,75% dold felfrekvens). Om ingen källa faktiskt
  slogs upp: max 9, oavsett hur säker granskningen kändes.
- **8–9** = ordboksbelagd betydelse, men exempelmening/synonymval eller
  tolkning av en tvetydig tagg (t.ex. fackuttryck som "(geo)") involverar
  eget omdöme — ELLER en minnesbaserad bedömning utan faktisk källkoll.
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

**Obligatorisk 6-punktschecklista (utökad 2026-08-19, punkt 6 tillagd efter
Adams kritik samma dag — se nedan för bakgrund):** kontrollera ALLTID alla
sex mot en riktig källa (se "Källor för faktakoll"), inte bara punkt 1:

1. **Är Huvudbetydelsen korrekt och tydlig?** Inte bara "har ordet fler
   betydelser" — är själva formuleringen rätt (se "subversiv"-fallet:
   definitionen beskrev "verksamhet" istället för att definiera
   adjektivet självt).
2. **Passar synonymerna verkligen den angivna betydelsen?** (se "hunsa":
   "misshandla" antydde fysiskt våld, ordet handlar om nedlåtande
   behandling; "lira": "kasta" hörde inte ihop alls).
3. **Illustrerar Exempelmeningen tydligt och korrekt just den betydelsen?**
   Kolla även sakfel i själva exemplet, inte bara språket (se
   "patetisk": exemplet blandade ihop Beethoven med Tjajkovskij).
4. **Saknas en betydelse helt?** (den ursprungliga "dold andra
   betydelse"-kontrollen, se nedan — men kolla ALLTID mot en källa, inte
   bara om synonymerna råkar avslöja det).
5. **Stämmer register OCH valör?** Båda axlarna, inte bara att en tagg
   är satt.
6. **Låter Huvudbetydelsen som du pratar med en kompis, eller som en
   uppslagsbok? (tillagd 2026-08-19)** Läs den högt. Grundreglerna ovan sa
   redan "undvik akademiska/latinska synonymer" och "förklara inte svårt
   med svårt" — men ingen punkt i checklistan tvingade fram frågan
   mekaniskt, och den mjuka regeln höll inte i praktiken. Adam hittade
   konkreta exempel som gick igenom godkänd granskning ändå: **småskrake**
   ("En liten, smal sjöfågel av **andsläktet**, med krokig, tunn näbb" —
   taxonomisk ordbokstermin, ingen säger "andsläktet" i vardagsspråk) och
   **häva** ("**Upphäva giltigheten av** något, t.ex. ett avtal" —
   byråkratspråk som förklarar ett byråkratord med samma register, precis
   det grundreglerna varnar för). Varningstecken att aktivt leta efter:
   fackordsuffix (`-släktet`, `-ordningen`, `-familjen`), tunga
   nominaliseringar (`upphävande av`, `genomförande av` i stället för ett
   vanligt verb), och passiv byråkratform. Hittar du något av detta i
   Huvudbetydelsen: skriv om innan kortet godkänns, även om innehållet
   sakligt sett stämmer — den här punkten underkänner FORM, inte fakta.

- **Dold andra betydelse (VÄSENTLIGT, beslutat 2026-08-05):** om synonymerna
  inte alla hör till SAMMA betydelse som Huvudbetydelsen beskriver — det är
  ett tecken på att ordet har en till betydelse som saknas på kortet.
  Exempel: "konglomerat" hade bara företagsbetydelsen i Huvudbetydelse
  ("koncern...") men synonymerna ("hopgyttring, sammangyttring, massa") hör
  till den ANDRA, allmänna betydelsen (brokig hopgyttring av olika saker) —
  den betydelsen saknades helt. Ett kort med flera betydelser MÅSTE visa
  ALLA relevanta betydelser, annars är kortet ofullständigt/missvisande.
  Fix: dela upp Huvudbetydelse med ` ; ` per betydelse, gruppera
  synonymerna i samma ordning med `synonym_groups` (samma ` ; `-separator).
  Kolla detta på VARJE kort, inte bara vid uppenbar `/`- eller `;`-notation
  redan i utkastet.
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

## GÄLLANDE REGEL: v3 är enda metoden (beslutat 2026-08-08)

Alla kort — nya som befintliga — byggs och granskas med full v3: sökkoll,
OLD-facit, intern kunskap, blindgranskning. Inga andra vägar används.
Målvolym 125 kort/dag (minimum för att kön inte ska ta slut), 300/dag när
de befintliga korten rättas parallellt. Skär i takten, aldrig i djupet.
