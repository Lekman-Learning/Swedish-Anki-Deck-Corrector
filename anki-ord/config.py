"""Konfiguration för anki-ord. Bekräftat via discover.py/live AnkiConnect-
anrop mot Adams riktiga deck (2026-08-03).
"""

DECK_NAME = "Humanities::Languages::Svenska 10 000"
MODEL_NAME = "Grundläggande-adc63"

FIELD_ORD = "Framsida"
FIELD_BAKSIDA = "Baksida"

# Baksida är EN HTML-blob per kort, inte separata fält:
#   <font color="#3498db">synonym1, synonym2, synonym3</font><br><br>
#   <ol><li>definition 1</li><li>definition 2</li></ol>
#   <i>exempelmening med <font color="#3498db">ordet</font> ibland markerat</i>
#   [valfri <br><br><img src="..." ...> sist, kort med bild]
SYNONYM_COLOR = "#3498db"

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
# Befintliga taggar (ai_optimized, ai_uncertain, ai_failed, granska_först)
# rörs ALDRIG - de är Adams egen historik. Nya taggar läggs bara till.

DEFAULT_BATCH_SIZE = 100  # Adam: granska/rätta 100 kort i taget per 5h-session
