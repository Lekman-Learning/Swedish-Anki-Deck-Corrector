# -*- coding: utf-8 -*-
"""Kallunderlag for arbetsbatchen: allt som behovs for att skriva ETT kort.

Slar ihop det _pool.py ger (SO-betydelser + de synonymer forgranska godtar)
med kortets NUVARANDE innehall och riskflaggor, eftersom spar B inte handlar
om att skriva fran noll utan om att avgora OM kortet behover andras.

Skrivs till fil i stallet for att skrivas ut styckevis: 100 kort ska lasas i
omgangar, och en fil gar att lasa om utan att kalla pa ordbockerna igen.
"""
import io, json, os, sys
import forgranska as F

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = sys.argv[1] if len(sys.argv) > 1 else "sessions/session_2026-09-02b_v3-batch.json"
UT = sys.argv[2] if len(sys.argv) > 2 else "_underlag_0902b.txt"

poster = json.load(io.open(FIL, encoding="utf-8"))
rader = []
for i, e in enumerate(poster):
    o = e["ord"]
    rader.append("=" * 70)
    rader.append("[%d] %s" % (i, o))
    f = os.path.join("uppslag", o + ".json")
    if os.path.exists(f):
        u = json.load(io.open(f, encoding="utf-8"))
        for d in F._so(u, "def"):
            rader.append("   SO def : %s" % d)
        for d in F._riktiga_underbetydelser(u):
            rader.append("   SO ub  : %s" % d)
        b = F._ordboksbelagg(u, o)
        if isinstance(b, (set, frozenset, list, tuple)):
            rader.append("   GODTAGNA SYN (%d): %s"
                         % (len(b), ", ".join(sorted(str(x) for x in b)) or "-- INGA --"))
        sam = (u.get("sammandrag") or {})
        saol = sam.get("saol") or sam.get("SAOL")
        if saol:
            rader.append("   SAOL    : %s" % json.dumps(saol, ensure_ascii=False)[:400])
    else:
        rader.append("   UPPSLAG SAKNAS")

    lg = e.get("legacy") or {}
    rader.append("   NU hb   : %s" % lg.get("huvudbetydelse"))
    rader.append("   NU reg  : %s" % lg.get("register"))
    rader.append("   NU syn  : %s" % lg.get("synonymer"))
    rader.append("   NU ex   : %s" % lg.get("exempelmening"))
    rader.append("   NU etym : %s" % lg.get("etymologi"))
    rader.append("   OLD     : %s" % e.get("old_facit"))
    for r in (e.get("riskflaggor") or []):
        rader.append("   FLAGGA %s/%s: %s"
                     % (r.get("flagga"), r.get("allvar"), r.get("forklaring")))

io.open(UT, "w", encoding="utf-8").write("\n".join(rader))
print("Skrev underlag for %d kort till %s (%d rader)"
      % (len(poster), UT, len(rader)))
