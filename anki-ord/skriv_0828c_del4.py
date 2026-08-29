# -*- coding: utf-8 -*-
"""Batch 2026-08-28 v3-batch100, kort 76-100. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch100.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
B = '<font color="#3498db">%s</font>'


def kallor(o, *extra):
    k = urllib.parse.quote(o)
    return " ".join([
        "https://svenska.se/api/msearch?ord=%s" % k,
        "https://www.synonymer.se/sv-syn/%s" % k,
        "https://sv.wiktionary.org/wiki/%s" % k,
        *extra,
    ])


def satt(o, bet, reg, syn, ex, ety, slutsats, grupper=None, extra=(), conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": grupper, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": kallor(o, *extra), "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True


satt("laminat",
     "Material som byggts upp av flera tunna lager limmade på varandra",
     "neutral, neutral, teknik",
     [],
     "Bänkskivan var av " + B % "laminat" + ", inte massivt trä.",
     "→ Till latin lamina 'metallskiva, brada'; samma rot som lamell.",
     "SO: 'material av sammanfogade tunna skikt'. SAOL sager samma sak. "
     "Ordet 'skikt' ar utbytt mot 'lager' i facit eftersom skikt ar lika "
     "ovanligt som uppslagsordet. SO:s JFR plastlaminat ar en "
     "sammansattning, inte en synonym.")

satt("lastbar",
     "Som lever ett liv fullt av laster och njutningar som omgivningen "
     "fördömer",
     "ngt ålderdomlig, nedsättande, allmän",
     [],
     "Bibelns berättelse om de " + B % "lastbara" + " kvinnorna.",
     None,
     "SO: 'som for ett osunt, klandervart leverne', med markningen nagot "
     "alderdomligt och underbetydelsen 'av. om handling och dylikt'. SAOL: "
     "'hemfallen at forkastligt livssatt'. FALLA: ordet ser ut att hora "
     "ihop med last i betydelsen 'borda pa ett fordon' men hor till last i "
     "betydelsen 'ovana, synd'. Den kopplingen ar inte utskriven som "
     "etymologi eftersom varken SO eller SAOL ger nagon harledning for "
     "ordet.")

satt("ljuster",
     "Fiskeredskap format som en gaffel med hullingar, som stöts eller "
     "kastas rakt ner i fisken",
     "fackspråklig, neutral, jakt",
     [],
     "Han stod i fören med " + B % "ljustret" + " lyft över vattnet.",
     "→ Fornsvenska liuster, till ett verb som motsvarar islandska ljosta "
     "'hugga, stota'.",
     "SO: 'ett gaffelformigt fiskredskap som kastas eller stots mot "
     "fisken'. SAOL: 'ett gaffel- el. kamliknande fiskeredskap'. Hullingarna "
     "kommer fran Wiktionary och ar med, eftersom de forklarar varfor "
     "fisken sitter kvar. SO:s JFR (gaffel, treudd) ar cohyponymer -- "
     "foremal med liknande form, inte utbytbara ord. Domanen ar satt till "
     "jakt eftersom listan saknar fiske.")

satt("misskundsam",
     "Som visar medlidande och förbarmar sig över den som har det svårt",
     "arkaisk, positiv, allmän",
     ["barmhärtig"],
     "En " + B % "misskundsam" + " herre som efterskänkte hela skulden.",
     None,
     "SVAGT BELAGD: varken SO eller SAOL har nagot uppslag alls for ordet. "
     "Enda kallan ar Wiktionary: 'barmhartig; medlidsam'. Att ordet saknas "
     "i bada de moderna ordbockerna ar i sig skalet till registret arkaisk "
     "-- det ar en slutsats av franvaron, inte en markning nagon kalla "
     "gett. Synonymen barmhartig ar Wiktionarys forsta glosa.",
     conf=5)

satt("munväder",
     "Tomt prat: stora ord som det inte finns någon täckning för",
     "vardaglig, nedsättande, allmän",
     [],
     "Han lovade evig trohet, men det var bara " + B % "munväder" + ".",
     None,
     "SO: '(mangd av) yttranden utan vasentligt innehall', med markningen "
     "vard. SAOL: 'tomt prat' -- darifran formuleringen i facit. SO:s JFR "
     "(struntprat, svammel) ar cohyponymmarkta och tas inte upp som "
     "synonymer: svammel ar osammanhangande, munvader ar valformulerat men "
     "tomt, och det ar just den skillnaden ordet bar.")

satt("oefterrättlig",
     "Som inte går att få ordning på och inte heller själv försöker bättra "
     "sig",
     "formell, negativ, allmän",
     ["oförbätterlig"],
     "Den odågan är helt " + B % "oefterrättlig" + ".",
     "→ Till o- och aldre efterrattlig 'som rattar sig efter'.",
     "SO: 'som inte kan forbattras eller forsoker forbattra sig', SYN-markt "
     "mot oforbatterlig, med markningen formellt. SAOL: 'som man inte kan "
     "fa ordning pa, oforbatterlig'. Bada leden i SO:s definition ar med i "
     "facit -- att andra misslyckas OCH att personen sjalv inte forsoker; "
     "det ar den andra halvan som gor ordet hardare an oforbatterlig.")

satt("patriarkat",
     "Samhällsskick där fadern eller männen har makten i familjen och "
     "samhället ; en kyrklig patriarks ämbete, eller det område han styr "
     "över",
     "neutral, neutral, allmän ; fackspråklig, neutral, religion",
     ["fadersvälde"],
     "Debatten om " + B % "patriarkatet" + " handlar om vem som egentligen "
     "har makten i hemmet.",
     None,
     "SO ger tre betydelser: patriarkens ambete, samhallsskicket dar fadern "
     "har oinskrankt myndighet, och 'fadersvalde' (av. forsvagat, dvs. det "
     "moderna bruket om mans makt i allmanhet). De tva sistnamnda ar samma "
     "sak i olika styrka och ar hopslagna; synonymen fadersvalde ar SO:s "
     "och SAOL:s egen definitionstext. Ordningen ar vand mot SO:s: den "
     "kyrkliga betydelsen ar aldst men den samhalleliga ar den enda de "
     "flesta moter. JFR matriarkat ar motsatsen, inte en synonym.")

satt("paulun",
     "Säng med tak och draperier runt om ; själva tyget som hänger runt "
     "sängen ; skämtsamt om vilken säng som helst",
     "ngt ålderdomlig, neutral, historia ; ngt ålderdomlig, neutral, "
     "historia ; ngt ålderdomlig, skämtsam, allmän",
     [],
     "Han låg kvar i sitt " + B % "paulun" + " långt fram på dagen.",
     "→ Fornsvenska paulun 'talt, sparlakanssang'; av lagtyska paulune "
     "'talt, baldakin'; av franska pavillon -- samma ord som paviljong.",
     "SO: 'himmelssang' och 'sangomhange', med underbetydelsen 'ibland om "
     "sang el. annan viloplats i allmanhet' och markningen skamtsamt. SAOL "
     "markar ald. Alla tre leden ar med. Etymologin ar med for att den "
     "forklarar varfor ordet betyder bade tyget och sangen: det var fran "
     "borjan ett talt.")

satt("principal",
     "Förr: den man arbetar åt — arbetsgivaren eller uppdragsgivaren ; i en "
     "orgel: den grundläggande huvudstämman ; som förled: huvud-, den "
     "viktigaste",
     "arkaisk, neutral, allmän ; fackspråklig, neutral, musik ; neutral, "
     "neutral, allmän",
     [],
     "Bokhållaren vågade inte säga emot sin " + B % "principal" + ".",
     "→ Latin principalis 'ursprunglig, fornamst', till princeps 'den "
     "fornamste'; samma rot som prins.",
     "SO ger tre betydelser: 'arbets- eller uppdragsgivare' (markning: "
     "alderdomligt), 'huvudstamma i orgel' och forleden 'huvud-'. SAOL "
     "bekraftar alla tre. Alla ar med -- forleden ar den enda som lever i "
     "modern svenska (principiell fraga, principal komponent), och den "
     "skulle fallit bort om bara den forsta betydelsen tagits.")

satt("probabilitet",
     "Sannolikhet",
     "fackspråklig, neutral, allmän",
     ["sannolikhet"],
     "Beräkningen bygger på " + B % "probabiliteten" + " för varje utfall.",
     None,
     "SO och SAOL ger bada exakt ett ord: 'sannolikhet' -- darav synonymen, "
     "ur definitionstexten. SO:s markning: nastan enbart i facksprak, darav "
     "formalitetsnivan fackspraklig. NAGON DOMAN ANGES INTE av SO, och "
     "trots att ordet i praktiken hor hemma i statistik ar domanen satt "
     "till allman -- att skriva matematik vore en gissning. Kortet ar "
     "avsiktligt ett rent glosekort: det finns ingenting att forklara ett "
     "steg neroat nar synonymen ar det vanliga svenska ordet.")

satt("pult",
     "Litet podium med notställ, som en dirigent står vid ; också om "
     "notstället ensamt",
     "fackspråklig, neutral, musik ; fackspråklig, neutral, musik",
     [],
     "De satt vid samma " + B % "pult" + " i symfoniorkestern.",
     "→ Tyska Pult; av latin pulpitum 'tribun'; samma rot som pulpet.",
     "SO: 'litet podium med pulpet' och 'notstall', med underbetydelsen "
     "'ibland av.' Bada med. SAOL: 'podium med notstall for dirigent; "
     "notstall'. SO:s exempel visar att musiker som delar notstall sags "
     "sitta vid samma pult -- det ar den vanligaste anvandningen och ar "
     "vald till exempelmening.")

satt("reda pengar",
     "Kontanter — pengar i sedlar och mynt, till skillnad från betalning på "
     "annat sätt",
     "neutral, neutral, ekonomi",
     ["kontanter"],
     "Han ville ha betalt i " + B % "reda pengar" + ", inte i löften.",
     "→ Fornsvenska redha, av lagtyska rede 'redo, tillganglig' -- pengar "
     "som finns till hands.",
     "MISSLYCKAD UPPSLAGNING: sokningen mot svenska.se traffade fel "
     "uppslagsord och returnerade artikeln for REDAKTION ('grupp av "
     "personer som staller samman text- och bildmaterial'), plus SAOL:s "
     "'reda' i betydelsen 'idka rederirorelse'. Ingetdera har med uttrycket "
     "att gora. Det enda anvandbara ur traffen ar att SO:s exempellista "
     "innehaller frasen 'i reda pengar' -- uttrycket ar alltsa belagt, men "
     "utan definition. Facit vilar darfor pa Wiktionary: 'kontanter'. "
     "Registret ar satt till neutralt eftersom den alderdomlighetsmarkning "
     "som syntes i traffen tillhorde det FELAKTIGA uppslagsordet och inte "
     "far overforas hit.",
     conf=6)

satt("sedesam",
     "Som lever anständigt och håller sig till vad omgivningen anser "
     "passande, särskilt i fråga om kläder och umgänge",
     "ngt ålderdomlig, positiv, allmän",
     ["dygdig"],
     "Hon hyrde bara ut rum till " + B % "sedesamma" + " flickor.",
     None,
     "SO: 'skotsam och moraliskt hogtstaende', med markningen nagot "
     "alderdomligt och underbetydelsen 'av. om foreteelse, handling eller "
     "dylikt som ger sadant intryck' -- darav ledet om klader (SO:s eget "
     "exempel: 'en sedesam klanning med vit krage'). SAOL: 'dygdig', darav "
     "synonymen. SO:s JFR arbar ar cohyponymmarkt och tas inte upp. "
     "Ordet siktar i praktiken nastan alltid pa kvinnor, vilket bada SO:s "
     "exempel visar.")

satt("simultan",
     "Som sker samtidigt med något annat",
     "fackspråklig, neutral, allmän",
     ["samtidig"],
     "Föredraget tolkades " + B % "simultant" + " till tre språk.",
     "→ Till latin simul 'pa samma gang'.",
     "SO och SAOL ger bada 'samtidig' -- darav synonymen, ur "
     "definitionstexten. SO:s markning: sarsk. i fackspraliga sammanhang, "
     "darav formalitetsnivan. SO:s JFR simultantolkning ar en "
     "sammansattning och ar anvand som exempelmening i stallet, eftersom "
     "det ar det sammanhang de flesta moter ordet i.")

satt("singulär",
     "Ensam i sitt slag: något som bara inträffat en enda gång eller inte "
     "liknar något annat",
     "neutral, neutral, allmän",
     ["säregen"],
     "En " + B % "singulär" + " händelse i historien, utan motstycke förr "
     "eller senare.",
     "→ Franska singulier; samma rot som singularis.",
     "SO: 'ensam i sitt slag'. SAOL lagger till 'saregen, egendomlig' -- "
     "darav synonymen, ur definitionstexten. Ingen bruklighetsmarkning i "
     "vare sig SO eller SAOL, sa registret ar neutralt trots att ordet "
     "kanns lart. FALLA: singular (matematikens och grammatikens ord) ar "
     "ett annat ord och ska inte blandas ihop; SO:s exempel 'singulara "
     "varden' hor till matematiken men ar samma adjektiv.")

satt("slana",
     "Lång, smal och böjlig stång av trä, ofta en avkvistad ung trädstam",
     "neutral, neutral, allmän",
     [],
     "Ett provisoriskt staket av " + B % "slanor" + ".",
     "→ Svensk dialekt slana; ev. beslaktat med norska slada 'luta svagt'.",
     "SO: 'smal och bojlig stang av tra'. SAOL: 'lang och smal tradstam; "
     "klen spira; stang'. Bada leden -- att den ar bojlig (SO) och att den "
     "kommer fran en ung tradstam (SAOL) -- ar med, eftersom de tillsammans "
     "skiljer en slana fran vilken stang som helst. Wiktionary ger "
     "dessutom en overford betydelse, 'lang, mager flicka'; den ar "
     "UTELAMNAD eftersom den bara har en kalla och saknas helt i bade SO "
     "och SAOL.")

satt("spe",
     "Hån: att göra narr av någon för att visa förakt ; i uttrycket \"in "
     "spe\": blivande, ännu inte men snart",
     "neutral, negativ, allmän ; neutral, neutral, allmän",
     ["hån", "gyckel"],
     "Han fick utstå spott och " + B % "spe" + " av hela byn.",
     "→ Fornsvenska spe, av lagtyska spe; beslaktat med spy. Uttrycket in "
     "spe ar daremot latin, till spes 'hopp'.",
     "SO ger tva betydelser under samma uppslag: 'illvilligt och "
     "forlojligande uttryck for forakt' och 'blivande'. VIKTIGT: det ar "
     "tva helt skilda ord med olika ursprung -- det forsta germanskt, det "
     "andra latinets spes 'hopp' i frasen in spe ('svager in spe'). Bada "
     "ar med men halls isar i facit, eftersom den som bara lart sig det "
     "ena garanterat lasar fel pa det andra. Synonymerna han och gyckel ar "
     "SAOL:s definitionstext; SO:s JFR (gack, han, spott) raknas inte som "
     "belagg.")

satt("stuckatur",
     "Utsmyckning i gips: lister, rosetter och figurer som formats på plats "
     "i taket och på väggarna",
     "fackspråklig, neutral, konst",
     [],
     "En gammal lägenhet med kakelugnar och " + B % "stuckatur" + " i taket.",
     "→ Italienska stuccatura, till stuck.",
     "SO: 'dekorativt arbete i stuck'. SAOL: 'stuckdekor'. Bada "
     "definitionerna forutsatter att man vet vad stuck ar, sa facit skriver "
     "ut det: gips. Var stuckaturen sitter (tak och vaggar) foljer av SO:s "
     "exempelmening, som ocksa ar behallen.")

satt("supponera",
     "Anta att något är sant och bygga vidare på det, utan att ha bevisat "
     "det",
     "neutral, neutral, allmän",
     ["anta", "förutsätta", "förmoda"],
     "Låt oss " + B % "supponera" + " att uppgiften stämmer.",
     None,
     "SVAGT BELAGD: SO har inget uppslag for ordet. SAOL ger 'anta, "
     "forutsatta, formoda' och Wiktionary samma tre ord -- darav "
     "synonymerna. Ingen bruklighetsmarkning finns hos SAOL, sa registret "
     "ar neutralt trots att ordet i praktiken bara forekommer i "
     "vetenskaplig och filosofisk text; markningen far inte hittas pa. "
     "Ledet 'utan att ha bevisat det' ar tillagt for att skilja ordet fran "
     "'anta' i vardaglig mening.",
     conf=7)

satt("tillsyn",
     "Att hålla ett öga på något eller någon och se till att det sköts som "
     "det ska",
     "neutral, neutral, allmän",
     ["uppsikt", "övervakning"],
     "Avfallet lagras under " + B % "tillsyn" + " av två kontrollanter.",
     "→ Fornsvenska tilsyn.",
     "SO: 'det att ge akt pa och vaka over'. SAOL: 'uppsikt, overvakning' "
     "-- darav bada synonymerna, ur definitionstexten. SO:s langa JFR-lista "
     "(kontroll, omsorg, barntillsyn m.fl.) ar cohyponymer och "
     "sammansattningar och raknas inte. I myndighetssprak har ordet en "
     "snavare, formell betydelse (statlig tillsyn over en verksamhet) som "
     "vaxt fram ur den allmanna -- den ar samma ord och ar inte skild ut.")

satt("truga",
     "Enträget försöka övertala någon, särskilt att äta eller ta emot något "
     "; trissan längst ner på en skidstav, som hindrar staven från att sjunka "
     "ner i snön",
     "neutral, neutral, allmän ; fackspråklig, neutral, sport",
     [],
     "Hon " + B % "trugade" + " dem att ta en kaka till.",
     "→ Fornsvenska thruga 'hota, tvinga, truga'; nordiskt ord, beslaktat "
     "med trycka.",
     "SO ger tva betydelser: 'entraget (forsoka) overtala' och "
     "'plaststycke eller dylikt som ar fastsatt i nedre andan av skidstav'. "
     "Bada med -- den andra ar helt oformodad och delar bara stavning med "
     "verbet. SAOL skriver den varianten 'tryga'. Preciseringen om mat "
     "kommer fran SAOL ('t.ex. att ata') och fran SO:s exempel, och ar "
     "med eftersom det ar den situation ordet nastan alltid anvands i.")

satt("yttring",
     "Något som visar sig utåt och avslöjar vad som pågår under ytan ; inom "
     "medicinen: ett symtom",
     "neutral, neutral, allmän ; fackspråklig, neutral, medicin",
     [],
     "Alla " + B % "yttringar" + " av rasism måste bekämpas.",
     None,
     "SO ger tre betydelser: 'tillkannagivande', 'uttryck for bakomliggande "
     "tillstand, forlopp eller verksamhet' och 'symtom' (spec. i medicinska "
     "sammanhang). De tva forsta ar samma sak i olika styrka och ar "
     "hopslagna; den medicinska ar behallen separat. SO:s JFR (yttrande, "
     "viljeyttring) ar cohyponymer och sammansattningar. Poangen som "
     "OLD-facit saknade ar att en yttring alltid pekar pa nagot bakomliggande "
     "-- den ar ett tecken, inte bara ett uttryck.")

satt("zootomi",
     "Läran om hur djurens kroppar är byggda — djurens anatomi",
     "fackspråklig, neutral, biologi",
     ["djuranatomi"],
     "Han undervisade i " + B % "zootomi" + " vid veterinärhögskolan.",
     "→ Grekiska zoon 'djur' och tome 'snitt'; samma rot som anatomi.",
     "SO: 'laran om djurens kroppsbyggnad'. SAOL: 'vetenskapen om djurens "
     "kroppsbyggnad, djuranatomi' -- darav synonymen, ur definitionstexten. "
     "Etymologin ar med eftersom den gor ordet genomskinligt: zoo- 'djur' "
     "plus samma efterled som i anatomi.")

satt("ävenså",
     "Likaså — och på samma sätt gäller det här också",
     "ngt ålderdomlig, neutral, allmän",
     ["likaså"],
     "Hans bror kom, och " + B % "ävenså" + " hans två systrar.",
     None,
     "SO och SAOL ger bada exakt ett ord: 'likasa', med markningen nagot "
     "alderdomligt respektive ald. Darav synonymen, ur definitionstexten. "
     "Wiktionary lagger till 'dessutom, dartill, ocksa'; de ar inte "
     "upptagna som synonymer eftersom de saknas i SO och SAOL, men de "
     "visar att ordet ocksa fungerar rent additivt, vilket facit tacker.")

satt("åmning",
     "Sifferskalan målad på fartygets stäv, som visar hur djupt skrovet "
     "ligger i vattnet",
     "fackspråklig, neutral, sjöfart",
     [],
     "Styrmannen läste av " + B % "åmningen" + " vid fören före avgång.",
     "→ Tyska Ahming, till ahmen 'mata ett karls volym'; till am.",
     "SO: 'markering pa utsida av fartygsskrov, dar djupgaendet kan "
     "avlasas'. SAOL preciserar att det ar en skala av siffror och att den "
     "sitter pa staven -- bada preciseringarna ar med, eftersom SO:s "
     "'markering' ensamt inte later nagon forestalla sig vad det ar. Ordet "
     "'djupgaende' ar upplost till 'hur djupt skrovet ligger i vattnet' "
     "enligt Adam-tal.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("skrev %d kort" % sum(1 for k in KORT if k.get("approved")))
