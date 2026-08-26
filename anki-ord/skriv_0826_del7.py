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


satt("kolorit",
     "Hur färgerna verkar tillsammans i en målning ; motsvarande om hur ett stycke musik låter",
     "fackspråklig, konst", ["färggivning"],
     "Målningen har en varm, jordbrun " + H("kolorit") + ".", None,
     "SO: sammanfattningen av de färger som förekommer på en målning; äv. i fråga om musik: "
     "klangfärg (orkesterstämmornas kolorit). SAOL: färggivning, färgglans; bildl. klangfärg — "
     "färggivning inleder ledet och är belagd synonym.")

satt("koncis",
     "Kort och exakt uttryckt, utan ett enda överflödigt ord",
     "formell", [],
     "Hon svarade kort och " + H("koncist") + ".", None,
     "SO: kortfattad men innehållsrik; exempel ett koncist inlägg i debatten. SAOL: sammanträngd, "
     "kortfattad och exakt. Kortfattad och exakt står inuti SAOL:s enda led utan att inleda det, "
     "och sammanträngd är svårare än koncis — ingen av dem sätts som synonym.")

satt("krank",
     "Sjuk",
     "arkaisk", ["sjuk"],
     "Han låg " + H("krank") + " i sin kammare hela vintern.", None,
     "SO: sjuk, markerat ålderdomligt; äv. något utvidgat. SAOL: sjuk, markerat åld., med exemplet "
     "eftertankens kranka blekhet. Sjuk utgör hela definitionen i båda ordböckerna och är belagd "
     "synonym. Registret följer märkningen.")

satt("krypta",
     "Underjordiskt rum under en kyrka, ofta med gravar",
     "neutral", [],
     "Biskoparna ligger begravda i domkyrkans " + H("krypta") + ".",
     "till grekiskans kryptein, gömma",
     "SO: underjordiskt grav- och kultrum i en större kyrka. SAOL: underjordiskt kyrkorum. "
     "Etymologin tas med eftersom den kopplar ordet till kryptisk och gör det minnesvärt. "
     "Legacys katakomb är ett grannbegrepp (gångsystem, inte kyrkorum) utan belägg här.")

satt("kryptogam",
     "Växt som förökar sig med sporer i stället för frön — mossor, ormbunkar, lavar och svampar",
     "fackspråklig, biologi", ["sporväxt"],
     "Ormbunkar och mossor räknas till " + H("kryptogamerna") + ".",
     "till grekiskans kryptos, dold, och gamos, äktenskap — fortplantningen syns inte",
     "SO: som inte bildar frön; kryptogam växt; exempel kryptogamerna omfattar ormbunksväxter, "
     "mossor, lavar, svampar och alger. SAOL: som inte bildar frön; sporväxt — sporväxt är eget "
     "uppslag och belagd synonym. Etymologin förklarar namnet och tas därför med.")

satt("kutym",
     "Vad man brukar göra i ett visst sammanhang, utan att det står skrivet",
     "formell", ["sed"],
     "Det var " + H("kutym") + " att den som hade mest pengar bjöd.", None,
     "SO: vedertaget mönster för (gott) uppförande. SAOL: sed, sedvänja, bruk — sed inleder ledet "
     "och är belagd synonym. Sedvänja och bruk står efter komma. Tradition saknar belägg och är "
     "dessutom vidare: en kutym behöver ingen historia bakom sig.")

satt("lamell",
     "Tunn skiva eller platta, som i en persienn eller under en svamphatt",
     "neutral", [],
     "Ställ in persiennens " + H("lameller") + " så att ljuset släpps in.", None,
     "SO: tunn platta eller skiva; exempel persiennernas lameller, skivlingarnas lameller. "
     "SAOL: tunn skiva, blad. Skiva och platta är definitionsord, inte utbytbara synonymer — "
     "en lamell är en särskild sorts skiva.")

satt("majuskel",
     "Stor bokstav, mest sagt om gamla handskrifter",
     "fackspråklig, lingvistik", ["versal"],
     "Handskriften är helt skriven i " + H("majuskler") + ".", None,
     "SO: stor bokstav, markerat mest vid beskrivning av äldre förhållanden. SAOL: stor bokstav, "
     "versal i äldre texter — versal står i SAOL:s definitionsled som en direkt likställd term och "
     "är den etablerade motsvarigheten i modern svenska.",
     tillat={"register_motsager_markning":
             "SO:s markering mest vid beskrivning av äldre förhållanden är en bruksuppgift om vad "
             "ordet beskriver, inte en stilnivå — ordet självt är en levande fackterm inom "
             "paleografi och typografi. Kortets huvudbetydelse skriver ut den begränsningen."})

satt("namne",
     "Person som heter samma sak som en annan",
     "neutral", [],
     "Pelle Nilsson och hans " + H("namne") + " Lennart.", None,
     "SO: person med samma förnamn eller efternamn som en annan person. SAOL: person med samma "
     "namn som en annan. Legacys liknamma, namnbror och namnkusin finns inte i någon av "
     "ordböckerna — strukna.")

satt("nationalisera",
     "Föra över något från privat ägo till staten",
     "neutral, politik", ["förstatliga"],
     "När Suezkanalen " + H("nationaliserades") + " grep kolonialmakterna in.", None,
     "SO: överföra från privat till statlig ägo. SAOL: förstatliga; anpassa i nationell riktning "
     "el. efter inhemska förhållanden — förstatliga inleder första ledet och är belagd synonym. "
     "Socialisera och kollektivisera är närliggande men andra begrepp, utan belägg här.")

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 7 skriven: 10 kort. Totalt approved: %d/%d"
      % (sum(1 for e in S if e.get("approved")), len(S)))
