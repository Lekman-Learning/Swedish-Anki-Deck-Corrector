"""Hämtar en kandidatbild från Wikipedia/Wikimedia Commons för ett ord som
saknar bild. Adams beslut 2026-08-19: kort utan bild ska kunna få en om en
relevant sådan finns på svenska Wikipedia (i första hand) eller Commons
(fallback) -- men BARA för ord där en bild faktiskt hjälper minnet: konkreta
substantiv (djur, växter, föremål, historiska artefakter, platser). Abstrakta
ord, verb och idiom saknar oftast en bra Wikipedia-bild -- det är ett
FÖRVÄNTAT normalfall att `hamta_kandidat()` returnerar None för dem, inte ett
fel.

VIKTIGT -- vad den här modulen INTE gör: den avgör inte om kandidaten
faktiskt matchar ordets relevanta betydelse. Den hämtar bara vad som finns
(titel, sammanfattningstext, bild-URL) så att granskaren (Claude, med
uttryckligt mandat från Adam 2026-08-19) kan jämföra `extract`/`beskrivning`
mot kortets Huvudbetydelse innan bilden används. En tvetydig artikel
(`disambiguation`) räknas ALDRIG som en träff -- funktionen faller vidare
till Commons-sökning istället för att gissa vilken betydelse som avsågs.

Samma urllib-mönster som slaupp.py (`_hamta_ratt`): beskrivande User-Agent
(Wikimedia stryper annars anrop till 429, se slaupp.py-kommentaren om
Wiktionary från 2026-08-10), backoff på 429/503, kastar aldrig -- fel
rapporteras som None/tom lista, aldrig som en krasch mitt i en batch.
"""

import base64
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request

ANVANDARAGENT = ("anki-ord/1.0 (svenskt ordkortsprojekt, bildhämtning; "
                  "kontakt via github.com/Lekman-Learning) python-urllib")

SV_SUMMARY_API = "https://sv.wikipedia.org/api/rest_v1/page/summary/{}"
COMMONS_API = "https://commons.wikimedia.org/w/api.php"

_BILD_EXT_OK = (".jpg", ".jpeg", ".png", ".gif", ".webp")


def _hamta_json(url, forsok=3):
    """Rå GET, tolkad som JSON. Returnerar (data, status). Kastar aldrig.

    404 särskiljs uttryckligen (ordet/artikeln finns inte -- normalt, inte
    ett fel). 429/503 backas av och görs om, samma logik som slaupp.py."""
    hdr = {"User-Agent": ANVANDARAGENT, "Accept": "application/json"}
    for n in range(forsok):
        try:
            with urllib.request.urlopen(
                    urllib.request.Request(url, headers=hdr), timeout=20) as r:
                return json.loads(r.read().decode("utf-8", "replace")), r.status
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None, 404
            if e.code in (429, 503) and n < forsok - 1:
                time.sleep(2.0 * (n + 1))
                continue
            return None, e.code
        except Exception:
            if n == forsok - 1:
                return None, 0
            time.sleep(1.0)
    return None, 0


def sok_wikipedia_summary(ord_):
    """Frågar sv.wikipedia REST-API:t (page/summary) efter ett ord.
    Returnerar None om artikeln inte finns. Annars en dict:
      disambiguation: bool -- True = flera betydelser, ANVÄND ALDRIG bilden
      titel, beskrivning, extract, bild_url (kan vara None), sidurl
    """
    if not ord_ or not ord_.strip():
        return None
    slug = urllib.parse.quote(ord_.strip().replace(" ", "_"), safe="")
    data, status = _hamta_json(SV_SUMMARY_API.format(slug))
    if not data or status != 200:
        return None
    if data.get("type") == "disambiguation":
        return {"disambiguation": True, "titel": data.get("title"),
                "beskrivning": None, "extract": None, "bild_url": None,
                "sidurl": (data.get("content_urls") or {}).get("desktop", {}).get("page")}
    bild = data.get("originalimage") or data.get("thumbnail")
    return {
        "disambiguation": False,
        "titel": data.get("title"),
        "beskrivning": data.get("description"),
        "extract": data.get("extract"),
        "bild_url": bild.get("source") if bild else None,
        "sidurl": (data.get("content_urls") or {}).get("desktop", {}).get("page"),
    }


def sok_commons(ord_, limit=5):
    """Fallback: fritextsökning på Wikimedia Commons efter bildfiler.
    Används när svenska Wikipedia saknar artikel eller bild för ordet.
    Returnerar en lista kandidater (Commons egen relevanssortering, ingen
    egen ranking görs här) -- eller tom lista."""
    if not ord_ or not ord_.strip():
        return []
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": f"filetype:bitmap {ord_.strip()}", "gsrnamespace": "6",
        "gsrlimit": str(limit), "prop": "imageinfo",
        "iiprop": "url|extmetadata", "iiurlwidth": "500",
    }
    url = COMMONS_API + "?" + urllib.parse.urlencode(params)
    data, status = _hamta_json(url)
    if not data or status != 200:
        return []
    pages = ((data.get("query") or {}).get("pages")) or {}
    kandidater = []
    for p in pages.values():
        infolista = p.get("imageinfo") or [{}]
        info = infolista[0]
        meta = info.get("extmetadata") or {}
        kandidater.append({
            "titel": (p.get("title") or "").replace("File:", "").replace("Fil:", ""),
            "bild_url": info.get("thumburl") or info.get("url"),
            "sidurl": info.get("descriptionurl"),
            "licens": (meta.get("LicenseShortName") or {}).get("value"),
            "konstnar": _strip_html(((meta.get("Artist") or {}).get("value"))),
        })
    return kandidater


def _strip_html(s):
    if not s:
        return None
    return re.sub(r"<[^>]+>", "", s).strip() or None


def hamta_kandidat(ord_):
    """Huvudfunktion. Försöker sv.wikipedia först, faller tillbaka till en
    Commons-bildsökning om Wikipedia saknar artikel/bild eller är tvetydig.

    Returnerar None om inget alls hittades -- FÖRVÄNTAT för de flesta
    abstrakta ord/verb/idiom, inget att larma om. Returnerar annars en dict:
      kalla_typ: "wikipedia" | "commons"
      titel, beskrivning, extract (kan vara None för Commons-träffar),
      bild_url, sidurl, licens (bara satt för Commons)

    Ingen relevansbedömning görs här -- se modulens docstring. Anroparen
    (granskaren) MÅSTE jämföra beskrivning/extract mot kortets
    Huvudbetydelse innan bilden används."""
    wp = sok_wikipedia_summary(ord_)
    if wp and not wp["disambiguation"] and wp.get("bild_url"):
        return {
            "kalla_typ": "wikipedia",
            "titel": wp["titel"],
            "beskrivning": wp.get("beskrivning"),
            "extract": wp.get("extract"),
            "bild_url": wp["bild_url"],
            "sidurl": wp["sidurl"],
            "licens": None,
        }
    kandidater = sok_commons(ord_, limit=3)
    if kandidater and kandidater[0].get("bild_url"):
        topp = kandidater[0]
        return {
            "kalla_typ": "commons",
            "titel": topp["titel"],
            "beskrivning": topp.get("konstnar"),
            "extract": None,
            "bild_url": topp["bild_url"],
            "sidurl": topp["sidurl"],
            "licens": topp.get("licens"),
        }
    return None


def hamta_bilddata_base64(bild_url, forsok=4):
    """Laddar ner bildens rådata och base64-kodar den, redo för
    images.store_new()/storeMediaFile. Backar av på 429/503 (upload.wikimedia.org
    strypte anrop under manuell granskning av pilotbatchen 2026-08-19 redan
    efter två nedladdningar i följd -- samma mönster som slaupp.py:s
    Wiktionary-anrop). Kastar efter uttömda försök -- anroparen ska fånga
    och hoppa över kortet, inte krascha hela batchen."""
    hdr = {"User-Agent": ANVANDARAGENT}
    for n in range(forsok):
        try:
            with urllib.request.urlopen(
                    urllib.request.Request(bild_url, headers=hdr), timeout=30) as r:
                raw = r.read()
                content_type = r.headers.get("Content-Type", "")
            return base64.b64encode(raw).decode("ascii"), content_type
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and n < forsok - 1:
                time.sleep(5.0 * (n + 1))
                continue
            raise


def filnamn_for(ord_, bild_url, content_type=""):
    """Bygger ett säkert Anki-mediafilnamn: wikipedia_<ord>.<ext>. Prefixet
    gör källan spårbar direkt i filnamnet, utan att öppna manifestet."""
    ext = os.path.splitext(urllib.parse.urlparse(bild_url).path)[1].lower()
    if ext not in _BILD_EXT_OK:
        if "png" in content_type:
            ext = ".png"
        elif "gif" in content_type:
            ext = ".gif"
        elif "webp" in content_type:
            ext = ".webp"
        else:
            ext = ".jpg"
    sakert = re.sub(r"[^a-z0-9åäö]+", "_", ord_.strip().lower()).strip("_")
    return f"wikipedia_{sakert}{ext}"
