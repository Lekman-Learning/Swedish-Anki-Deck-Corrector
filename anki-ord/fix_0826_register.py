# -*- coding: utf-8 -*-
"""Normaliserar register mot baksida.validate_adamtal:s axeltilldelning.

Regeln (baksida.py, 2026-08-10):
  entydig tagg  -> sin egen axel
  tvetydig tagg (neutral/oklart) -> forsta ANNU LEDIGA axeln: stilniva -> valor -> doman
  stilniva OCH valor kravs; max en per axel; doman valfri.

'neutral, neutral' ar alltsa RATT svar for ett vanligt ord utan laddning.
"""
import json, config

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))

FORM = list(config.REGISTER_FORMALITY)
VAL = list(config.REGISTER_VALENS)
DOM = list(config.REGISTER_DOMAN)
AXLAR = [("stilnivå", FORM), ("valör", VAL), ("domän", DOM)]

# Kort dar jag valt TVA taggar pa samma axel -- kraver ett beslut, inte en autofix.
BESLUT = {
    "långledas": "ngt ålderdomlig, neutral",        # dialektal stryks: SO ger bada, ngt ald. ar bredare
    "obstruktion": "ngt ålderdomlig, neutral",      # formell stryks: SO:s markning ar alderdomlighet
    "talja": "fackspråklig, neutral, sjöfart",      # ngt ald. stryks: markningen gallde verbformen
    "avlat": "formell, neutral, religion",          # historia stryks: religion ar det narmare facket
    "knekt": "ngt ålderdomlig, nedsättande",        # historia stryks, domanen ar inte obligatorisk
    "häckla": "ngt ålderdomlig, neutral",           # historia stryks av samma skal
}

andrade = 0
for e in S:
    p = e.get("proposed")
    if not p:
        continue
    o = e["ord"]
    if o in BESLUT:
        p["register"] = BESLUT[o]
        andrade += 1
        continue
    tags = [t.strip() for t in (p.get("register") or "").split(",") if t.strip()]
    upptagen = {}
    tvetydiga = []
    ok = True
    for t in tags:
        traffar = [n for n, v in AXLAR if t in v]
        if len(traffar) == 1:
            if traffar[0] in upptagen:
                ok = False          # dubblett pa samma axel
            upptagen[traffar[0]] = t
        elif len(traffar) > 1:
            tvetydiga.append(t)
        else:
            ok = False              # okand tagg
    for t in tvetydiga:
        ledig = next((n for n, _ in AXLAR if n not in upptagen), None)
        if ledig:
            upptagen[ledig] = t
        else:
            ok = False
    saknas = [a for a in ("stilnivå", "valör") if a not in upptagen]
    if saknas and ok:
        # fyll de saknade obligatoriska axlarna med neutral, i ratt ordning
        ny = list(tags)
        for _ in saknas:
            ny.append("neutral")
        # sortera sa att stilniva kommer forst, sedan valor, sedan doman
        p["register"] = ", ".join(ny)
        andrade += 1
    elif not ok:
        print("KRAVER BESLUT:", o, "->", p["register"])

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Normaliserade %d register." % andrade)

# verifiera direkt mot valideraren
import baksida
fel = 0
for e in S:
    p = e.get("proposed")
    if not p:
        continue
    w = baksida.validate_adamtal(p["huvudbetydelse"], p.get("synonymer") or [],
                                 p.get("exempelmening") or "", p["register"]) \
        if hasattr(baksida, "validate_adamtal") else []
    reg = [x for x in (w or []) if "register" in str(x) or "axel" in str(x)
           or "stilnivå" in str(x) or "valör" in str(x)]
    if reg:
        fel += 1
        print("  KVAR:", e["ord"], reg[:1])
print("Kort med kvarvarande registerfel:", fel)
