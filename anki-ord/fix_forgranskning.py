# -*- coding: utf-8 -*-
"""Rattar forgranska.py:s ovriga anmarkningar pa 100-kortsomgangen 2026-08-30.

Tre saker, alla entydiga:

 1. `doman_utan_stod` (21 st) -- jag satte domantaggar (sjofart, ekonomi,
    juridik ...) pa ord som varken SO eller SAOL markerar som fackord och som
    dessutom ar vanliga i sprakbruket. En domantagg som inte star i kallan ar
    min tolkning, inte ett faktum, och den styr hur Adam laser kortet. Bort.
    De domaner som HAR stod (atrofi/medicin, respons/psykologi) ar inte
    flaggade och rors inte.

 2. `uppslagsord_saknas` -- carpe diem har noll traffar i bade SO och SAOL.
    Samma harda regel som pausade hippopotamus, echappera och passiar. Pausas.

 3. `register_motsager_markning` -- 'se tiden an': kallan markerar 'nagot
    alderdomligt', kortet sa 'formell'. Kallan vinner.

`synonym_saknas_trots_belagg` pa mycel/prisma/mitos/gaa-tretton lamnas som
det ar: kandidaterna verktyget foreslar ur definitionstexten ar
'mycelium' (samma ord), 'kongruenta basytor', 'delning' och 'avlida' --
ingen av dem ar en utbytbar synonym. Korten ar redan pausade av just det
skalet.
"""
import io
import json
import re

SES = "sessions/session_2026-08-30_v3-omgranskning-repetition-mognad.json"
FG = "fg.json"


def main():
    d = json.load(io.open(SES, encoding="utf-8"))
    fg = json.load(io.open(FG, encoding="utf-8"))

    bort = {}
    for p in fg:
        for a in p["fel"]:
            if a["regel"] != "doman_utan_stod":
                continue
            m = re.search(r"domän '([^']+)'", a["detalj"])
            if m:
                bort.setdefault(p["ord"], set()).add(m.group(1))

    n_dom = 0
    for p in d:
        o = p["ord"]
        v = p.get("proposed")
        if not v:
            continue

        if o in bort and v.get("register"):
            nya = []
            for del_ in v["register"].split(";"):
                kvar = [t.strip() for t in del_.split(",")
                        if t.strip() not in bort[o]]
                nya.append(", ".join(kvar))
            ny = " ; ".join(nya)
            if ny != v["register"]:
                v["register"] = ny
                n_dom += 1

        if o == "se tiden an":
            v["register"] = "ngt ålderdomlig, neutral"
            p["sokkoll"]["slutsats"] += (
                " REGISTER RÄTTAT efter förgranskningen: SO/SAOL märker ordet "
                "'något ålderdomligt'; kortet sa 'formell'. Källan vinner.")

        if o == "carpe diem":
            p["approved"] = False
            p["pausad"] = True
            p["paus_tagg"] = "v3_pausad::inget_uppslagsord_i_so_saol"
            p["sokkoll"]["slutsats"] += (
                " PAUSAT: förgranskningens hårda regel uppslagsord_saknas slog "
                "till -- 0 träffar i både SO och SAOL. Exakt den varning som "
                "stod i kortets egen sökkollsnotis när det skrevs. Samma "
                "behandling som hippopotamus, echappera och passiar fick. "
                "Betydelsen är belagd i Wiktionary och synonymer.se, så kortet "
                "är förmodligen riktigt -- men det uppfyller inte v3:s krav på "
                "ordbokstäckning, och det kravet är inte mitt att göra "
                "undantag från.")

    json.dump(d, io.open(SES, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("kort med borttagen domäntagg : %d" % n_dom)
    print("carpe diem pausat, se tiden an omregistrerat")


main()
