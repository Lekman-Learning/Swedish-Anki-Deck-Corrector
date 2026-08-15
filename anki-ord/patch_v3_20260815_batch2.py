# -*- coding: utf-8 -*-
"""50 provisoriska kort ur spår B (is:review, sökkollade men ej full v3) -> full v3.

## Regeln som styrde den här batchen

Blindgranskningen av dagens första batch underkände **fem kort, alla för samma
sak: bortskalade betydelser** -- och tre av dem hade jag uttryckligen motiverat i
patchens avsnitt om medvetna avgränsningar. Samma fel fällde `tariff`, `potpurri`
och `excellera` den 13 augusti. Mönstret är tre batcher gammalt.

**Regeln här är därför omvänd mot förut: står betydelsen i SO eller SAOL kommer
den med.** Tveksamma fall löses genom att ta med, inte genom att skriva en fotnot
om varför den utelämnats. En motivering i patchen är inte samma sak som att ha
rätt.

Följden syns i `abrovink`-felet från förra omgången: **`eller` får aldrig stå
mellan två skilda betydelser** -- där ska det vara ` ; `.

## Nio ord med förorenat underlag

Den här poolen är värre än spår A, eftersom den innehåller fler flerordsuttryck:

* `alla taggar utåt` fick hela posten för **`utåt`** ("dörren öppnas utåt")
* `få nöja sig med smulorna från den rikes bord` fick **`bord`**, inklusive
  "slå näven i bordet" och bridgetermer
* `klä skott för något` fick **`skott`** -- projektil, växtskott och skiljevägg
  i fartyg
* `barka åt skogen` fick **`barka`** i betydelsen 'skala bark av'
* `lid` fick **`lida`** (utstå smärta) -- helt annat ord
* `fiken` fick **`fik`** (kaféet), som är ett annat ord än adjektivet
* `divan` fick **`diva`** i bestämd form
* `regel / rigel` fick **`regel`** i betydelsen 'föreskrift, norm'
* `förtörnad` fick verbet **`förtörna`**

Fyra av dem -- `alla taggar utåt`, `smulorna från den rikes bord`,
`klä skott för något` och `barka åt skogen` -- är skrivna mot **allmän
websökning** enligt Adams regel 2026-08-11.

## Fyndet om smulorna

Uttrycket är **bibliskt** och det förklarar tonen: det kommer ur liknelsen om den
rike mannen och Lasarus (Luk. 16:20-21), där tiggaren låg vid porten och gärna
velat mätta sig med smulorna som föll från bordet. Det är alltså inte bara "få
lite" utan "få det andra inte brydde sig om" -- därav domänen `bibliskt` och den
lätt negativa valören.

## Grupperade synonymer

Fem kort har belagd glosa för **varje** betydelse och grupperas: `binge`,
`drägg`, `evalvera`, `lämpa`, `plombera`-mönstret från batch 1. Övriga
flerbetydelsekort får tom lista hellre än en platt.

## Avgränsningar -- färre än förra gången, med flit

* **`vitsord` får inte den juridiska betydelsen 'beviskraft'.** Den finns i SAOB
  men i varken SO eller SAOL, och källhierarkin låter de två avgöra dagens
  betydelser. SAOL:s finlandssvenska 'betyg i enskilt ämne' är märkt `finl.` och
  är en regional variant av samma betydelse, inte en egen.
* **`köpeskilling` får tom synonymlista** trots att SAOL:s hela definition är
  `köpesumma`. Glosan delar förleden `köpe-` och röjer halva ordet.
* **`strömning`** likaså: SAOL:s 'strömmande; ström' innehåller uppslagsordets
  stam.
* **`kelen`** likaså: SO:s definition ÄR `kelsjuk`.
* **`hövisk` märks INTE ålderdomlig.** SO skriver "särsk. vid beskrivning av
  äldre förhållanden" -- det beskriver vad ordet används OM, inte hur brukligt
  ordet är. Samma fälla som `paletå` den 13 augusti.
"""
import json
import sys
import urllib.parse

SESSION = "sessions/session_2026-08-15_v3-omgranskning-repetition.json"
SVENSKA = "https://svenska.se/api/msearch?ord={}"

# Kortets framsida -> det uppslagsord som faktiskt slogs upp.
K = {
    "regel / rigel": "rigel",
}

PAUSAS = set()

TILLAT = {
    "alla taggar utåt": {
        "frammande_uppslagsord":
            "Flerordsfras: fritextsökningen returnerade hela posten för `utåt` "
            "('dörren öppnas utåt', 'gå utåt med fötterna') plus växtsläktet "
            "aralia. Frasen själv finns inte som uppslagsord. Skriven mot allmän "
            "websökning enligt regeln 2026-08-11: uttrycket betyder att vara i "
            "försvarsställning och avvisa allt som sägs, och kommer av igelkotten "
            "som reser taggarna. Synonymlistan är tom.",
    },
    "få nöja sig med smulorna från den rikes bord": {
        "frammande_uppslagsord":
            "Grövsta fallet: svaret gäller `bord` i alla dess betydelser -- "
            "möbeln, bordet med framdukade rätter, 'slå näven i bordet', 'pengar "
            "under bordet' och de upplagda korten i bridge. Skriven mot allmän "
            "websökning, som ger det bibliska ursprunget (liknelsen om den rike "
            "mannen och Lasarus, Luk. 16:20-21). Synonymlistan är tom.",
    },
    "klä skott för något": {
        "frammande_uppslagsord":
            "Svaret gäller `skott` -- projektil, fotbollsskott, växtskott och "
            "skiljevägg i fartyg. SO:s andra definition ('utsättas för kritik') "
            "hör dock till frasen, och SO:s egen etymologirad daterar idiomet till "
            "1596 med grundbetydelsen 'uthärda beskjutning, utgöra måltavla för'. "
            "Bekräftat med websökning. Synonymlistan är tom.",
    },
    "barka åt skogen": {
        "frammande_uppslagsord":
            "Svaret blandar `barka` i betydelsen 'skala bort bark' och 'behandla "
            "segel med garvämnen' med den rätta. SO:s tredje definition, "
            "'utvecklas på visst (okontrollerat) sätt', har frasen som eget "
            "exempel, och synonymer.se och Wiktionary ger båda 'gå på tok'. "
            "Synonymlistan är tom eftersom glosorna inte kan skiljas rent.",
        "register_motsager_markning":
            "Märkningen 'delvis historiskt' hör till `barka` = 'behandla segel med "
            "garvämnen ur bark', ett hantverk som knappt utövas längre. Idiomet är "
            "levande vardagsspråk.",
    },
    "lid": {
        "frammande_uppslagsord":
            "Träffarna domineras av `lida` (utstå smärta, framskrida) -- ett helt "
            "annat ord med egen etymologi. Kortet bygger uteslutande på SO:s och "
            "SAOL:s substantivpost: 'sluttande stycke mark eller väg' respektive "
            "'backe, sluttning'. Synonymerna kommer bara från SAOL:s post.",
    },
    "fiken": {
        "frammande_uppslagsord":
            "Svaret slår ihop adjektivet `fiken` ('som har starkt begär') med "
            "substantivet `fik` ('enklare kafé') -- SO ger dem skild etymologi och "
            "skilda första belägg (1300-tal respektive 1934). Kortet använder bara "
            "adjektivposten; synonymen `lysten` är SAOL:s definition av just den.",
        "register_motsager_markning":
            "SO ger TVÅ märkningar i samma svar: 'mindre brukligt' för adjektivet "
            "`fiken` och 'vardagligt' för substantivet `fik`; SAOL:s 'vard.' hör "
            "likaså till kaféet. Kortet gäller adjektivet, och dess märkning "
            "'mindre brukligt' saknar exakt motsvarighet i den fasta listan -- "
            "`ngt ålderdomlig` ligger närmast.",
    },
    "divan": {
        "frammande_uppslagsord":
            "Formen är tvetydig: `divan` är dels möbeln (grundform), dels bestämd "
            "form av `diva`. SO och SAOL listar båda i samma svar. Kortet skriver "
            "möbeln, som är den form uppslagsordet faktiskt har -- `diva` är ett "
            "eget uppslagsord med egen etymologi (italienska diva 'gudomlig' mot "
            "persiska diwan 'skrivrum'). Tvetydigheten är noterad i ATT_GORA.md.",
    },
    "regel / rigel": {
        "frammande_uppslagsord":
            "Framsidan ger två stavningar av samma ord, och `regel` är dessutom "
            "ett helt annat ord ('föreskrift, norm'), som dominerar träffarna. "
            "Uppslaget gjordes därför på `rigel`, som bara har låsanordnings- och "
            "trävirkesbetydelserna; `kalla` pekar dit via K-mappningen.",
    },
    "konsiliant": {
        "frammande_uppslagsord":
            "Enda främmande träffen är `konciliant`, som är SAMMA ord i den "
            "vanligare stavningen -- SO:s definition lyder 'som präglas av "
            "koncilians' med exemplet 'en konciliant person', och Wiktionary "
            "kallar `konsiliant` en variant av `konciliant`. Det finns bara ett "
            "ord. Synonymlistan är dessutom tom.",
    },
    "vitsord": {
        "register_motsager_markning":
            "Märkningen `finl.` gäller SAOL:s ANDRA betydelse, 'betyg i enskilt "
            "ämne', som är finlandssvenskt bruk. Kortets huvudbetydelse är den "
            "allmänsvenska -- formellt utlåtande med värderande bedömning -- som "
            "varken SO eller SAOL märker regionalt. Registerlistan har inte heller "
            "någon term för finlandssvenska.",
    },
    "förtörnad": {
        "frammande_uppslagsord":
            "Uppslagsordsträffen är `förtörna`, verbet som participet bildas av -- "
            "svaret gav ingen egen post för participformen. SO:s 'starkt förarga' "
            "med märkningen 'något högtidligt' och SAOL:s 'bli arg' beskriver "
            "samma ord i verbform; kortet skriver participets betydelse. "
            "Synonymlistan är tom.",
    },
}

B = '<font color="#3498db">{}</font>'

KORT = {
    "alla taggar utåt": {
        "hb": "i försvarsställning och avvisande mot allt som sägs",
        "syn": [],
        "grp": None,
        "ex": f'Hon kom till mötet med {B.format("alla taggar utåt")} och lyssnade inte på ett ord.',
        "reg": "vardaglig, lätt negativ, allmän",
        "ety": "bildligt av igelkotten, som reser taggarna när den känner sig hotad",
        "skal": "Ordboksuppslaget gäller `utåt`, inte frasen. Skriven mot allmän "
                "websökning: uttrycket betyder att vara defensiv och sluten för "
                "avvikande åsikter, och bilden kommer från igelkottens uppresta taggar.",
    },
    "beskärm": {
        "hb": "skydd och värn, ofta om Guds omsorg",
        "syn": ["skydd", "beskydd"],
        "grp": None,
        "ex": f'De sökte sig under kyrkans {B.format("beskärm")} när förföljelserna började.',
        "reg": "högtidlig, positiv, bibliskt",
        "ety": "fornsvenska beskärm; jfr beskärma",
        "skal": "SO: 'skydd och värn', märkt 'särsk. bibliskt', med exemplet 'under den "
                "Allsmäktiges beskärm'. SAOL: 'beskydd', märkt 'bibl.' -- båda glosorna "
                "inleder sina led. Domänen `bibliskt` följer ordböckernas egen märkning.",
    },
    "förvärva": {
        "hb": "bli ägare till ; gradvis lära in eller skaffa sig",
        "syn": [],
        "grp": None,
        "ex": f'Kommunen fick erbjudande om att {B.format("förvärva")} byggnaden.',
        "reg": "formell, neutral, allmän ; neutral, neutral, allmän",
        "ety": "fornsvenska forvärva; av lågtyska vorwerven; jfr värva",
        "skal": "SO ger två betydelser: 'bli ägare till' och 'gradvis lära in' "
                "(förvärva kunskaper, förvärvade behov i motsats till medfödda). "
                "Ingen av dem har en inledande enordsglosa, så tom lista.",
    },
    "apoplexi": {
        "hb": "slaganfall orsakat av blödning eller propp i hjärnan",
        "syn": ["slaganfall", "hjärnblödning"],
        "grp": None,
        "ex": f'Han drabbades av {B.format("apoplexi")} och förlorade talförmågan.',
        "reg": "fackspråklig, neutral, medicin",
        "ety": "av grekiska apoplexia med samma betydelse",
        "skal": "SO: 'slaganfall'. SAOL: 'slaganfall, hjärnblödning' -- båda inleder "
                "var sitt led och är belagda.",
    },
    "attribuera": {
        "hb": "ange ett anonymt verk som troligen skapat av en viss upphovsman",
        "syn": ["hänföra"],
        "grp": None,
        "ex": f'Målningen har {B.format("attribuerats")} till Rembrandt.',
        "reg": "fackspråklig, neutral, konst",
        "ety": "av latin attribuere 'tilldela'; jfr attribut",
        "skal": "SAOL: 'hänföra ngt anonymt till ngn som upphovsman' -- 'hänföra' "
                "inleder ledet. SO: 'ange såsom troligen skapad av'. 'tillskriva' står i "
                "SO:s jfr-fält som cohyponym, inte som synonym.",
    },
    "barka åt skogen": {
        "hb": "utvecklas åt fel håll och sluta illa",
        "syn": [],
        "grp": None,
        "ex": f'Efter andra baklängesmålet {B.format("barkade")} det {B.format("åt skogen")} för hemmalaget.',
        "reg": "vardaglig, negativ, allmän",
        "ety": "till barka i betydelsen 'utvecklas okontrollerat'",
        "skal": "SO:s tredje betydelse, 'utvecklas på visst (okontrollerat) sätt', har "
                "frasen som eget exempel; de övriga träffarna gäller `barka` = skala "
                "bark. Synonymer.se och Wiktionary ger båda 'gå på tok'. Bekräftat med "
                "websökning eftersom underlaget är blandat.",
    },
    "bygdemål": {
        "hb": "dialekt som talas i en viss trakt",
        "syn": ["dialekt"],
        "grp": None,
        "ex": f'Hon skrev sina dikter på hemtraktens {B.format("bygdemål")}.',
        "reg": "ngt ålderdomlig, neutral, lingvistik",
        "ety": None,
        "skal": "SAOL:s hela definition är 'dialekt'. SO: 'dialekt som talas i en viss "
                "trakt', märkt 'något ålderdomligt' -- registret följer den märkningen.",
    },
    "despot": {
        "hb": "härskare som utsätter sina underlydande för godtyckligt förtryck ; upplyst enväldig statschef på 1700-talet",
        "syn": [],
        "grp": None,
        "ex": f'Bruksägaren styrde byn som en {B.format("despot")}, utan att fråga någon.',
        "reg": "neutral, nedsättande, politik ; neutral, neutral, historia",
        "ety": "av grekiska despotes 'härskare, husbonde'",
        "skal": "SO ger två betydelser, och den andra -- 'statschef som utövade upplyst "
                "despotism', med Fredrik den store som exempel -- är historiskt neutral "
                "och inte nedsättande. SAOL:s 'förtryckare; självhärskare' belägger bara "
                "betydelse 1, så listan lämnas tom i stället för platt.",
    },
    "dignitär": {
        "hb": "innehavare av hög värdighet eller högt ämbete",
        "syn": ["överhetsperson"],
        "grp": None,
        "ex": f'Ärkebiskopen och de andra kyrkliga {B.format("dignitärerna")} tog plats längst fram.',
        "reg": "formell, neutral, allmän",
        "ety": "av franska dignitaire; till dignitet",
        "skal": "SAOL: 'överhetsperson, person av rang' -- 'överhetsperson' inleder "
                "ledet. SO: 'innehavare av hög värdighet eller högt ämbete'.",
    },
    "divan": {
        "hb": "låg soffa utan ryggstöd och karmar",
        "syn": [],
        "grp": None,
        "ex": f'Hon vilade på {B.format("divanen")}, stödd på en mängd kuddar.',
        "reg": "neutral, neutral, allmän",
        "ety": "ur persiska diwan 'register; skrivrum, ämbetsrum'",
        "skal": "Formen är tvetydig -- `divan` är både möbelns grundform och bestämd "
                "form av `diva`. Kortet skriver möbeln, som är det uppslagsord formen "
                "faktiskt utgör; `diva` har egen etymologi (italienska diva 'gudomlig'). "
                "SO: 'låg soffa utan ryggstöd och karmar'. Ingen glosa inleder ett led.",
    },
    "duka under": {
        "hb": "till slut ge vika och gå under",
        "syn": ["omkomma", "förolyckas"],
        "grp": None,
        "ex": f'Hon {B.format("dukade")} till sist {B.format("under")} för sjukdomen.',
        "reg": "neutral, negativ, allmän",
        "ety": "av lågtyska underduken 'dyka ner'; jfr ducka, dyka",
        "skal": "SO:s hela definition är 'omkomma'. SAOL: 'gå under, förolyckas' -- "
                "'förolyckas' inleder ett eget led. Huvudbetydelsen undviker att upprepa "
                "'gå under', eftersom det ligger för nära uppslagsordets egen form.",
    },
    "enaktare": {
        "hb": "skådespel eller teaterpjäs i en enda akt",
        "syn": [],
        "grp": None,
        "ex": f'Strindbergs {B.format("enaktare")} spelades på en liten scen utan paus.',
        "reg": "neutral, neutral, konst",
        "ety": None,
        "skal": "SO: 'skådespel i en akt'. SAOL: 'teaterpjäs i en akt'. 'skådespel' "
                "inleder visserligen SO:s led men är ett överordnat begrepp, inte en "
                "synonym -- alla enaktare är skådespel, inte tvärtom. Endast två källor: "
                "varken synonymer.se eller Wiktionary har posten.",
    },
    "excentrisk": {
        "hb": "som ligger utanför medelpunkten ; som beter sig påfallande avvikande",
        "syn": [],
        "grp": None,
        "ex": f'En {B.format("excentrisk")} lord som höll apa som sällskapsdjur.',
        "reg": "fackspråklig, neutral, matematik ; neutral, lätt negativ, allmän",
        "ety": "bildning till latin ex 'ut' och centrum 'medelpunkt'",
        "skal": "SO ger den geometriska betydelsen (med `koncentrisk` som antonym) och "
                "beteendebetydelsen. SAOL: 'utanför medelpunkten' och 'underlig, egen' -- "
                "de senare belägger bara betydelse 2, så listan lämnas tom i stället för "
                "platt.",
    },
    "fiken": {
        "hb": "som har ett starkt och otåligt begär efter något",
        "syn": ["lysten"],
        "grp": None,
        "ex": f'Han kastade {B.format("fikna")} blickar mot fatet med bakelser.',
        "reg": "ngt ålderdomlig, lätt negativ, allmän",
        "ety": "fornsvenska fikin; till fika 'sträva efter'",
        "skal": "SAOL:s definition av adjektivet är 'lysten'. SO märker just den "
                "betydelsen 'mindre brukligt' -- därav registret. Kafébetydelsen i "
                "svaret hör till `fik`, ett annat ord med annan etymologi.",
    },
    "formsak": {
        "hb": "något som bara behöver göras för formens skull",
        "syn": ["formalitet"],
        "grp": None,
        "ex": f'Eftersom segern redan var klar var sista omgången en ren {B.format("formsak")}.',
        "reg": "neutral, neutral, allmän",
        "ety": None,
        "skal": "SO och SAOL ger båda 'formalitet' som hela definitionen, och SO taggar "
                "den dessutom SYN:synonym -- starkast möjliga belägg.",
    },
    "futurolog": {
        "hb": "person som yrkesmässigt studerar och förutsäger framtida utveckling",
        "syn": ["framtidsforskare"],
        "grp": None,
        "ex": f'En {B.format("futurolog")} bjöds in för att tala om arbetsmarknaden 2050.',
        "reg": "neutral, neutral, allmän",
        "ety": "efter engelska futurologist; jfr futurum",
        "skal": "SO:s hela definition är 'framtidsforskare'. SAOL har posten men utan "
                "definitionstext. Endast två källor -- Wiktionary saknar ordet.",
    },
    "få nöja sig med smulorna från den rikes bord": {
        "hb": "få bara det lilla som blir över sedan andra tagit det mesta",
        "syn": [],
        "grp": None,
        "ex": f'De små åkerierna fick {B.format("nöja sig med smulorna från den rikes bord")} när kontraktet delades ut.',
        "reg": "högtidlig, lätt negativ, bibliskt",
        "ety": "efter liknelsen om den rike mannen och Lasarus (Luk. 16:20–21), där "
               "tiggaren låg vid porten och gärna velat mätta sig med smulorna som föll "
               "från den rikes bord",
        "skal": "Ordboksuppslaget gäller `bord` i alla betydelser, inklusive bridge och "
                "'slå näven i bordet'. Skriven mot allmän websökning, som ger det "
                "bibliska ursprunget. Det förklarar tonen: uttrycket handlar inte bara "
                "om att få lite, utan om att få det de andra inte brydde sig om.",
    },
    "förtörnad": {
        "hb": "starkt förargad och vred",
        "syn": [],
        "grp": None,
        "ex": f'Kungen blev {B.format("förtörnad")} över den brist på aktning som visades honom.',
        "reg": "högtidlig, negativ, allmän",
        "ety": "fornsvenska fortörna; av lågtyska vortörnen, till torn 'vrede'",
        "skal": "Uppslaget gav bara verbet `förtörna` -- 'starkt förarga', märkt 'något "
                "högtidligt' -- och SAOL:s 'bli arg, göra arg'. Kortet skriver "
                "participets betydelse. Synonymlistan är tom: synonymer.se:s förslag "
                "('förargad', 'förbittrad') inleder inget led i SO eller SAOL.",
    },
    "heteronom": {
        "hb": "styrd av regler som kommer utifrån i stället för inifrån",
        "syn": ["osjälvständig"],
        "grp": None,
        "ex": f'En {B.format("heteronom")} moral hämtar sina regler från auktoriteter utanför individen.',
        "reg": "fackspråklig, neutral, filosofi",
        "ety": None,
        "skal": "SO saknar ordet helt. SAOL: 'osjälvständig, styrd utifrån' -- glosan "
                "inleder ledet. Endast två källor (SAOL och SAOB); varken synonymer.se "
                "eller Wiktionary har posten. Motsatsen är `autonom`.",
    },
    "hövisk": {
        "hb": "artig och taktfull på ett förfinat och elegant sätt",
        "syn": ["ärbar", "taktfull", "ridderlig"],
        "grp": None,
        "ex": f'En {B.format("hövisk")} butler tog emot dem i hallen.',
        "reg": "formell, positiv, allmän",
        "ety": "fornsvenska hövisker; av lågtyska hövesch, till hov — efter franska "
               "courtois, till cour 'hov'",
        "skal": "SAOL: 'ärbar, taktfull; ridderlig' -- alla tre inleder var sitt led. "
                "SO:s märkning 'särsk. vid beskrivning av äldre förhållanden' beskriver "
                "vad ordet används OM, inte hur brukligt ordet är, och gör det därför "
                "INTE ålderdomligt -- samma fälla som `paletå`.",
    },
    "kelen": {
        "hb": "som gärna vill smekas och sitta nära",
        "syn": [],
        "grp": None,
        "ex": f'Katten blev {B.format("kelen")} så fort den satte sig i knät.',
        "reg": "vardaglig, ömsint, allmän",
        "ety": None,
        "skal": "SO:s hela definition är 'kelsjuk' och SAOL:s 'som gärna vill kela' -- "
                "båda innehåller uppslagsordets stam och kan varken bli synonym eller "
                "huvudbetydelse. 'smeksam' står i SO:s jfr-fält som cohyponym. Båda "
                "ordböckerna märker ordet vardagligt.",
    },
    "klä skott för något": {
        "hb": "få ta emot kritik eller skuld för något man inte själv orsakat",
        "syn": [],
        "grp": None,
        "ex": f'Hon har ofta fått {B.format("klä skott för")} åsikter hon aldrig framfört.',
        "reg": "neutral, lätt negativ, allmän",
        "ety": "belagt sedan 1596, ursprungligen 'uthärda beskjutning, utgöra måltavla för'",
        "skal": "SO:s andra betydelse, 'utsättas för kritik', har frasen som eget "
                "exempel, och SO:s etymologirad daterar idiomet och ger grundbetydelsen. "
                "Övriga träffar gäller `skott` = projektil, växtskott och skiljevägg i "
                "fartyg.",
    },
    "konsiliant": {
        "hb": "försonlig och tillmötesgående i sitt sätt",
        "syn": [],
        "grp": None,
        "ex": f'Han var {B.format("konsiliant")} i förhandlingen och gav efter på flera punkter.',
        "reg": "ngt ålderdomlig, positiv, allmän",
        "ety": "av franska conciliant 'försonlig'; jfr koncilium",
        "skal": "SO märker ordet 'något ålderdomligt'. SAOL ger 'försonlig, smidig', men "
                "de glosorna ligger under stavningsvarianten `konciliant`, som är ett "
                "eget uppslagsord i svaret -- de räknas därför inte som belägg för den "
                "här formen, och listan lämnas tom. Två källor; Wiktionary hänvisar "
                "bara vidare till konciliant.",
    },
    "köpeskilling": {
        "hb": "den summa som betalas vid ett köp",
        "syn": [],
        "grp": None,
        "ex": f'Företaget förvärvade fastigheten till en {B.format("köpeskilling")} på tio miljoner kronor.',
        "reg": "formell, neutral, juridik",
        "ety": "till skilling i betydelsen 'avgift'",
        "skal": "SAOL:s hela definition är 'köpesumma', vilket tekniskt är belagt -- men "
                "glosan delar förleden `köpe-` med uppslagsordet och röjer halva svaret. "
                "Tom lista i stället.",
    },
    "lid": {
        "hb": "sluttande stycke mark eller väg",
        "syn": ["backe", "sluttning"],
        "grp": None,
        "ex": f'Stigen gick uppför en brant {B.format("lid")} mot fäboden.',
        "reg": "högtidlig, neutral, allmän",
        "ety": "fornsvenska liþ '(bergs)sluttning'; besläktat med latin clivus 'kulle'",
        "skal": "SAOL: 'backe, sluttning' -- båda inleder var sitt led. SO märker ordet "
                "'något högtidligt el. dialektalt'; av de två valdes `högtidlig`, "
                "eftersom `dialektal` skulle antyda att ordet saknas i standardspråket. "
                "Övriga träffar gäller `lida`, ett annat ord.",
    },
    "moratorium": {
        "hb": "överenskommet tillfälligt avbrott i en verksamhet ; anstånd med betalning av en skuld",
        "syn": [],
        "grp": None,
        "ex": f'Flera delstater införde ett {B.format("moratorium")} för avrättningar.',
        "reg": "formell, neutral, politik ; formell, neutral, ekonomi",
        "ety": "bildning till latin mora 'dröjsmål'",
        "skal": "SO ger båda betydelserna, med skilda första belägg (1965 respektive "
                "1655 -- den ekonomiska är alltså den äldre). SAOL har båda i samma led. "
                "Ingen inledande enordsglosa.",
    },
    "märgfull": {
        "hb": "full av inre kraft och uttrycksfullhet",
        "syn": ["spännande"],
        "grp": None,
        "ex": f'Hennes romaner utmärktes av ett {B.format("märgfullt")} språk.',
        "reg": "litterär, positiv, allmän",
        "ety": None,
        "skal": "SAOL: 'äv. bildl. färgstark, spännande'. 'spännande' inleder ett eget "
                "led och är belagt; 'färgstark' stod först med men ströks, eftersom "
                "markören 'äv. bildl.' inte skalas bort och glosan därmed inte inleder "
                "sitt led. SO ger `märglös` som antonym och `kärnfull` som cohyponym.",
    },
    "nogräknad": {
        "hb": "som gör sig samvetsbetänkligheter ; som ställer höga krav",
        "syn": [],
        "grp": None,
        "ex": f'Mindre {B.format("nogräknade")} företag utnyttjade kryphålet direkt.',
        "reg": "neutral, neutral, allmän ; neutral, neutral, allmän",
        "ety": None,
        "skal": "SO ger två betydelser med skilda första belägg (1753 och 1740). SAOL:s "
                "'fordrande, krävande' belägger bara den andra, så listan lämnas tom i "
                "stället för platt. Den första betydelsen syns nästan alltid nekad -- "
                "'inte särskilt nogräknad'.",
    },
    "pittoresk": {
        "hb": "brokig och charmfullt oordnad, värd att avbilda",
        "syn": ["målerisk"],
        "grp": None,
        "ex": f'Ett {B.format("pittoreskt")} fiskeläge klättrade uppför bergssidan.',
        "reg": "neutral, positiv, allmän",
        "ety": "av franska pittoresque, av italienska pittoresco, till pittore 'målare'",
        "skal": "SAOL:s hela definition är 'målerisk'. SO: 'brokig och oordnad (och "
                "färgrik) på ett charmfullt sätt'. Etymologin förklarar glosan -- ordet "
                "betyder ordagrant 'som en målare skulle måla det'.",
    },
    "reminiscens": {
        "hb": "svag och ofullständig minnesbild ; stildrag från ett äldre verk som skymtar i ett yngre",
        "syn": [],
        "grp": None,
        "ex": f'Han hade bara suddiga {B.format("reminiscenser")} av gårdagens fest.',
        "reg": "formell, neutral, allmän ; fackspråklig, neutral, konst",
        "ety": "till latin reminisci 'erinra sig'",
        "skal": "SO ger båda betydelserna med skilda första belägg (1795 och 1820). "
                "SAOL:s 'erinring, svagt minne av ngt' belägger bara den första, så "
                "listan lämnas tom i stället för platt.",
    },
    "renegat": {
        "hb": "person som övergett den lära eller sida hen tidigare bekänt sig till",
        "syn": ["avfälling", "överlöpare"],
        "grp": None,
        "ex": f'Propagandan utmålade honom som en {B.format("renegat")} och förrädare.',
        "reg": "ngt ålderdomlig, nedsättande, politik",
        "ety": "av medeltidslatin renegatus, till renegare 'förneka'; jfr negera",
        "skal": "SAOL: 'avfälling, överlöpare' -- båda inleder var sitt led, och SAOL "
                "märker posten 'åld., nedsätt.'. SO märker den 'nedsättande; särsk. "
                "(förr) i kommunistisk polemik', vilket registret följer.",
    },
    "resolut": {
        "hb": "kraftfull och bestämd i sitt handlande",
        "syn": ["beslutsam", "rask"],
        "grp": None,
        "ex": f'Hon tog {B.format("resolut")} initiativet när de andra tvekade.',
        "reg": "neutral, positiv, allmän",
        "ety": "av franska résolu; av latin resolutus 'fri, otvungen'; till resolvera",
        "skal": "SAOL: 'beslutsam, rask' -- båda inleder var sitt led. SO: 'kraftfull "
                "och bestämd', med underbetydelsen 'äv. om handling eller dylikt', "
                "alltså samma betydelse överförd på handlingen.",
    },
    "taverna": {
        "hb": "enklare värdshus eller matservering, ofta i Sydeuropa",
        "syn": ["värdshus"],
        "grp": None,
        "ex": f'De åt på en liten {B.format("taverna")} vid hamnen.',
        "reg": "neutral, neutral, allmän",
        "ety": "fornsvenska tavärne; via lågtyska av latin taberna 'bod, härbärge, "
               "värdshus'; jfr tabernakel",
        "skal": "SAOL: 'italiensk restaurang, värdshus' -- 'värdshus' inleder ett eget "
                "led. SO: 'typ av värdshus', med underbetydelsen 'äv. om enklare "
                "matservering'. Ordet är belagt i svenskan sedan 1300-talet trots att "
                "det i dag känns som ett sydeuropeiskt lånord.",
    },
    "tillhandahålla": {
        "hb": "ställa något till någons förfogande",
        "syn": [],
        "grp": None,
        "ex": f'Skolan {B.format("tillhandahåller")} alla läromedel utan kostnad.',
        "reg": "formell, neutral, allmän",
        "ety": None,
        "skal": "SO och SAOL har ordagrant samma definition, 'ställa till (någons) "
                "förfogande'. Den inleder ledet men är identisk med huvudbetydelsen och "
                "alltså cirkulär som synonym.",
    },
    "tälja": {
        "hb": "forma trä genom att skära bort bit efter bit med kniv",
        "syn": [],
        "grp": None,
        "ex": f'Pojken satt på trappan och {B.format("täljde")} på en enbit.',
        "reg": "neutral, neutral, allmän",
        "ety": "fornsvenska tälghia; nordiskt ord",
        "skal": "SO: 'bearbeta genom att skära bort bit efter bit'. SAOL: 'skära med "
                "kniv' -- 'skära' inleder tekniskt ledet men är alldeles för brett som "
                "synonym (man skär även bröd). 'karva' står i jfr-fältet. Synonymlistan "
                "från synonymer.se är dessutom smittad av `förtälja` ('räkna upp, "
                "berätta'), ett annat ord.",
    },
    "överloppsgärning": {
        "hb": "handling som görs utöver det nödvändiga och därför är överflödig",
        "syn": [],
        "grp": None,
        "ex": f'Det var en {B.format("överloppsgärning")} att byta system så kort efter förra bytet.',
        "reg": "formell, neutral, allmän",
        "ety": "efter latin opera supererogationis, ursprungligen om det överskott av "
               "goda gärningar som uppstår när någon inte bara följer buden utan också "
               "råden om fattigdom och kyskhet",
        "skal": "SO och SAOL ger båda 'onödig handling' som hela definitionen -- "
                "identisk med huvudbetydelsen, alltså ingen brukbar synonym. Etymologin "
                "är ovanligt upplysande och förklarar `överlopps-`: det handlade "
                "ursprungligen om gärningar utöver plikten.",
    },
    "överrumpla": {
        "hb": "plötsligt och oväntat komma på någon så att denne tappar handlingsförmågan",
        "syn": ["överraska"],
        "grp": None,
        "ex": f'Inbrottstjuven {B.format("överrumplades")} i hallen av hemvändande ägare.',
        "reg": "neutral, neutral, allmän",
        "ety": "efter tyska überrumpeln; besläktat med rumla",
        "skal": "SAOL: 'oväntat överfalla; överraska' -- 'överraska' inleder ett eget "
                "led. SO:s andra betydelse, 'överraska på negativt sätt', är märkt 'äv. "
                "i fråga om själslig reaktion' och är samma betydelse överförd, inte en "
                "egen.",
    },
    "binge": {
        "hb": "avbalkning eller stor lår för torra varor ; stor och obestämd mängd",
        "syn": ["avbalkning", "lår", "hög", "hop"],
        "grp": [["avbalkning", "lår"], ["hög", "hop"]],
        "ex": f'Han hade en hel {B.format("binge")} med gamla tidningar på vinden.',
        "reg": "neutral, neutral, allmän ; neutral, neutral, allmän",
        "ety": "fornsvenska binge; av ovisst ursprung",
        "skal": "Båda betydelserna har belagd glosa, alltså grupperas de. SAOL: "
                "'avbalkning, lår; hög, hop' -- fyra led, två per betydelse, i samma "
                "ordning som SO listar dem.",
    },
    "fikonspråk": {
        "hb": "hemligt låtsasspråk ; svårbegripligt expertspråk",
        "syn": [],
        "grp": None,
        "ex": f'{B.format("Fikonspråket")} på kultursidorna gjorde artikeln nästan oläslig.',
        "reg": "neutral, neutral, lingvistik ; neutral, lätt negativ, allmän",
        "ety": None,
        "skal": "SO: 'ett hemligt språk' och 'svårbegripligt expertspråk', den senare "
                "märkt 'ofta bildligt'. SAOL: 'ett hemligt låtsasspråk; obegripligt "
                "fackspråk'. Ingen inledande enordsglosa i någon av dem.",
    },
    "strömning": {
        "hb": "rörelse hos en vätska eller gas ; spridd riktning i kultur- och samhällsliv",
        "syn": [],
        "grp": None,
        "ex": f'Nationalistiska {B.format("strömningar")} växte sig starkare under decenniet.',
        "reg": "fackspråklig, neutral, fysik ; neutral, neutral, allmän",
        "ety": None,
        "skal": "SO ger båda betydelserna med skilda första belägg (1822 och 1824). "
                "SAOL:s glosor för betydelse 1 -- 'strömmande; ström' -- innehåller "
                "uppslagsordets stam och röjer svaret; 'åsiktsriktning, kulturrörelse' "
                "belägger bara betydelse 2. Alltså tom lista.",
    },
    "vitsord": {
        "hb": "formellt utlåtande med en värderande bedömning av någon",
        "syn": ["omdöme", "intyg", "vittnesbörd"],
        "grp": None,
        "ex": f'Hon fick goda {B.format("vitsord")} för sitt sätt att sköta ordförandeskapet.',
        "reg": "formell, neutral, allmän",
        "ety": "fornsvenska vitsorþ 'bevisning; intyg'; eventuellt till vett i "
               "betydelsen 'kunskap' och ord",
        "skal": "SO:s andra led är 'betyg, omdöme' och SAOL:s 'vittnesbörd, intyg; "
                "betyg' -- glosorna inleder var sitt led. SAOB:s juridiska betydelse "
                "'beviskraft' tas INTE med: den saknas i både SO och SAOL, och "
                "källhierarkin låter de två avgöra dagens betydelser. SAOL:s "
                "finlandssvenska 'betyg i enskilt ämne' är märkt `finl.` och är en "
                "regional variant av samma betydelse, inte en egen.",
    },
    "ackreditera": {
        "hb": "ge någon fullmakt eller officiellt tillstånd att företräda eller bevaka",
        "syn": [],
        "grp": None,
        "ex": f'Evenemanget bevakades av över hundra {B.format("ackrediterade")} journalister.',
        "reg": "formell, neutral, politik",
        "ety": "av franska accréditer 'rekommendera, ackreditera'; jfr kredit",
        "skal": "SO: 'förse med fullmakt', med specialiseringen 'ge (diplomat) fullmakt "
                "att representera sitt land'. SAOL har bara diplomatbetydelsen. SO:s "
                "tredje rad, '(väl) ansedd', är märkt 'i perfekt particip äv.' och är "
                "en particip-användning, inte en egen betydelse. 'förse' inleder ledet "
                "men är för brett som synonym.",
    },
    "drägg": {
        "hb": "bottensats i en vätska ; nedsättande om samhällets sämsta skikt",
        "syn": ["bottensats", "slödder"],
        "grp": [["bottensats"], ["slödder"]],
        "ex": f'{B.format("Dräggen")} hade sjunkit till botten av tunnan.',
        "reg": "ngt ålderdomlig, neutral, allmän ; neutral, starkt nedsättande, allmän",
        "ety": "fornsvenska dräg 'jäsningsämne; bottensats'; nordiskt ord av "
               "omdiskuterat ursprung",
        "skal": "Båda betydelserna har belagd glosa -- SO ger 'bottensats' och 'slödder' "
                "som var sitt led -- alltså grupperas de. SO märker den konkreta "
                "betydelsen 'mindre brukligt', vilket registret följer; den bildliga är "
                "märkt 'äv. bildligt' och lever kvar.",
    },
    "evalvera": {
        "hb": "uppskatta värdet av något ; räkna om till annan valuta",
        "syn": ["uppskatta", "räkna om"],
        "grp": [["uppskatta"], ["räkna om"]],
        "ex": f'Beloppen {B.format("evalverades")} till dagens penningvärde.',
        "reg": "formell, neutral, ekonomi ; fackspråklig, neutral, ekonomi",
        "ety": None,
        "skal": "SO saknar ordet helt. SAOL: 'uppskatta värde; räkna om till annat mynt' "
                "-- två led, ett per betydelse, båda med inledande glosa, alltså "
                "grupperas de. Endast två källor (SAOL och SAOB).",
    },
    "favör": {
        "hb": "förmån eller fördel ; ynnestbevis ; gynnsamt resultat i en tävling",
        "syn": [],
        "grp": None,
        "ex": f'Matchen slutade 3–1 i svensk {B.format("favör")}.',
        "reg": "formell, positiv, allmän ; formell, positiv, allmän ; neutral, neutral, sport",
        "ety": "av franska faveur; av latin favor, till favere 'gynna'; jfr favorit",
        "skal": "SO ger fyra betydelser. Tre tas med; den fjärde -- den extra sticket i "
                "kortspel -- är märkt 'äv. (i kortspel)' och är en facktillämpning av "
                "'fördel'. Glosorna 'förmån' och 'ynnestbevis' belägger bara två av tre "
                "betydelser, så listan lämnas tom i stället för platt.",
    },
    "fissur": {
        "hb": "sprickformig skada i kroppsvävnad, till exempel i ben eller slemhinna",
        "syn": ["spricka"],
        "grp": None,
        "ex": f'Röntgen visade en {B.format("fissur")} i handlovsbenet.',
        "reg": "fackspråklig, neutral, medicin",
        "ety": "av latin fissura '(en) spricka, rämna'",
        "skal": "SAOL: 'spricka el. springa i ben' -- 'spricka' inleder ledet. SO: "
                "'sprickformig kroppsskada', med underbetydelsen att ordet även används "
                "om naturliga fåror i skelett och hjärna, vilket huvudbetydelsen fångar "
                "genom 'kroppsvävnad' snarare än 'skada på ben'.",
    },
    "fosforescent": {
        "hb": "som lyser i mörker en tid efter att ha belysts, utan att avge värme",
        "syn": [],
        "grp": None,
        "ex": f'Urtavlan var målad med ett {B.format("fosforescent")} skikt som lyste hela natten.',
        "reg": "fackspråklig, neutral, fysik",
        "ety": "till fosforescera",
        "skal": "SO: 'som kan fosforescera' -- cirkulärt, därför omskrivet efter "
                "Wiktionarys 'uppvisar ett sken i mörker utan att använda värme'. "
                "'självlysande' och 'fluorescerande' står i SO:s jfr-fält som "
                "cohyponymer, inte synonymer -- och fluorescens slocknar direkt när "
                "ljuset släcks, vilket fosforescens inte gör. Endast två källor: SAOL "
                "saknar ordet.",
    },
    "lämpa": {
        "hb": "hovsamhet och varsamhet ; förflytta eller stuva om tung last ; anpassa efter förhållandena",
        "syn": ["hovsamhet", "varsamhet", "förflytta", "anpassa"],
        "grp": [["hovsamhet", "varsamhet"], ["förflytta"], ["anpassa"]],
        "ex": f'Om det inte går med {B.format("lämpor")} får vi ta till tvång.',
        "reg": "formell, neutral, allmän ; neutral, neutral, sjöfart ; neutral, neutral, allmän",
        "ety": "fornsvenska lämpa; av lågtyska limpen 'vara passande, göra passande'; "
               "jfr förolämpa",
        "skal": "Alla tre betydelserna har belagd glosa i SAOL ('hovsamhet, varsamhet', "
                "'förflytta', 'anpassa'), alltså grupperas de. SO märker "
                "förflyttningsbetydelsen 'spec. sjöfart' i undergruppen om att stuva om "
                "och langa, vilket domänen följer.",
    },
    "regel / rigel": {
        "hb": "enklare låsanordning i form av en bom som skjuts för ; långsmalt stycke trävirke som används som stomme i väggar",
        "syn": [],
        "grp": None,
        "ex": f'Han sköt för {B.format("regeln")} innan han la sig.',
        "reg": "neutral, neutral, teknik ; fackspråklig, neutral, teknik",
        "ety": "av lågtyska regel 'tvärstång; reling; regel'; av omdiskuterat ursprung",
        "skal": "Framsidan ger två stavningar av samma ord. Uppslaget gjordes på "
                "`rigel`, eftersom `regel` domineras av det helt andra ordet "
                "'föreskrift, norm' (som har egen etymologi, latin regula 'rättesnöre'). "
                "SO under `rigel`: låsanordningen och trävirket, med skilda första "
                "belägg (1546 och 1585). Ingen inledande enordsglosa.",
    },
    "svärmisk": {
        "hb": "romantiskt drömmande och lätt överspänd",
        "syn": ["drömmande"],
        "grp": None,
        "ex": f'En {B.format("svärmisk")} yngling som skrev dikter till sin granne.',
        "reg": "litterär, neutral, allmän",
        "ety": None,
        "skal": "SAOL:s hela definition är 'drömmande'. SO: 'som hänger sig åt "
                "svärmeri' -- cirkulärt, därför omskrivet. Wiktionarys andra betydelse "
                "'exalterad, fanatisk' ligger inom SO:s 'svärmeri' och fångas av "
                "'överspänd' i huvudbetydelsen snarare än som egen rad.",
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
