# HP Verbal-coachsystem — Adam

Två separata, relaterade delsystem för HP-verbal-plugg (5-timmarspass).
Kvantitativ HP hanteras INTE här — separat spår, annan konversation.

## System A — `anki-ord/` — Anki ORD-kortsgranskning

Mål: kvalitet, inte kvantitet. Gå igenom flaggade kort i Adams riktiga
Anki-deck, förenkla till "Adam-tal", validera synonymer/exempelmeningar.
Detaljerad status + alla script beskrivna i [anki-ord/CLAUDE.md](anki-ord/CLAUDE.md) —
läs den filen för att fortsätta härifrån.

**Flaggsemantik (enda sanningskällan, viktigare än taggar):**
Blå = stämmer 100% (rör ej) · Gul = osäker (granska) · Röd = fel (granska,
högst prioritet). Granskningsordning: röd → gul → (blå, bara vid misstänkt
synonym, se nedan).

**Just nu — aktiv kö:**
`anki-ord/sessions/session_2026-08-04.json`, 106 kort: **28 godkända OCH
redan applicerade till riktiga Anki** (kört 2026-08-04), 78 väntar. Fas 2
pågår, nästa kort = "förråda sig". Adam har beslutat (2026-08-04) att kort
han redan pluggar (sedd i Anki, `-is:new`) ska granskas FÖRE aldrig visade
kort — implementerat permanent i `fetch_queue.py`. Se `anki-ord/CLAUDE.md`
för full status, inkl. en kodbugg som fixades samma dag (flagg/konfidens-
koppling i `apply_updates.py`).

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

## System B — `verbal-misstag/` — misstagsanalys ORD/LÄS/MEK/ELF

Levande minne över Adams återkommande misstagsmönster i riktiga HP-prov
(laddas ner från HP-guiden, blandar alla fyra delmoment). Se
[verbal-misstag/CLAUDE.md](verbal-misstag/CLAUDE.md) — auto-laddas när en
session körs i den mappen. Status: strukturen finns, inga prov genomgångna
än, inga mönster identifierade än.

Helt separat från System A — rör inte Anki-kortens innehåll, bara Adams
provresultat/resonemang.
