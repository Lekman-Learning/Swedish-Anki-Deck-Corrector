# Instruktion till blindgranskaren

Du granskar tio färdiga Anki-kort som **någon annan** har skrivit. Du ska inte
förbättra dem — du ska avgöra om de **stämmer**.

Du får inte veta hur korten blev till, vad som ändrades, eller vilka källor som
användes. Det är avsiktligt: en granskare som ser resonemanget granskar
resonemanget i stället för resultatet.

## Det här löser förra gångens problem

Blindgranskningen 2026-08-09 gav **3 godkända, 2 underkända**, och båda
underkännandena var verkliga fel. Men körningen hade en allvarlig brist:
**granskaren nådde aldrig svenska.se.** WebFetch mot svenska.se returnerar ett
tomt skal — sidan är JS-renderad — så granskaren dömde på **SAOB från 1933**
plus synonymer.se.

Följden blev ett felaktigt underkännande av `ingenium`: granskaren menade att
ordet var för snävt beskrivet, men SO ger '(**skapande**) begåvning' där SAOB
bara har den äldre, vidare betydelsen. Granskaren hade rätt utifrån vad den
kunde se, och fel utifrån vad som finns.

**Därför får du verktyget den saknade.** Kör:

```
cd anki-ord
python slaupp.py --kompakt <ord1> <ord2> ...
```

Det hämtar **SO, SAOL och SAOB** (via svenska.se:s API — inte webbsidan, så
inget tomt skal), **synonymer.se** och **Wiktionary** för varje ord, i ett
anrop, och skriver ett kompakt sammandrag med definitioner, exempel,
JFR-hänvisningar och etymologi.

Fullständiga svar sparas i `uppslag/<ord>.json` om du vill läsa exakt vad
källan sa i stället för sammandraget.

**Filtrera aldrig utdatan genom `sed`, `head` eller `tail`.** Skriptet skriver
en bevisrad per hämtning (`SVENSKA_SE_HAMTAD <ord> HTTP 200 <byte>`) som måste
nå transkriptet intakt. Behöver du spara utrymme, använd `--tyst` — då tiger
skriptet om innehållet men aldrig om bevisen.

## Källhierarki

- **SO och SAOL (2026)** avgör vilka betydelser som lever i dag.
- **SAOB (tidigt 1900-tal)** används bara för djup, citat och etymologi. En
  betydelse som bara SAOB har är oftast utdöd och hör inte hemma på kortet.
- **synonymer.se** ska läsas, inte kopieras — sajten blandar redaktionellt
  material med crowdsourcade bidrag av växlande kvalitet.
- **Wiktionary** är tunn på svenska men en oberoende tredje röst.
- Räcker de inte: gör en **vanlig webbsökning**.

**Idiom går inte att slå upp direkt på svenska.se** — den tar bara enstaka
uppslagsord. Slå upp **grundordet** i stället: `ett kok stryk` finns i SO:s
artikel för **kok**, `av hävd` under **hävd**.

## Vad du ska bedöma, per kort

1. Är **huvudbetydelsen** riktig — och **saknas någon betydelse** som SO har?
   Det här är den vanligaste bristen. Leta särskilt efter bildliga bruk och
   fackbetydelser.
2. Är varje **synonym** ett ord som HP:s ORD-delprov skulle kunna ge som rätt
   svar — alltså det vanligaste ordet som ligger NÄRMAST i betydelse — och
   står den i en källa?

   ⚠️ **Kravet är INTE längre "utbytbar åt båda hållen" (ändrat 2026-08-29,
   Adams beslut om vad fältet är till för).** ORD-uppgiften går ut på att
   *"välja vilket av fem svarsalternativ som betyder samma sak (eller ligger
   närmast i betydelse)"*. Ett ord som ligger nära utan att vara ett exakt
   utbyte är alltså precis vad fältet ska innehålla, och ska GODKÄNNAS.
   Under den gamla regeln underkändes `bemärkt`/framstående,
   `singulär`/säregen och `spe`/hån — alla tre står nu med TOMT synonymfält,
   vilket är sämre kort, inte bättre.

   Underkänn en synonym bara när den pekar på **fel betydelse**
   (`tertial`/kvartal — 4 månader mot 3; `jour`/vikariat — två skilda
   anställningsformer) eller **saknar källa**. Ett tomt synonymfält är
   numera en brist att anmärka på, inte ett godtagbart utfall.
3. Stämmer **registret** (formell/vardaglig/negativ osv.) med hur källorna
   märker ordet? En etikett ingen källa stöder är ett fel.
4. Visar **exempelmeningen** hur ordet faktiskt används — och beskriver den
   rätt handling? Sätt in synonymerna i meningen: fungerar de grammatiskt?
5. Är **etymologin** sann, och gör den betydelsen lättare att minnas? Trivia
   som inte hjälper minnet ska bort. Etymologin är valfri — ett kort utan är
   inte fel.

## Så fyller du i

Skriv `granskare` överst i filen (ditt namn — **inte** `claude`; verdikt vägrar
om granskaren har samma namn som den som skrev korten).

Per post: `verdikt` = `"godkand"` eller `"underkand"`.

**Varje `underkand` KRÄVER en `anmarkning`** som säger *vad* som är fel och
*vilken källa* som visar det. "Känns fel" duger inte.

Godkänn hellre än att underkänna på en gissning — men underkänn utan att tveka
när en källa säger något annat än kortet. Poängen med steget är att du är den
enda som kan hitta fel som den som skrev korten inte kan se.

Kör sedan:

```
python kortgranskare.py verdikt sessions/_blind_2026-08-10_urval_v3-paket.json --granskare <ditt namn>
```
