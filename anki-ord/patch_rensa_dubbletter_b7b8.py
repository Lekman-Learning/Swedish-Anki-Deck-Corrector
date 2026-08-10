# -*- coding: utf-8 -*-
"""Lyfter ut de poster ur b7/b8 som redan fått full v3 i en annan batch.

Bakgrunden: b7 och b8 blindgranskades, men `verdikt` vägrade skriva in dem —
färskhetsspärren såg att 10 kort ändrats sedan paketen byggdes. Spärren hade
rätt, men slutsatsen var inte "granskningen är förlorad".

De 10 orden fanns nämligen i BÅDA dagens batchar. Jag skrev om dem i
omgranskningsbatchen senare på dagen, och där gick de hela kedjan — alla tio
bär redan `oberoende_verifierad`. Deras b7/b8-domar gäller en äldre version och
ska därför inte skrivas in; de är inte förlorade, de är ersatta.

Kvar blir 35 poster vars innehåll fortfarande stämmer med Anki. Dem kan
`verdikt` behandla som vanligt.

Posterna kastas inte — de flyttas till nyckeln `ersatta_av_senare_batch` i
samma fil, så att det går att se i efterhand vad som lyftes ut och varför.
"""
import glob
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import baksida                      # noqa: E402
import config                       # noqa: E402
from ankiconnect import invoke      # noqa: E402

FALT = ("huvudbetydelse", "register", "synonymer", "exempelmening", "etymologi")


def main():
    for f in sorted(glob.glob(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "sessions", "session_2026-08-10_v3-tre-kallor-b[78]_v3-paket.json"))):
        d = json.load(open(f, encoding="utf-8"))
        poster = d["poster"]
        info = {n["noteId"]: n for n in
                invoke("notesInfo", notes=[p["noteId"] for p in poster])}

        kvar, utlyfta = [], []
        for p in poster:
            n = info.get(p["noteId"])
            live = baksida.parse(n["fields"][config.FIELD_BAKSIDA]["value"]) if n else {}
            inaktuell = any(p["kort"].get(k) != live.get(k) for k in FALT)
            if not inaktuell:
                kvar.append(p)
                continue
            # Sakerhetskontroll: lyft bara ut kort som FAKTISKT redan ar
            # verifierade nagon annanstans. Ett inaktuellt kort UTAN tagg ar ett
            # verkligt problem och ska stanna kvar sa att spärren fortsatter
            # larma om det.
            har_v3 = any(t.startswith("oberoende_verifierad")
                         for t in (n["tags"] if n else []))
            if har_v3:
                p["utlyft_skal"] = ("kortet omskrivet i en senare batch och redan "
                                    "full v3-verifierat dar; den har domen galler "
                                    "en version som inte langre finns")
                utlyfta.append(p)
            else:
                kvar.append(p)

        d["poster"] = kvar
        if utlyfta:
            d.setdefault("ersatta_av_senare_batch", []).extend(utlyfta)
        json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("%-24s %2d kvar, %2d utlyfta (%s)"
              % (os.path.basename(f).split("_")[-2], len(kvar), len(utlyfta),
                 ", ".join(p["ord"] for p in utlyfta) or "-"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
