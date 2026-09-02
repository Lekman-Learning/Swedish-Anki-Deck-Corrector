# -*- coding: utf-8 -*-
"""Skriver ut vilka synonymer forgranska.py faktiskt GODTAR for varje ord.

Byggd pa forgranskas egna funktioner, inte pa en kopia av reglerna -- annars
kan verktyget och kontrollen glida isar. Mott 2026-09-02: forsta batchen om 18
kort fick synonym_utan_ordboksbelagg pa 13 av 18 eftersom synonymerna togs fran
synonymer.se, som INTE ar ordboksbelagg. Bara SO:s SYN-falt och SO/SAOL:s
definitionstext raknas. Tom lista ar godkant och ar normalfallet (69 %).

Skriver ocksa antalet SO-betydelser, eftersom betydelse_kan_saknas ar ett hart
fel som kraver antingen fler betydelser pa kortet eller en skriven motivering
i forgranska_tillat.
"""
import argparse, io, json, os, sys
import forgranska as F

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def visa(o):
    f = os.path.join("uppslag", o + ".json")
    if not os.path.exists(f):
        print("==== %s   UPPSLAG SAKNAS" % o)
        return
    u = json.load(io.open(f, encoding="utf-8"))
    print("==== %s" % o)

    n_def = len(F._so(u, "def"))
    n_ub = len(F._riktiga_underbetydelser(u))
    print("   SO-betydelser: %d def + %d riktiga underbetydelser = %d"
          % (n_def, n_ub, n_def + n_ub))
    for d in F._so(u, "def"):
        print("      def:", d)
    for d in F._riktiga_underbetydelser(u):
        print("      ub :", d)

    belagg = F._ordboksbelagg(u, o)
    if isinstance(belagg, (set, frozenset, list, tuple)):
        rad = sorted(str(x) for x in belagg)
        print("   GODTAGNA SYNONYMER (%d): %s" % (len(rad), ", ".join(rad) or "-- INGA --"))
    else:
        print("   belagg (ratyp %s): %r" % (type(belagg).__name__, belagg))
    print()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("ord", nargs="*")
    p.add_argument("--fil")
    p.add_argument("--fran", type=int, default=0)
    p.add_argument("--antal", type=int, default=10)
    a = p.parse_args()
    orden = a.ord
    if a.fil:
        poster = json.load(io.open(a.fil, encoding="utf-8"))
        orden = [e["ord"] for e in poster][a.fran:a.fran + a.antal]
    for o in orden:
        visa(o)
