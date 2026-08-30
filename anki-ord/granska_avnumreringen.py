# -*- coding: utf-8 -*-
"""Jamfor varje kort som avnumreringen rorde mot Ankis backup fran 17:56.

VARFOR. Efter korningen visade sig kortet `agnat` ha huvudbetydelsen
"Slakting pa fadernesidan, SLAKTING PA MANSSIDAN ; ..." i Anki, medan
backupen fran 17:56 -- alltsa fore korningen -- har den ratta formen
"... ALLTSA VIA MAN ; ...". Notens mod-tid ar 18:17:58, vilket ar nar
avnumrera_synonymer.py korde.

Rundturen parse->build pa exakt det gamla innehallet ger den RATTA formen
nar jag kor den nu, sa orsaken ar inte klarlagd. Men orsaken spelar mindre
roll an omfattningen: det enda tillatna resultatet av en avnumrering ar att
sifferprefixen forsvinner. ALLT annat ar en skada.

Skriptet ar rent lasande och listar varje kort dar backupen och Anki
skiljer sig i nagot MER an sifferprefixen.
"""
import io
import json
import re
import sqlite3
import zipfile

import baksida
import config
from ankiconnect import invoke

BACKUP = (r"C:\Users\Adam\AppData\Local\Temp\claude"
          r"\c--Obsidian-Study-Coach-Ai\43ac5a98-66b6-483c-aa0b-4534e753849c"
          r"\scratchpad\col1756.anki2")
NUMMER = re.compile(r"(^|;\s*)\d+\.\s")


def synonymrad(html):
    m = baksida._MAIN_RE.search(html or "")
    return m.group("syn") if m else None


def avnumrera(html):
    """Tar bort sifferprefixen ur SYNONYMRADEN och ror inget annat."""
    m = baksida._MAIN_RE.search(html or "")
    if not m:
        return html
    rad = m.group("syn")
    ren = NUMMER.sub(lambda x: x.group(1), rad)
    return html[:m.start("syn")] + ren + html[m.end("syn"):]


def main():
    c = sqlite3.connect(BACKUP)
    gamla = {}
    for nid, flds in c.execute("select id, flds from notes"):
        delar = flds.split(chr(31))
        if len(delar) < 2:
            continue
        rad = synonymrad(delar[1])
        if rad and NUMMER.search(rad):
            gamla[nid] = (delar[0], delar[1])
    print("kort med numrerad synonymrad i backupen 17:56: %d" % len(gamla))

    nids = list(gamla)
    skadade, rena, saknas = [], 0, 0
    for i in range(0, len(nids), 500):
        for n in invoke("notesInfo", notes=nids[i:i + 500]):
            if not n:
                saknas += 1
                continue
            nu = (n["fields"].get(config.FIELD_BAKSIDA) or {}).get("value", "")
            fram, gammal = gamla[n["noteId"]]
            vantad = avnumrera(gammal)
            if nu == vantad:
                rena += 1
            else:
                skadade.append((n["noteId"],
                                re.sub("<[^>]+>", "", fram).strip(),
                                vantad, nu))

    print("oforandrade utover numreringen : %d" % rena)
    print("SKILJER SIG PA ANNAT SATT      : %d" % len(skadade))
    for nid, ord_, vantad, nu in skadade:
        pv = baksida.parse(vantad)
        pn = baksida.parse(nu)
        print("\n  %s  (nid %s)" % (ord_, nid))
        for falt in ("huvudbetydelse", "register", "exempelmening", "etymologi"):
            if (pv.get(falt) or "") != (pn.get(falt) or ""):
                print("    %-14s FORE : %s" % (falt, pv.get(falt)))
                print("    %-14s NU   : %s" % ("", pn.get(falt)))
        if pv["synonymer"] != pn["synonymer"]:
            print("    synonymer      FORE : %s" % pv["synonymer"])
            print("                   NU   : %s" % pn["synonymer"])

    json.dump([{"noteId": n, "ord": o, "aterstall": v}
               for n, o, v, _ in skadade],
              io.open("skadade_avnumrering.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("\nskrev skadade_avnumrering.json (%d poster)" % len(skadade))


main()
