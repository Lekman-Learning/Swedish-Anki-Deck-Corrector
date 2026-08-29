# -*- coding: utf-8 -*-
"""Synonymbatch 01 -- de 30 forsta korten utan synonymrad.

Valda ur synonymer.se + SO/SAOL/Wiktionary, mot kortets EGEN huvudbetydelse.
" ; " = per betydelse (position 1 = betydelse 1). "≈" = narmaste ord, inte
utbyte. None = ingen synonym i nagon kalla -> tag synonym::saknas.
"""
import fyll_synonymer

VAL = {
    # --- akta synonymer ---
    "lappkast":        "helomvändning ; kovändning",
    "stansa":          "slå hål i, skära ut",
    "hajk":            "fotvandring",
    "fjolla":          "våp, toka",
    "lillgammal":      "brådmogen, förnumstig",
    "konsternera":     "förbrylla, förvirra",
    "eskalation":      "intensifiering",
    "serpentin":       "slingerväg",
    "litania":         "kyrkobön ; jeremiad",
    "sabbat":          "vilodag ; vila",
    "deklarera":       "tillkännage ; uppge inkomst ; kungöra",
    "ibidem":          "sammastädes",
    "aber":            "hake, stötesten",
    "försumma":        "underlåta, negligera",
    "vädra":           "lufta, ventilera",
    "buskis":          "bondkomik, buskteater",
    "gigolo":          "yrkesdansör ; betald eskort",
    "sly":             "snår, småskog",
    "dysenteri":       "rödsot",
    "i tid och otid":  "jämt och ständigt",

    # --- narmaste ord, inte utbyte ---
    # natla ar specifikt skomakeri; somma ar vidare.
    "nåtla":           "≈ sömma",
    # daxel och bila ar olika yxor -- bila ar det narmaste sourcade ordet.
    "däxel":           "≈ bila",
    # utarmad om jord/resurs ar inte samma som utfattig om person, men
    # utfattig ar det ord ORD skulle stalla mot det.
    "utarmad":         "≈ utfattig, exploaterad",

    # --- ingen synonym i SO, SAOL, synonymer.se eller Wiktionary ---
    "grafologi":       None,   # facktermen ar sitt eget namn
    "ferrit":          None,   # materialteknisk term
    "tertial":         None,   # kvartal ar FEL (3 mot 4 man), SO JFR-markerar
    "lombardera":      None,   # bankterm, inget utbyte finns
    "farin":           None,   # rasocker star i sjalva definitionen
    "humifiera":       None,   # markkemisk term
    "stetoskop":       None,   # foremalsnamn
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
