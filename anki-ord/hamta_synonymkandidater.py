# -*- coding: utf-8 -*-
"""Hamtar synonymkandidater for korten som saknar synonym (2026-08-29).

Adams prioritering: "det viktigaste ar att fa in synonymer pa alla kort som
inte har det och efterat losa de formell markta korten."

Skilt fran slaupp.py --fil: det verktyget skriver ut FULLSTANDIG JSON per ord
(flera KB var) och har ett standardtak pa 20 ord. Har behovs bara det som
styr synonymvalet -- betydelser ur SO/SAOL, synonymer.se sektionsvis, och
Wiktionary -- for 909 ord.

BEVISRADERNA SKRIVS UT som vanligt (SVENSKA_SE_HAMTAD ... HTTP 200), eftersom
sokkoll_verifiering.py kraver dem i transkriptet innan korten far skrivas.

RIMLIGHETSKONTROLL: skriptet larmar om synonymer.se-traffkvoten faller under
40 % over ett fonster pa 25 ord. Skalet star i valvet -- kallan var tyst i
~18 dagar utan att nagot markte det, och ETT ord utan synonym ar normalt
medan tjugo i rad ar ett trasigt monster.
"""
import io
import json
import sys
import time

import slaupp

# Utdatafil kan overridas med 4:e argumentet, sa flera strommar kan kora
# parallellt utan att skriva over varandras JSON. Slas ihop efterat.
UT = "sessions/synonymkandidater.json"
LARM_FONSTER = 25
LARM_GRANS = 0.40


def plocka(ord_):
    post = {"ord": ord_}
    sv, sv_status, sv_byte = slaupp.hamta(ord_)
    print("SVENSKA_SE_HAMTAD %s HTTP %s %s" % (ord_, sv_status, sv_byte))
    if sv:
        for kalla in ("so", "saol", "saob"):
            d = (sv.get(kalla) or {})
            if d.get("def"):
                post[kalla] = d["def"]
            if d.get("jfr"):
                post[kalla + "_jfr"] = d["jfr"]

    syn, sy_status, sy_byte = slaupp.hamta_synonymer(ord_)
    print("SYNONYMER_SE_HAMTAD %s HTTP %s %s" % (ord_, sy_status, sy_byte))
    if syn and syn.get("avdelningar"):
        post["synonymer_se"] = {k: v[:12] for k, v in syn["avdelningar"].items()}

    wik, wi_status, wi_byte = slaupp.hamta_wiktionary(ord_)
    print("WIKTIONARY_HAMTAD %s HTTP %s %s" % (ord_, wi_status, wi_byte))
    if wik and wik.get("definitioner"):
        post["wiktionary"] = wik["definitioner"][:6]
    return post


def main():
    ord_lista = json.load(io.open(sys.argv[1], encoding="utf-8"))
    fran = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    antal = int(sys.argv[3]) if len(sys.argv) > 3 else len(ord_lista)
    ord_lista = ord_lista[fran:fran + antal]
    global UT
    if len(sys.argv) > 4:
        UT = sys.argv[4]

    try:
        klara = json.load(io.open(UT, encoding="utf-8"))
    except Exception:
        klara = {}

    fonster = []
    for i, o in enumerate(ord_lista, 1):
        if o in klara:
            continue
        try:
            post = plocka(o)
        except Exception as fel:                      # noqa: BLE001
            post = {"ord": o, "FEL": str(fel)}
        klara[o] = post
        fonster.append(1 if post.get("synonymer_se") else 0)
        if len(fonster) > LARM_FONSTER:
            fonster.pop(0)
        if len(fonster) == LARM_FONSTER:
            kvot = sum(fonster) / float(LARM_FONSTER)
            if kvot < LARM_GRANS:
                print("\n*** LARM: synonymer.se gav traff pa bara %.0f %% av de "
                      "senaste %d orden. Kontrollera parsern INNAN korten "
                      "skrivs -- sa sag det ut nar kallan var tyst. ***\n"
                      % (kvot * 100, LARM_FONSTER))
        if i % 25 == 0:
            json.dump(klara, io.open(UT, "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)
            print("--- %d/%d klara, %d med synonymer.se-traff ---"
                  % (i, len(ord_lista),
                     sum(1 for v in klara.values() if v.get("synonymer_se"))))
        time.sleep(0.4)

    json.dump(klara, io.open(UT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    med = sum(1 for v in klara.values() if v.get("synonymer_se"))
    print("\nKLART: %d ord i %s, varav %d (%.0f %%) har synonymer.se-trafF"
          % (len(klara), UT, med, 100.0 * med / max(1, len(klara))))


if __name__ == "__main__":
    main()
