import re
from bs4 import BeautifulSoup

# Swedish stop words to ignore in comparisons
STOPWORDS = {
    "och", "att", "det", "en", "ett", "i", "på", "av", "som", "är", "med",
    "för", "inte", "om", "den", "till", "har", "de", "vi", "kan", "man",
    "så", "men", "sig", "var", "eller", "han", "hon", "nu", "sin", "sina",
    "sitt", "vid", "från", "mot", "efter", "under", "över", "ut", "upp",
    "ner", "in", "också", "då", "redan", "igen", "just", "när", "vad",
    "hur", "här", "där", "denna", "detta", "dessa", "deras", "dess",
    "ska", "skulle", "hade", "vara", "bli", "bli", "blev", "blivit",
    "någon", "något", "några", "alla", "allt", "mer", "mest", "mycket",
    "lite", "bara", "även", "både", "dock", "ändå", "sedan", "innan",
    "while", "the", "and", "or", "of", "to", "a", "is", "in", "it",
    "verb", "adj", "subst", "adv",
}

# Lines that are grammar/boilerplate — NOT definitions
_GRAMMAR_PATTERNS = re.compile(
    # Verb conjugation
    r"presens|preteritum|supinum|imperativ|infinitiv|particip|"
    r"finita former|infinita former|"
    r"\baktiv\b|\bpassiv\b|"
    r"^\s*att \w+\s*$|"
    r"har/hade|"
    r"\+ substantiv|"
    r"^en \w+\s*$|^ett \w+\s*$|^den/det/de\b|"
    # Noun/adjective declension
    r"obestämd form|bestämd form|genitiv|"
    r"^en \w+s?\t|^ett \w+s?\t|"
    r"\bpl\.\s|best\.\s*pl\.|"
    # Metadata/boilerplate
    r"publicerad:|ordklass:|uttal:|historik:|konstruktion:|"
    r"sammansättn|"
    r"dölj|visa mer|"
    r"hoppa till|svenska akademien|sök i tre|"
    r"träffar i saol|träffar i so|träffar i saob|"
    # Single word forms
    r"^\w+s\s*$|"
    r"^\w+de\s*$|"
    r"^\w+nde\s*$|"
    r"^\w+er\s*$|"
    r"^\w+ens?\s*$|"
    r"^\w+erna\s*$|"
    r"^\w+arnas?\s*$",
    re.IGNORECASE,
)


def _extract_words(text: str) -> set[str]:
    words = re.findall(r'\b[a-zåäöA-ZÅÄÖ]{3,}\b', text.lower())
    return {w for w in words if w not in STOPWORDS}


def _clean_svenska_text(raw_text: str) -> str:
    """Filtrera bort grammatik, konjugationer och boilerplate från Svenska.se-text."""
    lines = re.split(r'[\n\t]+', raw_text)
    definition_lines = []

    for line in lines:
        stripped = line.strip()
        if not stripped or len(stripped) < 4:
            continue
        if _GRAMMAR_PATTERNS.search(stripped):
            continue
        if re.match(r"^[a-zåäö]+\s*$", stripped, re.IGNORECASE) and len(stripped) < 25:
            continue
        if re.match(r"^\w+\s+(verb|adj|subst|adv)\b", stripped, re.IGNORECASE):
            continue
        if re.match(r"^[a-zåäö·|]+$", stripped, re.IGNORECASE) and len(stripped) < 30:
            continue
        definition_lines.append(stripped)

    return " ".join(definition_lines)


def parse_card_back(html: str) -> dict:
    """Extract synonyms, explanations and example from the card's back HTML."""
    soup = BeautifulSoup(html, "html.parser")

    # Synonyms: first <font color="..."> tag, comma-separated
    synonyms = []
    font_tags = soup.find_all("font", color=True)
    if font_tags:
        first_text = font_tags[0].get_text(strip=True)
        synonyms = [s.strip().lower() for s in first_text.split(",") if s.strip()]

    # Explanations from <ol><li> tags
    explanations = []
    for li in soup.find_all("li"):
        text = li.get_text(strip=True)
        if text:
            explanations.append(text.lower())

    # Example from <i> tag
    example = ""
    italic = soup.find("i")
    if italic:
        example = italic.get_text(strip=True).lower()

    full_text = soup.get_text(separator=" ", strip=True)

    return {
        "synonyms": synonyms,
        "explanations": explanations,
        "example": example,
        "full_text": full_text,
        "words": _extract_words(full_text),
    }


def _card_has_good_structure(card: dict) -> bool:
    """Kontrollera om kortet har rätt format: synonymer + förklaringar + exempel."""
    has_syns = len(card["synonyms"]) >= 2
    has_defs = len(card["explanations"]) >= 1
    has_example = len(card["example"]) > 10
    return has_syns and has_defs and has_example


def compare(card_back_html: str, svenska_result: dict, threshold: float = 0.25,
            synonymer_text: str = "") -> dict:
    """
    Compare a card's back content against Svenska.se + synonymer.se.

    Philosophy: the scanner's job is to catch WRONG cards, not to verify
    every word. A well-structured card (3 synonyms, 2 definitions, example)
    with ANY match from sources is assumed correct. Only flag mismatch when
    there's strong evidence the card is wrong.

    Returns a dict with:
      verdict  - "correct", "mismatch", "not_found", or "unclear"
      score    - 0.0–1.0 confidence
      tag      - Anki tag to apply
    """
    svenska_found = svenska_result.get("found", False)

    # If neither source has data → not found
    if not svenska_found and not synonymer_text:
        return {
            "verdict": "not_found",
            "score": 0.0,
            "tag": "swe_not_found",
            "detail": "Ordet hittades inte i SAOL, SO, SAOB eller synonymer.se",
        }

    card = parse_card_back(card_back_html)

    if not card["words"]:
        return {
            "verdict": "unclear",
            "score": 0.0,
            "tag": "swe_unclear",
            "detail": "Kunde inte läsa kortets baksida",
        }

    # Clean Svenska.se text
    clean_text = ""
    if svenska_found:
        clean_text = _clean_svenska_text(svenska_result.get("text", ""))

    # Combine sources
    combined_text = clean_text
    if synonymer_text:
        combined_text += " " + synonymer_text
    combined_lower = combined_text.lower()
    ref_words = _extract_words(combined_text)

    if not ref_words:
        return {
            "verdict": "not_found",
            "score": 0.0,
            "tag": "swe_not_found",
            "detail": "Inget användbart innehåll från någon källa",
        }

    # ── Check card structure ──
    good_structure = _card_has_good_structure(card)

    # ── 1. Synonym matching ──
    syn_hits = 0
    if card["synonyms"]:
        for syn in card["synonyms"]:
            if syn in combined_lower:
                syn_hits += 1
                continue
            syn_words = _extract_words(syn)
            if syn_words and syn_words & ref_words:
                syn_hits += 1
                continue
            if len(syn) >= 4:
                stem = syn[:4].lower()
                if any(w.startswith(stem) for w in ref_words):
                    syn_hits += 1
    syn_ratio = syn_hits / len(card["synonyms"]) if card["synonyms"] else 0.0

    # ── 2. Definition matching ──
    def_hits = 0
    def_total = 0
    for explanation in card["explanations"]:
        exp_words = _extract_words(explanation)
        if exp_words:
            for ew in exp_words:
                def_total += 1
                if ew in ref_words:
                    def_hits += 1
                    continue
                if len(ew) >= 4:
                    stem = ew[:4]
                    if any(w.startswith(stem) for w in ref_words):
                        def_hits += 1
    def_ratio = def_hits / def_total if def_total > 0 else 0.0

    # ── 3. General word overlap ──
    card_core_words = set()
    for syn in card["synonyms"]:
        card_core_words |= _extract_words(syn)
    for exp in card["explanations"]:
        card_core_words |= _extract_words(exp)

    if card_core_words:
        core_overlap = card_core_words & ref_words
        overlap_ratio = len(core_overlap) / len(card_core_words)
    else:
        overlap_ratio = 0.0

    # ── Decide verdict ──
    combined_score = syn_ratio * 0.40 + def_ratio * 0.40 + overlap_ratio * 0.20
    any_match = syn_hits > 0 or def_ratio > 0.1 or overlap_ratio > 0.1

    # A card is CORRECT if:
    #  1. It has good structure AND at least some source data exists
    #     (well-formed card = probably correct, we can't verify semantics via string matching)
    #  2. OR any text matching signal fires
    #  3. OR combined score passes threshold
    if good_structure and (svenska_found or synonymer_text):
        verdict, tag = "correct", "swe_ok"
        combined_score = max(combined_score, threshold)
    elif combined_score >= threshold:
        verdict, tag = "correct", "swe_ok"
    elif any_match:
        verdict, tag = "correct", "swe_ok"
        combined_score = max(combined_score, threshold)
    else:
        verdict, tag = "mismatch", "swe_mismatch"

    return {
        "verdict": verdict,
        "score": round(combined_score, 3),
        "syn_score": round(syn_ratio, 3),
        "def_score": round(def_ratio, 3),
        "overlap_score": round(overlap_ratio, 3),
        "tag": tag,
        "syn_hits": syn_hits,
        "synonyms_found": card["synonyms"],
        "good_structure": good_structure,
    }
