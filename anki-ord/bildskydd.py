"""Skydd mot att bilder försvinner ur decket. Adams krav 2026-08-10.

    *"Old, svenska Old, har inte alla bilderna som efter decket har. Det
    betyder att om du tar bort bilder på vissa kort, så kommer de vara borta
    för alltid. Så snälla, fixa bildgrejen jätte, jättevälgjort."*

MÄTT SAMMA DAG, och han har rätt:

    levande decket : 10 031 kort, 2 841 med bild
    OLD (facit)    : 10 030 kort, 1 810 med bild
    bilder i levande som INTE finns i OLD: **1 071**

Alltså: **38 % av bilderna har ingen backup alls.** Antagandet att OLD är ett
facit man alltid kan återställa ifrån är falskt. `restore_images_from_old_deck.py`
kan bara rädda de 1 770 som finns i båda.

Det gör bildförlust till den enda **oåterkalleliga** felklassen i hela
projektet. Allt annat går att skriva om från källorna; en bild som raderas ur
en not och vars mediafil sedan städas bort av Anki är borta för gott.

Tre lager, i den ordning som faktiskt skyddar:

1. `sakra()`  — skriver ett manifest över VARJE bild i decket, ord för ord,
   plus en kopia av mediafilerna. Det är den riktiga försäkringen: även om
   både noten och Ankis mediamapp skadas finns filen kvar i repot.
2. `kontrollera()` — jämför decket mot manifestet och listar varje bild som
   FÖRSVUNNIT sedan sist. Körs efter varje batch.
3. `aterstall()` — lägger tillbaka en förlorad bild ur manifestet.

Lager 1 måste köras FÖRE nästa skrivning, inte efter. Ett manifest som skapas
efter att bilden försvunnit bevarar ingenting.
"""
import base64
import hashlib
import json
import os
import re
import shutil
import sys

import config
from ankiconnect import invoke

MANIFEST = "bildmanifest.json"
MEDIAKAT = "bildbackup"
_IMG_SRC = re.compile(r'<img[^>]+src="([^"]+)"')


def _alla_noter(deck):
    ids = invoke("findNotes", query=f'"deck:{deck}"') or []
    ut = []
    for i in range(0, len(ids), 1000):
        ut.extend(invoke("notesInfo", notes=ids[i:i + 1000]))
    return ut


def _bild_html(note):
    bak = note["fields"].get(config.FIELD_BAKSIDA, {}).get("value", "")
    m = re.search(r"((?:<br>\s*)*<img.*)$", bak, re.DOTALL)
    return m.group(1).strip() if m else None


def sakra():
    """Manifest + kopia av varje mediafil. Idempotent, kan köras när som helst."""
    os.makedirs(MEDIAKAT, exist_ok=True)
    gammalt = {}
    if os.path.exists(MANIFEST):
        gammalt = json.load(open(MANIFEST, encoding="utf-8")).get("kort", {})

    nytt, kopierade, missade = {}, 0, []
    for n in _alla_noter(config.DECK_NAME):
        ord_ = n["fields"][config.FIELD_ORD]["value"]
        html = _bild_html(n)
        if not html:
            continue
        filer = _IMG_SRC.findall(html)
        nytt[ord_] = {"noteId": n["noteId"], "html": html, "filer": filer}
        for f in filer:
            mal = os.path.join(MEDIAKAT, f)
            if os.path.exists(mal):
                continue
            # retrieveMediaFile ger base64. Gar det inte att hamta ar filen
            # redan borta ur Ankis mediamapp -- da ar noten enda spar som
            # finns kvar, och det skrivs ut i stallet for att tigas ihjal.
            try:
                data = invoke("retrieveMediaFile", filename=f)
            except Exception:
                data = None
            if not data:
                missade.append((ord_, f))
                continue
            with open(mal, "wb") as fh:
                fh.write(base64.b64decode(data))
            kopierade += 1

    # Ord som HADE bild i det gamla manifestet men inte langre -- forlust
    # som redan hunnit ske. Skrivs ut, aldrig tyst overskrivet.
    forlorade = sorted(set(gammalt) - set(nytt))

    json.dump({"deck": config.DECK_NAME, "antal": len(nytt), "kort": nytt},
              open(MANIFEST, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"Manifest: {len(nytt)} kort med bild "
          f"({len(nytt) - len(gammalt):+d} mot förra körningen)")
    print(f"Mediafiler kopierade denna gång: {kopierade}")
    print(f"Totalt i {MEDIAKAT}/: {len(os.listdir(MEDIAKAT))}")
    if missade:
        print(f"VARNING: {len(missade)} filer gick inte att hämta ur Ankis "
              f"mediamapp — noten är enda spåret som finns kvar:")
        for o, f in missade[:10]:
            print(f"  {o}: {f}")
    if forlorade:
        print(f"FÖRLUST SEDAN FÖRRA KÖRNINGEN: {len(forlorade)} kort har "
              f"tappat sin bild: {', '.join(forlorade[:15])}")
        print("  Kör 'aterstall' för att lägga tillbaka dem ur manifestet.")
    return nytt, forlorade


def kontrollera():
    """Jämför decket mot manifestet. Returnerar listan över förlorade bilder."""
    if not os.path.exists(MANIFEST):
        sys.exit(f"{MANIFEST} saknas — kör 'sakra' först.")
    manifest = json.load(open(MANIFEST, encoding="utf-8"))["kort"]
    nu = {n["fields"][config.FIELD_ORD]["value"]: _bild_html(n)
          for n in _alla_noter(config.DECK_NAME)}
    forlorade = [o for o in manifest if not nu.get(o)]
    andrade = [o for o in manifest
               if nu.get(o) and nu[o] != manifest[o]["html"]]
    print(f"Manifest: {len(manifest)} kort med bild")
    print(f"Saknar bild NU: {len(forlorade)}")
    if forlorade:
        print("  " + ", ".join(forlorade[:20]))
    print(f"Ändrad bild-HTML (kan vara ok): {len(andrade)}")
    return forlorade


def aterstall(ord_lista=None):
    """Lägger tillbaka bilder ur manifestet på kort som tappat dem."""
    manifest = json.load(open(MANIFEST, encoding="utf-8"))["kort"]
    import baksida
    mal = ord_lista or kontrollera()
    lagade = []
    for ord_ in mal:
        post = manifest.get(ord_)
        if not post:
            print(f"  {ord_}: finns inte i manifestet, kan inte återställas")
            continue
        n = invoke("notesInfo", notes=[post["noteId"]])[0]
        raw = n["fields"][config.FIELD_BAKSIDA]["value"]
        p = baksida.parse(raw)
        if p["bild_html"]:
            continue
        ny = baksida.build(
            p["huvudbetydelse"], synonymer=p["synonymer"],
            synonym_groups=p["synonym_groups"], exempelmening=p["exempelmening"],
            register=p["register"], etymologi=p["etymologi"],
            bild_html=post["html"])
        invoke("updateNoteFields",
               note={"id": post["noteId"], "fields": {config.FIELD_BAKSIDA: ny}})
        lagade.append(ord_)
    print(f"Återställde {len(lagade)} bilder: {', '.join(lagade[:20])}")
    return lagade


if __name__ == "__main__":
    steg = sys.argv[1] if len(sys.argv) > 1 else "sakra"
    {"sakra": sakra, "kontrollera": kontrollera, "aterstall": aterstall}[steg]()
