# -*- coding: utf-8 -*-
"""Synonymbatch 17 -- sista 19 korten.

Nastan uteslutande IDIOM. Ett idiom har sallan ett utbyte -- det ar just
poangen med ett idiom: uttrycket ar inte utbytbart mot sina ord. De far
darfor synonym::saknas, och det ar ratt svar, inte en lucka.
"""
import fyll_synonymer

VAL = {
    "changera":         "sjangsera, blekas",
    "kontrastera":      "sticka av, bryta av",
    "ditt och datt":    "≈ lite av varje",

    "god dag yxskaft":  None,
    "greppa efter ett halmstrå": None,
    "inget man snyter ur näsan": None,
    "jämnt skägg":      None,
    "en polsk riksdag": None,
    "ha satt sin sista potatis": None,
    "sopa rent framför sin dörr": None,
    "trolla med knäna": None,
    "salig i åminnelse": None,
    "blåsa faran över": None,
    "det flyger inga stekta sparvar i munnen på en": None,
    "det går sin gilla gång": None,
    "det knallar och går": None,
    "genetiker":        None,   # yrkesbeteckning
    "swedenborgianism": None,   # larans eget namn
    "gå tretton på dussinet": None,
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
