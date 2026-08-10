# -*- coding: utf-8 -*-
"""v3-omgranskning av 30 kort ur is:new, 2026-08-10.

Forsta batchen som skrivs mot den NYA registertaxonomin (tre axlar, `neutral`
pa bada, fackomrade). Det ar ocksa poangen med att kora just den har omgangen:
20 av 30 kort hade `formell` -- och for de allra flesta var det inte sant, bara
det enda lagliga svaret innan `neutral` fanns.

Innehallsfel som hittades (utover register):
  bestort     SO har aven 'om handling' (bestorta rop) -- saknades
  forfakta    kortet la till 'trots motstand', som INGEN ordbok har
  modifiera   SAOL 'mildra' (modifiera sitt skarpa uttalande) -- saknades
  skenhelig   SO:s karna ar 'from eller godhjartad', inte 'battre an man ar'
  futuristisk SO leder med 'som har att gora med FUTURISM' (konstriktningen)
  humid       SO ar en klimatterm: 'kannetecknas av riklig nederbord'
  voyeur      SO:s karna ar EROTISK/lustkanslor -- kortet gjorde det till nyfikenhet
  abstrakt    SO har aven 'ytterst allmant hallen och darfor foga askadlig'
  avhysa      SO har aven tillfallig uppehallsplats (ockupanterna avhystes)
  fjord       SO har aven 'storre oppet havsomrade inomskars' (Vastkusten)
  presidera   SO har TRE betydelser, kortet hade en
  samarit     SAOL 'person som kan ge forsta hjalpen' -- saknades helt
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HAR = os.path.dirname(os.path.abspath(__file__))
FIL = os.path.join(HAR, "sessions", "session_2026-08-10_v3-omgranskning-nya.json")
BLA = '<font color="#3498db">%s</font>'


def kalla(ord_):
    return ("https://svenska.se/api/msearch?ord=%s "
            "https://www.synonymer.se/sv-syn/%s "
            "https://sv.wiktionary.org/wiki/%s" % (ord_, ord_, ord_))


# ord: (huvudbetydelse, register, synonymer, exempelmening_mall, etymologi, slutsats)
# {} i exempelmallen ersatts av det highlightade ordet.
R = {
"bekantgöra": ("Göra allmänt bekant", "formell, neutral",
  ["tillkännage", "offentliggöra", "kungöra"],
  "Departementet {} promemorian i början av året.", None,
  "SO: 'göra allmänt bekant'. Definitionen stämde. Register var `formell` utan valör; ordet ÄR myndighetsspråk, så stilnivån behålls och `neutral` valör skrivs ut."),

"bestört": ("Bragt ur fattningen, häpen ; äv. om handling: som uttrycker bestörtning",
  "neutral, neutral", ["förskräckt", "häpen", "chockad"],
  "De var {} över hans utbrott.", None,
  "SAKNAD BETYDELSE. SO: 'som har bragts ur fattningen' PLUS underbetydelsen 'äv. om handling och dylikt' (SO:s eget exempel: *bestörta rop*). Kortet hade bara personbetydelsen. Dessutom sa kortet 'oväntade DÅLIGA nyheter' — SO säger inget om dåliga, bara att fattningen brister. Register `negativ` var en valör utan stilnivå; ordet är varken högtidligt eller nedsättande."),

"fägring": ("Vackert utseende, skönhet", "litterär, positiv",
  ["skönhet", "behag", "prakt"],
  "Trädgårdarna stod i prunkande {}.", None,
  "SO: 'vackert utseende', SAOL: 'skönhet'. synonymer.se märker ordet '(högt.)', vilket stöder `litterär`. Kortets 'Det vackra hos något' var vagare än källorna; skärpt. Valör `positiv` tillagd — ordet är genuint lovordande."),

"förfäkta": ("Ivrigt tala för en åsikt", "neutral, neutral",
  ["hävda", "förespråka", "argumentera för"],
  "Han {} radikala åsikter.", None,
  "SAKFEL. Kortet sa 'Driva en åsikt TROTS MOTSTÅND'. Varken SO ('(ivrigt) tala för') eller SAOL ('argumentera för') har någon motståndsklausul — kortet lade till ett villkor som inte finns. Samma felklass som *pittoresk* 2026-08-09."),

"modifiera": ("Förändra lätt ; mildra (t.ex. ett uttalande)", "neutral, neutral",
  ["ändra", "jämka på", "mildra"],
  "Hon blev tvungen att {} sitt skarpa uttalande.", None,
  "SAKNAD BETYDELSE. SAOL: 'jämka på, ändra; MILDRA', och SO:s eget exempel är 'modifiera sitt skarpa uttalande' — alltså mildra, inte bara ändra. Kortet hade bara 'göra mindre ändringar'."),

"portabel": ("Bärbar, går lätt att bära med sig", "neutral, neutral",
  ["bärbar", "flyttbar", "transportabel"],
  "Han köpte en {} högtalare till resan.", None,
  "SO och SAOL: båda 'bärbar'. Innehållet stämde. Register `formell` var fel — ordet är vanlig standardsvenska, inte myndighetsspråk."),

"skenhelig": ("Som ger sken av att vara from eller godhjärtad utan att vara det ; äv. om handling",
  "neutral, nedsättande", ["hycklande", "skrymtaktig", "falskt from"],
  "Han tog på sig en {} min.", None,
  "SO: 'som försöker ge intryck av att vara FROM ELLER GODHJÄRTAD (utan att vara det)' plus underbetydelsen 'äv. om handling'. Kortets 'Låtsas vara bättre än man är' tappade fromhetsledet, som är ordets kärna (jfr *skrymtare*), och saknade handlingsbetydelsen. Valör skärpt till `nedsättande` — ordet fälls om personer."),

"verifiera": ("Bestyrka riktigheten av något", "neutral, neutral",
  ["bekräfta", "styrka", "intyga"],
  "Uppgifterna om gränskränkningar var svåra att {}.", None,
  "SO: 'bestyrka riktigheten av', SAOL: 'fastställa riktigheten av'. Kortets 'mot en källa' var en inskränkning källorna inte gör — man kan verifiera mot ett kvitto, ett experiment eller en observation."),

"anletsdrag": ("Ett ansiktes konturlinjer", "litterär, neutral",
  ["ansiktsdrag", "drag"],
  "Han hade regelbundna {}.", None,
  "SO: 'ett ansiktes konturlinjer'. Innehållet stämde; `litterär` behålls (anlete är bokspråk), valör `neutral` utskriven."),

"futuristisk": ("Som hör till futurismen (konstriktningen) ; äv. som ser ut att höra hemma i framtiden",
  "neutral, neutral, konst", ["framtidsinriktad", "modernistisk"],
  "Byggnaden hade en {} design av glas och stål.", None,
  "SAKNAD HUVUDBETYDELSE. SO leder med 'som har att göra med FUTURISM' och exemplifierar med 'futuristisk konst' — konstriktningen, inte framtidskänslan. Kortet hade bara den vardagliga betydelsen. Ny domän-tagg `konst` (axeln tillagd samma dag)."),

"elokvent": ("Vältalig", "litterär, positiv", ["vältalig", "oratorisk"],
  "Talaren var {} och fångade hela publiken.", None,
  "SO och SAOL: båda 'vältalig'. synonymer.se märker '(litt.)' — kortet saknade stilnivå helt och hade bara valören `positiv`."),

"humid": ("Som kännetecknas av riklig nederbörd (om klimat)", "fackspråklig, neutral",
  ["fuktig", "nederbördsrik"],
  "Regnskogen har en {} klimattyp.", None,
  "SO: 'som kännetecknas av RIKLIG NEDERBÖRD', exempel 'en humid klimattyp' — det är en klimatterm, inte ett allmänt ord för fuktig luft. Kortets 'Fuktig i luften' var vardagsengelskans *humid*, inte svenskans. Stilnivå `fackspråklig`."),

"intoxikation": ("Förgiftning", "fackspråklig, neutral, medicin",
  ["förgiftning", "överdosering"],
  "Patienten fördes in med akut {}.", None,
  "SO: 'förgiftning'. Innehållet stämde. Registret gjordes om: ordet är inte byråkratiskt utan medicinskt fackspråk — nu synligt på den nya domänaxeln."),

"voyeur": ("Person som får lustkänslor av att i smyg titta på andras erotiska aktiviteter",
  "neutral, nedsättande", ["smygtittare", "fönstertittare"],
  "Grannen visade sig vara en {}.", None,
  "SAKFEL — betydelsen var urvattnad. SO: 'person som får LUSTKÄNSLOR genom att (i smyg) titta på andras EROTISKA aktiviteter'; SAOL säger 'sexuella aktiviteter'. Kortets 'andras privata stunder' gjorde ordet till en nyfiken granne. Det erotiska ledet ÄR ordet."),

"hugfästa": ("Säkra hågkomsten av något", "högtidlig, neutral",
  ["bevara minnet av", "föreviga"],
  "Minnesmärket skulle {} offrens namn.",
  "Av håg 'sinne, minne' + fästa — att fästa något i minnet.",
  "SO och SAOL: båda 'säkra hågkomsten av'. Innehåll och etymologi stämde. Stilnivå ändrad från `formell` till `högtidlig` (ny tagg): ordet hör till minnesmärken och jubileer, inte till blanketter."),

"hurtbulle": ("Överdrivet pigg och sportig person", "vardaglig, skämtsam",
  ["friskus", "frisksportare"],
  "Kontorets {} sprang alltid en mil före frukost.",
  "hurtig + bulle — en 'bulle' är i äldre slang en rundlagd, godmodig typ.",
  "Kortet var redan rätt på båda axlarna (`vardaglig, skämtsam`) — ett av få. Oförändrat i sak."),

"utmönstra": ("Skilja bort såsom föråldrat eller mindre värdefullt", "formell, neutral",
  ["gallra ut", "kassera", "utrangera"],
  "Begreppet 'kyrkobokföring' {} på 1990-talet.", None,
  "SO: 'skilja bort såsom föråldrad eller mindre värdefull'. Stämde. `formell` behålls — ordet ÄR förvaltningsspråk (SO:s eget exempel är kyrkobokföring)."),

"abstrakt": ("Som inte kan uppfattas med sinnena ; äv. ytterst allmänt hållen och därför föga åskådlig",
  "neutral, neutral", ["teoretisk", "ogripbar", "svårfattlig"],
  "Konceptet kändes för {} för att förstå direkt.",
  "Latin abstractus 'fråndragen' — det konkreta är bortdraget.",
  "SAKNAD BETYDELSE. SO har utöver sinnesbetydelsen även 'ytterst allmänt hållen (och därför föga åskådlig)' — den vardagliga klagan att något är 'för abstrakt'. Kortet hade bara den filosofiska."),

"ad interim": ("Tills vidare, under en övergångsperiod", "formell, neutral",
  ["tillfälligt", "provisoriskt", "tills vidare"],
  "Hon utsågs till vd {} tills en permanent lösning fanns.",
  "Latin ad interim, 'för mellantiden'.",
  "EJ I SO ELLER SAOL — uttrycket saknas i båda; endast synonymer.se ('tills vidare') och facit belägger det. Innehållet stämmer mot dem, men underlaget är tunnare än på övriga kort och det ska synas. `formell` är rätt: uttrycket lever i titlar och protokoll."),

"anhålla": ("Tillfälligt beröva friheten ; formellt begära", "formell, neutral, juridik",
  ["gripa", "begära", "hemställa"],
  "En 46-årig man har {} för inbrottet.", None,
  "SO har båda betydelserna och kortet hade båda — ett av de bättre korten i bunten. Endast register ändrat: den ena betydelsen är rent juridisk, vilket nu syns på domänaxeln."),

"anvisa": ("Ge upplysning om ; bevilja eller tilldela", "formell, neutral",
  ["hänvisa", "tilldela", "bevilja"],
  "Hon blev {} plats längst bak i lokalen.", None,
  "SO: 'ge upplysning om' + 'bevilja'. Kortet hade båda. Oförändrat i sak; register kompletterat."),

"avhysa": ("Tvinga att flytta från sin bostad ; äv. från en mer tillfällig uppehållsplats",
  "formell, neutral, juridik", ["vräka", "fördriva"],
  "Ockupanterna {} efter beslutet.",
  "av + hysa — fornsvenskans 'skilja från hus och gård', motsatsen till att hysa någon.",
  "SAKNAD BETYDELSE. SO har utöver bostadsfallet även 'tvinga att flytta från mer tillfällig uppehållsplats', med exemplet 'ockupanterna avhystes'. Kortet hade bara bostad — men just ockupationsfallet är det man oftast läser i tidningen."),

"besynnerlig": ("Svår att förstå sig på ; om person: något tokig", "neutral, neutral",
  ["egendomlig", "märkvärdig", "sällsam"],
  "Kattugglan har ett {} utseende.",
  "Släkt med sönderlig/besinna — det man inte kan besinna sig på.",
  "SO har båda betydelserna och kortet hade båda. Register `formell` var fel — ordet är vanlig standardsvenska, om än något bokligt."),

"deadline": ("Bestämd tidpunkt när något senast måste vara avslutat", "vardaglig, neutral",
  ["tidsgräns", "slutdatum"],
  "Han missade sin {} för rapporten.",
  "Engelska dead-line — ursprungligen en linje i ett fångläger som fångar sköts vid om de passerade.",
  "SO: 'bestämd tidpunkt när något senast måste vara avslutat', SYN-markerad synonym: *tidsgräns* (= facit). Stämde. Valör utskriven."),

"fjord": ("Djup, långt inskjutande, smal havsvik ; på Västkusten äv. större öppet havsområde inomskärs",
  "neutral, neutral, geologi", ["havsvik", "fjärd"],
  "Båten gled tyst in i den norska {}.", None,
  "SAKNAD BETYDELSE. SO ger utöver den norska bilden även 'äv. om större, öppet havsområde inomskärs (på Västkusten)' — den svenska användningen, som en svensk läsare möter oftare än den norska. Domän `geologi`."),

"håvor": ("Gåvor, rikedomar (endast plural)", "ngt ålderdomlig, neutral",
  ["gåvor", "skänker", "nådegåvor"],
  "Kungen delade ut rika {} till sina gäster.",
  "Plural av gammalt hava 'egendom' — samma ord som ha. Därför bara i plural.",
  "SO: 'gåvor', SAOL: 'gåvor, rikedomar'. synonymer.se märker '(pl., åld.)'. Innehåll och etymologi stämde; stilnivån preciserad från `litterär` till `ngt ålderdomlig` (ny tagg) eftersom det är daterat snarare än poetiskt. Pluralformen skriven in i definitionen."),

"presidera": ("Vara ordförande ; vara ledare vid samtal eller umgänge ; bildligt: sitta som den förnämste, trona",
  "formell, neutral", ["leda", "föra ordet", "trona"],
  "Rektorn {} vid disputationen.", None,
  "TVÅ SAKNADE BETYDELSER. SO ger tre: 'vara ordförande', 'vara ledare vid samtal, umgänge eller dylikt' (NN presiderade vid middagen) och bildligt 'sitta (som den förnämste), trona'. Kortet hade bara den första."),

"samarit": ("Osjälviskt hjälpsam person ; person som kan ge första hjälpen ; invånare i Samarien",
  "neutral, positiv", ["hjälpare", "sjukvårdare", "samarier"],
  "Hon fick hjälp av en anonym {}.",
  "Efter liknelsen om den barmhärtige samariern i Lukasevangeliet.",
  "TVÅ SAKNADE BETYDELSER. SO: 'osjälviskt hjälpsam person' + 'invånare i Samarien', och SAOL lägger till 'person som kan ge FÖRSTA HJÄLPEN vid olycksfall' — den betydelsen används i praktiken (samariterförbund) och saknades helt. Etymologin tillagd: den gör ordet självförklarande."),

"åskådlig": ("Som gör att man kan göra sig en tydlig bild av något", "neutral, neutral",
  ["tydlig", "illustrativ", "belysande"],
  "Diagrammet visar {} förhållandet mellan reallöner och hyror.", None,
  "SO: 'som på ett tydligt sätt låter sig betraktas och uttolkas'. Kortets 't.ex. med bilder' var en inskränkning SO inte gör — ett resonemang kan vara åskådligt utan bilder. Register `formell` ändrat: ordet är vanlig standardsvenska."),

"överflödig": ("Som inte är nödvändig", "neutral, neutral", ["onödig", "obehövlig"],
  "Möbeln kändes helt {} i det lilla rummet.", None,
  "SO: 'som inte är nödvändig'. Stämde. Register `formell` ändrat till `neutral` — vanligt ord."),
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
        e["proposed"] = {
            "huvudbetydelse": hb,
            "register": reg,
            "synonymer": syn,
            "synonym_groups": None,
            "exempelmening": ex.replace("{}", BLA % e["ord"]),
            "etymologi": etym,
        }
        e["sokkoll"] = {"kalla": kalla(e["ord"]), "slutsats": slutsats}
        e["approved"] = True
        n += 1
    json.dump(d, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("skrev forslag for %d av %d kort" % (n, len(kort)))
    if saknas:
        print("UTAN FORSLAG: %s" % ", ".join(saknas))


if __name__ == "__main__":
    main()
