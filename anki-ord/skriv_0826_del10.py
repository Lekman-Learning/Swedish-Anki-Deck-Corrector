# -*- coding: utf-8 -*-
import json, urllib.parse

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}


def H(w):
    return '<font color="#3498db">' + w + '</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, ordfix=None, tillat=None, conf=9):
    e = BY[o]
    q = urllib.parse.quote(o)
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": None, "exempelmening": ex, "etymologi": ety}
    if ordfix:
        e["proposed"]["proposed_ord"] = ordfix
    e["sokkoll"] = {"kalla": "SO och SAOL via https://svenska.se/api/msearch?ord=" + q
                    + " (hämtat 2026-08-26, HTTP 200)", "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("implementera",
     "Sätta något i verket på riktigt ; få ett datorprogram att fungera på en viss maskin",
     "neutral, IT", ["förverkliga"],
     "Företaget ska " + H("implementera") + " de nya rutinerna före årsskiftet.", None,
     "SO: göra (programsystem) körbart; äv. allmännare: införa. SAOL: förverkliga, genomföra; göra "
     "dataprogram körbart på en viss maskin — förverkliga inleder ledet och är belagd synonym. "
     "Belagt sedan 1960-talet, alltså ett ungt ord.")

satt("knekt",
     "Enkel soldat, sagt lite föraktfullt ; spelkortet mellan tia och dam",
     "historia, nedsättande", [],
     "Ruter " + H("knekt") + " låg överst i högen.", None,
     "SO: (fot)soldat, äv. om militär i allmänhet, äv. bildligt om någons handgångne man "
     "(maffialedarens knektar); spelkort med valör närmast över tian; samt stöd för båge eller "
     "valv. SAOL: soldat; ett spelkort, med bruksuppgifterna nedsättande och mest historiskt. "
     "Byggnadsbetydelsen utelämnas som fackterm.",
     tillat={"betydelse_kan_saknas":
             "SO:s sex poster är tre betydelser plus tre markörer. Kortet har de två som bär "
             "ordförrådet — soldaten och spelkortet, båda i SAOL. Den tredje (stöd för båge eller "
             "valv) är en byggnadsteknisk term utan koppling till de andra."})

satt("kredensa",
     "Smaka av mat eller dryck innan man bjuder fram den",
     "arkaisk", [],
     "Munskänken " + H("kredensade") + " vinet innan det bars in till kungen.", None,
     "🔴 SVAGARE BELÄGG ÄN NORMALT. Varken SO eller SAOL har ordet — svenska.se gav ingen artikel. "
     "Enda källan är svenska Wiktionary: 'provsmaka dryck eller maträtt, skänka i, smaka av, bjuda "
     "(dryck för avsmakning)', vilket stämmer med OLD-facit 'bjuda (mat)' och med legacy. "
     "Kärnan i alla källor är avsmakningen före framförandet. Konfidens sänkt till 7 — kortet är "
     "INTE släppbart utan att en granskare kontrollerar mot SAOB för hand.",
     tillat={"uppslagsord_saknas":
             "Ordet finns varken i SO eller SAOL. Betydelsen vilar på Wiktionary plus OLD-facit, "
             "vilket är svagare än valvets normala krav. Det står utskrivet i sökkollen och "
             "konfidensen är satt till 7, under släppgränsen."},
     conf=7)

satt("vurm",
     "Starkt, ofta överdrivet intresse för något",
     "neutral", [],
     "Romantikens " + H("vurm") + " för det exotiska syns i hela konsten.",
     "av tyskans Wurm, mask — som att ha en mask i huvudet",
     "SO: starkt (och ibland överdrivet) intresse; exempel romantikens vurm för det exotiska. "
     "SAOL: överdrivet intresse, mani. Mani står efter komma och inleder inget eget led — inte "
     "belagd som synonym. Etymologin tas med eftersom bilden gör ordet minnesvärt.")

satt("väsenskild",
     "Helt olik till sin natur, inte bara i detaljer",
     "formell", [],
     "Den asiatiska kapitalismen är " + H("väsensskild") + " från den amerikanska.", None,
     "🔴 FRAMSIDAN ÄR FELSTAVAD. Uppslag på väsenskild gav ingen artikel. Uppslag på väsensskild "
     "(dubbel-s) gav SO: 'helt olik till sin natur', med exemplet den asiatiska kapitalismen är "
     "väsensskild från den amerikanska, belagt sedan 1895. Wiktionary: fullkomligt olik, grundligt "
     "annorlunda. proposed_ord sätter rätt stavning. Andra stavfelet i den här batchen efter crepe.",
     ordfix="väsensskild")

# --- kvarvarande motiveringar ---
BY["umbärande"].setdefault("forgranska_tillat", {}).update({
    "frammande_uppslagsord":
        "Det främmande uppslaget är umbära, verbet som substantivet umbärande bildas av. Samma "
        "ord i annan form, inte ett annat uppslag.",
    "betydelse_kan_saknas":
        "SO:s två poster är substantivet (allvarlig brist på elementära förutsättningar) och "
        "verbet umbära (klara sig utan). Kortet ger substantivet, vilket är den form OLD-facit "
        "och båda exempelmeningarna visar."})
BY["vals"].setdefault("forgranska_tillat", {}).update({
    "frammande_uppslagsord":
        "Det främmande uppslaget är val — ett annat ord som fuzzy-matchningen drog in på "
        "bokstavslikhet. Ingen glosa på kortet kommer därifrån."})
BY["tabulatur"].setdefault("forgranska_tillat", {}).update({
    "synonym_saknas_trots_belagg":
        "Notskrift är definitionens huvudord och vidare än tabulatur — vanliga noter är också "
        "notskrift. Inte utbytbar. Tom lista är rätt svar."})

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 10 skriven: 5 kort. Totalt approved: %d/%d"
      % (sum(1 for e in S if e.get("approved")), len(S)))
