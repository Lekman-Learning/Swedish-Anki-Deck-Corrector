import json
import re
import time
from pathlib import Path

CACHE_FILE = Path("svenska_cache.json")

# Nav boilerplate to strip out
_NAV_LINES = {"hem", "om", "hjälp", "kontakt", "alla", "saol", "so", "saob", "söktips", "cookies", "integritetspolicy"}


def load_cache() -> dict:
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    return {}


def save_cache(cache: dict) -> None:
    CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


class SvenskaScraper:
    def __init__(self):
        self.cache = load_cache()
        self._dirty = 0
        self._pw = None
        self._browser = None
        self._page = None

    def start(self):
        from playwright.sync_api import sync_playwright
        self._pw = sync_playwright().start()
        self._browser = self._pw.chromium.launch(headless=True)
        context = self._browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        self._page = context.new_page()

    def stop(self):
        self.flush()
        if self._browser:
            self._browser.close()
        if self._pw:
            self._pw.stop()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

    def search(self, word: str) -> dict:
        key = word.lower().strip()

        if key in self.cache:
            return self.cache[key]

        result = self._fetch(key)
        self.cache[key] = result
        self._dirty += 1

        if self._dirty >= 25:
            save_cache(self.cache)
            self._dirty = 0

        time.sleep(0.5)
        return result

    def _fetch(self, word: str) -> dict:
        try:
            url = f"https://svenska.se/tre/?sok={word}"
            self._page.goto(url, wait_until="domcontentloaded", timeout=15000)
            self._page.wait_for_timeout(1000)

            # Klicka på alla "Visa mer"-knappar för att få fullständiga definitioner
            for selector in [
                'button:has-text("VISA MER")',
                'button:has-text("Visa mer")',
                'button:has-text("visa mer")',
                '[class*="show-more"]',
                '[class*="expand"]',
            ]:
                try:
                    buttons = self._page.query_selector_all(selector)
                    for btn in buttons:
                        btn.click()
                except Exception:
                    pass

            # Vänta lite för att innehållet ska laddas efter klick
            if self._page.query_selector_all('button:has-text("MER")'):
                self._page.wait_for_timeout(1000)

            text = self._page.inner_text("body")
            return self._parse(word, text)
        except Exception as e:
            return {"word": word, "found": False, "text": "", "lines": [], "error": str(e)}

    def _parse(self, word: str, raw_text: str) -> dict:
        lines = [l.strip() for l in raw_text.split("\n")]
        # Remove empty lines and nav boilerplate
        content_lines = [
            l for l in lines
            if l and l.lower() not in _NAV_LINES and len(l) > 1
        ]

        # Determine if word was found (not just in nav)
        # Svenska.se shows "Inga träffar" when nothing is found
        full_text = "\n".join(content_lines)
        not_found_signals = ["inga träffar", "hittades inte", "no results"]
        found = (
            word.lower() in full_text.lower()
            and not any(s in full_text.lower() for s in not_found_signals)
        )

        # Tag which dictionaries returned results
        dicts_found = []
        text_lower = full_text.lower()
        # After stripping nav, if SAOL/SO/SAOB section headers appear as content
        for d in ["saol", "so", "saob"]:
            # Look for dictionary name appearing with surrounding content
            if re.search(rf'\b{d}\b', text_lower):
                dicts_found.append(d.upper())

        return {
            "word": word,
            "found": found,
            "text": full_text,
            "lines": content_lines[:80],
            "dicts": dicts_found,
        }

    def flush(self):
        if self._dirty > 0:
            save_cache(self.cache)
            self._dirty = 0
