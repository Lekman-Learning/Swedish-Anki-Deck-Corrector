# -*- coding: utf-8 -*-
"""Tredje rattelserundan: obandig och fraktion."""
import io, json
FIL = "sessions/session_2026-09-04_v3-batch.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
FIX = {
"obändig": dict(
  hb="Går inte att tygla eller tämja — om en vilja, en kraft eller ett humör",
  reg="neutral, neutral",
  grp=[["vild"]],
  ex="Han hade ett %s humör som ingen fick bukt med." % B("obändigt"),
  add=" TREDJE RUNDAN: de tva granskarna sade EMOT varandra. Den forsta underkande kortet "
      "for att valdsam/vild inte var utbytbara (en vild vilja ar inte svenska); jag tog da "
      "bort dem. Den andra underkande for att de UTELAMNATS ur SAOL:s kommalista, som ar EN "
      "betydelse. Bada hade delvis ratt: ordet bar bade den okuvliga viljan och det "
      "otambara humoret, och felet var att definitionen bara rymde den ena. Definitionen "
      "breddad med SO:s definitionstillagg <<om person el. (vanligen) handling>>, exemplet "
      "flyttat till humoret — dar vild faktiskt ar utbytbart."),
"fraktion": dict(
  hb="Grupp inom ett parti som driver en egen linje, särskilt förr i kommunistiska partier ; "
     "del som skilts ut ur en blandning genom fraktionering",
  reg="neutral, neutral, politik ; fackspråklig, neutral, kemi",
  grp=[["meningsgrupp"],["delmängd"]],
  ex="En %s inom partiet krävde att ledaren skulle avgå." % B("fraktion"),
  add=" TREDJE RUNDAN: bada betydelsernas definitionstillagg saknades — <<sarsk. (mest forr) "
      "i kommunistiskt parti>> och <<genom fraktionering>>. Bada intagna."),
}
poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    f = FIX.get(e["ord"])
    if not f: continue
    e["proposed"]["huvudbetydelse"] = f["hb"]
    e["proposed"]["register"] = f["reg"]
    e["proposed"]["synonym_groups"] = f["grp"]
    e["proposed"]["synonymer"] = [s for g in f["grp"] for s in g]
    e["proposed"]["exempelmening"] = f["ex"]
    e["sokkoll"]["slutsats"] += f["add"]
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"rattade {n}")
