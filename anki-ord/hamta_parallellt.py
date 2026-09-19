"""hamta_parallellt.py -- kör slaupp.py i flera processer över en lång ordlista.

Bakgrund (2026-09-20): 6 385 ord saknade uppslag. I ett spår tar det timmar,
eftersom nästan all tid är väntan på nätverket. Skriptet delar listan i N delar
och kör en `slaupp.py` per del.

🔴 VARFÖR DET INTE BARA ÄR "SNABBARE": `slaupp.py`s egen kommentar dokumenterar
att Wikimedia strypte anropen till HTTP 429 efter ett tiotal ord, och att en 429
såg ut som "ordet finns inte i Wiktionary". Fler processer = fler anrop per
sekund mot samma värd. Därför:

  * `--delar` styr hur många processer som körs (standard 3).
  * Varje process får sin egen delfil; uppslag/<ord>.json är en fil per ord,
    så processerna skriver aldrig i samma fil.
  * 🔴 `tre_kallor_saknas.json` (bristlistan) skrivs av VARJE process vid
    avslut, med läs-ändra-skriv. Sista processen vinner. Därför skriver det här
    skriptet om den från uppslagsfilerna efteråt, med `bristlista_bygg.py`.
  * Kör alltid ett litet testpass först (`--delar 3 --antal 50`) och jämför
    andelen ord som fick alla tre källorna mot ett enkelspårigt pass.

    python hamta_parallellt.py saknade_uppslag.json --delar 3
    python hamta_parallellt.py saknade_uppslag.json --delar 3 --antal 50   # test
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time

HAR = os.path.dirname(os.path.abspath(__file__))
OTILLATNA = re.compile(r'[\\/:*?"<>|]')


def har_uppslag(o):
    return os.path.exists(os.path.join(HAR, "uppslag", OTILLATNA.sub("_", o) + ".json"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fil")
    ap.add_argument("--delar", type=int, default=3)
    ap.add_argument("--antal", type=int, help="ta bara de N första orden (testpass)")
    a = ap.parse_args()

    orden = json.load(open(a.fil, encoding="utf-8"))
    orden = [o for o in orden if not har_uppslag(o)]
    if a.antal:
        orden = orden[:a.antal]
    if not orden:
        print("inget att hämta -- alla ord har redan uppslag")
        return

    # Varannan-fördelning i stället för block: delarna blir lika stora även om
    # listan är sorterad och orden i ena änden är dyrare att hämta.
    delar = [orden[i::a.delar] for i in range(a.delar)]
    katalog = os.path.join(HAR, "_parallellt")
    os.makedirs(katalog, exist_ok=True)

    procs = []
    start = time.time()
    for i, del_ in enumerate(delar):
        f = os.path.join(katalog, f"del{i}.json")
        json.dump(del_, open(f, "w", encoding="utf-8"), ensure_ascii=False)
        logg = open(os.path.join(katalog, f"del{i}.log"), "w", encoding="utf-8")
        p = subprocess.Popen([sys.executable, "-X", "utf8", "slaupp.py", "--fil", f, "--tyst"],
                             cwd=HAR, stdout=logg, stderr=subprocess.STDOUT)
        procs.append((i, p, logg, len(del_)))
        print(f"del {i}: {len(del_)} ord, pid {p.pid}")

    print(f"\n{len(orden)} ord i {a.delar} processer. Följ med:  "
          f"python hamta_parallellt.py {a.fil} --antal 0 2>nul  (eller räkna filer i uppslag/)")
    for i, p, logg, n in procs:
        p.wait()
        logg.close()
        print(f"del {i} klar ({n} ord), kod {p.returncode}")

    klara = sum(1 for o in orden if har_uppslag(o))
    sek = time.time() - start
    print(f"\n{klara}/{len(orden)} ord fick en uppslagsfil på {sek/60:.1f} min "
          f"({sek/max(1,klara):.2f} s/ord)")
    print("🔴 Kör nu:  python bristlista_bygg.py   (parallella körningar skriver över varandras bristlista)")


if __name__ == "__main__":
    main()
