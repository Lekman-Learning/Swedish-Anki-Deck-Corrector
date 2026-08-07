"""Generisk kondenserad-dump-generator för sessions-JSON-filer (2026-08-07).

Ersätter de ad-hoc scratchpad-scripten som skrevs om för hand i varje
granskningsomgång denna session (review_batch2_condensed.txt,
newtest50_full.txt, m.fl.) med ett enda återanvändbart script. Fungerar
på både v2-formaterade och legacy-formaterade "current"-poster (se
baksida.parse()/parse_legacy()), och tar med "format_bug_hints" om
sessionsfilen har dem (se snabbkoll2_blanya_v2.py) så granskaren direkt
ser vilka kort som statistiskt förtjänar extra uppmärksamhet.

Användning:
    python condense_session.py sessions/session_2026-08-07_xxx.json
Skriver <samma namn>_condensed.txt i samma katalog.
"""

import argparse
import json
import os
import re


def strip_html(s):
    if not s:
        return ""
    return re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ").strip()


def format_current(current):
    """Formaterar antingen v2- eller legacy-formen av 'current' till en
    kort HB=.../SYN=.../EX=...-sträng. Legacy-kort saknar huvudbetydelse
    och har istället en definitioner-lista -- den slås ihop med ' / '
    här (bara för läsbarhet i dumpen, inte en style_guide-betydelse)."""
    if "huvudbetydelse" in current:
        hb = strip_html(current.get("huvudbetydelse"))
        syn = current.get("synonymer") or []
        ex = strip_html(current.get("exempelmening"))
    else:
        defs = [strip_html(d) for d in (current.get("definitioner") or [])]
        hb = " / ".join(d for d in defs if d)
        syn = current.get("synonymer") or []
        ex = strip_html(current.get("exempelmening"))
    return hb, syn, ex


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("session_file")
    args = parser.parse_args()

    with open(args.session_file, encoding="utf-8") as f:
        entries = json.load(f)

    lines = []
    for i, e in enumerate(entries):
        hb, syn, ex = format_current(e["current"])
        old = strip_html(e.get("old_facit"))
        fmt = e.get("current_format", "")
        hints = e.get("format_bug_hints") or []
        line = (
            f"[{i}] {e['ord']} :: HB={hb} :: SYN={syn} :: EX={ex} "
            f":: OLD={old} :: FMT={fmt}"
        )
        if hints:
            line += f" :: HINTS={hints}"
        lines.append(line)

    base, _ = os.path.splitext(args.session_file)
    out_path = f"{base}_condensed.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Skrev {len(lines)} rader till {out_path}")


if __name__ == "__main__":
    main()
