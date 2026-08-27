# -*- coding: utf-8 -*-
"""Batch 2026-08-28, kort 18-34. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
KALLA = ("SO och SAOL via https://svenska.se/api/msearch?ord=%s "
         "(hamtat 2026-08-28, HTTP 200)")
B = '<font color="#3498db">%s</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, grupper=None, tillat=None,
         conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": grupper, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": KALLA % urllib.parse.quote(o),
                    "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("sabbat",
     "Judendomens vilodag, från fredagskväll till lördagskväll ; bildligt: "
     "ledighet från allt arbete",
     "fackspråklig, neutral, religion ; neutral, neutral",
     [],
     "Under " + B % "sabbaten" + " fick inget arbete utföras.",
     "→ Hebreiska shabbat 'vila'.",
     "SO: 'veckodag som inom judendomen raknas som vilodag', med 'nagon gang "
     "av. om sondagen som kristen vilodag' och 'av. bildligt om ledighet i "
     "allmanhet'. VIKTIG AVGRANSNING: bade SO och SAOL listar ocksa "
     "'sabotera; forstora' -- men det ar verbet SABBA (till sabotera), ett "
     "helt annat ord med annat ursprung som slaupp.py drar in i samma "
     "trafflista. Den betydelsen hor INTE till uppslagsordet sabbat och ar "
     "utelamnad. Legacys 'lordag' som synonym ar struken: sabbaten borjar "
     "pa fredagskvallen.")

satt("sinnrik",
     "Smart uttänkt, så att lösningen blir både enkel och oväntad",
     "neutral, positiv",
     ["fyndig", "skarpsinnig"],
     "En " + B % "sinnrik" + " mekanism gjorde att dörren låste sig själv.",
     None,
     "SO: 'fyndigt och skarpsinnigt uttankt'. SAOL: 'skarpsinnig, fyndig; "
     "konstrik' -- bada synonymerna star i SAOL:s definitionstext och ar "
     "belagda. Legacys 'pahittig' star i ingen kalla och ar struken. "
     "finurlig och konstfardig ar SO:s JFR:cohyponym, inte SYN:synonym.")

satt("aber",
     "Ett oväntat problem som dyker upp och gör att något inte går som tänkt",
     "neutral, lätt negativ",
     [],
     "Planen var bra, men det fanns ett " + B % "aber" + ": pengarna räckte "
     "inte.",
     "→ Tyska aber 'men' — hela ordet är alltså ett inbakat 'men'.",
     "SO: '(ovantat) hinder'. SAOL: 'ovantat hinder, problem'. Legacys "
     "'stotesten' star i ingen kalla och ar struken; 'hinder' och "
     "'svarighet' ar SO:s och SAOL:s definitionsord och skulle bli "
     "cirkulara. Listan lamnas tom.")

satt("antropofag",
     "Människa som äter kött av andra människor",
     "ngt ålderdomlig, neutral",
     ["kannibal"],
     "Berättelserna om öns " + B % "antropofager" + " visade sig vara "
     "sjömansskrönor.",
     "→ Grekiska anthropos 'människa' och phagein 'äta'.",
     "SO: 'manniskoatare', markerat SYN:synonym mot kannibal -- kannibal ar "
     "darmed belagd. SO markerar ordet 'mindre brukligt', vilket ger "
     "registret 'ngt alderdomlig'. Legacys 'androfag' star i ingen kalla "
     "och ar struken.")

satt("avtrubbad",
     "Som slutat reagera lika starkt, för att man vant sig vid för mycket",
     "neutral, lätt negativ",
     [],
     "Efter tjugo år i yrket var han " + B % "avtrubbad" + " inför blod.",
     None,
     "SO (avtrubba): 'minska kanslighet hos', med exemplen 'folk blir "
     "avtrubbade av allt vald pa tv' och 'hans omdome var avtrubbat av "
     "alkohol'. SAOL identisk. forsloa och trubba ar SO:s JFR:cohyponym, "
     "inte SYN:synonym -- legacys 'bedovad', 'kanslolos' och 'forslodad' ar "
     "darfor strukna. 'kanslolos' ar dessutom for starkt: avtrubbad ar en "
     "gradvis forsvagning, inte franvaro av kansla.")

satt("blödig",
     "Så känslig inför andras lidande att man inte står ut med att se det",
     "neutral, lätt negativ",
     ["lättrörd"],
     "Han var för " + B % "blödig" + " för att själv avliva den skadade "
     "fågeln.",
     None,
     "SO: 'som latt kanner obehag infor lidande', med 'av. om handling eller "
     "dylikt'. SAOL: 'lattrord, sentimental' -- lattrord star i SAOL:s "
     "definitionstext och ar belagd. Legacys 'vek' och 'pjoskig' star i "
     "ingen kalla; 'pjoskig' fangar dessutom fel sak (overdriven omtanke om "
     "sig sjalv, inte om andras lidande). Strukna.")

satt("buskis",
     "Enkel folklig humor med breda skämt och tydliga poänger",
     "vardaglig, lätt negativ",
     [],
     "Sommarens " + B % "buskis" + " på friluftsteatern sålde slut varje "
     "kväll.",
     "→ Till buskteater, där busk- betydde 'utomhus-'.",
     "SO: '(framforande som kannetecknas av) enkla poanger och effekter', "
     "med 'av. om film, teaterstycke eller dylikt' och 'av. bildligt' "
     "(debatten urartade till rena buskisen). SAOL: 'buskteater'. "
     "'buskteater' som synonym ar VALD BORT trots att den star i SAOL: den "
     "avslojar uppslagsordet. bondkomik ar SO:s JFR:cohyponym, inte "
     "SYN:synonym.")

satt("clou",
     "Det bästa numret i ett program — den del alla väntar på",
     "neutral, positiv",
     ["glansnummer", "höjdpunkt"],
     "Kvällens " + B % "clou" + " var när kören klev in bakifrån i salongen.",
     "→ Franska clou 'spik' — det som spikar fast hela kvällen i minnet.",
     "SO: 'hojdpunkt'. SAOL: 'glansnummer, hojdpunkt' -- bada synonymerna "
     "star i SAOL:s definitionstext och ar belagda. Legacys 'klimax' star i "
     "ingen kalla och ar struken.")

satt("duplikat",
     "Ett andra exemplar som är exakt likadant som originalet",
     "formell, neutral",
     ["dubblett"],
     "Han begärde ett " + B % "duplikat" + " av kvittot till försäkringen.",
     None,
     "SO: 'kopia', med dubblett som JFR. SAOL: 'dubblett; avskrift' -- "
     "dubblett star i SAOL:s definitionstext och ar belagd. 'avskrift' ar "
     "utelamnad: en avskrift ar handskriven och behover inte vara identisk. "
     "Legacys 'dublettexemplar' ar en sammansattning som avslojar samma sak "
     "tva ganger -- struken.")

satt("dysenteri",
     "Smittsam tarmsjukdom med svår, blodig diarré och ont i magen",
     "fackspråklig, neutral, medicin",
     [],
     "Det trasiga avloppet gjorde att flera i byn fick " + B % "dysenteri" +
     ".",
     "→ Grekiska dys- 'dålig' och enteron 'tarm'.",
     "SO: 'en smittsam tarmsjukdom med smartsamma, blodiga diarreer'. SAOL: "
     "'en tarmsjukdom'. Legacys 'rodsot' ar det gamla svenska namnet men "
     "star varken som SYN:synonym eller i SO/SAOL:s definitionstext -- "
     "struken. 'diarre' ar ett symtom, inte en synonym.")

satt("däxel",
     "Yxa där eggen sitter på tvären mot skaftet, så att man kan hugga ur "
     "trä i en yta",
     "fackspråklig, neutral, teknik",
     [],
     "Med en " + B % "däxel" + " högg han ur skrovet ur ekstocken.",
     None,
     "SO: 'ett yxliknande verktyg med bladet vinkelratt mot skaftet'. SAOL: "
     "'ett yxliknande verktyg med eggen tvarstalld mot skaftet'. Legacys "
     "'yxa', 'bila' och 'hacka' ar alla FEL som synonymer: hela poangen med "
     "en daxel ar att eggen star pa tvaren, vilket en vanlig yxa och en bila "
     "inte gor. Strukna.")

satt("eskalation",
     "Att en konflikt trappas upp steg för steg och blir allvarligare",
     "formell, neutral",
     [],
     "Man befarade en " + B % "eskalation" + " av konflikten efter attacken.",
     "→ Engelska escalation, samma ord som escalator 'rulltrappa' — det går "
     "uppåt av sig självt.",
     "SO: 'upptrappning'. Endast en betydelse i SO; SAOL ger ingen egen "
     "definitionstext. Legacys 'intensifiering' och 'acceleration' star i "
     "ingen kalla -- strukna. 'upptrappning' ar SO:s enda definitionsord och "
     "ar utelamnad som synonym for att undvika en helt cirkular rad.")

satt("fallbila",
     "Redskap för halshuggning där ett tungt blad faller ner mellan två "
     "stolpar ; bildligt: det som avgör om något får leva vidare eller "
     "stoppas",
     "ngt ålderdomlig, neutral, historia ; neutral, negativ",
     ["giljotin"],
     "Projektet riskerar att hamna under " + B % "fallbilan" + " när "
     "budgeten ses över.",
     None,
     "SO: 'giljotin', med 'nagon gang bildligt' och exemplet 'projektet "
     "loper risk att hamna under fallbilan'. SAOL: 'i aldre tid: anordning "
     "for halshuggning'. giljotin ar SO:s hela definition och darmed belagd "
     "som synonym. Legacys 'halshuggningsredskap' och 'avrattningsverktyg' "
     "ar konstruerade sammansattningar utan kalla -- strukna. Den bildliga "
     "betydelsen saknades helt i legacy.")

satt("fjolla",
     "Nedsättande om kvinna som uppfattas som tanklös ; nedsättande om man "
     "som uppfattas som feminin ; att bete sig tillgjort och fånigt",
     "ngt ålderdomlig, nedsättande ; vardaglig, nedsättande ; vardaglig, "
     "nedsättande",
     [],
     "Hon " + B % "fjollade" + " sig på scenen för att få publiken att "
     "skratta.",
     None,
     "SO: 'tanklos flicka eller kvinna' (markerat 'nagot alderdomligt; "
     "nedsattande'), 'ibland av. om man med feminin framtoning', samt verbet "
     "'bete sig fjolligt'. SAOL bekraftar alla tre. Legacys 'toka', 'vap' "
     "och 'sjap' star i ingen kalla -- strukna. Legacy hade bara den forsta "
     "betydelsen; bade manbetydelsen och verbet saknades.")

satt("förnöjsam",
     "Nöjd med lite, och sällan sugen på mer än man redan har",
     "neutral, positiv",
     [],
     "Han levde " + B % "förnöjsamt" + " på det lilla han hade.",
     None,
     "SO: 'fornojd' -- ett cirkulart definitionsord som inte gar att "
     "anvanda. SAOL ar den brukbara kallan: 'nojd med lite'. Kortet foljer "
     "SAOL. Legacys 'ansprakslos', 'tillfreds' och 'glad' star i ingen "
     "kalla; 'glad' ar dessutom sakligt fel -- fornojsam handlar om vad man "
     "kraver, inte om humor. Strukna.")

satt("gigolo",
     "Man som mot betalning dansar med eller är sällskap åt rika kvinnor",
     "neutral, lätt negativ",
     [],
     "Han jobbade som " + B % "gigolo" + " på hotellets danssalong.",
     None,
     "SO: 'man som mot betalning dansar med kvinnliga gaster', med 'av. om "
     "man som mot betalning ar alskare till (rika) kvinnor'. SAOL: "
     "'yrkesdansor pa restaurang; man som lever pa rika kvinnor'. Legacys "
     "'hyrkavaljer' och 'betald eskort' star i ingen kalla -- strukna.")

satt("glop",
     "Ung kille som beter sig oförskämt och tror sig veta bäst",
     "vardaglig, nedsättande",
     ["spoling", "slyngel"],
     "Ett par unga " + B % "glopar" + " stod och hånade honom vid "
     "hållplatsen.",
     "→ Fornsvenska gloper 'fåne', egentligen 'en som gapar och ser dum ut'.",
     "SO: 'slyngel' (vard.). SAOL: 'spoling, slyngel' -- bada star i SAOL:s "
     "definitionstext och ar belagda. Legacys 'valp' star i ingen kalla och "
     "ar struken. Legacys ANDRA definition ('nagot av dalig kvalitet eller "
     "lagt varde') finns varken i SO eller SAOL -- den kommer fran "
     "Wiktionarys bibetydelse 'sorja, klet' och ar struken.")

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Skrev %d kort." % sum(1 for k in KORT if k.get("approved")))
