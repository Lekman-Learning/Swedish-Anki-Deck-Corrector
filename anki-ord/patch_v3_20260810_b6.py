"""Batch 6, 2026-08-10 — 19 kort (degression hanteras separat).

`degression` gav **noll träffar i alla tre källorna**, och en allmän
webbsökning gav inget som håller ordbokskvalitet heller. Kortet skrivs därför
INTE om — det rödflaggas och suspenderas enligt Adams regel 2026-08-10. Att
skriva om ett kort utan källa vore precis det Hål 0 byggdes för att stoppa.

Etymologin ger den här gången sex ord som blir självförklarande: frotté↔frottera,
rutt↔rutin, entente↔'förståelse', marinera↔marin, gruvlig↔gruva sig,
effeminerad↔feminin.
"""
import patchlib as pl

MAL = "sessions/session_2026-08-10_v3-tre-kallor-b6.json"
P = {}


def lagg(ord_, slutsats, kalla=None, **andr):
    P[ord_] = (kalla or pl.kallor(ord_), slutsats, andr)


lagg("frotté",
     "SYNONYMERNA VAR INTE SYNONYMER. Kortet hade 'öglelugg' och "
     "'handduksfrotté'. Det första är tygets EGENSKAP (SO: 'poröst bomullstyg "
     "**med öglelugg**'), det andra en sammansättning av ordet självt. Ingen "
     "av dem kan ersätta *frotté* i en mening. Etymologin är däremot precis "
     "vad kortet behövde: frotté är bildat till **frottera**, 'gnida' — tyget "
     "heter så för att man gnuggar sig med det. "
     "TVÅ KÄLLOR: synonymer.se saknar uppslaget — rödflaggas.",
     synonymer=["handduksväv", "poröst bomullstyg"],
     etymologi="Till frottera, 'gnida' — tyget man gnuggar sig torr med.")

lagg("imperium",
     "BEKRÄFTAT + ETYMOLOGI. SO: '(geografiskt vidsträckt) stormaktsvälde med "
     "ett antal underkuvade stater', och noterar att ordet numera ofta "
     "utvidgas till affärsvärlden — vilket kortet redan har. Ursprunget: latin "
     "*imperium* '**befallning**; högsta makten' — **samma ord som "
     "imperativ**, den befallande formen i grammatiken.",
     etymologi="Latin imperium 'befallning' — samma ord som imperativ.")

lagg("rutt",
     "REGISTRET SAKNAR STÖD, OCH ETYMOLOGIN ÄR ETT FYND. Kortet var märkt "
     "**vardaglig**; varken SO eller SAOL märker ordet, och SO:s exempel är "
     "sakliga ('trafikera en rutt'). Ändrat till formell. Ursprunget: "
     "franskans *route*, av latin *(via) rupta* '**uppröjd väg**' — vägen man "
     "brutit fram. **Samma ord som rutin** (den upptrampade vägen) och "
     "**ruptur** (bristning).",
     register="formell",
     etymologi="Latin via rupta, 'uppröjd väg' — samma ord som rutin, den "
               "upptrampade vägen.")

lagg("platonisk",
     "BEKRÄFTAT — OCH STAVNINGSNOTISEN ÄR VÄRDEFULL. SO ger uppslaget bara som "
     "hänvisning till *platonsk*, med exemplet 'platonisk kärlek'. Kortets "
     "parentes om att filosofibetydelsen stavas *platonsk* är alltså riktig "
     "och står i ingen ordbok så tydligt. Etymologin: efter **Platon**, vars "
     "Gästabudet beskriver kärleken till det sköna som stegvis lämnar det "
     "kroppsliga bakom sig — därav betydelsen.",
     etymologi="Efter filosofen Platon, som beskrev en kärlek som lämnar det "
               "kroppsliga bakom sig.")

lagg("cypress",
     "EN NYANS SOM FAKTISKT SÄTTER DIT FOLK. SO noterar att ordet i "
     "allmänspråket '**ofta äv. används om (vanlig) tuja**', som är det man "
     "planterar i Sverige — den äkta cypressen växer inte här. Att kalla "
     "grannens häck för cypress är alltså vardagligt men botaniskt fel, och "
     "det är just den sortens sak som kan komma på prov. Kortet saknade "
     "synonymer helt. TVÅ KÄLLOR: synonymer.se saknar uppslaget — rödflaggas.",
     huvudbetydelse="Ständigt grönt träd med fjällika barr, typiskt för "
                    "Medelhavet — i Sverige kallas ofta tujan felaktigt så",
     synonymer=["medelhavscypress"],
     etymologi="Grekiska kyparissos; ursprunget bortom det är okänt.")

lagg("effeminerad",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'som liknar en kvinna', SAOL: 'förkvinnligad, "
     "förvekligad' — kortets synonymer är alltså tagna ordagrant ur SAOL. "
     "Registret **nedsättande** stöds av att SO:s enda exempel är 'en "
     "effeminerad yngling', en formulering som bara förekommer klandrande. "
     "Ursprunget: latin *femina* 'kvinna' — **samma ord som feminin**.",
     etymologi="Latin femina 'kvinna' — samma ord som feminin.")

lagg("blaskig",
     "BEKRÄFTAT, TRE BETYDELSER STÄMMER. SO ger exakt kortets tre: 'urvattnad "
     "smak', 'intetsägande' (om färger) och 'som kännetecknas av blöta' (om "
     "väder). Det är ovanligt att ett kort träffar alla tre. SO ger ingen "
     "etymologi, men ordet hör till **blask** — slask, blöta — vilket "
     "förklarar varför väderbetydelsen finns.",
     etymologi="Till blask, 'slask' — därav både den vattniga smaken och "
               "vädret.")

lagg("fadd",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'som har ointressant (och ofta oangenäm) "
     "smak', och 'äv. bildligt i uttryck för olustkänslor' — SO:s exempel "
     "'pjäsen lämnar en **fadd eftersmak**' visar den bildliga användningen, "
     "som kortet också har. Ursprunget: franska *fade*, av latin *fatuus* "
     "'smaklös' — samma latinska ord betyder också 'dåraktig'.",
     etymologi="Latin fatuus 'smaklös' — samma ord betydde också 'dåraktig'.")

lagg("mikrofiche",
     "BEKRÄFTAT + ETYMOLOGI. SO: '(genomskinligt) kort med mycket stor mängd "
     "information i form av kraftigt förminskade tecken', SYN **mikrokort**. "
     "Kortets skillnad mot mikrofilm ('ett ark, inte en rulle') står inte i "
     "SO men följer av att SO säger *kort* och SAOL *stycke film*. "
     "Etymologin: mikro- + franska *fiche* '**notislapp**' — alltså en "
     "pytteliten lapp. TVÅ KÄLLOR: Wiktionary saknar uppslaget — rödflaggas.",
     etymologi="mikro- + franska fiche 'notislapp' — en pytteliten lapp.")

lagg("kalorimeter",
     "BEKRÄFTAT, INGEN ÄNDRING. SO och SAOL ger samma: 'apparat för mätning "
     "av värmemängder'. Kortets definition är mer användbar än båda, eftersom "
     "den säger VAD man mäter värmen på (en reaktion). Belagt sedan 1798. "
     "Ordet behöver ingen etymologi utöver sina egna delar: kalori + meter. "
     "TVÅ KÄLLOR: synonymer.se saknar uppslaget — rödflaggas.",
     etymologi="kalori + -meter — mätaren för värmemängd.")

lagg("vokabulär",
     "BEKRÄFTAT + ETYMOLOGI. SO ger kortets båda betydelser: språkets "
     "ordförråd och en enskild persons. SO:s exempel visar den andra tydligt: "
     "'ord som \"förty\" ingick i hans vokabulär'. Ursprunget: franska "
     "*vocabulaire*, till **vokabel** — ett enskilt ord i en ordlista.",
     etymologi="Franska vocabulaire, till vokabel — ett enskilt ord.")

lagg("entente",
     "ETYMOLOGIN ÄR HELA ORDET. SO: '(avtal om) vänskapsförbindelse mellan "
     "stater'. Ursprunget är franskans *entente*, till *entendre* '**höra, "
     "förstå**' — en entente är alltså ordagrant en **förståelse** mellan "
     "parter, inte ett bindande förbund. Det förklarar varför SO skriver "
     "'vänskapsförbindelse' och inte 'allians', och varför den historiska "
     "*entente cordiale* heter 'hjärtligt samförstånd'. Kortets synonym "
     "'pakt' är därför något för stark och stryks.",
     synonymer=["samförstånd", "överenskommelse", "statsförbund"],
     etymologi="Franska entendre 'förstå' — en entente är en förståelse, "
               "inte ett bindande förbund.")

lagg("ekvivalent",
     "BEKRÄFTAT + ETYMOLOGI. SO ger både adjektivet ('likvärdig') och "
     "substantivet ('fullgod motsvarighet') — kortet har båda. SO:s exempel "
     "ur fysiken ('värme och mekaniskt arbete är ekvivalenta') och kemin ('en "
     "atom klor är ekvivalent med en atom väte') visar att ordet är "
     "vetenskapligt, inte bara juridiskt. Ursprunget: latin *aequus* 'lika' + "
     "*valere* 'gälla, vara värd' — **samma valere som i valör och valid**.",
     etymologi="Latin aequus 'lika' + valere 'vara värd' — samma valere som i "
               "valör.")

lagg("allegat",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'handling eller kvitto som bekräftar "
     "ekonomisk transaktion', SAOL: 'bilaga, verifikation' — kortets båda "
     "synonymer är belagda. SO:s exempel ('revisorerna efterlyste vissa "
     "allegat') visar att ordet lever i revision. Ursprunget: latin *allegare* "
     "'**åberopa**' — ett allegat är det man åberopar som stöd.",
     etymologi="Latin allegare 'åberopa' — det man åberopar som stöd.")

lagg("gruvlig",
     "ETYMOLOGIN GÖR ORDET HÄRLEDBART, OCH EN ANVÄNDNING SAKNADES. SO: 'som "
     "orsakar fasa och oro'. Men SO lägger till att ordet **i adverbiell "
     "användning är allmänt förstärkande** — 'hon tog **gruvligt** miste' "
     "betyder bara 'grundligt', inte 'fasansfullt'. Den skillnaden fanns inte "
     "på kortet och är precis den sorts fälla ett prov använder. Ursprunget: "
     "till **gruva sig** — det gruvliga är det man gruvar sig för.",
     huvudbetydelse="Så hemsk att den väcker fasa ; som adverb bara "
                    "förstärkande: 'ta gruvligt miste' = ta grundligt miste",
     etymologi="Till gruva sig — det man gruvar sig för.")

lagg("marinera",
     "BEKRÄFTAT + EN ETYMOLOGI SOM ÄR VÄRD HELA KORTET. SO: 'lägga i "
     "marinad'. Ursprunget: franska *mariner*, till **marin** — marinaden var "
     "från början **saltlake, alltså havsvatten**. Att marinera är ordagrant "
     "att lägga något i 'havet'. Kortets synonym 'lägga i lag' är riktig men "
     "ensam; utökad. TVÅ KÄLLOR: synonymer.se saknar uppslaget — rödflaggas.",
     synonymer=["lägga i lag", "lägga in"],
     etymologi="Till marin — marinaden var från början saltlake, havsvatten.")

lagg("hybris",
     "ETT TILLÄGG SOM KÄLLORNA INTE HAR. Kortet sa 'självöverskattning **som "
     "leder till fall**'. SO säger bara 'starkt överdriven uppskattning av "
     "det egna jaget och den egna förmågan'; SAOL 'övermod, förhävelse'. "
     "Fallet är den grekiska tragedins konvention, inte ordets betydelse — "
     "man kan ha hybris utan att falla. SO:s exempel antyder visserligen "
     "följden ('greps spelarna av hybris och **det straffade sig**'), så "
     "sambandet nämns, men som vanlig följd i stället för som del av "
     "definitionen.",
     huvudbetydelse="Kraftig överskattning av sig själv och sin egen förmåga "
                    "— straffar sig ofta, men behöver inte göra det",
     etymologi="Grekiska hybris, med samma betydelse — övermodet som utmanar "
               "gudarna.")

lagg("anblick",
     "BEKRÄFTAT + EN NYANS. SO ger 'synintryck vid betraktande' och även "
     "'**ögonkast**' — den andra syns i kortets egen exempelmening ('vid "
     "första anblicken'), där ordet betyder en snabb blick snarare än det man "
     "ser. Skillnaden skrivs ut. Ursprunget: tyska *Anblick*, till **blick**. "
     "TVÅ KÄLLOR: Wiktionary strypte anropet — rödflaggas för omprövning.",
     huvudbetydelse="Det man ser när man tittar på något ; i 'vid första "
                    "anblicken': den snabba första blicken",
     etymologi="Tyska Anblick, till blick.")

lagg("märla",
     "BEKRÄFTAT, TRE BETYDELSER STÄMMER. SO ger U-haken, hyskan och "
     "förstärkningsringen — kortet har alla tre. SO har dessutom **verbet** "
     "'fästa med märla' ('märla fast en kabel i marken'), som kortet saknar "
     "men som är samma ord i annan ordklass. SAOL nämner också ett kräftdjur "
     "vid namn märla; det är ett annat ord och tas inte med. "
     "TVÅ KÄLLOR: Wiktionary strypte anropet — rödflaggas för omprövning.",
     huvudbetydelse="U-formad metallhake att fästa med ; hyska på plagg ; "
                    "liten metallring som förstärker ett hål — även som verb: "
                    "märla fast något",
     etymologi="Fornsvenska märla; verbet av nederländska marlen 'surra, "
               "förtöja'.")


if __name__ == "__main__":
    pl.bygg(P, MAL)
