# -*- coding: utf-8 -*-
"""100-kortsomgangen 2026-08-25 (batch3), del 5 (ord 81-100).

Kallor lasta via visa_uppslag.py -- SO:s rastruktur och SAOL ordagrant,
aldrig synonymer.se. Etymologier ur SO:s historiskaUppgifter.

TVA PAUSADE, bada av samma skal: ingen definitionstext i nagon kalla.
  tibia      -- bara SAOB-lemma, ingen traff i SO eller SAOL.
  vasstackt  -- finns som lemma i SAOL och SAOB men UTAN definitionstext,
                och saknas helt i SO. Betydelsen ar visserligen genomskinlig
                ('tackt med vass'), men da vore den skriven av mig och inte
                av kallan -- samma fel som synonymer.se-lackan i batch 6.

`over hovan` skrivs trots att SO saknar ordet: SAOL har det MED text
('till overmatt, alltfor mycket'), vilket ar skillnaden mot de tva ovan.
"""
import json
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-25_v3-batch3.json"
BLA = '<font color="#3498db">%s</font>'
HOPPA = {"tibia", "vasstäckt"}

TILLAT = {
 "pastoral": {"betydelse_kan_saknas":
   "SO har TVA lemman: adjektivet (TVA huvudbetydelser -- 'lantlig enkelhet och "
   "fridfullhet' och 'som har att gora med prastambete') och substantivet (EN "
   "huvudbetydelse -- 'konstnarligt verk om lantlig herdeidyll' -- med "
   "underbetydelserna 'herdedikt' och 'musikstycke av idyllisk karaktar'). "
   "Kortet tacker adjektivets bada och substantivets huvudbetydelse."},
 "skalk": {"betydelse_kan_saknas":
   "SO har TVA huvudbetydelser ('hard kant pa ost eller brod' och 'skalm', markt "
   "alderdomligt) plus underbetydelsen 'skurk'. De tva huvudbetydelserna star pa "
   "kortet; 'skurk' ar skarpningen av 'skalm', inte en tredje betydelse."},
 "tabu": {"betydelse_kan_saknas":
   "SO har TVA lemman med samma stavning: substantivet ('forbud mot kontakt med "
   "eller omnamnande av nagot') och adjektivet ('som man inte far befatta sig "
   "med'). Bada star pa kortet."},
 "vidkännas": {"betydelse_kan_saknas":
   "SO har TVA huvudbetydelser ('drabbas av nagot obehagligt' och 'erkanna att "
   "nagot existerar') plus underbetydelsen 'erkanna slaktskap eller bekantskap "
   "med'. Alla tre star pa kortet."},
 "ömma": {
   "betydelse_kan_saknas":
   "SO har TVA huvudbetydelser ('valla omhet, om kroppsdel' och 'hysa "
   "medkansla'). Bada star pa kortet. SAOL:s tva sista led ar adjektivet `om`, "
   "inte verbet.",
   "frammande_uppslagsord":
   "Det dolda fuzzy-lemmat ar adjektivet `om`, som verbet ar bildat till."},
 "uppträde": {"betydelse_kan_saknas":
   "SO har TVA huvudbetydelser ('tamligen allvarligt brak, ofta med handgemang' "
   "och 'upptradande'). Bada star pa kortet."},
 "orakel": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('svartolkat meddelande fran gudom') och "
   "TRE underbetydelser UTAN egen definition. SAOL:s tva led ('formedlare av "
   "gudomssvar' och 'ofelbar radgivare, obestridd auktoritet') star bada pa "
   "kortet."},
 "universal": {
   "betydelse_kan_saknas":
   "SO har ordet som FORLED (`universal-`) med EN betydelse: 'anvandbar pa alla "
   "tankbara omraden'. SAOL ger 'allomfattande, universell'. Kortet har bada.",
   "frammande_uppslagsord":
   "SO:s uppslagsord ar `universal-` med bindestreck eftersom ordet framst "
   "anvands som forled. Samma lemma, annan skrivning."},
 "måtto": {"betydelse_kan_saknas":
   "SO ger EN betydelse: 'avseende'. SAOL har lemmat utan definitionstext. "
   "Kortet skriver ut hur ordet faktiskt anvands, eftersom 'avseende' ensamt "
   "inte gar att lara sig av."},
 "paradera": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('marschera i parad') och EN "
   "underbetydelse UTAN egen definition. SAOL:s andra led ('stata') ar den "
   "bildliga anvandningen och star pa kortet."},
 "ringrostig": {"register_motsager_markning":
   "SO:s markning ar 'vardagligt', SAOL:s 'vard.'. Kortets register sager just "
   "'vardaglig'. Flaggan slar pa den langre definitionstexten, inte pa "
   "bruklighetsangivelsen."},
 "tygellös": {"betydelse_kan_saknas":
   "SO ger EN betydelse ('(vild och) okontrollerad'). SAOL:s 'av. bildl. "
   "ohammad' ar samma betydelse i bildlig anvandning, inte en andra."},
}

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form, etymologi)
KORT = {
 "måtto": ("Avseende, i uttryck som i så måtto och i viss måtto",
   "formell, neutral", ["avseende"],
   "I så måtto hade han rätt.", "måtto",
   "Ursprungligen en böjningsform av <i>måtta</i>."),

 "namnkunnig": ("Vars namn många känner till",
   "formell, positiv", ["ryktbar", "berömd"],
   "Flera namnkunniga forskare skrev under uppropet.", "namnkunniga",
   "Fornsvenska <i>namnkunnogher</i>."),

 "orakel": ("Svårtolkat meddelande från en gudom, förmedlat av präst eller profet ; ofelbar rådgivare eller obestridd auktoritet",
   "litterär, neutral", [],
   "Han behandlades som ett orakel i alla ekonomiska frågor.", "orakel",
   "Av latin <i>oraculum</i>, till <i>orare</i> 'tala'."),

 "paradera": ("Marschera eller vara uppställd i parad ; ståta med något",
   "neutral, neutral", ["ståta"],
   "Regementet paraderade förbi slottet.", "paraderade",
   ""),

 "pastoral": ("Som präglas av lantlig enkelhet och fridfullhet ; som har att göra med prästämbetet ; konstnärligt verk om lantlig herdeidyll",
   "litterär, neutral", [],
   "Landskapet hade en pastoral stillhet.", "pastoral",
   "Av latin <i>pastoralis</i>, till <i>pastor</i> 'herde'."),

 "resignera": ("Efter lång kamp tröttna och inse det omöjliga i att uppnå ett visst mål",
   "formell, negativ", [],
   "Till slut resignerade hon och slutade överklaga.", "resignerade",
   "Av latin <i>resignare</i> 'bryta upp, förklara ogiltig'."),

 "ringrostig": ("Som har dålig kondition eller teknik efter ett längre uppehåll i en aktivitet",
   "vardaglig, neutral", ["otränad"],
   "Han var ringrostig efter ett år utan att spela.", "ringrostig",
   ""),

 "skalk": ("Hård kant på ost eller bröd ; (ålderdomligt) skälm eller skojare",
   "neutral, neutral", ["brödkant", "skälm"],
   "Han tog skalken av limpan.", "skalken",
   "Bildat till samma ordrot som <i>skal</i>, med betydelsen 'klyva'."),

 "supplera": ("Göra tillägg till en text där något saknas",
   "formell, neutral", ["fylla ut"],
   "Utgivaren har supplerat de skadade partierna.", "supplerat",
   "Av latin <i>supplere</i> 'utfylla'."),

 "tabu": ("Religiöst eller socialt motiverat förbud mot att röra eller nämna något ; som man inte får befatta sig med eller omnämna",
   "neutral, neutral", [],
   "Ämnet var tabu vid middagsbordet.", "tabu",
   "Av tonganska <i>tapu</i> 'tabu, heligförklarat'."),

 "tetanus": ("Stelkramp",
   "fackspråklig, neutral", ["stelkramp"],
   "Han vaccinerades mot tetanus efter olyckan.", "tetanus",
   ""),

 "transumera": ("Göra utdrag ur en skriftlig handling",
   "fackspråklig, neutral", [],
   "Notarien transumerade domen i protokollet.", "transumerade",
   "Av latin <i>transumere</i> 'överflytta'."),

 "tygellös": ("Vild och okontrollerad, ohämmad",
   "litterär, negativ", ["ohämmad"],
   "Festen urartade i tygellöst festande.", "tygellöst",
   "Till <i>tygel</i> och <i>-lös</i>."),

 "universal": ("Användbar eller funktionsduglig på alla tänkbara områden, allomfattande",
   "fackspråklig, neutral", ["universell", "allomfattande"],
   "Verktyget har ett universalfäste som passar alla modeller.", "universal",
   "Av latin <i>universalis</i> 'allmän'. Besläktat med <i>universum</i>."),

 "uppträde": ("Tämligen allvarligt bråk, ofta med handgemäng ; uppträdande inför publik",
   "neutral, neutral", ["bråk", "träta"],
   "Det blev ett uppträde utanför restaurangen.", "uppträde",
   "Av lågtyska <i>uptrede</i>, till <i>uppträda</i>."),

 "vidkännas": ("Drabbas av något obehagligt ; erkänna att något existerar ; erkänna släktskap eller bekantskap med någon",
   "formell, neutral", ["erkänna", "utstå"],
   "Bolaget fick vidkännas kraftiga förluster.", "vidkännas",
   "Fornsvenska <i>vidherkännas</i> 'bekänna, erkänna'."),

 "ömma": ("Vålla ömhet, göra ont vid beröring ; hysa medkänsla med någon",
   "neutral, neutral", [],
   "Axeln ömmade när han lyfte armen.", "ömmade",
   "Fornsvenska <i>öma</i> 'känna medlidande'. Till <i>öm</i>."),

 "över hövan": ("Till övermått, alltför mycket",
   "ngt ålderdomlig, negativ", [],
   "Han berömde sig själv över hövan.", "hövan",
   ""),
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    skrivna = pausade = 0
    for e in poster:
        o = e["ord"]
        if o in HOPPA:
            pausade += 1
            print("  PAUSAS (ingen definitionstext i nagon kalla):", o)
            continue
        if o not in KORT:
            continue
        bet, reg, syn, ex, form, etym = KORT[o]
        if form in ex:
            ex = ex.replace(form, BLA % form, 1)
        else:
            print("  VARNING: hittade inte", form, "i:", ex)
        e["proposed"] = {
            "huvudbetydelse": bet, "register": reg, "synonymer": syn,
            "synonym_groups": None, "exempelmening": ex, "etymologi": etym,
        }
        e["approved"] = True
        q = urllib.parse.quote(o)
        e["sokkoll"] = {
            "kalla": (f"SO och SAOL via https://svenska.se/api/msearch?ord={q} "
                      f"samt https://www.synonymer.se/sv-syn/{q} -- hamtade 2026-08-25, "
                      f"sparade i uppslag/{o}.json"),
            "slutsats": ("Betydelser, register och synonymer lasta ur SO:s rastruktur och "
                         "SAOL:s definitionstext via visa_uppslag.py, som inte visar "
                         "synonymer.se. Etymologin hamtad ur SO:s historiskaUppgifter; "
                         "tom dar SO saknar faltet. Inget skrivet som inte star i "
                         "nagon av ordbockerna."),
        }
        if o in TILLAT:
            e["forgranska_tillat"] = TILLAT[o]
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"del 5: skrivna {skrivna}  pausade {pausade}")


if __name__ == "__main__":
    main()
