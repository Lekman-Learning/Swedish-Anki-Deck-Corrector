# -*- coding: utf-8 -*-
"""Batch G (kort 77-88). Samma synonympolicy som skriv_batch_a.py."""
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

P["inflation"] = dict(
    hb="Att priserna stiger allmänt och pengarna blir mindre värda ; att något förekommer så ofta att det tappar värde",
    reg="neutral, neutral, ekonomi ; neutral, neutral",
    grupper=[["prisstegring", "penningvärdesförsämring"], []],
    ex="Hög %s gör att sparade pengar tappar värde." % (B % "inflation"),
    etym="till latin inflatio 'uppblåsning'",
    notis="SAOL har den bildliga betydelsen ('äv. bildl.') och SO beskriver den "
          "utförligt ('något som förekommer ofta och därför minskar i värde') "
          "-- kortet hade den inte. Båda synonymerna är SAOL:s egna "
          "definitionsord. 'deflation' är motsatsen och 'stagflation' en "
          "kohyponym; ingen av dem hör hemma i synonymraden.")

P["intellektuell"] = dict(
    hb="Som har att göra med tänkande och analys ; person som lever av tankearbete",
    reg="formell, neutral ; neutral, neutral",
    grupper=[["förståndsmässig"], ["tankearbetare"]],
    ex="Hennes %s skärpa imponerade på alla i seminariet." % (B % "intellektuella"),
    etym=None,
    notis="Kortet hade båda betydelserna men lade synonymerna platt, så "
          "'mental' och 'lärd' såg ut att höra ihop. 'intelligent' används "
          "inte -- SO markerar det JFR:cohyponym, och det är just förväxlingen "
          "HP:s ORD-del prövar: intelligent är en förmåga, intellektuell en "
          "inriktning. 'förståndsmässig' matchar SAOL:s 'som gäller "
          "förståndet'.")

P["journal"] = dict(
    hb="Löpande anteckningar om ett förlopp ; en tidskrift",
    reg="neutral, neutral, medicin ; neutral, neutral",
    grupper=[["dagbok", "liggare"], ["tidskrift"]],
    ex="Sjuksköterskan förde noggrann %s över patientens tillstånd varje timme." % (B % "journal"),
    etym="av franska journal 'dagbok, tidning', till fornfranska jorn 'dag'",
    notis="Alla fyra orden i SO:s jfr-lista bär JFR:cohyponym, men 'liggare', "
          "'dagbok' och 'tidskrift' står OCKSÅ i SAOL:s egen definition "
          "('liggare, dagbok särsk. i sjukvårdssammanhang | tidskrift') och är "
          "därmed attesterade. 'loggbok' struket -- det är en journal till "
          "sjöss, alltså en snävare sak.")

P["kleptomani"] = dict(
    hb="Tvångsmässigt behov att stjäla",
    reg="formell, neutral, psykologi",
    grupper=[["stöldmani"]],
    ex="Hennes %s fick henne att stjäla saker hon inte ens behövde." % (B % "kleptomani"),
    etym="till grekiska kleptein 'stjäla' och mania 'vansinne'",
    notis="Huvudbetydelsen är SO:s definition ordagrant och SAOL säger detsamma "
          "('sjuklig drift att stjäla'). 'stöldbegär' struket -- ordet finns "
          "inte i någon källa; 'stöldmani' står i synonymer.se:s redaktionella "
          "lista och bär samma tvångskomponent.")

P["kondensera"] = dict(
    hb="Övergå från gas till vätska ; tränga ihop något på mindre plats",
    reg="fackspråklig, neutral, kemi ; formell, neutral",
    grupper=[["förtäta"], ["sammanpressa"]],
    ex="Vattenångan %s till droppar på det kalla fönstret." % (B % "kondenserade"),
    etym="av latin condensare 'tränga samman', till densus 'tät'",
    notis="'indunsta' STRUKET -- det är en annan process (vätska som kokas "
          "bort), inte samma som att gas blir vätska. Kortet hade den i samma "
          "platta lista som 'förtäta'. 'koncentrera' används inte, SO markerar "
          "det JFR:cohyponym.")

P["kooperativ"] = dict(
    hb="Som drivs gemensamt av dem som är med ; sammanslutning som drivs så",
    reg="neutral, neutral, ekonomi ; neutral, neutral, ekonomi",
    grupper=[["samverkande"], []],
    ex="De driver en %s butik i byn där alla medlemmar delar vinsten." % (B % "kooperativ"),
    etym="till latin cooperari 'samarbeta'",
    notis="SO har substantivbetydelsen ('kooperativt organiserad "
          "(arbets)enhet') som egen; kortet hade bara adjektivet. "
          "'samverkande' är SAOL:s definitionsord ('samverkande grupp'). "
          "Substantivet får ingen synonym -- ingen finns belagd som inte "
          "innehåller ordstammen.")

P["limit"] = dict(
    hb="Den övre eller undre punkt man får hålla sig inom",
    reg="neutral, neutral, ekonomi",
    grupper=[["gräns", "beloppsgräns"]],
    ex="Banken höjde hans %s på kreditkortet." % (B % "limit"),
    etym="av latin limes (genitiv limitis) 'gränslinje'",
    notis="'gräns' är SO:s eget definitionsord ('övre eller undre (tillåten) "
          "gräns'), 'beloppsgräns' står i synonymer.se:s redaktionella lista "
          "och fångar den ekonomiska användningen som SAOL lyfter fram ('gräns "
          "för kredit'). Huvudbetydelsen omskriven så att den inte innehåller "
          "synonymordet.")

P["metabolism"] = dict(
    hb="Alla kemiska processer som håller kroppen igång",
    reg="formell, neutral, biologi",
    grupper=[["ämnesomsättning"]],
    ex="En hög %s gör att kroppen förbränner kalorier snabbt." % (B % "metabolism"),
    etym="till grekiska metabole 'förändring'",
    notis="'ämnesomsättning' är SO:s hela definition och står också i SAOL:s. "
          "Kortet hade samma ord både som huvudbetydelse och som synonym, "
          "vilket gör synonymraden meningslös -- huvudbetydelsen är därför "
          "omskriven till vad processen faktiskt gör.")

P["mollusk"] = dict(
    hb="Mjukt ryggradslöst djur ; liten vårta i huden av en virusinfektion",
    reg="fackspråklig, neutral, biologi ; fackspråklig, neutral, medicin",
    grupper=[["blötdjur"], []],
    ex="Snäckor och musslor är exempel på %s." % (B % "mollusker"),
    etym="av franska mollusque; till latin molluscus 'mjuk'",
    notis="Kortet hade EN betydelse; både SAOL ('en virusinfektion som orsakar "
          "knottror på huden') och SO ('liten vårtliknande upphöjning i huden') "
          "har hudbetydelsen som egen. 'blötdjur' är båda källornas "
          "definitionsord. Hudbetydelsen får ingen synonym -- ingen finns.")

P["mångfaldiga"] = dict(
    hb="Göra något många gånger fler ; framställa i många exemplar",
    reg="formell, neutral ; neutral, neutral",
    grupper=[[], ["kopiera", "reproducera"]],
    ex="Exemplen på hans slarv kunde lätt %s." % (B % "mångfaldigas"),
    etym="fornsvenska mangfaldogher; till mången och -faldig",
    notis="'mångdubbla' STRUKET trots att kortet hade det: SO markerar det "
          "JFR:cohyponym, och SAOL har ingen definitionstext att falla tillbaka "
          "på. Detsamma gäller 'duplicera'. Betydelse 1 blir därför utan "
          "synonym; 'kopiera' och 'reproducera' står i synonymer.se:s "
          "redaktionella lista utan kohyponymmarkering.")

P["naturalisera"] = dict(
    hb="Ge en utlänning medborgarskap ; göra något inhemskt",
    reg="formell, neutral, juridik ; formell, neutral",
    grupper=[["ge medborgarskap"], ["göra inhemsk", "assimilera"]],
    ex="Han kom hit som flykting och är numera %s svensk." % (B % "naturaliserad"),
    etym="av franska naturaliser; till natur",
    notis="SO har den andra betydelsen ('göra inhemsk') som egen och SAOL "
          "skriver 'bringa att smälta samman med ny omgivning' -- kortet hade "
          "bara medborgarskapsbetydelsen. Alla synonymer står i källornas egna "
          "definitioner eller i synonymer.se:s redaktionella lista.")

PAUSAD = {}

PAUSAD["mitos"] = dict(
    hb="Vanlig celldelning där en cell blir två likadana",
    reg="fackspråklig, neutral, biologi",
    grupper=[[]],
    ex="Under %s fördelas kromosomerna jämnt mellan de nya cellerna." % (B % "mitosen"),
    etym="till grekiska mitos 'tråd'",
    notis="Kortets synonym 'celldelning' är ordets ÖVERBEGREPP, inte en "
          "synonym: meios är också celldelning, och det är precis den "
          "skillnaden ett ordkort ska lära ut. Ingen annan kandidat finns -- "
          "bara SO har artikeln (ingen SAOL-träff), synonymer.se har ingen, och "
          "Wiktionary skriver samma omskrivning. Huvudbetydelse och register är "
          "färdigrättade; bara synonymfrågan är öppen.")

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
