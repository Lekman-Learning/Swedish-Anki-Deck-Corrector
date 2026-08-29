# -*- coding: utf-8 -*-
"""Numrerar kort med >=3 betydelser men ETT gemensamt register (2026-08-29).

Uppfoljning till konvertera_numrerad.py, som bara tog kort dar antalet
register var LIKA med antalet betydelser (68 st). De 94 som hade tre eller
fler betydelser men ett enda register foll igenom och behöll den enradiga
layouten -- alltsa med kvar precis det problem Adam pekade pa i krackelera:
fetstilsraden bryts till tva rader.

Registret star kvar pa egen rad under stapeln och dubbleras INTE ut per
rad; se kommentaren i baksida.build.
"""
import io
import json
import re
import urllib.request

import baksida

DECK = 'deck:"Humanities::Languages::Svenska 10 000"'
BACKUP = "backup_numrerad2_2026-08-29.json"


def call(a, **p):
    r = urllib.request.urlopen(
        "http://127.0.0.1:8765",
        json.dumps({"action": a, "version": 6, "params": p}).encode(),
        timeout=180)
    d = json.loads(r.read().decode())
    if d.get("error"):
        raise SystemExit("ANKI-FEL: %s" % d["error"])
    return d["result"]


notes = call("notesInfo", notes=call("findNotes", query=DECK + " tag:kortformat::v2"))
kandidater = []
for n in notes:
    b = n["fields"]["Baksida"]["value"]
    if re.search(r"<b>\s*\d+\.\s", b):        # redan numrerat
        continue
    p = baksida.parse(b)
    if not p["huvudbetydelse"] or not p["register"]:
        continue
    if (len(p["huvudbetydelse"].split(" ; ")) >= baksida.NUMRERAD_FRAN
            and len(p["register"].split(" ; ")) == 1):
        kandidater.append((n, p))

print("kandidater: %d" % len(kandidater))
json.dump({str(n["noteId"]): n["fields"]["Baksida"]["value"]
           for n, _ in kandidater},
          io.open(BACKUP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

gjorda = 0
for n, p in kandidater:
    ny = baksida.build(p["huvudbetydelse"], synonymer=p["synonymer"],
                       exempelmening=p["exempelmening"], register=p["register"],
                       bild_html=p["bild_html"],
                       synonym_groups=p["synonym_groups"],
                       etymologi=p["etymologi"])
    k = baksida.parse(ny)
    for falt in ("register", "exempelmening", "etymologi", "bild_html"):
        if k[falt] != p[falt]:
            raise SystemExit("RUNDTUR BROT pa %s: %s\n  fore: %r\n  efter: %r"
                             % (n["fields"]["Framsida"]["value"], falt,
                                p[falt], k[falt]))
    if len(k["huvudbetydelse"].split(" ; ")) != len(p["huvudbetydelse"].split(" ; ")):
        raise SystemExit("BETYDELSEANTAL ANDRAT pa %s"
                         % n["fields"]["Framsida"]["value"])
    call("updateNoteFields", note={"id": n["noteId"], "fields": {"Baksida": ny}})
    gjorda += 1

print("numrerade: %d" % gjorda)
print("backup   : %s" % BACKUP)
