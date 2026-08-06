"""Konfiguration för anki-ord. Bekräftat via discover.py/live AnkiConnect-
anrop mot Adams riktiga deck (2026-08-03).
"""

DECK_NAME = "Humanities::Languages::Svenska 10 000"
MODEL_NAME = "Grundläggande-adc63"

FIELD_ORD = "Framsida"
FIELD_BAKSIDA = "Baksida"

# Baksida är EN HTML-blob per kort, format beslutat 2026-08-04, korrigerat
# 2026-08-04 (inga fältetiketter, bara huvudbetydelsens värde fet, register
# i temats standardfärg) — se style_guide.md, "Kortformat v2":
#   <b>fras 1 / fras 2</b><br>
#   (register)<br>   [obligatorisk, minst en tagg]
#   <br>
#   <font color="#3498db">synonym1, synonym2</font><br>
#   <br>
#   <i>mening med <font color="#3498db">ordet</font> markerat</i>
#   [valfri <br><br><img src="..." ...> sist, kort med bild]
SYNONYM_COLOR = "#3498db"

# Register-tagg: STÄNGD vokabulär, en tagg per axel max (se style_guide.md).
# Fritext gled isär över 10k kort/flera pass tidigare (t.ex. fabricerade
# synonymer) — samma risk gäller register om det inte låses.
REGISTER_FORMALITY = [
    "arkaisk", "litterär", "formell", "vardaglig", "dialektal", "slang", "vulgär",
]  # omärkt = neutral
REGISTER_VALENS = [
    "positiv", "lätt negativ", "negativ", "nedsättande", "skämtsam", "ironisk",
    "eufemistisk",
]  # omärkt = neutral

# Flagg-nummer bekräftade via cardsInfo mot riktiga kort (2026-08-03):
#   flag:1 (849 kort)  = Röd  = stämmer inte alls -> hög prioritet
#   flag:2 (1328 kort) = Gul  = osäker -> granskas efter röda
#   flag:4 (7772 kort) = Blå  = stämmer 100% -> rör inte
#   flag:3 (84 kort)   = utanför scope (litet, separat historiskt bucket, ej nämnt av Adam)
FLAG_ROD = 1
FLAG_GUL = 2
FLAG_GRON = 3
FLAG_BLA = 4

REVIEWED_TAG_PREFIX = "granskad"  # tagg blir granskad::YYYY-MM-DD
FORMAT_TAG_V2 = "kortformat::v2"  # sätts på alla kort som skrivs i v2-formatet
FLERBETYDELSE_TAG_PREFIX = "flerbetydelse_granskad"  # tagg blir flerbetydelse_granskad::YYYY-MM-DD,
# sätts på kort som gått igenom "dold andra betydelse"-kollen (style_guide.md,
# beslutat 2026-08-05, se scan_multiple_meanings.py) — skild från granskad::
# eftersom kortet redan kan ha granskats en gång innan denna kontroll fanns.

# Sökkoll är OBLIGATORISKT sedan 2026-08-06 (se style_guide.md
# "Flerbetydelse-genomgång" — ett A/B-test visade att minnesbaserad
# snabbkoll INTE mätbart minskar felfrekvensen, 8,75% dolda fel kvar även
# efter "godkänd" snabbkoll). FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX ska
# alltid sättas tillsammans med FLERBETYDELSE_TAG_PREFIX för nya/omgranskade
# v2-kort. FLERBETYDELSE_SNABBKOLL_TAG_PREFIX finns kvar för historik/äldre
# kort och som valfri billig prioriteringssignal, men ersätter aldrig sökkoll.
FLERBETYDELSE_SNABBKOLL_TAG_PREFIX = "flerbetydelse_snabbkoll"  # minnesbaserad bedömning, ingen källa slagen upp (historisk/prioritering, ej tillräckligt ensamt)
FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX = "flerbetydelse_sokverifierad"  # faktiskt källkollad (svenska.se/synonymer.se/SAOB/OLD-decket/annat) -- OBLIGATORISKT för nya v2-kort
# Befintliga taggar (ai_optimized, ai_uncertain, ai_failed, granska_först)
# rörs ALDRIG - de är Adams egen historik. Nya taggar läggs bara till.

DEFAULT_BATCH_SIZE = 100  # Adam: granska/rätta 100 kort i taget per 5h-session
