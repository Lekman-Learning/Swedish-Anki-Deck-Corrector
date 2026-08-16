# -*- coding: utf-8 -*-
"""Rangordnar de PROVISORISKA is:review-korten efter hur bråttom full v3 är.

Adams beslut 2026-08-16: *"skriv om 50 av de sökkollade provisoriska v3 korten
i is:review"*. Det vänder på prioriteringen från 2026-08-11, där de 1 982
suspenderade korten gick först med motiveringen att de var helt osynliga för
honom. De provisoriska är det motsatta: de ligger i kön och pluggas varje dag,
så ett fel där kostar löpande.

VARFÖR EN EGEN FIL I STÄLLET FÖR EN FLAGGA I `v3_urgency.py`. Den filen
*undantar* provisoriska uttryckligen (rad 111-113), och undantaget är inte en
detalj utan hela dess uppdrag -- den rankar restpoolen. Att lägga in ett
`--bara-provisoriska` hade gjort samma fil till två motsatta verktyg och gjort
det lätt att köra fel läge utan att märka det. Utfilerna heter därför också
något annat, så att en körning aldrig skriver över den andras rankning.

SKILLNADEN I RISKPROFIL, och varför vikterna inte kan återanvändas rakt av:
per definition HAR varje kort i den här poolen en riktig sökkoll och saknar
röd/gul flagga och 3+ lapses -- det var villkoren för att släppas provisoriskt.
Fyra av `v3_urgency.RISK`-posterna är alltså konstanta över hela poolen och
diskriminerar ingenting. De behålls ändå (de kostar inget och gör poängen
jämförbar mellan filerna), men det som faktiskt sorterar här är exponeringen
och registerbristen.

    python v3_urgency_provisorisk.py            # skriv rankad lista
    python v3_urgency_provisorisk.py --antal 50 # + skriv id-fil för kortbyggare
"""

import argparse
import json
import re
from collections import Counter

import baksida
import config
from ankiconnect import invoke
from v3_urgency import RISK, REGISTER_POANG, exponering

DECK = f'deck:"{config.DECK_NAME}"'
MALGRUPP = f"{DECK} is:review -is:learn tag:v3_provisorisk::*"

UTFIL_MD = "v3_urgency_provisorisk.md"
UTFIL_JSON = "v3_urgency_provisorisk.json"
UTFIL_IDS = "v3_provisorisk_ids.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--antal", type=int, metavar="N",
                    help=f"skriv de N översta som id-lista till {UTFIL_IDS}, "
                         "för kortbyggare.py --ids-fil")
    args = ap.parse_args()

    # Samma undantag som i v3_urgency: färdiga och pausade kort har inget
    # arbete kvar, och `--ids-fil` går förbi POOL_FRAGA och därmed förbi det
    # filter som annars håller dem ute.
    klara = set(invoke("findCards", query=(
        f"{MALGRUPP} tag:{config.OBEROENDE_TAG_PREFIX}::*")))
    pausade = set(invoke("findCards", query=f"{DECK} tag:v3_pausad::*"))
    kort = [c for c in invoke("findCards", query=MALGRUPP)
            if c not in klara and c not in pausade]
    print(f"provisoriska is:review: {len(kort)} kort att granska "
          f"({len(klara)} redan blindgranskade, {len(pausade)} pausade — undantagna)")
    if not kort:
        raise SystemExit("Inget att ranka.")

    traffar = {}
    for namn, uttryck, _vikt in RISK:
        traffar[namn] = set(invoke("findCards", query=f"{MALGRUPP} {uttryck}"))
    snart_set = set(invoke("findCards", query=f"{MALGRUPP} prop:due<=7"))

    info = invoke("cardsInfo", cards=kort)
    noter = invoke("notesInfo", notes=list({c["note"] for c in info}))
    ord_per_not, register_brist = {}, set()
    for n in noter:
        ra = n["fields"].get(config.FIELD_ORD, {}).get("value", "")
        ord_per_not[n["noteId"]] = re.sub(r"<[^>]+>", "", ra).strip()
        try:
            parsed = baksida.parse(
                n["fields"].get(config.FIELD_BAKSIDA, {}).get("value", ""))
            if baksida.validate_register(parsed.get("register")):
                register_brist.add(n["noteId"])
        except Exception:
            register_brist.add(n["noteId"])

    rader = []
    for c in info:
        cid = c["cardId"]
        skal, risk = [], 0
        for namn, _u, vikt in RISK:
            if cid in traffar[namn]:
                risk += vikt
                skal.append(namn)
        if c["note"] in register_brist:
            risk += REGISTER_POANG
            skal.append("ogiltigt register")
        exp = exponering(c["interval"], c["lapses"], cid in snart_set)
        rader.append({
            "cardId": cid, "noteId": c["note"],
            "ord": ord_per_not.get(c["note"], "?"),
            "poang": risk + exp, "risk": risk, "exp": exp,
            "ivl": c["interval"], "lapses": c["lapses"], "reps": c["reps"],
            "due_snart": cid in snart_set, "skal": skal,
        })

    rader.sort(key=lambda r: (-r["poang"], -r["lapses"], r["ivl"]))

    with open(UTFIL_JSON, "w", encoding="utf-8") as f:
        json.dump(rader, f, ensure_ascii=False, indent=1)

    fordelning = Counter()
    for r in rader:
        for s in r["skal"]:
            fordelning[s] += 1

    with open(UTFIL_MD, "w", encoding="utf-8") as f:
        f.write("# Provisoriska is:review-kort, rankade för full v3\n\n")
        f.write(f"{len(rader)} kort. Genererad av `v3_urgency_provisorisk.py`.\n\n")
        f.write("## Riskskäl, fördelning\n\n| Skäl | Kort |\n|---|---|\n")
        for s, n in fordelning.most_common():
            f.write(f"| {s} | {n} |\n")
        f.write("\n## Topp 100\n\n")
        f.write("| # | Ord | Poäng | Risk | Exp | Ivl | Lapses | Skäl |\n")
        f.write("|---|---|---|---|---|---|---|---|\n")
        for i, r in enumerate(rader[:100], 1):
            f.write(f"| {i} | {r['ord']} | {r['poang']} | {r['risk']} | "
                    f"{r['exp']} | {r['ivl']} | {r['lapses']} | "
                    f"{', '.join(r['skal'])} |\n")

    print(f"Skrev {UTFIL_JSON} och {UTFIL_MD}.")

    if args.antal:
        topp = rader[:args.antal]
        with open(UTFIL_IDS, "w", encoding="utf-8") as f:
            json.dump(topp, f, ensure_ascii=False, indent=1)
        print(f"Skrev {UTFIL_IDS} med {len(topp)} kort "
              f"(poäng {topp[0]['poang']}–{topp[-1]['poang']}).")


if __name__ == "__main__":
    main()
