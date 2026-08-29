# -*- coding: utf-8 -*-
"""Kopplar synonymer till RATT betydelse pa mina egna kort (2026-08-29).

Adams fraga vid astrakan: "varfor inget ; tecken mellan synonymerna?"
Astrakan var korrekt, men fragan avslojade att 660 kort saknar kopplingen
-- 511 sedan tidigare och 149 skrivna av MIG idag. Jag valde synonymerna
utan att tanka pa att positionen betyder nagot.

KONVENTION: "—" for en betydelse som saknar synonym. Tomma grupper gick
att bygga men gav en hangande "; " sist, vilket ser ut som ett skrivfel.
Med tankstreck syns det pa kortet att betydelsen saknar ord.
"""
import fyll_synonymer

VAL = {
    "excentrisk":     "— ; originell, kufisk",
    "reminiscens":    "hågkomst, svagt minne ; —",
    "mosaisk":        "— ; judisk, israelitisk",
    "analfabet":      "≈ illitterat ; — ; —",
    "despot":         "tyrann ; envåldshärskare",
    "kontinuitet":    "sammanhang, oavbruten följd ; —",
    "försoning":      "förlikning ; gottgörelse",
    "bildad":         "beläst, kultiverad ; —",
    "bolster":        "dyna, kudde ; —",
    "brokig":         "mångfärgad, spräcklig ; —",
    "förvärva":       "anskaffa, införskaffa ; —",
    "tafatt":         "fumlig, valhänt ; —",
    "sensualism":     "sinnlighet, sensualitet ; —",
    "flärd":          "ytlighet, prål ; —",
    "inpyrd":         "indränkt, genomdränkt ; —",
    "kategorisera":   "klassificera, gruppera ; —",
    "andlös":         "spänd ; andäktig",
    "jakaranda":      "palisander ; —",
    "dräktig":        "havande, fosterbärande ; —",
    "gimmick":        "trick ; jippo",
    "saklöst":        "— ; utan påföljd, ostraffat",
    "förläggare":     "bokförläggare, bokutgivare ; —",
    "vittra":         "sönderfalla ; — ; —",
    "döbattang":      "pardörr, dubbeldörr ; —",
    "passivera":      "— ; — ; göra overksam",
    "amnesti":        "benådning, straffrihet ; —",
    "konvoj":         "eskort ; — ; —",
    "dia":            "amma ; —",
    "kateder":        "≈ pulpet ; —",
    "tåt":            "snörstump, tamp ; —",
    "tamp":           "repända, tågända ; —",
    "fläng":          "jäkt, stök ; —",
    "göra sig":       "≈ ta sig bra ut ; —",
    "backa upp":      "stödja, beskydda ; —",
    "syna":           "granska, skärskåda ; —",
    "slå an":         "göra intryck, tilltala ; —",
    "tygel":          "töm ; —",
    "tova":           "trassel, knut ; —",
    "antagonistisk":  "fientlig ; motverkande",
    "alumn":          "— ; ≈ lärjunge",
    "libell":         "vattenpass ; —",
    "kartell":        "syndikat, trust ; —",
    "sond":           "≈ kateter ; — ; —",
    "beråd":          "≈ bryderi ; —",
    "tråkad":         "— ; uttråkad, less",
    "diskant":        "— ; — ; sopran",
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
