"""Batch 7, 2026-08-10 — 20 kort.

Tre kort saknade synonymer helt (granulera, dekantera, och katakomb hade bara
en). Två register saknade stöd i källorna (borsjtj, talträngd).

Etymologin ger sex ord som blir självförklarande: vernissage↔fernissa,
katedral↔kateder, dekantera↔kanna, granulera↔korn, changera↔växla,
borsjtj↔borst.
"""
import patchlib as pl

MAL = "sessions/session_2026-08-10_v3-tre-kallor-b7.json"
P = {}


def lagg(ord_, slutsats, kalla=None, **andr):
    P[ord_] = (kalla or pl.kallor(ord_), slutsats, andr)


lagg("granulera",
     "KORTET SAKNADE SYNONYMER HELT. SO ger kortets båda betydelser "
     "(kornformen och sårläkningen), SAOL lägger till 'finfördela, korna'. "
     "Etymologin gör ordet genomskinligt: senlatin *granulum* '**litet "
     "korn**', av *granum* 'korn' — samma *granum* som i **granulat** och "
     "**granat** (frukten full av korn).",
     synonymer=["finfördela", "korna", "söndersmula"],
     etymologi="Latin granulum 'litet korn' — samma korn som i granulat.")

lagg("adoratör",
     "BEKRÄFTAT. SAOL: 'tillbedjare, beundrare'; SO saknar uppslaget. "
     "Wiktionary lägger till nyansen '**ofta en förälskad sådan**', vilket "
     "bekräftar kortets 'svärmisk beundrare, oftast av en kvinna' — den "
     "preciseringen står alltså inte i Akademiens ordböcker men är belagd. "
     "Etymologin: latin *adorare* '**tillbe**' — samma ord som i engelskans "
     "*adore*.",
     etymologi="Latin adorare 'tillbe' — samma ord som engelskans adore.")

lagg("borsjtj",
     "REGISTRET SAKNAR STÖD, OCH ETYMOLOGIN ÄR OVÄNTAD. Kortet var märkt "
     "**vardaglig**; varken SO eller SAOL märker ordet — det är namnet på en "
     "maträtt, inte ett vardagsord för något annat. Ändrat till formell. "
     "Ursprunget är verkligt egendomligt: via ryskan av ukrainska *borsjtj*, "
     "ursprungligen '**skärpa**' — efter de skarptaggiga bladen hos "
     "björnlokssläktet, som soppan en gång kokades på. **Besläktat med "
     "borst.** Rödbetorna kom senare.",
     register="formell",
     etymologi="Ursprungligen 'skärpa', efter björnlokans taggiga blad som "
               "soppan förr kokades på. Släkt med borst.")

lagg("kalibrera",
     "BEKRÄFTAT + ETYMOLOGI MED EN ÖVERRASKNING. SO: 'anpassa eller ställa in "
     "efter i förväg fastställda mått'. Ordet hör till **kaliber**, och SO "
     "daterar det till 1784 '**i fråga om uppmätning av kalibern hos "
     "eldvapen**' — ordet kommer alltså från vapenmätning innan det blev "
     "allmänt. Kortets 'mot en känd referens' är en bra precisering som "
     "källorna inte har.",
     synonymer=["justera", "finjustera", "ställa in", "nollställa"],
     etymologi="Till kaliber — ordet kom från uppmätning av eldvapens kaliber.")

lagg("dekantera",
     "KORTET SAKNADE SYNONYMER, OCH ETYMOLOGIN ÄR ETT KÄRL. SO: 'försiktigt "
     "hälla av (vätska) för att skilja undan bottensats'. Kortets "
     "vinkarafffokus är riktigt men snävare än SO, som gäller vätska i "
     "allmänhet. Ursprunget: franska *décanter*, av latin *de* 'av' + "
     "*canthus* '**pip på en kanna**' — att dekantera är ordagrant att hälla "
     "av över pipen.",
     huvudbetydelse="Försiktigt hälla av en vätska så bottensatsen blir kvar "
                    "— oftast om vin",
     synonymer=["hälla av", "sila från bottensatsen"],
     etymologi="Latin canthus, 'pip på en kanna' — att hälla av över pipen.")

lagg("stilisera",
     "EN BETYDELSE TILL, OCH DEN ÄR NEGATIV. SO ger 'förenkla och framhäva "
     "det typiska' — kortet har den. Men SO lägger till 'äv. bildligt om "
     "annan förenkling el. renodling', med exemplet 'bokens **stiliserade "
     "persongalleri**', och Wiktionary preciserar att bruket ofta är "
     "**nedsättande**: schablonmässigt, stelt. Att stilisera en bild är "
     "beröm; att stilisera personer är kritik. Den skillnaden fanns inte på "
     "kortet. TVÅ KÄLLOR: Wiktionary strypte anropet — rödflaggas för "
     "omprövning.",
     huvudbetydelse="Förenkla så att det typiska framhävs ; om personer och "
                    "text ofta klandrande: göra schablonmässig",
     synonymer=["förenkla", "schematisera", "renodla"],
     etymologi="Till stil, via italienskans stilizzare.")

lagg("nimbus",
     "BEKRÄFTAT + EN ETYMOLOGI SOM FÖRKLARAR BÅDA BETYDELSERNA. SO ger "
     "kortets två: ljuskransen och det höga anseendet, och noterar att den "
     "andra numera är den vanliga. Ursprunget är latin *nimbus* '**oväder; "
     "moln**; helgongloria' — molnet gudarna svepte in sig i blev glorian "
     "runt helgonet, som blev glansen runt professorn. Samma ord lever kvar i "
     "molnnamnet **nimbostratus**.",
     etymologi="Latin nimbus 'moln' — molnet kring guden blev glorian kring "
               "helgonet. Samma ord som i nimbostratus.")

lagg("affekt",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'stark sinnesrörelse', med exemplet 'handla "
     "i affekt' — precis kortets vinkling, och den enda form ordet i praktiken "
     "möts i. JFR **emotion**. Ursprunget: latin *affectus* '**sinnestillstånd**', "
     "till *afficere* 'påverka' — samma rot som **affektera** och engelskans "
     "*affect*.",
     etymologi="Latin affectus 'sinnestillstånd', till afficere 'påverka'.")

lagg("goodwill",
     "BEKRÄFTAT — OCH MOTSATSEN FINNS PÅ RIKTIGT. SO ger 'gott rykte eller "
     "anseende' och listar **badwill** som motsats, vilket är ett verkligt "
     "svenskt uppslagsord och inte ett skämt. Kortets ekonomiska betydelse "
     "(det immateriella värdet i bokföringen) står inte i SO men följer av "
     "SAOL:s 'gott anseende som t.ex. **företag** åtnjuter' och är den "
     "betydelse ordet har i årsredovisningar. Behålls. Etymologin: engelska "
     "goodwill, egentligen '**välvilja**'.",
     etymologi="Engelska goodwill, egentligen 'välvilja'.")

lagg("bödel",
     "BEKRÄFTAT + EN ETYMOLOGI SOM ÄR NÄSTAN LUSTIG. SO ger kortets två "
     "betydelser, inklusive den bildliga om makthavare ('Franco, Spaniens "
     "bödel'). SO:s exempel 'den siste bödeln i Sverige avled 1920' är värt "
     "att minnas. Ursprunget: lågtyska *bödel*, egentligen '**tjänare; "
     "bud**', **besläktat med bjuda**. Skarprättaren hette alltså från början "
     "bara 'den som utför order'.",
     synonymer=["skarprättare", "mästerman"],
     etymologi="Lågtyska bödel, egentligen 'tjänare, bud' — släkt med bjuda.")

lagg("katakomb",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'underjordisk begravningsplats som består av "
     "långa gångar med uthuggna gravkammare i väggarna' — kortet är nästan "
     "ordagrant detta. Wiktionary ger en andra, modern betydelse kortet "
     "saknar: **gångarna under en arena** med omklädningsrum. Den lever i "
     "sportspråk. Ursprunget: troligen grekiska *kata* 'ned' + latin *tumba* "
     "'grav'.",
     huvudbetydelse="Underjordisk begravningsplats med gångar och "
                    "gravkammare i väggarna ; i sportspråk: gångarna under "
                    "en arena",
     synonymer=["gravgång", "gravvalv", "krypta"],
     etymologi="Troligen grekiska kata 'ned' + latin tumba 'grav'.")

lagg("talträngd",
     "REGISTRET SAKNAR STÖD, OCH EN TON SAKNADES. Kortet var märkt "
     "**vardaglig**; ingen källa märker ordet, och SO:s exempel är litterärt "
     "('flera av middagstalarna var så talträngda att dansen försenades "
     "betänkligt'). Ändrat till formell. SO noterar däremot något kortet "
     "saknade: ordet används '**ofta något ironiskt**' — det är inte neutralt "
     "beskrivande, utan lätt kritiskt. TVÅ KÄLLOR: Wiktionary saknar "
     "uppslaget — rödflaggas.",
     register="formell, ironisk",
     huvudbetydelse="Ivrig att få tala — sägs oftast med en gnutta ironi",
     synonymer=["pratsam", "talför", "språksam", "mångordig"])

lagg("hutlös",
     "BEKRÄFTAT + ETYMOLOGI SOM ÄR HELA ORDET. SO: 'som tyder på fullständig "
     "brist på skamkänsla', med exemplen 'hutlösa priser' och 'reparationen "
     "var hutlöst dyr' — kortets prisfokus är alltså belagt. Wiktionary ger "
     "den perfekta förklaringen: hutlös är den 'som **inte vet hut**'. *Hut* "
     "är ett gammalt ord för anständighet, som lever kvar i 'lära någon hut'.",
     etymologi="Den som inte vet hut — hut är gammalt för anständighet, som i "
               "'lära någon hut'.")

lagg("dupera",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'medvetet ge (någon) felaktigt intryck'. "
     "SO:s exempel träffar kortets 'falsk fasad' exakt: 'en försäljare som "
     "duperar alla kunder genom sin **skenbara saklighet**'. Ursprunget: "
     "franska *duper*, till *dupe* '**narr, godtrogen person**' — att dupera "
     "någon är att göra hen till narr.",
     etymologi="Franska dupe 'narr' — att dupera är att göra någon till narr.")

lagg("changera",
     "BEKRÄFTAT + ETYMOLOGI. SO: 'märkbart förändras **till det sämre**' — "
     "riktningen nedåt är inbyggd i ordet, precis som kortet säger. SO:s båda "
     "exempel visar de två bruken: personen ('han har changerat mycket efter "
     "pensioneringen') och tyget ('tröjan changerade redan efter första "
     "tvätten'). synonymer.se ger den försvenskade stavningen **sjangsera**. "
     "Ursprunget: franska *changer* 'ändra', av latin *cambire* '**växla**' — "
     "samma ord som i *change* och *växelkurs*.",
     synonymer=["förfalla", "blekna", "deklinera"],
     etymologi="Franska changer 'ändra', av latin cambire 'växla' — samma ord "
               "som engelskans change.")

lagg("katedral",
     "BEKRÄFTAT + ETYMOLOGI SOM BINDER IHOP KYRKAN MED SKOLBÄNKEN. SO och "
     "SAOL ger båda bara 'domkyrka'. Kortets 'biskopens huvudkyrka i ett "
     "stift' är mer upplysande än båda och stöds av etymologin: medeltidslatin "
     "*cathedralis* 'som hör till **biskopssätet**', till *cathedra* 'stol' — "
     "**samma ord som kateder**. En katedral är ordagrant kyrkan där "
     "biskopens stol står.",
     etymologi="Latin cathedra 'stol' — samma ord som kateder. Katedralen är "
               "kyrkan där biskopens stol står.")

lagg("vernissage",
     "ETYMOLOGIN ÄR EN LITEN KONSTHISTORIA. SO: 'öppnande av "
     "konstutställning'. Ursprunget: franska *vernissage*, till *vernir* "
     "'**fernissa, lacka**' — **samma ord som fernissa**. Dagen före "
     "utställningens öppnande fick konstnärerna fernissa sina målningar på "
     "plats, och den dagen blev med tiden själva invigningen. Kortets synonym "
     "'invigning' är för allmän och stryks till förmån för belagda. "
     "TVÅ KÄLLOR: Wiktionary strypte anropet — rödflaggas för omprövning.",
     synonymer=["utställningsöppnande", "konstpremiär", "premiärvisning"],
     etymologi="Franska vernir 'fernissa' — konstnärerna fernissade sina "
               "tavlor dagen före öppningen.")

lagg("affektiv",
     "BEKRÄFTAT + EN FACKBETYDELSE SOM SAKNADES. SO: 'som har att göra med "
     "affekter', men lägger till '**spec. medicin**' med exemplen 'affektiv "
     "störning' och 'affektiva sjukdomar' — det är psykiatrins term för "
     "sjukdomar som drabbar stämningsläget, alltså depression och bipolär "
     "sjukdom. Den betydelsen är den man faktiskt möter i text och saknades "
     "på kortet. TVÅ KÄLLOR: Wiktionary strypte anropet — rödflaggas.",
     huvudbetydelse="Som rör känslolivet ; i medicin: som rör stämningsläget, "
                    "som i 'affektiv störning'",
     etymologi="Avledning till affekt.")

lagg("hugfästa",
     "BEKRÄFTAT + ETYMOLOGI. SO och SAOL ger båda 'säkra hågkomsten av'. "
     "Kortets 'göra så att något fastnar i minnet' är samma sak i klarspråk. "
     "SO:s exempel visar det typiska bruket, som kortet saknar: ordet gäller "
     "nästan alltid ett MINNESMÄRKE eller en handling till någons minne "
     "('jubileet hugfästes med en utsökt liten bok'). Ursprunget: **håg** "
     "'sinne, minne' + fästa — samma håg som i *hågkomst* och *hugad*.",
     synonymer=["bevara minnet av", "föreviga", "rädda undan glömskan"],
     etymologi="håg 'sinne, minne' + fästa — samma håg som i hågkomst.")

lagg("utmönstra",
     "BEKRÄFTAT + EN ETYMOLOGI SOM VÄNDER ORDET. SO: 'skilja bort såsom "
     "föråldrad eller mindre värdefull'. Kortets 'ta bort, fasa ut' är för "
     "tunt — det som utmönstras tas bort **för att det är förlegat**, inte "
     "bara bort. SO:s exempel är bra: 'det gamla begreppet "
     "\"kyrkobokföring\" utmönstrades på 1990-talet'. Ursprunget: fornsvenska "
     "*utmönstra* betydde '**vid mönstring UTVÄLJA**' — alltså raka motsatsen "
     "till i dag. Ordet har vänt betydelse.",
     huvudbetydelse="Rensa bort något för att det blivit föråldrat eller "
                    "oanvändbart",
     synonymer=["gallra ut", "kassera", "utrangera", "sovra"],
     etymologi="Betydde förr 'välja UT vid mönstring' — ordet har vänt.")


if __name__ == "__main__":
    pl.bygg(P, MAL)
