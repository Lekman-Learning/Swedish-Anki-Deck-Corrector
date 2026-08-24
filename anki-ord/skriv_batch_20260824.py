# -*- coding: utf-8 -*-
"""Skriver proposed-innehall for batch 2026-08-24 (20 is:new-kort).

Reglerna som galler har, alla satta samma dag:
  * synonymer: BARA det SO/SAOL sjalva pekar ut eller skriver i definitionen
  * etymologi: bara dar jag ar saker -- tomt slar fel
  * exempelmening: ska visa den betydelse som star FORST
  * idiom: mest anvanda betydelsen forst, bokstavlig bild i etymologin
"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-24_v3-batch2.json"

# Kort som inte gar att losa rent mot SO/SAOL -- pausas i stallet for att gissas.
PAUSA = {
    "barkad": "SO och SAOL har bara verbet `barka` ('ta barken av trad'). "
              "Adjektivet i vaderbiten-betydelsen finns i syn.se och i facit "
              "men inte i nagon av ordbockerna -- uppslagsordet matchar inte.",
    "nerts": "Ordbokerna har ordet under stavningen `nertz`, sa "
             "_ordboksbelagg() returnerar TOM mangd for `nerts` och ingen "
             "synonym gar att belagga. Loses genom att slaupp koras pa "
             "`nertz`, inte genom att gissa.",
}

# Motiverade undantag. `forgranska_tillat` finns just for det har: en flagga
# som ar korrekt utlost men vars orsak ar utredd och ofarlig.
TILLAT = {
 "tillmotesgaende": {"frammande_uppslagsord":
   "Trafffen `tillmotesga` ar verbet till samma lemma, inte ett annat ord."},
 "got": {"frammande_uppslagsord":
   "Trafffarna gjuta/gjuta av/gjuta in/gjuta over kommer av att `got` ocksa "
   "ar preteritum av `gjuta`. Homograf, inte fel uppslagsord."},
}

KORT = {
 "hologram": dict(
   huvudbetydelse="Tredimensionell bild som framställts med holografi",
   register="neutral",
   synonymer=["tredimensionell bild"],
   exempelmening="Vid konsertens final svävade ett hologram av artisten över scenen.",
   etymologi="Av grekiska <i>holos</i> 'hel' och <i>gramma</i> 'skrift, bild' — en bild som återger helheten, inklusive djupet."),

 "degel": dict(
   huvudbetydelse="Eldfast och kemikaliebeständigt kärl för kraftig upphettning och smältning",
   register="fackspråklig, neutral",
   synonymer=["kärl", "skål"],
   exempelmening="Silvret smältes ned i en degel över gaslågan.",
   etymologi="Från lågtyskan, besläktat med tyskans <i>Tiegel</i> 'smältkärl'."),

 "pivå": dict(
   huvudbetydelse="Tapp som något vrider sig kring ; (sport) den spelare som lagets spel byggs kring",
   register="fackspråklig, neutral",
   synonymer=["svängtapp", "tapp"],
   exempelmening="Fönstret satt på en pivå och kunde vridas ett helt varv.",
   etymologi="Av franska <i>pivot</i> 'tapp, vridpunkt'. Sportbetydelsen är samma bild: den fasta punkt allt annat rör sig runt."),

 "tillmötesgående": dict(
   huvudbetydelse="Ivrig att uppfylla någons önskemål ; hjälpsam",
   register="neutral",
   synonymer=["hjälpsam"],
   exempelmening="Personalen på hotellet var mycket tillmötesgående.",
   etymologi="Av <i>gå någon till mötes</i> — att röra sig mot den andra i stället för att stå kvar."),

 "exkommunicera": dict(
   huvudbetydelse="Bannlysa, utesluta ur en religiös gemenskap ; (utvidgat) utesluta ur en organisation",
   register="formell, neutral",
   synonymer=["bannlysa", "utesluta"],
   exempelmening="Luther exkommunicerades från den katolska kyrkan 1521.",
   etymologi="Av latin <i>ex</i> 'ut ur' och <i>communio</i> 'gemenskap' — bokstavligt att ställas utanför gemenskapen."),

 "göt": dict(
   huvudbetydelse="Gjutet metallblock avsett för vidare bearbetning ; invånare i Götaland vid forntidens slut",
   register="neutral",
   synonymer=["gjutet metallblock", "kokill"],
   exempelmening="Stålverket gjuter göt som sedan valsas till plåt.",
   etymologi=""),

 "nerts": dict(
   huvudbetydelse="Mörkbrun päls från mink ; (äv.) själva mårddjuret",
   register="neutral",
   synonymer=["mink", "flodiller"],
   exempelmening="Kappan var fodrad med nerts.",
   etymologi="Av tyska <i>Nerz</i> 'mink'."),

 "försaka": dict(
   huvudbetydelse="Uppoffra sig genom att avstå från något ; tvingas vara utan",
   register="litterär, neutral",
   synonymer=["avstå från"],
   exempelmening="De fick försaka semesterresan det året de köpte hus.",
   etymologi=""),

 "acceptans": dict(
   huvudbetydelse="Det att många accepterar något ; (tendens till) accepterande",
   register="formell, neutral",
   synonymer=["accepterande"],
   exempelmening="Att genomföra stora förändringar utan folklig acceptans är omöjligt.",
   etymologi="Av latin <i>accipere</i> 'ta emot'."),

 "ruva": dict(
   huvudbetydelse="Ligga på ägg för att kläcka dem ; vakta ; (bildligt) tänka på och planera i tysthet ; (bildligt) utgöra hotfull bakgrund",
   register="något ålderdomlig, neutral",
   synonymer=["ligga på ägg", "vakta"],
   exempelmening="Hönan ruvade på sina ägg i tre veckor.",
   etymologi=""),

 "snörliv": dict(
   huvudbetydelse="Hårt åtsnört plagg som formar överkroppen, buret under klänningen",
   register="ålderdomlig, neutral",
   synonymer=["korsett"],
   exempelmening="Under 1800-talet snörde kvinnorna in midjan med snörliv.",
   etymologi="Av <i>snöra</i> och <i>liv</i> i den äldre betydelsen 'överkropp, midja'."),

 "välboren": dict(
   huvudbetydelse="Av förnäm släkt, av god familj",
   register="ålderdomlig, neutral",
   synonymer=[],
   exempelmening="Brevet var ställt till den välborne herr baronen.",
   etymologi="Av <i>väl</i> och <i>boren</i>, gammal perfektparticipform av <i>bära</i> — alltså 'väl född'."),

 "blottställa": dict(
   huvudbetydelse="Göra skyddslös, ofta i fråga om social eller ekonomisk skyddslöshet",
   register="litterär, neutral",
   synonymer=["göra skyddslös"],
   exempelmening="Efter rättegången var han helt blottställd.",
   etymologi="Av <i>blott</i> i äldre betydelsen 'bar, naken' — att ställa någon bar."),

 "analfabet": dict(
   huvudbetydelse="Person som inte kan läsa och skriva ; person vars läs- och skrivfärdigheter är otillräckliga efter avslutad skolgång ; (bildligt) person med minimala kunskaper på ett område",
   register="neutral",
   synonymer=[],
   exempelmening="I området är mer än 25 procent av befolkningen funktionella analfabeter.",
   etymologi="Av grekiska <i>an-</i> 'icke' och <i>alfabetos</i> — bokstavligt 'utan alfabet'."),

 "osedvanlig": dict(
   huvudbetydelse="Mycket ovanlig ; (adverbiellt) allmänt förstärkande",
   register="litterär, neutral",
   synonymer=["ovanlig"],
   exempelmening="Hon var en osedvanlig begåvning.",
   etymologi=""),

 "reservoar": dict(
   huvudbetydelse="Större behållare för vätska eller gas ; (bildligt) förråd av något outnyttjat",
   register="neutral",
   synonymer=["behållare"],
   exempelmening="Stadens reservoar rymmer vatten för tre dygns förbrukning.",
   etymologi="Av franska <i>réservoir</i>, till latin <i>reservare</i> 'spara, hålla i reserv'."),

 "cello": dict(
   huvudbetydelse="Violoncell, ett djuptonat stråkinstrument",
   register="neutral",
   synonymer=["violoncell"],
   exempelmening="Hon har spelat cello sedan hon var sex år.",
   etymologi="Kortform av italienska <i>violoncello</i>, egentligen 'liten violone'."),

 "luxuös": dict(
   huvudbetydelse="Ytterst elegant och påkostad ; lyxig, praktfull",
   register="neutral",
   synonymer=["lyxig", "praktfull"],
   exempelmening="Paret bodde i en luxuös villa vid stranden.",
   etymologi="Av latin <i>luxus</i> 'överflöd, prakt'."),

 "bokföring": dict(
   huvudbetydelse="Systematisk registrering av ett företags affärshändelser",
   register="fackspråklig, neutral",
   synonymer=[],
   exempelmening="Företaget skötte sin bokföring med hjälp av en extern konsult.",
   etymologi="Av <i>föra bok</i> — att skriva in händelserna i en bok."),
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    skrivna = pausade = ororda = 0
    for e in poster:
        o = e["ord"]
        if o in PAUSA:
            e["proposed"] = None
            e["pausa_skal"] = PAUSA[o]
            pausade += 1
            continue
        if o not in KORT:
            ororda += 1
            continue
        nu = e.get("nuvarande_format") or {}
        p = dict(nu)
        p.update(KORT[o])
        e["proposed"] = p
        e["approved"] = True
        nyckel = (o.replace("ö", "o").replace("å", "a")
                   .replace("ä", "a"))
        if nyckel in TILLAT:
            e["forgranska_tillat"] = TILLAT[nyckel]
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"skrivna {skrivna}  pausade {pausade}  ororda {ororda}")


if __name__ == "__main__":
    main()
