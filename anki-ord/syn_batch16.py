# -*- coding: utf-8 -*-
"""Synonymbatch 16 -- 115 kort, sista omgangen.

MOTSATSORD uteslutna (nu 30 fall): "avbruten" (fortlopande), "jamstalldhet"
(sexism), "kongruens" (inkongruens), "sjalvklarhet/foljdriktighet"
(paradox), "disponibel" (indisponibel), "fjarma" (nalkas), "verbal"
(visuell), "a posteriori/i efterhand" (a priori).

Alla flerbetydelsekort far " ; "-koppling direkt, med "—" for betydelser
utan synonym -- konventionen fran syn_fixsep01/02.
"""
import fyll_synonymer

VAL = {
    "fortlöpande":      "oavbruten, kontinuerlig",
    "hamstra":          "bunkra, lagra",
    "ligist":           "huligan, buse",
    "perpendikel":      "normal ; sänklod ; pendel",
    "kverulant":        "gnällspik, rättshaverist",
    "akronym":          "initialförkortning",
    "cementa":          "belägga med cement ; befästa, konsolidera",
    "visthus":          "matbod, visthusbod",
    "stocka sig":       "skocka sig, tilltäppas",
    "kuse":             "häst ; bulle ; —",
    "sexism":           "könsdiskriminering",
    "förströelse":      "tidsfördriv, förlustelse",
    "vräkig":           "prålig, pompös",
    "spjuver":          "skälm, filur",
    "partisan":         "gerillakrigare, motståndsman",
    "krypta":           "gravkammare, gravvalv",
    "dalta":            "pjoska, klema",
    "alias":            "även kallad ; täcknamn",
    "övertalig":        "överflödig, överskjutande",
    "origo":            "nollpunkt",
    "silo":             "lagertorn, spannmålsmagasin ; —",
    "generator":        "strömalstrare, dynamo ; —",
    "likar":            "likasinnade, meningsfränder",
    "excentriker":      "original, kuf",
    "destinera":        "avsända, skicka",
    "harakiri":         "självmord ; —",
    "girigbuk":         "snåljåp, gnidare",
    "happening":        "spontanföreställning, improvisation",
    "enfaldig":         "inskränkt, oförståndig",
    "merkantil":        "kommersiell, affärsmässig",
    "flirta":           "stöta ; —",
    "diktion":          "uttal, frasering",
    "lagbunden":        "reglerad ; regelbunden",
    "kandera":          "glasera, insockra",
    "mission":          "— ; beskickning ; kall, livsuppgift",
    "oavvislig":        "ofrånkomlig, oeftergivlig",
    "cellulosa":        "växttråd ; pappersmassa",
    "konservator":      "— ; taxidermist, preparator",
    "jargong":          "yrkesspråk, kotterispråk ; slentrian",
    "intim":            "förtrolig, privat ; nära, innerlig ; — ; hemtrevlig ; —",
    "skrivelse":        "inlaga, promemoria",
    "inkongruens":      "bristande överensstämmelse",
    "paradox":          "självmotsägelse, antinomi",
    "dränera":          "täckdika, torrlägga ; avleda sårvätska ; —",
    "apanage":          "underhållsanslag, understöd",
    "emittera":         "— ; sända ut",
    "pragmatisk":       "praktiskt inriktad, jordnära",
    "tjo och tjim":     "hålligång, tjohej",
    "vinnlägga sig":    "bemöda sig, beflita sig",
    "memorera":         "lära in, instudera",
    "slapphänt":        "eftergiven, efterlåten",
    "nalkas":           "närma sig, stunda",
    "manifestera":      "ådagalägga, lägga i dagen",
    "kryptera":         "chiffrera, koda",
    "lösöre":           "lösegendom, bohag",
    "estrad":           "podium, tribun",
    "reinkarnation":    "återfödelse, själavandring",
    "plysch":           "yllesammet, schagg",
    "tabu":             "förbud, bannlysning ; bannlyst, okränkbar",
    "gendarm":          "polissoldat, krigspolis",
    "fjäskig":          "inställsam, servil",
    "visuell":          "synlig ; —",
    "suspendera":       "avstänga ; upphäva",
    "smörja kråset":    "kalasa, frossa",
    "rannsaka":         "granska, pröva ; förhöra",
    "pampusch":         "galosch, bottin",
    "aerosol":          "sprej ; —",

    "gluten":           "≈ mjölprotein",
    "kronblad":         "≈ hylleblad",
    "i andanom":        "≈ i fantasin",
    "sociologi":        "≈ samhällslära",
    "komminister":      "≈ kaplan",
    "multilateral":     "≈ flersidig",
    "dra sitt strå till stacken": "≈ bidra",
    "fanera":           "≈ klä med faner",
    "alimentär":        "≈ närings-",
    "ettdera":          "≈ den ene",
    "seans":            "≈ spiritistmöte",
    "deodorant":        "≈ luktborttagare",
    "indisponibel":     "≈ oanträffbar",
    "ametist":          "≈ ädelsten",
    "inte skräda orden": "≈ tala rent ut",
    "tillhands":        "≈ till reds",
    "stor lyhördhet":   "≈ fingertoppskänsla",
    "löst folk":        "≈ patrask",
    "därmed basta":     "≈ punkt slut",

    "få gehör för":     None,
    "göra en höna av en fjäder": None,
    "sätta bocken till trädgårdsmästare": None,
    "processa med":     None,
    "evidensbaserad":   None,
    "sätta någon på pottkanten": None,
    "trampa vatten":    None,
    "fahrenheit":       None,   # matenhet
    "titta/se i månen efter något": None,
    "mortel":           None,   # foremalsnamn
    "farmaci":          None,   # vetenskapsgren
    "namne":            None,
    "synaps":           None,   # anatomisk term
    "a priori":         None,   # kallan upprepar definitionen
    "gordisk knut":     None,
    "harmynt":          None,
    "bilda epok":       None,
    "röklin":           None,   # liturgiskt plaggnamn
    "kastanjett":       None,   # instrumentnamn
    "liljeväxt":        None,   # vaxtfamilj
    "public service":   None,
    "inte på långt när": None,
    "ett angenämt problem": None,
    "homosocial":       None,
    "syndafall":        None,
    "på kuppen":        None,
    "fördragen":        None,
    "överburen":        None,
    "neonatal":         None,
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
