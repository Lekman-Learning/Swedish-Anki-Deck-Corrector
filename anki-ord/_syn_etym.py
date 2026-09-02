# -*- coding: utf-8 -*-
"""Skriver ut synonymer.se-avdelningarna och etymologin ur uppslag/<ord>.json.

Komplement till visa_uppslag.py, som visar SO/SAOL-definitionerna men varken
synonymkandidater eller etymologi. Lasar bara cache -- inget nat.
"""
import argparse, io, json, os, re, sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def ren(t):
    if not t: return ""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", str(t))).strip()

def visa(o):
    f = os.path.join("uppslag", o + ".json")
    if not os.path.exists(f):
        print("==== %s   UPPSLAG SAKNAS" % o); return
    d = json.load(io.open(f, encoding="utf-8"))
    print("==== %s" % o)
    samm = d.get("sammandrag") or {}
    syn = samm.get("synonymer_se") or {}
    avd = syn.get("avdelningar") if isinstance(syn, dict) else None
    if not avd and isinstance(syn, dict):
        avd = {k: v for k, v in syn.items() if isinstance(v, list)}
    if avd:
        for rubrik, lista in avd.items():
            print("   SYN(%s): %s" % (rubrik, ", ".join(ren(x) for x in lista[:14])))
    else:
        raw = json.dumps(syn, ensure_ascii=False)[:300]
        if len(raw) > 4: print("   SYN-RA:", raw)
    # etymologi: SO forst, sedan SAOB, sedan Wiktionary
    ratt = d.get("svenska_se_ratt") or {}
    for kod in ("so", "saol", "saob"):
        for h in (ratt.get(kod) or {}).get("hits", {}).get("hits", [])[:2]:
            s = h["_source"]
            for hb in s.get("huvudbetydelser", []):
                for e in (hb.get("etymologi") or []):
                    print("   ETYM(%s): %s" % (kod, ren(e.get("text") if isinstance(e, dict) else e)))
            for e in (s.get("etymologi") or []):
                print("   ETYM(%s): %s" % (kod, ren(e.get("text") if isinstance(e, dict) else e)))
    w = samm.get("wiktionary") or {}
    if isinstance(w, dict) and w.get("etymologi"):
        print("   ETYM(wikt):", ren(w["etymologi"])[:260])
    print()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("ord", nargs="*")
    p.add_argument("--fil"); p.add_argument("--fran", type=int, default=0)
    p.add_argument("--antal", type=int, default=10)
    a = p.parse_args()
    orden = a.ord
    if a.fil:
        poster = json.load(io.open(a.fil, encoding="utf-8"))
        orden = [e["ord"] for e in poster][a.fran:a.fran + a.antal]
    for o in orden: visa(o)
