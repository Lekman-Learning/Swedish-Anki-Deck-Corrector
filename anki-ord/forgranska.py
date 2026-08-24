# -*- coding: utf-8 -*-
"""Deterministisk förkontroll: kortets INNEHÅLL mot det som faktiskt hämtades.

## Varför filen finns

`baksida.validate_adamtal()` kollar FORM (tom exempelmening, saknad highlight,
grupper som inte matchar betydelser). Ingenting kollar innehållet mot källan
förrän blindgranskaren gör det -- för hand, mot betalning, sist i kedjan.

Mätt 2026-08-11: av 25 underkännanden i en batch om 100 var 10 synonymfel och
flera av resten var fel som SYNS I DEN HÄMTADE DATAN. Tre exempel, alla
verifierade i `uppslag/`:

    ganglie   SO 0 träffar, SAOL 0 träffar   -- uppslagsordet finns inte
    pryd      hits = [pryd (adj), pryda (verb)] -- glosorna blandar två ord
    oval      popularity_count 9673, märkning [] -- ingen fackterm, ändå
              satte jag domänen "matematik"

Alla tre går att fånga med ett villkor var. Varje fel som fångas här är ett
kort granskaren slipper underkänna OCH ett kort jag slipper göra om -- det är
därför den här kontrollen både höjer kvaliteten och sänker kostnaden.

## Vad den INTE är

Den dömer inte. Den flaggar, så att felen rättas innan det dyra steget körs.
En flagga kan vara falsk (homografer är legitima, `oval` är både adjektiv och
substantiv) -- därför skiljer scriptet på HÅRD och MJUK precis som
`lint_adamtal.py`, och massfixar aldrig.

**Regellogik för FORM bor i `baksida.py` och får inte dupliceras hit.** Det
här scriptet äger bara innehåll-mot-källa, en dimension baksida inte kan se
eftersom den aldrig får uppslagsdatan.

    python forgranska.py sessions/<fil>.json
    python forgranska.py sessions/<fil>.json --bara-hard
    python forgranska.py sessions/<fil>.json --json ut.json
"""
import argparse
import json
import os
import re
import sys
from collections import Counter

import baksida
import config

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HAR = os.path.dirname(os.path.abspath(__file__))

HARDA = (
    # Flyttad fran MJUKA 2026-08-24. Matt samma dag: av batch 3:s SJU
    # blindunderkannanden hade SEX redan den har flaggan -- forgranskningen
    # visste, men slappte igenom, och den dyra granskaren fick saga samma sak
    # for 0,78 USD.
    #
    # Den ska inte blockera absolut: SO:s underbetydelser ar ibland brus, och
    # ett kort behover inte alltid alla. Men beslutet maste SKRIVAS. Med
    # flaggan hard kravs en motivering i `forgranska_tillat`, precis som for
    # ovriga harda -- da blir "kortet racker" ett stallningstagande i stallet
    # for tystnad.
    #
    # Tredje gangen samma feltyp dyker upp i dag: en kontroll som observerar
    # men inte tvingar fram ett beslut blir ignorerad. Jfr spegelkontrollen
    # `synonym_saknas_trots_belagg` (4d) och registerkontrollen 2026-08-12.
    "betydelse_kan_saknas",
    "uppslagsord_saknas",
    "frammande_uppslagsord",
    "synonym_fel_relation",
    "synonym_utan_stod",
    "synonym_utan_ordboksbelagg",
    "register_motsager_markning",
)
MJUKA = (
    "doman_utan_stod",
    "uppslag_saknas",
    "synonym_saknas_trots_belagg",
)

# Underbetydelselistan innehåller maskinmarkörer som inte är betydelser.
_EJ_BETYDELSE = re.compile(r"^(SYN|JFR|ANT|SE):", re.I)

# "neutral"/"allmän" påstår ingenting och kan aldrig motsäga en märkning.
_NEUTRALA = {"neutral", "allmän", "allman", ""}

# MÄTT 2026-08-12, och det avgjorde regelns utformning: av 747 uppslag har
# bara 110 (14,7 %) någon SO-märkning alls. Den första versionen av den här
# kontrollen flaggade "stilnivå utan märkning" och slog därför ut på 19 av 20
# kort i backtestet -- den mätte frånvaro av data, inte fel i kortet.
#
# Rätt riktning är den omvända: flagga när ordboken FAKTISKT säger något och
# kortet säger något annat. Då är tystnad tystnad, och utsaga är bevis.
_MARKNING_NEUTRAL = re.compile(
    r"^(särsk|äv|ibland|vanligen|spec|numera|ofta|i sht|jfr|se|ursprungligen"
    r"|sammanfattande|eg|urspr)\b", re.I)

# Ordbokens etikett och valvets registerord är samma utsaga med olika ord.
# Utan den här tabellen slog regeln ut på `sint`, vars märkning är "prov."
# medan kortet -- korrekt -- säger "dialektal".
_MARKNING_LIKA = {
    "prov": "dialektal", "provinsiellt": "dialektal", "dial": "dialektal",
    "mindre brukligt": "ålderdomlig", "åld": "ålderdomlig",
    "ålderdomligt": "ålderdomlig", "vard": "vardaglig", "vardagligt": "vardaglig",
    "nedsätt": "nedsättande", "skämtsamt": "skämtsam", "ironiskt": "ironisk",
    "formellt": "formell", "litt": "litterär", "språkv": "lingvistik",
    "sjö": "sjöfart", "geol": "geologi", "vulg": "vulgär",
}

# Popularitetsgräns: över detta är ordet för vanligt för att rimligen bära en
# fackspråklig domän utan att ordboken märkt det som fackterm. 9673 (oval)
# ligger över; äkta facktermer i decket ligger typiskt en tiopotens lägre.
POPULARITET_VARDAGSORD = 5000


# Matchar slaupp.py:s _sakert_filnamn() (bugfix 2026-08-20): ord med "/" i sig
# (t.ex. "företa /företaga") kraschade slaupp.py:s filskrivning eftersom "/" är
# otillåtet i ett Windows-filnamn. Läsvägen här måste sanera på EXAKT samma
# sätt som skrivvägen, annars letar den här funktionen efter en fil som aldrig
# skapades under det namnet och ordet ser ut som "uppslag_saknas" trots att
# slaupp.py bevisligen kört.
_FILNAMN_OTILLATNA = re.compile(r'[\\/:*?"<>|]')


def _uppslag(ord_):
    f = os.path.join(HAR, "uppslag", _FILNAMN_OTILLATNA.sub("_", ord_) + ".json")
    if not os.path.exists(f):
        return None
    try:
        return json.load(open(f, encoding="utf-8"))
    except Exception:
        return None


def _hits(u, kalla):
    try:
        return u["svenska_se_ratt"][kalla]["hits"]["hits"]
    except Exception:
        return []


def _ortografier(u, kalla):
    ut = []
    for h in _hits(u, kalla):
        o = (h.get("_source") or {}).get("ortografi")
        if o:
            ut.append(str(o))
    return ut


def _popularitet(u):
    """Högsta popularity_count bland träffarna -- ordets vanlighet."""
    pop = []
    for kalla in ("so", "saol"):
        for h in _hits(u, kalla):
            p = (h.get("_source") or {}).get("popularity_count")
            if isinstance(p, int):
                pop.append(p)
    return max(pop) if pop else None


def _so(u, falt):
    try:
        return u["sammandrag"]["svenska_se"]["so"].get(falt) or []
    except Exception:
        return []


def _saol(u, falt):
    try:
        return u["sammandrag"]["svenska_se"]["saol"].get(falt) or []
    except Exception:
        return []


def _kallord(u):
    """Alla ord som förekommer i NÅGON hämtad källa -- stödunderlaget.

    Gloser, exempel, syn.se och wiktionary slås ihop till en påse. En synonym
    som inte finns någonstans i den påsen har inget hämtat stöd alls.
    """
    bitar = []
    for f in ("def", "underbetydelser", "exempel", "jfr"):
        bitar += [str(x) for x in _so(u, f)] + [str(x) for x in _saol(u, f)]
    try:
        avd = u["sammandrag"]["synonymer_se"].get("avdelningar") or {}
        for namn, lista in avd.items():
            # ALDRIG motsatsord. Fram till 2026-08-12 loopades avd.values()
            # rakt av, vilket gjorde att syn.se:s motsatslista räknades som
            # STÖD för en synonym -- regeln godkände alltså ord som betyder
            # tvärtom.
            if "motsats" in str(namn).lower() or "antonym" in str(namn).lower():
                continue
            bitar += [str(x) for x in lista]
    except Exception:
        pass
    try:
        bitar += [str(x) for x in (u["sammandrag"]["wiktionary"].get("definitioner") or [])]
    except Exception:
        pass
    text = " ".join(bitar).lower()
    return set(re.findall(r"[a-zåäöéèü]+", text)), text


def _stam(ord_):
    """Grov stamning: klipp vanliga svenska ändelser så att böjda former matchar."""
    o = ord_.lower().strip()
    for e in ("ande", "ende", "aste", "are", "ade", "ing", "en", "et", "er",
              "or", "ar", "as", "an", "a", "t", "s"):
        if len(o) - len(e) >= 4 and o.endswith(e):
            return o[: -len(e)]
    return o


def _har_stod(syn, kallpase, kalltext):
    """Finns synonymen i det hämtade underlaget, direkt eller som stam?"""
    s = re.sub(r"<[^>]+>", "", str(syn or "")).strip().lower()
    if not s:
        return True  # tom synonym är baksidas regel, inte vår
    if s in kalltext:
        return True
    delar = re.findall(r"[a-zåäöéèü]+", s)
    if not delar:
        return True
    # Flerordssynonym: räcker att huvudordet har stöd.
    for d in delar:
        if d in kallpase:
            return True
        st = _stam(d)
        if len(st) >= 4 and any(k.startswith(st) for k in kallpase):
            return True
    return False


# --- Ordboksbelägg för synonymer (Adams beslut 2026-08-12) --------------------
#
# `_har_stod` ovan frågar bara om ordet FÖREKOMMER någonstans i det hämtade
# underlaget. syn.se ingår i det underlaget, och syn.se blandar synonymer,
# överordnade begrepp, syskonord och lösa associationer i EN platt lista som
# `las.py` mycket riktigt märker "KANDIDATER, ej facit". Regeln var alltså
# uppfylld av precis allt syn.se råkade lista, och fyra av fem underkännanden
# i batch2 (2026-08-12) var syn.se-ord: `farsot` åt pandemi (överordnad term),
# `boja`+`förtöjning` åt kätting (fotboja respektive tross), `antikviteter` åt
# kuriosa (definieras av ålder, inte av det udda), `inmontering` åt
# installation (hörde till fel betydelse).
#
# Belägg kräver härefter att ORDBOKEN säger det, på ett av två sätt:
#   (a) SO taggar korshänvisningen `SYN:synonym`, eller
#   (b) ordet inleder ett eget led i SO:s/SAOL:s definition av uppslagsordet.
#
# Att kräva att ordet INLEDER ledet är hela finessen. SAOL definierar pandemi
# som "allomfattande farsot" -- `farsot` står där, men modifierat, och bara
# hela frasen är utbytbar. Jämför SAOL för triumfera: "segra; jubla efter att
# ha vunnit framgång", där både `segra` och `jubla` inleder sina led och
# därför är riktiga synonymglosor. En ren containment-kontroll hade släppt
# igenom farsot; den här släpper igenom segra och jubla men inte farsot.
#
# Mätt över 828 uppslag med egen SO/SAOL-post: 7 % har SYN:synonym, 24 % har
# en definition som är en synonymuppräkning, 69 % har INGET belägg alls.
# TOM SYNONYMLISTA ÄR DÄRFÖR NORMALFALLET OCH ETT GODKÄNT KORT -- se
# `baksida.tom_synonym`, som bara fångar tomma strängar i listan, aldrig en
# tom lista. För ett deck som pluggas mot HP-provets ORD-del är det dessutom
# det pedagogiskt rätta: distraktorerna där ÄR ord som ligger nära utan att
# vara utbytbara, så en nästan-synonym tränar exakt det fel provet straffar.
# SAOL inleder ofta ett synonymled med en bruklighetsmarkör: "äv. blek,
# ointressant", "ofta nedsättande", "bildl. hård". Markören är metatext om
# glosan, inte en del av den -- utan den här strippningen föll `blek` bort
# som obelagt trots att SAOL listar det, eftersom `äv.` stod först i ledet.
# Gradadverben tillagda 2026-08-13, samma argument: SO definierar `avfallen`
# som "starkt avmagrad" och `ofelbar` som "helt säkert" -- graden hör till
# definitionen, glosan är `avmagrad` respektive `säkert`. Utan dem föll båda
# bort som obelagda trots att ordboken säger exakt det ordet.
_LEDMARKOR = re.compile(
    r"^(äv\.?|ofta|ibl\.?|ibland|särsk\.?|särskilt|eg\.?|egentligen|bildl\.?|"
    r"bildligt|vanl\.?|vanligen|numera|förr|ngt|något|mest|i sht|i synnerhet|"
    r"starkt|helt|mycket|ganska|tämligen|alltför)\s+",
    re.I)

# SO sätter ofta ett frivilligt led inom parentes FÖRE glosan: "(mild)
# uppmaning till visst handlande", "(svag) ansats till förekomst". Parentesen
# är en precisering av definitionen, inte en del av synonymen -- utan den här
# strippningen blev `uppmaning` och `ansats` obelagda trots att de står där.
_INLEDANDE_PARENTES = re.compile(r"^\([^)]*\)\s*")


def _ordboksbelagg(u, ord_):
    """Ord som SO/SAOL själva pekar ut som synonymer till uppslagsordet."""
    belagg = set()
    for txt, typ in so_relationer(u).items():
        if typ == "SYN:synonym":
            belagg.add(txt)
    for kalla in ("so", "saol"):
        for h in _hits(u, kalla):
            s = h.get("_source") or {}
            if not _samma_uppslag(str(s.get("ortografi", "")), ord_):
                continue
            for hb in (s.get("huvudbetydelser") or []):
                # Underbetydelserna räknas också. SO lägger ofta sina RENASTE
                # synonymglosor där: `balsamisk` har definitionen "som doftar
                # som balsam" (en omskrivning, oanvändbar som synonym) och
                # underbetydelserna "väldoftande" + "lindrande" -- alltså
                # precis de två ord som HÖR hemma på kortet. Utan den här
                # raden underkände spärren dem båda. Hittat 2026-08-13.
                defs = [hb.get("definition") or ""]
                defs += [ub.get("definition") or "" for ub in (hb.get("underbetydelser") or []) if ub]
                for d in defs:
                    d = _LANKTEXT.sub("", d)
                    for led in re.split(r"[;,]", d):
                        led = _INLEDANDE_PARENTES.sub("", led.strip().lower())
                        led = _LEDMARKOR.sub("", led).strip().strip(".")
                        if not led:
                            continue
                        belagg.add(led)
                        forsta = re.findall(r"[a-zåäöéèü]+", led)
                        if forsta:
                            belagg.add(forsta[0])
    return belagg


_STOPPORD = frozenset(
    "som att vilken vilket vilka i med utan av pa for den det de en ett "
    "ngn ngt sarsk aven ibland vanligen ofta samt eller mycket helt "
    "delvis mojlig mojligt svag svagt starkt lite ganska utanfor inom".split())


def _synonymkandidater(belagg, ord_):
    """Ur `_ordboksbelagg`-mängden: de lemman som rimligen KAN vara synonymer.

    Mängden från `_ordboksbelagg` är avsiktligt vid -- den ska släppa igenom
    allt ordboken säger, för den används till att GODKÄNNA. Här går den åt
    andra hållet och ska föreslå, så bruset måste bort: hela definitionsfraser
    ("som beter sig på ett avvikande sätt"), stoppord och uppslagsordet själv.
    """
    def _nyckel(x):
        # jamfor utan diakriter sa "utanfor" i stopplistan traffar "utanför"
        return (x.lower().replace("å", "a").replace("ä", "a")
                 .replace("ö", "o").replace("é", "e"))

    rena = []
    for k in sorted(belagg):
        k = (k or "").strip().strip(".")
        if len(k) < 3 or len(k.split()) > 2:
            continue
        if _nyckel(k) in _STOPPORD:
            continue
        if any(_nyckel(w) in _STOPPORD for w in k.split()[:1]):
            continue
        if _samma_uppslag(k, ord_) or k.lower() == (ord_ or "").lower():
            continue
        rena.append(k)

    # `_ordboksbelagg` lagger in bade hela ledet OCH dess forsta ord. Det forsta
    # ordet ensamt ar nastan alltid ett fragment av en definitionsfras
    # ("utanfor" ur "utanfor medelpunkten"), inte en synonym. Ta bort enordare
    # som bara finns dar for att de inleder en langre kandidat.
    flerord = [k for k in rena if len(k.split()) > 1]
    ut = [k for k in rena
          if len(k.split()) > 1
          or not any(f.lower().startswith(k.lower() + " ") for f in flerord)]
    return ut


def _har_ordboksbelagg(syn, belagg):
    """Säger ordboken själv att det här är en synonym?"""
    s = _LANKTEXT.sub("", str(syn or "")).strip().strip(".").lower()
    if not s:
        return True  # tom sträng är baksidas regel, inte vår
    if s in belagg:
        return True
    # Flerordssynonym duger om dess huvudord (det första) är belagt -- "insättning
    # i ämbete" mot SAOL:s "insättning i ämbete".
    delar = re.findall(r"[a-zåäöéèü]+", s)
    if delar and delar[0] in belagg:
        return True
    # Synonymen står ORDAGRANT inne i en definitionsfras. Tillagt 2026-08-24.
    #
    # Regeln lyder att synonymen får skrivas in om den "står i SO:s eller
    # SAOL:s definitionstext". `_ordboksbelagg` delar bara på ; och , och
    # lägger in hela ledet plus dess FÖRSTA ord -- ord längre in i en fras
    # blev därför aldrig belagda. SO:s definition av `försaka` är "uppoffra
    # sig genom att avstå från", och "avstå från" underkändes trots att det
    # står där. Det är implementationen som var snävare än regeln.
    #
    # Ordgräns kollas för hand i stället för med regex: en tidigare version av
    # den här filen fick en literal backspace () inbakad när ett regex
    # skrevs via ett patchskript, och matchade då aldrig.
    for b in belagg:
        i = b.find(s)
        while i != -1:
            fore = b[i - 1] if i > 0 else " "
            efter = b[i + len(s)] if i + len(s) < len(b) else " "
            if not fore.isalpha() and not efter.isalpha():
                return True
            i = b.find(s, i + 1)

    # Böjningsvariant: ordboken skriver singular, kortet plural (rarietet/
    # rariteter). Stammen får matcha, men bara mot ett belagt ord -- inte mot
    # hela underlaget, vilket var den gamla regelns lucka.
    st = _stam(s.replace(" ", ""))
    return len(st) >= 4 and any(b.replace(" ", "").startswith(st) for b in belagg)


# SO taggar varje korshänvisning med sin RELATION. Det är den uppgiften hela
# synonymproblemet handlar om, och den kastades tidigare bort som brus.
#
# MÄTT 2026-08-12 över hela uppslagscachen:
#     JFR:cohyponym    1204     syskonord      -- ellips/oval, klenät/struva
#     SYN:synonym       148     likvärdigt     -- böld/abscess
#     MOTSATS:antonym    58     motsats        -- konkret/abstrakt
#     JFR:hyponym        23     underordnat    -- infix/affix
#     JFR:hyperonym       4     överordnat     -- rentjur/härk
#
# Åtta gånger fler syskon än synonymer. Att läsa "SO nämner ordet" som stöd
# för synonymi är alltså fel i ungefär åtta fall av nio -- vilket är precis
# felfrekvensen i synonymlistorna innan den här kontrollen fanns.
# BACKTESTAT 2026-08-12, och hypotesen FÖLL. Jag antog att `JFR:cohyponym`
# kunde blockera synonymer, eftersom taggen förklarar ellips/oval och
# klenät/struva. Mot två dygns kända domar slog regeln ut på 27 kort, varav
# bara 7 faktiskt underkändes -- och den underkände `girig`/*snål*,
# `grossist`/*grosshandlare* och `bleke`/*stiltje*, där ordet ifråga är
# SAOL:s EGEN gloss. SO använder `cohyponym` löst, även om nära synonymer.
# Den får därför inte blockera.
#
# De tre precisa taggarna behålls som ett billigt skyddsnät. De är sällsynta
# (85 förekomster mot cohyponyms 1204) och gav noll falska utslag -- men också
# noll äkta, eftersom taggarna bara täcker SO:s egna länkord: `affix` länkar
# till *prefix*, medan kortet skriver *förstavelse*. Regeln fångar alltså
# bara den som råkar använda exakt ordbokens ord.
RELATION_FEL = {
    "JFR:hyponym": "underordnat specialfall, inte synonym",
    "JFR:hyperonym": "överordnat begrepp, inte synonym",
    "MOTSATS:antonym": "MOTSATS -- betyder tvärtom",
    "mots.": "MOTSATS -- betyder tvärtom",
}
# Informativ, blockerar inte. Visas när jag skriver kort, som underlag för
# ett omdöme -- inte som dom.
RELATION_ATT_TANKA_PA = {"JFR:cohyponym": "syskonord — kontrollera utbytbarhet"}
_LANKTEXT = re.compile(r"<[^>]+>")
# SO numrerar homografer i länktexten ("1konkret", "tagg 1"). Siffran hör till
# uppslagsordets identitet, inte till ordet.
_HOMOGRAFNR = re.compile(r"^\d+|\s+\d+$")


def so_relationer(u):
    """{ord: relationstyp} ur SO:s och SAOL:s egna korshänvisningar."""
    ut = {}
    for kalla in ("so", "saol"):
        for h in _hits(u, kalla):
            for hb in ((h.get("_source") or {}).get("huvudbetydelser") or []):
                for hv in (hb.get("hänvisningar") or []):
                    typ = hv.get("typ")
                    txt = _HOMOGRAFNR.sub("", _LANKTEXT.sub("", hv.get("hänvisning") or "")).strip()
                    if typ and txt:
                        ut.setdefault(txt.lower(), typ)
    return ut


def _samma_uppslag(traff, ord_):
    """Är träffens uppslagsord samma ord, eller bara en formvariant av det?

    svenska.se listar reflexiva och avledda former som EGNA uppslagsord:
    `ajournera` ger även `ajournera sig`, `kardinal` ger `kardinal-`,
    `pellets` ger `pellet`. Sådana är inte solvens-fällan -- de hör till
    samma ord. Det som ska fångas är `pryd` -> `pryda` och `ans` -> `a`,
    alltså träffar på ett ANNAT lexem.
    """
    a, b = traff.lower().strip(" -"), ord_.lower().strip(" -")
    if a == b:
        return True
    # Partikelverb listas som egna uppslagsord: `spritta` ger även
    # `spritta till`, `bona` ger `bona om`. Listan var tidigare fyra partiklar
    # lång och missade bland annat `till`, vilket gjorde att `spritta` larmade
    # om sin egen partikelform. Partiklarna är ett slutet ordförråd -- att
    # räkna upp dem alla är billigare än att gissa.
    for suffix in (" sig", " ut", " av", " om", " till", " på", " i", " upp",
                   " ner", " ned", " bort", " fram", " efter", " igenom",
                   " emot", " mot", " för", " över", " under", " undan",
                   " ifrån", " från", " åt", " in", " loss", " sönder", " till sig"):
        if a == b + suffix or b == a + suffix:
            return True
    # Particip av partikelverb, där partikeln flyttar fram och blir prefix:
    # `bona om` -> `ombonad`, `skriva om` -> `omskriven`. Ordföljden kastas om,
    # så varken suffixlistan ovan eller prefixjämförelsen nedan ser släktskapet.
    for x, y in ((a, b), (b, a)):
        delar = x.split()
        if len(delar) == 2:
            verb, partikel = delar
            st = _stam(verb)
            if len(st) >= 3 and y.startswith(partikel) and y[len(partikel):].startswith(st):
                return True
    # Singular/plural och bestämd form av samma ord (pellets/pellet).
    #
    # Längdkravet är inte kosmetik. Utan det blev `gem` (pappersklämma) samma
    # ord som `gemen` och `te` samma ord som `tes`, eftersom -en och -s också
    # är böjningsändelser -- och då räknades det främmande uppslagsordets
    # glosor som ordets egna. `te`/`tes` stod som öppen defekt sedan
    # 2026-08-11; `gem`/`gemen` dök upp i batch3 och gjorde "pappersklämma"
    # till en belagd synonymkandidat för `gemen`. Ett kort ord plus en
    # ändelse är oftare ett ANNAT ord än en böjning av det korta.
    kort, lang = sorted((a, b), key=len)
    if len(kort) < 5:
        return False
    return lang.startswith(kort) and lang[len(kort):] in ("s", "n", "t", "en", "et", "er")


def _riktiga_underbetydelser(u):
    return [x for x in _so(u, "underbetydelser")
            if isinstance(x, str) and not _EJ_BETYDELSE.match(x.strip())]


def granska_post(p):
    """Returnerar lista med (regel, detalj) för en post.

    En post kan bära `forgranska_tillat`: {regel: motivering}. Undantaget
    döljer INTE regeln -- flaggan skrivs om till `<regel>_tillaten` och blir
    mjuk, så den syns både i förgranskningens utskrift och i sessionsfilen som
    blindgranskaren läser. Samma princip som `baksida.validate_adamtal(tillat=)`:
    *"Använd den hellre än att göra en regel mjuk -- undantaget syns då i
    sessionsfilen."* Ett tyst undantag vore värre än ingen regel alls, eftersom
    kortet då ser granskat ut.

    Motiveringen är obligatorisk. Ett undantag utan skäl behandlas som om det
    inte fanns.
    """
    fel = []
    ord_ = (p.get("ord") or "").strip()
    pr = p.get("proposed") or {}
    if not pr:
        return fel

    u = _uppslag(ord_)
    if u is None:
        fel.append(("uppslag_saknas", f"ingen uppslag/{ord_}.json -- kör slaupp.py"))
        return fel

    # 1. Uppslagsordet finns inte alls (ganglie).
    so_h, saol_h = _hits(u, "so"), _hits(u, "saol")
    if not so_h and not saol_h:
        dym = []
        for kalla in ("so", "saol"):
            try:
                for f in u["svenska_se_ratt"][kalla].get("didYouMean") or []:
                    t = f.get("text") if isinstance(f, dict) else str(f)
                    if t and t not in dym:
                        dym.append(t)
            except Exception:
                pass
        fel.append(("uppslagsord_saknas",
                    "0 träffar i SO och SAOL"
                    + (f" -- menade du: {', '.join(dym[:3])}?" if dym else "")))

    # 2. Glosorna kommer delvis från ett ANNAT uppslagsord (pryd -> pryda).
    frammande = set()
    for kalla in ("so", "saol"):
        for o in _ortografier(u, kalla):
            if not _samma_uppslag(o, ord_):
                frammande.add(o)
    if frammande:
        # Flerordsuttryck går alltid genom fritextsökningen och drar då med sig
        # tiotals grannord (solvens-fällan). Visa några och räkna resten -- hela
        # listan är brus, men ANTALET säger hur illa förorenat underlaget är.
        vis = sorted(frammande)[:6]
        mer = f" (+{len(frammande) - len(vis)} till)" if len(frammande) > len(vis) else ""
        fel.append(("frammande_uppslagsord",
                    f"{len(frammande)} främmande uppslagsord i träffarna: "
                    f"{', '.join(vis)}{mer} -- glosor kan höra till fel ord"))

    # 3. SO har fler betydelser än kortet.
    antal_so = len(_so(u, "def")) + len(_riktiga_underbetydelser(u))
    antal_kort = len(baksida.betydelser(pr.get("huvudbetydelse") or ""))
    if antal_so and antal_kort and antal_so > antal_kort:
        fel.append(("betydelse_kan_saknas",
                    f"SO har {antal_so} betydelser/underbetydelser, kortet har "
                    f"{antal_kort}"))

    # 4a. Synonym som SO uttryckligen taggar som NÅGOT ANNAT än synonym.
    #     Starkaste kontrollen i hela filen: ordboken har redan sagt att orden
    #     inte är utbytbara, med ord.
    rel = so_relationer(u)
    for s in (pr.get("synonymer") or []):
        nyckel = re.sub(r"<[^>]+>", "", str(s or "")).strip().lower()
        typ = rel.get(nyckel)
        if typ in RELATION_FEL:
            fel.append(("synonym_fel_relation",
                        f"{s!r}: SO taggar ordet som {typ} — {RELATION_FEL[typ]}"))

    # 4b. Synonymer utan stöd i något hämtat underlag.
    kallpase, kalltext = _kallord(u)
    if kallpase:
        utan = [s for s in (pr.get("synonymer") or []) if not _har_stod(s, kallpase, kalltext)]
        if utan:
            fel.append(("synonym_utan_stod",
                        f"saknar stöd i hämtad källa: {', '.join(map(str, utan))}"))

    # 4c. Synonymer som bara syn.se/wiktionary stöder -- ordboken själv säger
    #     ingenting. Tom lista passerar tyst: det är normalfallet (69 %).
    belagg = _ordboksbelagg(u, ord_)
    obelagda = [s for s in (pr.get("synonymer") or [])
                if not _har_ordboksbelagg(s, belagg)]
    if obelagda:
        fel.append(("synonym_utan_ordboksbelagg",
                    f"{', '.join(map(str, obelagda))} -- varken SO:s SYN:synonym "
                    f"eller SO/SAOL:s definitionstext säger att ordet är en synonym. "
                    f"Stryk det; tom synonymlista är godkänt"))

    # 4d. SPEGELN till 4c, tillagd 2026-08-24. Adam upptäckte att 321 av 1 432
    #     full v3-kort hade tomt synonymfält, och att andelen gick från 0 % den
    #     10-11 augusti till 13-70 % från den 12:e -- samma dag 4c infördes som
    #     HÅRT fel.
    #
    #     Orsaken var inte en bugg: `_ordboksbelagg` läser SO/SAOL:s
    #     definitionstext precis som regeln säger, och 242 av de 251 tomma
    #     korten HAR användbara kandidater. Felet var att spärren var ensidig.
    #     Att skriva en obelagd synonym underkände kortet; att utelämna den
    #     passerade tyst. Under den gradienten är det rationellt att alltid
    #     lämna fältet tomt när man är osäker -- och det är precis vad som hände.
    #
    #     Samma feltyp som registerkontrollen 2026-08-12 (se _MARKNING_NEUTRAL
    #     ovan): den mätte frånvaro av data i stället för fel i kortet. Där
    #     vändes riktningen om; här saknades motsvarigheten.
    #
    #     MJUK med flit. Kandidatmängden innehåller definitionsfraser och
    #     stoppord, så den duger till att väcka en bedömning -- aldrig till att
    #     skriva in något automatiskt.
    if not (pr.get("synonymer") or []):
        kand = _synonymkandidater(belagg, ord_)
        if kand:
            fel.append(("synonym_saknas_trots_belagg",
                        f"synonymfältet är tomt, men SO/SAOL:s egen definitionstext "
                        f"ger kandidater: {', '.join(kand[:6])}. "
                        f"Bedöm om någon är en äkta synonym -- tom lista kan "
                        f"fortfarande vara rätt svar"))

    # 5. Ordboken HAR märkt ordet, men kortets register nämner inte märkningen.
    reg = str(pr.get("register") or "").lower()
    markning = [str(x) for x in _so(u, "märkning")] + [str(x) for x in _saol(u, "märkning")]
    # Fältet `märkning` innehåller ibland en hel definitionsfras i stället för
    # en stiletikett ("sammanfattande benämning på kambrium, ordovicium och
    # silur"). En sådan kan inte motsägas av ett register. Etiketter är korta.
    sagande = [m for m in markning
               if not _MARKNING_NEUTRAL.match(m.strip()) and len(m.strip()) <= 30]
    for m in sagande:
        lag = m.lower().strip(" .")
        likvärdig = _MARKNING_LIKA.get(lag)
        if likvärdig and _stam(likvärdig)[:5] in reg:
            continue
        kärna = [w for w in re.findall(r"[a-zåäöéèü]{4,}", lag)
                 if w not in ("sammanhang", "brukligt", "dylikt")]
        kärna += [_MARKNING_LIKA[w] for w in kärna if w in _MARKNING_LIKA]
        if kärna and not any(_stam(w)[:5] in reg for w in kärna):
            fel.append(("register_motsager_markning",
                        f"SO/SAOL märker ordet {m!r} men kortets register säger "
                        f"{pr.get('register')!r}"))

    # 6. Fackspråklig domän på ett vardagsord som ordboken inte märkt som fackterm.
    pop = _popularitet(u)
    for grupp in [g.strip() for g in reg.split(";") if g.strip()]:
        delar = [d.strip() for d in grupp.split(",")]
        doman = delar[2] if len(delar) > 2 else ""
        if doman and doman not in _NEUTRALA and not markning:
            if pop is not None and pop > POPULARITET_VARDAGSORD:
                fel.append(("doman_utan_stod",
                            f"domän {doman!r} men popularitet {pop} och ingen "
                            f"märkning i SO/SAOL"))
    return fel


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fil")
    ap.add_argument("--bara-hard", action="store_true")
    ap.add_argument("--json")
    a = ap.parse_args()

    d = json.load(open(a.fil, encoding="utf-8"))
    poster = d["poster"] if isinstance(d, dict) and "poster" in d else d

    rapport, rakning = [], Counter()
    for p in poster:
        fel = granska_post(p)
        tillat = {k: v for k, v in (p.get("forgranska_tillat") or {}).items()
                  if str(v or "").strip()}
        if tillat:
            fel = [(f"{r}_tillaten", f"{t}  || MOTIVERING: {tillat[r]}")
                   if r in tillat else (r, t) for r, t in fel]
        if a.bara_hard:
            fel = [f for f in fel if f[0] in HARDA]
        if fel:
            rapport.append({"ord": p.get("ord"), "noteId": p.get("noteId"),
                            "fel": [{"regel": r, "detalj": t} for r, t in fel]})
        for r, _ in fel:
            rakning[r] += 1

    print("=" * 74)
    print(f"FÖRGRANSKNING  {os.path.basename(a.fil)}  --  {len(poster)} poster, "
          f"{len(rapport)} med anmärkning")
    print("=" * 74)
    for grupp, namn in ((HARDA, "HÅRD"), (MJUKA, "MJUK")):
        rader = [(r, n) for r, n in rakning.most_common() if r in grupp]
        if rader:
            print(f"\n[{namn}]")
            for r, n in rader:
                print(f"  {n:4d}  {r}")
    for post in rapport:
        print(f"\n  {str(post['ord']).upper()}")
        for f in post["fel"]:
            märke = "!!" if f["regel"] in HARDA else "  "
            print(f"    {märke} {f['regel']}: {f['detalj']}")

    if a.json:
        json.dump(rapport, open(a.json, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        print(f"\nSkrev {a.json}")

    hard = sum(n for r, n in rakning.items() if r in HARDA)
    print(f"\n{hard} hårda anmärkningar -- rätta dem INNAN blindgranskningen.")


if __name__ == "__main__":
    main()
