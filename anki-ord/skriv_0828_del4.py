# -*- coding: utf-8 -*-
"""Batch 2026-08-28, kort 53-69. Full v3."""
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


satt("membran",
     "Tunn, böjlig hinna som skiljer två sidor åt",
     "fackspråklig, neutral, biologi",
     ["hinna"],
     "Högtalarens " + B % "membran" + " vibrerade så att man kunde se det.",
     None,
     "SO: 'tunn (elastisk) hinna'. SAOL: 'tunn hinna'. hinna ar bada "
     "ordbockernas huvudord och darmed belagd. Legacys 'skiljevagg' ar "
     "struken -- ett membran ar mjukt och slapper ofta igenom nagot, en "
     "skiljevagg gor ingetdera. 'diafragma' star i ingen kalla.")

satt("nämnd",
     "Mindre grupp som utsetts att sköta ett bestämt område ; de vanliga "
     "medborgare som sitter med domaren i tingsrätten",
     "formell, neutral, politik ; formell, neutral, juridik",
     [],
     "Kommunens " + B % "nämnd" + " för kultur och fritid beslutade om "
     "bidraget.",
     None,
     "SO: '(mindre) grupp personer med vissa avgransade uppgifter' och 'del "
     "av domstol eller dylikt som bestar av lekman'. SAOL: 'underorgan till "
     "styrelse e.d.; radgivande grupp'. AVGRANSNING: SO:s trafflista "
     "innehaller ocksa 'kort omtala' och 'ingen namnd och ingen glomd' -- "
     "det ar perfekt particip av verbet NAMNA, ett annat uppslagsord, och "
     "hor inte hit. Utelamnat. Legacys 'utskott', 'kommitte' och "
     "'kommission' ar strukna: SO listar dem som JFR:cohyponym, inte "
     "SYN:synonym.")

satt("nåtla",
     "Sy ihop de delar av en sko som ligger ovanpå foten",
     "fackspråklig, neutral",
     [],
     "Skomakaren " + B % "nåtlade" + " ovanlädret innan sulan sattes fast.",
     None,
     "SO: 'sy ihop de olika delarna av ovanladret till', markerat 'delvis "
     "historiskt'. SAOL: 'sy ihop ovanlader'. Ordet ar alltsa specifikt for "
     "skotillverkning. Legacys andra definition ('sammanfoga tyg eller "
     "liknande material genom somnad') ar for vid -- den gor ordet till en "
     "synonym for 'sy', vilket det inte ar. Struken tillsammans med "
     "synonymerna 'sy', 'somma' och 'laska'.")

satt("oligarki",
     "Styre där makten ligger hos ett litet fåtal ; själva den lilla grupp "
     "som har makten",
     "fackspråklig, neutral, politik ; neutral, negativ",
     ["fåmannavälde"],
     "Landet styrdes i praktiken av en " + B % "oligarki" + " av fem "
     "familjer.",
     "→ Grekiska oligoi 'få' och arkhe 'välde'.",
     "SO: 'styrelsesatt dar makten utovas av ett fatal personer', med 'av. "
     "om gruppen av dessa personer' och 'numera ofta om grupp av ekonomiskt "
     "maktiga personer'. SAOL: 'famannavalde' -- SAOL:s hela definition och "
     "darmed belagd. Legacys 'fatalsvalde' och 'klickvalde' star i ingen "
     "kalla -- strukna. Legacy hade bara styrelseskicksbetydelsen; "
     "gruppbetydelsen (den vanligaste i dagens nyhetstext) saknades.")

satt("omaka",
     "Som inte hör ihop, till exempel två strumpor av olika sort ; omaka "
     "sig: göra sig besvär",
     "neutral, neutral ; ngt ålderdomlig, neutral",
     [],
     "Han kom ner till frukosten i två " + B % "omaka" + " strumpor.",
     None,
     "SO: 'som inte hor samman' och 'gora sig besvar'. SAOL bekraftar bada. "
     "Legacys 'olika', 'missmatchande' och 'oparig' ar strukna: oforenlig "
     "och olikartad ar SO:s JFR:cohyponym och de tre i legacy star i ingen "
     "kalla alls. 'olika' ar dessutom for brett -- tva olika saker behover "
     "inte vara omaka, det kravs att de borde ha hort ihop. Betydelse tva "
     "(omaka sig) saknades helt i legacy.")

satt("oskära",
     "Smutsa ner något heligt så att det inte längre räknas som rent",
     "arkaisk, negativ, religion",
     ["vanhelga", "besudla"],
     "Han menade att bygget skulle " + B % "oskära" + " den gamla "
     "begravningsplatsen.",
     None,
     "SARSKILT FALL: SO har ingen artikel for ordet. SAOL har det som "
     "uppslagsord med definitionen 'beflacka, besudla, vanhelga', markerat "
     "'ald.' och amnesomrade 'relig.'. Bada synonymerna star darmed i "
     "SAOL:s definitionstext och ar belagda. 'beflacka' ar utelamnad som "
     "tredje synonym for att inte upprepa samma sak tre ganger. Registret "
     "arkaisk kommer direkt ur SAOL:s ald.-markering.")

satt("pladask",
     "Rakt ner utan att kunna ta emot sig ; bildligt: bli blixtförälskad",
     "vardaglig, neutral ; vardaglig, positiv",
     ["huvudstupa", "handlöst"],
     "Hon föll " + B % "pladask" + " för hans skratt redan första kvällen.",
     "→ Ljudhärmande, en utbyggd form av plask.",
     "SO: 'helt utan kontroll over rorelsen', med 'av. bildligt' och "
     "exemplet 'hon foll pladask for hans charm'. SAOL: 'huvudstupa, "
     "handlost' -- bada star i SAOL:s definitionstext och ar belagda. "
     "Legacys 'raklang' ar struken: raklang beskriver hur man LIGGER "
     "efterat, pladask hur man faller. Den bildliga betydelsen saknades i "
     "legacy och ar den vanligaste i dagligt tal.")

satt("postskriptum",
     "Tillägg man skriver efter att brevet redan är avslutat och skrivet "
     "under",
     "formell, neutral",
     ["PS", "efterskrift"],
     "I ett " + B % "postskriptum" + " lade hon till att hon ändå tänkte "
     "komma.",
     "→ Latin post scriptum 'efter det skrivna'.",
     "SO: 'skrivet tillagg', med PS markerat SYN:synonym. SAOL: 'tillagg i "
     "brev, efterskrift' -- efterskrift star i SAOL:s definitionstext och ar "
     "belagd. epilog ar SO:s JFR:cohyponym och ar struken: en epilog "
     "avslutar ett verk, ett postskriptum kommer EFTER avslutningen. "
     "Legacys gemena 'ps' ar rattat till versalt PS.")

satt("primär",
     "Som kommer först och väger tyngst ; som utgör själva grunden man "
     "bygger vidare på",
     "neutral, neutral ; formell, neutral",
     ["ursprunglig"],
     "Bataljonens " + B % "primära" + " uppgift var att rädda liv.",
     None,
     "SO: 'som kommer i forsta hand' och 'grundlaggande, ursprunglig', med "
     "sekundar markerat som MOTSATS:antonym. SAOL: 'forsta, grundlaggande, "
     "forberedande, forstahands-; ursprunglig' -- ursprunglig star i bade "
     "SO:s och SAOL:s definitionstext och ar belagd. 'grundlaggande' ar "
     "utelamnad som synonym eftersom ordet redan bar betydelse tva och "
     "raden hade blivit cirkular.")

satt("pur",
     "Ren och oblandad ; framför ett känsloord: av rent och skärt",
     "neutral, neutral ; vardaglig, neutral",
     [],
     "De frågade av " + B % "pur" + " nyfikenhet.",
     None,
     "SO: 'ren och oforfalskad' och 'mycket', den senare med exemplen 'av "
     "pur gladje' och 'av pur nyfikenhet'. SAOL: 'ren, oforfalskad'. "
     "Legacys andra definition ('autentisk och av hogsta kvalitet utan "
     "forfalskning') ar bara en omskrivning av den forsta och missar SO:s "
     "faktiska andra betydelse: den forstarkande anvandningen i 'av pur "
     "X'. Rattat. 'ren' som synonym ar utelamnad -- det ar definitionsordet "
     "och raden hade blivit cirkular.")

satt("påkalla",
     "Kräva att något görs, ofta i lagtext ; kalla på någon för att få "
     "hjälp",
     "formell, neutral, juridik ; formell, neutral",
     ["begära"],
     "Han försökte " + B % "påkalla" + " lokförarens uppmärksamhet.",
     None,
     "SO: 'krava' (sarskilt i juridiska sammanhang) och 'tillkalla, kalla "
     "pa'. SAOL: 'begara; krava' -- begara star i SAOL:s definitionstext och "
     "ar belagd. 'krava' ar utelamnad som synonym eftersom det ar "
     "huvudbetydelsens eget ord. Legacys 'fordra' star i ingen kalla; "
     "legacys andra definition ('framkalla eller foranleda nagot att "
     "intraffa') ar fel -- det ar FORANLEDA, inte pakalla, och SO:s andra "
     "betydelse ar i stallet 'kalla pa'. Rattat.")

satt("rabiat",
     "Rasande på ett sätt man inte kan styra ; om åsikter: så hätsk att "
     "inget annat får plats",
     "neutral, negativ ; neutral, negativ",
     ["ursinnig"],
     "Han blev alldeles " + B % "rabiat" + " när hans bisysslor kom på tal.",
     "→ Till rabies — samma ord som sjukdomen rabies, rasande hos djur.",
     "SO: 'okontrollerat ursinnig', med 'ibland allmant forstarkande' och "
     "'av. om handling eller dylikt' (en rabiat motstandare, rabiata krav). "
     "SAOL: 'ursinnig, ettrig, inbiten' -- ursinnig star i bade SO:s och "
     "SAOL:s definitionstext och ar belagd. fanatisk ar SO:s JFR:cohyponym "
     "och ar inte inskriven. Legacys 'elak' ar struken: rabiat handlar om "
     "intensitet, inte om ondska.")

satt("sekvestrera",
     "Ta något i beslag med lagens stöd tills en tvist är avgjord",
     "fackspråklig, neutral, juridik",
     [],
     "Upplagan " + B % "sekvestrerades" + " och fick inte säljas förrän "
     "domen fallit.",
     None,
     "SARSKILT FALL: varken SO eller SAOL har ordet som uppslagsord (mätt: "
     "0 traffar i bada). Enda ordboken ar SAOB, som ar utforlig: 'belagga "
     "(ngt) med sekvester l. kvarstad; taga (ngt) i beslag, beslagta', med "
     "sarskilt (a) '(provisoriskt) beslagta (tryckalster) for att forhindra "
     "(dess) forsaljning l. spridning' och (b) om stat som tillfalligt "
     "lagger under sig ett omtvistat landomrade. Exempelmeningen bygger pa "
     "SAOB:s (a)-fall. ⚠️ Kortet vilar alltsa pa EN kalla, och den ar fran "
     "1967 -- SO:s och SAOL:s tystnad betyder att ordet ar pa vag ut ur "
     "bruket. Konfidens satt till 8 av det skalet.",
     conf=8,
     kalla="SAOB via https://www.saob.se/artikel/?seek=sekvestrera "
           "(hamtat 2026-08-28, HTTP 200, publicerad 1967). SO och SAOL "
           "kontrollerade via https://svenska.se/api/msearch?ord=sekvestrera "
           "-- 0 uppslagsordstraffar i bada.")

satt("sifon",
     "Flaska som trycker ut kolsyrad dryck med hjälp av gas ; hos musslor "
     "och andra vattendjur: röret som vatten sugs in och ut genom",
     "neutral, neutral ; fackspråklig, neutral, biologi",
     ["hävert"],
     "Musslan sticker upp sin " + B % "sifon" + " genom sanden.",
     "→ Grekiska siphon 'rör'.",
     "SO: 'anordning med havertmekanism for framstallning av kolsyrad "
     "dryck' och 'rorlik kroppsdel som utgor in- eller "
     "utstromningsoppning for omgivande vatten'. SAOL: 'havert, sugror; "
     "flaska med havert for servering av kolsyrad dryck' -- havert star i "
     "SAOL:s definitionstext och ar belagd. Legacys 'sprutflaska' star i "
     "ingen kalla och ar struken.")

satt("skavank",
     "Litet fel eller märke som drar ner värdet men inte förstör något",
     "neutral, lätt negativ",
     [],
     "Bordet hade ett par " + B % "skavanker" + ", så de fick det för halva "
     "priset.",
     None,
     "SO: 'mindre fel eller skada'. SAOL: 'mindre skada el. fel'. Legacys "
     "'defekt' ar struken: SO listar den som JFR:jamfor, inte SYN:synonym, "
     "och en defekt kan vara hur stor som helst medan en skavank per "
     "definition ar liten. 'fel' och 'brist' ar SO:s egna definitionsord "
     "och skulle bli cirkulara.")

satt("sly",
     "Tät samling tunna, unga skott från träd och buskar",
     "neutral, neutral",
     [],
     "Diket hade vuxit igen av " + B % "sly" + " på bara några år.",
     None,
     "SO: 'bestand av unga skott av trad eller buskar', med 'av. om enstaka "
     "sadant skott'. SAOL: 'tat vaxtlighet av buskar el. unga lovtrad'. "
     "Legacys 'smaskog', 'snarskog' och 'buskage' star i ingen av "
     "ordbockerna -- strukna. Wiktionarys tredje betydelse ('slug, listig') "
     "ar ett annat, homograft ord och hor inte hit.")

satt("stansa",
     "Slå ut ett hål eller en form ur tunt material med ett verktyg som "
     "pressas ner",
     "fackspråklig, neutral, teknik",
     [],
     "Maskinen " + B % "stansade" + " hundra brickor i minuten.",
     None,
     "SO: 'sla hal i (nagot) med stans', med 'spec. med avseende pa kort "
     "eller dylikt for datamaskin' (markerat historiskt). SAOL: 'sla hal i, "
     "skara ut med stans'. Legacys 'skara ut', 'stampla' och 'pragla' ar "
     "strukna: att pragla ar att trycka in ett monster utan att ta bort "
     "material, vilket ar motsatsen till att stansa, och 'stampla' har "
     "samma fel. Ingen av dem star som SYN:synonym.")

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Skrev %d kort." % sum(1 for k in KORT if k.get("approved")))
