# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch2, kort 26-50. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch2.json"
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


satt("antecedentia",
     "En persons tidigare liv och vad hen gjort dessförinnan",
     "formell, neutral",
     [],
     "De jämförde sina " + B % "antecedentia" + " och kom fram till att de "
     "omöjligt kunde ha träffats förut.",
     "→ Latin antecedere 'gå före' — det som gick före i livet.",
     "SO: 'en persons forflutna'. SAOL: 'ngns foregaende liv'. Ordet star "
     "alltid i plural. Etymologin ar med eftersom ordet annars ar helt "
     "ogenomskinligt for den som inte kan latin -- 'ante' (fore) plus "
     "'cedere' (ga) gor det sjalvforklarande. Inga synonymer belagda.")

satt("astenisk",
     "Kraftlös och svag ; om kroppsbyggnad: smal och spenslig",
     "ålderdomlig, neutral ; fackspråklig, neutral, medicin",
     ["kraftlös"],
     "Han beskrevs som blek och " + B % "astenisk" + " efter månaderna på "
     "sjukhuset.",
     None,
     "SO: 'som kannetecknas av sjalslig kraftloshet' samt -- markt 'forr "
     "av.' -- 'som har spenslig kroppsbyggnad'. SAOL: 'kraftlos', bruk "
     "'ald.'. 'kraftlos' star i SAOL:s definitionstext och ar darmed "
     "belagd synonym. Bada betydelserna behalls; kroppsbyggnadsbetydelsen "
     "lever kvar i medicinskt sprak aven om SO markt den som aldre.")

satt("baldakin",
     "Tak av tyg som hänger över en säng, tron eller predikstol",
     "neutral, neutral",
     ["takhimmel", "sänghimmel"],
     "Sängen stod under en tung " + B % "baldakin" + " av rött sammet.",
     "→ Efter Baldac, medeltidens namn på Bagdad, varifrån sidentyget kom.",
     "SO: 'ett slags prydnadsdetalj med skenbar funktion av tak'. SAOL: "
     "'takhimmel'. JFR i SO: 'pall', 'sanghimmel', 'takhimmel', "
     "'tronhimmel'. 'takhimmel' och 'sanghimmel' behalls som synonymer "
     "(bada belagda); 'pall' ar struket eftersom det ordet framst betyder "
     "nagot annat i modern svenska. Etymologin ar med for att den ar "
     "minnesvard och forklarar det ovanliga ordet.")

satt("basa",
     "Vara den som bestämmer och leder arbetet ; mjuka upp trä genom att "
     "hetta upp det",
     "vardaglig, neutral ; fackspråklig, neutral, hantverk",
     [],
     "Hon " + B % "basar" + " för ett gäng på hundrafemtio man.",
     None,
     "SO ger tre betydelser: 'utova formanskap', 'rusa (ivag) "
     "okontrollerat' och 'mjuka upp genom upphettning'. Den forsta och "
     "tredje behalls -- de ar de belagda i bade SO och SAOL. "
     "Rusa-betydelsen ('basa ivag') ar utelamnad som mest dialektal. De ar "
     "olika ord i ursprung: formanskapsbetydelsen till 'bas' (chef), "
     "upphettningen till fornsvenska basa 'varma'.")

satt("bebådelse",
     "Budskap om att något ska komma ; särskilt om ängelns besked till Maria "
     "att hon ska föda Jesus",
     "högtidlig, neutral, religion",
     [],
     "Kyrkan firar Jungfru Marie " + B % "bebådelse" + " i slutet av mars.",
     None,
     "SO: 'forutsagelse om Jesu fodelse', bruk 'ngt ald.', med exemplen "
     "'den heliga bebadelsen; Jungfru Marie bebadelse'. Wiktionary ger den "
     "vidare betydelsen 'forebud om nagot'. Bada tas med -- den allmanna "
     "forst, den religiosa som den specifika anvandningen, eftersom SO:s "
     "definition ar snavare an ordets faktiska bruk. Inga synonymer "
     "belagda.")

satt("bettlare",
     "Person som tigger",
     "ålderdomlig, neutral",
     ["tiggare"],
     "Utanför kyrkporten satt en " + B % "bettlare" + " med mössan i "
     "handen.",
     None,
     "SO: 'person som agnar sig at (vanemassigt) tiggande', bruk 'mest i "
     "juridiska sammanhang; nagot alderdomligt'. Wiktionary: 'tiggare' -- "
     "belagd synonym. Ordet ar i praktiken utdott utanfor historiska och "
     "juridiska texter (belagt sedan 1536). Definitionen ar hallen sa kort "
     "som mojligt eftersom ordet ar ett rakt synonympar till ett vanligt "
     "ord.")

satt("bidé",
     "Låg tvättskål som man tvättar underlivet i",
     "neutral, neutral",
     [],
     "Badrummet i hotellet hade både badkar och " + B % "bidé" + ".",
     "→ Franska bidet 'liten häst' — man sitter grensle över den.",
     "SO: 'lagt tvattstall for tvattning av underlivet'. SAOL ordagrant "
     "samma. Etymologin ar medtagen eftersom den ar minnesvard och "
     "forklarar formen: man sitter over den som pa en hast. 'Tvattstall' "
     "ar bytt mot 'tvattskal' i definitionen -- tvattstall ar ett ovanligt "
     "ord som skulle forklara svart med svart.")

satt("bronkit",
     "Inflammation i luftrören",
     "fackspråklig, neutral, medicin",
     ["luftrörskatarr"],
     "Rökningen hade gett honom kronisk " + B % "bronkit" + ".",
     None,
     "SO: 'luftrorskatarr'. SAOL identisk. 'luftrorskatarr' ar darmed "
     "belagd synonym, men duger INTE som huvudbetydelse -- katarr ar ett "
     "lika ovanligt ord som bronkit och skulle forklara svart med svart. "
     "Definitionen sager darfor 'inflammation i luftroren', vilket ar vad "
     "bade katarr och -it betyder. Andelsen -it anvands genomgaende om "
     "inflammationer.")

satt("bylte",
     "Stort klumpigt knyte av saker som buntats ihop",
     "neutral, neutral",
     ["knyte"],
     "Ur " + B % "byltet" + " stack ett litet babyansikte fram.",
     None,
     "SO: 'storre, oformligt paket'. SAOL: 'knyte, hopbuntad packe' -- "
     "'knyte' darmed belagd i definitionstexten. JFR i SO: 'bylta ihop', "
     "'knyte', 'packe'. 'packe' ar struket som synonym: en packe ar "
     "ordnad och staplad, ett bylte ar det uttryckligen inte "
     "('oformligt'). Den skillnaden ar hela ordets poang.")

satt("bålverk",
     "Kraftigt hinder byggt till försvar ; bildligt: ett starkt skydd mot "
     "något",
     "neutral, neutral, historisk ; neutral, positiv",
     [],
     "FN beskrevs som ett " + B % "bålverk" + " mot ett nytt storkrig.",
     "→ Lågtyska bolwerk, till bole 'planka' — samma ord som boulevard.",
     "SO: 'typ av avsparrning som fungerar som forsvarsverk' samt 'starkt "
     "forsvar', markt 'ofta bildligt'. SAOL: 'forskansning; bildl. varn, "
     "skydd'. Den bildliga betydelsen ar i dag den vanligaste och far "
     "exempelmeningen. JFR i SO: 'barrikad', 'palissad', 'vall' -- alla "
     "strukna, de ar naraliggande men inte utbytbara. Etymologin ar med "
     "eftersom slaktskapen med boulevard ar ovantad och minnesvard.")

satt("deformation",
     "Att formen ändras till det sämre",
     "neutral, neutral",
     [],
     "Plåten hade fått en tydlig " + B % "deformation" + " efter smällen.",
     None,
     "SO: 'ooonskad andring av den ursprungliga formen', med 'av. "
     "bildligt'. SAOL: 'forandrad, ofta forsamrad form'. Definitionen "
     "haller sig till det konkreta eftersom det ar den vanliga "
     "anvandningen; den bildliga ('kanslomassig deformation') ar sallsynt "
     "och skulle gora huvudbetydelsen otydligare. Inga synonymer belagda "
     "i SO/SAOL:s definitionstext.")

satt("diametral",
     "Rakt motsatt i varenda del",
     "neutral, neutral",
     [],
     "De två utredningarna kom till " + B % "diametralt" + " motsatta "
     "slutsatser.",
     "→ Till diameter — de ligger på var sin ände av samma linje.",
     "SO: 'i alla avseenden motsatt', med exemplen 'systern var hennes "
     "diametrala motsats; diametralt motsatta standpunkter'. INGEN traff i "
     "SAOL:s definitionstext utover uppslagsordet. Ordet anvands nastan "
     "alltid som adverb ihop med 'motsatt' -- det speglas i "
     "exempelmeningen. Etymologin gor bilden konkret: tva punkter sa langt "
     "isar som en cirkel tillater.")

satt("diskrepans",
     "Skillnad mellan två saker som borde stämma överens",
     "formell, neutral",
     [],
     "Det fanns en " + B % "diskrepans" + " mellan vad han sa och vad han "
     "gjorde.",
     None,
     "SO: 'storande brist pa overensstammelse'. SAOL: 'brist pa "
     "overensstammelse, avvikelse'. JFR i SO: 'diskordans', "
     "'disproportion' -- bada strukna, de ar ovanligare an diskrepans och "
     "bryter regeln att inte forklara svart med svart. Definitionen fangar "
     "att det inte ar vilken skillnad som helst: det ligger en forvantan om "
     "overensstammelse i ordet.")

satt("ektomi",
     "Operation där ett organ helt eller delvis tas bort",
     "fackspråklig, neutral, medicin",
     [],
     "Ändelsen " + B % "ektomi" + " visar att något har opererats bort.",
     "→ Grekiska ektome 'utskärning'.",
     "SO: 'operativt ingrepp varvid ett organ helt eller delvis "
     "avlagsnas'. SAOL ordagrant samma. INGEN traff i SAOB eller "
     "Wiktionary -- belagt via SO och SAOL (sedan 1930). Ordet forekommer "
     "i praktiken nastan bara som efterled (hysterektomi, appendektomi), "
     "vilket exempelmeningen speglar i stallet for att konstruera en "
     "onaturlig mening med ordet ensamt.")

satt("enahanda",
     "Tråkigt likadant gång på gång, utan omväxling",
     "formell, negativ",
     ["enformig"],
     "Dagarna vid det löpande bandet var grå och " + B % "enahanda" + ".",
     None,
     "SO: 'helt igenom likadan' samt 'trottande eller trakigt lika', markt "
     "'ofta med negativ bibetydelse'. SAOL: 'trottande enformig' -- "
     "'enformig' darmed belagd i definitionstexten. JFR i SO: 'enhetlig', "
     "'likartad', 'oforandrad', 'stereotyp' -- alla strukna, de saknar "
     "enahandas negativa laddning, som ar sjalva poangen med ordet.")

satt("erinring",
     "Påminnelse om något ; mild tillsägelse",
     "formell, neutral ; formell, neutral, juridik",
     ["erinran"],
     "Han fick en " + B % "erinring" + " av chefen men slapp varning.",
     None,
     "SO: 'erinran', med hanvisning till bada betydelserna av erinran. "
     "SAOL: 'erinran'. Ordet ar en sidoform till erinran och delar dess "
     "tva betydelser: minnesbild respektive formell tillsagelse. Den "
     "juridiska/arbetsrattsliga betydelsen ar den som gor ordet vart att "
     "kunna -- en erinring ar mildare an en varning, vilket "
     "exempelmeningen visar.")

satt("espri",
     "Snabb och lekfull kvickhet i tanke och tal",
     "formell, positiv",
     [],
     "Hennes tal sprudlade av " + B % "espri" + " och fick hela salen att "
     "skratta.",
     "→ Franska esprit 'ande, kvickhet' — samma ord som i sprit.",
     "SO: 'kvicktankthet och spiritualitet'. SAOL: 'rorlig intelligens; "
     "kvickhet'. JFR i SO: 'spiritualitet' -- struket som synonym, det ar "
     "ovanligare an espri sjalvt. Wiktionarys andra betydelse ('knippe "
     "fina fjadrar pa damhattar') ar utelamnad som helt utdod. Etymologin "
     "ar med for slaktskapen med sprit, som ar oantad.")

satt("farin",
     "Gulbrunt råsocker",
     "neutral, neutral",
     [],
     "Receptet krävde både strösocker och " + B % "farin" + ".",
     "→ Franska farine, latin farina 'mjöl'.",
     "SO: 'rasocker med gulbrun farg'. SAOL: 'gulbrunt rasocker'. "
     "Wiktionary-hamtningen gav forst HTTP 429 och kordes om (HTTP 200). "
     "Definitionen ar hallen kort -- ordet ar konkret och behover ingen "
     "omskrivning. Etymologin ar med eftersom kopplingen till mjol "
     "forklarar det annars omotiverade namnet pa ett socker.")

satt("fägnas",
     "Bli glad åt något",
     "högtidlig, positiv",
     ["glädjas"],
     "Det " + B % "fägnar" + " mig att höra att ni har det bra.",
     None,
     "SO: 'gladja', bruk 'nagot hogtidligt'. SAOL: 'bli glad' samt "
     "'gladja, behaga'. INGEN traff i Wiktionary -- belagt via SO och SAOL "
     "(sedan forra halften av 1400-talet). Ordet anvands nastan bara i "
     "formen 'det fagnar mig', vilket exempelmeningen foljer. Slakt med "
     "'fager' och 'foga'.")

satt("fästa avseende vid",
     "Bry sig om något och låta det spela roll",
     "formell, neutral",
     [],
     "Domstolen " + B % "fäste inget avseende vid" + " hans tidigare "
     "löften.",
     None,
     "VARNING om kallan: svenska.se-traffen pa hela frasen var FORORENAD "
     "-- fritextsokningen matchade uttrycket inuti andra artiklar (bry sig "
     "om, ignorera) och returnerade deras definitioner, inte fraseens. "
     "Slog darfor upp grundordet 'avseende' separat (samma datum, HTTP "
     "200, traffar i saol och so). SAOL ger uttrycket direkt: 'tillskriva "
     "betydelse'. Definitionen bygger pa det, inte pa den fororenade "
     "traffen. Uttrycket anvands oftast NEKANDE ('faste inget avseende "
     "vid'), vilket exempelmeningen speglar.",
     extra=("https://svenska.se/api/msearch?ord=avseende",))

satt("gluten",
     "Protein i vete, råg och korn som gör degen seg",
     "neutral, neutral",
     [],
     "Hon undvek bröd eftersom hon inte tålde " + B % "gluten" + ".",
     "→ Latin gluten 'lim, klister' — samma rot som i agglutinera.",
     "SO: 'typ av protein som forekommer i de vanliga sadesslagen'. SAOL: "
     "'ett protein som kan forekomma i vete, rag, korn och havre'. "
     "Definitionen namner de tre sadesslag som faktiskt innehaller gluten "
     "-- havre ar med i SAOL:s lista men ar naturligt glutenfritt och "
     "kontamineras vanligen i hanteringen, sa det utelamnas hellre an "
     "skrivs fel. Etymologin forklarar varfor degen blir seg.")

satt("greve",
     "Man med hög adlig titel, under hertig men över friherre",
     "neutral, neutral, historisk",
     [],
     "Godset hade gått i arv inom samma " + B % "greve" + "familj i tre "
     "sekler.",
     None,
     "SO: '(titel for) manlig medlem av hogsta adelsgruppen', bruk 'mest "
     "vid beskrivning av aldre forhallanden'. SAOL: 'hogadlig man'. SO ger "
     "aven betydelsen 'en rundpipig, svensk ost' (belagd sedan 1964) -- "
     "utelamnad, den ar ett varumarkesnamn bildat till titeln, inte en "
     "sjalvstandig betydelse att kunna. Rangordningen i definitionen gor "
     "titeln placerbar i stallet for bara 'hog'.")

satt("grums",
     "Smuts och små partiklar som lagt sig i en vätska",
     "neutral, neutral",
     ["bottensats"],
     "Det blev en massa " + B % "grums" + " i vattnet när de bytte rör.",
     None,
     "SO: 'fallning av (ooonskade) smapartiklar'. SAOL: 'slam i vatska; "
     "bottensats' samt en andra, vardaglig betydelse 'missnojt mummel, "
     "muttrande'. JFR i SO: 'bottensats', 'dragg', 'slam'. 'bottensats' "
     "behalls som belagd synonym; 'dragg' ar struket som ovanligare. Den "
     "vardagliga mummel-betydelsen ar utelamnad -- den ar sallsynt och "
     "skulle gora kortet otydligt.")

satt("gumse",
     "Hanne av får",
     "neutral, neutral",
     ["bagge"],
     "En stor " + B % "gumse" + " med krokiga horn vaktade flocken.",
     None,
     "SO: 'bagge'. SAOL: 'hanne av far, bagge' -- 'bagge' darmed belagd i "
     "definitionstexten. Huvudbetydelsen sager 'hanne av far' i stallet "
     "for 'bagge', eftersom bagge sjalvt ar ett ord man kan behova sla "
     "upp. Rakt synonympar i ovrigt. Belagt sedan 1546, av okant "
     "ursprung.")

satt("honnett",
     "Hederlig och anständig i sitt uppträdande",
     "ålderdomlig, positiv",
     ["hederlig"],
     "Han var i alla stycken en " + B % "honnett" + " affärsman.",
     None,
     "OFULLSTANDIG KALLBILD: traffar i saol och saob, men INGEN i SO -- "
     "ordet saknas i Svensk ordbok. SAOL: 'hederlig, anstandig'. "
     "Wiktionary: 'hederlig; anstandig'. Bada kallorna ger samma tva ord, "
     "vilket gor betydelsen sakert faststalld trots SO-luckan. 'hederlig' "
     "behalls som synonym eftersom den star i SAOL:s definitionstext. "
     "Ordet lever kvar i uttrycket 'honnett ambition'.")

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("skrev %d av %d kort" % (sum(1 for k in KORT if k.get("proposed")),
                               len(KORT)))
