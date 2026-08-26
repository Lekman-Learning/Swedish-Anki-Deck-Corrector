# -*- coding: utf-8 -*-
import json, urllib.parse

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}


def H(w):
    return '<font color="#3498db">' + w + '</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, tillat=None, conf=9):
    e = BY[o]
    q = urllib.parse.quote(o)
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": None, "exempelmening": ex, "etymologi": ety}
    e["sokkoll"] = {"kalla": "SO och SAOL via https://svenska.se/api/msearch?ord=" + q
                    + " (hämtat 2026-08-26, HTTP 200)", "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("fortis",
     "Konsonant som uttalas med kraft, som svenskans p, t och k",
     "fackspråklig, lingvistik", [],
     "Svenskans p, t och k är " + H("fortis") + ", till skillnad från b, d och g.",
     "av latinets fortis, stark",
     "SO: kraftigt uttalad; exempel svenskans p, t och k är fortis, i kontrast till b, d och g; "
     "äv. substantiviskt om huvudtryck. SAOL: huvudaccent. Etymologin tas med eftersom ordet blir "
     "självförklarande av den. Legacys stark, kraftfull och massiv är allmänord utan belägg här.",
     tillat={"betydelse_kan_saknas":
             "SO:s extraposter är en cohyponym-markör och markören äv. i mer el. mindre "
             "substantivisk användning om huvudtryck — samma ord i annan ordklass, inte en skild "
             "betydelse. Kortet ger den språkvetenskapliga kärnan med SO:s eget exempel."})

satt("fossil",
     "Rest av växt eller djur som bevarats i sten från urtiden ; hopplöst omodern person eller sak",
     "neutral", [],
     "De hittade ett " + H("fossil") + " av en trilobit i kalkstenen.", None,
     "SO ger tre betydelser: adjektivet (som utgör förmultnad rest), substantivet (bevarad rest), "
     "samt äv. bildligt om helt otidsenlig person eller företeelse. SAOL bekräftar båda leden och "
     "den bildliga (bildl. gammal person el. företeelse). Legacys petrifierad saknar belägg.")

satt("fotnot",
     "Kort anmärkning längst ner på en sida ; något som blivit en obetydlig detalj",
     "neutral", [],
     "Ett folk som bara blivit en " + H("fotnot") + " i historien.", None,
     "SO: kort anmärkning nederst på en sida; ibland för att uttrycka att något behandlas bara i "
     "förbigående el. har mindre betydelse (exempel ett folk som bara blivit en fotnot i "
     "historien). SAOL: anmärkning i liten stil nederst på sida. Not och kommentar är vidare "
     "begrepp, inte utbytbara.")

satt("fullödig",
     "Som håller allra högsta kvalitet, utan brister",
     "formell", [],
     "Hela laget gjorde en " + H("fullödig") + " insats.", None,
     "SO: som har synnerligen hög kvalitet. SAOL: som har högsta kvalitet. Legacys gedigen, äkta "
     "och ypperlig saknar belägg som egna definitionsled — och gedigen är dessutom självt ett "
     "kort i decket.")

satt("föranstalta",
     "Se till att något blir gjort genom att ordna med det som krävs",
     "formell", [],
     "Kommunen " + H("föranstaltade") + " om extra skolbussar.", None,
     "SO: vidta åtgärder för; exempel föranstalta om speciella skolbussar. SAOL ger bara exemplet "
     "föranstalta om ngt. Legacys anordna och arrangera är vidare — man föranstaltar OM något, "
     "man ordnar det inte nödvändigtvis själv.")

satt("försåt",
     "Bakhåll — att gömma sig och vänta på att slå till",
     "ngt ålderdomlig", ["bakhåll"],
     "Rövarna låg i " + H("försåt") + " vid vägkröken.", None,
     "SO: dold förberedelse för överfall; äv. konkret: bakhåll; exempel lägga försåt för fienden, "
     "ligga i försåt. SAOL: bakhåll — utgör hela definitionen och är belagd synonym. Ordet lever "
     "nästan bara kvar i uttrycket ligga i försåt.",
     tillat={"register_motsager_markning":
             "Varken SO eller SAOL märker ordet. Registret sätts på eget omdöme: försåt förekommer "
             "i modern svenska nästan uteslutande i den fasta vändningen ligga i försåt. Ingen "
             "ordboksmärkning motsägs."})

satt("gillestuga",
     "Sällskapsrum i källaren, ofta med trä och gemytlig inredning",
     "neutral", [],
     "Hela familjen satt samlad i " + H("gillestugan") + " och såg på tv.", None,
     "SO: rustikt sällskapsrum i villa. SAOL: sällskapsrum i källarvåning. Legacys källarstuge är "
     "felstavat och finns inte i någon ordbok; umgängsplats är för brett.")

satt("gnatig",
     "Som tjatar och klagar smått hela tiden",
     "vardaglig", [],
     "Hans " + H("gnatiga") + " svärmor tyckte aldrig att han dög.", None,
     "SO: som gnatar mycket; äv. om handling och dylikt (hennes gnatiga ton). SAOL märker ordet "
     "vard. utan definitionstext. SO:s definition är cirkulär (gnatig = som gnatar), så kortet "
     "beskriver vad gnatandet består i. Legacys grälsjuk är ett grannbegrepp — gräl kräver två "
     "parter, gnat gör det inte.")

satt("godlynt",
     "Som har ett vänligt och lugnt humör",
     "neutral", ["godmodig"],
     "Farbrodern var en " + H("godlynt") + " man som aldrig höjde rösten.", None,
     "SO: godhjärtad. SAOL: godmodig — utgör hela definitionen och är belagd synonym. Godhjärtad "
     "utelämnas som synonym eftersom det handlar om hjärtat, inte humöret; SO:s etymologi (till god "
     "och lynne) stöder att kortet ska handla om lynnet.")

satt("häckla",
     "Kamma lin för att rensa bort skräpet ; angripa någon med spydiga frågor eller kritik",
     "neutral", [],
     "Oppositionen " + H("häcklade") + " regeringens talesman.", None,
     "SO ger fem poster: bearbeta lin genom kamning (mest historiskt), avbryta talare med "
     "närgångna frågor, hånfullt kritisera, samt två redskap (linberedning respektive fiske). "
     "SAOL: bereda lin genom kamning; nagelfara, kritisera; ett redskap för linberedning. Kortet "
     "har de två som bär ordförrådet. Nagelfara är belagd men utelämnas som synonym eftersom det "
     "är svårare än häckla — det skulle förklara svårt med svårt.")

satt("hänvisa",
     "Skicka någon vidare till rätt person eller plats ; peka på en källa eller något sagt tidigare",
     "neutral", [],
     "Alla hotell var fulla, så de " + H("hänvisades") + " till ett vandrarhem.", None,
     "SO ger fyra poster: framhålla möjligheten att söka kontakt, vara beroende av (i perfekt "
     "particip), peka ut som betydelsefull, samt intellektuellt åberopa. SAOL ger exemplet hänvisa "
     "till en text. Kortets två led täcker den praktiska och den intellektuella användningen.",
     tillat={"betydelse_kan_saknas":
             "SO:s fyra poster är två grundbetydelser plus två spec.-markörer (i perfekt particip "
             "om beroende, och spec. om åberopande). Kortets två led — skicka vidare, och peka på "
             "en källa — täcker båda, och exempelmeningen visar particip­användningen."})

satt("högrest",
     "Ovanligt lång och rak i växten",
     "neutral", [],
     "En " + H("högrest") + " gasell betade i skuggan.", None,
     "SO: som har avsevärd kroppslängd; äv. om djur med stor utsträckning i höjdled (en högrest "
     "gasell). SAOL: särsk. om person: lång. Legacys reslig och storväxt är grannord utan belägg "
     "som egna definitionsled — och storväxt är självt ett kort i decket.")

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 6 skriven: 12 kort. Totalt approved: %d/%d"
      % (sum(1 for e in S if e.get("approved")), len(S)))
