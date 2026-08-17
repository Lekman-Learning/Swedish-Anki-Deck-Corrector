# -*- coding: utf-8 -*-
"""Rattar batch30 efter forgranska.py: stryker synonymer utan ordboksbelagg,
mappar register mot ordbokens markning, plockar bort 'drive' (frammande
uppslagsord i kallan -- gar tillbaka till poolen for en renare batch)."""
import json
import re
import sys

F = 'sessions/session_2026-08-17_v3-batch.json'
FG = 'fg1.txt'

# Register som motsager ordbokens markning. Regeln i forgranska.py: nagot
# ord ur markningen (>=4 bokstaver) maste finnas som stam i registret.
#   'mest historiskt'            -> kraver "histo"  -> doman 'historia'
#   'nagot nedsattande'          -> kraver "nedsa"  -> valor 'nedsättande'
#   'bibliskt'                   -> kraver "bibli"  -> doman 'bibliskt'
#   'alderdomligt utom i en fras'-> kraver "ålder"  -> 'ngt ålderdomlig'
REG = {
    "ackordera":  "ngt ålderdomlig, neutral, historia",
    "ekipage":    "ngt ålderdomlig, neutral, historia ; neutral, neutral, sport",
    "jargong":    "neutral, nedsättande, lingvistik",
    "stadfästa":  "formell, neutral, juridik ; högtidlig, neutral, bibliskt",
    "stundligen": "ngt ålderdomlig, neutral, allmän",
}

UTESLUT = {"drive"}  # frammande uppslagsord i kallan, se ATERUPPTA_batch30.md

# --- las ut vilka synonymer forgranska vill ha strukna -------------------
text = open(FG, encoding='utf-8').read()
strik = {}
ord_nu = None
for rad in text.splitlines():
    s = rad.strip()
    if re.match(r'^[A-ZÅÄÖ][A-ZÅÄÖa-zåäö\- ]*$', s) and len(s) > 1 and not s.startswith('!!'):
        ord_nu = s.lower().strip()
        continue
    if not ord_nu:
        continue
    mm = re.search(r'!! synonym_utan_(?:ordboksbelagg|stod): (.+?) --', s)
    if not mm:
        mm = re.search(r'!! synonym_utan_stod: saknar stöd i hämtad källa: (.+)$', s)
    if mm:
        for syn in mm.group(1).split(','):
            syn = syn.strip()
            if syn:
                strik.setdefault(ord_nu, set()).add(syn)

print('forgranska vill stryka synonymer pa %d ord' % len(strik))

d = json.load(open(F, encoding='utf-8'))
poster = d['poster'] if isinstance(d, dict) else d
andrade = borttagna = uteslutna = 0
for p in poster:
    w = p['ord']
    pr = p.get('proposed')
    if not pr:
        continue
    if w in UTESLUT:
        p['proposed'] = None
        p['approved'] = False
        uteslutna += 1
        print('  UTESLUTEN ur batchen:', w)
        continue
    if w in strik:
        fore = list(pr['synonymer'])
        pr['synonymer'] = [s for s in fore if s not in strik[w]]
        n = len(fore) - len(pr['synonymer'])
        if n:
            borttagna += n
            print('  %-14s strok %d: %s -> %s' % (w, n, fore, pr['synonymer']))
    if w in REG:
        pr['register'] = REG[w]
        andrade += 1
        print('  %-14s register -> %s' % (w, REG[w]))

json.dump(d, open(F, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
kvar = sum(1 for p in poster if p.get('proposed'))
print('\nstrok %d synonymer, andrade %d register, uteslot %d kort' % (borttagna, andrade, uteslutna))
print('kort kvar med proposed: %d' % kvar)
