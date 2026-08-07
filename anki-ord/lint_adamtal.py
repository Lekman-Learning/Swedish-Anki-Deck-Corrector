"""Mekanisk kontroll av att korten följer Adam-tal (style_guide.md).

Kompletterar snabbkoll 2.0/sökkoll, som båda kollar SAKINNEHÅLL (stämmer
betydelsen? saknas någon?). Ingen av dem kollar FORM -- det var precis
därför "pöbel" kunde passera båda samma dag den var trasig (se
CLAUDE.md). Ändrar aldrig något.

**Reglerna bor i `baksida.validate_adamtal()`, inte här.** Samma funktion
kör som hård spärr i skrivvägen (`apply_flerbetydelse.apply_card()`,
`apply_updates.apply_single()`), så ett kort som skulle underkännas av
den här linten går inte att skriva från början. Detta script är den
RETROAKTIVA vyn: kort som skrevs innan spärren fanns. Duplicera aldrig
regellogik hit -- två definitioner som glider isär är precis den buggklass
som gav upphov till hela genomgången 2026-08-07.

Kontroller märkta [SÄKER] (= `baksida.ADAMTAL_HARDA`) blockerar skrivning
och kan åtgärdas rakt av. [BEDÖM] (= `ADAMTAL_MJUKA`) har kända legitima
undantag och ska aldrig massfixas.

Körning:
    python lint_adamtal.py                 # sammanfattning
    python lint_adamtal.py --visa REGEL    # alla träffar för en regel
    python lint_adamtal.py --json ut.json  # fullständig maskinläsbar rapport
"""

import argparse
import json
from collections import Counter, defaultdict

import baksida
import config
from ankiconnect import invoke

NOTES_CHUNK = 2000


def lint_card(ord_, raw):
    """Returnerar lista med (regel, detalj) för ett kort.

    Delegerar allt regelinnehåll till baksida.validate_adamtal(). Bara
    kontroller som kräver den OPARSADE Baksidan görs här -- de kan inte
    uttryckas i validatorn, som arbetar på färdiga fält.
    """
    p = baksida.parse(raw)
    if not p["huvudbetydelse"]:
        return [("ej_v2_format", "Baksida går inte att parsa som kortformat v2")]

    fel, varn = baksida.validate_adamtal(
        huvudbetydelse=p["huvudbetydelse"],
        synonymer=p["synonymer"],
        synonym_groups=p["synonym_groups"],
        exempelmening=p["exempelmening"],
        register=p["register"],
        ord_=ord_,
    )
    issues = [tuple(m.split(": ", 1)) for m in fel + varn]

    # --- Bara det som kräver rå HTML ---
    if p["register"]:
        issues += [("register_ogiltigt", w) for w in baksida.validate_register(p["register"])]
    for junk in baksida._HTML_SKRAP:
        if junk in raw and not any(r == "html_skrap" for r, _ in issues):
            issues.append(("html_skrap", f"kvarglömd HTML i Baksida: {junk!r}"))
            break
    if "<b>" in raw.split("</b>", 1)[-1]:
        issues.append(("fet_utanfor_hb", "fet stil förekommer efter Huvudbetydelse"))
    return issues


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
        typ = "[SÄKER]" if rule not in baksida.ADAMTAL_MJUKA else "[BEDÖM]"
        print(f"{rule:<34} {c:>6}  {typ}")
    if not counts:
        print("(inga anmärkningar)")
    print("\n[SÄKER] blockeras numera av spärren i apply_card()/apply_single() "
          "— nya kort kan inte få dessa fel.")

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
