"""kortfakta.py -- skriver ut ENBART sammandraget ur uppslag/<ord>.json.

Bakgrund (2026-09-20): tanken var att låta en lokal modell (Qwen via LM Studio)
komprimera uppslagsfilerna innan Opus läser dem, för att spara kvot. Mätningen
visade att komprimeringen redan finns: `slaupp.py` skriver nyckeln `sammandrag`,
som är 7,6 gånger mindre än hela filen (median 943 mot 7 144 tecken, mätt på 300
filer). Ingen modell behövs alltså för steget -- bara att läsa rätt nyckel.

    python kortfakta.py abakus aber          # ett eller flera ord
    python kortfakta.py --fil batch50.json   # alla ord i en byggfil
    python kortfakta.py --matt               # mät besparingen på hela cachen

Fälten är ordagranna ur SO/SAOL/synonymer.se/Wiktionary. Inget skrivs om.
"""
import argparse
import json
import os
import re
import statistics
import sys

HAR = os.path.dirname(os.path.abspath(__file__))
UPPSLAG = os.path.join(HAR, "uppslag")
OTILLATNA = re.compile(r'[\\/:*?"<>|]')


def sokvag(ord_):
    return os.path.join(UPPSLAG, OTILLATNA.sub("_", ord_) + ".json")


def sammandrag(ord_):
    """Returnerar (sammandrag, hela_filens_storlek) eller (None, 0)."""
    f = sokvag(ord_)
    if not os.path.exists(f):
        return None, 0
    ra = open(f, encoding="utf-8").read()
    u = json.loads(ra)
    d = {
        "ord": u.get("ord", ord_),
        "uppslagsform": u.get("uppslagsform"),
        "verifieringsgrund": u.get("verifieringsgrund"),
        "sammandrag": u.get("sammandrag", {}),
    }
    return d, len(ra)


def ord_ur_fil(fil):
    d = json.load(open(fil, encoding="utf-8"))
    poster = d["poster"] if isinstance(d, dict) and "poster" in d else d
    if isinstance(poster, list) and poster and isinstance(poster[0], dict):
        return [p.get("ord") for p in poster if p.get("ord")]
    return [x for x in poster if isinstance(x, str)]


def matt():
    filer = [f for f in os.listdir(UPPSLAG) if f.endswith(".json")]
    hel, kort, utan = [], [], 0
    for f in filer:
        ra = open(os.path.join(UPPSLAG, f), encoding="utf-8").read()
        s = json.loads(ra).get("sammandrag")
        if not s:
            utan += 1
            continue
        hel.append(len(ra))
        kort.append(len(json.dumps(s, ensure_ascii=False)))
    if not hel:
        print("inga uppslag med sammandrag")
        return
    mh, mk = statistics.median(hel), statistics.median(kort)
    print(f"filer                 {len(filer)}  (utan sammandrag: {utan})")
    print(f"hel fil, median       {int(mh)} tecken  (~{int(mh/3.5)} tokens)")
    print(f"sammandrag, median    {int(mk)} tecken  (~{int(mk/3.5)} tokens)")
    print(f"kvot                  {mh/mk:.1f}x mindre att mata in")
    print(f"summa hel/sammandrag  {sum(hel)/1e6:.1f} MB / {sum(kort)/1e6:.1f} MB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ord", nargs="*")
    ap.add_argument("--fil", help="byggfil (JSON) att ta orden ur")
    ap.add_argument("--matt", action="store_true", help="mät besparingen")
    a = ap.parse_args()

    if a.matt:
        return matt()

    orden = list(a.ord) + (ord_ur_fil(a.fil) if a.fil else [])
    if not orden:
        ap.error("ange ord eller --fil")

    ut, saknas, sparat = [], [], 0
    for o in orden:
        d, hel = sammandrag(o)
        if d is None:
            saknas.append(o)
            continue
        ut.append(d)
        sparat += hel - len(json.dumps(d, ensure_ascii=False))
    print(json.dumps(ut, ensure_ascii=False, indent=1))
    if saknas:
        print(f"\n# saknar uppslag ({len(saknas)}): {', '.join(saknas)}", file=sys.stderr)
    print(f"# {len(ut)} ord, {sparat} tecken mindre än att läsa hela filerna", file=sys.stderr)


if __name__ == "__main__":
    main()
