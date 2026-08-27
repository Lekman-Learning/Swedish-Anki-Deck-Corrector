# -*- coding: utf-8 -*-
"""Batch 2026-08-28, kort 1-17. Full v3."""
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


satt("ataxi",
     "Att inte kunna styra sina rörelser så att de blir jämna och träffsäkra",
     "fackspråklig, neutral, medicin",
     [],
     "Sjukdomen gav honom " + B % "ataxi" + ", och handen for förbi glaset "
     "varje gång han sträckte sig efter det.",
     "→ Grekiska ataxia 'oordning' — rörelserna kommer i oordning.",
     "SO: 'oformaga att samordna muskelrorelser'. SAOL samma ordalydelse. "
     "Legacys tre synonymer (koordinationsrubbning, asynergi, motorisk "
     "stelhet) star varken som SYN:synonym eller i SO/SAOL:s definitionstext "
     "-- strukna. 'motorisk stelhet' ar dessutom sakligt fel: ataxi ar inte "
     "stelhet utan bristande traffsakerhet.")

satt("barrikad",
     "Hinder man snabbt bygger av det som finns till hands för att spärra en "
     "gata ; bildligt: den sida i en strid man kämpar på",
     "neutral, neutral ; neutral, neutral",
     ["förskansning"],
     "De välte bilar och soptunnor till en " + B % "barrikad" + " tvärs över "
     "gatan.",
     "→ Italienska barricata, till barra 'stång' — man spärrade gatan med "
     "stänger.",
     "SO: 'tillfallig forsvarsvall for avsparrning', med explicit 'ofta "
     "bildligt, spec. for att beteckna plats for upprorsstrider'. SAOL: "
     "'tillfallig avsparrning el. forskansning vid gatustrid' -- forskansning "
     "star darmed i SAOL:s definitionstext och ar belagd som synonym. "
     "'befastningsvall' ur legacy ar struket: en barrikad ar per definition "
     "tillfallig, en befastningsvall ar det inte.")

satt("emalj",
     "Hård, glasartad yta som bränns fast på metall ; det hårda yttersta "
     "skiktet på en tand",
     "neutral, neutral ; fackspråklig, neutral, medicin",
     [],
     "Muggen hade ett hack där " + B % "emaljen" + " flagnat av.",
     None,
     "SO ger tva betydelser: 'tackande (och prydande), fastbrand glasmassa' "
     "och 'tandkronans harda ytterst lager'. Legacys synonymer "
     "(emaljbelaggning, tandemalj, glasbelaggning) ar alla sammansattningar "
     "med uppslagsordet eller avslojar det -- strukna, inga belagda "
     "synonymer finns.")

satt("ferrit",
     "Järn som nästan inte innehåller något kol ; hård, magnetisk massa av "
     "bränd järnoxid som används i spolar och magneter",
     "fackspråklig, neutral, kemi ; fackspråklig, neutral, teknik",
     [],
     "Spolens kärna av " + B % "ferrit" + " gjorde att den tålde höga "
     "frekvenser.",
     "→ Latin ferrum 'järn'.",
     "SO: 'jarn med mycket lag kolhalt' och 'kemisk forening med (trevard) "
     "jarnoxid som huvudkomponent'. SAOL bekraftar bada. Legacys "
     "'keramiskt material' och 'magnetiskt material' ar overordnade termer, "
     "inte synonymer -- strukna.")

satt("lappkast",
     "Att svänga runt 180 grader på stället med skidorna på ; att plötsligt "
     "byta till den rakt motsatta åsikten",
     "neutral, neutral ; neutral, lätt negativ",
     [],
     "Partiets " + B % "lappkast" + " i frågan kom bara två veckor före "
     "valet.",
     None,
     "SO: 'helomvandning pa stallet pa skidor' och 'plotslig "
     "asiktsforandring' (av. bildligt). SAOL samma tva. Legacys "
     "'helomvandning', 'kovandning' och 'tvarvandning' star inte som "
     "SYN:synonym; 'helomvandning' ar dessutom SO:s definitionsord och skulle "
     "bli cirkulart -- strukna.")

satt("läppja",
     "Dricka i små, långsamma klunkar",
     "neutral, neutral",
     ["smutta"],
     "Hon " + B % "läppjade" + " på teet medan hon läste färdigt sidan.",
     None,
     "SO: 'dricka langsamt i sma klunkar', markerat SYN:synonym mot smutta. "
     "Smutta ar darmed belagd. 'lapa' ur legacy ar struket -- lapa ar att "
     "dricka med tungan, motsatsen till sma klunkar.")

satt("serpentin",
     "Väg eller flod som slingrar sig fram i täta kurvor ; hoprullad "
     "pappersremsa som rullar ut sig när man kastar den ; ett grönaktigt "
     "mineral",
     "neutral, neutral ; neutral, neutral ; fackspråklig, neutral, geologi",
     [],
     "Barnen kastade " + B % "serpentiner" + " tills hela golvet var täckt.",
     "→ Latin serpens 'orm' — den ringlar som en orm.",
     "SO ger tre betydelser: slingrande vag/flod, pappersremsan och "
     "mineralet. SAOL bekraftar alla tre. Legacys 'ormskinn' ar sakligt fel "
     "och 'serpentinstens' avslojar uppslagsordet -- bada strukna. Legacy "
     "hade bara tva av tre betydelser; mineralet saknades.")

satt("stationär",
     "Som står kvar på ett och samma ställe och inte är gjord för att "
     "flyttas ; som inte ändrar sig över tid",
     "neutral, neutral ; fackspråklig, neutral",
     ["fast"],
     "Han bytte ut den bärbara datorn mot en " + B % "stationär" + ".",
     None,
     "SO: 'som inte flyttar sig | som normalt inte flyttas | bofast | som "
     "inte forandras'. SAOL: 'fast; bofast' -- 'fast' star darmed i SAOL:s "
     "definitionstext och ar belagd. 'immobil' och 'ororlig' ur legacy ar "
     "strukna: en stationar dator kan flyttas, den ar bara inte gjord for "
     "det, sa 'ororlig' ar for starkt.")

satt("terrakotta",
     "Rödbrunt bränt lergods utan blank yta ; färgen som sådant lergods har",
     "neutral, neutral ; neutral, neutral",
     [],
     "Krukorna av " + B % "terrakotta" + " hade blekts av solen.",
     "→ Italienska terra 'jord' och cotto 'bränd' — bränd jord.",
     "SO: 'typ av rodbrunt, brant, oglaserat lergods', med 'av. om fargen'. "
     "SAOL: 'oglaserat gul- el. rodbrunt lergods'. Legacys 'lergods' och "
     "'keramik' ar overordnade termer -- terrakotta ar en SORT lergods, inte "
     "samma sak. Strukna. Fargbetydelsen saknades i legacy.")

satt("utarmad",
     "Tömd på det som gav värde eller näring, så att nästan inget är kvar",
     "neutral, negativ",
     [],
     "Jorden var " + B % "utarmad" + " efter tjugo år med samma gröda.",
     None,
     "SO (utarma): 'gora fattig', med 'av. om att skapa brist pa nagot'. "
     "SAOL: 'gora utfattig'. Legacys forsta definition ('daligt tillstand "
     "fran brist pa energi') traffar bara den bildliga anvandningen om "
     "personer och missar karnan: att nagot toms pa sina tillgangar. "
     "Omskrivet. Inga belagda synonymer.")

satt("deklarera",
     "Säga rakt ut vad man tycker eller tänker göra ; lämna in uppgifter om "
     "vad man tjänat under året ; tala om vid tullen vad man har med sig",
     "neutral, neutral ; formell, neutral, ekonomi ; formell, neutral",
     [],
     "Han " + B % "deklarerade" + " att han tänkte sluta redan i höst.",
     "→ Latin declarare 'göra klart'.",
     "SO ger tre betydelser: 'offentligt tillkannage', 'skriftligt lamna "
     "uppgifter om sina inkomster' och 'av. om att lamna viktiga uppgifter "
     "vid granskontroll'. Legacy hade bara de tva forsta -- tullbetydelsen "
     "saknades och ar tillagd. Inga belagda synonymer: 'tillkannage' och "
     "'ange' ar SO:s definitionsord, inte SYN:synonym.")

satt("dossier",
     "Samlade papper om en viss person eller sak, ofta med känsligt innehåll",
     "formell, neutral",
     [],
     "Polisen hade en tjock " + B % "dossier" + " om mannen.",
     "→ Franska dos 'rygg' — en bunt handlingar med titeln skriven på "
     "ryggen.",
     "SO: 'dokument med fakta om visst (ofta kansligt) amne'. SAOL: 'samling "
     "handlingar rorande ett arende'. Legacys 'aktsamling' och "
     "'faktasamling' star i ingen kalla -- strukna.")

satt("försumma",
     "Låta bli att sköta något man borde ha skött",
     "neutral, negativ",
     [],
     "Han " + B % "försummade" + " sina barn under åren då jobbet gick "
     "först.",
     None,
     "SO: 'inte agna tillrackligt uppmarksamhet at | utebli fran | glomma "
     "bort, missa'. VIKTIGT: SO listar eftersatta, negligera och nonchalera "
     "som JFR:cohyponym -- INTE SYN:synonym. Enligt valvets synonymsparr "
     "(2026-08-12) far en cohyponym aldrig skrivas in som synonym. Legacys "
     "alla tre synonymer ar just dessa tre -- strukna, listan lamnas tom.")

satt("härsken",
     "Om smör och annat fett: som fått unken lukt och smak av att ha stått "
     "för länge ; om person: sur och lättretad",
     "neutral, negativ ; vardaglig, negativ",
     [],
     "Smöret hade blivit " + B % "härsket" + " av att stå framme i värmen.",
     None,
     "SO: 'som genom kemisk forandring fatt obehaglig lukt och smak' och "
     "'arg och vresig' (vardagligt). SAOL: 'ankommen, ngt skamd | sur, arg'. "
     "Legacys andra definition ('fett eller olja som oxiderat och blivit "
     "atbar') ar direkt fel -- harsket fett ar tvartom OATBART. Rattat. "
     "Personbetydelsen saknades helt i legacy.",
     grupper=[["skämd"], ["sur"]])

satt("krabb",
     "Om sjön: med korta, branta vågor som slår tätt",
     "fackspråklig, neutral, sjöfart",
     [],
     "Båten stampade i den " + B % "krabba" + " sjön utanför udden.",
     None,
     "SO: 'som utmarks av korta, toppiga vagor', enda exemplet 'krabb sjo'. "
     "Ordet anvands alltsa bara om sjo/vatten. Legacys synonymer ('sjo', "
     "'korta', 'stormig') ar inte synonymer alls -- 'sjo' ar substantivet "
     "ordet beskriver och 'stormig' ar fel: krabb sjo handlar om vagornas "
     "FORM, inte om vindstyrkan. Strukna.")

satt("nonchalera",
     "Med flit låta bli att bry sig om någon eller något",
     "neutral, negativ",
     ["strunta i"],
     "Hon " + B % "nonchalerade" + " frågan och gick vidare.",
     None,
     "SO: 'underlata att beakta och ta hansyn till', med 'ibland med "
     "avseende pa person (ofta med avsikt att sara)'. SAOL: 'inte bry sig "
     "om, strunta i; forsumma, vardslosa' -- 'strunta i' star i SAOL:s "
     "definitionstext och ar belagd. 'forsumma' star ocksa dar men skiljer "
     "sig i avsikt: att forsumma kan vara oavsiktligt, att nonchalera ar det "
     "inte. Struken.")

satt("plätera",
     "Lägga ett tunt skikt av en finare metall utanpå en enklare",
     "fackspråklig, neutral, teknik",
     [],
     "Ringen var bara " + B % "pläterad" + ", inte massivt guld.",
     None,
     "SO: 'forse (plat av oadel metall) med ett overdrag av adel eller "
     "rostbestandig metall'. SAOL: 'forse med skikt av annat dyrbarare "
     "material'. Legacys 'forgylla' och 'forsilvra' ar specialfall av "
     "platering (en viss metall), inte synonymer -- strukna. "
     "'metallisera' star i ingen kalla.")

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Skrev %d kort." % sum(1 for k in KORT if k.get("approved")))
