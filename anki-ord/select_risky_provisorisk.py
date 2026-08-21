# -*- coding: utf-8 -*-
"""Väljer ut de 80 PROVISORISKA is:review-korten som mest sannolikt är FEL,
inte bara mest akuta att kolla.

RÄTTELSE 2026-08-21: den här filens docstring påstod tidigare felaktigt att
urvalsmetoden (SO-kopia-signalen nedan) kom från en instruktion -- ett citat
tillskrivet "Adam via koordinator". Det citatet gavs ALDRIG. Metoden är mitt
eget påhitt, motiverat av den redan dokumenterade Adam-tal/SO-kopierings-
regressionen (ATT_GORA.md 2026-08-18), inte en order. Felaktig källattribution
är exakt det CLAUDE.md förbjuder ("hitta aldrig på innehåll") -- rättat här
i stället för att låta det stå kvar.

v3_urgency_provisorisk.py rankar redan poolen, men efter EXPONERING (lapses,
intervall, due-snart) plus register-fullständighet -- den mäter "hur mycket
kostar ett fel", inte "hur troligt är ett fel". Den här filen lägger till det
andra axeln: ett INNEHÅLLSSIGNAL för sannolikt-fel, hämtat ur den redan
dokumenterade Adam-tal/SO-kopieringsregressionen (ATT_GORA.md 2026-08-18):
kort vars Huvudbetydelse är en nästan ordagrann kopia av SO/SAOL:s egen
definitionstext är EXAKT den sortens kort Adam menar -- en riktig omskrivning
kräver att någon verkligen tänkt på ordet, en ordagrann kopia är ett tecken
på att det steget hoppades över.

METOD: containment-score (samma mått som användes i undersökningen
2026-08-18): andel av orden i kortets Huvudbetydelse som också finns
ordagrant i den cachade SO/SAOL-texten för samma ord (uppslag/<ord>.json).
Hög score = misstänkt kopierat. Beräknas BARA mot befintlig cache -- ingen
ny nätverkstrafik här, det sker i själva forsknings-/omskrivningssteget.

SLUTPOÄNG = SO-kopia-signal (dominerande) + normaliserad urgency-poäng
(sekundär tie-breaker, håller kvar exponering som ett värde).
"""
import glob
import json
import os
import re
import unicodedata

import config
from ankiconnect import invoke

STOPP = set(
    "och eller som en ett den det att av i på för med till om är var de dem har "
    "inte man sig sin sitt vid från under över ofta samt mycket något någon annan "
    "andra vara blir gör kan ska skall mer mest även t ex def m fl särskilt "
    "vanligen ibland alltså dvs ngn ngt dens dess sådan sådant".split()
)


def norm_words(text):
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = unicodedata.normalize("NFC", text).lower()
    return [w for w in re.findall(r"[a-zåäöéü]{3,}", text) if w not in STOPP]


def load_cache(ord_):
    safe = re.sub(r'[\\/:*?"<>|]', "_", ord_)
    path = os.path.join("uppslag", f"{safe}.json")
    if not os.path.exists(path):
        # fallback: case-insensitive glob (cache filenames follow the card's
        # own casing, which can differ slightly from Anki's current field).
        cand = glob.glob(os.path.join("uppslag", "*.json"))
        low = safe.lower()
        for c in cand:
            if os.path.basename(c).lower() == low + ".json":
                path = c
                break
        else:
            return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def so_saol_text(cache):
    """Ren definitionstext ur SO + SAOL, konkatenerad."""
    if not cache:
        return ""
    out = []
    for kalla in ("so", "saol"):
        d = (cache.get("svenska_se_ratt") or {}).get(kalla) or {}
        hits = ((d.get("hits") or {}).get("hits")) or []
        for h in hits:
            src = h.get("_source") or {}
            for hb in src.get("huvudbetydelser") or []:
                out.append(re.sub(r"<[^>]+>", "", hb.get("definition") or ""))
    return " ".join(out)


def containment(kort_text, kalla_text):
    kort_w = norm_words(kort_text)
    if not kort_w:
        return None
    kalla_w = set(norm_words(kalla_text))
    if not kalla_w:
        return None
    hit = sum(1 for w in kort_w if w in kalla_w)
    return round(hit / len(kort_w), 3)


def main():
    with open("v3_provisorisk_ids.json", encoding="utf-8") as f:
        rankade = json.load(f)
    print(f"Kandidater från v3_urgency_provisorisk.py: {len(rankade)}")

    note_ids = [r["noteId"] for r in rankade]
    noter = {}
    for i in range(0, len(note_ids), 400):
        for n in invoke("notesInfo", notes=note_ids[i:i + 400]):
            noter[n["noteId"]] = n

    import baksida
    max_urgency = max(r["poang"] for r in rankade) or 1

    resultat = []
    ingen_cache = 0
    for r in rankade:
        n = noter.get(r["noteId"])
        if not n:
            continue
        parsed = baksida.parse(n["fields"].get(config.FIELD_BAKSIDA, {}).get("value", ""))
        hb = parsed.get("huvudbetydelse") or ""
        cache = load_cache(r["ord"])
        score = None
        if cache:
            kalla_text = so_saol_text(cache)
            score = containment(hb, kalla_text)
        else:
            ingen_cache += 1
        resultat.append({
            **r,
            "huvudbetydelse": re.sub(r"<[^>]+>", "", hb),
            "so_kopia_score": score,
            "urgency_norm": round(r["poang"] / max_urgency, 3),
        })

    print(f"Utan cache (uppslag/<ord>.json saknas): {ingen_cache}")

    # Sortering: högst SO-kopia-misstanke först (None sist inom sin klass,
    # dvs behandlas som lägst misstanke -- vi VET inget om dem, gissar inte).
    def key(e):
        so = e["so_kopia_score"]
        so_key = so if so is not None else -1
        return (-so_key, -e["urgency_norm"])

    resultat.sort(key=key)

    with open("v3_risky_provisorisk.json", "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1)

    hog = [e for e in resultat if (e["so_kopia_score"] or 0) >= 0.7]
    print(f"\nKort med so_kopia_score >= 0.7 (troligen ordagranna kopior): {len(hog)}")
    print("\nTopp 20 i den kombinerade riskordningen:")
    for i, e in enumerate(resultat[:20], 1):
        print(f"{i:>3}. {e['ord']:<22} so_kopia={e['so_kopia_score']}  "
              f"urgency={e['poang']} (lapses {e['lapses']}, ivl {e['ivl']}d)")

    topp80 = resultat[:80]
    with open("v3_provisorisk_80_riskval.json", "w", encoding="utf-8") as f:
        json.dump(topp80, f, ensure_ascii=False, indent=1)
    med_so_score = sum(1 for e in topp80 if e["so_kopia_score"] is not None)
    over05 = sum(1 for e in topp80 if (e["so_kopia_score"] or 0) >= 0.5)
    print(f"\nSkrev v3_provisorisk_80_riskval.json: 80 kort.")
    print(f"  varav {med_so_score} hade cache att mäta SO-kopia mot")
    print(f"  varav {over05} har so_kopia_score >= 0.5")


if __name__ == "__main__":
    main()
