# -*- coding: utf-8 -*-
import json

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}

# svarighetskoll: "officiell" ar sjalvt ett kort. Omskrivning, inte synonymbyte.
BY["enrollera"]["proposed"]["huvudbetydelse"] = \
    "Skriva in någon i en lista över medlemmar eller soldater"

TILLAT = {
    "changemang": {"betydelse_kan_saknas":
        "SO:s fem poster är tre betydelser plus två spec.-markörer. Kortet har den allmänna "
        "(snabb synlig förändring) och den som SAOL lyfter fram (scenväxling), sammanförda i en "
        "formulering. Den tredje — ombyte av galopp i språnget — är en ridsportterm som är för "
        "smal för ett ordförrådskort och skulle dra fokus från ordets kärna."},
    "demaskera": {"betydelse_kan_saknas":
        "SO:s tredje post är markören ofta bildligt. Båda betydelserna — ta av masken och avslöja "
        "— finns på kortet, i samma ordning som SAOL."},
    "determinism": {"betydelse_kan_saknas":
        "SO:s två definitioner är samma lära i vid och snäv form (varje skeende är "
        "orsaksbetingat; allt är förutbestämt och viljan inte fri), plus en markör. Kortets "
        "formulering — allt som händer är bestämt i förväg av det som hänt innan — täcker båda."},
    "diskurs": {"betydelse_kan_saknas":
        "SO:s tre poster är en definition (samtal) plus två markörer: spec. språkvetenskapligt om "
        "uppbyggnaden av samtal och texter, och ofta äv. om förhärskande ideologi. Kortets andra "
        "led — sättet man pratar och tänker om ett ämne — täcker just dem."},
    "enrollera": {"betydelse_kan_saknas":
        "SO:s andra post är markören numera allmännare, ofta med tonvikt på att vederbörande blir "
        "medlem. Kortets formulering nämner både medlemmar och soldater och täcker därmed både den "
        "militära och den allmänna användningen."},
    "epidermis": {"betydelse_kan_saknas":
        "SO:s andra post är markören äv. om liknande skikt hos växter. Kortet gäller hudlagret, "
        "vilket är ordets kärnbetydelse och den enda SAOL sätter först."},
    "filolog": {"betydelse_kan_saknas":
        "SO:s tre poster är två definitioner plus markören förr äv. allmännare. Den andra "
        "(språkvetare, lingvist) är kortets belagda synonym, inte en skild betydelse — samma yrke "
        "med ett annat ord."},
}

for o, d in TILLAT.items():
    BY[o].setdefault("forgranska_tillat", {}).update(d)

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("enrollera omskriven. Motiveringar på %d kort." % len(TILLAT))
