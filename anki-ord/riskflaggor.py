"""Mekaniska risksignaler för v3-kortbyggaren (2026-08-07).

Signalerna körs INNAN kortet skrivs om, och deras enda uppgift är att
styra var granskaren lägger sin uppmärksamhet. De avgör aldrig något
själva och ändrar aldrig något -- ett kort kan ha noll flaggor och ändå
vara fel, och en flagga kan vara falsklarm.

**Varje signal här är vald för att den faktiskt gav utdelning
2026-08-07, inte för att den lät rimlig.** Allvarsgraden speglar hur
väl den bevisat sig:

  hog   -- hittade riktiga fel i material som redan var granskat
  medel -- style_guide.md dokumenterar mönstret, men signalen är
           bredare än felet
  lag   -- svag indikation, hög andel falsklarm, tas med för att den
           är gratis

Bakgrund: "saknad hel betydelse" har varit det dominerande felmönstret i
ÅTTA granskningsomgångar i rad, och en blind svepning 2026-08-07 hittade
34 sådana kort som ALLA redan var flerbetydelse-granskade (25 av dem
sökverifierade). Det är den felklassen de flesta signalerna nedan siktar
på.
"""

import re

import baksida

# Ord som bär för lite betydelse för att räknas som innehållsord vid
# jämförelse mellan kort och OLD-facit.
_STOPP = set(
    "och eller som en ett den det att av i på för med till om är var de dem har "
    "inte man sig sin sitt vid från under över ofta samt mycket något någon annan "
    "andra vara blir gör kan ska skall mer mest äv ex def ety t.ex bl.a m.fl "
    "särskilt vanligen ibland alltså dvs".split()
)


def _innehallsord(text):
    text = re.sub(r"<[^>]+>", " ", text or "").replace("&nbsp;", " ").lower()
    return {baksida._stam(w) for w in re.findall(r"[a-zåäöé]{4,}", text) if w not in _STOPP}


def _old_delar(old_facit):
    """OLD-facit skiljer betydelser med ';'. Delar upp och rensar bort
    inbakade exempelmeningar (vanligt i OLD-decket -- 'randas: börja**en
    ny dag randas**; ...' är EN betydelse plus ett exempel, inte två)."""
    if not old_facit:
        return []
    txt = re.sub(r"<[^>]+>", " ", old_facit).replace("&nbsp;", " ")
    delar = [d.strip(" .,") for d in txt.split(";")]
    return [d for d in delar if d and len(d.split()) <= 6]


def berakna(ord_, legacy, old_facit):
    """Returnerar lista med (flagga, allvar, förklaring).

    `legacy` är resultatet av baksida.parse_legacy() -- alltså
    definitioner/synonymer/exempelmening, INTE ett v2-kort.
    """
    flaggor = []
    defs = [d for d in (legacy.get("definitioner") or []) if d and d.strip()]
    syns = [s for s in (legacy.get("synonymer") or []) if s and s.strip()]
    old_delar = _old_delar(old_facit)

    # --- hog: sonden som hittade 34 riktiga fel 2026-08-07 ---
    if len(old_delar) > max(1, len(defs)):
        flaggor.append((
            "old_har_fler_betydelser", "hog",
            f"OLD anger {len(old_delar)} betydelser ({' | '.join(old_delar[:4])}) "
            f"men kortet har {len(defs)}. Kontrollera om en HEL betydelse saknas.",
        ))

    if not old_facit:
        flaggor.append((
            "old_saknas", "hog",
            "Inget OLD-facit finns för ordet. Kortet kan inte jämföras mot något "
            "andra underlag -- kräver riktig sökkoll, och flaggas Gult, inte Grönt.",
        ))

    # --- hog: 'dold andra betydelse', style_guide.md:s eget kärnmönster ---
    if len(defs) <= 1 and len(syns) >= 3:
        flaggor.append((
            "dold_betydelse", "hog",
            f"{len(syns)} synonymer men bara {len(defs)} betydelse "
            f"({', '.join(syns[:5])}). Hör alla till SAMMA betydelse? "
            "Om inte saknar kortet en betydelse (jfr konglomerat).",
        ))

    # --- medel: OLD nämner något kortet inte alls berör ---
    if old_facit and defs:
        kort_ord = _innehallsord(" ".join(defs) + " " + " ".join(syns))
        old_ord = _innehallsord(old_facit)
        saknade = old_ord - kort_ord
        if saknade and not (old_ord & kort_ord):
            flaggor.append((
                "old_delar_inget_ordforrad", "medel",
                f"Kortet och OLD delar inget innehållsord (OLD: {', '.join(sorted(saknade)[:5])}). "
                "Oftast bara en parafras -- men det är så här ett rakt motsatt "
                "innehåll ser ut (jfr ingäld).",
            ))

    # --- medel: nästan identiska definitioner, ska slås ihop ---
    prefix = [re.sub(r"<[^>]+>", "", d)[:15].lower() for d in defs]
    if len(prefix) >= 2 and len(set(prefix)) < len(prefix):
        flaggor.append((
            "dubblettdefinition", "medel",
            "Två definitioner börjar likadant -- troligen samma betydelse "
            "formulerad två gånger, slå ihop till en.",
        ))

    # --- medel: cirkulär synonym, avslöjar svaret ---
    if " " not in ord_.strip():
        st = baksida._stam(ord_)
        cirk = [s for s in syns if len(st) >= 4 and st in s.lower().replace(" ", "")]
        if cirk:
            flaggor.append((
                "cirkular_synonym", "medel",
                f"Synonymen {', '.join(cirk)} innehåller uppslagsordet och avslöjar svaret.",
            ))

    # --- lag: exempelmeningen behöver skrivas om ändå ---
    ex = re.sub(r"<[^>]+>", "", legacy.get("exempelmening") or "").strip()
    if not ex:
        flaggor.append(("tom_exempelmening", "lag", "Exempelmening saknas, måste skrivas."))
    elif len(ex.split()) < 4:
        flaggor.append((
            "fragment_exempel", "lag",
            f"Exempelmeningen är en fras, inte en mening: {ex!r}",
        ))

    return flaggor


def sammanfatta(flaggor):
    """Kortform för dumpar: 'hog:old_har_fler_betydelser,dold_betydelse'."""
    if not flaggor:
        return ""
    per = {}
    for namn, allvar, _ in flaggor:
        per.setdefault(allvar, []).append(namn)
    return " ".join(f"{a}:{','.join(n)}" for a, n in
                    sorted(per.items(), key=lambda kv: {"hog": 0, "medel": 1, "lag": 2}[kv[0]]))


def hogsta_allvar(flaggor):
    for a in ("hog", "medel", "lag"):
        if any(f[1] == a for f in flaggor):
            return a
    return None
