# -*- coding: utf-8 -*-
"""50 legacy-kort ur spår A (is:new, suspenderade) -> full v3.

## Det som styrde arbetet den här gången

Tre ord visade sig ha **förorenat underlag trots att trekällskontrollen sa
godkänt**. Det är samma hål som beskrivs i projektets CLAUDE.md: `slaupp.py`s
sammandrag slår ihop alla fuzzy-träffar, så en flerordsfras drar med sig sina
beståndsdelar och grannord.

* `på nåder` fick SO:s definitioner för **`nåd`** -- "efterskänkning eller
  mildring av straff", "synda därför att man litar på att man blir förlåten",
  "mycket framstående". Ingen av dem är frasen.
* `till fromma för` fick **`from`** -- "religiös på ett stillsamt, allvarligt
  sätt", "from som ett lamm" -- blandat med den riktiga betydelsen.
* `vind för våg` fick **`våg`**, **`vind`** och till och med **`grön våg`**
  ("samordning av trafikljus"). Frasen själv fanns bara som exempelrad.
* `råk` fick en synonymlista med *"bortrensat innanmäte, rens, avfall, på sin
  tallrik"* -- det är `råka`/`rå`, inte spricka i is.

De tre första är skrivna mot **allmän websökning** enligt Adams regel från
2026-08-11 (färre än tre rena källor -> sök alltid). `råk` har rena definitioner
i SO och SAOL; bara synonymlistan var smittad, och den används inte.

## Ett kort med defekt framsida

`kvintessensen` står i **bestämd form** på framsidan. Ordboken har lemmat
`kvintessens`, så Hål 0 gav `traffar=INGEN` och bara synonymer.se + Wiktionary
svarade -- de bryr sig inte om böjning. Spärren gjorde alltså rätt: den fångade
att svaret gällde ett annat uppslagsord än kortet frågar om.

Lemmat slogs upp separat (tre källor, godkänt) och `K` nedan pekar `kalla` dit.
**Framsidan är orörd** -- den ändrar vad Adam testas på och är hans beslut. Lagd
i `ATT_GORA.md`, samma klass som `te`/`tes` och `gem`/`gemen`.

## Val som är värda att kunna försvara

* **`sanktionera` får bara "officiellt godkänna".** SAOL:s andra betydelse
  "införa sanktioner" står där som en hänvisning (`till sanktion 2`), inte som en
  egen definition, och SO saknar den helt. Enligt källhierarkin avgör SO och SAOL
  dagens betydelser -- men en ren korshänvisning är inte en betydelse.
* **`myllra` slås ihop till en betydelse.** SO delar den i "förekomma i ... mängd"
  och "vara fylld av ... mängd". Det är samma verb i två konstruktioner, inte två
  betydelser, och två rader hade tvingat fram en tom synonymgrupp.
* **`töcknig` får inte ordet `töcken` i definitionen.** SO:s egen lydelse är
  "uppfylld av töcken", vilket avslöjar svaret på framsidan -- samma cirkularitet
  som fällde `urmodig`.
* **`sensualism` får inte synonymen `sensualitet`** trots att SAOL leder med den.
  Den delar hela ordstammen och röjer svaret.
* **`hugad` får inte `hågad`.** SAOL:s definition ÄR den formen; det är samma ord
  i annan stavning, inte en synonym.
* **`fanera` och `liberalisera` får tom synonymlista** fast SO:s definitioner
  ("belägga med faner", "göra friare") tekniskt inleder ett led. Glosan är
  identisk med huvudbetydelsen, alltså cirkulär.
* **`partikuljär` märks `ngt ålderdomlig`.** SO skriver "mindre brukligt", som
  saknar exakt motsvarighet i den fasta registerlistan; `ngt ålderdomlig` ligger
  närmast. Ordet har bara två källor -- SO och synonymer.se -- eftersom Wiktionary
  saknar posten.

## Grupperade synonymer

Fyra kort har belagd synonym för **varje** betydelse och grupperas därför:
`plombera`, `prägel`, `tillknäppt`, `murrig`. Övriga flerbetydelsekort får tom
lista i stället för en platt lista -- det är just den tvetydigheten Adam
påpekade 2026-08-13.
"""
import json
import sys
import urllib.parse

SESSION = "sessions/session_2026-08-15_v3-batch.json"
SVENSKA = "https://svenska.se/api/msearch?ord={}"

# Kortets framsida -> det uppslagsord som faktiskt slogs upp.
K = {
    "kvintessensen": "kvintessens",
}

PAUSAS = set()

# Redovisade undantag från förgranskningens hårda regler. Regeln tystas inte --
# flaggan blir `<regel>_tillaten` och följer med in i sessionsfilen som
# blindgranskaren läser, tillsammans med motiveringen.
TILLAT = {
    "på nåder": {
        "frammande_uppslagsord":
            "Flerordsfras: fritextsökningen drar med sig `nåd`, `nådens år` och "
            "`synda på nåden`. SO:s definitioner i svaret gäller ALLA dessa, inte "
            "frasen. Kortet är därför skrivet mot en allmän websökning enligt "
            "Adams regel 2026-08-11, som ger entydigt 'av någon annans välvilja "
            "och överseende, utan egen rätt' -- ofta med nedlåtande ton. "
            "Synonymlistan är tom, så ingen glosa kan ha vandrat över.",
        "register_motsager_markning":
            "Samma förorening: märkningarna 'något högtidligt', 'ursprungligen "
            "bibliskt' och 'formellt, skämtsamt el. ålderdomligt' gäller `nådens "
            "år`, `synda på nåden` och `nåd` i religiös mening -- inte frasen. "
            "`på nåder` är vardagsspråk utan högtidlighet: 'han bor på nåder hos "
            "sin bror'.",
    },
    "till fromma för": {
        "frammande_uppslagsord":
            "Samma sak: svaret blandar `from` ('stillsamt religiös', 'from som "
            "ett lamm') med `fromma` ('nytta, fördel'). Bara den senare hör till "
            "frasen. SO:s egen exempelrad -- 'konkurrensen ökar, till "
            "konsumenternas fromma' -- och websökningen ger samma betydelse. "
            "Synonymlistan är tom.",
    },
    "vind för våg": {
        "frammande_uppslagsord":
            "Grövsta fallet i batchen: SO returnerade `våg`, `vind`, `vågrörelse` "
            "och `grön våg` ('samordning av trafikljus'). Frasen finns bara som "
            "exempelrad. Websökningen ger 'utan tillsyn, utan att någon bryr sig "
            "om hur det går', och att uttrycket är en förvanskning av det äldre "
            "'(segla) för vind och våg'. Synonymlistan är tom.",
        "register_motsager_markning":
            "Märkningen 'vardagligt' hör till `grön våg` ('samordning av "
            "trafikljus') och kommer ur samma förorenade svar. `vind för våg` är "
            "stilistiskt neutralt och förekommer i sakprosa.",
    },
    "kvintessensen": {
        "frammande_uppslagsord":
            "Kortets framsida står i bestämd form; ordbokens lemma är "
            "`kvintessens`. Hål 0 gav därför `traffar=INGEN` på den formen. "
            "Lemmat slogs upp separat och gav saol+so+saob; `kalla` pekar på den "
            "hämtningen via K-mappningen. Framsidan är medvetet orörd.",
    },
    "förbehåll": {
        "frammande_uppslagsord":
            "Enda främmande träffen är `förbehålla`, verbet som substantivet är "
            "bildat av -- SO listar dem i samma svar. Kortet använder bara "
            "substantivposten ('särskilt förhandsvillkor för godkännande' och "
            "'reservation'); verbbetydelserna ('kräva att få behålla', 'låta vara "
            "i ensam besittning av') är medvetet uteslutna just för att de hör "
            "till verbet.",
    },
    "reflektion": {
        "frammande_uppslagsord":
            "Enda främmande träffen är `reflexion`, som är SAMMA ord i den andra "
            "godkända stavningen -- SO hänvisar själv dit med SE:se, och "
            "Wiktionary definierar `reflektion` som 'stavningsvariant av "
            "reflexion'. Ingen glosa kan alltså höra till fel ord; det finns bara "
            "ett ord.",
    },
    "plombera": {
        "register_motsager_markning":
            "SO:s märkning 'delvis historiskt' gäller ordagrant *delvis* -- den "
            "hör till sigillbetydelsen (blyplomberade järnvägsvagnar), inte till "
            "tandlagningen, som är fullt levande språk. Kortet uttrycker just den "
            "uppdelningen: första betydelsen bär 'ngt ålderdomlig', andra "
            "'neutral'. Ett register som märkte HELA ordet som historiskt vore "
            "felaktigt.",
    },
    "abrovink": {
        "register_motsager_markning":
            "SO och SAOL säger olika saker: SO märker 'vardagligt', SAOL 'prov.' "
            "(provinsiellt). Kortet följer SO, eftersom källhierarkin låter SO "
            "avgöra dagens bruk medan SAOL:s märkning beskriver ordets dialektala "
            "ursprung -- vilket också är vad etymologin säger ('svensk dialekt "
            "abravink'). Ordet är i dag allmänt vardagsspråk, inte dialektalt.",
    },
}

B = '<font color="#3498db">{}</font>'

KORT = {
    "alienera": {
        "hb": "få någon att känna sig främmande och utanför",
        "syn": ["göra främmande"],
        "grp": None,
        "ex": f'Den nya ledningens ton {B.format("alienerade")} hela avdelningen på ett halvår.',
        "reg": "formell, lätt negativ, allmän",
        "ety": "efter engelska alienate; av latin alienus 'annan tillhörig, främmande'",
        "skal": "SO: 'skapa alienation hos'. SAOL leder med 'göra främmande, ge känsla "
                "av främlingskap' -- därifrån synonymen. Huvudbetydelsen undviker ordet "
                "`alienation`, som delar stam med uppslagsordet och röjer svaret.",
    },
    "amanuens": {
        "hb": "tjänsteman i början av sin karriär vid ämbetsverk eller institution",
        "syn": ["assistent"],
        "grp": None,
        "ex": f'Hon arbetade som {B.format("amanuens")} på institutionen medan hon skrev sin avhandling.',
        "reg": "formell, neutral, allmän",
        "ety": "av latin amanuensis 'handsekreterare', till a manu 'till hands'",
        "skal": "SO: '(titel för) tjänsteman i början av karriären vid ämbetsverk eller "
                "institution'. SAOL:s andra led inleds med 'assistent på "
                "universitetsinstitution' -- belägget för synonymen.",
    },
    "brokig": {
        "hb": "sammansatt av sinsemellan olikartade färger ; blandad och oenhetlig",
        "syn": [],
        "grp": None,
        "ex": f'Publiken var en {B.format("brokig")} samling studenter, pensionärer och turister.',
        "reg": "neutral, neutral, allmän ; neutral, neutral, allmän",
        "ety": "fornsvenska brokoter; jfr svensk dialekt brok 'mörk fläck'",
        "skal": "SO ger två betydelser, den andra märkt 'ofta bildligt'. Betydelse 2 har "
                "belagda glosor ('blandad', 'oenhetlig' inleder var sitt led), men "
                "betydelse 1 har ingen enordsglosa i vare sig SO eller SAOL. Tom lista "
                "i stället för en platt lista över två betydelser.",
    },
    "dolsk": {
        "hb": "som hyser dolda och illasinnade avsikter",
        "syn": ["lömsk", "opålitlig"],
        "grp": None,
        "ex": f'Han sände henne en {B.format("dolsk")} blick över bordet.',
        "reg": "neutral, negativ, allmän",
        "ety": "till fornsvenska dul 'förtegenhet'; besläktat med dölja",
        "skal": "SO: 'som hyser dolda, illasinnade planer'. SAOL: 'lömsk, opålitlig' -- "
                "båda orden inleder var sitt led. Varken SO eller SAOL sätter någon "
                "bruklighetsmärkning, så registret är neutralt trots att ordet känns "
                "litterärt.",
    },
    "gnom": {
        "hb": "dvärgliknande väsen som tänks bo i jordens inre ; kort allmän levnadsregel",
        "syn": [],
        "grp": None,
        "ex": f'I sagan vaktade en {B.format("gnom")} skatten djupt inne i berget.',
        "reg": "neutral, neutral, allmän ; ngt ålderdomlig, neutral, litteraturvetenskap",
        "ety": "av nylatin gnomus om väsendet; betydelsen 'tänkespråk' av grekiska "
               "gnome 'förnuft, insikt'",
        "skal": "Två helt skilda ord som fallit ihop i formen -- SO ger dem olika "
                "etymologi och olika första belägg (1785 respektive 1817). SAOL märker "
                "posten 'ngt åld.', vilket rimligen gäller tänkespråksbetydelsen. "
                "Betydelse 1 saknar enordsglosa, alltså tom lista.",
    },
    "kabaré": {
        "hb": "blandat underhållningsprogram med sång, tal och dansnummer",
        "syn": [],
        "grp": None,
        "ex": f'De avslutade kvällen på en {B.format("kabaré")} i Montmartre.',
        "reg": "neutral, neutral, allmän",
        "ety": "av franska cabaret 'värdshus; kabaré'",
        "skal": "SO: 'blandat underhållningsprogram med sång-, tal- och dansnummer'. "
                "'varieté' och 'revy' står bara i SO:s jfr-fält som cohyponymer, inte "
                "som synonymer -- alltså inte belagda.",
    },
    "kapitulation": {
        "hb": "formellt uppgivande av allt motstånd",
        "syn": [],
        "grp": None,
        "ex": f'De allierade krävde villkorslös {B.format("kapitulation")}.',
        "reg": "neutral, neutral, militär",
        "ety": "till kapitulera",
        "skal": "SO: 'formellt uppgivande av allt motstånd', med underbetydelsen 'äv. "
                "bildligt' (samhällets kapitulation inför läktarvåldet). Den bildliga "
                "användningen är samma betydelse överförd, inte en egen. Ingen glosa "
                "inleder ett led, så tom lista.",
    },
    "statist": {
        "hb": "person som uppträder som bakgrundsfigur i film eller på scen",
        "syn": ["bifigur"],
        "grp": None,
        "ex": f'Han fick jobb som {B.format("statist")} i masscenerna.',
        "reg": "neutral, neutral, konst",
        "ety": "av tyska Statist; bildning till status",
        "skal": "SAOL: 'bifigur i teaterpjäs, film e.d.' -- inleder ledet, alltså belagd. "
                "SO:s underbetydelse 'ibland bildligt om betydelselös person' är den "
                "överförda användningen, inte en egen betydelse.",
    },
    "bildstod": {
        "hb": "fristående staty, ofta i klassisk stil",
        "syn": ["staty"],
        "grp": None,
        "ex": f'På torget stod en {B.format("bildstod")} av stadens grundare.',
        "reg": "neutral, neutral, konst",
        "ety": "till bild och stod",
        "skal": "SO: '(klassisk) staty'. SAOL: 'staty'. Efter att den inledande "
                "parentesen skalats bort inleder 'staty' ledet i båda ordböckerna.",
    },
    "myllra": {
        "hb": "förekomma i stor, rörlig och osorterad mängd",
        "syn": ["vimla"],
        "grp": None,
        "ex": f'Kajerna {B.format("myllrade")} av folk i sommarkvällen.',
        "reg": "neutral, neutral, allmän",
        "ety": "jfr svensk dialekt myrla; troligen till mya 'vimla'",
        "skal": "SAOL: 'vimla'. SO delar posten i 'förekomma i ... mängd' och 'vara "
                "fylld av ... mängd' -- samma verb i två konstruktioner (folk myllrade "
                "/ det myllrade av folk), inte två betydelser. Slås ihop; två rader "
                "hade tvingat fram en tom synonymgrupp.",
    },
    "negociera": {
        "hb": "underhandla eller mäkla",
        "syn": ["underhandla", "mäkla"],
        "grp": None,
        "ex": f'Han {B.format("negocierade")} fram ett avtal mellan de två husen.',
        "reg": "formell, neutral, allmän",
        "ety": None,
        "skal": "SO saknar ordet helt. SAOL: 'underhandla, mäkla' -- båda inleder var "
                "sitt led. SAOL:s övriga betydelser ('förmedla lån', 'diskontera växel') "
                "är fackekonomiska specialiseringar av samma grundbetydelse och tas inte "
                "med som egna rader. Ingen etymologi anges i någon källa, så fältet "
                "lämnas tomt i stället för att gissa på franskt ursprung.",
    },
    "övertalig": {
        "hb": "som överskrider det nödvändiga antalet och därför inte behövs",
        "syn": [],
        "grp": None,
        "ex": f'Efter omorganisationen blev tolv anställda {B.format("övertaliga")}.',
        "reg": "formell, eufemistisk, allmän",
        "ety": "till tal",
        "skal": "SO: 'som överskrider det nödvändiga antalet'. SAOL: 'som inte behövs el. "
                "kan sysselsättas'. Valören är eufemistisk och inte bara negativ -- SO:s "
                "eget exempel ('efter 15 år som lärare blev hon övertalig') visar att "
                "ordet används i stället för att säga uppsagd. 'överflödig' finns bara i "
                "synonymer.se.",
    },
    "abrovink": {
        "hb": "kringgående rörelse eller tillfällig listig lösning",
        "syn": [],
        "grp": None,
        "ex": f'Han hade ingen skruv, så han löste det med en {B.format("abrovink")} av ståltråd.',
        "reg": "vardaglig, neutral, allmän",
        "ety": "svensk dialekt abravink; av ovisst ursprung",
        "skal": "SO märker ordet 'vardagligt' och ger 'kringgående rörelse' samt "
                "'(tillfällig) listig lösning'; SAOL har bara den senare. SO:s tredje "
                "betydelse 'konstig sak' är märkt 'någon gång äv.' och tas inte med. "
                "'krumelur' och 'trick' står bara i synonymer.se.",
    },
    "apati": {
        "hb": "tillstånd av fullständig likgiltighet och oföretagsamhet",
        "syn": ["håglöshet", "likgiltighet"],
        "grp": None,
        "ex": f'Den långa arbetslösheten hade drivit honom in i {B.format("apati")}.',
        "reg": "neutral, negativ, allmän",
        "ety": "av grekiska apatheia; till a- 'icke' och patos 'känsla'",
        "skal": "SAOL: 'håglöshet, likgiltighet' -- båda inleder var sitt led. SO:s "
                "definition använder 'likgiltighet' inne i ledet, men SAOL räcker som "
                "belägg.",
    },
    "bolero": {
        "hb": "spansk dans i trefjärdedelstakt ; kort och öppen jacka",
        "syn": [],
        "grp": None,
        "ex": f'Hon bar en vit {B.format("bolero")} över klänningen.',
        "reg": "neutral, neutral, musik ; neutral, neutral, allmän",
        "ety": "av spanska bolero, namn på en nationaldans; jackan uppkallad efter dansen",
        "skal": "SO ger dansen och jackan; SAOL lägger till en bredbrättad hatt, som "
                "varken SO eller Wiktionary känner igen och som därför utelämnas enligt "
                "källhierarkin. Ingen betydelse har en enordsglosa -- tom lista.",
    },
    "bolster": {
        "hb": "större kudde eller dyna ; metalldel på en kniv som förenar egg och skaft",
        "syn": [],
        "grp": None,
        "ex": f'Hon sjönk ner i ett mjukt {B.format("bolster")} av dun.',
        "reg": "neutral, neutral, allmän ; fackspråklig, neutral, teknik",
        "ety": "fornsvenska bulster; germanskt ord med grundbetydelsen 'något svällande'",
        "skal": "SO ger båda betydelserna; knivdelen är belagd sedan 2005 och är alltså "
                "inte gammal utan ny. SAOL:s 'dyna, täcke' inleder led och belägger "
                "betydelse 1, men betydelse 2 saknar glosa -- alltså tom lista i stället "
                "för en platt.",
    },
    "bondfångare": {
        "hb": "person som lurar godtrogna med enkla knep",
        "syn": ["bedragare"],
        "grp": None,
        "ex": f'Han visade sig vara en {B.format("bondfångare")} som sålt värdelösa aktier.',
        "reg": "neutral, nedsättande, allmän",
        "ety": "efter tyska Bauernfänger med samma betydelse",
        "skal": "SO inleder sin definition med 'bedragare som använder sig av enkla "
                "knep' -- glosan inleder ledet. SAOL: 'person som lurar godtrogna'.",
    },
    "censor": {
        "hb": "person med uppgift att förhandsgranska och kunna stoppa material som ska spridas",
        "syn": ["förhandsgranskare"],
        "grp": None,
        "ex": f'Boken stoppades av en {B.format("censor")} innan den hann tryckas.',
        "reg": "neutral, neutral, politik",
        "ety": "av latin censor 'granskare, övervakare', till censere 'granska, värdera'",
        "skal": "SAOL inleder med 'förhandsgranskare t.ex. av filmer'. SO:s båda övriga "
                "betydelser -- romersk ämbetsman och övervakare av studentexamen -- är "
                "märkta 'förr i Sverige' respektive 'ursprungligen', alltså historiska, "
                "och utelämnas från huvudbetydelsen.",
    },
    "dissident": {
        "hb": "person som öppet har en annan uppfattning än den officiellt erkända",
        "syn": [],
        "grp": None,
        "ex": f'Flera {B.format("dissidenter")} fängslades efter att ha skrivit under uppropet.',
        "reg": "neutral, neutral, politik",
        "ety": "av engelska dissident; av latin dissidere 'sitta åtskils, vara oense'",
        "skal": "SO: 'person som har annan uppfattning än den officiellt erkända'. "
                "'oliktänkande' står i SO:s jfr-fält och inleder inte SAOL:s led -- där "
                "lyder det 'politiskt oliktänkande person', alltså med 'politiskt' "
                "först. Inte belagd enligt regeln, därför tom lista.",
    },
    "fanera": {
        "hb": "belägga en yta med ett tunt skikt av ädlare träslag",
        "syn": [],
        "grp": None,
        "ex": f'Lådbottnarna var {B.format("fanerade")} med ek på ovansidan.',
        "reg": "fackspråklig, neutral, teknik",
        "ety": "till faner",
        "skal": "SO: 'belägga med faner'. SAOL: 'förse med beläggning el. inläggning av "
                "faner'. 'belägga' inleder tekniskt SO:s led, men glosan är identisk med "
                "huvudbetydelsen och därmed cirkulär -- tom lista i stället.",
    },
    "fräkne": {
        "hb": "liten brun pigmentfläck i huden",
        "syn": [],
        "grp": None,
        "ex": f'Sommaren gav henne {B.format("fräknar")} över näsryggen.',
        "reg": "neutral, neutral, allmän",
        "ety": "jfr ursprung till fräknig",
        "skal": "SO och SAOL är nästan ordagrant lika ('liten brun' respektive 'liten "
                "gulbrun pigmentfläck i huden'). 'pigmentfläck' inleder inget led, "
                "eftersom 'liten' står först.",
    },
    "förbehåll": {
        "hb": "särskilt förhandsvillkor för ett godkännande",
        "syn": ["reservation"],
        "grp": None,
        "ex": f'Handlingarna lämnades ut med vissa {B.format("förbehåll")}.',
        "reg": "formell, neutral, allmän",
        "ety": "till förbehålla; av lågtyska vorbehalden",
        "skal": "SO ger 'särskilt förhandsvillkor för godkännande' och som eget led "
                "'reservation' -- glosan ÄR ett helt led. SO:s verbbetydelser ('kräva "
                "att få behålla', 'låta vara i ensam besittning av') hör till "
                "`förbehålla`, inte till substantivet.",
    },
    "gecko": {
        "hb": "liten insektsätande ödla med bred nos och klätterförmåga",
        "syn": [],
        "grp": None,
        "ex": f'En {B.format("gecko")} satt orörlig på väggen ovanför lampan.',
        "reg": "neutral, neutral, biologi",
        "ety": "av malajiska gekoq, bildat efter djurets läte",
        "skal": "SO: 'typ av liten insektsätande, brednosig ödla'. SAOL: 'en ödla'. "
                "Ingen synonym -- 'ödla' är överordnat begrepp, inte synonym, och "
                "inleds dessutom av 'en' i SAOL.",
    },
    "hugad": {
        "hb": "intresserad av att utnyttja en möjlighet",
        "syn": ["intresserad"],
        "grp": None,
        "ex": f'Visningen lockade många {B.format("hugade")} spekulanter.',
        "reg": "formell, neutral, allmän",
        "ety": None,
        "skal": "SO:s hela definition är ordet 'intresserad'. SAOL:s 'hågad' tas INTE "
                "med -- det är samma ord i annan stavning, inte en synonym, och röjer "
                "svaret. Varken SO eller SAOL anger etymologi.",
    },
    "högsinnad": {
        "hb": "som handlar generöst och gärna bortser från oförrätter",
        "syn": ["högsint"],
        "grp": None,
        "ex": f'Fursten var {B.format("högsinnad")} nog att räcka sin besegrade motståndare handen.',
        "reg": "högtidlig, positiv, allmän",
        "ety": None,
        "skal": "SO märker ordet 'högtidligt' och listar 'högsint' med SYN-relation. "
                "'ädel 2' stod först med men ströks: SO märker den JFR:cohyponym, "
                "alltså sidoordnat begrepp och inte synonym. SAOL: 'moraliskt "
                "högtstående'.",
    },
    "kvintessensen": {
        "hb": "det väsentliga eller bästa i något",
        "syn": ["kärna"],
        "grp": None,
        "ex": f'Inledningen ger på fem sidor {B.format("kvintessensen")} av hans tänkande.',
        "reg": "formell, neutral, allmän",
        "ety": "via franska av medeltidslatin quinta essentia 'det femte grundämnet', "
               "alltså etern, som enligt äldre lära kom utöver eld, jord, luft och vatten",
        "skal": "Uppslaget gjordes på lemmat `kvintessens` sedan den bestämda formen gav "
                "`traffar=INGEN`. SAOL: 'det väsentliga el. bästa, kärna' -- 'kärna' "
                "inleder ett eget led. SO: 'det väsentliga av något'. Framsidans "
                "bestämda form är orörd och noterad i ATT_GORA.md.",
    },
    "liberalisera": {
        "hb": "göra lagar eller regler friare och mindre begränsande",
        "syn": [],
        "grp": None,
        "ex": f'Spelmarknaden {B.format("liberaliserades")} i flera steg under 2000-talet.',
        "reg": "neutral, neutral, politik",
        "ety": "till liberal",
        "skal": "SO och SAOL har ordagrant samma definition, 'göra friare'. Den inleder "
                "ledet men är identisk med huvudbetydelsen och alltså cirkulär som "
                "synonym -- tom lista. 'avreglera' finns bara i synonymer.se.",
    },
    "malträtera": {
        "hb": "behandla illa eller misshandla",
        "syn": ["misshandla"],
        "grp": None,
        "ex": f'Han kände sig {B.format("malträterad")} av myndigheternas långa tystnad.',
        "reg": "ngt ålderdomlig, negativ, allmän",
        "ety": "av franska maltraiter, till mal 'dåligt' och traiter 'behandla'",
        "skal": "SO märker ordet 'något ålderdomligt' -- registret följer den märkningen, "
                "det är inte min bedömning. SAOL: 'behandla illa, misshandla', där "
                "'misshandla' inleder ett eget led.",
    },
    "mischmasch": {
        "hb": "helt oordnad blandning",
        "syn": ["röra"],
        "grp": None,
        "ex": f'Rapporten var ett {B.format("mischmasch")} av rykten och lösa antaganden.',
        "reg": "vardaglig, negativ, allmän",
        "ety": "av tyska Mischmasch, till mischen 'blanda'",
        "skal": "SO märker 'vardagligt' och ger 'helt oordnad blandning'. SAOL: 'oredig "
                "blandning, röra' -- 'röra' inleder ett eget led.",
    },
    "murrig": {
        "hb": "sur och vresig ; mörk, grumlig och dyster i färgen",
        "syn": ["knarrig", "surmulen", "mörk"],
        "grp": [["knarrig", "surmulen"], ["mörk"]],
        "ex": f'Väggarna hade en {B.format("murrig")} brungrön ton som slukade allt ljus.',
        "reg": "vardaglig, negativ, allmän ; neutral, lätt negativ, allmän",
        "ety": "till murra",
        "skal": "Båda betydelserna har belagd glosa, alltså grupperas de. SAOL ger "
                "'knarrig, surmulen' för humöret (två egna led) och 'mörk och oklar' "
                "för färgen, där 'mörk' inleder. SO listar humöret först, och den "
                "ordningen följs här.",
    },
    "oavvislig": {
        "hb": "som inte kan avvisas eller nonchaleras",
        "syn": [],
        "grp": None,
        "ex": f'Det var hans {B.format("oavvisliga")} plikt att anmäla saken.',
        "reg": "formell, neutral, allmän",
        "ety": None,
        "skal": "SO: 'som inte kan avvisas eller nonchaleras'. SAOL: 'som inte kan "
                "avvisas'. Båda definitionerna är omskrivningar utan enordsglosa. "
                "'ofrånkomlig' och 'oeftergivlig' finns bara i synonymer.se.",
    },
    "odyssé": {
        "hb": "lång och äventyrlig resa med många upplevelser",
        "syn": [],
        "grp": None,
        "ex": f'Deras {B.format("odyssé")} genom Latinamerika tog nio månader.',
        "reg": "litterär, neutral, allmän",
        "ety": "till grekiska Odysseia, Homeros epos om Odysseus långa hemfärd",
        "skal": "SO: 'lång resa med många sevärdheter och upplevelser'. SAOL: 'lång och "
                "äventyrlig resa'. 'irrfärd' står i SO:s jfr-fält som cohyponym, inte "
                "som synonym -- och betyder dessutom något delvis annat: en irrfärd har "
                "inget mål, en odyssé har det.",
    },
    "ombudsman": {
        "hb": "person som yrkesmässigt bevakar någon annans rättsliga angelägenheter",
        "syn": [],
        "grp": None,
        "ex": f'Facket skickade sin {B.format("ombudsman")} till förhandlingen.',
        "reg": "neutral, neutral, juridik",
        "ety": "fornsvenska umbuds man; belagt sedan slutet av 1200-talet",
        "skal": "SO: '(titel för) person som (yrkesmässigt) sköter juridiska "
                "angelägenheter åt annan part'. Alla glosor i synonymer.se ('ombud', "
                "'representant', 'förtroendeman') saknar belägg i SO och SAOL; SAOL "
                "nöjer sig med exemplet 't.ex. inom fackförbund'.",
    },
    "ovation": {
        "hb": "stormande hyllning med applåder och rop",
        "syn": ["jubel"],
        "grp": None,
        "ex": f'Publiken reste sig och gav henne stående {B.format("ovationer")}.',
        "reg": "neutral, positiv, allmän",
        "ety": "av latin ovatio 'mindre segertåg', till ovare 'jubla'",
        "skal": "SO: 'stormande hyllning, jubel eller bifallsrop'. Ledet delas på komma, "
                "så 'jubel' inleder ett eget led och är belagt -- men 'bifallsrop' "
                "står efter 'eller' inne i samma led och ströks därför.",
    },
    "partikuljär": {
        "hb": "som avviker från det vanliga på ett eget och särpräglat sätt",
        "syn": ["säregen"],
        "grp": None,
        "ex": f'Hans sätt att formulera sig var {B.format("partikuljärt")} och gick inte att ta miste på.',
        "reg": "ngt ålderdomlig, neutral, allmän",
        "ety": "av franska particulier med samma betydelse; till partikulär",
        "skal": "SO:s hela definition är 'säregen', med märkningen 'mindre brukligt'. Den "
                "märkningen saknar exakt motsvarighet i den fasta registerlistan; 'ngt "
                "ålderdomlig' ligger närmast och valdes medvetet framför 'formell'. "
                "Endast två källor -- SAOL och Wiktionary saknar posten helt.",
    },
    "plombera": {
        "hb": "försegla med sigill ; fylla ett hål i en trasig tand",
        "syn": ["försegla", "fylla"],
        "grp": [["försegla"], ["fylla"]],
        "ex": f'Tandläkaren {B.format("plomberade")} hålet i kindtanden.',
        "reg": "ngt ålderdomlig, neutral, teknik ; neutral, neutral, medicin",
        "ety": "till plomb; av franska plomb 'bly', efter de gamla blysigillen",
        "skal": "SAOL: 'försegla med blysigill; fylla (hål i) tand' -- båda betydelserna "
                "får sin egen inledande glosa, alltså grupperas de. SO:s tredje betydelse "
                "(fylla ihålighet i trädstam med betong) är märkt 'äv. utvidgat' och tas "
                "inte med som egen rad. SO:s märkning 'delvis historiskt' gäller "
                "sigillbetydelsen -- blyplomberade järnvägsvagnar -- inte tandlagningen, "
                "därför bär bara första betydelsen 'ngt ålderdomlig'.",
    },
    "preses": {
        "hb": "ordförande i en vetenskaplig akademi",
        "syn": ["ordförande"],
        "grp": None,
        "ex": f'Han valdes till {B.format("preses")} i Vetenskapsakademien.',
        "reg": "formell, neutral, allmän",
        "ety": "av latin praeses 'ordförande, föreståndare'",
        "skal": "SO: 'ordförande i akademi'. SAOL: 'ordförande i akademi e.d.' -- glosan "
                "inleder ledet i båda. Wiktionarys övriga betydelser (ordförande vid "
                "disputation, i domkapitel, vid prästmöte) saknas i SO och SAOL och tas "
                "inte med enligt källhierarkin.",
    },
    "prägel": {
        "hb": "den samlade karaktär som något ger intryck av ; avtryck eller reliefmönster i metall",
        "syn": ["särart", "avtryck", "stämpel"],
        "grp": [["särart"], ["avtryck", "stämpel"]],
        "ex": f'Domkyrkan sätter sin {B.format("prägel")} på hela stadskärnan.',
        "reg": "neutral, neutral, allmän ; fackspråklig, neutral, teknik",
        "ety": "till prägla",
        "skal": "Båda betydelserna har belagd glosa, alltså grupperas de. SAOL: 'avtryck "
                "t.ex. på mynt; stämpel' och 'framkallad beskaffenhet, särart' -- "
                "'avtryck', 'stämpel' och 'särart' inleder var sitt led. SO listar den "
                "abstrakta betydelsen först, och den ordningen följs.",
    },
    "på nåder": {
        "hb": "av någon annans välvilja och överseende, utan egen rätt till det",
        "syn": [],
        "grp": None,
        "ex": f'Efter skilsmässan bodde han {B.format("på nåder")} hos sin bror.',
        "reg": "neutral, lätt negativ, allmän",
        "ety": "till nåd, fornsvenska naþ 'vila, beskydd, nåd'",
        "skal": "Ordboksuppslaget är obrukbart: SO returnerade definitioner för `nåd`, "
                "`nådens år` och `synda på nåden`, ingen av dem frasen. Skrivet mot "
                "allmän websökning enligt Adams regel 2026-08-11. Källorna är eniga om "
                "'leva/bo på nåder' = beroende av någon annans välvilja, ofta med en "
                "nedlåtande underton -- därav lätt negativ valör. Tom synonymlista.",
    },
    "reflektion": {
        "hb": "återkastande av ljus eller ljud ; noggrann eftertanke",
        "syn": [],
        "grp": None,
        "ex": f'Efter en stunds {B.format("reflektion")} ändrade hon sig.',
        "reg": "fackspråklig, neutral, fysik ; neutral, neutral, allmän",
        "ety": None,
        "skal": "SO ger tre betydelser; den tredje ('spontan tanke eller slutsats') är "
                "märkt 'äv.' och ligger nära den andra, så de slås ihop. SAOL:s "
                "'återkastning, återspegling' belägger betydelse 1, men betydelse 2 "
                "saknar inledande enordsglosa -- SO skriver 'noggrann (och djup) "
                "eftertanke', där 'noggrann' står först. Alltså tom lista i stället för "
                "en platt. Varken SO eller SAOL anger etymologi.",
    },
    "råk": {
        "hb": "långsträckt spricka med öppet vatten i isen på en sjö eller ett hav",
        "syn": [],
        "grp": None,
        "ex": f'Skridskoåkarna vek av i god tid för att undvika en {B.format("råk")} i isen.',
        "reg": "neutral, neutral, allmän",
        "ety": "svensk dialekt råk 'hårbena; strömfåra'; troligen besläktat med rak",
        "skal": "SO och SAOL är eniga och rena: 'långsträckt spricka med öppet vatten i "
                "isbeläggning' respektive 'bred spricka i is'. Synonymlistan från "
                "synonymer.se är däremot smittad av grannorden `råka` och `rå` -- den "
                "innehåller 'bortrensat innanmäte', 'avfall' och 'på sin tallrik'. "
                "Ingenting därifrån används; tom lista.",
    },
    "sanktionera": {
        "hb": "officiellt godkänna eller stadfästa",
        "syn": ["stadfästa", "godkänna"],
        "grp": None,
        "ex": f'Utspelet var {B.format("sanktionerat")} av hela partiledningen.',
        "reg": "formell, neutral, politik",
        "ety": "till sanktion",
        "skal": "SO: 'officiellt godkänna eller godta'. SAOL: 'stadfästa, godkänna' -- "
                "båda inleder var sitt led. SAOL:s andra rad, 'införa sanktioner', står "
                "som ren korshänvisning (`till sanktion 2`) och saknas helt i SO; en "
                "korshänvisning är inte en definition, så den tas inte med.",
    },
    "sensualism": {
        "hb": "inriktning på det sinnliga ; uppfattningen att allt vetande kommer ur sinnesintryck",
        "syn": [],
        "grp": None,
        "ex": f'Romanens {B.format("sensualism")} märks i varje beskrivning av mat och väder.',
        "reg": "formell, neutral, allmän ; fackspråklig, neutral, filosofi",
        "ety": "till sensuell",
        "skal": "SO ger den estetiska betydelsen, SAOL lägger till den filosofiska -- "
                "två skilda betydelser som båda hör hit. SAOL:s 'sensualitet' inleder "
                "visserligen ett led men tas INTE med: den delar hela ordstammen med "
                "uppslagsordet och röjer svaret på framsidan.",
    },
    "skrank": {
        "hb": "avskiljande räcke i offentlig lokal, särskilt framför domarbordet i en rättssal",
        "syn": [],
        "grp": None,
        "ex": f'Den forne diktatorn ställdes till sist inför {B.format("skranket")}.',
        "reg": "neutral, neutral, juridik",
        "ety": "av lågtyska schrank 'galler, avspärrning'; besläktat med inskränka",
        "skal": "SO: 'avskiljande räcke', plus den bundna frasen 'stå/ställas inför "
                "skranket' = prövas inför domstol. Frasbetydelsen bärs av uttrycket, "
                "inte av ordet ensamt, och skrivs därför in i huvudbetydelsen via "
                "rättssalen i stället för som egen rad. 'räcke' inleder inget led "
                "('avskiljande' står först), så tom lista.",
    },
    "sprättig": {
        "hb": "som uppträder överdrivet elegant och självbelåtet",
        "syn": ["snobbig"],
        "grp": None,
        "ex": f'En {B.format("sprättig")} ung officer gjorde entré mitt under middagen.',
        "reg": "neutral, nedsättande, allmän",
        "ety": "till sprätt",
        "skal": "SAOL:s hela definition är 'snobbig'. SO: 'som uppträder som en sprätt' "
                "-- den formuleringen kan inte användas som huvudbetydelse eftersom den "
                "innehåller uppslagsordets stam. Varken SO eller SAOL sätter "
                "bruklighetsmärkning, så registret är neutralt trots att ordet känns "
                "gammaldags.",
    },
    "tafatt": {
        "hb": "som uppträder oskickligt och klumpigt ; en springlek där man ska hinna ifatt de andra",
        "syn": [],
        "grp": None,
        "ex": f'Hans {B.format("tafatta")} försök att inleda ett samtal gjorde saken värre.',
        "reg": "neutral, lätt negativ, allmän ; neutral, neutral, sport",
        "ety": "till tag och få, alltså 'med liten företagsamhet'; leken till ta och fatt",
        "skal": "Två ord med skild etymologi som fallit ihop i formen -- SO ger dem "
                "olika ursprung och olika första belägg (1769 respektive 1687). SAOL: "
                "'fumlig, klumpig' belägger betydelse 1, men leken har bara 'en lek' "
                "som definition. Alltså tom lista i stället för en platt. Synonymlistan "
                "från synonymer.se är dessutom trasig och innehåller uttalsangivelser "
                "och avhuggna exempelmeningar.",
    },
    "till fromma för": {
        "hb": "till nytta eller gagn för",
        "syn": [],
        "grp": None,
        "ex": f'Vi avstår från flygresan {B.format("till fromma för")} miljön.',
        "reg": "formell, positiv, allmän",
        "ety": "fornsvenska froma 'nytta'; av lågtyska vrome 'nytta, fördel'",
        "skal": "Uppslaget blandar `from` ('stillsamt religiös', 'from som ett lamm') "
                "med `fromma` ('fördel'). Bara den senare hör till frasen. SO:s egen "
                "exempelrad -- 'konkurrensen mellan varuhusen ökar, till konsumenternas "
                "fromma' -- och en allmän websökning ger samma betydelse. Tom "
                "synonymlista, eftersom ingen glosa kan skiljas rent från fel post.",
    },
    "tillknäppt": {
        "hb": "som ogärna deltar i samtal eller umgänge ; mycket defensiv i sitt spel",
        "syn": ["tystlåten", "defensiv"],
        "grp": [["tystlåten"], ["defensiv"]],
        "ex": f'Han var {B.format("tillknäppt")} och svarade bara med enstaviga ord.',
        "reg": "neutral, lätt negativ, allmän ; neutral, neutral, sport",
        "ety": None,
        "skal": "Båda betydelserna har belagd glosa, alltså grupperas de. SAOL: 'mest "
                "bildl. svårtillgänglig, tystlåten; defensiv' -- 'tystlåten' och "
                "'defensiv' inleder var sitt led. 'svårtillgänglig' stod först med men "
                "ströks: det inleds av 'mest bildl.', som inte skalas bort, och räknas "
                "därför inte som belagt.",
    },
    "töcknig": {
        "hb": "insvept i dimma eller dis ; intellektuellt oklar och suddig",
        "syn": [],
        "grp": None,
        "ex": f'Silhuetterna på andra sidan viken var {B.format("töckniga")} i gryningsljuset.',
        "reg": "neutral, neutral, allmän ; neutral, lätt negativ, allmän",
        "ety": None,
        "skal": "SO ger 'uppfylld av töcken', '(delvis) dold av töcken' och "
                "'(intellektuellt) oklar'. De två första slås ihop och skrivs om -- "
                "ordboksformuleringen innehåller `töcken`, alltså uppslagsordets stam, "
                "och avslöjar svaret på framsidan precis som fällde `urmodig`. "
                "'dimmig' och 'disig' står i SO:s jfr-fält som cohyponymer, inte som "
                "synonymer. SAOL saknar definitionstext.",
    },
    "vind för våg": {
        "hb": "utan tillsyn och utan att någon bryr sig om hur det går",
        "syn": [],
        "grp": None,
        "ex": f'Efter konkursen lämnades hela anläggningen {B.format("vind för våg")}.',
        "reg": "neutral, lätt negativ, allmän",
        "ety": "förvanskning av det äldre '(segla) för vind och våg', om ett fartyg som "
               "lät vinden och vågorna bestämma kursen",
        "skal": "Grövsta föroreningen i batchen: SO returnerade `våg`, `vind`, "
                "`vågrörelse` och `grön våg` ('samordning av trafikljus'). Frasen själv "
                "fanns bara som exempelrad utan definition. Skriven mot allmän "
                "websökning enligt regeln 2026-08-11; källorna ger entydigt 'utan "
                "tillsyn' och bekräftar sjöfartsursprunget. Tom synonymlista.",
    },
}


def main():
    data = json.load(open(SESSION, encoding="utf-8"))
    poster = data["poster"] if isinstance(data, dict) else data

    kvar = [p for p in poster if p["ord"] not in PAUSAS]
    pausade = [p["ord"] for p in poster if p["ord"] in PAUSAS]

    saknar = [p["ord"] for p in kvar if p["ord"] not in KORT]
    if saknar:
        sys.exit(f"saknar rättelse för: {', '.join(saknar)}")

    for p in kvar:
        o = p["ord"]
        r = KORT[o]
        p["proposed"] = {
            "huvudbetydelse": r["hb"][0].upper() + r["hb"][1:],
            "synonymer": r["syn"],
            "synonym_groups": r.get("grp"),
            "exempelmening": r["ex"],
            "register": r["reg"],
            "etymologi": r.get("ety"),
        }
        p["approved"] = True
        if o in TILLAT:
            p["forgranska_tillat"] = TILLAT[o]
        p["sokkoll"] = {
            "kalla": SVENSKA.format(urllib.parse.quote(K.get(o, o))),
            "slutsats": r["skal"],
        }
        p.pop("applicerad", None)

    if isinstance(data, dict):
        data["poster"] = kvar
        ut = data
    else:
        ut = kvar
    json.dump(ut, open(SESSION, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    tomma = sum(1 for p in kvar if not p["proposed"]["synonymer"])
    grupperade = sum(1 for p in kvar if p["proposed"]["synonym_groups"])
    flerbet = sum(1 for p in kvar if ";" in p["proposed"]["huvudbetydelse"])
    print(f"fyllde {len(kvar)} poster -- {tomma} med tom synonymlista, "
          f"{grupperade} med grupperade synonymer av {flerbet} flerbetydelsekort.")
    if pausade:
        print(f"UTESLUTNA (pausas separat): {', '.join(pausade)}")


if __name__ == "__main__":
    main()
