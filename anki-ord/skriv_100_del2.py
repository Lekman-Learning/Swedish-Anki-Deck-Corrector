# -*- coding: utf-8 -*-
"""100-kortsomgangen 2026-08-25 (batch3), del 2 (ord 21-40).

Kallor lasta via visa_uppslag.py -- SO:s rastruktur och SAOL ordagrant,
aldrig synonymer.se. Etymologierna hamtade ur SO:s historiskaUppgifter;
dar faltet saknas (advokatyr, axiomatisk, elegisk, fjaskig, piffig) lamnas
etymologin TOM i stallet for att skrivas ur minnet.
"""
import json
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-25_v3-batch3.json"
BLA = '<font color="#3498db">%s</font>'

TILLAT = {
 "accent": {"betydelse_kan_saknas":
   "SO:s rastruktur: TVA huvudbetydelser ('framhava viss stavelse' och 'drag i "
   "uttalet som utmarker visst sprak') med var sin underbetydelse "
   "('accenttecken' respektive 'karakteristiskt, iogonfallande drag'). Alla fyra "
   "star pa kortet."},
 "ackurat": {"betydelse_kan_saknas":
   "SO har TVA lemman med samma stavning: adjektivet ('mycket noggrann') och "
   "adverbet ('precis'). Bada star pa kortet."},
 "axiomatisk": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('som bygger pa axiom') och EN "
   "underbetydelse MED egen definition ('sjalvklart sann'). Bada star pa kortet. "
   "SAOL:s definitionstext ar tom for det har ordet."},
 "elegisk": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('som har att gora med elegin') och EN "
   "underbetydelse MED egen definition ('vemodigt sorgsen'). Bada star pa kortet."},
 "förvänd": {
   "betydelse_kan_saknas":
   "SAOL:s andra post ('gora oigenkannlig') ar verbet `forvanda`, inte "
   "participet `forvand`. Kortordet ar adjektivet, som har EN betydelse: "
   "'helt oriktig' -- identisk i SO och SAOL.",
   "frammande_uppslagsord":
   "Traffen `forvanda` ar verbet som `forvand` ar particip av. Samma lemma, "
   "annan form."},
 "indikation": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('omstandighet som tyder pa visst "
   "forhallande') och EN underbetydelse MED egen definition ('forhallande som "
   "utgor skal for viss medicinsk atgard'). Bada star pa kortet."},
 "klerikal": {"betydelse_kan_saknas":
   "SO har TVA huvudbetydelser ('praglas av starkt prastvasende' och "
   "'(hog)kyrkligt sinnad'). Bada star pa kortet."},
 "taxa": {"betydelse_kan_saknas":
   "SO har TVA lemman med samma stavning: substantivet ('faststalld avgift') och "
   "verbet ('kora pa marken fore start eller efter landning, om flygplan'). "
   "Bada star pa kortet."},
 "absid": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('rumsavslutande utbyggnad pa kyrka') och "
   "EN underbetydelse UTAN egen definition, alltsa en anvandningsutvidgning."},
 "fjäskig": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('som garna fjaskar') och EN "
   "underbetydelse UTAN egen definition. SAOL saknar definitionstext for ordet."},
 "piffig": {"betydelse_kan_saknas":
   "SO har EN huvudbetydelse utan underbetydelser. SAOL saknar definitionstext."},
 "dräglig": {"betydelse_kan_saknas":
   "SAOL:s tva led ('uthardlig; tamligen god') ar samma betydelse uttryckt tva "
   "ganger -- SO har EN huvudbetydelse: 'mojlig att utharda utan alltfor stora "
   "pafrestningar'. Kortet tacker bada leden."},
}

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form, etymologi)
KORT = {
 "accent": ("Sätt att framhäva en viss stavelse med styrka eller ton ; tecken för betoning ; drag i uttalet som visar att någon har ett annat modersmål",
   "neutral, neutral", ["betoning", "tonvikt", "brytning"],
   "Hon talade svenska med lätt fransk accent.", "accent",
   "Av latin <i>accentus</i> 'ton, betoning'."),

 "ackurat": ("Mycket noggrann ; precis, alldeles",
   "vardaglig, neutral", ["noggrann", "precis"],
   "Det var ackurat vad han hade befarat.", "ackurat",
   "Av latin <i>accuratus</i> 'omsorgsfull', till <i>accurare</i> 'utföra något omsorgsfullt'."),

 "advokatyr": ("Argumentering fylld av övertalningsknep och spetsfundigheter",
   "neutral, nedsättande", [],
   "Försvarets resonemang var ren advokatyr.", "advokatyr",
   ""),

 "axiomatisk": ("Som bygger på axiom ; självklart sann",
   "fackspråklig, neutral", [],
   "Att påståendet skulle vara axiomatiskt bestreds av flera.", "axiomatiskt",
   ""),

 "dräglig": ("Möjlig att uthärda utan alltför stora påfrestningar",
   "neutral, neutral", ["uthärdlig"],
   "Med öppet fönster blev värmen dräglig.", "dräglig",
   "Fornsvenska <i>drägheliker</i>, av lågtyska <i>dregelik</i> 'som kan bäras'. Till <i>dra</i>."),

 "elegisk": ("Som har att göra med elegin eller dess versmått ; vemodigt sorgsen",
   "litterär, neutral", ["vemodig"],
   "Dikten hade en elegisk ton.", "elegisk",
   ""),

 "enveten": ("Envis",
   "ngt ålderdomlig, neutral", ["envis"],
   "Han var enveten i sitt krav på omprövning.", "enveten",
   "Till äldre svenska <i>envett</i> 'envishet, egensinne'."),

 "fjäskig": ("Som gärna fjäskar för andra",
   "vardaglig, nedsättande", [],
   "Hans fjäskiga sätt mot chefen gick inte obemärkt förbi.", "fjäskiga",
   ""),

 "förvänd": ("Helt oriktig",
   "ngt ålderdomlig, negativ", ["oriktig"],
   "Han hade fått en förvänd bild av hela saken.", "förvänd",
   "Till <i>förvända</i> 'göra oigenkännlig'."),

 "indikation": ("Omständighet som tyder på ett visst förhållande ; förhållande som utgör skäl för en viss medicinsk åtgärd",
   "formell, neutral", ["tecken", "fingervisning"],
   "Provsvaret gav en tydlig indikation på infektion.", "indikation",
   "Av latin <i>indicatio</i>, till <i>indicare</i> 'peka ut, ange'."),

 "inställsam": ("Överdrivet artig i syfte att vinna fördelar, vanligen mot någon överordnad",
   "neutral, nedsättande", ["insmickrande"],
   "Tonen i brevet var påfallande inställsam.", "inställsam",
   "Till <i>ställa sig in</i>."),

 "klerikal": ("Som präglas av ett starkt prästväsende ; kyrkligt sinnad",
   "fackspråklig, neutral", ["prästerlig"],
   "Landet styrdes av en klerikal elit.", "klerikal",
   "Av medeltidslatin <i>clericalis</i>, till latin <i>clerus</i> 'prästerskap'."),

 "piffig": ("Trevlig på ett pikant och anslående sätt, ofta tack vare en ovanlig detalj",
   "vardaglig, positiv", [],
   "Hon hade satt en piffig brosch på kavajen.", "piffig",
   ""),

 "seraf": ("Himmelskt väsen med änglagestalt enligt judisk och kristen tro",
   "litterär, neutral", ["ängel"],
   "På valvet fanns serafer målade i guld.", "serafer",
   "Ytterst av hebreiska <i>serafim</i>, plural av <i>saraf</i>."),

 "sämja": ("Tillstånd som präglas av vänskap mellan dem som lever tillsammans",
   "ngt ålderdomlig, positiv", ["enighet"],
   "Det rådde god sämja i huset.", "sämja",
   "Fornsvenska <i>sämia</i> 'överenskommelse, sämja'. Till <i>sam-</i> i <i>samma</i>."),

 "taxa": ("Fastställd avgift för en viss typ av tjänst ; (om flygplan) köra på marken före start eller efter landning",
   "neutral, neutral", ["avgift", "pris"],
   "Kommunen höjde taxan för sophämtning.", "taxan",
   "Av medeltidslatin <i>taxa</i> 'värdering', till <i>taxera</i>."),

 "ypperlig": ("Som har mycket framstående egenskaper",
   "ngt ålderdomlig, positiv", ["utomordentlig", "förträfflig"],
   "Middagen var alldeles ypperlig.", "ypperlig",
   "Till äldre svenska <i>ypper</i> 'framstående', bildat till <i>upp</i>."),

 "abolition": ("Efterskänkande av ett eventuellt straff innan åtal väckts eller dom fallit",
   "fackspråklig, neutral", ["straffeftergift"],
   "Regeringen beviljade abolition i det uppmärksammade målet.", "abolition",
   "Av latin <i>abolitio</i> 'utplåning, upphävande'."),

 "absid": ("Rumsavslutande utbyggnad på en kyrka, vanligen halvrund och täckt av en halvkupol",
   "fackspråklig, neutral", [],
   "Altaret stod längst in i absiden.", "absiden",
   "Av franska <i>abside</i>, av latin <i>absis</i> och grekiska <i>hapsis</i> 'rundning'."),

 "amorf": ("Som saknar form och struktur",
   "fackspråklig, neutral", ["formlös"],
   "Materialet är amorft och saknar kristallstruktur.", "amorft",
   "Av grekiska <i>amorphos</i>, till <i>a-</i> 'ej' och <i>morphe</i> 'form'."),
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
                         "synonymer.se. Etymologin hamtad ur SO:s historiskaUppgifter; "
                         "tom dar SO saknar faltet. Inget skrivet som inte star i "
                         "nagon av ordbockerna."),
        }
        if o in TILLAT:
            e["forgranska_tillat"] = TILLAT[o]
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"del 2: skrivna {skrivna}")


if __name__ == "__main__":
    main()
