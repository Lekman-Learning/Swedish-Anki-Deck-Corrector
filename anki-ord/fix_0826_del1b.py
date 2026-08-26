# -*- coding: utf-8 -*-
import json

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}

EXTRA = {
    "girland": {
        "frammande_uppslagsord":
            "Det enda främmande uppslagsordet är girlang — SAOL:s och SO:s sidoform av samma "
            "ord (SO-exemplen växlar: girlanger till midsommarstången). Inte ett annat ord, "
            "alltså ingen risk att glosorna hör till fel uppslag.",
        "betydelse_kan_saknas":
            "SO:s andra post är markören äv. något utvidgat, inte en egen betydelse — den täcker "
            "girlang av kulörta lyktor, vilket ryms i kortets formulering av blommor eller löv "
            "som hänger i mjuka bågar. En enda betydelse är rätt.",
    },
    "i onåd": {
        "frammande_uppslagsord":
            "De 44 träffarna kommer av att uppslaget gjordes på flerordsuttrycket i onåd; "
            "svenska.se fuzzy-matchar då varje ord för sig och drar in hela i-, ingen- och "
            "intet-serien. Känd artefakt i slaupp.py (dokumenterad 2026-08-11). Kortets innehåll "
            "är uteslutande hämtat ur SO:s och SAOL:s artikel för onåd — SO: överordnad persons "
            "missnöje, exempel han föll i onåd hos makthavarna; SAOL: ogunst, exempel falla i onåd. "
            "Ingen glosa kommer från något av de andra uppslagen.",
    },
    "karda": {
        "betydelse_kan_saknas":
            "SO:s fjärde post är markören äv. bildligt till verbet, inte en egen betydelse. "
            "Kortets tre — redskapet, verbet och den vardagliga hand — är samtliga betydelser "
            "som SAOL självständigt räknar upp.",
    },
}

n = 0
for o, d in EXTRA.items():
    BY[o].setdefault("forgranska_tillat", {}).update(d)
    n += 1

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Motiveringar tillagda på %d kort." % n)
