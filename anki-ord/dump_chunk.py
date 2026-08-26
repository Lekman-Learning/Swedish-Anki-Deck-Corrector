import json,sys
a,b=int(sys.argv[1]),int(sys.argv[2])
S=json.load(open("sessions/session_2026-08-26_v3-batch.json",encoding="utf-8"))
for i,e in enumerate(S):
    if not (a<=i<b): continue
    o=e["ord"]
    try: sm=json.load(open(f"uppslag/{o}.json",encoding="utf-8"))["sammandrag"]
    except Exception as ex: print(f"\n### {i} {o}  UPPSLAG SAKNAS {ex}"); continue
    ss=sm.get("svenska_se") or {}
    print(f"\n### {i} {o}")
    print(f"  OLD: {e.get('old_facit')}")
    lg=e.get("legacy",{})
    print(f"  LEG-def: {lg.get('definitioner')}")
    print(f"  LEG-syn: {lg.get('synonymer')}")
    for k in ("so","saol","saob"):
        d=ss.get(k) or {}
        bits=[]
        if d.get("def"): bits.append(f"def={d['def']}")
        if d.get("märkning"): bits.append(f"mark={d['märkning']}")
        if d.get("underbetydelser"): bits.append(f"under={d['underbetydelser']}")
        if d.get("exempel"): bits.append(f"ex={d['exempel'][:2]}")
        if d.get("etymologi"): bits.append(f"ety={d['etymologi']}")
        if bits: print(f"  {k.upper()}: {' | '.join(bits)}")
    sy=sm.get("synonymer_se") or {}
    if sy.get("finns"): print(f"  SYN.SE: {json.dumps(sy.get('avdelningar'),ensure_ascii=False)[:300]}")
    rf=[f["flagga"] for f in e.get("riskflaggor",[])]
    if rf: print(f"  RISK: {rf}")
