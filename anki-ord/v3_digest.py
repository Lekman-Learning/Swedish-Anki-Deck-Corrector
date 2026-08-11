# -*- coding: utf-8 -*-
"""Kompakt sammandrag ur redan hämtade uppslag/ — en rad per fält, inget fett.

## Varför filen finns

`slaupp.py --kompakt` skriver ~700 tecken per ord: fulla synonymlistor, fyra
språkprov, alla JFR-hänvisningar. Bra när man läser tio ord. Vid 250 kort på en
dag blir det ohanterligt att läsa igenom, och den som skummar missar saker —
vilket är precis hur `bruklighetskommentar` kunde vara osynligt i månader.

Den här filen läser SAMMA sparade svar i `uppslag/` och skriver ~200 tecken per
ord: de fält som faktiskt avgör hur kortet ska se ut.

    SO      betydelserna, numrerade — det som avgör om en betydelse saknas
    SO+     "äv. …"-utvidgningarna, där de saknade betydelserna brukar gömma sig
    SAOL    andra källans formulering
    BRUK    SO:s bruklighetskommentar — avgör REGISTRET. Se slaupp.py.
    SYN     synonymer.se, max 8 — underlaget för synonymfältet
    ETYM    etymologin, kapad

Ingen hämtning sker här. Filen läser bara disk, så den kan köras hur många
gånger som helst utan att röra svenska.se — och den kan därför INTE användas
som sökkollsbevis. Beviset är `slaupp.py`-körningen i transkriptet.

    python v3_digest.py sessions/<ordlista>.json
    python v3_digest.py ord1 ord2 ...
"""
import glob
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HAR = os.path.dirname(os.path.abspath(__file__))
UPPSLAG = os.path.join(HAR, "uppslag")


def _txt(v):
    if isinstance(v, str):
        return re.sub(r"<[^>]+>", "", v).strip()
    if isinstance(v, list):
        return " | ".join(x for x in (_txt(i) for i in v) if x)
    return ""


def _plocka(nod, nycklar, tak=99):
    ut = []

    def ga(n):
        if isinstance(n, dict):
            for k, v in n.items():
                if k in nycklar:
                    t = _txt(v)
                    if t and t not in ut:
                        ut.append(t)
                ga(v)
        elif isinstance(n, list):
            for v in n:
                ga(v)
    ga(nod)
    return ut[:tak]


def _kallor(data, bok):
    traffar = (((data or {}).get(bok) or {}).get("hits") or {}).get("hits") or []
    return [t.get("_source", {}) for t in traffar[:2]]


def sammandrag(ord_):
    f = os.path.join(UPPSLAG, ord_.replace(" ", "_") + ".json")
    if not os.path.exists(f):
        traff = glob.glob(os.path.join(UPPSLAG, "%s*.json" % ord_.split()[0]))
        f = traff[0] if traff else None
    if not f:
        return "### %-22s  [INGEN SPARAD UPPSLAGNING]" % ord_

    d = json.load(open(f, encoding="utf-8"))
    # RÅDATAN, inte det cachade sammandraget. Filerna innehåller båda, men
    # `sammandrag` skrevs av den slaupp.py som gällde när ordet slogs upp --
    # och fram till 2026-08-10 hade den ett TOMT `märkning`-fält, eftersom
    # `bruklighetskommentar` aldrig plockades ut. Ett äldre sammandrag ser
    # alltså komplett ut men saknar just den uppgift som avgör registret.
    # Rådatan är oförändrad och har den. Läs därifrån.
    sv = d.get("svenska_se_ratt") or d.get("svenska_se") or d
    so, saol = _kallor(sv, "so"), _kallor(sv, "saol")
    syn = ((d.get("sammandrag") or {}).get("synonymer_se")) or {}

    rader = ["### %s" % ord_]

    def lagg(etikett, varden, tak=None):
        v = [x for x in varden if x]
        if not v:
            return
        text = " | ".join(v)
        if tak and len(text) > tak:
            text = text[:tak] + " […]"
        rader.append("  %-5s %s" % (etikett, text))

    lagg("SO", _plocka(so, {"definition", "definition_full", "def",
                            "huvudbetydelse", "betydelse"}, 6), 400)
    lagg("SO+", _plocka(so, {"typ"}, 6), 260)
    lagg("SAOL", _plocka(saol, {"definition", "def", "huvudbetydelse"}, 4), 220)
    # BRUK ligger sist i koden men FÖRST i huvudet när registret sätts.
    lagg("BRUK", _plocka(so + saol, {"bruklighetskommentar", "stilmarkering",
                                     "bruklighet", "markering"}, 4))
    s = []
    for avd in (syn.get("avdelningar") or {}).values():
        for x in (avd if isinstance(avd, list) else [avd]):
            t = _txt(x)
            if t:
                s += [y.strip() for y in t.split(",")]
    lagg("SYN", [", ".join(dict.fromkeys(x for x in s if x)[:8]
                           if False else list(dict.fromkeys(s))[:8])], 200)
    lagg("ETYM", _plocka(so, {"etymologi"}, 2), 170)
    return "\n".join(rader)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    a = sys.argv[1]
    if a.endswith(".json") and os.path.exists(a):
        ord_ = json.load(open(a, encoding="utf-8"))
        if isinstance(ord_, dict):
            ord_ = ord_.get("ord") or list(ord_)
        # Sessionsfilerna från kortbyggare.py är listor av POSTER, inte av ord.
        # Samma normalisering finns i slaupp.py. Utan den kraschar filen på
        # 'dict' object has no attribute 'replace' -- ett fel som pekar på
        # strängoperationen, inte på att filformatet var ett annat än väntat.
        ord_ = [p.get("ord") if isinstance(p, dict) else p for p in ord_]
    else:
        ord_ = sys.argv[1:]
    for o in ord_:
        print(sammandrag(o))
    return 0


if __name__ == "__main__":
    sys.exit(main())
