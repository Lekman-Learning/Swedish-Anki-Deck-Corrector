# -*- coding: utf-8 -*-
"""De fyra orden som saknade egen SO/SAOL-artikel.

Tre går att belägga ändå — via samma teknik som geriatri->geriatrik: slå upp
grundordet eller komponenterna. Ett pausas, för underlaget räcker inte.
"""
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


# --- crepe: framsidan ar felstavad, ratt form ger full ordbokstackning ---
satt("crepe",
     "Tunn pannkaka, ofta rullad kring en fyllning",
     "neutral, matlagning", [],
     "Han vek ihop sin " + H("crêpe") + " kring nutella och banan.",
     None,
     "🔴 FRAMSIDAN ÄR FELSTAVAD. Uppslaget på crepe gav NOLL källor "
     "(kallor_med_innehall: []). Samma uppslag på crêpe gav full täckning: SO 'typ av tunn "
     "pannkaka', SAOL 'tunn pannkaka med fyllning', etymologi av franska crêpe, ur latin crispus "
     "'krusig', belagt sedan 1889. Legacys egen synonymlista innehöll redan crêpe, vilket "
     "bekräftar att accenten fallit bort. proposed_ord sätter rätt stavning.",
     ordfix="crêpe")

# --- epilering: substantivet har SAOL-uppslag utan definition, verbet har den ---
satt("epilering",
     "Att ta bort hår ända från roten",
     "fackspråklig, medicin", [],
     "Hon bokade tid för " + H("epilering") + " av benen.", None,
     "SAOL har epilering som eget uppslag (ämnesområde: med.) men utan definitionstext — posten "
     "hänvisar till verbet epilera. Uppslag på epilera 2026-08-26: SO 'avlägsna oönskad hårväxt "
     "från', SAOL 'avlägsna hårväxt ända ner till rötterna från viss del av kroppen', etymologi "
     "till latin e 'från' och pilus 'hår'. Samma teknik som geriatri->geriatrik. Legacys vaxning "
     "är en metod, inte ordets betydelse — struken.",
     tillat={"uppslagsord_saknas":
             "Uppslagsordet epilering FINNS i SAOL men utan definitionstext (hänvisningspost till "
             "epilera). Definitionen är hämtad från epilera i ett eget, loggat uppslag samma dag."})

# --- helioterapi: sammansattning, bada leden ordboksbelagda ---
satt("helioterapi",
     "Behandling av sjukdom med solljus",
     "fackspråklig, medicin", [],
     "Före antibiotikan behandlades tuberkulos med " + H("helioterapi") + " på sanatorier.",
     "av grekiskans helios, sol",
     "Ordet saknar SO- och SAOL-artikel; bara en SAOB-post som är en avledd underlemma "
     "(derived: 1) under helio- utan definitionstext. Betydelsen är därför sammansatt av två "
     "ordboksbelagda led, båda uppslagna 2026-08-26: helio- av grekiska helios 'sol' (belagt via "
     "SO:s etymologi för heliocentrisk), och terapi = SO 'särskild medicinsk eller psykologisk "
     "behandling'. Sammansättningen stämmer med OLD-facit 'solljusbehandling'. "
     "⚠️ SVAGARE BELÄGG ÄN NORMALT: ingen ordbok definierar ordet som helhet.",
     tillat={"uppslagsord_saknas":
             "Varken SO eller SAOL har ordet. Betydelsen är härledd ur två belagda led, vilket "
             "står utskrivet i sökkollen. Konfidensen är sänkt till 8 för att markera det."},
     conf=8)

# --- postponera: PAUSAS, underlaget racker inte ---
p = BY["postponera"]
p["approved"] = False
p["sokkoll"] = {
    "kalla": "SO och SAOL via https://svenska.se/api/msearch?ord=postponera "
             "(hämtat 2026-08-26, HTTP 200) — samt kontrolluppslag på ponera och uppskjuta",
    "slutsats":
        "🔴 PAUSAS. Varken SO eller SAOL har ordet; enda träffen är en avledd SAOB-underlemma "
        "(post-ponera) utan definitionstext. Härledning via roten går INTE: svenska ponera betyder "
        "'förutsätta som ett faktum' (SO), inte 'placera' — en sammansättning den vägen skulle ge "
        "fel betydelse. Dessutom ser OLD-facit ut att vara fel: det säger 'inställa', men att "
        "ställa in och att skjuta upp är olika saker. Legacy säger 'skjuta upp till senare "
        "tidpunkt', vilket stämmer med latinets postponere och engelskans postpone — men det är "
        "min egen kunskap, inte en källa, och kortet får inte vila på den. "
        "ÅTGÄRD: kräver SAOB-uppslag för hand, eller Adams beslut att stryka kortet."}
p["note_till_granskare"] = (p.get("note_till_granskare") or "") + \
    " || PAUSAD 2026-08-26: otillräckligt ordboksunderlag, se sokkoll."

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 5: 3 skrivna (crepe med stavningsfix), 1 pausad. Totalt approved: %d/%d"
      % (sum(1 for e in S if e.get("approved")), len(S)))
