# anki-ord — System A status (Anki ORD-kortsgranskning)

Se [../CLAUDE.md](../CLAUDE.md) för helheten. Denna fil = teknisk detalj +
exakt var vi står, så en ny chatt kan fortsätta direkt.

## Bekräftat mot riktig, öppen Anki (Fas 0, `discover.py`, klart 2026-08-03)

- Deck: `Humanities::Languages::Svenska 10 000`
- Note type: `Grundläggande-adc63`
- Fält: `Framsida` (ordet), `Baksida` (EN HTML-blob, se `baksida.py`)
- Flaggor: flag:1 = **Röd** (849 kort, fel) · flag:2 = **Gul** (1328, osäker)
  · flag:4 = **Blå** (7772, stämmer) · flag:3 = 84 kort, utanför scope, ej
  nämnt av Adam, rör inte
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
| `apply_updates.py` | Fas 3 — skriver godkända ändringar (`updateNoteFields` via `baksida.build`), flyttar flagga till blå, taggar `granskad::<datum>`. `apply_single` per kort under passet, eller batchat i `main()` |
| `style_guide.md` | "Adam-tal"-checklista — struktur, grundregler, bevara humor, bildhantering, vanliga fällor |

## Öppna sessionsfiler

**`sessions/session_2026-08-04.json`** — AKTIV KÖ, 106 kort totalt:
- 21 `"approved": true` (redan granskade/godkända, orörda, ligger överst)
- 85 `"approved": false, "proposed": null` (väntar på Fas 2)

De 85 väntande är i denna ordning:
1. **6 prioriterade** — röda kort Adam redan pluggar (`-is:new`), hittade
   2026-08-04 via live AnkiConnect-sökning och manuellt inklistrade allra
   först i kön, eftersom Adam vill rätta det han redan lär sig innan nytt
   material (se regel nedan). Ordning: "spel för galleriet", "bolare",
   "påbel", "vara i svang", "kanalje", "bottna i".
2. **79 övriga** — samtliga är `is:new` (aldrig visade i Anki), ursprungligt
   `fetch_queue.py`-resultat. Första i denna grupp: **"vina"** — OBS,
   innehållet är trasigt (beskriver vinbär, inte ordets faktiska betydelse;
   platshållar-exempelmening), måste researchas från grunden mot
   svenska.se/synonymer.se innan godkännande.

**Prioriteringsregel (beslutad 2026-08-04):** Adam vill granska kort han
redan håller på att lära sig FÖRE kort han aldrig sett, så han inte lär in
fel version av ett ord han redan pluggar. `fetch_queue.py`/`queue_lib.py`
(`fetch_cards_prioritized`) implementerar detta permanent för alla framtida
körningar — se script-tabellen ovan. Denna omgörning av session-04 var en
engångs-retroaktiv fix eftersom filen redan fanns när regeln beslutades.

**`sessions/session_2026-08-03.json`** — 10 röda kort, HELT ogranskad
(oberörd av 08-04-arbetet). Ord: kautschuk, eternell, driven, + 7 till.

**`sessions/session_2026-08-03_blaa-misstankta.json`** — 59 blå kort från
`scan_blue_synonyms.py`/`fetch_blue_suspects.py`, alla ogranskade. Exempel:
"omnipotent" har synonymen "evighetsmaktig" (misstänkt fel) OCH en
definition som ser trasig ut ("Hovärendes, som har full makt...") — trots
att `fetch_blue_suspects.py`s docstring antar att definitionen alltid
stämmer på blå kort. Kontrollera det antagandet under granskningen, inte
bara synonymen.

## Nästa steg

Fortsätt Fas 2 i `session_2026-08-04.json`, börja med **"spel för
galleriet"** (första prioriterade kortet). Kör kort för kort genom de 6
prioriterade, sen "vina" (kräver research från grunden) och resten av de
79. Applicera godkända kort via `apply_updates.py`.

De två 08-03-filerna (10 röda + 59 blå-misstänkta) väntar fortfarande,
Adam har inte valt att prioritera dem än.

## Style guide — kärnpunkter (full version i `style_guide.md`)

- Målstruktur 3 synonymer / 2 definitioner, avvikelse OK om ordet motiverar det
- Korta meningar, vardagliga ord, konkret före abstrakt
- Bevara humor i befintliga exempelmeningar — förenkla språk, inte tonen
- Bilder är personliga minnesknep — kritisera/föreslå fritt, ändra ALDRIG
  utan Adams uttryckliga godkännande (kostar credits per generering)
