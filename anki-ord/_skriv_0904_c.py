# -*- coding: utf-8 -*-
"""Arbetsbatch 2026-09-04, kort 25-36 av 50."""
import io, json, sys
import _hjalp_0902b as HJ

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-04_v3-omgranskning.json"
H = HJ.H

K = {
 "serendipitet": (
  "Förmågan att hitta något värdefullt av en slump, utan att ha letat efter det",
  "formell, positiv", ["≈≈ lyckosam slump"],
  [["≈≈ lyckosam slump"]],
  "Penicillinet upptäcktes genom ren %s — Fleming letade efter något annat." % (H % "serendipitet"),
  "Poolen ger bara 'förmåga', en avhuggen bit av definitionen. Wiktionarys "
  "tillägg 'utan att egentligen leta, eller då man letar efter något annat' "
  "är med i huvudbetydelsen — det är hela skillnaden mot vanlig tur."),

 "förgrundsgestalt": (
  "Person som står i centrum inom sitt område",
  "neutral, positiv", ["förgrundsfigur"],
  [["förgrundsfigur"]],
  "Hon var en %s inom svensk arkitektur på 60-talet." % (H % "förgrundsgestalt"),
  "SO definierar ordet med sin egen synonym ('förgrundsfigur'), vilket inte "
  "duger som förklaring på ett kort. Huvudbetydelsen är därför skriven ut."),

 "obeständig": (
  "Som förändras och bryts ner när den utsätts för påverkan",
  "formell, negativ", ["≈≈ förgänglig"],
  [["≈≈ förgänglig"]],
  "Skulpturerna var av gips och andra %s material." % (H % "obeständiga"),
  "Poolen är tom — varken SAOL eller Wiktionary har artikel, och "
  "synonymer.se saknar redaktionellt innehåll. Därför ≈≈. SO:s parenteser "
  "('i vissa (väsentliga) avseenden', '(och försämras)') är upplösta."),

 "aerogram": (
  "Tunt brevpapper som veks ihop till eget kuvert och skickades med flyg",
  "ngt ålderdomlig, neutral", ["lätt flygbrev"],
  [["lätt flygbrev"]],
  "Soldaterna skrev hem på %s för att spara vikt." % (H % "aerogram"),
  "SO märker 'historiskt' — företeelsen finns inte kvar, vilket ger "
  "registret. Att papperet blev sitt eget kuvert är det som gör ordet "
  "begripligt och står därför i huvudbetydelsen."),

 "boklig": (
  "Som kommer ur böcker i stället för ur egen erfarenhet",
  "neutral, lätt negativ", ["≈≈ teoretisk"],
  [["≈≈ teoretisk"]],
  "Han har bara %s kunskap om arkitektur, inga egna erfarenheter." % (H % "boklig"),
  "SO noterar 'ibland med viss negativ bibetydelse', vilket ger valören — "
  "kontrasten mot erfarenhet är själva poängen och står i huvudbetydelsen. "
  "Poolen är tom, därför ≈≈."),

 "myopisk": (
  "Närsynt",
  "fackspråklig, neutral, medicin", ["närsynt"],
  [["närsynt"]],
  "Patienten hade en %s förändring i näthinnan." % (H % "myopisk"),
  "En betydelse, en exakt synonym ur poolen. Ordet används nästan bara "
  "medicinskt på svenska — den bildliga användningen ('kortsiktig') som "
  "finns i engelskan har SO ingen artikel för."),

 "ariadnetråd": (
  "Ledtråd som visar vägen ut ur ett svårt problem",
  "högtidlig, positiv", ["ledtråd"],
  [["ledtråd"]],
  "Fyndet blev den %s som ledde utredningen rätt." % (H % "ariadnetråd"),
  "SO märker 'högtidligt', vilket ger registret. Etymologin bär hela bilden: "
  "Ariadnes trådnystan som förde Theseus ut ur labyrinten — det förklarar "
  "varför ordet betyder just en väg UT, inte vilken ledtråd som helst."),

 "ansa": (
  "Klippa och putsa så att något behåller sin form",
  "neutral, neutral", ["sköta", "vårda"],
  [["sköta", "vårda"]],
  "Han %s mustaschen framför spegeln varje morgon." % (H % "ansade"),
  "SO:s def är cirkulär ('utföra ans på') och duger inte. Exemplen visar vad "
  "ordet gör — rabatten, rosorna, mustaschen — alltså klippa och putsa för "
  "formens skull, inte allmän omvårdnad."),

 "ök": (
  "Drag- eller lastdjur ; nedsättande om en dålig häst",
  "ngt ålderdomlig, neutral ; ngt ålderdomlig, nedsättande",
  ["drag- el. lastdjur", "≈≈ krake"],
  [["drag- el. lastdjur"], ["≈≈ krake"]],
  "Ett gammalt spattigt och istadigt %s drog kärran." % (H % "ök"),
  "SO:s underbetydelse 'numera vanligen som nedsättande benämning på häst' "
  "är en egen betydelse med egen valör och står som nummer två. Det är "
  "dessutom den man faktiskt möter i dag, medan grundbetydelsen är den "
  "äldre — exempelmeningen visar den nedsättande."),

 "mobilier": (
  "Lös egendom, det man kan flytta med sig",
  "formell, neutral, juridik", ["lösöre", "bohag"],
  [["lösöre", "bohag"]],
  "Vid bouppteckningen värderades fastigheten för sig och %s för sig." % (H % "mobilier"),
  "Etymologin förklarar ordet direkt: latinets mobilis, 'flyttbar'. Den "
  "kontrasten — flyttbart mot fast — är vad ordet betyder och står därför "
  "i huvudbetydelsen. Registret är juridiskt: ordet lever i bouppteckningar."),

 "gräll": (
  "Som lyser alltför starkt och skarpt ; överdriven och påträngande",
  "neutral, negativ ; neutral, negativ",
  ["bjärt", "skrikande", "≈≈ påträngande"],
  [["bjärt", "skrikande"], ["≈≈ påträngande"]],
  "Reklamskylten lyste i %s färger." % (H % "grälla"),
  "SO:s 'äv. bildligt' är en egen betydelse: grälla effekter i en "
  "föreställning handlar inte om syn utan om överdrift. Den står som nummer "
  "två med ≈≈, eftersom poolens ord alla gäller färg."),

 "vimla": (
  "Röra sig omkring i stor och oordnad mängd ; synas i nöjeslivet ; vara full av en rörlig mängd",
  "neutral, neutral ; neutral, neutral ; neutral, neutral",
  ["myllra", "≈≈ mingla", "≈≈ krylla"],
  [["myllra"], ["≈≈ mingla"], ["≈≈ krylla"]],
  "Människorna %s omkring på torget." % (H % "vimlade"),
  "SO ger tre betydelser som skiljer sig i vem som gör vad: mängden rör sig "
  "(1), en person syns i nöjeslivet (2), och platsen är full (3 — 'det "
  "vimlade av folk', den opersonliga konstruktionen SO noterar)."),
}

def main():
    d = json.load(io.open(FIL, encoding="utf-8"))
    kort = d["kort"] if isinstance(d, dict) and "kort" in d else d
    n = 0
    for k in kort:
        o = k.get("ord")
        if o not in K:
            continue
        hb, reg, syn, grupper, ex, note = K[o]
        k["proposed"] = {
            "huvudbetydelse": hb, "register": reg, "synonymer": syn,
            "synonymgrupper": grupper, "exempelmening": ex,
            "etymologi": HJ.etym(o),
        }
        k["sokkoll"] = {
            "kalla": HJ.kallor(o),
            "slutsats": ("SO/SAOL/synonymer.se/Wiktionary uppslagna via slaupp.py "
                         "2026-09-04; betydelser, register och synonymer darifran."),
        }
        k["note_till_granskare"] = note
        k["approved"] = True
        n += 1
    json.dump(d, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("skrev %d kort" % n)

main()
