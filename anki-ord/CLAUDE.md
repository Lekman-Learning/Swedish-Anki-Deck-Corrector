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
