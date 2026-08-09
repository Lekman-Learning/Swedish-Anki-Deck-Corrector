"""Slår upp många ord i SAOL/SO/SAOB på en gång, utanför agentens kontextfönster.

BAKGRUND. Adam 2026-08-09: *"finns det något jag kan göra så att du gör alla 20,
och inte bara 7?"* Diagnosen: taket är inte kvoten (15 kort kostade 4 % av ett
femtimmarsfönster) utan **kontextfönstret**. Varje kort krävde två
webbläsaranrop vars svar sedan ligger kvar i kontexten hela sessionen. Tjugo kort
= fyrtio anrop = slut på utrymme långt före slut på kvot.

Det här skriptet gör uppslagningen i EN process i stället. Tjugo ord blir ett
verktygsanrop och en kompakt sammanfattning, i stället för fyrtio svar.

HUR BEVISKEDJAN HÅLLER. Hål 0 bygger på att `kalla` måste peka på en hämtning som
finns i ett vittne agenten inte kan skriva i. Med webbläsaren var vittnet
`browser_navigate`-anropets `input.url` i transkriptet. Här är vittnet i stället
**skriptets utskrift**: raden

    SVENSKA_SE_HAMTAD <ord> HTTP <status> <byte>

skrivs av processen, fångas av verktygslagret och hamnar i transkriptet och i
`raw-verktyg/`. Agenten kan formulera kommandot men inte hitta på dess utdata.
Egenskapen som gör Hål 0 meningsfull är alltså bevarad: **det går inte att påstå
en hämtning som inte gjordes.**

Vad skriptet INTE skyddar mot är detsamma som förut: att jag hämtar rätt sida och
ändå läser den fel. Det är vad `verdikt` finns för.

ANVÄNDNING
    python slaupp.py ord1 ord2 ...
    python slaupp.py --fil kvar.json --antal 20

Full JSON per ord sparas i `uppslag/<ord>.json` så att en senare granskare kan
läsa exakt vad källan sa, inte bara min sammanfattning.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

API = "https://svenska.se/api/msearch"
UTKAT = "uppslag"
INDEX = {"saol": "sa-svenska-saol", "so": "sa-svenska-so", "saob": "sa-svenska-saob"}


def _kropp(ord_):
    return {"debugDidYouMean": False,
            **{k: {"index": v, "query": ord_, "exact_match": True,
                   "from": 0, "size": 30} for k, v in INDEX.items()}}


def hamta(ord_, forsok=3):
    """Returnerar (data, status, byte). Kastar aldrig — fel rapporteras."""
    data = json.dumps(_kropp(ord_)).encode()
    hdr = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0",
           "Origin": "https://svenska.se", "Referer": "https://svenska.se/"}
    for n in range(forsok):
        try:
            with urllib.request.urlopen(
                    urllib.request.Request(API, data=data, headers=hdr), timeout=25) as r:
                rå = r.read()
                return json.loads(rå), r.status, len(rå)
        except urllib.error.HTTPError as e:
            return None, e.code, 0
        except Exception:
            if n == forsok - 1:
                return None, 0, 0
            time.sleep(1.5 * (n + 1))
    return None, 0, 0


def _text(x):
    """Plockar ut ren text ur SO:s/SAOL:s HTML-fragment."""
    if x is None:
        return ""
    if isinstance(x, list):
        return " ; ".join(_text(i) for i in x if i)
    if isinstance(x, dict):
        return _text(x.get("value") or x.get("text") or "")
    return re.sub(r"\s{2,}", " ", re.sub(r"<[^>]+>", "", str(x))).strip()


def _plocka(kalla, nycklar):
    ut = []
    def gå(n):
        if isinstance(n, dict):
            for k, v in n.items():
                if k in nycklar:
                    t = _text(v)
                    if t:
                        ut.append(t)
                gå(v)
        elif isinstance(n, list):
            for v in n:
                gå(v)
    gå(kalla)
    return ut


def sammanfatta(data):
    """Kompakt sammandrag — det agenten behöver läsa, inte hela svaret."""
    s = {}
    for bok in ("saol", "so"):
        träffar = (((data or {}).get(bok) or {}).get("hits") or {}).get("hits") or []
        if not träffar:
            s[bok] = None
            continue
        källa = [t.get("_source", {}) for t in träffar[:2]]
        s[bok] = {
            "def": _plocka(källa, {"definition", "def", "huvudbetydelse", "betydelse",
                                   "explanation", "grundbetydelse"})[:6],
            "exempel": _plocka(källa, {"exempel", "example", "idiom", "syntex"})[:4],
            "jfr": _plocka(källa, {"jfr", "se", "hänvisning", "synonym"})[:6],
            "märkning": _plocka(källa, {"stilmarkering", "bruklighet", "markering",
                                        "stil", "anvandning"})[:4],
        }
    return s


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ord", nargs="*")
    p.add_argument("--fil", help="JSON-lista eller {relearn:[],ovriga:[]}")
    p.add_argument("--antal", type=int, default=20)
    p.add_argument("--hoppa", type=int, default=0)
    a = p.parse_args()

    ord_ = list(a.ord)
    if a.fil:
        d = json.load(open(a.fil, encoding="utf-8"))
        if isinstance(d, dict):
            d = d.get("relearn", []) + d.get("ovriga", [])
        ord_ += d
    ord_ = ord_[a.hoppa:a.hoppa + a.antal]
    if not ord_:
        sys.exit("inga ord")

    os.makedirs(UTKAT, exist_ok=True)
    sammandrag = {}
    for o in ord_:
        data, status, byte = hamta(o)
        # ---- BEVISRADEN. Skrivs av processen, inte av agenten. ----
        print(f"SVENSKA_SE_HAMTAD {o} HTTP {status} {byte}")
        if data is None:
            sammandrag[o] = {"FEL": f"HTTP {status}"}
            continue
        sh = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:12]
        json.dump({"ord": o, "url": API, "status": status, "sha": sh, "svar": data},
                  open(os.path.join(UTKAT, f"{o}.json"), "w", encoding="utf-8"),
                  ensure_ascii=False)
        sammandrag[o] = sammanfatta(data)
        time.sleep(0.3)

    print("---SAMMANDRAG---")
    print(json.dumps(sammandrag, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
