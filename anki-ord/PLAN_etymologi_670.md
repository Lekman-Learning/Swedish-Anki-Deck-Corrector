# Plan: fyll i 811 saknade etymologier — 670 blint, 141 för hand

**Skriven 2026-09-04.** Kan köras kallt av en ny session utan förkunskap.

---

## Varför

Revision av alla **2 393** kort med `tag:oberoende_verifierad`:

| | Antal | Andel |
|---|---|---|
| Saknar etymologi på kortet | **1 227** | 51,3 % |
| → källan saknade den (inte vårt fel) | 410 | |
| → ingen uppslagning på disk | 6 | |
| 🔴 **→ källan HADE den, den skrevs aldrig in** | **811** | **33,9 %** |

En tredjedel av decket missar något som redan låg gratis i `uppslag/`.

**Detta är inte en omskrivning.** Etymologin kopieras ordagrant ur SO via
`_hjalp_0902b.etym()`, som hämtar `sammandrag.svenska_se.so.etymologi[0]`.
Ingen formulering, ingen bedömning, inget som kan bli "fel på ett nytt sätt".

---

## Urvalet: 670 säkra av 811

Fyra filter. Ett kort måste klara **alla fyra** för att ingå.

| # | Filter | Faller bort | Varför |
|---|---|---|---|
| 1 | Kortet saknar grått block (`#9e9e9e`) | — | annars finns redan en etymologi |
| 2 | `HJ.etym(ord)` returnerar något | — | annars finns inget att skriva |
| 3 | 🔴 **Ordet innehåller inget mellanslag** | **81** | flerordsuttryck har förgiftade uppslagningar (se frasspärren 2026-09-04) |
| 4 | 🔴 **SO gav bara EN etymologirad** | **94** | flera rader = flera artiklar = risk för fel homograf |
| 5 | 🔴 **`uppslagsform` == kortets ord** | **4** | avvikande lemma = uppslagningen gäller ett annat ord |

**Kvar: 670 (82,6 % av 811).**

### 🔴 Varför filter 4 inte är överdrivet försiktigt

Kortet **`dia`** skulle utan det filtret få:

> *"av engelska dia med samma betydelse, kortform av diapositive"*

Det är **diabilden**. Kortet `dia` handlar om att amma. `etym()` tar rad 0, och
`sammanfatta()` bygger sammandraget av SO:s **två första träffar** — är träff
ett fel homograf skrivs fel etymologi in med full självsäkerhet.

**Risken är alltså mätt på ett verkligt fall, inte antagen.**

---

## Metoden

### Insättningspunkten

Kanonisk ordning på baksidan, verifierad mot **328 av 328** kort som har både
etymologi och bild — **etymologin ligger alltid före bilden, aldrig efter**:

```
<b>huvudbetydelse</b>
<br>(register)
<br><br><font color="#3498db">synonymer</font>
<br><br><i>exempelmening</i>
<br><br><font color="#9e9e9e">→ etymologi</font>      <-- HÄR
<br><br><img src="..." style="...">                    (om bilden finns)
```

🔴 **Naiv `+=` på slutet är därför fel.** 216 av de 670 slutar inte med
exempelmeningen — **188 slutar med ett `<img>`-block**. Etymologin skulle hamna
under bilden och bryta layouten mot resten av decket.

### Regeln

**Sätt in direkt efter det avslutande `</i>`.**

Verifierat: **alla 670 innehåller exakt ett (1) `</i>`.** Insättningspunkten är
alltså entydig — ingen gissning om vilket som är rätt.

```python
NY = '<br><br><font color="#9e9e9e">→ %s</font>' % etym
i = b.index('</i>') + len('</i>')
b_ny = b[:i] + NY + b[i:]
```

**Escaping behövs inte:** noll av de 670 etymologierna innehåller `&` eller `<`.
Kontrollera det ändå i steg 1 — förutsättningen kan ha ändrats.

### 🔴 Skrivdisciplin (från `agnat`-skadan)

1. **Bygg hela planen först. Skriv ingenting.**
2. För varje kort: verifiera att `</i>` förekommer **exakt en gång** och att
   `#9e9e9e` förekommer **noll gånger**.
3. **Avviker ett enda kort — avbryt hela körningen utan att skriva något.**
   Inte "hoppa över det och fortsätt".
4. Skriv först när alla 670 är verifierade.
5. Läs tillbaka alla 670 ur Anki och räkna.

---

## Kostnad

| | |
|---|---|
| Tokens | 🟢 **~4 000–5 000 totalt** |
| Väggklocka | 🟢 **under 2 minuter** |
| Pengar | 🟢 **0 kr** — ingen blindgranskning behövs |

🎯 **Varför så billigt:** det finns **ingen bedömning per kort**. Ett skript
loopar; ingen text formuleras. Kostnaden är skriptet plus en sammanfattning —
inte 670 × läsa-och-skriva.

⚠️ **Skriv INTE en rad per kort till utdata.** 670 rader ≈ 8 000 tokens i ren
loggning. Skriv en summering plus tio stickprov.

**Detta är inte ett fempassjobb. Det är ett femminutersjobb.**

---

## Körning

```
python _etymologi_670.py --torr     # bygger planen, skriver ingenting
python _etymologi_670.py            # verifierar allt, skriver sedan
```

### Verifiering efteråt

```python
# Ska ga fran 1227 till 557 (1227 - 670)
saknar = [n for n in alla_full_v3 if '#9e9e9e' not in baksida]
```

| Mått | Före | Förväntat efter |
|---|---|---|
| Full v3 utan etymologi | 1 227 | **557** |
| Andel utan etymologi | 51,3 % | **23,3 %** |
| Kort med grått block | 1 166 | **1 836** |

**Stämmer inte siffran exakt — utred innan något mer skrivs.**

### Rollback

Anki har ångra-historik per session, men säkraste vägen är
`deck_snapshot.py` **före** körningen. Ändringen är additiv (inget skrivs
över), så en rollback behöver bara ta bort det tillagda blocket — men ta
snapshotet ändå.

---

## 🟡 De 179 som INTE ingår

De ska **inte** köras blint. Var och en behöver en rad ögnad.

| Grupp | Antal | Vad som ska kontrolleras |
|---|---|---|
| Flerordsuttryck | 81 | Gäller etymologin frasen eller ett av orden? För idiom är komponentetymologin ofta ändå rätt (`leva i sus och dus` → *"till susa; jfr dus"* stämmer) |
| Flera etymologirader | 94 | Vilken artikel är kortets ord? Det är här `dia` sitter |
| Avvikande uppslagsform | 4 | T.ex. `vederkvickt` → uppslagsform `vederkvicka`. Oftast rätt, men kontrollera |

🎯 **Kör dem i en egen omgång efter de 670**, med `--torr` och ordet plus
etymologin utskrivna sida vid sida — det är då tio minuters läsning, inte ett
projekt.

---

## Kopplingar

- `slaupp.py` — frasspärren och `--antal`-fixen, båda 2026-09-04
- `_hjalp_0902b.etym()` — hämtningen, oförändrad
- `CLAUDE.md` → *"frasspärren"* — varför flerordsuttryck är undantagna
- `Study Coach Ai/log.md` 2026-09-04 — hela revisionen
