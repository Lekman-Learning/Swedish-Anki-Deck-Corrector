# -*- coding: utf-8 -*-
"""Fyller proposed+sokkoll for de sista 30 korten i session_2026-08-29_v3-batch3.

Underlag: slaupp_batch3_29aug_del2.txt + riktade omhamtningar (hamtat 2026-08-29).

TRE KORT SKRIVS INTE:

1. `luxos` -- 🔴 FELSTAVAT UPPSLAGSORD. uppslagsordstraffar = [] i SAOL, SO OCH
   SAOB, och Wiktionary sager finns:false. Ordet existerar inte. Ratt form ar
   `luxuos`, som traffar ALLA TRE: SO "ytterst elegant och pakostad",
   SAOL "lyxig, praktfull", ex "en luxuos villa", av franska luxueux.
   Kortet lar alltsa ut en stavning som inte finns. Kraver Adams beslut:
   byta framsidan till `luxuos` eller ta bort kortet.

2. `endossat` -- bara SAOB som uppslagsord, och SAOB:s def-lista ar TOM.
   SO och SAOL: noll traffar. Enda innehallet ar Wiktionarys "den som vaxeln
   overlates pa". En kalla racker inte. Samma behandling som `in infinitum`
   2026-08-28 och `forborgad` 2026-08-18.

3. `vermillon` -- samma sak: bara SAOB-uppslag med tom def, plus Wiktionarys
   "cinnoberrod". Kontrollerade aven stavningen `vermiljon` -- ocksa noll
   traffar, sa det ar inte ett stavfel utan ett ord utan ordboksuppslag.

FEM MOTSATSORD i synonymer.se:s listor, alla uteslutna:
  angransande -> avlagsen, fjarran
  bracklig    -> hallbar, talig, robust
  gunstig     -> ovanlig, ofordelaktig
  magistral   -> odmjuk, timid, medioker
  bracklig    -> (aven) "Hanga pa en skor trad" -- fras, inte synonym

TVA HOMONYMFOROERENINGAR i uppslaget:
  `vite`  -- SO:s def-lista blandar in hela `vit`-artikeln ("farg som nyfallen
             sno", "mycket blek", "som varnar det bestaende samhallet"). Bara
             den forsta defen (rattslig pafoljd) hor till `vite`. Skild
             etymologi bekraftar: fornsvenska vite 'straff' mot runform huita.
  `limes` -- SO:s andra def ("en liten gulgron, sur citrusfrukt", ex "marinera
             i lime") ar artikeln for `lime`, med egen etymologi (engelska lime
             mot latin limes 'granslinje'). Bara gransvardet hor hit.
"""
import io, json

FIL = "sessions/session_2026-08-29_v3-batch3.json"
B = '<font color="#3498db">%s</font>'
K = {}

K["alligator"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO: 'typ av krokodilliknande kraldjur med bred, platt nos'. SAOL: 'ett krokodildjur'. En betydelse. "
                 "UTESLUTNA: 'krokodil', 'kajman', 'gavial', 'nilkrokodil' -- alla SLAKTINGAR, inte utbytbara ord. "
                 "En alligator ar inte en krokodil; nosformen ar just det som skiljer dem, och Wiktionary preciserar "
                 "att alligatorn bara finns i Amerika och Kina."),
    proposed=dict(huvudbetydelse="Krokodildjur med bred, trubbig nos, som bara lever i Amerika och Kina",
        register="neutral, zoologi", synonymer=[], synonym_groups=None,
        exempelmening="En %s har bredare nos än en krokodil, och tänderna syns inte när gapet är stängt." % (B % "alligator"),
        etymologi="→ Spanska el lagarto 'ödlan' — vägen gick via engelskan."))

K["angränsande"] = dict(
    sokkoll=dict(kalla="SO via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO: 'belagen narmast intill', aven bildligt ('bilbranschen och angransande branscher'). En betydelse "
                 "som tacker bade det rumsliga och det bildliga. UTESLUTNA ur synonymer.se: 'avlagsen' och 'fjarran' -- MOTSATSORD."),
    proposed=dict(huvudbetydelse="Som ligger alldeles bredvid, med en gemensam gräns",
        register="neutral", synonymer=["intilliggande", "närliggande"], synonym_groups=None,
        exempelmening="Branden spred sig till de %s fastigheterna innan brandkåren hann fram." % (B % "angränsande"),
        etymologi=None))

K["avtrubba"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO och SAOL har samma ordalydelse: 'minska kanslighet hos'. En betydelse. "
                 "SO:s tva exempel visar bade det kansliga ('folk blir avtrubbade av allt vald pa tv') och det omdomesmassiga "
                 "('hans omdome var avtrubbat av alkohol') -- samma betydelse, tva tillampningar."),
    proposed=dict(huvudbetydelse="Göra någon mindre känslig, så att sådant som förr gjorde intryck inte längre gör det",
        register="neutral", synonymer=["förslöa", "bedöva"], synonym_groups=None,
        exempelmening="Efter tjugo år i yrket var han %s och kunde äta lunch mitt i eländet." % (B % "avtrubbad"),
        etymologi=None))

K["belamra"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO: 'fylla (utrymme) med skrymmande eller hindrande foremal', aven bildligt om huvudet "
                 "('hans hjarna var belamrad med onyttiga kunskaper'). SAOL: 'ta upp mycket plats i'. En betydelse. "
                 "UTESLUTNA: 'belasta', 'betunga', 'nedtynga' -- de handlar om tyngd/borda, inte om att fylla ett utrymme."),
    proposed=dict(huvudbetydelse="Fylla ett utrymme med saker som tar plats och står i vägen",
        register="neutral", synonymer=["proppa full", "skrymma"], synonym_groups=None,
        exempelmening="Hallen var %s med kartonger, och man fick gå i sicksack för att komma till dörren." % (B % "belamrad"),
        etymologi=None))

K["blemma"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO: 'liten blasa i huden'. SAOL: 'liten blasa pa huden, kvissla'. En betydelse. "
                 "'kvissla' star i bade SAOL och Wiktionary och ar darmed belagd. UTESLUTEN: 'akne' (anvandarbidrag) -- "
                 "akne ar ett hudtillstand med manga blemmor, inte en enskild blemma."),
    proposed=dict(huvudbetydelse="Liten blåsa i huden, ofta röd och upphöjd",
        register="neutral", synonymer=["kvissla", "finne"], synonym_groups=None,
        exempelmening="Hon fick en %s på hakan kvällen innan fotograferingen." % (B % "blemma"),
        etymologi=None))

K["bräcklig"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO har TVA betydelser: 'foga hallfast' om foremal, och 'liten och klen' om levande varelse "
                 "(SO:s eget exempel: 'en bracklig, vitharig gammal dam', 'han har bracklig halsa'). SAOL: 'skor'. "
                 "UTESLUTNA ur synonymer.se: 'hallbar', 'talig', 'robust' -- alla MOTSATSORD. "
                 "Aven 'Hanga pa en skor trad' utesluts: en fras, inte ett utbytbart ord."),
    proposed=dict(huvudbetydelse="Som lätt går sönder om man tar i ; svag och klen i kroppen",
        register="neutral",
        synonymer=["skör", "spröd", "klen", "skröplig"],
        synonym_groups=[["skör", "spröd"], ["klen", "skröplig"]],
        exempelmening="Bryggan var så %s att de gick över en i taget." % (B % "bräcklig"),
        etymologi=None))

K["bärsärk"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO har TVA betydelser: (1) 'kampe som ar gripen av oemotstandligt raseri' -- SAOL preciserar "
                 "'i fornnordisk tid', (2) 'stark person som (ofta) rakar i raseri', markt 'numera forsvagat'. "
                 "SO:s exempel visar bada: veritabla barsarkar i ett fotbollslag, och uttrycket 'ga barsark'."),
    proposed=dict(huvudbetydelse="Nordisk forntidskrigare som gick in i blint raseri i strid ; person som lätt tappar besinningen och blir våldsam",
        register="neutral, historia ; neutral",
        synonymer=["rasande krigare", "vilde"],
        synonym_groups=[["rasande krigare"], ["vilde"]],
        exempelmening="En gäst gick %s i baren och slog sönder tre bord innan vakterna hann fram." % (B % "bärsärk"),
        etymologi="→ Isländska berserkr, troligen 'man klädd i björnskinn' — ber- 'björn' + serkr 'skjorta'."))

K["eutanasi"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO och SAOL sager bada bara 'dodshjalp'. Wiktionary preciserar: 'pa medicinsk vag malmedvetet orsaka "
                 "eller bidra till en patients dod, pa dennes, eller nara anhorigs begaran'. En betydelse. "
                 "'barmhartighetsmord' star som SO:s JFR och i synonymer.se, men bar ett vardeomdome ordet sjalvt inte har "
                 "-- behalls som synonym eftersom bada kallorna anger den, men ar inte neutral."),
    proposed=dict(huvudbetydelse="Att en läkare avsiktligt avslutar en patients liv, på patientens egen begäran",
        register="neutral, medicin", synonymer=["dödshjälp"], synonym_groups=None,
        exempelmening="Riksdagen debatterade %s utan att komma fram till något beslut." % (B % "eutanasi"),
        etymologi="→ Grekiska eu 'god' + thanatos 'död'."))

K["fosgen"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + Wiktionary (2026-08-29, HTTP 200). synonymer.se saknar uppslag.",
        slutsats="SO: 'en fargelos, giftig gas'. SAOL: 'en giftig gas'. Wiktionary lagger till det som gor ordet "
                 "igenkannbart: 'anvand som stridsgas under forsta varldskriget'. En betydelse. "
                 "Legacys synonym 'klorvate' ar sakligt FEL -- klorvate ar HCl, fosgen ar COCl2. Struken."),
    proposed=dict(huvudbetydelse="Färglös giftgas som användes som stridsmedel i första världskriget",
        register="fackspråklig, kemi", synonymer=[], synonym_groups=None,
        exempelmening="%s luktar svagt av hö, vilket gjorde den ännu farligare i skyttegravarna." % (B % "Fosgen"),
        etymologi="→ Grekiska phos 'ljus' + -genes 'som alstrar' — gasen bildas i solljus."))

K["förebrå"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se (2026-08-29, HTTP 200). Wiktionary gav HTTP 429.",
        slutsats="SO: 'direkt uttala missnoje med (nagon) for felaktigt handlande'. SAOL: 'klandra, kritisera'. En betydelse. "
                 "Nyckeln ar 'direkt' -- man forebrar nagon i ansiktet, till skillnad fran att kritisera i tredje person. "
                 "UTESLUTNA: 'anklaga', 'beskylla', 'tillvita' -- de pastar att nagon gjort nagot, forebra forutsatter att det redan ar klarlagt."),
    proposed=dict(huvudbetydelse="Säga rakt ut till någon att man är missnöjd med vad han gjort",
        register="neutral", synonymer=["klandra", "tillrättavisa"], synonym_groups=None,
        exempelmening="Hon %s sig själv i flera år för att hon inte ringt samma kväll." % (B % "förebrådde"),
        etymologi="→ Egentligen 'kasta något i ansiktet på någon', av fornsvenska bræghþa 'kasta'."))

K["förrätta"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se (2026-08-29, HTTP 200). Wiktionary gav HTTP 429.",
        slutsats="SO: 'formellt utfora'. SAOL: 'utfora, verkstalla'. En betydelse -- det som skiljer ordet fran vanligt "
                 "'utfora' ar att handlingen ar formell, en ceremoni eller ett tjansteuppdrag. SO markerar uttrycket "
                 "'forratta sina naturbehov' som 'ibland skamtsamt', alltsa en anvandningsnot, inte en egen betydelse "
                 "(samma slutsats som for `pur` 2026-08-28: rakna i strukturen, inte i sammandraget)."),
    proposed=dict(huvudbetydelse="Utföra en högtidlig handling eller ett uppdrag som hör till ens ämbete",
        register="formell", synonymer=["verkställa", "uträtta"], synonym_groups=None,
        exempelmening="Det var kyrkoherden som %s vigseln, trots att han egentligen var ledig." % (B % "förrättade"),
        etymologi=None))

K["gagn"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO: 'gynnsam verkan'. SAOL: 'nytta, fordel'. Wiktionary: 'nytta'. En betydelse, tre kallor overens. "
                 "UTESLUTEN: 'skada' ur synonymer.se -- MOTSATSORD. Aven 'profit' och 'mervarde' utesluts: de ar ekonomiska "
                 "och snavare an gagn, som galler all gynnsam verkan."),
    proposed=dict(huvudbetydelse="Den nytta något gör",
        register="något formell", synonymer=["nytta", "fördel"], synonym_groups=None,
        exempelmening="Han var chef mera till namnet än till %s — besluten fattades av någon annan." % (B % "gagnet"),
        etymologi=None))

K["gunstig"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO har TVA betydelser: (1) 'valvillig' om person -- markt 'nagot alderdomligt', (2) 'fordelaktig' om "
                 "omstandigheter ('ma vindar och vagor vara er gunstiga'). SO noterar aven ironisk anvandning om "
                 "hogfardig person ('gunstig herre'). SAOL: 'valvillig, gynnsam; nadig'. "
                 "UTESLUTNA ur synonymer.se: 'ovanlig' och 'ofordelaktig' -- MOTSATSORD."),
    proposed=dict(huvudbetydelse="Vänligt inställd till någon och beredd att hjälpa ; som ger goda förutsättningar",
        register="något ålderdomlig ; neutral",
        synonymer=["välvillig", "bevågen", "gynnsam", "läglig"],
        synonym_groups=[["välvillig", "bevågen"], ["gynnsam", "läglig"]],
        exempelmening="Vindarna var %s och de var framme två dygn tidigare än beräknat." % (B % "gunstiga"),
        etymologi=None))

K["infektiös"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO: 'smittsam', markt BRUK: medicin. SAOL: 'smittsam; uppkommen genom smitta; smittbarande'. "
                 "En betydelse. Registret ar det enda som skiljer ordet fran vardagliga 'smittsam' och maste sta pa kortet."),
    proposed=dict(huvudbetydelse="Som sprids genom smitta",
        register="fackspråklig, medicin", synonymer=["smittsam", "kontagiös"], synonym_groups=None,
        exempelmening="Avdelningen stängdes efter ett utbrott av %s tarmsjukdom." % (B % "infektiös"),
        etymologi=None))

K["inkunabel"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO: 'bok som ar tryckt under boktryckarkonstens forsta stadium i Europa'. SAOL ger den exakta gransen: "
                 "'bok tryckt fore 1501 el. i Sverige 1525, vaggtryck'. Wiktionary: 'skrift tryckt fore 1501'. "
                 "Argranskan ar sjalva definitionen och maste med. 'paleotyp' ar enda synonymen i synonymer.se och ar "
                 "belagd som fackterm."),
    proposed=dict(huvudbetydelse="Bok tryckt före år 1501, alltså under tryckkonstens första femtio år",
        register="fackspråklig, bokhistoria", synonymer=["vaggtryck"], synonym_groups=None,
        exempelmening="Biblioteket har fjorton %s, alla inlåsta i ett klimatstyrt rum." % (B % "inkunabler"),
        etymologi="→ Latin incunabula 'linda, barndom' — böckerna från tryckkonstens spädbarnstid."))

K["kolli"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO har TVA betydelser: 'ett stycke frakt- eller resgods' och 'stort paket' (markt 'av. allmannare'). "
                 "SAOL slar ihop dem: 'stycke frakt- el. resgods, paket'. Skrivs som en betydelse, eftersom SO:s andra ar "
                 "en generalisering av den forsta, inte en skild betydelse. SO:s bildliga anvandning om svart skadad manniska "
                 "('bli liggande som ett kolli pa langvarden') ar en anvandningsnot, inte en egen betydelse. "
                 "UTESLUTEN: 'hankatt' ur Wiktionary -- ett helt annat ord."),
    proposed=dict(huvudbetydelse="Ett enskilt packat stycke gods, räknat som en enhet när något fraktas",
        register="fackspråklig, transport", synonymer=["fraktgods", "packe"], synonym_groups=None,
        exempelmening="Priset är trettio kronor per %s, oavsett vad som ligger i lådan." % (B % "kolli"),
        etymologi="→ Italienska collo 'paket', egentligen 'halsbörda' — det man bar på nacken."))

K["konkubin"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO: 'alskarinna (ofta till gift man) med erkand stallning', ursprungligen om en losare form av aktenskap. "
                 "Markt BRUK: 'nagot alderdomligt'. SAOL: 'alskarinna; bihustru'. En betydelse. "
                 "Nyckeln som skiljer ordet fran 'alskarinna' ar den ERKANDA stallningen -- forhallandet var offentligt, inte hemligt."),
    proposed=dict(huvudbetydelse="Kvinna som levde med en gift man i ett känt och accepterat förhållande vid sidan av äktenskapet",
        register="ålderdomlig", synonymer=["bihustru", "frilla"], synonym_groups=None,
        exempelmening="Kungen hade fyra barn med sin %s, och alla erkändes officiellt." % (B % "konkubin"),
        etymologi="→ Latin concubina, av con- 'tillsammans' + cubare 'ligga'."))

K["limes"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + Wiktionary (2026-08-29, HTTP 200). synonymer.se saknar uppslag.",
        slutsats="🔴 HOMONYMFOROERENING i uppslaget: SO:s def-lista innehaller aven 'en liten gulgron, sur citrusfrukt' "
                 "med exemplet 'marinera i lime' -- det ar artikeln for `lime`, inte `limes`. Etymologierna bevisar det: "
                 "'av latin limes granslinje' mot 'av engelska lime'. Bara gransvardet hor till uppslagsordet. "
                 "Wiktionary anger dessutom 'forsvarssystem vid Romarrikets granser' -- historiskt korrekt, men EN kalla "
                 "racker inte, sa den betydelsen skrivs inte. Ingen synonym i nagon kalla."),
    proposed=dict(huvudbetydelse="Det värde en matematisk funktion närmar sig utan att nödvändigtvis nå fram",
        register="fackspråklig, matematik", synonymer=[], synonym_groups=None,
        exempelmening="%s för 1/x när x växer mot oändligheten är noll." % (B % "Limes"),
        etymologi="→ Latin limes 'gränslinje' — värdet fungerar som en gräns kurvan aldrig passerar."))

K["magistral"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO har TVA betydelser: (1) 'som framtrader med eller pragas av stor myndighet' -- SAOL preciserar "
                 "'overlagset undervisande, mastrande', (2) 'som imponerar genom sitt yttre' (SO:s exempel: 'en magistral "
                 "barockkyrka'). UTESLUTNA ur synonymer.se: 'odmjuk', 'timid', 'medioker' -- alla MOTSATSORD."),
    proposed=dict(huvudbetydelse="Som talar uppifrån och ner, som en lärare till ett barn ; så storslagen till det yttre att man blir imponerad",
        register="neutral",
        synonymer=["mästrande", "docerande", "imponerande", "storslagen"],
        synonym_groups=[["mästrande", "docerande"], ["imponerande", "storslagen"]],
        exempelmening="Statsministerns %s tillrättavisning av journalisterna gjorde saken värre." % (B % "magistrala"),
        etymologi="→ Latin magistralis 'som hör till en lärare', av magister."))

K["okynnig"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO: 'som staller till besvar i onodan', ofta med POSITIV bibetydelse ('ett okynnigt skratt', "
                 "'en okynnig vindil'). SAOL: 'som hittar pa ganska oskyldiga spratt'. En betydelse. "
                 "🔴 Den positiva bitonen ar avgorande och maste sta pa kortet -- UTESLUTNA: 'ohorsam' och 'olydig' ur "
                 "synonymer.se, som bada ar rent negativa och missar hela poangen med ordet."),
    proposed=dict(huvudbetydelse="Som hittar på små ofog utan elak avsikt, mer på skoj än för att skada",
        register="neutral", synonymer=["busig", "odygdig"], synonym_groups=None,
        exempelmening="Pojkarna var uppsluppna och %s sista kvällen på lägret." % (B % "okynniga"),
        etymologi=None))

K["penetrera"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se (2026-08-29, HTTP 200). Wiktionary gav HTTP 429.",
        slutsats="SO har TVA betydelser: (1) '(gradvis) tranga igenom eller in i' konkret, (2) 'gora sig grundligt bekant "
                 "med och behandla (intellektuellt)', vanligen bildligt. SAOL bekraftar bada. "
                 "Belaggsaren visar att den INTELLEKTUELLA betydelsen ar aldst (1656 mot 1734) -- vart att veta, eftersom "
                 "den konkreta kanns som grundbetydelsen idag."),
    proposed=dict(huvudbetydelse="Tränga in i eller igenom något ; sätta sig in i en fråga så grundligt att inget återstår att förstå",
        register="neutral",
        synonymer=["genomtränga", "undersöka"],
        synonym_groups=[["genomtränga"], ["undersöka"]],
        exempelmening="Arbetsgruppen ska %s frågan och komma tillbaka med ett förslag i höst." % (B % "penetrera"),
        etymologi=None))

K["proposition"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se (2026-08-29, HTTP 200). Wiktionary gav HTTP 429.",
        slutsats="SO: 'forslag om beslut fran regering till riksdag'. SAOL: 'forslag fran regering till riksdag; forslag "
                 "till beslut'. SO:s 'av. om liknande forslag till annan beslutande grupp' star i SO+, alltsa en "
                 "anvandningsnot -- men den ar sa vanlig i motessammanhang ('Kan vi stalla proposition?') att den skrivs som "
                 "andra betydelse. UTESLUTEN: 'motion' -- MOTSATSEN i riksdagssammanhang: en proposition kommer fran "
                 "regeringen, en motion fran en ledamot. Att synonymer.se listar den ar direkt vilseledande."),
    proposed=dict(huvudbetydelse="Förslag som regeringen lägger fram för riksdagen att rösta om ; den fråga en mötesordförande ställer för att få fram ett beslut",
        register="fackspråklig, politik ; fackspråklig, mötesteknik",
        synonymer=["regeringsförslag", "—"],
        synonym_groups=[["regeringsförslag"], ["—"]],
        exempelmening="Regeringens %s om högre bensinskatt röstades ner med fyra rösters marginal." % (B % "proposition"),
        etymologi=None))

K["ritsa"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO: 'gora (tunn skara) med spetsigt verktyg'. SAOL: 'gora repor, repa, rista'. "
                 "Wiktionary: 'gora repa eller skara med verktyg'. En betydelse, tre kallor overens. "
                 "VERKTYGET ar det som skiljer ordet fran 'repa' -- man ritsar avsiktligt med nagot spetsigt."),
    proposed=dict(huvudbetydelse="Dra ett tunt streck i ett material med något vasst, för att märka ut var det ska brytas eller sågas",
        register="neutral, hantverk", synonymer=["rista", "rispa"], synonym_groups=None,
        exempelmening="Han %s glaset med diamanten och knäckte det sedan över bordskanten." % (B % "ritsade"),
        etymologi=None))

K["slagfärdig"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="SO: 'som snabbt hittar effektiva (och drapande) svar'. SAOL: 'snabb i repliken'. "
                 "Wiktionary: 'snabb i genmale'. En betydelse. SNABBHETEN ar karnan -- 'fyndig' ensamt racker inte, "
                 "det kan man vara i efterhand. UTESLUTNA: 'vitsig', 'klatschig' -- de beskriver skamtet, inte formagan att svara."),
    proposed=dict(huvudbetydelse="Som direkt hittar ett träffande svar, utan att behöva tänka efter",
        register="neutral", synonymer=["repliksnabb", "munvig"], synonym_groups=None,
        exempelmening="Hon var för %s för honom och vann varje diskussion på tio sekunder." % (B % "slagfärdig"),
        etymologi=None))

K["stick i stäv"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="⚠️ Uppslaget ar delvis fororenat av artikeln for `spar` (JFR: sparstampel, fotspar, hjulspar). "
                 "Men uttrycket sjalvt ar belagt i alla tre kallorna: SO 'rakt emot | tvart emot' med exemplet "
                 "'vinden stick i stav, det var bara att satta igang att kryssa', etymologi 'av lagtyska stik'. "
                 "synonymer.se: tvartemot, tvarsemot. Wiktionary: 'rakt emot t.ex. vinden... vilka alltsa kommer rakt mot staven'. "
                 "Alltsa INTE samma fall som `in suspenso` -- har finns uttrycket pa riktigt."),
    proposed=dict(huvudbetydelse="Rakt emot, i motsatt riktning mot vad som var meningen",
        register="neutral", synonymer=["tvärtemot", "tvärsemot"], synonym_groups=None,
        exempelmening="Utvecklingen går %s med målet att minska utsläppen." % (B % "stick i stäv"),
        etymologi="→ Stäven är fartygets framdel; vinden kommer rakt mot den och man måste kryssa."))

K["triage"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + Wiktionary (2026-08-29, HTTP 200). synonymer.se saknar uppslag.",
        slutsats="SO: 'process inom varden for att bedoma och prioritera patienter'. SAOL: 'process for att sortera och "
                 "prioritera patienter'. Wiktionary preciserar underlaget: anamnes, symtom och vitalparametrar. "
                 "En betydelse, tre kallor overens. Belagt forst sedan 2000 -- ett ungt lanord i svenskan. Ingen synonym anges."),
    proposed=dict(huvudbetydelse="Att snabbt bedöma vilka patienter som måste tas om hand först när alla inte kan hjälpas samtidigt",
        register="fackspråklig, sjukvård", synonymer=[], synonym_groups=None,
        exempelmening="Efter olyckan gjorde sjuksköterskan %s direkt på parkeringen och märkte de svårast skadade med rött." % (B % "triage"),
        etymologi="→ Franska trier 'sortera' — samma ord som i sortering av kaffebönor."))

K["vite"] = dict(
    sokkoll=dict(kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (2026-08-29, HTTP 200)",
        slutsats="🔴 HOMONYMFOROERENING: SO:s def-lista har fyra poster, men tre av dem ('som har farg som nyfallen sno', "
                 "'mycket blek', 'som varnar det bestaende samhallet') tillhor adjektivet `vit`, inte substantivet `vite`. "
                 "Etymologierna skiljer dem at: fornsvenska vite 'straff; boter' mot runform huita. "
                 "Bara den forsta defen skrivs: 'rattslig pafoljd for person som bryter mot en bestammelse eller inte "
                 "fullgor viss forpliktelse'. SAOL bekraftar: 'pafoljd for lagovertradelse i form av boter'. "
                 "SKILLNADEN MOT BOTER som maste med: ett vite bestams i FORVAG som ett hot, for att tvinga fram lydnad."),
    proposed=dict(huvudbetydelse="Penningstraff som bestäms i förväg och som man tvingas betala om man inte gör som myndigheten sagt",
        register="fackspråklig, juridik", synonymer=["bötesstraff"], synonym_groups=None,
        exempelmening="Företaget blev vid %s ålagt att minska utsläppen före årsskiftet." % (B % "vite"),
        etymologi=None))

PAUSA = {
    "endossat": ("v3_pausad::inget_uppslagsord_i_so_saol",
        "Bara SAOB har `endossat` som uppslagsord, och SAOB:s def-lista ar TOM. SO och SAOL: noll traffar. "
        "Enda innehallet ar Wiktionarys 'den som vaxeln overlates pa'. EN kalla racker inte. "
        "Samma behandling som `in infinitum` 2026-08-28 och `forborgad` 2026-08-18."),
    "vermillon": ("v3_pausad::inget_uppslagsord_i_so_saol",
        "Bara SAOB-uppslag med tom def, plus Wiktionarys 'cinnoberrod'. Kontrollerade aven stavningen "
        "`vermiljon` -- ocksa noll traffar i alla kallor. Det ar alltsa inte ett stavfel utan ett ord "
        "utan brukbart ordboksuppslag."),
    "luxös": ("v3_pausad::felstavat_uppslagsord",
        "🔴 ORDET FINNS INTE. uppslagsordstraffar = [] i SAOL, SO OCH SAOB, och Wiktionary sager finns:false. "
        "Ratt form ar `luxuos`, som traffar alla tre: SO 'ytterst elegant och pakostad', SAOL 'lyxig, praktfull', "
        "exempel 'en luxuos villa', av franska luxueux. Kortet lar ut en stavning som inte existerar. "
        "KRAVER ADAMS BESLUT: byta framsidan till `luxuos`, eller ta bort kortet."),
}


def main():
    d = json.load(io.open(FIL, encoding="utf-8"))
    s = p = 0
    for k in d:
        o = k["ord"]
        if o in PAUSA and not k.get("pausad"):
            tag, skal = PAUSA[o]
            k["pausad"] = tag
            k["sokkoll"] = dict(kalla="svenska.se msearch + synonymer.se + Wiktionary 2026-08-29", slutsats=skal)
            k["approved"] = False
            p += 1
        elif o in K:
            k["sokkoll"] = K[o]["sokkoll"]
            k["proposed"] = K[o]["proposed"]
            k["approved"] = True
            s += 1
    json.dump(d, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("skrivna denna omgang :", s)
    print("pausade denna omgang :", p)
    print("TOTALT skrivna       :", sum(1 for k in d if k.get("proposed")))
    print("TOTALT pausade       :", sum(1 for k in d if k.get("pausad")))
    print("kvar orörda          :", sum(1 for k in d if not k.get("proposed") and not k.get("pausad")))


if __name__ == "__main__":
    main()
