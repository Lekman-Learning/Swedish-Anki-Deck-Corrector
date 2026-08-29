# -*- coding: utf-8 -*-
"""Batch 2026-08-29b -- 5 kort.

REGLERNA, i den ordning de kostat mest:

1. SLA ALDRIG IHOP tva betydelser som SO eller SAOL haller isar. Bevisbordan
   ligger hos mig for att de ar SAMMA. Att skriva ut i sokkollen att jag slar
   ihop gor inte hopslagningen riktig -- fem av nio underkanda kort 28/8 hade
   just den anteckningen.
   Undantag som faktiskt raknas: SO:s egen markering "el." binder ihop tva
   formuleringar till EN betydelse. Da ar det SO som slar ihop, inte jag.
2. Synonym bara om ordet ar utbytbart AT BADA HALLEN och inte ar JFR-markerat
   i SO. JFR ar kohyponym-markering, inte synonymbevis.
3. Ingen betydelse som bara Wiktionary har.
4. Facit styrs av DEFINITIONEN -- aldrig av etymologin eller av en synonym.
5. ETYMOLOGIFALTET RENDERAS PA KORTET: full svenska, aldrig ASCII-slarv.
   Sokkollen ar intern och far vara ASCII; etymologin far det inte.
"""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-29_v3-batch2.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
B = '<font color="#3498db">%s</font>'


def kallor(o, *extra):
    k = urllib.parse.quote(o)
    return " ".join([
        "https://svenska.se/api/msearch?ord=%s" % k,
        "https://www.synonymer.se/sv-syn/%s" % k,
        "https://sv.wiktionary.org/wiki/%s" % k,
        *extra])


def satt(o, bet, reg, syn, ex, ety, slutsats, grupper=None, extra=(), conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": grupper, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": kallor(o, *extra), "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True


# ---------------------------------------------------------------- hardra
# SO ger tva formuleringar men binder dem med markeringen "el." -- alltsa EN
# betydelse i tva halvor, inte tva betydelser. Bada exemplen visar samma sak.
# Wiktionarys 'dra nagon i haret' och 'misshandla' finns INTE i SO eller SAOL
# och far darfor inte plats (regel 3).
satt(
    "hårdra",
    "Driva ett resonemang eller en liknelse för långt, ut i minsta detalj, "
    "så att slutsatserna blir orimliga",
    "formell, lätt negativ, allmän",
    [],
    "Man ska inte %s liknelsen — då bevisar den plötsligt motsatsen."
    % (B % "hårdra"),
    "→ Jämför fornsvenska hardragha 'dra i håret'. Från det bokstavliga "
    "slitandet i hår till det bildliga: att dra i ett resonemang tills det "
    "ger vika. Belagt sedan 1749.",
    "SO ger 'fora (resonemang) anda till enskilda detaljer' EL. 'dra alltfor "
    "langtgaende (och detaljerade) slutsatser'. Markeringen 'el.' i "
    "underbetydelser ar SO:s egen -- de tva formuleringarna ar EN betydelse, "
    "inte tva, och bada exemplen (liknelsen / hans resonemang) visar samma "
    "anvandning. SAOL: 'pressa', ett ord. INGEN synonym satt: SO JFR-markerar "
    "'pressa 1', och JFR ar kohyponym, inte synonym (regel 2); 'pressa' ar "
    "dessutom inte utbytbart at andra hallet. Wiktionarys 'dra nagon i haret' "
    "och 'misshandla' saknas i bade SO och SAOL -- utelamnade enligt regel 3.")

# ---------------------------------------------------------------- kantele
satt(
    "kantele",
    "Finskt stränginstrument: en flat trälåda med strängar som knäpps med "
    "fingrarna",
    "neutral, neutral, musik",
    [],
    "Hon spelade en gammal runosång på sin %s." % (B % "kantele"),
    "→ Av finska kantele med samma betydelse, möjligen av litauiskt ursprung. "
    "Belagt i svenskan sedan 1811.",
    "En betydelse i bade SO och SAOL. SO: 'ett ladformat (finskt) "
    "musikinstrument med strangar som knappas med fingrarna'. SAOL: 'ett "
    "stranginstrument'. Wiktionary: 'liknande en cittra'. Inga synonymer i "
    "nagon kalla -- synonymer.se saknar uppslagsord, SO saknar JFR. Ordet ar "
    "ett lanat foremalsnamn utan svenskt utbytbart alternativ.")

# ---------------------------------------------------------------- tinnitus
# SO:s parentes '(plagsamt besvar i form av)' ar en inramning av samma
# betydelse, inte en andra betydelse.
satt(
    "tinnitus",
    "Ihållande ringningar eller sus i öronen utan ljudkälla utifrån, ofta "
    "plågsamt",
    "neutral, neutral, medicin",
    [],
    "Efter åratal på verkstadsgolvet fick han %s på båda öronen."
    % (B % "tinnitus"),
    "→ Till latin tinnire 'ringa, klinga'. Belagt i svenskan sedan 1935.",
    "En betydelse i alla tre kallorna. SO: '(plagsamt besvar i form av) "
    "ringningar och sus i oronen' -- parentesen ramar in samma betydelse och "
    "ar inte en andra. SAOL: 'en sjukdom med susningar och ringningar i "
    "oronen'. Wiktionary: 'det att det oavbrutet piper i orat'. INGEN synonym "
    "satt: 'oronsus' finns i sprakbruket men star inte i nagon av de tre "
    "kallorna -- att skriva in det vore att hitta pa.")

# ---------------------------------------------------------------- graverande
# HAR SKRIVER JAG FARRE BETYDELSER AN SOKNINGEN GAV -- las motiveringen.
satt(
    "graverande",
    "Som gör saken allvarligare för den som är anklagad; belastande",
    "formell, negativ, allmän",
    ["försvårande"],
    "Att kvittona var förfalskade var det mest %s i hela utredningen."
    % (B % "graverande"),
    "→ Av latin gravare 'belasta, besvära', till gravis 'tung' — samma rot "
    "som i gravitation. Belagt sedan omkring 1520.",
    "VARNING TILL GRANSKAREN: sokningen pa 'graverande' gav TRE definitioner, "
    "kortet har EN. Skalet ar inte hopslagning utan att de tva andra tillhor "
    "ett annat uppslagsord. SO listar 'som kan ha svara foljder' | 'rista "
    "(dekorativt monster) pa hard yta' | 'belasta (fastighet) med "
    "inteckning'. Tre bevis for att bara den forsta ar 'graverande': "
    "(1) SO ger TVA skilda etymologier -- franska graver 'grava' for "
    "ristbetydelsen, latin gravare 'belasta' for de ovriga; det ar tva "
    "homonyma verb gravera som sokningen slagit ihop. (2) Ingen av de tva "
    "andra betydelsernas exempel anvander formen graverande: 'namnet "
    "GRAVERAT pa baksidan' och 'fastigheten GRAVERAS av inteckningar' -- "
    "bada ar verbet gravera, inte adjektivet. (3) SAOL:s enda exempel pa "
    "graverande ar 'en graverande omstandighet', alltsa enbart den forsta. "
    "SYNONYM: 'forsvarande' hamtat ur SAOL:s definitionstext ('besvarande, "
    "forsvarande') och utbytbart at bada hallen i 'forsvarande/graverande "
    "omstandighet'. 'besvarande' och 'allvarlig' ar JFR-markerade i SO och "
    "utesluts enligt regel 2.",
    conf=8)

# ---------------------------------------------------------------- skildra
# TVA betydelser i SO, med varsin exempelgrupp. Halls isar (regel 1).
satt(
    "skildra",
    "Återge ett händelseförlopp eller en upplevelse ingående, i ord eller "
    "bild ; framställa någon eller något på ett visst sätt",
    "neutral, neutral, allmän ; neutral, neutral, allmän",
    [],
    "Boken %s uppväxten i ett brukssamhälle på sjuttiotalet."
    % (B % "skildrar"),
    "→ Av tyska schildern, lågtyska schilderen 'måla en vapensköld', till "
    "tyska Schild 'sköld'. I svenskan betydde ordet först 'måla', därefter "
    "'ge en bild av; berätta'. Besläktat med sköld. Belagt sedan 1792, i "
    "betydelsen 'måla' sedan 1700.",
    "SO ger TVA definitioner med varsin exempelgrupp och de halls darfor isar "
    "(regel 1): 'ingaende aterge' (hon skildrade sina upplevelser under "
    "resan ; tavlan skildrade slaget vid Lund) och -- markerad 'av.' -- "
    "'beskriva' (i boken skildras de vuxna som standiga forlorare ; skildra "
    "djurens beteende). Skillnaden ar att den forsta aterger ett forlopp "
    "ingaende, den andra framstaller nagon pa ett visst satt. SAOL slar ihop "
    "dem till 'beratta om, beskriva', men SAOL ar kortare per konstruktion "
    "och far inte overtrumfa SO:s uppdelning. INGA synonymer: SO JFR-markerar "
    "'beratta', 'beskriva 1', 'skildring' och 'skildrare' -- samtliga "
    "utesluts av regel 2, och 'beskriva' ar dessutom vidare an skildra.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("skrev %d kort" % sum(1 for k in KORT if k.get("approved")))
