# -*- coding: utf-8 -*-
"""Kompakt granskningsunderlag: kortet, facit, SO/SAOL och riskflaggorna sida vid sida.

Finns for att v3-granskningen annars kraver att man laser tre stora JSON-filer
per kort. Kontextfonstret -- inte kvoten -- ar taket (matt 2026-08-09), sa det
som avgor hur manga kort som ryms i ett pass ar hur tatt underlaget ar.

    python v3_underlag.py sessions/<fil>.json --fran 0 --antal 10
"""
import argparse
import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HAR = os.path.dirname(os.path.abspath(__file__))


def _ren(s, n=None):
    s = re.sub(r"<[^>]+>", "", str(s or ""))
    s = " ".join(s.split())
    return s[:n] + "..." if n and len(s) > n else s


def _uppslag(ord_):
    """slaupp.py skriver EN fil per ord: uppslag/<ord>.json."""
    f = os.path.join(HAR, "uppslag", ord_ + ".json")
    if not os.path.exists(f):
        return None
    try:
        return json.load(open(f, encoding="utf-8"))
    except Exception:
        return None


def _so_betydelser(u):
    """Sammandraget forst; annars fritextsokning i hela uppslaget.

    Formen pa svenska.se:s svar varierar mellan SO/SAOL/SAOB, sa en strikt
    nyckelvag skulle tappa tysta trafffar. Hellre trubbigt och komplett an
    exakt och tomt -- underlaget ska visa VAD som hamtades, inte tolka det.
    """
    if not u:
        return []
    s = u.get("sammandrag") or {}
    sv = (s.get("svenska_se") or {}) if isinstance(s, dict) else {}
    ut = []
    for kalla in ("so", "saol"):
        d = sv.get(kalla) or {}
        if not isinstance(d, dict):
            continue
        rader = []
        if d.get("def"):
            rader.append(" | ".join(d["def"]))
        # Underbetydelser ar dar de SAKNADE betydelserna gommer sig -- det
        # dominerande felet i decket. De far darfor aldrig kapas bort har.
        for ub in (d.get("underbetydelser") or []):
            rader.append("  ub: " + (ub if isinstance(ub, str) else str(ub)))
        if d.get("märkning"):
            rader.append("  märkn: " + " ".join(map(str, d["märkning"])))
        if d.get("exempel"):
            rader.append("  ex: " + " / ".join(map(str, d["exempel"][:2])))
        if rader:
            ut.append("%-5s %s" % (kalla.upper(), rader[0]))
            ut += ["      " + r for r in rader[1:]]
    syn = ((s.get("synonymer_se") or {}).get("avdelningar") or {}) if isinstance(s, dict) else {}
    for namn in ("synonymer", "motsatsord"):
        if syn.get(namn):
            ut.append("SYN.SE %s: %s" % (namn, ", ".join(map(str, syn[namn][:8]))))
    return ut


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fil")
    ap.add_argument("--fran", type=int, default=0)
    ap.add_argument("--antal", type=int, default=10)
    a = ap.parse_args()

    d = json.load(open(a.fil, encoding="utf-8"))
    kort = d["kort"] if isinstance(d, dict) and "kort" in d else d

    for e in kort[a.fran:a.fran + a.antal]:
        print("=" * 78)
        print("%-22s  noteId=%s  prio=%s" % (e["ord"].upper(), e["noteId"], e.get("prio")))
        nu = e.get("nuvarande_format") or {}
        if isinstance(nu, dict) and nu:
            print("  NU  bet : %s" % _ren(nu.get("huvudbetydelse"), 220))
            print("      reg : %s   syn: %s" % (_ren(nu.get("register")),
                                                _ren(nu.get("synonymer"), 90)))
            print("      ex  : %s" % _ren(nu.get("exempelmening"), 130))
            if nu.get("etymologi"):
                print("      etym: %s" % _ren(nu.get("etymologi"), 130))
        else:
            print("  NU  legacy: %s" % _ren(e.get("legacy"), 260))
        print("  FACIT: %s" % _ren(e.get("old_facit"), 240))
        rf = e.get("riskflaggor") or []
        if rf:
            namn = [r.get("namn", r) if isinstance(r, dict) else r for r in rf]
            print("  RISK : %s" % _ren(", ".join(str(r.get('flagga',r)) if isinstance(r,dict) else str(r) for r in rf), 120))
        for b in _so_betydelser(_uppslag(e["ord"])):
            print("  ORDB : %s" % _ren(b, 300))
    print("=" * 78)
    print("visade %d-%d av %d" % (a.fran, min(a.fran + a.antal, len(kort)), len(kort)))


if __name__ == "__main__":
    main()
