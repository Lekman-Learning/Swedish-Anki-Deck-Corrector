# -*- coding: utf-8 -*-
"""Kompakt granskningsunderlag: nuvarande kort + ordbokskallor sida vid sida.

Finns for att v3 pa spar B ar en JAMFORELSE, inte en nyskrivning -- kortet
finns redan och fragan ar om det stammer. Att lasa sessionsfilen och
uppslag/ var for sig gor den jamforelsen i huvudet, vilket ar precis dar
kohyponymfelet 2026-08-30 uppstod.

JFR skrivs alltid ut, aven tomt: SO markerar kohyponymer dar, och en synonym
som i sjalva verket ar en kohyponym ar den vanligaste felkallan i decket.
"""
import io
import json
import os
import sys

SES = "sessions/session_2026-08-30_v3-omgranskning-repetition-mognad.json"


def kort(x, n=150):
    s = " | ".join(x) if isinstance(x, list) else str(x or "")
    return s[:n] + ("..." if len(s) > n else "")


def main():
    fran = int(sys.argv[1]); till = int(sys.argv[2])
    d = json.load(io.open(SES, encoding="utf-8"))
    for i, p in enumerate(d[fran:till], start=fran):
        o = p["ord"]; L = p.get("legacy") or {}
        print("=" * 70)
        print("[%d] %s   (old_facit: %s)" % (i, o, p.get("old_facit")))
        print("  NU hb   : %s" % kort(L.get("huvudbetydelse")))
        print("  NU reg  : %s" % kort(L.get("register")))
        print("  NU syn  : %s" % kort(L.get("synonymer")))
        print("  NU ex   : %s" % kort(L.get("exempelmening")))
        print("  NU etym : %s" % kort(L.get("etymologi")))
        for f in p.get("riskflaggor") or []:
            print("  FLAGGA  : %s (%s)" % (f["flagga"], f["allvar"]))
        sv = "uppslag/%s.json" % o
        if not os.path.exists(sv):
            print("  !! INGEN UPPSLAGNING")
            continue
        u = json.load(io.open(sv, encoding="utf-8"))
        print("  traffar : %s" % u.get("uppslagsordstraffar"))
        sam = u.get("sammandrag") or {}
        for kalla in ("saol", "so"):
            blk = (sam.get("svenska_se") or {}).get(kalla) or {}
            if not blk:
                continue
            print("  %-5s def: %s" % (kalla.upper(), kort(blk.get("def"))))
            for f in ("underbetydelser", "jfr", "märkning", "etymologi"):
                if blk.get(f):
                    print("  %-5s %-4s: %s" % (kalla.upper(), f[:4], kort(blk[f])))
        syn = (sam.get("synonymer_se") or {})
        if syn:
            print("  SYN.SE  : %s" % kort(((syn.get("avdelningar") or {}).get("synonymer") or []), 170))
        wik = (sam.get("wiktionary") or {})
        if wik:
            print("  WIKT    : %s" % kort((wik.get("definitioner") or []), 170))


main()
