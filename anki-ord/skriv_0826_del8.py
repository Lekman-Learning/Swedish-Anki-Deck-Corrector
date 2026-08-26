# -*- coding: utf-8 -*-
import json, urllib.parse

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}


def H(w):
    return '<font color="#3498db">' + w + '</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, tillat=None, conf=9):
    e = BY[o]
    q = urllib.parse.quote(o)
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": None, "exempelmening": ex, "etymologi": ety}
    e["sokkoll"] = {"kalla": "SO och SAOL via https://svenska.se/api/msearch?ord=" + q
                    + " (hämtat 2026-08-26, HTTP 200)", "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("oförmedlad",
     "Som sker tvärt, utan något som binder ihop eller förbereder",
     "formell", [],
     "Samtalet gled " + H("oförmedlat") + " över i en politisk debatt.", None,
     "SO: som överförs utan förbindande länk; äv. försvagat: utan förvarning. Ingen SAOL-artikel i "
     "träffen. Legacys abrupt är ett grannord utan belägg här — och abrupt är dessutom självt ett "
     "kort i den här batchen.")

satt("omse",
     "Ta hand om och sköta något, särskilt sår eller skador",
     "ngt ålderdomlig", [],
     "Han fick åka till sjukhus för att få sina blessyrer " + H("omsedda") + ".", None,
     "SO och SAOL identiskt: sköta om. SAOL:s exempel visar att formen numera är ovanlig: "
     "omse el. vanl. se om ngt. Sköta om är hela definitionen, inte en utbytbar synonym.",
     tillat={"register_motsager_markning":
             "Varken SO eller SAOL sätter en stilmärkning. SAOL skriver dock ut att formen är "
             "ovanlig (omse el. VANL. se om ngt), vilket är grunden för registret. Ingen "
             "ordboksmärkning motsägs."})

satt("parlör",
     "Liten ordbok med färdiga fraser för resenärer",
     "neutral", [],
     "De hade god nytta av " + H("parlören") + " på Parisrestaurangerna.", None,
     "SO: mindre två- eller flerspråkig ordbok för praktiskt bruk. SAOL: mindre turistordbok med "
     "fraser för olika situationer, samtalsordbok. Legacys fickordbok är OLD-facit men saknar "
     "ordboksbelägg — och missar att det är fraserna, inte formatet, som gör en parlör.")

satt("petition",
     "Skriftlig begäran till en myndighet, ofta med många underskrifter",
     "formell, politik", [],
     "I en " + H("petition") + " till regeringen protesterade forskarna mot beslutet.", None,
     "SO: begäran som riktas till myndighet från enskild person eller organisation; äv. utvidgat: "
     "formell begäran. SAOL: hemställan till myndighet om åtgärd. Hemställan är SAOL:s "
     "definitionsord men svårare än petition — sätts inte som synonym.")

satt("pochera",
     "Låta något sjuda försiktigt i vatten utan att det kokar",
     "fackspråklig, matlagning", [],
     "Hon serverade " + H("pocherad") + " fisk med vitvinssås.", None,
     "SO: (låta) sjuda i vätska; exempel pocherade ägg, pocherad fisk med vitvinssås. "
     "SAOL: sjuda i vätska. Legacys småkoka är OLD-facit men fångar inte att poängen är att det "
     "INTE ska koka.")

satt("pomerans",
     "Citrusfrukt som liknar apelsin men är sur och har beskt skal",
     "neutral", [],
     "Marmeladen fick sin beska av " + H("pomerans") + ".", None,
     "SO: en apelsinliknande citrusfrukt med surt fruktkött och beskt skal; äv. om motsvarande "
     "träd. SAOL: en citrusfrukt. Kortet tar SO:s fylligare definition eftersom SAOL:s inte "
     "skiljer pomerans från vilken citrusfrukt som helst.")

satt("pomologi",
     "Läran om odlade fruktträd och deras sorter",
     "fackspråklig, biologi", [],
     "Han var en av landets främsta kännare inom " + H("pomologi") + ".", None,
     "SO: vetenskapen om odlade fruktträd. SAOL: vetenskapen om odlade trädfrukter. De två skiljer "
     "sig marginellt (träden respektive frukterna); kortet nämner båda leden.")

satt("pretendent",
     "Person som gör anspråk på något, ofta en tron eller en post",
     "neutral, politik", ["tronkrävare"],
     "Efter första valomgången återstod två " + H("pretendenter") + " till presidentposten.", None,
     "SO: person som gör anspråk på något. SAOL: person som gör anspråk på ngt; tronkrävare — "
     "tronkrävare inleder andra ledet och är belagd synonym, även om den är snävare än ordet.")

satt("pulsera",
     "Slå eller strömma i jämna stötar, som blodet i takt med hjärtat",
     "neutral", [],
     "Han kände blodet " + H("pulsera") + " snabbare i ådrorna.", None,
     "SO: klappa i takt med hjärtslagen; förekomma eller ske stötvis; äv. bildligt särskilt med "
     "tanke på livfullhet. SAOL: röra sig av och an; strömma fram i vågor; regelbundet växla i "
     "styrka; sjuda. Kortets formulering täcker både den bokstavliga och den stötvisa "
     "användningen.")

satt("päll",
     "Tyghimmel som spänns upp eller bärs över något viktigt",
     "ngt ålderdomlig", ["takhimmel"],
     "Processionen gick fram under en " + H("päll") + " av rött sammet.", None,
     "SO: dukliknande anordning som är uppspänd eller bärs över viktigt föremål eller viktig "
     "person, markerat något ålderdomligt; äv. bildligt (under himlens päll). SAOL: himmel; "
     "takhimmel — takhimmel inleder andra ledet och är belagd. Himmel utelämnas, det är "
     "tvetydigt mot väderleken.")

satt("renässans",
     "Ny blomstring efter en nedgång ; den europeiska kulturepok som återupplivade antikens ideal",
     "neutral, historia", ["pånyttfödelse"],
     "Folkmusiken upplevde en " + H("renässans") + " på 1960-talet.",
     "av franskans renaissance, återfödelse",
     "SO: (tillstånd av) förnyelse och fruktbar aktivitet; en kulturrörelse som försökte "
     "återuppliva antikens ideal, äv. om motsvarande historiska epok. SAOL: den stora "
     "kulturströmningen vid medeltidens slut; pånyttfödelse; ny glansperiod — pånyttfödelse "
     "inleder ett eget led och är belagd synonym.")

satt("riksha (rickshaw)",
     "Tvåhjulig kärra för passagerare som dras av en människa",
     "neutral", [],
     "De tog en " + H("riksha") + " genom de trånga gränderna.",
     "av japanskans jin-riki-sha: människa, kraft, fordon",
     "SO: tvåhjulig personkärra som dras av människa; numera ibland om en trehjulig cykelvariant. "
     "SAOL: tvåhjulig dragkärra el. trehjulig cykel för persontransport bl.a. i Östasien. "
     "🔴 VIKTIGT: uppslaget drog in RIKSDAG (folkrepresentation i ett land; polsk riksdag = stormig "
     "och resultatlös sammankomst) — ett helt annat ord som är uteslutet ur kortet. Etymologin tas "
     "med eftersom den gör ordet självförklarande.",
     tillat={"frammande_uppslagsord":
             "Fuzzy-matchningen drog in riksdag och rikssamtal — andra ord som råkar dela "
             "bokstavsföljd. Ingen glosa på kortet kommer därifrån; det står utskrivet i sökkollen.",
             "betydelse_kan_saknas":
             "SO:s extraposter tillhör riksdag (se ovan) plus markören om trehjuliga cykelvarianter. "
             "Rikshans enda betydelse — dragkärra för passagerare — finns på kortet."})

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 8 skriven: 12 kort. Totalt approved: %d/%d"
      % (sum(1 for e in S if e.get("approved")), len(S)))
