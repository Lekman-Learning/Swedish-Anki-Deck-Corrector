# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch100, kort 51-75. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch100.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
B = '<font color="#3498db">%s</font>'


def kallor(o, *extra):
    k = urllib.parse.quote(o)
    return " ".join([
        "https://svenska.se/api/msearch?ord=%s" % k,
        "https://www.synonymer.se/sv-syn/%s" % k,
        "https://sv.wiktionary.org/wiki/%s" % k,
        *extra,
    ])


def satt(o, bet, reg, syn, ex, ety, slutsats, grupper=None, extra=(), conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": grupper, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": kallor(o, *extra), "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True


satt("cedilj",
     "Den lilla kroken under bokstaven c (ç), som visar att den ska uttalas "
     "som s",
     "fackspråklig, neutral, lingvistik",
     [],
     "Franskans garçon skrivs med " + B % "cedilj" + ".",
     "→ Franska cédille; av spanska cedilla 'litet c'.",
     "SO: 'ett hakliknande tecken som anbringas pa bokstaven c (c) och "
     "markerar att den ska uttalas som s'. SAOL ger samma sak och namner "
     "att svenskan har det i lanordet garcon -- darav exempelmeningen. "
     "OLD-facit 'hake under bokstaven c' sager inte vad tecknet BETYDER, "
     "vilket ar hela poangen med det.")

satt("celebrera",
     "Fira något högtidligt",
     "neutral, neutral, allmän",
     ["fira"],
     "De " + B % "celebrerade" + " sin tioåriga bröllopsdag med middag ute.",
     "→ Fornsvenska celebrera; av latin celebrare 'talrikt besoka; fira'.",
     "SO och SAOL ger bada exakt ett ord: 'fira' -- darav synonymen, ur "
     "definitionstexten. Ingen bruklighetsmarkning finns i nagondera "
     "ordboken, sa registret ar neutralt trots att ordet kanns hogtidligare "
     "an fira; en markning far inte hittas pa. Ordet 'hogtidligt' i facit "
     "beskriver vad man firar, inte hur ordet later.")

satt("dekis",
     "På nedgång: sliten, förfallen och på väg utför — om en person eller en "
     "verksamhet",
     "vardaglig, negativ, allmän",
     [],
     "Restaurangen verkade vara på " + B % "dekis" + " sedan kocken slutat.",
     "→ Kortform till deka ner sig, av dekadens.",
     "SO: '(vara) fysiskt eller psykiskt forfallen', med markningen "
     "vardagligt. Ordet anvands i praktiken bara i uttrycket 'pa dekis', "
     "vilket bade SO:s och SAOL:s exempel visar -- darfor ar "
     "exempelmeningen byggd sa. OLD-facit 'vara forfallen' fangar "
     "betydelsen men inte att det galler lika mycket verksamheter som "
     "personer.")

satt("dressör",
     "Person som yrkesmässigt lär djur att utföra bestämda konster eller "
     "uppgifter",
     "neutral, neutral, allmän",
     [],
     B % "Dressören" + " fick björnen att balansera på en boll.",
     "→ Franska dresseur, till dressera.",
     "SO: 'person som yrkesmassigt dresserar djur'. VIKTIG RATTELSE: "
     "OLD-facit sa 'djurtamjare', vilket ar ett annat yrke. Att tamja ar "
     "att gora ett vilt djur hanterligt; att dressera ar att lara in "
     "bestamda beteenden hos ett djur som redan ar tamt. Facit ar "
     "omskrivet, och 'yrkesmassigt' ar behallet eftersom SO uttryckligen "
     "har med det -- den som lar sin egen hund sitta ar ingen dressor.")

satt("drömslott",
     "Ett sagolikt vackert slott ; bildligt: en plan eller önskedröm som är "
     "för vacker för att kunna bli verklighet",
     "neutral, neutral, allmän ; neutral, neutral, allmän",
     [],
     "Många nya it-företag visade sig vara " + B % "drömslott" + " byggda på "
     "orealistiska prognoser.",
     None,
     "SO ger tva betydelser: 'slott med (nastan overkligt) fantastiska "
     "egenskaper' och 'orealistiska onskedrommar' (ofta bildligt). Bada med "
     "-- den bildliga ar den enda som anvands i praktiken, och SO:s enda "
     "exempelmening ar just bildlig. OLD-facit 'ouppnaelig fantasi' hade "
     "bara den bildliga och missade den bokstavliga.")

satt("eklatera",
     "Offentligt tillkännage något som varit privat, framför allt en "
     "förlovning",
     "ngt ålderdomlig, neutral, allmän",
     ["tillkännage", "offentliggöra"],
     "Paret " + B % "eklaterade" + " sin förlovning på midsommarafton.",
     "→ Franska éclater 'brista, krevera; bli allmant bekant'.",
     "SO: 'tillkannage', med markningen nagot alderdomligt. SAOL: "
     "'offentliggora forlovning'. Bada synonymerna star i definitionstexten "
     "hos respektive ordbok. Preciseringen 'framfor allt en forlovning' "
     "kommer fran SAOL och ar avgorande: ordet ar i praktiken nastan "
     "reserverat for just det, vilket OLD-facit ('offentliggora "
     "forlovning') fangade men utan att saga att det gar att anvanda "
     "vidare.")

satt("fingerad",
     "Påhittad och satt i stället för det verkliga, för att dölja vem eller "
     "vad det egentligen gäller",
     "neutral, neutral, allmän",
     [],
     "Alla namn i filmen var " + B % "fingerade" + ".",
     "→ Latin fingere 'forma i lera, ge form'; samma rot som fiktion, "
     "fiktiv och fint.",
     "SO: 'ersatta med icke-autentiskt'. SAOL: 'latsa, anta, fejka'. "
     "OLD-facit 'latsad' ar for brett: ett latsat leende ar inte fingerat. "
     "Det avgorande ar att nagot AKTA byts ut mot nagot pahittat, och att "
     "syftet ar att dolja -- den preciseringen ar inskriven. Inga "
     "synonymer: SAOL:s 'latsa, anta, fejka' ar verbet fingera i andra "
     "anvandningar, inte utbytbara mot adjektivet.")

satt("företal",
     "Kort text först i en bok, där författaren eller utgivaren säger något "
     "om verket innan det börjar",
     "neutral, neutral, litteraturvetenskap",
     [],
     "I " + B % "företalet" + " tackar hon alla som ställt upp på intervju.",
     None,
     "SO: 'kort inledande text till en bok'. SAOL: 'till bok'. SO:s JFR "
     "(forord, inledning) ar cohyponymmarkta och tas inte upp som "
     "synonymer, trots att forord ligger mycket nara -- skillnaden ar att "
     "en inledning hor till sjalva verket medan foretalet star utanfor det. "
     "OLD-facit 'inledning' suddar just den skillnaden och ar darfor "
     "ersatt.")

satt("förtrytelse",
     "Vrede blandad med sårad stolthet, över något man upplever som "
     "orättvist mot en själv",
     "neutral, negativ, allmän",
     ["indignation"],
     "Till sin stora " + B % "förtrytelse" + " fick han inte tjänsten.",
     None,
     "SO: 'vrede och upprordhet som orsakas av nagot som upplevs som en "
     "oforratt', SYN-markt mot indignation. Harm ar daremot JFR-markt och "
     "raknas inte som synonym. Ledet 'som UPPLEVS som en oforratt' ar "
     "viktigt och ar inskrivet: fortrytelse sager ingenting om huruvida "
     "man faktiskt har blivit orattvist behandlad. OLD-facit 'indignation, "
     "missnoje' var en synonymrad, och missnoje ar dessutom for svagt.")

satt("gastkramning",
     "Att gripas av en isande skräck som håller en fast ; i äldre folktro: "
     "att ha blivit antastad av en gast och vakna med blåmärken efter det",
     "neutral, neutral, allmän ; ngt ålderdomlig, neutral, allmän",
     [],
     "Filmens sista halvtimme är en enda lång " + B % "gastkramning" + ".",
     "→ Till gast 'spoke' och krama i den aldre betydelsen 'trycka hart'.",
     "SVAGT BELAGD: varken SO eller SAOL har ett uppslag for ordet. Bara "
     "Wiktionary, som ger bada betydelserna: folktrons sjukdomssymtom efter "
     "en natt utomhus, och den moderna 'hallas i skrackfylld spanning'. "
     "Facit vilar alltsa pa EN kalla och ar markt darefter. I dag ar "
     "adjektivet gastkramande betydligt vanligare an substantivet.",
     conf=6)

satt("hätta",
     "Enkel mössa som sluter tätt om huvudet ; det mössliknande krönet på "
     "ett torn ; skyddande kåpa över änden på något, som en tåhätta",
     "neutral, neutral, allmän ; fackspråklig, neutral, teknik ; neutral, "
     "neutral, teknik",
     [],
     "Gråsiskan känns igen på den röda " + B % "hättan" + " på hjässan.",
     "→ Fornsvenska hätta, bildat till hatt.",
     "SO ger 'typ av enklare huvudbonad' och 'rund, mossliknande overdel pa "
     "torn', med underbetydelsen 'av. om andra foremal med liknande form el. "
     "funktion' -- dit hor SO:s egen JFR tahatta, som ar skalet till att "
     "kapbetydelsen ar med som tredje led. SAOL: 'en enkel mossa; skydd'. "
     "SO:s exempel med grasiskans roda hatta visar att ordet ocksa anvands "
     "om fargteckning hos faglar; det ar samma bild och ar inte skilt ut.")

satt("in manu",
     "Personligen till handa — påskrift på ett brev som bara mottagaren "
     "själv får öppna",
     "neutral, neutral, allmän",
     [],
     "Brevet var märkt " + B % "in manu" + " och öppnades av honom själv.",
     "→ Latin in manu 'i handen'; samma rot som manuell och manuskript.",
     "SO: 'personligen till handa'. Ingen bruklighetsmarkning finns i SO, "
     "sa registret ar satt till neutralt trots att ett latinskt uttryck "
     "kanns formellt -- markningen far inte hittas pa. Facit sager ut VAR "
     "uttrycket faktiskt anvands (som paskrift pa brev), eftersom SO:s "
     "definition ensam inte later nagon gissa det.")

satt("in natura",
     "I varor eller tjänster i stället för i pengar",
     "neutral, neutral, ekonomi",
     [],
     "Statarna fick sin lön " + B % "in natura" + " — i mjölk, potatis och "
     "husrum.",
     "→ Latin in natura, eg. 'i naturligt tillstand'.",
     "SO: 'i annat varde an pengar'. SAOL: 'i varor el. livsfornodenheter'. "
     "SO:s definition ar formulerad negativt (vad det INTE ar) och ar "
     "vand till det positiva i facit. SO:s eget exempel om statarna ar "
     "behallet och utbyggt, eftersom det ar den enda situation de flesta "
     "moter uttrycket i.")

satt("ingivelse",
     "En idé som plötsligt dyker upp av sig själv, utan att man har tänkt "
     "sig fram till den",
     "neutral, neutral, allmän",
     [],
     "En talare som litar på stundens " + B % "ingivelse" + ".",
     None,
     "SO: 'plotslig (ny) tanke eller impuls'. SAOL: 'plotslig ny tanke'. "
     "SO:s JFR inspiration ar cohyponymmarkt och tas inte upp som synonym: "
     "inspiration ar ett tillstand som varar, en ingivelse ar ett enda "
     "ogonblick. OLD-facit saknades i praktiken -- facit ar skrivet fran "
     "grunden och betonar att tanken kommer utan foregaende resonemang, "
     "vilket ar det som skiljer ordet fran 'ide'.")

satt("intonation",
     "Hur rösten går upp och ner i tonhöjd när man talar ; inom musiken: att "
     "träffa tonhöjden rätt",
     "fackspråklig, neutral, lingvistik ; fackspråklig, neutral, musik",
     [],
     "Han har ingen brytning om man bortser från " + B % "intonationen" + ".",
     "→ Franska intonation, till intonera; samma rot som detonation.",
     "SO ger tva betydelser: 'karakteristisk variation i rostens tonhojd "
     "vid tal' och 'traffande av ratt tonhojd'. Bada med -- det ar tva "
     "skilda fackomraden och den vanligaste forvaxlingen. SAOL: 'tonansats; "
     "tonfall'. SO:s JFR (satsaccent, satsmelodi) ar cohyponymer inom "
     "samma faltet, inte utbytbara ord. Wiktionarys orgelbetydelse ar for "
     "specialiserad och ar utelamnad.")

satt("irrigation",
     "Att leda vatten till odlingsmark på konstgjord väg ; inom vården: att "
     "spola rent ett sår eller en kroppshåla",
     "fackspråklig, neutral, jordbruk ; fackspråklig, neutral, medicin",
     ["konstbevattning"],
     "Utan " + B % "irrigation" + " går det inte att odla i öknen.",
     "→ Latin irrigatio 'bevattning', till in 'in' och rigare 'leda "
     "vatten'.",
     "SO: 'konstbevattning' -- ett ord, darav synonymen ur "
     "definitionstexten. SAOL lagger till den medicinska betydelsen: "
     "'spolning av sar'. Bada betydelserna ar med; den medicinska saknas "
     "helt i SO och skulle ha fallit bort om bara SO lasts.")

satt("jalu",
     "Svartsjuk, eller avundsjuk på det någon annan har",
     "ngt ålderdomlig, negativ, allmän",
     ["svartsjuk", "avundsjuk"],
     "Han blev " + B % "jalu" + " när hon dansade med någon annan hela "
     "kvällen.",
     "→ Franska jaloux; till latin zelus, grekiska zelos 'iver, avund'. "
     "Samma ord som engelskans jealous.",
     "SO: 'svartsjuk eller avundsjuk', med markningen mindre brukligt; SAOL "
     "markar ald. Bada synonymerna star i definitionstexten. Ordet tacker "
     "BADA kanslorna, vilket svenskan annars haller isar -- det ar hela "
     "svarigheten och ar inskrivet i facit.")

satt("jungman",
     "Den lägsta graden i besättningen på ett handelsfartyg: en sjöman som "
     "fortfarande lärs upp",
     "fackspråklig, neutral, sjöfart",
     [],
     "Han mönstrade på som " + B % "jungman" + " vid sjutton års ålder.",
     "→ Lagtyska jungmann 'ung sjoman', eg. 'ung man'; samma rot som "
     "junker.",
     "SO: '(titel for) sjoman med lagsta tjanstgoringsgrad bland "
     "besattningen pa handelsfartyg'. SAOL: 'sjomanslarling'. SO:s JFR "
     "lattmatros ar en cohyponym -- det ar naste grad UPPAT i samma "
     "hierarki, alltsa raka motsatsen till en synonym. OLD-facit "
     "'sjomanslarling' ar SAOL:s ord och lika svart som uppslagsordet.")

satt("kalkera",
     "Kopiera en bild genom att lägga genomskinligt papper över och rita av "
     "linjerna ; bildligt: härma ett verk så nära att det blir en avbild",
     "neutral, neutral, konst ; neutral, lätt negativ, allmän",
     [],
     "Pjäsen är närmast " + B % "kalkerad" + " på ett stycke av Tjechov.",
     "→ Franska calquer 'rita av'; av italienska calcare 'pressa in, "
     "trampa'; till latin calx 'hal'. Samma rot som dekal.",
     "SO ger tva betydelser: 'kopiera (bild) genom att folja dess linjer' "
     "och 'plagiera' (sarsk. bildligt). Bada med. SAOL: 'gora kopia pa "
     "underliggande papper; efterbilda slaviskt'. Den bildliga betydelsen "
     "bar en klart negativ laddning ('slaviskt', 'plagiera') och registret "
     "ar satt darefter -- det ar belagt i definitionstexten, inte gissat.")

satt("kannstöperi",
     "Tvärsäkert tyckande om politik från någon som inte vet något om saken",
     "neutral, nedsättande, politik",
     [],
     "En massa " + B % "kannstöperier" + " i pressen om presidentens hälsa.",
     None,
     "SO: 'osakkunnigt prat om politik'. Valensen nedsattande foljer direkt "
     "av ordet 'osakkunnigt' i definitionen, inte av nagon gissning; nagon "
     "bruklighetsmarkning ger SO daremot inte, sa formalitetsnivan ar "
     "neutral. Ordet anvands nastan bara i plural. Ursprunget (Holbergs "
     "komedi om tenngjutaren som trodde sig kunna styra riket) ar valkant "
     "men star INTE i de kallor som slagits upp har, och ar darfor inte "
     "inskrivet som etymologi.")

satt("kollationera",
     "Läsa igenom en avskrift mot originalet för att kontrollera att de "
     "stämmer överens ; inom teatern: hålla den första repetitionen, där "
     "hela pjäsen läses igenom",
     "fackspråklig, neutral, allmän ; fackspråklig, neutral, konst",
     ["motläsa"],
     "Notarien " + B % "kollationerade" + " avskriften mot "
     "originalhandlingen.",
     "→ Medeltidslatin collationare 'sammanstalla, jamfora'; till "
     "kollation.",
     "SO ger tva betydelser: 'kontrollasa (avskrift) mot original' och "
     "'genomfora forsta repetitionen av'. Bada med -- teaterbetydelsen ar "
     "helt oformodad och skulle fallit bort utan uppslagning. Synonymen "
     "motlasa star i SAOL:s definitionstext ('jamfora och granska, "
     "motlasa').")

satt("konklav",
     "Det inlåsta mötet där kardinalerna väljer ny påve ; också om själva "
     "den låsta lokalen, och vidare om vilken sluten krets som helst",
     "neutral, neutral, religion ; neutral, neutral, allmän",
     [],
     B % "Konklaven" + " bekräftade påvevalet genom att sända ut vit rök.",
     "→ Latin conclave 'rum som kan lasas', till clavis 'nyckel' -- "
     "kardinalerna lases in tills de ar eniga.",
     "SO: 'slutet rum for hemliga overlaggningar', med underbetydelserna "
     "'av. om de deltagande personerna' och 'sarsk. om kardinalerna nar de "
     "ar samlade till paveval'. SAOL vander pa ordningen och satter "
     "paveval forst. Facit foljer SAOL, eftersom det ar den enda betydelse "
     "de flesta faktiskt moter ordet i -- men bade lokalen och den vidare "
     "anvandningen ar kvar. Etymologin ar med for att den forklarar hela "
     "seden.")

satt("koryfé",
     "Den ledande gestalten inom ett område, ofta sagt med ett stänk av "
     "ironi ; i det antika grekiska dramat: körens ledare",
     "neutral, ironisk, allmän ; fackspråklig, neutral, historia",
     [],
     "En av rörelsens " + B % "koryféer" + " höll högtidstalet.",
     "→ Grekiska koryphaios, till koryphe 'huvud, topp'.",
     "SO ger tva betydelser: 'tongivande person inom visst samhallsomrade' "
     "(markning: ibland ironiskt) och 'korledare i det antika dramat' "
     "(markning: historiskt). Bada med, med respektive markning i "
     "registret. Ironin ar en del av ordets nutida bruk och far inte "
     "utelamnas -- att kalla nagon koryfe ar sallan rent berom.")

satt("kretong",
     "Kraftigt bomullstyg med tryckt mönster i flera färger, ofta använt "
     "till möbler och gardiner",
     "neutral, neutral, allmän",
     [],
     "En soffa klädd i blommig " + B % "kretong" + ".",
     "→ Franska cretonne, efter Creton, en by i Normandie.",
     "SO: 'bomulls- eller linnetyg med patryckt flerfargsmonster'. "
     "Wiktionary preciserar vavtekniken (tuskaft) -- den detaljen ar "
     "utelamnad som for facklig for kortet. SAOL sager bara 'ett tyg', "
     "vilket inte hjalper nagon. Anvandningen (mobler, gardiner) foljer av "
     "SO:s exempel om soffan.")

satt("kut",
     "Krökning på ryggen så att den buktar utåt ; unge av säl",
     "neutral, neutral, allmän ; neutral, neutral, biologi",
     [],
     "Jägarna gav sig ut för att jaga " + B % "kut" + " på isen.",
     "→ I ryggbetydelsen till kuta; i salbetydelsen svensk dialekt kut, "
     "troligen samma ord.",
     "SO ger tva betydelser som saknar samband i bruket: 'konvex krokning "
     "av rygg' och 'salunge'. Bada med. SAOL bekraftar bada. Wiktionary "
     "listar dessutom 'haftigt springande', som hor till verbet kuta och "
     "inte till substantivet -- det ar inte med. Ordet 'konvex' ar for "
     "svart och ar upplost till 'buktar utat'.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("skrev %d kort" % sum(1 for k in KORT if k.get("approved")))
