# -*- coding: utf-8 -*-
"""Kategori (`≈≈`) pa de 65 idiom/uttryck som blev over.

RATTELSE av mitt eget beslut tidigare samma dag. Jag klassade 65 kort som
"idiom kan inte ha synonym" -- men klassificeringen var MEKANISK
(mellanslag i uppslagsordet = idiom) och slutsatsen for bred.

Tva fel i den:

1. Flera ar inte idiom alls, bara ord med mellanslag eller snedstreck:
   `fasa ut` (= avveckla), `processa med` (= stamma), `sticka av mot`
   (= kontrastera), `regel / rigel`, `public service`, `riksha (rickshaw)`.
   Dar finns riktiga synonymer, inte bara kategorier.

2. For de AKTA idiomen galler samma logik som raddade `tertial`: en
   kategori beskriver inte uttryckets ord, utan vad det BETYDER. `en polsk
   riksdag` betyder kaos; `kla skott for nagot` ar att vara syndabock.

Kvar utan nagot: de tre ordleden `-tyg`, `-vill`, `iso-`. Ett efterled har
ingen kategori -- det ar en byggsten, inte ett begrepp.
"""
import fyll_synonymer

VAL = {
    # --- inte idiom: riktiga synonymer ---
    "fasa ut":            "avveckla",
    "processa med":       "stämma",
    "sticka av mot":      "kontrastera",
    "ligga av sig":       "≈ förslappas",
    "få gehör för":       "≈ få medhåll",
    "med bravur":         "≈ skickligt",
    "över hövan":         "≈ överdrivet",
    "till fromma för":    "≈ till gagn för",
    "på basis av":        "≈ utifrån",
    "på kuppen":          "≈ på köpet",
    "inte på långt när":  "≈ långt ifrån",
    "a priori":           "≈ på förhand",
    "i onåd":             "≈ i vanrykte",
    "på nåder":           "≈ av välvilja",
    "vind för våg":       "≈ utan tillsyn",

    # --- ord med mellanslag/snedstreck: kategori ---
    "regel / rigel":      "≈≈ låsanordning ; ≈≈ trävirke",
    "public service":     "≈≈ allmänradio",
    "riksha (rickshaw)":  "≈≈ dragkärra",
    "a la carte":         "≈≈ beställningssätt",
    "retorisk fråga":     "≈≈ stilfigur",
    "gordisk knut":       "≈≈ olösligt problem",
    "trojansk häst":      "≈≈ infiltratör",

    # --- akta idiom: kategorin ar vad uttrycket BETYDER ---
    "(ngns) väl och ve":  "≈≈ livsöde",
    "alla taggar utåt":   "≈≈ avvisande",
    "bilda epok":         "≈≈ epokgörande",
    "blåsa faran över":   "≈≈ ge klartecken",
    "det allena saliggörande": "≈≈ universallösning",
    "det drar ihop sig":  "≈≈ nalkas",
    "det flyger inga stekta sparvar i munnen på en": "≈≈ ingen genväg",
    "det går sin gilla gång": "≈≈ oförändrat",
    "det knallar och går": "≈≈ hanka sig fram",
    "en polsk riksdag":   "≈≈ kaos",
    "envar blir salig på sin tro/fason": "≈≈ tolerans",
    "ett angenämt problem": "≈≈ lyxproblem",
    "få nöja sig med smulorna från den rikes bord": "≈≈ smulor",
    "god dag yxskaft":    "≈≈ missförstånd",
    "greppa efter ett halmstrå": "≈≈ desperation",
    "gå tretton på dussinet": "≈≈ alldaglig",
    "göra en höna av en fjäder": "≈≈ överdrift",
    "ha satt sin sista potatis": "≈≈ utspelad",
    "i stadens hank och stör": "≈≈ stadsområde",
    "inget man snyter ur näsan": "≈≈ krävande",
    "inte säga flaska":   "≈≈ tyst",
    "jämnt skägg":        "≈≈ oavgjort",
    "kasta/slänga pärlor för svin": "≈≈ slöseri",
    "klä skott för något": "≈≈ syndabock",
    "koka soppa på en spik": "≈≈ improvisation",
    "komma som lök på laxen": "≈≈ förvärring",
    "komma upp sig i smöret": "≈≈ bli rik",
    "kärringen mot strömmen": "≈≈ motvalls person",
    "lägga rabarber på något": "≈≈ lägga beslag på",
    "salig i åminnelse":  "≈≈ avliden",
    "se ut som en fågelholk": "≈≈ förbluffad",
    "slåss mot väderkvarnar": "≈≈ meningslös kamp",
    "som en löpeld":      "≈≈ blixtsnabbt",
    "sopa rent framför sin dörr": "≈≈ självrannsakan",
    "sätta bocken till trädgårdsmästare": "≈≈ olämpligt val",
    "sätta någon på pottkanten": "≈≈ förlägenhet",
    "titta/se i månen efter något": "≈≈ förgäves",
    "trampa vatten":      "≈≈ hålla sig flytande ; ≈≈ stå still",
    "trolla med knäna":   "≈≈ bravad",
    "veta hur en slipsten ska dras": "≈≈ erfarenhet",
    "visa framfötterna":  "≈≈ briljera",
    "vända på kuttingen": "≈≈ perspektivskifte",
    "över stock och sten": "≈≈ oländigt",
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
