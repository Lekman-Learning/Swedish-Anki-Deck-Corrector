"""Pausar kort som inte går att sökkolla — de blockerar kön i stället för att lagas.

Adams beslut 2026-08-11: *"kort som ytong sätts på paus tills vi har
tillräckligt många granskade ord för att ha tid över för sådant arbete."*

## Vilka kort det gäller

`ytong` är ett varumärke, inte ett uppslagsord. svenska.se har ingen artikel
och returnerar grannartiklar (`yta`, `ytaktiv`) — uppslagsordsspärren i
`slaupp.py` fångar det numera, men den kan bara säga att källan saknas. Att
faktiskt belägga ordet kräver en vanlig webbsökning per kort, alltså flera
minuters arbete som inte skalar i en 300-kortsdag.

## Varför paus och inte bara "hoppa över"

Ett kort som tyst hoppas över ser likadant ut som ett kort som aldrig valdes.
Det kommer tillbaka i nästa urval, misslyckas igen, och kostar samma arbete
varje gång utan att någon märker mönstret. Taggen gör kostnaden synlig och
kön ärlig: `tag:v3_pausad::*` är en körbar fråga, "det där ordet som brukar
strula" är det inte.

Korten är redan suspenderade (allt som inte är full v3 är det sedan
2026-08-11), så pausen ändrar inte vad Adam ser. Den ändrar vad KÖN
innehåller — pausade kort ska inte äta platser i dagsbatchen.

    python v3_pausa.py --lista              # vilka som skulle pausas
    python v3_pausa.py --pausa
    python v3_pausa.py --aterta ytong       # när det finns tid
"""

import argparse
import json
import os
import re
import sys
import unicodedata

import config
from ankiconnect import invoke

# Windows-konsolen är cp1252 och kan inte skriva t.ex. pilar. Utan detta dör
# skriptet i en print() EFTER att Anki redan ändrats -- ett fel som ser ut som
# att körningen misslyckades trots att arbetet är gjort.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PAUS_TAG = "v3_pausad::ingen_ordbokstraff"
UPPSLAG = "uppslag"
HUVUDORDSFALT = {"saol": "ordled", "so": "ortografi", "saob": "lemma"}


def _norm(x):
    return re.sub(r"[^0-9a-zåäöéèüáó]", "", unicodedata.normalize("NFC", str(x or "")).lower())


def har_ordbokstraff(ord_):
    """None = ingen sparad uppslagning (vet inte), True/False = mätt."""
    for namn in (f"{UPPSLAG}/{ord_}.json", f"{UPPSLAG}/{ord_.replace(' ', '_')}.json"):
        if os.path.exists(namn):
            break
    else:
        return None
    d = json.load(open(namn, encoding="utf-8"))
    # Adams regel 2026-08-11: en redaktionell synonymer.se-post räknas som
    # fullgod verifiering, inte bara en ordbokstroff. `sobriquet` saknas i
    # alla tre ordböckerna men har en riktig redaktionell post -- att pausa
    # det som "osökbart" vore fel, och skulle dessutom göra pauslistan
    # otillförlitlig på precis de lånord den finns för.
    if "verifieringsgrund" in d:
        return d["verifieringsgrund"] != "SAKNAS — kräver websökning"
    # Nyare filer bär svaret direkt; äldre måste räknas om ur råsvaret.
    if "uppslagsordstraffar" in d:
        return bool(d["uppslagsordstraffar"])
    no = _norm(ord_)
    delar = {_norm(x) for x in ord_.split()} - {""}
    for kalla, falt in HUVUDORDSFALT.items():
        r = (d.get("svenska_se_ratt") or {}).get(kalla) or {}
        huvud = {_norm((h.get("_source") or {}).get(falt))
                 for h in ((r.get("hits") or {}).get("hits") or [])} - {""}
        if no in huvud or (len(delar) > 1 and delar & huvud):
            return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lista", action="store_true")
    ap.add_argument("--pausa", action="store_true")
    ap.add_argument("--aterta", nargs="+", metavar="ORD")
    a = ap.parse_args()

    if a.aterta:
        for o in a.aterta:
            nids = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" "Framsida:{o}"')
            if not nids:
                print(f"  {o}: hittade inget kort")
                continue
            invoke("removeTags", notes=nids, tags=PAUS_TAG)
            print(f"  {o}: paus borttagen")
        return

    if not (a.lista or a.pausa):
        sys.exit("Ange --lista, --pausa eller --aterta.")

    nids = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" -tag:{PAUS_TAG}')
    noter = invoke("notesInfo", notes=nids)
    traffar, okand = [], 0
    for n in noter:
        o = re.sub(r"<[^>]+>", "", n["fields"].get(config.FIELD_ORD, {}).get("value", "")).strip()
        r = har_ordbokstraff(o)
        if r is None:
            okand += 1
        elif r is False:
            traffar.append((n["noteId"], o))

    # ETT ORD utan uppslagsordsträff är oftast osökbart på riktigt (varumärken,
    # egennamn) -- det är pausfallet. ETT FLERORDSUTTRYCK utan träff betyder
    # nästan alltid bara att frasen inte är en egen artikel; grundordet finns.
    # `ett kok stryk` står under **kok**, `lägga sordin på` under **sordin**.
    # Att pausa dem vore att skriva av ord som går att belägga på en minut, och
    # de skulle försvinna ur kön utan att någon saknade dem.
    enkla = [(n, o) for n, o in traffar if " " not in o]
    fraser = [(n, o) for n, o in traffar if " " in o]

    print(f"Utan sparad uppslagning (vet inte än)     : {okand}")
    print(f"ENSKILDA ord utan ordbokstraff → PAUSAS   : {len(enkla)}")
    for _nid, o in sorted(enkla, key=lambda x: x[1]):
        print(f"   {o}")
    print(f"\nFLERORDSUTTRYCK utan träff → SLÅ UPP GRUNDORDET, pausas ej: {len(fraser)}")
    for _nid, o in sorted(fraser, key=lambda x: x[1]):
        print(f"   {o}")
    if fraser:
        print("   → python slaupp.py <grundord> ...")

    if a.pausa and enkla:
        invoke("addTags", notes=[nid for nid, _ in enkla], tags=PAUS_TAG)
        print(f"\nPausade {len(enkla)} kort med {PAUS_TAG}.")
        print("De är redan suspenderade; pausen håller dem ur dagsbatchen.")
        print("Ta tillbaka med:  python v3_pausa.py --aterta <ord>")


if __name__ == "__main__":
    main()
