# -*- coding: utf-8 -*-
"""Rattar forgranska.py:s 25 harda anmarkningar pa del 1.
Synonymer: bara ord som INLEDER ett led i SO/SAOL:s definition. Ovriga
ersatta med `≈≈ kategori` (far hamtas ur kortets egen definition)."""
import io, json
FIL = "sessions/session_2026-09-04_v3-batch.json"
U = "utvidgningar utan egen definition i SO:s rastruktur, inte skilda betydelser"

G = {  # ord -> (synonym_groups, forgranska_tillat)
"sprätta":   ([["krafsa","riva"],["skvätta"],["≈≈ skryta"],["skära upp","öppna"]],
              {"betydelse_kan_saknas": "SO:s 9 ar 4 DEF plus 5 " + U +
               ". Alla fyra DEF finns pa kortet."}),
"bastion":   ([["≈≈ befästning"]],
              {"betydelse_kan_saknas": "SO:s andra post ar en utvidgning utan egen "
               "definition. SAOL ger bara den historiska betydelsen."}),
"buffert":   ([["stötdämpare"],["≈≈ skydd"]],
              {"betydelse_kan_saknas": "SO: 1 DEF + 4 unders, varav bara 'foretelse som "
               "mildrar yttre paverkan' har egen definition. Bada finns pa kortet."}),
"butter":    ([["vresig","sur"]],
              {"betydelse_kan_saknas": "SO:s andra post ar " + U + "."}),
"edikt":     ([["påbud","kungörelse"]], None),
"famna":     ([["omsluta"],["≈≈ täcka in"]], None),
"fariseism": ([["≈≈ hyckleri"]], None),
"fiffla":    ([["smussla"]], None),
"hurts":     ([["sidoskåp","underskåp"]],
              {"betydelse_kan_saknas": "SO:s andra post ar " + U + "."}),
}
# Kort dar ratt atgard ar att LAGGA TILL betydelsen, inte kvittera bort den
NYA_BET = {
"funtad": dict(
  hb="Skruvad på ett visst sätt i huvudet ; byggd eller gjord på ett visst sätt",
  grp=[["beskaffad"],["≈≈ konstruerad"]],
  ex='Hur är man <font color="#3498db">funtad</font> om man tycker det där är kul?',
  extra=" SO:s underbetydelse har EGEN definition ('som har de grundlaggande egenskaperna "
        "som framgar av sammanhanget') och ar alltsa en riktig betydelse — tillagd."),
"hysa": dict(
  hb="Ge någon tak över huvudet ; rymma och innehålla ; bära på en känsla inom sig",
  grp=[["≈≈ husrum"],["innesluta","rymma"],["känna","ha"]],
  ex='Hon <font color="#3498db">hyser</font> fortfarande ett agg mot honom.',
  extra=" SAOL delar med semikolon i tre led: 'ge husrum at; innesluta, rymma' och "
        "'ha, kanna'. Tredje betydelsen tillagd."),
"hägna": dict(
  hb="Sätta stängsel runt något ; utgöra själva avgränsningen ; skydda och värna",
  grp=[["≈≈ stängsla"],["≈≈ avgränsa"],["skydda","värna"]],
  ex='Föreningen vill <font color="#3498db">hägna</font> om de sista strandängarna.',
  extra=" SO:s underbetydelse 'utgora avgransning' har egen definition (om stangslet "
        "sjalvt, inte handlingen) — tillagd som tredje betydelse."),
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    o = e["ord"]
    if o in G:
        grp, tillat = G[o]
        e["proposed"]["synonym_groups"] = grp
        e["proposed"]["synonymer"] = [s for g in grp for s in g]
        if tillat:
            e["forgranska_tillat"] = tillat
        n += 1
    elif o in NYA_BET:
        f = NYA_BET[o]
        e["proposed"]["huvudbetydelse"] = f["hb"]
        e["proposed"]["synonym_groups"] = f["grp"]
        e["proposed"]["synonymer"] = [s for g in f["grp"] for s in g]
        e["proposed"]["exempelmening"] = f["ex"]
        e["sokkoll"]["slutsats"] += f["extra"]
        n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"rattade {n} kort")
