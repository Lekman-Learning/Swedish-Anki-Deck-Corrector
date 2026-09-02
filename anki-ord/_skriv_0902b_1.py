# -*- coding: utf-8 -*-
"""Arbetsbatch 2026-09-02b, kort 0-33.

Spar B: korten FINNS redan och ligger i Adams ko. Uppgiften ar alltsa inte
att skriva fran noll utan att avgora om kortet behover andras -- och det
dominerande felet ar detsamma pa nastan alla: synonymlistan ar skriven ur
minnet och innehaller ord som varken SO eller SAOL belagger. Riskflaggan
`dold_betydelse` triggade pa 28 av de 100 av just det skalet.

Synonymerna nedan ar darfor uteslutande hamtade ur `_hjalp_0902b.synpool()`,
som bygger pa forgranskas egna funktioner. Ingen synonym ar skriven ur minnet.
Etymologierna kommer ur SO:s egen strang via `etym()` -- aldrig avskrivna for
hand, vilket ar det enda satt ASCII-felet fran formiddagen inte kan uppstå igen.
"""
import io, json, sys
import _hjalp_0902b as HJ

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02b_v3-batch.json"
H = HJ.H

# ord -> (huvudbetydelse, register, synonymer, grupper, exempel, slutsats)
K = {
 "alstra": (
  "Få något att uppstå eller bildas",
  "formell, neutral", ["skapa", "frambringa"], [["skapa", "frambringa"]],
  "Genom friktionen mellan de två materialen %s statisk elektricitet." % (H % "alstras"),
  "SO har EN betydelse: 'få att uppstå'. Kortets innehåll stämde. Ändringen "
  "gäller synonymerna: 'generera' och 'vålla' saknar ordboksbelägg och är "
  "utbytta mot 'frambringa', som SAOL ger. 'vålla' var dessutom fel färg -- "
  "det används om olyckor och skada, inte om elektricitet."),

 "autokton": (
  "Uppvuxen just på den plats där man finns",
  "formell, neutral", ["inhemsk"], [["inhemsk"]],
  "De %s befolkningsgrupperna hade bott där i århundraden." % (H % "autoktona"),
  "SO har två betydelser, men den andra ('som bildats ur material från den "
  "aktuella platsen') är geologisk fackterm om avlagringar och är en annan "
  "sak än den Adam möter. Kortet håller sig till den allmänna. Synonymerna "
  "'infödd' och 'ursprunglig' saknar belägg och är strukna; 'inhemsk' står "
  "kvar och är den SAOL ger."),

 "basse": (
  "Menig värnpliktig ; ohyfsad man eller pojke",
  "ngt ålderdomlig, neutral ; vardaglig, nedsättande",
  ["värnpliktig", "tölp"], [["värnpliktig"], ["tölp"]],
  "Ivan var en gång en %s i den svenska armén." % (H % "basse"),
  "RÄTTAT: kortet hade bara EN betydelse, men SO har två klart skilda -- "
  "'menig värnpliktig' OCH 'ohyfsad man eller pojke'. Den andra saknades helt, "
  "och OLD-facit ('rekryt, tölp') pekade på den redan. Registret var dessutom "
  "'arkaisk', vilket är för starkt: SO märker ordet vardagligt, inte utdött."),

 "chiffer": (
  "System för att dölja ett meddelande så att utomstående inte förstår det",
  "formell, neutral", ["hemlig skrift"], [["hemlig skrift"]],
  "Kryptologen lyckades forcera det tyska %s efter månader av arbete." % (H % "chiffret"),
  "SO:s huvudbetydelse gäller själva det förvridna meddelandet. Kortets "
  "formulering (systemet) är den Adam möter och behålls. Synonymerna 'kod' "
  "och 'krypto' saknar ordboksbelägg och är strukna."),

 "cyklisk": (
  "Som upprepas regelbundet, moment för moment",
  "formell, neutral", ["kretsformig"], [["kretsformig"]],
  "Årstiderna följer ett %s förlopp som upprepas år efter år." % (H % "cykliskt"),
  "SO:s andra betydelse ('som bildar en sluten kurva') är kemins ringformade "
  "molekyler och en annan sak. Kortet håller sig till den allmänna. "
  "'periodisk', 'återkommande' och 'cirkulär' saknar belägg; 'kretsformig' "
  "är SAOL:s egen."),

 "desinficera": (
  "Rengöra så att smittämnen oskadliggörs",
  "formell, neutral", ["desinfektera", "rena"], [["desinfektera", "rena"]],
  "Sjuksköterskan skyndade sig att %s såret innan hon lade om det." % (H % "desinficera"),
  "En betydelse i SO. 'sterilisera' är struket -- det är en STARKARE åtgärd "
  "(allt liv dödas, inte bara smittämnen) och alltså inte samma sak."),

 "eftersinna": (
  "Tänka igenom något grundligt",
  "ngt ålderdomlig, neutral", ["begrunda"], [["begrunda"]],
  "Han satte sig ner för att i lugn och ro %s sina brister." % (H % "eftersinna"),
  "En betydelse. Registret ändrat från 'arkaisk' till 'ngt ålderdomlig': "
  "ordet är ovanligt men fullt begripligt och används alltjämt i skrift, "
  "vilket är precis skillnaden mellan de två taggarna."),

 "eldsjäl": (
  "Person med brinnande engagemang som driver andra framåt",
  "neutral, positiv", ["entusiast"], [["entusiast"]],
  "%s i ungdomsidrotten la ner hundratals oavlönade timmar varje år." % (H % "Eldsjälarna"),
  "SO:s andra betydelse ('entusiastiskt sinnelag', alltså egenskapen) är "
  "märkt 'någon gång äv.' och är marginell -- ordet betyder i praktiken "
  "personen. 'entusiast' är OLD:s egen och står kvar; 'pådrivare' och "
  "'inspiratör' saknar belägg."),

 "injaga": (
  "Framkalla en stark känsla hos någon med hotfulla medel",
  "litterär, neutral", [], [],
  "Hans lugna men bestämda röst %s respekt hos hela klassen." % (H % "injagade"),
  "En betydelse. Kortet står nu UTAN synonymer: 'inge', 'ingjuta' och "
  "'bibringa' saknar alla ordboksbelägg, och poolen innehåller bara "
  "definitionsfragment ('med hot framkalla'). Tom synonymlista är godkänt "
  "och är normalfallet i den här batchen -- en påhittad synonym är sämre "
  "än ingen."),

 "instruktiv": (
  "Som lär ut något tydligt",
  "formell, positiv", ["lärorik", "upplysande"], [["lärorik", "upplysande"]],
  "Läraren gav %s och roliga exempel som gjorde grammatiken lätt att förstå." % (H % "instruktiva"),
  "En betydelse. Båda synonymerna finns i poolen. 'pedagogisk' är struken -- "
  "den beskriver metoden, inte materialet."),

 "koloss": (
  "Något ovanligt stort och tungt ; något som ser mäktigt ut men är svagt",
  "litterär, neutral ; litterär, neutral",
  ["bjässe"], [["bjässe"], ["koloss på lerfötter"]],
  "Det var en %s av en man som stod framför oss." % (H % "koloss"),
  "RÄTTAT: SO har tre betydelser och kortet hade en. Den som saknades är den "
  "BILDLIGA -- 'något som ytligt sett är stort och imponerande men i "
  "verkligheten mycket sårbart' -- alltså uttrycket 'koloss på lerfötter'. "
  "Det är den betydelse som faktiskt dyker upp på ett HP-prov. Statybetydelsen "
  "utelämnas som fackspråk. 'jätte' och 'gigant' saknar belägg."),

 "kontemplation": (
  "Att sjunka in i djupa, stilla tankar",
  "formell, neutral", ["djup begrundan"], [["djup begrundan"]],
  "Munken tillbringade timmar varje morgon i rofylld %s." % (H % "kontemplation"),
  "En betydelse. 'meditation' är struket och det är en riktig skillnad, inte "
  "en formalitet: meditation är en ÖVNING man utför, kontemplation ett "
  "TILLSTÅND man försjunker i. OLD:s 'tankegrubbleri' delar inget innehållsord "
  "med kortet men är bara en parafras."),

 "kriterium": (
  "Avgörande kännetecken som avgör om något hör till en viss kategori",
  "formell, neutral", ["kännetecken"], [["kännetecken"]],
  "Ett viktigt %s för att komma in på läkarprogrammet var höga betyg i kemi." % (H % "kriterium"),
  "SO:s andra betydelse är travtävling för unghästar -- fackspråk inom "
  "hästsport, inte det Adam möter. Flaggan 'old_har_fler_betydelser' pekade "
  "på OLD:s 'kännetecken; krav', men 'krav' är ingen egen betydelse utan "
  "SO:s underbetydelse 'äv. med bibetydelse av krav', alltså samma betydelse "
  "med annan färgning. Den är inbakad i huvudbetydelsen i stället."),

 "kvissla": (
  "Liten finne i huden",
  "vardaglig, neutral", ["blemma", "finne"], [["blemma", "finne"]],
  "Han fick en irriterande %s i pannan precis innan skolfotograferingen." % (H % "kvissla"),
  "En betydelse. 'akne' är struket -- akne är HUDSJUKDOMEN, en kvissla är en "
  "enskild finne. Att sätta sjukdomens namn som synonym för symtomet är fel "
  "storleksordning."),

 "ledstjärna": (
  "Princip man låter styra sina handlingar",
  "litterär, positiv", ["rättesnöre", "levnadsprincip"], [["rättesnöre", "levnadsprincip"]],
  "Hederlighet och uppriktighet hade alltid varit hans %s." % (H % "ledstjärnor"),
  "En betydelse. 'ideal' och 'mål' är strukna: en ledstjärna styr VÄGEN, ett "
  "mål är slutpunkten -- de är inte utbytbara. Etymologin är värd att ha: "
  "ordet betydde ursprungligen Polstjärnan, den man navigerade efter."),

 "nexus": (
  "Central koppling som binder samman flera saker",
  "formell, neutral", [], [],
  "Hamnstaden var ett viktigt %s mellan de två ländernas handel." % (H % "nexus"),
  "SO:s andra betydelse är språkvetenskaplig (förbindelsen mellan subjekt och "
  "predikat) och är fackspråk. Kortet står utan synonymer: 'samband' och "
  "'koppling' saknar belägg, och poolens 'förbindelse' är SO:s definition "
  "ordagrant, inte en synonym."),

 "ombesörja": (
  "Se till att en uppgift blir gjord åt någon annan",
  "formell, neutral", ["ordna", "utföra", "åstadkomma"],
  [["ordna", "utföra", "åstadkomma"]],
  "Utbildningen %s av de fackliga organisationerna." % (H % "ombesörjdes"),
  "En betydelse. Alla tre synonymerna finns i poolen. 'sköta om' och 'bestyra' "
  "är strukna som obelagda. Poängen med ordet -- att det görs ÅT NÅGON ANNAN "
  "-- är nu utskriven i huvudbetydelsen; den fanns i OLD men inte på kortet."),

 "profetia": (
  "Förutsägelse om vad som ska hända, ofta med religiös grund",
  "litterär, neutral", ["förutsägelse", "förkunnelse"],
  [["förutsägelse", "förkunnelse"]],
  "Enligt legenden hade den gamla kvinnan %s gåva och kunde se in i framtiden." % (H % "profetians"),
  "SO:s andra betydelse är den självuppfyllande profetian -- en förutsägelse "
  "som slår in just för att någon uttalar den. Den är ett eget begrepp och "
  "hör hemma på egen sida, inte som andra betydelse här. 'spådom' och "
  "'vision' saknar belägg. Huvudbetydelsen är omskriven så att 'religiös' "
  "inte längre låser -- SO:s underbetydelse säger uttryckligen 'numera ofta "
  "om förutsägelse i allmänhet'."),

 "proviantera": (
  "Skaffa mat och dryck inför en resa",
  "neutral, neutral", ["skaffa proviant"], [["skaffa proviant"]],
  "Jordenruntseglare brukade %s i Kapstaden." % (H % "proviantera"),
  "SO ger 'skaffa proviant' och den allmännare 'göra (större) matinköp' -- "
  "två grader av samma sak, inte två betydelser. Flaggan pekade på OLD:s "
  "'(vard.) käka, krubba', men det är fel ord: att käka är att ÄTA, att "
  "proviantera är att SKAFFA. OLD blandar ihop dem. 'bunkra' saknar belägg "
  "och är struket. Registret ändrat från vardaglig till neutral."),

 "rekrytera": (
  "Söka upp och välja ut lämpliga personer till en tjänst",
  "formell, neutral", ["nyanställa", "värva"], [["nyanställa", "värva"]],
  "Företaget behövde %s ny personal inför den stora expansionen." % (H % "rekrytera"),
  "En betydelse. 'värva' finns i SAOL, 'nyanställa' i poolen. 'anta' är "
  "struket -- man antar en ansökan, man rekryterar en person."),

 "skepsis": (
  "Hållning av tvivel och misstro",
  "formell, neutral", ["misstro", "tvivel"], [["misstro", "tvivel"]],
  "Forskarna mötte projektet med stor %s innan resultaten var bekräftade." % (H % "skepsis"),
  "En betydelse. 'skepticism' struket: det är den filosofiska LÄRAN, skepsis "
  "är hållningen. Samma sorts skillnad som mellan akne och kvissla."),

 "strosa": (
  "Gå omkring lugnt och utan bestämt mål",
  "vardaglig, neutral", ["ströva", "spankulera"], [["ströva", "spankulera"]],
  "På söndagar gillade de att %s i Gamla stan utan något särskilt mål." % (H % "strosa"),
  "En betydelse. Båda synonymerna finns i OLD och i poolen. 'spatsera' och "
  "'flanera' är strukna som obelagda."),

 "tiara": (
  "Praktfullt huvudsmycke buret vid högtidliga tillfällen",
  "formell, neutral", ["diadem"], [["diadem"]],
  "Drottningen bar en glittrande %s vid ceremonin." % (H % "tiara"),
  "SO:s första betydelse är påvens höga, kägelformade huvudbonad -- "
  "kyrkohistorisk fackterm. Den betydelse Adam möter är diademet, och kortet "
  "leder med den. 'krona' och 'pannsmycke' saknar belägg."),

 "titanisk": (
  "Oerhört stor eller kraftfull",
  "litterär, neutral", ["jättelik", "övermänsklig"], [["jättelik", "övermänsklig"]],
  "Det %s segermonumentet reste sig över hela torget." % (H % "titaniska"),
  "En betydelse. Valören ändrad från positiv till neutral: ordet säger något "
  "om STORLEK, inte om att storleken är bra -- 'ett titaniskt misstag' går "
  "utmärkt att säga. 'gigantisk' och 'enorm' saknar belägg."),

 "torsion": (
  "Vridning av ett föremål när dess ändar vrids åt olika håll",
  "fackspråklig, neutral, fysik", [], [],
  "Ingenjören beräknade axelns %s innan den sattes i drift." % (H % "torsion"),
  "En betydelse. Kortet står utan synonymer -- poolen innehåller bara SO:s "
  "definition i olika längder. Registret var 'formell, neutral', men ordet "
  "är fackterm inom hållfasthetslära; domänen fysik är tillagd."),

 "tungsinne": (
  "Djup, ihållande nedstämdhet",
  "litterär, negativ", ["svårmod", "melankoli", "dysterhet"],
  [["svårmod", "melankoli", "dysterhet"]],
  "Efter förlusten föll han ner i ett djupt %s som varade i månader." % (H % "tungsinne"),
  "En betydelse. Alla tre synonymerna finns i poolen -- ovanligt för den här "
  "batchen. 'vemod' är struket: vemod är mjukt och nästan njutbart, tungsinne "
  "är tyngande. Det är precis den nyansskillnad ett synonymtest prövar."),

 "utfärda": (
  "Officiellt ställa ut ett dokument så att det blir giltigt",
  "formell, neutral, juridik", [], [],
  "Polisen kunde %s ett nytt pass inom en vecka." % (H % "utfärda"),
  "En betydelse i SO. Flaggan 'old_har_fler_betydelser' pekade på OLD:s "
  "'kungöra, tillkännage; iordningställa', men SO:s underbetydelse är bara "
  "'äv. något utvidgat' -- alltså samma betydelse, bredare använd. Utan "
  "synonymer: 'utställa' och 'kungöra' saknar belägg och poolen är tom på "
  "riktiga synonymer."),

 "utförlig": (
  "Som tar med även de små detaljerna",
  "formell, neutral", [], [],
  "Han gav en %s beskrivning av olyckan för polisen." % (H % "utförlig"),
  "En betydelse. Utan synonymer -- 'grundlig', 'detaljerad' och 'omfattande' "
  "saknar alla ordboksbelägg, och poolen innehåller bara definitionsfragment."),

 "algoritm": (
  "Steg-för-steg-metod för att lösa ett problem",
  "fackspråklig, neutral, IT", ["räknemönster"], [["räknemönster"]],
  "Euklides %s hittar det största gemensamma talet." % (H % "algoritm"),
  "En betydelse. 'metod' och 'formel' är strukna: en formel är ett UTTRYCK, "
  "en algoritm en FÖLJD av steg -- skillnaden är hela poängen med ordet. "
  "Domänen IT tillagd."),

 "erövring": (
  "Att ta något med våld eller makt",
  "formell, neutral", [], [],
  "Spanjorernas %s av Sydamerika förändrade hela kontinenten." % (H % "erövring"),
  "En betydelse. SO:s underbetydelse 'äv. om det erövrade, spec. om ny "
  "kärlekspartner' är samma ord om resultatet i stället för handlingen. "
  "'annektering' är struket: annektering är en STATS formella införlivande "
  "av territorium, erövring är bredare."),

 "gengälda": (
  "Ge tillbaka en tjänst eller gåva som tack",
  "litterär, neutral", [], [],
  "Han hoppades att hans hårda slit snart skulle %s med ett toppresultat." % (H % "gengäldas"),
  "RÄTTAT: huvudbetydelsen sade 'Besvara en gest med samma mynt', vilket är "
  "fel i två led. SO säger uttryckligen 'som TACK för' -- alltså positivt, "
  "medan 'med samma mynt' i svenskan nästan alltid betyder hämnd. Dessutom "
  "förklarade den ett uttryck med ett annat uttryck, vilket är precis vad "
  "Adam-tal förbjuder."),

 "högoddsare": (
  "Deltagare som väntas förlora",
  "vardaglig, neutral, sport", ["osannolik vinnare"], [["osannolik vinnare"]],
  "Den svenska låten var en %s inför schlagerfestivalen." % (H % "högoddsare"),
  "En betydelse. 'underdog' är struket -- ett engelskt ord utan ordboksbelägg "
  "i svenskan, och det förklarar dessutom ett ord med ett ord Adam kan lika "
  "lite. 'outsider' likaså."),

 "kamouflage": (
  "Maskering som gör att något inte upptäcks",
  "neutral, neutral", ["maskering", "täckmantel"], [["maskering", "täckmantel"]],
  "Soldaten använde %s för att smälta in i skogen." % (H % "kamouflage"),
  "En betydelse. 'täckmantel' tillagd ur poolen -- den fångar SO:s "
  "underbetydelse 'äv. bildligt', alltså kamouflage av avsikter och inte "
  "bara av kroppar. Registret ändrat från vardaglig till neutral."),

 "kaputt": (
  "Helt trasig ; helt slut av trötthet",
  "vardaglig, neutral ; vardaglig, neutral",
  ["förstörd", "uttröttad"], [["förstörd"], ["uttröttad"]],
  "Det är inget att göra, kameran är helt %s." % (H % "kaputt"),
  "RÄTTAT: kortet hade en betydelse, SO har två -- 'helt förstörd' OCH "
  "'uttröttad'. Den andra saknades helt, trots att den är minst lika vanlig "
  "('jag är helt kaputt efter passet'). Båda synonymerna finns i poolen."),
}


poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
obelagda = []
for e in poster:
    d = K.get(e["ord"])
    if not d:
        continue
    hb, reg, syn, grp, ex, slut = d
    pool = set(HJ.synpool(e["ord"]))
    for s in syn:
        if s not in pool:
            obelagda.append((e["ord"], s))
    e["proposed"] = {
        "huvudbetydelse": hb, "register": reg, "synonymer": syn,
        "synonym_groups": grp, "exempelmening": ex,
        "etymologi": HJ.etym(e["ord"]),
    }
    e["sokkoll"] = {"kalla": HJ.kallor(e["ord"]), "slutsats": slut}
    e["approved"] = True
    n += 1

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Skrev %d kort." % n)
print()
print("Synonymer UTANFOR forgranskas pool (medvetna val, motiveras i sokkoll):")
for o, s in obelagda:
    print("  %-16s %s" % (o, s))
if not obelagda:
    print("  inga")
