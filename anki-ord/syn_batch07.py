# -*- coding: utf-8 -*-
"""Synonymbatch 07 -- 49 kort. Mycket idiom och ordled.

MOTSATSORD uteslutet: "skuld" (tillgodohavande).

HOMONYMFEL -- dia: synonymer.se gav diabild, diapositiv, ljusbild,
stordia... alltsa ordet 'dia' som i diabild, medan kortet galler att AMMA.
Andra fallet efter `strava`. Ingen synonym satt.

NY KATEGORI -- ordled. Decket innehaller `iso-`, `-tyg` och `-vill`, som
inte ar ord utan for- och efterled. De kan per definition inte ha en
synonym; de far synonym::saknas och ska inte provas igen. Samma sak galler
langre idiom som "fa noja sig med smulorna fran den rikes bord".
"""
import fyll_synonymer

VAL = {
    # --- akta synonymer ---
    "inpass":            "replik, inlägg",
    "saklöst":           "utan påföljd, ostraffat",
    "förläggare":        "bokförläggare, bokutgivare",
    "herdedikt":         "pastoral, eklog",
    "utstaka":           "staka ut, markera",
    "döbattang":         "pardörr, dubbeldörr",
    "tillgodohavande":   "fordran, behållning",
    "vankelmod":         "obeslutsamhet, tvehågsenhet",
    "husvill":           "bostadslös, hemlös",
    "förhäva sig":       "yvas, brösta sig",
    "förespegla":        "inbilla, ställa i utsikt",
    "sel":               "lugnvatten",
    "tåt":               "snörstump, tamp",
    "tamp":              "repända, tågända",
    "fläng":             "jäkt, stök",
    "förråda sig":       "försäga sig",
    "understå sig":      "drista sig, djärvas",
    "ondgöra sig":       "harmas, förtörnas",
    "beskärma sig":      "förfasa sig, himla sig",
    "dabba sig":         "dumma sig, trampa i klaveret",
    "skrida":            "glida ; förflyta",
    "slå an":            "göra intryck, tilltala",
    "pösa":              "jäsa, svälla ; brösta sig",
    "tova":              "trassel, knut",
    "barka åt skogen":   "gå på tok, gå galet",

    # --- narmaste ord, inte utbyte (ETT ord, se style_guide 2026-08-29) ---
    "galär":             "≈ galeja",
    "rabbin":            "≈ judisk religionslärare",
    "kateder":           "≈ pulpet",
    "dra det tyngsta lasset": "≈ göra grovjobbet",
    "gruva sig":         "≈ oroa sig",
    "ta till intäkt":    "≈ åberopa",
    "ta skruv":          "≈ göra susen",
    "etsa sig":          "≈ fästa sig",

    # --- ingen synonym i nagon av de tre kallorna ---
    "dräll":             None,   # vavnadsslag
    "sari":              None,   # plaggnamn; "skynke/schal" ar fel sak
    "dia":               None,   # HOMONYMFEL, se docstring
    "småskrake":         None,   # artnamn
    "ligga av sig":      None,   # kallan upprepar bara definitionen
    "som en löpeld":     None,
    "det allena saliggörande": None,
    "inte säga flaska":  None,
    "kärringen mot strömmen": None,
    "nitlott":           None,
    "(ngns) väl och ve": None,
    "få nöja sig med smulorna från den rikes bord": None,
    "över stock och sten": None,
    # ordled -- kan per definition inte ha synonym
    "-vill":             None,
    "iso-":              None,
    "-tyg":              None,
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
