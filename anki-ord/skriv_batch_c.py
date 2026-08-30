# -*- coding: utf-8 -*-
"""Batch C (kort 29-40). Samma synonympolicy som skriv_batch_a.py."""
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

P["sympati"] = dict(
    hb="Varm förståelse och medkänsla för någon",
    reg="neutral, positiv",
    grupper=[["medkänsla", "tillgivenhet"]],
    ex="Hans ärliga berättelse väckte %s hos hela publiken." % (B % "sympati"),
    etym="av grekiska sympatheia 'medlidande'",
    notis="'medkänsla' står i SO:s jfr-lista med JFR:cohyponym men också i "
          "Wiktionarys definition -- attesterat. 'tillgivenhet' står i SAOL:s "
          "definition. 'omsorg' struket, går inte att belägga; 'förståelse' "
          "struket som ensamt ord, det är för brett (teknisk förståelse är "
          "ingen sympati).")

P["tjära"] = dict(
    hb="Svart trögflytande vätska ur trä eller kol ; stryka den vätskan på något",
    reg="neutral, neutral ; neutral, neutral",
    grupper=[["beck"], ["becka"]],
    ex="Fiskarna brukade %s båtarna varje vår." % (B % "tjära"),
    etym="fornsvenska tiära, gemensamt germanskt ord, bildat till trä",
    notis="ETYMOLOGIFÄLTET VAR TRASIGT: det innehöll en klistrad Google "
          "Images-länk med hel HTML-taggsträng, inte en etymologi. Ersatt med "
          "SO:s. Betydelserna separerades med '/' i stället för ' ; ', vilket "
          "gör att parsern läser dem som en enda. 'bitumen' och 'asfalt' "
          "strukna -- besläktade material, inte samma sak (kohyponymer).")

P["veritabel"] = dict(
    hb="Som verkligen är det ordet säger, inte överdrivet",
    reg="formell, neutral",
    grupper=[["sannskyldig", "äkta", "verklig"]],
    ex="Fiskarens sista kast var ett %s mästarkast som avgjorde tävlingen." % (B % "veritabelt"),
    etym="av franska véritable; till latin veritas 'sanning'",
    notis="Ovanligt väl belagt: SO markerar 'sannskyldig' med SYN:synonym "
          "(inte cohyponym), och SAOL:s definition är 'verklig, sannskyldig, "
          "äkta' -- alla tre orden alltså attesterade i definitionstext.")

P["briefing"] = dict(
    hb="Snabb information till en grupp innan de sätter igång",
    reg="neutral, neutral",
    grupper=[["kortfattad information", "genomgång"]],
    ex="Innan mötet fick teamet en %s om de nya riktlinjerna." % (B % "briefing"),
    etym="av engelska briefing, till brief 'kortfattad'",
    notis="Bara SAOL har artikeln (ingen SO-träff), och dess definition ÄR "
          "'kortfattad information'. 'genomgång' är Wiktionarys definition. "
          "Huvudbetydelsen omformulerad så att den inte innehåller "
          "synonymordet 'genomgång'.")

P["carpe diem"] = dict(
    hb="Ta vara på dagen medan den finns",
    reg="litterär, positiv",
    grupper=[["fånga dagen", "njut av stunden"]],
    ex="%s, tänkte hon, och bokade resan samma kväll." % (B % "Carpe diem"),
    etym="latin, 'plocka dagen', ur Horatius oden",
    notis="VARNING: uttrycket har varken SO- eller SAOL-artikel (traffar=[]). "
          "Betydelsen vilar helt på Wiktionary och synonymer.se, som är "
          "samstämmiga. Om forgranska.py:s regel uppslagsord_saknas slår till "
          "ska kortet pausas i stället -- samma behandling som hippopotamus "
          "och echappera fick.")

P["centrera"] = dict(
    hb="Placera något mitt på en yta ; inrikta mot en punkt",
    reg="neutral, neutral ; neutral, neutral",
    grupper=[["mittplacera"], ["inrikta"]],
    ex="Han %s ringen så den satt mitt i hålet." % (B % "centrerade"),
    etym="av franska centrer; till centrum",
    notis="SO har två betydelser, kortet hade en. 'inrikta' är SO:s och SAOL:s "
          "egen definition av betydelse 2. 'fokusera' struket -- det närmaste "
          "källorna ger är 'koncentrera sig', som SO markerar JFR:cohyponym.")

P["crème de la crème"] = dict(
    hb="De allra finaste och främsta i en grupp",
    reg="formell, neutral",
    grupper=[["gräddan", "eliten"]],
    ex="Endast %s från konstvärlden bjöds in till vernissagen." % (B % "crème de la crème"),
    etym="franska, 'gräddan av grädden'",
    notis="Bara SAOL har artikeln; dess definition är 'högsta societeten, "
          "gräddan'. 'eliten' står i Wiktionarys definition. Registret ändrat "
          "från 'litterär' till 'formell' -- ingen källa märker uttrycket som "
          "litterärt.")

P["dividera"] = dict(
    hb="Dela ett tal med ett annat ; hålla på och diskutera fram och tillbaka",
    reg="neutral, neutral, matematik ; vardaglig, lätt negativ",
    grupper=[["dela"], ["käbbla"]],
    ex="%s 15 med 3 så får du 5." % (B % "Dividera"),
    etym="av latin dividere 'dela'",
    notis="REGISTERFEL RÄTTAT: kortet angav 'dialektal' för betydelse 2, men "
          "SAOL märker den 'vard.' -- vardaglig, inte dialektal. 'dela' är "
          "SAOL:s definition, 'käbbla' står i Wiktionarys. 'tvista' och "
          "'disputera' strukna, ingen källa har dem. SO:s jfr-lista (addera, "
          "multiplicera, subtrahera) är rena kohyponymer och rörs inte.")

P["eruption"] = dict(
    hb="Utbrott där material sprutar ut ur jordens inre",
    reg="formell, neutral, geologi",
    grupper=[["vulkanutbrott", "utbrott"]],
    ex="En serie våldsamma %s skakade marken runt vulkanen." % (B % "eruptioner"),
    etym="av latin eruptio 'utbrott'",
    notis="Kortet hade huvudbetydelsen 'Vulkanutbrott' OCH synonymen "
          "'vulkanutbrott' -- alltså samma ord två gånger, vilket gör "
          "synonymraden meningslös. Huvudbetydelsen bär nu SO:s formulering, "
          "och 'utbrott' (SAOL: 'vulkaniskt utbrott') står kvar som andra "
          "synonym.")

PAUSA = {
    "turbin": (
        "Ingen belagd synonym finns. SAOL och SO definierar båda omskrivande "
        "('maskin som utvinner nyttig energi ur framströmmande vatten el. "
        "gas') utan synonymord, och synonymer.se har ingen artikel alls. "
        "Kortets gamla ord håller inte: 'maskin' är överbegreppet, "
        "'skovelhjul' är en DEL av turbinen (Wiktionary: 'maskin med "
        "skovelhjul'), och 'roterande enhet' går inte att belägga någonstans. "
        "Samma öppna fråga som diaspora, plektrum och feromon."),
    "autism": (
        "Ingen användbar synonym finns, och de som erbjuds är sämre än ingen. "
        "SO och SAOL har ordagrant samma definition ('en funktionsnedsättning "
        "som bl.a. innebär problem med den sociala förmågan') utan synonym. "
        "synonymer.se ger 'sjuklig självförsjunkenhet' och 'kontaktlöshet' -- "
        "föråldrade beskrivningar som dessutom motsäger SO:s egen definition. "
        "Kortets nuvarande 'autismspektrumtillstånd' innehåller uppslagsordet "
        "och trippar cirkular_synonym (flaggad redan i riskflaggorna)."),
    "feromon": (
        "Ingen belagd synonym finns. SAOL, SO och Wiktionary definierar alla "
        "omskrivande ('doftämne som överförs mellan individer av samma art') "
        "och synonymer.se har ingen artikel. 'doftämne' är definitionens "
        "överbegrepp, inte ett utbytbart ord, och kortets 'luktsignal' går "
        "inte att belägga i någon källa."),
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
