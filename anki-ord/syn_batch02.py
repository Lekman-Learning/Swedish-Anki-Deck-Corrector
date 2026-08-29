# -*- coding: utf-8 -*-
"""Synonymbatch 02 -- 72 kort.

VARNING som styrt flera val: synonymer.se blandar in MOTSATSORD i samma
lista. Kontrollerade och uteslutna har: "framsynt" (kortsynt), "dygdig" och
"sedesam" (lastbar), "upprätt/staende/noggrann" (kursiv). Att kopiera listan
rakt av hade satt motsatsen pa kortet.

Fem kort i satsen ar de som TOMDES av den strangare regeln 27-28/8 och nu
far tillbaka ett ord: spe, bemarkt, singular, eklatera, autograf.
"""
import fyll_synonymer

VAL = {
    # --- akta synonymer ---
    "kartig":          "omogen ; kaxig",
    "spaljé":          "spjälverk",
    "angöra":          "anlöpa ; ta landkänning",
    "kofferdist":      "sjöman vid handelsflottan ; handelsfartyg",
    "gräsrötter":      "fotfolk",
    "anfang":          "utsirad initial ; valvstöd",
    "pannå":           "dörrspegel ; träskiva",
    "basa":            "leda, förestå",
    "espri":           "kvickhet, slagfärdighet",
    "via":             "genom ; med hjälp av",
    "fäbod":           "säter",
    "deformation":     "formförändring, vanställande",
    "proselyt":        "nyomvänd, konvertit",
    "barbarisk":       "omänsklig, grym",
    "grums":           "bottensats, drägg",
    "kortsynt":        "korttänkt, obetänksam",
    "kreation":        "modeskapelse",
    "antecedentia":    "förhistoria",
    "erotisk":         "sinnlig, amorös",
    "patina":          "ärg ; ålderdomlig prägel",
    "kursiv":          "lutande ; flyktig",
    "defilera":        "paradera, tåga förbi",
    "moaré":           "vattrat siden",
    "fistel":          "sårgång",
    "ratificera":      "stadfästa, godkänna",
    "diligens":        "postvagn",
    "bemärkt":         "framstående, ansedd",
    "fingerad":        "påhittad, uppdiktad",
    "kretong":         "kattun, chintz",
    "dressör":         "djurtämjare, domptör",
    "kut":             "krokig hållning ; sälunge",
    "alstring":        "skapande, frambringande",
    "eklatera":        "tillkännage, offentliggöra",
    "drömslott":       "sagoslott ; luftslott",
    "spe":             "hån, åtlöje",
    "intonation":      "tonfall ; tonträffning",
    "slana":           "stör, stång",
    "paulun":          "himmelssäng ; sängomhänge",
    "lastbar":         "utsvävande, liderlig",
    "beväring":        "värnpliktig",
    "jungman":         "sjömanslärling, lättmatros",
    "yttring":         "yttrande ; uttryck",
    "stuckatur":       "stuckdekor, gipsornament",
    "missanpassad":    "asocial, illa anpassad",
    "anlöpa":          "angöra, lägga till",
    "dekis":           "förfallen, på fallrepet",
    "kannstöperi":     "ovederhäftigt prat",
    "spjäll":          "ventil ; klaff",
    "koryfé":          "föregångsman, pamp",
    "rauk":            "strandpelare, stenpelare",
    "ingivelse":       "inspiration, infall",
    "företal":         "förord, inledning",
    "harnesk":         "bröstpansar ; fientlig",
    "kalkera":         "rita av ; efterhärma",
    "singulär":        "säregen, särpräglad",
    "munväder":        "struntprat, svammel",
    "ax":              "sädesax ; blomställning",
    "truga":           "övertala, tjata",
    "varp":            "ränning ; slagg",

    # --- narmaste ord, inte utbyte ---
    "greve":           "≈ adelsman",           # greve ar EN rang, adelsman vidare
    "befaren":         "≈ berest",             # befaren galler specifikt sjoss
    "toga":            "≈ mantel",             # toga ar en bestamd romersk drakt
    "cyklop":          "≈ jätte ; undervattensmask",
    "in natura":       "≈ i varor",
    "autograf":        "≈ namnteckning",       # autograf = av en KAND person
    "in manu":         "≈ tillhanda",
    "ljuster":         "≈ treudd, harpun",     # ljuster ar ett fiskredskap
    "falsett":         "≈ högt röstregister",

    # --- ingen synonym i nagon av de tre kallorna ---
    "cedilj":          None,   # diakritiskt tecken, eget namn
    "laminat":         None,   # materialterm
    "lymfa":           None,   # medicinsk term
    "sinus":           None,   # "sinusfunktion" upprepar bara uppslagsordet
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
