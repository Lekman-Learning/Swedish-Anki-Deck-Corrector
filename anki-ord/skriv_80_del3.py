# -*- coding: utf-8 -*-
"""80-kortsomgangen 2026-08-25, del 3 (ord 41-60).

Kallor lasta via visa_uppslag.py -- SO:s rastruktur och SAOL ordagrant,
aldrig synonymer.se.
"""
import json
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-25_v3-batch2.json"
BLA = '<font color="#3498db">%s</font>'

TILLAT = {
 "blaffa": {"betydelse_kan_saknas":
   "SAOL har tva poster: substantivet ('stor, oformlig sak; flack') och verbet "
   "('kladda med skrikiga farger'). Kortordet ar substantivet, och bada dess "
   "led star pa kortet."},
 "diktat": {"betydelse_kan_saknas":
   "SO:s ovriga lemman ar `dikta` och `dikta upp`, alltsa verbet. Kortordet "
   "`diktat` har EN huvudbetydelse: 'patvingad losning av motsattning'.",
   "frammande_uppslagsord":
   "Traffarna `dikta` och `dikta upp` ar verbet, inte substantivet `diktat`."},
 "familjär": {"betydelse_kan_saknas":
   "SO:s rastruktur: TVA huvudbetydelser ('otvungen i umganget' och 'allmant "
   "bekant') med var sin underbetydelse ('alltfor intim' respektive 'fortrogen'). "
   "Kortet har bada huvudbetydelserna plus den intima nyansen."},
 "få gehör för": {"betydelse_kan_saknas":
   "Uttrycket bygger pa SO:s andra huvudbetydelse av `gehor` ('forstaelse och "
   "samtycke'). Den forsta ('formaga att uppfatta tonhojd') hor till ordet "
   "gehor, inte till uttrycket.",
   "frammande_uppslagsord":
   "Uttrycket ar tre ord, sa fuzzy-sokningen traffar `fa` och `for` som egna "
   "lemman. Sjalva uttrycket star under `gehor`."},
 "inackordering": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('permanent kost och logi') med tva "
   "underbetydelser ('person som bor inackorderad', 'det att inhysa och "
   "utfodra'). Kortet har boendet och personen."},
 "konservativ": {"betydelse_kan_saknas":
   "SO:s rastruktur: TVA huvudbetydelser ('som vill bevara det bestaende' och "
   "den medicinska 'som undviker operativa ingrepp'). Bada star pa kortet. "
   "Underbetydelsen om samhallsforhallanden ar den politiska tillampningen av "
   "den forsta."},
 "förment": {"betydelse_kan_saknas":
   "SAOL:s andra post ('anse', ald.) ar verbet `formena`, inte participet "
   "`forment`. Kortet galler participet, som har en betydelse."},
}

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form, etymologi)
KORT = {
 "blaffa": ("Större färgfläck ; stor och oformlig sak",
   "vardaglig, neutral", ["fläck"],
   "Det satt en blaffa av rödvin mitt på duken.", "blaffa",
   ""),

 "bondfångeri": ("Bedrägeri av enklare slag",
   "neutral, nedsättande", [],
   "Erbjudandet var rent bondfångeri.", "bondfångeri",
   "Till <i>bonde</i> och <i>fånga</i> — ursprungligen om att lura godtrogna lantbor i staden."),

 "desinfektera": ("Desinficera, oskadliggöra smittämnen",
   "neutral, neutral", ["desinficera"],
   "Såret desinfekterades innan förbandet lades om.", "desinfekterades",
   "Till <i>des-</i> 'bort' och latin <i>inficere</i> 'smitta'."),

 "diadem": ("Halvcirkelformat pann- eller hårsmycke",
   "neutral, neutral", [],
   "Bruden bar ett diadem av pärlor.", "diadem",
   "Av grekiska <i>diadema</i> 'pannband', till <i>diadein</i> 'binda om'."),

 "diktat": ("Påtvingad lösning av en motsättning ; påbud",
   "neutral, lätt negativ", ["påbud"],
   "Fredsavtalet uppfattades som ett diktat från segrarmakterna.", "diktat",
   "Av latin <i>dictatum</i> 'det befallda', till <i>dictare</i> 'diktera, befalla'."),

 "djurisk": ("Som visar ett rent driftstyrt och därför icke-mänskligt beteende",
   "neutral, nedsättande", ["rå", "brutal"],
   "Överfallet hade en djurisk brutalitet.", "djurisk",
   "Till <i>djur</i>."),

 "ekumenik": ("Strävan efter enhet mellan olika kristna samfund",
   "fackspråklig, neutral", [],
   "Församlingen engagerade sig i ekumenik och höll gemensamma gudstjänster.", "ekumenik",
   "Av grekiska <i>oikoumene</i> 'den bebodda världen', till <i>oikos</i> 'hus'."),

 "entitet": ("Avgränsad och enhetlig företeelse",
   "formell, neutral", ["ting", "föremål"],
   "Varje entitet i databasen har ett eget id.", "entitet",
   "Av medeltidslatin <i>entitas</i>, till <i>ens</i> 'varande'."),

 "eskapism": ("Flykt undan verklighetens problem",
   "neutral, neutral", ["verklighetsflykt"],
   "Han läste fantasy som ren eskapism.", "eskapism",
   "Till engelska <i>escape</i> 'fly', av fornfranska <i>eschaper</i>."),

 "familjär": ("Otvungen och förtrolig i umgänget, ibland alltför intim ; allmänt bekant",
   "neutral, neutral", ["förtrolig", "ogenerad"],
   "Han slog an en familjär ton som chefen inte uppskattade.", "familjär",
   "Av latin <i>familiaris</i> 'som hör till huset', till <i>familia</i> 'hushåll'."),

 "fasa ut": ("Successivt avveckla något",
   "neutral, neutral", [],
   "Kommunen ska fasa ut alla oljepannor till 2030.", "fasa ut",
   ""),

 "frekventera": ("Regelbundet besöka",
   "formell, neutral", [],
   "Han frekventerade stadens finare restauranger.", "frekventerade",
   "Av latin <i>frequentare</i> 'ofta besöka', till <i>frequens</i> 'talrik, tät'."),

 "få gehör för": ("Få förståelse och samtycke för något",
   "neutral, neutral", [],
   "Hon fick till slut gehör för sitt förslag i styrelsen.", "gehör",
   "Till <i>gehör</i>, av tyska <i>Gehör</i> 'hörsel', till <i>hören</i> 'höra'."),

 "förment": ("Som med orätt påstås vara något eller ha en viss egenskap",
   "neutral, neutral", ["förmodad", "inbillad"],
   "Hans förmenta expertis visade sig sakna grund.", "förmenta",
   "Perfekt particip av <i>förmena</i> 'anse', efter tyska <i>vermeinen</i>."),

 "gråben": ("Varg",
   "ngt ålderdomlig, skämtsam", ["varg"],
   "I sagorna smyger gråben kring gårdarna om natten.", "gråben",
   "Förskönande omskrivning — vargens rätta namn ansågs farligt att uttala."),

 "harpun": ("Spjutliknande fångstredskap med hulling, som skjuts eller kastas mot villebrådet",
   "neutral, neutral", [],
   "Valfångarna sköt en harpun från fören.", "harpun",
   "Av franska <i>harpon</i>, till <i>harpe</i> 'klo, krok'."),

 "inackordering": ("Permanent kost och logi i någons bostad ; person som bor inackorderad",
   "neutral, neutral", [],
   "Studenten sökte inackordering hos en familj i stan.", "inackordering",
   "Till <i>ackord</i> i äldre betydelsen 'överenskommelse'."),

 "indisponibel": ("Inte tillgänglig, som man inte förfogar över",
   "formell, neutral", [],
   "Medlen är indisponibla fram till årsskiftet.", "indisponibla",
   "Till latin <i>in-</i> 'o-' och <i>disponere</i> 'förfoga över'."),

 "irreal": ("Som inte är verklig eller faktisk",
   "fackspråklig, neutral", ["overklig"],
   "Filosofen skiljer mellan reala och irreala storheter.", "irreala",
   "Till latin <i>in-</i> 'o-' och <i>realis</i> 'verklig'."),

 "konservativ": ("Som vill bevara det bestående ; (om behandling) som undviker operativa ingrepp",
   "neutral, neutral", [],
   "Läkaren valde en konservativ behandling i stället för operation.", "konservativ",
   "Av latin <i>conservare</i> 'bevara', till <i>servare</i> 'vakta, rädda'."),
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    skrivna = 0
    for e in poster:
        o = e["ord"]
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
                         "synonymer.se. Inget skrivet som inte star i nagon av ordbockerna."),
        }
        if o in TILLAT:
            e["forgranska_tillat"] = TILLAT[o]
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"del 3: skrivna {skrivna}")


if __name__ == "__main__":
    main()
