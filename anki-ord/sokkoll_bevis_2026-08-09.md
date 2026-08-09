# Sökkoll 2026-08-09 — omgörning av de 130 obelagda korten

Varje rad är en faktisk hämtning. URL:erna ligger i Claude Codes transkript och är
därmed maskinellt kontrollerbara av `sokkoll_verifiering.py`.

**Metod (skärpt av Adam 2026-08-09, efter att första omgången mätts):**

1. **Tre källor är ett MINIMUM, inte ett tak.** SAOB + synonymer.se + Wiktionary på
   varje ord. Räcker de inte för att avgöra frågan — sök vidare, fri webbsökning
   inkluderad. Första omgången körde två källor som kostnadsbeslut; `bonitet` visade
   varför det inte duger, betydelsen "kreditvärdighet" fanns bara i tredje källan.
2. **Uppslagningen ska gälla ORDET SJÄLVT.** Sju kort i första omgången hade bara den
   *borttagna synonymen* uppslagen — kortets eget innehåll stod fortfarande utan
   källa. Att slå upp ett ord man tänker radera är inte en sökkoll av kortet.
3. **SAOB och svenska.se tar bara enstaka uppslagsord.** Idiom och flerordsuttryck går
   inte att slå upp där — de ska sökas på synonymer.se, Wiktionary och fri webb.
   `lägga sordin på` är fallet som visade det; grundordet `sordin` bär beläggen.
4. **Går ordet inte att belägga: rödflagga kortet och gå vidare.** Ett kort utan källa
   ska märkas ut och tas upp senare, inte skrivas på förtroende. Rätta först det som
   går att rätta väl.

Ett antagande som sprack: jag hade struntat i att söka `slapstick` i SAOB för att
ordet "är för modernt". **SAOB har det.** Antaganden om vad en källa innehåller är
samma sorts påstående som antaganden om vad ett ord betyder — de ska mätas.

## Två begränsningar i SAOB:s `?seek=`, upptäckta under körningen

1. **Sammansättningar landar ibland på grundordet.** `?seek=blindskrift` gav artikeln
   BLIND med 13 betydelser — inte blindskrift. Träff på grundordet är alltså INTE
   belägg för sammansättningen.
2. **Ibland returneras en sökträfflista i stället för artikeln.** `?seek=förhala` gav
   en länklista ("förhala v. 1"), inte texten. Då duger SAOB inte som källa för det
   ordet och synonymer.se/Wiktionary får bära.

Båda är fall där en slarvig läsning hade gett ett falskt "belagt". De ska räknas som
misslyckad hämtning, inte som källa.

## Grupp A — de åtta påståendena "ordet finns inte"

Alla åtta gjordes 2026-08-09 utan uppslagning. Nu kontrollerade mot två källor var.

| Ord | SAOB | synonymer.se | Utfall |
|---|---|---|---|
| **hävdaforskare** | **JA** — "person som forskar i hävderna; historieforskare, historiker" (belägg 1813) | JA | **Påståendet var FALSKT** |
| **bortskämmande** | **JA** — "BORTSKÄMMANDE, sbst., se bortskämma, v." | NEJ | **Påståendet var FALSKT** |
| boköppning | NEJ (föreslår bomöppning, bokning) | NEJ (broöppning, botövning) | Håller |
| habegärlig | NEJ (föreslår högbegärlig, halvårlig) | NEJ (hanegället, haverering) | Håller |
| initialera | NEJ (föreslår instillera, installera, inhalera) | NEJ (installera, initialord) | Håller |
| brunton | NEJ (föreslår basunton, brunt, bruten) | NEJ (runtom, grundton, brandtorn) | Håller |
| öppningsvisning | NEJ | NEJ | Håller |
| misskastning | NEJ | NEJ | Håller |

**Konsekvensen av de två felen är mindre än den ser ut — men skälet måste rättas.**
Båda gällde synonymer jag *tog bort*, inte kortens uppslagsord:

- `hävdatecknare`: jag tog bort *hävdaforskare* med motiveringen att ordet inte finns.
  Det finns. Men borttagningen var ändå rätt av ett annat skäl: en **forskare** forskar
  i hävderna, en **tecknare** skriver ned dem. SAOB:s egen definition visar att de inte
  är utbytbara. Kortet ändras inte; motiveringen ändras.
- `dalt`: jag tog bort *bortskämmande* på samma grund. SAOB har formen, men **bara som
  korshänvisning till verbet** — ingen egen betydelse, och varken synonymer.se eller
  Wiktionary känner den. Som synonym till *dalt* är den inte brukbar. Samma sak: rätt
  handling, falskt skäl.

Detta är precis den distinktion Hål 0 finns för. Ett kort kan vara rätt medan
motiveringen bakom det är påhittad, och utan källa går de två inte att skilja åt.

## En tredje fälla, hittad vid tillämpningen

`synonym_groups` (synonymer per betydelse) **vinner över** `synonymer` när båda
finns. På `bilateral` och `bonitet` slog alltså mina källbelagda synonymlistor inte
igenom fullt ut. Följden: `bonitet` bär fortfarande *bördighet*, som ingen av de tre
källorna gav. En patch som bara sätter `synonymer` är tyst verkningslös på kort som
har grupper — den skriver utan att ändra.

## Grupp B — de 97 innehållsändrade korten

| Ord | SAOB | synonymer.se | Följd för kortet |
|---|---|---|---|
| beprövad | endast korshänvisning ("bepröfvad, se bepröfva") | "som prövats och visat sig bra"; tillförlitlig, pålitlig, erfaren, van, härdad, befunnen god | Borttagningen av *bevisad* bekräftad — finns inte i någon källa |
| bilateral | (1) tvåsidig/symmetrisk, fackspråk (2) ömsesidigt förpliktande, juridik (3) fonetiskt: ljud på båda sidor av tungan | tvåsidig, ömsesidig, ömsesidigt förpliktigande; motsats unilateral/multilateral | Tillägget av den medicinska/dubbelsidiga betydelsen bekräftat av SAOB (1). Borttagningen av *parvis* bekräftad. SAOB har en **tredje**, fonetisk betydelse som kortet saknar — för specialiserad för HP |
| blindskrift | ✗ `?seek=` landade på grundordet BLIND | punktskrift, brailleskrift | SAOB duger inte som källa här; synonymer.se bär |
| depreciera | (1) om valuta/mynt: sjunka i värde under det nominella | devalvera, nedvärdera, nedskriva, skriva ned; motsats appreciera | **Löser cirkulariteten.** Kortet definierade *depreciera* som "minska i värde" och gav samma sak som synonym. Belagda, icke-cirkulära synonymer finns nu |
| fonetik | (1) äldre: verslärans rimavsnitt (Almqvist 1840) (2) läran om språkljuden, akustiskt/anatomiskt/fysiologiskt | ljudlära, läran om språkljuden, fonologi | Borttagningen av *språkvetenskap* bekräftad (för brett). **Lägg INTE till synonymer.se:s "fonologi"** — det är en angränsande disciplin, inte en synonym |
| förhala | ✗ `?seek=` gav träfflista, inte artikel | (1) dra ut på, fördröja, uppskjuta, försena, sinka, obstruera (2) **sjöterm: förflytta fartyg med trossar, varpa, bogsera** | Sjötermen är en andra betydelse kortet saknar — och den är ordets ursprung (lågtyska/nederländska *verhalen*) |
| glyptotek | (1) museum med skulptursamling | skulpturmuseum, skulptursamling | Enbetydelseord, bekräftat |
| konstitutiv | (1) konstitutionell, som rör författning (2) grundläggande, väsentlig, konstituerande | grundläggande, bestämmande, väsentlig, författnings- | Två betydelser — kontrollera att kortet har båda |
