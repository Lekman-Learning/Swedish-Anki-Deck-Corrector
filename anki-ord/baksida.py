"""Parse/bygg Baksida-fältets HTML-mikroformat (se config.py för formatspec,
"Kortformat v2", beslutat 2026-08-04, korrigerat 2026-08-04 efter Adams
feedback: inga fältetiketter ("Huvudbetydelse:" osv) skrivs ut alls. ENDAST
huvudbetydelsens värde ska vara fet — inget annat. Register ska ha temats
standardfärg (vit i nattläge), inte en hårdkodad grå ton.

Exempel på ett fält:
  <b>vara mycket trött</b><br>
  (vardaglig)<br>
  <br>
  <font color="#3498db">utmattad, dödstrött</font><br>
  <br>
  <i>Han var helt <font color="#3498db">slut</font> efter passet.</i>
  <br><br><img src="bild.jpg" style="max-width:400px; border-radius:4px;">   (valfritt, sist)

parse()/build() nedan hanterar detta v2-format. parse_legacy()/build_legacy()
hanterar det gamla formatet (blå synonymrad + <ol><li>-definitioner) och
finns kvar bara för att migrera redan skrivna kort — skriv aldrig nytt
innehåll med dem.
"""

import re

import config

_MAIN_RE = re.compile(
    r"<b>(?P<huvud>.*?)</b>\s*<br>"
    r"(?:\((?P<register>[^)]*)\)\s*<br>)?"
    r"\s*<br>\s*"
    rf'<font color="{re.escape(config.SYNONYM_COLOR)}">(?P<syn>.*?)</font>\s*<br>'
    r"\s*<br>\s*"
    r"<i>(?P<ex>.*?)</i>",
    re.DOTALL,
)
_IMG_TAIL_RE = re.compile(r"(<br>\s*<br>\s*<img.*)$", re.DOTALL)


def parse(baksida_html):
    match = _MAIN_RE.search(baksida_html)
    if not match:
        return {
            "huvudbetydelse": "",
            "register": None,
            "synonymer": [],
            "exempelmening": "",
            "bild_html": None,
            "synonym_groups": None,
        }

    huvudbetydelse = match.group("huvud").strip()
    register = match.group("register").strip() if match.group("register") else None

    raw = match.group("syn")
    synonym_groups = None
    if ";" in raw:
        synonym_groups = [[s.strip() for s in g.split(",")] for g in raw.split(";")]
        synonymer = [s for g in synonym_groups for s in g]
    else:
        synonymer = [s.strip() for s in raw.split(",") if s.strip()]

    exempelmening = match.group("ex").strip()

    img_match = _IMG_TAIL_RE.search(baksida_html)
    bild_html = img_match.group(1).strip() if img_match else None

    return {
        "huvudbetydelse": huvudbetydelse,
        "register": register,
        "synonymer": synonymer,
        "exempelmening": exempelmening,
        "bild_html": bild_html,
        "synonym_groups": synonym_groups,
    }


def build(huvudbetydelse, synonymer=None, exempelmening="", register=None, bild_html=None, synonym_groups=None):
    """register: sträng typ "formell" / "lätt negativ" / "formell, lätt negativ".
    Obligatoriskt i praktiken (style_guide.md, beslutat 2026-08-04) — minst en
    tagg på varje kort, None bara accepteras här på kodnivå för flexibilitet."""
    if huvudbetydelse:
        huvudbetydelse = huvudbetydelse[0].upper() + huvudbetydelse[1:]
    huvud_html = f"<b>{huvudbetydelse}</b><br>"

    register_html = f"({register})<br>" if register else ""

    if synonym_groups:
        synonym_text = " ; ".join(", ".join(g) for g in synonym_groups)
    else:
        synonym_text = ", ".join(synonymer or [])
    synonym_html = f'<font color="{config.SYNONYM_COLOR}">{synonym_text}</font><br>'

    example_html = f"<i>{exempelmening}</i>"

    parts = [huvud_html, register_html, "<br>", synonym_html, "<br>", example_html]
    if bild_html:
        parts.append(bild_html)
    return "".join(parts)


def validate_register(register):
    """Returnerar lista med varningssträngar (tom = ok). Kollar mot den låsta
    vokabulären i config.py — kraschar inte, bara ett granskningshjälpmedel.
    Register är obligatoriskt och båda axlarna (formalitet+valör) krävs,
    beslutat 2026-08-04 (skärpt från "minst en av dem")."""
    if not register:
        return ['register saknas helt — obligatoriskt, se style_guide.md']
    tags = [t.strip() for t in register.split(",")]
    warnings = [
        f'okänd register-tagg "{tag}", inte i config.REGISTER_FORMALITY/REGISTER_VALENS'
        for tag in tags
        if tag not in config.REGISTER_FORMALITY and tag not in config.REGISTER_VALENS
    ]
    formality_count = sum(1 for t in tags if t in config.REGISTER_FORMALITY)
    valens_count = sum(1 for t in tags if t in config.REGISTER_VALENS)
    # Minst en axel krävs totalt (kollas ovan via "if not register"). Båda
    # axlarna fylls bara när båda GENUINT passar (beslutat 2026-08-04,
    # nyanserat samma dag) — tvinga aldrig fram en gissad valör på ett
    # neutralt substantiv/facktermer bara för att nå två taggar.
    if formality_count > 1:
        warnings.append(f'flera formalitets-taggar i "{register}", max en per axel')
    if valens_count > 1:
        warnings.append(f'flera valör-taggar i "{register}", max en per axel')
    return warnings


# --- Legacy (format t.o.m. 2026-08-04, används bara av migrate_format.py) ---

_LEGACY_SYNONYM_RE = re.compile(
    rf'<font color="{re.escape(config.SYNONYM_COLOR)}">(.*?)</font>\s*<br>\s*<br>',
    re.DOTALL,
)
_LEGACY_LIST_RE = re.compile(r"<ol>\s*(.*?)\s*</ol>", re.DOTALL)
_LEGACY_LI_RE = re.compile(r"<li>(.*?)</li>", re.DOTALL)
_LEGACY_EXAMPLE_RE = re.compile(r"<i>(.*?)</i>", re.DOTALL)


def parse_legacy(baksida_html):
    synonym_match = _LEGACY_SYNONYM_RE.search(baksida_html)
    synonym_groups = None
    if synonym_match:
        raw = synonym_match.group(1)
        if ";" in raw:
            synonym_groups = [[s.strip() for s in g.split(",")] for g in raw.split(";")]
            synonymer = [s for g in synonym_groups for s in g]
        else:
            synonymer = [s.strip() for s in raw.split(",")]
    else:
        synonymer = []

    list_match = _LEGACY_LIST_RE.search(baksida_html)
    definitioner = [li.strip() for li in _LEGACY_LI_RE.findall(list_match.group(1))] if list_match else []

    example_match = _LEGACY_EXAMPLE_RE.search(baksida_html)
    exempelmening = example_match.group(1).strip() if example_match else ""

    img_match = _IMG_TAIL_RE.search(baksida_html)
    bild_html = img_match.group(1).strip() if img_match else None

    return {
        "synonymer": synonymer,
        "definitioner": definitioner,
        "exempelmening": exempelmening,
        "bild_html": bild_html,
        "synonym_groups": synonym_groups,
    }
