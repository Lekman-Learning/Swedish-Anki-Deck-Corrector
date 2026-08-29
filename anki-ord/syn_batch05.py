# -*- coding: utf-8 -*-
"""Synonymbatch 05 -- 49 kort.

MOTSATSORD uteslutna: "allman/generell" (selektiv), "torr" (slabbig).

manipulera ar satsens kansligaste kort: SO:s FORSTA betydelse ar helt
neutral ("stod och manipulerade med laset"), den andra klart negativ.
Synonymerna foljer den uppdelningen -- "hantera, mixtra" pa betydelse 1,
"styra" pa betydelse 2. Slas de ihop blir hela kortet negativt, vilket ar
precis det fel deckets gamla facit gjorde ("paverka").

skildra ar kortet som UNDERKANDES 29/8 for att jag delade det i fler
betydelser an SO har. Synonymen ar satt mot den rattade texten.
"""
import fyll_synonymer

VAL = {
    # --- akta synonymer ---
    "pascha":            "hög turkisk ämbetsman ; vällevnadsman",
    "meander":           "flodslinga, flodkrök",
    "bokstavstrogen":    "bokstavlig, bibeltrogen",
    "selektiv":          "utväljande, sovrande",
    "astigmatism":       "brytningsfel",
    "manipulera":        "hantera, mixtra ; styra",
    "snusmumrik":        "snusgubbe",
    "gisslare":          "flagellant, självplågare ; satiriker",
    "verv":              "schvung, glöd",
    "småskuren":         "småaktig, småsint",
    "anekdot":           "historiett, skämthistoria",
    "motvalls":          "motsägelselysten, trilsk",
    "brushuvud":         "hetsporre, vildhjärna",
    "argot":             "slangspråk, förbrytarslang",
    "balk":              "bjälke",
    "portiär":           "dörrförhänge, draperi",
    "moarera":           "vattra",
    "nutrition":         "näringstillförsel",
    "slabbig":           "slaskig, kladdig",
    "sampel":            "stickprov, urval",
    "hårdra":            "pressa, göra våld på",
    "skildra":           "beskriva, återge",
    "tinnitus":          "öronsus, öronsusning",
    "förtörnad":         "förbittrad, vred",
    "divan":             "ottoman, schäslong",
    "despot":            "tyrann, envåldshärskare",
    "ackreditera":       "befullmäktiga, ge fullmakt",
    "amnesti":           "benådning, straffrihet",
    "föredrag":          "föreläsning, anförande ; framställningssätt",
    "mellanhavande":     "tvist, kontrovers",
    "impressario":       "artistagent, manager",
    "piffig":            "snitsig, pikant",
    "sörja":             "slask, modd",
    "prosaisk":          "alldaglig, nykter",
    "hissna":            "hisna",
    "tillhandahålla":    "erbjuda, förse",
    "strömning":         "flöde ; tendens",
    "fikonspråk":        "rotvälska ; fackspråk",
    "köpeskilling":      "köpesumma, betalningssumma",
    "reminiscens":       "hågkomst, svagt minne",

    # --- narmaste ord, inte utbyte ---
    "damejeanne":        "≈ korgflaska",
    "drivbänk":          "≈ odlingsbädd",
    "ta reson":          "≈ ta skäl",

    # --- ingen synonym i nagon av de tre kallorna ---
    "camembert":         None,   # ostsort, eget namn
    "kantele":           None,   # instrumentnamn
    "överloppsgärning":  None,
    "klä skott för något": None, # idiom utan utbyte
    "redning":           None,   # synonymer.se ger bara "sas", vilket ar FEL sak
    "regel / rigel":     None,   # snedstrecket bryter uppslaget -- kraver egen sokning
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
