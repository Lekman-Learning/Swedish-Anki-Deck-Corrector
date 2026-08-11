"""Nollställer schemaläggningen för kort vars BETYDELSE ändrats — tillbaka till is:new.

Adams beslut 2026-08-11: "om ett av de is:review korten verkade vara fel så får
du glömma de alltså lägga det i is:new så att jag lär mig om rätt."

PROBLEMET SOM LÖSES. När ett is:review-kort rättas i sak har Adam redan lärt
sig den gamla, felaktiga versionen — och Ankis schemaläggning speglar just den
inlärningen. Ett kort med 90 dagars intervall betyder "Adam kan det här";
efter en sakrättning är det påståendet falskt, men intervallet står kvar. Kortet
dyker då upp igen om tre månader, och fram till dess är det enda han minns fel
version. `forgetCards` river schemat och lägger kortet i nya-kön så att det
lärs in på nytt från grunden.

NÄR DEN *INTE* SKA ANVÄNDAS — det här är hela poängen med att ha ett eget
skript i stället för ett löst kommando. Att glömma ett kort KOSTAR: månader av
repetitionshistorik kastas. Det är rätt pris när Adam lärt sig något felaktigt,
och fel pris annars. Regeln:

  GLÖM      huvudbetydelsen ändrad, en betydelse tillagd/borttagen, en synonym
            som var sakligt fel, register som vänder ordets innebörd
  GLÖM INTE stavfel i exempelmeningen, formatfix, tillagd etymologi, ny bild,
            omformulering som betyder samma sak

Tumregeln: skulle Adam ha svarat FEL på det gamla kortet med den nya kunskapen?
Då ska det glömmas. Annars inte.

Skriptet loggar varje glömt kort till `glomda.jsonl` med skälet, eftersom en
raderad repetitionshistorik inte går att granska i efterhand — utan loggen
finns ingen skillnad mellan "glömdes med gott skäl" och "glömdes av misstag".

  python v3_glom.py --torr              # visa vad som skulle glömmas
  python v3_glom.py --fil glom.json     # [{"ord":..., "skal":...}, ...]
"""

import argparse
import datetime
import json
import os
import re

import config
from ankiconnect import invoke

LOGG = os.path.join(os.path.dirname(__file__), "glomda.jsonl")


def kort_for_ord(ord_):
    """Kort-ID för ett uppslagsord. Exakt matchning på Framsida-fältet."""
    # Anki-sökningens "Framsida:x" matchar hela fältet, vilket är vad vi vill
    # -- en fritextsökning hade träffat ordet inne i andra korts exempelmeningar.
    esc = ord_.replace('"', '\\"')
    return invoke("findCards", query=f'deck:"{config.DECK_NAME}" "Framsida:{esc}"')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fil", required=True,
                    help='JSON: [{"ord": "...", "skal": "..."}, ...]')
    ap.add_argument("--torr", action="store_true")
    args = ap.parse_args()

    poster = json.load(open(args.fil, encoding="utf-8"))
    saknar_skal = [p["ord"] for p in poster if not p.get("skal", "").strip()]
    if saknar_skal:
        raise SystemExit(
            f"AVBRYTER: {len(saknar_skal)} poster saknar 'skal': {saknar_skal[:5]}. "
            "Ett glömt kort utan nedskrivet skäl går inte att granska i efterhand."
        )

    plan = []
    for p in poster:
        ids = kort_for_ord(p["ord"])
        if not ids:
            raise SystemExit(f"AVBRYTER: hittade inget kort för '{p['ord']}'.")
        plan.append((p, ids))

    info = {c["cardId"]: c for c in invoke(
        "cardsInfo", cards=[i for _p, ids in plan for i in ids])}

    print(f"{'Ord':<24}{'Ivl':>6}{'Reps':>6}{'Laps':>6}  Skäl")
    for p, ids in plan:
        c = info[ids[0]]
        print(f"{p['ord']:<24}{c['interval']:>5}d{c['reps']:>6}{c['lapses']:>6}  {p['skal'][:60]}")

    alla = [i for _p, ids in plan for i in ids]
    print(f"\n{len(plan)} ord / {len(alla)} kort. Repetitionshistoriken nollställs.")

    if args.torr:
        print("--torr: inget ändrat.")
        return

    invoke("forgetCards", cards=alla)

    kvar = [i for i in alla if i not in set(invoke(
        "findCards", query=f'deck:"{config.DECK_NAME}" is:new'))]
    if kvar:
        raise SystemExit(f"VARNING: {len(kvar)} kort ligger inte i is:new efteråt.")

    nu = datetime.datetime.now().isoformat(timespec="seconds")
    with open(LOGG, "a", encoding="utf-8") as f:
        for p, ids in plan:
            c = info[ids[0]]
            f.write(json.dumps({
                "tid": nu, "ord": p["ord"], "skal": p["skal"], "kort": ids,
                "fore": {"interval": c["interval"], "reps": c["reps"],
                         "lapses": c["lapses"], "factor": c["factor"]},
            }, ensure_ascii=False) + "\n")

    print(f"Klart: {len(alla)} kort glömda och loggade i {os.path.basename(LOGG)}.")


if __name__ == "__main__":
    main()
