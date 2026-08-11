# -*- coding: utf-8 -*-
"""Kort 51-100 av 100 urgency-rankade suspenderade is:review-kort (2026-08-11).

Sökkoll i transkriptet samma session. Domän bedöms per ord (Adams beslut).

TVÅ KORT HAR EGEN KÄLLA, inte svenska.se:
* `sobriquet` -- saknas i alla tre ordböckerna; vilar på synonymer.se:s
  REDAKTIONELLA post (Adams källregel 2026-08-11).
* `anhedoni` -- saknas också, och synonymer.se har bara ett användarbidrag
  som dessutom är fel ("livströtthet"). Belagt via websökning mot NE och
  Svensk MeSH i samma session.

Digesten för båda är dessutom fuzzy-fel (`sobriquet` -> sobel/mårddjur,
`anhedoni` -> anhalt/hållplats) och får inte läsas som källa.
"""

import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SESSION = "sessions/session_2026-08-11_v3-omgranskning-repetition4.json"

DOMAN = {
    "kria": "allmän", "baggböleri": "jordbruk", "adenit": "medicin",
    "transitera": "militär", "dille": "allmän", "fäbless": "allmän",
    "anrättning": "matlagning", "fältspat": "geologi", "förborga": "allmän",
    "bejaka": "allmän", "tara": "ekonomi", "apoteos": "religion",
    "agorafobi": "medicin", "myriad": "allmän", "hypokondri": "medicin",
    "emissarie": "politik", "affekterad": "allmän", "faksimil": "allmän",
    "spoliera": "allmän", "gemmologi": "geologi", "gejd": "teknik",
    "skändlig": "allmän", "livsbejakande": "allmän", "sobriquet": "allmän",
    "galge": "allmän", "invand": "allmän", "förmedelst": "allmän",
    "inmänga": "allmän", "agremanger": "allmän", "paria": "historia",
    "späcka": "matlagning", "förhärska": "allmän", "gengångare": "allmän",
    "samfällighet": "juridik", "anhedoni": "medicin", "arkaisera": "lingvistik",
    "vara tillstädes": "allmän", "lyfta på förlåten": "allmän",
    "bautasten": "historia", "andemening": "allmän",
    "antecedentier": "allmän", "rissel": "jordbruk", "lågsint": "allmän",
    "parkett": "allmän", "malja": "allmän", "intrikat": "allmän",
    "heuristik": "filosofi", "ornat": "religion", "tillvita": "allmän",
    "öronmärka": "allmän",
}

EGEN_KALLA = {
    "sobriquet": "https://www.synonymer.se/sv-syn/sobriquet",
    "anhedoni": "https://www.ne.se/uppslagsverk/skola/article/anhedoni",
}

RATTELSER = {
    "kria": {
        "huvudbetydelse": "Skoluppsats över ett bestämt ämne ; numera om text med "
                          "förenklade resonemang och dålig stil",
        "synonymer": ["skoluppsats", "övningsuppsats", "skolmässig text"],
        "_skal": "SO+: 'numera vanligen om text i allmänhet, ofta med antydan om dålig "
                 "stil, förenklade resonemang' -- den nutida, nedsättande betydelsen "
                 "saknades, och det är den som faktiskt används i dag.",
    },
    "bejaka": {
        "huvudbetydelse": "Svara ja på ; vara positiv till, välkomna",
        "synonymer": ["bekräfta", "acceptera", "välkomna"],
        "_skal": "SO ger 'vara positiv till, välkomna' som egen betydelse (vanligen "
                 "bildligt). Det är den vanligaste användningen och saknades.",
    },
    "agorafobi": {
        "synonymer": ["torgskräck", "platsångest", "rädsla för öppna platser"],
        "_skal": "Synonymen 'social fobi' var sakligt fel -- social fobi är rädsla för "
                 "att bli bedömd av andra, agorafobi är rädsla för platser man inte kan "
                 "fly från. SO/SAOL ger 'torgskräck'.",
    },
    "affekterad": {
        "huvudbetydelse": "Som uppträder överdrivet och tillgjort ; (medicin) påverkad, "
                          "angripen",
        "synonymer": ["tillgjord", "konstlad", "angripen"],
        "_skal": "SAOL ger 'påverkad' med bruklighetskommentaren 'med.' -- den "
                 "medicinska betydelsen (om organ: angripen) saknades helt.",
    },
    "livsbejakande": {
        "register": "neutral, positiv, allmän",
        "_skal": "Kortet sa 'vardaglig'. Ordet är stilistiskt neutralt och tydligt "
                 "POSITIVT laddat, vilket valören inte fångade.",
    },
    "inmänga": {
        "register": "ngt ålderdomlig, neutral, allmän",
        "_skal": "SO:s bruklighetskommentar är 'ngt åld.', inte litterär.",
    },
    "agremanger": {
        "register": "ngt ålderdomlig, neutral, allmän",
        "_skal": "SO: 'mindre brukligt | ngt åld.'. Kortet sa formell, vilket antyder ett "
                 "levande byråkratiskt ord.",
    },
    "gengångare": {
        "huvudbetydelse": "Död människa som tänks gå igen ; bildligt om otidsenlig "
                          "person eller företeelse",
        "synonymer": ["spöke", "vålnad", "kvarleva från förr"],
        "_skal": "SO+: 'ibland bildligt om otidsenlig person el. företeelse'. Den "
                 "bildliga betydelsen saknades.",
    },
    "anhedoni": {
        "huvudbetydelse": "Oförmåga att känna njutning och glädje",
        "synonymer": ["lustlöshet", "glädjelöshet"],
        "register": "fackspråklig, neutral, medicin",
        "_skal": "NE och Svensk MeSH (Karolinska): 'oförmåga att uppleva njutning, nöje "
                 "och glädje', grekiska 'utan njutning'. Kortets 'glädje' var för smalt "
                 "-- njutningen är kärnan. Synonymen 'apati' var FEL: apati är brist på "
                 "motivation, anhedoni är att njutningen uteblir. OBS: OLD-facit "
                 "('livströtthet') och synonymer.se:s användarbidrag är båda felaktiga.",
    },
    "intrikat": {
        "register": "formell, neutral, allmän",
        "_skal": "Kortet sa vardaglig; intrikat är ett formellt ord.",
    },
    "heuristik": {
        "huvudbetydelse": "Metod att upptäcka eller bilda ny kunskap",
        "synonymer": ["upptäcktsmetod", "metodlära", "tumregel"],
        "_skal": "SO: 'metod att UPPTÄCKA ELLER BILDA NY (vetenskaplig) kunskap'. "
                 "Kortets 'hitta lösningar genom erfarenhet' beskriver tumregeln, inte "
                 "begreppet -- det handlar om kunskapsbildning, inte om erfarenhet.",
    },
    "öronmärka": {
        "huvudbetydelse": "Märka djur för igenkänning ; noggrant ange användningen av "
                          "en penningsumma",
        "synonymer": ["märka", "reservera", "avsätta"],
        "_skal": "SAOL ger den bokstavliga betydelsen ('märka djur för igenkänning') "
                 "först -- den som gav ordet dess bild. Kortet hade bara den bildliga.",
    },
}

STANDARD = ("Jamfort mot SO/SAOL/synonymer.se i denna session: betydelse, register och "
            "synonymer stammer. Ingen saknad betydelse hittad. Doman bedomd per ord.")


def _med_doman(register, ord_):
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
    for p in poster[50:]:
        o = p["ord"]
        L = p["legacy"]
        r = RATTELSER.get(o, {})
        p["proposed"] = {
            "huvudbetydelse": r.get("huvudbetydelse", L.get("huvudbetydelse")),
            "synonymer": r.get("synonymer", L.get("synonymer")),
            "synonym_groups": r.get("synonym_groups", L.get("synonym_groups")),
            "exempelmening": r.get("exempelmening", L.get("exempelmening") or ""),
            "register": r.get("register") or _med_doman(L.get("register"), o),
            "etymologi": r.get("etymologi", L.get("etymologi")),
        }
        p["approved"] = True
        p["sokkoll"] = {
            "kalla": EGEN_KALLA.get(o, f"https://svenska.se/api/msearch?ord={o}"),
            "slutsats": r.get("_skal", STANDARD),
        }
        p.pop("applicerad", None)
        n += 1
    json.dump(poster, open(SESSION, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Fyllde {n} poster. Rattelser: {len(RATTELSER)}. Domaner: {len(DOMAN)}")


if __name__ == "__main__":
    main()
