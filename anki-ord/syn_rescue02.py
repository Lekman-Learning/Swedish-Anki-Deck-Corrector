# -*- coding: utf-8 -*-
"""Raddar de flaggade korten med uppslag mot RATT form (2026-08-29).

De tre homonym-/formfelen loste sig genom att sla upp en narliggande form
i stallet for uppslagsordet sjalvt:

  strava  -> `efterstrava` ger "strava efter, trakta efter, astunda".
  dia     -> `amma` listar "ge di, dia, dagga". OMVANT belagt.
  befrynda-> `befryndad` ger "beslaktad, slakt". 

RATTELSE: jag flaggade `befrynda` som mojligt innehallsfel, eftersom
Wiktionary definierar det som "bli van med" medan kortet sager "bli slakt
genom giftermal". Uppslaget pa `befryndad` visar att KORTET har ratt och
Wiktionary ar avvikaren. Flaggan tas bort.

`regel / rigel` forblir tom: synonymer.se-sidan for "regel" serverar
homonymen REGEL SOM BESTAMMELSE (lag, stadga, forordning), inte
lasanordningen. Enda kandidat for ratt betydelse ar "hasp", som bara ar
ett anvandarbidrag.
"""
import fyll_synonymer

VAL = {
    "sträva":   "≈ trakta",
    "dia":      "amma",
    "befrynda": "≈ bli besläktad",
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
