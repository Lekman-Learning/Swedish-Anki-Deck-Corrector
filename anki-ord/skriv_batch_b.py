# -*- coding: utf-8 -*-
"""Batch B (kort 20-27) i 100-kortsomgangen 2026-08-30. Samma synonympolicy
som skriv_batch_a.py -- se dess dokstrang, den ar normen for hela omgangen.
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

P["passionerad"] = dict(
    hb="Driven av starka känslor",
    reg="neutral, positiv",
    grupper=[["lidelsefull", "intensiv"]],
    ex="Hennes älskare var av en %s natur och skrev henne kärleksbrev varje dag." % (B % "passionerad"),
    etym=None,
    notis="'lidelsefull' står i SO:s jfr-lista med JFR:cohyponym, MEN också i "
          "SAOL:s egen definition ('lidelsefullt engagerad') och i Wiktionarys "
          "definition -- alltså attesterat. 'intensiv' likaså (Wiktionary). "
          "'glödande' struket, bara synonymer.se. Registret ändrat från "
          "'litterär': ingen källa märker ordet som litterärt.")

P["permanent"] = dict(
    hb="Gjord för att bestå ; behandling som gör håret lockigt länge",
    reg="neutral, neutral ; vardaglig, neutral",
    grupper=[["beständig", "varaktig"], []],
    ex="Efter flera års pendlande skaffade familjen sig äntligen en %s bostad." % (B % "permanent"),
    etym="till latin permanere 'bestå, vara ihållande'",
    notis="Kortet hade EN betydelse; både SAOL och SO har hårbehandlingen som "
          "egen betydelse (dold_betydelse). 'beständig' står i SAOL:s "
          "definition, 'varaktig' i Wiktionarys. 'stadigvarande' används inte "
          "-- det står bara i SO:s jfr-lista, som bär JFR:cohyponym. "
          "Hårbetydelsen får ingen synonym; ingen finns belagd.")

P["ravin"] = dict(
    hb="Djup och smal sänka med branta väggar",
    reg="neutral, neutral, geologi",
    grupper=[["klyfta", "dalsänka"]],
    ex="Vandrarna klättrade försiktigt ner i den uttorkade %s." % (B % "ravinen"),
    etym="av franska ravin 'grop, hålväg'; till latin rapere 'föra bort'",
    notis="'kanjon' STRUKET -- SO markerar det uttryckligen som JFR:cohyponym, "
          "alltså en jämförbar men annan landform, precis den felsort som "
          "fällde esplanad. 'klyfta' och 'dalsänka' står båda i SAOL:s egen "
          "definition ('smal, djup dalsänka, klyfta').")

P["reträtt"] = dict(
    hb="Att dra sig tillbaka från strid eller ståndpunkt ; plats dit man drar sig undan",
    reg="formell, neutral, militär ; neutral, neutral",
    grupper=[["återtåg"], ["tillflyktsort"]],
    ex="Efter det oväntade bakhållet tvingades trupperna slå till %s." % (B % "reträtt"),
    etym="av franska retraite, till latin retrahere 'dra tillbaka'",
    notis="SAOL har båda betydelserna ('återtåg; tillflyktsort'), kortet hade "
          "en och blandade in båda ordens synonymer i samma grupp. 'flykt' "
          "struket: en reträtt är ordnad, en flykt är det inte -- de är inte "
          "utbytbara, och SO listar flykt under jfr med JFR:cohyponym.")

P["saldo"] = dict(
    hb="Det som finns kvar på ett konto när allt räknats ihop",
    reg="neutral, neutral, ekonomi",
    grupper=[["behållning", "tillgodohavande"]],
    ex="Efter lönen kom in hade han äntligen ett positivt %s på kontot." % (B % "saldo"),
    etym="av italienska saldo 'vad som återstår att betala'; av latin solidus 'fast'",
    notis="'balans' struket -- ordet betyder för många andra saker för att "
          "fungera som ensamt igenkänningsord på ett kort. 'behållning' står i "
          "Wiktionarys definition, 'tillgodohavande' i synonymer.se:s "
          "redaktionella lista.")

P["simpel"] = dict(
    hb="Mycket enkel och torftig ; som saknar heder och moral",
    reg="vardaglig, neutral ; vardaglig, nedsättande",
    grupper=[["enkel", "torftig"], ["tarvlig", "gemen"]],
    ex="Familjen bodde i en %s koja utan bekvämligheter." % (B % "simpel"),
    etym="fornsvenska simpel; via franska av latin simplex 'enkel'",
    notis="Kortet hade båda betydelserna men lade deras synonymer i EN grupp, "
          "så 'enkel' och 'tarvlig' såg ut att betyda samma sak "
          "(old_har_fler_betydelser). SAOL definierar 'enkel; tarvlig', "
          "Wiktionary 'tarvlig, torftig, låg'. 'nedrig' används inte -- SO:s "
          "jfr-lista, JFR:cohyponym.")

P["småsinnad"] = dict(
    hb="Som fastnar i petitesser och inte unnar andra något",
    reg="neutral, nedsättande",
    grupper=[["inskränkt", "självisk"]],
    ex="Ivan var %s och ville bara cykla till Thailand istället för hela vägen." % (B % "småsinnad"),
    etym=None,
    notis="SAOL:s enda definition är 'småsint' -- den kan inte användas som "
          "synonym, den delar ordstam med uppslagsordet och skulle trippa "
          "cirkular_synonym. Samma sak med kortets gamla 'småaktig'. "
          "Wiktionarys definition ('inskränkt och självisk') är den enda källa "
          "som ger utbytbara ord. Skämtet i exempelmeningen behållet med flit.")

P["stranda"] = dict(
    hb="Köra fast med ett fartyg på grund ; (bildligt) misslyckas och gå om intet",
    reg="neutral, neutral, sjöfart ; neutral, negativ",
    grupper=[["gå på grund"], ["misslyckas"]],
    ex="Förhandlingarna %s på grund av oenighet om budgeten." % (B % "strandade"),
    etym=None,
    notis="Kortet hade rätt betydelser men lade båda betydelsernas synonymer i "
          "EN platt lista, så 'gå på grund' och 'misslyckas' såg ut att höra "
          "ihop. Nu en grupp per betydelse. 'rinna ut i sanden' struket: det "
          "är ett idiom med egen bildlighet, inte ett utbytbart ord.")

PAUSA = {
    "plektrum": (
        "Ingen belagd synonym finns. SAOL och SO definierar båda ordet "
        "omskrivande ('liten skiva som strängarna slås an med') utan att ge "
        "något synonymord, synonymer.se har ingen artikel alls, och "
        "Wiktionary ger bara samma omskrivning. Kortets gamla 'skiva' är "
        "ordets överbegrepp, 'plock' går inte att belägga någonstans, och "
        "'plektron' är samma ord i annan form (samma grekiska plektron) -- "
        "alltså cirkulärt, inte en synonym. Kräver Adams beslut i samma fråga "
        "som diaspora och språkförbistring: får ett kort stå helt utan "
        "synonym?"),
}
TAGG = "v3_pausad::ingen_belagd_synonym"


def kallor(o):
    u = json.load(io.open("uppslag/%s.json" % o, encoding="utf-8"))
    return " ".join(u["urler"][k] for k in sorted(u["urler"]))


def main():
    d = json.load(io.open(F, encoding="utf-8"))
    n_s = n_p = 0
    for p in d:
        o = p["ord"]
        if o in PAUSA:
            p["approved"] = False
            p["pausad"] = True
            p["paus_tagg"] = TAGG
            p["sokkoll"] = {"kalla": kallor(o), "slutsats": PAUSA[o]}
            n_p += 1
        elif o in P:
            f = P[o]
            p["proposed"] = {
                "huvudbetydelse": f["hb"],
                "register": f["reg"],
                "synonym_groups": f["grupper"],
                "synonymer": [s for g in f["grupper"] for s in g],
                "exempelmening": f["ex"],
                "etymologi": f.get("etym"),
            }
            p["sokkoll"] = {"kalla": kallor(o),
                            "slutsats": POLICY + " " + f["notis"]}
            p["approved"] = True
            n_s += 1
    json.dump(d, io.open(F, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("skrivna: %d   pausade: %d" % (n_s, n_p))


main()
