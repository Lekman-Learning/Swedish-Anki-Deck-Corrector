# -*- coding: utf-8 -*-
"""Batch 2026-08-31. Del 3: kort 15-22."""
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


# -------------------------------------------------------------- 15. libido
satt("libido",
     "Psykisk energi som hänger samman med könsdriften ; numera vanligen helt "
     "enkelt könsdrift",
     "fackspråklig, neutral ; neutral, neutral",
     ["könsdrift"],
     "Ett naturmedel som påstods kunna öka " + B % "libidon" + ".",
     "av latinets libido 'lust, begär', till libet 'det behagar'; termen fick "
     "sin fackbetydelse genom Sigmund Freuds psykoanalys",
     "SO haller isar tva betydelser: 'psykisk energi som hanger samman med "
     "konsdriften' och 'konsdrift', den senare markt 'numera vanligen'. Bada "
     "skrivs ut (regel 1). SAOL har bara den andra, 'konsdrift', vilket "
     "belagger den som synonym till just den gruppen. syn.se:s begar, atra "
     "och lusta saknar ordboksbelagg.",
     grupper=[[], ["könsdrift"]])

# -------------------------------------------------------------- 16. uppbåd
satt("uppbåd",
     "Stor grupp personer som kallats samman för ett särskilt syfte, ibland "
     "utan tanke på vem som kallade ; i finlandssvenska: mönstring eller "
     "inskrivning till militärtjänst",
     "neutral, neutral ; dialektal, neutral",
     ["mönstring", "inskrivning"],
     "Ett stort " + B % "uppbåd" + " deltog i skallgången efter den försvunne.",
     "till bjuda upp 'kalla samman'; fornsvenska upbudh om kallelse till "
     "häroch tingsförsamling",
     "SO: 'stor grupp personer som kallats samman for sarskilt syfte' med "
     "underbetydelsen 'ibland utan tanke pa sammankallande' -- UB, foljer med. "
     "SAOL delar upp i tva och lagger till 'monstring, inskrivning' markt "
     "finl. Eftersom SAOL haller isar dem skrivs de som tva betydelser "
     "(regel 1); den finlandssvenska markningen aterges som dialektal, "
     "eftersom registervokabularen inte har ett eget varde for finlandssvenska. "
     "Monstring och inskrivning inleder bada sitt led i SAOL:s andra "
     "definition och belagger darmed andra gruppen.",
     grupper=[[], ["mönstring", "inskrivning"]])

# ------------------------------------------------------------ 17. inprägla
satt("inprägla",
     "Fästa något djupt i minnet, ofta genom upprepning",
     "formell, neutral",
     [],
     "Hon läste texten om och om igen och " + B % "inpräglade" + " namnen.",
     "av in och prägla 'stämpla, slå mynt', av lågtyskans pregen; bilden är "
     "myntstampen som trycker in ett märke som inte går bort",
     "SO och SAOL ger bada exakt 'fasta i minnet'. En betydelse. Inga belagda "
     "synonymer: definitionen ar en flerordsfras dar inget enskilt ord ar "
     "utbytbart. syn.se:s inpranta och inskarpa ligger nara men star inte i "
     "nagon ordboksdefinition, och inpranta ar dessutom ett annat uppslagsord.")

# --------------------------------------------------------------- 18. kuliss
satt("kuliss",
     "Flyttbar bakgrundsdekoration på en teaterscen ; utrymmet mellan eller "
     "bakom dessa, som i uttrycket bakom kulisserna om att agera i det "
     "fördolda ; bildligt om något som döljer det verkliga förhållandet",
     "neutral, neutral ; neutral, neutral ; neutral, negativ",
     [],
     "Partiledaren agerade " + B % "bakom kulisserna" + " i stället för att "
     "gå ut offentligt.",
     "av franskans coulisse 'ränna, skjutbar skiva', till couler 'glida, "
     "rinna'; kulisserna sköts ursprungligen in i rännor på scengolvet",
     "SO haller isar tre: 'flyttbar bakgrundsdekoration pa teaterscen' med "
     "UB:n 'av. om utrymmet mellan el. bakom kulisser', 'agera i det fordolda' "
     "och 'nagot som doljer'. Alla tre skrivs ut (regel 1). SAOL bekraftar "
     "'flyttbar scendekoration; av. bildl.'. INGEN synonym: SAOL:s definition "
     "inleds av flyttbar, inte av scendekoration, sa scendekoration ar "
     "modifierat och inte belagt. syn.se:s sattstycke och fond ar dessutom "
     "narliggande men inte utbytbara begrepp.")

# -------------------------------------------------------------- 19. uppsyn
satt("uppsyn",
     "Ansiktsuttryck som visar ett visst sinnestillstånd ; övervakning eller "
     "uppsikt över någon eller något",
     "neutral, neutral ; formell, neutral",
     ["min", "utseende"],
     "Han lyssnade på diskussionen med road " + B % "uppsyn" + ".",
     "fornsvenska upsyn; till syn, alltså ordagrant 'det man ser upp mot'",
     "SO haller isar tva: '(visst) ansiktsuttryck' och 'overvakning'. SAOL "
     "likasa: 'min, utseende' och 'uppsikt'. Bada skrivs ut (regel 1). Min och "
     "utseende inleder bada sitt led i SAOL:s forsta definition och hor till "
     "forsta gruppen; uppsikt ar hela SAOL:s andra definition och hor till den "
     "andra.",
     grupper=[["min", "utseende"], ["uppsikt"]])

# --------------------------------------------------- 20. lagga hamsko pa
satt("lägga hämsko på",
     "Hindra eller bromsa något så att det inte kan utvecklas fritt",
     "formell, neutral",
     [],
     "Partiet ville " + B % "lägga hämsko på" + " statens utgiftsökningar.",
     "av tyskans Hemmschuh 'broms på vagnshjul', till hämma och sko; "
     "hämskon var den kloss man lade under hjulet i en backe",
     "SO ger hamsko betydelsen 'hindrande omstandighet' och exemplet 'partiet "
     "ville lagga (en) hamsko pa statens utgiftsokningar'. SAOL har uttrycket "
     "'lagga (en) hamsko pa'. En betydelse. VARNING som ar kontrollerad: "
     "traffistan innehaller sex poster, men fem av dem ('placera sig i "
     "horisontell stallning', 'ga till sangs', 'ge stor tillfredsstallelse', "
     "'forsatta sig', 'frivilligt avsta fran kamp') hor till uppslagsordet "
     "LAGGA SIG och ar en annan flerordsfras -- de har ingenting med hamsko "
     "att gora och skrivs inte in. Inga belagda synonymer: 'hindrande "
     "omstandighet' definierar substantivet hamsko, inte hela uttrycket.")

# ------------------------------------------------------------ 21. deviation
satt("deviation",
     "Avvikelse från en riktning eller från det normala, särskilt om det "
     "riktningsfel en kompass får av järnet i ett fartyg",
     "fackspråklig, neutral",
     ["riktningsändring", "avvikelse"],
     "Kompassen i en stålbåt kan påverkas, en så kallad " + B % "deviation"
     + ".",
     "av latinets deviatio 'avvikelse', till de 'bort från' och via 'väg'; "
     "samma rot som i devis och trivial",
     "SO: 'riktningsandring' med underbetydelsen 'av. avvikelse'. En "
     "betydelse med UB, alltsa en grupp (regel 1 galler betydelser, inte "
     "underbetydelser). SAOL har bara en hanvisning. Bada synonymerna "
     "riktningsandring och avvikelse ar hela SO:s respektive definitioner och "
     "darmed belagda och utbytbara. Statistikbetydelsen som det gamla kortet "
     "hade (spridningsmatt) star inte i nagon av ordbockerna och stryks.")

# --------------------------------------------------------- 22. galvanometer
satt("galvanometer",
     "Instrument som mäter svaga elektriska strömmar",
     "fackspråklig, neutral",
     [],
     "Med en " + B % "galvanometer" + " kunde de mäta den svaga strömmen i "
     "kretsen.",
     "efter den italienske läkaren Luigi Galvani, som på 1780-talet upptäckte "
     "att grodlår ryckte av elektricitet, plus -meter av grekiskans metron "
     "'mått'",
     "SO: 'ett instrument for matning av svaga elektriska strommar'. SAOL: "
     "'ett matinstrument for svaga elektriska strommar'. En betydelse, och de "
     "tva definitionerna ar praktiskt taget identiska. Inga synonymer: "
     "instrument och matinstrument inleder visserligen sina led men ar "
     "overordnade termer, inte utbytbara at bada hallen -- varje "
     "galvanometer ar ett matinstrument, men langt ifran tvartom.")


json.dump(KORT, io.open(FIL, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
skrivna = sum(1 for k in KORT if k.get("proposed"))
pausade = sum(1 for k in KORT if k.get("v3_pausad"))
print("del 3 klar: %d skrivna, %d pausade, %d kvar av 40"
      % (skrivna, pausade, 40 - skrivna - pausade))
