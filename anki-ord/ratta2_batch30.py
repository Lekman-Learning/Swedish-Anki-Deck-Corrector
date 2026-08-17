# -*- coding: utf-8 -*-
"""Runda 2: rattar (a) bojningsfel i exempelmeningar -- min @-substitution
stoppade in uppslagsformen dar meningen kraver bojd form -- och (b) de sju
kort blindgranskningen underkande."""
import json

F = 'sessions/session_2026-08-17_v3-batch.json'
C = '<font color="#3498db">%s</font>'

# (a) bojningsfel. Hela meningen skrivs om med ratt form inne i fargtaggen.
EX = {
"ekipage":     "Det svenska " + (C % "ekipaget") + " red felfritt genom banan och tog hem segern.",
"inkrustera":  "Hantverkaren " + (C % "inkrusterade") + " bordsskivan med små bitar av pärlemor.",
"intim":       "Samtalet blev betydligt mer " + (C % "intimt") + " än hon hade tänkt sig från början.",
"jargong":     "Det tog honom ett halvår att lära sig " + (C % "jargongen") + " på verkstaden.",
"kännare":     "Han smakade på vinet med en " + (C % "kännares") + " lugna säkerhet.",
"refusera":    "Förlaget " + (C % "refuserade") + " hennes debutroman utan någon närmare motivering.",
"slingerbult": "Varje gång jag frågar om pengarna kommer det nya " + (C % "slingerbultar") + ".",
}

# (b) de sju underkanda. Betydelser kompletterade / obelagda synonymer strukna.
HB = {
"lagra":   "Samla i förråd för framtida bruk ; lägga eller samla sig i skikt på skikt ; förse (hjulaxel eller dylikt) med lager",
"symbios": "Samliv mellan organismer av olika slag, ofta till ömsesidig nytta ; äv. bildligt om två personers eller gruppers uppgående i varandra ; ibland äv. om olika kulturyttringars ömsesidiga befruktning av varandra",
"intim":   "Som rör det privata eller innersta ; mycket nära och förtrolig ; äv. som har att göra med underlivet ; äv. om miljö som skapar förutsättningar för gemenskapskänslor",
# blindgranskaren ansag tillagget obelagt trots att SO har underbetydelsen
# "någon gång äv. om motsvarande person". Kortet forenklas till huvudledet.
"slingerbult": "Undanflykt eller försök till bortförklaring",
}

SYN = {
"origo": [],   # 'skärningspunkt' ar bredare an origo, SO ger ingen synonym
"flärd": [],   # 'fåfänga' ej bekraftad som synonym av SO
}

d = json.load(open(F, encoding='utf-8'))
poster = d['poster'] if isinstance(d, dict) else d
a = b = 0
for p in poster:
    w = p['ord']
    pr = p.get('proposed')
    if not pr:
        continue
    if w in EX:
        pr['exempelmening'] = EX[w]
        a += 1
        print('  BOJNING  %s' % w)
    if w in HB:
        pr['huvudbetydelse'] = HB[w]
        b += 1
        print('  BETYDELSE %s' % w)
    if w in SYN:
        pr['synonymer'] = SYN[w]
        b += 1
        print('  SYNONYM  %s -> []' % w)

json.dump(d, open(F, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\nrattade %d bojningsfel och %d innehallsanmarkningar' % (a, b))
