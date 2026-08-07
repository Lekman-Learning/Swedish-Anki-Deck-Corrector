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

# Snabbkoll 2.0 + villkorlig sökkoll-eskalering, se style_guide.md
# "Flerbetydelse-genomgång". Historik: den GAMLA minnesbaserade snabbkollen
# (FLERBETYDELSE_SNABBKOLL_TAG_PREFIX) klarade inte ett A/B-test (8,75%
# dolda fel kvar även efter "godkänd" snabbkoll) och ledde tillfälligt till
# obligatorisk sökkoll på ALLA kort. Snabbkoll 2.0 (jämförelse mot
# Svenska OLD-decket + egen kunskap, se snabbkoll2.py) validerades sedan
# på 50 kort samma dag: 3 fel hittade av snabbkoll 2.0 själv, 0
# ytterligare fel hittade av en efterföljande sökkoll av samma 50 kort.
# Regel: FLERBETYDELSE_SNABBKOLL2_TAG_PREFIX sätts på ALLA kort som körts
# igenom snabbkoll 2.0. FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX sätts BARA
# på kort som eskalerats till riktig sökkoll (OLD/v2 stämmer inte överens,
# ordet saknar OLD-matchning, eller granskaren själv är osäker) -- inte på
# varje kort längre. FLERBETYDELSE_SNABBKOLL_TAG_PREFIX finns kvar som ren
# historik för kort granskade innan 2.0 fanns.
FLERBETYDELSE_SNABBKOLL_TAG_PREFIX = "flerbetydelse_snabbkoll"  # LEGACY: minnesbaserad bedömning, ingen källa slagen upp
FLERBETYDELSE_SNABBKOLL2_TAG_PREFIX = "flerbetydelse_snabbkoll2"  # jämförd mot Svenska OLD-decket + egen kunskap -- sätts på alla kort som körs igenom snabbkoll2.py
FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX = "flerbetydelse_sokverifierad"  # eskalerad till och bekräftad/rättad via riktig websökning -- bara på kort snabbkoll 2.0 flaggade
# Befintliga taggar (ai_optimized, ai_uncertain, ai_failed, granska_först)
# rörs ALDRIG - de är Adams egen historik. Nya taggar läggs bara till.

DEFAULT_BATCH_SIZE = 100  # Adam: granska/rätta 100 kort i taget per 5h-session

# --- v3.0: kortbyggare + kortgranskare (beslutat 2026-08-07) ---
#
# Från 2026-08-08 skrivs 125 kort/dag om från legacy till v2 och släpps in
# i Adams kö. Kravet: ett kort får INTE avsuspenderas förrän det passerat
# hela kedjan. Tidigare var "granskat" ett påstående i en logg; nu är det
# ett villkor maskinen kontrollerar före släpp (se kortgranskare.py).
#
# Den avgörande lärdomen bakom v3 (2026-08-07): en granskare som verifierar
# sitt EGET arbete i samma sittning bekräftar sig själv. style_guide.md
# noterade risken redan om snabbkoll 2.0 ("samma granskare ... i samma
# sittning"), och den visade sig befogad -- 34 kort med saknad betydelse
# hittades i material som passerat både snabbkoll OCH sökverifiering.
# Därför är OBEROENDE_TAG_PREFIX skild från SOKVERIFIERAD: den får bara
# sättas av en granskare som sett kortet UTAN att se hur det blev till.
OBEROENDE_TAG_PREFIX = "oberoende_verifierad"  # blind andragranskning, ren kontext
DAGSBATCH_TAG_PREFIX = "v3_dagsbatch"          # v3_dagsbatch::YYYY-MM-DD, spårar vilken batch kortet kom i
DAGSBATCH_STORLEK = 125                        # spår A: legacy -> v2, per dag
OMGRANSKNING_STORLEK = 25                      # spår B: redan släppta v2-kort, per dag
# Spår B är kort Adam pluggar JUST NU och som skrevs under den gamla
# processen (3 232 st vid start). Ett fel där kostar varje dag det får stå,
# till skillnad från spår A som är suspenderat och gör noll skada medan det
# väntar. 125/25 optimerar för volym; väg om mot HP-datumet vid behov.

# Taggar ett kort MÅSTE ha för att få avsuspenderas av kortgranskare.slapp().
# Register och Adam-tal kontrolleras dessutom mot LIVE-innehållet, inte mot
# vad som en gång skickades in -- se kortgranskare.kontrollera_slappbar().
SLAPP_KRAVER_TAGGAR = (
    FORMAT_TAG_V2,                          # kortet är faktiskt v2
    FLERBETYDELSE_TAG_PREFIX,                # flerbetydelse-kollen körd
    FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX,  # riktig sökkoll gjord
    OBEROENDE_TAG_PREFIX,                    # blind andragranskning godkänd
)
