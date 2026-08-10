# -*- coding: utf-8 -*-
"""v3-omgranskning av 20 kort ur is:new, andra omgången 2026-08-10.

Varje exempelmening skrivs ut i sin helhet med den böjda formen redan
highlightad. Ingen {}-mall — det var den som gav "Rektorn presidera vid
disputationen" i förra omgången.

Innehållsfel som hittades:
  besätta      SO har fyra betydelser, kortet två; "hålla plats upptagen" saknades
  förtecken    ' / ' mellan två GENUINT skilda betydelser (ska vara ' ; ')
  upphov       ' / ' igen, plus att SO:s "någons förälder" saknades
  blossa       SAKNAD BETYDELSE: "rodna starkt" (kinderna blossade) -- mycket vanlig
  koloni       två av SO:s fem betydelser saknades + cirkulär synonym
  puritan      den historiska kalvinistbetydelsen saknades
  hålfot       SO:s "äv. om motsvarande del av sko" saknades
  lotsa        SAKNAD KÄRNBETYDELSE: vägleda genom farled -- ordet kommer av *lots*
  provinsiell  "trångsynt" är SO:s BIbetydelse, inte del av huvudbetydelsen
  regatta      SO preciserar "serie kappseglingar över flera dagar"
  snuthäck     SAKNAD BETYDELSE: polisstation
  vederkvickt  kortet böjer ordet som adjektiv; SO har verbet *vederkvicka*
  härk         "tränad för arbete" finns inte i någon källa
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HAR = os.path.dirname(os.path.abspath(__file__))
FIL = os.path.join(HAR, "sessions", "session_2026-08-10_v3-omgranskning-nya2.json")
B = '<font color="#3498db">%s</font>'


def kalla(o):
    import urllib.parse
    q = urllib.parse.quote(o)
    return ("https://svenska.se/api/msearch?ord=%s "
            "https://www.synonymer.se/sv-syn/%s "
            "https://sv.wiktionary.org/wiki/%s" % (q, q, q))


R = {
"besätta": ("Militärt ta kontroll över ett område ; tillsätta en tjänst med en innehavare ; hålla en plats upptagen ; förse med tillskott, t.ex. pärlor",
  "formell, neutral", ["ockupera", "tillsätta", "garnera"],
  "Åtta stridsvagnar %s regeringsbyggnaden." % (B % "besatte"), None,
  "SAKNAD BETYDELSE. SO har FYRA betydelser; kortet slog ihop de två första och saknade helt 'hålla (plats eller dylikt) upptagen' — den man möter i *platsen är besatt*. Alla fyra är nu utskrivna, separerade med ' ; ' eftersom de är genuint skilda."),

"förtecken": ("Notskriftstecken som höjer, sänker eller återställer en ton ; bildligt: den prägel något sker under",
  "neutral, neutral, musik", ["prägel", "inriktning", "anstrykning"],
  "En valkampanj med socialistiska %s." % (B % "förtecken"), None,
  "SEPARATORFEL. Kortet skilde de två betydelserna med ' / ', som enligt style_guide betyder omformuleringar av SAMMA betydelse. Ett notskriftstecken och en prägel är inte omskrivningar av varandra — ' ; ' är rätt. Domänen `musik` tillagd (ny axel), och registret ändrat från `formell`: notationstecken är fackspråk, inte byråkrati."),

"upphov": ("Det som orsakar eller utgör första steget i något ; äv. om person: någons förälder",
  "formell, neutral", ["ursprung", "källa", "upprinnelse"],
  "Ryktet hade sitt %s i en missuppfattning." % (B % "upphov"), None,
  "SAKNAD BETYDELSE + separatorfel. SO ger utöver orsaksbetydelsen även 'ibland äv. om person' med språkprovet *hans dagars upphov* — alltså förälder. Kortet saknade den och skilde dessutom sina två led med ' / ' i stället för ' ; '."),

"blossa": ("Brinna med häftig, lysande låga ; rodna starkt ; dra in tobaksrök",
  "neutral, neutral", ["flamma", "glöda", "bolma"],
  "Hennes kinder %s av upphetsning." % (B % "blossade"), None,
  "SAKNAD BETYDELSE, och en vanlig. SO listar fem betydelseskikt; kortet hade två och missade 'rodna starkt' — SO:s eget språkprov är *den sjukes panna blossade*, SAOL:s *hennes kinder blossade*. Det är förmodligen den betydelse Adam oftast möter i text. Registret `vardaglig` saknade stöd: SO markerar ingenting."),

"eftersläpning": ("Det att något är senare än det borde vara", "formell, neutral",
  ["försening", "dröjsmål", "fördröjning"],
  "Bolagets bokföring har skett med stor %s." % (B % "eftersläpning"), None,
  "SO: 'det att något är senare än det borde vara'. Innehållet stämde. Exempelmeningen bytt till SO:s egen, som visar den byråkratiska användning ordet faktiskt har."),

"härk": ("Kastrerad rentjur", "neutral, neutral", ["renoxe", "rentjur"],
  "%s spändes för ackjan." % (B % "Härken"), None,
  "ÖVERSKOTT BORTTAGET. SO och SAOL säger båda exakt 'kastrerad rentjur'. Kortets tillägg 'tränad för arbete' finns inte i någon av de tre källorna — det är en rimlig gissning ur sammanhanget, men inte belagt. Registret `dialektal` ströks: varken SO eller SAOL markerar ordet så, det är en fackterm inom renskötsel."),

"koloni": ("Område underställt en annan nation ; grupp landsmän på en plats långt från hemlandet ; samling jordlotter för husbehovsodling ; sommarhem på landet för barn",
  "neutral, neutral", ["besittning", "lydstat", "koloniträdgård", "sommarläger"],
  "De franska %s i Afrika." % (B % "kolonierna"), None,
  "TVÅ SAKNADE BETYDELSER + cirkulär synonym. SO har fem betydelser. Kortet hade tre och saknade 'personer som bildar en sammanhållen grupp på en plats långt från hemlandet' (SO:s exempel: *den svenska kolonin i Rom*) samt 'samling av mindre jordlotter' (kolonilott/koloniträdgård). Synonymen 'kolonialområde' innehöll dessutom uppslagsordet och är struken."),

"manuell": ("Som utförs med händerna, inte maskinellt", "neutral, neutral",
  ["handdriven", "för hand"],
  "Påsättningen av kapsyler skedde %s." % (B % "manuellt"), None,
  "SO: 'som utförs med händerna'. Innehållet stämde. Registret `formell` ändrat — *manuell växellåda* är vardagsspråk, inte myndighetsspråk."),

"puritan": ("Överdrivet ivrig anhängare av renlevnad och enkla seder ; ursprungligen om sträng kalvinist i 1600-talets England",
  "neutral, lätt negativ", ["renlevnadsman", "sedlighetsivrare", "asket"],
  "Många %s utvandrade till Amerika." % (B % "puritaner"), None,
  "SAKNAD BETYDELSE. SO:s underbetydelse — 'ursprungligen om sträng anhängare av kalvinismen i England, särsk. på 1600-talet' — saknades, och det är den betydelsen ordet har i all historisk text. Valören skärpt till `lätt negativ`: SO skriver '(överdrivet) ivrig', vilket bär en värdering."),

"avsmak": ("Stark motvilja", "neutral, negativ", ["avsky", "vämjelse", "leda"],
  "Hans närmanden fyllde henne med %s." % (B % "avsmak"), None,
  "SO: 'stark motvilja'. Innehållet stämde. Registret var `negativ` ensamt — en valör utan stilnivå. Nu båda axlarna."),

"hålfot": ("Den välvda delen av fotsulan mellan hälen och tåvalken ; äv. om motsvarande del av en sko eller ett skoinlägg",
  "neutral, neutral", ["fotvalv"],
  "Sulan var uppbyggd i %s för att ge extra stabilitet." % (B % "hålfoten"), None,
  "SAKNAD BETYDELSE. SO har 'äv. om motsvarande del av sko el. skoinlägg', och det är just den betydelsen SO:s eget språkprov visar. Kortet hade bara anatomin."),

"högakta": ("Hysa stor aktning för någon", "formell, positiv",
  ["respektera", "värdera högt", "akta"],
  "Hon %s och respekterade honom." % (B % "högaktade"), None,
  "SO och SAOL: båda 'hysa stor aktning för'. Innehållet stämde. Registret var `positiv` utan stilnivå; ordet är formellt (jfr *Högaktningsfullt*)."),

"kroasera": ("Korsa raser eller sorter för att få fram en ny", "fackspråklig, neutral",
  ["korsa"],
  "Han %s två rosensorter för att få en ny färg." % (B % "kroaserade"), None,
  "EJ BELAGT I SO ELLER SAOL — ordet gav ingen artikel i någon av de tre källorna, bara facit ('korsa raser') stödjer betydelsen. Definitionen behålls därför som den var, men underlaget är tunnare än på övriga kort och det ska synas. Synonymen 'föröka fram' är struken: den är inte ett etablerat uttryck. Registret satt till `fackspråklig` — ordet hör till avel och växtförädling."),

"lotsa": ("Vägleda ett fartyg genom svår farled ; bildligt: vägleda någon fram genom något besvärligt",
  "neutral, neutral", ["vägleda", "ledsaga", "guida"],
  "Trots stormen kunde fartyget %s i hamn." % (B % "lotsas"), None,
  "SAKNAD KÄRNBETYDELSE. Kortet hade bara den bildliga användningen ('leda eller visa vägen'). SO leder med sjöfartsbetydelsen — *vägleda genom svårare farled* — och det är den som förklarar ordet: en **lots** är den som för fartyg in i hamn. Utan det ledet är ordet omotiverat. Registret `vardaglig` ströks, SO markerar ingenting."),

"provinsiell": ("Som hör till landsorten ; ofta med bibetydelsen inskränkt och ovillig mot yttre intryck",
  "neutral, lätt negativ", ["landsortsmässig", "småstadsaktig"],
  "Den svenska kulturdebatten har ibland varit rätt %s." % (B % "provinsiell"), None,
  "PRECISERAT. Kortet skrev 'Landsortsmässig, trångsynt' som om båda vore huvudbetydelsen. SO har grundbetydelsen 'som avser eller tillhör landsortsområden' och trångsyntheten som BIbetydelse ('ibland med bibetydelse av inskränkthet'). Skillnaden spelar roll: *provinsiella uttryck* är neutralt beskrivande."),

"regatta": ("Serie kappseglingar över flera dagar för flera båtklasser ; äv. om motsvarande tävling i kanotsport",
  "neutral, neutral, sport", ["kappsegling", "båttävling"],
  "Hela staden samlades för att se %s." % (B % "regattan"), None,
  "PRECISERAT. Kortets 'arrangemang med båttävlingar' var vagare än källan. SO: 'serie kappseglingar under flera dagar och för ett flertal båtklasser' — det är serien och flerdagarsformatet som skiljer en regatta från en enskild kappsegling. Kanotbetydelsen tillagd, domänen `sport` satt."),

"snuthäck": ("Polisbil ; äv. polisstation", "slang, neutral",
  ["polispiket", "polisstation"],
  "En %s svängde runt hörnet med blåljusen på." % (B % "snuthäck"), None,
  "SAKNAD BETYDELSE. SO ger två: 'polisbil' OCH 'polisstation'. Kortet hade bara den första. Registret `slang` behålls — det stämmer — men valören skrivs nu ut."),

"termometer": ("Instrument för mätning av temperatur", "neutral, neutral",
  ["temperaturmätare", "värmemätare"],
  "%s visade 30 grader i skuggan." % (B % "Termometern"), None,
  "SO: 'instrument för mätning av temperatur'. Innehållet stämde. Registret `formell` ändrat — en termometer är ett vardagsföremål."),

"vederkvickt": ("Som fått nya krafter, upplivad och stärkt", "litterär, positiv",
  ["upplivad", "stärkt", "uppfriskad"],
  "Sömnen hade %s henne." % (B % "vederkvickt"), None,
  "FORMFEL RÄTTAT. SO och SAOL har VERBET *vederkvicka* — 'ge nya krafter åt'. Kortets exempel *'Det kändes vederkvickt att duscha'* böjer ordet som ett neutralt adjektiv, vilket inte är gångbar svenska; där krävs *vederkvickande*. Exemplet är nu perfekt particip med objekt, precis som SO:s eget *sömnen vederkvickte henne*."),

"ögonfägnad": ("Något som är en glädje att vila blicken på", "litterär, positiv",
  ["ögonfröjd", "blickfång", "prydnad"],
  "All %s i parken på försommaren." % (B % "ögonfägnaden"), None,
  "SO: 'något som är en glädje att se', SAOL: 'ngt som är angenämt att vila blicken på'. Innehåll och register (`litterär, positiv`) stämde redan — ett av få kort där båda axlarna var rätt från början. Endast exempelmeningen bytt till SO:s egen."),
}


def main():
    d = json.load(open(FIL, encoding="utf-8"))
    kort = d["kort"] if isinstance(d, dict) and "kort" in d else d
    n = 0
    saknas = []
    for e in kort:
        r = R.get(e["ord"])
        if not r:
            saknas.append(e["ord"])
            continue
        hb, reg, syn, ex, etym, slutsats = r
        e["proposed"] = {"huvudbetydelse": hb, "register": reg, "synonymer": syn,
                         "synonym_groups": None, "exempelmening": ex,
                         "etymologi": etym}
        e["sokkoll"] = {"kalla": kalla(e["ord"]), "slutsats": slutsats}
        e["approved"] = True
        e.pop("applicerad", None)
        n += 1
    json.dump(d, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("skrev förslag för %d av %d kort" % (n, len(kort)))
    if saknas:
        print("UTAN FÖRSLAG: %s" % ", ".join(saknas))


if __name__ == "__main__":
    main()
