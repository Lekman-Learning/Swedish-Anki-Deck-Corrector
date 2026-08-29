# -*- coding: utf-8 -*-
"""Synonymbatch 09 -- 25 kort.

MOTSATSORD uteslutna: "betrakta noga, iaktta" (ogna -- kortet betyder just
FLYKTIGT seende, sa de tva orden ar raka motsatsen till uppslagsordet).

rotting: kallans lista ar mest ordet som SLAGVAPEN (karbas, piskkajpp,
ridpiska), medan kortet galler MATERIALET. Valt spanskror, som ar samma
sak som kortet beskriver.
"""
import fyll_synonymer

VAL = {
    # --- akta synonymer ---
    "logg":              "hastighetsmätare ; loggbok",
    "urkund":            "källskrift, aktstycke",
    "bräsera":           "grytsteka",
    "avkok":             "dekokt, extrakt",
    "indisposition":     "opasslighet, olust",
    "ögna":              "skumma, snabbläsa",
    "rotting":           "spanskrör",
    "telning":           "skott, stickling ; avkomma",
    "mista sansen":      "dåna",
    "bondfångeri":       "lurendrejeri, bluff",
    "sedeslös":          "osedlig, lösaktig",
    "diadem":            "pannsmycke, tiara",
    "schvungfull":       "medryckande, klatschig",
    "kor":               "altarrum",

    # --- narmaste ord, inte utbyte ---
    "daler":             "≈ riksdaler",
    "karyatid":          "≈ pelare",
    "interpellation":    "≈ spörsmål",
    "neuros":            "≈ nervlidande",
    "perukstock":        "≈ träbock ; stofil",
    "ulster":            "≈ överrock",

    # --- ingen synonym i nagon av de tre kallorna ---
    "kvader":            None,   # kallan upprepar definitionen
    "teach-in":          None,   # lanord, eget namn
    "ekumenik":          None,
    "prospektera":       None,
    "ymnighetshorn":     None,
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
