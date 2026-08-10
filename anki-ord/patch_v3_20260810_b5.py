"""Batch 5, 2026-08-10 — 20 kort.

Två riktiga innehållsfel: `försigkommen` var märkt **positiv** trots att SO:s
eget exempel är negativt, och `gourmand` saknade den halva av betydelsen som
gör ordet värt att kunna — gränsdragningen mot *gourmet*.

Etymologin ger fem par den här gången: djäkne↔diakon, tabernakel↔taverna,
exkludera↔kloster, girig↔begära, eolisk↔Aiolos.
"""
import patchlib as pl

MAL = "sessions/session_2026-08-10_v3-tre-kallor-b5.json"
P = {}


def lagg(ord_, slutsats, kalla=None, **andr):
    P[ord_] = (kalla or pl.kallor(ord_), slutsats, andr)


lagg("girig",
     "BEKRÄFTAT + ETYMOLOGI. SO ger kortets två bruk: 'alltför starkt "
     "inriktad på att äga' och 'ivrig att få' ('giriga blickar mot "
     "smörgåsbordet'). Belagt sedan 1200-talet. Ursprunget knyter ihop ordet "
     "med två vardagsord: girig hör till fornsvenskans *giri* 'begär' och är "
     "besläktat med **begära** och **gärna**.",
     etymologi="Till giri 'begär' — besläktat med begära och gärna.")

lagg("åma",
     "BEKRÄFTAT, OCH URSPRUNGET SKRIVS UT SOM OKÄNT. SO: 'göra sig till', "
     "SAOL: 'åbäka sig, sjåpa sig'. Kortet stämmer. SO säger uttryckligen att "
     "ordet är av **ovisst ursprung** — det skrivs ut i stället för att "
     "lämnas tomt, eftersom 'ingen etymologi' och 'etymologin är okänd' är "
     "två olika besked. SO:s exempel är dessutom mer träffande än kortets: "
     "'pojkbandet stod och åmade sig på scen'.",
     etymologi="Av ovisst ursprung — SO vet inte varifrån ordet kommer.")

lagg("eolisk",
     "ETYMOLOGIN ÄR ETT NAMN. SO: 'som har att göra med vinden', med exemplet "
     "'eoliska avlagringar'. Kortet stämmer. Ordet kommer av **Aiolos**, "
     "vindarnas gud i grekisk mytologi — samma gud som i Odysséen ger "
     "Odysseus en säck med vindar. Kortet saknade synonymer helt; Wiktionary "
     "ger den konkreta innebörden 'lössjord och flygsand'. "
     "TVÅ KÄLLOR: synonymer.se saknar uppslaget — rödflaggas.",
     synonymer=["vindburen", "vindavlagrad"],
     etymologi="Efter Aiolos, vindarnas gud i grekisk myt.")

lagg("djäkne",
     "ETYMOLOGIN ÄR OVÄNTAD OCH BINDER IHOP TVÅ ORD. SO: 'elev i äldre typ av "
     "läroverk'. Kortet stämmer, och dess exempelmening om tiggande djäknar "
     "bekräftas av SO: 'många av djäknarna fick försörja sig på att tigga'. "
     "Ursprunget: fornsvenska *diäkne*, ur grekiskans *diakonos* '**tjänare**' "
     "— **samma ord som diakon**. Skoleleven och kyrkotjänaren är alltså "
     "samma ord, vilket är logiskt: skolorna var kyrkans.",
     etymologi="Ur grekiskans diakonos 'tjänare' — samma ord som diakon. "
               "Skolorna var kyrkans.")

lagg("salongsfähig",
     "BEKRÄFTAT + EN NYANS. SO: 'som passar för finare salonger', men lägger "
     "till att ordet **ofta används försvagat** om beteende som helt enkelt "
     "inte är olämpligt — alltså inte bara om det fina, utan om det "
     "godtagbara. JFR **rumsren**, som kortet redan har. Etymologin: tyska "
     "*salonfähig*, där *fähig* betyder 'i stånd till'.",
     huvudbetydelse="Passande att visa upp i finare kretsar ; ofta svagare: "
                    "helt enkelt inte olämpligt",
     etymologi="Tyska salonfähig — fähig betyder 'i stånd till'.")

lagg("avbörda sig",
     "BEKRÄFTAT. SAOL: 'göra sig fri från'. SO saknar uppslaget som eget "
     "lemma. synonymer.se ger 'lätta sitt samvete, göra sig kvitt, befria sig "
     "från' — vilket bekräftar kortets 'något tungt, oftast ett ansvar'. "
     "Etymologin är genomskinlig: av + börda. TVÅ KÄLLOR: Wiktionary saknar "
     "uttrycket — rödflaggas.",
     synonymer=["göra sig fri från", "lämna ifrån sig", "lätta sitt samvete"],
     etymologi="av + börda — att lägga av sig en börda.")

lagg("försigkommen",
     "REGISTRET VAR FEL ÅT FEL HÅLL. Kortet var märkt '**positiv**'. SO säger "
     "uttryckligen att ordet finns 'äv. med bibetydelse av att vara **alltför** "
     "avancerad', och SO:s andra exempel är entydigt negativt: 'de mest "
     "försigkomna eleverna hade redan börjat röka'. Ordet bär alltså en "
     "dubbelhet som kortet stängde av. Etymologin: bildat till **komma sig "
     "för** 'komma igång'. Belagt sedan 1534.",
     register="litterär",
     huvudbetydelse="Mer mogen än åldern medger — ibland beundrande, ibland "
                    "om någon som gått för fort fram",
     etymologi="Bildat till komma sig för, 'komma igång'.")

lagg("tabernakel",
     "BEKRÄFTAT + EN ETYMOLOGI SOM ÄR SVÅR ATT TRO. Kortets tre betydelser "
     "stämmer mot SO och SAOL. Ursprunget är latinets *tabernaculum* "
     "'**tält**', diminutiv till *taberna* 'bod' — **samma ord som taverna**. "
     "Helgedomen och krogen delar alltså ord, och det förklarar varför den "
     "första betydelsen är ett TÄLT.",
     etymologi="Latin tabernaculum 'tält', till taberna 'bod' — samma ord som "
               "taverna.")

lagg("gourmand",
     "HALVA BETYDELSEN SAKNADES, OCH DET ÄR DEN SOM TESTAS. Kortet sa bara "
     "'person som äter stora mängder mat'. SO: 'person som gärna äter **mycket "
     "(och god)** mat', SAOL: '**storätare och finsmakare**'. Poängen med "
     "ordet är just gränsdragningen mot **gourmet**, som SO har under JFR: "
     "gourmeten söker kvalitet, gourmanden både kvalitet och mängd. Utan den "
     "kontrasten är kortet bara ett svårt ord för storätare.",
     huvudbetydelse="Person som äter både mycket och gott — till skillnad "
                    "från en gourmet, som söker kvaliteten allena",
     synonymer=["storätare", "frossare", "läckergom"],
     etymologi="Franska gourmand, till gourmet.")

lagg("skrymma",
     "BEKRÄFTAT — MEN REGISTRET SAKNAR STÖD. SO: 'ta upp (onödigt) stort "
     "utrymme', SAOL detsamma, och SO:s exempel är sakliga ('skrymmande "
     "gods'). **Ingen källa märker ordet som vardagligt**, vilket kortet gör. "
     "Jag ändrar det ändå inte: kortformatet kräver minst en registeretikett, "
     "och 'formell' vore lika obelagt som 'vardaglig'. Noteras här i stället, "
     "så att felet är synligt om registervokabulären senare får ett neutralt "
     "värde. Kortets observation att ordet mest används som *skrymmande* "
     "bekräftas av att alla SO:s exempel har den formen.",
     etymologi="Från dialektalt skrymma; ursprunget är osäkert enligt SO.")

lagg("vidlyftig",
     "BEKRÄFTAT + ETYMOLOGI. SO: '(alltför) omfattande', med den särskilda "
     "betydelsen 'spec. med tanke på (fritt) sexualliv' — kortets 'om "
     "levnadssätt: utsvävande' fångar den. Ursprunget förklarar bilden: "
     "lågtyska *witlüftich*, egentligen '**som löper vida**', besläktat med "
     "**löpa**. Det vidlyftiga är det som löper iväg.",
     etymologi="Lågtyska witlüftich, 'som löper vida' — släkt med löpa.")

lagg("medaljong",
     "BEKRÄFTAT + EN ETYMOLOGI SOM GÅR EMOT MAGKÄNSLAN. Kortets tre "
     "betydelser (smycket, infattningen, köttbiten) stämmer alla mot SO. "
     "Ändelsen *-ong* låter som en förminskning, men franskans *médaillon* "
     "betyder egentligen '**stor medalj**'. En medaljong är alltså en STÖRRE "
     "medalj, inte en mindre. Kortets synonym 'amulett' finns i ingen källa — "
     "en amulett skyddar, en medaljong minns. Struken. "
     "TVÅ KÄLLOR: Wiktionary strypte anropet — rödflaggas för omprövning.",
     synonymer=["hängsmycke", "kamé"],
     etymologi="Franska médaillon, egentligen 'stor medalj' — inte en liten.")

lagg("trolsk",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'som tycks overklig och förtrollande', SAOL: "
     "'sällsam och tjusande, sagoaktig'. Kortet stämmer. Ordet hör till "
     "**troll** — det trolska är ordagrant det trollkunniga, och fornsvenskans "
     "*trolsker* betydde just 'trollkunnig'. Betydelsen har alltså mjuknat "
     "från farlig magi till vacker stämning. "
     "TVÅ KÄLLOR: Wiktionary strypte anropet — rödflaggas för omprövning.",
     etymologi="Till troll — fornsvenskans trolsker betydde 'trollkunnig'.")

lagg("imperialism",
     "PRECISERAT UR SO. Kortets 'politiken att utöva makt och kontroll över "
     "andra länder' är för vid — den beskriver lika gärna vanlig stormakts"
     "politik. SO är skarpare: 'utrikespolitik som är inriktad på behärskning "
     "av områden **(långt) utanför de egna gränserna**'. Avståndet är "
     "definierande. SO noterar också att ordet numera ofta gäller ekonomisk "
     "eller kulturell behärskning, inte bara militär — vilket är det bruk man "
     "möter i dag.",
     huvudbetydelse="Att lägga under sig områden långt utanför de egna "
                    "gränserna — numera ofta ekonomiskt eller kulturellt, "
                    "inte bara militärt",
     etymologi="Till imperium, latin för 'befallning, välde'.")

lagg("grossist",
     "BEKRÄFTAT. SO: 'person som bedriver grosshandel', med MOTSATSEN "
     "**detaljist** — precis den kontrast kortet redan bygger på. SO:s "
     "exempel visar hela kedjan: 'från fabrikantledet över grossisten till "
     "detaljisten'. Etymologin: tyska *Grossist*, till franskans *en gros* "
     "'i stort'.",
     etymologi="Till en gros, franska för 'i stort' — motsatsen till i "
               "detalj.")

lagg("exkludera",
     "BEKRÄFTAT + EN OVÄNTAD SLÄKTING. SO ger kortets två bruk och MOTSATSEN "
     "inkludera, som kortet redan har. Ursprunget är latinets *excludere* "
     "'utestänga', till *claudere* 'stänga' — **samma rot som kloster och "
     "sluss**. Ett kloster är ordagrant ett stängt rum.",
     etymologi="Latin excludere 'stänga ute', till claudere 'stänga' — samma "
               "rot som kloster.")

lagg("uttrycklig",
     "BEKRÄFTAT, INGEN ÄNDRING. SO: 'tydlig och bestämd', SAOL: 'tydligt "
     "uttryckt'. SO:s exempel ('en uttrycklig order', 'hennes uttryckliga "
     "önskan') visar att ordet nästan alltid står framför ett substantiv som "
     "betecknar en VILJEYTTRING — order, begäran, önskan, tillstånd — vilket "
     "kortets exempelmening också gör. Belagt sedan 1568. SO ger ingen "
     "etymologi; ordet är genomskinligt sammansatt.")

lagg("extraordinär",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'som går mycket utöver det vanliga', med "
     "motsatsen **ordinär** enligt synonymer.se. Ursprunget är latinets "
     "*extra ordinem* '**utanför ordningen**' — vilket är hela betydelsen "
     "packad i två ord.",
     synonymer=["enastående", "exceptionell", "utomordentlig"],
     etymologi="Latin extra ordinem, 'utanför ordningen'.")

lagg("tillstå",
     "BEKRÄFTAT — OCH MOTVILJAN STÄMMER. SO: 'erkänna riktigheten av'. "
     "Kortets tillägg '**motvilligt**' står inte i SO:s definition, men "
     "bekräftas av båda SO:s exempel: 'jag måste tillstå att jag har "
     "underskattat konkurrensen' och 'han ville inte tillstå sin "
     "överklassbakgrund'. I båda kostar erkännandet något. Tillägget "
     "behålls. Belagt sedan 1400-talets början.",
     etymologi="Fornsvenska tilstanda, efter lågtyska tostan — att stå för "
               "något.")

lagg("driftig",
     "BEKRÄFTAT, INGEN ÄNDRING. SO: 'som har förmåga att uppnå resultat', "
     "SAOL: 'företagsam, energisk', JFR företagsam och verksam — kortets "
     "synonymer är belagda. SO:s exempel ('en driftig kvinna som just har "
     "startat eget') är i praktiken kortets egen exempelmening. SO ger ingen "
     "etymologi; ordet hör till **drift** i betydelsen 'framåtanda'.",
     etymologi="Till drift i betydelsen 'framåtanda'.")


if __name__ == "__main__":
    pl.bygg(P, MAL)
