# -*- coding: utf-8 -*-
"""Fyller synonymraden pa kort som saknar den (2026-08-29).

Adams prioritering: "det viktigaste ar att fa in synonymer pa alla kort som
inte har det". Faltets syfte ar ORD-traning -- det vanligaste ordet som
ligger NARMAST i betydelse, inte nodvandigtvis ett exakt utbyte
(style_guide.md, andrat 2026-08-29).

MARKNING, beslutad av Adam samma dag:
  inget tecken  = akta synonym, utbytbart          -> tag synonym::akta
  "≈" framfor   = narmaste ordet som finns          -> tag synonym::narmaste
  tom rad       = ingen synonym i nagon av tre kallor -> tag synonym::saknas

Tecknet lagras i sjalva synonymstrangen ("≈ bila"), sa parse/build tar det
utan ny mekanism -- till skillnad fran numren och registerfargen, som maste
skalas av och pa vid varje rundtur. Verifierat att validate_adamtal godkanner
tecknet (0 harda, 0 mjuka fel).

" ; " skiljer BETYDELSER at (position 1 = betydelse 1), ", " skiljer flera
ord inom samma betydelse. Samma konvention som resten av decket.
"""
import io
import json
import sys
import urllib.request

import baksida

DECK = 'deck:"Humanities::Languages::Svenska 10 000"'


def call(a, **p):
    r = urllib.request.urlopen(
        "http://127.0.0.1:8765",
        json.dumps({"action": a, "version": 6, "params": p}).encode(),
        timeout=120)
    d = json.loads(r.read().decode())
    if d.get("error"):
        raise SystemExit("ANKI-FEL: %s" % d["error"])
    return d["result"]


def fyll(val, torrkorning=False):
    """val: {ord: synonymsträng | None}. None = synonym::saknas."""
    poster = json.load(io.open("sessions/synonymfyllning_alla.json",
                               encoding="utf-8"))
    by = {p["ord"]: p for p in poster}
    gjorda = saknas = missade = 0
    backup = {}
    for o, syn in val.items():
        p = by.get(o)
        if not p:
            print("  SAKNAS I KON: %s" % o)
            missade += 1
            continue
        nid = p["noteId"]
        n = call("notesInfo", notes=[nid])[0]
        gammal = n["fields"]["Baksida"]["value"]
        backup[str(nid)] = gammal
        if syn is None:
            if not torrkorning:
                call("addTags", notes=[nid], tags="synonym::saknas")
            saknas += 1
            print("  %-18s (ingen synonym i nagon kalla)" % o)
            continue
        m = baksida.parse(gammal)
        grupper = [[s.strip() for s in g.split(",")] for g in syn.split(" ; ")]
        ny = baksida.build(m["huvudbetydelse"], synonym_groups=grupper,
                           exempelmening=m["exempelmening"],
                           register=m["register"], bild_html=m["bild_html"],
                           etymologi=m["etymologi"])
        k = baksida.parse(ny)
        for falt in ("huvudbetydelse", "register", "exempelmening",
                     "etymologi", "bild_html"):
            if k[falt] != m[falt]:
                raise SystemExit("RUNDTUR BROT pa %s: %s" % (o, falt))
        if not torrkorning:
            call("updateNoteFields",
                 note={"id": nid, "fields": {"Baksida": ny}})
            tagg = "synonym::narmaste" if "≈" in syn else "synonym::akta"
            call("addTags", notes=[nid], tags=tagg)
        gjorda += 1
        print("  %-18s %s" % (o, syn))
    if backup and not torrkorning:
        fil = "backup_synonymer_%s.json" % sys.argv[1] if len(sys.argv) > 1 \
            else "backup_synonymer.json"
        gammalt = {}
        try:
            gammalt = json.load(io.open(fil, encoding="utf-8"))
        except Exception:
            pass
        gammalt.update(backup)
        json.dump(gammalt, io.open(fil, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
    print("\nifyllda: %d   utan synonym: %d   ej i kon: %d"
          % (gjorda, saknas, missade))
