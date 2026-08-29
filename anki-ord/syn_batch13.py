# -*- coding: utf-8 -*-
"""Synonymbatch 13 -- 50 kort.

MOTSATSORD uteslutna: "storhet/betydelsefullhet" (ringhet).

NY FALLTYP -- slanghomonym. `kitt` fick "knark, narkotika, hasch" i samma
lista som "fogmassa, fonsterkitt". Sajten skiljer inte pa byggmaterialet
och slangordet. Samma sort som homonymfelen pa strava och dia, men inom
ETT uppslag i stallet for mellan tva.
"""
import fyll_synonymer

VAL = {
    "matiné":            "eftermiddagsföreställning",
    "seeda":             "rangordna, ranka",
    "nubb":              "småspik, stift",
    "bylte":             "knyte, packe",
    "skäkta":            "armborstpil",
    "ringhet":           "litenhet, obetydlighet",
    "stenografi":        "snabbskrift, kortskrift",
    "fästa avseende vid": "beakta, ta hänsyn till",
    "väderbiten":        "garvad, barkad",
    "baldakin":          "tronhimmel, sänghimmel",
    "insulär":           "öpräglad ; avskärmad",
    "bålverk":           "förskansning, skyddsvärn",
    "diametral":         "motsatt, polär",
    "akribi":            "noggrannhet, sorgfällighet",
    "kitt":              "fogmassa",
    "globetrotter":      "världsresenär, kosmopolit",
    "krackelera":        "spricka",
    "kommissionär":      "ombud, mellanhand",
    "expropriera":       "tvångsinlösa",
    "rättmätig":         "berättigad, befogad",
    "satyr":             "faun ; vällusting",
    "färm":              "flink, rapp",
    "minaret":           "bönetorn",
    "armod":             "fattigdom, misär",
    "kärve":             "nek, sädesbunt",
    "fåfäng":            "egenkär, inbilsk ; fruktlös",
    "nämnd":             "utskott, kommitté ; jury",
    "talg":              "ister",
    "hädisk":            "blasfemisk, hädande",
    "nogräknad":         "samvetsgrann ; kräsen",
    "infinna sig":       "inställa sig ; bli märkbar",
    "förgapa sig":       "förälska sig, bli betagen",
    "precedens":         "försteg",
    "flottilj":          "flygförband ; sjöstyrka",
    "hänvisa":           "anvisa, remittera ; referera till",

    "bebådelse":         "≈ uppenbarelse",
    "ad notam":          "≈ lägga på minnet",
    "konfektion":        "≈ färdigsydda kläder",
    "kommod":            "≈ tvättbord",
    "ombudsman":         "≈ ombud",
    "vara på örat":      "≈ berusad",

    "bidé":              None,
    "ektomi":            None,   # kallan upprepar definitionen
    "tajga":             None,   # naturgeografisk zon, eget namn
    "lux":               None,   # matenhet
    "eponym":            None,   # sprakvetenskaplig term
    "sodomi":            None,   # kallans ord ar daterade vardeomdomen
    "canasta":           None,   # spelnamn
    "anafor":            None,   # stilfigurens eget namn
    "överpröva":         None,
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
