"""Bildsvep over ALLA bildlosa levande kort. Adam 2026-09-06:
"kan du lagga in bilder i de kandidat korten du hittade? battre an inget".

🔴 Varfor hela decket och inte min kandidatlista: den handplockade listan
missade bade `brikett` och `gyro` -- huvudordet ("stycke", "instrument") lag
inte i min handskrivna vitlista. Tva av tva. En vitlista over konkreta
substantiv ar samma felkalla som redan fallit en gang, sa den ersatts har av
det enda oberoende testet som finns: FINNS det en svensk Wikipedia-artikel med
bild? Om ja ar ordet konkret nog. Om nej returnerar hamtakandidat None -- det
ar ett forvantat normalfall for abstrakta ord, inte ett fel.

Skriptet APPLICERAR ingenting. Det skriver en sessionsfil med kandidat +
artikelns extract, sa att traffen kan jamforas mot kortets huvudbetydelse
innan bilden anvands (samma krav som wikipedia_bild.py:s egen docstring
staller). En fel bild ar samre an ingen bild pa ett minneskort.
"""
import datetime, json, os, sys, time
sys.path.insert(0, r"C:\Users\Adam\Projects\Swedish-Anki-Deck-Corrector\anki-ord")
import baksida, config
import wikipedia_bild as wb
from ankiconnect import invoke

ids = invoke("findCards", query=f'deck:"{config.DECK_NAME}" -is:suspended')
info = invoke("cardsInfo", cards=ids)
info.sort(key=lambda c: c["due"])

kort = []
for c in info:
    f = {n: v["value"] for n, v in c["fields"].items()}
    p = baksida.parse(f.get(config.FIELD_BAKSIDA, ""))
    if p["bild_html"]:
        continue
    kort.append((c, f, p))

print("Bildlosa levande kort: %d" % len(kort), flush=True)

poster, traff, miss, fel = [], 0, 0, 0
t0 = time.time()
for i, (c, f, p) in enumerate(kort, 1):
    ordet = f.get(config.FIELD_ORD, "").strip()
    kand, felm = None, None
    try:
        kand = wb.hamta_kandidat(ordet)
    except Exception as exc:
        felm = str(exc); fel += 1
    if kand:
        traff += 1
    elif not felm:
        miss += 1
    poster.append({"noteId": c["note"], "ord": ordet,
                   "huvudbetydelse": p["huvudbetydelse"],
                   "kandidat": kand, "hamtningsfel": felm,
                   "godkand": None, "motivering": None, "applicerad": False})
    if i % 100 == 0:
        print("  %4d/%d  traff %d  ingen %d  fel %d  (%.0f s)"
              % (i, len(kort), traff, miss, fel, time.time() - t0), flush=True)

ut = os.path.join(r"C:\Users\Adam\Projects\Swedish-Anki-Deck-Corrector\anki-ord\sessions",
                  "session_%s_bildsvep-alla-bildlosa.json" % datetime.date.today())
json.dump(poster, open(ut, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("\nKLART. %d kort, kandidat hittad for %d (%.0f %%), ingen %d, fel %d"
      % (len(poster), traff, 100.0 * traff / max(len(poster), 1), miss, fel))
print("Skrev", ut)
