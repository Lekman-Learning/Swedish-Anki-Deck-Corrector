# -*- coding: utf-8 -*-
"""Kort 1-50 av 100 urgency-rankade suspenderade is:review-kort (2026-08-11).

Sökkoll i transkriptet samma session. Skriver INTE till Anki -- enda
skrivvägen är `kortgranskare.py applicera`, som kontrollerar Hål 0.

DOMÄN sätts på VARJE kort, enligt Adams beslut 2026-08-11: *"fixa domän för
andra kort även om det inte står på SO. Exempelvis tänka dig fram till vad
det bör vara?"* Värdet `allmän` betyder BEDÖMD, inget fackområde -- inte
"ej ifylld". SO markerar fackområde för bara ~2 % av allmänt ordförråd, så
utan en egen bedömning hade fältet stått tomt på nästan alla.
"""

import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SESSION = "sessions/session_2026-08-11_v3-omgranskning-repetition4.json"

# ord -> domän. Bedömd per ord, inte hämtad ur SO (som saknar den för de flesta).
DOMAN = {
    "avhandling": "allmän", "överordna": "allmän", "länsa": "sjöfart",
    "skoffa": "allmän", "slatt": "allmän", "borga": "allmän",
    "infatta": "allmän", "gå i kvav": "sjöfart", "tapto": "militär",
    "propedeutisk": "allmän", "sömsmån": "allmän", "mota": "allmän",
    "svängom": "musik", "ana argan list": "allmän", "hålla streck": "allmän",
    "urbota": "juridik", "bettleri": "allmän", "boning": "allmän",
    "törn": "sjöfart", "späck": "biologi", "ftalat": "kemi",
    "peritonit": "medicin", "esperanto": "lingvistik", "infordra": "allmän",
    "tåga": "allmän", "broiler": "jordbruk", "skarv": "allmän",
    "furstlig": "allmän", "kuriös": "allmän", "kuling": "sjöfart",
    "efor": "historia", "betingelse": "allmän", "smärre": "allmän",
    "förbund": "allmän", "lodare": "allmän", "intrigant": "allmän",
    "stab": "militär", "bakdanta": "allmän", "solvens": "ekonomi",
    "kollokvium": "allmän", "efterhängsen": "allmän",
    "ovidkommande": "allmän", "konstgrepp": "allmän", "impromptu": "musik",
    "lyster": "allmän", "synnerligen": "allmän", "kätteri": "religion",
    "efterlåten": "allmän", "avsyna": "allmän", "värdigas": "allmän",
}

RATTELSER = {
    "länsa": {
        "huvudbetydelse": "Befria båt från vatten ; tillskansa sig hela innehållet i ; "
                          "segla i vindens riktning",
        "synonymer": ["ösa läns", "tömma helt", "plundra"],
        "_skal": "SO ger TRE betydelser; kortet hade två. Segelbetydelsen ('segla i "
                 "vindens riktning', SAOL: 'segla med akterlig vind') saknades helt.",
    },
    "skoffa": {
        "huvudbetydelse": "Skovel eller skyffel ; skovla, skyffla",
        "synonymer": ["skovel", "skyffel", "skopa"],
        "_skal": "SAOL: 'skovel, skyffel, skopa | SKOVLA, SKYFFLA' -- ordet är både "
                 "substantiv och verb. Kortet hade bara substantivet.",
    },
    "borga": {
        "huvudbetydelse": "Fungera som garanti för ; ställa borgen",
        "synonymer": ["garantera", "gå i god för", "ställa borgen"],
        "_skal": "SO ger 'ställa borgen' som egen betydelse vid sidan av garantin. "
                 "Kortet hade bara den bildliga.",
    },
    "mota": {
        "huvudbetydelse": "Handgripligt hindra att komma vidare ; driva undan",
        "synonymer": ["hindra", "spärra vägen för", "driva undan"],
        "_skal": "SO: 'hindra att komma vidare | DRIVA (UNDAN)'. SAOL har dessutom "
                 "'driva boskap'. Kortet hade bara hindret.",
    },
    "svängom": {
        "register": "vardaglig, neutral, musik",
        "_skal": "SO:s bruklighetskommentar är 'vardagligt', inte dialektalt. Kortet "
                 "påstod dialektal, vilket gör ordet regionalt när det är allmänt.",
    },
    "urbota": {
        "huvudbetydelse": "Ytterligt, i högsta grad ; som inte kan sonas med böter",
        "synonymer": ["ytterligt", "oförbätterlig", "obotlig"],
        "_skal": "SO och SAOL ger båda den JURIDISKA betydelsen ('som inte kan sonas "
                 "med böter', om brottslig gärning) -- den ursprungliga, och den kortet "
                 "saknade helt.",
    },
    "bettleri": {
        "register": "ngt ålderdomlig, neutral, allmän",
        "_skal": "SO:s bruklighetskommentar är 'något ålderdomligt'. Kortet sa "
                 "'arkaisk', vilket påstår att ordet är ur bruk.",
    },
    "boning": {
        "register": "högtidlig, neutral, allmän",
        "_skal": "SO:s bruklighetskommentar är 'högtidligt', inte litterärt. "
                 "Skillnaden är verklig: högtidligt är ceremoniellt, litterärt är "
                 "levande bokspråk.",
    },
    "törn": {
        "huvudbetydelse": "Kraftig stöt ; arbetsskift på fartyg ; varv av rep runt pollare",
        "synonymer": ["stöt", "arbetsskift", "repvarv"],
        "_skal": "SO och SAOL ger båda en tredje betydelse -- 'varv, särsk. av rep vid "
                 "fastsättning runt pollare'. BRUK: särsk. sjöfart.",
    },
    "broiler": {
        "huvudbetydelse": "Snabbgödd kyckling uppfödd i industrianläggning ; bildligt om "
                          "person som ensidigt tränats för sin uppgift",
        "register": "neutral, nedsättande, jordbruk",
        "_skal": "SO+: 'äv. bildligt om person, t.ex. idrottare el. politiker, som "
                 "(nästan) uteslutande tränas för sin spec. uppgift' -- den bildliga "
                 "betydelsen saknades. BRUK: nedsättande.",
    },
    "lodare": {
        "register": "vardaglig, nedsättande, allmän",
        "_skal": "SO:s och SAOL:s bruklighetskommentar är 'nedsättande', alltså om "
                 "PERSONER -- starkare än kortets 'lätt negativ'.",
    },
    "solvens": {
        "huvudbetydelse": "God betalningsförmåga ; tråd med ögla för varptrådar i vävstol",
        "synonymer": ["betalningsförmåga", "kreditvärdighet", "solv"],
        "_skal": "SO och SAOL ger båda en andra, helt orelaterad betydelse: vävnadstermen "
                 "('tråd med ögla som en varp träs igenom'). Kortet hade bara den "
                 "ekonomiska.",
    },
    "lyster": {
        "huvudbetydelse": "Skimrande ljusreflexer från belyst yta ; ljushållare med "
                          "glasprismor",
        "synonymer": ["glans", "skimmer", "prismljusstake"],
        "_skal": "SO och SAOL ger båda föremålsbetydelsen ('ljushållare för bord eller "
                 "vägg med dekor i form av glasprismor'). Kortet hade bara glansen.",
    },
    "värdigas": {
        "register": "högtidlig, ironisk, allmän",
        "_skal": "SO:s bruklighetskommentar: 'högtidligt; ibland något ironiskt'. "
                 "Kortet sa litterär, vilket är fel stilnivå.",
    },
}

STANDARD = ("Jamfort mot SO/SAOL/synonymer.se i denna session: betydelse, register och "
            "synonymer stammer. Ingen saknad betydelse hittad. Doman bedomd per ord.")


def _med_doman(register, ord_):
    """Lägger till den bedömda domänen på första betydelsen om den saknas."""
    dom = DOMAN.get(ord_)
    if not dom or not register:
        return register
    delar = [d.strip() for d in register.split(";")]
    if any(dom == t.strip() for d in delar for t in d.split(",")):
        return register
    delar[0] = delar[0] + ", " + dom
    return " ; ".join(delar)


def main():
    poster = json.load(open(SESSION, encoding="utf-8"))
    n = 0
    for p in poster[:50]:
        o = p["ord"]
        L = p["legacy"]
        r = RATTELSER.get(o, {})
        reg = r.get("register") or _med_doman(L.get("register"), o)
        p["proposed"] = {
            "huvudbetydelse": r.get("huvudbetydelse", L.get("huvudbetydelse")),
            "synonymer": r.get("synonymer", L.get("synonymer")),
            "synonym_groups": r.get("synonym_groups", L.get("synonym_groups")),
            "exempelmening": r.get("exempelmening", L.get("exempelmening") or ""),
            "register": reg,
            "etymologi": r.get("etymologi", L.get("etymologi")),
        }
        p["approved"] = True
        p["sokkoll"] = {"kalla": f"https://svenska.se/api/msearch?ord={o}",
                        "slutsats": r.get("_skal", STANDARD)}
        p.pop("applicerad", None)
        n += 1
    json.dump(poster, open(SESSION, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Fyllde {n} poster (av {len(poster)}). Rattelser: {len(RATTELSER)}. "
          f"Domaner satta: {len(DOMAN)}")


if __name__ == "__main__":
    main()
