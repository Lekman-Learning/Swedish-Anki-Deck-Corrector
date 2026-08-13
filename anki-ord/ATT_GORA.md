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
