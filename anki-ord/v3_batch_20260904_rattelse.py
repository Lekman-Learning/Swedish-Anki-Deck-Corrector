# -*- coding: utf-8 -*-
"""Rattar de 5 kort blindgranskaren fallde eller anmarkte pa (2026-09-04).
Alla fem gallde SO:s definitionstillagg eller en synonym av fel ordklass."""
import io, json
FIL = "sessions/session_2026-09-04_v3-batch.json"
B = lambda o: '<font color="#3498db">%s</font>' % o

FIX = {
# UNDERKANDA
"sprätta": dict(
  hb="Krafsa så att smått yr omkring ; stänka och yra iväg, om små partiklar ; "
     "stoltsera och visa upp sig ; skära upp något med kniv",
  reg="neutral, neutral ; neutral, neutral ; neutral, lätt negativ ; neutral, neutral",
  grp=[["krafsa","riva"],["skvätta"],["≈≈ skryta"],["skära upp","öppna"]],
  ex="Fettet %s i stekpannan." % B("sprätte"),
  add=" RÄTTAT efter blindgranskning: SO:s definitionstillägg <<om små partiklar>> saknades "
      "på betydelse 2. Utan det läste sig 'fara iväg med fart' som att en PERSON rusar iväg "
      "— och synonymen skvätta, som bara går ihop med partikelbetydelsen, pekade då åt ett "
      "annat håll än definitionen. Exempelmeningen bytt till partikelfallet."),
"hysa": dict(
  hb="Ge någon tak över huvudet ; ha plats för ; placera något någonstans ; "
     "bära på en känsla inom sig",
  reg="neutral, neutral ; neutral, neutral ; neutral, neutral ; neutral, neutral",
  grp=[["ge husrum"],["innesluta","rymma"],["≈≈ placera"],["känna","ha"]],
  ex="Hon %s fortfarande ett agg mot honom." % B("hyser"),
  add=" RÄTTAT efter blindgranskning: SO har FYRA betydelser med egen definition — den "
      "transitiva '(låta) placera' (hysa något någonstans) saknades och är inte samma sak "
      "som lokalens 'ha rum för'. Dessutom var '≈≈ husrum' ett SUBSTANTIV satt som kategori "
      "för ett VERB och kunde aldrig sättas in i ordets plats; SAOL:s glosa är verbfrasen "
      "'ge husrum åt', som nu används."),
# GODKANDA MED ANMARKNING - lagas anda
"friställa": dict(
  hb="Säga upp folk för att jobbet tagit slut, sagt på ett snyggare sätt ; "
     "göra något ledigt att använda",
  reg="neutral, eufemistisk ; fackspråklig, neutral",
  grp=[["≈≈ avskeda"],["≈≈ frigöra"]],
  ex="Fabriken %s fyrtio anställda när ordern uteblev." % B("friställde"),
  add=" RÄTTAT efter blindgranskning: SO:s definitionstillägg <<p.g.a. brist på "
      "arbetstillfällen>> är precis det som skiljer friställa från avskeda — orsaken ligger "
      "hos företaget, inte hos den anställde. Tillagt i både definition och exempel."),
"asocial": dict(
  hb="Bryter mot samhällets grundregler ; vill inte umgås med andra",
  reg="neutral, negativ ; neutral, neutral",
  grp=[["avvikande"],["≈≈ tillbakadragen"]],
  ex="Skadegörelsen dömdes som %s och farlig." % B("asocial"),
  add=" RÄTTAT efter blindgranskning: SO märker betydelse 2 'någon gång äv.', alltså "
      "ovanlig. Exempelmeningen illustrerade just den ovanliga betydelsen; bytt till "
      "huvudbetydelsen, som är den HP faktiskt testar."),
"synkron": dict(
  hb="Sker samtidigt ; går i exakt samma takt och fas",
  reg="neutral, neutral ; fackspråklig, neutral, fysik",
  grp=[["samtidig"],["≈≈ i fas"]],
  ex="Ljudet låg inte %s med bilden." % B("synkront"),
  add=" RÄTTAT efter blindgranskning: SO säger 'spec. i fysikaliska sammanhang'; domänen "
      "ändrad från teknik till fysik."),
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    f = FIX.get(e["ord"])
    if not f:
        continue
    e["proposed"]["huvudbetydelse"] = f["hb"]
    e["proposed"]["register"] = f["reg"]
    e["proposed"]["synonym_groups"] = f["grp"]
    e["proposed"]["synonymer"] = [s for g in f["grp"] for s in g]
    e["proposed"]["exempelmening"] = f["ex"]
    e["sokkoll"]["slutsats"] += f["add"]
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"rattade {n} kort")
