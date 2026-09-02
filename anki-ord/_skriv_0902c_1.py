# -*- coding: utf-8 -*-
"""Arbetsbatch 2026-09-02c, kort 0-33.

Fyra regler ligger inbakade fran borjan i stallet for att rattas i efterhand,
en for varje sak som kostade tid i dagens tva foregaende batchar:

  1. ALLA numrerade SO-betydelser kommer med. Att valja bort en och skriva en
     motivering fungerar inte -- motiveringen nar aldrig blindgranskaren
     (paket() utelamnar den avsiktligt), sa bortvalet ser ut som ett
     forbiseende och underkanns. Mott: 3 av 25 i forsta omgangen.
     UNDANTAGET ar betydelser som bara finns i en FAST FRAS -- granskaren
     underkande `koloss` och `profetia` for att jag skrivit ut 'koloss pa
     lerfotter' och 'sjalvuppfyllande profetia' som egna betydelser av
     grundordet. En fast fras ar inte en betydelse hos ordet i sig.
  2. Varje enskilt ord far minst en synonym -- exakt, `≈` eller `≈≈`.
  3. Synonymer bara ur `_hjalp_0902c.synpool()`, aldrig ur minnet.
  4. Inga deck-ord i huvudbetydelsen (svarighetskoll.py).
"""
import io, json, sys
import _hjalp_0902b as HJ

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02c_v3-batch.json"
H = HJ.H

K = {
 "bindel": (
  "Band som knyts runt en kroppsdel",
  "neutral, neutral", ["band"], [["band"]],
  "Han fick en %s för ögonen innan överraskningsfesten avslöjades." % (H % "bindel"),
  "En betydelse i SO. 'förband' och 'bandage' är strukna -- de är till för att "
  "täcka sår, medan en bindel lika gärna kan sitta för ögonen, vilket "
  "exempelmeningen visar. 'linda' saknar ordboksbelägg."),

 "lira": (
  "Spela, särskilt boll",
  "vardaglig, neutral", ["spela"], [["spela"]],
  "Han %s fotboll med sin kompis i parken varje kväll." % (H % "lirade"),
  "SO:s artikel drar in tre olika ord: instrumentet lira (vevlira), "
  "stormfågeln lira och verbet lira 'spela'. Bara det sista är Adams kort -- "
  "de andra är HOMONYMER, alltså skilda ord som råkat sammanfalla, inte "
  "betydelser hos samma ord. 'trixa' och 'spela boll' saknar belägg."),

 "motto": (
  "Kort mening som säger vad man står för",
  "neutral, neutral", ["valspråk", "sentens"], [["valspråk", "sentens"]],
  '%s "Känn ditt land" präglades under Turistföreningens första år.' % (H % "Mottot"),
  "En betydelse. Båda synonymerna finns i poolen. 'devis' och 'slagord' är "
  "strukna som obelagda; ett slagord säljer dessutom något, ett motto "
  "uttrycker en hållning."),

 "prioritera": (
  "Ge företräde åt det viktigaste ; ge något lägre företräde och skjuta upp det",
  "formell, neutral ; formell, neutral",
  ["ge företräde åt", "välja bort"], [["ge företräde åt"], ["välja bort"]],
  "Banken behandlade skulden som en %s fordran vid konkursen." % (H % "prioriterad"),
  "RÄTTAT: kortet hade en betydelse, SO har två motsatta -- att ge företräde "
  "OCH att ge lägre prioritet (bortprioritera). Den andra saknades helt, "
  "trots att den är minst lika vanlig i myndighetsspråk. 'rangordna' och "
  "'främja' saknar belägg."),

 "snörvla": (
  "Andas med bubblande ljud genom näsan ; tala otydligt med täppt näsa",
  "vardaglig, neutral ; vardaglig, neutral",
  ["andas med bubblande ljud genom näsan", "tala otydligt"],
  [["andas med bubblande ljud genom näsan"], ["tala otydligt"]],
  "De hostande och %s barnen satt hemma med förkylning hela veckan." % (H % "snörvlande"),
  "RÄTTAT: SO har två betydelser och kortet hade en. 'fnysa' och 'rossla' är "
  "strukna: att fnysa är ett kort utandningsljud av förakt, att rossla sker "
  "i halsen. Båda är fel plats i kroppen."),

 "veritabel": (
  "Som verkligen är det ordet säger",
  "formell, neutral", ["sannskyldig", "äkta", "verklig"],
  [["sannskyldig", "äkta", "verklig"]],
  "Fiskarens sista kast var ett %s mästarkast som avgjorde tävlingen." % (H % "veritabelt"),
  "En betydelse. Alla tre synonymerna finns i poolen. Kortet är i sak "
  "oförändrat -- formuleringen 'inte överdrivet' är struken eftersom ordet "
  "tvärtom nästan alltid FÖRSTÄRKER ('ett veritabelt kaos')."),

 "vulgär": (
  "Som visar tydlig brist på smak och bildning",
  "neutral, nedsättande", ["simpel", "grov", "ohyfsad"],
  [["simpel", "grov", "ohyfsad"]],
  "Hans %s skämt fick flera gäster att resa sig och gå." % (H % "vulgära"),
  "En betydelse; SO:s 'äv. om person' är samma omdöme riktat mot någon i "
  "stället för mot ett beteende. 'tarvlig' är struket som obelagt. Registret "
  "ändrat från formell till neutral -- ordet används i vanligt tal."),

 "adjutant": (
  "Officer som hjälper en hög chef med det praktiska",
  "formell, neutral, militär", ["officer"], [["officer"]],
  "%s följde generalen på alla hans resor och skötte den dagliga planeringen." % (H % "Adjutanten"),
  "En betydelse. Synonymraden var TOM och är nu fylld ur poolen. "
  "Huvudbetydelsen säger nu OFFICER, inte bara 'person' -- det är en "
  "militär befattning, inte vilken medhjälpare som helst."),

 "aktuell": (
  "Som tilldrar sig uppmärksamhet just nu ; som finns i tankarna för tillfället ; som planeras för närvarande",
  "neutral, neutral ; neutral, neutral ; neutral, neutral",
  ["giltig", "≈≈ närvarande", "≈≈ planerad"],
  [["giltig"], ["≈≈ närvarande"], ["≈≈ planerad"]],
  "Klimatfrågan är mer %s än någonsin i årets valrörelse." % (H % "aktuell"),
  "RÄTTAT: kortet hade EN betydelse, SO har tre. De två som saknades är "
  "'som finns i medvetandet vid det givna tillfället' (den aktuella frågan) "
  "och 'som planeras för närvarande' (aktuell för tjänsten). Synonymraden "
  "var dessutom tom."),

 "amöba": (
  "Encelligt djur som ändrar form hela tiden ; bildligt om en slö och oföretagsam person",
  "neutral, neutral, biologi ; vardaglig, nedsättande",
  ["ett encelligt urdjur", "≈≈ slöfock"],
  [["ett encelligt urdjur"], ["≈≈ slöfock"]],
  "%s rör sig genom att bukta ut sitt cellmembran." % (H % "Amöban"),
  "Kortet hade båda betydelserna. 'urdjur' ensamt saknar belägg och är bytt "
  "mot poolens fullständiga form; den bildliga betydelsen har fått kategori."),

 "autism": (
  "Funktionsnedsättning som bland annat gör socialt samspel svårt",
  "neutral, neutral, medicin", ["≈≈ funktionsnedsättning"],
  [["≈≈ funktionsnedsättning"]],
  "%s påverkar hur hjärnan hanterar social information." % (H % "Autism"),
  "En betydelse. Synonymraden var tom; poolen ger bara definitionen ordagrant, "
  "så kategorin används. OLD:s 'självförsjunkenhet' är en föråldrad och "
  "missvisande beskrivning och är inte använd."),

 "bipolär": (
  "Som har två motsatta poler ; som pendlar mellan två ytterlägen",
  "formell, neutral ; fackspråklig, neutral, medicin",
  ["tvåpolig", "≈≈ växlande"], [["tvåpolig"], ["≈≈ växlande"]],
  "Debatten fick en %s karaktär där åsikterna delade sig i två skarpt motsatta läger." % (H % "bipolär"),
  "RÄTTAT: synonymen 'bipolär sjukdom' innehöll uppslagsordet och avslöjade "
  "svaret rakt av -- den flaggades som cirkulär. 'manodepressiv' saknar "
  "belägg. Den psykiatriska användningen är SO:s underbetydelse 'ofta "
  "utvidgat, särsk. medicin' av betydelse 2, och ligger därför där."),

 "böjelse": (
  "Stadig dragning åt något ; särskild förkärlek",
  "litterär, neutral ; litterär, neutral",
  ["lust", "förkärlek"], [["lust"], ["förkärlek"]],
  "Hans olyckliga %s för sprit ledde till hans fall." % (H % "böjelse"),
  "RÄTTAT: SO har två betydelser och kortet hade en. 'tendens' saknar "
  "belägg och är dessutom svagare -- en tendens är statistisk, en böjelse "
  "personlig."),

 "centrera": (
  "Placera något mitt på en yta ; rikta in mot en enda punkt",
  "neutral, neutral ; neutral, neutral",
  ["placera i centrum", "inrikta"], [["placera i centrum"], ["inrikta"]],
  "Han %s ringen så den satt mitt i hålet." % (H % "centrerade"),
  "Kortet hade båda betydelserna. Ändringen gäller synonymgrupperna: den "
  "första stod utan synonym trots att poolen har en."),

 "croissant": (
  "Halvmåneformat frukostbröd av smördeg",
  "neutral, neutral, matlagning", ["halvmånformigt bröd av smördeg"],
  [["halvmånformigt bröd av smördeg"]],
  "Jag åt en %s med smör och marmelad till frukost." % (H % "croissant"),
  "En betydelse. Synonymraden var tom och är fylld ur poolen. Etymologin är "
  "värd att ha: franskans croissant betyder 'växande' och syftar på "
  "månskäran -- samma bild som formen."),

 "dassig": (
  "I dåligt skick, hängig",
  "vardaglig, lätt negativ", ["dålig", "trist"], [["dålig", "trist"]],
  "Efter ett par sömnlösa nätter kände hon sig rätt %s." % (H % "dassig"),
  "En betydelse. 'krasslig' och 'vissen' saknar belägg. Poolens 'ful' är "
  "utelämnad -- den gäller saker, inte hur man mår, och kortet handlar om "
  "det senare."),

 "destillera": (
  "Skilja en vätskas delar åt genom att koka och kyla",
  "fackspråklig, neutral, kemi", ["skilja vätskor åt genom uppvärmning och kondensering"],
  [["skilja vätskor åt genom uppvärmning och kondensering"]],
  "På destilleriet lärde hon sig att %s whisky." % (H % "destillera"),
  "SO har EN betydelse; den bildliga ('äv. bildligt') är samma handling "
  "överförd på tankar och är inte en egen betydelse. Kortet bar den som en "
  "andra betydelse och är därför förkortat. Synonymraden var tom."),

 "dividera": (
  "Dela ett tal med ett annat ; hålla på och diskutera fram och tillbaka",
  "neutral, neutral, matematik ; vardaglig, lätt negativ",
  ["dela", "samtala hit och dit"], [["dela"], ["samtala hit och dit"]],
  "%s 15 med 3 så får du 5." % (H % "Dividera"),
  "Kortet hade båda betydelserna. Andra gruppen stod utan synonym och har "
  "fått poolens egen."),

 "dåsig": (
  "Halvsovande och loj",
  "vardaglig, neutral", ["≈≈ trött"], [["≈≈ trött"]],
  "Hon kände sig %s efter den tunga middagen." % (H % "dåsig"),
  "En betydelse. 'slö' och 'sömnig' saknar båda ordboksbelägg -- poolen ger "
  "bara SO:s definition ordagrant -- så kategorin används i stället."),

 "exotisk": (
  "Som kommer från fjärran, ofta tropiska länder ; främmande och ovanlig",
  "neutral, positiv ; neutral, neutral",
  ["från fjärran land", "främmande", "sällsam", "ovanlig"],
  [["från fjärran land"], ["främmande", "sällsam", "ovanlig"]],
  "Djurparken hade en avdelning full av %s djur från hela världen." % (H % "exotiska"),
  "Kortet hade båda betydelserna. Ändringen gäller grupperna: alla tre "
  "synonymer låg på den första betydelsen, men de hör till den andra -- "
  "främmande och sällsam säger ingenting om geografi."),

 "feromon": (
  "Doftämne som djur av samma art skickar signaler med",
  "fackspråklig, neutral, biologi", ["doftämne"], [["doftämne"]],
  "Honan sänder ut ett %s som lockar till sig hannarna." % (H % "feromon"),
  "En betydelse. Synonymraden var tom och är fylld ur poolen."),

 "fibrill": (
  "Mycket tunn tråd i kroppens vävnad",
  "fackspråklig, neutral, biologi", ["mikroskopisk fiber"],
  [["mikroskopisk fiber"]],
  "Spermiens svans består av ett knippe %s." % (H % "fibriller"),
  "En betydelse. 'tråd' ensamt saknar belägg och är bytt mot poolens "
  "fullständiga form."),

 "fortskaffningsmedel": (
  "Något man förflyttar sig med",
  "formell, neutral", ["transportmedel", "färdmedel"],
  [["transportmedel", "färdmedel"]],
  "Cykeln är ett hälsosamt %s." % (H % "fortskaffningsmedel"),
  "En betydelse. Båda synonymerna finns i poolen. Kortet var redan korrekt "
  "och behålls i sak."),

 "fusionera": (
  "Slå samman två företag till ett",
  "formell, neutral, ekonomi", ["gå samman", "slå samman", "smälta samman"],
  [["gå samman", "slå samman", "smälta samman"]],
  "De två bankerna beslutade att %s nästa år." % (H % "fusionera"),
  "En betydelse. Alla tre synonymerna finns i poolen."),

 "geografi": (
  "Vetenskapen om jordytan och hur människor använder den ; själva terrängen på en plats",
  "neutral, neutral ; vardaglig, neutral",
  ["vetenskapen om jordytan", "≈≈ terräng"],
  [["vetenskapen om jordytan"], ["≈≈ terräng"]],
  "Han älskade %s och kunde namnge alla världens huvudstäder utantill." % (H % "geografi"),
  "Kortet hade båda betydelserna men stod utan synonymer. SO:s andra "
  "definition är avhuggen i uppslaget ('ut i omgivande natur') -- den gäller "
  "uttrycket 'ut i geografin', alltså terrängen, vilket kortet redan fångat."),

 "grädda": (
  "Tillaga i ugn eller stekpanna så ytan bryns ; det finaste skiktet i samhället",
  "neutral, neutral, matlagning ; vardaglig, neutral",
  ["bereda i ugn el. stekpanna", "elit"],
  [["bereda i ugn el. stekpanna"], ["elit"]],
  "Varje söndag brukade pappa %s pannkakor till hela familjen." % (H % "grädda"),
  "Kortet hade båda betydelserna. 'eliten' i bestämd form saknade belägg och "
  "är bytt mot poolens 'elit'. Andra betydelsen är egentligen substantivet "
  "grädda ('societetens grädda'), som SO för till samma artikel."),

 "insinuation": (
  "Antydan som svärtar ner någon utan att säga det rakt ut",
  "formell, negativ", ["försåtlig antydan", "beskyllning"],
  [["försåtlig antydan", "beskyllning"]],
  "Journalisternas %s om korruption fick borgmästaren att avgå." % (H % "insinuationer"),
  "En betydelse. Synonymraden var tom och är fylld ur poolen."),

 "kibbutz": (
  "Israelisk gård där en grupp bor och arbetar tillsammans",
  "neutral, neutral", ["israeliskt jordbrukskollektiv"],
  [["israeliskt jordbrukskollektiv"]],
  "Flera nya %s anlades i gränstrakterna." % (H % "kibbutzer"),
  "En betydelse. 'kollektivjordbruk' och 'jordbrukskollektiv' saknar belägg "
  "var för sig; poolens fullständiga form används."),

 "kineseri": (
  "Europeisk stil som härmar kinesisk konst ; onödigt krångliga formaliteter",
  "fackspråklig, neutral, konst ; neutral, negativ",
  ["efterlikning av kinesisk konst", "meningslöst formtvång"],
  [["efterlikning av kinesisk konst"], ["meningslöst formtvång"]],
  "Slottets inredning var präglad av 1700-talets förtjusning i %s." % (H % "kineserier"),
  "Kortet hade båda betydelserna. 'kinesisk stil', 'efterbildning' och "
  "'exotism' saknar alla belägg och är utbytta mot poolens egna."),

 "lateral": (
  "Belägen vid sidan av något",
  "fackspråklig, neutral, medicin", ["sidoställd", "sido-"],
  [["sidoställd", "sido-"]],
  "%s rörelser är viktiga för god balans." % (H % "Laterala"),
  "SO:s andra och tredje poster gäller det språkvetenskapliga l-ljudet -- "
  "hur det bildas, respektive ljudet självt. Det är fonetikens fackterm och "
  "en annan sak än den anatomiska riktningsbetydelsen kortet lär ut; "
  "domänen medicin är satt eftersom det är där Adam möter ordet."),

 "limit": (
  "Övre eller undre gräns man måste hålla sig inom",
  "neutral, neutral", ["gräns för kredit"], [["gräns för kredit"]],
  "Banken höjde hans %s på kreditkortet." % (H % "limit"),
  "SO:s andra betydelse är pokerns satsningsgräns -- spelterm. 'gräns' "
  "ensamt saknar belägg; poolens fullständiga form används och passar "
  "exempelmeningen."),

 "nedlåtande": (
  "Som behandlar andra som mindre värda",
  "neutral, nedsättande", ["högdragen", "föraktfull"],
  [["högdragen", "föraktfull"]],
  "Chefen gav honom en %s blick när han föreslog idén." % (H % "nedlåtande"),
  "En betydelse. Båda synonymerna finns i poolen. Kortet var redan korrekt."),

 "optimal": (
  "Så bra som det över huvud taget kan bli i just den situationen",
  "neutral, positiv", ["bästa möjliga"], [["bästa möjliga"]],
  "Vinklarna gav %s ljus i rummet hela eftermiddagen." % (H % "optimalt"),
  "SO:s andra definition ('som är så stor som möjligt') är samma "
  "maximeringstanke uttryckt om storlek -- inte en egen betydelse, utan "
  "vad som optimeras."),

 "platonsk": (
  "Som hör till filosofen Platon ; fri från kroppslig lust",
  "fackspråklig, neutral, filosofi ; neutral, neutral",
  ["platonisk", "passionsfri"], [["platonisk"], ["passionsfri"]],
  "Deras vänskap var djup men helt %s." % (H % "platonsk"),
  "Kortet hade båda betydelserna. SO:s tredje post ('passionsfri, sval') är "
  "samma betydelse som den andra, uttryckt med andra ord. Första gruppen "
  "stod utan synonym och har fått poolens 'platonisk'."),
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
        if not s.startswith("≈") and s not in pool:
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
