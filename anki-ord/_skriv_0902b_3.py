# -*- coding: utf-8 -*-
"""Arbetsbatch 2026-09-02b, kort 66-99. Sista tredjedelen."""
import io, json, sys
import _hjalp_0902b as HJ

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02b_v3-batch.json"
H = HJ.H

K = {
 "glaukom": (
  "Ögonsjukdom där trycket i ögat stiger och synen gradvis förstörs",
  "fackspråklig, neutral, medicin", ["grön starr"], [["grön starr"]],
  "%s kan leda till blindhet om det inte behandlas i tid." % (H % "Glaukom"),
  "En betydelse. 'grön starr' är det svenska namnet och finns i poolen. "
  "Huvudbetydelsen är kompletterad med att förloppet är GRADVIS -- det är "
  "därför sjukdomen är farlig, den märks inte förrän skadan är gjord."),

 "homofon": (
  "Ord som uttalas likadant som ett annat men betyder något annat",
  "fackspråklig, neutral, lingvistik", [], [],
  'Orden "själ", "skäl" och "stjäl" är %s.' % (H % "homofoner"),
  "SO:s andra betydelse är musikalisk (om sats med en enda melodiförande "
  "stämma) och är fackterm i ett annat fält. Kortet håller sig till "
  "språkvetenskapen, som är den betydelse Adam möter. 'likljudande ord' "
  "saknar belägg som fristående synonym."),

 "irrelevant": (
  "Som saknar betydelse för det man talar om",
  "formell, neutral", ["ovidkommande", "betydelselös"],
  [["ovidkommande", "betydelselös"]],
  "Anmärkningen var intressant men helt %s för fallet." % (H % "irrelevant"),
  "En betydelse. Båda synonymerna finns i poolen. Huvudbetydelsen är "
  "omskriven till vardagsord: 'i sammanhanget' är ordboksprosa, 'för det "
  "man talar om' är hur man faktiskt säger det."),

 "järv": (
  "Kraftigt mårddjur, mörkbrunt och kortsvansat, som fäller djur mycket större än sig självt",
  "neutral, neutral, biologi", ["kortsvansat mårddjur"], [["kortsvansat mårddjur"]],
  "%s kan riva renar och unga älgar." % (H % "Järven"),
  "En betydelse. Huvudbetydelsen är utbyggd med det som gör djuret värt "
  "att minnas -- att det tar byten långt över sin egen storlek. 'mårddjur' "
  "ensamt är för brett: det omfattar också mård, utter och grävling."),

 "kardiologi": (
  "Läran om hjärtat och dess sjukdomar",
  "fackspråklig, neutral, medicin", [], [],
  "Patienten remitterades till %s för utredning av sitt hjärtproblem." % (H % "kardiologi"),
  "En betydelse. 'hjärtläran' saknar ordboksbelägg och är dessutom ett ord "
  "ingen använder. Poolen är tom på riktiga synonymer."),

 "kiropraktor": (
  "Behandlare som arbetar med ryggrad och leder med händerna",
  "neutral, neutral, medicin", ["utövare av kiropraktik"],
  [["utövare av kiropraktik"]],
  "En %s behandlade hennes ryggsmärtor." % (H % "kiropraktor"),
  "En betydelse. 'kotknackare' är struket -- det är ett skämtsamt öknamn "
  "och saknar belägg som synonym. Huvudbetydelsen säger nu MED HÄNDERNA, "
  "vilket är det som skiljer yrket från andra ryggbehandlare."),

 "kollaps": (
  "Plötsligt och fullständigt sammanbrott",
  "neutral, neutral", ["sammanbrott"], [["sammanbrott"]],
  "Transportsystemet drabbades av %s vid elavbrottet." % (H % "kollaps"),
  "En betydelse; SO:s 'spec. hopfallande av lunga' är medicinsk fackterm "
  "för samma skeende. 'ras' är struket -- ett ras är fysiskt, en kollaps "
  "kan gälla ett system, en marknad eller en människa."),

 "kontinental": (
  "Som hör till fastlandet ; elegant och världsvan på europeiskt vis",
  "neutral, neutral ; neutral, positiv",
  ["fastlands-", "världsmannamässig"], [["fastlands-"], ["världsmannamässig"]],
  "Hotellet hade en %s atmosfär med marmor och kristallkronor." % (H % "kontinental"),
  "Kortet hade redan båda betydelserna. Ändringen gäller synonymerna: "
  "'kosmopolitisk' saknar belägg och är utbytt mot poolens "
  "'världsmannamässig'. Valören på andra betydelsen är satt till positiv "
  "-- ordet är beröm i den användningen."),

 "kvittens": (
  "Skriftligt bevis på att en betalning eller leverans tagits emot",
  "formell, neutral, ekonomi", ["kvitto"], [["kvitto"]],
  "Butiken utfärdade en %s när jag köpte kläderna." % (H % "kvittens"),
  "SO:s andra betydelse är växten kvitten (busken med päronlika frukter) -- "
  "ett annat ord som fuzzy-sökningen dragit in, och poolens 'päronlika "
  "frukter' kommer därifrån. Samma feltyp som formiddagens essens/ess. "
  "'betalningsbevis' saknar belägg; 'kvitto' finns i poolen, med "
  "reservationen att en kvittens är generellare än ett kvitto."),

 "lockrop": (
  "Läte som används för att locka till sig djur",
  "neutral, neutral", [], [],
  "Hannens %s hördes över hela myren." % (H % "lockrop"),
  "SO:s två definitioner skiljer på vem som ropar -- djuret självt eller "
  "boskapsskötaren -- men det är samma ljud med samma syfte. "
  "'locksignal' saknar belägg."),

 "långrandig": (
  "Tröttsamt utdragen",
  "neutral, lätt negativ", ["långtråkig"], [["långtråkig"]],
  "Filmen hade en %s handling som drog ut på tiden." % (H % "långrandig"),
  "SO:s första betydelse är den bokstavliga ('randig på längden'), men den "
  "används knappt -- ordet betyder i praktiken enformig. Kortet leder med "
  "den. 'monoton' är struket: monotont är enformigt utan att nödvändigtvis "
  "vara långt, långrandigt tröttar just genom LÄNGDEN. Huvudbetydelsen är "
  "skärpt så att tidsaspekten syns."),

 "morän": (
  "Blandning av grus och sten som en glaciär lämnat efter sig",
  "fackspråklig, neutral, geologi", [], [],
  "Det kuperade landskapet bestod av %s som isen lämnat efter sig för tusentals år sedan." % (H % "morän"),
  "En betydelse. 'bergart' är struket och det är ett riktigt fel: morän är "
  "en JORDART, alltså löst material, inte fast berg. 'jordmassor' saknar "
  "belägg. Att materialet är OSORTERAT -- allt från lerpartiklar till "
  "block om vartannat -- är det som gör morän igenkännbar i fält."),

 "narr": (
  "Löjlig och självgod person som andra skrattar åt",
  "neutral, nedsättande", ["gyckelmakare"], [["gyckelmakare"]],
  "Den gamle %s trodde att flickan verkligen hade fallit för hans charm." % (H % "narren"),
  "SO:s tredje betydelse är hovnarren, en historisk yrkesroll. Den ligger "
  "bakom ordet men är inte den man möter; kortet leder med den moderna. "
  "SO:s andra post ('få någon att framstå som löjlig') är verbet narra, ett "
  "annat uppslagsord. 'dumbom' och 'tok' saknar belägg. Valören skärpt "
  "från 'lätt negativ' till 'nedsättande' -- att kalla någon narr är ett "
  "hån, inte en mild anmärkning."),

 "oinvigd": (
  "Som står utanför och inte fått veta hur något ligger till",
  "neutral, neutral", [], [],
  "Facktermerna sa inte en %s så mycket." % (H % "oinvigd"),
  "En betydelse. 'ovetande' och 'utomstående' står i OLD men saknar "
  "ordboksbelägg, och poolen ger bara definitionsfragment. Ordets poäng är "
  "att kunskapen finns men undanhålls -- inte att den saknas i allmänhet."),

 "pardon": (
  "Skonsamhet i stället för straff",
  "ngt ålderdomlig, neutral", ["förskoning", "benådning"],
  [["förskoning", "benådning"]],
  "Regeringen gav inte upprorsmännen någon %s." % (H % "pardon"),
  "En betydelse. Båda synonymerna finns i poolen. Registret ändrat från "
  "'litterär' till 'ngt ålderdomlig': ordet lever nästan bara i den fasta "
  "vändningen 'ge/få ingen pardon'. 'nåd' är struket -- nåd är religiöst "
  "eller kungligt laddat på ett sätt pardon inte är."),

 "pugilist": (
  "Boxare",
  "ngt ålderdomlig, neutral, sport", ["boxare"], [["boxare"]],
  "Han var en skicklig %s som vann de flesta av sina matcher." % (H % "pugilist"),
  "En betydelse, och den enda synonymen är den ordboken själv ger. "
  "Registret ändrat från 'arkaisk' till 'ngt ålderdomlig' -- ordet dyker "
  "upp i sportjournalistik som medveten stilmarkör, alltså inte utdött."),

 "radiator": (
  "Värmeelement som värmer rummet genom att avge strålningsvärme",
  "neutral, neutral, teknik", ["värmeelement"], [["värmeelement"]],
  "%s i huset värms upp av centralvärmesystemet." % (H % "Radiatorerna"),
  "En betydelse. Poolens 'kylare' hör till bilmotorns radiator -- samma "
  "princip, motsatt syfte -- och är utelämnad för att inte förvirra. "
  "Registret ändrat från vardaglig till neutral."),

 "ratatouille": (
  "Fransk gryta på stuvade grönsaker",
  "neutral, neutral, matlagning", ["en fransk grönsaksrätt"],
  [["en fransk grönsaksrätt"]],
  "%s serverades ofta som huvudrätt på franska restauranger." % (H % "Ratatouille"),
  "En betydelse. 'grönsaksrätt' ensamt saknar belägg; poolens fullständiga "
  "form används i stället. Huvudbetydelsen säger STUVADE, vilket är det "
  "som skiljer rätten från en sallad."),

 "relik": (
  "Kvarleva av ett helgon, bevarad som helig",
  "fackspråklig, neutral, religion", [], [],
  "Munkarna vaktade en helig %s som sades vara ett finger från ett helgon." % (H % "relik"),
  "En betydelse; SO:s underbetydelse om föremål som RÖRT en helig person "
  "är samma kult i vidare mening. Kortet bar tre synonymer -- "
  "'helgonlämning', 'kvarleva', 'heliga föremål' -- varav ingen har "
  "ordboksbelägg som fristående synonym. 'kvarleva' ensamt är dessutom för "
  "brett: det heliga är hela poängen."),

 "statistisk": (
  "Som bygger på insamlade sifferuppgifter och deras analys",
  "formell, neutral, matematik", [], [],
  "Forskarna presenterade sina %s beräkningar i rapporten." % (H % "statistiska"),
  "SO:s två definitioner skiljer på metod och ämnesområde -- samma ord "
  "sett från två håll. 'siffermässig' saknar belägg och är dessutom "
  "missvisande: allt som rör siffror är inte statistiskt."),

 "stridsäpple": (
  "Fråga som ständigt vållar bråk",
  "neutral, neutral", ["tvistefråga"], [["tvistefråga"]],
  "Skolan blev ett av de stora %s i valrörelsen." % (H % "stridsäpplena"),
  "En betydelse. 'tvistefråga' finns i poolen. Registret ändrat från "
  "'litterär' till neutral -- uttrycket är vanligt i nyhetsspråk. "
  "Etymologin är värd att ha: det är Eris gyllene äpple, kastat bland "
  "gudarna med texten 'åt den skönaste', som utlöste trojanska kriget."),

 "taktfull": (
  "Som är noga med att inte såra andra",
  "neutral, positiv", ["finkänslig"], [["finkänslig"]],
  "Han var %s nog att inte nämna misstaget vid namn." % (H % "taktfull"),
  "En betydelse. 'hänsynsfull' är struket -- hänsyn gäller handlingar, takt "
  "gäller vad man säger och låter bli att säga. 'finkänslig' finns i poolen."),

 "trashank": (
  "Fattig person i trasiga kläder",
  "ngt ålderdomlig, nedsättande", ["fattig person"], [["fattig person"]],
  "Vid vägkanten satt en %s och tiggde." % (H % "trashank"),
  "SO:s två definitioner ('person klädd i trasor', 'mycket fattig person') "
  "är samma person beskriven utifrån och inifrån. 'slusk' och 'luffare' "
  "saknar belägg och betyder dessutom delvis annat -- en luffare är "
  "kringvandrande, en trashank behöver inte vara det."),

 "tryffel": (
  "Underjordisk svamp som räknas som delikatess ; chokladkonfekt med mjuk fyllning",
  "neutral, neutral, matlagning ; neutral, neutral, matlagning",
  ["tryffelsvamp", "en chokladmassa"], [["tryffelsvamp"], ["en chokladmassa"]],
  "Hunden var tränad att leta efter %s i skogen." % (H % "tryffel"),
  "Kortet hade båda betydelserna. Ändringen: 'svamp' och 'chokladkonfekt' "
  "saknar belägg som synonymer och är utbytta mot poolens egna, samt att "
  "huvudbetydelsen nu säger UNDERJORDISK -- det är därför man behöver hund "
  "för att hitta den, och det förklarar exempelmeningen."),

 "vagel": (
  "Varig inflammation i kanten av ögonlocket",
  "neutral, neutral, medicin", ["inflammation i ögonlocksrand"],
  [["inflammation i ögonlocksrand"]],
  "Hon fick en %s i ögat efter förkylningen." % (H % "vagel"),
  "SO:s andra betydelse är sittstången för höns -- ett homonym utan "
  "släktskap med ögonbetydelsen. Kortet leder med den Adam möter. "
  "'hordeolum' är struket: det är latin och förklarar ett svårt ord med "
  "ett svårare, vilket Adam-tal uttryckligen förbjuder. Registret ändrat "
  "från formell till neutral."),

 "vattenpuss": (
  "Liten vattenpöl på marken",
  "vardaglig, neutral", ["liten vattenpöl"], [["liten vattenpöl"]],
  "Barnen hoppade glatt i varenda %s på gården." % (H % "vattenpuss"),
  "En betydelse. 'pöl' ensamt saknar belägg; poolens fullständiga form "
  "används."),

 "versfot": (
  "Minsta rytmiska enhet i en vers, en grupp betonade och obetonade stavelser",
  "fackspråklig, neutral, litteraturvetenskap", [], [],
  "En anapest är en %s med två obetonade och en betonad stavelse." % (H % "versfot"),
  "En betydelse. 'takt' är struket -- takt är musikens enhet, versfot "
  "diktens, och de sammanfaller inte. Poolen ger bara definitionen i två "
  "längder."),

 "acceptans": (
  "Att något godtas av många",
  "formell, neutral", ["accepterande"], [["accepterande"]],
  "Att genomföra stora förändringar utan folklig %s är omöjligt." % (H % "acceptans"),
  "En betydelse. Huvudbetydelsen var 'Tendens till accepterande av en viss "
  "företeelse hos en viss grupp människor' -- ordboksprosa av det slag "
  "Adam-tal förbjuder, och den innehöll dessutom uppslagsordet självt "
  "('accepterande'). Nu står den i vardagsord."),

 "dyig": (
  "Full av lös gyttja",
  "neutral, neutral", [], [],
  "Sjöns botten var %s och svår att gå i." % (H % "dyig"),
  "En betydelse. 'gyttjig' och 'lerig' saknar båda ordboksbelägg, och "
  "'lerig' är dessutom fel: lera är fast och formbar, dy är lös och rutten. "
  "Poolen ger bara 'full av dy', alltså definitionen med uppslagsordet i."),

 "pivå": (
  "Tapp som något vrider sig kring",
  "fackspråklig, neutral, teknik", ["svängtapp", "tapp"], [["svängtapp", "tapp"]],
  "Fönstret satt på en %s och kunde vridas ett helt varv." % (H % "pivå"),
  "En betydelse. Båda synonymerna finns i poolen. Kortet var redan korrekt "
  "och behålls i sak."),

 "välboren": (
  "Av adlig släkt",
  "ngt ålderdomlig, neutral", ["av adlig börd"], [["av adlig börd"]],
  "Brevet var ställt till den %s herr baronen." % (H % "välborne"),
  "En betydelse. Huvudbetydelsen var SO:s definition ordagrant, inklusive "
  "parentesen '(låg)adlig'; nu står den i vardagsord. 'högättad' saknar "
  "belägg. Ordet levde främst som TILLTAL i brev, vilket exempelmeningen "
  "visar."),

 "dramatisera": (
  "Skriva om en berättelse till pjäs ; framställa något som mer omskakande än det var",
  "neutral, neutral, konst ; vardaglig, lätt negativ",
  ["omarbeta för teatern", "framställa"],
  [["omarbeta för teatern"], ["framställa"]],
  "Tidningen valde att %s den redan spännande händelsen." % (H % "dramatisera"),
  "Kortet hade båda betydelserna. Ändringen gäller synonymgrupperna: den "
  "andra betydelsen stod utan synonym trots att poolen har en. Den andra "
  "betydelsen är den Adam möter oftast och den enda som bär värdering -- "
  "att säga 'dramatisera inte' är alltid kritik."),

 "inflation": (
  "Att priserna stiger allmänt och pengarna blir mindre värda ; att något förekommer så ofta att det tappar värde",
  "fackspråklig, neutral, ekonomi ; neutral, lätt negativ",
  ["allmän prisstegring", "penningvärdesförsämring"],
  [["allmän prisstegring", "penningvärdesförsämring"], []],
  "Hög %s gör att sparade pengar tappar värde." % (H % "inflation"),
  "Kortet hade båda betydelserna, men registret sade 'neutral, neutral ; "
  "neutral, neutral' för båda -- alltså ingen skillnad alls mellan en "
  "ekonomisk fackterm och en vardaglig, lätt nedsättande bild "
  "('betygsinflation'). Registret skiljer nu på dem. Grupp 2 lämnas tom: "
  "poolen har ingen belagd synonym för den bildliga betydelsen."),
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
print("Oskrivna kvar:", [e["ord"] for e in poster if not e.get("proposed")] or "inga")
