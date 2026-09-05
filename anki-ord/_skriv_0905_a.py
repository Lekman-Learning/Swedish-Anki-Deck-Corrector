# -*- coding: utf-8 -*-
"""Fyller proposed + sokkoll for de 50 is:review-korten (spar B, 2026-09-05).

Grundregel: kortet ar redan v2 och oftast korrekt -- da kopieras legacy
oforandrat till proposed och sokkoll noterar det. ANDRINGAR gors bara dar
kallan sager nagot annat an kortet.
"""
import io
import json

FIL = 'sessions/session_2026-09-05_v3-omgranskning-repetition.json'
BLA = '<font color="#3498db">%s</font>'

F = {}


def s(ord_, sokkoll, **andringar):
    F[ord_] = (andringar, sokkoll)


# ---------- ANDRADE KORT ----------

s('dra på munnen',
  "synonymer.se + Wiktionary (frasen saknar uppslagsord i SO/SAOL/SAOB -- "
  "svenska.se-traffarna gallde bestandsdelarna och kastades). syn.se ger "
  "'le, skratta', Wiktionary '(sma)le'. ANDRAT: synonymen 'smila' struken -- "
  "smila betyder 'le installsamt, fjaska', vilket ar en annan sak an att dra "
  "pa munnen. Ingen kalla ger smila. Huvudbetydelsen star oforandrad.",
  synonymer=['le'])

s('ombesörja',
  "SO 'utfora', SAOL 'ordna, astadkomma', Wiktionary 'ta ansvar for att nagot "
  "ska komma till stand'. Riskflaggan dold_betydelse (3 synonymer, 1 "
  "betydelse) ar en FALSK POSITIV: alla tre horde till samma betydelse i bada "
  "ordbockerna. ANDRAT: 'at nagon annan' mjukat till 'ofta at nagon annan' -- "
  "SO:s eget exempel ('fastighetsagaren anmodas ombesorja att gangvagarna "
  "sandas') har ingen mottagare, sa villkoret var for hart.",
  huvudbetydelse='Se till att en uppgift blir gjord, ofta åt någon annan')

s('betsel',
  "SO/SAOL 'styrmedel for hast', Wiktionary 'remtyg OCH bett som anvands for "
  "att beharska och styra en hast'. ANDRAT: kortet sa 'redskap i hastens mun' "
  "-- det ar bettet, inte betslet. Betslet ar hela huvudlaget: remmarna plus "
  "bettet. Synonymen 'styrmedel for hast' var en definition, inte en synonym, "
  "och upprepade huvudbetydelsen; utbytt mot 'trans' som SO sjalv ger under "
  "JFR.",
  huvudbetydelse='Remmar och bett på hästens huvud som ryttaren styr med',
  synonymer=['träns'])

s('högoddsare',
  "SO 'nagon/nagot som med storsta sannolikhet inte kommer att vinna', SAOL "
  "'osannolik vinnare av tavling'. ANDRAT: kortet sa 'deltagare', men SO "
  "sager uttryckligen 'nagon/NAGOT' -- ordet anvands ocksa om lag, latar och "
  "forslag. Synonymen '≈≈ forlorarkandidat' var en omskrivning; 'outsider' "
  "star i syn.se och ar det ord Adam faktiskt moter i sporttext.",
  huvudbetydelse='Den som få tror ska vinna',
  synonymer=['outsider'])

s('koloss',
  "SO ger TRE betydelser, kortet hade tva. Den som saknades: 'nagot som "
  "ytligt sett ar stort och imponerande men i verkligheten mycket sarbart' "
  "(SO:s exempel: 'myndigheten har blivit en koloss pa lerfotter'). TILLAGD "
  "som tredje betydelse -- alla tre delar samma etymologi (grekiska "
  "kolossos), det ar alltsa akta flerbetydelse och inte homografi. ANDRAT "
  "ocksa: forsta betydelsens register var 'fackspraklig ... konst', men SO "
  "markerar ingen fackspraklighet -- kolossen pa Rhodos ar allmansprak.",
  huvudbetydelse=('Mycket stor staty ; ovanligt stor person eller sak ; '
                  'något som ser mäktigt ut men är svagt inuti'),
  register='neutral, neutral ; neutral, neutral ; litterär, neutral',
  synonymer=['stor staty', 'bjässe', '≈≈ jätte på lerfötter'],
  synonym_groups=[['stor staty'], ['bjässe'], ['≈≈ jätte på lerfötter']])

s('kronometer',
  "SO 'ur for mycket noggrann tidmatning', SAOL 'ur som haller tiden med stor "
  "noggrannhet'. Huvudbetydelsen ar ratt. ANDRAT: synonymen '≈≈ ur' var for "
  "vid -- den tappar hela poangen (noggrannheten) och gor kortet till en "
  "hyperonym. syn.se ger 'precisionsur', som behaller den.",
  synonymer=['precisionsur'])

s('rayon',
  "SO 'typ av textilfiber som framstalls av cellulosa', med BRUK-markningen "
  "'aldre beteckning, numera ersatt av viskos'. ANDRAT: kortet hade inte med "
  "att ordet ar utdaterat och att samma material i dag heter viskos -- det ar "
  "den enda uppgift som gor ordet begripligt nar Adam moter det. Synonymen "
  "'≈≈ textilfiber' var en hyperonym; 'viskos' ar den verkliga.",
  huvudbetydelse='Konstfiber av cellulosa, numera oftast kallad viskos',
  synonymer=['viskos'])

s('autostrada',
  "SO 'vag med skilda korbanor och utan korsningar i samma plan', SAOL "
  "'motorvag'. ANDRAT: kortet sa 'italiensk motorvag' -- ingen av ordbockerna "
  "begransar ordet till Italien. Etymologin ar italiensk och det ar den "
  "vanligaste anvandningen, sa 'sarskilt italiensk' behalls, men som tillagg "
  "och inte som definition.",
  huvudbetydelse='Motorväg, särskilt italiensk')

s('dyig',
  "SO 'full av dy'. ANDRAT: kortet definierade dyig med 'full av dy' -- ordet "
  "i sin egen definition, vilket ar den harda Adam-tal-regeln. SO far gora "
  "det, decket far inte. Omskrivet utan roten. Betydelsen oforandrad.",
  huvudbetydelse='Full av lös, blöt bottensmörja')

s('eftersinna',
  "SO 'grundligt tanka efter', BRUK 'nagot alderdomligt'. Huvudbetydelse och "
  "register stammer. ANDRAT: synonymen '≈≈ tanka' var for vid -- att tanka ar "
  "inte att eftersinna, hela ordet ligger i grundligheten. '≈≈ tanka efter' "
  "behaller den.",
  synonymer=['≈≈ tänka efter'])

s('injaga',
  "SO 'med hotfulla medel framkalla'. Huvudbetydelsen stammer. ANDRAT: "
  "exempelmeningen sa 'hans LUGNA men bestamda rost injagade respekt', vilket "
  "motsade kortets egen definition ('med hotfulla medel') i samma andetag. "
  "Utbytt mot SO:s eget exempel.",
  exempelmening=('Terroristerna ' + (BLA % 'injagade') +
                 ' skräck i hela befolkningen.'))

s('paternalism',
  "SO 'relation mellan en overordnad och en underordnad part som praglas av "
  "en BESKYDDANDE attityd fran den starkare partens sida'. ANDRAT tva saker: "
  "(1) kortet sa '... och kallar det omtanke', vilket lagger in en anklagelse "
  "om oarlighet som ingen kalla ger -- SO beskriver attityden som "
  "beskyddande, inte som forestalld. (2) valensen 'negativ' struken av samma "
  "skal: varken SO eller SAOL satter nagon BRUK-markning. Att ordet ofta "
  "ANVANDS kritiskt ar en sak; att ordboken markerar det som nedsattande ar "
  "en annan, och den gor den inte.",
  huvudbetydelse=('Att en starkare part bestämmer över en svagare, '
                  'för dennes bästa'),
  register='formell, neutral, politik')

s('pugilist',
  "SO/SAOL 'boxare', BRUK 'nagot alderdomligt'. Huvudbetydelsen ar ratt och "
  "kan inte goras battre -- ordet betyder precis boxare. ANDRAT: synonymen "
  "var ocksa 'boxare', alltsa identisk med huvudbetydelsen, vilket gor "
  "synonymfaltet innehallslost. Utbytt mot 'knytnavskampe', som star bade i "
  "syn.se och i SO:s etymologi (latin pugil).",
  synonymer=['knytnävskämpe'])

s('välboren',
  "SO 'som har (LAG)adlig harstamning', JFR hogvalboren. ANDRAT: kortet sa "
  "bara 'av adlig slakt' och tappade darmed hela distinktionen -- valboren ar "
  "titeln for LAGRE adel, hogvalboren for hogre. Wiktionary sager samma sak: "
  "'lagre rang an greve- och friherreklasserna'. Utan det ar ordet bara en "
  "synonym till adlig.",
  huvudbetydelse='Av adlig släkt, av lägre adel')

# ---------- OFORANDRADE KORT ----------

O = {
    'en polsk riksdag':
        "INGEN ORDBOKSKALLA. Varken svenska.se, synonymer.se eller Wiktionary "
        "har frasen som uppslagsord, och svenska.se-traffarna gallde "
        "bestandsdelarna och kastades. Innehallet stammer med hur uttrycket "
        "faktiskt anvands, men det ar OBELAGT och ska inte flaggas gront. "
        "Kortet lamnas oforandrat -- att skriva om ett obelagt kort utan "
        "kalla gor det inte mer belagt.",
    'acceptans':
        "SO '(tendens till) accepterande', SAOL 'det att manga accepterar "
        "ngt'. Kortets 'att nagot godtas av manga' ar SAOL:s formulering i "
        "Adam-tal. Etymologin 'till acceptera' stammer mot SO. Ingen andring "
        "behovs.",
    'cyklisk':
        "SO ger tva betydelser: 'som regelbundet upprepas, moment for moment' "
        "och 'som bildar en sluten kurva' (JFR alifatisk, alltsa kemi). "
        "Kortet har bada, i den ordning Adam moter dem, med ratt "
        "domanmarkning pa den andra. Ingen andring.",
    'erövring':
        "SO ger tre: sjalva erovrandet, 'av. om det erovrade' (SO:s exempel "
        "'teknikens erovringar') och 'spec. om ny karlekspartner' med BRUK "
        "'ofta nedsattande'. Kortet har alla tre, med latt negativ valens pa "
        "den tredje. Ingen andring.",
    'ledstjärna':
        "SO 'grundlaggande rattesnore', SAOL 'levnadsprincip'. Kortets "
        "synonym ar SAOL:s ord rakt av och exemplet ar SO:s. Etymologin "
        "(fornsvenska ledhestiarna, ofta om Polstjarnan) stammer. Ingen "
        "andring.",
    'långrandig':
        "SO ger 'randig pa langden' forst och 'som trottar genom att ta "
        "alltfor lang tid' som bildlig andrabetydelse. Kortet vander pa "
        "ordningen, vilket ar RATT enligt regeln att kortet ska leda med den "
        "betydelse Adam faktiskt moter -- den bokstavliga ar nastan dod. Bada "
        "finns med. Ingen andring.",
    'pampusch':
        "SO '(fodrad) skaftad yttersko som anvands till skydd mot vata och "
        "kyla', SAOL 'bottin'. Kortets synonym ar SAOL:s ord, exemplet "
        "parafraserar SO:s. Etymologin (tyska Pampusche, persiska papush) "
        "stammer. Bara tva kallor (Wiktionary saknar ordet), men de tva ar "
        "eniga. Ingen andring.",
    'resorbera':
        "SO/SAOL 'suga upp', BRUK 'sarsk. i medicinska sammanhang'. Kortet "
        "har bade betydelsen, det medicinska registret och SO:s eget exempel "
        "om tarmen. Ingen andring.",
    'sovel':
        "SO 'mat forutom brod eller potatis', SAOL 'tilltugg till brod el. "
        "potatis; smorgaspalagg'. Kortets formulering tacker bada och lagger "
        "till det matiga (kott, fisk), vilket Wiktionary uttryckligen ger. "
        "Ingen andring.",
    'underförstå':
        "SO 'antyda eller forutsatta utan att klart uttrycka', SAOL 'mena "
        "utan att klart saga'. Kortet ar SAOL i Adam-tal och exemplet ar "
        "SO:s. Ingen andring.",
    'adolescens':
        "SO 'period i livet nar man overgar fran att vara barn till att vara "
        "vuxen'. Kortet ar den meningen, kortad. Psykologiregistret stods av "
        "att ordet i praktiken bara forekommer i facktext; SO:s exempel ar "
        "ett psykologiexempel. Ingen andring.",
    'assurera':
        "SO 'lata forsakra', SAOL 'forsakra mot skada'. Kortets 'teckna en "
        "forsakring for nagot' tacker bada. Etymologin (franska assurer, "
        "latin securus) stammer. Ingen andring.",
    'dissekera':
        "SO ger tva: 'skara upp och sonderdela (kropp) for anatomiskt "
        "studium' och 'noggrant analysera' (av. bildligt). Kortet har bada "
        "med ratt domanmarkning pa den forsta. Ingen andring.",
    'eldsjäl':
        "SO ger tva: 'person med brinnande entusiasm' och 'entusiastiskt "
        "sinnelag' (SO: 'nagon gang av.'). Kortet har bada, och den andra ar "
        "sallsynt nog att litterart register ar ratt. Ingen andring.",
    'en orm i paradiset':
        "INGEN ORDBOKSKALLA -- frasen saknas i alla tre. OLD-facit ger "
        "'(bibl.) ngn elr ngt som forstor en idealisk tillvaro', vilket "
        "kortet foljer. Kortet lamnas oforandrat men ar OBELAGT och ska inte "
        "flaggas gront.",
    'fission':
        "SO ger tva: 'uppdelning av foretag' och 'klyvning av atomkarna', med "
        "skilda belaggdatum (1994 resp. 1952). Kortet har bada men i omvand "
        "ordning, vilket ar ratt -- karnklyvningen ar den Adam moter, och den "
        "ar aldre i svenskan. Ingen andring.",
    'gengälda':
        "SO 'gora (nagon) en tjanst eller ge (nagon) en gava som tack for'. "
        "Kortet ar den meningen kortad. Exemplet anvander passivformen, som "
        "SO:s eget ('gengalda en gava'). Ingen andring.",
    'järv':
        "SO 'ett stort, brunsvart, kortsvansat marddjur', exempel 'jarven kan "
        "riva renar och unga algar' -- kortet anvander SO:s exempel och SO:s "
        "kannetecken. Etymologin (fornsvenska iarver) stammer. Bara tva "
        "kallor (syn.se saknar ordet). Ingen andring.",
    'kontinental':
        "SO ger tva: 'som har att gora med kontinenter' och 'utmarkande for "
        "viss typ av (attraktiv) livsstil'. Kortet har bada, med positiv "
        "valens pa den andra -- SO:s '(attraktiv)' bar den. Ingen andring.",
    'kvittens':
        "SO listar tva uppslag: betalningsbeviset och en buske med gula, "
        "paronlika frukter. DE AR HOMOGRAFER, INTE FLERBETYDELSE -- SO ger "
        "dem skilda etymologier (fornsvenska kvittancia till kvittera, resp. "
        "grekiska kydonia via lagtyska) och skilda belaggdatum (1442 resp. "
        "1578). Vaxten heter dessutom normalt 'kvitten'. Den lamnas darfor "
        "medvetet utanfor kortet; att lagga en botanisk homograf pa ett "
        "ordforstaelsekort forvirrar mer an det ger. Betalningsbetydelsen ar "
        "ratt och oforandrad.",
    'lockrop':
        "SO ger tva: djurets lockrop och boskapsskotarens. Kortet har bada, "
        "och 'ngt alderdomlig' pa den andra stods av att vallning inte langre "
        "praktiseras. Ingen andring.",
    'misstroendevotum':
        "SO 'formell deklaration av folkrepresentation att den forlorat "
        "fortroendet for regeringen', exempel 'regeringen overlevde tva "
        "misstroendevotum' -- kortet anvander SO:s exempel. Bara en kalla "
        "(saknas i syn.se och Wiktionary), men SO ar entydig. Ingen andring.",
    'oinvigd':
        "SO 'som inte har gjorts fortrogen', exempel 'facktermer som inte "
        "sager en oinvigd sa mycket' -- kortet anvander SO:s exempel. Ingen "
        "andring.",
    'pardon':
        "SO 'det att avsta fran att tillgripa de strangaste atgarderna', SAOL "
        "'forskoning, benadning' -- kortets bada synonymer ar SAOL:s tva ord. "
        "Exemplet ar SO:s. Ingen andring.",
    'pivå':
        "SO 'svangtapp', SAOL 'tapp som ngt (t.ex. ett fonster) vrider sig "
        "kring' -- kortets huvudbetydelse ar SAOL:s formulering och exemplet "
        "foljer SAOL:s fonster. Ingen andring.",
    'proviantera':
        "SO ger tva: 'skaffa proviant' (fackspraket, om fartyg) och 'gora "
        "(storre) matinkop' (av. allmannare). Kortet har bada med SO:s egna "
        "formuleringar som synonymer. Ingen andring.",
    'radiator':
        "SO 'anordning som avger (stralnings)varme', JFR varmeelement. OPPEN "
        "PUNKT: SAOL och Wiktionary ger ocksa 'kylare' (bilens), vilket "
        "kortet saknar. Lamnas utanfor eftersom SO -- primarkallan -- inte "
        "kanner betydelsen, och svenskan normalt sager 'kylare'. Noterat sa "
        "att nasta granskare ser att det ar ett val och inte ett "
        "forbiseende. Ingen andring.",
    'ratatouille':
        "SO 'en (fransk) gronsaksrora', Wiktionary specificerar tomater, "
        "squash och aggplanta -- kortets uppräkning stods darav. Etymologin "
        "stammer. Bara tva kallor (saknas i syn.se). Ingen andring.",
    'relik':
        "SO 'kvarleva av helgon eller dylikt', 'av. om foremal som forknippas "
        "med helig person'. Kortet tacker bada i en mening. Etymologin (latin "
        "reliquiae) stammer. Ingen andring.",
    'skepsis':
        "SO '(benagenhet till) tvivel eller misstro', SAOL 'tvivel, misstro' "
        "-- kortets bada synonymer ar SAOL:s tva ord, och 'hallning' fangar "
        "SO:s 'benagenhet till'. Ingen andring.",
    'stridsäpple':
        "SO 'hett diskuterad fraga', SAOL 'bildl. tvistefraga'. Kortets "
        "synonym ar SAOL:s ord och exemplet ar SO:s. Ingen andring.",
    'strosa':
        "SO 'promenera lugnt och avspant', SAOL 'strova omkring, spankulera' "
        "-- kortets bada synonymer ar SAOL:s tva ord. Exemplet foljer SO:s "
        "Gamla stan. Ingen andring.",
    'taktfull':
        "SO 'som stravar att undvika att sara eller forarga andra', JFR "
        "finkanslig -- kortets synonym ar SO:s eget JFR-ord. Exemplet "
        "parafraserar SO:s. Ingen andring.",
    'trashank':
        "SO ger tva: '(mans)person kladd i trasor' och 'mycket fattig "
        "person'. Kortet har bada. SO:s '(mans)' star inom parentes och "
        "SAOL:s 'mansperson' ar aldre praxis -- utelamnat medvetet, det "
        "begransar inte anvandningen i dag. Ingen andring.",
    'tryffel':
        "SO ger tva: svampen och chokladkonfekten, med skilda belaggdatum "
        "(1704 resp. 1955) men samma etymologi -- alltsa akta flerbetydelse. "
        "Kortet har bada. Ingen andring.",
    'vattenpuss':
        "SO/SAOL 'liten vattenpol'. Kortet ar den meningen. Ingen andring.",
}

for _o, _txt in O.items():
    s(_o, _txt)


def main():
    kort = json.load(io.open(FIL, encoding='utf-8'))
    saknas = [k['ord'] for k in kort if k['ord'] not in F]
    if saknas:
        raise SystemExit('SAKNAR sokkoll for: %s' % saknas)

    andrade = 0
    for k in kort:
        andringar, sokkoll = F[k['ord']]
        p = dict(k['legacy'])
        p.update(andringar)
        k['proposed'] = p
        k['sokkoll'] = sokkoll
        if andringar:
            andrade += 1

    json.dump(kort, io.open(FIL, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('Skrev proposed + sokkoll for %d kort. %d andrade, %d oforandrade.'
          % (len(kort), andrade, len(kort) - andrade))


main()
