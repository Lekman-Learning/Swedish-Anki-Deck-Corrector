# -*- coding: utf-8 -*-
"""Rattar tva saker jag hade fel pa i hela batch3, bada fangade av sparrarna.

1. REGISTRET. Jag skrev fri text ("neutral", "fackspraklig, medicin",
   "nagot alderdomlig"). Formatet ar last: VARJE betydelse kraver bade en
   stilniva-tagg OCH en valor-tagg, ur config.REGISTER_FORMALITY /
   REGISTER_VALENS / REGISTER_DOMAN. Flera av mina domantaggar fanns inte
   ens i vokabularen (zoologi, motesteknik, transport, sjukvard, bokhistoria,
   hantverk).

2. KALLAN. `kalla` maste innehalla en URL som ocksa finns som vittne i
   sokkoll-transkriptet -- fri text duger inte (sokkoll_verifiering.py).
   URL:erna hamtas darfor ur uppslag/<ord>.json:s `urler`-falt, alltsa
   exakt de adresser slaupp.py faktiskt anropade, i stallet for att jag
   konstruerar dem for hand.
"""
import io, json, os

FIL = "sessions/session_2026-08-29_v3-batch3.json"

# stilniva, valor, doman -- per betydelse, ' ; ' mellan betydelser
REG = {
    "kurant": "neutral, neutral, ekonomi ; neutral, neutral, allmän ; neutral, neutral, allmän",
    "cerat": "neutral, neutral, medicin",
    "definition": "neutral, neutral, allmän",
    "knaper": "vardaglig, neutral, allmän",
    "beting": "neutral, neutral, ekonomi ; neutral, neutral, allmän ; fackspråklig, neutral, sjöfart",
    "betänklig": "neutral, negativ, allmän",
    "biennal": "neutral, neutral, konst",
    "deliciös": "högtidlig, positiv, allmän",
    "eminent": "neutral, positiv, allmän ; formell, neutral, allmän",
    "enväldig": "neutral, neutral, politik",
    "graciös": "neutral, positiv, allmän",
    "ihållande": "neutral, neutral, allmän",
    "justera": "neutral, neutral, teknik ; fackspråklig, neutral, allmän ; vardaglig, neutral, sport",
    "karg": "neutral, neutral, allmän ; neutral, lätt negativ, allmän",
    "märglös": "neutral, negativ, allmän",
    "siesta": "neutral, neutral, allmän",
    "skiljaktig": "neutral, neutral, allmän",
    "tjäle": "neutral, neutral, geologi",
    "abstraktion": "neutral, neutral, filosofi ; neutral, neutral, filosofi",
    "alligator": "neutral, neutral, biologi",
    "angränsande": "neutral, neutral, allmän",
    "avtrubba": "neutral, lätt negativ, allmän",
    "belamra": "neutral, lätt negativ, allmän",
    "blemma": "neutral, neutral, medicin",
    "bräcklig": "neutral, neutral, allmän ; neutral, ömsint, allmän",
    "bärsärk": "neutral, neutral, historia ; vardaglig, negativ, allmän",
    "eutanasi": "fackspråklig, neutral, medicin",
    "fosgen": "fackspråklig, neutral, kemi",
    "förebrå": "neutral, negativ, allmän",
    "förrätta": "formell, neutral, allmän",
    "gagn": "formell, positiv, allmän",
    "gunstig": "ngt ålderdomlig, positiv, allmän ; neutral, positiv, allmän",
    "infektiös": "fackspråklig, neutral, medicin",
    "inkunabel": "fackspråklig, neutral, historia",
    "kolli": "fackspråklig, neutral, allmän",
    "konkubin": "ngt ålderdomlig, neutral, historia",
    "limes": "fackspråklig, neutral, matematik",
    "magistral": "neutral, nedsättande, allmän ; neutral, positiv, allmän",
    "okynnig": "neutral, ömsint, allmän",
    "penetrera": "neutral, neutral, allmän ; formell, neutral, allmän",
    "proposition": "fackspråklig, neutral, politik ; fackspråklig, neutral, allmän",
    "ritsa": "neutral, neutral, teknik",
    "slagfärdig": "neutral, positiv, allmän",
    "stick i stäv": "neutral, neutral, allmän",
    "triage": "fackspråklig, neutral, medicin",
    "vite": "fackspråklig, neutral, juridik",
}


def urler(ord_):
    """De adresser slaupp.py faktiskt anropade for ordet."""
    p = os.path.join("uppslag", ord_ + ".json")
    if not os.path.exists(p):
        return []
    d = json.load(io.open(p, encoding="utf-8"))
    u = d.get("urler") or {}
    med = set(d.get("kallor_med_innehall") or [])
    # ta med svenska.se alltid (den ar alltid anropad), ovriga bara med innehall
    ut = []
    for namn, adress in u.items():
        if namn == "svenska.se" or namn in med:
            ut.append(adress)
    return ut


def main():
    d = json.load(io.open(FIL, encoding="utf-8"))
    import baksida
    nreg = nurl = 0
    fel = []
    for k in d:
        o = k["ord"]
        p = k.get("proposed")
        if p and o in REG:
            w = baksida.validate_register(REG[o])
            if w:
                fel.append((o, w))
                continue
            p["register"] = REG[o]
            nreg += 1
        if k.get("sokkoll"):
            us = urler(o)
            if us:
                k["sokkoll"]["kalla"] = (
                    "Hämtat 2026-08-29 (HTTP 200) från: " + " · ".join(us))
                nurl += 1
    if fel:
        for o, w in fel:
            print("🔴 REGISTER FEL", o, w)
        raise SystemExit("avbryter -- ratta registret forst")
    json.dump(d, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("register satta :", nreg)
    print("kallor med URL :", nurl)


if __name__ == "__main__":
    main()
