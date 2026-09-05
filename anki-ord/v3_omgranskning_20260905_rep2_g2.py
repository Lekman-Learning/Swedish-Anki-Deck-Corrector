# -*- coding: utf-8 -*-
"""Spar B (omgranskning), session_2026-09-05_v3-omgranskning-repetition2.json.
Grupp 2, ord 9-16 (vinsch .. feedback)."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-05_v3-omgranskning-repetition2.json"
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"vinsch": dict(
  unchanged=True,
  hb="Maskin som drar eller lyfter last med en lina som rullas upp",
  reg="neutral, neutral, teknik",
  grp=[["vindspel"]],
  ex='<font color="#3498db">Vinscharna</font> skramlade när lasten drogs upp.',
  etym="av engelska winch med samma betydelse; besläktat med vinka",
  sl="SO: 'drag- eller hissanordning för förflyttning av last med hjälp av en lina som lindas på eller "
     "av en vals', EN betydelse, inget definitionstillägg -- matchar legacy exakt. SAOL: 'anordning "
     "för att dra eller lyfta last; vindspel' -- semikolonet ger 'vindspel' som ett eget led (SAOL:s "
     "egen konvention för alternativ benämning på SAMMA sak här, inte en andra betydelse -- SO har "
     "bara en betydelse och listar 'vindspel' som JFR:cohyponym, inte som en skild sense av ordet "
     "'vinsch'). 'vindspel' inleder sitt SAOL-led ordagrant -- belagd, oförändrad. Etymologi matchar "
     "SO. Ingen ändring behövs."),

"alstra": dict(
  hb="Få något -- t.ex. värme, elektricitet eller en känsla -- att uppstå, sällan en vanlig produkt",
  reg="formell, neutral",
  grp=[["skapa", "frambringa"]],
  ex='Genom friktionen mellan de två materialen <font color="#3498db">alstras</font> statisk '
     'elektricitet.',
  sl="SAKNAT DEFINITIONSTILLÄGG. SO: 'få att uppstå' med tillägget 'om fysikaliskt fenomen, känsla "
     "eller dylikt (sällan konkret produkt)' -- legacys 'Få något att uppstå eller bildas' saknade "
     "denna avgränsning helt (särskilt 'sällan konkret produkt', som skiljer alstra från vanliga "
     "'skapa/tillverka'). Tillagt med konkreta exempel (värme, elektricitet, känsla) hämtade ur SO:s "
     "egna syntex. SAOL: 'frambringa, skapa' -- båda orden inleder var sitt komma-led, fullt belagda "
     "(SO:s egna hänvisningar är JFR:cohyponym, inte SYN, så SAOL är källan här). Exempelmeningen "
     "matchar SO:s egen syntex ('genom friktionen alstras elektricitet') och illustrerar just "
     "fysikaliskt-fenomen-fallet -- oförändrad. Ingen etymologi finns i SO (fältet saknas helt i "
     "källan), lämnat null."),

"autokton": dict(
  hb="Uppvuxen på samma plats där den nu finns, om människor eller djur ; om jordlager: bildat av "
     "material från platsen själv",
  reg="formell, neutral ; fackspråklig, neutral, geologi",
  grp=[["inhemsk"], ["≈≈ ortsbildad"]],
  ex='De <font color="#3498db">autoktona</font> befolkningsgrupperna hade bott där i århundraden.',
  etym="till auto- och grekiska khthon 'jord'",
  sl="SO: 'uppvuxen på platsen i fråga' med definitionstillägget 'och alltså inte inflyttad; om "
     "människor el. djurformer' -- legacys 'Uppvuxen på samma plats som den finns på nu' fångade "
     "'inte inflyttad'-nyansen implicit men saknade den explicita avgränsningen till människor/djur. "
     "Tillagt. Underbetydelsen (typ 'äv. om geologisk avlagring') HAR egen definitionstext: 'som "
     "bildats ur material från den aktuella platsen' -- riktig andra betydelse, redan korrekt på "
     "kortet. SAOL: 'inhemsk', hela ledet, fullt belagd (matchar SO:s JFR-lista också). Kategorin "
     "'≈≈ ortsbildad' för geologibetydelsen är byggd ur kortets egen definition ('bildat av material "
     "från platsen'), ingen källa krävs för ≈≈. Etymologi matchar SO ordagrant."),

"avglans": dict(
  hb="Svagt ljus som speglas från något ; en svag antydan om något som en gång funnits",
  reg="ngt ålderdomlig, neutral",
  grp=[["återsken"], ["svag återstod"]],
  ex='Spegeln hade förlorat sin <font color="#3498db">avglans</font> efter många års användning.',
  etym="av förleden 'av-' och 'glans' -- alltså den svaga glans som är kvar",
  sl="SO: 'ljus som reflekteras från något' [ålderdomligt, SYN:synonym 'återsken'] + underbetydelse "
     "(typ 'särsk. bildligt') MED egen definition: 'svag antydan' (t.ex. 'en avglans av en svunnen "
     "skönhet') -- redan korrekt fångad som betydelse 2, bara omformulerad lite för Adam-tal ('blek "
     "rest av något som en gång var stort' -> 'svag antydan om något som en gång funnits', närmare "
     "SO:s ord och mindre överspecificerat, källan säger inte uttryckligen 'stort'). SAOL: 'svag "
     "återstod' [högt.] -- matchar bildlig-betydelsen bättre än ljus-betydelsen, inleder hela SAOL-"
     "ledet, fullt belagd för betydelse 2. REGISTER FÖRENKLAT till en rad (samma register gäller båda "
     "betydelserna, ingen källa skiljer dem åt). ETYMOLOGI ÄNDRAD: legacy hade 'till 1av 3 och glans "
     "1' -- en olöst SO-intern korsreferens (superskript+sifferkod), inte läsbar text. Löst till 'av "
     "förleden av- och glans' -- alltså 'den svaga glansen som är kvar', vilket faktiskt hjälper "
     "minnet (samma buggtyp som homofons etymologi i grupp 1)."),

"blickfång": dict(
  hb="Det område blicken överskådar ; det som drar till sig blicken, med eller utan avsikt",
  reg="neutral, neutral",
  grp=[["synfält"], ["≈≈ blickpunkt"]],
  ex='Den nya fabriken hamnade rakt i grannarnas <font color="#3498db">blickfång</font>.',
  sl="SO ger TVÅ huvudbetydelser: 'område som direkt överskådas av blicken' och 'något som naturligen "
     "fångar blicken' med definitionstillägget 'avsiktligt el. oavsiktligt' -- legacy hade redan båda "
     "betydelserna men saknade tillägget på betydelse 2 (tillagt: 'med eller utan avsikt'). SAOL: "
     "'synfält; ngt som fångar blicken' bekräftar samma tvådelning. REGISTER FÖRENKLAT till en rad "
     "(identiskt för båda leden, ingen anledning att upprepa). SYNONYM FIXAD: 'som fångar blicken' i "
     "betydelse 2 var bara ett ordagrant citat av SAOL:s definitionstext, inte ett fristående ord man "
     "kan sätta in (bryter mot regeln att ≈≈ ska vara ETT ord). Bytt mot '≈≈ blickpunkt', ett riktigt "
     "enda-ords kategoriord draget ur samma begrepp. 'synfält' inleder SAOL:s första led ordagrant, "
     "oförändrad. Exempelmeningen ('hamnade rakt i grannarnas blickfång' = kom inom deras synhåll) "
     "illustrerar betydelse 1, som star forst -- ratt. Ingen etymologi i kallan."),

"chiffer": dict(
  hb="Meddelande skrivet så att utomstående inte förstår det utan rätt kodnyckel ; sammanflätade "
     "bokstäver som bildar ett namntecken",
  reg="neutral, neutral ; fackspråklig, neutral, historia",
  grp=[["hemlig skrift"], ["≈≈ monogram"]],
  ex='Kryptologen lyckades forcera det tyska <font color="#3498db">chiffret</font> efter månader av '
     'arbete.',
  etym="av franska chiffre 'siffra; chiffer', äldre 'noll'; av arabiska sifr 'tom; noll'; jfr "
       "ursprung till siffra",
  sl="SAKNAT DEFINITIONSTILLÄGG. SO: 'meddelande vars språkliga form är förvriden så att det är "
     "obegripligt för utomstående' med tillägget 'och begripligt bara med hjälp av en kodnyckel' -- "
     "legacy saknade just kodnyckel-delen, vilket är det som skiljer ett chiffer från obegriplig "
     "text i allmänhet. Tillagt. Underbetydelsen 'äv. om monogram' (ingen egen definitionstext, men "
     "type-fältet pekar rakt på 'monogram' och morfex ger 'namnchiffer') -- redan korrekt fångad som "
     "betydelse 2. REGISTER ÄNDRAT: SO ger ingen bruklighetskommentar alls för huvudbetydelsen -- "
     "'formell' var en ogrundad gissning (samma mönster som desinficera/chiffer-poolens övriga kort "
     "i den här batchen, sannolikt kvarleva från innan 'neutral' fanns, style_guide.md 2026-08-10). "
     "Ordet är vardagligt känt (spionfilm, kodknäckning) -- neutral. 'hemlig skrift' inleder SAOL:s "
     "hela led, fullt belagd. '≈≈ monogram' oförändrad, extra stärkt av att SO:s eget typfält "
     "explicit namnger 'monogram'. Etymologi matchar SO ordagrant, hjälper minnet (chiffer <- siffra "
     "<- arabiska för 'noll'), oförändrad."),

"desinformation": dict(
  hb="Vilseledande information som sprids med avsikt",
  reg="neutral, negativ",
  grp=[["≈≈ propaganda"]],
  ex='Regeringen anklagades för att sprida <font color="#3498db">desinformation</font> om '
     'giftutsläppen.',
  etym="av engelska disinformation med samma betydelse; till latin dis- 'isär' och information",
  sl="SO: '(försök att överföra) vilseledande information' -- legacys 'Falsk information' var för "
     "SMALT: 'vilseledande' täcker även sant-men-missvisande/urklippt information, inte bara "
     "osanningar, vilket är den faktiska poängen med ordet (jfr moderna exempel: halvsanningar "
     "räknas som desinformation). Ändrat till 'vilseledande'. SYNONYM FIXAD: 'vilseledande "
     "information' var ett ordagrant citat av SO:s egen definitionstext, cirkulärt som synonym (kan "
     "inte sättas in som ett fristående ord). Bytt mot '≈≈ propaganda' -- kategorin ordet tillhör "
     "(en typ av vilseledande informationskampanj), draget ur kortets egen definition, ingen källa "
     "krävs för ≈≈. REGISTER ÄNDRAT: SO ger ingen bruklighetskommentar -- 'formell' var ogrundad "
     "(ordet är vardagligt vanligt i nyhetsspråk); bytt till neutral. Valören 'negativ' behållen -- "
     "ordet beskriver alltid en skadlig avsikt, äkta negativ laddning. bild_html BEVARAD oförändrad. "
     "Etymologi matchar SO."),

"feedback": dict(
  hb="Signal som går tillbaka till sändaren och styr det som händer sedan ; svar eller synpunkter på "
     "en idé eller prestation",
  reg="fackspråklig, neutral, teknik ; neutral, neutral",
  grp=[["återkoppling"], ["respons"]],
  ex='Auditiv <font color="#3498db">feedback</font> är nödvändig för att barn ska utveckla sitt tal.',
  etym="av engelska feedback med samma betydelse, till feed 'mata, föda' och back 'tillbaka'",
  sl="SO huvudbetydelse: 'det att (en del av) en utsänd signal går tillbaka till sändaren' med "
     "tillägget 'och reglerar den fortsatta aktiviteten' -- redan korrekt med på kortet ('styr det "
     "som händer sedan'), ingen ändring där. Underbetydelse (typ 'ofta om gensvar på en idé, en "
     "prestation eller dylikt', JFR:jämför 'respons') saknar egen definitionstext men beskriver "
     "tydligt vardagsbetydelsen -- legacys 'svar på hur någon presterat' täckte bara 'prestation', "
     "inte 'en idé' -- breddat till 'svar eller synpunkter på en idé eller prestation'. SYNONYM "
     "FIXAD: betydelse 1:s synonym 'återkoppling för reglering av process' var hela SAOL-"
     "definitionstexten ordagrant, inte ett fristående ord -- kortat till 'återkoppling' (det "
     "faktiska svenska ordet, bekräftat av SO:s egen JFR-hänvisning till 'återkoppling' och SAOL:s "
     "semikolon-avskilda första led). 'respons' inleder SAOL:s andra led ordagrant och matchar SO:s "
     "JFR:jämför för underbetydelsen -- fullt belagd, oförändrad. Exempelmeningen matchar SO:s egen "
     "syntex om språkutveckling, illustrerar betydelse 1 som står först -- korrekt. bild_html "
     "BEVARAD oförändrad. Etymologi matchar SO ordagrant, hjälper minnet (feed+back = mata "
     "tillbaka)."),
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    f = FIX.get(e["ord"])
    if not f:
        continue
    e["proposed"] = {
        "huvudbetydelse": f["hb"], "register": f["reg"],
        "synonymer": [s for g in f["grp"] for s in g],
        "synonym_groups": f["grp"], "exempelmening": f["ex"],
    }
    if f.get("etym"):
        e["proposed"]["etymologi"] = f["etym"]
    bild = (e.get("legacy") or {}).get("bild_html")
    if bild:
        e["proposed"]["bild_html"] = bild
    e["sokkoll"] = {"kalla": U(e["ord"]), "slutsats": f["sl"]}
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("godkande %d kort" % n)
