"""Hittar v2-kort där Huvudbetydelse binder ihop betydelser med "eller"
istället för den överenskomna ` ; `-separatorn (se baksida.py build()-
docstring "huvudbetydelse-separatorer" och style_guide.md "Separatorer").

Systerscript till find_old_slash_separator.py, som täckte ` / `-varianten
av samma bugg. Motiverat av "pöbel"-fyndet 2026-08-07: det kortet hade
`"en okontrollerad folkmassa, eller människor från samhällets lägsta
skikt"` och hade ändå passerat BÅDE flerbetydelse_snabbkoll2 OCH
flerbetydelse_sokverifierad samma dag -- varken snabbkollen eller
sökkollen letar efter det här formateringsmönstret, bara efter sakfel i
själva betydelsen.

ÄNDRAR INGET. "eller" är ett helt normalt svenskt ord inuti en enskild
betydelse ("en våg eller krökning i hår eller ull" är korrekt), så en
blind ersättning skulle förstöra fler kort än den lagar. Scriptet
rankar därför kandidater i tre nivåer via signaler som går att räkna
fram mekaniskt, och lämnar själva bedömningen till granskaren:

  hog    -- synonym_groups har 2+ grupper (dvs synonymerna ÄR redan
            uppdelade i skilda betydelser) men Huvudbetydelse saknar
            ` ; ` och innehåller "eller". Exakt pöbel-mönstret.
  medel  -- ", eller" (komma + eller) utan ` ; ` i Huvudbetydelse.
            Kommatecknet före "eller" är i sig ett svagt tecken på att
            två fristående led binds ihop, inte en enkel uppräkning.
  lag    -- något " eller " alls, utan ` ; `. Mestadels legitima
            betydelser, tas med för fullständighetens skull.

Kort som REDAN har ` ; ` i Huvudbetydelse hoppas över helt -- där är
flerbetydelsestrukturen redan uttryckt, och ett "eller" inuti en av
delarna är nästan alltid korrekt svenska.

Tar med OLD-deckets baksida (samma facit som snabbkoll2.py) per kort, så
granskaren kan avgöra om de två leden verkligen är skilda betydelser
utan ett extra uppslag.

Skriver sessions/session_<datum>_eller-separator.json + en kondenserad
_condensed.txt (samma format som condense_session.py).
"""

import argparse
import datetime
import json
import os
import re

import baksida
import config
from ankiconnect import invoke
from snabbkoll2 import build_old_lookup

# " ; " är den överenskomna separatorn; parse() ger tillbaka den rå, så
# leta efter semikolon oavsett omgivande mellanslag.
_SEMICOLON_RE = re.compile(r"\s;\s")
_KOMMA_ELLER_RE = re.compile(r",\s+eller\s+", re.IGNORECASE)
_ELLER_RE = re.compile(r"\s+eller\s+", re.IGNORECASE)

NOTES_CHUNK = 2000  # notesInfo på hela decket på en gång spränger 60s-timeouten


def fetch_all_v2_notes():
    """Alla v2-kort i decket, oavsett suspend-status. Till skillnad från
    find_old_slash_separator.py filtreras suspenderade INTE bort -- den
    suspenderade poolen (~6850 kort) släpps in i Adams kö efterhand, och
    en separatorbugg där skulle överleva ända fram till att kortet visas.
    """
    note_ids = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" tag:{config.FORMAT_TAG_V2}')
    notes = []
    for i in range(0, len(note_ids), NOTES_CHUNK):
        notes.extend(invoke("notesInfo", notes=note_ids[i:i + NOTES_CHUNK]))
    return notes


def classify(huvudbetydelse, synonym_groups):
    """Returnerar (nivå, skäl) eller (None, None) om kortet inte är en
    kandidat alls."""
    if _SEMICOLON_RE.search(huvudbetydelse):
        return None, None  # flerbetydelse redan korrekt uttryckt
    if not _ELLER_RE.search(huvudbetydelse):
        return None, None

    n_groups = len(synonym_groups) if synonym_groups else 0
    if n_groups >= 2:
        return "hog", f"synonym_groups har {n_groups} grupper men Huvudbetydelse saknar ' ; '"
    if _KOMMA_ELLER_RE.search(huvudbetydelse):
        return "medel", "', eller' binder ihop två led utan ' ; '"
    return "lag", "' eller ' finns, men inga andra signaler"


def strip_html(s):
    if not s:
        return ""
    return re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ").strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-level", choices=["hog", "medel", "lag"], default="lag",
                        help="lägsta nivå att ta med i utdatafilen (default: alla)")
    args = parser.parse_args()

    levels_wanted = {"hog": ["hog"], "medel": ["hog", "medel"], "lag": ["hog", "medel", "lag"]}[args.min_level]

    notes = fetch_all_v2_notes()
    old_lookup = build_old_lookup()

    candidates = []
    counts = {"hog": 0, "medel": 0, "lag": 0}
    for n in notes:
        raw = n["fields"][config.FIELD_BAKSIDA]["value"]
        parsed = baksida.parse(raw)
        hb = parsed["huvudbetydelse"]
        if not hb:
            continue

        level, reason = classify(hb, parsed["synonym_groups"])
        if not level:
            continue
        counts[level] += 1
        if level not in levels_wanted:
            continue

        ord_ = n["fields"][config.FIELD_ORD]["value"]
        candidates.append({
            "noteId": n["noteId"],
            "ord": ord_,
            "niva": level,
            "skal": reason,
            "current": parsed,
            "old_facit": old_lookup.get(ord_.strip().lower()),
            "tags": n.get("tags", []),
            "proposed": None,
            "approved": False,
            "note_till_granskare": (
                "Avgor om 'eller' binder ihop TVA SKILDA betydelser (fel -> byt till ' ; ') "
                "eller star inuti EN betydelse (ratt -> ror ej). Verifiera mot old_facit/kalla, "
                "byt aldrig separator blint."
            ),
        })

    order = {"hog": 0, "medel": 1, "lag": 2}
    candidates.sort(key=lambda c: (order[c["niva"]], c["ord"]))

    print(f"{len(notes)} v2-kort skannade.")
    print(f"  hog:   {counts['hog']}")
    print(f"  medel: {counts['medel']}")
    print(f"  lag:   {counts['lag']}")
    if not candidates:
        print("Inga kandidater.")
        return

    today = datetime.date.today().isoformat()
    sessions_dir = os.path.join(os.path.dirname(__file__), "sessions")
    os.makedirs(sessions_dir, exist_ok=True)
    out_path = os.path.join(sessions_dir, f"session_{today}_eller-separator.json")
    n_dup = 2
    while os.path.exists(out_path):
        out_path = os.path.join(sessions_dir, f"session_{today}_eller-separator-batch{n_dup}.json")
        n_dup += 1
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(candidates, f, ensure_ascii=False, indent=2)

    condensed_path = f"{os.path.splitext(out_path)[0]}_condensed.txt"
    with open(condensed_path, "w", encoding="utf-8") as f:
        for i, c in enumerate(candidates):
            cur = c["current"]
            f.write(
                f"[{i}] {c['ord']} <{c['niva']}> :: HB={strip_html(cur['huvudbetydelse'])} "
                f":: REG={cur['register']} :: SYN={cur['synonymer']} "
                f":: GRP={cur['synonym_groups']} :: EX={strip_html(cur['exempelmening'])} "
                f":: OLD={strip_html(c['old_facit'])}\n"
            )

    print(f"Skrev {len(candidates)} kandidater till {out_path}")
    print(f"Kondenserad dump: {condensed_path}")


if __name__ == "__main__":
    main()
