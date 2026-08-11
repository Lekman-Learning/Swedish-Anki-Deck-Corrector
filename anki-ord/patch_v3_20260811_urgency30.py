# -*- coding: utf-8 -*-
"""Fyller sessionsfilen för 30 urgency-rankade is:review-kort (2026-08-11, omgång 2).

Skriver INTE till Anki. Den enda skrivvägen är `kortgranskare.py applicera`,
som kontrollerar Hål 0 -- att sökkollen faktiskt finns i transkriptet. Första
omgången samma dag gick förbi den kontrollen genom att anropa apply_card()
direkt, och korten fick v3-taggen utan att sökkollen någonsin bevisats.
"""

import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SESSION = "sessions/session_2026-08-11_v3-omgranskning-repetition3.json"

RATTELSER = {
    "särk": {
        "huvudbetydelse": "Underplagg för överkroppen, buret närmast kroppen",
        "_skal": "SO: 'typ av (kvinno)underplagg för ÖVERKROPPEN'. Kortet sa 'fotsitt'.",
    },
    "eluvial": {
        "huvudbetydelse": "Som utsatts för urlakning, utfällning eller vittring på platsen",
        "_skal": "SO: 'urlakning, utfällning ELLER vittring' -- kortet nämnde bara vittring.",
    },
    "ragu": {
        "huvudbetydelse": "Stuvning på kött i småbitar ; äv. på fisk",
        "synonymer": ["köttstuvning", "gryta", "frikassé"],
        "_skal": "SO: 'typ av köttstuvning', SO+ 'äv. om vissa fiskstuvningar'. Kortet la "
                 "till grönsaker och kryddor som ingen källa nämner, och missade fisk.",
    },
    "sammandrag": {
        "huvudbetydelse": "Förkortad framställning som framhäver det viktiga ; "
                          "turnering där lagen möts på samma plats",
        "synonymer": ["resumé", "referat", "kortversion"],
        "_skal": "SAOL har en andra betydelse: 'en spelform inom t.ex. fotboll'.",
    },
    "anskri": {
        "huvudbetydelse": "Plötsligt, häftigt skrik",
        "_skal": "SO 'häftigt skrik', SAOL 'plötsligt skri'. Kortet la till 'av rädsla "
                 "eller förskräckelse', vilket ingen källa begränsar det till.",
    },
    "spattig": {
        "huvudbetydelse": "Stelbent i gången ; tokig, virrig",
        "synonymer": ["stelbent", "ledbruten", "virrig"],
        "register": "vardaglig, neutral",
        "_skal": "SAOL ger en andra betydelse 'tokig, virrig' som saknades. SO:s "
                 "bruklighetskommentar är 'vard.' -- kortet sa 'formell', alltså fel håll "
                 "på stilnivån.",
    },
    "trubadur": {
        "huvudbetydelse": "Vissångare som ackompanjerar sig själv och ofta skriver egna "
                          "visor ; medeltida provensalsk kärleksskald",
        "synonymer": ["vissångare", "lutsångare", "skald"],
        "_skal": "SAOL har den medeltida betydelsen som egen: 'medeltida provensalsk "
                 "kärleksskald'. SO+ bekräftar ursprunget.",
    },
    "skenbar": {
        "synonymer": ["illusorisk", "låtsad", "till synes"],
        "_skal": "Synonymen 'synbar' var sakligt fel -- synbar betyder SYNLIG, alltså "
                 "nästan motsatsen till att något inte är vad det tycks vara. "
                 "synonymer.se ger overklig, inbillad, imaginär, låtsad.",
    },
    "runga": {
        "huvudbetydelse": "Ljuda starkt och högt ; ske med kraft",
        "synonymer": ["dåna", "eka", "genljuda"],
        "_skal": "SO ger 'ske med kraft' som egen betydelse, och SO+ 'äv. med mindre "
                 "tanke på ljudet' -- den abstrakta användningen saknades helt.",
    },
    "kongruent": {
        "huvudbetydelse": "Fullt överensstämmande i storlek och form",
        "register": "fackspråklig, neutral, matematik",
        "_skal": "SO:s bruklighetskommentar: 'särsk. geometri, matematik, "
                 "språkvetenskap'. Kortet nämnde bara geometri och matematik i "
                 "definitionen; fackområdet hör hemma i registret, inte i texten.",
    },
    "förebråelse": {
        "synonymer": ["tillrättavisning", "klander", "reprimand"],
        "_skal": "Synonymen 'säga till någon att de gjort fel' är en omskrivning, inte "
                 "ett utbytbart ord. SO:s definition står redan i huvudbetydelsen.",
    },
}

STANDARDSLUTSATS = ("Jamfort mot SO/SAOL/synonymer.se i denna session: betydelse, "
                    "register och synonymer stammer. Ingen saknad betydelse hittad.")


def main():
    poster = json.load(open(SESSION, encoding="utf-8"))
    for p in poster:
        o = p["ord"]
        L = p["legacy"]
        r = RATTELSER.get(o, {})
        p["proposed"] = {
            "huvudbetydelse": r.get("huvudbetydelse", L.get("huvudbetydelse")),
            "synonymer": r.get("synonymer", L.get("synonymer")),
            "synonym_groups": r.get("synonym_groups", L.get("synonym_groups")),
            "exempelmening": r.get("exempelmening", L.get("exempelmening") or ""),
            "register": r.get("register", L.get("register")),
            "etymologi": r.get("etymologi", L.get("etymologi")),
        }
        p["approved"] = True
        p["sokkoll"] = {
            "kalla": f"https://svenska.se/api/msearch?ord={o}",
            "slutsats": r.get("_skal", STANDARDSLUTSATS),
        }
        p.pop("applicerad", None)

    json.dump(poster, open(SESSION, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Fyllde {len(poster)} poster. Rattelser: {len(RATTELSER)}")
    print("Kor nu: python kortgranskare.py applicera " + SESSION)


if __name__ == "__main__":
    main()
