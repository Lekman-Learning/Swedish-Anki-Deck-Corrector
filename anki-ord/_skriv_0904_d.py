# -*- coding: utf-8 -*-
"""Arbetsbatch 2026-09-04, kort 37-50 av 50. Sista delen."""
import io, json, sys
import _hjalp_0902b as HJ

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-04_v3-omgranskning.json"
H = HJ.H

K = {
 "epifyt": (
  "Växt som sitter fast på en annan växt utan att ta näring från den",
  "fackspråklig, neutral, biologi", ["≈≈ påväxtväxt"],
  [["≈≈ påväxtväxt"]],
  "Orkidéer är ofta %s och sitter högt uppe i trädkronorna." % (H % "epifyter"),
  "Poolen ger bara 'växt', en kategori som inte skiljer epifyten från något "
  "annat. Att den INTE tar näring ur värdväxten är hela poängen — det är "
  "skillnaden mot en parasit — och står därför i huvudbetydelsen."),

 "kollegial": (
  "Som gäller ett kollegium ; som avgörs genom omröstning i stället för av chefen ensam ; som beter sig som en god kollega",
  "formell, neutral ; formell, neutral, politik ; neutral, positiv",
  ["kollegie-", "≈≈ genom samråd", "kamratlig"],
  [["kollegie-"], ["≈≈ genom samråd"], ["kamratlig"]],
  "Beslutet fattades genom %s omröstning, inte av rektorn ensam." % (H % "kollegial"),
  "Tre betydelser enligt SO. Den andra är den som förvirrar: 'kollegialt "
  "beslut' betyder inte vänligt beslut utan beslut i grupp — Wiktionary "
  "skriver ut kontrasten mot chefen ensam, och den står i huvudbetydelsen."),

 "arta sig": (
  "Verka utvecklas åt ett visst håll ; utvecklas på ett bra sätt ; sluta väl",
  "neutral, neutral ; neutral, positiv ; neutral, positiv",
  ["utvecklas", "≈≈ gå bra", "≈≈ ordna sig"],
  [["utvecklas"], ["≈≈ gå bra"], ["≈≈ ordna sig"]],
  "Den nya modellen %s till en stor succé." % (H % "artade sig"),
  "SO ger två betydelser plus 'äv. positivt'. Skillnaden är att den första "
  "är neutral riktning ('hur artar det sig?') medan de andra två bär "
  "förväntan om något bra ('allt skulle arta sig med tiden')."),

 "förirra sig": (
  "Tappa orienteringen och hamna någonstans av misstag ; komma bort från ämnet",
  "neutral, neutral ; neutral, lätt negativ",
  ["gå vilse", "tappa orienteringen", "≈≈ avvika från ämnet"],
  [["gå vilse", "tappa orienteringen"], ["≈≈ avvika från ämnet"]],
  "Två tågluffare hade %s till den lilla byn." % (H % "förirrat sig"),
  "SO:s 'äv. bildligt' är en egen betydelse med eget bruk — 'han förirrade "
  "sig bort från ämnet' handlar inte om geografi. Den står som nummer två."),

 "likare": (
  "Normalmått som andra mått justeras efter ; erkänd förebild ; måttstock i sammansättningar",
  "fackspråklig, neutral, teknik ; formell, positiv ; formell, neutral",
  ["normalmått", "≈≈ förebild", "≈≈ måttstock"],
  [["normalmått"], ["≈≈ förebild"], ["≈≈ måttstock"]],
  "Riksarkivet förvarade en %s för mått och vikt." % (H % "likare"),
  "Grundbetydelsen är teknisk — det fysiska normalmåttet. Den andra är "
  "överförd (en person som andra mäts mot), och den tredje är SO:s "
  "'äv. bildligt (i sammansättn.)', alltså rikslikare och liknande."),

 "gärdsmyg": (
  "En mycket liten brunspräcklig fågel med kort, uppåtriktad stjärt",
  "neutral, neutral, biologi", ["≈≈ småfågel"],
  [["≈≈ småfågel"]],
  "En %s hoppade omkring i snåret och letade efter insekter." % (H % "gärdsmyg"),
  "Poolen ger 'en fågel', vilket är SAOL:s hela artikel och för brett. "
  "SO:s eget faktum är värt att ha: gärdsmygen är näst kungsfågeln Sveriges "
  "minsta fågel, vilket 'mycket liten' i huvudbetydelsen bär."),

 "förfara": (
  "Gå till väga på ett visst sätt",
  "formell, neutral", ["gå till väga"],
  [["gå till väga"]],
  "Instruktionen beskriver hur man ska %s vid eldsvåda." % (H % "förfara"),
  "En betydelse, en exakt synonym ur poolen. Ordet lever nästan bara i "
  "skrivna instruktioner och föreskrifter, vilket ger det formella "
  "registret."),

 "gensträvig": (
  "Som gör motstånd och inte vill lyda",
  "neutral, lätt negativ", ["motsträvig"],
  [["motsträvig"]],
  "Hästen var %s och vägrade gå in i transporten." % (H % "gensträvig"),
  "Alla tre källorna ger samma enda synonym, 'motsträvig'. Den duger inte "
  "ensam som förklaring på ett kort — huvudbetydelsen är därför skriven ut "
  "i stället för att upprepa synonymen."),

 "kollekt": (
  "Insamling av pengar under en gudstjänst ; pengarna som samlats in",
  "neutral, neutral, religion ; neutral, neutral, religion",
  ["insamling", "≈≈ insamlade pengar"],
  [["insamling"], ["≈≈ insamlade pengar"]],
  "Församlingen tog upp %s till förmån för de hemlösa." % (H % "kollekt"),
  "SO:s 'äv. med tanke på de insamlade pengarna' är en egen betydelse: "
  "'kollekten uppgick till 5 000 kronor' handlar om summan, inte om "
  "handlingen. Den står som nummer två."),

 "skvattram": (
  "En starkt doftande myrväxt med vita blommor",
  "neutral, neutral, biologi", ["getpors"],
  [["getpors"]],
  "Doften av %s låg tung över myren." % (H % "skvattram"),
  "'getpors' är SO:s eget SYN-fält och alltså belagd synonym, inte en "
  "gissning. Att den doftar starkt är det som gör växten igenkännlig och "
  "står därför före blommorna i huvudbetydelsen."),

 "kutting": (
  "Liten tunna ; vända på kuttingen — se saken från motsatt håll",
  "dialektal, neutral ; neutral, neutral",
  ["kagge", "liten tunna", "≈≈ kasta om perspektivet"],
  [["kagge", "liten tunna"], ["≈≈ kasta om perspektivet"]],
  "Skolan har vänt på %s och byggt fler grupprum än lärosalar." % (H % "kuttingen"),
  "SO märker ordet 'dialektalt' i grundbetydelsen. Den andra betydelsen är "
  "uttrycket 'vända på kuttingen', som lever kvar i allmänsvenska långt "
  "efter att tunnan gjort det — och det är den Adam faktiskt möter, vilket "
  "exempelmeningen visar."),

 "simpa": (
  "Bottenlevande rovfisk med brett, platt huvud och stora bröstfenor",
  "neutral, neutral, biologi", ["≈≈ bottenfisk"],
  [["≈≈ bottenfisk"]],
  "Han fick upp en %s med taggiga gällock." % (H % "simpa"),
  "Poolen ger 'en fisk' (SAOL:s hela artikel) och lösryckta fragment ur "
  "SO:s definition. Därför ≈≈. Det breda platta huvudet är det som gör "
  "fisken igenkännlig och står kvar i huvudbetydelsen."),

 "strimmig": (
  "Försedd med smala, ofta oregelbundna ränder",
  "neutral, neutral", ["≈≈ randig"],
  [["≈≈ randig"]],
  "Katten var grå och %s över ryggen." % (H % "strimmig"),
  "Poolen ger bara 'försedd', ett fragment av definitionen. 'randig' är "
  "närmast men saknar ordboksbelägg som synonym, därför ≈≈. SO:s parentes "
  "'(oregelbundna)' är upplöst till 'ofta oregelbundna'."),

 "svängtapp": (
  "Tappliknande del som något kan svänga runt",
  "fackspråklig, neutral, teknik", ["≈≈ vridpunkt"],
  [["≈≈ vridpunkt"]],
  "Luckan satt på en %s och kunde fällas åt båda hållen." % (H % "svängtapp"),
  "Bara SO har artikel — SAOL och Wiktionary saknar ordet helt, och poolen "
  "är tom. Därför ≈≈. Ordet är rent tekniskt och förekommer i "
  "konstruktionsbeskrivningar."),
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
