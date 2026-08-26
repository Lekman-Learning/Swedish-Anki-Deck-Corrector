# -*- coding: utf-8 -*-
"""Rättar de 16 hårda anmärkningarna från forgranska.py på del 1.

Två slags åtgärder:
  1. RIKTIGA FIX av register — ordbokens märkning ska speglas i registret.
  2. forgranska_tillat med skriven motivering där en betydelse är medvetet
     utelämnad. Undantaget döljer inte regeln, den blir mjuk och syns.
"""
import json

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}

# ---- 1. Registerfix (ordbokens märkning vinner) ----
REG = {
    "i onåd": "högtidlig",
    "långledas": "ngt ålderdomlig, dialektal",
    "obstruktion": "formell, ngt ålderdomlig",
    "talja": "fackspråklig, sjöfart, ngt ålderdomlig",
}
for o, r in REG.items():
    BY[o]["proposed"]["register"] = r

# ---- karda: ta in den betydelse märkningen 'vardagligt' hör till ----
k = BY["karda"]["proposed"]
k["huvudbetydelse"] = ("Redskap med tänder som reder ut ull före spinning ; reda ut ull med ett "
                       "sådant redskap ; hand")
k["register"] = "neutral, vardaglig"
BY["karda"]["sokkoll"]["slutsats"] = (
    "SO: redskapet, verbet luckra upp och reda ut, samt hand märkt vardagligt. SAOL bekräftar alla "
    "tre: redskap för kardning; hand (vard.); bearbeta ull för spinning. Rättat 2026-08-26: "
    "hand-betydelsen var först utelämnad som särbetydelse, men då stämde inte registret mot "
    "ordbokens vardagligt-märkning. Betydelsen är med, registret är vardaglig.")

# ---- 2. Motiverade undantag ----
TILLAT = {
    "i onåd": {"betydelse_kan_saknas":
        "SO:s åtta betydelser gäller uppslagsordet nåd (nåd, benådning, bibliska uttryck, "
        "på nåd och onåd m.fl.). Kortet är det fasta uttrycket i onåd, som SO redovisar som "
        "ett eget exempel under en enda betydelse: överordnad persons missnöje. Övriga är "
        "andra uttryck, inte betydelser av detta."},
    "inventarium": {"betydelse_kan_saknas":
        "SO:s fem poster är tre betydelser plus två av-markörer. Kortet har de två som bär "
        "ordförrådet: förteckningen och den bildliga om en person. Den tredje (förteckning "
        "över tillgångar OCH skulder) är en bokföringsteknisk underavdelning av den första "
        "och tillför inget för ordinlärning.",
        "synonym_saknas_trots_belagg":
        "Kandidaterna förteckning och person är definitionens huvudord, inte utbytbara "
        "synonymer till inventarium. Tom lista är rätt svar."},
    "karda": {"synonym_saknas_trots_belagg":
        "Kandidaterna (bearbeta, bomull, hand, kardad, luckra, redskap) är definitionsord, inte "
        "synonymer. Kardmaskin är cirkulär. Tom lista är rätt svar."},
    "kainsmärke": {"synonym_saknas_trots_belagg":
        "Kandidaten tecken är definitionens huvudord, inte en synonym — ett kainsmärke är en "
        "särskild sorts tecken. Tom lista är rätt svar."},
    "ketch": {"synonym_saknas_trots_belagg":
        "Kandidaten tvåmastad är ett adjektiv ur definitionen. SO listar yawl och galeas som "
        "cohyponymer, alltså andra båttyper — inte synonymer. Tom lista är rätt svar."},
    "långledas": {"synonym_saknas_trots_belagg":
        "Kandidaten ha långtråkigt är SAOL:s hela definition, inte ett utbytbart ord. "
        "Tom lista är rätt svar."},
    "obstruktion": {"betydelse_kan_saknas":
        "SO:s sex poster är tre betydelser plus tre spec.-markörer (parlamentarisk förhalning, "
        "bollspel, medicin). Kortet har båda huvudbetydelserna; spec.-fallen är tillämpningar "
        "av dem och nämns i exempelmeningen (votering)."},
    "solidarisk": {"betydelse_kan_saknas":
        "SO:s fyra poster är två betydelser plus två markörer (äv. om handling, äv. med "
        "konstruktionsväxling). Båda betydelserna finns på kortet.",
        "synonym_saknas_trots_belagg":
        "Kandidaten gemensamt ansvarig är SAOL:s definitionsled, en omskrivning snarare än ett "
        "utbytbart ord. Tom lista är rätt svar."},
    "talja": {"synonym_saknas_trots_belagg":
        "Kandidaterna (förflytta, hala, hissanordning, lyftanordning) är definitionsord. "
        "Taljblock är cirkulär, tackel och blocktyg saknar belägg. Tom lista är rätt svar."},
    "ympa": {"betydelse_kan_saknas":
        "SO:s fem poster är två betydelser plus tre markörer (äv. med konstruktionsväxling, "
        "äv., äv. bildligt). Båda betydelserna — foga in kvist, och vaccinera — finns på kortet.",
        "synonym_saknas_trots_belagg":
        "Kandidaterna foga och skära är definitionsverb; vaccinera är kortets andra betydelse, "
        "inte en synonym till den första. Inympa är cirkulär. Tom lista är rätt svar."},
    "grav": {"betydelse_kan_saknas":
        "SO:s poster blandar substantivet grav med adjektivet grav och fyra bildliga uttryck "
        "(vända sig i sin grav, gå i graven m.fl.). Kortet har båda ordklassernas "
        "kärnbetydelser, vilket är vad OLD-facit och ordförrådet kräver."},
    "gom": {"synonym_saknas_trots_belagg":
        "Garnityr är SO:s definitionsord för den andra betydelsen, inte en synonym till gom. "
        "Tom lista är rätt svar."},
    "disputation": {"synonym_saknas_trots_belagg":
        "Doktorsdisputation är cirkulär (innehåller uppslagsordet). Försvar och avhandling är "
        "delar av vad en disputation är, inte utbytbara ord. Tom lista är rätt svar."},
    "girland": {"synonym_saknas_trots_belagg":
        "Prydnadsranka är SAOL:s definitionsord. Festong och slinga saknar ordboksbelägg. "
        "Tom lista är rätt svar."},
    "gördla": {"synonym_saknas_trots_belagg":
        "Förse med gördel är hela definitionen; förse och omge är definitionsverb utan belägg "
        "som synonymer. Tom lista är rätt svar."},
    "krusig": {"betydelse_kan_saknas":
        "SAOL ger smålockig; veckig, räfflad — samtliga är samma grundbetydelse (full av små "
        "vågor) tillämpad på hår, tyg respektive yta. Kortet täcker den med vågor eller lockar."},
}
n = 0
for o, d in TILLAT.items():
    if o in BY:
        BY[o]["forgranska_tillat"] = d
        n += 1

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Register rättat på %d kort (+ karda utökad). Motiverade undantag på %d kort."
      % (len(REG), n))
