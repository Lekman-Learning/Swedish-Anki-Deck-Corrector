import json
import re
import time
import requests
from pathlib import Path
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

CACHE_FILE = Path("synonymer_cache.json")
_cache: dict | None = None


def _load_cache() -> dict:
    global _cache
    if _cache is None:
        if CACHE_FILE.exists():
            _cache = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        else:
            _cache = {}
    return _cache


def _save_cache():
    if _cache is not None:
        CACHE_FILE.write_text(json.dumps(_cache, ensure_ascii=False, indent=2), encoding="utf-8")


def fetch_synonymer(word: str) -> str:
    """Hämta synonymer från synonymer.se. Returnerar råtext (cachad)."""
    cache = _load_cache()
    key = word.lower().strip()
    if key in cache:
        return cache[key]

    # Hantera fraser — sök på hela frasen först, sedan första ordet
    words_to_try = [word]
    if " " in word:
        words_to_try.append(word.split()[0])

    result = ""
    for w in words_to_try:
        text = _fetch_one(w)
        if text:
            result = text
            break

    cache[key] = result
    if len(cache) % 25 == 0:
        _save_cache()
    return result


def flush_cache():
    """Spara cachen till disk."""
    _save_cache()


def _fetch_one(word: str) -> str:
    url = f"https://www.synonymer.se/sv-syn/{word.lower().replace(' ', '-')}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=8)
        if resp.status_code != 200:
            return ""

        soup = BeautifulSoup(resp.text, "html.parser")

        # Synonymer.se listar synonymer i <a>-taggar i huvud-content
        synonyms = []
        for a in soup.select("a[href*='/sv-syn/']"):
            text = a.get_text(strip=True)
            if text and len(text) > 1 and text.lower() != word.lower():
                synonyms.append(text)

        if not synonyms:
            # Fallback: ta all text från main/article
            main = soup.find("main") or soup.find("article") or soup.body
            if main:
                return main.get_text(separator=" ", strip=True)[:800]

        return ", ".join(synonyms[:20])
    except Exception:
        return ""
    finally:
        time.sleep(0.3)
