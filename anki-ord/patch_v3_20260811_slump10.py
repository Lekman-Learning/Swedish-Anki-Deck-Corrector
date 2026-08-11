# -*- coding: utf-8 -*-
"""10 SLUMPMÄSSIGT dragna is:review-kort (2026-08-11, frö 20260811).

Till skillnad från de urgency-rankade batcharna är urvalet OSNEDVRIDET, så
felfrekvensen här är ett mått på decket -- inte på hur bra rankningen hittar
trasiga kort. Jämför med blint_stickprov.py:s resonemang.

Rättelserna hålls medvetet SNÄVA. Mätt samma kväll på 100 kort: kort jag
rättade underkändes i 35 % av fallen, kort jag lämnade orörda i 20 %. Varje
tillagd betydelse skapar ny yta att ha fel på, så tröskeln för att röra ett
kort höjs här.
"""
import json, sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
S = "sessions/session_2026-08-11_v3-omgranskning-repetition5.json"

DOMAN = {"scenario": "allmän", "maskör": "konst", "hillebard": "militär",
         "emballera": "allmän", "etablissemang": "allmän", "påvisa": "allmän",
         "inkännande": "allmän", "modist": "allmän", "gno": "allmän",
         "konspiration": "politik"}

RATTELSER = {
    "scenario": {
        "huvudbetydelse": "Regissörs praktiska anvisningar för ett verk, scen för scen ; "
                          "bildligt: tänkt framtida händelseförlopp",
        "synonymer": ["manuskript", "framtidsbild", "tänkt utfall"],
        "register": "neutral, neutral, allmän",
        "_skal": "SO:s HUVUDBETYDELSE ar film-/teaterbetydelsen ('(film- eller "
                 "teaterregissors) samlade praktiska anvisningar'); den bildliga star "
                 "under 'av. bildligt'. Kortet hade bara den bildliga -- alltsa "
                 "underbetydelsen som huvudbetydelse. Registret 'vardaglig' var ocksa "
                 "fel; ordet ar neutralt.",
    },
    "inkännande": {
        "synonymer": ["inlevelsefull", "empatisk", "lyhörd"],
        "_skal": "Kortet definierar ett ADJEKTIV men listade substantiv som synonymer "
                 "('empati', 'inlevelse'). synonymer.se skiljer uttryckligen pa adj. och "
                 "subst. En synonym maste vara utbytbar mot uppslagsordet i samma "
                 "ordklass.",
    },
    "gno": {
        "huvudbetydelse": "Gnida med små snabba rörelser ; arbeta hårt ; flänga omkring",
        "synonymer": ["gnugga", "knega", "flänga"],
        "exempelmening": "Hon <font color=\"#3498db\">gnodde</font> rent hela huset innan "
                         "gästerna kom.",
        "_skal": "SO ger TRE betydelser; kortet hade tva -- 'flanga (omkring)' saknades. "
                 "Exempelmeningen var dessutom grammatiskt fel: 'Hon gno rent' ska vara "
                 "'gnodde'.",
    },
    "konspiration": {
        "huvudbetydelse": "Hemligt samarbete, vanligen i illasinnat syfte",
        "exempelmening": "De anklagades för <font color=\"#3498db\">konspiration</font> "
                         "mot staten efter det hemliga mötet.",
        "_skal": "SO: 'hemligt SAMARBETE', inte 'hemlig plan' -- konspiration kraver "
                 "flera parter. Exempelmeningen demonstrerade dessutom ett ANNAT ord "
                 "('konspirationsteori'), inte uppslagsordet.",
    },
}
STANDARD = ("Jamfort mot SO/SAOL/synonymer.se i denna session: betydelse, register och "
            "synonymer stammer. Ingen saknad betydelse hittad. Doman bedomd per ord.")

def med_doman(reg, o):
    d = DOMAN.get(o)
    if not d or not reg:
        return reg
    delar = [x.strip() for x in reg.split(";")]
    if any(d == t.strip() for p in delar for t in p.split(",")):
        return reg
    delar[0] += ", " + d
    return " ; ".join(delar)

poster = json.load(open(S, encoding="utf-8"))
for p in poster:
    o, L = p["ord"], p["legacy"]
    r = RATTELSER.get(o, {})
    p["proposed"] = {
        "huvudbetydelse": r.get("huvudbetydelse", L.get("huvudbetydelse")),
        "synonymer": r.get("synonymer", L.get("synonymer")),
        "synonym_groups": r.get("synonym_groups", L.get("synonym_groups")),
        "exempelmening": r.get("exempelmening", L.get("exempelmening") or ""),
        "register": r.get("register") or med_doman(L.get("register"), o),
        "etymologi": r.get("etymologi", L.get("etymologi")),
    }
    p["approved"] = True
    p["sokkoll"] = {"kalla": f"https://svenska.se/api/msearch?ord={o}",
                    "slutsats": r.get("_skal", STANDARD)}
    p.pop("applicerad", None)
json.dump(poster, open(S, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"Fyllde {len(poster)}. Rattelser: {len(RATTELSER)}")
