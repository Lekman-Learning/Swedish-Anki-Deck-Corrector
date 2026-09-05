# -*- coding: utf-8 -*-
"""Rattar de 6 kort som underkandes i blindgranskningen 2026-09-04."""
import io, json
FIL = "sessions/session_2026-09-04_v3-batch.json"
B = lambda o: '<font color="#3498db">%s</font>' % o

FIX = {
# --- underkanda av MINA-granskarna (kort jag skrev) ---
"famna": dict(
  hb="Sluta armarna om någon ; rymma och täcka in ett helt område",
  reg="litterär, neutral ; litterär, neutral",
  grp=[["omsluta"],["≈≈ täcka in"]],
  ex="Boken %s hela efterkrigstiden på trehundra sidor." % B("famnar"),
  add=" RÄTTAT: registret hade axlarna omkastade — litterär ar en STILNIVA "
      "(REGISTER_FORMALITY), inte en valor. neutral, litterar var alltsa formellt "
      "giltigt men semantiskt fel; ratt ordning ar litterar, neutral per betydelse."),
"fariseism": dict(
  hb="Att spela from utåt och samtidigt känna sig förmer än andra",
  reg="formell, negativ",
  grp=[["≈≈ hyckleri"]],
  ex="Talet om solidaritet var ren %s." % B("fariseism"),
  ety="efter fariséerna i Nya testamentet, kända för yttre regelfromhet",
  add=" RÄTTAT: SO sager hycklande OCH SJALVGOD installning — tva skilda egenskaper. "
      "Kortet hade bara hyckleriet; sjalvgodheten (att kanna sig former) saknades helt "
      "och ar nu med."),
"obändig": dict(
  hb="Går inte att tygla eller trycka ner",
  reg="neutral, neutral",
  grp=[["≈≈ oböjlig"]],
  ex="Hon hade en %s vilja att vinna." % B("obändig"),
  add=" RÄTTAT: valdsam och vild STAR i SAOL:s kommalista men ar inte utbytbara i den "
      "betydelse SO ger (som inte later sig paverkas och undertryckas) — en valdsam vilja "
      "ar inte svenska. Ordboksbelagg ar ett golv, inte ett tak; samma feltyp som "
      "projektets mor/sprod-fall. Ersatta med en kategori ur kortets egen definition."),
"workshop": dict(
  hb="Träff där en liten grupp delar kunskap kring ett bestämt tema, ofta inom forskning eller konst",
  reg="neutral, neutral",
  grp=[["kollokvium","≈≈ möte"]],
  ex="Institutionen ordnar en %s om källkritik i november." % B("workshop"),
  add=" RÄTTAT: SO:s definitionstillagg <<inom ett visst tema; sarsk. i vetenskapliga el. "
      "konstnarliga sammanhang>> saknades HELT, samtidigt som kortet lade till jobbar "
      "praktiskt, som varken SO eller SAOL sager. Den obligatoriska nyansen var alltsa "
      "utbytt mot en pahittad. Bada delarna atgardade."),
# --- underkanda av mig (kort skrivaragenten skrev) ---
"fraktion": dict(
  hb="Grupp inom ett parti som driver en egen linje ; del som skilts ut ur en kemisk blandning",
  reg="neutral, neutral, politik ; fackspråklig, neutral, kemi",
  grp=[["meningsgrupp"],["delmängd"]],
  ex="En %s inom partiet krävde att ledaren skulle avgå." % B("fraktion"),
  add=" RÄTTAT: kortet sa utbrytargrupp och exemplet fullbordade utbrytningen. SO sager "
      "grupp I politiskt parti, SAOL meningsgrupp INOM parti — en fraktion ar kvar i "
      "partiet, och upphor att vara en fraktion nar den bryter sig ur. Bade definition "
      "och exempel omskrivna."),
"frifräsare": dict(
  hb="Frispråkigt radikal person som varken följer partilinjen eller god ton",
  reg="vardaglig, neutral",
  grp=[["≈≈ radikal"]],
  ex="Han var partiets %s och röstade emot sin egen ledning." % B("frifräsare"),
  add=" RÄTTAT: SO och SAOL sager bada ordagrant frispråkigt RADIKAL person. Kortet hade "
      "bara frispråkigheten — den halvan som inte ar sarskiljande — och missade radikalismen "
      "helt, aven i kategorin. Bada halvorna ar nu med."),
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
    if f.get("ety"):
        e["proposed"]["etymologi"] = f["ety"]
    e["sokkoll"]["slutsats"] += f["add"]
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"rattade {n} kort")
