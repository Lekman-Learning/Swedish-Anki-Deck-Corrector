"""Batch 3, 2026-08-10 — 20 kort.

Batchen är den hittills tydligaste illustrationen av vad etymologin tillför:
tolv av tjugo ord får en koppling till ett ord Adam redan kan. Ett par av dem
gör ordet nästan självförklarande — `yuppie` ÄR en förkortning (young urban
professional), `glyptotek` har samma -tek som bibliotek, `avi` är latinets
'till + se'.

Två ord fick sin andra källa via allmän webbsökning, enligt Adams regel
2026-08-10 (svenska.se, synonymer.se, Wiktionary — och därefter en vanlig
sökning när de inte räcker): `grisaille` och `bekväma sig`.
"""
import patchlib as pl

MAL = "sessions/session_2026-08-10_v3-tre-kallor-b3.json"
P = {}


def lagg(ord_, slutsats, kalla=None, **andr):
    P[ord_] = (kalla or pl.kallor(ord_), slutsats, andr)


lagg("otolog",
     "BEKRÄFTAT + ETYMOLOGI + EN NYANS. SO: 'specialist på otologi'. Kortet "
     "stämmer. SO lägger till att ordet 'någon gång äv.' används om "
     "MOTTAGNINGEN: 'hon arbetar på otologen' — samma mönster som *kirurgen* "
     "eller *akuten*. Etymologin är genomskinlig och binder ihop ordet med "
     "otit, som Adam troligen känner igen: grekiska *ous* 'öra' + *logos* "
     "'lära'. TVÅ KÄLLOR: Wiktionary saknar uppslaget — rödflaggas.",
     etymologi="Grekiska ous 'öra' + logos 'lära' — samma ous som i otit.")

lagg("hävdatecknare",
     "ETYMOLOGI VIA GRUNDORDET. SO och SAOL ger båda bara 'historieskrivare'. "
     "Ordet är genomskinligt när man vet vad *hävd* betyder: 'sedvänja eller "
     "förhållande som länge varit förhärskande', bildat till **hava** — det "
     "man länge haft. En hävdatecknare tecknar alltså ned det som varit. "
     "SO:s exempel är bra och konkret: 'den romerske hävdatecknaren "
     "Plutarchos'.",
     etymologi="hävd = det man länge haft (till hava) — den som tecknar ned "
               "det som varit.")

lagg("grisaille",
     "ETYMOLOGIN ÄR ORDET SJÄLVT. SO: 'målning i olika valörer av samma gråa "
     "färgton', av franska *gris* 'grå'. Kortets tillägg 'ofta för att härma "
     "stenrelief' bekräftas av tredje källan: tekniken används i tak för att "
     "ge illusion av stuckatur, och finns på Drottningholm, Gripsholm och "
     "Skokloster. Kortets exempelmening är alltså sakligt riktig, inte "
     "påhittad. TREDJE KÄLLAN VIA ALLMÄN SÖKNING (Adams regel 2026-08-10): "
     "varken synonymer.se eller Wiktionary har uppslaget.",
     kalla=pl.kallor("grisaille") + " https://sv.wikipedia.org/wiki/Grisaillemåleri",
     etymologi="Av franskans gris, 'grå'.")

lagg("evakuera",
     "ETYMOLOGIN KOPPLAR IHOP TVÅ ORD. Kortets tre betydelser stämmer mot SO. "
     "Ursprunget gör den tekniska betydelsen begriplig i stället för "
     "godtycklig: latin *evacuare* 'göra tom', **samma rot som vakuum**. Att "
     "pumpa ut luften ur något och att tömma en stad på människor är alltså "
     "samma handling språkligt sett.",
     etymologi="Latin evacuare, 'göra tom' — samma rot som vakuum.")

lagg("bekväma sig",
     "MOTVILJAN ÄR HELA POÄNGEN, OCH DEN STOD REDAN RÄTT. SO: '(**motvilligt**) "
     "göra ansträngningar', SAOL: 'motvilligt förmå sig'. Kortet har det. "
     "ANDRA KÄLLAN HITTAD VIA ALLMÄN SÖKNING: synonymer.se har uttrycket under "
     "/sv-syn/bekväma-sig (med bindestreck) och ger 'förmå sig, gitta, nedlåta "
     "sig till, idas' — *gitta* och *idas* är utmärkta, för de bär samma "
     "motvilja. Etymologin: bekväm kommer av tyskans *bequem*, ytterst latinets "
     "*commodus* 'lämplig'. Att bekväma sig är alltså att motvilligt finna "
     "något lämpligt nog.",
     synonymer=["förmå sig till", "nedlåta sig till", "idas", "gitta"],
     etymologi="Till bekväm, av latinets commodus 'lämplig' — att motvilligt "
               "finna något lämpligt nog.")

lagg("konstitutiv",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'grundläggande', SAOL: 'grundläggande, "
     "väsentlig'. SO:s exempel 'kvickhet var en konstitutiv del av hans "
     "personlighet' visar precis kortets poäng: en del som ordet inte skulle "
     "vara sig självt utan. Ursprunget är till **konstituera** — att utgöra.",
     etymologi="Till konstituera, 'utgöra' — det som något är gjort av.")

lagg("putslustig",
     "SYNONYM UTAN BELÄGG BORTTAGEN. SO och SAOL ger båda 'smårolig, skojig', "
     "JFR skämtsam. Kortets '**tokrolig**' finns i ingen källa och är dessutom "
     "för starkt — putslustig är mild, inte tokig. SO ger ingen etymologi, men "
     "förleden är *puts* i den gamla betydelsen 'spratt, upptåg' (jfr 'spela "
     "någon ett puts'), vilket är den enda ledtråd ordet behöver.",
     synonymer=["smårolig", "skojig", "skämtsam", "lustig"],
     etymologi="Till puts i betydelsen 'spratt' — som i 'spela någon ett puts'.")

lagg("depreciera",
     "MOTSATSEN SAKNADES, OCH DEN ÄR MINNESREGELN. Kortet sa bara 'sjunka i "
     "värde'. SO ger uttryckligen MOTSATSEN **appreciera** och JFR devalvera. "
     "Ett ekonomiskt par som appreciera/depreciera är lättare att minnas som "
     "par än var för sig. Etymologin binder dessutom ordet till *pris*: latin "
     "*pretium* 'värde'.",
     huvudbetydelse="Sjunka i värde — motsatsen till appreciera",
     synonymer=["sjunka i värde", "skriva ned", "devalvera"],
     etymologi="Latin pretium 'värde' — samma rot som pris. de- = nedåt.")

lagg("terapeutisk",
     "BEKRÄFTAT, INGEN ÄNDRING. SO ger exakt kortets två betydelser: 'som har "
     "att göra med terapi' och 'som har botande eller lindrande verkan'. "
     "SO:s exempel 'samtalet verkade terapeutiskt på henne' matchar kortets "
     "egen exempelmening i form. synonymer.se ger motsatsen **preventiv** "
     "(förebyggande), vilket är den skarpaste gränsdragningen för ordet: "
     "terapeutisk botar det som redan hänt, preventiv hindrar det. SO saknar "
     "etymologi.")

lagg("glyptotek",
     "ETYMOLOGIN GÖR ORDET GENOMSKINLIGT. SO: 'museum med skulpturer'. Ordet "
     "är byggt av grekiska *glyptos* 'skulpterad' + *theke* 'förvaringsrum' — "
     "och **-tek är samma efterled som i bibliotek och diskotek**. Vet man det "
     "är ordet inte längre något att lära utantill. SO:s exempel är dessutom "
     "det Adam troligen känner igen: 'glyptoteket i Köpenhamn'.",
     etymologi="Grekiska glyptos 'skulpterad' + theke 'förvaringsrum' — samma "
               "-tek som i bibliotek.")

lagg("kontenta",
     "REGISTRET VAR FEL. Kortet märkte ordet **vardaglig**. Ingen källa gör "
     "det: SO och SAOL har det omärkt, och SO:s exempel är formella "
     "('kontentan av rapporten var att kommunens organisation måste "
     "förändras'). Ordet är belagt sedan 1655 och hör hemma i normal "
     "sakprosa — neutralt, inte vardagligt. Etymologin: latin *contentus* "
     "'sammanfattad', det som ryms i något.",
     register="formell",
     synonymer=["kärna", "sammanfattning", "slutkläm", "essens"],
     etymologi="Latin contentus, 'sammanfattad' — det som ryms i något.")

lagg("försonlig",
     "BEKRÄFTAT + MOTSATSEN. SO: 'beredd att ge efter för att åter uppnå ett "
     "vänskapligt förhållande' — kortet stämmer. synonymer.se ger motsatsen "
     "**oförsonlig**, som är värd att ha med eftersom den formen är vanligare "
     "i text än den positiva. SO noterar att ordet även används om handlingar, "
     "inte bara personer: 'en försonlig gest'. Ingen etymologi i SO.",
     huvudbetydelse="Villig att förlåta och göra upp efter en konflikt ; även "
                    "om handlingar: en försonlig gest",
     synonymer=["förlåtande", "medgörlig", "kompromissvillig"])

lagg("presumera",
     "BEKRÄFTAT + ETYMOLOGI SOM BINDER IHOP TRE ORD. SO: 'förmoda', SAOL: "
     "'förutsätta, anta'. SO:s exempel är juridiskt, precis som kortets — det "
     "är där ordet lever. Latin *praesumere* 'ta i förväg': **prae-** (före) + "
     "*sumere* (ta), samma *sumere* som i **konsumera** och **resumé**. "
     "TVÅ KÄLLOR: Wiktionary strypte anropet — rödflaggas för omprövning, inte "
     "för att ordet saknas.",
     etymologi="Latin prae- 'före' + sumere 'ta' — att ta något i förväg. "
               "Samma sumere som i konsumera.")

lagg("oktett",
     "KORTET SAKNADE SYNONYMER HELT, OCH EN BETYDELSE. SO ger tre bruk: "
     "musikstycket, musikgruppen och '**äv. om grupp med åtta personer i "
     "allmänhet**' — den tredje står inte på kortet och är den enda som gör "
     "ordet användbart utanför musiken. Etymologin: italienska *otto* 'åtta', "
     "**samma rot som oktav och oktober** (som en gång var årets åttonde "
     "månad). TVÅ KÄLLOR: Wiktionary strypte anropet — rödflaggas för "
     "omprövning.",
     huvudbetydelse="Musikstycke för åtta stämmor ; grupp om åtta — oftast "
                    "musiker, men kan vara vilken åttamannagrupp som helst",
     synonymer=["ensemble om åtta", "åttamannagrupp"],
     etymologi="Italienska otto 'åtta' — samma rot som oktav och oktober.")

lagg("yuppie",
     "ETYMOLOGIN ÄR ORDET. SAOL: 'ung välutbildad och välavlönad "
     "storstadsbo'. Ordet är en engelsk **förkortning**: *young urban "
     "professional* + -ie. Det behöver alltså inte läras in alls, bara "
     "packas upp. Belagt sedan 1985, vilket bekräftar kortets 80-talsexempel.",
     etymologi="Engelsk förkortning av young urban professional.")

lagg("urmodig",
     "BEGRÄNSNINGEN PÅ KORTET ÄR OBELAGD. Kortet påstod '(**endast om saker, "
     "aldrig om personer**)'. Varken SO, SAOL eller Wiktionary säger något "
     "sådant; SO ger bara 'fullständigt omodern' med exemplet 'en urmodig "
     "kostym'. Att uppfinna en regel som källorna inte har är samma fel som "
     "att uppfinna en synonym. Struken. Etymologin är däremot upplysande: "
     "jämför **gammalmodig** och **nymodig** — leden är -modig 'i modet', och "
     "ur- betyder här 'ur (modet)', inte 'ursprunglig'.",
     huvudbetydelse="Fullständigt omodern, sedan länge ur bruk",
     synonymer=["föråldrad", "förlegad", "gammalmodig"],
     etymologi="ur (modet) + -modig — jämför gammalmodig och nymodig.")

lagg("monstruös",
     "BEKRÄFTAT + ETYMOLOGI. SO ger kortets två betydelser: 'oformlig och "
     "skrämmande' och, försvagat, 'orimlig' ('en monstruös kränkning'). "
     "Ursprunget är latinets *monstrum*, som ursprungligen betydde **järtecken, "
     "varsel** — något onaturligt som VISADE att gudarna var missnöjda (till "
     "*monstrare* 'visa', samma ord som demonstrera). Det förklarar varför "
     "ordet bär både 'vidunder' och 'orimlig'.",
     etymologi="Latin monstrum 'järtecken', till monstrare 'visa' — samma ord "
               "som i demonstrera.")

lagg("repressalie",
     "BEKRÄFTAT + ETYMOLOGI. SO: '(militär) hämndaktion', SAOL: "
     "'vedergällningsåtgärd'. Kortets observation att ordet nästan alltid står "
     "i plural stämmer med SO:s enda exempel ('hotade med militära "
     "repressalier'). Ursprunget: medeltidslatin *represalia* 'återtagande med "
     "våld', till *reprendere* 'återta' — **samma rot som repris**. En "
     "repressalie är alltså ett åter-tagande.",
     etymologi="Till latinets reprendere 'återta' — samma rot som repris.")

lagg("avi",
     "ETYMOLOGIN GÖR ORDET LOGISKT. SO: 'kort skriftligt meddelande om "
     "ankomst av viss postförsändelse', och SO noterar att det utvidgats till "
     "andra skriftliga meddelanden — vilket kortet redan har. Ursprunget är "
     "franskans *avis* 'underrättelse', av latin *ad* 'till' + *videre* 'se': "
     "något som ges någon att se. **Samma videre som i vision och tv.**",
     etymologi="Franska avis, av latin ad 'till' + videre 'se' — något man "
               "ges att se.")

lagg("gyro",
     "BEKRÄFTAT — OCH EN FÖRVÄXLING SOM INTE FANNS. SO: 'gyroskop', till "
     "grekiska *gyros* 'ring'. Kortet stämmer och blandar INTE ihop ordet med "
     "maträtten gyros, vilket vore den uppenbara fällan. Etymologin är "
     "densamma för båda: den grekiska maträtten heter så för att köttet "
     "roterar. Ett ord, två helt olika saker, samma grundbetydelse 'snurra'. "
     "TVÅ KÄLLOR: synonymer.se saknar uppslaget — rödflaggas.",
     etymologi="Grekiska gyros 'ring, snurra' — samma ord som i maträtten "
               "gyros, där köttet roterar.")


if __name__ == "__main__":
    pl.bygg(P, MAL)
