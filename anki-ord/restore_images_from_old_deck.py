"""Engångsscript (2026-08-05): OLD-decket ("Humanities::Languages::Svenska OLD")
som bildfacit for nya decket. For v2-kort utan bild i nya decket, om samma ord
(Framsida-matchning) har en bild i OLD-kortets Baksida, kopieras bilden over,
skalas ned sa langsta sidan inte overstiger MAX_DIM px (om den redan ar mindre
lamnas den orord), och laggs till som bild_html via baksida.build().

Bilden sparas under ett NYTT filnamn (aldrig samma som originalet) sa att
OLD-kortets egen visning inte paverkas av nedskalningen.
"""

import base64
import io
import re
import urllib.request

from PIL import Image

from ankiconnect import invoke
import baksida
import config

OLD_DECK = "Humanities::Languages::Svenska OLD"
MAX_DIM = 250
RESTORE_TAG = "bild_atergiven::2026-08-05"

FRONT_KEYS = ["Framsida", "Front"]
BACK_KEYS = ["Baksida", "Back"]
IMG_RE = re.compile(r'<img[^>]*src="([^"]+)"[^>]*>')


def build_old_lookup():
    old_nids = invoke("findNotes", query=f'deck:"{OLD_DECK}"')
    old_info = invoke("notesInfo", notes=old_nids)
    lookup = {}
    for n in old_info:
        fkey = next((k for k in FRONT_KEYS if k in n["fields"]), None)
        bkey = next((k for k in BACK_KEYS if k in n["fields"]), None)
        if not fkey or not bkey:
            continue
        front = n["fields"][fkey]["value"].strip().lower()
        lookup[front] = n["fields"][bkey]["value"]
    return lookup


def find_missing_image_notes():
    note_ids = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" tag:{config.FORMAT_TAG_V2} -is:suspended')
    info = invoke("notesInfo", notes=note_ids)
    return [n for n in info if "<img" not in n["fields"][config.FIELD_BAKSIDA]["value"]]


def fetch_image_bytes(src):
    if src.startswith("http://") or src.startswith("https://"):
        req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.read()
    data = invoke("retrieveMediaFile", filename=src)
    if not data:
        return None
    return base64.b64decode(data)


def resize_if_needed(raw_bytes):
    img = Image.open(io.BytesIO(raw_bytes))
    img.load()
    if max(img.size) <= MAX_DIM:
        return raw_bytes, img.format
    img.thumbnail((MAX_DIM, MAX_DIM), Image.LANCZOS)
    buf = io.BytesIO()
    fmt = img.format if img.format in ("JPEG", "PNG", "WEBP") else "PNG"
    save_img = img.convert("RGB") if fmt == "JPEG" and img.mode in ("RGBA", "P") else img
    save_img.save(buf, format=fmt)
    return buf.getvalue(), fmt


def safe_stem(src):
    name = src.rsplit("/", 1)[-1]
    name = re.sub(r"[^A-Za-z0-9_.\-]", "_", name)
    if "." in name:
        stem, ext = name.rsplit(".", 1)
    else:
        stem, ext = name, "png"
    return stem, ext


def main():
    old_lookup = build_old_lookup()
    missing = find_missing_image_notes()
    print(f"v2-kort utan bild: {len(missing)}")

    candidates = []
    for n in missing:
        word = n["fields"][config.FIELD_ORD]["value"].strip().lower()
        old_back = old_lookup.get(word)
        if not old_back or "<img" not in old_back:
            continue
        m = IMG_RE.search(old_back)
        if not m:
            continue
        candidates.append((n, m.group(1)))

    print(f"kandidater med bild i OLD: {len(candidates)}")

    ok, failed = [], []
    for n, src in candidates:
        word = n["fields"][config.FIELD_ORD]["value"]
        try:
            raw_bytes = fetch_image_bytes(src)
            if not raw_bytes:
                failed.append((word, src, "kunde inte hamta bilddata"))
                continue
            resized_bytes, fmt = resize_if_needed(raw_bytes)
            stem, ext = safe_stem(src)
            ext = {"JPEG": "jpg", "PNG": "png", "WEBP": "webp"}.get(fmt, ext)
            new_filename = f"restored_{stem}.{ext}"

            b64 = base64.b64encode(resized_bytes).decode("ascii")
            invoke("storeMediaFile", filename=new_filename, data=b64)

            current_baksida = n["fields"][config.FIELD_BAKSIDA]["value"]
            parsed = baksida.parse(current_baksida)
            parsed["bild_html"] = (
                f'<br><br><img src="{new_filename}" style="max-width:400px; border-radius:4px;">'
            )
            new_baksida = baksida.build(
                parsed["huvudbetydelse"],
                synonymer=parsed["synonymer"],
                exempelmening=parsed["exempelmening"],
                register=parsed["register"],
                bild_html=parsed["bild_html"],
                synonym_groups=parsed["synonym_groups"],
            )

            invoke(
                "updateNoteFields",
                note={"id": n["noteId"], "fields": {config.FIELD_BAKSIDA: new_baksida}},
            )
            invoke("addTags", notes=[n["noteId"]], tags=RESTORE_TAG)
            ok.append((word, new_filename))
            print(f"  OK: {word} -> {new_filename}")
        except Exception as exc:
            failed.append((word, src, str(exc)))
            print(f"  FEL: {word} ({src}): {exc}")

    print(f"\nKlart. Lyckades: {len(ok)}  Misslyckades: {len(failed)}")
    if failed:
        print("Misslyckade:")
        for word, src, err in failed:
            print(f"  {word}: {src} -> {err}")


if __name__ == "__main__":
    main()
