"""Fyller i `neutral` på den registeraxel som saknas.

Adams beslut 2026-08-11: *"fyll i neutralt då."*

## Bakgrunden

`baksida.validate_register()` kräver sedan 2026-08-11 både stilnivå och valör
på varje betydelse -- en regel som stått i docstringen sedan 2026-08-04 men
aldrig implementerats. När den slogs på föll **86 av 342 full-v3-kort** och
2 681 av 3 233 v2-kort, nästan alla för att valören saknas.

## Invändningen, och varför den ändå inte fäller beslutet

Jag invände att auto-ifyllnad återskapar den tvetydighet Adams eget
2026-08-10-beslut tog bort: *"neutral skrivs UT, inte utelämnas: ett tomt fält
och ett bedömt fält såg tidigare likadana ut."* Ett automatiskt `neutral` är
inte en bedömning, och kortet ser efteråt ut som om någon vägt frågan.

Adam vidhöll. Det är rätt avvägning av ett skäl jag först undervärderade:
`neutral` är enligt `config.py` **"VANLIGASTE RÄTTA SVARET"** på båda axlarna.
Alternativet -- att låta 2 700 kort ligga ogiltiga tills någon bedömt dem en
och en -- betyder att spärren blockerar hela kön i månader.

Invändningen hanteras i stället genom att göra ifyllnaden **spårbar**: varje
rörd not taggas `register_autoifylld::<datum>` och skrivs till en logg med sitt
tidigare värde. Skillnaden mot ett bedömt fält går alltså fortfarande att
ställa en fråga om, vilket var hela poängen med 2026-08-10-beslutet.

## Vad som INTE rörs

Kort vars register innehåller en **okänd tagg** lämnas. Där är felet inte en
saknad axel utan ett värde utanför vokabulären (`negativ` satt som stilnivå,
`arkaisk` där SO säger *ngt ålderdomlig*). Att lägga till `neutral` ovanpå
hade gjort kortet giltigt utan att göra det riktigt -- alltså dolt felet i
stället för att laga det.

    python v3_register_neutral.py --torr
    python v3_register_neutral.py --kor
"""

import argparse
import datetime
import json
import os
import sys

import baksida
import config
from ankiconnect import invoke

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

LOGG = os.path.join(os.path.dirname(__file__), "register_autoifyllda.jsonl")
IDAG = datetime.date.today().isoformat()
TAG = f"register_autoifylld::{IDAG}"


def komplettera(register):
    """Lägger till `neutral` på saknad axel. Returnerar (ny, skal) eller None.

    None = rör inte kortet (okänd tagg, eller redan giltigt).
    """
    if not register:
        return None
    if any("okänd register-tagg" in w for w in baksida.validate_register(register)):
        return None

    nya_delar, skal = [], []
    for del_ in register.split(";"):
        del_ = del_.strip()
        saknar = [a for a in ("stilnivå", "valör")
                  if any(f"saknar {a}-tagg" in w
                         for w in baksida.validate_register(del_))]
        if saknar:
            # Stilnivå skrivs först, valör sedan -- samma ordning som AXLAR i
            # baksida.py, så att raden blir läsbar i den ordning den valideras.
            if "stilnivå" in saknar:
                del_ = "neutral, " + del_
            if "valör" in saknar:
                del_ = del_ + ", neutral"
            skal.append("+".join(saknar))
        nya_delar.append(del_)

    if not skal:
        return None
    ny = " ; ".join(nya_delar)
    if baksida.validate_register(ny):
        return None      # blev inte giltigt ändå -- lämna åt en människa
    return ny, ",".join(skal)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--torr", action="store_true")
    ap.add_argument("--kor", action="store_true")
    a = ap.parse_args()
    if not (a.torr or a.kor):
        sys.exit("Ange --torr eller --kor.")

    nids = invoke("findNotes",
                  query=f'deck:"{config.DECK_NAME}" tag:{config.FORMAT_TAG_V2}')
    noter = invoke("notesInfo", notes=nids)
    print(f"v2-noter: {len(noter)}")

    plan, hoppade_okand, redan_ok, oparsbara = [], 0, 0, 0
    for n in noter:
        rå = n["fields"].get(config.FIELD_BAKSIDA, {}).get("value", "")
        try:
            p = baksida.parse(rå)
        except Exception:
            oparsbara += 1
            continue
        if not baksida.validate_register(p.get("register")):
            redan_ok += 1
            continue
        res = komplettera(p.get("register"))
        if res is None:
            hoppade_okand += 1
            continue
        ny, skal = res
        plan.append((n, p, ny, skal))

    print(f"  redan giltiga              : {redan_ok}")
    print(f"  ATT FYLLA I                : {len(plan)}")
    print(f"  lämnas (okänd tagg m.m.)   : {hoppade_okand}")
    print(f"  oparsbara                  : {oparsbara}")
    for n, p, ny, skal in plan[:12]:
        ord_ = n["fields"].get(config.FIELD_ORD, {}).get("value", "")
        print(f"    {ord_:<22} \"{p['register']}\"  ->  \"{ny}\"")
    if len(plan) > 12:
        print(f"    ... och {len(plan) - 12} till")

    if a.torr:
        print("\n--torr: inget ändrat.")
        return

    skrivna = 0
    with open(LOGG, "a", encoding="utf-8") as logg:
        for n, p, ny, skal in plan:
            html = baksida.build(
                huvudbetydelse=p.get("huvudbetydelse"),
                synonymer=p.get("synonymer"),
                exempelmening=p.get("exempelmening") or "",
                register=ny,
                bild_html=p.get("bild_html"),
                synonym_groups=p.get("synonym_groups"),
                etymologi=p.get("etymologi"),
            )
            invoke("updateNoteFields",
                   note={"id": n["noteId"], "fields": {config.FIELD_BAKSIDA: html}})
            invoke("addTags", notes=[n["noteId"]], tags=TAG)
            logg.write(json.dumps({
                "tid": datetime.datetime.now().isoformat(timespec="seconds"),
                "noteId": n["noteId"],
                "ord": n["fields"].get(config.FIELD_ORD, {}).get("value", ""),
                "fore": p.get("register"), "efter": ny, "saknade": skal,
            }, ensure_ascii=False) + "\n")
            skrivna += 1

    print(f"\nSkrev {skrivna} noter, taggade {TAG}.")
    print(f"Logg med tidigare värden: {os.path.basename(LOGG)}")
    print("Sök `tag:register_autoifylld::*` för att skilja dem från bedömda kort.")


if __name__ == "__main__":
    main()
