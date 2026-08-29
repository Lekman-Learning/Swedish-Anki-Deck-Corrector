# -*- coding: utf-8 -*-
"""Raddar synonym::saknas-kort med '≈' dar ett RIKTIGT annat ord finns.

Adams fraga: "funkar inte avrundnings synonym for de korten heller?"

Kriteriet jag lagt: ett '≈' ar vart nagot bara om det ar ett ANNAT ORD man
kan mota -- inte en hopklamd upprepning av definitionen som redan star i
fetstil pa samma kort. "halvpension ≈ hotellrum med frukost och en maltid"
lar ingenting; "farin ≈ rasocker" lar ett nytt ord.

Alla nio ar uppslagna, inte pahittade. Tva ar OMVANT belagda -- synonymer.se
listar mangold under bladbeta och farin under rasocker, alltsa exakt det
sambandet vi vill ha.
"""
import fyll_synonymer

VAL = {
    # Omvant belagda pa synonymer.se (starkaste belagget som finns)
    "mangold":      "≈ bladbeta",
    "farin":        "≈ råsocker",

    # Eget uppslag pa synonymer.se bekraftar ordet och betydelsen
    "humifiera":    "≈ förmultna",      # forvandlas till mull, multna
    "lombardera":   "≈ belåna",         # pantsatta -> belana, forpanta
    "jade":         "≈ nefrit",         # nefrit: "gronaktig prydnadssten"

    # Wiktionarys definition ger ordet ordagrant
    "etyd":         "≈ övningsstycke",  # "musikaliskt ovningsstycke"
    "lymfa":        "≈ vävnadsvätska",  # "uppsugen vavnadsvatska"
    "sponta":       "≈ foga samman",    # "foga samman en brada med spont"
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
