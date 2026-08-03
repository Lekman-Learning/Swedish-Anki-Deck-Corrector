"""Parse/bygg Baksida-fältets HTML-mikroformat (se config.py för formatspec).

Exempel på ett fält:
  <font color="#3498db">synonym1, synonym2, synonym3</font><br><br>
  <ol><li>definition 1</li><li>definition 2</li></ol>
  <i>exempelmening med <font color="#3498db">ordet</font> ibland markerat</i>
  <br><br><img src="bild.jpg" style="max-width:400px; border-radius:4px;">   (valfritt, sist)
"""

import re

import config

_SYNONYM_RE = re.compile(
    rf'<font color="{re.escape(config.SYNONYM_COLOR)}">(.*?)</font>\s*<br>\s*<br>',
    re.DOTALL,
)
_LIST_RE = re.compile(r"<ol>\s*(.*?)\s*</ol>", re.DOTALL)
_LI_RE = re.compile(r"<li>(.*?)</li>", re.DOTALL)
_EXAMPLE_RE = re.compile(r"<i>(.*?)</i>", re.DOTALL)
_IMG_TAIL_RE = re.compile(r"(<br>\s*<br>\s*<img.*)$", re.DOTALL)


def parse(baksida_html):
    synonym_match = _SYNONYM_RE.search(baksida_html)
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

    list_match = _LIST_RE.search(baksida_html)
    definitioner = [li.strip() for li in _LI_RE.findall(list_match.group(1))] if list_match else []

    example_match = _EXAMPLE_RE.search(baksida_html)
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


def build(synonymer, definitioner, exempelmening, bild_html=None, synonym_groups=None):
    if synonym_groups:
        synonym_text = " ; ".join(", ".join(g) for g in synonym_groups)
    else:
        synonym_text = ", ".join(synonymer)
    synonym_html = f'<font color="{config.SYNONYM_COLOR}">{synonym_text}</font><br><br>'
    list_html = "<ol>" + "".join(f"<li>{d}</li>" for d in definitioner) + "</ol>"
    example_html = f"<i>{exempelmening}</i>"

    parts = [synonym_html, list_html, example_html]
    if bild_html:
        parts.append(bild_html)
    return "".join(parts)
