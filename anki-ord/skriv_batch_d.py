# -*- coding: utf-8 -*-
"""Batch D (kort 41-52). Samma synonympolicy som skriv_batch_a.py.

NYTT HAR: kort som pausas far anda sitt `proposed` ifyllt. Tidigare pausade
jag genom att lamna proposed tomt, vilket kastade bort ratningen av
huvudbetydelse och register -- den enda oppna fragan pa de korten ar
synonymen. Nu ligger arbetet kvar och slapps i samma stund Adam svarar pa
fragan "far ett kort sta helt utan synonym?".
"""
import io
import json

F = "sessions/session_2026-08-30_v3-omgranskning-repetition-mognad.json"
B = '<font color="#3498db">%s</font>'
POLICY = (
    "Betydelser, register och etymologi lästa ur SO/SAOL. Synonympolicy: "
    "SAOL/SO/Wiktionarys definitionstext först, synonymer.se:s redaktionella "
    "lista i andra hand, ALDRIG ett ord som bara står i SO:s jfr-lista när "
    "JFR:cohyponym är satt. Tom grupp hellre än gissning.")

P = {}

P["fortskaffningsmedel"] = dict(
    hb="Något man förflyttar sig med",
    reg="formell, neutral",
    grupper=[["transportmedel", "färdmedel"]],
    ex="Cykeln är ett hälsosamt %s." % (B % "fortskaffningsmedel"),
    etym=None,
    notis="Båda synonymerna ÄR SAOL:s definition ('transportmedel, "
          "färdmedel'). 'fordon' struket: ett fordon är en sorts "
          "fortskaffningsmedel, men en häst är också ett -- alltså kohyponym, "
          "inte utbytbart.")

P["grunda sig på"] = dict(
    hb="Ha något som underlag för ett resonemang",
    reg="neutral, neutral",
    grupper=[["bygga på"]],
    ex="Hennes slutsatser %s omfattande forskning." % (B % "grundar sig på"),
    etym=None,
    notis="VARNING: SO-artikeln i uppslagningen är FEL ORD -- den handlar om "
          "ackord (samklang av toner, överenskommelse med långivare, "
          "etymologi 'av franska accord'). Flerordsfällan igen. Hela "
          "SO-blocket, inklusive dess jfr-lista ('basera 1'), är därför "
          "bortsett från. Betydelsen vilar på SAOL ('ha som utgångspunkt; "
          "motiveras'), synonymen på synonymer.se ('bygga').")

P["grädda"] = dict(
    hb="Tillaga i ugn eller stekpanna så ytan bryns ; (i bestämd form) det finaste skiktet i samhället",
    reg="neutral, neutral, matlagning ; vardaglig, neutral",
    grupper=[["ugnsbaka"], ["eliten"]],
    ex="Varje söndag brukade pappa %s pannkakor till hela familjen." % (B % "grädda"),
    etym="fornsvenska grädda, speciellt svenskt ord",
    notis="CIRKULÄR SYNONYM RÄTTAD: kortet hade 'gräddan/eliten' som synonym "
          "till grädda -- samma ord. 'baka' används inte: SO markerar 'baka 2' "
          "JFR:cohyponym och ordet står inte i någon definitionstext. "
          "'ugnsbaka' kommer från synonymer.se:s redaktionella lista, 'eliten' "
          "från Wiktionarys definition av den bestämda formen.")

P["hamn"] = dict(
    hb="Skyddad plats där fartyg lägger till ; (ålderdomligt) yttre gestalt",
    reg="neutral, neutral, sjöfart ; ngt ålderdomlig, neutral",
    grupper=[["tilläggsplats"], ["skepnad", "gestalt"]],
    ex="Staden hade en isfri %s året runt." % (B % "hamn"),
    etym="fornsvenska hamn, gemensamt germanskt ord, ursprungligen 'behållare'",
    notis="CIRKULÄR SYNONYM RÄTTAD: 'hamnplats' innehåller uppslagsordet. "
          "'kaj' struket -- en kaj är en DEL av en hamn, inte samma sak. "
          "'skepnad' och 'gestalt' är SAOL:s egen definition av betydelse 2 "
          "('yttre gestalt, skepnad'). 'vålnad' struket ur synonymraden: det "
          "är en tredje, ännu snävare betydelse och hör inte ihop med "
          "skepnad.")

P["kibbutz"] = dict(
    hb="Israelisk gård där en grupp bor och arbetar tillsammans",
    reg="neutral, neutral",
    grupper=[["kollektivjordbruk", "jordbrukskollektiv"]],
    ex="Flera nya %s anlades i gränstrakterna." % (B % "kibbutzer"),
    etym="av hebreiska qibbutz, egentligen 'samling, gemenskap'",
    notis="Båda synonymerna är källornas egna definitioner: SO skriver "
          "'israeliskt kollektivjordbruk', SAOL 'israeliskt "
          "jordbrukskollektiv'. Huvudbetydelsen omskriven så att den inte "
          "innehåller synonymorden.")

P["mixtur"] = dict(
    hb="Läkemedel i flytande form ; en stämma på en orgel",
    reg="neutral, neutral, medicin ; fackspråklig, neutral, musik",
    grupper=[["läkemedelsblandning"], ["orgelstämma"]],
    ex="Barnet fick medicinen som %s istället för tablett." % (B % "mixtur"),
    etym="av latin mixtura 'blandning', till miscere 'blanda'",
    notis="Kortet hade EN betydelse; både SAOL och SO har orgelstämman som "
          "egen betydelse. 'preparat' struket -- alldeles för brett, en "
          "tablett är också ett preparat. Synonymerna är källornas egna "
          "definitionsord.")

P["respons"] = dict(
    hb="Det man får tillbaka när något påverkar utifrån",
    reg="neutral, neutral, psykologi",
    grupper=[["gensvar", "reaktion"]],
    ex="Behavioristerna beskrev beteende med hjälp av stimulus och %s." % (B % "respons"),
    etym="av engelska response; till latin respondere 'svara'",
    notis="'gensvar' står i både SAOL:s och SO:s definition, 'reaktion' i "
          "SO:s. 'svar' struket som eget led: SO listar det under jfr med "
          "JFR:cohyponym, och ett svar på en fråga är inte en respons i "
          "ordets fackbetydelse. 'stimulus' är ordets MOTPART, inte synonym.")

P["språksam"] = dict(
    hb="Som gärna tar till orda och håller igång ett samtal",
    reg="neutral, neutral",
    grupper=[["pratsam"]],
    ex="Hennes bordskavaljer var inte särskilt %s under middagen." % (B % "språksam"),
    etym=None,
    notis="SO markerar sina två jfr-ord olika: ett med SYN:synonym, ett med "
          "JFR:cohyponym, i samma ordning som listan (pratsam, talför). "
          "'talför' är alltså den kohyponyma och är struken -- den som är "
          "talför talar mycket, den som är språksam tycker om att samtala.")

P["utvikning"] = dict(
    hb="Det att vika ut sig naken i en tidning ; avstickare från det man egentligen talar om",
    reg="vardaglig, neutral ; formell, neutral",
    grupper=[[], ["exkurs", "digression"]],
    ex="Efter en lång %s återgick han till föreläsningens ämne." % (B % "utvikning"),
    etym=None,
    notis="CIRKULÄR SYNONYM RÄTTAD: 'utvikningsbild' innehåller uppslagsordet. "
          "'exkurs' står i SO:s jfr-lista men med JFR:jämför, INTE "
          "JFR:cohyponym -- alltså tillåtet. 'digression' kommer från "
          "synonymer.se:s redaktionella lista. 'sidospår' struket: det används "
          "om hela skeenden, inte om en avvikelse i ett resonemang.")

# --- Pausas for synonymfragan, men proposed skrivs anda ---
P_PAUSAD = {}

P_PAUSAD["mycel"] = dict(
    hb="Svampens nätverk av trådar under jorden",
    reg="formell, neutral, biologi",
    grupper=[[]],
    ex="%s sprider sig genom jorden och försörjer svampen med näring." % (B % "Mycelet"),
    etym="till grekiska mykes 'svamp'",
    notis="Ingen icke-cirkulär synonym finns. SO:s hela definition är ordet "
          "'mycelium' -- samma ord i latinsk form. SAOL och Wiktionary skriver "
          "båda omskrivningar ('näringsupptagande nätverksliknande del av "
          "svamp'), synonymer.se har ingen artikel. Kortets gamla 'hyfnätverk' "
          "går inte att belägga i någon källa. Huvudbetydelse och register är "
          "färdigrättade -- bara synonymfrågan är öppen.")

P_PAUSAD["prisma"] = dict(
    hb="Genomskinlig kropp med raka sidor som bryter ljus",
    reg="formell, neutral, fysik",
    grupper=[[]],
    ex="Spektroskopet använde ett %s för att dela upp ljuset." % (B % "prisma"),
    etym="av grekiska prisma 'det söndersågade'",
    notis="CIRKULÄR SYNONYM: kortets 'glasprisma' innehåller uppslagsordet "
          "(redan flaggat). Inget användbart alternativ finns: 'lins' och "
          "'objektiv' är andra optiska komponenter (kohyponymer), 'polyeder' "
          "och 'parallellepiped' är andra geometriska kroppar, och "
          "'ljusbrytande kropp' är definitionen. Huvudbetydelsen är rättad -- "
          "bara synonymfrågan är öppen.")

P_PAUSAD["på kuppen"] = dict(
    hb="Som en plötslig och oväntad följd av något annat",
    reg="vardaglig, neutral",
    grupper=[[]],
    ex="Han fixade grannens bil och fick en gratis biltvätt %s." % (B % "på kuppen"),
    etym="av franska coup 'hugg, slag'",
    notis="HUVUDBETYDELSEN VAR FEL: kortet sa 'som en extra bonus, utan "
          "ytterligare ansträngning', men SO:s definition är 'som en plötslig "
          "och oväntad följd' -- det oväntade är kärnan, inte att det är en "
          "bonus. Följden kan lika gärna vara dålig. Rättat. Synonymen kvar "
          "öppen: kortets '≈ på köpet' går inte att belägga (synonymer.se har "
          "ingen artikel för uttrycket, Wiktionary ger 'på grund därav').")

TAGG = "v3_pausad::ingen_belagd_synonym"


def kallor(o):
    u = json.load(io.open("uppslag/%s.json" % o, encoding="utf-8"))
    return " ".join(u["urler"][k] for k in sorted(u["urler"]))


def bygg(f):
    return {
        "huvudbetydelse": f["hb"],
        "register": f["reg"],
        "synonym_groups": f["grupper"],
        "synonymer": [s for g in f["grupper"] for s in g],
        "exempelmening": f["ex"],
        "etymologi": f.get("etym"),
    }


def main():
    d = json.load(io.open(F, encoding="utf-8"))
    n_s = n_p = 0
    for p in d:
        o = p["ord"]
        if o in P_PAUSAD:
            f = P_PAUSAD[o]
            p["proposed"] = bygg(f)
            p["sokkoll"] = {"kalla": kallor(o),
                            "slutsats": POLICY + " PAUSAT: " + f["notis"]}
            p["approved"] = False
            p["pausad"] = True
            p["paus_tagg"] = TAGG
            n_p += 1
        elif o in P:
            f = P[o]
            p["proposed"] = bygg(f)
            p["sokkoll"] = {"kalla": kallor(o),
                            "slutsats": POLICY + " " + f["notis"]}
            p["approved"] = True
            n_s += 1
    json.dump(d, io.open(F, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("skrivna: %d   pausade (med proposed): %d" % (n_s, n_p))


main()
