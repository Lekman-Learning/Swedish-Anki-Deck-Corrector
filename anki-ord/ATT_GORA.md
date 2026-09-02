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

### LÖST 2026-08-16: paketstorleken, och de tre kontrollerna i tur och ordning

Kontrollistan ovan följdes, och den första punkten avfärdade genast de två
hypoteser som stod kvar:

```
$ claude -p "hej" --output-format json      # i tom katalog
{"is_error":false,"duration_api_ms":1710,"total_cost_usd":0.0665526, ...}
```

**Alltså varken kvoten eller CLI:t.** Kontot svarade normalt minuterna efter att
fjärde försöket nekats. Punkt 2 och 3 behövde aldrig köras.

Kvar stod paketet, och delkörningar avgjorde saken:

| Poster | Turer | Kostnad | Utfall |
|---|---|---|---|
| **53** | 1 / 4 / 11 / 1 | 3,67 USD + 3 | ❌ fyra gånger |
| **20** | 38 | 1,28 USD | ✅ |
| **10** | 20 | 0,74 USD | ✅ |

**Granskaren gör ~1,9 turer per kort.** Det är den siffran som förklarar allt:
53 kort kräver omkring **100 turer**, och en `claude -p`-process har ett tak för
hur många turer den får ta. Körning 1 passar mönstret exakt — 23 minuter och
3,67 USD betalt, alltså arbetet faktiskt utfört, men `num_turns: 1` och inget
svar när taket slog i innan JSON:en hann skrivas.

**Det rättar min egen felslutning från i går.** Jag mätte paketen i *byte* (42 854
mot 53 049) och skrev "inte storleken — det failade paketet är mindre". Måttet var
fel: granskaren betalar per **kort**, inte per tecken, eftersom varje kort kostar
sina egna uppslagningar. Ett kompakt paket med fler poster är dyrare i turer än ett
mångordigt med färre. Byte var aldrig rätt enhet.

**Regel härefter: högst ~25 poster per blindgranskning.** Är paketet större, dela
med `--antal`. Spärren i `granska()` säger nu ifrån före körningen i stället för
efter att pengarna är spenderade.

**Tre ändringar i `blindgranska.py`:**

1. **`--antal N`** — granska bara de N första odömda. Urvalet görs på
   `verdikt`-fältet, så delkörningar är återupptagbara utan egen bokföring.
2. **Felmeddelandet kapades vid 500 tecken → 8 000.** `claude` lägger sin
   felorsak i JSON-fältet `result`, som kommer EFTER `usage`-blocket. Alla fyra
   failade körningar visade därför bara *att* något gick fel, aldrig *vad* —
   stdout tog slut mitt i usage-siffrorna. Samma felklass som `raw-verktyg/`s
   kapningsregel finns för att stänga: en kapad utdata som ser komplett ut är
   värre än ingen alls.
3. **`granskning_korningar`** — varje delkörning läggs till i en lista.
   `granskning_turer` skrivs över av nästa omgång, och då försvann mätningen för
   de tidigare; exakt den lucka fältet lades till för att stänga.

### `apoplexi` — andra gången en blindgranskare har bevisligen fel

Underkändes för "sakfel: kortet anger 'blödning ELLER propp', men SAOL definierar
ordet som hjärnblödning". SO:s kedja säger motsatsen:

* `apoplexi` → **"slaganfall"**
* `slaganfall` → **"plötslig förlamning, medvetslöshet eller död särsk. till följd
  av cirkulationsstörning i hjärnan (blödning el. blodpropp)"**

Kortet följer SO ordagrant. **Samma felmönster som `brödtext` 2026-08-12:**
granskaren dömde på SAOL:s korta glosa där SO — som prompten uttryckligen säger
"avgör dagens betydelser" — har den fylliga definitionen. Två observationer är ett
mönster: SAOL är ett *stavnings*lexikon och dess glosor är avsiktligt knappa, men
de läser som fullständiga definitioner.

**Värt att pröva i prompten:** säg rakt ut att SAOL:s korthet inte är ett
motargument mot en fylligare betydelse i SO, och att ett `jfr`- eller
hänvisningsord ska följas ett steg. Ändra dock inte mitt i ett paket — då blir
delkörningarna inte jämförbara.

Kortet skickas tillbaka **oförändrat** med SO-citatet inskrivet i sökkollen, samma
väg som `brödtext`. Domen vänds inte för hand.

---

## Hittat 2026-08-18

### 1. `blindgranska.py` måste startas som förgrundsprocess

**Symtom:** tom loggfil, `granskare: None`, alla 19 verdikt `None` — och
exitkod 0, alltså inget som ser ut som ett fel.

**Orsak:** startad som `nohup python blindgranska.py ... &` inifrån ett
verktygsanrop. Skriptet startar en fristående `claude`-process; när det
anropande skalet returnerar dör hela processträdet med det. Ingenting skrivs,
och `&` gör att felet inte syns i exitkoden.

⚠️ **Förväxla inte med 16 augusti-felet.** Då gav körningen *23 minuter,
3,67 USD och noll utdata* — orsaken var paketstorleken. Här är kostnaden noll
och tiden noll. **Samma tomma resultat, helt olika orsak** — kontrollera
alltid loggens storlek innan slutsatsen dras.

**Regel:** kör `blindgranska.py` i förgrunden (låt anropet självt vara
bakgrundat om det behövs), aldrig med `nohup ... &`. Kontrollera efteråt att
`granskare` är ifyllt och att verdikträknaren inte är `{None: N}`.

### 2. Bevisraderna kapades — fjärde och femte gången

`slaupp.py`s `SVENSKA_SE_HAMTAD`-rader måste nå transkriptet intakt, annars
vägrar Hål 0 skriva korten. Kapades den här gången först med `grep -v` och sedan
med `tail -70`. **`--tyst` finns för exakt det här** och användes först i tredje
försöket.

**Spärren fungerade som avsett** — inget obelagt kort kom in, båda gångerna.
Det är kommandovanan som är problemet, inte skriptet. Överväg att låta
`slaupp.py` skriva bevisraderna även till en fil, så att de överlever ett
filtrerat stdout.

### 3. Idiom: `kalla` måste peka på grundordet

`i förbigående` slås upp som **förbigående** — men `sokkoll.kalla` sattes till
`?ord=i`, vilket Hål 0 underkände. Sätt alltid `kalla` till det uppslagsord
`slaupp.py` faktiskt hämtade, inte till kortets framsida.

**Spotkollad 2026-08-18 (senare samma kväll): fortfarande rätt.** Både
`i förbigående` och `trojansk häst` i dagens batch har `kalla` satt till
respektive grundords faktiska uppslag (`?ord=förbigående`,
`?ord=trojansk häst`), inte framsidans första ord. Inget kodfel kvar att
åtgärda — bara ett mönster att komma ihåg vid nästa idiomkort.

### 4. LÖST 2026-08-18: Hål 0 hittade aldrig en subagents transkript

**Symtom:** en `kortgranskare.py applicera`-körning från en Agent-verktygs-
subagent blockerade 14 av 19 kort med `SÖKKOLL EJ BEVISAD ... hämtningen
gjordes aldrig` — trots att `slaupp.py` bevisligen hade kört och skrivit
`SVENSKA_SE_HAMTAD <ord> HTTP 200 <byte>` för alla 19, och `grep` hittade
raderna direkt i transkriptfilen.

**Orsak:** `sokkoll_verifiering.py`s glob-mönster var `projects/*/*.jsonl` —
EN nivå under `~/.claude/projects/`. En subagent (startad via Agent-
verktyget) loggar till en EGEN fil TRE nivåer ned:
`projects/<projekt>/<session-id>/subagents/agent-<id>.jsonl`. Mönstret
missade den helt. De 5 kort som ändå gick igenom (av 19) berodde på en
slump: föräldrasessionens EGEN transkriptfil (en nivå ned, alltså
matchande) råkade innehålla en tidig, ofullständig kopia av subagentens
utskrift — bara de första fem orden hade hunnit speglas dit innan
kopieringen (vad det nu var) slutade följa med.

**Fix:** bytt till rekursiv glob (`projects/**/*.jsonl`, `recursive=True`) i
BÅDA `_urler_ur_transkript()` och `_ord_ur_skriptutskrift()`. Verifierat:
alla 19 ord gick från `False` till `True` i `granska_kalla()`, körtiden för
en full genomsökning av hela `~/.claude/projects/` (inklusive en 130 MB-fil)
var ~6 sekunder — ingen prestandaoro.

**Påverkar bara arbete gjort via en subagent.** Vanliga huvudsessioner
loggar redan en nivå ned och träffades av det gamla mönstret. Värt att
komma ihåg om Adam ser samma felmeddelande från en huvudsession framöver —
då är förklaringen en ANNAN, inte den här.

### 5. `slaupp.py` kan tysta hämta FEL ord för flerordsuttryck

Upptäckt 2026-08-18 vid en rutinkomplettering av `uppslag/trojansk häst.json`
(gjord bara för att städa bort en mjuk `uppslag_saknas`-varning -- ordet var
redan skrivet och släppt utan denna fil). Hämtningen gav HTTP 200 och
`traffar=saol,so` -- ser alltså ut som en lyckad uppslagning -- men
`sammandrag.svenska_se.so.def` innehåller Troja-etymologi, dragdjursspann,
brovalv och skidbindning: **det är ordet `spann`s artikel**, inte idiomets.
`trojansk häst` förekommer bara som EXEMPELMENING i `spann`s artikel
("spannet var förspänt"-familjen), och svenska.se:s fuzzy-sök i
`msearch?ord=trojansk häst` landade på den artikeln istället för idiomets
egen (om en sådan ens är egen-indexerad).

**Samma felklass som redan dokumenterad 2026-08-15** ("Förorenade
MÄRKNINGAR, inte bara definitioner") -- fast där gällde det enskilda ord med
närliggande stavning, här ett helt flerordsuttryck som inte alls matchar
sökträffen semantiskt. `forgranska.py`s `frammande_uppslagsord`-regel fångade
det (35 obesläktade uppslagsord i träffarna: "biff, box, däst, flank, fäst
+29 till" -- en tydlig signal att sökträffen inte hör hemma här).

**Ingen skada skedd den här gången**: kortets faktiska innehåll (skrivet av
en tidigare session) verkar korrekt källat på annat sätt (troligen riktig
websökning, inte `slaupp.py`), och den lokala cachefilen läses aldrig av
`blindgranska.py` (som bara ser paketfilens `facit`+`kort`). Men **kör alltid
`forgranska.py` på en fil EFTER en `slaupp.py`-komplettering**, inte bara
efter att ha skrivit nytt innehåll -- annars upptäcks en förorenad cache för
sent, som här (upptäckt efter att blindgranskningen redan startats).

Möjlig framtida fix: låt `slaupp.py` jämföra sökordet mot den TRÄFFADE
artikelns `ortografi`/`ordled`-fält (samma mekanism som redan finns för
`frammande_uppslagsord` i `forgranska.py`) och vägra spara/flagga tydligt
när de inte stämmer överens, i stället för att skriva en fil som SER
komplett ut.

---

## Hittat 2026-08-18, sent: Adam-tal-regression -- kort läser som ordbok

**Adam, mitt i ett HP-prov, utan tid att peka ut exempel:** *"jag ser kort
som läser ut som kopior av SO/SAOB istället för Adam-tal."* Undersökt utan
honom, mot cachad källa i `uppslag/`.

### Mätningen

Alla 45 kort släppta till full v3 idag (14 innan kvällens fortsättning +
15 från review18 + 16 från review17) jämförda ord-för-ord mot sin egen
cachade SO/SAOL-definition (containment-score: andel ord i Huvudbetydelsen
som också finns i källtexten).

| Score | Antal | Vad det betyder |
|---|---|---|
| 1.00 (ordagrant) | 15 av 45 (33 %) | Varje ord i Huvudbetydelsen finns i SO/SAOL:s egen text |
| 0,83-0,90 | 4 av 45 | Nästan ordagrant, enstaka ord bytt |
| ≤0,5 | 26 av 45 | Genuint omskrivet med egna ord |

**Verdikt: verklig regression, inte normal variation.** 19 av 45 (42 %) är
ordagranna eller nästan ordagranna kopior. Motbeviset mot "vissa ord saknar
en piggare formulering" finns i samma mätning: kort som `i förbigående`
("Bara flyktigt, som en parentes i något annat man höll på med"),
`konnässör` ("...ofta mat eller vin", draget ur SO:s exempel, inte
definitionen) och `husvill` ("Utan tak över huvudet") visar att en
Adam-tal-omskrivning GÅR att göra för nästan vilket ord som helst -- de
ordagranna korten är inte ord utan alternativ, de är kort där omskrivningen
aldrig gjordes.

**Rotorsak: inget steg i pipelinen kontrollerar avstånd till källan.**
`forgranska.py`s enda längdrelaterade regel (`ordbokslangd_hb`) blockerar
bara betydelser över 12 ord -- den mäter LÄNGD, inte NÄRHET till SO/SAOL:s
egen formulering, så en kort ordagrann kopia (t.ex. `burrig`: "Yvig, krusig
och något rufsig", 5 ord) passerar den perfekt. Blindgranskningens egen
`VERIFIERARINSTRUKTION` (punkt 8) frågar bara "går kortet att läsa högt och
förstå direkt, utan att slå upp ännu ett ord" -- en ordagrann SO-kopia
klarar OCKSÅ det trivialt, eftersom SO:s korta glosor per definition är
begripliga. **Ingen kontroll i hela kedjan (varken den mekaniska spärren
eller den blinda granskaren) frågar "är detta AdamS röst eller ordbokens?"**
Det är alltså inte ett slarvfel av en enskild skrivare -- det är en riktig
lucka i vad pipelinen mäter, och den drabbar flera sessioner samma kväll
(både kort skrivna innan denna fortsättning och kort jag själv skrev).

### Fem värsta exemplen (score 1.00, med förslag på Adam-tal -- INTE applicerat)

| Ord | Nuvarande (= SO/SAOL ordagrant) | Föreslaget Adam-tal |
|---|---|---|
| `vederhäftig` | "Saklig och sanningsenlig ; Pålitlig när det gäller sakuppgifter" | "Går att lita på -- säger sanningen och håller sig till fakta" |
| `burrig` | "Yvig, krusig och något rufsig" | "Håret står åt alla håll, lite tovigt" |
| `exkrement` | "Avföring från tarmen" | "Bajs -- det medicinska ordet för det" |
| `paradox` | "Skenbart orimligt men ändå djupare sett sant påstående" | "Något som låter motsägelsefullt först, men stämmer om man tänker efter" |
| `konvoj` | "Grupp av handelsfartyg som åtföljs och skyddas av örlogsfartyg ; Skyddad transport till lands ; Rad av fordon som färdas tillsammans, utan att nödvändigtvis vara skyddade" | "En grupp fartyg som reser tillsammans med militärt skydd ; En rad fordon som kör i följd, med eller utan skydd" |

`konvoj` är mitt eget fel -- jag skrev om kortet tidigare i kväll (efter ett
annat underkännande om en saknad betydelse) och lade till den tredje
betydelsen i exakt SO:s egen hedge-formulering ("utan att nödvändigtvis
vara skyddade") istället för att formulera om den. `vederhäftig`, `burrig`,
`exkrement`, `paradox` skrevs INTE av mig -- de fanns bland de 14 som redan
var släppta innan kvällens fortsättning började, alltså från en tidigare
session/dag. Regressionen är alltså inte knuten till en enda skrivomgång.

### Vad som INTE gjorts

**Inga av de 45 korten har ändrats som en följd av den här undersökningen.**
Adam bad uttryckligen att inte tyst massrätta -- han behöver se
omfattningen själv först. De fem exemplen ovan är förslag i den här filen,
inte applicerade ändringar.

**Konsekvens för kvällens 50 nya kort (samma session, se nedan i
loggen/commit-historiken):** varje Huvudbetydelse kontrollerades mot samma
containment-mått INNAN applicering, med en informell tumregel: score över
~0,6 mot SO/SAOL = skriv om innan kortet skickas vidare.

### Förslag till permanent fix (ej byggt, Adams beslut om det ska prioriteras)

En mjuk regel i `forgranska.py`, `ordagrann_kopia`: räkna containment
mellan varje betydelse i Huvudbetydelsen och den cachade SO/SAOL-texten
(samma metod som användes i den här undersökningen). Larma vid t.ex. >70 %
overlap. Mjuk, inte hård -- några ord (korta, redan vardagliga SAOL-glosor
som `sari`s "ett indiskt kvinnoplagg") har helt enkelt ingen piggare
formulering, och en hård spärr hade tvingat fram konstlade omskrivningar

---

## Hittat 2026-08-18, sent (batch2 50 is:new-kort): Hål 0 trunkerar flerordsuppslag i `kalla`

`kortgranskare.py applicera` blockerade 4 av 48 kort (`som en löpeld`,
`förhäva sig`, `göra en höna av en fjäder`, `i blindo`) med "SÖKKOLL EJ
BEVISAD ... hämtningen gjordes aldrig" -- felmeddelandet visade
`https://svenska.se/api/msearch?ord=som` för `som en löpeld`, alltså
`kalla`-URL:en trunkerad vid mellanslaget.

**Orsak:** `sokkoll_verifiering._URL_RE = re.compile(r"https?://[^\s\"'<>,;)\]]+")`
stannar vid första blanksteget -- korrekt för att skanna fri text efter
URL:er (t.ex. i ett WebFetch-anrop), men fel när själva `kalla`-fältet
ÄR URL:en och `ord=`-värdet innehåller mellanslag (flerordsuttryck).
`slaupp.py` bygger sin egen bevisrad (och `kalla` skrevs, i linje med det,
via) med ett BOKSTAVLIGT mellanslag i `ord=`-värdet -- inte
procentkodat -- så den extraherade (trunkerade) URL:en matchar aldrig
bevisnyckeln, som är den fullständiga strängen.

**Förvillande detalj:** `trojansk häst` (skrivet TIDIGARE i kväll, se punkt
4 ovan) klarade sig ändå -- men av en slump, inte för att det fungerade
rätt. En separat, ORELATERAD bevisrad för bara `ord=trojansk` (utan
`häst`) råkade redan finnas i transkriptet (troligen en bieffekt av
`slaupp.py "trojansk häst" "i förbigående" --tyst`-körningen tidigare
samma kväll, som av oklar anledning även loggade en post för enbart
`trojansk`). Den trunkerade extraktionen matchade DEN posten. Kortets
innehåll är fortfarande korrekt sökkollat -- den maskinella bevisningen
för just det kortet var bara tur, inte en fungerande kontroll.

**Verifierat workaround (använt för alla fyra blockerade korten):**
procentkoda mellanslaget i `kalla` (`urllib.parse.quote`, t.ex.
`?ord=som%20en%20l%C3%B6peld`). Då stannar `_URL_RE` inte vid URL:en, och
`_normalisera()`s `urllib.parse.unquote`-steg gör att den avkodade formen
matchar bevisnyckeln (som har ett bokstavligt mellanslag) exakt. Bekräftat
med ett direkttest mot `sokkoll_verifiering.granska_kalla()` innan det
användes skarpt.

**Ingen kodändring gjord i `sokkoll_verifiering.py`** -- `_URL_RE` används
även för fri textskanning (WebFetch-anrop) där en bredare regel som
tillåter mellanslag skulle riskera att sluka efterföljande prosa. En
riktig fix kräver antingen en URL-kodad konvention för `kalla` (dokumentera
och eventuellt validera vid skrivning) eller en särskild, snävare regel
bara för `svenska.se/api/msearch`-mönstret. Adams beslut om det är värt
att bygga.

**Regel för framtida flerordsuppslag i `kalla`:** procentkoda alltid
mellanslag (`urllib.parse.quote(ord, safe="")`) när uppslagsordet har fler
än ett ord -- annars ser sökkollen ut att misslyckas trots en bevisligen
gjord hämtning.
bara för sakens skull.

---

## N. `v3_underkand*`-wildcarden fångar `v3_underkand_rensad` — fel håll

**Hittat 2026-09-02** på Adams fråga *"hur kan ej suspenderade kort vara 5 fler
än full v3-korten?"*

`v3_invariant.py:53` undantar kort med

```python
UNDANTAG = "(tag:v3_underkand* OR tag:v3_pausad::*)"
```

Wildcarden matchar även **`v3_underkand_rensad::2026-08-26`**, som fem kort bär:
`märgfull`, `apoplexi`, `förvärva`, `beskärm`, `alla taggar utåt`.

**De ska inte undantas.** `_rensad` betyder att underkännandet är åtgärdat, och
korten uppför sig därefter: alla fem är **blåflaggade** (full-v3-flaggan),
**avsuspenderade**, bär **hela v3-tagguppsättningen**, och fyra har 2-dagars
intervall — alltså omlärda kring 26 augusti.

**Följd:** skriptet rapporterar `Full v3, ej undantagna: 2257` när det korrekta
är **2262**, och listar fem aktivt använda kort som *"ska förbli röda+spärrade"*.
Hade `--fixa` körts på undantagslistan hade de suspenderats — fem kort Adam
pluggar dagligen.

**Åtgärd:** byt till en pattern som inte fångar `_rensad`, t.ex.

```python
UNDANTAG = "(tag:v3_underkand::* OR tag:v3_pausad::*)"
```

⚠️ **Rotorsaken är större än den här taggen:** `v3_underkand_rensad` finns
**ingenstans i koden eller i någon markdown-fil** — den sattes för hand 26
augusti och lever bara i Anki. Ett undantagsfilter som matchar wildcard mot
odokumenterade taggar kommer fånga fel igen. Taggvokabulären bör stå i
`config.py` och kontrolleras.

## 2026-09-02: synonymregeln, och tva verktyg som gjorde resten mekanisk

**Felet:** forsta batchen om 18 kort skrevs med synonymer fran synonymer.se.
**13 av 18 fick `synonym_utan_ordboksbelagg`.** synonymer.se raknas INTE som
ordboksbelagg -- bara SO:s `SYN:`-falt och SO/SAOL:s egen definitionstext gor
det. Regeln star i forgranska.py 4c, och spegeln 4d (`synonym_saknas_trots_belagg`)
sager rakt ut att **tom lista ar normalfallet, 69 % av korten**.

**Nya verktyg (bada laser bara cache, inget nat):**

- `_pool.py <ord>` -- skriver ut exakt vilka synonymer forgranska GODTAR, plus
  antalet SO-betydelser. Anropar forgranskas egna funktioner (`_ordboksbelagg`,
  `_so`, `_riktiga_underbetydelser`) i stallet for att aterimplementera regeln,
  sa verktyget och kontrollen inte kan glida isar.
- `_syn_etym.py` -- synonymer.se-avdelningarna och etymologin ur uppslag/,
  som komplement till `visa_uppslag.py` (den visar bara SO/SAOL-definitioner).
  OBS: syn.se-listan ar BAKGRUND, inte belagg -- valj alltid ur `_pool.py`.

**Observation vard att atgarda:** `_riktiga_underbetydelser` slapper igenom
rena grammatiska etiketter. `coupe` raknades som 3 betydelser dar tva var
**"best. form"** och **"plural"**; `sakral` som 2 dar den andra var
**"MOTSATS:antonym"**. Foljden ar att `betydelse_kan_saknas` -- ett HART fel --
utloses pa brus och maste tystas med en skriven motivering per kort. Ett filter
mot `best. form|plural|MOTSATS:|el.$|spec.$` skulle ta bort merparten.

**Batch A klar: 18 kort, 0 harda anmarkningar.** Kvar: 113 (135 minus 18 minus
de fyra pauskandidaterna).
