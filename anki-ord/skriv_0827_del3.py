# -*- coding: utf-8 -*-
"""Batch 2026-08-27, kort 20-29. Full v3."""
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


satt("judiciell",
     "Som har med domstolar och rättsväsendet att göra",
     "fackspråklig, neutral, juridik",
     ["rättslig", "domstols-"],
     "Landet delades in i " + B % "judiciella" + " distrikt med var sin domstol.",
     "→ Till latin judicium 'domstol, rättegång'.",
     "SAOL: 'rattslig, domstols-' -- bada synonymerna leder var sitt led. SO: "
     "'som har att gora med rattsvasendet'. JFR ger juridisk och rattslig; "
     "juridisk ar cohyponym och darfor inte inskriven som synonym.")

satt("karantän",
     "Att hållas isolerad en tid för att en smitta inte ska spridas vidare ; "
     "platsen där det sker ; "
     "bildligt: att stängas ute socialt eller politiskt",
     "neutral, neutral ; neutral, neutral ; neutral, lätt negativ",
     ["isolering"],
     "Hunden fick sitta i " + B % "karantän" + " en månad innan den släpptes in i landet.",
     "→ Franska quarantaine 'fyrtio dagar' — spärrtiden för pestmisstänkta omkring år 1400.",
     "SAOL: 'isolering av manniskor el. djur vid ett lands gräns for att "
     "forhindra smittspridning'. SO ger tre betydelser: sjalva isoleringen, "
     "platsen, och den bildliga ('sattes landet i karantan av EU'). "
     "Etymologin forklarar ordet direkt och ar darfor med.")

satt("kavitet",
     "Hålighet — ett tomt utrymme inuti något",
     "fackspråklig, neutral, medicin",
     ["hålighet"],
     "Röntgen visade en " + B % "kavitet" + " i skallbasen som inte borde ha funnits.",
     "→ Via franska av latin cavitas, till cavus 'ihålig'.",
     "SO och SAOL sager bada exakt 'halighet'. Wiktionary ger aven "
     "'halrum', men det star inte i SO/SAOL och ar darfor struket. Anvands nastan bara i medicin och geologi.")

satt("knappologi",
     "Att systematisera struntsaker — att lägga ner stort arbete på fakta som inte betyder något",
     "neutral, ironisk",
     ["systematisering av struntsaker"],
     "Hela rapporten var " + B % "knappologi" + ": tusen siffror och inte en slutsats.",
     "→ Strindbergs parodi på knapp + grekiska logos 'lära'.",
     "SAOL: 'systematisering av struntsaker'. SO: 'systematisering av "
     "ointressanta fakta', markt 'iron.'. Ordet ar Strindbergs egen "
     "uppfinning fran 1883 och ar ironiskt fran borjan -- darfor valoren.")

satt("nasa",
     "Gå runt och sälja billiga varor vid dörrarna",
     "ngt ålderdomlig, nedsättande",
     ["sälja vid dörren"],
     "Han försörjde sig på att " + B % "nasa" + " hötorgskonst i förorterna.",
     "→ Av månsing (gammalt handelsspråk) nasa 'sälja, handla'.",
     "SO: 'salja (billiga varor) vid dorren', markt 'alderdomligt; "
     "nedsattande'. SAOL: 'sarsk. i aldre tid: salja vid dorren'. Bada "
     "markningarna finns i kortets register. En nasare ar den som gor det.")

satt("nocturne",
     "Stämningsfullt musikstycke, oftast för piano, som ska ge känslan av natt",
     "fackspråklig, neutral, musik",
     ["nattstycke"],
     "Chopins " + B % "nocturner" + " spelas långsamt och nästan viskande.",
     "→ Franska nocturne, av latin nocturnus 'nattlig'.",
     "SO: 'musikstycke (sarskilt for piano) som kan ge upphov till drommande "
     "nattstamning'. SAOL vidgar till 'malning el. dikt med nattligt motiv'. "
     "'nattstycke' star i Wiktionary och i old_facit ('musikaliskt "
     "nattstycke') men INTE i SO/SAOL:s definitionstext -- behallen anda "
     "eftersom det ar den etablerade svenska termen.",
     tillat={"synonym_utan_ordboksbelagg":
             "nattstycke ar den svenska fackterm som SO:s egen definition "
             "beskriver ('drommande nattstamning') och som old_facit anger. "
             "Ordet ar dessutom ordagrant Wiktionarys forsta glosa.",
             "betydelse_kan_saknas":
             "SO:s 3 poster ar EN betydelse plus tva bojningsformer "
             "('best. form' och 'plural'), vilka inte ar betydelser."},
     conf=8)

satt("reguljär",
     "Som följer de vanliga reglerna — den normala varianten, inte undantaget ; "
     "om trupper: som tillhör statens egen krigsmakt ; "
     "som har regelbunden form",
     "fackspråklig, neutral ; fackspråklig, neutral ; fackspråklig, neutral",
     ["regelbunden", "regelrätt", "vanlig"],
     "Han flög " + B % "reguljärt" + " till Berlin, inte med charter.",
     "→ Franska régulier, latin regularis. Till regel.",
     "SAOL: 'regelbunden; regelratt; vanlig' -- alla tre synonymerna leder "
     "var sitt led. SO ger tre betydelser plus 'spec. om flygtrafik, i "
     "kontrast till charter'. Kontrasten reguljar/charter ar den HP provar.",
     tillat={"betydelse_kan_saknas":
             "SO:s 5 poster ar 3 betydelser plus 2 JFR-taggar (ordinarie, "
             "regelratt). Kortet tacker alla tre.",
             "register_motsager_markning":
             "SO:s markning 'i vetenskapliga sammanhang' ar precis vad "
             "valvets stilniva 'fackspraklig' betyder -- de sager samma sak "
             "med olika ord, och tabellen _MARKNING_LIKA saknar bara raden."})

satt("reslig",
     "Ovanligt lång och ståtlig",
     "litterär, positiv",
     ["högrest", "högväxt"],
     "Lagets " + B % "reslige" + " mittback nickade in alla hörnor.",
     "→ Av lågtyska reisich 'reslig, smärt'. Besläktat med resa sig.",
     "SAOL: 'hogrest, hogvaxt' -- bada synonymerna leder var sitt led. SO: "
     "'som har stor kroppslangd', med tillagget 'av. om vaxt' ('resliga "
     "tallar') -- samma betydelse om trad, inte en egen.",
     tillat={"betydelse_kan_saknas":
             "SO:s andra post ar 'av. om vaxt' -- samma betydelse (stor "
             "langd) tillampad pa trad, inte en skild betydelse."})

satt("rosslig",
     "Som låter skrapigt och tungt när man andas eller talar",
     "neutral, lätt negativ",
     [],
     "Han svarade med " + B % "rosslig" + " röst att han nog borde ha slutat röka.",
     "→ Till rossla, ett ljudhärmande ord.",
     "SO: 'som rosslar'. Ingen SAOL-post och ingen Wiktionary-post -- SO ar "
     "enda kallan, och dess definition ar cirkular (rosslig = som rosslar), "
     "sa huvudbetydelsen ar skriven ur exemplen 'en rosslig rost' och 'hon "
     "andades rossligt'. Tom synonymlista: ordboken ger ingen kandidat.",
     conf=7)

satt("suspekt",
     "Som man har goda skäl att misstänka — något känns fel utan att man kan peka på vad",
     "neutral, negativ",
     ["misstänkt", "tvivelaktig"],
     "En " + B % "suspekt" + " figur stod och rökte utanför porten i tre timmar.",
     "→ Latin suspectus, till suspicere 'misstänka'. Samma rot som respekt och aspekt.",
     "SAOL: 'misstankt; tvivelaktig' -- bada synonymerna leder var sitt led. "
     "SO: 'som inger (moraliska) betankligheter'. JFR ger ljusskygg och skum, "
     "som ar cohyponymer och darfor inte inskrivna.")

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Totalt godkanda kort nu: %d" % sum(1 for k in KORT if k.get("approved")))
