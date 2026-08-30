# -*- coding: utf-8 -*-
"""Ratter de avdiakritiserade raderna som aao_koll.py belagt.

Adam 2026-08-30: "kan du borja skriva korrekt med aao overallt?"

METOD. Exakt strangbyte i den RAA HTML:en, inte parse->build. Rundturen
skrev om ett kort (`agnat`) pa ett satt jag inte kunde reproducera tidigare
i dag; ett strangbyte som verifieras trafffa exakt en gang kan inte gora
det. Varje par kontrolleras: hittas gamla strangen inte, eller flera
ganger, avbryts HELA korningen utan att nagot skrivits.

OMFATTNING. Bara rader dar en avdiakritiserad SVENSK glosa ar belagd.
Latinska, grekiska och fornsvenska FORMER lamnas ororda -- `sokn`,
`fortappad`, `kvaþe`, `stinder` ar riktiga fornsvenska stavningar, inte
mina stavfel.
"""
import io
import json
import sys

import config
from ankiconnect import invoke

# (uppslagsord, gammal strang, ny strang)
BYTEN = [
 ("alltjämt", "'standigt'", "'ständigt'"),
 ("promulgera", "'ansla, kungora'", "'anslå, kungöra'"),
 ("ratificera", "'slutgiltigt faststalla'", "'slutgiltigt fastställa'"),
 ("cyklop", "ops 'oga'", "ops 'öga'"),
 ("in natura", "'i naturligt tillstand'", "'i naturligt tillstånd'"),
 ("rauk", "Gotlandsk dialekt rauk; samma rot som rok.",
  "Gotländsk dialekt rauk; samma rot som rök."),
 ("laminat", "'metallskiva, brada'", "'metallskiva, bräda'"),
 ("socken", "bildat till soka -- omradet vars folk sokte sig",
  "bildat till söka — området vars folk sökte sig"),
 ("kollationera", "'sammanstalla, jamfora'", "'sammanställa, jämföra'"),
 ("celebrera", "'talrikt besoka; fira'", "'talrikt besöka; fira'"),
 ("absolutism", "'obegransad, oinskrankt'", "'obegränsad, oinskränkt'"),
 ("förtappad", "till fortappa 'forlora, forspilla'",
  "till fortappa 'förlora, förspilla'"),
 ("stinn", "'hard, spand'", "'hård, spänd'"),
 ("motspänstig", "till spanna.", "till spänna."),
 ("kväde", "till kvada 'kvada, sjunga'", "till kväda 'kväda, sjunga'"),
 ("distorsion", "'vridning isar'", "'vridning isär'"),
 ("allenarådande", "+ radande;", "+ rådande;"),
 ("implodera", "in 'inat' som forled", "in 'inåt' som förled"),
 ("subtil", "'fin, harfin, skarpsinnig'", "'fin, hårfin, skarpsinnig'"),
 ("koloratur", "colorare 'farga' -- sangen 'fargas'",
  "colorare 'färga' — sången 'färgas'"),
 ("epitet", "'tillagg'", "'tillägg'"),
 ("alias", "'vid annat tillfalle'", "'vid annat tillfälle'"),
 ("skurril", "'dagdrivare, skamtare'", "'dagdrivare, skämtare'"),
 ("agentur", "'satta i rorelse, handla'", "'sätta i rörelse, handla'"),
 ("dyslexi", "'daligt, svart'", "'dåligt, svårt'"),
 ("eufemism", "'anvandning av ett vackert ord for en dalig sak'",
  "'användning av ett vackert ord för en dålig sak'"),
 ("eufemism", "pheme 'ord, sprak'", "pheme 'ord, språk'"),
 # Enda fyndet utanfor etymologiraden. Kortet har ocksa kongruensfelet
 # "pomaderad har" (ska vara "pomaderat"), men det ar inte ett diakritfel
 # och ratttas i nasta v3-omgang, inte har.
 ("pomaderad", "med glansande produkt", "med glänsande produkt"),
]

fynd = json.load(io.open("aao_fynd.json", encoding="utf-8"))
nid_for_ord = {}
for f in fynd:
    nid_for_ord.setdefault(f["ord"], f["noteId"])

planerat = {}
fel = []
for ord_, gammal, ny in BYTEN:
    nid = nid_for_ord.get(ord_)
    if nid is None:
        fel.append("%s: ingen not i aao_fynd.json" % ord_)
        continue
    if nid not in planerat:
        n = invoke("notesInfo", notes=[nid])[0]
        planerat[nid] = [ord_, n["fields"][config.FIELD_BAKSIDA]["value"]]
    raw = planerat[nid][1]
    if raw.count(gammal) != 1:
        fel.append("%s: %d traffar pa %r" % (ord_, raw.count(gammal), gammal))
        continue
    planerat[nid][1] = raw.replace(gammal, ny)

if fel:
    print("AVBRYTER -- inget skrivet:")
    for f in fel:
        print("  " + f)
    sys.exit(1)

print("noter att skriva: %d" % len(planerat))
if "--kor" not in sys.argv:
    for nid, (o, _) in planerat.items():
        print("  %s" % o)
    print("\n(torrkorning -- kor med --kor)")
    sys.exit(0)

for nid, (o, raw) in planerat.items():
    invoke("updateNoteFields",
           note={"id": nid, "fields": {config.FIELD_BAKSIDA: raw}})
print("skrivna: %d" % len(planerat))
