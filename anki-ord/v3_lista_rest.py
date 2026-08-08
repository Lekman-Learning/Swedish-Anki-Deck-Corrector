# -*- coding: utf-8 -*-
import re
from ankiconnect import invoke
import config
D = f'deck:"{config.DECK_NAME}"'
def strip(h):
    h = re.sub(r'<br\s*/?>', ' ~ ', h)
    h = re.sub(r'<[^>]+>', '', h).replace('&nbsp;', ' ')
    return re.sub(r'\s+', ' ', h).strip()
nids = invoke('findNotes', query=f'{D} prop:due=0 flag:3')
info = invoke('notesInfo', notes=nids)
for i, x in enumerate(info, 1):
    f = strip(x['fields']['Framsida']['value'])
    b = strip(x['fields']['Baksida']['value'])
    o = invoke('findNotes', query=f'deck:"Humanities::Languages::Svenska OLD" "Framsida:{f}"')
    fac = 'INGET FACIT'
    if o:
        fac = strip(invoke('notesInfo', notes=[o[0]])[0]['fields']['Baksida']['value'])[:90]
    print(f'{i}. {f} :: {b}')
    print(f'    FACIT: {fac}')
