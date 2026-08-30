# -*- coding: utf-8 -*-
"""Batch E (kort 53-64). Samma synonympolicy som skriv_batch_a.py."""
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

P["absorbera"] = dict(
    hb="Suga upp något ; helt uppta någons intresse",
    reg="neutral, neutral, kemi ; neutral, neutral",
    grupper=[["uppsuga", "uppta"], ["uppsluka"]],
    ex="Växternas rötter kan %s näringsämnen från jorden." % (B % "absorbera"),
    etym="av latin absorbere 'uppsluka, uppsuga'",
    notis="Kortet hade en betydelse; både SAOL ('helt lägga beslag på intresse "
          "el. krafter') och SO ('helt uppta intresset hos') har den bildliga "
          "som egen. 'uppsuga' och 'uppta' står i SAOL:s definition, "
          "'uppsluka' i Wiktionarys.")

P["ackord"] = dict(
    hb="Samklang av flera toner ; lön efter hur mycket man hinner ; uppgörelse med långivare om nedskriven skuld",
    reg="neutral, neutral, musik ; neutral, neutral, ekonomi ; formell, neutral, ekonomi",
    grupper=[["samklang"], ["prestationslön", "beting"], ["ekonomisk uppgörelse"]],
    ex="Pianisten slog ett vackert %s." % (B % "ackord"),
    etym="av franska accord 'överensstämmelse'; till latin cor 'hjärta'",
    notis="Kortet hade alla tre betydelserna men lade deras synonymer i EN "
          "platt lista, så 'harmoni' och 'prestationslön' såg ut att höra ihop. "
          "'harmoni' dessutom struket: SO markerar det JFR:cohyponym och SAOL:s "
          "definition är bara 'samklang'. Övriga synonymer står i SAOL:s "
          "definitionstext eller synonymer.se:s redaktionella lista.")

P["amfibie"] = dict(
    hb="Djur som lever både på land och i vatten ; farkost som går både på land och i vatten",
    reg="neutral, neutral, biologi ; neutral, neutral, teknik",
    grupper=[["groddjur"], []],
    ex="Jättesalamandern är en av världens största %s." % (B % "amfibier"),
    etym="till grekiska amfi- 'på två sätt' och bios 'liv'",
    notis="Kortet hade bara djurbetydelsen; både SAOL ('konstruerad för el. "
          "gällande både vatten och land') och SO ('farkost som kan framföras "
          "både till lands och till sjöss') har fordonet som egen betydelse. "
          "'groddjur' är SAOL:s hela definition. Fordonsbetydelsen får ingen "
          "synonym -- ingen finns belagd.")

P["amöba"] = dict(
    hb="Encellig organism som ändrar form hela tiden ; (bildligt) slö och oföretagsam person",
    reg="neutral, neutral, biologi ; vardaglig, nedsättande",
    grupper=[["urdjur", "protozo"], ["mähä"]],
    ex="%s rör sig genom att bukta ut sitt cellmembran." % (B % "Amöban"),
    etym="till grekiska amoibe 'växling'",
    notis="SO har den nedsättande bildbetydelsen ('spec. äv. om slö el. "
          "oföretagsam person') som egen; kortet hade den inte. 'urdjur' står i "
          "både SAOL:s och SO:s definition, 'protozo' och 'mähä' i "
          "synonymer.se:s redaktionella lista. Huvudbetydelsen skriven om så "
          "att den inte innehåller synonymordet 'urdjur'.")

P["anstucken"] = dict(
    hb="Till hälften övertygad om en tvivelaktig lära",
    reg="ngt ålderdomlig, lätt negativ",
    grupper=[["påverkad", "besmittad"]],
    ex="Var den gamle finansmannen nazistiskt %s?" % (B % "anstucken"),
    etym="till äldre svenska ansticka 'sticka i brand, smitta'",
    notis="'påverkad' är både SAOL:s ('påverkad av ett (tvivelaktigt) "
          "tänkesätt') och SO:s ('intellektuellt påverkad') definition. "
          "'besmittad' från synonymer.se. 'influerad' struket -- ingen källa "
          "har det, och det saknar ordets negativa laddning.")

P["astronomisk"] = dict(
    hb="Som har att göra med astronomi ; ofattbart stor",
    reg="fackspråklig, neutral, fysik ; vardaglig, neutral",
    grupper=[[], ["enorm", "skyhög"]],
    ex="Priserna på bostäder i innerstaden hade nått %s nivåer." % (B % "astronomiska"),
    etym=None,
    notis="Betydelserna står nu i SO:s ordning (fackbetydelsen först, den "
          "bildliga sedan); kortet hade dem omvända. 'himlarelaterad' struket "
          "-- ordet finns inte i någon källa och är påhittat. Fackbetydelsen "
          "får ingen synonym: den enda kandidaten vore 'astronomi', som är "
          "samma ord.")

P["belysning"] = dict(
    hb="Ljus som kommer från lampor i stället för från dagen ; det att göra ett sammanhang tydligt",
    reg="neutral, neutral ; formell, neutral",
    grupper=[["ljus", "lyse"], ["klarläggande"]],
    ex="Den svaga %s i källaren gjorde det svårt att läsa." % (B % "belysningen"),
    etym=None,
    notis="'klarläggande' är SO:s egen definition av betydelse 2 ('åskådligt "
          "klarläggande'). 'sken' struket -- ett sken kommer från en enskild "
          "källa och kan inte bytas mot belysning. 'perspektiv' struket, ingen "
          "källa har det. 'upplysning 1' i SO:s jfr-lista bär JFR:cohyponym och "
          "används inte.")

P["blommor och bin"] = dict(
    hb="Omskrivning för sex och fortplantning när man talar med barn",
    reg="vardaglig, eufemistisk",
    grupper=[["fortplantning"]],
    ex="Föräldrarna hade ett samtal om %s med sin son." % (B % "blommor och bin"),
    etym=None,
    notis="VARNING: SO-artikeln i uppslagningen är FEL ORD -- den handlar om "
          "insekten bi och om väv (etymologi 'fornsvenska bi, by'), inte om "
          "uttrycket. Flerordsfällan. SO-blocket är därför bortsett från. "
          "Betydelsen vilar helt på Wiktionary, som har uttrycket ordagrant: "
          "'omskrivning för fortplantning, hur sex går till'. Det räckte för "
          "att BEKRÄFTA kortet, som redan sa detta -- till skillnad från 'med "
          "varm hand', där ingen källa alls täckte uttrycket och kortet därför "
          "pausades.")

P["bärkraft"] = dict(
    hb="Förmåga att ta upp tyngd ; (bildligt) att en verksamhet står stadigt ekonomiskt",
    reg="neutral, neutral, teknik ; neutral, neutral, ekonomi",
    grupper=[[], ["hållbarhet", "soliditet"]],
    ex="Isens %s räckte inte för att bära bilen." % (B % "bärkraft"),
    etym=None,
    notis="'bärförmåga' och 'bärighet' är strukna trots att de står i "
          "synonymer.se: båda delar ordstam med uppslagsordet och skulle "
          "trippa cirkular_synonym -- de förklarar 'bärkraft' med 'bär'. "
          "Betydelse 1 lämnas därför utan synonym. 'hållbarhet' är SO:s egen "
          "definition av betydelse 2.")

P["deportera"] = dict(
    hb="Tvinga bort någon till en avlägsen plats",
    reg="formell, neutral, juridik",
    grupper=[["förvisa", "tvångsförflytta"]],
    ex="På 1800-talet %s England förbrytare till Australien." % (B % "deporterade"),
    etym="av latin deportare 'bortföra'",
    notis="'förvisa' står i SO:s jfr-lista med JFR:cohyponym MEN är också hela "
          "SAOL:s definition ('förvisa till avlägsen plats') -- attesterat. "
          "'tvångsförflytta' står i Wiktionarys definition. 'utvisa' struket: "
          "att utvisa är att neka någon att stanna, att deportera är att aktivt "
          "föra bort -- inte utbytbart.")

P["destillera"] = dict(
    hb="Skilja en vätskas delar åt genom att koka och kyla ; få fram det viktigaste ur en stor mängd",
    reg="fackspråklig, neutral, kemi ; formell, neutral",
    grupper=[["rena", "avskilja"], ["koncentrera"]],
    ex="På destilleriet lärde hon sig att %s whisky." % (B % "destillera"),
    etym="av latin destillare 'droppa ned', till stilla 'droppe'",
    notis="Kortet var i sak rätt; synonymerna låg platt och är nu delade per "
          "betydelse. Alla tre står i synonymer.se:s redaktionella lista och "
          "stämmer med SAOL:s definition ('skilja vätskor åt genom "
          "uppvärmning och kondensering').")

P["diskotek"] = dict(
    hb="Lokal där man dansar till inspelad musik ; (äldre) en samling grammofonskivor",
    reg="ngt ålderdomlig, neutral ; ngt ålderdomlig, neutral",
    grupper=[["danslokal", "dansställe"], ["skivsamling"]],
    ex="Ungdomarna gick på %s varje fredag för att dansa till sent på natten." % (B % "diskotek"),
    etym="av franska discothèque; till latin discus 'skiva' och grekiska theke 'förvaringsrum'",
    notis="REGISTER RÄTTAT: SO märker ordet 'mindre brukligt', vilket kortets "
          "'vardaglig' inte fångade -- det är ett ord man känner igen men inte "
          "själv säger längre. 'disko' struket som synonym: det är samma ord "
          "förkortat. Övriga står i SAOL:s definition ('danslokal med inspelad "
          "musik; skivsamling').")


def kallor(o):
    u = json.load(io.open("uppslag/%s.json" % o, encoding="utf-8"))
    return " ".join(u["urler"][k] for k in sorted(u["urler"]))


def main():
    d = json.load(io.open(F, encoding="utf-8"))
    n = 0
    for p in d:
        o = p["ord"]
        if o not in P:
            continue
        f = P[o]
        p["proposed"] = {
            "huvudbetydelse": f["hb"],
            "register": f["reg"],
            "synonym_groups": f["grupper"],
            "synonymer": [s for g in f["grupper"] for s in g],
            "exempelmening": f["ex"],
            "etymologi": f.get("etym"),
        }
        p["sokkoll"] = {"kalla": kallor(o), "slutsats": POLICY + " " + f["notis"]}
        p["approved"] = True
        n += 1
    json.dump(d, io.open(F, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("skrivna: %d" % n)


main()
