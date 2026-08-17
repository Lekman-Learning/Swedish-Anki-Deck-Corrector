# -*- coding: utf-8 -*-
"""Skriver proposed for de 28 aktiva korten i batch30 (ordig/reglementarisk pausade)."""
import json

F = 'sessions/session_2026-08-17_v3-batch.json'


def m(w, txt):
    return txt.replace('@', '<font color="#3498db">%s</font>' % w)


K = {
"autopsi": ("Iakttagelse man gjort med egna ogon, sjalvsyn; av. (mindre brukligt) obduktion".replace('sjalvsyn', 'självsyn').replace('ogon', 'ögon').replace('av.', 'äv.'),
 ["självsyn", "obduktion"],
 "Domstolen nöjde sig inte med vittnesmål utan krävde @ på olycksplatsen.",
 "ngt ålderdomlig, neutral, allmän",
 "av grekiska autopsía 'självsyn', av autós 'själv' och ópsis 'syn'"),

"cellulosa": ("Organiskt ämne med mycket långa molekylkedjor som bygger upp växternas cellväggar; äv. om kemiskt framställd pappersmassa",
 ["växttråd", "cellämne", "trämassa"],
 "Bomullsfibern består till största delen av nästan ren @.",
 "fackspråklig, neutral, kemi",
 "till latinets cellula 'liten cell'"),

"drive": ("Särskilt insatt, ökad verksamhet; kampanj eller satsning. Äv. långt svepande slag i golf eller tennis",
 ["kampanj", "satsning", "framstöt"],
 "Föreningen gjorde en @ för att värva nya medlemmar före årsskiftet.",
 "neutral, neutral, allmän",
 "av engelska drive 'kraft, kampanj'"),

"kategorisera": ("Dela in i kategorier; äv. försvagat beskriva eller karakterisera någon",
 ["klassificera", "sortera", "gruppera"],
 "Bibliotekarien började @ de nyinkomna böckerna efter ämnesområde.",
 "neutral, neutral, allmän",
 "till kategori, av grekiska katēgoría 'utsaga, klass'"),

"konservator": ("Person som yrkesmässigt vårdar och återställer konst- och museiföremål; särskilt äv. person som stoppar upp döda djur",
 ["restaurator", "djuruppstoppare", "preparator"],
 "En @ arbetade i flera månader med att rädda den spruckna altartavlan.",
 "neutral, neutral, konst",
 "av latinets conservator 'bevarare', till conservare 'bevara'"),

"lagra": ("Samla i förråd för framtida bruk; äv. lägga eller samla sig i skikt på skikt",
 ["magasinera", "förvara", "avsätta i skikt"],
 "Bönderna vill @ spannmålet över vintern för att få bättre betalt.",
 "neutral, neutral, allmän",
 "till lager, av lågtyska lager 'läger, förråd'"),

"origo": ("Skärningspunkten mellan koordinataxlarna i ett koordinatsystem",
 ["nollpunkt", "skärningspunkt"],
 "Kurvan passerar rakt genom @ och fortsätter upp i första kvadranten.",
 "fackspråklig, neutral, matematik",
 "av latinets origo 'ursprung, början'"),

"probat": ("Beprövad och därvid befunnen god",
 ["beprövad", "tillförlitlig"],
 "Att sova på saken är ett @ medel mot förhastade beslut.",
 "ngt ålderdomlig, neutral, allmän",
 "av latinets probatus 'prövad, godkänd'"),

"stursk": ("Trotsig och fräck; uppstudsig",
 ["uppstudsig", "näsvis", "trotsig"],
 "Pojken svarade så @ att hela klassrummet tystnade.",
 "neutral, negativ, allmän",
 "av lågtyska sturs 'högfärdig, styv'"),

"symbios": ("Samliv mellan organismer av olika slag, ofta till ömsesidig nytta; äv. bildligt om två personers eller gruppers uppgående i varandra",
 ["samlevnad", "samliv", "samexistens"],
 "Efter trettio år tillsammans levde paret i en nästan total @.",
 "fackspråklig, neutral, biologi",
 "av grekiska symbíōsis 'samliv', av syn- 'med' och bíos 'liv'"),

"undfly": ("Fly undan för och lyckas komma undan; äv. bildligt om ansvar eller straff",
 ["undkomma", "undvika", "sky"],
 "Ingen kan i längden @ följderna av sina egna beslut.",
 "litterär, neutral, allmän",
 "till und- 'undan' och fly"),

"flärd": ("Ytlig prakt; äv. om njutningsfyllt och klandervart levnadssätt".replace('klandervart', 'klandervärt'),
 ["ytlighet", "fåfänga", "prål"],
 "Hon vände ryggen åt storstadens @ och flyttade ut till kusten.",
 "litterär, negativ, allmän",
 "fornsvenska flærþ 'svek, fåfänglighet'"),

"fotocell": ("Anordning där en elektrisk spänning uppstår när den träffas av ljus",
 ["ljuscell", "ljussensor"],
 "Tidtagningen i loppet sköttes av en @ strax bakom mållinjen.",
 "fackspråklig, neutral, teknik",
 "till foto- 'ljus' och cell"),

"inpyrd": ("Helt genomträngd av något, särskilt lukt eller rök; äv. bildligt",
 ["genomdränkt", "indränkt", "ovädrad"],
 "Jackan var @ av gammal grillrök och gick inte att vädra ren.",
 "neutral, lätt negativ, allmän",
 "till in- och pyra 'ryka, glöda'"),

"ackordera": ("Försöka träffa en ekonomisk överenskommelse; underhandla och köpslå",
 ["köpslå", "underhandla", "pruta"],
 "Handlarna brukade @ länge innan de till slut skakade hand.",
 "ngt ålderdomlig, neutral, ekonomi",
 "av franska accorder 'komma överens', till latinets accordare"),

"dekorum": ("Värdigt och passande uppförande; det som anständigheten kräver",
 ["anständighet", "etikett", "god ton"],
 "Trots grälet lyckades båda parter bevara @ inför gästerna.",
 "högtidlig, neutral, allmän",
 "av latinets decorum 'det passande', till decere 'anstå, passa'"),

"desertör": ("Person som olovligen har lämnat sin militärtjänst",
 ["rymling", "fanflykting", "överlöpare"],
 "En @ greps vid gränsen och fördes tillbaka till sitt förband.",
 "neutral, negativ, militär",
 "av franska déserteur, till latinets deserere 'överge'"),

"ekipage": ("Finare åkdon med dragare och betjäning; numera äv. om häst och ryttare eller fordon med förare, särskilt i tävlingssammanhang",
 ["åkdon", "häst och vagn", "häst med ryttare"],
 "Det svenska @ red felfritt genom banan och tog hem segern.",
 "neutral, neutral, sport",
 "av franska équipage 'utrustning', till équiper 'utrusta'"),

"förlikas": ("Träffa överenskommelse i godo och därmed undvika strid eller rättegång",
 ["försonas", "enas", "ingå förlikning"],
 "Efter tre år i domstol valde bolagen att @ utanför rättssalen.",
 "formell, neutral, juridik",
 "till förlika, av lågtyska vorliken 'jämka samman'"),

"inkrustera": ("Förse med inläggningar av annat material",
 ["förse med inläggningar", "infatta"],
 "Hantverkaren @ bordsskivan med små bitar av pärlemor.",
 "fackspråklig, neutral, konst",
 "av latinets incrustare 'överdra med skorpa', till crusta 'skorpa'"),

"intim": ("Som rör det privata eller innersta; mycket nära och förtrolig. Äv. som har att göra med underlivet",
 ["förtrolig", "privat", "innerlig"],
 "Samtalet blev betydligt mer @ än hon hade tänkt sig från början.",
 "neutral, neutral, allmän",
 "av latinets intimus 'innerst', superlativ till inter 'inom'"),

"jargong": ("Språkform med särskild stil och egna uttryck som används inom en viss grupp; äv. slentrianmässigt uttryckssätt",
 ["gruppspråk", "yrkesspråk", "facksnack"],
 "Det tog honom ett halvår att lära sig @ på verkstaden.",
 "neutral, lätt negativ, lingvistik",
 "av franska jargon 'obegripligt tal, fågelkvitter'"),

"kännare": ("Person som har gedigna kunskaper inom ett område och kan bedöma det säkert",
 ["expert", "specialist", "konnässör"],
 "Han smakade på vinet med en @ lugna säkerhet.",
 "neutral, positiv, allmän",
 "till känna i betydelsen 'ha kunskap om'"),

"pekoral": ("Text som blir oavsiktligt komisk genom att stil och ämne inte passar ihop",
 ["löjeväckande text", "dravel", "smörja"],
 "Hyllningsdikten till chefen blev ett rent @.",
 "neutral, nedsättande, litteraturvetenskap",
 "trol. till latinets pecus 'boskap'"),

"refusera": ("Vägra att anta till publicering, uppförande eller utställning",
 ["avvisa", "förkasta", "avslå"],
 "Förlaget @ hennes debutroman utan någon närmare motivering.",
 "formell, neutral, litteraturvetenskap",
 "av franska refuser 'vägra', till latinets refutare"),

"slingerbult": ("Undanflykt eller försök till bortförklaring; någon gång äv. om person som beter sig så",
 ["undanflykt", "krumbukt", "kringelkrok"],
 "Varje gång jag frågar om pengarna kommer det nya @.",
 "vardaglig, negativ, allmän",
 "till slingra och bult"),

"stadfästa": ("Formellt fastlägga och ge laga kraft; äv. bibliskt styrka eller befästa",
 ["fastställa", "lagfästa", "sanktionera"],
 "Hovrätten valde att @ den dom som tingsrätten hade meddelat.",
 "formell, neutral, juridik",
 "till stad 'fast punkt' och fästa"),

"stundligen": ("Ständigt, i varje stund — numera nästan bara i frasen dagligen och stundligen",
 ["ständigt", "jämt", "städse"],
 "Hon påmindes dagligen och @ om vad hon en gång hade lovat.",
 "arkaisk, neutral, allmän",
 "till stund, med adverbändelsen -ligen"),
}

d = json.load(open(F, encoding='utf-8'))
poster = d['poster'] if isinstance(d, dict) else d
n = 0
for p in poster:
    w = p['ord']
    if w not in K:
        print('  hoppar (pausad):', w)
        continue
    hb, syn, ex, reg, ety = K[w]
    p['proposed'] = {
        "huvudbetydelse": hb,
        "synonymer": syn,
        "synonym_groups": None,
        "exempelmening": m(w, ex),
        "register": reg,
        "etymologi": ety,
    }
    p['approved'] = True
    n += 1

json.dump(d, open(F, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('skrev proposed pa %d kort -> %s' % (n, F))
