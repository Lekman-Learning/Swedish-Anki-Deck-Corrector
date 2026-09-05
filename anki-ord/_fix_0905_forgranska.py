# -*- coding: utf-8 -*-
"""Rattar de 21 harda forgranskningsanmarkningarna INNAN blindgranskningen.

Lardomen som styr filen (kostade en underkand omgang 2026-09-02): synonymer
far bara komma ur den pool forgranska.py sjalv godtar -- SO:s SYN-falt och
SO/SAOL:s definitionstext. synonymer.se raknas INTE. Fem av dagens andringar
hamtade synonymer darifran och maste backas.
"""
import io
import json

FIL = 'sessions/session_2026-09-05_v3-omgranskning-repetition.json'

# ord -> falt att skriva om i proposed
SYN = {
    # syn.se-synonymer backade till poolgodkanda (se docstring)
    'betsel': ['styrmedel för häst'],
    'högoddsare': ['osannolik vinnare av tävling'],
    'kronometer': ['≈≈ ur'],
    'rayon': ['≈≈ textilfiber'],
    'pugilist': ['boxare'],
    # idiom utan uppslagsord: tom synonymrad ar det ratta svaret
    'dra på munnen': [],
    'en orm i paradiset': [],
}

HB = {
    'relik': ('Kvarleva av ett helgon, eller föremål som hört till '
              'någon helig, bevarat och vördat'),
}

# ord -> {regel: motivering}
TILLAT = {
    'dra på munnen': {'uppslagsord_saknas':
        'Idiom. Frasen finns inte som uppslagsord i SO/SAOL -- bara '
        'bestandsdelarna dra och mun, som inte bar betydelsen. Kortet vilar '
        'pa synonymer.se och Wiktionary, och synonymraden ar darfor tom, '
        'vilket style_guide anger som ratt svar for idiom.'},
    'en polsk riksdag': {'uppslagsord_saknas':
        'Idiom. Saknas i alla tre kallorna. Kortet ar OBELAGT och far inte '
        'flaggas gront -- noterat i sokkoll. Behalls oforandrat eftersom en '
        'omskrivning utan kalla inte gor det mer belagt.'},
    'en orm i paradiset': {'uppslagsord_saknas':
        'Bibliskt idiom. Saknas i alla tre kallorna; enda stodet ar '
        'OLD-facit. Synonymraden tomd (idiomregeln) och kortet flaggas som '
        'obelagt i sokkoll.'},

    # --- betydelse_kan_saknas: raknaren inkluderar SO:s underbetydelser ---
    'långrandig': {'betydelse_kan_saknas':
        'SO har 2 definitioner och kortet har bada. De tva ovriga posterna ar '
        'underbetydelser ("ofta bildligt, spec." och "spec. av. om person") '
        'som modifierar definitionerna, inte nya betydelser.'},
    'dissekera': {'betydelse_kan_saknas':
        'SO har 2 definitioner och kortet har bada. Den tredje posten ar '
        'underbetydelsen "av. bildligt" till definition 2, alltsa den '
        'bildliga anvandningen av "noggrant analysera" -- samma betydelse.'},
    'kvittens': {'betydelse_kan_saknas':
        'SO:s andra uppslag (busken med paronlika frukter) ar en HOMOGRAF, '
        'inte en andra betydelse: skild etymologi (grekiska kydonia via '
        'lagtyska, mot fornsvenska kvittancia till kvittera) och skilt '
        'belagg (1578 mot 1442). Vaxten heter dessutom normalt kvitten. Att '
        'lagga en botanisk homograf pa ett ordforstaelsekort forvirrar mer '
        'an det ger.'},
    'lockrop': {'betydelse_kan_saknas':
        'SO har 2 definitioner och kortet har bada. Den tredje posten ar '
        'underbetydelsen "av. bildligt" (gatuforsaljarnas lockrop) -- samma '
        'handling, mansklig i stallet for djurisk, och tacks av kortets '
        'andra betydelse.'},
    'misstroendevotum': {'betydelse_kan_saknas':
        'En definition plus underbetydelsen "av. om liknande atgard av annat '
        'beslutande organ". Det ar samma procedur tillampad i en styrelse i '
        'stallet for i riksdagen, inte en annan betydelse.'},
    'pardon': {'betydelse_kan_saknas':
        'En definition plus underbetydelsen "ofta forsvagat el. skamtsamt", '
        'som ar en REGISTERanmarkning och inte en betydelse.'},
    'proviantera': {'betydelse_kan_saknas':
        'SO har 2 definitioner och kortet har bada. De tva ovriga ar '
        'underbetydelser om konstruktion ("i facksprak ibland i konstruktion '
        'med objekt") och rackvidd ("av. allmannare").'},
    'relik': {'betydelse_kan_saknas':
        'En definition plus underbetydelsen "av. om foremal som forknippas '
        'med helig person". Den luckan var akta -- kortet talade bara om '
        'kvarlevor och missade foremalen (SO:s eget exempel: en traflisa av '
        'det heliga korset). Huvudbetydelsen ar darfor UTVIDGAD att tacka '
        'bada, i en och samma betydelse, eftersom SO sjalv hanterar dem sa.'},
    'taktfull': {'betydelse_kan_saknas':
        'En definition plus underbetydelsen "av. om handling eller dylikt". '
        'Kortets formulering ("som ar noga med att inte sara andra") gäller '
        'bade personen och handlingen.'},
    'tryffel': {'betydelse_kan_saknas':
        'SO har 2 definitioner (svampen och chokladen) och kortet har bada. '
        'Den tredje posten ar underbetydelsen "spec. av. som krydda" till '
        'svampbetydelsen.'},
}


def main():
    kort = json.load(io.open(FIL, encoding='utf-8'))
    reg = {k['ord']: k for k in kort}

    for o, syn in SYN.items():
        p = reg[o]['proposed']
        p['synonymer'] = syn
        p['synonym_groups'] = None
    for o, hb in HB.items():
        reg[o]['proposed']['huvudbetydelse'] = hb
    for o, t in TILLAT.items():
        reg[o]['forgranska_tillat'] = t

    json.dump(kort, io.open(FIL, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('Rattade %d synonymrader, %d huvudbetydelser, %d undantag.'
          % (len(SYN), len(HB), len(TILLAT)))


main()
