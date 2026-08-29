# -*- coding: utf-8 -*-
"""Konverterar kort med >=3 betydelser till numrerad layout (2026-08-29).

Adams beslut: "kanske battre om alla kort som har 3 huvudbetydelser
anvander nummrerade huvudbetydelse listor? exempelvis krackelera forvirrar
nar det blir 2 rader."

krackelera: 3 betydelser, 163 tecken fetstil, 79 &nbsp;. Fetstilsraden
bryts till tva rader medan registerraden bryts pa annat stalle, sa
justeringen pekar pa en position som inte finns kvar.

Rorer INTE innehallet -- bara renderingen. Backup av all gammal HTML
skrivs till backup_numrerad_<datum>.json fore forsta skrivning.
"""
import io
import json
import re
import urllib.request

import baksida

DECK = 'deck:"Humanities::Languages::Svenska 10 000"'
BACKUP = "backup_numrerad_2026-08-29.json"


def call(a, **p):
    r = urllib.request.urlopen(
        "http://127.0.0.1:8765",
        json.dumps({"action": a, "version": 6, "params": p}).encode(),
        timeout=180)
    d = json.loads(r.read().decode())
    if d.get("error"):
        raise SystemExit("ANKI-FEL: %s" % d["error"])
    return d["result"]


nids = call("findNotes", query=DECK + " tag:kortformat::v2")
notes = call("notesInfo", notes=nids)

kandidater = []
for n in notes:
    b = n["fields"]["Baksida"]["value"]
    m = re.match(r"<b>(.*?)</b>", b, re.S)
    if not m:
        continue
    if len(m.group(1).split(" ; ")) >= baksida.NUMRERAD_FRAN:
        kandidater.append(n)

print("kort med >=%d betydelser: %d" % (baksida.NUMRERAD_FRAN, len(kandidater)))

backup = {str(n["noteId"]): n["fields"]["Baksida"]["value"] for n in kandidater}
json.dump(backup, io.open(BACKUP, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("backup skriven: %s (%d kort)\n" % (BACKUP, len(backup)))

gjorda = hoppade = 0
avvikelser = []
for n in kandidater:
    gammal = n["fields"]["Baksida"]["value"]
    p = baksida.parse(gammal)
    if not p["huvudbetydelse"]:
        hoppade += 1
        avvikelser.append((n["fields"]["Framsida"]["value"], "gick ej att parsa"))
        continue
    ny = baksida.build(p["huvudbetydelse"], synonymer=p["synonymer"],
                       exempelmening=p["exempelmening"], register=p["register"],
                       bild_html=p["bild_html"],
                       synonym_groups=p["synonym_groups"],
                       etymologi=p["etymologi"])
    if "&nbsp;" in ny:
        # Foll tillbaka pa gamla vagen -- antalet register matchar inte
        # antalet betydelser, och da vet vi inte vilket hor till vilket.
        hoppade += 1
        avvikelser.append((n["fields"]["Framsida"]["value"],
                           "register/betydelser i otakt"))
        continue
    k = baksida.parse(ny)
    for falt in ("register", "exempelmening", "etymologi", "bild_html"):
        if k[falt] != p[falt]:
            raise SystemExit("RUNDTUR BROT pa %s: %s" %
                             (n["fields"]["Framsida"]["value"], falt))
    call("updateNoteFields",
         note={"id": n["noteId"], "fields": {"Baksida": ny}})
    gjorda += 1

print("konverterade : %d" % gjorda)
print("hoppade over : %d" % hoppade)
for o, skal in avvikelser:
    print("   %-20s %s" % (o, skal))
