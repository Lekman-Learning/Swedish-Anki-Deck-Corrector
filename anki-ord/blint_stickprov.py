"""Blint stickprov -- mäter felfrekvensen i redan släppta kort.

Det här är den enda delen av v3 som mäter om resten fungerar. Allt annat
kontrollerar enskilda kort; det här kontrollerar PROCESSEN, genom att dra
ett slumpmässigt urval ur kort som släpptes för flera dagar sedan och
låta en fristående granskare döma dem utan att veta något om hur de
skrevs.

style_guide.md efterlyste precis detta och specificerade även varför det
måste vara FÖRDRÖJT: "gör periodiska BLINDA stickprov senare (kort
granskade dagar/veckor tidigare, omgranskade fristående)". Ett stickprov
i samma sittning mäter bara att granskaren är konsekvent med sig själv.

Utan det här skriptet är "kortet är verifierat" ett påstående utan
mätning bakom sig. Med det får varje vecka en siffra.

    python blint_stickprov.py                  # 10 kort, minst 3 dagar gamla
    python blint_stickprov.py --antal 20 --alder 7
    python blint_stickprov.py --sammanstall sessions/..._stickprov.json
"""

import argparse
import datetime
import json
import os
import random

import baksida
import config
from ankiconnect import invoke
from kortgranskare import VERIFIERARINSTRUKTION
from snabbkoll2 import build_old_lookup


def valj(antal, alder_dagar, fro):
    """Kort som släppts (ej suspenderade, oberoende_verifierade) och vars
    dagsbatch är minst `alder_dagar` gammal."""
    granss = datetime.date.today() - datetime.timedelta(days=alder_dagar)
    nids = invoke("findNotes", query=(
        f'deck:"{config.DECK_NAME}" -is:suspended '
        f'tag:{config.OBEROENDE_TAG_PREFIX}::*'
    ))
    if not nids:
        return []
    info = []
    for i in range(0, len(nids), 2000):
        info.extend(invoke("notesInfo", notes=nids[i:i + 2000]))
    passande = []
    for n in info:
        datum = None
        for t in n.get("tags", []):
            if t.startswith(f"{config.DAGSBATCH_TAG_PREFIX}::"):
                try:
                    datum = datetime.date.fromisoformat(t.split("::", 1)[1])
                except ValueError:
                    pass
        if datum is None or datum <= granss:
            passande.append(n)
    random.seed(fro)
    return random.sample(passande, min(antal, len(passande)))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--antal", type=int, default=10)
    p.add_argument("--alder", type=int, default=3, help="minsta ålder i dagar")
    p.add_argument("--fro", type=int, default=None, help="slumpfrö (utelämna = slumpmässigt)")
    p.add_argument("--sammanstall", help="läs en ifylld stickprovsfil och räkna ut felfrekvens")
    a = p.parse_args()

    if a.sammanstall:
        with open(a.sammanstall, encoding="utf-8") as f:
            data = json.load(f)
        poster = data["poster"]
        dom = [x for x in poster if x.get("verdikt") in ("godkand", "underkand")]
        if not dom:
            print("Inga verdikt ifyllda än.")
            return
        fel = [x for x in dom if x["verdikt"] == "underkand"]
        andel = len(fel) / len(dom)
        # Rule of three: vid 0 fel av n är övre 95%-gränsen ~3/n.
        ovre = 3 / len(dom) if not fel else None
        print(f"Bedömda: {len(dom)}   Underkända: {len(fel)}   Felfrekvens: {andel:.1%}")
        if ovre:
            print(f"0 fel av {len(dom)} ger en övre 95%-gräns på ca {ovre:.1%} "
                  f"-- inte bevisad nolla, bara ett tak.")
        for x in fel:
            print(f"  UNDERKÄND {x['ord']}: {x.get('anmarkning')}")
        return

    fro = a.fro if a.fro is not None else random.randrange(1_000_000)
    urval = valj(a.antal, a.alder, fro)
    if not urval:
        print(f"Inga släppta kort som är minst {a.alder} dagar gamla än.")
        return

    old = build_old_lookup()
    poster = []
    for n in urval:
        ord_ = n["fields"][config.FIELD_ORD]["value"]
        p_ = baksida.parse(n["fields"][config.FIELD_BAKSIDA]["value"])
        poster.append({
            "noteId": n["noteId"], "ord": ord_,
            "facit": old.get(ord_.strip().lower()),
            "kort": {"huvudbetydelse": p_["huvudbetydelse"], "register": p_["register"],
                     "synonymer": p_["synonymer"], "synonym_groups": p_["synonym_groups"],
                     "exempelmening": p_["exempelmening"]},
            "verdikt": None, "anmarkning": None,
        })

    idag = datetime.date.today().isoformat()
    katalog = os.path.join(os.path.dirname(__file__), "sessions")
    mal = os.path.join(katalog, f"session_{idag}_stickprov.json")
    n_ = 2
    while os.path.exists(mal):
        mal = os.path.join(katalog, f"session_{idag}_stickprov-{n_}.json")
        n_ += 1
    with open(mal, "w", encoding="utf-8") as f:
        json.dump({"instruktion": VERIFIERARINSTRUKTION, "slumpfro": fro,
                   "minsta_alder_dagar": a.alder, "poster": poster}, f,
                  ensure_ascii=False, indent=2)
    print(f"Skrev {len(poster)} slumpvis valda, redan släppta kort till {mal}")
    print(f"Slumpfrö {fro} (sparat i filen, så urvalet går att återskapa).")
    print("Låt en FRISTÅENDE granskare fylla i verdikt, kör sedan --sammanstall.")


if __name__ == "__main__":
    main()
