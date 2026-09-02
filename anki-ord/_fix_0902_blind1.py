# -*- coding: utf-8 -*-
"""Rattar de fyra underkanda ur blindgranskning 1, plus ETT SYSTEMATISKT FEL.

Det systematiska felet ar mitt: etymologierna skrevs med ASCII-translittererad
svenska ("avgorande", "hard", "karlek") eftersom kallkoden undveks fran att
bara diakriter. Valvets regel ar uttrycklig -- ASCII-translitteration ar
forbjuden i KORTENS innehall; bara kodkommentarer far vara ASCII. Blind-
granskaren fangade det pa 'definitiv' och hade fangat det pa 20 kort till,
till en kostnad av 1,32 USD per 25 poster.

Lardom: en systematisk brist ska rattas INNAN nasta granskningsomgang, annars
betalar man for att fa samma anmarkning om och om igen.
"""
import io, json, re, sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02_v3-batch.json"

# ASCII -> ratt svenska. Helordsmatchning, sa "franskans" inte ror sig.
ORD = {
 "avgorande": "avgörande", "avgransa": "avgränsa", "bestamma": "bestämma",
 "hard": "hård", "harda": "hårda", "forma": "förmåga", "gora": "göra",
 "latt": "lätt", "hana": "håna", "kott": "kött", "karlek": "kärlek",
 "harskarlosthet": "härskarlöshet", "harskare": "härskare",
 "forbund": "förbund", "skonhet": "skönhet", "hjarta": "hjärta",
 "anger": "ånger", "angra": "ångra", "sorja": "sörja",
 "kannetecken": "kännetecken", "fran": "från", "gangorna": "gängorna",
 "handelse": "händelse", "fardig": "färdig", "aldre": "äldre",
 "manniskas": "människas", "framstallan": "framställan", "dod": "död",
 "allman": "allmän", "vagkost": "vägkost", "fodelse": "födelse",
 "sprod": "spröd", "handelser": "händelser", "vaxter": "växter",
 "aterkommande": "återkommande", "fagellim": "fågellim", "andelse": "ändelse",
 "bojningsandelse": "böjningsändelse", "lopare": "löpare", "fasta": "fästa",
 "dorrhange": "dörrhänge", "vandpunkt": "vändpunkt", "hanvisa": "hänvisa",
 "fora": "föra", "sta": "stå", "halla": "hålla", "ingivelse": "ingivelse",
 "seg": "seg", "sarart": "särart", "forfattaren": "författaren",
 "handelsespraket": "handelsspråket", "uppkomst": "uppkomst",
 "smarta": "smärta", "hemkomst": "hemkomst", "lara": "lära",
 "varelse": "varelse", "utrusta": "utrusta", "lovtal": "lovtal",
 "lovprisning": "lovprisning", "stridsformationen": "stridsformationen",
 "bevingat": "bevingat", "smycka": "smycka", "vattenbehallare": "vattenbehållare",
 "kista": "kista", "nedstigande": "nedstigande", "stiga": "stiga",
 "forfoga": "förfoga", "over": "över", "ordna": "ordna",
}
_RE = re.compile(r"\b(" + "|".join(sorted(ORD, key=len, reverse=True)) + r")\b")


def ratta(t):
    return _RE.sub(lambda m: ORD[m.group(1)], t) if isinstance(t, str) else t


# --- de fyra underkanda -------------------------------------------------
NY = {
 "coupe": {
  # Granskaren: 'coupe' kommer av senlatinets cuppa, inte av couper.
  "etymologi": "franskans coupe 'skål, bägare', av senlatinets cuppa — samma rot "
               "som engelskans cup och svenskans kopp",
  "_slutsats_tillagg":
   " RATTAT efter blindgranskning 2026-09-02: etymologin sade tidigare att ordet "
   "kommer av verbet couper 'skara'. Det ar fel led. Franskans coupe i betydelsen "
   "kärl gar tillbaka pa senlatinets cuppa (samma rot som kopp och cup); det "
   "likljudande couper ar ett annat ord."},
 "periferisk": {
  "huvudbetydelse": "Som ligger på periferin, alltså på ytterkanten av en cirkel "
                    "eller ett område",
  "register": "fackspråklig, neutral, matematik",
  "_slutsats":
   "RATTAT efter blindgranskning 2026-09-02. Kortet sade tidigare 'som ligger i "
   "utkanten och darfor ar av underordnad betydelse' — den BILDLIGA betydelsen hos "
   "perifer, som inte ar belagd for periferisk. Vad kallorna faktiskt ger: SO saknar "
   "ordet helt (0 traffar). SAOL har det, markt 'mat.' (matematik), med definitionen "
   "enbart 'perifer'. Kortet ar darfor smalnat till den geometriska betydelsen och "
   "domanen satt till matematik. TVA AV TRE KALLOR."},
 "spisa": {
  "huvudbetydelse": "Äta ; lyssna på musik",
  "synonymer": ["äta", "lyssna på"],
  "synonym_groups": [["äta"], ["lyssna på"]],
  "_slutsats":
   "TVA betydelser. SO ger 'ata' (alderdomligt el. skamtsamt) med underbetydelsen "
   "'lyssna pa' musik (vardagligt). SAOL bekraftar bada. RATTAT efter blindgranskning "
   "2026-09-02: kortet bar tidigare en tredje betydelse, 'avvisa/avfarda'. Den kom ur "
   "en trafft som tillhor ett ANNAT lemma (spisa av), inte uppslagsordet spisa, och "
   "ar struken. Fuzzy-traffar som ser ut som extra betydelser ar batchens vanligaste "
   "felkalla — samma sak hande med essens och ess."},
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n_ascii = 0
for e in poster:
    pr = e.get("proposed")
    if not pr:
        continue
    for f in ("etymologi", "huvudbetydelse", "exempelmening"):
        v = pr.get(f)
        ny = ratta(v)
        if ny != v:
            pr[f] = ny
            n_ascii += 1
    sk = e.get("sokkoll") or {}
    if sk.get("slutsats"):
        sk["slutsats"] = ratta(sk["slutsats"])

for e in poster:
    d = NY.get(e["ord"])
    if not d:
        continue
    pr = e["proposed"]
    for k, v in d.items():
        if k == "_slutsats":
            e["sokkoll"]["slutsats"] = ratta(v)
        elif k == "_slutsats_tillagg":
            e["sokkoll"]["slutsats"] = ratta(e["sokkoll"]["slutsats"] + v)
        else:
            pr[k] = v

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("falt med ASCII rattade:", n_ascii)
print("underkanda kort omskrivna:", len(NY))

kvar = []
for e in poster:
    pr = e.get("proposed") or {}
    for f in ("etymologi", "huvudbetydelse", "exempelmening"):
        v = pr.get(f) or ""
        for w in re.findall(r"\b[a-z]{4,}\b", v):
            if w in ORD:
                kvar.append((e["ord"], f, w))
print("kvarvarande ASCII-traffar:", kvar or "inga")
