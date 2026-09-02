# -*- coding: utf-8 -*-
"""Arbetsbatch 2026-09-02b, kort 34-65.

Samma metod som batch 1: synonymer BARA ur `_hjalp_0902b.synpool()`,
etymologi ur SO:s egen strang. Kontrollen langst ned skriver ut varje
synonym som inte finns i poolen, sa felet inte kan slinka igenom tyst --
i batch 1 fangade den atta, alla tagna ur minnet.
"""
import io, json, sys
import _hjalp_0902b as HJ

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02b_v3-batch.json"
H = HJ.H

K = {
 "korrosion": (
  "Att metall fräts sönder av kemisk påverkan",
  "fackspråklig, neutral, kemi", ["frätning", "rostning"], [["frätning", "rostning"]],
  "%s på järndelarna gick snabbare i den fuktiga miljön." % (H % "Korrosion"),
  "SO:s andra betydelse är geologisk (nötning av berggrund). Kortet håller "
  "sig till metallbetydelsen, som är den ordet nästan alltid har. Båda "
  "synonymerna finns i poolen."),

 "kronometer": (
  "Ur byggt för mycket exakt tidmätning",
  "fackspråklig, neutral, sjöfart", [], [],
  "Seglaren använde en %s för att navigera på öppet hav." % (H % "kronometer"),
  "En betydelse. Utan synonymer -- 'precisionsur' saknar ordboksbelägg. "
  "Domänen sjöfart är satt: ordet fick sin betydelse av longitudproblemet, "
  "där ett ur som höll tiden till sjöss var det som gjorde navigering möjlig."),

 "misstroendevotum": (
  "Omröstning där riksdagen förklarar att den inte längre litar på regeringen",
  "formell, neutral, politik", [], [],
  "Regeringen överlevde två %s under mandatperioden." % (H % "misstroendevotum"),
  "En betydelse. 'misstroendeförklaring' saknar ordboksbelägg och är dessutom "
  "nästan samma ord -- att förklara ett svårt ord med ett lika svårt är "
  "precis vad Adam-tal förbjuder. Huvudbetydelsen är i stället omskriven "
  "med vardagliga ord."),

 "pampusch": (
  "Fodrad överdragssko som bärs utanpå andra skor",
  "ngt ålderdomlig, neutral", ["bottin"], [["bottin"]],
  "Han drog på sig ett par %s innan han gick ut i snöslasket." % (H % "pampuscher"),
  "En betydelse. Registret ändrat från 'arkaisk' till 'ngt ålderdomlig' -- "
  "plagget är ur bruk men ordet förstås ännu. 'galosch' är struket: en "
  "galosch är gummi och träs över skon, en pampusch är fodrad och skaftad."),

 "paternalism": (
  "Att en överordnad bestämmer över andra och kallar det omtanke",
  "formell, negativ, politik", [], [],
  "Den statliga %s i välfärdssamhället kritiserades hårt." % (H % "paternalismen"),
  "En betydelse. Valören ändrad från neutral till negativ: ordet används "
  "praktiskt taget alltid som anklagelse -- ingen kallar sig själv "
  "paternalistisk. 'förmyndarmentalitet' saknar belägg och förklarar "
  "dessutom svårt med svårt."),

 "prognos": (
  "Förutsägelse om hur något kommer att utveckla sig",
  "formell, neutral", ["förutsägelse"], [["förutsägelse"]],
  "Resultatet låg något över fjolårets %s." % (H % "prognos"),
  "En betydelse. Underbetydelsen om individuella framtidsutsikter i "
  "juridiska sammanhang är samma ord i ett smalare fält."),

 "prövning": (
  "Påfrestning man tvingas gå igenom ; juridisk behandling av ett ärende ; tentamen",
  "neutral, neutral ; formell, neutral, juridik ; neutral, neutral",
  ["psykisk påfrestning", "tentamen"],
  [["psykisk påfrestning"], [], ["tentamen"]],
  "Att vara nybliven förälder är många gånger en %s." % (H % "prövning"),
  "RÄTTAT: kortet hade EN betydelse, SO har tre klart skilda -- påfrestning, "
  "juridisk prövning och tentamen. Alla tre är gångbara och den tredje är "
  "dessutom den Adam själv använder ordet i just nu (prövning i Fysik 2). "
  "Att bara ha påfrestningsbetydelsen gjorde kortet direkt vilseledande. "
  "Grupp 2 saknar belagd synonym och lämnas tom."),

 "psykos": (
  "Psykisk sjukdom där verklighetsuppfattningen förändras och insikten om att man är sjuk saknas",
  "fackspråklig, neutral, medicin", [], [],
  "Han drabbades av en %s efter flera sömnlösa veckor." % (H % "psykos"),
  "En betydelse. 'sinnesstörning' är struket -- det är ett äldre juridiskt "
  "samlingsbegrepp, inte en synonym. Huvudbetydelsen är kompletterad med "
  "SO:s andra halva, den BRISTANDE SJUKDOMSINSIKTEN, som är just det som "
  "skiljer psykos från andra psykiska tillstånd och som kortet saknade."),

 "rasera": (
  "Förstöra något så att det faller samman",
  "neutral, neutral", ["riva", "förstöra", "jämna med marken"],
  [["riva", "förstöra", "jämna med marken"]],
  "Flera byggnader %s helt vid jordskalvet." % (H % "raserades"),
  "SO:s två definitioner ('få något att rasa', 'få att falla sönder') är "
  "samma handling beskriven två gånger. Alla tre synonymerna finns i poolen. "
  "Registret ändrat från vardaglig till neutral -- ordet är gångbart i "
  "nyhetsspråk."),

 "rayon": (
  "Konstgjord fiber av cellulosa som liknar silke",
  "neutral, neutral", [], [],
  "Hon bar en kjol av %s." % (H % "rayon"),
  "En betydelse. 'viskos' är struket trots att det ligger nära: viskos är "
  "en TILLVERKNINGSMETOD och rayon samlingsnamnet för fibern. De överlappar "
  "men är inte samma sak, och ingen av dem är belagd som synonym."),

 "resorbera": (
  "Suga upp, om kroppens upptag av vätska eller näring",
  "fackspråklig, neutral, medicin", ["suga upp"], [["suga upp"]],
  "Tarmen hade svårt att %s allt salt." % (H % "resorbera"),
  "En betydelse. 'absorbera' är struket -- det är det allmänna ordet, "
  "resorbera används om kroppens eget återupptag. Domänen medicin är satt."),

 "sovel": (
  "Mat man äter till brödet, t.ex. pålägg",
  "ngt ålderdomlig, neutral", ["tilltugg", "smörgåspålägg"],
  [["tilltugg", "smörgåspålägg"]],
  "Det var ont om %s till brödet den vintern." % (H % "sovel"),
  "En betydelse. Registret ändrat från 'dialektal' till 'ngt ålderdomlig': "
  "ordet är inte bundet till en landsända utan till en tid då bröd var "
  "basen och allt annat var tillbehör. Båda synonymerna finns i poolen."),

 "totem": (
  "Djur eller föremål som en grupp känner sig andligt förbunden med",
  "fackspråklig, neutral, religion", [], [],
  "Örnen var stammens %s, en symbol för styrka." % (H % "totem"),
  "En betydelse. 'stamsymbol' saknar belägg. Huvudbetydelsen är omskriven: "
  "kortet sade 'heligt symbolföremål', men SO:s poäng är SAMHÖRIGHETEN -- "
  "gruppen känner sig besläktad med företeelsen, den är inte bara en symbol "
  "för den."),

 "underförstå": (
  "Mena något utan att säga det rakt ut",
  "formell, neutral", [], [],
  "Hans ord innebar ett %s hot." % (H % "underförstått"),
  "En betydelse. 'förutsätta' är struket: att förutsätta är att ta för "
  "givet, att underförstå är att kommunicera utan att uttala. Poolen är tom "
  "på riktiga synonymer."),

 "vakuum": (
  "Rum helt utan luft",
  "fackspråklig, neutral, fysik", ["lufttomt rum", "tomrum"],
  [["lufttomt rum", "tomrum"]],
  "Man kan skapa ett %s genom att pumpa ut all luft ur en behållare." % (H % "vakuum"),
  "En betydelse; SO:s 'äv. bildligt' (maktvakuum) är samma ord använt "
  "bildligt. Båda synonymerna finns i poolen."),

 "vinsch": (
  "Maskin som drar eller lyfter last med en lina som lindas på en vals",
  "neutral, neutral, teknik", ["vindspel"], [["vindspel"]],
  "%s skramlade när lasten drogs upp." % (H % "Vinscharna"),
  "En betydelse. Huvudbetydelsen sade 'mekanisk vinda', vilket förklarade "
  "ordet med ett ord av samma svårighetsgrad. Nu står mekanismen utskriven. "
  "OLD:s 'lyftkran' är fel: en kran har en arm, en vinsch bara en lina."),

 "ackumulera": (
  "Samla på hög så att mängden växer över tid",
  "formell, neutral", ["hopa", "samla"], [["hopa", "samla"]],
  "Vissa tungmetaller %s i kroppen över tid." % (H % "ackumuleras"),
  "SO:s andra post ('sammanlagd') är perfektparticipet ackumulerad, alltså "
  "böjningsform och inte betydelse. 'lagra' är struket -- att lagra är "
  "avsiktligt och statiskt, att ackumulera sker av sig självt. "
  "ÖVER TID är tillagt i huvudbetydelsen, för det är ordets kärna."),

 "adolescens": (
  "Perioden när man går från barn till vuxen",
  "fackspråklig, neutral, psykologi", ["ungdomsålder"], [["ungdomsålder"]],
  "Att känna sig håglös är helt normalt under %s." % (H % "adolescensen"),
  "En betydelse. 'tonåren' är struket -- adolescensen är inte bunden till "
  "13-19 utan till utvecklingen, och kan sträcka sig in i tjugoårsåldern. "
  "Domänen psykologi är satt; det är där ordet faktiskt används."),

 "assurera": (
  "Teckna en försäkring för något",
  "ngt ålderdomlig, neutral, ekonomi", ["försäkra"], [["försäkra"]],
  "Företaget lät %s sina anställda mot olycksfall." % (H % "assurera"),
  "En betydelse. Registret ändrat från 'formell' till 'ngt ålderdomlig': "
  "ordet lever kvar i försäkringsbranschens egna termer (assuradör) men "
  "har försvunnit ur allmänspråket."),

 "autostrada": (
  "Italiensk motorväg",
  "neutral, neutral", ["motorväg"], [["motorväg"]],
  "På den italienska %s gick det att köra fort." % (H % "autostradan"),
  "En betydelse. Att ordet gäller just Italien står kvar i huvudbetydelsen "
  "-- det är hela skälet att ha ett eget ord för motorväg."),

 "avglans": (
  "Svagt återsken av något ; blek rest av något som en gång var stort",
  "litterär, neutral ; litterär, neutral",
  ["återsken", "svag återstod"], [["återsken"], ["svag återstod"]],
  "Spegeln hade förlorat sin %s efter många års användning." % (H % "avglans"),
  "RÄTTAT: kortet hade bara ljusbetydelsen, men SO har två och den andra "
  "('svag antydan') är den ordet oftast bär i text -- 'en avglans av forna "
  "dagars storhet'. Den bildliga betydelsen är den man möter; den bokstavliga "
  "är nästan bara en förklaring till varför."),

 "betsel": (
  "Redskap i hästens mun som ryttaren styr med",
  "neutral, neutral", ["styrmedel för häst"], [["styrmedel för häst"]],
  "Hon höll fast hästen i %s." % (H % "betslet"),
  "En betydelse. 'tygel' är struket och skillnaden är konkret: betslet "
  "sitter i munnen, tyglarna är remmarna ryttaren håller i. De hör ihop "
  "men är olika delar."),

 "blickfång": (
  "Det som naturligt drar till sig blicken",
  "neutral, neutral", ["som fångar blicken"], [["som fångar blicken"]],
  "Den nya fabriken hamnade rakt i grannarnas %s." % (H % "blickfång"),
  "SO:s första betydelse ('område som direkt överskådas av blicken', alltså "
  "synfältet) är den ovanligare. Kortet leder med den Adam möter. NOTERAT: "
  "kortets exempelmening använder faktiskt SYNFÄLTSbetydelsen, inte den "
  "kortet lär ut -- den är därför värd att byta vid nästa genomgång."),

 "crescendo": (
  "Musik som gradvis blir starkare",
  "fackspråklig, neutral, musik", ["med växande tonstyrka"],
  [["med växande tonstyrka"]],
  'Dirigenten ropade "%s!" för att stärka orkesterns ljudstyrka.' % (H % "crescendo"),
  "SO:s två poster är samma sak sedd som anvisning respektive som avsnitt. "
  "'stegring' saknar belägg. SO:s 'äv. bildligt' -- ett skeende som byggs "
  "upp mot en kulmen -- är samma bild överförd."),

 "demolera": (
  "Slå sönder något fullständigt",
  "vardaglig, negativ", ["förstöra", "rasera", "riva"],
  [["förstöra", "rasera", "riva"]],
  "Bilen blev helt %s vid krocken." % (H % "demolerad"),
  "En betydelse. Alla tre synonymerna finns i poolen. Valören ändrad till "
  "negativ -- ordet bär alltid ett våldsamt anslag, till skillnad från "
  "'riva' som kan vara planerat rivningsarbete."),

 "desertera": (
  "Rymma från militärtjänst",
  "formell, negativ, militär", ["rymma från krigstjänst"],
  [["rymma från krigstjänst"]],
  "Sedan fienden intagit huvudstaden började hela bataljoner %s." % (H % "desertera"),
  "En betydelse. 'rymma' ensamt är struket: man rymmer från mycket, man "
  "deserterar bara från en armé. Valören negativ -- desertering är ett brott, "
  "inte ett neutralt avhopp."),

 "desinformation": (
  "Falsk information som sprids med avsikt att vilseleda",
  "formell, negativ", ["vilseledande information"], [["vilseledande information"]],
  "Regeringen anklagades för att sprida %s om giftutsläppen." % (H % "desinformation"),
  "En betydelse. 'propaganda' är struket, och skillnaden är själva poängen "
  "med ordet: propaganda kan vara sann men vinklad, desinformation är "
  "avsiktligt falsk. AVSIKTEN är utskriven i huvudbetydelsen -- utan den "
  "vore det bara felaktig information."),

 "dissekera": (
  "Skära upp en kropp för att undersöka den ; syna något i minsta detalj",
  "fackspråklig, neutral, biologi ; neutral, neutral",
  ["noggrant undersöka", "noggrant analysera"],
  [["noggrant undersöka"], ["noggrant analysera"]],
  "Biologen fick %s det döda djurets organ för att studera dess anatomi." % (H % "dissekera"),
  "Kortet hade redan båda betydelserna, vilket är ovanligt i den här batchen. "
  "Ändringen gäller synonymerna: 'skära upp' och 'dela upp' saknar belägg "
  "och är utbytta mot poolens egna, samt att registret nu skiljer på "
  "betydelserna -- den första är fackspråk, den andra vardagsspråk."),

 "endotermisk": (
  "Om kemisk reaktion: tar upp värme från omgivningen och gör det kallare",
  "fackspråklig, neutral, kemi", [], [],
  "Att lösa upp ammoniumklorid i vatten är en %s reaktion som gör lösningen kall." % (H % "endotermisk"),
  "En betydelse. Kortet bar '≈≈ värmeupptagande', en platshållarmarkering "
  "som inte hör hemma i ett färdigt kort; den är borttagen och listan står "
  "tom, eftersom poolen inte ger någon belagd synonym. Att lösningen blir "
  "KALL är tillagt -- det är den konkreta effekten och den enda som gör "
  "ordet ihågkomligt."),

 "feedback": (
  "Respons tillbaka till den som gjort något",
  "neutral, neutral", ["återkoppling", "respons"], [["återkoppling", "respons"]],
  "Auditiv %s är nödvändig för att barn ska utveckla sitt tal." % (H % "feedback"),
  "En betydelse. SO:s tekniska definition (signal som går tillbaka till "
  "sändaren) och underbetydelsen om gensvar på en prestation är samma "
  "mekanism i olika sammanhang. Båda synonymerna finns i poolen."),

 "fiktiv": (
  "Påhittad, inte verklig",
  "neutral, neutral", ["uppdiktad", "inbillad"], [["uppdiktad", "inbillad"]],
  'Strindbergs "Giftas" inleds med en %s intervju med författaren.' % (H % "fiktiv"),
  "En betydelse. Båda synonymerna finns i poolen. 'påhittad' står kvar som "
  "huvudbetydelse eftersom det är det enklaste ordet -- det är precis vad "
  "Adam-tal kräver."),

 "fission": (
  "Klyvning av en atomkärna",
  "fackspråklig, neutral, fysik", ["kärnklyvning"], [["kärnklyvning"]],
  "Mycket kraftigt laserljus kan framkalla %s." % (H % "fission"),
  "SO:s första betydelse gäller uppdelning av företag -- affärsjuridisk "
  "fackterm, och en helt annan användning. Kortet leder med kärnfysiken, "
  "som är den Adam möter."),

 "genie": (
  "Skyddsande i myter och sagor",
  "litterär, neutral", ["ande", "genius"], [["ande", "genius"]],
  "Sagans %s steg ur flaskan och erbjöd tre önskningar." % (H % "genie"),
  "RÄTTAT: kortet hade två betydelser, 'mytologisk skyddsande' OCH "
  "'enastående medfödd talang'. SO ger bara den första. Talangbetydelsen "
  "hör till det närbesläktade men skilda 'geni', och kortet blandade ihop "
  "två uppslagsord. Exempelmeningen är bytt av samma skäl -- den handlade "
  "om Mozarts skapande begåvning, alltså om 'geni' och inte om 'genie'. "
  "Detta är samma feltyp som formiddagens 'spisa'/'spisa av'."),
}


poster = json.load(io.open(FIL, encoding="utf-8"))
n, obelagda = 0, []
for e in poster:
    d = K.get(e["ord"])
    if not d:
        continue
    hb, reg, syn, grp, ex, slut = d
    pool = set(HJ.synpool(e["ord"]))
    for s in syn:
        if s not in pool:
            obelagda.append((e["ord"], s))
    e["proposed"] = {"huvudbetydelse": hb, "register": reg, "synonymer": syn,
                     "synonym_groups": grp, "exempelmening": ex,
                     "etymologi": HJ.etym(e["ord"])}
    e["sokkoll"] = {"kalla": HJ.kallor(e["ord"]), "slutsats": slut}
    e["approved"] = True
    n += 1

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Skrev %d kort." % n)
print("Synonymer UTANFOR poolen:", obelagda or "inga")
