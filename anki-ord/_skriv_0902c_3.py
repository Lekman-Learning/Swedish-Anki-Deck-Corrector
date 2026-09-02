# -*- coding: utf-8 -*-
"""Arbetsbatch 2026-09-02c, kort 67-99. Sista tredjedelen."""
import io, json, sys
import _hjalp_0902b as HJ

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02c_v3-batch.json"
H = HJ.H

K = {
 "insinuera": (
  "Antyda något kränkande utan att säga det rakt ut",
  "neutral, lätt negativ", ["försåtligt antyda", "låta påskina"],
  [["försåtligt antyda", "låta påskina"]],
  "%s du att jag har tagit mutor?" % (H % "Insinuerar"),
  "En betydelse. 'antyda' ensamt är struket -- man kan antyda vad som helst, "
  "medan insinuera alltid bär något kränkande. Poolens fullständiga former "
  "används i stället."),

 "irreparabel": (
  "Omöjlig att laga eller ersätta",
  "formell, negativ", ["obotlig", "ohjälplig"], [["obotlig", "ohjälplig"]],
  "Bilkrocken orsakade %s skador på motorn." % (H % "irreparabla"),
  "En betydelse. Båda synonymerna finns i poolen. Kortet var redan korrekt."),

 "kleptomani": (
  "Tvångsmässigt behov att stjäla",
  "fackspråklig, neutral, psykologi", ["sjuklig drift att stjäla"],
  [["sjuklig drift att stjäla"]],
  "Hennes %s fick henne att stjäla saker hon inte ens behövde." % (H % "kleptomani"),
  "En betydelse. Synonymraden var tom och är fylld ur poolen."),

 "kommission": (
  "Grupp sakkunniga med ett utredningsuppdrag ; uppdrag att sälja åt någon annan i eget namn",
  "formell, neutral, politik ; formell, neutral, ekonomi",
  ["grupp av sakkunniga", "uppdrag el. åtagande att sälja el. köpa varor"],
  [["grupp av sakkunniga"], ["uppdrag el. åtagande att sälja el. köpa varor"]],
  "Konstnären sålde sina tavlor på %s genom galleriet." % (H % "kommission"),
  "Kortet hade båda betydelserna men blandade tre obelagda synonymer i en "
  "grupp. Grupperna är delade och synonymerna hämtade ur poolen. "
  "Ordningen är också bytt så att den betydelse exempelmeningen visar inte "
  "står sist."),

 "kompromiss": (
  "Lösning där båda sidor ger efter för att kunna mötas",
  "neutral, neutral", ["medelväg"], [["medelväg"]],
  "Partierna enades till slut om en %s efter veckor av förhandling." % (H % "kompromiss"),
  "SO:s andra betydelse är folkrättslig -- ett avtal mellan stater om "
  "skiljedom -- och är fackterm. Synonymraden var tom och är fylld ur "
  "poolen."),

 "kondensera": (
  "Övergå från gas till vätska ; tränga ihop något på mindre plats",
  "fackspråklig, neutral, kemi ; formell, neutral",
  ["förtäta", "tränga samman (på begränsat utrymme)"],
  [["förtäta"], ["tränga samman (på begränsat utrymme)"]],
  "Vattenångan %s till droppar på det kalla fönstret." % (H % "kondenserade"),
  "Kortet hade båda betydelserna. Andra gruppen stod utan synonym."),

 "kooperativ": (
  "Som drivs gemensamt av dem som är med ; sammanslutning som drivs så",
  "neutral, neutral, ekonomi ; neutral, neutral, ekonomi",
  ["samverkande grupp", "kooperativt organiserad (arbets)enhet"],
  [["samverkande grupp"], ["kooperativt organiserad (arbets)enhet"]],
  "De driver en %s butik i byn där alla medlemmar delar vinsten." % (H % "kooperativ"),
  "Kortet hade båda betydelserna. SO:s tredje post ('utmärkande för "
  "kooperation') är samma adjektivbetydelse som den första."),

 "kreatur": (
  "Större husdjur som hålls i jordbruket ; skapad varelse ; någons viljelösa redskap",
  "neutral, neutral ; arkaisk, neutral, bibliskt ; litterär, nedsättande",
  ["boskapsdjur", "varelse", "lydigt redskap"],
  [["boskapsdjur"], ["varelse"], ["lydigt redskap"]],
  "Bonden gick ut varje morgon klockan sex för att utfodra %s." % (H % "kreaturen"),
  "Kortet hade två betydelser. SO:s underbetydelse 'äv. bildligt om person "
  "betraktad som någons osjälvständiga redskap' bär eget innehåll och är "
  "tillagd. 'boskap' och 'husdjur' saknar belägg var för sig. Registret "
  "ändrat från vardaglig -- ordet är neutralt fackspråk i jordbruket."),

 "krusta": (
  "Hård yttre beläggning, till exempel på bröd ; skorpa som bildas på ett sår",
  "neutral, neutral, matlagning ; fackspråklig, neutral, medicin",
  ["hårt överdrag", "sårskorpa"], [["hårt överdrag"], ["sårskorpa"]],
  "Brödets %s var sprö och gyllenbrun." % (H % "krusta"),
  "RÄTTAT: SO har två betydelser och kortet hade en. Den medicinska "
  "sårskorpan saknades. 'skorpa' ensamt saknar belägg."),

 "lakej": (
  "Livréklädd betjänt ; någon som underdånigt tjänar en makthavare",
  "ngt ålderdomlig, neutral ; neutral, nedsättande",
  ["livréklädd betjänt", "hantlangare", "eftersägare"],
  [["livréklädd betjänt"], ["hantlangare", "eftersägare"]],
  "Grevens %s öppnade dörren för gästerna." % (H % "lakej"),
  "Kortet hade båda betydelserna. 'betjänt' ensamt saknar belägg. "
  "Registret ändrat från 'arkaisk' till 'ngt ålderdomlig' -- den bildliga "
  "betydelsen används alltjämt i politisk polemik."),

 "lurvig": (
  "Med tjock, rufsig päls eller hårväxt ; lätt berusad",
  "vardaglig, neutral ; vardaglig, skämtsam",
  ["luden och rufsig", "lätt berusad"],
  [["luden och rufsig"], ["lätt berusad"]],
  "Hunden hade en %s päls som blev full av kardborrar efter varje skogspromenad." % (H % "lurvig"),
  "Kortet hade båda betydelserna. 'raggig', 'hårig' och 'på pickalurven' "
  "saknar belägg. SO:s andra def, 'dansa', hör till ett annat uppslagsord "
  "som fuzzy-sökningen dragit in."),

 "långskott": (
  "Skott mot mål från långt håll ; försök med liten chans att lyckas",
  "neutral, neutral, sport ; vardaglig, neutral",
  ["fotbollsskott från långt håll", "vild gissning"],
  [["fotbollsskott från långt håll"], ["vild gissning"]],
  "Ett otagbart %s tätt intill stolpen." % (H % "långskott"),
  "Kortet hade båda betydelserna. 'fjärrskott' och 'chansning' saknar "
  "belägg och är utbytta mot poolens egna."),

 "malaj": (
  "Person ur en stor folkgrupp i Sydostasien ; värnpliktig utan vapen, i enklare tjänst",
  "neutral, neutral ; ngt ålderdomlig, neutral, militär",
  ["≈≈ folkgrupp", "icke vapenför värnpliktig"],
  [["≈≈ folkgrupp"], ["icke vapenför värnpliktig"]],
  "Under kriget tilldelades de fysiskt svagaste männen tjänst som %s." % (H % "malaj"),
  "RÄTTAT: kortet hade BARA den militära betydelsen och kallade ordet "
  "arkaiskt. SO:s första betydelse är folkgruppen, som är fullt aktuell — "
  "malajiska talas av miljoner. Att utelämna den och märka ordet som utdött "
  "var två fel i samma rad. Synonymen '≈ köksbiträde' är struken: den var "
  "varken belagd eller riktig."),

 "malplacerad": (
  "Som hamnat i ett sammanhang där den inte hör hemma",
  "neutral, lätt negativ", ["≈≈ opassande"], [["≈≈ opassande"]],
  "Den gamla kyrkan verkade helt %s intill det nya köpcentret." % (H % "malplacerad"),
  "En betydelse. 'olämplig' och 'opassande' saknar båda ordboksbelägg -- "
  "poolen ger bara SO:s definition ordagrant -- så kategorin används."),

 "marionett": (
  "Docka som styrs med trådar ovanifrån ; person som är någon annans viljelösa redskap",
  "neutral, neutral ; neutral, nedsättande",
  ["leddocka", "viljelöst redskap"], [["leddocka"], ["viljelöst redskap"]],
  "%s dansade över scenen när skådespelaren drog i trådarna." % (H % "Marionetten"),
  "Kortet hade båda betydelserna. 'tråddocka' och 'lydig lekboll' saknar "
  "belägg och är utbytta mot poolens egna."),

 "mitos": (
  "Vanlig celldelning där en cell blir två likadana",
  "fackspråklig, neutral, biologi", ["≈≈ celldelning"], [["≈≈ celldelning"]],
  "Under %s fördelas kromosomerna jämnt mellan de nya cellerna." % (H % "mitosen"),
  "En betydelse. Synonymraden var tom; poolen ger bara definitionen "
  "ordagrant, så kategorin används. Att cellerna blir IDENTISKA är "
  "kärnan -- det är där mitos skiljer sig från meios."),

 "mixtur": (
  "Läkemedel i flytande form ; en blandstämma på en orgel",
  "fackspråklig, neutral, medicin ; fackspråklig, neutral, musik",
  ["flytande blandning", "en orgelstämma"],
  [["flytande blandning"], ["en orgelstämma"]],
  "Barnet fick medicinen som %s istället för tablett." % (H % "mixtur"),
  "Kortet hade båda betydelserna. 'läkemedelsblandning' och 'orgelstämma' "
  "saknar belägg var för sig; poolens former används."),

 "mollusk": (
  "Mjukt ryggradslöst djur som snäcka eller mussla ; liten vårta i huden av en virusinfektion",
  "fackspråklig, neutral, biologi ; fackspråklig, neutral, medicin",
  ["ett blötdjur", "en virusinfektion som orsakar knottror på huden"],
  [["ett blötdjur"], ["en virusinfektion som orsakar knottror på huden"]],
  "Snäckor och musslor är exempel på %s." % (H % "mollusker"),
  "Kortet hade båda betydelserna. Andra gruppen stod utan synonym."),

 "multipel": (
  "Som förekommer på flera ställen samtidigt ; ett tal som fås genom multiplikation",
  "formell, neutral, medicin ; fackspråklig, neutral, matematik",
  ["mångfaldig", "mångfald av ett tal"],
  [["mångfaldig"], ["mångfald av ett tal"]],
  "Talet 15 är en %s av både 3 och 5." % (H % "multipel"),
  "Kortet hade båda betydelserna. 'flerfaldig' saknar belägg. Ordningen är "
  "behållen -- den medicinska användningen (multipel skleros) är den Adam "
  "möter oftast, även om SO leder med matematiken."),

 "naturalisera": (
  "Ge en utlänning medborgarskap ; göra något främmande inhemskt",
  "formell, neutral, juridik ; formell, neutral",
  ["ge medborgarrätt åt inflyttad utlänning", "göra inhemsk"],
  [["ge medborgarrätt åt inflyttad utlänning"], ["göra inhemsk"]],
  "Han kom hit som flykting och är numera %s svensk." % (H % "naturaliserad"),
  "Kortet hade båda betydelserna. 'ge medborgarskap' saknar belägg och är "
  "bytt mot poolens fullständiga form."),

 "nipprig": (
  "Lätt tokig på ett fjolligt sätt",
  "vardaglig, skämtsam", ["fjollig", "tokig"], [["fjollig", "tokig"]],
  "Han blev lite %s och skrattade åt ingenting." % (H % "nipprig"),
  "En betydelse. Båda synonymerna finns i poolen. 'knäpp' saknar belägg."),

 "optik": (
  "Läran om hur ljuset beter sig ; linssystemet i ett instrument",
  "fackspråklig, neutral, fysik ; fackspråklig, neutral, teknik",
  ["vetenskapen om ljuset", "system av linser m.m. i optiskt instrument"],
  [["vetenskapen om ljuset"], ["system av linser m.m. i optiskt instrument"]],
  "Astronomen fick finjustera teleskopets %s för att få en skarp bild av planeten." % (H % "optik"),
  "Kortet hade båda betydelserna men bara en synonym. SO:s andra post, "
  "'ljusverkan', är samma sak som den tredje sedd som resultat i stället "
  "för som utrustning."),

 "pamflett": (
  "Kort skrift med häftig kritik mot någon",
  "litterär, negativ", ["nidskrift", "kritisk skrift"],
  [["nidskrift", "kritisk skrift"]],
  "En anonym %s med hård kritik mot borgmästaren spreds i hela staden." % (H % "pamflett"),
  "En betydelse. Kortet bar en andra, 'enklare broschyr eller häfte', som "
  "SO inte har -- den kommer från engelskans pamphlet, som betyder just "
  "broschyr utan kritisk laddning. På svenska är angreppet hela poängen. "
  "'smädeskrift', 'broschyr' och 'häfte' saknar belägg."),

 "passionerad": (
  "Driven av starka känslor",
  "neutral, positiv", ["lidelsefullt engagerad"], [["lidelsefullt engagerad"]],
  "Hennes älskare var av en %s natur och skrev henne kärleksbrev varje dag." % (H % "passionerad"),
  "En betydelse. 'lidelsefull' ensamt saknar belägg; poolens fullständiga "
  "form används."),

 "pedagogisk": (
  "Som rör konsten att lära ut ; som är bra på att förklara",
  "neutral, neutral ; neutral, positiv",
  ["undervisnings-", "skickligt undervisande"],
  [["undervisnings-"], ["skickligt undervisande"]],
  "Läraren använde en %s metod som fick alla att förstå direkt." % (H % "pedagogisk"),
  "Kortet hade båda betydelserna men bara en synonym. Skillnaden är värd "
  "att hålla isär: en pedagogisk metod hör till ämnet, en pedagogisk person "
  "är skicklig."),

 "permanent": (
  "Gjord för att bestå ; behandling som gör håret lockigt länge",
  "neutral, neutral ; vardaglig, neutral",
  ["beständig", "varaktig", "behandling av hår så att det förblir lockigt under längre tid"],
  [["beständig", "varaktig"],
   ["behandling av hår så att det förblir lockigt under längre tid"]],
  "Efter flera års pendlande skaffade familjen sig äntligen en %s bostad." % (H % "permanent"),
  "Kortet hade båda betydelserna. SO:s tredje post ('permanentat hår') är "
  "resultatet av den andra, inte en egen betydelse. Andra gruppen stod "
  "utan synonym."),

 "pörte": (
  "Stuga utan skorsten, med bara en röklucka i taket",
  "ngt ålderdomlig, neutral", ["finsk skorstenslös stuga"],
  [["finsk skorstenslös stuga"]],
  "Ett gammalt %s stod kvar djupt inne i finnmarken." % (H % "pörte"),
  "En betydelse. Synonymraden var tom och är fylld ur poolen. Etymologin "
  "förklarar varför byggnadstypen är finsk: ordet kommer av finskans "
  "pirtti."),

 "ravin": (
  "Djup och smal sänka med branta väggar",
  "neutral, neutral, geologi", ["klyfta", "djup dalsänka"],
  [["klyfta", "djup dalsänka"]],
  "Vandrarna klättrade försiktigt ner i den uttorkade %s." % (H % "ravinen"),
  "En betydelse. Båda synonymerna finns i poolen. 'dalsänka' ensamt är "
  "bytt mot poolens fullständiga form."),

 "realisera": (
  "Göra något planerat till verklighet ; sälja till nedsatt pris ; omvandla en tillgång till pengar",
  "formell, neutral ; neutral, neutral, ekonomi ; formell, neutral, ekonomi",
  ["förverkliga", "genomföra", "försälja till nedsatt pris", "omvandla till reda pengar"],
  [["förverkliga", "genomföra"], ["försälja till nedsatt pris"],
   ["omvandla till reda pengar"]],
  "Efter tjugo års sparande kunde han äntligen %s sin gamla dröm om ett hus vid havet." % (H % "realisera"),
  "RÄTTAT: kortet hade två betydelser, SO har tre. Den som saknades är "
  "REA-betydelsen -- att sälja till nedsatt pris -- som är den vanligaste "
  "i vardagen. Kortet slog ihop den med 'omvandla till pengar', men de är "
  "skilda: en rea sänker priset, en realisering av tillgångar behöver inte."),

 "regent": (
  "Statsöverhuvud i en monarki ; den som styr i monarkens ställe",
  "formell, neutral ; formell, neutral, historia",
  ["statsöverhuvud", "ställföreträdare för monark"],
  [["statsöverhuvud"], ["ställföreträdare för monark"]],
  "%s undertecknade deklarationen med sitt sigill." % (H % "Regenten"),
  "RÄTTAT: SO har två betydelser och kortet hade en. Den andra är den "
  "ursprungliga -- en regent i egentlig mening är den som styr FÖR en "
  "omyndig eller frånvarande monark. 'monark' ensamt saknar belägg och är "
  "dessutom missvisande för just den betydelsen."),

 "repressiv": (
  "Som slår ner motstånd och kväver frihet",
  "formell, negativ, politik", ["undertryckande", "hämmande"],
  [["undertryckande", "hämmande"]],
  "Militärjuntans %s apparat slog ner alla protester." % (H % "repressiva"),
  "En betydelse. Båda synonymerna finns i poolen."),

 "respons": (
  "Det man får tillbaka när något påverkar utifrån",
  "neutral, neutral, psykologi", ["gensvar", "reaktion", "svar"],
  [["gensvar", "reaktion", "svar"]],
  "Behavioristerna beskrev beteende med hjälp av stimulus och %s." % (H % "respons"),
  "SO:s två definitioner -- reaktion på yttre retning och gensvar -- är "
  "samma begrepp i fysiologisk respektive vardaglig tappning. Alla tre "
  "synonymerna finns i poolen."),

 "restera": (
  "Finnas kvar av något ; ännu ha kvar att betala",
  "formell, neutral ; formell, neutral, ekonomi",
  ["återstå", "vara obetald"], [["återstå"], ["vara obetald"]],
  "Det %s bara en minut av matchen." % (H % "resterade"),
  "RÄTTAT: SO har två betydelser och kortet hade en. Skuldbetydelsen "
  "saknades, trots att det är den som gett ordet 'restskuld'. 'kvarstå' "
  "saknar belägg."),
}


poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    d = K.get(e["ord"])
    if not d:
        continue
    hb, reg, syn, grp, ex, slut = d
    e["proposed"] = {"huvudbetydelse": hb, "register": reg, "synonymer": syn,
                     "synonym_groups": grp, "exempelmening": ex,
                     "etymologi": HJ.etym(e["ord"])}
    e["sokkoll"] = {"kalla": HJ.kallor(e["ord"]), "slutsats": slut}
    e["approved"] = True
    n += 1

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Skrev %d kort." % n)
print("Oskrivna kvar:", [e["ord"] for e in poster if not e.get("proposed")] or "inga")
