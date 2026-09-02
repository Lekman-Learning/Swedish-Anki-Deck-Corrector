# -*- coding: utf-8 -*-
"""Batch F: kort 97-116 (instinkt .. proviant). Plus tre fix i batch E.

Registerkontrollen kraver att SO:s egna markord finns med i registerstrangen;
en synonym formulering rakas inte. Darfor star t.ex. 'nagot hogtidligt' och
'finl.' ordagrant i registren nedan.
"""
import io, json, os, sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02_v3-batch.json"
H = '<font color="#3498db">%s</font>'


def kallor(o):
    d = json.load(io.open(os.path.join("uppslag", o + ".json"), encoding="utf-8"))
    u = d.get("urler") or {}
    return " ".join(u[k] for k in ("svenska.se", "synonymer.se", "wiktionary") if u.get(k))


REG_FIX = {
 "blott": "något högtidligt, ålderdomligt utom i vissa uttryck",
 "disponent": "neutral, mest historisk; finl. om verkställande direktör",
}
FIX_TILLAT = {
 "gniden": {"frammande_uppslagsord":
   "Det frammande uppslagsordet ar verbet 'gnida', som particip-adjektivet gniden ar "
   "bildat till. Fritextsokningen drar med sig verbet; inget innehall darifran har "
   "anvants pa kortet."},
}

K = {}

K["instinkt"] = (
 "Inre drift som styr beteendet utan vilja eller tanke",
 "neutral",
 ["inre drift"],
 None,
 "Han duckade av ren " + H % "instinkt" + " innan han hann tänka.",
 "latinets instinctus 'ingivelse, drift'",
 "SO: 'inre drift som inte ar vilje- eller tankestyrd och som leder till visst beteende'. "
 "NEGATIONEN ar hela definitionen: instinkt definieras av vad den INTE ar - varken viljad "
 "eller tankt. Ett kort som bara sa 'inre drift' skulle inte skilja instinkt fran "
 "motivation.")

K["iteration"] = (
 "Fullständig och regelbunden upprepning ; i juridik: återfall i brott",
 "fackspråklig",
 ["upprepning", "återfall i brott"],
 [["upprepning"], ["återfall i brott"]],
 "Varje " + H % "iteration" + " av algoritmen kom närmare rätt svar.",
 "latinets iteratio 'upprepning', till iterum 'ater, an en gang'",
 "TVA betydelser, bada egna SO-huvudbetydelser: 'fullstandig och regelbunden upprepning' "
 "och 'aterfall i brott'. Den juridiska ar helt osynlig fran den vanliga och ar just den "
 "sorts betydelse ett prov fragar om. REGELBUNDENHETEN skiljer iteration fran upprepning "
 "i allmanhet.")

K["kalligrafi"] = (
 "Konsten att skriva vackert för hand",
 "neutral",
 ["skönskrift", "skönskrivning"],
 None,
 "Hon studerade japansk " + H % "kalligrafi" + " i tre år.",
 "grekiskans kallos 'skonhet' och graphein 'skriva'",
 "SO: 'konsten att astadkomma vacker skrift'. SAOL: 'skonskrift, skonskrivning'. Att det "
 "ar en KONST och inte bara en fardighet ligger i SO:s formulering och behalls; "
 "kalligrafi ar ett estetiskt hantverk, inte prydlig handstil.")

K["kardinalfel"] = (
 "Grundläggande fel som allt annat vilar på",
 "neutral",
 ["grundläggande fel"],
 None,
 "Att inte fråga kunden vad den ville ha var projektets " + H % "kardinalfel" + ".",
 "till latinets cardo 'dorrhange, vandpunkt' - det som allt vrider sig kring",
 "SO och SAOL ger bada 'grundlaggande fel'. GRUNDLAGGANDET ar inte samma sak som 'stort': "
 "ett kardinalfel ar det fel som allt annat foljer av, inte nodvandigtvis det mest "
 "synliga. Etymologin (dorrhanget som allt vrider sig kring) sager samma sak och star "
 "kvar for att gora skillnaden minnesvard.")

K["konfession"] = (
 "Trosbekännelse",
 "fackspråklig, religion",
 ["trosbekännelse"],
 None,
 "Skolan är fristående från varje " + H % "konfession" + ".",
 "latinets confessio 'bekannelse', till confiteri 'bekanna'",
 "SO och SAOL ger bada enbart 'trosbekannelse'. Ordet anvands i praktiken ocksa om det "
 "SAMFUND som omfattar bekannelsen (jfr 'konfessionslos skola'), men den anvandningen "
 "saknar ordboksbelagg i de hamtade kallorna och skrivs darfor INTE in i "
 "huvudbetydelsen - exempelmeningen visar bruket utan att pasta betydelsen.")

K["kordial"] = (
 "Hjärtlig och förtrolig",
 "formell, ålderdomlig",
 ["hjärtlig", "förtrolig"],
 None,
 "Stämningen mellan dem var " + H % "kordial" + " trots meningsskiljaktigheterna.",
 "latinets cor 'hjarta'",
 "SO: 'hjartlig och fortrolig'. Bada leden godtas som synonymer ur definitionstexten. "
 "Etymologin (cor = hjarta) ar samma bild som i svenskans 'hjartlig' och gor ordet latt "
 "att halla kvar.")

K["korist"] = (
 "Medlem av en kör",
 "neutral",
 ["körmedlem"],
 None,
 "Som " + H % "korist" + " sjöng han andra tenor i tjugo år.",
 None,
 "SO: 'medlem av kor'. SAOL: 'kormedlem'. Entydigt. Ordet ar en ren yrkes-/rollbeteckning "
 "utan vardering, vilket registret markerar som neutralt.")

K["kväsa"] = (
 "Kuva någon och göra honom ödmjuk",
 "vardaglig",
 ["kuva", "stuka"],
 None,
 "Ett enda svar från läraren " + H % "kväste" + " honom för resten av lektionen.",
 None,
 "SO: 'gora (nagon) odmjuk'. SAOL: 'kuva, stuka'. ODMJUKHETEN ar resultatet som ingar i "
 "betydelsen - att kvasa nagon ar inte att besegra utan att fa personen att sluta hava "
 "sig, och det ledet star darfor kvar i huvudbetydelsen.")

K["kält"] = (
 "Upprepat småtjat",
 "vardaglig, nedsättande",
 ["upprepat småtjat"],
 None,
 "Hon gav efter till slut, mest för att slippa hans " + H % "kält" + ".",
 None,
 "TVA AV TRE KALLOR (wiktionary saknade artikel). SO och SAOL ger bada 'upprepat "
 "smatjat'. BADA leden bar betydelsen: upprepningen och smaskaligheten. Kalt ar inte "
 "hogljudda krav utan idelig gnat om smasaker.")

K["lidelse"] = (
 "Stark och dominerande känsla ; stark åtrå",
 "formell, högtidlig",
 ["passion", "åtrå"],
 [["passion"], ["åtrå"]],
 "Han talade om saken med en " + H % "lidelse" + " som överraskade alla.",
 None,
 "TVA betydelser, bada egna SO-huvudbetydelser: 'stark och dominerande kansla' och 'stark "
 "atra'. DOMINANSEN ar det som skiljer lidelse fran kansla i allmanhet - en lidelse tar "
 "over. Ordet ar besläktat med 'lida' och bar darfor en ton av att kanslan drabbar en "
 "snarare an valjs.")

K["lingua franca"] = (
 "Gemensamt hjälpspråk mellan människor som saknar gemensamt modersmål",
 "fackspråklig, språkvetenskap",
 ["blandspråk"],
 None,
 "Engelska fungerar som " + H % "lingua franca" + " på de flesta internationella konferenser.",
 "italienskans 'frankiskt sprak', ursprungligen handelssprakret i Medelhavet",
 "ENDAST SO har artikel (SAOL saknar uppslagsordet). SO: 'blandsprak som ar fattbart for "
 "alla sprakbrukare'. Huvudbetydelsen preciserar FUNKTIONEN i stallet for formen: ett "
 "lingua franca behover inte langre vara ett blandsprak (engelskan ar det inte), utan "
 "definieras av att det anvands mellan parter utan gemensamt modersmal. Det ar sa ordet "
 "faktiskt anvands idag.")

K["metamorfos"] = (
 "Genomgripande förvandling ; i biologi: övergång från ett utvecklingsstadium till ett annat",
 "formell; betydelse 2 fackspråklig",
 ["förvandling", "omdaning"],
 [["förvandling", "omdaning"], []],
 "Larvens " + H % "metamorfos" + " till fjäril tar omkring två veckor.",
 "grekiskans metamorphosis 'omgestaltning', av meta- 'om' och morphe 'form'",
 "SO ger flera poster; kortet bar de tva praktiskt atskilda: den allmanna 'genomgripande "
 "forandring' och den biologiska 'overgang fran ett utvecklingsstadium till ett annat'. "
 "Den biologiska ar snavare och den ordet oftast moter i, men den allmanna anvands lika "
 "mycket bildligt. GENOMGRIPANDE ar nyckeln - en metamorfos ar inte en justering.")

K["nostalgi"] = (
 "Vemodig men njutningsfylld längtan tillbaka till något förlorat",
 "neutral",
 [],
 None,
 "Låten väckte en oväntad " + H % "nostalgi" + " efter somrarna på landet.",
 "grekiskans nostos 'hemkomst' och algos 'smarta'",
 "SO: 'vemodig men njutningsfylld langtan hem eller tillbaka till nagot forlorat'. "
 "PARADOXEN ar hela ordet - kanslan ar samtidigt smartsam och angenam - och maste sta "
 "kvar. Etymologin sager bokstavligen 'hemkomstsmarta'. Poolen ger bara fragment och hela "
 "definitionsstrangar, sa synonymfaltet lamnas tomt.")

K["näsvis"] = (
 "Som svarar fräckt och respektlöst ; närgången och indiskret",
 "neutral, nedsättande",
 ["uppnosig", "indiskret"],
 [["uppnosig"], ["indiskret"]],
 "Svaret var " + H % "näsvist" + " nog för att han skulle bli utvisad från lektionen.",
 None,
 "TVA betydelser i SO: 'som svarar pa ett frackt satt' och 'indiskret'. Den forsta ror "
 "TONEN i ett svar, den andra att man lagger sig i det man inte har med att gora. Bada "
 "star pa kortet. Ordet anvands mest om barn och yngre, vilket foljer av att det "
 "forutsatter en overordnad som blir nasvist bemott.")

K["paleontologi"] = (
 "Vetenskapen om utdöda växter och djur som bevarats som fossil",
 "fackspråklig, geologi och biologi",
 [],
 None,
 "Fyndet av benen blev en vändpunkt inom svensk " + H % "paleontologi" + ".",
 "grekiskans palaios 'gammal', on 'varelse' och logia 'lara'",
 "TVA AV TRE KALLOR (synonymer.se saknade artikel). SO: 'laran om de utdoda vaxter och "
 "djur som bevarats i form av fossil i geologiska avlagringar'. SAOL: 'vetenskapen om "
 "fossila organismer'. FOSSILEN ar avgransningen - paleontologi handlar om det som "
 "bevarats, inte om forntida liv i allmanhet. Poolen ger bara hela definitionsstrangar, "
 "sa synonymfaltet lamnas tomt.")

K["pampig"] = (
 "Ståtlig och imponerande",
 "vardaglig",
 ["ståtlig"],
 None,
 "Entrén var " + H % "pampig" + " med marmortrappa och pelare.",
 None,
 "SO och SAOL ger bada 'statlig och imponerande'. Ordet ar positivt men vardagligt - det "
 "gar inte att anvanda i formell text om samma sak, dar 'statlig' vore ratt. Registret "
 "markerar det.")

K["penitens"] = (
 "Botgöring, straff man tar på sig för att sona något",
 "formell, religiös",
 ["botgöring"],
 None,
 "Han gjorde " + H % "penitens" + " genom att arbeta gratis hela sommaren.",
 "latinets paenitentia 'anger', till paenitere 'angra'",
 "SO och SAOL ger bada 'botgoring'. FRIVILLIGHETEN ar det som skiljer penitens fran "
 "straff: man tar det pa sig, det doms inte ut. Det ledet star i huvudbetydelsen eftersom "
 "'botgoring' ensamt kan lasas som pafort. Etymologin ('anger') bekraftar riktningen.")

K["proaktiv"] = (
 "Som i förväg vidtar åtgärder i stället för att vänta och reagera",
 "neutral, fackspråklig",
 ["förebyggande", "förutseende"],
 None,
 "Ett " + H % "proaktivt" + " underhåll byter delarna innan de går sönder.",
 "bildat till reaktiv med prefixet pro- 'i forvag'",
 "SO: 'inriktad pa att i forvag vidta lampliga atgarder'. KONTRASTEN mot reaktiv ar hela "
 "poangen med ordet - det bildades som motsats till reaktiv - och skrivs darfor ut i "
 "huvudbetydelsen. Utan den blir 'proaktiv' bara ett finare ord for 'aktiv'.")

K["proper"] = (
 "Snygg och välvårdad ; socialt acceptabel och anständig",
 "neutral",
 ["snygg", "välvårdad", "sober"],
 [["snygg", "välvårdad"], ["sober"]],
 "Han kom i " + H % "propra" + " kläder och nyputsade skor.",
 "franskans propre 'ren, egen', av latinets proprius",
 "TVA betydelser i SO: 'snygg och ordentlig' och 'socialt acceptabel'. Den andra ar den "
 "overraskande - 'en proper losning' handlar inte om utseende utan om att nagot gar att "
 "forsvara offentligt. Bada star pa kortet.")

K["proviant"] = (
 "Förråd av mat som tas med på en resa",
 "neutral",
 ["vägkost", "förråd av livsmedel"],
 None,
 "De packade " + H % "proviant" + " för fyra dagar i fjällen.",
 "latinets providere 'sorja for'",
 "SO: 'forrad av mat som ar avsett att anvandas vid resa eller dylikt'. RESAN ar med i "
 "definitionen - proviant ar inte matforrad i allmanhet utan det man tar med sig. SAOL "
 "ger 'vagkost', som bar samma sak i ett ord.")


TILLAT = {
 "instinkt": {"betydelse_kan_saknas":
   "SO raknar 4; de extra ar underbetydelser utan egen definition och en narliggande "
   "variant ('spontan tendens till visst beteende'). Ordet har en betydelse."},
 "iteration": {"betydelse_kan_saknas":
   "SO:s tredje post ar en underbetydelse utan egen definition. Kortets tva betydelser "
   "motsvarar SO:s tva riktiga def."},
 "kalligrafi": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse."},
 "kardinalfel": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse."},
 "kväsa": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse."},
 "lidelse": {"betydelse_kan_saknas":
   "SO:s tredje post ar en underbetydelse utan egen definition. Kortets tva betydelser "
   "motsvarar SO:s tva riktiga def."},
 "lingua franca": {"betydelse_kan_saknas":
   "SO raknar 4; tre ar underbetydelser utan egen definition. Flerordsuttrycket har en "
   "betydelse."},
 "metamorfos": {"betydelse_kan_saknas":
   "SO raknar 5: tre def varav 'genomgripande forandring' och 'fullstandig omvandling av "
   "uppbyggnad' ar samma innebord, plus tva underbetydelser utan egen definition. Kortets "
   "tva betydelser tacker de sarskiljbara (allman och biologisk)."},
 "näsvis": {"betydelse_kan_saknas":
   "SO:s tredje post ar en underbetydelse utan egen definition. Kortets tva betydelser "
   "motsvarar SO:s tva riktiga def."},
 "proaktiv": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse."},
 "proper": {"betydelse_kan_saknas":
   "SO:s tredje post ar en underbetydelse utan egen definition. Kortets tva betydelser "
   "motsvarar SO:s tva riktiga def."},
}


poster = json.load(io.open(FIL, encoding="utf-8"))
n = t = f = 0
for e in poster:
    o = e["ord"]
    if o in REG_FIX:
        e["proposed"]["register"] = REG_FIX[o]
        f += 1
    if o in FIX_TILLAT:
        e.setdefault("forgranska_tillat", {}).update(FIX_TILLAT[o])
        f += 1
    d = K.get(o)
    if d:
        hb, reg, syn, grp, ex, etym, slut = d
        e["proposed"] = {"huvudbetydelse": hb, "register": reg, "synonymer": syn,
                         "synonym_groups": grp, "exempelmening": ex, "etymologi": etym}
        e["sokkoll"] = {"kalla": kallor(o), "slutsats": slut}
        e["approved"] = True
        n += 1
    if o in TILLAT:
        e.setdefault("forgranska_tillat", {}).update(TILLAT[o])
        t += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("batch F: %d kort, %d motiveringar, %d fix" % (n, t, f))
saknas = [o for o in K if not any(e["ord"] == o for e in poster)]
print("ord i K som inte fanns:", saknas or "inga")
