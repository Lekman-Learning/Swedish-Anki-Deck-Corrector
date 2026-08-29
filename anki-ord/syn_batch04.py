# -*- coding: utf-8 -*-
"""Synonymbatch 04 -- 52 kort.

MOTSATSORD uteslutna: "enorm/ofantlig/kolossal" (diminutiv), "tydlig/
valstrukturerad" (plottrig), "oinspirerad" (besjalad), "platt/flack"
(kuperad), "oppenhet/offentlighet" (sekretess), "valdoft" (odor).

HOMONYMFEL: synonymer.se gav for `strava` synonymerna till SUBSTANTIVET
(strabstotta, snedstod, bjalke) medan kortet galler VERBET "kampa
malmedvetet". Ingen synonym satt -- listan hor till ett annat ord, och att
anvanda den hade satt "stodbjalke" som synonym till "strava efter". Kravar
egen uppslagning.

aktualisera och formaten ar tva kort som underkandes 28/8 (uppdiktade
tillagg respektive ASCII i etymologin). Synonymerna ar valda mot den
rattade texten.
"""
import fyll_synonymer

VAL = {
    # --- akta synonymer ---
    "annullera":        "upphäva, ogiltigförklara",
    "epitet":           "benämning, öknamn",
    "gourmet":          "finsmakare, läckergom",
    "kapellmästare":    "orkesterledare, dirigent",
    "recession":        "lågkonjunktur, avmattning",
    "skurril":          "burlesk, plump",
    "koncept":          "utkast, kladd ; förlora fattningen",
    "gerilla":          "friskara, partisaner",
    "teknikalitet":     "teknisk detalj, formalitet",
    "preciös":          "tillgjord, affekterad",
    "bondsk":           "bondaktig, lantlig",
    "tålig":            "tålmodig, fördragsam",
    "kristyr":          "glasyr, sockeröverdrag",
    "transversal":      "tvärgående",
    "avvika":           "vika av ; rymma",
    "drittel":          "smörtunna, laggkärl",
    "kräslig":          "läcker, överdådig",
    "undfå":            "motta, ta emot",
    "jokk":             "fjällbäck",
    "agentur":          "agentskap, representantskap",
    "struma":           "sköldkörtelförstoring",
    "förmäten":         "övermodig, anspråksfull",
    "nitid":            "prydlig, lättläst",
    "fog":              "skarv, sammanfogning",
    "åthävor":          "later, manér",
    "utläggning":       "utplacering ; redogörelse",
    "robust":           "kraftig, stadig",
    "betagande":        "förtjusande, bedårande",
    "ity att":          "emedan",
    "profetera":        "förkunna ; förutsäga",
    "besjälad":         "inspirerad, uppfylld",
    "aktualisera":      "föra på tal",
    "diminutiv":        "minimal, obetydlig ; förminskningsord",
    "plottrig":         "rörig, oredig",
    "dyslexi":          "ordblindhet, läs- och skrivsvårigheter",
    "memoarer":         "levnadsminnen, självbiografi",
    "omfång":           "omfattning, vidd",
    "eufemism":         "förskönande omskrivning, omskrivning",
    "odör":             "stank, os",
    "ranglig":          "vinglig, ostadig",
    "glossarium":       "ordlista, ordförteckning",
    "klenod":           "dyrgrip, dyrbarhet",
    "kuperad":          "backig, kullig ; stubbad",
    "apologi":          "försvarstal, försvarsskrift",
    "försynt":          "anspråkslös, finkänslig",
    "sekretess":        "tystnadsplikt, hemlighållande",
    "adonis":           "bildskön yngling ; pigtjusare",

    # --- narmaste ord, inte utbyte ---
    "supera":           "≈ dinera",   # supera ar specifikt SENT kvallsmal

    # --- ingen synonym i nagon av de tre kallorna ---
    "postmodernism":    None,   # stilriktningens eget namn
    "spinal":           None,   # anatomisk term
    "klåfingrig":       None,   # bara "klafingrad", en stavningsvariant
    "sträva":           None,   # HOMONYMFEL -- se docstring, kraver ny uppslagning
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
