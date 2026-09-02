# HP-coachsystem — Adam

Tre separata, relaterade delsystem för HP-plugg (5-timmarspass): två verbala
(System A, B) och ett kvantitativt (System C, 2026-08-07).

## System A — `anki-ord/` — Anki ORD-kortsgranskning

Mål: kvalitet, inte kvantitet. Gå igenom flaggade kort i Adams riktiga
Anki-deck, förenkla till "Adam-tal", validera synonymer/exempelmeningar.
Detaljerad status + alla script beskrivna i [anki-ord/CLAUDE.md](anki-ord/CLAUDE.md) —
läs den filen för att fortsätta härifrån.

**Flaggsemantik (enda sanningskällan, viktigare än taggar):**
Blå = stämmer 100% (rör ej) · Gul = osäker (granska) · Röd = fel (granska,
högst prioritet). Granskningsordning: röd → gul → (blå, bara vid misstänkt
synonym, se nedan).

**Just nu — aktiv kö:** Den ursprungliga `session_2026-08-04.json`-kön (106
kort) samt hela "Lär om"/"Mogna"-genomgången (55+34+380 kort) är klara och
applicerade. Adam beslutade därefter att utöka scope till alla kort som
INTE är "Nya" (Nya-orange + Unga + Låst = 2042 kort), batchat i 6 filer:
`sessions/session_2026-08-04_resten-batch1.json` t.o.m. `...batch6.json`.
**Batch 1 och batch 2 (800 kort) är klara** (381 fixade kort totalt: 180 i
batch 1, 201 i batch 2, applicerade till riktiga Anki). Batch 1 hittade ett
helt påhittat/obefintligt ord ("gentaga") som suspenderades och väntar på
Adams beslut — batch 2 hittade inga påhittade ord. Den ordinarie batch
3-6-sekvensen (1242 kort) står fortfarande på paus.

**Urgent-pass 2026-08-04 (körd utanför batch-sekvensen):** Adam bad om att
istället prioritera kort han faktiskt läser inom en dag eller två.
`sessions/session_2026-08-04_resten-batch3-urgent.json` (300 kort: 200
redan sedda + 100 helt nya, sorterade på när de dyker upp) granskades och
**102 kort fixades och applicerades**. Detta inkluderar ett **nytt
permanent scope-beslut**: de närmast förestående nya korten (som Adam
aldrig sett än, tidigare uttryckligen utanför scope) förgranskas nu innan
han introduceras för dem, som stående policy framåt — inte bara en
engångsavvikelse. Inga påhittade ord hittades denna gång. Se
`anki-ord/CLAUDE.md` ("Urgent-pass"-avsnittet) för fullständig lista över
sakfel, en kyrillisk-bokstavsbugg som hittades, och en liten bugg i
`apply_updates.py`-flödet (kort med enbart Framsida-fix kunde hoppas över
tyst) som nu är dokumenterad och undviks.

**Sållningsfilter, Blå Nya (2026-08-05):** de ~6876 ogranskade "Blå Nya"-
korten (aldrig sedda av Adam) är nu suspenderade i riktiga Anki — bara
`kortformat::v2`-granskade kort (630 st) syns i hans nya-kort-kö. Kort
avsuspenderas automatiskt av `apply_updates.py` när de granskats färdigt.
Se "Sållningsfilter för Blå Nya" i `anki-ord/CLAUDE.md` för detaljer och
nästa steg (`fetch_bla_nya.py`).

**Backup inför powerwash (2026-08-04):** kod pushad till GitHub
(`Lekman-Learning/Swedish-Anki-Deck-Corrector`), Anki-collection synkad
till AnkiWeb. Se "Backup-status" i `anki-ord/CLAUDE.md` för återställning.

Två filer väntar fortfarande, ej påbörjade:
1. `anki-ord/sessions/session_2026-08-03.json` — 10 röda kort
   (kautschuk, eternell, driven, m.fl.), 0 godkända.
2. `anki-ord/sessions/session_2026-08-03_blaa-misstankta.json` — 59 blå kort
   där en känd felaktig synonym ("allsmäktig"/"allrådande"/"alrådande")
   hittades via riktad sökning (`scan_blue_synonyms.py`). Adam har själv
   identifierat mönstret: definitionerna på dessa ska stämma, bara
   synonymen är fel — men första exemplet i filen ("omnipotent") hade även
   en definition som ser trasig/felaktig ut ("Hovärendes, som har...").
   **Verifiera detta antagande vid granskning, lita inte blint på det.**

Nästa steg: fortsätt Fas 2 på session-04, kort för kort, applicera via
`apply_updates.py` per godkänt kort. De två 08-03-filerna väntar tills
Adam väljer att prioritera dem.

### 🔴 2026-09-02: fyra regler som blev KOD, inte prosa

Dagens genomgående lärdom, tre gånger på en dag: **en regel som bara står i
en styleguide följs inte.** Alla fyra är nu kontroller.

| Regel | Var den lever | Vad som utlöste den |
|---|---|---|
| **Varje enskilt ord ska ha minst en synonym** — exakt, `≈ närmaste ord` (kräver källa) eller `≈≈ kategori` (får tas ur kortets egen definition). Tom rad är rätt **bara** för idiom och ordled | `forgranska.HARDA` → `synonymrad_tom` | Regeln stod i `style_guide.md` sedan 29 aug och följdes inte: **56 kort** skrevs med tom rad samma dag |
| **`≈≈` undantas från källkraven** och ska inte dömas som synonym | `forgranska` 4a/4b/4c + `VERIFIERARINSTRUKTION` | Utan undantaget gav 28 korrekt ifyllda rader **30 hårda anmärkningar** — förgranskningen straffade det styleguiden föreskriver |
| **Svåra kort skjuts upp i stället för att rättas** — `v3_prio::senare` taggar **och suspenderar** | `config.PRIO_TAG_SENARE`, `v3_senare.py`, `kortbyggare --senare` | Mätt: 5+ SO-betydelser ⇒ 44 % underkända mot 8 % för 1–2. Taggen utesluts ur `hamta_pool()` — en tagg som bara syns i browsern ändrar ingenting |
| **`paket()` arkiverar befintliga domar** innan den skriver över | `kortgranskare.paket()` | 84 betalda godkännanden skrevs över och gick inte att återskapa. Kostnad: ~4 USD |

#### Två buggar i `forgranska` som fanns hela tiden

- **`betydelse_kan_saknas` räknade markörer som betydelser.** Mätt över
  samtliga 2 502 underbetydelser i `uppslag/`: `äv.` (287), `el.` (195),
  `MOTSATS:antonym` (105), `spec.` (59) — **26 % utan en stavelse innehåll**.
  Flaggan slog därför på halva materialet. Filtret behåller allt som bär
  innehåll (`äv. bildligt`, 174 st). Räknade underbetydelser: 2 502 → 1 702.
- **Screeningen mätte flerordsuttryck på fel ord.** svenska.se:s msearch har
  inga uppslagsord för fraser — den matchar de ingående orden och rapporterar
  TRÄFF. `dra på munnen` fick SO:s artiklar för *"dra till med"* och *"sele"*
  (remtyg på häst), och synonympoolen blev "ackordeon, drakskepp, handklaver".
  För enstaka ord fångas samma fel; för fraser inte.

#### 🔬 Blindgranskningen är inte repeterbar — 15 %

Samma **84 oförändrade kort** granskades två gånger. **13 (15 %) bytte dom.**
Följden styr planeringen: **"0 underkända" går inte att nå genom att
iterera** — rättar man 16 kort får man 13 nya, à ~4,5–5,3 USD per 100 kort
och omgång.

🎯 **Kör EN omgång. Lägg de underkända i `v3_prio::senare` i stället för att
rätta och granska om.** Grinden är "inga underkända som betyder något", inte
noll.

Granskaren är ändå inte brus: 81 % av rättningarna höll och ingen invändning
var sakligt felaktig — den hittade bl.a. att exempelmeningen till `algoritm`
sade *"största gemensamma talet"* där det heter **delaren**.

Full mätning: `Study Coach Ai/rapporter/2026-09-02-blindgranskningen-ar-inte-repeterbar.md`

## Mål — Hösten 2026

Satt av Adam 2026-08-07. **Kvantitativt: mål 2.0, lägsta godtagbart 1.8.**
**Verbalt: mål 1.5, lägsta godtagbart 1.3.** Detaljerat läge mot dessa mål i
respektive System B/C-fils "Mål"-avsnitt — kort sagt: kvant ligger ~0.3–0.5
under, verbalt ~0.2–0.4 under och med färre sessioner. Om något ska
prioriteras i pluggtiden pekar datan mot verbalt, LÄS-delmomentet specifikt.

**Uppdatering 2026-08-07, samma dag:** Adam beslutade att riva gränsen mot sin
Obsidian-wiki ("Study Coach AI", `c:\Obsidian\Study Coach Ai`) — den täcker nu
studier/jobb/liv i en enda domänmodell istället för att hålla HP-provet
separat. Målen, delmoment-träffsäkerheten och mönstren ovan är sedan dess
**kompilerade in i wikin** som `wiki/ämnen/hp-provet.md` plus åtta
begreppssidor (en per delmoment). **Wikin är nu den aktuella, lästa
framställningen** — den här filen och `sessions/`-mapparna i System B/C är
kvar som den detaljerade bakomliggande datan (fråga-för-fråga, provkalender)
som wikin kompilerades från, men uppdateras inte längre parallellt vid varje
nytt provpass. Nya HP-provet-genomgångar bör i första hand loggas i wikin;
uppdatera dessa filer bara om den råa fråga-nivån behövs igen.

## System B — `verbal-misstag/` — misstagsanalys ORD/LÄS/MEK/ELF

Levande minne över Adams återkommande misstagsmönster i riktiga HP-prov
(laddas ner från HP-guiden, blandar alla fyra delmoment). Se
[verbal-misstag/CLAUDE.md](verbal-misstag/CLAUDE.md) — auto-laddas när en
session körs i den mappen. Status (2026-08-07): 3 provpass genomgångna
(Hösten 2015 pp1, Våren 2015 pp3+pp5). LÄS klart svagast (40 % rätt) av alla
åtta delmoment i hela HP-underlaget. 0/3 når lägstanivån 1.3.

Helt separat från System A — rör inte Anki-kortens innehåll, bara Adams
provresultat/resonemang.

## System C — `kvantitativ-misstag/` — misstagsanalys XYZ/KVA/NOG/DTK

Samma metod som System B, tillämpad på HP:s kvantitativa del istället för
verbala. Se [kvantitativ-misstag/CLAUDE.md](kvantitativ-misstag/CLAUDE.md) —
auto-laddas när en session körs i den mappen. Status (2026-08-07): 12
provpass genomgångna (Våren 2022 Första, Hösten 2020, Hösten 2015, Våren
2015 ×4, Våren 2012). DTK och KVA svagast (~72 %), XYZ starkast (81 %). En
tidigare "gissar D"-hypotes testades mot 119 feltillfällen och avskrevs.
Bara 1/12 provpass når lägstanivån 1.8 (och det var det första, bästa).

Helt separat från System A och B — egen mapp, egen misstagshistorik, delar
bara arbetsflödet i grunden.
