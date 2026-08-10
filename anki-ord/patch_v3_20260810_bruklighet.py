# -*- coding: utf-8 -*-
"""Rättar register utifrån SO:s `bruklighetskommentar` — fältet som var osynligt.

## Vad som gick fel

`slaupp.py --kompakt` skrev aldrig ut SO:s stilmarkering, och `_plocka`
letade dessutom efter nyckeln `bruklighet` medan SO:s faktiska nyckel heter
`bruklighetskommentar` (exakt nyckelmatchning — den träffade aldrig). Fältet
var alltså osynligt i BÅDA ändarna av kedjan.

Följden: registret på hela nya3-batchen sattes utifrån ett sammandrag som
saknade precis den uppgift som avgör registret. Värre än att bara gissa —
patchtexterna kom att PÅSTÅ "SO markerar ingenting" om ord där SO markerar
något. *lappri* fälldes av blindgranskaren just på den punkten: SO säger
"något ålderdomligt", kortet sa `neutral`.

Det är rimligen en huvudorsak till att 49 % av decket står som `formell`:
fältet har aldrig varit synligt för den som satte värdet, så `formell` blev
det som skrevs när man inte visste.

Båda felen är lagade i slaupp.py. Den här filen rättar de kort i nya3 som
ännu inte hunnit blindgranskas — de fem ligger alla i del 2.

## Vad SO faktiskt säger (utläst ur redan sparade svar i uppslag/)

    begiven         "något nedsättande"     kortet sa: neutral, neutral
    dra i långbänk  "något vardagligt"      kortet sa: neutral, negativ
    en masse        "vardagligt"            kortet sa: neutral, neutral
    framdeles       "något högtidligt"      kortet sa: neutral, neutral
    lamentation     "något högtidligt"      kortet sa: formell, lätt negativ

De fyra som redan fällts i del 1 (depression, eau-de-vie, lappri, sint) rörs
INTE här — de är rödflaggade och suspenderade enligt Adams regel att
underkända kort rättas för hand senare.
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HAR = os.path.dirname(os.path.abspath(__file__))
FIL = os.path.join(HAR, "sessions", "session_2026-08-10_v3-omgranskning-nya3.json")

# ord -> (nytt register, tillägg till sökkollens slutsats)
R = {
"begiven": ("neutral, lätt negativ",
  " REGISTER RÄTTAT i efterhand: SO markerar ordet *något nedsättande* i fältet "
  "`bruklighetskommentar`, vilket kortet inte speglade. Att säga att någon är "
  "*begiven på* något är inte neutralt beskrivande — det ligger en antydan om "
  "omåttlighet i ordet."),

"dra i långbänk": ("vardaglig, negativ",
  " REGISTER RÄTTAT i efterhand: SO markerar uttrycket *något vardagligt*. "
  "Stilnivån stod som `neutral` på grund av att stilmarkeringen inte var synlig "
  "i uppslagningens sammandrag."),

"en masse": ("vardaglig, neutral",
  " REGISTER RÄTTAT i efterhand: SO markerar uttrycket *vardagligt*, och "
  "synonymer.se skriver '(vard.)'. Kortet sa `neutral` — och den ursprungliga "
  "patchtexten påstod dessutom uttryckligen att 'SO markerar ingenting', vilket "
  "var fel. Ett franskt lånord ser formellt ut men används vardagligt."),

"framdeles": ("högtidlig, neutral",
  " REGISTER RÄTTAT i efterhand: SO markerar ordet *något högtidligt*. Det "
  "ursprungliga `litterär` var alltså närmare sanningen än det `neutral` jag "
  "ändrade till — jag tog bort en riktig markering därför att jag inte kunde se "
  "att källan hade den."),

"lamentation": ("högtidlig, lätt negativ",
  " REGISTER RÄTTAT i efterhand: SO markerar ordet *något högtidligt*, inte "
  "`formell`. Skillnaden spelar roll: högtidligt betyder att ordet drar "
  "uppmärksamhet till sig, formellt att det hör hemma i sakprosa."),
}


def main():
    d = json.load(open(FIL, encoding="utf-8"))
    kort = d["kort"] if isinstance(d, dict) and "kort" in d else d
    n = 0
    for e in kort:
        r = R.get(e["ord"])
        if not r:
            continue
        nytt, tillagg = r
        gammalt = e["proposed"]["register"]
        if gammalt == nytt:
            print("%-16s redan %s" % (e["ord"], nytt))
            continue
        e["proposed"]["register"] = nytt
        e["sokkoll"]["slutsats"] = (e["sokkoll"].get("slutsats") or "") + tillagg
        e.pop("applicerad", None)
        print("%-16s %-24s -> %s" % (e["ord"], gammalt, nytt))
        n += 1
    json.dump(d, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("\n%d kort rättade." % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
