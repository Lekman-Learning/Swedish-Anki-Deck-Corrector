# -*- coding: utf-8 -*-
"""Synonymbatch 10 -- 50 kort.

MOTSATSORD uteslutna: "urban" (pastoral), "barnslig/omogen" (bradmogen).
"""
import fyll_synonymer

VAL = {
    # --- akta synonymer ---
    "ligga i träda":     "ligga nere",
    "advokatyr":         "lagvrängning, sofistik",
    "faktur":            "ytstruktur",
    "disös":             "recitatris, chansonett",
    "ekolod":            "sonar",
    "kanapé":            "smördegsbakelse ; sandwich ; soffa",
    "biton":             "underton, anstrykning",
    "transumera":        "excerpera",
    "atrium":            "förgård ; hjärtförmak",
    "pastoral":          "idyllisk, lantlig ; prästerlig ; herdedikt",
    "axiomatisk":        "självklar, obestridlig",
    "libation":          "drickoffer ; dryckesgille",
    "desavouera":        "förkasta, ogilla",
    "mo":                "sandhed, tallhed",
    "kamarilla":         "kotteri, klick",
    "lealös":            "slapp, hållningslös",
    "kohandel":          "köpslående, schackrande",
    "kapson":            "nosgrimma",
    "ånyo":              "åter, återigen",
    "orakel":            "gudomssvar, spådom ; ofelbar rådgivare",
    "ömma":              "värka, smärta",
    "bigotteri":         "skenhelighet, skrymteri",
    "geriatri":          "geriatrik",
    "alltiallo":         "faktotum, mångsysslare",
    "brådmogen":         "lillgammal, försigkommen",
    "föranstalta":       "anordna, sörja för",
    "omse":              "sköta om, vårda",
    "girland":           "blomsterranka, festong",
    "inventarium":       "förteckning ; trotjänare",
    "kredensa":          "avsmaka",
    "isomorf":           "likformig, kongruent",
    "talja":             "taljblock, tackel",
    "uppvigla":          "uppegga, agitera",
    "knekt":             "fotsoldat",
    "foglig":            "medgörlig, eftergiven",
    "doktrin":           "lära, lärosats",
    "högrest":           "reslig, välväxt",

    # --- narmaste ord, inte utbyte ---
    "med berått mod":    "≈ kallblodigt",
    "ketch":             "≈ galeas",
    "disputation":       "≈ lärdomsprov",
    "chaussé":           "≈ huvudväg",
    "adagio":            "≈ långsamt",

    # --- ingen synonym i nagon av de tre kallorna ---
    "absid":             None,   # kallan upprepar definitionen
    "cirkumflex":        None,   # tecknets namn
    "över hövan":        None,   # kallan upprepar definitionen
    "gemination":        None,   # sprakvetenskaplig term
    "fortis":            None,   # fonetisk term
    "encefalografi":     None,   # medicinsk undersokningsmetod
    "epilering":         None,
    "pomologi":          None,   # vetenskapsgren, eget namn
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
