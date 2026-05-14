import json
import re

import ollama
from bs4 import BeautifulSoup

MODEL = "mistral"


def check_ollama(model: str = None) -> str:
    """Kontrollera att Ollama är igång och modellen finns. Returnerar modellnamn."""
    m = model or MODEL
    try:
        ollama.chat(model=m, messages=[{"role": "user", "content": "hej"}])
        return m
    except Exception as e:
        raise RuntimeError(
            f"Ollama svarar inte med modell '{m}': {e}\n"
            f"Kör: ollama serve  (i ett terminalfönster)\n"
            f"Kör: ollama pull {m}"
        )


def list_models() -> list[str]:
    """Lista alla installerade Ollama-modeller."""
    try:
        models = ollama.list()
        return [m.model for m in models.models]
    except Exception:
        return []


def extract_card_content(word: str, svenska_text: str, synonymer_text: str, model: str = None) -> dict:
    """Skicka scrapad text till lokal AI och få tillbaka strukturerat kortinnehåll."""
    m = model or MODEL

    prompt = f"""Du är en svensk ordboksredaktör. Skapa ett Anki-kort för ordet "{word}".

INFORMATION FRÅN SVENSKA.SE:
{svenska_text[:2000]}

SYNONYMER FRÅN SYNONYMER.SE:
{synonymer_text[:600]}

REGLER (följ EXAKT):
1. Välj EXAKT 3 synonymer, komma-separerade. De MÅSTE stämma semantiskt med ordets betydelse.
   - DÅLIGT: om ordet betyder "gå långsamt" → "springa" (FEL betydelse)
   - BRA: om ordet betyder "gå långsamt" → "traska" (RÄTT betydelse)
2. Skriv förklaring 1: ordets VANLIGASTE betydelse. Max 2 meningar. Enkelt språk.
3. Skriv förklaring 2: en ANNAN betydelse eller vanligt sammanhang. Max 2 meningar.
4. Skriv EN exempelmening (10-20 ord) som visar ordet i vardaglig användning.
   Ordet "{word}" MÅSTE finnas med i meningen.

Svara ENBART med detta JSON-format, inget annat:
{{"synonymer": "ord1, ord2, ord3", "forklaring1": "...", "forklaring2": "...", "exempel": "..."}}"""

    response = ollama.chat(
        model=m,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.2, "num_ctx": 4096},
    )

    raw = response["message"]["content"]

    match = re.search(r"\{[^{}]*\}", raw, re.DOTALL)
    if not match:
        raise ValueError(f"AI svarade inte med JSON: {raw[:300]}")

    data = json.loads(match.group())

    # ── Validera och fixa formatet ──
    for key in ("synonymer", "forklaring1", "forklaring2", "exempel"):
        if key not in data or not data[key]:
            data[key] = ""

    # Säkerställ exakt 3 synonymer
    syns = [s.strip() for s in data["synonymer"].split(",") if s.strip()]
    if len(syns) > 3:
        syns = syns[:3]
    elif len(syns) < 3 and synonymer_text:
        # Fyll på från synonymer.se om AI gav för få
        extra = [s.strip() for s in synonymer_text.split(",") if s.strip()]
        for e in extra:
            if e.lower() not in [s.lower() for s in syns] and e.lower() != word.lower():
                syns.append(e)
                if len(syns) >= 3:
                    break
    data["synonymer"] = ", ".join(syns[:3])

    # Säkerställ att båda förklaringarna finns
    if not data["forklaring1"] and data["forklaring2"]:
        data["forklaring1"] = data["forklaring2"]
        data["forklaring2"] = ""
    if not data["forklaring2"]:
        data["forklaring2"] = f'Ordet "{word}" används ofta i vardagligt tal och skrift.'

    # Säkerställ exempelmening
    if not data["exempel"]:
        data["exempel"] = f'Det är viktigt att förstå vad {word} betyder.'

    return data


def build_card_back(word: str, data: dict) -> str:
    """Bygg HTML för kortets baksida.

    Format (exakt som deckets original):
        <font color="#3498db">syn1, syn2, syn3</font>
        <br><br>
        <ol>
        <li>Förklaring 1.</li>
        <li>Förklaring 2.</li>
        </ol>
        <i>Exempelmening med <font color="#3498db">ordet</font> markerat.</i>
    """
    synonymer = data.get("synonymer", "").strip()
    f1 = data.get("forklaring1", "").strip()
    f2 = data.get("forklaring2", "").strip()
    exempel = data.get("exempel", "").strip()

    # Markera ordet i blått i exempelmeningen
    if exempel and word:
        # Prova hela ordet först, sen bara grundformen (första ordet i en fras)
        marked = False
        for w in [word, word.split()[0]]:
            base = re.escape(w)
            # Matcha ordet och eventuella böjningsändelser
            new_ex, n = re.subn(
                rf"\b({base}[a-zåäöA-ZÅÄÖ]*)\b",
                r'<font color="#3498db">\1</font>',
                exempel,
                flags=re.IGNORECASE,
                count=1,
            )
            if n > 0:
                exempel = new_ex
                marked = True
                break

    # Bygg HTML — alltid exakt 3 delar: synonymer, 2 förklaringar, exempel
    parts = [
        f'<font color="#3498db">{synonymer}</font>',
        "<br><br>",
        "<ol>",
        f"<li>{f1}</li>" if f1 else "<li>—</li>",
        f"<li>{f2}</li>" if f2 else "<li>—</li>",
        "</ol>",
        f"<i>{exempel}</i>" if exempel else "",
    ]

    return "\n".join(p for p in parts if p)


def preview_card(word: str, old_html: str, new_html: str):
    """CLI-förhandsgranskning."""
    def strip(html):
        return BeautifulSoup(html, "html.parser").get_text(separator=" | ", strip=True)

    print(f"\n  Ord:      {word}")
    print(f"  Gammalt:  {strip(old_html)[:120]}")
    print(f"  Nytt:     {strip(new_html)[:120]}")
