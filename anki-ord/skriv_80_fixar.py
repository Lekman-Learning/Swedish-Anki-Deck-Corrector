# -*- coding: utf-8 -*-
"""80-kortsomgangen 2026-08-25: rattelser efter forgranskningen.

Kors EFTER del1-del4. Patchar sessionsfilen pa plats.

TVA SORTERS RATTELSE:

1. `betydelse_kan_saknas` som ar falsk. Kontrollerat mot SO:s RASTRUKTUR via
   visa_uppslag.py, aldrig mot sammandraget -- sammandraget dubbelraknar. I
   samtliga fall nedan har SO EN huvudbetydelse och EN underbetydelse vars
   `definition` ar None, alltsa en anvandningsutvidgning och inte en betydelse
   kortet saknar. Visaren skriver ut dem som
   "under: (ingen egen definition -- utvidgning)".

2. `register_motsager_markning` dar markningen ar ett AMNESOMRADE, inte en
   bruklighet. Registerfaltet har tre positioner per betydelsegrupp
   (formalitet, valens, doman) och grupper skiljs med semikolon. Domanen
   saknades -- den laggs till har i stallet for att viftas bort.
"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-25_v3-batch2.json"

_UTVIDGNING = (
    "Kontrollerat mot SO:s rastruktur via visa_uppslag.py: EN huvudbetydelse "
    "och EN underbetydelse vars `definition` ar None. En underbetydelse utan "
    "egen definition ar en anvandningsutvidgning av betydelsen ovanfor, inte "
    "en egen betydelse. Kortet saknar alltsa ingenting."
)

TILLAT = {
 "rotting": {"betydelse_kan_saknas": _UTVIDGNING},
 "regim": {"betydelse_kan_saknas": _UTVIDGNING},
 "urkund": {"betydelse_kan_saknas": _UTVIDGNING},
 "alternera": {"betydelse_kan_saknas": _UTVIDGNING},
 "antagonist": {"betydelse_kan_saknas": _UTVIDGNING},
 "irreal": {"betydelse_kan_saknas": _UTVIDGNING},
 "prospektera": {"betydelse_kan_saknas": _UTVIDGNING},
 "sedeslös": {"betydelse_kan_saknas": _UTVIDGNING},
 "ymnighetshorn": {"betydelse_kan_saknas": _UTVIDGNING},

 "skrävel": {"betydelse_kan_saknas":
   "SO har EN huvudbetydelse ('storordigt skryt') utan underbetydelser. SAOL:s "
   "'storskryt' ar samma betydelse med ett annat ord, inte en andra."},
 "kurvatur": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('bagformighet') och EN underbetydelse "
   "MED egen definition ('bojt eller krokt parti av nagot'). Bada star pa "
   "kortet. Trean kommer av att SAOL:s 'krokning, buktighet' raknas separat."},
 "allena": {"register_motsager_markning":
   "Markningen ar 'ald. utom i nagra uttr.'. Kortets register sager 'ngt "
   "alderdomlig', vilket ar exakt vad 'ald.' betyder. Flaggan slar pa orden "
   "'utom', 'nagra' och 'uttr' -- alltsa pa reservationen, inte pa "
   "bruklighetsangivelsen sjalv."},
 "förment": {"frammande_uppslagsord":
   "Traffen `formena` ar verbet som `forment` ar perfekt particip av. Samma "
   "lemma, annan form."},
 "kor": {"frammande_uppslagsord":
   "Traffen `ko` ar ett annat lemma (notkreatur) vars PLURAL rakar stavas som "
   "kortordet. SO listar `kor` (kyrkans altarrum) som eget uppslag."},
}

# Amnesomraden som ska in i registrets tredje position i stallet for att
# viftas bort. Format per grupp: "formalitet, valens, doman", grupper med ";".
REGISTER = {
 "elliptisk": "neutral, neutral; neutral, neutral, språkvetenskap",
 "antites": "fackspråklig, neutral, filosofi",
 "irreal": "fackspråklig, neutral, filosofi",
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    t = r = 0
    for e in poster:
        o = e["ord"]
        if o in TILLAT:
            e.setdefault("forgranska_tillat", {}).update(TILLAT[o])
            t += 1
        if o in REGISTER and e.get("proposed"):
            e["proposed"]["register"] = REGISTER[o]
            r += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"tillat tillagda: {t}   register rattade: {r}")


if __name__ == "__main__":
    main()
