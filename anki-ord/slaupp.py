"""Slår upp många ord i SAOL/SO/SAOB på en gång, utanför agentens kontextfönster.

BAKGRUND. Adam 2026-08-09: *"finns det något jag kan göra så att du gör alla 20,
och inte bara 7?"* Diagnosen: taket är inte kvoten (15 kort kostade 4 % av ett
femtimmarsfönster) utan **kontextfönstret**. Varje kort krävde två
webbläsaranrop vars svar sedan ligger kvar i kontexten hela sessionen. Tjugo kort
= fyrtio anrop = slut på utrymme långt före slut på kvot.

Det här skriptet gör uppslagningen i EN process i stället. Tjugo ord blir ett
verktygsanrop och en kompakt sammanfattning, i stället för fyrtio svar.

HUR BEVISKEDJAN HÅLLER. Hål 0 bygger på att `kalla` måste peka på en hämtning som
finns i ett vittne agenten inte kan skriva i. Med webbläsaren var vittnet
`browser_navigate`-anropets `input.url` i transkriptet. Här är vittnet i stället
**skriptets utskrift**: raden

    SVENSKA_SE_HAMTAD <ord> HTTP <status> <byte>

skrivs av processen, fångas av verktygslagret och hamnar i transkriptet och i
`raw-verktyg/`. Agenten kan formulera kommandot men inte hitta på dess utdata.
Egenskapen som gör Hål 0 meningsfull är alltså bevarad: **det går inte att påstå
en hämtning som inte gjordes.**

Vad skriptet INTE skyddar mot är detsamma som förut: att jag hämtar rätt sida och
ändå läser den fel. Det är vad `verdikt` finns för.

ANVÄNDNING
    python slaupp.py ord1 ord2 ...
    python slaupp.py --fil kvar.json --antal 20

Full JSON per ord sparas i `uppslag/<ord>.json` så att en senare granskare kan
läsa exakt vad källan sa, inte bara min sammanfattning.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# Windows-konsolen kor cp1252 och kan inte skriva a/a/o. Utan raden nedan
# skrevs bevisraden "SVENSKA_SE_HAMTAD bekantgora HTTP 200" med ett
# ERSATTNINGSTECKEN (U+FFFD) i stallet for o -- redan innan Claude Codes
# transkript sag den.
#
# Foljden var inte en synlig krasch utan en TYST sparr: Hal 0-kontrollen letar
# efter ordet i bevisraden, hittade "bekantg<FFFD>ra", och kunde darfor aldrig
# belagga ett enda ord med a, a eller o. Atta kort stoppades 2026-08-10 med
# beskedet "hamtningen gjordes aldrig" -- fast den var gjord, tre ganger om.
# En sparr som avvisar en tredjedel av svenskan ser exakt likadan ut som en
# sparr som gor sitt jobb.
#
# TREDJE forekomsten av samma buggklass samma dag (verktyg/lint.py i valvet och
# kortgranskare.py fick samma rad). Monstret ar alltid detsamma: svensk text +
# Windows-konsol + ett script som ingen kor interaktivt och darfor ingen ser
# fela.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

API = "https://svenska.se/api/msearch"
UTKAT = "uppslag"

# Filnamnsbugg hittad 2026-08-20 (batch5): ord som "företa /företaga" har ett
# "/" i sig -- en giltig del av ordet (två alternativa former separerade med
# mellanslag-snedstreck), men ett OTILLÅTET tecken i ett Windows-filnamn.
# os.path.join(UTKAT, f"{o}.json") kastade FileNotFoundError och kraschade HELA
# processen (inte bara det ordet) eftersom skriptet kör alla ord i EN loop utan
# per-ord felfångst -- exakt den kontextfönsterbesparing filen finns för att ge
# blev alltså också en enda felkälla för alla 50 ord i batchen. Samma riskklass
# som windows-encodingbuggarna ovan: ett tecken som är helt normalt i svensk
# text kraschar tyst mot en plattformsbegränsning ingen ser förrän den kör.
_FILNAMN_OTILLATNA = re.compile(r'[\\/:*?"<>|]')


def _sakert_filnamn(ord_: str) -> str:
    """Ersätter Windows-otillåtna filnamnstecken med '_' för uppslag/<ord>.json.

    Bara filnamnet påverkas -- ordet som skickas till API:erna och skrivs i
    JSON-innehållet (fältet "ord") är orört, så uppslaget fortfarande går att
    hitta på det riktiga ordet vid läsning av filens innehåll.
    """
    return _FILNAMN_OTILLATNA.sub("_", ord_)

# Uppslagsordskontroll (2026-08-11). svenska.se:s msearch är en FRITEXTSÖKNING:
# saknas ordet returnerar den grannartiklar med HTTP 200 i stället för tomt.
# `ytong` (ett varumärke, inte ett uppslagsord) gav artikeln för **yta** --
# "yttersta skikt av något" -- och trekällskontrollen räknade svenska.se som
# komplett, eftersom den bara såg att anropet lyckades. Kortet såg alltså
# sökkollat ut medan uppslagningen handlade om ett annat ord.
#
# Fixen stod föreslagen men ogenomförd i CLAUDE.md sedan 2026-08-11:
# "låt trekällskontrollen räkna en källa som fullständig först när den har en
# exakt uppslagsordsträff. Då blir 'tre källor' ett påstående om ORDET i
# stället för om HTTP-anropen."
#
# Varje ordbok lagrar uppslagsordet i sitt eget fält:
HUVUDORDSFALT = {"saol": "ordled", "so": "ortografi", "saob": "lemma"}


def _norm(x):
    """Jämförbar form: gemener, utan bindestreck, punkter och avstavningstecken.

    SAOL:s `ordled` avstavas med '·' (yt·lig) och SO:s `ortografi` kan bära
    accenter -- en rå strängjämförelse hade underkänt korrekta träffar.
    """
    return re.sub(r"[^0-9a-zåäöéèüáó]", "", (x or "").lower())


def variantformer(ord_):
    """Former att prova när kortets ord inte är ordbokens uppslagsform.

    Adam 2026-08-11: *"är det inte bara att loafer är loafers istället."* Han
    hade rätt -- `loafers` träffar SAOL och SO, `loafer` ingenting. Ordet är
    inlånat i pluralform, och SAOL för in det så.

    Utan den här listan pausas sådana kort som "osökbara" trots att de står i
    ordboken under en annan form. Det är ett dyrare fel än det ser ut: ett
    pausat kort försvinner ur kön och ingen letar efter det igen.

    Listan är avsiktligt KORT och mekanisk -- inte en böjningsmotor. Den
    provar de former som faktiskt orsakat missar, och varje träff verifieras
    ändå mot uppslagsordet, så en felaktig gissning kan inte smyga in.
    """
    o = ord_.strip()
    kand = [o + "s", o + "er", o + "ar", o + "or", o + "a", o + "e"]
    if o.endswith("s"):
        kand.insert(0, o[:-1])          # loafers -> loafer, och tvärtom
    if o.endswith(("d", "t")):
        kand += [o[:-1], o[:-1] + "a"]  # flängd -> flänga, vederkvickt -> ...
    if o.endswith("ad"):
        kand.append(o[:-2] + "a")
    # Bevara ordning, ta bort dubbletter och ordet självt.
    sett, ut = {o}, []
    for k in kand:
        if k not in sett and len(k) > 2:
            sett.add(k)
            ut.append(k)
    return ut


# synonymer.se som fullvärdig källa -- men bara den REDAKTIONELLA delen
# (Adams beslut 2026-08-11: "om ordet finns på synonymer.se så räcker det …
# synonymer.se räknas också som en top tier verifiering").
#
# Villkoret behövde skärpas ett steg, och motexemplet kom ur samma samtal:
# `anhedoni` FINNS på synonymer.se, men bara som användarbidrag, och glosan
# där är "livströtthet" -- vilket är fel. Anhedoni är oförmåga att känna
# njutning, inte livströtthet. En regel som säger "finns på synonymer.se
# räcker" hade alltså godkänt kortet mot en felaktig källa.
#
# Skillnaden är mekanisk och behöver inget omdöme: sajten levererar sina
# avsnitt med namn, och `Användarnas bidrag` är utpekat. Mätt över 583
# sparade uppslagningar: 555 har redaktionellt innehåll, 27 har BARA
# användarbidrag -- och de 27 är genomgående facktermer (anhedoni, ftalat,
# gemmologi, daktyloskopi), alltså precis där en crowdsourcad gloss är som
# minst pålitlig.
ANVANDARAVDELNING = "användarnas bidrag"


def synonymer_se_redaktionell(syn):
    """True om synonymer.se har RIKTIGT redaktionellt innehåll för ordet.

    Användarbidrag räknas inte, och inte heller sajtens tomma platshållare
    ("tillbaka i grottekvarnen"), som annars gör en tom avdelning till en
    falsk träff.
    """
    if not isinstance(syn, dict) or not syn.get("finns"):
        return False
    for namn, innehall in (syn.get("avdelningar") or {}).items():
        if ANVANDARAVDELNING in namn.lower():
            continue
        poster = innehall if isinstance(innehall, list) else [innehall]
        if any(p and "grottekvarnen" not in str(p) for p in poster):
            return True
    return False


def uppslagsordstraffar(data, ord_):
    """Vilka ordböcker som faktiskt har ORDET som uppslagsord.

    För flerordsuttryck räcker det att ett av leden är uppslagsord: idiom
    finns inte som egna artiklar (`av hävd` står under **hävd**), vilket
    BLINDGRANSKNING.md redan föreskriver som arbetssätt. Utan det undantaget
    hade varje idiom felaktigt rapporterats som osourcat.
    """
    no = _norm(ord_)
    delar = {_norm(d) for d in ord_.split()} - {""}
    traffar = []
    for kalla, falt in HUVUDORDSFALT.items():
        traf = (data or {}).get(kalla) or {}
        huvudord = {_norm((h.get("_source") or {}).get(falt))
                    for h in ((traf.get("hits") or {}).get("hits") or [])} - {""}
        if no in huvudord or (len(delar) > 1 and delar & huvudord):
            traffar.append(kalla)
    return traffar
INDEX = {"saol": "sa-svenska-saol", "so": "sa-svenska-so", "saob": "sa-svenska-saob"}

# TRE KÄLLOR PÅ VARJE KORT (Adams krav 2026-08-10): svenska.se (SO+SAOL+SAOB
# räknas som EN källa), synonymer.se och Wiktionary. Kort där någon av dem inte
# ger något ska rödflaggas och samlas i en egen lista att gå igenom senare --
# de ska INTE tyst skrivas med två källor, för då blir ett halvbelagt kort
# omöjligt att skilja från ett fullbelagt i efterhand.
#
# Alla tre hämtas i SAMMA process av samma skäl som svenska.se gjorde det:
# annars kostar tre källor tre gånger så mycket kontextfönster, och det är
# kontextfönstret -- inte kvoten -- som är taket (mätt 2026-08-09).
SYN_URL = "https://www.synonymer.se/sv-syn/{}"
WIKT_API = ("https://sv.wiktionary.org/w/api.php?action=query&prop=extracts"
            "&explaintext=1&redirects=1&format=json&titles={}")
WIKT_URL = "https://sv.wiktionary.org/wiki/{}"
BRISTLISTA = "tre_kallor_saknas.json"


def _kropp(ord_, exakt=True):
    return {"debugDidYouMean": False,
            **{k: {"index": v, "query": ord_, "exact_match": exakt,
                   "from": 0, "size": 30} for k, v in INDEX.items()}}


def hamta(ord_, forsok=3, exakt=True):
    """Returnerar (data, status, byte). Kastar aldrig — fel rapporteras.

    `exakt=False` faller tillbaka på fritextsökning. Behövs eftersom
    `exact_match` kräver att uppslagsordets EXAKTA form träffas: *loafer* gav
    noll träffar därför att SAOL och SO har uppslaget under pluralformen
    **loafers**. Ordet fanns hela tiden; frågan var för strikt. Upptäckt
    2026-08-10 efter att Adam ifrågasatte att just det ordet skulle saknas i
    ordböckerna -- han hade rätt.

    Exakt sökning provas alltid först, eftersom fritext annars ger grannord
    ('deg' för *degression*) som ser ut som träffar men inte är det."""
    data = json.dumps(_kropp(ord_, exakt)).encode()
    hdr = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0",
           "Origin": "https://svenska.se", "Referer": "https://svenska.se/"}
    for n in range(forsok):
        try:
            with urllib.request.urlopen(
                    urllib.request.Request(API, data=data, headers=hdr), timeout=25) as r:
                rå = r.read()
                return json.loads(rå), r.status, len(rå)
        except urllib.error.HTTPError as e:
            return None, e.code, 0
        except Exception:
            if n == forsok - 1:
                return None, 0, 0
            time.sleep(1.5 * (n + 1))
    return None, 0, 0


# Wikimedia kräver en beskrivande User-Agent och strypte annars anropen till
# HTTP 429 efter ett tiotal ord (uppmätt 2026-08-10). Det var farligare än det
# lät: en 429 gav tom text, och tom text tolkades som "ordet finns inte i
# Wiktionary" -- alltså hamnade fullt normala ord som `pöbel` och `förvärva` i
# bristlistan över kort som saknar en källa. En strypning som ser ut som ett
# saknat uppslag är precis den sortens tysta fel hela sökkollen finns för att
# hindra, och den skulle ha fått mig att rödflagga rätt kort av fel skäl.
ANVANDARAGENT = ("anki-ord/1.0 (svenskt ordkortsprojekt; kontakt via "
                 "github.com/Lekman-Learning) python-urllib")


def _hamta_ratt(url, forsok=4):
    """Rå GET. Returnerar (text, status, byte). Kastar aldrig.

    Status 429 backas av och görs om -- den betyder 'för snabbt', inte 'finns
    inte'. Går det ändå inte returneras 429 som status, och anroparen skiljer
    den från ett tomt men lyckat svar."""
    hdr = {"User-Agent": ANVANDARAGENT}
    for n in range(forsok):
        try:
            with urllib.request.urlopen(
                    urllib.request.Request(url, headers=hdr), timeout=25) as r:
                rå = r.read()
                return rå.decode("utf-8", "replace"), r.status, len(rå)
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and n < forsok - 1:
                time.sleep(3.0 * (n + 1))
                continue
            return None, e.code, 0
        except Exception:
            if n == forsok - 1:
                return None, 0, 0
            time.sleep(1.5 * (n + 1))
    return None, 0, 0


# synonymer.se renderas av ett JS-ramverk (Qwik) men skickar ändå med färdig
# HTML i svaret, så en vanlig GET räcker -- till skillnad från svenska.se, som
# bara skickar ett tomt skal. Innehållet ligger i numrerade block med den här
# klassen; varje block är en avdelning på sidan.
# 2026-08-29: klassen matchades tidigare som "px-6 py-3 border-b". Sajten
# bytte markup och skriver numera "py-3 border-b border-border
# last:border-none" -- utan px-6. Monstret slutade traffa HELT, och
# funktionen returnerade `finns: false` for VARJE ord i stallet for att
# larma. Foljden: 910 av 4 735 kort (19 %) star utan synonym, inte for att
# orden saknar synonymer utan for att kallan tystnade.
#
# Prefixet ar darfor borttaget ur monstret och `px-6` behovs inte langre.
# Se ocksa `_syn_sanity()` nedan: en tyst nollstallning far inte upprepas.
_SYN_BLOCK = re.compile(
    r'<div class="[^"]*py-3 border-b[^"]*"[^>]*>(.*?)</div>', re.DOTALL)
_SYN_H2 = re.compile(r"<h2[^>]*>(.*?)</h2>", re.DOTALL)
_TAGGAR = re.compile(r"<[^>]+>")
_KOMMENTARER = re.compile(r"<!--.*?-->", re.DOTALL)


# Sidans reklam- och sidospaltsblock delar CSS-klass med synonymblocken, så
# "Vad betyder girigbuk?", "Läs mer om dagens uttryck" och "FörklaringSe
# inbillade faror" följde med in bland synonymerna till *estetik*. De går inte
# att skilja på uppmärkningen -- däremot på formen: en synonym är kort och är
# inte en fråga eller en uppmaning.
_WIDGET_INLEDNING = ("vad betyder", "läs mer", "förklaring", "se även",
                     "här hittar du", "dagens", "vill du föreslå")

# Sidfotslänken och avdelningsrubrikerna ligger i SAMMA block som orden och
# följde tidigare med in i listan som om de vore synonymer.
#
# Mätt 2026-08-11 på de tio kort blindgranskaren fällde på synonymerna:
# "tillbaka i grottekvarnen" stod i ALLA TIO, och för `hortonom` och `kväkare`
# var den det ENDA som extraherats. Parsern returnerade alltså ett svar som såg
# ifyllt ut fast den inte hittat en enda synonym -- samma felklass som registret
# hade före 2026-08-10: ett tomt fält och ett bedömt fält får inte se likadana ut.
_EJ_SYNONYM = ("tillbaka i grottekvarnen", "motsatsord", "användarnas bidrag",
               "synonymer", "synonymer till", "andra ord", "korsord",
               "föreslå synonym", "alla synonymer")


# Gransssnittstext som sajten blandar in bland orden. "Visa fler" ar en
# knapp, inte en synonym (2026-08-29).
_UI_TEXT = {"visa fler", "visa farre", "visa mindre", "subst.", "äv.", "verb",
            "adj.", "adv.", "vard.", "bildl.", "ngt högt.", "högt.", "åld.",
            "ngt åld."}
# Sektionsrubriker och exempelinledningar som sajten renderar mellan orden.
# Till skillnad fran _UI_TEXT ar de INLEDNINGAR, inte hela strangen -- t.ex.
# "Uttryck som innehaller lappkast" eller "Betydelse: gora en helomvandning".
# Hittade 2026-08-29 pa lappkast, utarmad och "i tid och otid".
_UI_INLEDNING = ("uttryck som innehåller", "uttryck med betydelsen",
                 "betydelse:", "exempel:", "läs mer", "vad betyder",
                 "förklaring:", "göra ett", "göra en", "hur används",
                 "liknande ord", "nästkommande ord", "rösta på")


def _ar_synonym(t):
    lag = t.lower().strip()
    if len(t) > 34 or "?" in t:
        return False
    # Taggavgränsaren delar även på parenteser och liknande, så "(", "av", ")"
    # dök upp som egna poster på `abstrahera`. En synonym innehåller bokstäver.
    if not re.search(r"[a-zåäöéA-ZÅÄÖÉ]", t):
        return False
    if lag in _EJ_SYNONYM or "grottekvarnen" in lag:
        return False
    return not any(lag.startswith(p) for p in _WIDGET_INLEDNING)


def hamta_synonymer(ord_):
    """synonymer.se. Returnerar (dict|None, status, byte).

    VARNING som följer med i utdata: sidan blandar redaktionellt material med
    'Användarnas bidrag'. Den andra sorten är crowdsourcad och håller inte
    ordbokskvalitet -- 'estetik' får t.ex. 'grafiskt snyggt'. Avdelningarna
    märks därför ut var för sig i stället för att slås ihop till en lista, så
    att det syns VILKEN sorts belägg en synonym har. synonymer.se ska läsas,
    inte kopieras (Adams regel).

    Den tidigare versionen av den här funktionen plockade alla /sv-syn/-länkar
    på sidan och fick därför med den alfabetiska grannlistan i sidfoten:
    'reservat' gav 'reservant', 'reservare', 'reservationsfri'. Det är inte
    synonymer, det är närliggande uppslagsord."""
    # synonymer.se skriver flerordsuppslag med BINDESTRECK: /sv-syn/bekväma-sig,
    # inte /sv-syn/bekv%C3%A4ma%20sig. Med mellanslag svarar sajten 200 men utan
    # innehåll, vilket tolkades som "uttrycket finns inte" -- och därför saknade
    # varje idiom (bära sig, bekväma sig, av hävd) sin andra källa. Hittat
    # 2026-08-10 genom en allmän webbsökning, alltså precis den reservväg Adam
    # bad om samma dag. Mellanslagsformen provas ändå först, eftersom den
    # fungerar för enstaka ord och för uppslag som verkligen har mellanslag.
    former = [urllib.parse.quote(ord_)]
    if " " in ord_:
        former.insert(0, urllib.parse.quote(ord_.replace(" ", "-")))
    html = None
    for form in former:
        html, status, byte = _hamta_ratt(SYN_URL.format(form))
        if html and "hittade tyvärr" not in html and _SYN_BLOCK.search(html):
            break
    if html is None:
        return None, status, byte
    avdelningar = {}
    for block in _SYN_BLOCK.findall(html):
        # HELA widgetblocket kastas, inte bara dess enskilda ord.
        #
        # Sidospalterna delar CSS-klass med synonymblocken. `_WIDGET_INLEDNING`
        # fanns redan, men tillämpades PER ORD: ett ord silades bort om det
        # började med "vad betyder", "förklaring" osv. Det höll så länge hela
        # widgeten blev EN lång sträng, som dessutom stoppades av
        # 34-teckensgränsen.
        #
        # När taggarna 2026-08-11 började ersättas med en avgränsare (för att
        # sluta foga ihop grannord till påhittade ord som "blandaspäcka")
        # sprack widgeten i stället i korta fragment -- "kvarn", "guld",
        # "Frode", "Väldigt berusad" -- och inget av dem BÖRJAR med en
        # widgetfras. De gick alltså rakt igenom. `hortonom` fick elva falska
        # synonymer och räknades felaktigt som täckt av tre källor.
        #
        # Mätt på hortonom: sajten levererar fyra block, och INGET av dem är
        # redaktionella synonymer -- ett användarbidrag och tre sidospalter
        # ("Vad betyder grottekvarn?", "Förklaring: Väldigt berusad", "Läs mer
        # om dagens uttryck"). Rätt svar för det ordet är alltså noll synonymer.
        #
        # Testet hör därför hemma på BLOCKET, inte på orden i det: ett block är
        # antingen synonymer eller inte.
        blocktext = " ".join(_TAGGAR.sub(" ", block).split()).lower()
        if any(blocktext.startswith(p) for p in _WIDGET_INLEDNING):
            continue
        # 2026-08-29: rubriken far bara tros pa om h2:n star FORE ordlistan.
        # synonymer.se lagger nasta sektions rubrik (t.ex. "motsatsord")
        # inuti det foregaende blocket, sa en h2 som star EFTER <ol> hor till
        # nasta avsnitt -- inte till orden ovanfor. Utan kontrollen etiketteras
        # despots synonymer (forfattare, diktator, tyrann...) som MOTSATSORD,
        # och en massifyllning skulle stoppa in motsatser i synonymfaltet.
        h2 = _SYN_H2.search(block)
        listpos = block.find("<ol")
        if listpos == -1:
            listpos = block.find('<a href="/sv-syn/')
        if h2 and listpos != -1 and h2.start() > listpos:
            h2 = None
        rubrik = _TAGGAR.sub("", h2.group(1)).strip() if h2 else "synonymer"
        kropp = _SYN_H2.sub("", block)
        # Taggarna byts mot en AVGRÄNSARE, inte mot ingenting. Varje synonym
        # ligger i sitt eget <a>-element utan mellanrum i källan, så en tom
        # ersättning fogade ihop grannar till ord som inte finns: `bemänga`
        # fick "blandaspäcka" (blanda + späcka) och `pryd` fick
        # "viktorianskmotsatsordlättsinnig" (viktoriansk + rubriken + lättsinnig).
        # Det är värre än att tappa en synonym -- kortet får ett PÅHITTAT ord
        # som ser ut att komma från en källa. Hittat 2026-08-11.
        text = _TAGGAR.sub("|", _KOMMENTARER.sub("", kropp))
        # Semikolon skiljer betydelsegrupper på synonymer.se. Utan det i
        # mönstret blev "detektiv; ombud" en enda post, som varken matchade
        # "detektiv" eller "ombud" vid jämförelse.
        ord_lista = [t.strip() for t in re.split(r"[,|;]", text) if t.strip()]
        ord_lista = [t for t in ord_lista
                     if t.lower() != ord_.lower() and _ar_synonym(t)
                     and t.lower() not in _UI_TEXT
                     and not t.lower().startswith(_UI_INLEDNING)]
        if ord_lista:
            avdelningar.setdefault(rubrik, []).extend(ord_lista[:20])
    saknas = "hittade tyvärr" in html or "inga synonymer" in html
    return ({"finns": bool(avdelningar) and not saknas,
             "avdelningar": avdelningar}, status, byte)


_WIKT_RUBRIK = re.compile(r"^=+\s*(.+?)\s*=+\s*$", re.MULTILINE)
_WIKT_MALL = re.compile(r"\{\{[^{}]*\}\}")
_WIKT_LANK = re.compile(r"\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]")


def _wikitext_rent(s):
    for _ in range(3):  # nästlade mallar kräver flera varv
        s = _WIKT_MALL.sub(" ", s)
    s = _WIKT_LANK.sub(r"\1", s).replace("'''", "").replace("''", "")
    return " ".join(s.split())


def hamta_wiktionary(ord_):
    """sv.wiktionary.org via `action=parse&prop=wikitext`.

    Först användes `prop=extracts&explaintext`, men det gav bara ~260 byte per
    ord -- alltså intron, inte avsnitten -- och 'Etymologi' gick därför aldrig
    att hitta. Wikitexten har rubrikerna kvar och går att dela på.

    Realistisk förväntan, mätt 2026-08-10: svenska Wiktionary är TUNN. 'estetik'
    och 'reservat' har definition, besläktade ord och översättningar men INGEN
    etymologi. Etymologin kommer i praktiken från SO:s `historiskaUppgifter`.
    Wiktionary är ändå en riktig tredje källa -- den bekräftar eller motsäger
    betydelsen oberoende av Akademien."""
    rå, status, byte = _hamta_ratt(
        "https://sv.wiktionary.org/w/api.php?action=parse&prop=wikitext"
        "&redirects=1&format=json&page=" + urllib.parse.quote(ord_))
    if rå is None:
        return None, status, byte
    try:
        w = json.loads(rå).get("parse", {}).get("wikitext", {}).get("*", "")
    except ValueError:
        return None, status, byte
    if not w.strip():
        return {"finns": False, "etymologi": None, "avsnitt": {}}, status, byte
    delar = {}
    rubriker = list(_WIKT_RUBRIK.finditer(w))
    for i, m in enumerate(rubriker):
        slut = rubriker[i + 1].start() if i + 1 < len(rubriker) else len(w)
        delar[m.group(1).strip().lower()] = w[m.end():slut]
    ety = None
    for nyckel in ("etymologi", "ursprung", "härledning"):
        if delar.get(nyckel):
            ety = _wikitext_rent(delar[nyckel])[:400]
            break
    # Definitionsraderna ligger som "#..." under ordklassrubriken.
    definitioner = [_wikitext_rent(r[1:]) for r in w.splitlines()
                    if r.startswith("#") and not r.startswith("#:")]
    return ({"finns": True, "etymologi": ety,
             "definitioner": [d for d in definitioner if d][:6],
             "avsnitt": {k: _wikitext_rent(v)[:300] for k, v in delar.items()
                         if k in ("etymologi", "synonymer", "besläktade ord",
                                  "antonymer")}},
            status, byte)


def _text(x):
    """Plockar ut ren text ur SO:s/SAOL:s HTML-fragment."""
    if x is None:
        return ""
    if isinstance(x, list):
        return " ; ".join(_text(i) for i in x if i)
    if isinstance(x, dict):
        return _text(x.get("value") or x.get("text") or "")
    return re.sub(r"\s{2,}", " ", re.sub(r"<[^>]+>", "", str(x))).strip()


def _plocka(kalla, nycklar):
    ut = []
    def gå(n):
        if isinstance(n, dict):
            for k, v in n.items():
                if k in nycklar:
                    t = _text(v)
                    if t:
                        ut.append(t)
                gå(v)
        elif isinstance(n, list):
            for v in n:
                gå(v)
    gå(kalla)
    return ut


def _har_riktig_traff(data, ord_):
    """Sant bara om nagon traff FAKTISKT galler uppslagsordet.

    Fritextsokningen ar generos: 'degression' ger 'deg', 'flau' ger 'flad'.
    Utan den har kontrollen hade fallbacken gjort saken varre an den strikta
    sokningen -- den hade hittat grannord och rapporterat dem som belagg."""
    mal = ord_.lower().replace(" ", "")
    for bok in INDEX:
        for t in (((data.get(bok) or {}).get("hits") or {}).get("hits") or []):
            s = t.get("_source", {})
            for nyckel in ("ortografi", "lemma", "grundform", "uppslagsord"):
                v = _text(s.get(nyckel)).lower().replace(" ", "")
                # bade exakt och bojd form godtas: loafer -> loafers
                if v and (v == mal or v.startswith(mal) or mal.startswith(v)):
                    return True
    return False


def sammanfatta(data):
    """Kompakt sammandrag — det agenten behöver läsa, inte hela svaret."""
    # SAOB var med i HÄMTNINGEN men inte i sammanfattningen -- alltså hämtades
    # den, betalades för, och kastades bort. Det gjorde att `flau` och
    # `degression` rapporterades som "finns inte i någon ordbok" trots att SAOB
    # har båda. Adam ifrågasatte just de orden 2026-08-10 och hade rätt.
    #
    # SAOB läses fortfarande som DJUP, inte som facit för dagens betydelser
    # (den är från tidigt 1900-tal) -- men "ordet finns inte" och "ordet finns
    # bara i den gamla ordboken" är två helt olika besked om ett kort.
    s = {}
    for bok in ("saol", "so", "saob"):
        träffar = (((data or {}).get(bok) or {}).get("hits") or {}).get("hits") or []
        if not träffar:
            s[bok] = None
            continue
        källa = [t.get("_source", {}) for t in träffar[:2]]
        s[bok] = {
            "def": _plocka(källa, {"definition", "def", "huvudbetydelse", "betydelse",
                                   "explanation", "grundbetydelse"})[:6],
            "exempel": _plocka(källa, {"exempel", "example", "idiom", "syntex"})[:4],
            "jfr": _plocka(källa, {"jfr", "se", "hänvisning", "synonym"})[:6],
            # SO:s stilmarkering ligger i `bruklighetskommentar` -- "något
            # ålderdomligt", "vardagligt", "nedsättande". Nyckeln stod tidigare
            # som `bruklighet`, och _plocka matchar EXAKT nyckelnamn, så fältet
            # plockades aldrig ut. Det skrevs inte heller ut i --kompakt.
            # Följden, upptäckt 2026-08-10 när blindgranskaren fällde *lappri*:
            # registret på korten sattes utifrån ett sammandrag som saknade
            # precis den uppgift som avgör registret, och patchtexterna kom att
            # påstå "SO markerar ingenting" om ord där SO markerar något.
            # Det är sannolikt en huvudorsak till att 49 % av decket står som
            # `formell` -- ett värde ingen kunde kontrollera.
            "märkning": _plocka(källa, {"bruklighetskommentar", "stilmarkering",
                                        "bruklighet", "markering", "stil",
                                        "anvandning", "stilkommentar"})[:4],
            # SO:s etymologi ligger i `historiskaUppgifter.etymologi`, inte i
            # ett fält som heter "historik" -- det första försöket sökte på fel
            # namn och gav tomt på varje ord, vilket såg ut som att SO saknade
            # etymologi. Det gör den inte: 'estetik' ger "ur grekiska
            # ai´sthesis 'förnimmelse; uppfattning'; jfr ursprung till
            # anestesi". Det är BÄTTRE etymologi än svenska Wiktionary har.
            "etymologi": _plocka(källa, {"etymologi"})[:3],
            "första_belägg": _plocka(källa, {"förstaBeläggOchKälla"})[:2],
            # Underbetydelser är SO:s "äv. om ..."-utvidgningar. De är ofta
            # precis den andra betydelsen som saknats på korten.
            "underbetydelser": _plocka(källa, {"typ"})[:6],
        }
    return s


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ord", nargs="*")
    p.add_argument("--fil", help="JSON-lista eller {relearn:[],ovriga:[]}")
    # default=None, inte 20. "Inget angivet" betyder HELA listan; bara det
    # losa ord-argumentet pa kommandoraden behaller den gamla taklosningen.
    # Den gamla defaulten slog av TYST mitt i en fil: 23 ord in, 20 uppslagna,
    # tre utan ett ord i utdatan (2026-08-11). Samma fel igen 2026-09-04 --
    # 150 ord in, 20 uppslagna, 130 tappade. En grans som inte syns i utdatan
    # ar samma sak som ingen grans alls, sa den skrivs nu ut nar den satts.
    p.add_argument("--antal", type=int, default=None)
    p.add_argument("--hoppa", type=int, default=0)
    p.add_argument("--kompakt", action="store_true",
                   help="kort textsammandrag i stället för full JSON")
    # `--tyst` finns för att göra ETT bestämt misstag omöjligt att upprepa.
    # Sammandraget är stort, så det är frestande att filtera utdata genom sed
    # eller head för att spara kontext -- och då försvinner bevisraderna på
    # vägen. Det hände 2026-08-09 (sex kort vägrades) och igen 2026-08-10 (elva
    # kort vägrades), båda gångerna av samma orsak. Spärren hade rätt varje
    # gång: bevis som inte syns i transkriptet är inget bevis.
    #
    # Rätt sätt att spara kontext är alltså att låta SKRIPTET tiga om
    # innehållet, aldrig att filtrera bort dess utdata i efterhand. Med --tyst
    # skrivs bevisraderna och trekällskontrollen, ingenting annat; innehållet
    # ligger kvar i uppslag/<ord>.json.
    p.add_argument("--tyst", action="store_true",
                   help="skriv BARA bevisrader och trekällskontroll")
    a = p.parse_args()

    ord_ = list(a.ord)
    if a.fil:
        d = json.load(open(a.fil, encoding="utf-8"))
        if isinstance(d, dict):
            d = d.get("relearn", []) + d.get("ovriga", [])
        # Sessionsfilerna från kortbyggare.py är listor av POSTER, inte av
        # ord. Utan den här normaliseringen gick v3:s egen sessionsfil inte
        # att mata in i v3:s eget uppslagningssteg -- felet kom först nere i
        # urllib som "quote_from_bytes() expected bytes", alltså långt från
        # orsaken och omöjligt att koppla till filformatet.
        d = [p.get("ord") if isinstance(p, dict) else p for p in d]
        if any(not isinstance(o, str) or not o for o in d):
            sys.exit(f"{a.fil}: posterna måste vara strängar eller objekt med 'ord'.")
        ord_ += d
    _fore = len(ord_)
    _antal = a.antal if a.antal is not None else (len(ord_) if a.fil else 20)
    ord_ = ord_[a.hoppa:a.hoppa + _antal]
    # Skriv ALLTID ut nar listan kapas. Tyst kapning ar felet ovan.
    if a.hoppa or len(ord_) < _fore:
        print(f"URVAL {len(ord_)} av {_fore} ord "
              f"(hoppa={a.hoppa}, antal={_antal}) -- "
              f"{_fore - a.hoppa - len(ord_)} kvar efter denna körning")
    if not ord_:
        sys.exit("inga ord")

    os.makedirs(UTKAT, exist_ok=True)
    sammandrag, ofullstandiga = {}, {}
    for o in ord_:
        post, kallor_med_innehall = {}, []

        data, status, byte = hamta(o)
        # Gav den exakta sokningen ingenting alls? Prova fritext en gang.
        # Traffarna maste kontrolleras mot uppslagsordet efterat -- fritext
        # returnerar grannord ('deg' for degression) som inte ar traffar.
        if data is not None and not any(
                ((data.get(b) or {}).get("hits") or {}).get("hits")
                for b in INDEX):
            fri, f_status, f_byte = hamta(o, exakt=False)
            if fri is not None and _har_riktig_traff(fri, o):
                data, status, byte = fri, f_status, f_byte
        # ---- BEVISRADERNA. Skrivs av processen, inte av agenten. ----
        print(f"SVENSKA_SE_HAMTAD {o} HTTP {status} {byte}")
        if data is None:
            post["svenska_se"] = {"FEL": f"HTTP {status}"}
        else:
            post["svenska_se"] = sammanfatta(data)
            # SAOB raknas med. Den avgor inte dagens betydelser -- men "finns
            # bara i SAOB" ar ett annat besked an "finns inte alls", och det
            # var just den skillnaden som gick forlorad pa `flau` och
            # `degression` fram till 2026-08-10.
            if any(post["svenska_se"].get(b) for b in ("saol", "so", "saob")):
                kallor_med_innehall.append("svenska.se")

        syn, s_status, s_byte = hamta_synonymer(o)
        print(f"SYNONYMER_SE_HAMTAD {o} HTTP {s_status} {s_byte}")
        post["synonymer_se"] = syn if syn is not None else {"FEL": f"HTTP {s_status}"}
        # `finns` räcker inte -- se synonymer_se_redaktionell() för varför.
        # Ett ord som bara har användarbidrag räknas som EJ täckt av källan,
        # inte som täckt av en svag källa: mellanlägen blir i praktiken
        # behandlade som täckning.
        syn_redaktionell = synonymer_se_redaktionell(syn)
        if syn_redaktionell:
            kallor_med_innehall.append("synonymer.se")
        elif syn and syn.get("finns"):
            print(f"SYNONYMER_SE_ENDAST_ANVANDARBIDRAG {o}")

        wik, w_status, w_byte = hamta_wiktionary(o)
        print(f"WIKTIONARY_HAMTAD {o} HTTP {w_status} {w_byte}")
        post["wiktionary"] = wik if wik is not None else {"FEL": f"HTTP {w_status}"}
        if wik and wik.get("finns"):
            kallor_med_innehall.append("wiktionary")

        # Hela svaren sparas, inte bara sammandraget, så att en senare
        # granskare kan läsa exakt vad källan sa i stället för min tolkning.
        # Uppslagsordskontrollen körs INNAN källan räknas. En fritextträff på
        # granngrannartiklar är inte en uppslagning av ordet -- se
        # uppslagsordstraffar() för hela resonemanget.
        ordbokstraffar = uppslagsordstraffar(data, o)
        via_form = None
        if not ordbokstraffar and " " not in o:
            # Kortets form är kanske inte ordbokens uppslagsform (loafer ->
            # loafers). Prova ett fåtal varianter INNAN ordet döms som osökbart.
            for v in variantformer(o):
                vdata, vstatus, _b = hamta(v)
                if vdata is None:
                    continue
                vtraffar = uppslagsordstraffar(vdata, v)
                if vtraffar:
                    ordbokstraffar, via_form, data = vtraffar, v, vdata
                    print(f"UPPSLAGSORD {o} hittad som uppslagsform '{v}'")
                    break
        print(f"UPPSLAGSORD {o} traffar={','.join(ordbokstraffar) or 'INGEN'}"
              + (f" via={via_form}" if via_form else ""))
        if not ordbokstraffar and "svenska.se" in kallor_med_innehall:
            kallor_med_innehall.remove("svenska.se")
            post["svenska_se"] = {
                "FEL": "INGEN UPPSLAGSORDSTRAFF -- svaret gallde andra ord",
                "returnerade_uppslagsord": sorted({
                    (h.get("_source") or {}).get(falt)
                    for kalla, falt in HUVUDORDSFALT.items()
                    for h in ((((data or {}).get(kalla) or {}).get("hits") or {}).get("hits") or [])
                    if (h.get("_source") or {}).get(falt)})[:8],
            }

        sh = hashlib.sha256(json.dumps(post, sort_keys=True, default=str)
                            .encode()).hexdigest()[:12]
        json.dump({"ord": o, "sha": sh,
                   "urler": {"svenska.se": f"{API}?ord={o}",
                             "synonymer.se": SYN_URL.format(o),
                             "wiktionary": WIKT_URL.format(o)},
                   "kallor_med_innehall": kallor_med_innehall,
                   "uppslagsordstraffar": ordbokstraffar,
                   "uppslagsform": via_form or o,
                   "synonymer_se_redaktionell": syn_redaktionell,
                   # Godtagbar sökkoll enligt Adams regel 2026-08-11: ordboks-
                   # träff ELLER redaktionell synonymer.se. Skrivs ut som ett
                   # eget fält så att en senare granskare kan se VILKEN grund
                   # kortet vilar på, inte bara att det passerade.
                   "verifieringsgrund": (
                       "ordbok" if ordbokstraffar
                       else "synonymer.se (redaktionell)" if syn_redaktionell
                       else "SAKNAS — kräver websökning"),
                   "svenska_se_ratt": data, "sammandrag": post},
                  open(os.path.join(UTKAT, f"{_sakert_filnamn(o)}.json"), "w", encoding="utf-8"),
                  ensure_ascii=False)

        post["_kallor"] = kallor_med_innehall
        sammandrag[o] = post
        if len(kallor_med_innehall) < 3:
            # SKILJ på "källan saknar ordet" och "hämtningen misslyckades".
            # Det första är ett besked om ordet och ska rödflagga kortet; det
            # andra säger ingenting om ordet alls och ska göras om. Slås de
            # ihop hamnar vanliga ord i bristlistan bara för att servern var
            # trög, och listan blir värdelös som arbetsunderlag.
            fel = [k for k, v in (("svenska.se", post["svenska_se"]),
                                  ("synonymer.se", post["synonymer_se"]),
                                  ("wiktionary", post["wiktionary"]))
                   if isinstance(v, dict) and "FEL" in v]
            ofullstandiga[o] = {"har": kallor_med_innehall,
                                "hamtning_misslyckades": fel}
        time.sleep(0.4)

    # ---- OMKÖRNINGSSVEP (2026-08-11) ----
    # `_hamta_ratt` backar redan av 429 fyra gånger (3+6+9 s). Det räcker inte
    # när 70 anrop går i rad: 2026-08-11 brände 10 av 70 ord alla sina försök
    # mot Wiktionary, och en manuell omkörning gav sedan 7 riktiga artiklar.
    #
    # Luckan var alltså inte att omförsök saknades utan att ett ord som brände
    # sina försök ALDRIG BESÖKTES IGEN -- det landade i tre_kallor_saknas.json
    # och såg där ut precis som ett ord källan faktiskt saknar. Svepet körs när
    # bursten lagt sig, alltså när chansen att lyckas är som störst.
    #
    # Bara RETUR-BARA fel görs om. Ett ord källan verkligen saknar ska inte
    # köras om i evighet: det är ett besked om ordet, inte ett serverfel.
    omkorning = {o: v for o, v in ofullstandiga.items() if v["hamtning_misslyckades"]}
    if omkorning:
        print(f"---OMKORNING--- {len(omkorning)} ord med misslyckad hamtning, "
              f"vantar 20 s")
        time.sleep(20)
        for o, v in list(omkorning.items()):
            if "wiktionary" not in v["hamtning_misslyckades"]:
                continue
            wik, w_status, w_byte = hamta_wiktionary(o)
            print(f"WIKTIONARY_OMKORD {o} HTTP {w_status} {w_byte}")
            if not (wik and wik.get("finns")):
                continue
            sokvag = os.path.join(UTKAT, f"{_sakert_filnamn(o)}.json")
            try:
                sparad = json.load(open(sokvag, encoding="utf-8"))
            except Exception:
                continue
            sparad["sammandrag"]["wiktionary"] = wik
            if "wiktionary" not in sparad["kallor_med_innehall"]:
                sparad["kallor_med_innehall"].append("wiktionary")
            json.dump(sparad, open(sokvag, "w", encoding="utf-8"), ensure_ascii=False)
            kvar = [k for k in v["hamtning_misslyckades"] if k != "wiktionary"]
            if len(sparad["kallor_med_innehall"]) >= 3:
                ofullstandiga.pop(o, None)
            else:
                ofullstandiga[o] = {"har": sparad["kallor_med_innehall"],
                                    "hamtning_misslyckades": kvar}
            time.sleep(1.5)

    print("---SAMMANDRAG---")
    if a.tyst:
        print(f"(tyst läge — {len(ord_)} ord, innehållet ligger i {UTKAT}/)")
    elif a.kompakt:
        # Bara det som faktiskt behövs för att skriva ett kort. Fullständiga
        # svar finns kvar i uppslag/<ord>.json och går att läsa när ett
        # enskilt ord behöver granskas närmare.
        #
        # OBS: bevisraderna ovan skrivs ALLTID i sin helhet, även här. Att
        # filtrera skriptets utdata genom något som råkade äta dem hände
        # 2026-08-09 och fick spärren att (helt riktigt) vägra sex kort:
        # bevis som inte syns är inget bevis.
        for o, p in sammandrag.items():
            sv_ = p.get("svenska_se") or {}
            so = sv_.get("so") or {}
            saol = sv_.get("saol") or {}
            syn = (p.get("synonymer_se") or {}).get("avdelningar") or {}
            wik = p.get("wiktionary") or {}
            print(f"\n### {o}   [{', '.join(p.get('_kallor', [])) or 'INGEN KÄLLA'}]")
            if so.get("def"):
                print("  SO   :", " | ".join(so["def"]))
            if so.get("underbetydelser"):
                print("  SO+  :", " | ".join(so["underbetydelser"]))
            if saol.get("def"):
                print("  SAOL :", " | ".join(saol["def"]))
            # BRUK skrivs ut DIREKT efter definitionerna och före allt annat,
            # eftersom det är fältet som avgör registret. Låg det längre ner
            # skulle det drunkna i synonymlistorna.
            bruk = (so.get("märkning") or []) + (saol.get("märkning") or [])
            if bruk:
                print("  BRUK :", " | ".join(dict.fromkeys(bruk)))
            if so.get("exempel"):
                print("  EX   :", " | ".join(so["exempel"][:3]))
            if so.get("jfr"):
                print("  JFR  :", ", ".join(so["jfr"]))
            if so.get("etymologi"):
                print("  ETYM :", " | ".join(so["etymologi"]))
            elif wik.get("etymologi"):
                print("  ETYM*:", wik["etymologi"][:200], "(Wiktionary)")
            if so.get("första_belägg"):
                print("  BELÄGG:", " | ".join(so["första_belägg"]))
            for rubrik, lista in syn.items():
                print(f"  SYN({rubrik}):", ", ".join(lista[:12]))
            if wik.get("definitioner"):
                print("  WIKT :", " | ".join(wik["definitioner"][:3]))
    else:
        print(json.dumps(sammandrag, ensure_ascii=False, indent=1))

    # ---- TREKÄLLSKONTROLLEN (Adams krav 2026-08-10) ----
    # Orden nedan saknar minst en av de tre källorna. De ska rödflaggas och
    # gås igenom separat, inte skrivas som om de vore fullbelagda. Listan
    # skrivs till fil också, eftersom en utskrift försvinner med sessionen.
    print("---TREKALLSKONTROLL---")
    print(json.dumps({"ofullstandiga": ofullstandiga,
                      "antal_fullstandiga": len(ord_) - len(ofullstandiga),
                      "antal_ord": len(ord_)}, ensure_ascii=False, indent=1))
    bef = {}
    if os.path.exists(BRISTLISTA):
        bef = json.load(open(BRISTLISTA, encoding="utf-8"))
    # Listan måste kunna STÄDA SIG SJÄLV. Nio ord (oknytt, damast, presumera,
    # oktett, sondera, medaljong, trolsk, anblick, märla) hamnade i den när
    # Wiktionary strypte anropen, och hade alla tre källorna vid omhämtning.
    # Utan den här raden hade de legat kvar för alltid och fått nio helt
    # normala kort rödflaggade. En bristlista som bara växer är en lista över
    # historiska nätverksfel, inte över kort som behöver arbete.
    lakta = [o for o in ord_ if o in bef and o not in ofullstandiga]
    for o in lakta:
        del bef[o]
    bef.update({o: {**k, "sedd": time.strftime("%Y-%m-%d")}
                for o, k in ofullstandiga.items()})
    json.dump(bef, open(BRISTLISTA, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    if lakta:
        print(f"tog bort {len(lakta)} ord ur {BRISTLISTA} (har nu tre källor): "
              f"{', '.join(lakta)}")
    if ofullstandiga:
        print(f"skrev {len(ofullstandiga)} ord till {BRISTLISTA} "
              f"(totalt {len(bef)})")


if __name__ == "__main__":
    main()
