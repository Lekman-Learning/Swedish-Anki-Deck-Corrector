# -*- coding: utf-8 -*-
"""Kompakt forskningsdump for de 80 valda orden -- lases direkt ur den
redan hamtade uppslag/-cachen (ingen natverkstrafik). Formatet speglar
slaupp.py --kompakt men filtrerat till bara var batch, plus kortets
NUVARANDE innehall och OLD-facit sida vid sida for snabb jamforelse.
"""
import json
import re

SESSION = "sessions/session_2026-08-21_v3-omgranskning.json"


def strip(s):
    return re.sub(r"<[^>]+>", " ", s or "").replace("&nbsp;", " ").strip()


def load_cache(ord_):
    safe = re.sub(r'[\\/:*?"<>|]', "_", ord_)
    try:
        with open(f"uppslag/{safe}.json", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def main():
    poster = json.load(open(SESSION, encoding="utf-8"))
    out = []
    for i, p in enumerate(poster):
        ord_ = p["ord"]
        legacy = p["legacy"]
        old = strip(p.get("old_facit") or "")
        cache = load_cache(ord_)
        out.append(f"\n{'='*80}\n[{i}] {ord_}   (risk: {p['hogsta_allvar']})")
        out.append(f"  NUVARANDE HB : {legacy.get('huvudbetydelse')}")
        out.append(f"  NUVARANDE SYN: {legacy.get('synonymer')}")
        out.append(f"  NUVARANDE REG: {legacy.get('register')}")
        out.append(f"  NUVARANDE EX : {strip(legacy.get('exempelmening'))}")
        out.append(f"  NUVARANDE ETY: {legacy.get('etymologi')}")
        out.append(f"  OLD-FACIT    : {old[:200]}")
        if not cache:
            out.append("  UPPSLAG: SAKNAS I CACHE")
            continue
        sam = (cache.get("sammandrag") or {}).get("svenska_se") or {}
        for kalla in ("so", "saol", "saob"):
            k = sam.get(kalla) or {}
            if not any(k.values()):
                continue
            out.append(f"  {kalla.upper()}:")
            if k.get("def"):
                out.append(f"    def : {' | '.join(k['def'])}")
            if k.get("underbetydelser"):
                out.append(f"    UB  : {' | '.join(k['underbetydelser'])}")
            if k.get("märkning"):
                out.append(f"    mark: {' | '.join(k['märkning'])}")
            if k.get("exempel"):
                out.append(f"    ex  : {' | '.join(k['exempel'][:3])}")
            if k.get("jfr"):
                out.append(f"    jfr : {', '.join(k['jfr'])}")
            if k.get("etymologi"):
                out.append(f"    ety : {' | '.join(k['etymologi'])}")
        synse = ((cache.get("sammandrag") or {}).get("synonymer_se") or {}).get("avdelningar") or {}
        for rubrik, lista in synse.items():
            out.append(f"  SYN.SE({rubrik}): {', '.join(lista[:12])}")
        wikt = (cache.get("sammandrag") or {}).get("wiktionary") or {}
        if wikt.get("definitioner"):
            out.append(f"  WIKT: {' | '.join(wikt['definitioner'][:3])}")
        if wikt.get("etymologi"):
            out.append(f"  WIKT ETYM: {str(wikt['etymologi'])[:150]}")

    with open("sessions/scratchpad_dump80.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"Skrev sessions/scratchpad_dump80.txt ({len(out)} rader)")


if __name__ == "__main__":
    main()
