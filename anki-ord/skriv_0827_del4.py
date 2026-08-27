# -*- coding: utf-8 -*-
"""Batch 2026-08-27, kort 30-41. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-27_v3-batch.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
KALLA = ("SO och SAOL via https://svenska.se/api/msearch?ord=%s "
         "(hamtat 2026-08-27, HTTP 200)")
B = '<font color="#3498db">%s</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, tillat=None, conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": None, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": KALLA % urllib.parse.quote(o),
                    "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("a la carte",
     "Att beställa rätt för rätt ur menyn i stället för att ta en färdig meny till fast pris",
     "neutral, neutral, matlagning",
     [],
     "De åt " + B % "a la carte" + " och valde varsin rätt i stället för dagens meny.",
     "→ Franska à la carte 'efter kortet', alltså efter matsedeln.",
     "🔴 UPPSLAGET GAV INGEN TRAFF: svenska.se returnerade INGEN KALLA for "
     "stavningen 'a la carte'. Ordboksformen ar 'a la carte' med accent grave "
     "(a), och kortets uppslagsord ar felstavat i decket. "
     "🔴 OLD_FACIT AR DESSUTOM FEL: det sager 'pa fasta menyen', vilket ar "
     "MOTSATSEN -- a la carte betyder just att INTE ta den fasta menyn utan "
     "valja rratt for ratt. Huvudbetydelsen ar darfor skriven mot uttryckets "
     "franska ordagranna innebord ('efter kortet'), inte mot old_facit. "
     "BOR OMGRANSKAS nar uppslagsordet rattats till 'a la carte'.",
     tillat={"uppslag_saknas":
             "svenska.se har ingen post for den felstavade formen. Se "
             "slutsatsen -- kortet ar markt for omgranskning.",
             "frammande_uppslagsord":
             "Det enda 'frammande' uppslagsordet ar 'a la carte' med accent "
             "-- alltsa RATT form av samma uttryck. Det bekraftar diagnosen "
             "i stallet for att motsaga den."},
     conf=6)

satt("analgesi",
     "Att inte känna smärta — antingen för att smärtan stillats eller för att förmågan att känna den saknas",
     "fackspråklig, neutral, medicin",
     ["smärtstillning"],
     "Patienten fick " + B % "analgesi" + " innan såret syddes.",
     "→ Grekiska an- 'utan' och algos 'smärta'.",
     "SAOL: 'smartstillning' -- enda ordboksposten. Ingen SO-post och ingen "
     "Wiktionary-post, sa underlaget ar tunt. old_facit sager 'sankt "
     "smartuppfattning', vilket tacker den andra halvan (utebliven kansla, "
     "inte bara behandling) -- bada finns darfor i huvudbetydelsen.",
     conf=7)

satt("antediluviansk",
     "Hopplöst föråldrad — så gammalmodig att det blir komiskt",
     "litterär, skämtsam",
     ["föråldrad"],
     "Han hade en " + B % "antediluviansk" + " syn på vem som skulle diska.",
     "→ Latin ante- 'före' och diluvium 'syndaflod' — alltså äldre än syndafloden.",
     "SO: 'totalt foraldrad', markt 'skamtsamt', med SYN:synonym-tagg. SAOL: "
     "'ytterligt foraldrad; urspr. aldre an syndafloden'. 'foraldrad' leder "
     "bada definitionerna. JFR ger urmodig (cohyponym, ej inskriven). "
     "Etymologin ar sjalva poangen med ordet och darfor med.")

satt("berått",
     "Med vett och vilja — efter att ha tänkt igenom det först. Används nästan bara i 'med berått mod'",
     "ngt ålderdomlig, neutral, juridik",
     [],
     "Han gjorde det med " + B % "berått" + " mod, inte i affekt.",
     "→ Fornsvenska beradt, av beradha 'rådslå'. Samma rot som råd.",
     "🔴 SO GER INGEN DEFINITION: uppslaget innehaller bara frasen 'med berat "
     "mod', en JFR till 'mod' och etymologin. Ordet lever inte sjalvstandigt i "
     "modern svenska -- det finns bara i det uttrycket. Huvudbetydelsen ar "
     "darfor harledd ur etymologin (beradha = radsla, overlagga) och ur "
     "frasens juridiska anvandning, inte ur en ordboksglosa. Tom "
     "synonymlista: ingen kandidat finns i SO eller SAOL.",
     tillat={"uppslag_saknas":
             "SO har posten men utan definitionsglosa -- bara frasen och "
             "etymologin. Se slutsatsen for hur betydelsen harleddes."},
     conf=7)

satt("bjäbb",
     "Uppkäftigt och tjatigt prat som tröttar ut den som lyssnar",
     "vardaglig, negativ",
     [],
     "Läraren orkade inte med mer " + B % "bjäbb" + " och skickade ut honom.",
     "→ Till bjäbba, ett ljudhärmande ord.",
     "SO: 'uppnosigt och trottande prat', markt 'vardagligt'. Ingen "
     "SAOL-post. JFR ger kabbel och tjafs -- bada ar cohyponymer, inte "
     "synonymer, och ar darfor inte inskrivna trots att old_facit listar dem.")

satt("boudoir",
     "En finare dams eget rum, dit hon drog sig undan från sällskapet",
     "ngt ålderdomlig, neutral, historia",
     [],
     "Grevinnan tog emot bara de närmaste i sin parfymerade " + B % "boudoir" + ".",
     "→ Franska boudoir, till bouder 'vara på dåligt humör' — rummet man surade i.",
     "SO: 'en dams finare privata salong', markt 'mest historiskt'. SAOL: 'en "
     "dams privata salong', markt 'ald.'. 'damrum' star som JFR (cohyponym) i "
     "SO och ar darfor INTE inskrivet som synonym. Svensk "
     "stavning ar budoar; boudoir ar franska formen. Etymologin ar ovanligt "
     "upplysande och darfor med.",
     tillat={"frammande_uppslagsord":
             "Det enda 'frammande' uppslagsordet ar 'budoar' -- den svenska "
             "stavningen av samma ord, inte ett annat ord."},
     conf=8)

satt("defekt",
     "Som har ett fel och därför inte fungerar som det ska ; själva felet eller skadan",
     "neutral, negativ ; neutral, negativ",
     ["bristfällig", "ofullständig", "brist"],
     "Servisen var " + B % "defekt" + " redan när den köptes.",
     "→ Latin defectus 'berövad något', till deficere 'fattas'.",
     "SAOL: 'ofullstandig; bristfallig | brist; skada, fel' -- ordet ar BADE "
     "adjektiv och substantiv, och alla tre synonymerna leder var sitt led. "
     "SO: 'behaftad med fel | brist i funktion eller utseende'. Att samma ord "
     "bar bada ordklasserna ar det HP provar.")

satt("fingervisning",
     "Försiktig antydan om hur något ligger till — en vink, inte ett besked",
     "neutral, neutral",
     ["antydan"],
     "Kvartalsrapporten gav en " + B % "fingervisning" + " om att konjunkturen vände.",
     "→ Att peka med fingret åt rätt håll utan att säga något.",
     "SAOL: 'forsiktig antydan'. SO: 'antydan'. Ordet 'forsiktig' i SAOL:s "
     "definition ar sjalva poangen -- en fingervisning ar svagare an ett "
     "besked, och det ar dar HP:s distraktorer brukar ligga.")

satt("frottera sig med",
     "Umgås med fina eller kända personer för att det ska smitta av sig på en själv",
     "neutral, lätt negativ",
     ["umgås"],
     "Han " + B % "frotterade sig med" + " intellektuella för att verka beläst.",
     "→ Franska frotter 'gnida'. Samma rot som friktion.",
     "SAOL: 'umgas av fafanga | gnida' -- 'av fafanga' ar precis nyansen som "
     "skiljer ordet fran vanligt umgange, och den finns i huvudbetydelsen. "
     "SO: 'umgas | gnida'. Grundbetydelsen 'gnida' (frottera ryggen) lever "
     "kvar men uppslagsordet ar frasen, dar bara umgangesbetydelsen galler.",
     tillat={"frammande_uppslagsord":
             "Frasuppslag: API:t slar upp varje ord for sig och returnerar 52 "
             "grannposter pa fr- (fram, fras, fritera...). Brus, inte fel.",
             "betydelse_kan_saknas":
             "SO:s andra betydelse ar 'gnida' -- grundordet frotteras "
             "bokstavliga betydelse, som INTE galler for frasen 'frottera sig "
             "med'. Frasen har en betydelse.",
             "synonym_utan_ordboksbelagg":
             "SAOL sager ordagrant 'umgas av fafanga' om just den har frasen. "
             "Belaggskontrollen missar det eftersom frasuppslaget blandat in "
             "52 andra ords definitioner i belaggsmangden."})

satt("futhark",
     "Runalfabetet — runorna uppradade i sin egen ordning, inte i A-B-C",
     "fackspråklig, neutral, historia",
     ["runalfabet", "runrad"],
     "Den äldre " + B % "futharken" + " hade tjugofyra tecken, den yngre bara sexton.",
     "→ Namnet är runraden själv: f, u, þ, a, r, k — de sex första tecknen.",
     "SAOL: 'runalfabet, runrad' -- bada synonymerna leder var sitt led. SO: "
     "'runalfabet'. Etymologin ar hela forklaringen till ordet och darfor med.")

satt("grundbult",
     "Liten detalj som allt annat vilar på — går den, rasar helheten",
     "vardaglig, neutral",
     [],
     "Pressfriheten är en av " + B % "grundbultarna" + " i ett fritt samhälle.",
     "→ Bulten som fäster en maskin i sitt fundament.",
     "SO: 'liten detalj som en mycket stor helhet ar beroende av', markt "
     "'vardagligt'. SAOL: 'av. bildl. detalj som allt annat ar beroende av'. "
     "Anvands nastan bara bildligt. Tom synonymlista: bada ordbockerna "
     "definierar med en fras, inte med ett utbytbart ord.")

satt("gäckas",
     "Retas och driva med någon ; svika en förväntning så att den inte blir uppfylld",
     "ngt ålderdomlig, neutral ; ngt ålderdomlig, lätt negativ",
     ["retas", "svika"],
     "Regissören " + B % "gäckades" + " med etablissemanget i varje scen.",
     "→ Fornsvenska gäkka. Samma rot som gäck 'narr'.",
     "SAOL: 'driva gyckel, retas, skoja | svika' -- bada synonymerna leder "
     "var sitt led i var sin betydelse. SO: 'retas | lamna (forvantning eller "
     "dylikt) ouppfylld | narra, lura', markt 'mindre brukligt'. De TVA "
     "betydelserna ar helt olika (retas mot svika) och det ar den skillnaden "
     "HP provar: 'de gackade forhoppningarna' betyder svikna, inte retade.",
     tillat={"betydelse_kan_saknas":
             "SO:s 4 poster ar 2 betydelser plus 2 JFR-taggar (bedra, svika) "
             "och en 'av. (om varelse)'-variant. Kortet tacker bada."})

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Totalt godkanda kort nu: %d" % sum(1 for k in KORT if k.get("approved")))
