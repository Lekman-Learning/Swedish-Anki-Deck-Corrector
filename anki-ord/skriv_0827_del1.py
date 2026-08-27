# -*- coding: utf-8 -*-
"""Batch 2026-08-27, kort 1-9. Full v3.

register ar en STRANG som delas pa ';' -- ett register per betydelse, i samma
ordning. Forsta versionen skickade en lista och forgranska rapporterade da
domanen som "'juridik']".

Flera betydelser separeras med ' ; ' i huvudbetydelsen (baksida.betydelser).
"""
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


satt("chanson",
     "Fransk visa där texten bär låten mer än melodin gör",
     "neutral, neutral, musik",
     ["visa"],
     "Hon sjöng en gammal " + B % "chanson" + " om Paris, och varje ord hördes.",
     "→ Franska chanson 'sång, visa', av latin cantio 'sång'.",
     "SO: 'typ av (fransk) visa med enkel melodi'. SAOL: 'fransk visa'. "
     "Legacy hade chansonett som synonym -- den avslojar uppslagsordet och ar struken.")

satt("dimension",
     "Hur stort något är åt ett visst håll: längd, bredd eller höjd ; "
     "färdig storleksklass som brädor och varor säljs i ; "
     "bildligt: en sida av en fråga som man inte sett förut",
     "neutral, neutral ; fackspråklig, neutral ; neutral, neutral",
     ["mått", "storlek", "utsträckning"],
     "Balken måste ha rätt " + B % "dimension" + ", annars håller inte taket.",
     "→ Latin dimensio 'uppmätning', av dis- 'isär' och metiri 'mäta'.",
     "SAOL: 'matt i langd, bredd el. hojd; utstrackning'. SO ger 'storlek' och "
     "sarskilt 'varor i standardiserade storlekar' samt den bildliga "
     "anvandningen. Alla tre synonymerna star ordagrant i definitionstexten.",
     tillat={"betydelse_kan_saknas":
             "SO:s 7 poster ar 3 betydelser plus 2 JFR-taggar och 2 "
             "'av. allmannare'-varianter av mattbetydelsen. Kortet tacker "
             "rumslig utstrackning, standardstorlek och den bildliga."})

satt("dynasti",
     "Familj som ärver makten och regerar i flera led efter varandra ; "
     "tidsperiod som en sådan familj styrde under ; "
     "bildligt: familj som dominerat ett område i generationer",
     "neutral, neutral, historia ; neutral, neutral ; neutral, neutral",
     ["härskarätt", "furstehus"],
     "Den egyptiska " + B % "dynastin" + " satt vid makten i över tvåhundra år.",
     "→ Grekiska dynasteia 'härskarmakt'.",
     "SAOL: 'harskaratt, furstehus' -- bada leder var sitt led. SO ger aven "
     "tidsmattsbetydelsen ('Egypten under den 14:e dynastin') och den bildliga "
     "('dynastin Wallenberg').")

satt("frisera",
     "Ordna håret snyggt ; bildligt: snygga till siffror eller en historia "
     "så att de ser bättre ut än de är",
     "neutral, neutral ; neutral, lätt negativ",
     ["ordna", "försköna"],
     "Regeringen försökte " + B % "frisera" + " arbetslöshetssiffrorna före valet.",
     "→ Franska friser 'krusa, ondulera'.",
     "SO: 'ordna (har eller dylikt) pa prydligt satt | forskona'. SAOL: "
     "'lagga haret pa; bildl. forskona'. SO:s ovriga tre poster ar "
     "bojningsvarianter av samma tva betydelser (frisera sig, frisera nagon), "
     "inte skilda betydelser -- darfor tva pa kortet.",
     tillat={"betydelse_kan_saknas":
             "SO:s 5 poster ar 2 betydelser plus 3 konstruktionsvarianter av "
             "dem (reflexivt och med personobjekt). Kortet tacker bada "
             "betydelserna; den bildliga ar den HP provar."})

satt("i stadens hank och stör",
     "Innanför stadens gränser — det som räknas som själva staden, inte landsbygden runt om",
     "ngt ålderdomlig, neutral",
     [],
     "De ville bo kvar inom " + B % "stadens hank och stör" + " och inte flytta ut på landet.",
     "→ Hank var vidjan som band ihop störarna i en gärdsgård.",
     "SO ger 'inom stadens granser' och exemplet 'inom stadens hank och stor', "
     "markt 'vard.'. VARNING: API:t hanterar inte flerordsuttryck, sa uppslaget "
     "drog in helt obeslaktade poster (rom, rum, insjo) -- bara hank-posten ar "
     "relevant. Tom synonymlista: uttrycket har ingen enordssynonym.",
     tillat={"frammande_uppslagsord":
             "Frasuppslag: svenska.se returnerar traffar for varje ingaende "
             "ord (hank, stor, stad) plus slumpvisa grannposter. De 29 "
             "'frammande' uppslagsorden ar API-brus, inte fel i kortet.",
             "betydelse_kan_saknas":
             "Samma orsak: de 6 betydelserna kommer fran olika uppslagsord. "
             "Uttrycket sjalvt har en betydelse.",
             "register_motsager_markning":
             "Samma API-brus: uppslaget returnerar bade 'vard.' (fran en "
             "obeslaktad post) och 'nagot alderdomligt' (fran hank-posten). "
             "Forgranska vaxlar mellan dem mellan korningar. Uttrycket ar "
             "alderdomligt -- belagt sedan 1300-talet och knappt anvant idag."},
     conf=8)

satt("instans",
     "Nivå i domstolstrappan — är man missnöjd överklagar man uppåt till nästa ; "
     "myndighet eller organ som fattar beslut i en fråga",
     "neutral, neutral ; neutral, neutral",
     ["nivå", "myndighet"],
     "Hovrätten fastställde den lägre " + B % "instansens" + " dom.",
     "→ Latin instantia 'enträgenhet', via tyska Instanz.",
     "SAOL: 'klass el. niva i domstolsvasen el. forvaltning; over- el. "
     "underordnad myndighet'. Bada synonymerna star dar ordagrant. SO skiljer "
     "domstolsnivan fran 'vissa andra myndigheter, ibland utan hansyn till "
     "niva' -- darfor tva betydelser.",
     tillat={"betydelse_kan_saknas":
             "SO:s 4 poster ar 2 betydelser plus frasen 'i sista instans' "
             "och en 'el.'-variant. Kortet tacker bada betydelserna."})

satt("likgiltigt",
     "Som inte bryr sig det minsta ; som inte är värd att bry sig om",
     "neutral, neutral ; neutral, neutral",
     ["ointresserad"],
     "Hon ställde sig " + B % "likgiltigt" + " till förslaget och ryckte på axlarna.",
     "→ Efter tyska gleichgültig med samma betydelse.",
     "SO: 'helt ointresserad | som inte formar vacka nagot intresse' -- exakt "
     "de tva betydelserna. SO:s JFR-lista (haglos, indifferent, liknojd, egal) "
     "ar cohyponymer, inte synonymer, och ar darfor inte inskrivna.")

satt("lyhörd",
     "Som snabbt märker vad andra känner och tar hänsyn till det ; "
     "om ett rum: där ljud lätt hörs rakt igenom väggarna",
     "neutral, positiv ; neutral, lätt negativ",
     ["dåligt ljudisolerad"],
     "Chefen var " + B % "lyhörd" + " för vad personalen faktiskt behövde.",
     "→ Efter danska lydhør, till lyd 'ljud'.",
     "SO: 'som latt uppfattar och tar hansyn till (nagot)' och 'som har sadan "
     "akustik att (onskade) ljud latt fortplantas'. TVA betydelser som drar at "
     "motsatt hall -- om person positivt, om lagenhet negativt, och det ar "
     "precis den kontrasten HP provar. 'uppmarksam' ur old_facit ar STRUKEN: "
     "ordet star varken som SYN:synonym eller i SO/SAOL:s definitionstext.",
     tillat={"betydelse_kan_saknas":
             "SO:s 4 poster ar 3 betydelser, varav 'fin och kanslig horsel' "
             "och 'uppfattar och tar hansyn till' ar samma betydelse "
             "bokstavligt respektive bildligt. Kortet ger den bildliga (den "
             "vanliga) plus akustikbetydelsen."})

satt("retardera",
     "Sakta ner ; få något annat att sakta ner ; "
     "bildligt: bromsa en utveckling så att den går långsammare",
     "fackspråklig, neutral ; fackspråklig, neutral ; neutral, lätt negativ",
     ["fördröja"],
     "Bilen " + B % "retarderade" + " långsamt nedför backen.",
     "→ Latin retardare 'göra långsam, fördröja'. Motsats: accelerera.",
     "SAOL: 'fa att minska farten; fordroja'. SO: 'minska sin hastighet | fa "
     "att minska hastigheten | av. bildligt'. SO markerar 'mest i facksprak'. "
     "accelerera star som MOTSATS:antonym -- det ar paret HP staller upp.",
     tillat={"betydelse_kan_saknas":
             "SO:s 5 poster ar 3 betydelser plus MOTSATS-taggen och en "
             "'nagon gang av.'-variant, vilka inte ar egna betydelser. "
             "Kortet tacker intransitivt, transitivt och bildligt."})

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Skrev %d kort." % sum(1 for k in KORT if k.get("approved")))
