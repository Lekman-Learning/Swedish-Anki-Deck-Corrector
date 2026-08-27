# -*- coding: utf-8 -*-
"""Batch 2026-08-27, kort 10-19. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-27_v3-batch.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
KALLA = ("SO och SAOL via https://svenska.se/api/msearch?ord=%s "
         "(hamtat 2026-08-27, HTTP 200)")
B = '<font color="#3498db">%s</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, tillat=None, conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": None, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": KALLA % urllib.parse.quote(o),
                    "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("rättfärdig",
     "Som lever hederligt och gör det som är rätt ; om en sak: som det finns goda skäl att kämpa för",
     "ngt ålderdomlig, positiv ; ngt ålderdomlig, positiv",
     ["rättrådig", "rättvis"],
     "Hon kämpade för en " + B % "rättfärdig" + " sak även när ingen annan orkade.",
     "→ Fornsvenska rätfärdogher, av lågtyska rechtverdich.",
     "SO: 'som lever ett gott och moraliskt riktigt liv | moraliskt "
     "valgrundad' -- tva betydelser, om person och om sak. SAOL: 'rattradig, "
     "ostraffad; rattvis; befriad fran syndaskuld'. Bada synonymerna leder var "
     "sitt led. SO markerar 'nagot alderdomligt'.",
     tillat={"betydelse_kan_saknas":
             "SO:s 4 poster ar 2 betydelser plus en 'el.'-variant och en "
             "'av. om handling'-variant, vilka bagge hor till sakbetydelsen. "
             "Kortet tacker person och sak."})

satt("slejf",
     "Fastsytt band som håller ihop ett plagg eller sitter där som prydnad ; "
     "remmen över vristen på en sko",
     "neutral, neutral ; neutral, neutral",
     ["band"],
     "Klänningen hade en smal " + B % "slejf" + " i ryggen som drog in midjan.",
     "→ Tyska Schleife 'ögla, rosett, slinga'.",
     "SAOL: 'band som haller samman ngt el. till prydnad t.ex. i ryggen i "
     "midjan pa kladesplagg | ogla for stropp'. SO ger aven 'skorem over "
     "vristen' som egen betydelse. 'band' leder SAOL:s definition.")

satt("uppstyltad",
     "Krånglig och stel på ett onaturligt sätt — som när någon försöker låta finare än hen är",
     "neutral, negativ",
     ["högtravande", "tillkrånglad"],
     "Brevet var skrivet på " + B % "uppstyltad" + " myndighetssvenska som ingen förstod.",
     "→ Till stylta — den som går på styltor står högre än naturligt.",
     "SAOL: 'hogtravande'. SO: 'onaturligt tillkranglad'. Bada synonymerna "
     "star ordagrant i definitionstexten, en i vardera ordbok.")

satt("välva",
     "Bygga något så att det buktar uppåt som ett tak ; "
     "själv forma sig i en båge ; "
     "röra sig i en rund bana",
     "litterär, neutral ; litterär, neutral ; litterär, neutral",
     ["kupig"],
     "Rymden " + B % "välvde" + " sig svart över slagfältet.",
     "→ Fornsvenska hvälva, nära besläktat med valv.",
     "SO: 'bygga upp i form av valv | forma sig till ett valv | rora sig i "
     "rund(ad) bana'. SAOL: 'gora valvformig el. kupig'. VIKTIGT: old_facit "
     "sager 'planera' (valva planer) -- den betydelsen star i Wiktionary men "
     "VARKEN i SO eller SAOL, och ar darfor inte inskriven pa kortet.",
     conf=8)

satt("brallis",
     "Snygg tjej. Ett gammalt slangord som knappt används längre",
     "vardaglig, neutral",
     ["flicka"],
     "Han kallade henne " + B % "brallis" + ", vilket lät lika gammalmodigt som det var.",
     "→ Till bralla.",
     "SO: 'snygg tjej', markt 'vardagligt; nagot alderdomligt'. SAOL: "
     "'flicka'. Belagt sedan 1949. Bara EN stilniva far anges, och SO:s "
     "forsta markning ar 'vardagligt' -- alderdomligheten star i "
     "huvudbetydelsen i stallet.")

satt("diabolisk",
     "Djävulsk — ondskefull på ett nästan övernaturligt sätt ; "
     "försvagat: busigt elak, mest på skoj",
     "litterär, negativ ; neutral, skämtsam",
     ["djävulsk"],
     "Fällan var " + B % "diabolisk" + " — ju mer man slet, desto hårdare satt den.",
     "→ Grekiska diabolikos, till diabolos 'djävul'.",
     "SO och SAOL sager bada 'djavulsk'. SO lagger till 'av. forsvagat', "
     "belagt med exemplet 'han fick en diabolisk lust att lura henne' -- "
     "darfor tva betydelser med olika valor.")

satt("egg",
     "Den vassa kanten på en kniv eller yxa — den som skär ; "
     "bildligt: den smala gränsen mellan två ytterligheter",
     "neutral, neutral ; litterär, neutral",
     ["skärande kant"],
     "Yxans " + B % "egg" + " var så vass att den bet i träet av sin egen tyngd.",
     "→ Fornsvenska äg, ursprungligen 'något spetsigt'. Jfr tyska Ecke 'kant'.",
     "SAOL: 'skarande kant pa kniv, yxa e.d.'. SO: 'skarp kant pa skarande "
     "eller huggande verktyg' plus 'ibland bildligt i uttryck for kanslig "
     "balans' med exemplet 'balanserade pa eggen mellan inbillning och fakta'.")

satt("ferie",
     "Längre ledighet, särskilt skollov",
     "ngt ålderdomlig, neutral",
     ["ledighet", "lov"],
     "Barnen var på landet hela " + B % "ferien" + " och kom hem först i augusti.",
     "→ Latin feriae 'ferier, högtidsdagar'. Släkt med fest och fira.",
     "SAOL: 'langre ledighet el. lov vid skola' -- bada synonymerna star dar. "
     "SO: 'langre period av ledighet'. Anvands nastan bara i plural (ferier).")

satt("grundlig",
     "Som går igenom allt viktigt och inte hoppar över något ; "
     "om person: som arbetar på det sättet ; "
     "som adverb: rejält, ordentligt",
     "neutral, positiv ; neutral, positiv ; neutral, neutral",
     ["noggrann", "ordentlig"],
     "Undersökningen var så " + B % "grundlig" + " att ingenting kunde ha missats.",
     "→ Fornsvenska grundeliker, av lågtyska grundlik. Till grund.",
     "SAOL: 'noggrann, ordentlig' -- bada synonymerna leder var sitt led. SO: "
     "'som omfattar alla viktiga delar' plus 'av. om person' och 'av. (som "
     "adverb) med forstarkande anvandning' ('han tog grundligt miste').",
     tillat={"betydelse_kan_saknas":
             "SO:s 4 poster ar 3 betydelser plus 4 JFR-taggar "
             "(genomgripande, ingaende, noggrann, ordentlig) som inte ar "
             "egna betydelser. Kortet tacker sak, person och adverb."})

satt("imaginär",
     "Bara inbillad — finns i huvudet men inte i verkligheten ; "
     "i matematik: tal som ger ett negativt resultat när det multipliceras med sig självt",
     "neutral, neutral ; fackspråklig, neutral, matematik",
     ["inbillad", "overklig"],
     "Han byggde ett helt " + B % "imaginärt" + " landskap i huvudet innan han somnade.",
     "→ Franska imaginaire, av latin imaginarius 'skenbar', till imago 'bild'.",
     "SAOL: 'endast inbillad, overklig | som vid multiplikation med sig sjalv "
     "ger en negativ produkt', markt 'mat.' for den andra betydelsen. Bada "
     "synonymerna star ordagrant. De tva betydelserna ar helt oberoende och "
     "matematikbetydelsen ar den HP oftast provar.")

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Totalt godkanda kort nu: %d" % sum(1 for k in KORT if k.get("approved")))
