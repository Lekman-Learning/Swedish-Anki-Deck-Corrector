# -*- coding: utf-8 -*-
"""Stader synonymer som forgranska.py flaggar som obelagda -- men inte blint.

BAKGRUND. forgranska.py:s regel `synonym_utan_ordboksbelagg` godtar bara tva
belagg: SO:s SYN:synonym-markor, eller att ordet star i SO/SAOL:s
definitionstext. Den ar alltsa STRANGARE an den policy jag skrev batcherna
efter, som ocksa godtog synonymer.se:s redaktionella lista. Regeln ar
projektets standard och vinner.

MEN den har tva kanda blinda flackar som skulle ge falska tomma kort:

  1. Den laser inte Wiktionary alls, trots att Wiktionary ar en av de tre
     kallor slaupp.py hamtar och en av dem `trekallskontrollen` raknar.
  2. Den matchar exakt, sa ett ord som star BOJT i definitionen missas
     ('konsdriften' i SO:s definition av sexualitet ar belagg for
     'konsdrift').

Skriptet stryker darfor en flaggad synonym bara om den saknas aven i
Wiktionarys definitioner OCH inte gar att hitta som stam i SO/SAOL:s
definitionstext. Det som stryks skrivs ut, och kort som blir HELT utan
synonym listas separat -- det ar de som stoter i `tom_synonymgrupp` och
kraver Adams beslut.
"""
import io
import json
import re
import sys

SES = "sessions/session_2026-08-30_v3-omgranskning-repetition-mognad.json"
FG = "fg.json"


def stam(w):
    w = (w or "").lower().strip()
    for suf in ("ande", "ende", "arna", "erna", "orna", "aren", "ade", "are",
                "ell", "en", "et", "er", "or", "ar", "an", "a", "s"):
        if len(w) - len(suf) >= 4 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def kalltext(ord_):
    """All definitionstext for ordet, gemener, fran alla tre kallorna."""
    try:
        u = json.load(io.open("uppslag/%s.json" % ord_, encoding="utf-8"))
    except IOError:
        return "", ""
    sam = u.get("sammandrag") or {}
    sv = sam.get("svenska_se") or {}
    bitar = []
    for k in ("saol", "so"):
        blk = sv.get(k) or {}
        for f in ("def", "underbetydelser", "märkning"):
            bitar += [str(x) for x in (blk.get(f) or [])]
    wik = (sam.get("wiktionary") or {}).get("definitioner") or []
    return " ".join(bitar).lower(), " ".join(str(x) for x in wik).lower()


def main():
    torr = "--kor" not in sys.argv
    d = json.load(io.open(SES, encoding="utf-8"))
    fg = json.load(io.open(FG, encoding="utf-8"))
    flaggade = {}
    for p in fg:
        for a in p["fel"]:
            if a["regel"] != "synonym_utan_ordboksbelagg":
                continue
            ord_ = a["detalj"].split(" -- ")[0]
            flaggade.setdefault(p["ord"], []).extend(
                [s.strip() for s in ord_.split(",")])

    struket, behallet, tomma = [], [], []
    for p in d:
        o = p["ord"]
        if o not in flaggade or not p.get("proposed"):
            continue
        so_saol, wikt = kalltext(o)
        grupper = p["proposed"]["synonym_groups"] or []
        nya = []
        for g in grupper:
            ng = []
            for s in g:
                if s not in flaggade[o]:
                    ng.append(s)
                    continue
                st = stam(s)
                if s.lower() in wikt or (len(st) >= 4 and st in so_saol):
                    behallet.append((o, s,
                                     "wiktionary" if s.lower() in wikt else "böjd i SO/SAOL"))
                    ng.append(s)
                else:
                    struket.append((o, s))
            nya.append(ng)
        if not torr:
            p["proposed"]["synonym_groups"] = nya
            p["proposed"]["synonymer"] = [s for g in nya for s in g]
        if not any(nya):
            tomma.append(o)

    print("STRUKNA (inget belagg i SO/SAOL/Wiktionary): %d" % len(struket))
    for o, s in struket:
        print("   %-24s %s" % (o, s))
    print()
    print("BEHÅLLNA trots flagga: %d" % len(behallet))
    for o, s, varfor in behallet:
        print("   %-24s %-22s %s" % (o, s, varfor))
    print()
    print("KORT SOM BLIR HELT UTAN SYNONYM: %d" % len(tomma))
    for o in tomma:
        print("   %s" % o)
    if not torr:
        json.dump(d, io.open(SES, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("\nSKRIVET till sessionsfilen.")
    else:
        print("\n(torrkörning -- kör med --kor för att skriva)")


main()
