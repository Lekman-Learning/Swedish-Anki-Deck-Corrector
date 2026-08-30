# -*- coding: utf-8 -*-
"""Batch H (kort 89-99), sista i 100-kortsomgangen. Samma synonympolicy."""
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

P["optik"] = dict(
    hb="Vetenskapen om hur ljus beter sig ; linssystemet i ett instrument",
    reg="fackspråklig, neutral, fysik ; fackspråklig, neutral, teknik",
    grupper=[["läran om ljuset"], ["linssystem"]],
    ex="Astronomen fick finjustera teleskopets %s för att få en skarp bild av planeten." % (B % "optik"),
    etym="ur grekiska optike (techne) 'läran om synen'",
    notis="Kortet hade båda betydelserna men lade synonymerna platt, så "
          "'ljuslära' och 'lins' såg ut att höra ihop. 'lins' struket: en lins "
          "är en DEL av optiken, inte samma sak. Båda kvarvarande synonymer "
          "står i synonymer.se:s redaktionella lista och matchar SAOL:s "
          "definition ('vetenskapen om ljuset; system av linser').")

P["pedagogisk"] = dict(
    hb="Som rör konsten att lära ut ; som är bra på att förklara",
    reg="neutral, neutral ; neutral, positiv",
    grupper=[["undervisande"], ["åskådlig"]],
    ex="Läraren använde en %s metod som fick alla att förstå direkt." % (B % "pedagogisk"),
    etym="till grekiska paidagogos 'den som leder barnet'",
    notis="SO skiljer på ordets två användningar: att något HÖR TILL "
          "undervisning, och att någon är BRA på att förklara. Kortet hade "
          "bara den första. 'didaktisk' används inte -- SO markerar det "
          "JFR:cohyponym. 'undervisande' är SAOL:s definitionsord.")

P["platonsk"] = dict(
    hb="Som hör till filosofen Platon ; fri från kroppslig lust",
    reg="formell, neutral, filosofi ; formell, neutral",
    grupper=[[], ["osinnlig", "passionsfri"]],
    ex="Deras vänskap var djup men helt %s." % (B % "platonsk"),
    etym="efter den grekiske filosofen Platon",
    notis="Kortet hade BARA kärleksbetydelsen, men både SO ('som har att göra "
          "med platonismen') och Wiktionary ger filosofibetydelsen först -- den "
          "saknades helt. SAOL:s enda definition är 'platonisk', alltså samma "
          "ord i annan form, och duger inte som synonym. Båda kvarvarande "
          "synonymer är SO:s egna definitionsord ('fri från sinnlighet och "
          "erotik', 'passionsfri, sval').")

P["prestanda"] = dict(
    hb="Hur mycket något klarar av att göra",
    reg="neutral, neutral, teknik",
    grupper=[["prestationsförmåga", "kapacitet"]],
    ex="Bilens %s imponerade på testförarna." % (B % "prestanda"),
    etym="av latin praestanda 'som bör fullgöras'; till prestera",
    notis="'prestationsförmåga' är både SAOL:s och SO:s definitionsord, "
          "'kapacitet' Wiktionarys ('kapacitet att utföra'). Kortet hade bara "
          "det senare. SO:s andra betydelse ('åligganden') är utelämnad med "
          "flit -- den är juridisk och används inte i den mening Adam möter "
          "ordet i.")

P["pörte"] = dict(
    hb="Finsk stuga utan skorsten, med bara en röklucka i taket",
    reg="ngt ålderdomlig, neutral",
    grupper=[["rökstuga"]],
    ex="Ett gammalt %s stod kvar djupt inne i finnmarken." % (B % "pörte"),
    etym="fornsvenska pörte; av finska pirtti",
    notis="'rökstuga' står i både Wiktionarys definition ('hus (rökstuga) med "
          "röklucka i taket') och synonymer.se:s redaktionella lista. Registret "
          "ändrat från 'dialektal': ingen källa märker ordet som dialektalt, "
          "det är ett historiskt ord för en byggnadstyp. 'torp', 'hydda' och "
          "'tjäll' i synonymer.se är andra sorters bostäder, alltså kohyponymer.")

P["raffinerad"] = dict(
    hb="Renad och förfinad ; (bildligt) slug på ett genomtänkt sätt",
    reg="neutral, neutral, kemi ; neutral, lätt negativ",
    grupper=[["renad", "förädlad"], ["utstuderad", "utspekulerad"]],
    ex="Det %s sockret var vitt och finkornigt." % (B % "raffinerade"),
    etym="av franska raffiner, till fin 'fin, fulländad'",
    notis="Kortet hade båda betydelserna men lade synonymerna platt, så "
          "'förfinad' och 'listig' såg ut att betyda samma sak. 'utstuderad' "
          "står i SO:s jfr-lista med JFR:cohyponym men också i SAOL:s egen "
          "definition ('renad; utsökt, förfinad; utstuderad') -- attesterad. "
          "'sofistikerad' struket, det finns bara i synonymer.se och är en "
          "annan nyans.")

P["repressiv"] = dict(
    hb="Som slår ner motstånd och kväver frihet",
    reg="formell, negativ, politik",
    grupper=[["undertryckande", "förtryckande"]],
    ex="Militärjuntans %s apparat slog ner alla protester." % (B % "repressiva"),
    etym="till latin reprimere 'trycka tillbaka'",
    notis="SO definierar cirkulärt ('som utövar repression'), så betydelsen är "
          "tagen ur SAOL ('hämmande, undertryckande'). 'undertryckande' står "
          "där, 'förtryckande' i synonymer.se:s redaktionella lista och i "
          "Wiktionary. 'tolerans' i SO:s jfr-lista är motsatsen, inte en "
          "synonym.")

P["se tiden an"] = dict(
    hb="Vänta och se hur det utvecklar sig innan man gör något",
    reg="formell, neutral",
    grupper=[["avvakta"]],
    ex="Vi får %s innan vi fattar något beslut." % (B % "se tiden an"),
    etym=None,
    notis="VARNING om uppslagningen: svenska.se-artiklarna som hämtades är för "
          "orden AN och TID var för sig (SO:s definition börjar 'en abstrakt "
          "men mätbar grundstorhet...'), inte för uttrycket. Flerordsfällan. "
          "De blocken är bortsedda från. synonymer.se har däremot uttrycket "
          "självt indexerat, med exakt en redaktionell synonym: 'avvakta'. "
          "Huvudbetydelsen omskriven så att den inte innehåller synonymordet.")

P["sexualitet"] = dict(
    hb="Allt som har med kroppens lust och samliv att göra",
    reg="neutral, neutral",
    grupper=[["könsliv", "könsdrift"]],
    ex="Skolan fick en öppnare syn på %s under 1970-talet." % (B % "sexualitet"),
    etym="till latin sexus 'kön'",
    notis="Båda synonymerna står i synonymer.se:s redaktionella lista och "
          "täcker SO:s definition ('behov och aktiviteter som har att göra med "
          "könsdriften'). SO:s jfr-lista (heterosexualitet, homosexualitet med "
          "flera) är hyponymer -- underordnade sorter, inte synonymer -- och "
          "rörs inte.")

P["succession"] = dict(
    hb="Ordningen för vem som tar över efter någon ; obruten rad av något efter varandra",
    reg="formell, neutral, juridik ; formell, neutral",
    grupper=[["tronföljd", "efterträdande"], ["följd"]],
    ex="Kunglig %s reglerar vem som blir nästa monark." % (B % "succession"),
    etym="av latin successio 'efterträdande', till succedere 'följa efter'",
    notis="Alla tre synonymerna står i SAOL:s egen definition ('efterträdande, "
          "följd; tronföljd'). Kortet hade dem i en platt lista, så 'tronföljd' "
          "och 'följd' såg ut att höra till samma betydelse -- nu en grupp per "
          "betydelse.")

P["tyfon"] = dict(
    hb="Tropisk storm med orkanstyrka över Stilla havet ; tryckluftsdriven ljudsignal på fartyg",
    reg="neutral, neutral, geologi ; fackspråklig, neutral, sjöfart",
    grupper=[["virvelstorm", "cyklon"], ["mistlur"]],
    ex="En %s drog in över Filippinerna och slog ut elnätet i flera dagar." % (B % "tyfon"),
    etym="via engelska av kinesiska tai fung 'mäktig vind'",
    notis="EXEMPELMENINGEN BYTT: den gamla ('Fartygets datastyrda tyfon ljöd "
          "genom dimman') illustrerade bara den andra, mycket ovanligare "
          "betydelsen -- kortet visade alltså inte ordet i den mening Adam "
          "möter det. 'orkan' struket: det är en annan stormklassning, alltså "
          "en kohyponym. 'virvelstorm' är SO:s definitionsord, 'cyklon' SAOL:s "
          "('tropisk cyklon').")


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
