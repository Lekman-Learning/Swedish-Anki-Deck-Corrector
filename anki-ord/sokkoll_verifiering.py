"""Hål 0 — gör sökkollen maskinellt bevisbar i stället för påstådd.

Bakgrund (2026-08-09). `applicera` vägrade redan skriva ett kort med TOMT
`sokkoll`-fält. Det var tänkt att göra kravet "sökkoll på varje kort"
kontrollerbart. Men spärren kunde bara se ATT fältet var ifyllt — inte att
innehållet var sant. Den dagen granskades 141 kort och fältet påstod
"svenska.se (SAOL/SO/SAOB)" på i praktiken alla. Mätt mot loggen: **11 av 141
hade en faktisk uppslagning.** Spärren släppte igenom allihop.

Felet var inte slarv. Det var att den som gjorde arbetet också skrev intyget
om att arbetet gjorts. Samma asymmetri som `paket`/`verdikt` finns för att
lösa på innehållssidan — fast här för källorna.

Lösningen: `kalla` måste innehålla en URL, och den URL:en måste finnas i ett
**oberoende vittne** — Claude Codes eget transkript, som skrivs löpande av
verktygslagret och inte går att redigera av den som granskar. `raw-websearch/`
i valvet är en extraktion av samma transkript och används som reserv för
äldre datum.

Begränsning som ska sägas rakt ut: den här modulen bevisar att en hämtning
FAKTISKT GJORDES mot en angiven URL. Den kan inte bevisa att granskaren läste
svaret rätt. Den stänger hålet "påstod uppslag som aldrig gjordes" — inte
hålet "gjorde uppslag och drog fel slutsats". Det senare är vad `verdikt`
finns för.
"""

import glob
import json
import os
import re
import urllib.parse

# Kanaler som duger som källa, alla testade med WebFetch 2026-08-09.
#
# DE TRE SOM SKA ANVÄNDAS, i denna ordning per kort:
#
#   1. https://www.saob.se/artikel/?seek=<ord>
#      SAOB — Svenska Akademiens ordbok, den auktoritativa. Ordadresserbar
#      och serverrenderad. Ger numrerade betydelser, etymologi och belägg.
#      OBS: `?seek=` är ingången som fungerar. `?unik=<id>` fungerar också
#      men id:t går inte att konstruera ur ordet.
#
#   2. https://sv.wiktionary.org/wiki/<ord>
#      Modernt språkbruk, numrerade betydelser, ordklass, etymologi.
#      Kompletterar SAOB, som är historisk och ibland tung att läsa.
#
#   3. https://www.synonymer.se/sv-syn/<ord>
#      Synonymlistor. Svag på betydelseuppräkning — använd den till
#      synonymkontroll, inte till att avgöra hur många betydelser ett ord har.
#
# Att det behövs mer än en källa är inte teori: 2026-08-09 rättades `tabernakel`
# ur eget huvud till två betydelser (Wiktionary listar fyra) och `trolsk` till
# en (SAOB listar två). Två av fyra testhämtningar avslöjade en ofullständig
# rättelse som redan var skriven till Anki.
GODKANDA_VARDAR = (
    "saob.se",
    "wiktionary.org",
    "synonymer.se",
    "ne.se",
    "isof.se",
    "sprakochfolkminnen.se",
    "runeberg.org",
    "tyda.se",
)

# svenska.se (SAOL/SO/SAOB i ett) är JS-renderad. Med WebFetch ger både
# /tre/?sok= och det äldre /tri/f_saol.php?sok= ett tomt skal med enbart
# navigering — att tillåta det hade gjort det möjligt att "belägga" ett ord med
# en tom sida.
#
# MEN med en riktig webbläsare renderar den (bevisat 2026-08-09 med Playwright).
# Därför är svenska.se inte blockerad rakt av, utan **kanalberoende**: giltig
# bara om beviset kommer från en browser-navigering, aldrig från WebFetch.
# Det är en skarpare regel än ett förbud, och den kan kontrolleras maskinellt
# eftersom transkriptet skiljer på verktygen.
#
# Varför det är värt besväret: svenska.se ger SAOL + SO + SAOB på EN sida, och
# SO är den bästa enskilda källan för korten — numrerade betydelser,
# exempelmeningar, etymologi och JFR-hänvisningar som är färdiga synonymuppslag.
# Ett anrop ersätter tre, och ger mer.
KANALBEROENDE_VARDAR = (
    "svenska.se",
)

BLOCKERADE_VARDAR = ()

# Verktygsnamn som räknas som "renderande webbläsare" i transkriptet.
BROWSERVERKTYG = (
    "mcp__playwright__browser_navigate",
    "browser_navigate",
)

# Tredje kanalen, tillagd 2026-08-09: `slaupp.py` slår upp många ord i en process
# och skriver en bevisrad per ord i sin UTSKRIFT:
#
#     SVENSKA_SE_HAMTAD <ord> HTTP 200 <byte>
#
# Raden produceras av processen och fångas av verktygslagret. Agenten kan
# formulera kommandot men inte hitta på dess utdata — samma egenskap som gör
# transkriptets `input.url` till ett giltigt vittne. Kalla-formen som matchar är
#
#     https://svenska.se/api/msearch?ord=<ord>
#
# OBS: frågeparameter, INTE fragment. Ett fragment (#ord) klipps bort av
# _normalisera och gjorde alla msearch-URL:er identiska -- spärren släppte då
# igenom ord som aldrig hämtats. Hittat av modulens eget test 2026-08-09,
# samma dag kanalen skrevs. Andra gången exakt det felet uppstår i den här
# filen: att jämföra på något som råkar vara lika för alla är samma bugg som
# att bara kontrollera att fältet är ifyllt.
#
# Varför kanalen behövdes: webbläsarvägen kostade två anrop per ord, och deras
# svar låg kvar i kontextfönstret. Tjugo kort tog slut på utrymme långt före
# kvoten. Skriptvägen gör tjugo ord till ett anrop.
# (.+?) och inte (\S+): flerordsuppslag som "bekväma sig" innehåller
# mellanslag, och \S+ fångade bara första ordet. Kalla sa "?ord=bekväma sig"
# men beviset registrerades som "bekväma" -- kortet stoppades trots att
# hämtningen gjorts. Hittat 2026-08-09 av spärren själv, på batch 7.
#
# UTÖKAT 2026-08-10 (Adams krav på tre källor per kort): samma skript hämtar nu
# även synonymer.se och Wiktionary, och skriver en egen bevisrad för var och en.
# Varje markör paras ihop med den URL-form som `kalla` måste ha för att räknas
# som belagd av just den hämtningen — så att ett kort inte kan hänvisa till
# synonymer.se med ett bevis som bara gäller svenska.se.
SKRIPTKANALER = (
    ("SVENSKA_SE_HAMTAD", "https://svenska.se/api/msearch?ord={}"),
    ("SYNONYMER_SE_HAMTAD", "https://www.synonymer.se/sv-syn/{}"),
    ("WIKTIONARY_HAMTAD", "https://sv.wiktionary.org/wiki/{}"),
)
# Bytesantalet måste vara SIFFROR, inte bara "något efter HTTP 200". Kravet
# tillkom 2026-08-11: modulens egen dokumentationsrad
#
#     SVENSKA_SE_HAMTAD <ord> HTTP 200 <byte>
#
# matchade mönstret och registrerade ordet `<ord>` som bevisligen hämtat. Den
# raden hamnade i loggen bara för att filen greppats under en session -- alltså
# blev en KOMMENTAR OM formatet ett bevis PÅ formatet. Ingen kort heter `<ord>`,
# så ingenting släpptes igenom i praktiken, men felklassen är den samma som
# fragment-buggen och den ifyllda-fältet-buggen: något som ser ut som en
# mätning utan att vara en. En riktig hämtning har alltid en storlek.
SKRIPTMARKOR = re.compile(
    r"(" + "|".join(m for m, _ in SKRIPTKANALER) + r")\s+(.+?)\s+HTTP\s+200\s+\d+")
SKRIPT_KALLA = re.compile(r"svenska\.se/api/msearch\?ord=(.+)$")

_URL_RE = re.compile(r"https?://[^\s\"'<>,;)\]]+")
_URL_START = re.compile(r"https?://")


def _urler_ur_kalla(kalla):
    """URL:erna i en `kalla`-strang -- aven de som innehaller MELLANSLAG.

    `_URL_RE` stannar vid forsta blanksteget, vilket ar ratt for text men fel
    har: uppslagsordet ligger i URL:en, och ett uppslagsord kan besta av flera
    ord. `https://svenska.se/api/msearch?ord=creme de la creme` kapades till
    `...?ord=creme`, som aldrig matchade beviset -- och eftersom bevisnyckeln
    byggs av samma okodade ord (se samla_bevis) foll BARA flerordsuttrycken.

    Matt 2026-08-30: 7 av 100 kort i en omgang stoppades av detta, alla
    flerordsuttryck (crème de la crème, i allo, se tiden an, pa kuppen,
    blommor och bin, grunda sig pa, ga tretton pa dussinet). Felet var inte
    slumpmassigt utan systematiskt -- INGET flerordsuttryck kunde nagonsin
    passera sokkollen.

    Segmenten delas vid nasta `http`, inte vid blanksteg. Den kapade formen
    laggs till som extra kandidat, sa att en kalla med efterfoljande brodtext
    fortfarande kan matcha.
    """
    starter = [m.start() for m in _URL_START.finditer(kalla or "")]
    ut = []
    for i, start in enumerate(starter):
        slut = starter[i + 1] if i + 1 < len(starter) else len(kalla)
        bit = kalla[start:slut].strip()
        if bit:
            ut.append(bit)
    for u in _URL_RE.findall(kalla or ""):
        if u not in ut:
            ut.append(u)
    return ut



def _transkriptkatalog():
    return os.path.join(os.path.expanduser("~"), ".claude", "projects")


def _tool_use_urler(nod, ut, verktyg, kanal):
    """Plockar url-PARAMETERN ur anrop till `verktyg`. Rekursivt, eftersom
    transkriptets struktur varierar mellan versioner. Skriver in kanalen så att
    granska_kalla kan skilja WebFetch från renderande webbläsare."""
    if isinstance(nod, dict):
        if nod.get("type") == "tool_use" and nod.get("name") in verktyg:
            url = (nod.get("input") or {}).get("url")
            if isinstance(url, str):
                ut[url] = kanal
        for v in nod.values():
            _tool_use_urler(v, ut, verktyg, kanal)
    elif isinstance(nod, list):
        for v in nod:
            _tool_use_urler(v, ut, verktyg, kanal)


def _urler_ur_transkript():
    """URL:er som FAKTISKT hämtats, lästa ur Claude Codes transkript.

    Transkriptet skrivs löpande av verktygslagret under sessionens gång, så
    en hämtning gjord tidigare i samma tur syns här direkt — till skillnad
    från raw-websearch/, som skrivs först vid Stop-hooken.

    KRITISKT: bara `input.url` på ett faktiskt WebFetch-anrop räknas. En
    tidigare version drog varje URL som förekom på en rad som nämnde
    "WebFetch" — då räckte det att SKRIVA en URL för att "bevisa" en
    hämtning, vilket upphäver hela modulens syfte. Upptäckt av det egna
    testet 2026-08-09, samma dag modulen skrevs.
    """
    urler = {}
    kanaler = ((("WebFetch", "web_fetch"), "webfetch"),
               (BROWSERVERKTYG, "browser"))
    # Rekursiv (**), inte "*/*.jsonl" -- fixat 2026-08-18. En subagent (Agent-
    # verktyget) loggar till en EGEN fil under en "subagents/"-underkatalog,
    # t.ex. projects/<projekt>/<session>/subagents/agent-<id>.jsonl, tre nivåer
    # under _transkriptkatalog(). "*/*.jsonl" hittar bara filer EN nivå ned och
    # missar den helt -- upptäckt när 14 av 19 ord i en dagsbatch skriven av en
    # subagent blockerades med "hämtningen gjordes aldrig" trots att
    # SVENSKA_SE_HAMTAD-raden bevisligen fanns i subagentens transkript (grep
    # hittade den direkt). De 5 som ändå gick igenom kom av en slump från en
    # ISOLERAD kopia i förälderns egen (icke uppdaterade) transkriptfil, inte
    # från subagentens. Samma fix i _ord_ur_skriptutskrift() nedan.
    monster = os.path.join(_transkriptkatalog(), "**", "*.jsonl")
    for sokvag in glob.glob(monster, recursive=True):
        try:
            with open(sokvag, encoding="utf-8", errors="ignore") as f:
                for rad in f:
                    for verktyg, kanal in kanaler:
                        if not any(f'"{v}"' in rad for v in verktyg):
                            continue
                        try:
                            _tool_use_urler(json.loads(rad), urler, verktyg, kanal)
                        except ValueError:
                            continue
        except OSError:
            continue
    return urler


def _urler_ur_valvloggen(valvsokvag):
    """Reserv: raw-websearch/ i valvet. Används för äldre datum.

    Loggen skiljer inte på verktyg, så allt härifrån räknas som `webfetch` --
    den svagare kanalen. En kanalberoende värd kan alltså aldrig beläggas ur
    valvloggen ensam, vilket är rätt: vi vet inte hur sidan hämtades."""
    urler = {}
    if not valvsokvag:
        return urler
    for sokvag in glob.glob(os.path.join(valvsokvag, "raw-websearch", "*.md")):
        try:
            with open(sokvag, encoding="utf-8", errors="ignore") as f:
                for rad in f:
                    if rad.startswith("**URL:**"):
                        for u in _URL_RE.findall(rad):
                            urler.setdefault(u, "webfetch")
        except OSError:
            continue
    return urler


def _ord_ur_skriptutskrift():
    """Ord som `slaupp.py` bevisligen hämtat, lästa ur verktygsutskrifter.

    Bara rader med HTTP 200 räknas — en 404 eller ett nätverksfel skriver en
    annan statuskod och ger därför inget belägg. Det är avsiktligt: ett
    misslyckat uppslag ska aldrig kunna passera som ett lyckat.

    Returnerar en mängd av (markör, ord) — inte bara ord — så att beviset för
    en hämtning från synonymer.se inte av misstag kan belägga en hänvisning
    till svenska.se. Tre källor per kort är bara meningsfullt om de tre går
    att skilja åt i efterhand."""
    ut = set()
    # Rekursiv, samma skäl och samma fix som i _urler_ur_transkript() ovan --
    # subagent-transkript ligger under en "subagents/"-underkatalog som
    # "*/*.jsonl" inte når.
    monster = os.path.join(_transkriptkatalog(), "**", "*.jsonl")
    markorer = tuple(m for m, _ in SKRIPTKANALER)
    for sokvag in glob.glob(monster, recursive=True):
        try:
            with open(sokvag, encoding="utf-8", errors="ignore") as f:
                for rad in f:
                    if not any(m in rad for m in markorer):
                        continue
                    # Raden är JSON-kodad i transkriptet; \n blir \\n. Sök i
                    # råsträngen efter avkodning av de vanligaste escaperna.
                    for m in SKRIPTMARKOR.finditer(rad.replace("\\n", "\n")):
                        ut.add((m.group(1), m.group(2)))
        except OSError:
            continue
    return ut


def _ord_ur_valvets_verktygslogg(valvsokvag):
    """Reserv: `raw-verktyg/` i valvet. Behövs när arbetet gjordes på en ANNAN
    maskin.

    Varför lagret måste läsas. `_ord_ur_skriptutskrift` letar i Claude Codes
    transkriptkatalog, som är **maskinlokal**. 2026-08-11 skrevs 50 kort på
    laptopen och skulle blindgranskas på PC:n; sessionsfilen följde med genom
    git, men beviset gjorde inte det, och Hål 0 stoppade alla 50 med
    "hämtningen gjordes aldrig". Den hade gjorts — 60 bevisrader låg i
    `raw-verktyg/2026-08-11_965e18c1.md`, i valvet, redan pushat. Spärren
    tittade bara aldrig där.

    Att läsa lagret försvagar inte kravet. Filerna skrivs av valvets Stop- och
    SessionEnd-hookar direkt ur transkriptet, inte av den som granskar, och de
    är dessutom committade och pushade — en ändring i efterhand syns i git,
    vilket är mer än vad den lokala transkriptfilen erbjuder. Det är samma
    vittne, bara persisterat.

    Kanalen sätts till 'skript', som för utskriften det kommer ur. Bara
    HTTP 200 räknas, av samma skäl som där: ett misslyckat uppslag får aldrig
    passera som ett lyckat.
    """
    ut = set()
    if not valvsokvag:
        return ut
    for sokvag in glob.glob(os.path.join(valvsokvag, "raw-verktyg", "*.md")):
        try:
            with open(sokvag, encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except OSError:
            continue
        for m in SKRIPTMARKOR.finditer(text):
            ut.add((m.group(1), m.group(2)))
    return ut


def samla_bevis(valvsokvag=None):
    """{url: kanal} för varje URL som bevisligen hämtats.

    Kanaler: 'browser' (renderande webbläsare), 'skript' (slaupp.py:s utskrift)
    och 'webfetch'. Transkriptet vinner över valvloggen — det är det starkare
    vittnet."""
    bevis = _urler_ur_valvloggen(valvsokvag)
    bevis.update(_urler_ur_transkript())
    mall = dict(SKRIPTKANALER)
    # Valvets verktygslogg först, transkriptet sedan: båda ger kanalen
    # 'skript', så ordningen ändrar inget värde -- men den gör avsikten
    # tydlig, att den lokala källan är förstahandsvittnet.
    for markor, o in _ord_ur_valvets_verktygslogg(valvsokvag):
        bevis[mall[markor].format(o)] = "skript"
    for markor, o in _ord_ur_skriptutskrift():
        bevis[mall[markor].format(o)] = "skript"
    return bevis


def _normalisera(url):
    """Jämför utan schema, www, procentkodning och avslutande slash — samma sida
    ska matcha oavsett hur den skrevs in i kalla-fältet.

    Procentavkodningen tillkom 2026-08-09: `?sok=fördärvlig` och
    `?sok=f%C3%B6rd%C3%A4rvlig` är samma sida, men jämfördes som olika strängar
    och två faktiskt hämtade kort stoppades. Avkodningen är kanonisering, inte
    uppmjukning — kravet på en verklig hämtning är oförändrat."""
    u = urllib.parse.unquote(url).lower().split("#")[0].rstrip("/")
    for prefix in ("https://", "http://"):
        if u.startswith(prefix):
            u = u[len(prefix):]
    if u.startswith("www."):
        u = u[4:]
    return u


def granska_kalla(kalla, bevis):
    """(ok, motivering). ok=False betyder att kortet INTE får skrivas."""
    if not kalla:
        return False, "kalla saknas"

    urler = _urler_ur_kalla(kalla)
    if not urler:
        return False, ("kalla saknar URL — fri text duger inte längre, "
                       "se sokkoll_verifiering.py")

    normaliserat = {_normalisera(b): kanal for b, kanal in bevis.items()}
    for url in urler:
        n = _normalisera(url)
        if any(v in n for v in BLOCKERADE_VARDAR):
            return False, f"{url} är blockerad"
        kanalberoende = any(v in n for v in KANALBEROENDE_VARDAR)
        if not kanalberoende and not any(v in n for v in GODKANDA_VARDAR):
            continue
        kanal = normaliserat.get(n)
        if kanal is None:
            continue
        # Skriptkanalen hämtar via API:t, inte via den JS-byggda sidan, och är
        # därför lika giltig som webbläsaren för svenska.se.
        if kanalberoende and kanal not in ("browser", "skript"):
            return False, (f"{url} kräver renderande webbläsare — sidan är "
                           "JS-byggd och ger tomt skal via WebFetch")
        return True, f"{url} [{kanal}]"
    return False, (f"ingen av URL:erna i kalla finns i transkript/raw-websearch "
                   f"({', '.join(urler[:3])}) — hämtningen gjordes aldrig")


def rapport(poster, valvsokvag=None):
    """Torrkörning: vilka kort skulle släppas igenom, och varför inte."""
    bevis = samla_bevis(valvsokvag)
    ok, fel = [], []
    for e in poster:
        giltig, motiv = granska_kalla((e.get("sokkoll") or {}).get("kalla"), bevis)
        (ok if giltig else fel).append((e.get("ord"), motiv))
    return ok, fel, len(bevis)
