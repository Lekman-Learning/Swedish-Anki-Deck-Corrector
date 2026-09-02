# -*- coding: utf-8 -*-
"""Skriver om samtliga register i batchen till den kontrollerade vokabularen.

FELET: registerfaltet ar inte fritext. baksida.validate_register kraver taggar
ur tre listor i config.py -- REGISTER_FORMALITY (stilniva), REGISTER_VALENS
(valor) och REGISTER_DOMAN (fackomrade) -- och BADE stilniva och valor maste
finnas. "formell, religios" och "nagot alderdomlig" ar darfor ogiltiga; det
heter "ngt alderdomlig" och "religion".

Foljden var mattbar: kortgranskare.py applicera skrev 6 kort och hoppade over
129, samtliga med "registret ogiltigt". forgranska.py sag ingenting -- den
kontrollerar att registret inte MOTSAGER ordbokens markning, inte att taggarna
finns i vokabularen. Tva kontroller pa samma falt som inte overlappar.

Registren nedan bevarar den markning SO/SAOL faktiskt satt, eftersom
forgranskas register_motsager_markning matchar pa ordstam: 'mindre brukligt'
och 'mest historiskt' kraver bada stammen "alder", 'dialektalt' kraver
"diale", 'nagot hogtidligt' kraver "hogti".
"""
import io, json, sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02_v3-batch.json"

R = {
 # --- batch A ---
 "absolvera": "ngt ålderdomlig, neutral, allmän",
 "sanslös": "vardaglig, neutral, allmän",
 "bylsig": "vardaglig, lätt negativ, allmän",
 "coupe": "neutral, neutral, matlagning",
 "digna": "litterär, neutral, allmän",
 "endokrin": "fackspråklig, neutral, medicin",
 "essens": "neutral, neutral, allmän",
 "expenser": "formell, neutral, ekonomi",
 "fiskal": "fackspråklig, neutral, juridik",
 "habil": "neutral, nedsättande, allmän",
 "hypotetisk": "neutral, neutral, allmän",
 "kont": "ngt ålderdomlig, neutral, allmän",
 "lisma": "ngt ålderdomlig, nedsättande, allmän",
 "periferisk": "ngt ålderdomlig, neutral, allmän",
 "sakral": "formell, neutral, religion",
 "saltomortal": "neutral, neutral, sport",
 "serum": "fackspråklig, neutral, medicin",
 "spisa": "ngt ålderdomlig, skämtsam, allmän",
 # --- batch B ---
 "stängel": "neutral, neutral, biologi",
 "tala med kluven tunga": "neutral, negativ, allmän",
 "trema": "fackspråklig, neutral, lingvistik",
 "vresig": "neutral, lätt negativ, allmän",
 "adressat": "formell, neutral, allmän",
 "definitiv": "neutral, neutral, allmän",
 "direktiv": "formell, neutral, allmän",
 "divergera": "formell, neutral, allmän",
 "drakonisk": "formell, negativ, allmän",
 "durkdriven": "neutral, lätt negativ, allmän",
 "dynamik": "neutral, neutral, allmän",
 "enkelspårig": "neutral, nedsättande, allmän",
 "falang": "neutral, neutral, politik",
 "fashionabel": "ngt ålderdomlig, neutral, allmän",
 "fiffa upp": "vardaglig, neutral, allmän",
 # --- batch C ---
 "garva": "vardaglig, neutral, allmän",
 "hermetisk": "formell, neutral, fysik",
 "idiom": "fackspråklig, neutral, lingvistik",
 "knapphändig": "neutral, lätt negativ, allmän",
 "kommitté": "formell, neutral, politik",
 "konsolidera": "formell, neutral, ekonomi",
 "konststycke": "neutral, neutral, allmän",
 "labil": "neutral, lätt negativ, allmän",
 "omen": "litterär, neutral, allmän",
 "parant": "ngt ålderdomlig, positiv, allmän",
 "sarkastisk": "neutral, negativ, allmän",
 "satirisk": "neutral, neutral, litteraturvetenskap",
 "spatiös": "fackspråklig, neutral, konst",
 "tjusa": "ngt ålderdomlig, positiv, allmän",
 "underkyld": "fackspråklig, neutral, fysik",
 "upprätta": "formell, neutral, juridik",
 "utopi": "neutral, neutral, filosofi",
 "ynklig": "neutral, nedsättande, allmän",
 "ämbete": "formell, neutral, religion",
 "överdådig": "neutral, positiv, allmän",
 # --- batch D ---
 "ackja": "neutral, neutral, historia",
 "additament": "formell, neutral, juridik",
 "amorin": "neutral, neutral, konst",
 "anarki": "neutral, neutral, politik",
 "antracit": "fackspråklig, neutral, geologi",
 "ballad": "neutral, neutral, musik",
 "bane": "arkaisk, neutral, allmän",
 "belacka": "ngt ålderdomlig, nedsättande, allmän",
 "bestyr": "ngt ålderdomlig, neutral, allmän",
 "bevågen": "ngt ålderdomlig, positiv, allmän",
 "blankvers": "fackspråklig, neutral, litteraturvetenskap",
 "blott": "högtidlig, ngt ålderdomlig, neutral, allmän",
 "bobin": "fackspråklig, neutral, teknik",
 "bombasm": "formell, nedsättande, allmän",
 "bonnett": "neutral, neutral, historia",
 "bängel": "vardaglig, nedsättande, allmän",
 "båga": "vardaglig, negativ, allmän",
 "bökig": "vardaglig, lätt negativ, allmän",
 "chikan": "ngt ålderdomlig, negativ, allmän",
 "cistern": "neutral, neutral, teknik",
 "dagdrivare": "neutral, nedsättande, allmän",
 "descendent": "fackspråklig, neutral, juridik",
 # --- batch E ---
 "disponent": "ngt ålderdomlig, neutral, ekonomi",
 "driftkucku": "vardaglig, nedsättande, allmän",
 "ekipera": "ngt ålderdomlig, neutral, allmän",
 "eloge": "neutral, positiv, allmän",
 "enständig": "arkaisk, neutral, allmän",
 "fallenhet": "neutral, neutral, allmän",
 "federalism": "fackspråklig, neutral, politik",
 "fejka": "vardaglig, negativ, allmän",
 "force majeure": "fackspråklig, neutral, juridik",
 "fylogeni": "fackspråklig, neutral, biologi",
 "fäderne": "ngt ålderdomlig, neutral, allmän",
 "förkomma": "formell, neutral, allmän",
 "förställa": "formell, negativ, allmän",
 "galej": "vardaglig, neutral, allmän",
 "gniden": "vardaglig, nedsättande, allmän",
 "goutera": "formell, neutral, allmän",
 "grift": "arkaisk, neutral, religion",
 "hugskott": "neutral, lätt negativ, allmän",
 "index": "fackspråklig, neutral, ekonomi",
 "insistera": "formell, neutral, allmän",
 # --- batch F ---
 "instinkt": "neutral, neutral, psykologi",
 "iteration": "fackspråklig, neutral, matematik",
 "kalligrafi": "neutral, neutral, konst",
 "kardinalfel": "neutral, negativ, allmän",
 "konfession": "fackspråklig, neutral, religion",
 "kordial": "högtidlig, positiv, allmän",
 "korist": "neutral, neutral, musik",
 "kväsa": "vardaglig, negativ, allmän",
 "kält": "dialektal, nedsättande, allmän",
 "lidelse": "litterär, neutral, allmän",
 "lingua franca": "fackspråklig, neutral, lingvistik",
 "metamorfos": "formell, neutral, biologi",
 "nostalgi": "neutral, neutral, psykologi",
 "näsvis": "neutral, nedsättande, allmän",
 "paleontologi": "fackspråklig, neutral, geologi",
 "pampig": "vardaglig, positiv, allmän",
 "penitens": "ngt ålderdomlig, neutral, religion",
 "proaktiv": "fackspråklig, neutral, allmän",
 "proper": "neutral, positiv, allmän",
 "proviant": "neutral, neutral, allmän",
 # --- batch G ---
 "pråm": "neutral, neutral, sjöfart",
 "påläggskalv": "neutral, lätt negativ, allmän",
 "referens": "formell, neutral, allmän",
 "ringa": "neutral, neutral, allmän",
 "schäs": "ngt ålderdomlig, neutral, historia",
 "skleros": "fackspråklig, neutral, medicin",
 "skört": "neutral, neutral, allmän",
 "specimen": "formell, neutral, allmän",
 "suffix": "fackspråklig, neutral, lingvistik",
 "tilldragelse": "ngt ålderdomlig, neutral, allmän",
 "trankil": "vardaglig, neutral, allmän",
 "träaktig": "neutral, nedsättande, allmän",
 "tråckla": "neutral, neutral, allmän",
 "tvärsnitt": "neutral, neutral, teknik",
 "viskositet": "fackspråklig, neutral, fysik",
 "vågspel": "litterär, neutral, allmän",
}

# Markningar som INTE gar att uttrycka i vokabularen och darfor motiveras.
TILLAT = {
 "disponent": {"register_motsager_markning":
   "SO:s markning ar 'finl.' - finlandssvenskt bruk. Det finns ingen motsvarande "
   "tagg i config.REGISTER_FORMALITY/VALENS/DOMAN, sa den gar inte att uttrycka i "
   "registerfaltet utan att bryta vokabularen. Uppgiften star i stallet i sokkollens "
   "slutsats. Registret 'ngt alderdomlig, neutral, ekonomi' ar korrekt for "
   "rikssvenskt bruk, dar titeln ar historisk."},
 "ämbete": {"register_motsager_markning":
   "SO:s markning ar 'i kyrkliga sammanhang'. Vokabularens narmaste tagg ar domanen "
   "'religion', som ar satt - men stammatchningen soker 'kyrkl' och hittar den inte. "
   "Markningen ar alltsa uttryckt, bara med vokabularens eget ord."},
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = t = 0
for e in poster:
    o = e["ord"]
    if o in R and e.get("proposed"):
        e["proposed"]["register"] = R[o]
        n += 1
    if o in TILLAT:
        e.setdefault("forgranska_tillat", {}).update(TILLAT[o])
        t += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("register omskrivna: %d, motiveringar: %d" % (n, t))

# Validera direkt mot samma funktion som kortgranskare anvander.
import baksida
fel = 0
for e in poster:
    pr = e.get("proposed")
    if not pr:
        continue
    v = baksida.validate_register(pr.get("register") or "")
    if v:
        print("  OGILTIGT %-22s %-42s %s" % (e["ord"], pr.get("register"), v))
        fel += 1
print("ogiltiga register kvar:", fel)
saknas = [e["ord"] for e in poster if e.get("proposed") and e["ord"] not in R]
print("kort utan nytt register:", saknas or "inga")
