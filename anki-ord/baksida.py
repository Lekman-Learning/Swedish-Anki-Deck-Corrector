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

Flera betydelser (beslutat 2026-08-05, se style_guide.md "Register per
bibetydelse"): om betydelse 2+ har ETT ANNAT register än betydelse 1,
skrivs BÅDA registren på SAMMA rad, andra registret indraget med &nbsp;
till ungefär under sin betydelses startpunkt i Huvudbetydelse-raden ovanför:
  <b>En våg eller krökning i hår eller ull ; att fjäska och smickra någon underdånigt</b><br>
  (dialektal)                              (vardaglig, negativ)<br>
  <br>
  ...
register-parametern till build() är då " ; "-separerad, en del per
betydelse — build() räknar ut indraget automatiskt utifrån
huvudbetydelsens textlängd (tecken-baserad approximation, inte
pixelperfekt eftersom fetstil inte är monospace).

parse()/build() nedan hanterar detta v2-format. parse_legacy()/build_legacy()
hanterar det gamla formatet (blå synonymrad + <ol><li>-definitioner) och
finns kvar bara för att migrera redan skrivna kort — skriv aldrig nytt
innehåll med dem.
"""

import re

import config

_MAIN_RE = re.compile(
    r"<b>(?P<huvud>.*?)</b>\s*<br>"
    r"(?P<register_block>(?:(?:&nbsp;)*\([^)]*\))*\s*<br>\s*)?"
    r"\s*<br>\s*"
    rf'<font color="{re.escape(config.SYNONYM_COLOR)}">(?P<syn>.*?)</font>\s*<br>'
    r"\s*<br>\s*"
    r"<i>(?P<ex>.*?)</i>",
    re.DOTALL,
)
_REGISTER_LINE_RE = re.compile(r"\(([^)]*)\)")
# Ett eller flera <br> före <img>, inte exakt två: build() skriver alltid
# <br><br>, men äldre/handredigerade kort kan ha ett enda <br> (hittat
# 2026-08-07 på "faun"). Med det gamla, strikta mönstret returnerade
# parse() bild_html=None för sådana kort, och nästa parse->build RADERADE
# bilden tyst -- t.ex. i restore_images_from_old_deck.py eller vilken
# innehållsfix som helst som bygger om kortet.
_IMG_TAIL_RE = re.compile(r"((?:<br>\s*)+<img.*)$", re.DOTALL)
# Fet bokstav är bredare än ett &nbsp;-mellanslag, så en ren teckenräkning
# hamnar för långt till vänster (upptäckt 2026-08-05, Adam: registret för
# betydelse 2 landade mitt i ; -gränsen istället för till höger om den).
# Skala upp offseten för att kompensera — justera denna konstant om
# indraget fortfarande sitter fel.
_REGISTER_INDENT_SCALE = 1.5


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
    register_lines = [r.strip() for r in _REGISTER_LINE_RE.findall(match.group("register_block") or "")]
    register = " ; ".join(register_lines) if register_lines else None

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
    tagg på varje kort, None bara accepteras här på kodnivå för flexibilitet.

    huvudbetydelse-separatorer (ändrat 2026-08-05, se style_guide.md):
    ` ; ` = faktiskt skilda betydelser, ` / ` = omformuleringar av samma
    betydelse. Fritext, kollas inte av denna funktion."""
    if huvudbetydelse:
        huvudbetydelse = huvudbetydelse[0].upper() + huvudbetydelse[1:]
    huvud_html = f"<b>{huvudbetydelse}</b><br>"

    if register:
        reg_parts = [r.strip() for r in register.split(";")]
        if len(reg_parts) > 1:
            # Flera betydelser med olika register (beslutat 2026-08-05, se
            # style_guide.md "Register per bibetydelse"): en rad, varje
            # register indraget till ungefär under SIN betydelses startpunkt
            # i Huvudbetydelse-raden ovanför. Tecken-baserad approximation
            # (fetstil är inte monospace, blir aldrig pixelperfekt) — bra
            # nog för att visuellt koppla ihop rätt register med rätt
            # betydelse.
            meanings = huvudbetydelse.split(" ; ")
            offsets = []
            pos = 0
            for m in meanings:
                offsets.append(pos)
                pos += len(m) + len(" ; ")
            pieces = []
            cursor = 0
            for i, part in enumerate(reg_parts):
                raw_offset = offsets[i] if i < len(offsets) else cursor
                offset = round(raw_offset * _REGISTER_INDENT_SCALE)
                pad = max(1, offset - cursor) if i > 0 else 0
                piece = f"{'&nbsp;' * pad}({part})"
                pieces.append(piece)
                cursor += pad + len(f"({part})")
            register_html = "".join(pieces) + "<br>"
        else:
            register_html = f"({reg_parts[0]})<br>"
    else:
        register_html = ""

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
    beslutat 2026-08-04 (skärpt från "minst en av dem").

    Stöder flera betydelser (beslutat 2026-08-05): register kan innehålla
    ` ; `-separerade delar, en per betydelse som har ETT EGET register
    (bara betydelser 2+ vars register skiljer sig behöver anges, se
    style_guide.md "Register per bibetydelse") — varje del valideras var
    för sig mot samma vokabulär/max-en-per-axel-regel."""
    if not register:
        return ['register saknas helt — obligatoriskt, se style_guide.md']

    warnings = []
    for part in register.split(";"):
        part = part.strip()
        tags = [t.strip() for t in part.split(",")]
        warnings += [
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
            warnings.append(f'flera formalitets-taggar i "{part}", max en per axel')
        if valens_count > 1:
            warnings.append(f'flera valör-taggar i "{part}", max en per axel')
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
