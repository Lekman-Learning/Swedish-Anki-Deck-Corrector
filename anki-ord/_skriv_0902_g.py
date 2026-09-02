# -*- coding: utf-8 -*-
"""Batch G, sista: kort 117-134 utom smulgrat (124) och vox (133).

De fyra pauskandidaterna (strog 18, insomnia 96, smulgrat 124, vox 133) lamnas
UTAN proposed och UTAN approved. kortgranskare.py applicera hoppar over poster
som saknar bada, sa de faller ur automatiskt utan att blockera batchen.
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
 "kordial": "något högtidligt, formell",
 "kält": "dialektalt, vardaglig och nedsättande",
 "penitens": "mindre brukligt, formell och religiös",
}

K = {}

K["pråm"] = (
 "Flatbottnat och lågt lastfartyg som oftast bogseras",
 "neutral",
 ["flatbottnat lastfartyg"],
 None,
 "Grus fraktades på " + H % "pråm" + " längs kanalen.",
 None,
 "SO: 'flatbottnat (last)fartyg'. SAOL lagger till 'lagt' och 'langt'. FLATBOTTNINGEN ar "
 "det tekniskt avgorande - den gor att pramen kan ga pa grunt vatten och lastas hogt - och "
 "star darfor kvar. Att pramar oftast saknar egen framdrivning foljer av bruket och "
 "preciseras i huvudbetydelsen.")

K["påläggskalv"] = (
 "Ung person som anses lovande och därför gynnas av sina överordnade ; kalv som föds upp i "
 "avelssyfte",
 "neutral; betydelse 1 något nedsättande",
 ["person som anses lovande och därför gynnas av sina överordnade",
  "kalv som föds upp i avelssyfte"],
 [["person som anses lovande och därför gynnas av sina överordnade"],
  ["kalv som föds upp i avelssyfte"]],
 "Han pekades tidigt ut som partiets " + H % "påläggskalv" + ".",
 None,
 "TVA betydelser, bada egna SO-huvudbetydelser. Den bildliga star forst eftersom den ar "
 "den enda man moter i text; den bokstavliga (avelskalven) forklarar bilden och maste vara "
 "med for att uttrycket ska ga att minnas. GYNNANDET ar det som ger ordet dess latt "
 "nedsattande ton: en palaggskalv ar inte bara lovande utan utpekad och framfodd av andra.")

K["referens"] = (
 "Hänvisning till en källa ; person som kan intyga någons kvaliteter ; i språkvetenskap: "
 "förhållandet mellan ett uttryck och det som det syftar på",
 "formell; betydelse 3 fackspråklig",
 ["hänvisning", "rekommendation", "relation"],
 [["hänvisning"], ["rekommendation"], ["relation"]],
 "Han angav sin förra chef som " + H % "referens" + " i ansökan.",
 "latinets referre 'fora tillbaka, hanvisa'",
 "TRE praktiskt atskilda betydelser ur SO: den bibliografiska hanvisningen, PERSONEN man "
 "hanvisar till for upplysningar om nagon annan, och det sprakvetenskapliga forhallandet "
 "mellan uttryck och verklighet. Alla tre bar samma grundbild - att peka pa nagot annat - "
 "vilket etymologin sager. Den andra ar den vanligaste i vardagen (jobbansokan) och star "
 "i exempelmeningen.")

K["ringa"] = (
 "Telefonera ; låta en klocka ljuda ; som har liten omfattning, obetydlig ; omge något med "
 "en ring",
 "neutral; betydelse 3 formell",
 ["telefonera", "enkel", "rita ring omkring"],
 [["telefonera"], [], ["enkel"], ["rita ring omkring"]],
 "Skillnaden var " + H % "ringa" + " och påverkade inte resultatet.",
 None,
 "FYRA betydelser ur SO:s atta poster, och ordet ar en av batchens svaraste just for att "
 "de hor till olika ordklasser och rotter. Verbet ringa (telefonera, lata klocka ljuda) "
 "ar ett ord; adjektivet ringa (obetydlig) ar ett HELT ANNAT ord med samma form; verbet "
 "ringa (omge med ring) ett tredje. Adjektivbetydelsen ar den som provas - 'av ringa "
 "betydelse' - och star darfor i exempelmeningen, eftersom telefonbetydelsen ar sa "
 "dominerande att den annars skymmer allt.")

K["schäs"] = (
 "Liten fjädrande vagn som spänns efter häst",
 "neutral, historisk",
 ["fjädrande vagn som spänns efter häst"],
 None,
 "De åkte till kyrkan i en öppen " + H % "schäs" + ".",
 "franskans chaise 'stol'",
 "SO: 'typ av liten fjadrande vagn som spanns efter hast'. SAOL: 'i aldre tid: tva- el. "
 "fyrhjulig anspand vagn'. FJADRINGEN ar det som skiljer schasen fran en karra och star "
 "kvar. Ordet lever i nutida svenska nastan bara i uttrycket 'ur schasen', som betyder ur "
 "gangorna - men den anvandningen saknar ordboksbelagg har och skrivs inte in.")

K["skleros"] = (
 "Förhårdnad av kroppsvävnad",
 "fackspråklig, medicin",
 ["förhårdnad", "förhårdning"],
 None,
 "Åderförkalkning är en form av " + H % "skleros" + " i blodkärlens väggar.",
 "grekiskans skleros 'hard'",
 "SO och SAOL sager samma sak med olika avledning: 'forhardnad' respektive 'forhardning' "
 "av vavnader. Bada tas som synonymer. Ordet moter mest i sammansattningar "
 "(ateroskleros, multipel skleros), vilket exempelmeningen visar.")

K["skört"] = (
 "Nedhängande del av ett klädesplagg, nedanför midjan",
 "neutral",
 ["nedhängande del av klädesplagg"],
 None,
 "Kavajens " + H % "skört" + " var för långa för hans längd.",
 None,
 "SO: 'nedhangande del av kladesplagg'. SAOL: 'del av ett plagg som faller nedanom "
 "midjan'. MIDJEGRANSEN fran SAOL preciserar SO och tas med - ett skort ar inte vilken "
 "nedhangande del som helst. OBS: ordet ska inte forvaxlas med adjektivet 'skor' "
 "(sprod), som ar ett annat ord.")

K["specimen"] = (
 "Exemplar som får representera en hel typ ; vetenskaplig skrift som åberopas som merit "
 "vid ansökan om tjänst",
 "formell, fackspråklig",
 ["exemplar"],
 None,
 "Han lämnade in sin avhandling som " + H % "specimen" + " vid ansökan om lektoratet.",
 "latinets specimen 'prov, kannetecken', till specere 'se'",
 "TVA betydelser, bada egna SO-huvudbetydelser: 'exemplar' och 'vetenskaplig skrift att "
 "aberopa som merit'. Den andra ar akademisk svenska och helt osynlig fran den forsta - "
 "det ar den sorts betydelse ett prov fragar om. FUNKTIONEN 'far representera' ligger i "
 "ordets latinska rot (prov, kannetecken) och skiljer specimen fran 'exemplar' i "
 "allmanhet.")

K["suffix"] = (
 "Betydelsebärande orddel som sätts sist i ett ord",
 "fackspråklig, språkvetenskap",
 ["ändelse"],
 None,
 "I ordet \"löpare\" är -are ett " + H % "suffix" + " som gör verbet till ett substantiv.",
 "latinets suffixum 'fastsatt under', av sub- och figere 'fasta'",
 "TVA AV TRE KALLOR (wiktionary gav HTTP 429 aven vid omkorning). SO: 'betydelsebarande "
 "orddel som placeras i slutet av ett ord'. SAOL: 'avlednings- el. bojningsandelse t.ex. "
 "-are i lopare' - SAOL:s eget exempel anvands i exempelmeningen. BETYDELSEBARANDET ar "
 "poangen: ett suffix ar inte vilka slutbokstaver som helst utan en del som gor nagot med "
 "ordet. Motsatsen ar prefix.")

K["tilldragelse"] = (
 "Händelse, särskilt en märklig eller minnesvärd",
 "formell, ålderdomlig",
 ["händelse"],
 None,
 "Bröllopet var årets stora " + H % "tilldragelse" + " i byn.",
 None,
 "SO och SAOL ger bada 'handelse'. Ordet ar inte en ren synonym till handelse i bruk: en "
 "tilldragelse ar nagot som TILLDRAR sig uppmarksamhet, vilket ar varfor man aldrig sager "
 "det om vardagliga handelser. Preciseringen star i huvudbetydelsen som en "
 "bruksupplysning, medan 'handelse' behalls som den belagda synonymen.")

K["trankil"] = (
 "Lugn och oberörd",
 "vardaglig, något ålderdomlig",
 ["lugn", "obekymrad"],
 None,
 "Han satt " + H % "trankil" + " kvar medan alla andra sprang omkring.",
 "franskans tranquille 'lugn', av latinets tranquillus",
 "SO: 'lugn och oberord'. SAOL: 'obekymrad'. OBERORDHETEN ar det som skiljer trankil fran "
 "lugn: det ligger en antydan om att man BORDE reagera men later bli. Bada synonymerna "
 "godtas ur ordbokstexten.")

K["träaktig"] = (
 "Tråkig och fantasilös",
 "neutral, nedsättande",
 ["långtråkig", "trivial"],
 None,
 "Framställningen var " + H % "träaktig" + " och saknade varje spår av liv.",
 None,
 "TVA AV TRE KALLOR (wiktionary saknade artikel). SO: 'trakig och fantasilos'. SAOL: "
 "'langtrakig, trivial'. Ordet anvands om framstallning och stil, inte om personer, "
 "vilket foljer av bruket. Bilden ar tydlig: nagot torrt och livlost som tra.")

K["tråckla"] = (
 "Sy provisoriskt med långa stygn ; mödosamt få något till stånd",
 "neutral; betydelse 2 vardaglig",
 ["få till stånd"],
 [[], ["få till stånd"]],
 "Han " + H % "tråcklade" + " ihop en lösning på en timme kvällen före deadline.",
 None,
 "TVA betydelser ur SO: 'sy (tillfalligt) med langa stygn' och 'fa till stand' / "
 "'modosamt ta sig fram'. PROVISORISKHETEN ar det som binder ihop dem - en tracklad som "
 "haller bara tills den riktiga somnaden gors, och en tracklad losning haller bara "
 "tills nagot battre finns. Den bildliga ar den man moter oftast och star i "
 "exempelmeningen.")

K["tvärsnitt"] = (
 "Genomskärning av något vinkelrätt mot längdriktningen ; bildligt: representativt urval",
 "neutral; betydelse 1 fackspråklig",
 ["genomskärning"],
 None,
 "Undersökningen bygger på ett " + H % "tvärsnitt" + " av befolkningen.",
 None,
 "SO: 'genomskarning av ngt vinkelratt mot langdriktningen', plus en bildlig anvandning "
 "som SAOL markerar 'bildl.'. VINKELRATHETEN ar det tekniskt avgorande - ett snitt i "
 "annan vinkel ar inte ett tvarsnitt. Den bildliga betydelsen (ett urval som visar "
 "helheten) ar den vanligaste i samhallstext och star i exempelmeningen.")

K["viskositet"] = (
 "En vätskas eller gas inre friktion, dess seghet",
 "fackspråklig, fysik",
 ["seghet"],
 None,
 "Oljans " + H % "viskositet" + " sjunker när den värms upp.",
 "latinets viscosus 'seg, klibbig', till viscum 'mistel, fagellim'",
 "SO: 'inre friktion hos vatska el. gas'. SAOL: 'inre seghet hos vatska eller gas'. "
 "Kallorna anvander olika ord for samma sak - friktion respektive seghet - och bada star "
 "darfor i huvudbetydelsen. INRE ar viktigt: det ar friktionen mellan vatskans egna "
 "skikt, inte mot karlet.")

K["vågspel"] = (
 "Handling som medför stora risker",
 "formell, något ålderdomlig",
 ["handling som medför risker"],
 None,
 "Att satsa allt på ett kort var ett " + H % "vågspel" + " som kunde ha slutat illa.",
 None,
 "SO och SAOL ger bada 'handling som medfor risker'. Ordet bar en ton av medvetet tagen "
 "risk - ett vagspel ar inte en olycka utan nagot man ger sig in i - och forledet 'vag-' "
 "(jfr 'vaga') sager det. STORLEKEN pa risken preciseras i huvudbetydelsen; ett vagspel "
 "ar aldrig en liten chansning.")


TILLAT = {
 "referens": {"betydelse_kan_saknas":
   "SO raknar 5; tva ar underbetydelser utan egen definition. Kortets tre betydelser "
   "motsvarar SO:s tre riktiga def."},
 "ringa": {"betydelse_kan_saknas":
   "SO raknar 8. Kortets fyra betydelser tacker samtliga sarskiljbara innebordar; ovriga "
   "poster ar specialfall av klockbetydelsen (skollektion borjar/slutar) eller "
   "underbetydelser utan egen definition."},
 "schäs": {"betydelse_kan_saknas":
   "SO:s tva poster ar samma vagn beskriven av SO och SAOL med olika detaljer, inte tva "
   "betydelser. Ordet har en betydelse."},
 "skleros": {"betydelse_kan_saknas":
   "SO:s tva poster ar 'forhardnad' och 'forhardning' av vavnader - samma innebord med "
   "olika avledning. Ordet har en betydelse."},
 "skört": {"betydelse_kan_saknas":
   "SO raknar 7; posterna ar varianter av samma plaggdel plus underbetydelser utan egen "
   "definition. Ordet har en betydelse i den har stavningen."},
 "tilldragelse": {"betydelse_kan_saknas":
   "SO:s tva poster ar bada 'handelse'. Ordet har en betydelse."},
 "trankil": {"betydelse_kan_saknas":
   "SO:s andra post ar en underbetydelse utan egen definition. Ordet har en betydelse."},
 "träaktig": {"betydelse_kan_saknas":
   "SO:s poster ar varianter av samma trakighet ('trakig och fantasilos', 'langtrakig', "
   "'trivial') plus en underbetydelse utan egen definition. Ordet har en betydelse."},
 "tråckla": {"betydelse_kan_saknas":
   "SO raknar 5: 'fa till stand' och 'modosamt ta sig fram' ar samma bildliga betydelse i "
   "tva formuleringar, plus tva underbetydelser utan egen definition. Kortets tva "
   "betydelser tacker den bokstavliga och den bildliga."},
 "tvärsnitt": {"betydelse_kan_saknas":
   "SO:s extra poster ar markoren 'bildl.' och en underbetydelse utan egen definition. "
   "Kortets tva betydelser motsvarar den bokstavliga och den bildliga anvandningen."},
}


poster = json.load(io.open(FIL, encoding="utf-8"))
n = t = f = 0
for e in poster:
    o = e["ord"]
    if o in REG_FIX:
        e["proposed"]["register"] = REG_FIX[o]
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
print("batch G: %d kort, %d motiveringar, %d fix" % (n, t, f))
klara = sum(1 for e in poster if e.get("approved") and e.get("proposed"))
print("TOTALT skrivna: %d av %d (4 pauskandidater lamnade medvetet)" % (klara, len(poster)))
oskrivna = [e["ord"] for e in poster if not (e.get("approved") and e.get("proposed"))]
print("oskrivna:", ", ".join(oskrivna))
