# -*- coding: utf-8 -*-
"""Synonymbatch 08 -- 24 kort.

FALLA -- drap: synonymer.se listar "mord" bland synonymerna, men kortets
EGEN text sager att drap "skiljer sig fran mord". Att satta mord dar hade
raderat den enda distinktion kortet finns for. Samma sort som tertial/
kvartal. Vald: mandrap.

arbitrage far ingen synonym: kallan ger bara "valutahandel", vilket ar EN
sorts arbitrage, inte ordet.
"""
import fyll_synonymer

VAL = {
    # --- akta synonymer ---
    "kola vippen":       "dö",
    "gans":              "kantband, prydnadssnöre",
    "paroxysm":          "krampanfall, känsloutbrott",
    "favör":             "fördel, förmån ; ynnestbevis",
    "aladåb":            "gelérätt, aspic",
    "martyr":            "blodsvittne, trosvittne",
    "dråp":              "mandråp",
    "latta":             "träribba, läkt",
    "indisponerad":      "opasslig, ur form",
    "florstunn":         "skir, genomskinlig",
    "göra avkall på":    "avstå",

    # --- narmaste ord, inte utbyte ---
    "skillingtryck":     "≈ ballad",
    "epigram":           "≈ satir",
    "kronvittne":        "≈ angivare",
    "panegyrisk":        "≈ lovprisande",
    "amfiteater":        "≈ arena",

    # --- ingen synonym i nagon av de tre kallorna ---
    "envar blir salig på sin tro/fason": None,
    "det drar ihop sig": None,
    "arbitrage":         None,   # "valutahandel" ar EN sorts arbitrage
    "extramural":        None,
    "faktori":           None,
    "pulpa":             None,   # anatomisk term
    "parnass":           None,   # kallan ger den grekiska grundbetydelsen
    "cinnober":          None,   # mineral- och fargnamn
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
