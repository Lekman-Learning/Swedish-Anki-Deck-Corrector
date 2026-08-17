# -*- coding: utf-8 -*-
"""Fyller sokkoll (kalla + slutsats) for batch30 ur uppslag/*.json."""
import json
import os

F = 'sessions/session_2026-08-17_v3-batch.json'

SLUTSATS = {
"autopsi": "SO ger TVA betydelser med 'iakttagelse som man gjort med egna ögon' FORST och 'obduktion' som andra, markt mindre brukligt. SAOL likadant: 'iakttagelse med egna ögon, självsyn; obduktion'. Kortet hade bara obduktionsbetydelsen, alltsa ordbokens andra och minst brukliga -- huvudbetydelsen saknades helt.",
"cellulosa": "SO: 'ett organiskt ämne med mycket långa molekylkedjor, som utgör stödsubstans i växternas cellväggar', med underbetydelse 'äv. om kemiskt framställd pappersmassa'. SAOL: 'en stödsubstans i växtcellväggar; kemisk pappersmassa'. Bada betydelserna med.",
"kategorisera": "SO: 'dela in i kategorier' plus underbetydelse 'äv. försvagat' = 'beskriva, karakterisera'. SAOL saknar egen definition. Exempel i SO: 'NN kan kategoriseras som gammalkonservativ'.",
"konservator": "SO: '(titel för) person som har till yrke att vårda och återställa konst- och utställningsföremål', med sarskild underbetydelse om den som stoppar upp doda djur for museum. SAOL: 'person som restaurerar konst- och museiföremål el. preparerar djur och växter'.",
"lagra": "SO ger fyra betydelser: 'samla i förråd', 'lägga i skikt på skikt', 'förse med lager', 'samla sig i skikt'. SAOL: 'placera i förråd ibl. för förädling; lägga i skikt'. Kortet tacker de tva huvudleden.",
"origo": "SO: 'skärningspunkten mellan koordinataxlarna i koordinatsystem'. SAOL: 'skärningspunkten mellan axlarna i koordinatsystem'. Entydigt matematiskt, ingen bibetydelse i ordbockerna.",
"probat": "Finns inte i SO. SAOL har det: 'beprövad och därvid befunnen god', markt ald. Synonymer.se ger 'tillförlitlig'. Ordet ar alltsa belagt i SAOL trots att SO saknar uppslagsordet.",
"stursk": "SO: 'trotsig och fräck'. SAOL: 'trotsig, uppstudsig; högfärdig'. Exempel i SO: 'bestraffningen gjorde honom bara mer stursk'.",
"symbios": "SO: 'samliv mellan organismer av olika slag', med underbetydelser 'äv. bildligt om två personers el. gruppers uppgående i varandra' och om kulturyttringar. SAOL: 'samlevnad till ömsesidig nytta mellan två artskilda organismer; äv. bildl.'. Bildliga betydelsen med.",
"undfly": "SO: 'fly undan för', med 'äv. bildligt'. SAOL: 'undvika'. Exempel i SO: 'han lyckades undfly poliserna / försöka undfly sitt straff'.",
"flärd": "SO: 'ytlig prakt', med underbetydelse 'äv. om njutningsfyllt (och klandervärt) levnadssätt'. SAOL: 'ytlig prakt; fåfänga'.",
"fotocell": "SO: 'anordning där en elektrisk spänning uppstår när den träffas av ljus'. SAOL: 'anordning som utnyttjar fotoelektricitet'. Ingen bibetydelse.",
"inpyrd": "SO: 'helt genomträngd', med 'äv. bildligt'. SAOL ger exemplet 'lokalen var inpyrd av rök'. SO:s bildliga exempel: 'boken var inpyrd med föråldrade könsschabloner'.",
"ackordera": "SO ger flera led: '(försöka) träffa ekonomisk överenskommelse', 'överlämna mot ekonomisk gottgörelse', 'lämna (barn) i någons vård', 'underhandla, köpslå' -- markt mest historiskt. SAOL: 'göra upp; underhandla, köpslå'.",
"dekorum": "SO: 'värdigt och passande uppförande', markt nagot hogtidligt. SAOL: 'anständighet, det passande'. Bada ger exemplet 'iaktta dekorum'.",
"desertör": "SO: 'person som deserterat'. SAOL hanvisar till desertera. Exempel i SO: 'alla desertörer riskerar dödsstraff'.",
"ekipage": "SO: 'typ av finare åkdon med dragare', markt mest historiskt, med flera underbetydelser -- numera om fordon eller hast med forare i tavlingssammanhang, aven hundspann. SAOL: 'finare åkdon med dragare och betjäning (i äldre tid); häst med ryttare; grupp jakthundar med förare'.",
"förlikas": "SO: 'träffa överenskommelse i godo' samt 'förmå att träffa överenskommelse i godo'. SAOL: 'förlika sig'. Exempel i SO: 'parterna kunde inte förlikas och strejk utbröt'.",
"inkrustera": "SO: 'förse med inkrustationer'. SAOL ger den klarare formuleringen 'förse med inläggningar'. Exempel: 'en mässingsask inkrusterad med silvertrådar'.",
"intim": "SO ger sju betydelser/underbetydelser: 'som rör det privata eller innersta', 'som har att göra med underlivet', 'mycket nära', plus underbetydelser om relationer och miljo. SAOL: 'privat; nära; som rör underlivet'.",
"jargong": "SO: 'språkform med en speciell stil och (ofta) med specialuttryck som används i viss grupp' samt 'slentrianmässigt uttryckssätt', markt nagot nedsattande. SAOL: 'språk typiskt för en yrkesgrupp; stereotypt uttryckssätt'.",
"kännare": "SO: 'person som har gedigna kunskaper'. SAOL: 'särsk. expert, specialist'. Exempel i SO: 'hon granskade innehållet med en kännares blick'.",
"pekoral": "SO: '(litterär) text som är oavsiktligt komisk genom att dess utformning inte passar ihop med ämnet eller syftet'. SAOL: 'text som är oavsiktligt komisk t.ex. genom att stil och ämne inte harmonierar'.",
"refusera": "SO: 'vägra att anta till publicering'. SAOL vidgar: 'vägra att publicera, uppföra el. ställa ut; avvisa, förkasta'. Exempel i SO: 'det första förlaget refuserade manuset'.",
"slingerbult": "SO: 'undanflykt eller försök till bortförklaring', med 'någon gång äv. om motsvarande person'. SAOL: 'slingring, kringelkrok; undanflykt'.",
"stadfästa": "SO: 'formellt fastlägga' samt en andra betydelse 'styrka', markt bibliskt. SAOL: 'fastställa; styrka'. Exempel i SO: 'stadfästa en dom' respektive 'stadfästa någon i tron'.",
"stundligen": "SO: 'ständigt', markt alderdomligt utom i en fras. SAOL ger bara exemplet 'dagligen och stundligen'. SO:s exempel: 'problem som man dagligen och stundligen stöter på'.",
}

d = json.load(open(F, encoding='utf-8'))
poster = d['poster'] if isinstance(d, dict) else d
n = saknas = 0
for p in poster:
    w = p['ord']
    if not p.get('proposed'):
        continue
    up = os.path.join('uppslag', w + '.json')
    if not os.path.exists(up):
        print('  SAKNAR uppslag:', w)
        saknas += 1
        continue
    u = json.load(open(up, encoding='utf-8'))
    kalla = (u.get('urler') or {}).get('svenska.se')
    if not kalla:
        print('  SAKNAR kalla:', w)
        saknas += 1
        continue
    p['sokkoll'] = {"kalla": kalla, "slutsats": SLUTSATS[w]}
    n += 1

json.dump(d, open(F, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('fyllde sokkoll pa %d kort (%d saknade)' % (n, saknas))
