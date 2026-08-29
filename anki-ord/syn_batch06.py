# -*- coding: utf-8 -*-
"""Synonymbatch 06 -- 48 kort.

MOTSATSORD uteslutna: "obildad" (bildad), "sondring/osamja" (forsoning).

INNEHALLSFLAGGA -- befrynda: kortet sager "bli slakt med nagon genom
giftermal", men Wiktionary definierar ordet som "paborja ett
vanskapsforhallande, bli van med". Det ar inte samma sak. Ingen synonym
satt; kortet behover en egen kontroll mot SO/SAOB innan nagot skrivs.
Samma sort av fynd som `sinus` och `docka` -- synonymarbetet hittar
innehallsluckor pa kopet.

affix far ingen synonym med flit: "prefix, suffix, andelse" ar TYPER av
affix, inte utbyten for ordet.
"""
import fyll_synonymer

VAL = {
    # --- akta synonymer ---
    "skärmytsling":     "småstrid ; ordstrid",
    "konsiliant":       "försonlig, medgörlig",
    "förnuftsvidrig":   "förnuftsstridig, orimlig",
    "fiffel":           "mygel, fuffens",
    "hydrokultur":      "vattenkultur",
    "moratorium":       "tillfälligt stopp ; betalningsanstånd",
    "inkråm":           "innanmäte ; inälvor",
    "försoning":        "förlikning, gottgörelse",
    "bildad":           "beläst, kultiverad",
    "vittgående":       "långtgående, genomgripande",
    "töcknig":          "dimmig, disig ; dunkel",
    "råk":              "isspricka, vak",
    "bolster":          "dyna, kudde",
    "brokig":           "mångfärgad, spräcklig",
    "förvärva":         "anskaffa, införskaffa",
    "skrank":           "räcke, barriär",
    "bolero":           "spansk folkdans ; bolerojacka",
    "tafatt":           "fumlig, valhänt",
    "kabaré":           "varieté, revy",
    "dissident":        "oliktänkande, avfälling",
    "flärd":            "ytlighet, prål",
    "inpyrd":           "indränkt, genomdränkt",
    "pekoral":          "dravel, rappakalja",
    "förflackas":       "förytliga, banalisera",
    "andlös":           "spänd, andäktig",
    "jakaranda":        "palisander",
    "dräktig":          "havande, fosterbärande",
    "stint":            "oavvänt, spänt",

    # --- narmaste ord, inte utbyte ---
    "homeopati":        "≈ alternativmedicin",
    "bokslut":          "≈ årsredovisning",
    "lektor":           "≈ lärare",
    "ontologi":         "≈ metafysik",
    "paletå":           "≈ överrock",
    "nimrod":           "≈ jägare",

    # --- ingen synonym i nagon av de tre kallorna ---
    "enaktare":         None,
    "affix":            None,   # prefix/suffix ar TYPER av affix, inte utbyten
    "balalajka":        None,   # instrumentnamn
    "sinologi":         None,   # vetenskapsgren, eget namn
    "med bravur":       None,
    "metates":          None,   # sprakvetenskaplig term
    "tilde":            None,   # tecknets namn
    "drätsel":          None,   # kallan upprepar bara definitionen
    "vind för våg":     None,
    "till fromma för":  None,
    "på nåder":         None,
    "fotocell":         None,
    "numen":            None,
    "befrynda":         None,   # INNEHALLSFLAGGA, se docstring
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
