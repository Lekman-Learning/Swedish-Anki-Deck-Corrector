# -*- coding: utf-8 -*-
"""100-kortsomgangen 2026-08-25 (batch3): rattelser efter forgranskningen.

Kors EFTER del1-del5. Patchar sessionsfilen pa plats. Fyra sorters atgard:

1. STRUKNA SYNONYMER (`synonym_utan_ordboksbelagg`). Batch 6 larde att flaggan
   inte bara betyder "tom faltet" -- den betyder ocksa "las om
   huvudbetydelsen", eftersom en synonym utan ordboksbelagg brukar komma fran
   synonymer.se och da kan aven betydelsen vara kontaminerad. Har ar samtliga
   atta fall i stallet ord JAG lade till som naraliggande; betydelserna sjalva
   ar lasta ur SO/SAOL och kontrollerade om.

2. RATTAT REGISTER dar markningen ar en riktig bruklighet. `klamra` ar
   'mindre brukligt' i SO, vilket _MARKNING_LIKA mappar till 'alderdomlig'.
   `ruggig`, `skalk` och `libation` far GRUPPVIS register, eftersom bara EN av
   deras betydelser bar markningen -- formatet ar "formalitet, valens" per
   grupp med ";" mellan grupperna.

3. TILLAGD BETYDELSE dar flaggan hade sakligt ratt. `resignera` hade bara
   SO:s definition; SAOL:s 'finna sig i sitt ode' ar en egen nyans och laggs
   till.

4. WAIVERS dar flaggan dubbelraknar. Sex ord (gendarm, anyo, enveten,
   cerealier, farsot) har EN huvudbetydelse i SO och EN i SAOL, och de ar
   samma betydelse -- flaggan summerar kallorna i stallet for att jamfora dem.
   Kontrollerat post for post mot rastrukturen, inte mot sammandraget.
"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-25_v3-batch3.json"

# --- 1. synonymer att stryka -------------------------------------------
STRYK = {
 "flöjel": {"vindflöjel"},
 "med berått mod": {"avsiktligt"},
 "ånyo": {"återigen"},
 "ypperlig": {"förträfflig"},
 "ge akt på": {"uppmärksamma"},
 "härbärgera": {"inhysa"},
 "knusslig": {"snål"},
 "skalk": {"brödkant"},
}

# --- 2. rattat register ------------------------------------------------
REGISTER = {
 # bara fjarde betydelsen ar vardaglig i SO
 "ruggig": "neutral, neutral; neutral, neutral; neutral, neutral; vardaglig, negativ",
 # bara andra betydelsen ('skalm') ar alderdomlig
 "skalk": "neutral, neutral; ngt ålderdomlig, skämtsam",
 # SO: 'i religiosa sammanhang' pa huvudbetydelsen, 'skamtsamt el. hogtidligt'
 # pa underbetydelsen
 "libation": "högtidlig, neutral, religion; skämtsam, neutral",
 # SO markerar 'mindre brukligt', som _MARKNING_LIKA mappar till alderdomlig
 "klamra": "ngt ålderdomlig, neutral",
}

# --- 3. tillagd betydelse ----------------------------------------------
BETYDELSE = {
 "resignera": ("Efter lång kamp tröttna och inse det omöjliga i att uppnå ett "
               "visst mål ; finna sig i sitt öde"),
}

# --- 4. waivers --------------------------------------------------------
_DUBBEL = ("Flaggan dubbelraknar: SO har EN huvudbetydelse och SAOL EN, och det "
           "ar SAMMA betydelse. Kontrollerat mot rastrukturen via "
           "visa_uppslag.py -- ingen av dem har nagra underbetydelser alls.")

TILLAT = {
 "gendarm": {"betydelse_kan_saknas": _DUBBEL +
   " SO: 'medlem av militart organiserad polis- eller ordningstrupp'. "
   "SAOL: 'medlem av gendarmeri'."},
 "ånyo": {"betydelse_kan_saknas": _DUBBEL +
   " SO: 'pa nytt'. SAOL: 'pa nytt, an en gang'."},
 "enveten": {"betydelse_kan_saknas": _DUBBEL +
   " Bada kallorna ger exakt samma ord: 'envis'."},
 "cerealier": {"betydelse_kan_saknas": _DUBBEL +
   " SO: 'sadesslag'. SAOL: 'produkter av sadesslag'. Kortet har bada leden."},
 "farsot": {"betydelse_kan_saknas": _DUBBEL +
   " Bada kallorna ger exakt samma text: 'epidemisk sjukdom'."},
 "resignera": {"betydelse_kan_saknas":
   "Atgardat i sak i stallet for att viftas bort: SAOL:s 'finna sig i sitt ode' "
   "ar tillagd som andra betydelse pa kortet."},
 "taxa": {"frammande_uppslagsord":
   "Traffen `va-taxa` ar en sammansattning med kortordet som efterled, inte ett "
   "frammande ord. Kortet galler grundordet."},
 "ledig": {"register_motsager_markning":
   "Markningen 'mest som kommandoord' sitter pa en UNDERBETYDELSE utan egen "
   "definition (militarens 'Lediga!') och ar en anvandningsnot, inte en "
   "bruklighet. Kortets fyra betydelser ar alla neutrala."},
 "ge akt på": {"register_motsager_markning":
   "Markningen 'mest historiskt' sitter pa `akt` betydelse 1 ('fredloshet i "
   "medeltida germansk ratt'), som inte har nagot med uttrycket att gora. "
   "Uttrycket star som idiom under betydelse 2 ('uppmarksamhet'), omarkt."},
 "illegitim": {"register_motsager_markning":
   "Markningen 'alderdomligt' galler ENBART underbetydelsen 'fodd utom "
   "aktenskapet', och kortet skriver ut '(alderdomligt)' framfor just den. "
   "Huvudbetydelsen ar omarkt."},
 "lavoar": {"register_motsager_markning":
   "Markningen 'finl.' sitter pa SAOL:s ANDRA led ('modernt tvattstall'), som "
   "kortet medvetet utelamnar som regional anvandning. Kortets betydelse ar "
   "SO:s huvudbetydelse, som ar omarkt men beskriver ett aldre foremal."},
 "libation": {"register_motsager_markning":
   "Bada markningarna ar nu inskrivna i registret gruppvis: 'hogtidlig, "
   "neutral, religion' for dryckesoffret och 'skamtsam, neutral' for "
   "dryckeslaget."},
 "ruggig": {"register_motsager_markning":
   "Markningen 'vardagligt' galler SO:s TREDJE huvudbetydelse ('skrammande och "
   "obehaglig'). Registret ar nu gruppvis och satter 'vardaglig' pa just den "
   "gruppen."},
 "skalk": {"register_motsager_markning":
   "Markningen 'alderdomligt' galler ENBART betydelsen 'skalm'. Registret ar nu "
   "gruppvis: 'neutral, neutral' for brodkanten, 'ngt alderdomlig, skamtsam' "
   "for skalmen."},
 "klamra": {"register_motsager_markning":
   "Atgardat i sak: SO:s markning 'mindre brukligt' motsvarar valvets "
   "'alderdomlig' enligt _MARKNING_LIKA, och kortets register ar andrat till "
   "'ngt alderdomlig, neutral'."},
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    s = r = b = t = 0
    for e in poster:
        o = e["ord"]
        p = e.get("proposed")
        if o in STRYK and p:
            fore = list(p.get("synonymer") or [])
            p["synonymer"] = [x for x in fore if x not in STRYK[o]]
            if len(p["synonymer"]) != len(fore):
                s += 1
        if o in REGISTER and p:
            p["register"] = REGISTER[o]
            r += 1
        if o in BETYDELSE and p:
            p["huvudbetydelse"] = BETYDELSE[o]
            b += 1
        if o in TILLAT:
            e.setdefault("forgranska_tillat", {}).update(TILLAT[o])
            t += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"synonymer strukna: {s}   register rattade: {r}   "
          f"betydelser utokade: {b}   tillat tillagda: {t}")


if __name__ == "__main__":
    main()
