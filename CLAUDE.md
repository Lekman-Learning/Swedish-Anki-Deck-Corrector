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

## System B — `verbal-misstag/` — misstagsanalys ORD/LÄS/MEK/ELF

Levande minne över Adams återkommande misstagsmönster i riktiga HP-prov
(laddas ner från HP-guiden, blandar alla fyra delmoment). Se
[verbal-misstag/CLAUDE.md](verbal-misstag/CLAUDE.md) — auto-laddas när en
session körs i den mappen. Status: strukturen finns, inga prov genomgångna
än, inga mönster identifierade än.

Helt separat från System A — rör inte Anki-kortens innehåll, bara Adams
provresultat/resonemang.
