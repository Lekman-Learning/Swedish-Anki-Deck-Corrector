"""Mekanisk kontroll av att korten följer Adam-tal (style_guide.md).

Kompletterar snabbkoll 2.0/sökkoll, som båda kollar SAKINNEHÅLL (stämmer
betydelsen? saknas någon?). Ingen av dem kollar FORM -- det var precis
därför "pöbel" kunde passera båda samma dag den var trasig (se
CLAUDE.md). Detta script kollar bara sådant som går att avgöra
mekaniskt, och ändrar aldrig något.

Varje kontroll pekar på en namngiven regel i style_guide.md. Kontroller
markerade [SÄKER] är i praktiken utan falsklarm och kan åtgärdas rakt av;
[BEDÖM] har kända legitima undantag och kräver mänskligt omdöme -- de
rapporteras separat och ska aldrig massfixas.

Körning:
    python lint_adamtal.py                 # sammanfattning
    python lint_adamtal.py --visa REGEL    # alla träffar för en regel
    python lint_adamtal.py --json ut.json  # fullständig maskinläsbar rapport
"""

import argparse
import json
import re
from collections import Counter, defaultdict

import baksida
import config
from ankiconnect import invoke

NOTES_CHUNK = 2000

# Förkortningar vars punkt inte avslutar en mening -- utan dessa skulle
# "t.ex." räknas som tre meningsslut i kontrollen "flera_meningar".
_ABBR = ["t.ex.", "bl.a.", "m.fl.", "d.v.s.", "dvs.", "osv.", "m.m.",
         "fr.o.m.", "t.o.m.", "ca.", "kl.", "s.k.", "e.Kr.", "f.Kr."]

# Regler där falsklarm är vanliga nog att massfix vore fel.
# "flera_meningar" ligger här efter genomgången 2026-08-07: 3 av 4 träffar
# var LEGITIMA. "anafor" illustrerar stilfiguren genom att upprepa
# satsinledningen ("Jag kommer. Jag ser. Jag förstår.") -- en enda mening
# hade förstört kortet. Två av de andra är repliksvar där frågan behövs för
# att idiomet ska gå fram ("Hur står det till? - Jodå, det knallar och går").
BEDOM = {"cirkular_synonym", "cirkular_definition", "osymmetriska_grupper",
         "ordbokslangd_hb", "fragment_exempel", "flera_meningar"}


def strip_html(s):
    if not s:
        return ""
    return re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ").strip()


def meanings(hb):
    return [m.strip() for m in re.split(r"\s;\s", hb) if m.strip()]


def count_sentences(text):
    for a in _ABBR:
        text = text.replace(a, "@" * len(a))
    return len(re.findall(r"[.!?]+(?=\s|$)", text))


def stem(word):
    """Grov svensk stam: klipp vanliga böjnings-/avledningsändelser. Bara
    till för substrängjämförelser, inte riktig morfologi."""
    w = word.lower().strip()
    for suf in ("ande", "ende", "arna", "erna", "orna", "aren", "ade", "are",
                "ell", "en", "et", "er", "or", "ar", "an", "a", "s"):
        if len(w) - len(suf) >= 4 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def lint_card(ord_, raw):
    """Returnerar lista med (regel, detalj) för ett kort."""
    p = baksida.parse(raw)
    hb = p["huvudbetydelse"]
    if not hb:
        return [("ej_v2_format", "Baksida går inte att parsa som kortformat v2")]

    out = []
    ms = meanings(hb)
    ex_raw = p["exempelmening"] or ""
    ex = strip_html(ex_raw)
    syns = p["synonymer"] or []
    groups = p["synonym_groups"]

    # --- Exempelmening (style_guide.md "Highlight av ordet i exempelmeningen",
    #     "Exempelmeningar - alltid bara en") ---
    if not ex:
        out.append(("tom_exempelmening", "exempelmening saknas helt"))
    else:
        if config.SYNONYM_COLOR not in ex_raw:
            out.append(("saknar_highlight", ex[:70]))
        n = count_sentences(ex)
        if n > 1:
            out.append(("flera_meningar", f"{n} meningar: {ex[:70]}"))
        # Ordräkning är en DÅLIG proxy för "fragment" -- "Prelaten välsignade
        # menigheten." är fyra ord och en fullgod mening. Tröskeln sänktes
        # från 5 till 4 ord 2026-08-07 efter genomgång: av 101 träffar vid
        # <5 var i princip alla fullständiga meningar. Det verkliga felet
        # (sats utan finit verb, t.ex. "En grov skymf.") går inte att skilja
        # ut mekaniskt utan ordklasstaggning -- behandla som svag signal.
        if len(ex.split()) < 4:
            out.append(("fragment_exempel", ex))

    # --- Huvudbetydelse (style_guide.md "Vanliga fällor", "Grundregler") ---
    if hb.rstrip().endswith((".", ",")):
        out.append(("avslutande_skiljetecken_hb", hb[-45:]))
    if "<b>" in hb or "<font" in hb:
        out.append(("formatering_i_hb", hb[:70]))
    for m in ms:
        if len(m.split()) > 12:
            out.append(("ordbokslangd_hb", f"{len(m.split())} ord: {m[:70]}"))
    # ordet förklarat med sig självt
    if " " not in ord_.strip():
        st = stem(ord_)
        if len(st) >= 4 and re.search(rf"\b\w*{re.escape(st)}\w*", hb.lower()):
            out.append(("cirkular_definition", f"{ord_} -> {hb[:60]}"))

    # --- Synonymer (style_guide.md "Undvik cirkulära synonymer",
    #     "Symmetriska synonymgrupper") ---
    for s in syns:
        if not s.strip():
            out.append(("tom_synonym", "tom synonym i listan"))
            continue
        st = stem(ord_)
        if " " not in ord_.strip() and len(st) >= 4 and st in s.lower().replace(" ", ""):
            out.append(("cirkular_synonym", f"{ord_} -> {s}"))
    if groups:
        if any(not [x for x in g if x.strip()] for g in groups):
            out.append(("tom_synonymgrupp", "tom grupp ger '; '-artefakt"))
        if len(groups) != len(ms):
            out.append(("grupper_matchar_ej_betydelser",
                        f"{len(groups)} synonymgrupper mot {len(ms)} betydelser"))
        sizes = [len([x for x in g if x.strip()]) for g in groups]
        if sizes and max(sizes) - min(sizes) >= 2:
            out.append(("osymmetriska_grupper", f"gruppstorlekar {sizes}"))

    # --- Register (style_guide.md "Register per bibetydelse") ---
    regw = baksida.validate_register(p["register"])
    if regw:
        out.append(("register_ogiltigt", "; ".join(regw)))
    if p["register"]:
        nreg = len([r for r in p["register"].split(";") if r.strip()])
        if nreg > len(ms):
            out.append(("fler_register_an_betydelser",
                        f"{nreg} register mot {len(ms)} betydelser"))

    # --- Kvarglömd HTML (återkommande buggklass i CLAUDE.md) ---
    for junk in ("<span", "<div", "<ol", "<li", "&amp;nbsp;", "&quot;"):
        if junk in raw:
            out.append(("html_skrap", junk))
    if "<b>" in raw.split("</b>", 1)[-1]:
        out.append(("fet_utanfor_hb", "fet stil förekommer efter Huvudbetydelse"))

    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--visa", help="skriv ut alla träffar för en regel")
    parser.add_argument("--json", dest="json_out", help="skriv fullständig rapport som JSON")
    args = parser.parse_args()

    nids = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" tag:{config.FORMAT_TAG_V2}')
    notes = []
    for i in range(0, len(nids), NOTES_CHUNK):
        notes.extend(invoke("notesInfo", notes=nids[i:i + NOTES_CHUNK]))

    counts = Counter()
    by_rule = defaultdict(list)
    dirty = 0
    for n in notes:
        ord_ = n["fields"][config.FIELD_ORD]["value"]
        raw = n["fields"][config.FIELD_BAKSIDA]["value"]
        issues = lint_card(ord_, raw)
        if issues:
            dirty += 1
        for rule, detail in issues:
            counts[rule] += 1
            by_rule[rule].append({"noteId": n["noteId"], "ord": ord_, "detalj": detail})

    print(f"{len(notes)} v2-kort granskade. {len(notes) - dirty} helt rena, {dirty} med minst en anmärkning.\n")
    print(f"{'REGEL':<34} {'ANTAL':>6}  TYP")
    print("-" * 60)
    for rule, c in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"{rule:<34} {c:>6}  {'[BEDÖM]' if rule in BEDOM else '[SÄKER]'}")
    if not counts:
        print("(inga anmärkningar)")

    if args.visa:
        print(f"\n--- {args.visa} ({len(by_rule.get(args.visa, []))} träffar) ---")
        for h in by_rule.get(args.visa, []):
            print(f"  {h['ord']:<26} {h['detalj']}")

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(by_rule, f, ensure_ascii=False, indent=2)
        print(f"\nFullständig rapport: {args.json_out}")


if __name__ == "__main__":
    main()
