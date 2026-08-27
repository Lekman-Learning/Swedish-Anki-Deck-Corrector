# -*- coding: utf-8 -*-
"""Batch 2026-08-28, kort 70-85. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
KALLA = ("SO och SAOL via https://svenska.se/api/msearch?ord=%s "
         "(hamtat 2026-08-28, HTTP 200)")
B = '<font color="#3498db">%s</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, grupper=None, tillat=None,
         conf=9, kalla=None):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": grupper, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": kalla or (KALLA % urllib.parse.quote(o)),
                    "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("stass",
     "De finaste kläderna man tar på sig när det är fest",
     "vardaglig, neutral",
     ["festdräkt"],
     "Han kom i bästa " + B % "stassen" + " till bröllopet.",
     None,
     "SO: 'festklader', markerat vardagligt. SAOL: 'stat, grannlat; "
     "festdrakt' -- festdrakt star i SAOL:s definitionstext och ar belagd. "
     "'grannlat' ar utelamnad: den betyder pyntande utsmyckning i "
     "allmanhet, inte klader. Legacys 'skrud' och 'gala' star i ingen "
     "kalla; 'gala' ar dessutom tillstallningen, inte klaeder. Strukna.")

satt("statisk",
     "Som står stilla och inte ändrar sig ; om elektricitet: laddning som "
     "blir kvar i ett material i stället för att flyta vidare",
     "neutral, neutral ; fackspråklig, neutral, fysik",
     ["stillastående"],
     "Tröjan var full av " + B % "statisk" + " elektricitet efter "
     "torktumlaren.",
     None,
     "SO ger tre poster: 'som har att gora med kroppars jamvikt under "
     "paverkan av krafter', 'som inte undergar forandring' och 'som inte "
     "aterspeglar en forandring som finns', med dynamisk som "
     "MOTSATS:antonym och 'statisk elektricitet' som eget exempel. SAOL: "
     "'stillastaende, inte dynamisk' -- stillastaende star i SAOL:s "
     "definitionstext och ar belagd. Legacys 'oforanderlig' och 'orubblig' "
     "star i ingen kalla; 'orubblig' ar dessutom fel -- statisk betyder att "
     "nagot INTE andrar sig, inte att det inte GAR att andra.")

satt("synnerlig",
     "Särskilt stor eller viktig — används mest i lagtext och högtidligt tal",
     "formell, neutral, juridik",
     [],
     "Straffet kan mildras om " + B % "synnerliga" + " skäl föreligger.",
     None,
     "SO: 'sarskilt stor eller viktig', markerat formellt, med 'spec. "
     "juridik' och exemplet 'om synnerliga skal foreligger'. SAOL: 'stor'. "
     "Legacys 'sarskild', 'utmarkt' och 'speciell' ar strukna: 'utmarkt' ar "
     "sakligt fel (synnerlig sager inget om kvalitet, bara om grad) och de "
     "tva andra star i ingen kalla som SYN:synonym. Den juridiska "
     "anvandningen, som ar den vanligaste, saknades helt i legacy.")

satt("talg",
     "Hårt djurfett som smälts ur, förr använt till ljus och tvål ; det "
     "feta som huden själv bildar",
     "neutral, neutral ; fackspråklig, neutral, medicin",
     [],
     "Ljusen var gjorda av " + B % "talg" + " och osade när de brann.",
     None,
     "SO: 'utsmalt fett av notkreatur' och 'fettrik substans som produceras "
     "i sarskilda kortlar i huden hos daggdjur'. SAOL: 'fast fett fran "
     "djur'. Legacys 'fett', 'sebum' och 'spack' ar strukna: flott, ister "
     "och spack ar SO:s JFR:cohyponym (olika sorters fett, inte samma "
     "sak), 'fett' ar overordnad term och 'sebum' ar latin, inte svenska. "
     "Hudbetydelsen fanns i legacys andra definition men inte i den "
     "forsta.")

satt("tertial",
     "Period på fyra månader — året delas i tre sådana",
     "formell, neutral, ekonomi",
     [],
     "Fonden steg åtta procent under årets första " + B % "tertial" + ".",
     "→ Latin tertialis 'som utgör en tredjedel', bildat efter mönster av "
     "kvartal.",
     "SO: 'period pa fyra manader'. SAOL: 'tredjedels ar'. 🔴 Legacys "
     "synonym 'kvartal' ar DIREKT FEL och den farligaste sortens fel pa "
     "det har kortet: ett kvartal ar TRE manader, ett tertial FYRA. SO "
     "listar kvartal som JFR:cohyponym just for att de ska halllas isar. "
     "Struken. Legacys andra definition ('tredje delen av ett kalenderar') "
     "ar tvetydig -- den kan lasas som 'den tredje delen' i stallet for 'en "
     "tredjedel'. Omskriven.")

satt("tjänlig",
     "Som duger till det man tänkt använda det till",
     "formell, neutral",
     ["lämplig", "användbar"],
     "Vattnet var inte " + B % "tjänligt" + " som dricksvatten.",
     None,
     "SO: 'anvandbar eller passande', med exemplet 'kottet var inte "
     "tjanligt som manniskofoda'. SAOL: 'lamplig, passande, anvandbar' -- "
     "bada synonymerna star i SAOL:s definitionstext och ar belagda.")

satt("trilsk",
     "Envis på ett sätt som gör att man vägrar följa med",
     "neutral, lätt negativ",
     ["omedgörlig"],
     "Hästen var " + B % "trilsk" + " och vägrade gå in i transporten.",
     None,
     "SO: 'enveten och motstravig'. SAOL: 'trotsig, omedgorlig' -- "
     "omedgorlig star i SAOL:s definitionstext och ar belagd. 'trotsig' ar "
     "utelamnad: trots riktar sig mot nagon, trilskhet behover ingen "
     "motpart. tredsk och trilskas ar SO:s JFR och ar inte inskrivna. "
     "Legacys 'envis' och 'egensinnig' star i ingen kalla som SYN:synonym.")

satt("tusenkonstnär",
     "Någon som kan lite av allt och löser det mesta praktiskt",
     "neutral, positiv",
     [],
     "En fastighetsskötare måste vara något av en " + B % "tusenkonstnär" +
     ".",
     None,
     "SO: 'person som ar skicklig pa manga (praktiska) omraden'. SAOL: "
     "'person som beharskar manga olika saker'. Legacys 'universalgeni' och "
     "'polyhistor' ar strukna och var sakligt fel: bada handlar om BREDD I "
     "KUNSKAP, medan SO uttryckligen sager PRAKTISKA omraden. En "
     "tusenkonstnar lagar saker, en polyhistor kan mycket. 'mangsysslare' "
     "star i ingen kalla.")

satt("täcka",
     "Lägga något över en yta så att den döljs ; räcka till för en kostnad ; "
     "omfatta ett helt område eller en hel tidsperiod",
     "neutral, neutral ; neutral, neutral ; neutral, neutral",
     [],
     "Hon " + B % "täckte" + " bordet med en duk innan gästerna kom.",
     None,
     "SO ger flera betydelser for verbet: 'lata (nastan) hela ytan av "
     "(nagot) doljas under eller bakom', 'lagga tak pa', 'dolja', 'ta "
     "hansyn till', 'breda ut sig over' och 'fylla (med innehall)'. "
     "⚠️ AVGRANSNING: SAOL:s rad 'vacker, natt' i samma trafflista hor till "
     "adjektivet TACK, ett annat uppslagsord med annat ursprung (fornsvenska "
     "thakker 'angenam'), inte till verbet tacka. Den ar utelamnad. Kortet "
     "tacker de tre vanligaste verbbetydelserna. Legacys tva definitioner "
     "var bada varianter av den forsta -- betydelserna 'racka till' och "
     "'omfatta' saknades helt.",
     tillat={"betydelse_kan_saknas":
             "SO:s sex poster ar i praktiken tre huvudlinjer (lagga over "
             "/ dolja, racka till, omfatta) plus tva specialfall (lagga "
             "tak pa, ta hansyn till). Kortet ger de tre huvudlinjerna."})

satt("uppdaga",
     "Få reda på något som var dolt",
     "formell, neutral",
     ["upptäcka"],
     "Fifflet " + B % "uppdagades" + " först flera år senare.",
     None,
     "SO: '(lyckas) skaffa fram kannedom om'. SAOL: 'upptacka, avsloja' -- "
     "upptacka star i SAOL:s definitionstext och ar belagd. 'avsloja' ar "
     "utelamnad: SO listar den som JFR:cohyponym, och att avsloja kraver "
     "att nagon berattar medan att uppdaga kan ske av sig sjalvt. Legacys "
     "'roja' star i ingen kalla.")

satt("upplag",
     "Plats där stora mängder av en vara ligger lagrade",
     "neutral, neutral",
     ["förråd"],
     "Åkern hade blivit ett " + B % "upplag" + " för gamla bilvrak.",
     None,
     "SO: 'plats dar stor mangd av en (typ av) vara forvaras'. SAOL: "
     "'upplagt forrad' -- forrad star i SAOL:s definitionstext och ar "
     "belagd. ⚠️ Ordet ska inte blandas ihop med UPPLAGA (antal tryckta "
     "exemplar av en bok), som ar ett annat uppslagsord. Legacys 'lager' "
     "och 'magasin' star i ingen kalla; 'magasin' ar dessutom en BYGGNAD, "
     "medan ett upplag oftast ligger utomhus.")

satt("utagerad",
     "Färdigt och avslutat, så att det inte är en fråga längre",
     "formell, neutral",
     ["slutbehandlad"],
     "Han får en tillsägelse, och därmed är saken " + B % "utagerad" + ".",
     None,
     "SO: 'fullstandigt slutford', med exemplet 'han far en tillsagelse och "
     "darmed far saken anses utagerad'. SAOL: 'slutford, slutbehandlad' -- "
     "slutbehandlad star i SAOL:s definitionstext och ar belagd. Legacys "
     "'avklarad' och 'avslutad' star i ingen kalla som SYN:synonym och "
     "missar nyansen OLD-facit faktiskt fangade: ordet anvands sarskilt om "
     "en KONFLIKT som inte langre ar ett problem.")

satt("vederlag",
     "Betalning man får för något man gjort eller lämnat ifrån sig ; i en "
     "byggnad: den del av muren som bär upp ett valv",
     "formell, neutral, juridik ; fackspråklig, neutral, teknik",
     [],
     "Hon gav ingenting utan " + B % "vederlag" + ".",
     "→ Lågtyska wedderlach, egentligen 'det som läggs emot'.",
     "SO ger tre betydelser: 'ersattning for (arbets)prestation', "
     "'avgangsvederlag' och 'byggnadsdel som utgor stod'. SAOL: "
     "'ersattning | murparti som stod for valv el. bage'. Kortet slar ihop "
     "SO:s tva forsta (avgangsvederlag ar ett specialfall av den forsta) "
     "och behaller byggnadsbetydelsen, som saknades helt i legacy. "
     "Legacys 'ersattning', 'lon' och 'gottgorelse' ar strukna: "
     "'ersattning' ar definitionsordet, betalning och lon ar SO:s "
     "JFR:cohyponym.")

satt("vädra",
     "Öppna fönster så att frisk luft kommer in ; hänga ut kläder i friska "
     "luften ; säga högt vad man tycker ; ana något innan det syns",
     "neutral, neutral ; neutral, neutral ; neutral, neutral ; neutral, "
     "neutral",
     [],
     "Han " + B % "vädrade" + " morgonluft när opinionssiffrorna vände.",
     None,
     "SO ger fyra linjer: 'slappa in frisk luft utifran', 'lata "
     "genomstrommas av frisk luft, lufta', 'lagga fram, visa' (vadra sitt "
     "missnoje) och 'anvanda sitt vaderkorn / ana' (vadra morgonluft). "
     "SAOL bekraftar tre av dem uttryckligen. Legacys BADA definitioner var "
     "samma sak (oppna fonster) -- tre av fyra betydelser saknades, "
     "inklusive de tva som HP faktiskt provar. Legacys synonymer 'lufta' "
     "och 'ventilera' ar SO:s JFR:cohyponym och ar strukna; 'oppna "
     "fonstret' ar ingen synonym alls.")

satt("ömsom",
     "Först det ena, sedan det andra, om och om igen",
     "neutral, neutral",
     ["växelvis"],
     "Publiken svarade " + B % "ömsom" + " med applåder, ömsom med burop.",
     None,
     "SO: 'i ett (annat) av de tva (eller flera) fallen eller tillfallena', "
     "med exemplet 'omsom vin, omsom vatten'. SAOL: 'vaxelvis' -- SAOL:s "
     "hela definition och darmed belagd. Legacys 'alternerande' och "
     "'omvaxlande' star i ingen kalla; 'omvaxlande' ar dessutom fel -- det "
     "beskriver att nagot ar varierat, inte att tva saker turas om.")

satt("överflygla",
     "Gå runt sidan på fienden och anfalla därifrån ; komma förbi någon och "
     "bli bättre",
     "fackspråklig, neutral, militär ; neutral, neutral",
     ["överträffa"],
     "Företaget blev " + B % "överflyglat" + " av konkurrenterna på två år.",
     "→ Tyska überflügeln, till flygel — arméns flygel är dess sida.",
     "SO: 'kringga flank hos' och 'overtraffa' (av. bildligt), med exemplen "
     "'Poros kavalleri overflyglades av Alexanders' och 'foretaget blev "
     "overflyglat av konkurrenterna'. SAOL: 'overtraffa | kringga och "
     "omfatta trupper' -- overtraffa star i SAOL:s definitionstext och ar "
     "belagd. Legacys 'kringga' och 'distansera' ar strukna: 'kringga' ar "
     "SO:s definitionsord och skulle bli cirkulart, 'distansera' star i "
     "ingen kalla. Legacys BADA definitioner var militara -- den bildliga "
     "betydelsen, som ar den vanligaste i dagens text, saknades.")

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Skrev %d kort." % sum(1 for k in KORT if k.get("approved")))
