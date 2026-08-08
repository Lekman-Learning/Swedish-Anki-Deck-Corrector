# -*- coding: utf-8 -*-
"""v3-omskrivning: gå upp i limningen.

Fel före: betydelsen låst vid ilska ("Bli så arg att man tappar kontrollen"),
trots att uttrycket i grunden betyder att tappa fattningen -- bilden kommer
från möbler som lossnar i limfogarna, och det gäller sammanbrott under press
lika mycket som vrede. Facit i OLD ("ilskna till") är lika smalt och hjälpte
alltså inte. Dessutom cirkulärt: "tappar kontrollen" i definitionen och
"tappa kontrollen" som synonym.

Efter: definitionen bär den breda betydelsen, synonymerna spänner båda polerna
-- ilska (ilskna till, explodera) och sammanbrott (bryta ihop). Exemplet
behålls: det är konkret och vardagligt, alltså bra Adam-tal.
"""
import apply_flerbetydelse as af
from ankiconnect import invoke
import config

B = '<font color="#3498db">%s</font>'
ORD = "gå upp i limningen"

nids = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" "Framsida:{ORD}"')
anm = af.apply_card(
    nids[0],
    huvudbetydelse="Tappa kontrollen helt, oftast av ilska",
    synonymer=["ilskna till", "explodera", "bryta ihop"],
    exempelmening=f"Han {B % 'gick upp i limningen'} när bilen gick sönder igen.",
    register="vardaglig",
    mode="sokkoll",
    escalated=True,
    ord_=ORD,
)
print("anmarkningar:", anm if anm else "inga")

cids = invoke("findCards", query=f'deck:"{config.DECK_NAME}" "Framsida:{ORD}"')
ci = invoke("cardsInfo", cards=cids)
print("flagga efter:", [c["flags"] for c in ci])
n = invoke("notesInfo", notes=nids)[0]
print("taggar efter:", ", ".join(n["tags"]))
