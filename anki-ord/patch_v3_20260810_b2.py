"""Batch 2, 2026-08-10 — 15 kort, tre källor + etymologi.

Korten i den här batchen var redan sökkollade 2026-08-09 och höll god
kvalitet. Det som tillförs är därför nästan uteslutande **etymologin** — och
den visar sig vara batchens största vinst: sex av femton ord får en koppling
till ett ord Adam redan kan (pöbel→populär, brokad→broccoli, beveka→vek,
bjugg→bygga, förvärva→värva, hävd→hava). Det är billigare att minnas ett ord
som hänger ihop med ett annat än ett ord som står ensamt.

Två idiom hämtades via GRUNDORDET, eftersom svenska.se bara tar enstaka
uppslagsord: `ett kok stryk` under **kok** och `av hävd` under **hävd**. Båda
uttrycken står som exempel i SO:s artikel för grundordet, alltså belagda av
samma källa som resten.
"""
import patchlib as pl

MAL = "sessions/session_2026-08-10_v3-tre-kallor-b2.json"
P = {}


def lagg(ord_, slutsats, kalla=None, **andr):
    P[ord_] = (kalla or pl.kallor(ord_), slutsats, andr)


lagg("bära sig",
     "BEKRÄFTAT, INGEN ÄNDRING. SO ger exakt kortets två betydelser: 'gå ihop "
     "ekonomiskt' och 'slumpa sig', med exemplen 'den lilla butiken bar sig "
     "inte längre' och 'det bar sig inte bättre än att han trillade i sjön'. "
     "SO saknar etymologi för uttrycket. ENDAST EN KÄLLA (svenska.se) — "
     "varken synonymer.se eller Wiktionary har uttrycket. Rödflaggas enligt "
     "Adams regel 2026-08-10.")

lagg("förvärva",
     "ETYMOLOGI TILLAGD. Kortets båda betydelser stämmer mot SO ('bli ägare "
     "till' / 'gradvis lära in'). SO lägger till en nyans kortet inte hade: "
     "ordet används **även om sådant man inte vill ha** — 'förvärva fiender'. "
     "Det är värt att veta, för det bryter mot magkänslan att förvärva = "
     "skaffa något bra.",
     huvudbetydelse="Få i sin ägo ; lära sig något gradvis — även om sådant "
                    "man inte vill ha, som fiender",
     etymologi="Samma ord som värva — att värva åt sig något.")

lagg("förvissning",
     "BEKRÄFTAT. SO: 'personlig, djupgående övertygelse', SAOL: 'visshet, "
     "fast övertygelse'. Kortets definition och exempel är hämtade rakt ur "
     "SO:s eget exempel. SO listar även en andra betydelse, 'det att vissna "
     "bort' (till förvissna), men den är en homograf och hör inte hemma på "
     "kortet — att blanda in den hade gjort kortet svårare, inte rikare. "
     "Ingen etymologi i SO för den här betydelsen.")

lagg("pöbel",
     "ETYMOLOGIN ÄR EN RIKTIG ÖGONÖPPNARE. Definitionen stämde. Men ordet "
     "kommer via fornfranskans *peuble* av latinets *populus* 'folk' — "
     "**samma ord som populär**. Ett nedsättande ord och ett positivt ord med "
     "samma ursprung; skillnaden ligger i vem som talar om folket.",
     etymologi="Av latinets populus, 'folk' — samma ord som populär.")

lagg("vråk",
     "ETYMOLOGI TILLAGD FÖR BÅDA BETYDELSERNA. Kortet har redan SO:s två "
     "uppslag rätt (rovfågeln och isrännan). SO ger skilda ursprung: fågeln "
     "till **vräka** i den äldre betydelsen 'förfölja', isrännan som variant "
     "av **råk**. Att de två betydelserna har olika ursprung förklarar varför "
     "ett så udda par sitter på samma ord — de är egentligen två ord.",
     etymologi="Fågeln av vräka, 'förfölja'; isrännan är samma ord som råk — "
               "två skilda ord som råkat bli lika.")

lagg("oväldig",
     "ETYMOLOGI TILLAGD. SO: 'rättvis', SAOL: 'opartisk', JFR objektiv, "
     "opartisk — kortet stämmer. Ordet är byggt på **väld**, ett utdött ord "
     "för partiskhet eller övervåld; o-väldig är alltså 'utan partiskhet'. "
     "Belagt sedan 1320-talet, vilket motiverar registret litterär.",
     etymologi="o- + väld, ett utdött ord för partiskhet — alltså 'utan "
               "partiskhet'.")

lagg("brokad",
     "ETYMOLOGIN BINDER IHOP TRE ORD. Definitionen stämmer (SO: 'tjockt, "
     "mönstrat sidentyg'). Ursprunget är italienskans *broccato*, till "
     "*brocco* 'spets, pinne' — **samma rot som broccoli och brosch**. Alla "
     "tre handlar om något som sticker ut: mönstret i tyget, blomknoppen, "
     "nålen. Kortets synonymer 'guldtyg, silvertyg' finns i ingen källa; SAOL "
     "beskriver guld-/silvertrådarna i definitionen, så innehållet är riktigt "
     "men orden är inte belagda som synonymer. Ersatta. "
     "TVÅ KÄLLOR: synonymer.se saknar uppslaget — rödflaggas.",
     synonymer=["sidentyg", "mönstervävt siden"],
     etymologi="Av italienskans brocco, 'spets' — samma rot som broccoli och "
               "brosch.")

lagg("förslagen",
     "ETYMOLOGIN GÖR ORDETS TON BEGRIPLIG. SO: 'som behärskar "
     "okonventionella, inte helt accepterade metoder', SAOL: 'slug, listig'. "
     "Kortet stämmer. Ursprunget förklarar varför ordet skaver: av tyskans "
     "*verschlagen*, troligen ursprungligen '**grundligt slagen, "
     "genompiskad**' — den som fått nog med stryk har lärt sig alla knep. "
     "OBS för egen del: SO blandar in substantivet *förslag* i samma "
     "artikel; det är ett annat ord och hör inte hit.",
     etymologi="Av tyskans verschlagen, troligen 'genompiskad' — den som "
               "lärt sig alla knep den hårda vägen.")

lagg("beskärm",
     "BEKRÄFTAT, REGISTRET SKÄRPT. SO: 'skydd och värn'. SO:s enda exempel är "
     "'**under den Allsmäktiges beskärm**' och synonymer.se märker ordet "
     "**(bibl.)** — ordet lever nästan bara i religiöst språk och i frasen "
     "'under någons beskärm', precis som kortet säger. Kortets exempel "
     "('under sin farmors beskärm') är därför bra, för det visar det "
     "vardagligare bruket. Registret ändras från arkaisk till litterär: "
     "arkaisk betyder utdött, och ordet används fortfarande.",
     register="litterär",
     etymologi="Samma ord som beskärma — att skärma av, alltså skydda.")

lagg("gensaga",
     "ETYMOLOGIN ÄR SJÄLVFÖRKLARANDE OCH BORDE STÅTT DÄR. SO: 'svar som "
     "bestämt uttrycker avvikande ståndpunkt'. Ordet är fornsvenskt "
     "*gensagha*: **gen-** betyder 'mot' (som i genmäle, gensvar) och "
     "**-saga** betyder 'tal'. Gensaga är alltså ordagrant 'mottal'. Det gör "
     "ordet härledbart i stället för utantillärt.",
     etymologi="gen- betyder 'mot' (som i genmäle) och -saga 'tal' — "
               "ordagrant 'mottal'.")

lagg("beveka",
     "ETYMOLOGIN ÄR HELA BETYDELSEN. SO: 'ändra eller mildra inställning hos "
     "någon genom vädjan'. Ordet kommer av lågtyskans *beweken* "
     "'**uppmjuka**' och hör ihop med **vek** — att beveka någon är att göra "
     "hen vek. Kortets definition säger redan 'få någon att mjukna', så "
     "etymologin bekräftar den exakt. SO:s exempel är dessutom minnesvärt: "
     "'Orfeus bevekte underjordens härskare med sin sång'. "
     "TVÅ KÄLLOR: Wiktionary saknar uppslaget — rödflaggas.",
     etymologi="Släkt med vek — att beveka någon är att göra hen vek.")

lagg("fisförnäm",
     "BEKRÄFTAT, INGEN ETYMOLOGI ATT GE. SO och SAOL ger båda samma enda "
     "förklaring: '**struntförnäm**'. Belagt först 1954, alltså ett modernt "
     "ord, och SO ger ingen historik. Kortets definition och exempel kommer "
     "ur SO. Synonymlistan utökas med belagda alternativ ur synonymer.se. "
     "TVÅ KÄLLOR: Wiktionary saknar uppslaget — rödflaggas.",
     synonymer=["struntförnäm", "struntviktig", "mallig", "högdragen"])

lagg("bjugg",
     "ETYMOLOGI TILLAGD. SO och SAOL ger båda 'sädesslaget korn'. Belagt "
     "sedan slutet av 1200-talet i Västgötalagen — bland de äldsta orden i "
     "hela decket. Ursprunget knyter ihop det med två ord Adam redan kan: "
     "bjugg är bildat till roten i **bygga** och **bo**, i den gamla "
     "betydelsen 'odla, så'. Att bo och odla var samma sak är själva poängen.",
     etymologi="Bildat till samma rot som bygga och bo, i den gamla "
               "betydelsen 'odla'.")

lagg("av hävd",
     "EN PÅHITTAD DEL STRUKEN, OCH ETYMOLOGIN TILLAGD. Kortet sa 'Enligt "
     "gammal tradition, **utan att någon vet varför**' — den sista delen "
     "finns i ingen källa. SO: hävd = 'sedvänja eller förhållande som länge "
     "varit förhärskande', med exemplet '**kulturlivet var av hävd ett "
     "privilegium för ett litet fåtal**'. Där vet man mycket väl varför; det "
     "handlar om att något är gammalt, inte om att skälet är glömt. "
     "Etymologin är dessutom klargörande: hävd är bildat till **hava** — "
     "hävd är det man länge HAFT. Belagt sedan 1200-talet. "
     "IDIOM: belagt via grundordet `hävd`, eftersom svenska.se bara tar "
     "enstaka uppslagsord.",
     kalla=pl.grundord("hävd"),
     huvudbetydelse="Enligt sedvänja som gällt så länge att den tas för given",
     synonymer=["av tradition", "sedan gammalt"],
     etymologi="hävd är bildat till hava — det man länge har haft.")

lagg("ett kok stryk",
     "GRUNDORDET FÖRKLARAR IDIOMET. SO listar '**ett kok stryk**' som exempel "
     "under uppslaget **kok**, där kok betyder '*mängd mat som kokas på en "
     "gång*' — alltså en PORTION. Ett kok stryk är en portion stryk, precis "
     "som ett kok äppelmos är en portion äppelmos. Det gör uttrycket "
     "härledbart. SO daterar idiomet till 1721 och jämför med '**få sina "
     "fiskar varma**'. Kortet saknade synonymer helt. "
     "IDIOM: belagt via grundordet `kok`.",
     kalla=pl.grundord("kok"),
     huvudbetydelse="En rejäl omgång stryk",
     synonymer=["smörj", "en omgång stryk"],
     etymologi="kok = en portion som kokas på en gång — alltså en portion "
               "stryk, som ett kok äppelmos.")


if __name__ == "__main__":
    pl.bygg(P, MAL)
