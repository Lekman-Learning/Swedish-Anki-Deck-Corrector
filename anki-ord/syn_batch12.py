# -*- coding: utf-8 -*-
"""Synonymbatch 12 -- 25 kort.

MOTSATSORD uteslutna: "kurant" (inkurant -- raka motsatsen, och listat
FORST i kallans lista), "klar/ljus" (rosslig), "missnojd/anspraksfull"
(fornojsam).
"""
import fyll_synonymer

VAL = {
    "ympa":            "okulera ; vaccinera",
    "butelj":          "flaska",
    "avlat":           "syndaförlåtelse, indulgens",
    "inkurant":        "osäljbar, trögsåld",
    "bolma":           "ryka ; blossa",
    "överhalning":     "krängning ; översyn ; utskällning",
    "guano":           "fågelspillning",
    "bjäbb":           "käbbel, gläfs",
    "rosslig":         "hes, skrovlig",
    "boudoir":         "damrum, gemak",
    "tusenkonstnär":   "mångsysslare, mångfrestare",
    "synnerlig":       "särskild, utpräglad",
    "vederlag":        "ersättning, gottgörelse ; anfang",
    "pur":             "ren, oblandad",
    "omaka":           "oparig, udda ; göra sig omak",
    "ataxi":           "koordinationsrubbning",
    "förnöjsam":       "anspråkslös, förnöjd",
    "sekvestrera":     "beslagta, konfiskera",

    "berått":          "≈ avsiktligt",
    "mammon":          "≈ jordisk rikedom",
    "terrakotta":      "≈ lergods",

    "a la carte":      None,
    "i stadens hank och stör": None,
    "kalejdoskop":     None,   # "tittskap" ar en annan sak
    "krabb":           None,   # sjofartsterm om vagor
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
