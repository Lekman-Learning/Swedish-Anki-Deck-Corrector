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

# svenska.se (SO/SAOL) är JS-renderad: både /tre/?sok= och det äldre
# /tri/f_saol.php?sok= ger ett tomt skal med enbart navigering (verifierat
# 2026-08-09). Att tillåta värden hade gjort det möjligt att "belägga" ett ord
# med en tom sida. Använd saob.se i stället — samma akademi, djupare artiklar.
BLOCKERADE_VARDAR = (
    "svenska.se",
)

_URL_RE = re.compile(r"https?://[^\s\"'<>,;)\]]+")


def _transkriptkatalog():
    return os.path.join(os.path.expanduser("~"), ".claude", "projects")


def _tool_use_urler(nod, ut):
    """Plockar url-PARAMETERN ur WebFetch-anrop. Rekursivt, eftersom
    transkriptets struktur varierar mellan versioner."""
    if isinstance(nod, dict):
        if nod.get("type") == "tool_use" and nod.get("name") in ("WebFetch", "web_fetch"):
            url = (nod.get("input") or {}).get("url")
            if isinstance(url, str):
                ut.add(url)
        for v in nod.values():
            _tool_use_urler(v, ut)
    elif isinstance(nod, list):
        for v in nod:
            _tool_use_urler(v, ut)


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
    urler = set()
    monster = os.path.join(_transkriptkatalog(), "*", "*.jsonl")
    for sokvag in glob.glob(monster):
        try:
            with open(sokvag, encoding="utf-8", errors="ignore") as f:
                for rad in f:
                    if '"WebFetch"' not in rad and '"web_fetch"' not in rad:
                        continue
                    try:
                        _tool_use_urler(json.loads(rad), urler)
                    except ValueError:
                        continue
        except OSError:
            continue
    return urler


def _urler_ur_valvloggen(valvsokvag):
    """Reserv: raw-websearch/ i valvet. Används för äldre datum."""
    urler = set()
    if not valvsokvag:
        return urler
    for sokvag in glob.glob(os.path.join(valvsokvag, "raw-websearch", "*.md")):
        try:
            with open(sokvag, encoding="utf-8", errors="ignore") as f:
                for rad in f:
                    if rad.startswith("**URL:**"):
                        urler.update(_URL_RE.findall(rad))
        except OSError:
            continue
    return urler


def samla_bevis(valvsokvag=None):
    """Returnerar mängden URL:er som bevisligen hämtats."""
    return _urler_ur_transkript() | _urler_ur_valvloggen(valvsokvag)


def _normalisera(url):
    """Jämför utan schema, www och avslutande slash — samma sida ska matcha
    oavsett hur den skrevs in i kalla-fältet."""
    u = url.lower().split("#")[0].rstrip("/")
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

    urler = _URL_RE.findall(kalla)
    if not urler:
        return False, ("kalla saknar URL — fri text duger inte längre, "
                       "se sokkoll_verifiering.py")

    for url in urler:
        n = _normalisera(url)
        if any(v in n for v in BLOCKERADE_VARDAR):
            return False, (f"{url} är blockerad: JS-renderad sida som ger tomt "
                           "innehåll via WebFetch")
        if not any(v in n for v in GODKANDA_VARDAR):
            continue
        if any(_normalisera(b) == n for b in bevis):
            return True, url
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
