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
        e["forgranska_tillat"] = tillat


satt("abrupt",
     "Som börjar eller slutar tvärt, utan förvarning",
     "neutral", ["plötslig"],
     "Samtalet fick ett " + H("abrupt") + " slut när hon lade på luren.", None,
     "SO: plötsligt inledd eller avslutad; exempel ett abrupt slut, ett abrupt svar. "
     "SAOL: tvärt avbruten, plötslig, tvär — plötslig är belagd. Hastig och oväntad saknar belägg.",
     {"synonym_fel_relation": "Plötslig står ordagrant i SAOL:s definitionsled och är utbytbar "
                              "i de flesta lägen (ett abrupt/plötsligt slut)."})

satt("anfäktelse",
     "Själslig oro eller plåga ; frestelse",
     "högtidlig, skämtsam", [],
     "Hans religiösa " + H("anfäktelser") + " höll honom vaken om nätterna.", None,
     "SO ger två betydelser: själslig oro eller plåga, samt frestelse — den senare markerad "
     "numera ofta skämtsamt (exempel hans postmodernistiska anfäktelser). Legacy hade bara den "
     "första. Synonymen själanöd är OLD-facit, inte ordboksbelagd.")

satt("anslå",
     "Bevilja en summa pengar till ett bestämt ändamål ; sätta upp ett meddelande ; träffa med slag",
     "formell", ["tilldela"],
     "Riksdagen " + H("anslog") + " tio miljoner till forskningen.", None,
     "SO ger tre betydelser: träffa med slag, bevilja viss summa för visst ändamål, sätta upp. "
     "SAOL: tilldela; sätta upp — tilldela inleder ett eget led och är belagd. OLD-facit nämner "
     "både meddela och bevilja pengar, alltså krävs båda.")

satt("betvingande",
     "Som bryter ner allt motstånd och tvingar fram beundran",
     "litterär", [],
     "Slutscenen har en " + H("betvingande") + " verkan på publiken.", None,
     "SO: som bryter ner allt motstånd, ofta bildligt; exempel hans betvingande personlighet. "
     "SAOL ger verbet betvinga: besegra efter hård kamp. Legacys överväldigande och oemotståndlig "
     "saknar ordboksbelägg som synonymer.")

satt("bistå",
     "Hjälpa någon, ofta med pengar eller praktiskt stöd",
     "formell", ["hjälpa"],
     "Konsultfirman kan " + H("bistå") + " med marknadsanalyser.", None,
     "SO: stödja genom att ge medel eller annan hjälp åt. SAOL: hjälpa — inleder hela definitionen "
     "och är därmed belagd synonym. Stödja och assistera saknar belägg.")

satt("drastisk",
     "Kraftig och långtgående ; chockerande rättfram",
     "neutral", ["kraftig", "grovkornig"],
     "Företaget vidtog " + H("drastiska") + " åtgärder och sade upp halva personalen.", None,
     "SO: kraftigt verkande, samt chockerande, burdus (exempel hon skämtade grovt på sitt vanliga "
     "drastiska sätt). SAOL: kraftig och långtgående; kraftigt verkande; grovkornig — kraftig och "
     "grovkornig inleder var sitt led och är belagda.")

satt("folklig",
     "Som hör till vanligt folk och är omtyckt av dem",
     "neutral", [],
     "Patron var riktigt " + H("folklig") + " och tog kaffe med drängarna.", None,
     "SO: som tillhör de breda folklagren; äv. om liknande uppträdande hos högt uppsatt person "
     "(exempel patron var riktigt folklig). SAOL: för vanligt folk, populär. Populär står efter "
     "komma, inte som eget led, och räknas därför inte som belagd synonym.",
     {"register_motsager_markning": "SO:s notering ofta i vänsterpolitisk debatt är en bruksuppgift "
                                    "om ett sammanhang, inte en stilnivå. Ordet är stilistiskt "
                                    "neutralt i SAOL och används lika gärna opolitiskt (folkliga "
                                    "sedvänjor, folklig fest)."})

satt("guttural",
     "Som bildas långt bak i strupen ; om röst: grötig och sträv",
     "fackspråklig, lingvistik", [],
     "Han svarade med en tjock, " + H("guttural") + " röst.", None,
     "SO: som frambringas i bakre delen av munhålan, i svalget eller i struphuvudet; äv. allmännare "
     "om ljud av otydlig el. grötig röst. SAOL har bara hänvisning och exemplet gutturala ljud. "
     "OLD-facit strup-; hes, grötig täcker båda leden.")

satt("jordbunden",
     "Som inte kan lyfta från marken ; nyktert praktisk, utan flykt i fantasin",
     "neutral", ["realistisk"],
     "Hans drömmar var inte precis " + H("jordbundna") + " — han ville bli polarforskare.", None,
     "SO ger två betydelser: som inte kan lyfta från marken (jordbundna larver), och som inte "
     "hänger sig åt fantasier, ofta bildligt om person. SAOL: realistisk, föga fantasifull — "
     "realistisk inleder ledet och är belagd.")

satt("saxa",
     "Ställa i kors, växelvis ; klippa ut ur en tidning för att citera",
     "neutral, vardaglig", ["klippa", "korsa"],
     "Hon " + H("saxade") + " över ribban på 160.", None,
     "SO: växelvis ställa i kors (spec. om äldre höjdhoppsteknik), klippa ut, citera — markerat "
     "något vardagligt. SAOL: klippa; korsa; röra sig som en sax, samt klippa ut ur tidning ofta i "
     "avsikt att citera. Klippa och korsa inleder var sitt led och är belagda.")

satt("stickling",
     "Avskuren bit av en växt som sätts i jord för att slå rot",
     "neutral", ["sättkvist", "skott"],
     "Hon satte " + H("sticklingar") + " av pelargonen i en kruka på fönsterbrädet.", None,
     "SO: avskuren stam-, gren- eller rotdel av en växt, som sticks ner i jorden för att slå rot. "
     "SAOL: sättkvist, skott — sättkvist inleder ledet; skott står i samma led men är SAOL:s enda "
     "övriga ord och bekräftas av SO:s cohyponym-hänvisning.")

satt("tentakel",
     "Smalt, rörligt spröt som djur känner och griper med",
     "neutral, biologi", ["känselspröt", "fångarm"],
     "Snigeln drog in sina " + H("tentakler") + " när jag rörde vid den.", None,
     "SO: smal, lättrörlig, utskjutande kroppsdel, vanligen med känselnerver; äv. bildligt. "
     "SAOL: känselspröt; fångarm — två skilda led, båda belagda synonymer.")

satt("vidmakthålla",
     "Se till att något fortsätter finnas eller gälla",
     "formell", ["bevara", "upprätthålla"],
     "Polisen har till uppgift att " + H("vidmakthålla") + " lag och ordning.", None,
     "SO: bevara; exempel vidmakthålla sin position, vidmakthålla lag och ordning. "
     "SAOL: upprätthålla, bevara. Bevara utgör hela SO:s definition och upprätthålla inleder "
     "SAOL:s — båda belagda.")

satt("acklimatisera",
     "Vänja sig vid ett nytt klimat eller nya förhållanden",
     "neutral", [],
     "Hon flyttade in för en månad sedan och har redan " + H("acklimatiserat") + " sig.", None,
     "SO: vänja vid nya förhållanden, spec. i fråga om tillvänjning till klimatförhållanden. "
     "SAOL: vänja vid klimatet; göra hemmastadd; bli hemmastadd. Legacys anpassa saknar belägg "
     "som eget definitionsled.")

satt("adagio",
     "I långsamt tempo ; musikstycke som spelas långsamt",
     "fackspråklig, musik", [],
     "Andra satsen är ett stillsamt " + H("adagio") + ".", None,
     "SO ger två betydelser, båda märkta musik: i långsamt tempo, samt musikstycke i långsamt tempo. "
     "SAOL: långsamt, märkt mus. Legacys moderato är ett annat tempo — struket.")

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 2 skriven: 15 kort. Totalt approved: %d/%d"
      % (sum(1 for e in S if e.get("approved")), len(S)))
