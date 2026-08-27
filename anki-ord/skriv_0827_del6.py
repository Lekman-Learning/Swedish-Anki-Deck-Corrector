# -*- coding: utf-8 -*-
"""Batch 2026-08-27, kort 55-68. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-27_v3-batch.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
KALLA = ("SO och SAOL via https://svenska.se/api/msearch?ord=%s "
         "(hamtat 2026-08-27, HTTP 200)")
B = '<font color="#3498db">%s</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, tillat=None, conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": None, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": KALLA % urllib.parse.quote(o),
                    "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("relief",
     "Bild som är uthuggen så att den skjuter fram ur sin bakgrund ; "
     "bildligt: bakgrund som får något annat att framträda tydligare",
     "fackspråklig, neutral, konst ; litterär, neutral",
     ["upphöjd bild", "skärpa"],
     "Kapitälen var prydda med " + B % "reliefer" + " av runda löv.",
     "→ Franska relief, till relever 'lyfta åter'. Besläktat med relevant.",
     "SAOL: 'upphojd bild som framtrader mot en slat bakgrund; skarpa, "
     "motsats'. SO: 'skulpterad bild som springer fram ur en yta som utgor "
     "bakgrund' plus 'av. bildligt' ('nagra stank av vemod ger relief at "
     "solskenslyckan'). Den bildliga betydelsen ar den HP provar.",
     tillat={"betydelse_kan_saknas":
             "SO:s 4 poster ar 2 betydelser plus en JFR-tagg och en 'av. om "
             "andra liknande foreteelser' (tryckt relief), som ar samma "
             "betydelse i annat material."})

satt("repellera",
     "Stöta bort — trycka ifrån sig i stället för att dra till sig",
     "fackspråklig, neutral, fysik",
     ["stöta bort", "stöta tillbaka"],
     "Laddningar av samma slag " + B % "repellerar" + " varandra.",
     "→ Latin repellere 'stöta tillbaka'. Samma rot som repulsion.",
     "SAOL: 'stota bort, stota tillbaka' -- bada synonymerna leder var sitt "
     "led. SO: 'stota bort eller tillbaka', med MOTSATS:antonym attrahera. "
     "Paret repellera/attrahera ar det HP och fysiken staller upp.",
     tillat={"betydelse_kan_saknas":
             "SO:s andra post ar MOTSATS:antonym (attrahera) -- en "
             "relationstagg, inte en egen betydelse."})

satt("retuschera",
     "Ta bort småfel i en bild så att den ser bättre ut ; "
     "bildligt: putsa på en text tills det obekväma försvunnit",
     "neutral, neutral ; neutral, lätt negativ",
     ["bättra på", "försköna"],
     "Blåtiran hade " + B % "retuscherats" + " bort på tidningsbilden.",
     "→ Franska retoucher 'åter vidröra, förbättra'.",
     "SAOL: 'avlagsna smafel fran fotografi; battra pa, forskona' -- bada "
     "synonymerna leder var sitt led. SO ger aven 'av. bildligt' "
     "('propositionen hade retuscherats av finansutskottet'), vilket ar den "
     "andra betydelsen. JFR ger photoshoppa -- modernt och inte inskrivet.",
     tillat={"betydelse_kan_saknas":
             "SO:s 5 poster ar 2 betydelser plus en JFR-tagg och tva "
             "konstruktionsvarianter ('av. med konstruktionsvaxling')."})

satt("rikoschett",
     "Projektil som studsar och far vidare åt ett annat håll än den skulle",
     "fackspråklig, neutral",
     ["studsande projektil"],
     "Befälseleven fick splitter i benet av en " + B % "rikoschett" + ".",
     "→ Franska ricochet, ursprungligen om en ändlös rad frågor och svar.",
     "SAOL: 'projektils studsning; studsande projektil' -- ordet bar BADE "
     "sjalva studsen och foremalet som studsar. SO: '(del av) projektil som "
     "studsar och fortsatter i annan bana an den ursprungliga'.")

satt("rättfram",
     "Ärlig och rakt på sak, utan omvägar eller krusiduller",
     "neutral, positiv",
     ["öppenhjärtig", "uppriktig"],
     "Hon var så enkel och " + B % "rättfram" + " att alla tyckte om henne.",
     "→ Till rätt och fram — den som går rakt fram.",
     "SAOL: 'oppenhjartig, uppriktig' -- bada synonymerna leder var sitt led. "
     "SO: 'arlig och okonstlad'. SO:s exempel visar att ordet kan glida mot "
     "det burdusa ('rattframma och lite burdusa barn'), men grundvaloren ar "
     "positiv. JFR ger frimodig (cohyponym, ej inskriven).",
     tillat={"betydelse_kan_saknas":
             "SO:s andra post ar 'av. om handling eller dylikt' ('en rattfram "
             "fraga') -- samma betydelse om en handling i stallet for en "
             "person, inte en skild betydelse."})

satt("sakristia",
     "Sidorum i en kyrka där prästen byter om och de heliga föremålen förvaras",
     "fackspråklig, neutral, historia",
     ["rum med plats för skrudar och nattvardskärl"],
     "Prästen försvann in i " + B % "sakristian" + " och kom ut i full skrud.",
     "→ Medeltidslatin sacristia, till latin sacer 'helig'. Samma rot som sakral.",
     "SO: 'sidorum i kyrka, anvant som omkladningsrum for prasten och for "
     "forvaring av heliga foremal'. SAOL: 'rum med plats for skrudar och "
     "nattvardskarl i kyrka'. Bada definierar med en fras -- ordet har ingen "
     "enordssynonym.")

satt("sentera",
     "Uppskatta något och förstå vad som är bra med det",
     "högtidlig, positiv",
     ["uppskatta", "gilla"],
     "Han förstår att " + B % "sentera" + " ett gott vin.",
     "→ Latin sentire 'förnimma'. Samma rot som sinne och sensation.",
     "SAOL: 'uppskatta, gilla' -- bada synonymerna leder var sitt led. SO: "
     "'satta varde pa', markt 'nagot hogtidligt'. Ordet innehaller bade "
     "vardering OCH forstaelse -- man senterar inte nagot man bara rakar "
     "tycka om, utan nagot man begriper varfor det ar bra.",
     tillat={"betydelse_kan_saknas":
             "SO:s andra post ar 'el.' -- en formuleringsvariant av samma "
             "betydelse, inte en skild betydelse."})

satt("smäda",
     "Håna någon grovt och offentligt",
     "ngt ålderdomlig, negativ",
     ["skymfa", "håna"],
     "Tidigare var det straffbart att " + B % "smäda" + " kungafamiljen.",
     "→ Till lågtyska smade 'smälek'. Besläktat med försmädlig.",
     "SAOL: 'skymfa; hana' -- bada synonymerna leder var sitt led. SO: "
     "'utsatta for grovt nedsattande omdomen eller tillmalen'. Ordet 'grovt' "
     "ar poangen: att smada ar starkare an att kritisera eller reta.")

satt("statur",
     "En människas kroppsbyggnad — hur lång och kraftig hon är",
     "formell, neutral",
     ["gestalt", "växt", "kroppsbyggnad"],
     "Mannen var av kraftig " + B % "statur" + " och fyllde hela dörröppningen.",
     "→ Latin statura 'växt, gestalt'. Till status.",
     "SAOL: 'gestalt, vaxt, kroppsbyggnad' -- alla tre synonymerna leder var "
     "sitt led. SO: 'gestalt | kroppsbyggnad'. Pa engelska betyder stature "
     "aven anseende; det gor det INTE pa svenska, och den falskvannen ar "
     "vard att kanna till.",
     tillat={"betydelse_kan_saknas":
             "SO:s 3 poster ar 'gestalt | kroppsbyggnad' plus 'spec.' -- tva "
             "formuleringar av SAMMA betydelse (kroppens storlek och form) "
             "och en precisering. Kortet tacker den."})

satt("tadel",
     "Skarp kritik för något man gjort fel ; brist i någons karaktär",
     "ngt ålderdomlig, negativ ; ngt ålderdomlig, negativ",
     ["klander"],
     "Han gick fri från allt " + B % "tadel" + " trots att han varit med.",
     "→ Tyska Tadel.",
     "SO och SAOL sager bada 'klander'. SO ger aven '(karaktars)fel' som egen "
     "betydelse, belagd med 'en riddare utan fruktan och tadel' -- dar betyder "
     "ordet fel hos personen, inte kritik mot honom. Markt 'nagot "
     "alderdomligt'.",
     tillat={"betydelse_kan_saknas":
             "SO:s 3 poster ar 2 betydelser plus 'el.' -- en "
             "formuleringsvariant, inte en egen betydelse."})

satt("tension",
     "Spänning — i kemi och medicin om tryck eller spänning i ett ämne eller en vävnad",
     "fackspråklig, neutral, kemi",
     ["spänning"],
     "Mätningen visade förhöjd " + B % "tension" + " i vävnaden.",
     "→ Latin tendere 'spänna'. Samma rot som tensid.",
     "SAOL: 'spanning'. SO: '(kemisk) spanning' med tillagget 'spec. av. "
     "medicin'. 🔴 Ordet ar en FALSK VAN mot engelskans tension, som betyder "
     "spanning i vidare mening (aven psykisk och politisk). Pa svenska ar det "
     "en fackterm, och det ar just det HP kan prova.",
     tillat={"betydelse_kan_saknas":
             "SO:s andra post ar 'spec. av. medicin' -- samma begrepp "
             "(spanning) i en annan doman, vilket redan star i "
             "huvudbetydelsen."})

satt("tilltagsen",
     "Som vågar ta för sig och sätta igång själv — ibland lite väl mycket",
     "ngt ålderdomlig, neutral",
     ["företagsam", "påflugen", "framfusig"],
     "En " + B % "tilltagsen" + " ung man bad att få tala direkt med ministern.",
     "→ Till ta sig till. Samma bildning som tilltag.",
     "SAOL: 'driftig, foretagsam; paflugen, framfusig' -- ordet bar BADA "
     "valorerna, positiv och negativ, i samma post. SO: 'djarv och "
     "foretagsam'. 🔴 Det ar hela poangen med ordet och precis vad HP provar: "
     "'tilltagsen' ar inte entydigt berom. Valoren i registret ar darfor "
     "neutral -- den avgors av sammanhanget, inte av ordet.",
     tillat={"betydelse_kan_saknas":
             "SO:s andra post ar 'av. om handling och dylikt' ('tilltagsen "
             "impulsivitet') -- samma betydelse om en handling i stallet for "
             "en person."})

satt("trivial",
     "Så vanlig och vardaglig att den inte är värd att fästa sig vid ; "
     "så självklar att den syns direkt",
     "neutral, lätt negativ ; fackspråklig, neutral",
     ["alldaglig", "vanlig", "utnött"],
     "Mysteriet fick till slut en helt " + B % "trivial" + " förklaring.",
     "→ Latin trivialis 'alldaglig', till tri- och via 'väg' — det man hör i vägkorsningen.",
     "SAOL: 'alldaglig, vanlig; platt, utnott' -- alla tre synonymerna leder "
     "var sitt led. SO: 'som inte i vasentlig grad avviker fran det valkanda "
     "och alldagliga | mycket naturlig (och latt insedd)'. Den andra "
     "betydelsen ar matematikens ('trivial losning') och ar inte nedsattande "
     "-- darfor olika valor pa de tva betydelserna.",
     tillat={"betydelse_kan_saknas":
             "SO:s 3 poster ar 2 betydelser plus 'av.' -- en "
             "formuleringsvariant av den forsta."})

satt("vämjelig",
     "Så äcklig att man mår illa av den ; om något osynligt: moraliskt vidrig",
     "litterär, negativ ; litterär, negativ",
     ["äcklig", "motbjudande", "avskyvärd"],
     "Den " + B % "vämjeliga" + " stanken från soptippen låg kvar i kläderna.",
     "→ Fornsvenska vämieliker, till vämjas 'må illa'.",
     "SAOL: 'acklig'. SO: 'som vacker vamjelse' -- cirkular, sa "
     "huvudbetydelsen ar skriven ur SAOL och ur exemplen. SO ger aven 'av. om "
     "nagot abstrakt' ('vamjeligt fortal') som egen betydelse. motbjudande "
     "och avskyvard star i SO:s JFR-lista; de ar inskrivna enligt beslutet "
     "2026-08-27 att synonymfaltet ska ge HP-gangbara ord.",
     tillat={"synonym_utan_ordboksbelagg":
             "motbjudande och avskyvard star i SO:s JFR-lista. Beslut "
             "2026-08-27 (Adam): synonymfaltet ska ge de ord som kan dyka upp "
             "som ratt svar pa HP:s ORD-del, inte bara strikt utbytbara ord."})

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Totalt godkanda kort nu: %d" % sum(1 for k in KORT if k.get("approved")))
