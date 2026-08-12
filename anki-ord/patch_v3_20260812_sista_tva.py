# -*- coding: utf-8 -*-
"""De två sista underkända korten 2026-08-12: rättade, men INTE blindgranskade.

`sätta sig` och `destillera` föll i omkörningen. Innehållet rättas här och
skrivs till Anki direkt, men korten får ingen blindgranskning i kväll — ett
paket om två kort betalar ~25 000 token i uppstart för två poster, alltså
sämst tänkbara utbyte. De ligger kvar som underkända och kommer tillbaka av
sig själva i nästa dagsbatch, då med rätt innehåll att döma om.

Det är skillnaden mot att bara lämna dem: **kortet i Adams kö blir korrekt i
kväll, taggen blir korrekt i morgon.** Båda ligger i is:review och pluggas
under tiden, så innehållet är det som brådskar.

## sätta sig — valören satt på fel nivå

Granskaren: SO:s underbetydelse 'vara nedlåtande' ("varför måste han alltid
sätta sig på sina yngre kompisar?") är entydigt negativ, men kortet gav
'neutral, neutral' för alla fyra betydelserna. Registret delas nu per
betydelse, och varje betydelse får en egen synonym — samma form som `preja`
och `apostel` redan har.

## destillera — den bildliga betydelsen

SO har 'destillera fram': utvinna slutsatser eller principer ur ett stort
material ("ur myllret av fakta försökte han destillera fram några mer allmänna
principer"). Kortet hade bara den kemiska. Värt att notera att det här är
ANDRA gången samma kort underkänns för en saknad betydelse — första gången
gällde det exempelmeningen (bryggeri i stället för destilleri), och när den
rättades hittade granskaren nästa lucka. Ett underkännande i taget är inte
samma sak som en fullständig lista över vad som är fel.
"""

import json
import sys
import urllib.parse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FARG = "#3498db"
SVENSKA = "https://svenska.se/api/msearch?ord={}"
SESSION = "sessions/session_2026-08-12_omkorning.json"


def h(o):
    return f'<font color="{FARG}">{o}</font>'


KORT = {
    "sätta sig": {
        "hb": "Placera sig i sittande ställning ; sjunka ihop, om mark eller "
              "husgrund ; vara nedlåtande mot någon ; hävda sin auktoritet",
        "reg": "neutral, neutral ; neutral, neutral ; vardaglig, negativ ; "
               "neutral, neutral",
        "grupper": [["slå sig ner"], ["sjunka"], ["se ner på"], ["hävda sig"]],
        "ex": f"Trött efter promenaden {h('satte hon sig')} på närmaste bänk.",
        "skal": "REGISTER DELAT PER BETYDELSE: SO:s underbetydelse 'vara "
                "nedlåtande' är entydigt negativ ('sätta sig på sina yngre "
                "kompisar'), medan de tre övriga är neutrala. Ett gemensamt "
                "register för alla fyra dolde det. Varje betydelse har nu också "
                "en egen synonym.",
    },
    "destillera": {
        "hb": "Skilja en vätskas beståndsdelar åt genom förångning och "
              "kondensering ; utvinna det väsentliga ur en stor mängd material",
        "reg": "fackspråklig, neutral, kemi ; formell, neutral",
        # Ingen synonym till den bildliga betydelsen: "utvinna" saknar stöd i
        # de hämtade källorna och "destillera fram" innehåller uppslagsordet.
        # Platt lista i stället för en grupp som skulle bli tom.
        "syn": ["rena", "avskilja"],
        "ex": f"På destilleriet lärde hon sig att {h('destillera')} whisky.",
        "skal": "TILLAGD BETYDELSE: SO har 'destillera fram' — utvinna slutsatser "
                "eller principer ur ett stort material ('ur myllret av fakta "
                "försökte han destillera fram några mer allmänna principer'). "
                "Kortet hade bara den kemisk-tekniska betydelsen.",
    },
}


def main():
    poster = json.load(open(SESSION, encoding="utf-8"))
    kvar = [p for p in poster if p["ord"] in KORT]
    if len(kvar) != len(KORT):
        sys.exit(f"hittade {len(kvar)} av {len(KORT)} poster")
    for p in kvar:
        r = KORT[p["ord"]]
        p["proposed"] = {
            "huvudbetydelse": r["hb"],
            "synonymer": r.get("syn", [s for g in r.get("grupper", []) for s in g]),
            "synonym_groups": r.get("grupper"),
            "exempelmening": r["ex"],
            "register": r["reg"],
            "etymologi": None,
        }
        p["approved"] = True
        p["sokkoll"] = {"kalla": SVENSKA.format(urllib.parse.quote(p["ord"])),
                        "slutsats": r["skal"]}
        p.pop("applicerad", None)
    json.dump(kvar, open("sessions/session_2026-08-12_sista_tva.json", "w",
                         encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"skrev {len(kvar)} poster till sessions/session_2026-08-12_sista_tva.json")


if __name__ == "__main__":
    main()
