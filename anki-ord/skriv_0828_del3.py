# -*- coding: utf-8 -*-
"""Batch 2026-08-28, kort 35-52. Full v3.

'in infinitum' skrivs INTE har -- se skriv_0828_pausa.py.
"""
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
         conf=9, kalla=None):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": grupper, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": kalla or (KALLA % urllib.parse.quote(o)),
                    "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("grafologi",
     "Tron att en persons karaktär går att läsa ut ur handstilen",
     "fackspråklig, neutral, psykologi",
     [],
     "Företaget använde " + B % "grafologi" + " vid anställningar, trots att "
     "metoden saknar vetenskapligt stöd.",
     "→ Grekiska graphein 'skriva' och logos 'lära'.",
     "SO: 'laran om hur en persons karaktar avspeglar sig i handstilen', med "
     "'av. om identifiering av person med ledning av handstilen'. SAOL "
     "lagger till en avgorande upplysning som legacy saknade helt: 'ej "
     "vetenskapligt erkand'. Den star nu i exempelmeningen. Legacys tre "
     "synonymer ar alla konstruerade sammansattningar utan kalla -- "
     "strukna.")

satt("hajk",
     "Längre vandring där man sover ute på vägen",
     "vardaglig, neutral",
     [],
     "Scouterna var ute på " + B % "hajk" + " i två dygn.",
     "→ Engelska hike 'vandring'.",
     "SO: 'langre fotvandring med overnattning utomhus', med 'av. om annan "
     "friluftsaktivitet'. SAOL: 'scoutvandring med overnattning i talt'. "
     "Legacys 'overnattning' som synonym ar fel ordklass och fel sak -- "
     "overnattningen ar en DEL av en hajk, inte samma sak. Strukna.")

satt("hebré",
     "Medlem av det forntida folk som Gamla testamentet handlar om ; person "
     "som talar hebreiska",
     "ngt ålderdomlig, neutral, historia ; neutral, neutral",
     ["israelit"],
     "Berättelsen om uttåget ur Egypten handlar om " + B % "hebréerna" + ".",
     "→ Hebreiska ibri, egentligen 'någon från andra sidan av floden'.",
     "SO: 'israelit' och 'hebreisktalande jude', den senare markerad 'i Nya "
     "testamentet ibland'. israelit ar SO:s hela forsta definition och "
     "darmed belagd. Legacys 'semit' ar struken: semit ar en sprakfamiljs "
     "vidare beteckning och sammanfaller inte med hebre. Legacys forsta "
     "definition ('tillhor den judiska religionen och kulturen') ar "
     "omskriven -- SO:s betydelse ar folkslaget, inte trosbekannelsen.")

satt("homograf",
     "Ord som stavas precis som ett annat ord men betyder något annat",
     "fackspråklig, neutral, lingvistik",
     [],
     "Att 'tomten' kan vara både en gubbe och en markbit gör ordet till en "
     + B % "homograf" + ".",
     "→ Grekiska homos 'samma' och graphein 'skriva' — jämför homofon, där "
     "fon betyder ljud.",
     "SO: 'ord (lemma) som stavas likadant som visst annat'. VIKTIGT: SO "
     "listar homofon och homonym som JFR:cohyponym, INTE SYN:synonym -- de "
     "ar narbeslaktade men skilda begrepp, och skillnaden ar precis det HP "
     "provar. Legacy hade 'homonym' som synonym, vilket ar sakligt fel: en "
     "homonym stavas OCH lat likadant. Struken tillsammans med 'likstavade "
     "ord' och 'stavning', som star i ingen kalla.")

satt("hyperbol",
     "Medveten överdrift som stilgrepp — den ska inte tas bokstavligt",
     "fackspråklig, neutral, litteraturvetenskap",
     ["överdrift"],
     "'Jag har sagt det tusen gånger' är en " + B % "hyperbol" + ".",
     "→ Grekiska hyperbole 'att kasta över målet'.",
     "SO: 'uttryck som innebar en stark (medveten) overdrift', med litotes "
     "markerat som MOTSATS:antonym. SAOL: 'overdrivet uttryck, overdrift' -- "
     "overdrift star i SAOL:s definitionstext och ar belagd. Legacys "
     "'forstorning' och 'exaggeration' star i ingen kalla -- strukna. "
     "'exaggeration' ar dessutom knappt svenska.")

satt("härförleden",
     "För bara en kort tid sedan",
     "formell, neutral",
     ["nyligen"],
     "I en debattartikel " + B % "härförleden" + " gick hon till angrepp mot "
     "förslaget.",
     None,
     "SO: 'for en kort tid sedan'. SAOL: 'nyligen' -- nyligen ar SAOL:s hela "
     "definition och darmed belagd. Legacys 'haromdagen' och 'nyss' star i "
     "ingen kalla; 'nyss' ar dessutom for narliggande i tid -- harforleden "
     "kan galla flera veckor tillbaka. Strukna.")

satt("ibidem",
     "I samma källa och på samma ställe som nyss nämndes — används i "
     "fotnoter",
     "fackspråklig, neutral, litteraturvetenskap",
     [],
     "Fotnoten nöjde sig med ett " + B % "ibidem" + " i stället för hela "
     "titeln en gång till.",
     "→ Latin ibidem 'på samma ställe'.",
     "SO: 'pa anfort stalle'. SAOL: 'vid vetenskapliga hanvisningar: i samma "
     "skriftliga kalla, pa samma stalle'. SAOL:s formulering ar den "
     "brukbara -- SO:s 'anfort stalle' ar sjalvt svarare an uppslagsordet. "
     "Legacys 'sammastades' och 'dar ocksa' star i ingen kalla; 'ibid.' ar "
     "bara en forkortning av uppslagsordet och avslojar det. Strukna.")

satt("involvera",
     "Dra in någon i något ; ha något som en del av sig",
     "neutral, neutral ; formell, neutral",
     ["innefatta"],
     "Han blev " + B % "involverad" + " i kampanjen nästan mot sin vilja.",
     None,
     "SO: 'komma (nagon) att bli inblandad' och 'innefatta'. SAOL: "
     "'innesluta i sig; innefatta; blanda in' -- innefatta star i bade SO:s "
     "och SAOL:s definitionstext och ar belagd. Legacys 'inkludera' ar "
     "struken: SO listar den som JFR:cohyponym, inte SYN:synonym. "
     "'engagera' star i ingen kalla och betyder dessutom att nagon gar in "
     "frivilligt -- involvera kan ske mot ens vilja.")

satt("kalejdoskop",
     "Rör med speglar och färgade glasbitar som visar ett nytt mönster varje "
     "gång man vrider ; bildligt: något brokigt som hela tiden växlar",
     "neutral, neutral ; litterär, neutral",
     [],
     "Boken är ett " + B % "kalejdoskop" + " av röster från hela kriget.",
     "→ Grekiska kalos 'skön', eidos 'form' och skopein 'se'.",
     "SO: 'tubformad anordning som man kan se skiftande, brokiga bilder i', "
     "med 'ofta bildligt om andra farggranna och mangskiftande foreteelser'. "
     "SAOL: 'en sorts optisk leksak'. Legacys 'tittskap' och 'spegelskap' "
     "star i ingen kalla och ar dessutom andra foremal -- strukna. Den "
     "bildliga betydelsen fanns inte i legacy och ar tillagd; den ar den "
     "vanligaste i skriven text.")

satt("konfirmation",
     "Kyrklig högtid där en ung person bekräftar sitt dop ; formellt: att "
     "något fastställs och blir gällande",
     "fackspråklig, neutral, religion ; formell, neutral",
     ["stadfästelse"],
     "Efter " + B % "konfirmationen" + " bjöd familjen på middag.",
     None,
     "SO ger tva betydelser: 'bekraftelse' (markerad formell) och 'kyrklig "
     "handling som bekraftar dopet'. SAOL: 'bekraftelse, stadfastelse | en "
     "kyrklig handling som bekraftar dopet' -- stadfastelse star i SAOL:s "
     "definitionstext och ar belagd. 'bekraftelse' ar utelamnad som synonym "
     "eftersom ordet redan bar huvudbetydelsen och raden hade blivit "
     "cirkular. Legacys 'dopbekraftelse' ar en konstruerad sammansattning "
     "utan kalla -- struken. Legacy hade bara den kyrkliga betydelsen.")

satt("konsternera",
     "Göra någon så förbluffad att hen tappar fattningen",
     "formell, neutral",
     [],
     "Frågan " + B % "konsternerade" + " honom så att han blev alldeles "
     "tyst.",
     None,
     "SO: 'gora hapen och forvirrad'. SAOL: 'gora hapen, bringa ur "
     "fattningen'. Legacys ANDRA definition ('lura eller bedra nagon genom "
     "forvirring') finns i ingen kalla och ar sakligt fel -- konsternera "
     "innebar ingen avsikt att bedra. Struken. Synonymerna 'forbrylla', "
     "'forvirra' och 'konfundera' star i ingen av de tva ordbockerna "
     "(forbrylla kommer fran Wiktionary) -- strukna.")

satt("lillgammal",
     "Om barn: som låter och beter sig som en vuxen",
     "neutral, skämtsam",
     [],
     "Sjuåringens " + B % "lillgamla" + " kommentarer fick alla vid bordet "
     "att skratta.",
     None,
     "SO: 'som verkar alltfor forstandig for sin alder', med 'av. om "
     "handling och dylikt'. SAOL: 'om barn: \"vuxen\" pa ett lustigt satt' "
     "-- det ar SAOL:s 'lustigt' som ger registret skamtsam. Legacys "
     "'bradmogen' ar struken: SO listar den som JFR:cohyponym, inte "
     "SYN:synonym, och bradmogen galler utveckling pa riktigt medan "
     "lillgammal galler hur det verkar. 'gammalklok' och 'forsigkommen' "
     "star i ingen kalla.")

satt("litania",
     "Lång kyrkobön där präst och församling turas om att sjunga ; bildligt: "
     "lång rad av klagomål som upprepas gång på gång",
     "fackspråklig, neutral, religion ; neutral, lätt negativ",
     [],
     "Hans vanliga " + B % "litania" + " om de höga skatterna började igen.",
     None,
     "SO: 'en langre kyrkobon som framfors genom vaxelsang mellan prasten "
     "och forsamlingen' och 'lang upprakning av klagomal' (ofta bildligt). "
     "SAOL: 'kyrkobon med upprepade instammande boneropp fran forsamlingen; "
     "lang klagovisa'. Legacys andra definition ('botfardig bon eller vadjan "
     "om nad under svara tider') ar fel -- den bildliga betydelsen handlar "
     "om KLAGOMAL, inte om bon. Rattat. 'jeremiad' och 'klagosang' star i "
     "ingen av ordbockerna -- strukna.")

satt("lombardera",
     "Låna ut pengar mot pant, eller själv ta lån med värdepapper som "
     "säkerhet",
     "fackspråklig, neutral, ekonomi",
     [],
     "Banken " + B % "lombarderade" + " aktierna och betalade ut lånet samma "
     "dag.",
     None,
     "SARSKILT FALL: ordet finns som uppslagsord i SAOL (verb, amnesomrade "
     "'ekon.') men SAOL ger INGEN definitionstext, bara 'jfr lombardlan'. SO "
     "har noll traffar. Kallan ar darfor SAOB, som ar entydig under "
     "avledningar till LOMBARD: 'ekon. till II: utlana (panningar) mot "
     "handfangen pant; av.: belana (pant som lamnas ss. sakerhet)'. "
     "🔴 OLD-FACIT AR FEL: det sager 'hyra ut', och legacys synonymlista "
     "borjar med just 'hyra ut'. Att lombardera har ingenting med uthyrning "
     "att gora. Bade OLD och legacy ar alltsa fel pa samma satt -- kortet ar "
     "helt omskrivet. Inga belagda synonymer.",
     kalla="SAOB via https://www.saob.se/artikel/?seek=lombardera "
           "(hamtat 2026-08-28, HTTP 200, publicerad 1941) plus SAOL via "
           "https://svenska.se/api/msearch?ord=lombardera (uppslagsord utan "
           "definitionstext)")

satt("makaber",
     "Obehagligt på ett sätt som drar tankarna till död och lik",
     "neutral, negativ",
     ["kuslig"],
     "Han har ett " + B % "makabert" + " intresse för gamla "
     "obduktionsbilder.",
     "→ Franska danse macabre 'dödsdans'.",
     "SO: 'som vacker obehagliga, skrackblandade kanslor', med 'av. "
     "forsvagat'. SAOL: 'kuslig genom anspelning pa doden' -- kuslig star i "
     "SAOL:s definitionstext och ar belagd. Legacys 'hemsk' och 'ohygglig' "
     "star i ingen kalla och missar dessutom det som skiljer makaber fran "
     "dem: kopplingen till DODEN. SAOL:s formulering ar darfor den som styr "
     "huvudbetydelsen.")

satt("mammon",
     "Pengar och ägodelar sedda som något man dyrkar i stället för Gud",
     "högtidlig, negativ, bibliskt",
     [],
     "Han varnade i predikan för att tjäna den snöda " + B % "mammon" + ".",
     "→ Arameiska mamon 'rikedomar'.",
     "SO: '(begar efter) jordisk rikedom', markerat hogtidligt. SAOL: "
     "'rikedom som avgud, jordiska agodelar' -- det ar SAOL:s 'som avgud' "
     "som ger ordet dess laddning, och den saknades helt i legacy, som bara "
     "skrev 'jordisk rikedom'. Utan avgudadelen ar mammon bara ett fint ord "
     "for pengar, vilket det inte ar. Legacys 'pengar' och 'penninggud' som "
     "synonymer ar strukna -- 'pengar' ar for platt, 'penninggud' star i "
     "ingen kalla.")

satt("matiné",
     "Föreställning som spelas mitt på dagen i stället för på kvällen",
     "neutral, neutral",
     [],
     "Barnen gick på " + B % "matiné" + " och var hemma långt före mörkret.",
     "→ Franska matin 'morgon' — trots namnet ligger den numera på "
     "eftermiddagen.",
     "SO: 'middagsforestallning'. SAOL: 'eftermiddagsforestallning ofta pa "
     "biograf'. Legacys 'lunchforestallning' star i ingen kalla och ar "
     "struken; 'eftermiddagsforestallning' och 'dagsforestallning' avslojar "
     "innehallet helt och ar ocksa strukna. Etymologin ar med just for att "
     "den ar kontraintuitiv: ordet betyder morgon men anvands om "
     "eftermiddagen.")

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Skrev %d kort." % sum(1 for k in KORT if k.get("approved")))
