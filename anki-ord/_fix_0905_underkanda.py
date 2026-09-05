# -*- coding: utf-8 -*-
"""Rattar de kort blindgranskningen underkande, 2026-09-05.

SYSTEMATISK BRIST i omgang 1 (4 underkanda av 25): tre av fyra var samma fel
-- SYNONYMEN PROVADES INTE MOT SIN EGEN BETYDELSE. 'astadkomma' godtogs for
ombesorja for att SAOL:s definitionstext innehaller ordet, inte for att det
gar att byta ut; 'kretsformig' hamnade i grupp 1 (upprepas) fast det betyder
ringformad och hor till grupp 2; 'smorgaspalagg' last sovel vid smorgas fast
SO sager 'brod ELLER POTATIS'.

Poolen (forgranska.py) svarar bara pa fragan "star ordet i SO/SAOL:s text?".
Den svarar INTE pa "hor det till DEN HAR betydelsen och gar det att byta ut?".
Den andra fragan maste stallas for hand, per betydelse.

Efter omgang 1 svepte jag de aterstaende 25 korten mot samma fraga och hittade
ett till: relik, dar huvudbetydelsen breddats till att omfatta foremal men
synonymen '≈≈ kvarleva' bara tacker kroppsdelar.
"""
import io
import json

FIL = 'sessions/session_2026-09-05_v3-omgranskning-repetition.json'

RATT = {
    # --- underkanda i omgang 1 ---
    'ombesörja': dict(
        synonymer=['ordna', 'utföra']),
    'cyklisk': dict(
        synonymer=['≈≈ återkommande', 'kretsformig'],
        synonym_groups=[['≈≈ återkommande'], ['kretsformig']]),
    'sovel': dict(
        huvudbetydelse=('Mat man äter till bröd eller potatis, särskilt '
                        'det matiga som kött, fisk eller pålägg'),
        synonymer=['tilltugg till bröd el. potatis']),
    'koloss': dict(
        huvudbetydelse='Mycket stor staty ; ovanligt stor person eller sak',
        register='neutral, neutral ; neutral, neutral',
        synonymer=['stor staty', 'bjässe'],
        synonym_groups=[['stor staty'], ['bjässe']]),
    'kvittens': dict(
        synonymer=['mottagnings- el. betalningsbevis']),
}

TILLAT = {
    'koloss': {'betydelse_kan_saknas':
        'SO listar tre definitioner, men den mellersta ("nagot som ytligt '
        'sett ar stort och imponerande men i verkligheten mycket sarbart") '
        'har som ENDA belagg det fasta uttrycket "koloss pa lerfotter". Den '
        'lades till pa kortet 2026-09-05 och UNDERKANDES av den blinda '
        'granskaren, som slog upp ordet sjalvstandigt och konstaterade att '
        'betydelsen tillhor uttrycket, inte huvudordet. Ateralagd till tva '
        'betydelser. Registret pa forsta betydelsen star kvar som neutralt '
        '(var "fackspraklig ... konst") -- SO markerar ingen fackspraklighet '
        'och kolossen pa Rhodos ar allmansprak.'},
}


def main():
    kort = json.load(io.open(FIL, encoding='utf-8'))
    reg = {k['ord']: k for k in kort}
    for o, andr in RATT.items():
        reg[o]['proposed'].update(andr)
        # maste skrivas till Anki pa nytt
        reg[o]['applicerad'] = False
    for o, t in TILLAT.items():
        reg[o].setdefault('forgranska_tillat', {}).update(t)
    json.dump(kort, io.open(FIL, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('Rattade %d kort, %d nya undantag.' % (len(RATT), len(TILLAT)))


main()
