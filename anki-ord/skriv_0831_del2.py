# -*- coding: utf-8 -*-
"""Batch 2026-08-31. Del 2: kort 7-14, plus rattelser av del 1.

Rattelserna kommer ur forgranskningen av del 1:

  molla   synonym_utan_ordboksbelagg pa vaderkvarn. SAOL:s "vader- el.
          vattenkvarn" ar en sammandragen uppraekning, inte tva ledinledande
          glosor -- alltsa belagger den varken vaderkvarn eller vattenkvarn.
          Kvar star kvarn, som ar hela SO:s definition.
  stor    doman biologi utan markning i SO/SAOL. Struken.
  stigma  tre domaner utan markning. Strukna. betydelse_kan_saknas kvarstar
          medvetet: SO:s tva extra poster ar UB till de tre skrivna.
  docent  doman utbildning utan markning. Struken.
"""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-31_v3-batch40.json"
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


# ============================================ RATTELSER AV DEL 1
BY["mölla"]["proposed"]["synonymer"] = ["kvarn"]
BY["mölla"]["sokkoll"]["slutsats"] += (" RATTAT efter forgranskning: vaderkvarn "
    "och vattenkvarn strukna. SAOL:s 'vader- el. vattenkvarn' ar en "
    "sammandragen uppraekning dar ingetdera ordet inleder ett eget led.")
BY["docent"]["proposed"]["register"] = "formell, neutral"
BY["stör"]["proposed"]["register"] = "neutral, neutral ; neutral, neutral"
BY["stigma"]["proposed"]["register"] = ("formell, neutral ; fackspråklig, "
                                        "neutral ; neutral, negativ")

# ------------------------------------------------------------ 7. forsavida
satt("försåvida",
     "Under förutsättning att; om det är så att",
     "högtidlig, neutral",
     ["försåvitt"],
     "Vi åker på lördag, " + B % "försåvida" + " vädret tillåter det.",
     "sammanskrivning av för så vida; jämför den vanligare formen försåvitt "
     "och det enkla såvida",
     "Bade SO och SAOL har forsavida som eget uppslagsord och hanvisar rakt "
     "till forsavitt, som alltsa ar samma ord i en annan stavning och darmed "
     "utbytbart at bada hallen. SO markerar 'nagot hogtidligt'. Betydelsen ar "
     "villkorsinledande, vilket SO:s hanvisning bekraftar.")

# ---------------------------------------------------------------- 8. agna
satt("agna",
     "Sätta fast bete på en fiskekrok eller ett annat fiskeredskap",
     "neutral, neutral",
     [],
     "Vi " + B % "agnade" + " krokarna med maskar innan vi rodde ut.",
     "till agn 'bete', av fornsvenskans agn; besläktat med isländskans agn "
     "i samma betydelse",
     "SO: 'forse (fiskredskap) med agn'. SAOL: 'forse med agn; satta agn pa "
     "krok'. EN betydelse. Det gamla kortets andra betydelse, 'de tunna "
     "torra skal som omsluter kornen', hor till substantivet agn/agnar och "
     "ar en annan homograf -- den star inte under agna i nagon av "
     "ordbockerna och stryks (regel 1 gar bada hallen: sla inte ihop, men "
     "hitta inte heller pa en betydelse ordboken lagger nagon annanstans). "
     "Synonymer: syn.se ger beta och angla, ingen av dem i en "
     "ordboksdefinition. Tom lista.")

# --------------------------------------------------------------- 9. kolugn
satt("kolugn",
     "Fullkomligt lugn, utan minsta tecken på oro",
     "vardaglig, positiv",
     [],
     "Hon var " + B % "kolugn" + " trots att hela salen tittade på henne.",
     "förstärkande sammansättning av ko och lugn, efter föreställningen om "
     "kon som ett oberört djur; samma förstärkningsmönster som i koklok",
     "SO och SAOL ger bada exakt 'fullkomligt lugn'. En betydelse. INGEN "
     "synonym: lugn star i definitionen men inleder inte ett eget led -- det "
     "ar modifierat av fullkomligt, och bara hela frasen ar utbytbar. Samma "
     "provning som falide farsot for pandemi. syn.se:s oberord, iskall och "
     "ataraxi saknar ordboksbelagg.")

# -------------------------------------------------------------- 10. vilsam
satt("vilsam",
     "Som ger vila och känsla av lugn",
     "neutral, positiv",
     [],
     "Rummet var inrett i " + B % "vilsamma" + " färger.",
     "till vila, med adjektivändelsen -sam som i fredsam och verksam",
     "SO: 'som medfor vila'. SAOL: 'som ger vila'. En betydelse. Ingen "
     "synonym ar belagd: bada definitionerna ar omskrivningar med relativsats, "
     "inte utbytbara glosor. syn.se:s rofylld, skon och behaglig star inte i "
     "nagon ordboksdefinition.")

# -------------------------------------------------------------- 11. inhysa
satt("inhysa",
     "Ge tillfällig bostad åt någon; även om att förvara föremål någonstans",
     "formell, neutral",
     [],
     "De nyanlända " + B % "inhystes" + " i baracker utanför staden.",
     "av in och hysa 'ge husrum'; hysa går tillbaka på fornsvenskans hysa, "
     "till hus",
     "SO: 'ge tillfallig bostad at', med underbetydelsen 'av. med avseende pa "
     "foremal eller dylikt'. SAOL: 'ge husrum at'. UB:n foljer med i samma "
     "betydelse (regel 1 galler betydelser, inte underbetydelser). Inga "
     "belagda synonymer: bada definitionerna ar flerordsfraser dar inget "
     "enskilt ord inleder ett utbytbart led.")

# ------------------------------------------------------------ 12. dagtinga
satt("dagtinga",
     "Göra ovärdiga eftergifter, särskilt mot sina egna principer ; förhandla "
     "med en motpart i syfte att underkasta sig",
     "högtidlig, negativ ; ålderdomlig, neutral",
     ["kompromissa", "köpslå"],
     "Han vägrade " + B % "dagtinga" + " med sitt samvete.",
     "av lågtyskans dagedingen 'sätta ut en dag för förhandling', till dag "
     "och ting i betydelsen 'rättsmöte'",
     "SO haller isar tva betydelser: 'gora (ovardiga) eftergifter' och "
     "'forhandla (med nagon) i syfte att underkasta sig'. Bada skrivs ut "
     "(regel 1). SO markerar 'nagot hogtidligt' och 'nagot alderdomligt'. "
     "SAOL:s hela definition ar 'kopsla, kompromissa' -- bada orden inleder "
     "sitt led och ar utbytbara i forsta betydelsen. Andra betydelsen har "
     "ingen belagd synonym.",
     grupper=[["kompromissa", "köpslå"], []])

# ----------------------------------------------------------- 13. lavinartad
satt("lavinartad",
     "Som sker mycket snabbt och okontrollerat, som en lavin",
     "neutral, neutral",
     [],
     "Stadens " + B % "lavinartade" + " tillväxt tog kommunen på sängen.",
     "till lavin, av schweizertyskans Lawine, ytterst av latinets labi "
     "'glida, falla'; efterledet -artad betyder 'av det slaget'",
     "SO: 'som sker snabbt och okontrollerat'. SAOL: 'kraftig, snabb'. En "
     "betydelse. INGEN synonym skrivs trots att SAOL:s tva ord bada inleder "
     "sitt led: varken kraftig eller snabb ar utbytbart at bada hallen, "
     "eftersom bada tappar det okontrollerade som SO gor till definitionens "
     "karna. En snabb okning ar inte samma sak som en lavinartad.")

# ------------------------------------------------------------ 14. klientel
satt("klientel",
     "Sammanfattningen av en viss persons eller verksamhets klienter, alltså "
     "kundkretsen ; nedsättande om en grupp mer eller mindre utslagna personer",
     "formell, neutral ; vardaglig, negativ",
     ["kundkrets"],
     "Advokatbyrån har byggt upp ett troget " + B % "klientel" + ".",
     "av latinets clientela 'skyddslingar', till cliens 'skyddsling'; i Rom "
     "de fria män som stod under en förnäm mans beskydd",
     "SO: 'sammanfattningen av (viss persons) klienter', med underbetydelsen "
     "'ofta nedsattande, sarsk. om grupp av mer el. mindre utslagna "
     "personer'. SAOL delar upp samma sak i tva: 'kundkrets t.ex. hos "
     "advokat' och 'grupp av utslagna personer', den senare markt vard. "
     "Eftersom SAOL haller isar dem skrivs de som tva betydelser (regel 1). "
     "Synonymen kundkrets inleder SAOL:s forsta definition och hor bara till "
     "den gruppen.",
     grupper=[["kundkrets"], []])


json.dump(KORT, io.open(FIL, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
skrivna = sum(1 for k in KORT if k.get("proposed"))
pausade = sum(1 for k in KORT if k.get("v3_pausad"))
print("del 2 klar: %d skrivna, %d pausade, %d kvar av 40"
      % (skrivna, pausade, 40 - skrivna - pausade))
