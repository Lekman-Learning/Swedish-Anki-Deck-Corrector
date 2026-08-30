# -*- coding: utf-8 -*-
"""Batch A (kort 0-19) i 100-kortsomgangen 2026-08-30, spar B, mognadsordnad.

SYNONYMPOLICY som gallde nar dessa skrevs -- utskriven har for att den ar
resultatet av tva misslyckade blindgranskningsrundor tidigare samma dag:

 1. Forstahandsval: ett ord som star i SAOL:s eller SO:s egen DEFINITIONSTEXT,
    eller i Wiktionarys definitionslista, och som gar att byta ut mot
    uppslagsordet i samma betydelse.
 2. Andrahandsval: synonymer.se:s REDAKTIONELLA lista, aldrig avdelningen
    "Anvandarnas bidrag", och bara nar ordet ar utbytbart.
 3. Aldrig: ett ord som BARA star i SO:s jfr-lista nar underbetydelser
    innehaller JFR:cohyponym. Det ar SO:s egen markering for "jamforbart
    begrepp", inte synonym -- felet som fallde esplanad, drabant och diaspora.
    Undantaget ar precist: star ordet OCKSA i SAOL:s eller SO:s definitionstext
    ar det attesterat anda (SAOL definierar nedlatande som "hogdragen;
    foraktfull" -- da AR de orden definitionen, inte en se-aven).
 4. Klarar inget ord 1-3 lamnas gruppen TOM. Ingen gissning, ingen platshallare.

Kommentarerna i den har filen ar avsiktligt utan diakriter (verktygskedjan
har historiskt hostat upp mojibake i kommentarer). KORTENS INNEHALL nedan ar
daremot riktig svenska med a-ring och umlaut -- det ar det Adam laser.
"""
import io
import json

F = "sessions/session_2026-08-30_v3-omgranskning-repetition-mognad.json"
B = '<font color="#3498db">%s</font>'
POLICY = (
    "Betydelser, register och etymologi lästa ur SO/SAOL. Synonymer valda "
    "efter policyn i skriv_batch_a.py: SAOL/SO/Wiktionarys definitionstext "
    "först, synonymer.se:s redaktionella lista i andra hand, ALDRIG ett ord "
    "som bara står i SO:s jfr-lista när JFR:cohyponym är satt. Tom grupp "
    "hellre än gissning.")

P = {}

P["adjutant"] = dict(
    hb="Person som hjälper en hög chef inom krigsmakten eller hovet med det praktiska",
    reg="formell, neutral, militär",
    grupper=[["officersbiträde"]],
    ex="%s följde generalen på alla hans resor och skötte den dagliga planeringen." % (B % "Adjutanten"),
    etym="av tyska Adjutant; till latin adjutare 'hjälpa'",
    notis="SO/SAOL ger EN betydelse. 'assistent' och 'medhjälpare' strukna: "
          "båda är överordnade ord, inte utbytbara (en assistent på ett kontor "
          "är ingen adjutant). 'officersbiträde' matchar SAOL:s definition "
          "'officer som tjänstgör som biträde åt högre officer'.")

P["aktuell"] = dict(
    hb="Som är av intresse just nu",
    reg="neutral, neutral",
    grupper=[["angelägen"]],
    ex="Klimatfrågan är mer %s än någonsin i årets valrörelse." % (B % "aktuell"),
    etym="av franska actuel; till latin actus 'handling'",
    notis="'viktig' struket -- något kan vara viktigt utan att vara aktuellt, "
          "orden är inte utbytbara. 'brännande' struket: det är en kollokation "
          "('brännande aktuell'), inte en synonym. 'angelägen' står i "
          "Wiktionarys definitionslista.")

P["atrofi"] = dict(
    hb="Att en kroppsdel tynar bort och krymper av att inte användas eller av sjukdom",
    reg="formell, neutral, medicin",
    grupper=[["förtvining"]],
    ex="Efter tre månader i gips syntes tydlig %s i vadmuskeln." % (B % "atrofi"),
    etym="av grekiska atrophia, till a- 'ej' och trophe 'näring'",
    notis="'genom bristande användning' i den gamla huvudbetydelsen var en "
          "överspecificering -- varken SO ('förtvining av kroppsvävnader') "
          "eller SAOL anger orsak. 'tillbakabildning' och 'förkrympning' kom "
          "bara från synonymer.se och är strukna.")

P["avträda"] = dict(
    hb="Lämna ifrån sig sina rättigheter till något ; (mer sällan) gå sin väg från ett rum",
    reg="formell, neutral, juridik ; ngt ålderdomlig, neutral",
    grupper=[[], ["avlägsna sig"]],
    ex="Sverige fick %s sina baltiska besittningar 1721." % (B % "avträda"),
    etym=None,
    notis="SO har TVÅ betydelser, kortet hade en (old_har_fler_betydelser). "
          "Betydelse 1 får ingen synonym: hela SO:s jfr-lista (avträdelse, "
          "frånträda, överlåta 1) bär JFR:cohyponym, och inget av orden står i "
          "någon definitionstext. 'avlägsna sig' ÄR SO:s egen definition av "
          "betydelse 2 och är utbytbar.")

P["banal"] = dict(
    hb="Så vanlig och uttjatad att den inte säger något",
    reg="neutral, negativ",
    grupper=[["alldaglig", "sliten"]],
    ex="Han tyckte manuset var %s och fullt av utslitna klyschor." % (B % "banalt"),
    etym="av franska banal, ursprungligen 'påbjuden till allmänt bruk'",
    notis="'alldaglig' och 'sliten' står i SAOL:s EGEN definition ('alldaglig, "
          "sliten, platt') -- därför attesterade trots att SO listar alldaglig "
          "under jfr med JFR:cohyponym. 'intetsägande' kom bara från "
          "synonymer.se. Registret ändrat från 'formell': varken SO eller SAOL "
          "har någon formalitetsmärkning.")

P["croissant"] = dict(
    hb="Halvmåneformat frukostbröd av smördeg",
    reg="neutral, neutral, matlagning",
    grupper=[["fransk frukostgiffel"]],
    ex="Jag åt en %s med smör och marmelad till frukost." % (B % "croissant"),
    etym="av franska croissant 'växande', till croître 'växa'",
    notis="'bakverk' struket (överordnat ord) och 'wienerbröd' struket -- det "
          "är ett ANNAT bakverk, alltså en kohyponym av precis den sort som "
          "fällde tidigare kort. Kvar står synonymer.se:s enda redaktionella "
          "post. Huvudbetydelsen bär nu SAOL:s 'halvmånformigt'.")

P["ed"] = dict(
    hb="Högtidligt löfte att tala sanning ; svordom ; smal landremsa mellan två farbara vatten",
    reg="formell, neutral, juridik ; vardaglig, negativ ; ngt ålderdomlig, neutral",
    grupper=[["sanningsförsäkran"], ["svordom"], ["landtunga", "näs"]],
    ex="Vittnet avlade %s innan förhöret började." % (B % "ed"),
    etym="fornsvenska eþer, gemensamt germanskt ord",
    notis="TRE betydelser i SO och SAOL, kortet hade två hopslagna "
          "(old_har_fler_betydelser). Alla tre synonymgrupperna är hämtade ur "
          "definitionstexten: SAOL skriver 'högtidlig sanningsförsäkran', "
          "'svordom' och 'landtunga', SO skriver 'näs'.")

P["eufori"] = dict(
    hb="Stark känsla av lycka och upprymdhet",
    reg="formell, positiv",
    grupper=[["lyckokänsla", "upprymdhet"]],
    ex="Löparna kände total %s när de äntligen korsade mållinjen." % (B % "eufori"),
    etym="till grekiska euphoros 'frisk', av eu 'väl' och pherein 'bära'",
    notis="Båda synonymerna står i definitionstexten (SAOL: 'förhöjt "
          "stämningsläge, lyckokänsla'; SO: 'stark känsla av lycka och "
          "upprymdhet'). 'välbefinnande' struket -- för svagt, ett lugnt "
          "välbefinnande är inte eufori.")

P["exotisk"] = dict(
    hb="Som kommer från fjärran, ofta tropiska länder ; (försvagat) främmande och ovanlig",
    reg="neutral, positiv ; neutral, neutral",
    grupper=[[], ["främmande", "sällsam", "ovanlig"]],
    ex="Djurparken hade en avdelning full av %s djur från hela världen." % (B % "exotiska"),
    etym="av grekiska exotikos 'utländsk, främmande'",
    notis="SO delar upp i två betydelser där den andra är uttryckligen "
          "försvagad. Grupp 2:s tre ord ÄR SO:s definition av den betydelsen. "
          "Betydelse 1 lämnas utan synonym -- 'utländsk' (synonymer.se) täcker "
          "inte 'fjärran, tropisk', som är hela poängen med ordet.")

P["fysisk"] = dict(
    hb="Som rör kroppen ; som rör den materiella världen, det man kan ta på",
    reg="neutral, neutral ; neutral, neutral",
    grupper=[["kroppslig"], ["materiell"]],
    ex="Efter operationen var hans %s ork borta i flera månader." % (B % "fysiska"),
    etym=None,
    notis="Exempelmeningen BYTT: den gamla ('de fysiska lagarna') illustrerade "
          "SO:s fysik-betydelse, som kortet inte tar upp -- exemplet visade "
          "alltså något annat än huvudbetydelsen. 'konkret' struket, det står i "
          "ingen källa. SO:s jfr-lista (materiell 1, mental, psykisk) bär "
          "JFR:cohyponym, men 'materiell' står också i SO:s definitionstext.")

P["förankra"] = dict(
    hb="Fästa ett fartyg med ankare ; (bildligt) skaffa stöd för ett beslut hos dem det gäller",
    reg="neutral, neutral, sjöfart ; neutral, neutral",
    grupper=[["fästa"], []],
    ex="Beslutet måste %s hos alla berörda innan det klubbas." % (B % "förankras"),
    etym=None,
    notis="Kortet hade en betydelse, SO har fyra som går att slå ihop till två "
          "(old_har_fler_betydelser). 'fästa' står i både SO:s och Wiktionarys "
          "definitionstext. 'förtöja' används INTE: det står bara i SO:s "
          "jfr-lista, och den listan bär JFR:cohyponym. Den bildliga betydelsen "
          "får ingen synonym -- ingen finns belagd.")

P["geografi"] = dict(
    hb="Vetenskapen om jordytan, landskapen och hur människor använder dem ; (vardagligt) själva terrängen på en plats",
    reg="neutral, neutral ; vardaglig, neutral",
    grupper=[[], ["terräng"]],
    ex="Han älskade %s och kunde namnge alla världens huvudstäder utantill." % (B % "geografi"),
    etym="av grekiska geographia 'jordbeskrivning', till ge 'jord' och graphein 'skriva'",
    notis="'geologi' står i synonymer.se:s lista och är en KOHYPONYM -- en "
          "annan vetenskap, inte samma. Att lista den hade varit exakt det fel "
          "HP:s ORD-del straffar. 'jordkunskap' och 'landskapslära' går inte "
          "att belägga någonstans. 'terräng' är SO:s vardagliga betydelse.")

P["insinuation"] = dict(
    hb="Antydan som är menad att svärta ner någon utan att sägas rakt ut",
    reg="formell, negativ",
    grupper=[["förtäckt beskyllning", "undermening"]],
    ex="Journalisternas %s om korruption fick borgmästaren att avgå." % (B % "insinuationer"),
    etym="till insinuera",
    notis="'antydan' struket som ensam synonym: en neutral antydan är ingen "
          "insinuation, det är det kränkande som är ordets kärna. SAOL "
          "definierar 'beskyllning i förtäckta ordalag'.")

P["irreparabel"] = dict(
    hb="Omöjlig att laga eller ersätta",
    reg="formell, negativ",
    grupper=[["obotlig", "ohjälplig"]],
    ex="Bilkrocken orsakade %s skador på motorn." % (B % "irreparabla"),
    etym="av latin irreparabilis 'som inte går att reparera'",
    notis="Kortet var i allt väsentligt rätt. Båda synonymerna ÄR SAOL:s "
          "definition ('obotlig, ohjälplig'). 'oreparerbar' struket -- bara "
          "synonymer.se, och det är dessutom en ren omskrivning av "
          "uppslagsordet. Huvudbetydelsen säger nu 'laga' i stället för "
          "'reparera', som ligger för nära själva ordet.")

P["kompromiss"] = dict(
    hb="Uppgörelse där båda parter ger efter på något för att mötas",
    reg="neutral, neutral",
    grupper=[["sammanjämkning"]],
    ex="Partierna enades till slut om en %s efter veckor av förhandling." % (B % "kompromiss"),
    etym="ur medeltidslatin compromissum 'ömsesidigt löfte'",
    notis="'jämkning' och 'medelväg' står i SO:s jfr-lista med JFR:cohyponym "
          "satt och används därför inte. 'överenskommelse' struket: det är "
          "ordets överordnade begrepp -- varje kompromiss är en "
          "överenskommelse, men inte tvärtom, alltså inte utbytbart.")

P["layout"] = dict(
    hb="Hur text och bilder placeras ut på en sida",
    reg="neutral, neutral",
    grupper=[["formgivning", "komposition"]],
    ex="Formgivaren la ner veckor på tidningens %s innan tryckningen." % (B % "layout"),
    etym="av engelska layout, till lay out 'lägga ut, planera'",
    notis="Huvudbetydelsen sa 'för tryck', vilket är föråldrat -- SAOL skriver "
          "uttryckligen 'i tryckta såväl som digitala medier'. 'komposition' "
          "står i SO:s definition, 'formgivning' i SAOL:s. 'disposition' "
          "struket, det används om texters innehåll snarare än om sidytan.")

P["moralisk"] = dict(
    hb="Som handlar om vad som är rätt och fel ; som följer det man anser vara rätt",
    reg="neutral, neutral ; neutral, positiv",
    grupper=[["etisk", "sedlig"], ["rättfärdig"]],
    ex="Att aldrig ljuga var hennes viktigaste %s princip." % (B % "moraliska"),
    etym=None,
    notis="Kortet slog ihop SO:s två betydelser och lade 'rättfärdig' i samma "
          "grupp som 'etisk' -- men rättfärdig hör till betydelse 2 (den som "
          "FÖLJER normerna), inte till betydelse 1 (den som HANDLAR om dem). "
          "'sedlig' är SAOL:s egen definition.")

P["nedlåtande"] = dict(
    hb="Som behandlar andra som om de vore mindre värda",
    reg="neutral, nedsättande",
    grupper=[["högdragen", "föraktfull"]],
    ex="Chefen gav honom en %s blick när han föreslog idén." % (B % "nedlåtande"),
    etym=None,
    notis="SO:s jfr-lista (föraktfull, högdragen, högfärdig) bär tre "
          "JFR:cohyponym -- men SAOL DEFINIERAR ordet som 'högdragen; "
          "föraktfull'. Då är orden definitionen, inte en se-även, och de står "
          "kvar. 'överlägsen' struket: det beskriver hållningen, men en "
          "överlägsen prestation är inget nedlåtande.")

P["optimal"] = dict(
    hb="Så bra som det över huvud taget kan bli i just den situationen",
    reg="neutral, positiv",
    grupper=[["bästa möjliga", "mest gynnsam"]],
    ex="Vinklarna gav %s ljus i rummet hela eftermiddagen." % (B % "optimalt"),
    etym="till optimum",
    notis="Båda synonymerna ÄR SAOL:s definition ord för ord. 'idealisk' och "
          "'perfekt' kom från synonymer.se:s avdelning 'Användarnas bidrag', "
          "som inte är redaktionell och därför inte räknas som källa.")

# --- Pausas: uppslagningen hamtade fel artikel ---
PAUSA = {
    "med varm hand": (
        "slaupp.py hämtade artikeln för ordet VARM, inte för uttrycket 'med "
        "varm hand': SO-definitionerna handlar om hög temperatur, "
        "friktionsvärme och att inte frysa, och SAOL:s 'successivt' hör till "
        "en annan artikel. Det är den kända flerordsfällan (se CLAUDE.md). "
        "Uttryckets betydelse går alltså inte att belägga ur den här "
        "uppslagningen, och kortets nuvarande formulering ('ge bort något "
        "medan man fortfarande lever') kan varken bekräftas eller motbevisas. "
        "Kräver en riktad uppslagning mot SO:s idiomavdelning."),
}
TAGG = "v3_pausad::fel_uppslagsord_hamtat"


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
