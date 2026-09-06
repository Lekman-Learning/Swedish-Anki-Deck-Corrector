# -*- coding: utf-8 -*-
"""Rattelser och verifierade falsklarm for sats 2, ord 21-40.

Fem av korten ar FLERORDSUTTRYCK, och for dem ar sifferflaggorna systematiskt
falska: svenska.se har ingen artikel for frasen, sa fritextsokningen matchar
delorden -- 'vara', 'sagt', 'darom', 'lans' -- och drar in 29-44 orelaterade
lemman vars betydelser och brukligheskommentarer sedan rakas. Det ar det
dokumenterade monstret fran 'ga i clinch' och 'karringen mot strommen'
(CLAUDE.md 2026-08-19). Var och en ar anda provad enskilt mot rastrukturen.

En andring i sak: histrions 'komediant'.
"""
import io, json

FIL = "sessions/session_2026-09-06_v3-omgranskning2.json"

_FRAS = ("Flerordsuttryck utan egen artikel i svenska.se. Fritextsokningen matchar "
         "delorden och drar in {n} orelaterade lemman ({ex}). ")

T = {
 "lov": {
  "frammande_uppslagsord": (
   "Det enda doljda lemmat ar GUDSKELOV, en sammansattning med lov som efterled och "
   "ett eget uppslagsord -- ingen betydelse hos lov. Ingen glosa pa kortet kommer "
   "darifran."),
  "betydelse_kan_saknas": (
   "Rakningen pa tio summerar aven underbetydelser utan egen definitionstext. "
   "Rastrukturen visar FYRA SO-lemman med sammanlagt FEM definitioner: (1) 'kursandring i "
   "riktning mot vinden' + underbetydelsen 'svang, gir' (som HAR egen text men ar samma "
   "rorelse), (2) 'tillatelse' OCH 'skyldighet' -- tva egna definitioner, (3) 'tid av "
   "ledighet fran skolundervisning', (4) 'starkt berom'. Underbetydelserna till (2) och "
   "(4) ar samtliga markta '(ingen egen definition -- utvidgning)'. Kortet har alla fem "
   "sanna betydelserna, vilket ar fyra fler an legacy hade.")},

 "vara (p)å färde": {
  "frammande_uppslagsord": _FRAS.format(n=29, ex="-vis, bestandig, dement, fara, fard") + (
   "SO-LEMMA farde har TOM definition -- ordet existerar bara i den har frasen. Kortet "
   "vilar darfor pa OLD-facit ('forsigga, halla pa att ske'), som stammer med legacys "
   "text."),
  "betydelse_kan_saknas": (
   "Rakningen galler verbet VARA (paga, befinna sig, kunna beskrivas som, kunna "
   "klassificeras som), inte frasen. Frasen har en betydelse."),
  "register_motsager_markning": (
   "Markningen 'alderdomligt' sitter pa en underbetydelse till verbet VARA i "
   "rastrukturen ('under: (ingen egen definition -- utvidgning) [brukl: alderdomligt]'), "
   "inte pa frasen. 'Nagot ar pa farde' ar levande svenska -- det forekommer i "
   "nyhetstext och deckare -- och SO-LEMMA farde bar ingen brukligheskommentar alls.")},

 "vara läns på": {
  "frammande_uppslagsord": _FRAS.format(n=39, ex="-vis, assessor, flans, lans, lins, lan") + (
   "Kortets innehall kommer fran SO-LEMMA lans (adjektiv) 'fri fran vatten' <<om bat>>, "
   "som ar frasens ursprung, plus OLD-facit ('vara tom pa')."),
  "betydelse_kan_saknas": (
   "Rakningen summerar lans-lemmanas sjofartsbetydelser (segling i vindens riktning; "
   "kedja av flytande stockar vid flottning) och verbet vara. Ingen av dem ar den "
   "overforda anvandning frasen har. Frasen har en betydelse.")},

 "snart sagt": {
  "frammande_uppslagsord": _FRAS.format(n=43, ex="sa, saft, saga, sagg, sagga, sagla") + (
   "Sokningen har traffat pa 'sagt' och dragit in halva sa-uppslaget. Kortet vilar pa "
   "OLD-facit ('sa gott som, nastan')."),
  "betydelse_kan_saknas": (
   "Rakningen galler adverbet SNART ('inom kort', 'om en liten stund', '(genast) nar') "
   "och verbet SAGA -- alltsa TIDSbetydelser och talbetydelser, ingen av dem den "
   "grad-betydelse frasen har. Frasen har en betydelse."),
  "register_motsager_markning": (
   "Markningen 'nagot alderdomligt' sitter pa ett av de indragna lemmana, inte pa "
   "frasen. Varken SO-LEMMA snart eller nagot led i SAOL:s snart-artikel bar den "
   "kommentaren. 'Snart sagt omojligt' ar vanlig sakprosa -- det forekommer i "
   "ledarartiklar och myndighetstext.")},

 "vara trakterad av": {
  "frammande_uppslagsord": _FRAS.format(n=44, ex="av, bara, fara, taktera, tara, trad") + (
   "Kortets innehall kommer i sin helhet fran SO-LEMMA trakterad (adjektiv) 'som "
   "reagerar positivt' <<pa visst bemotande eller dylikt>> -- en ren traff som tacker "
   "hela definitionen."),
  "betydelse_kan_saknas": (
   "Rakningen galler verbet och substantivet VARA (paga, befinna sig, kunna beskrivas "
   "som, foreteelse som ar foremal for handel ...). SO-LEMMA trakterad har EN definition "
   "utan underbetydelser, vilket ar vad kortet har.")},

 "därom tvista de lärde": {
  "frammande_uppslagsord": _FRAS.format(n=30, ex="a vista, bevista, brista, farde, gnista") + (
   "Sokningen har traffat pa 'tvista' och 'larde' var for sig. Kortet vilar pa OLD-facit "
   "('(skamt.) fraga som ej har svar')."),
  "betydelse_kan_saknas": (
   "Rakningen summerar SO-LEMMA darom (tva betydelser), SO-LEMMA tvista ('ligga i tvist' "
   "plus underbetydelsen 'grala, disputera') och lemman ur lara-familjen. Frasen sjalv "
   "har en betydelse."),
  "register_motsager_markning": (
   "Markningen 'formellt' sitter pa SO-LEMMA darom (adverb), alltsa pa ett av frasens "
   "DELORD i dess sjalvstandiga anvandning ('darom rader ingen tvekan'). Frasen som "
   "helhet ar tvartom skamtsam -- OLD-facit markerar den uttryckligen '(skamt.)', och "
   "den anvands som en axelryckning. Att arva delordets stilniva vore samma fel som att "
   "kalla 'ga med haven' hogtidligt for att 'hav' har en kyrklig anvandning.")},

 "strömfåra": {"betydelse_kan_saknas": (
   "Rastrukturen: SO-LEMMA stromfara har EN definition ('snabbast rinnande del av "
   "vattendrag') och EN underbetydelse markt '(ingen egen definition -- utvidgning)'. "
   "SAOL har inget led alls for ordet. En betydelse ar ratt.")},

 "bräm": {"betydelse_kan_saknas": (
   "Rastrukturen: SO-LEMMA bram har EN definition ('bred ytterkant pa kladesplagg') och "
   "TVA underbetydelser, varav den FORSTA ar markt '(ingen egen definition -- "
   "utvidgning)' och den ANDRA har egen text ('ytter- eller overkant pa fagelfjader eller "
   "blomhylle'). Tva sanna betydelser, vilket ar vad kortet har. Legacys tredje rad "
   "('Kant som avviker i utseende') ar struken just for att den inte motsvarar nagot "
   "led i ordboken.")},

 "svulst": {"betydelse_kan_saknas": (
   "Rastrukturen: SO-LEMMA svulst har EN definition ('tumor') och EN underbetydelse "
   "markt '(ingen egen definition -- utvidgning)'. SAOL har ett led, 'tumor'. En "
   "betydelse ar ratt. (Ordet har en bildlig anvandning om uppblast sprak -- 'svulstig' "
   "-- men det ar ett eget adjektiv med egen artikel, inte en betydelse hos "
   "substantivet.)")},

 "vittnesgill": {"betydelse_kan_saknas": (
   "Rastrukturen: SO-LEMMA vittnesgill har EN definition ('vars vittnesmal enligt lag ar "
   "giltigt' <<om person>>) och EN underbetydelse med EGEN text ('trovardig') -- tva "
   "betydelser. SAOL bekraftar bada i ett semikolonseparerat led. Kortet har bada; den "
   "andra ar den legacy saknade. Det tredje som rakningen kommer at ar SAOL:s led, "
   "som ar samma tva betydelser i en annan ordboks formulering.")},

 "dimpa": {"betydelse_kan_saknas": (
   "Rastrukturen: SO-LEMMA dimpa har EN definition ('falla tungt och overraskande') och "
   "EN underbetydelse med EGEN text ('ovantat uppenbara sig') -- tva betydelser. SAOL "
   "ger samma tva som egna led ('falla pladask' och 'av. bildl. dyka upp'), och det ar "
   "SAOL:s andra led som rakningen tar som en tredje. Kortet har bada.")},
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n_t = 0
for e in poster:
    o = e["ord"]
    if o in T:
        e["forgranska_tillat"] = T[o]
        n_t += 1
    if o == "histrion" and e.get("proposed"):
        e["proposed"]["synonym_groups"] = [["≈≈ komediant"]]
        e["proposed"]["synonymer"] = ["≈≈ komediant"]
        e["sokkoll"]["slutsats"] += (
            " RATTAT EFTER FORGRANSKNING: 'komediant' underkandes som obelagd. SO namner ordet "
            "i PLURAL i sitt tillagg ('sarsk. om komedianter, gycklare och dylikt'), och den "
            "automatiska kontrollen matchar bara grundformen -- men tillagget ar ocksa en "
            "exemplifiering av vilka slags skadespelare som avses, inte ett synonympastaende. "
            "Nedgraderad till kategori, som far hamtas ur kortets egen definition. Ordet star "
            "kvar, eftersom det ar OLD-facit och den enda traffsakra beskrivningen som finns.")
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("tillat: %d" % n_t)
