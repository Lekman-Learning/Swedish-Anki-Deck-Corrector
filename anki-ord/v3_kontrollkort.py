"""Blandar in redan godkända kort som DOLDA KONTROLLER i varje blint paket.

Adams fråga 2026-08-11: *"kan vi implementera blint_stickprov.py i våran blind
granskning inom full v3?"* Svaret är ja, och det blir bättre än det separata
skriptet på tre sätt.

## Vad blint_stickprov.py gör i dag, och vad som är fel med det

Det drar 10 slumpmässiga redan släppta kort en gång i veckan och startar en
EGEN granskarsession för dem. Två problem:

1. **Det är ett separat kommando**, och v3:s egen historia visar vad som
   händer med sådana: blindgranskningen var ett separat manuellt steg och
   `oberoende_verifierad` stod på 3 av 10 034 kort. Ett steg som måste
   startas för hand blir inte startat.
2. **Granskaren vet att det är ett stickprov.** Hela paketet består av gamla
   kort. Det mäter inte samma sak som en vanlig körning: en granskare som vet
   att den letar fel letar annorlunda än en som tror den gör dagens batch.

## Vad det här gör i stället

Varje blint paket får `--antal` extra poster som är **redan godkända kort**,
minst `--alder` dagar gamla, blandade in bland de nya. De ser exakt likadana
ut som resten -- ingen markering, ingen ordning som avslöjar dem. Facit ligger
i en SIDOFIL som granskaren aldrig får se.

Det ger tre saker gratis:

* **Kontinuerlig mätning.** Varje paket producerar en felfrekvens på kända
  kort, i stället för en siffra i veckan. Vid 300 kort/dag och 10 % kontroller
  blir det ~30 mätpunkter om dagen mot 10 i veckan.
* **Granskardrift upptäcks.** Om en granskare börjar stämpla igenom allt syns
  det direkt: kontroller som tidigare underkändes börjar godkännas. Det går
  inte att se i en vanlig körning, där varje kort bara döms en gång någonsin.
* **Ingen extra granskarsession.** Kontrollerna åker med i paket som ändå
  körs, alltså noll extra kostnad utöver de få posterna.

## Vad det INTE mäter

Kontrollerna är kort som REDAN godkänts av en tidigare granskare. Att en ny
granskare godkänner dem igen betyder "de två är överens", inte "kortet är
rätt" -- två granskare kan ha samma blinda fläck. Det som mäts är alltså
**samstämmighet över tid**, vilket är ett golv för kvalitet, inte ett bevis.
`blint_stickprov.py` har exakt samma begränsning; skillnaden är takten.

    python v3_kontrollkort.py blanda sessions/<paket>.json --antal 3
    python v3_kontrollkort.py sammanstall sessions/<paket>.json
"""

import argparse
import datetime
import glob
import json
import os
import random
import sys

import config
from ankiconnect import invoke

# Facit läggs bredvid paketet, inte i det. Att lagra svaret i samma fil som
# granskaren läser vore inte en blind granskning, hur väl gömt fältet än är.
FACIT_SUFFIX = ".kontrollfacit.json"
MATLOGG = "kontrollmatningar.jsonl"


def _facitvag(paket):
    return paket[:-5] + FACIT_SUFFIX if paket.endswith(".json") else paket + FACIT_SUFFIX


def valj_kontroller(antal, alder_dagar, undvik_nids, fro=None):
    """Redan blindgodkända kort som är minst `alder_dagar` gamla.

    Åldern är inte kosmetisk: ett kort som godkändes i dag av samma granskare
    mäter bara att den är konsekvent med sig själv inom en session. Samma
    resonemang som blint_stickprov.py:s `--alder`.
    """
    granss = (datetime.date.today() - datetime.timedelta(days=alder_dagar)).isoformat()
    nids = invoke("findNotes", query=(
        f'deck:"{config.DECK_NAME}" tag:{config.OBEROENDE_TAG_PREFIX}::*'))
    kandidater = []
    for n in invoke("notesInfo", notes=nids):
        if n["noteId"] in undvik_nids:
            continue
        datum = [t.split("::", 1)[1] for t in n["tags"]
                 if t.startswith(f"{config.OBEROENDE_TAG_PREFIX}::") and "::" in t]
        if datum and max(datum) <= granss:
            kandidater.append(n)
    if fro is not None:
        random.seed(fro)
    random.shuffle(kandidater)
    return kandidater[:antal]


def blanda(paket, antal, alder, fro):
    with open(paket, encoding="utf-8") as f:
        data = json.load(f)
    poster = data["poster"] if isinstance(data, dict) else data

    facitvag = _facitvag(paket)
    if os.path.exists(facitvag):
        sys.exit(f"AVBRYTER: {facitvag} finns redan — paketet är nog redan blandat. "
                 "Att blanda två gånger ger kontroller som räknas dubbelt.")

    befintliga = {p.get("noteId") for p in poster}
    kontroller = valj_kontroller(antal, alder, befintliga, fro)
    if len(kontroller) < antal:
        print(f"VARNING: bara {len(kontroller)} av {antal} kandidater fanns "
              f"(kort äldre än {alder} dagar med {config.OBEROENDE_TAG_PREFIX}).")

    # Kontrollposten måste vara OSKILJAKTIG från en vanlig post.
    #
    # Första versionen satte fältet `kort_html` och utelämnade `facit`. Ett
    # testkörning visade att kontrollerna då gick att peka ut på fältnamnen
    # ensamt -- riktiga poster hade `facit`/`kort`/`verdikt`/`anmarkning`,
    # kontrollerna hade `kort_html`. Granskaren hade sett exakt vilka tre som
    # var kontroller utan att läsa ett enda ord, och mätningen hade varit värd
    # noll medan den såg ut att fungera.
    #
    # Posten byggs därför med kortbyggare.bygg_post(), alltså samma funktion
    # som skapar de riktiga posterna. Att härma formatet för hand vore att
    # skapa en andra definition av vad en post är, och de två skulle glida
    # isär vid nästa formatändring.
    # OBS: paketets postformat är INTE sessionsfilens. Sessionsfilen (från
    # kortbyggare.bygg_post) har `legacy`/`old_facit`/`riskflaggor`; paketet
    # har `facit`/`kort`/`verdikt`. Ett första försök återanvände bygg_post
    # och gav kontroller med bara `noteId` och `ord` -- fortfarande
    # utpekbara. Posten byggs därför mot paketformatet, härlett ur en RIKTIG
    # post i samma fil i stället för ur en hårdkodad fältlista, så den följer
    # med om formatet ändras.
    import baksida
    from snabbkoll2 import build_old_lookup
    old_lookup = build_old_lookup()
    faltnamn = list(poster[0]) if poster else [
        "noteId", "ord", "facit", "kort", "verdikt", "anmarkning"]

    nya = []
    for n in kontroller:
        ord_ = n["fields"].get(config.FIELD_ORD, {}).get("value", "")
        rå = n["fields"].get(config.FIELD_BAKSIDA, {}).get("value", "")
        try:
            kort = baksida.parse(rå)
        except Exception:
            continue
        varden = {
            "noteId": n["noteId"],
            "ord": ord_,
            "facit": old_lookup.get(ord_.strip().lower()),
            "facit_signal": None,
            "kort": kort,
            "verdikt": None,
            "anmarkning": None,
        }
        nya.append({k: varden.get(k) for k in faltnamn})

    alla = poster + nya
    random.shuffle(alla)   # kontrollerna får inte ligga sist
    if isinstance(data, dict):
        data["poster"] = alla
    else:
        data = alla
    with open(paket, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with open(facitvag, "w", encoding="utf-8") as f:
        json.dump({"skapad": datetime.datetime.now().isoformat(timespec="seconds"),
                   "paket": os.path.basename(paket), "alder_dagar": alder,
                   "kontroller": [{"noteId": n["noteId"],
                                   "ord": n["fields"].get(config.FIELD_ORD, {}).get("value", ""),
                                   "tidigare": "godkand"} for n in kontroller]},
                  f, ensure_ascii=False, indent=1)

    print(f"Blandade in {len(nya)} kontroller bland {len(poster)} riktiga poster.")
    print(f"Facit: {facitvag}  — den filen får granskaren ALDRIG se.")


def sammanstall(paket):
    facitvag = _facitvag(paket)
    if not os.path.exists(facitvag):
        sys.exit(f"Hittar inget facit ({facitvag}). Blandades paketet någonsin?")
    facit = json.load(open(facitvag, encoding="utf-8"))

    # Verdikten hamnar i DELARNA, inte i originalet: dela_paket.py lämnar
    # ursprungsfilen orörd som facit på vad batchen bestod av. Att bara läsa
    # originalet gav "inga kontroller är dömda än" trots att granskningen var
    # klar -- ett svar som såg ut som ett tomt resultat i stället för som en
    # fil som lästes på fel ställe.
    stam = paket[:-5] if paket.endswith(".json") else paket
    filer = sorted(glob.glob(f"{stam}-del*.json")) or [paket]
    dom = {}
    for f in filer:
        data = json.load(open(f, encoding="utf-8"))
        for p in (data["poster"] if isinstance(data, dict) else data):
            if p.get("verdikt"):
                dom[p.get("noteId")] = (p.get("verdikt"), p.get("anmarkning"))
    print(f"Läste verdikt ur {len(filer)} fil(er): "
          f"{', '.join(os.path.basename(f) for f in filer)}")

    rader, odomda = [], 0
    for k in facit["kontroller"]:
        v, anm = dom.get(k["noteId"], (None, None))
        if v is None:
            odomda += 1
            continue
        rader.append((k["ord"], v, anm))

    if not rader:
        sys.exit("Inga kontroller är dömda än — kör blindgranskningen först.")

    underkanda = [r for r in rader if r[1] != "godkand"]
    kvot = len(underkanda) / len(rader)
    print(f"\nKONTROLLER I {os.path.basename(paket)}")
    print(f"  dömda            : {len(rader)}" + (f"  (odömda: {odomda})" if odomda else ""))
    print(f"  underkända       : {len(underkanda)}")
    print(f"  AVVIKELSEKVOT    : {kvot:.0%}")
    print("\n  Korten var godkända av en TIDIGARE granskare. En underkänd "
          "kontroll betyder\n  att de två granskarna är oense — inte "
          "automatiskt att kortet är fel.")
    for o, v, anm in underkanda:
        print(f"    - {o}: {(anm or '')[:90]}")

    with open(MATLOGG, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "tid": datetime.datetime.now().isoformat(timespec="seconds"),
            "paket": os.path.basename(paket), "domda": len(rader),
            "underkanda": len(underkanda), "kvot": round(kvot, 4),
            "ord": [r[0] for r in underkanda],
        }, ensure_ascii=False) + "\n")
    print(f"\n  Loggat till {MATLOGG} — det är där trenden över tid syns.")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("blanda")
    b.add_argument("paket")
    b.add_argument("--antal", type=int, default=3)
    b.add_argument("--alder", type=int, default=3,
                   help="kontroller måste vara minst så här många dagar gamla")
    b.add_argument("--fro", type=int, default=None)
    s = sub.add_parser("sammanstall")
    s.add_argument("paket")
    a = ap.parse_args()

    if a.cmd == "blanda":
        blanda(a.paket, a.antal, a.alder, a.fro)
    else:
        sammanstall(a.paket)


if __name__ == "__main__":
    main()
