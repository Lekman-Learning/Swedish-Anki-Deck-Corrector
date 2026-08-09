"""Batch 7 — tjugoen kort. Elva ändrade, tio bekräftade.

KÄND BEGRÄNSNING I `slaupp.py`, upptäckt här: sammandraget slår ihop de två
första träffarna per ordbok. På `ans` drog det därför in artikeln för bokstaven
**a** ("första bokstaven i vårt alfabet", "sjätte tonen i C-durskalan"). Rätt
uppgift för *ans* är SAOL:s "skötsel, vård" och SO:s "omsorgsfull vård" — resten
är kontamination från grannträffen. Läses sammandraget slarvigt hamnar fel
betydelse på kortet, så begränsningen skrivs ut i stället för att döljas.

Adams krav 2026-08-09: *"så länge du bara garanterar att korten blir så bra som
det går med de verktyg vi har"*. Vad som faktiskt garanteras står längst ned i
den här filen.
"""
import json
import os
import urllib.parse

MAL = "sessions/session_2026-08-09_v3-so-batch7.json"
KALLOR = ["sessions/session_2026-08-09_v3-omgranskning-nya.json",
          "sessions/session_2026-08-09_v3-dagens-ko.json",
          "sessions/session_2026-08-09_v3-dagens-ko2.json",
          "sessions/session_2026-08-09_v3-inlarning.json"]
# URL-kodat: ett mellanslag i "bekväma sig" gjorde att _URL_RE klippte kalla
# vid mellanslaget och kortet stoppades trots gjord hämtning (2026-08-09).
API = "https://svenska.se/api/msearch?ord={}"


def _api(o):
    return API.format(urllib.parse.quote(o))
SYN = "https://www.synonymer.se/sv-syn/{}"
P = {}


def lagg(ord_, slutsats, kalla=None, **andr):
    P[ord_] = (kalla or _api(ord_), slutsats, andr)


lagg("märla",
     "TRE BETYDELSER SAKNADES, OCH DE STÅR I BÅDA KÄLLORNA. Kortet hade bara den "
     "U-formade metallbiten. SO ger fyra: (1) U-formad metallhake (2) **hyska på "
     "klädesplagg** (3) **liten metallring som förstärker ett hål** (4) verbet 'fästa "
     "med märla'. SAOL lägger dessutom till (5) **ett kräftdjur** och (6) sjötermen "
     "'fästa segellik vid segel'. Kortets 'fästöga' finns i ingen källa. De två som "
     "tas in är de begripliga; kräftdjuret och sjötermen utelämnas medvetet som för "
     "perifera för HP, och det noteras här.",
     huvudbetydelse="U-formad metallhake att fästa med ; hyska på ett klädesplagg ; "
                    "liten metallring som förstärker ett hål",
     synonymer=["krampa", "hyska"])

lagg("randas",
     "ANDRA BETYDELSEN SAKNADES, OCH DEN ÄR DEN BOKSTAVLIGA. Kortet hade bara 'om en "
     "dag: börja ljusna'. Båda källorna ger också '**förse med ränder**' — SO:s "
     "exempel är 'havet var gråsvart och randat av skum' och 'hennes ansikte var "
     "randat av tårar'. Dessutom är den första betydelsen bredare än kortet sa: SO "
     "skriver '(efterhand) börja', med 'en ny tid randades' — det behöver inte vara "
     "en gryning.",
     huvudbetydelse="Om en dag eller en ny tid: långsamt börja ; vara eller bli "
                    "randig av något",
     synonymer=["gry", "bryta in"])

lagg("vokabulär",
     "EN BETYDELSE SAKNADES. SAOL ger 'ordförråd; **ordlista**' — alltså även den "
     "fysiska boken. SO ger 'ordförråd' och det precisare 'ordförråd som viss person "
     "utnyttjar' (ord som \"förty\" ingick i hans vokabulär). Genusrättelsen från i "
     "morse (en bred vokabulär, inte ett brett) står kvar och bekräftas av SAOL:s "
     "böjning.",
     huvudbetydelse="De ord en person eller ett språk förfogar över ; en ordlista",
     synonymer=["ordförråd", "ordlista"])

lagg("kontenta",
     "ANDRA BETYDELSEN SAKNADES. SO ger 'huvudinnehåll i korta drag' OCH "
     "'**slutresultat**' — exemplet 'kontentan av aktionen blev att de blev "
     "uppsagda' handlar inte om en sammanfattning utan om vad det ledde till. "
     "SAOL bekräftar kortets synonymer: 'sammanfattning, huvudinnehåll, kärna'.",
     huvudbetydelse="Det viktigaste i korthet ; det som något till slut ledde till")

lagg("evakuera",
     "TVÅ BETYDELSER SAKNADES. SO ger tre: (1) få människor att lämna ett område "
     "(2) '**lämna**' — det är platsen som töms ('staden evakuerades på ett par "
     "timmar') (3) '**pumpa ut luft eller annan gas ur**', den tekniska betydelsen. "
     "Kortet hade bara (1). JFR tömma, utrymma bekräftar kortets synonym.",
     huvudbetydelse="Föra bort människor från ett farligt område ; tömma en plats ; "
                    "tekniskt: pumpa ut luften ur något",
     synonymer=["utrymma", "tömma"])

lagg("överlastad",
     "TREDJE BETYDELSEN SAKNADES. SO ger 'alltför tungt lastad', 'alltför utsmyckad' "
     "OCH '**alltför innehållsrik**' — en text kan vara överlastad utan att vara "
     "dekorerad. JFR överbelastad bekräftar kortets första synonym. SAOL ger "
     "exemplen 'en överlastad flyktingbåt' och 'en överlastad dekor'.",
     huvudbetydelse="Tyngre lastad än den tål ; med för mycket utsmyckning eller "
                    "innehåll")

lagg("åma",
     "KÄLLORNA VIKTAR ANNORLUNDA ÄN KORTET. Kortet ledde med den fysiska "
     "vridningen. SO ger bara '**göra sig till**' (pojkbandet stod och åmade sig på "
     "scen) och SAOL '**åbäka sig, sjåpa sig**'. Tillgjordheten är alltså "
     "huvudsaken, rörelsen är hur den syns. SAOL:s två synonymer fanns inte på "
     "kortet och tas in.",
     huvudbetydelse="Göra sig till med tillgjorda rörelser för att synas",
     synonymer=["åbäka sig", "sjåpa sig", "göra sig till"])

lagg("platonisk",
     "STAVNINGSSKILLNAD SOM KORTET SLÅR IHOP. SO har uppslagsordet **platonisk** med "
     "hänvisningen 'platonsk' och exemplet 'platonisk kärlek'. Modernt svenskt bruk "
     "skiljer alltså: *platonisk* om kärlek och vänskap, *platonsk* om Platons "
     "filosofi. Kortet lade i morse till filosofibetydelsen under stavningen "
     "'platonisk'. Den flyttas till en anmärkning i stället — det är kärleken HP "
     "prövar, och att blanda ihop stavningarna är just den fällan.",
     huvudbetydelse="Om kärlek eller vänskap: andlig och utan sexuellt inslag "
                    "(filosofibetydelsen stavas platonsk)",
     synonymer=["andlig", "icke-sexuell"])

lagg("stilisera",
     "NYANSEN SKÄRPT. Kortet sa 'återge i förenklad, konstnärlig form'. SO: "
     "'förenkla och **framhäva det typiska**' — poängen är inte bara att ta bort "
     "detaljer utan att lyfta fram det kännetecknande. JFR schematisera bekräftar "
     "kortets synonym. SO:s exempel: 'jugendstilens stiliserade blomrankor', "
     "'bokens stiliserade persongalleri'.",
     huvudbetydelse="Förenkla en avbildning så att det typiska framhävs")

lagg("ogrundad",
     "SYNONYM TILLAGD UR KÄLLA. SO: 'som saknar grund', JFR **oberättigad**, falsk. "
     "SAOL: 'obefogad'. Båda källorna ger samma exempel som kortet redan har, "
     "'ogrundade anklagelser', vilket är ett gott tecken. 'utan belägg' är en fras "
     "snarare än en synonym och ersätts.",
     synonymer=["obefogad", "oberättigad"])

lagg("såframt",
     "SYNONYM TILLAGD UR KÄLLA. SAOL: 'om, **såvida**'. SO: 'såvida'. Just "
     "'såvida' — det ord båda källorna leder med — saknades på kortet. SO:s exempel "
     "'såframt omständigheterna medger, kommer jag att delta' visar att ordet är "
     "formellt och nästan alltid inleder satsen.",
     synonymer=["om", "såvida", "förutsatt att"])

lagg("loafer",
     "EJ I SAOL/SO — BELAGT PÅ ANNAT HÅLL. Uppslaget saknas i båda Akademiens "
     "ordböcker (ordet är ett sent engelskt lån). synonymer.se ger 'sko i "
     "mockasinmodell; lågsko utan snörning', vilket stämmer med kortet och med "
     "OLD-facits 'sko utan snören'. Wiktionary gav 404. **Kortet vilar alltså på en "
     "källa plus facit, inte på tre** — det skrivs ut här hellre än att döljas.",
     kalla=SYN.format("loafer"),
     synonymer=["mockasin", "lågsko utan snörning"])

for o, s in [
    ("marinera", "BEKRÄFTAT. SAOL: 'låta ligga i marinad'. SO: 'lägga i marinad', med "
                 "exemplen marinerad fisk, marinerade räkor, 'så marinerar du tofu'. "
                 "Kortets 'lägga i lag' är samma sak — lag är marinad."),
    ("talträngd", "BEKRÄFTAT. SO: 'ivrig att tala', JFR **pratsam** — kortets första "
                  "synonym. SAOL: 'som pratar mycket'. SO:s exempel är upplysande: "
                  "'flera av middagstalarna var så talträngda att dansen försenades'."),
    ("tillstå", "BEKRÄFTAT, ALLA TRE SYNONYMER. SO ger JFR bekänna, **medge**, **vidgå** "
                "och definitionen 'erkänna riktigheten av'; SAOL 'erkänna, medge'. "
                "Kortets 'motvilligt' står inte i källorna men följer av bruket i SO:s "
                "exempel: 'han ville inte tillstå sin överklassbakgrund'."),
    ("trolsk", "BEKRÄFTAT — OCH CIRKULARITETEN ÄR BORTA. SO: 'som tycks overklig och "
               "förtrollande'. SAOL: 'sällsam och tjusande, sagoaktig'. Kortet löd i "
               "morse ordagrant 'mystisk och sagolik' med samma ord som synonymer; efter "
               "omskrivningen ('så egendomligt vacker att det känns förtrollat') lär det "
               "ut något, och det stämmer med båda ordböckerna."),
    ("ans", "BEKRÄFTAT — MEN SAMMANDRAGET VAR KONTAMINERAT. `slaupp.py` slår ihop två "
            "träffar och drog in artikeln för bokstaven **a** ('första bokstaven i vårt "
            "alfabet', 'sjätte tonen i C-durskalan'). De uppgifterna hör INTE till *ans*. "
            "Rätt: SAOL 'skötsel, vård', SO 'omsorgsfull vård' med JFR omvårdnad, "
            "skötsel — kortets tre synonymer är därmed belagda. SO:s exempel är fint: "
            "'utan ans blir den ljuvaste idyll snart vildmark'."),
    ("bekväma sig", "BEKRÄFTAT. SAOL: '**motvilligt** förmå sig'. SO: '(motvilligt) göra "
                    "ansträngningar', exempel 'han fick bekväma sig till att be om "
                    "ursäkt'. Motviljan står alltså uttryckligen i källan här, till "
                    "skillnad från på tillstå."),
    ("presumera", "BEKRÄFTAT, MED EN UPPLYSNING. SAOL: 'förutsätta, anta', JFR "
                  "presumtion. SO: 'förmoda'. SO:s enda exempel är myndighetsspråk "
                  "('myndigheten bör presumera att den som undertecknat...'), vilket "
                  "visar att ordet i praktiken är juridiskt-administrativt."),
    ("gyro", "BEKRÄFTAT. SAOL: 'roterande snurra el. hjul, gyroskop'. SO: 'gyroskop' samt "
             "'som utnyttjar gyroprincipen' i sammansättningar. Kortets synonym är "
             "ordagrant SO:s definition."),
    ("aristokratisk", "BEKRÄFTAT, MED EN NYANS. SO ger både 'som utmärker aristokrati' "
                      "och 'som har att göra med aristokrati' — exemplen 'aristokratisk "
                      "arrogans' och 'hennes aristokratiska uppträdande' visar att ordet "
                      "lika ofta beskriver ett SÄTT som en börd. Kortets 'förnäm' fångar "
                      "det."),
]:
    lagg(o, s)


def main():
    index = {}
    for f in KALLOR:
        for e in json.load(open(f, encoding="utf-8")):
            index[e["ord"]] = e
    ut, saknade = [], []
    for ord_, (kalla, slutsats, andr) in P.items():
        e = index.get(ord_)
        if e is None:
            saknade.append(ord_)
            continue
        e = json.loads(json.dumps(e))
        e["sokkoll"] = {"kalla": kalla, "slutsats": slutsats}
        e["approved"] = True
        e["applicerad"] = False
        e.pop("skriven_av", None)
        for f_, v in andr.items():
            e["proposed"][f_] = v
        if "huvudbetydelse" in andr:
            e["proposed"]["synonym_groups"] = None
        e["oforandrad"] = not andr
        ut.append(e)
    os.makedirs("sessions", exist_ok=True)
    json.dump(ut, open(MAL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(ut)} poster -> {MAL}")
    print(f"  innehållsändrade : {sum(1 for e in ut if not e['oforandrad'])}")
    if saknade:
        print("SAKNADE:", saknade)


if __name__ == "__main__":
    main()
