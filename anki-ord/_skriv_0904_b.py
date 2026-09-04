# -*- coding: utf-8 -*-
"""Arbetsbatch 2026-09-04, kort 13-24 av 50."""
import io, json, sys
import _hjalp_0902b as HJ

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-04_v3-omgranskning.json"
H = HJ.H

K = {
 "knollrig": (
  "Med små, täta lockar",
  "neutral, neutral", ["smålockig"],
  [["smålockig"]],
  "Han hade tjockt, %s svart hår." % (H % "knollrigt"),
  "En betydelse, en synonym ur poolen. SO ger 'smålockig' rakt av."),

 "histrion": (
  "Enkel skådespelare",
  "ngt ålderdomlig, lätt negativ", ["skådespelare", "enklare skådespelare"],
  [["skådespelare", "enklare skådespelare"]],
  "Truppen bestod av kringresande %s utan fast scen." % (H % "histrioner"),
  "SO märker ordet 'något ålderdomligt', vilket står i registret. Valören är "
  "lätt negativ: SO:s parentes '(enklare) skådespelare' är en nedvärdering, "
  "inte en neutral avgränsning."),

 "tillkortakommande": (
  "Brist eller svaghet som leder till misslyckande",
  "formell, negativ", ["misslyckande"],
  [["misslyckande"]],
  "Rapporten pekade ut flera %s hos myndigheten." % (H % "tillkortakommanden"),
  "SO:s parentes '(svaghet eller brist som leder till) misslyckande' är "
  "upplöst i huvudbetydelsen — parentesen bär hela skillnaden mot ett vanligt "
  "misslyckande och ska inte gömmas."),

 "förhärda": (
  "Göra någon kall och okänslig ; förhärda sig — göra sig okänslig",
  "formell, negativ ; formell, negativ",
  ["≈≈ förråa", "vara hård och okänslig"],
  [["≈≈ förråa"], ["vara hård och okänslig"]],
  "Modern bad och grät, men han %s sig." % (H % "förhärdade"),
  "SO markerar 'ofta refl.' och SAOL ger två former: den transitiva ('göra "
  "hård') och den reflexiva ('vara hård och okänslig'). Den reflexiva är den "
  "Adam möter — därför står den i exempelmeningen. Poolen ger bara 'vara', "
  "ett fragment, så första gruppen får ≈≈."),

 "holism": (
  "Uppfattningen att helheten är mer än summan av delarna",
  "fackspråklig, neutral, filosofi", ["≈≈ helhetssyn"],
  [["≈≈ helhetssyn"]],
  "Inom %s studeras systemet som helhet, inte del för del." % (H % "holismen"),
  "Poolen ger bara 'teori', en kategori utan innehåll. SAOL:s formulering "
  "('helheten är mer än summan av delarna') är kortare och tydligare än "
  "SO:s och används i huvudbetydelsen."),

 "bräm": (
  "Bred kant på ett klädesplagg ; ytterkant på en fjäder eller ett blomhylle",
  "neutral, neutral ; fackspråklig, neutral, biologi",
  ["kant", "bård"],
  [["kant", "bård"], ["≈≈ ytterkant"]],
  "Kappan hade ett %s av mörk päls runt halsen." % (H % "bräm"),
  "SO ger två betydelser: plaggets kant och den biologiska. Den andra är "
  "märkt biologi i registret. 'bård' och 'kant' kommer ur SAOL via poolen; "
  "den biologiska gruppen får ≈≈ eftersom poolen inte täcker den."),

 "burgen": (
  "Välbärgad sedan lång tid tillbaka",
  "ngt ålderdomlig, positiv", ["välbärgad"],
  [["välbärgad"]],
  "Hon växte upp i ett %s ämbetsmannahem från slutet av 1800-talet." % (H % "burget"),
  "SO märker 'mest vid beskrivning av äldre förhållanden' — det ger registret "
  "och förklarar varför ordet nästan alltid står i historisk text. SO:s "
  "parentes '(sedan gammalt)' är med i huvudbetydelsen: det är skillnaden mot "
  "'rik', som kan vara nyvunnet."),

 "girera": (
  "Föra över pengar från ett konto till ett annat",
  "fackspråklig, neutral, ekonomi", ["överföra genom giro"],
  [["överföra genom giro"]],
  "Han %s medlemsavgiften till föreningen." % (H % "girerade"),
  "Poolens 'överföra' ensamt är för brett — man kan överföra vad som helst. "
  "Den fullständiga formen ur SAOL används i stället."),

 "bonbonjär": (
  "Skål med lock för konfekt",
  "neutral, neutral", ["konfektskål med lock"],
  [["konfektskål med lock"]],
  "På bordet stod en %s i slipat glas." % (H % "bonbonjär"),
  "Locket är med i huvudbetydelsen eftersom det är det som skiljer en "
  "bonbonjär från en vanlig godisskål — SO skriver ut det, SAOL inte."),

 "diger": (
  "Som har stort omfång ; förr även om människor: tjock",
  "neutral, neutral ; arkaisk, neutral",
  ["omfattande", "tjock"],
  [["omfattande"], ["tjock"]],
  "Han lämnade in en %s avhandling på 600 sidor." % (H % "diger"),
  "SO:s underbetydelse 'förr ofta äv. om människor' är en egen, numera "
  "arkaisk användning (Olav digre) och står som andra betydelse med det "
  "registret. Nutida bruk gäller nästan bara omfång: en diger lunta, ett "
  "digert program."),

 "dragé": (
  "Tablett eller sötsak överdragen med ett hårt lager glasyr",
  "neutral, neutral", ["≈≈ överdragen tablett"],
  [["≈≈ överdragen tablett"]],
  "Medicinen kom som %s med sött ytterlager." % (H % "dragéer"),
  "Poolen ger 'dragerad' och 'tablett' — det första är ordets eget "
  "particip och det andra en kategori som utelämnar överdraget, alltså "
  "kärnan. Därför ≈≈. Ordet täcker både läkemedel och konfekt, vilket "
  "huvudbetydelsen skriver ut."),

 "omtöckna": (
  "Göra oklar eller förvirrad",
  "litterär, negativ", ["förmörka", "göra andligen förvirrad"],
  [["förmörka", "göra andligen förvirrad"]],
  "Febern %s hans sinnen så att han inte kände igen någon." % (H % "omtöcknade"),
  "SO saknar artikel för ordet; SAOL och Wiktionary bär betydelsen och båda "
  "synonymerna kommer ur SAOL via poolen. Registret är litterärt — ordet "
  "lever nästan bara i skriven text, oftast som particip (omtöcknad)."),
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
            "huvudbetydelse": hb,
            "register": reg,
            "synonymer": syn,
            "synonymgrupper": grupper,
            "exempelmening": ex,
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
    saknas = [o for o in K if not any(x.get("ord") == o for x in kort)]
    if saknas:
        print("VARNING, fanns inte i sessionsfilen:", saknas)

main()
