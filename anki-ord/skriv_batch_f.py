# -*- coding: utf-8 -*-
"""Batch F (kort 65-76). Samma synonympolicy som skriv_batch_a.py."""
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

P["donera"] = dict(
    hb="Ge bort något större till ett gott ändamål",
    reg="neutral, neutral",
    grupper=[["skänka"]],
    ex="Hon %s hela sin porslinssamling till museet." % (B % "donerade"),
    etym="av latin donare 'ge, skänka bort'",
    notis="'skänka' är SO:s eget definitionsverb ('skänka (större gåva) till "
          "visst ändamål'). 'testamentera' från synonymer.se är struket -- det "
          "sker först vid dödsfall och är alltså en snävare handling, inte "
          "utbytbart.")

P["dramatisera"] = dict(
    hb="Skriva om en berättelse till pjäs ; framställa något som mer omskakande än det var",
    reg="neutral, neutral, konst ; vardaglig, lätt negativ",
    grupper=[["omarbeta för teatern"], ["överdriva"]],
    ex="Tidningen valde att %s den redan spännande händelsen." % (B % "dramatisera"),
    etym=None,
    notis="Kortet hade båda betydelserna men lade synonymerna platt. "
          "'omarbeta för teatern' är SAOL:s egen definition, 'överdriva' står "
          "i synonymer.se:s redaktionella lista och matchar SAOL:s 'göra stort "
          "nummer av'.")

P["essentiell"] = dict(
    hb="Så viktig att det inte går utan",
    reg="formell, neutral",
    grupper=[["väsentlig", "livsviktig"]],
    ex="De ställdes inför %s frågor om liv och död." % (B % "essentiella"),
    etym="av franska essentiel",
    notis="SO märker ordet uttryckligen 'formellt', vilket kortets register "
          "redan hade rätt. 'väsentlig' står i både SAOL:s och SO:s definition, "
          "'livsviktig' i SO:s. Huvudbetydelsen omskriven så att den inte "
          "innehåller synonymordet 'väsentlig'.")

P["evident"] = dict(
    hb="Så tydlig att den inte går att ifrågasätta",
    reg="formell, neutral",
    grupper=[["uppenbar", "obestridlig"]],
    ex="Han skriver så snårigt att budskapet inte är omedelbart %s." % (B % "evident"),
    etym="av latin evidens 'klart seende'",
    notis="Ovanligt väl belagt: SO markerar 'uppenbar' med SYN:synonym, inte "
          "cohyponym, och SAOL:s definition är 'obestridlig, uppenbar'. "
          "'tydlig' struket som eget led -- SO:s definition är 'fullständigt "
          "tydlig', och det är just fullständigheten som skiljer evident från "
          "tydlig.")

P["evolution"] = dict(
    hb="Långsam förändring av arter över mycket lång tid",
    reg="formell, neutral, biologi",
    grupper=[["utveckling"]],
    ex="Under %s utvecklade vissa djur ett inre skelett." % (B % "evolutionen"),
    etym="av latin evolutio, till evolvere 'upprulla, utveckla'",
    notis="'utveckling' är SO:s hela definition. Kortet var redan rätt; "
          "huvudbetydelsen är bara skärpt med SAOL:s precisering att det gäller "
          "levande organismer över lång tid -- utan den kan kortet inte skiljas "
          "från vilken utveckling som helst.")

P["exceptionell"] = dict(
    hb="Som är ett undantag från det vanliga",
    reg="formell, neutral",
    grupper=[["högst ovanlig", "enastående"]],
    ex="Hon var en %s begåvning redan som barn." % (B % "exceptionell"),
    etym="av franska exceptionnel; till latin exceptio 'undantag'",
    notis="'sällsynt' STRUKET -- SO markerar det uttryckligen JFR:cohyponym. "
          "Något sällsynt förekommer sällan; något exceptionellt bryter mot "
          "mönstret. 'högst ovanlig' är SAOL:s egen definition. Registret "
          "ändrat från 'vardaglig': ingen källa märker ordet som vardagligt.")

P["farmakologi"] = dict(
    hb="Vetenskapen om hur läkemedel verkar i kroppen",
    reg="fackspråklig, neutral, medicin",
    grupper=[["läran om läkemedel"]],
    ex="%s studerar hur läkemedel tas upp och bryts ner i kroppen." % (B % "Farmakologi"),
    etym="till grekiska pharmakon 'läkemedel' och logos 'lära'",
    notis="Kortets huvudbetydelse VAR SO:s definition ordagrant ('läran om "
          "läkemedel'), samtidigt som synonymen sa något annat -- nu är "
          "definitionen synonym och huvudbetydelsen omskriven. "
          "'läkemedelsvetenskap' struket, ordet finns inte i någon källa.")

P["fusionera"] = dict(
    hb="Låta två företag bli ett enda",
    reg="formell, neutral, ekonomi",
    grupper=[["sammansmälta", "gå samman"]],
    ex="De två bankerna beslutade att %s nästa år." % (B % "fusionera"),
    etym="till latin fusio 'gjutning, sammansmältning'",
    notis="SO definierar bara cirkulärt ('genomföra fusion av'), så "
          "betydelsen är tagen ur SAOL ('smälta samman, slå samman; gå "
          "samman'). Båda synonymerna står där eller i synonymer.se:s "
          "redaktionella lista.")

P["grammatik"] = dict(
    hb="Reglerna för hur ord och meningar byggs i ett språk ; lärobok i de reglerna",
    reg="neutral, neutral, lingvistik ; neutral, neutral, lingvistik",
    grupper=[["språklära"], []],
    ex="Han satt uppe hela natten och pluggade %s inför tentan." % (B % "grammatik"),
    etym="via latin av grekiska grammatike, till gramma 'skrivtecken'",
    notis="SO har läroboken som egen betydelse ('äv. om motsvarande lärobok'); "
          "kortet hade den i huvudbetydelsen men utan egen synonymgrupp. "
          "'syntax' och 'formlära' STRUKNA: båda är DELAR av grammatiken, "
          "alltså kohyponymer -- syntax handlar bara om satsbyggnad. "
          "'språklära' står i SO:s jfr-lista med JFR:cohyponym men är också "
          "hela SAOL:s definition, och är därmed attesterad.")

P["i allo"] = dict(
    hb="I alla avseenden, från början till slut",
    reg="ngt ålderdomlig, neutral",
    grupper=[["helt och hållet"]],
    ex="Det var en lyckad resa %s." % (B % "i allo"),
    etym="gammal böjningsform (dativ) av all",
    notis="VARNING om uppslagningen: SAOL-artikeln som hämtades är för "
          "BOKSTAVEN i ('nionde bokstaven i vårt alfabet') och är bortsedd "
          "från. SO:s artikel för 'all' innehåller däremot uttrycket ordagrant "
          "('allt igenom, helt och hållet'), och Wiktionary har 'i alla "
          "avseenden' -- betydelsen är alltså belagd i två källor trots det "
          "felaktiga SAOL-träffen.")

P["imitativ"] = dict(
    hb="Som går ut på att härma något",
    reg="formell, neutral",
    grupper=[["efterliknande"]],
    ex="Barnen lärde sig språket med en %s metod, genom att härma vuxna." % (B % "imitativ"),
    etym="till latin imitari 'efterlikna'",
    notis="Tunt underlag: synonymer.se och Wiktionary har ingen artikel alls. "
          "'efterliknande' är hela SAOL:s definition och stämmer med SO:s "
          "('som utgörs eller utmärks av efterhärmning'), så den ena synonymen "
          "är väl belagd -- men det finns ingen andra att ställa bredvid.")

PAUSAD = {}

PAUSAD["gå tretton på dussinet"] = dict(
    hb="Finnas i sådant överflöd att det inte är värt något",
    reg="vardaglig, lätt negativ",
    grupper=[[]],
    ex="Såna cyklar %s, du hittar likadana i vilken affär som helst." % (B % "går tretton på dussinet"),
    etym=None,
    notis="Uttrycket går inte att belägga. slaupp.py hämtade artiklarna för "
          "TRETTON och GRIFT (etymologi 'fornsvenska þrättan' respektive "
          "'latin crypta') -- flerordsfällan igen -- och varken synonymer.se "
          "eller Wiktionary har någon artikel för uttrycket. Kortets gamla "
          "synonym '≈≈ alldaglig' är dessutom trasigt formaterad. "
          "Huvudbetydelsen är omformulerad efter old_facit (Adams eget gamla "
          "facit), men den är INTE källkollad, och synonymen är öppen.")

TAGG = "v3_pausad::inget_uppslagsord_i_so_saol"


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
        if o in PAUSAD:
            f = PAUSAD[o]
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
    print("skrivna: %d   pausade: %d" % (n_s, n_p))


main()
