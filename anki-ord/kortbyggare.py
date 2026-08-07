"""Kortbyggare v3.0 -- bygger dagsbatchen som ska skrivas om till v2.

Ersätter snabbkoll2_blanya_v2.py för det dagliga flödet från 2026-08-08:
125 kort/dag ur den suspenderade legacy-poolen (6 805 kort vid start,
~54 dagar). snabbkoll2_blanya_v2.py finns kvar för engångskörningar.

Vad den här filen gör: samlar ALLT granskaren behöver för ett kort på
ett ställe, så att inget steg kan glömmas bort mitt i en batch om 125.
Den skriver aldrig till Anki.

Per kort i sessionsfilen:
  legacy        -- nuvarande innehåll (parse_legacy)
  old_facit     -- uppslag i Svenska OLD-decket, projektets andra källa
  riskflaggor   -- mekaniska signaler, se riskflaggor.py
  adamtal_krav  -- de hårda reglerna kortet MÅSTE klara för att skrivas
  sokkoll       -- tomt fält som granskaren fyller med källa + slutsats
  proposed      -- tomt fält för det omskrivna kortet

Ordningen i kön är inte godtycklig: kort med `hog`-riskflagga läggs
FÖRST. Vid 125 kort/dag är uppmärksamheten som skarpast i början, och
"saknad hel betydelse" -- det dominerande felmönstret i åtta omgångar i
rad -- är exakt det som kräver skärpa.

Körning:
    python kortbyggare.py                    # 125 kort (config.DAGSBATCH_STORLEK)
    python kortbyggare.py --antal 25         # mindre sats
    python kortbyggare.py --dump             # skriv även en läsbar .txt
"""

import argparse
import datetime
import json
import os
import re

import baksida
import config
import riskflaggor
from ankiconnect import invoke
from queue_lib import fetch_cards_sorted_by_due
from snabbkoll2 import build_old_lookup

ALLVAR_ORDNING = {"hog": 0, "medel": 1, "lag": 2, None: 3}

GRANSKARINSTRUKTION = (
    "V3 -- ETT KORT ÄR INTE KLART FÖRRÄN ALLA FYRA STEGEN ÄR GJORDA: "
    "(1) Jämför mot old_facit. (2) Gör en RIKTIG sökkoll mot svenska.se/"
    "synonymer.se och skriv källa + slutsats i fältet 'sokkoll' -- ett tomt "
    "sokkoll-fält betyder att kortet inte får släppas. (3) Skriv om i Adam-tal: "
    "vardagliga ord, kort nog att läsas högt och förstås direkt, aldrig ordboksprosa, "
    "aldrig ordet i sin egen definition, förklara inte svårt med svårt, konkret före "
    "abstrakt, bevara humor. EN exempelmening med ordet i blått. Bara utbytbara "
    "synonymer. (4) Läs riskflaggorna -- 'hog' betyder att kortet statistiskt "
    "sannolikt saknar en HEL betydelse, det vanligaste felet i decket. "
    "Alla betydelser separeras med ' ; ' och synonymerna grupperas i samma ordning."
)


def hamta_pool(antal):
    """Suspenderade kort som ännu inte är v2. Due-sorterat = samma ordning
    Adam möter dem i när de väl släpps."""
    query = (
        f'deck:"{config.DECK_NAME}" is:suspended -tag:{config.FORMAT_TAG_V2} '
        f'-tag:{config.DAGSBATCH_TAG_PREFIX}::*'
    )
    return fetch_cards_sorted_by_due(query, antal)


def bygg_post(card, old_lookup):
    falt = {n: v["value"] for n, v in card["fields"].items()}
    ord_ = falt.get(config.FIELD_ORD, "")
    raw = falt.get(config.FIELD_BAKSIDA, "")

    parsed = baksida.parse(raw)
    ar_v2 = bool(parsed["huvudbetydelse"])
    legacy = parsed if ar_v2 else baksida.parse_legacy(raw)
    old = old_lookup.get(ord_.strip().lower())
    flaggor = riskflaggor.berakna(ord_, legacy, old)

    return {
        "noteId": card["note"],
        "ord": ord_,
        "nuvarande_format": "v2" if ar_v2 else "legacy",
        "legacy": legacy,
        "old_facit": old,
        "har_old_facit": bool(old),
        "riskflaggor": [
            {"flagga": f, "allvar": a, "forklaring": t} for f, a, t in flaggor
        ],
        "hogsta_allvar": riskflaggor.hogsta_allvar(flaggor),
        "adamtal_krav": list(baksida.ADAMTAL_HARDA),
        # --- fylls av granskaren ---
        "sokkoll": None,          # {"kalla": "...", "slutsats": "..."} -- OBLIGATORISKT
        "proposed": None,         # {"huvudbetydelse","register","synonymer","synonym_groups","exempelmening"}
        "approved": False,
        "note_till_granskare": GRANSKARINSTRUKTION,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--antal", type=int, default=config.DAGSBATCH_STORLEK)
    p.add_argument("--dump", action="store_true", help="skriv även en läsbar .txt")
    args = p.parse_args()

    cards = hamta_pool(args.antal)
    if not cards:
        print("Poolen är tom -- alla kort är omskrivna eller redan uttagna i en batch.")
        return

    old_lookup = build_old_lookup()
    poster = [bygg_post(c, old_lookup) for c in cards]
    poster.sort(key=lambda e: (ALLVAR_ORDNING[e["hogsta_allvar"]], e["ord"]))

    idag = datetime.date.today().isoformat()
    katalog = os.path.join(os.path.dirname(__file__), "sessions")
    os.makedirs(katalog, exist_ok=True)
    sokvag = os.path.join(katalog, f"session_{idag}_v3-batch.json")
    n = 2
    while os.path.exists(sokvag):
        sokvag = os.path.join(katalog, f"session_{idag}_v3-batch{n}.json")
        n += 1
    with open(sokvag, "w", encoding="utf-8") as f:
        json.dump(poster, f, ensure_ascii=False, indent=2)

    # Markera korten som uttagna så nästa körning inte tar samma igen.
    # ETT anrop för hela batchen, inte 125 stycken: ett avbrott mitt i en
    # kort-för-kort-loop hade lämnat halva batchen otaggad, och nästa
    # körning hade då plockat upp samma kort igen och dubblerat arbetet.
    invoke("addTags", notes=[e["noteId"] for e in poster],
           tags=f"{config.DAGSBATCH_TAG_PREFIX}::{idag}")

    if args.dump:
        rader = []
        for i, e in enumerate(poster):
            defs = e["legacy"].get("definitioner") or [e["legacy"].get("huvudbetydelse", "")]
            rensa = lambda s: re.sub(r"<[^>]+>", "", s or "").strip()
            rader.append(
                f"[{i}] {e['ord']}  <{e['hogsta_allvar'] or 'ren'}>\n"
                f"     NU  : {' | '.join(rensa(d) for d in defs)}\n"
                f"     SYN : {e['legacy'].get('synonymer')}\n"
                f"     OLD : {rensa(e['old_facit'])[:110]}\n"
                f"     RISK: {riskflaggor.sammanfatta([(r['flagga'], r['allvar'], '') for r in e['riskflaggor']])}"
            )
        with open(f"{os.path.splitext(sokvag)[0]}_dump.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(rader))

    antal_hog = sum(1 for e in poster if e["hogsta_allvar"] == "hog")
    utan_old = sum(1 for e in poster if not e["har_old_facit"])
    print(f"Skrev {len(poster)} kort till {sokvag}")
    print(f"  hög risk (läs dessa först) : {antal_hog}")
    print(f"  utan OLD-facit (blir Gula)  : {utan_old}")
    print(f"  kvar i poolen efter denna   : "
          f"{len(invoke('findNotes', query=f'deck:\"{config.DECK_NAME}\" is:suspended -tag:{config.FORMAT_TAG_V2} -tag:{config.DAGSBATCH_TAG_PREFIX}::*'))}")


if __name__ == "__main__":
    main()
