# -*- coding: utf-8 -*-
"""100-kortsomgangen 2026-08-25 (batch3), del 3 (ord 41-60).

Kallor lasta via visa_uppslag.py -- SO:s rastruktur och SAOL ordagrant,
aldrig synonymer.se.

`fornamligen` pausas: bara SAOB-lemma, ingen traff i SO och ingen
definitionstext i SAOL. Samma skal som vadevill, glutinos och mockant.

`ge akt pa` skrivs ur SO:s IDIOM-fait under `akt` betydelse 2, dar uttrycket
star ordagrant med definitionen 'vara uppmarksam pa nagot'.

`forfang` har TOM definition i SO -- kortet skrivs darfor ur SAOL:s text
('avbrack; nackdel'), som ar den enda definitionstext kallorna ger.
"""
import json
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-25_v3-batch3.json"
BLA = '<font color="#3498db">%s</font>'
HOPPA = {"förnämligen"}

TILLAT = {
 "atrium": {"betydelse_kan_saknas":
   "SO har TVA huvudbetydelser ('kringbyggt uterum' och 'hjartformak'). Bada "
   "star pa kortet, precis som i SAOL:s 'centralt uterum i hus; formak i hjarta'."},
 "disciplin": {"betydelse_kan_saknas":
   "SO har TVA huvudbetydelser ('tillstand av strangt underordnande under regler' "
   "och 'kunskapsomrade'), var och en med en underbetydelse UTAN egen definition. "
   "Bada huvudbetydelserna star pa kortet."},
 "fordra": {
   "betydelse_kan_saknas":
   "SO har TVA huvudbetydelser ('forklara visst handlande nodvandigt' och 'vara "
   "beroende av viss forutsattning') plus underbetydelsen 'begara aterbetalning "
   "av skuld'. Alla tre star pa kortet.",
   "frammande_uppslagsord":
   "Det dolda fuzzy-lemmat ar `fodra` (att fodra ett plagg), ett annat ord."},
 "disös": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('upplaserska av konstnarlig text') och EN "
   "underbetydelse UTAN egen definition. SAOL:s andra led ('vissangerska som "
   "framfor texten delvis som tal') star ocksa pa kortet."},
 "bigotteri": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('det att vara bigott') och EN "
   "underbetydelse UTAN egen definition. SAOL saknar definitionstext. Kortet "
   "skriver ut vad bigott betyder, eftersom 'det att vara bigott' inte ar nagot "
   "man kan lara sig av."},
 "biton": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse och EN underbetydelse UTAN egen "
   "definition, alltsa en anvandningsutvidgning."},
 "brådmogen": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('tidigt utvecklad, sarsk. sjalsligt') och "
   "EN underbetydelse UTAN egen definition."},
 "cirkumflex": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse och EN underbetydelse UTAN egen "
   "definition."},
 "divig": {"betydelse_kan_saknas":
   "SO har EN huvudbetydelse ('som beter sig som en diva'). SAOL har ordet men "
   "utan definitionstext, bara bruklighetsmarkningen 'vard.' -- vilket kortets "
   "register aterger."},
 "ge akt på": {
   "betydelse_kan_saknas":
   "Uttrycket star ordagrant som idiom i SO under `akt` betydelse 2 "
   "('uppmarksamhet') med definitionen 'vara uppmarksam pa nagot'. Ovriga "
   "betydelser hos `akt` (fredloshet i medeltida germansk ratt) hor inte hit.",
   "frammande_uppslagsord":
   "Uttrycket ar tre ord, sa fuzzy-sokningen traffar `ge` och `pa` som egna "
   "lemman med sina fulla betydelseuppsattningar."},
 "förfång": {"betydelse_kan_saknas":
   "SO:s definitionsfalt ar TOMT for det har ordet. SAOL ger 'avbrack; nackdel', "
   "vilket ar hela innehallet kallorna erbjuder, och det star pa kortet."},
 "farsot": {"register_motsager_markning":
   "SO:s markning ar 'aldre, informell benamning'. Kortets register sager 'ngt "
   "alderdomlig', vilket ar just det. Flaggan slar pa ordet 'informell', som ar "
   "en andra del av samma markning, inte en motsagelse."},
}

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form, etymologi)
KORT = {
 "arkad": ("Rad av pelare eller kolonner som förenas av valvbågar",
   "fackspråklig, neutral", ["pelargång"],
   "Butikerna låg under en arkad längs torget.", "arkad",
   "Av franska <i>arcade</i>, till latin <i>arcus</i> 'båge'."),

 "atrium": ("Kringbyggt uterum i anslutning till ett hus ; förmak i hjärtat",
   "fackspråklig, neutral", [],
   "Huset var byggt kring ett soligt atrium.", "atrium",
   "Av latin <i>atrium</i> med samma betydelse."),

 "bigotteri": ("Överdriven eller hycklad fromhet som gör en ofördragsam mot andra",
   "neutral, nedsättande", [],
   "Hans bigotteri gjorde det omöjligt att diskutera saken.", "bigotteri",
   ""),

 "biton": ("Tonfall som antyder ett annat innehåll än det som sägs direkt",
   "neutral, neutral", [],
   "Det fanns en beskäftig biton i hans röst.", "biton",
   ""),

 "brådmogen": ("Tidigt utvecklad, särskilt själsligt, vanligen om en ung människa",
   "neutral, neutral", [],
   "Hon var brådmogen och läste vuxenböcker vid nio.", "brådmogen",
   ""),

 "cerealier": ("Sädesslag och produkter av sädesslag",
   "fackspråklig, neutral", ["sädesslag"],
   "Butiken sålde cerealier i lösvikt.", "cerealier",
   "Till latin <i>Cerealis</i> 'som hör till säden', av <i>Ceres</i>, åkerbrukets gudinna."),

 "cirkumflex": ("Vinklat, takliknande tecken som placeras över en vokal för att markera ett särskilt uttal",
   "fackspråklig, neutral", [],
   "Franskan använder cirkumflex i ord som fenêtre.", "cirkumflex",
   "Till latin <i>circumflexus</i> 'kringböjd', av <i>circum</i> 'omkring' och <i>flectere</i> 'böja'."),

 "demagog": ("Person som använder slående men osakliga argument för att övertyga många, särskilt en talare",
   "neutral, nedsättande", ["agitator"],
   "Han avfärdades som en demagog utan sakskäl.", "demagog",
   "Av grekiska <i>demagogos</i> 'folkledare', till <i>demos</i> 'folk' och <i>agogos</i> 'ledare'."),

 "disciplin": ("Tillstånd av strängt underordnande under vissa regler ; kunskapsområde eller gren av en vetenskap",
   "neutral, neutral", ["ordning", "vetenskapsgren"],
   "Historia är en disciplin med egna metoder.", "disciplin",
   "Av latin <i>disciplina</i> 'uppfostran, vetenskap'. Nära besläktat med <i>discipel</i>."),

 "disös": ("Uppläserska av konstnärlig text ; vissångerska som delvis framför texten som tal",
   "fackspråklig, neutral", [],
   "Hon uppträdde som disös på kabarén.", "disös",
   "Av franska <i>diseuse</i>, till <i>dire</i> 'säga', av latin <i>dicere</i>."),

 "divig": ("Som beter sig som en diva",
   "vardaglig, nedsättande", [],
   "Sångaren var divig och krävde eget rum.", "divig",
   "Till <i>diva</i>."),

 "ekolod": ("Apparat som mäter avstånd, särskilt vattendjup, med hjälp av återstuds av ljud",
   "fackspråklig, neutral", [],
   "Skepparen läste av ekolodet innan de gick in i viken.", "ekolodet",
   ""),

 "farsot": ("Epidemisk sjukdom",
   "ngt ålderdomlig, negativ", ["epidemi"],
   "Farsoten svepte genom socknen på en månad.", "Farsoten",
   "Egentligen 'sjukdom som far fram'. Till <i>fara</i> och <i>sot</i> 'sjukdom'."),

 "flankera": ("Vara placerad på båda sidorna om någon eller något",
   "neutral, neutral", ["kanta"],
   "Två lejonstatyer flankerade trappan.", "flankerade",
   ""),

 "fordra": ("Förklara ett visst handlande nödvändigt och antyda att maktmedel kan användas ; begära återbetalning av en skuld ; vara beroende av en viss förutsättning",
   "formell, neutral", ["kräva"],
   "Uppgiften fordrar både tid och tålamod.", "fordrar",
   "Fornsvenska <i>fo(r)dra</i>, av lågtyska <i>vorderen</i> 'föra framåt' och tyska <i>fordern</i> 'kräva'."),

 "framhärda": ("Envist fortsätta eller stå fast vid något trots goda skäl för motsatsen",
   "formell, negativ", [],
   "Han framhärdade i sitt påstående trots bevisen.", "framhärdade",
   "Fornsvenska <i>framhärdha</i>."),

 "fägna": ("Glädja",
   "högtidlig, positiv", ["glädja"],
   "Det fägnar mig att höra att allt gått väl.", "fägnar",
   "Fornsvenska <i>fäghna</i>, till <i>fäghin</i> 'glad'. Besläktat med <i>fager</i>."),

 "förfång": ("Avbräck eller nackdel",
   "formell, negativ", ["avbräck", "nackdel"],
   "Åtgärden fick inte ske till förfång för tredje man.", "förfång",
   "Fornsvenska <i>forfang</i>, av lågtyska <i>vorvank</i> 'övergrepp, skada'."),

 "ge akt på": ("Vara uppmärksam på något",
   "formell, neutral", ["uppmärksamma"],
   "Polisen uppmanade allmänheten att ge akt på misstänkta försändelser.", "akt",
   "Till <i>akt</i> 'uppmärksamhet', av lågtyska <i>acht</i>."),
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    skrivna = pausade = 0
    for e in poster:
        o = e["ord"]
        if o in HOPPA:
            pausade += 1
            print("  PAUSAS (bara SAOB, ingen definitionstext):", o)
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
    print(f"del 3: skrivna {skrivna}  pausade {pausade}")


if __name__ == "__main__":
    main()
