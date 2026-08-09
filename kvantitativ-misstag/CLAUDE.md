# Kvantitativ-misstag — Adams misstagsmönster (XYZ/KVA/NOG/DTK)

Detta dokument är levande minne för misstagsanalys av Adams kvantitativa HP-prov.
Uppdateras i slutet av varje genomgången provsession (se `sessions/`). Håll
det kurerat och kortfattat — syntetiserade mönster, inte en rå logg av varje
enskilt fel.

Verbal HP hanteras INTE här — se [../verbal-misstag/CLAUDE.md](../verbal-misstag/CLAUDE.md)
(System B), separat spår, samma metod.

## Mål — Hösten 2026

Satt av Adam 2026-08-07. **Mål: 2.0.** **Lägsta godtagbara: 1.8.**

**Läget nu (12 genomgångna provpass, normerat resultat per provpass):**
1.9, 1.7, 1.7, 1.6, 1.5, 1.5, 1.4, 1.4, 1.4, 1.3, 1.3, 1.2 — se Sessionshistorik
för vilket prov som gav vilket. **1 av 12 (1.9) når lägstanivån 1.8. 0 av 12 når
målet 2.0.** Bästa resultatet (1.9, Våren 2022 Första provet pp5) är samtidigt
den ENDA sessionen som når godkänt — och det var den allra första loggade.
Medel över alla 12: ~1.5. Gapet till lägstanivån är omkring 0.3, till målet 0.5.

## Arbetsflöde (körs varje session i denna mapp)

1. Adam lägger provet + facit i `prov/`, eller berättar i chatten vilka
   frågor som blev fel.
2. Jämför Adams svar mot facit, identifiera fel per fråga och delmoment.
3. Stäm av mot mönstren nedan — är detta en upprepning av en känd svaghet,
   eller något nytt?
4. Kommentera varje misstag: varför det blev fel — räknefel, feltolkad fråga,
   fel metod vald, tidsbrist, eller ett genuint kunskapslucka. Skilj DESSA åt,
   det avgör vad som faktiskt behöver tränas (en räknefel-slarv löses inte av
   att repetera en formel).
5. Uppdatera mönstren nedan: förstärk kända, lägg till nya, notera om ett
   tidigare svagt område nu gick bra (ta bort/nedgradera om löst — peka inte
   ut samma sak för evigt).

## Letter-gissning — TESTAD OCH AVSKRIVEN (2026-08-07)

Ursprungshypotesen ("gissar D vid osäkerhet") byggde på 1 session (3/3 fel = D).
Efter 12 genomgångna kvantitativa provpass (119 feltillfällen totalt) höll den
INTE: **B 34, D 32, C 24, A 24, E 5**. Spridningen är i praktiken jämn över
A–D — E är sällsynt bara för att färre frågor (i praktiken bara NOG) har en
E-option. Ingen bokstavsbias att träna bort. Skrivet av här så det inte
återuppstår som fråga nästa gång ett litet urval råkar peka åt samma håll.

## Träffsäkerhet per delmoment (12 provpass, 2026-08-07)

Räknat över Våren 2022 (Första, provpass 3+5), Hösten 2020 (provpass 3+5),
Hösten 2015 (provpass 3+5), Våren 2015 (provpass 2×2, 4×2 — se öppen fråga om
dubbletterna nedan), Våren 2012 (provpass 3+5).

| Delmoment | Rätt/Totalt | Andel |
|---|---|---|
| XYZ — matematisk problemlösning | 116/144 | 81 % |
| NOG — kvantitativa resonemang | 56/72 | 78 % |
| KVA — kvantitativa jämförelser | 86/120 | 72 % |
| DTK — diagram, tabeller och kartor | 103/144 | 72 % |

(Omräknat programmatiskt 2026-08-07 direkt från fråga-för-fråga-data i
`sessions/` — rättar en manuell avrundningsmiss på XYZ/KVA i första utkastet.)

**DTK och KVA är svagast**, inte XYZ som första sessionen (37/40, nästan
perfekt) antydde. Det gamla antagandet att matte-problemlösning är svagast
höll alltså inte heller — dra inte den slutsatsen av en enda stark session.

Viktig begränsning: detta är poäng- och bokstavsdata från sparade rättningssidor,
inte frågetext eller förklaringar (de laddas via JS som en statisk sida inte
fångar). Så mönstret säger VILKA delmoment som är svaga, inte VARFÖR
(räknefel vs. feltolkning vs. metodval vs. tidsbrist) — den skillnaden kräver
att Adam själv kommenterar varje fel, eller att förklaringssidan klipps separat.

## Öppen fråga — dubbla "provpass 2" och "provpass 4" för Våren 2015

Fyra sparade rättningssidor säger alla "Våren 2015", men två par delar samma
provpass-nummer med OLIKA innehåll (olika fel-frågor, olika facit):

- Provpass 2: id 1181534 (7 fel) och id 1080691 (7 fel) — delar 3 av 7 fel
  (fråga 19, 22, 28) men skiljer sig på resten. Om det vore samma prov skulle
  alla fel matcha.
- Provpass 4: id 1183412 (10 fel) och id 1083180 (9 fel) — helt olika felmönster.

Rimlig gissning: hpguiden.se återanvänder provpass-numret för flera olika
verkliga provtillfällen under samma säsongsetikett (t.ex. "Våren 2015" kan
dölja fler än en faktisk provomgång), men det är en gissning — inte
verifierat. Fråga Adam: kommer han ihåg att ha gjort samma provpass två
gånger, eller är det två olika prov som råkat hamna under samma säsong?

## Provkalender 2014–2026

26 sittningar, källa: UHR/studera.nu (fritt tillgängliga, inte hpguiden VIP).
Samma kalender som `../verbal-misstag/CLAUDE.md` — varje sittning ger både
ett kvantitativt och ett verbalt provpass. Bocka av i takt med att provet
laddas ner respektive faktiskt genomförs (logga det senare i
Sessionshistorik nedan).

| Prov | Nedladdat | Genomfört |
|---|---|---|
| Våren 2026 | ☐ | ☐ |
| Hösten 2025 | ☐ | ☐ |
| Våren 2025 | ☐ | ☐ |
| Hösten 2024 | ☐ | ☐ |
| Våren 2024 | ☐ | ☐ |
| Hösten 2023 | ☐ | ☐ |
| Våren 2023 | ☐ | ☐ |
| Hösten 2022 | ☐ | ☐ |
| Våren 2022 (Andra provet) | ☐ | ☐ |
| Våren 2022 (Första provet) | ☑ | ☑ |
| Hösten 2021 | ☐ | ☐ |
| Våren 2021 (Andra provet) | ☐ | ☐ |
| Våren 2021 (Första provet) | ☐ | ☐ |
| Hösten 2020 | ☑ | ☑ |
| Hösten 2019 | ☐ | ☐ |
| Våren 2019 | ☐ | ☐ |
| Hösten 2018 | ☐ | ☐ |
| Våren 2018 | ☐ | ☐ |
| Hösten 2017 | ☐ | ☐ |
| Våren 2017 | ☐ | ☐ |
| Hösten 2016 | ☐ | ☐ |
| Våren 2016 | ☐ | ☐ |
| Hösten 2015 | ☑ | ☑ |
| Våren 2015 | ☑ | ☑ |
| Hösten 2014 | ☐ | ☐ |
| Våren 2014 | ☐ | ☐ |

*(Våren 2020 inställt pga corona — ingår inte i kalendern.)*

**Öppen fråga:** två genomgångna provpass (id 1046335, 1051015) är märkta
"Våren 2012" — utanför kalenderns deklarerade 2014–2026-fönster (26 sittningar
från UHR/studera.nu). Loggat i Sessionshistorik ändå eftersom det är verklig
data, men Våren 2012 saknar egen rad ovan tills det är klart om den hör hemma
i kalendern eller kom från en annan källa (hpguidens betalarkiv går längre
tillbaka än den fria kalendern).

Full fråga-för-fråga-data för varje rad finns i `sessions/` (en fil per provpass).

## Sessionshistorik

| Datum | Prov | Delmoment | Antal fel | Resultat | Mål? | Nya/förstärkta mönster |
|-------|------|-----------|-----------|----------|------|-------------------------|
| 2026-08-07 | Våren 2022, Första provet (provpass 5) | XYZ 10/12, KVA 10/10, NOG 5/6, DTK 12/12 | 3/40 | **1.9** | Når lägstanivån (1.8) | Ursprunget till D-gissningshypotesen — se nedan, avskriven. |
| 2026-08-07 | Våren 2022, Första provet (provpass 3) | XYZ 12/12, KVA 7/10, NOG 4/6, DTK 7/12 | 10/40 | 1.3 | Under lägstanivån | — |
| 2026-08-07 | Hösten 2020 (provpass 5) | XYZ 11/12, KVA 7/10, NOG 6/6, DTK 9/12 | 7/40 | 1.5 | Under lägstanivån | — |
| 2026-08-07 | Hösten 2020 (provpass 3) | XYZ 9/12, KVA 9/10, NOG 6/6, DTK 5/12 | 11/40 | 1.3 | Under lägstanivån | DTK 5/12 — svagaste enskilda delmoment i hela urvalet. |
| 2026-08-07 | Hösten 2015 (provpass 3) | XYZ 12/12, KVA 6/10, NOG 4/6, DTK 7/12 | 11/40 | 1.4 | Under lägstanivån | — |
| 2026-08-07 | Hösten 2015 (provpass 5) | XYZ 8/12, KVA 7/10, NOG 6/6, DTK 8/12 | 11/40 | 1.4 | Under lägstanivån | — |
| 2026-08-07 | Våren 2015 (provpass 2, id 1181534) | XYZ 10/12, KVA 8/10, NOG 5/6, DTK 10/12 | 7/40 | 1.7 | Under lägstanivån (nära) | Se öppen fråga: dubblett-provpass-nummer. |
| 2026-08-07 | Våren 2015 (provpass 2, id 1080691) | XYZ 11/12, KVA 7/10, NOG 5/6, DTK 10/12 | 7/40 | 1.7 | Under lägstanivån (nära) | Delar 3 fel (frå 19, 22, 28) med föregående rad trots olika facit totalt — se öppen fråga. |
| 2026-08-07 | Våren 2015 (provpass 4, id 1183412) | XYZ 9/12, KVA 8/10, NOG 4/6, DTK 9/12 | 10/40 | 1.5 | Under lägstanivån | Se öppen fråga: dubblett-provpass-nummer. |
| 2026-08-07 | Våren 2015 (provpass 4, id 1083180) | XYZ 11/12, KVA 6/10, NOG 3/6, DTK 11/12 | 9/40 | 1.6 | Under lägstanivån | NOG 3/6 — svagaste NOG-resultat i urvalet. |
| 2026-08-07 | Våren 2012 (provpass 3) — utanför kalenderfönstret | XYZ 8/12, KVA 6/10, NOG 4/6, DTK 7/12 | 15/40 | 1.4 | Under lägstanivån | Klart svagare än 2015/2020/2022-sessionerna. |
| 2026-08-07 | Våren 2012 (provpass 5) — utanför kalenderfönstret | XYZ 5/12, KVA 5/10, NOG 4/6, DTK 8/12 | 18/40 | 1.2 | Under lägstanivån | Svagaste sessionen totalt (22/40). XYZ 5/12 bryter mot att XYZ annars är starkast. |
