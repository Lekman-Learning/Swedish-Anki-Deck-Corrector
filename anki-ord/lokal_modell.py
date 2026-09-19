"""lokal_modell.py -- extraherar kortfakta med en lokal modell via LM Studio.

🔴 LÄS FÖRST: den här vägen är INTE nödvändig för uppslagen. `slaupp.py` skriver
redan nyckeln `sammandrag`, som är 7,6x mindre än hela uppslagsfilen (mätt på
3 712 filer, 2026-09-20) och är ordagrann. `kortfakta.py` skriver ut den gratis.
Skriptet finns för nästa steg: när sammandraget ska kokas ned ytterligare, eller
när flera källor ska vägas ihop till ett förslag.

🔴 SPÄRREN SOM GÖR DET SÄKERT: modellen får bara KOPIERA. Varje sträng den
lämnar ifrån sig kontrolleras mot källtexten, tecken för tecken. Det som inte
finns ordagrant i uppslagsfilen kastas och loggas. En lokal modells
hallucination kan därmed inte nå ett kort.

Kräver: LM Studio igång med servern startad (`lms server start`) och en modell
laddad. Ingen API-nyckel.

    python lokal_modell.py --ping                 # kollar server + modell
    python lokal_modell.py abakus aber            # extraherar, skriver inget
    python lokal_modell.py --fil saknade.json --ut extrakt.jsonl
"""
import argparse
import json
import os
import time
import urllib.request

import kortfakta

BAS = os.environ.get("LOKAL_MODELL_URL", "http://127.0.0.1:1234/v1")
MODELL = os.environ.get("LOKAL_MODELL", "")  # tom = första laddade modellen

SYSTEM = (
    "Du extraherar fält ur svenska ordboksdata. Du får ENDAST kopiera text "
    "ordagrant ur indata. Du får aldrig översätta, omformulera, förkorta, "
    "förklara eller lägga till något. Hittar du inte ett fält lämnar du det "
    "som en tom lista. Svara med enbart JSON enligt schemat."
)

SCHEMA = {
    "type": "object",
    "properties": {
        "ord": {"type": "string"},
        "betydelser": {"type": "array", "items": {"type": "string"}},
        "synonymer": {"type": "array", "items": {"type": "string"}},
        "exempel": {"type": "array", "items": {"type": "string"}},
        "ordklass": {"type": "string"},
    },
    "required": ["ord", "betydelser", "synonymer", "exempel"],
}


def anropa(prompt, temperatur=0.0, max_tokens=700):
    kropp = {
        "messages": [{"role": "system", "content": SYSTEM},
                     {"role": "user", "content": prompt}],
        "temperature": temperatur,
        "max_tokens": max_tokens,
        "response_format": {"type": "json_schema",
                            "json_schema": {"name": "kortfakta", "strict": True, "schema": SCHEMA}},
    }
    if MODELL:
        kropp["model"] = MODELL
    req = urllib.request.Request(BAS + "/chat/completions",
                                 data=json.dumps(kropp).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})
    t = time.time()
    with urllib.request.urlopen(req, timeout=900) as r:
        svar = json.load(r)
    text = svar["choices"][0]["message"]["content"]
    bruk = svar.get("usage", {})
    return json.loads(text), time.time() - t, bruk


def validera(extrakt, kalltext):
    """Kastar allt som inte står ORDAGRANT i källan. Returnerar (rent, kastat)."""
    rent, kastat = {}, []
    for nyckel, varde in extrakt.items():
        if isinstance(varde, list):
            behall = []
            for s in varde:
                (behall if isinstance(s, str) and s and s in kalltext else kastat).append(s)
            rent[nyckel] = behall
        elif isinstance(varde, str):
            # Tomt fält är inte en hallucination -- det är modellen som säger
            # "hittade inget", precis som systemprompten ber om.
            if not varde or varde in kalltext:
                rent[nyckel] = varde
            else:
                kastat.append(varde)
        else:
            rent[nyckel] = varde
    return rent, kastat


def ett_ord(ord_):
    d, hel = kortfakta.sammandrag(ord_)
    if d is None:
        return None
    kalltext = json.dumps(d, ensure_ascii=False)
    prompt = (f"Ordboksdata för ordet \"{ord_}\" som JSON:\n{kalltext}\n\n"
              "Plocka ut betydelser, synonymer, exempelmeningar och ordklass. "
              "Kopiera ordagrant.")
    extrakt, sek, bruk = anropa(prompt)
    rent, kastat = validera(extrakt, kalltext)
    ut_tok = bruk.get("completion_tokens") or 0
    return {"ord": ord_, "extrakt": rent, "kastat": kastat, "sekunder": round(sek, 1),
            "tokens_ut": ut_tok, "tok_per_s": round(ut_tok / sek, 1) if sek > 0.01 else None,
            "in_tecken_hel": hel, "in_tecken_sammandrag": len(kalltext)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ord", nargs="*")
    ap.add_argument("--fil")
    ap.add_argument("--ut")
    ap.add_argument("--ping", action="store_true")
    a = ap.parse_args()

    if a.ping:
        with urllib.request.urlopen(BAS + "/models", timeout=10) as r:
            modeller = [m["id"] for m in json.load(r)["data"]]
        print("server: OK")
        print("modeller:", ", ".join(modeller) or "(ingen laddad)")
        return

    orden = list(a.ord) + (json.load(open(a.fil, encoding="utf-8")) if a.fil else [])
    rader, tot_s, tot_t = [], 0.0, 0
    for o in orden:
        r = ett_ord(o)
        if r is None:
            print(f"{o}: saknar uppslagsfil")
            continue
        rader.append(r)
        tot_s += r["sekunder"]
        tot_t += r["tokens_ut"]
        print(f"{o}: {r['sekunder']} s, {r['tokens_ut']} tokens ut "
              f"({r['tok_per_s']} tok/s), kastade {len(r['kastat'])} strängar")
    if rader:
        takt = f"{tot_t/tot_s:.1f} tokens/s totalt" if tot_s > 0.05 else "för snabbt för att mäta"
        print(f"\n{len(rader)} ord, {tot_s/len(rader):.2f} s/ord, {takt}")
        print(f"kastat totalt: {sum(len(r['kastat']) for r in rader)} strängar "
              "(ej ordagranna -- hade blivit hallucinationer i ett kort)")
    if a.ut and rader:
        with open(a.ut, "w", encoding="utf-8") as f:
            for r in rader:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"skrev {a.ut}")


if __name__ == "__main__":
    main()
