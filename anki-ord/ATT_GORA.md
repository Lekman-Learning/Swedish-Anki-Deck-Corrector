# Att göra — Anki-ord

Kö för arbete som är **identifierat och avgränsat men medvetet uppskjutet**.
Skilt från `CLAUDE.md`, som beskriver hur systemet fungerar. En rad stryks när
den är gjord — historiken hör hemma i valvets `log.md`.

---

## 1. Synonymgrupper saknar `;` på 238 kort

**Adams observation 2026-08-13:** *"jag hittar ibland kort där synonymerna inte
har `;`-tecknet för de olika betydelserna."* Uppskjutet samma dag av
tokenskäl — **inte** avfärdat.

### Var felet sitter

`baksida.py:345` kör gruppkontrollen bara om grupper redan skickats in:

```python
if synonym_groups:
    if len(synonym_groups) != len(ms):
        lagg("grupper_matchar_ej_betydelser", ...)
```

Skickas en platt lista med `synonym_groups=None` händer ingenting, även om
kortet har tre betydelser. **Spärren kontrollerar alltså bara de kort som redan
följer regeln.** Renderingen faller tyst tillbaka på samma ställe
(`baksida.py:181–184`): utan grupper blir det `", ".join(...)` — ingen
avgränsare, ingen varning.

### Omfattningen (mätt 2026-08-13 mot sessionsfilerna i git, deduplicerat på noteId)

| | Antal |
|---|---|
| Unika kort i v3-paketen | 907 |
| En betydelse — berörs inte | 599 |
| Flera betydelser, **grupperat** | 68 |
| Flera betydelser, **platt (defekt)** | **238** |

**78 % av flerbetydelsekorten med synonymer saknar `;`.** Anki var inte igång
vid mätningen, så siffran gäller paketen, inte det levande decket — men
riktningen är entydig.

**Det är inte ett gammalt problem som växt bort.** Det växlar med vilket
patchskript som råkade skriva grupper: `session_2026-08-12_v3-paket-nya.json`
har 14 grupperade mot 1 platt, medan `session_2026-08-12_v3-paket3.json` —
batch3, den första under den nya synonymspärren — har **0 grupperade mot 4
platta**. Utan spärr blir utfallet slump.

### Vad som ska göras

1. Ny **hård** regel `synonymer_ogrupperade` i `validate_adamtal`: flera
   betydelser + minst en synonym ⇒ grupper krävs. Lägg i `ADAMTAL_HARDA`.
2. **Mjuka upp `tom_synonymgrupp`.** Den är i dag hård ("tom grupp ger ett
   `; `-artefakt"), vilket krockar med Adams beslut 2026-08-12 att tom
   synonymlista är godkänt: ett ord med två betydelser där bara den ena har
   belagd synonym har ingen laglig form i dag. **Förslag, ej godkänt än:**
   rendera tom plats som tankstreck — `väluppfostrad, kultiverad ; –`.
   Skälet är att den platta formen är *tvetydig* — man ser inte om synonymerna
   gäller båda betydelserna eller bara en. Strecket är information, inte skräp.
3. Arbetslista över de 238. **Billig att beta av** — betydelserna och
   synonymerna finns redan på korten, det är en fördelning, inga nya
   uppslagningar. Kan tas batchvis vid sidan av ordinarie produktion.

---

## 2. Adam-ändrade och rödflaggade kort ska granskas om

**Adams regel 2026-08-13:** *"kort som jag ändrar själv eller ger röd flagga är
kort vi behöver gå igenom igen även om de är full v3 — kanske har de ett litet
fel."*

Full v3 är alltså **inte** ett sluttillstånd. Två signaler bryter det:

| Signal | Vad den betyder |
|---|---|
| Adam har redigerat kortet | Något var fel nog att han rättade det för hand — och det jag skrev runt omkring är då också misstänkt |
| Adam har satt röd flagga | Uttrycklig markering: gå igenom det här igen |

**Obs kollisionen:** röd flagga används redan av `v3_underkand`-flödet för kort
som blindgranskningen underkänt. Adams manuella flaggor bär **inte** den taggen,
så de går att skilja åt: `flag:1 -tag:v3_underkand::*`.

### Så hittas de Adam-ändrade

Mekanismen finns redan byggd — färskhetsspärren i `verdikt()` vägrar döma ett
kort som ändrats sedan paketeringen. Samma jämförelse gör jobbet här: notens
nuvarande innehåll mot vad sessionsfilen registrerade att jag skrev. Skiljer de
sig har någon annan än jag rört kortet.

### Vad som ska göras

1. Ett urvalskommando som listar båda grupperna (`flag:1 -tag:v3_underkand::*`
   plus innehållsdiff mot sessionsfilerna).
2. Låt `kortbyggare.py` behandla dem som en egen kö med företräde — de är
   bevisade problem, till skillnad från kort som bara *kan* ha fel.
3. Fundera på om `slapp` ska ta bort `oberoende_verifierad` när Adam rört
   kortet. Annars påstår decket att ett kort är oberoende verifierat i en form
   det inte längre har.

---

## Hittat 2026-08-15

### 1. `slaupp.py` kraschar på uppslagsord som innehåller `/`

`regel / rigel` gav `FileNotFoundError: 'uppslag\regel / rigel.json'` — snedstrecket
gör filnamnet till en ogiltig sökväg. Två följdproblem gör den värre än den ser ut:

* **Kraschen sker EFTER hämtningen.** Alla tre API-anropen görs, svaret kastas.
* **Körningen avbryts.** Ord som ligger efter det trasiga i listan slås aldrig upp
  — `svärmisk` (nr 50) föll bort tyst och upptäcktes bara för att applicera-steget
  saknade det.

Fix: `re.sub(r'[\/:*?"<>|]', '_', ordet)` på filnamnet, och låt loopen fånga
undantag per ord i stället för att fälla hela körningen.

### 2. Två kort har defekt framsida

* **`kvintessensen`** står i bestämd form; ordbokens lemma är `kvintessens`.
  Hål 0 gav `traffar=INGEN`. Samma klass som `te`/`tes` och `gem`/`gemen`.
* **`regel / rigel`** har två stavningar i samma fält, och `regel` är dessutom ett
  helt annat ord ('föreskrift, norm', latin *regula*) än låsanordningen.
* **`divan`** är genuint tvetydig: möbelns grundform ELLER bestämd form av `diva`.
  SO och SAOL listar båda. Kortet skriver möbeln.

Alla tre är lämnade orörda — framsidan ändrar vad Adam testas på och är hans beslut.

### 3. Förorenade MÄRKNINGAR, inte bara definitioner

Känt sedan tidigare att `slaupp.py`s sammandrag slår ihop fuzzy-träffar. Nytt fynd:
**registermärkningen smittas likadant**, och den spärren larmar på det.

| Ord | Fick märkningen | Från |
|---|---|---|
| `på nåder` | "något högtidligt" | `nådens år` |
| `vind för våg` | "vardagligt" | `grön våg` |
| `barka åt skogen` | "delvis historiskt" | `barka` = behandla segel |
| `fiken` | "vardagligt" | `fik` = kaféet |
| `vitsord` | "finl." | SAOL:s finlandssvenska bibetydelse |

Alla fem krävde redovisat undantag. Det är värt en egen kontroll: när ett ord har
främmande uppslagsord i träffarna är dess märkning lika misstänkt som dess glosor.

### 4. Blindgranskningen kraschade på ett 53-posters paket (2026-08-15)

`blindgranska.py sessions/session_2026-08-15_v3-paket-repetition.json` gav:

```
RuntimeError: claude gav inget användbart svar (returkod 1)
stdout: {"is_error":true,"duration_api_ms":1397289,"num_turns":1,
         "stop_reason":"stop_sequence","total_cost_usd":3.66566955,
         "usage":{"input_tokens":0,"output_tokens":0, ...}}
```

**23 minuter, 3,67 USD, noll utdata, noll tokens registrerade.** `num_turns: 1`
och `stop_reason: "stop_sequence"` -- granskaren stannade direkt utan att svara.

Skillnaden mot batchen som gick igenom samma kväll: **53 poster mot 50.** Det kan
vara storleken, men det kan lika gärna vara en övergående störning -- en enda
observation räcker inte för att avgöra.

**Följd just nu: 50 kort ligger skrivna och applicerade i Anki men utan
`oberoende_verifierad`.** De är alltså INTE full v3 och släpps inte. Frågan
`tag:v3_granskad::2026-08-15 -tag:oberoende_verifierad::*` hittar dem (55 st,
inklusive de 5 underkända från spår A-batchen).

**Nästa gång:** kör om paketet först utan ändringar -- om det fungerar var det
en störning. Fungerar det inte, dela paketet i två om ~27 (fortfarande långt
över golvet på 17) och jämför. Logga utfallet här oavsett vilket; det här är
första gången steget failat helt sedan det byggdes.

**Omkörning samma kväll — failade igen, men annorlunda:**

```
AVBRYTER: granskaren gjorde bara 4 turer på 53 kort (kräver >= 13).
```

Andra gången är alltså **inte** en krasch utan en spärr som gjorde sitt jobb:
granskaren svarade utan att slå upp något, och en obelagd dom får inte skrivas in.

**Det ändrar diagnosen.** Storleken är sannolikt inte problemet — samma kväll
klarades 50 poster med 18 turer. Båda felen pekar i stället mot att
granskarprocessen **inte kommer åt uppslagningarna**: första gången noll utdata
efter 23 minuter, andra gången svar utan hämtningar. Felmeddelandet säger det
själv: *"Kontrollera att WebFetch är tillåten och att svenska.se svarar."*

**Dela alltså INTE paketet än** — det åtgärdar fel sak. Kontrollera först att den
fristående `claude -p`-processen får använda WebFetch, och att svenska.se svarar
från den miljön. Kostnad hittills för de två försöken: **3,67 USD plus en
omkörning, noll granskade kort.**

**Diagnosen rättad efter kontroll (2026-08-15, sent):** båda mina hypoteser var fel.

* **Inte behörigheten.** `TILLATNA_VERKTYG = ["Read", "WebFetch", "WebSearch"]` —
  WebFetch är redan tillåten, så felmeddelandets egen gissning stämmer inte.
* **Inte storleken.** Paketet som failade är **mindre** än det som lyckades:
  42 854 byte på 53 poster mot 53 049 byte på 50. Snitt per post 647 mot 896 tecken.

Kvar står **variation i granskarens beteende**. Tröskeln är `max(5, antal // 4)`,
alltså 13 turer för 53 kort. Samma sorts jobb gav 18 turer i den lyckade körningen
och 4 i den failade. Spärren gör exakt vad den ska — den skiljer en granskare som
slår upp från en som svarar ur minnet — men den kan inte tvinga fram uppslagningar.

**Slutsats: dela inte paketet, kör om.** Failar tre körningar i rad är det något
systematiskt och då är delning nästa steg. En enstaka miss är väntad variation.

Värt att överväga senare: låta scriptet **själv köra om en gång** vid turer under
tröskeln, i stället för att avbryta och kräva manuellt ingripande. Kostnaden för
en omkörning är densamma som för den misslyckade körningen som redan betalats.

**ÅTGÄRDAT 2026-08-15 (sent): två ändringar i `blindgranska.py`.**

*1. Kravet syns nu för granskaren.* Spärren var **osynlig för den som granskades** —
prompten sa "SLÅ UPP ORDET SJÄLVT" men nämnde aldrig att för få verktygsanrop
kasserar hela jobbet. En granskare som optimerar för att bli klar hade alltså
inget skäl att veta att genvägen förstörde körningen. Prompten säger nu rakt ut:

> *"du ska göra minst {krav} verktygsanrop … En granskning med färre anrop
> KASSERAS automatiskt och sparas inte … det gör hela körningen värdelös, inte
> snabbare."*

*2. Automatisk omkörning.* Ny `_granska_med_omkorning()` kör granskaren igen **en
gång** om turerna hamnar under tröskeln, i stället för att avbryta och kräva att
någon startar om för hand. Kostnaden för omkörningen är densamma som för den
misslyckade körning som redan är betald.

⚠️ **Spärren är INTE borttagen.** Den ligger kvar nedströms och fäller även andra
försöket om det också svarar ur minnet. Det som ändrats är bara att ett
misslyckande inte längre kräver mänskligt ingripande.

**Fjärde körningen (2026-08-16, strax efter midnatt) — nytt felmönster, och det pekar bort från modellen.**

Omkörningsloopen fungerade som byggd: två försök, båda rapporterade. Men båda
failade **omedelbart**:

```
forsok 1/2 misslyckades: claude gav inget användbart svar (returkod 1).
forsok 2/2 misslyckades: claude gav inget användbart svar (returkod 1).
stdout: {"is_error":true,"duration_api_ms":0,"num_turns":1,
         "stop_reason":"stop_sequence","total_cost_usd":0,
         "usage":{"input_tokens":0,"output_tokens":0,
                  "server_tool_use":{"web_fetch_requests":0}}}
```

**`duration_api_ms: 0` och `total_cost_usd: 0` betyder att API:et aldrig
anropades.** Det är inte en granskare som svarar dåligt — det är en process som
vägras innan den börjar. Jämför med körning 1 samma kväll: 23 minuter och 3,67
USD, alltså samma slutresultat men efter att arbetet faktiskt utförts.

Hela serien, i ordning:

| # | Turer | Duration | Kostnad | Tolkning |
|---|---|---|---|---|
| 1 | 1 | 1 397 s | 3,67 USD | kördes, dog vid utskrift |
| 2 | 4 | — | — | kördes, för få uppslagningar |
| 3 | 11 | — | — | kördes, marginellt under tröskeln |
| 4 | 1 + 1 | **0 s** | **0 USD** | **startade aldrig** |

**Sannolikaste förklaringen: användningsgräns.** Kvällen innehöll en fullständig
granskning (3,67 USD) plus tre försök till, och nummer fyra nekas utan att kosta
något. Rate limit eller veckokvot ger exakt det mönstret.

**Att kontrollera innan nästa försök**, i den här ordningen:

1. Kör `claude -p "hej" --output-format json` för hand i en tom katalog. Failar
   den likadant är det kontot, inte scriptet.
2. Kolla veckokvoten. Blindgranskningen startar ett **eget** `claude`-anrop som
   drar från samma tak som huvudsessionen.
3. Först därefter är det värt att titta på paketet igen.

**Kör inte fler försök blint.** Tre av fyra kostade pengar utan att ge ett enda
granskat kort.
