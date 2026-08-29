# -*- coding: utf-8 -*-
"""Synonymbatch 11 -- 25 kort.

MOTSATSORD uteslutna: "osolidarisk/illojal" (solidarisk), "sot" (pomerans --
kortet sager uttryckligen SUR och besk). Nionde och tionde fallet.
"""
import fyll_synonymer

VAL = {
    # --- akta synonymer ---
    "gnatig":         "grinig, tjatig",
    "beredvillig":    "tjänstvillig, hjälpsam",
    "umbärande":      "försakelse, armod",
    "väsensskild":    "artskild",
    "vurm":           "mani, dille",
    "karda":          "handkarda",
    "bemyndiga":      "befullmäktiga, auktorisera",
    "guttural":       "sträv, grötig",
    "lamell":         "platta, blad",
    "skrupler":       "samvetsbetänkligheter, betänkligheter",
    "berlock":        "hängsmycke, medaljong",
    "solidarisk":     "lojal, kamratlig",
    "gillestuga":     "sällskapsrum, mysrum",
    "parlör":         "fraslexikon, samtalsordbok",
    "oförmedlad":     "abrupt, plötslig",
    "sejdel":         "ölmugg, stop",
    "fullödig":       "gedigen, ypperlig",

    # --- narmaste ord, inte utbyte ---
    "helioterapi":    "≈ solbad",

    # --- ingen synonym i nagon av de tre kallorna ---
    "tabulatur":      None,   # notskriftsform
    "kainsmärke":     None,
    "gördla":         None,
    "långledas":      None,
    "riksha (rickshaw)": None,
    "i onåd":         None,
    "pomerans":       None,   # kallan ger "sot", vilket ar MOTSATSEN
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
