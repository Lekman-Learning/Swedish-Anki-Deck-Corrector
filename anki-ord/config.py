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
#   [valfri <br><br><font color="#9e9e9e">→ etymologi</font>, se nedan]
#   [valfri <br><br><img src="..." ...> sist, kort med bild]
#
# Etymologiraden (tillagd 2026-08-08 på Adams begäran): samma <br><br>-lucka
# som mellan de övriga blocken, alltid efter exempelmeningen och före bilden.
# Tas BARA med när ursprunget gör betydelsen lättare att förstå eller minnas,
# aldrig som språkhistorisk trivia.
#
# UTSEENDET ÄNDRAT 2026-08-10 (Adam valde mellan tre uppritade alternativ):
# raden var förut ren text utan färg, vilket byggde på antagandet att
# etymologin skulle vara sällsynt. Nu ska den finnas på varje kort där
# ursprunget säger något -- och då blir en omarkerad textrad direkt efter en
# KURSIV exempelmening svår att skilja från själva exemplet. Därför: egen grå
# rad med inledande pil. Grå och inte fet, eftersom bara huvudbetydelsen får
# vara fet (samma regel som registret) -- pilen bär igenkänningen i stället
# för vikten, så raden går att hoppa över vid snabb repetition.
#
# Färgen är mellangrå med flit: den ska vara läsbar mot BÅDE Ankis ljusa och
# mörka tema. En ljusare grå försvinner i dagläge, en mörkare i nattläge.
SYNONYM_COLOR = "#3498db"
ETYMOLOGI_COLOR = "#9e9e9e"
ETYMOLOGI_PIL = "→"

# Register-tagg: STÄNGD vokabulär, en tagg per axel max (se style_guide.md).
# Fritext gled isär över 10k kort/flera pass tidigare (t.ex. fabricerade
# synonymer) — samma risk gäller register om det inte låses.
#
# `neutral` tillagt 2026-08-10 efter en mätning som förklarade ett fel ingen
# granskning hittat på elva omgångar: **1 587 av 3 233 kort (49,1 %) var märkta
# `formell`** -- och de v3-granskade låg HÖGRE (56,4 %) än de ogranskade
# (48,7 %), alltså gjorde granskningen fältet sämre.
#
# Orsaken var strukturell, inte slarv. Tre regler tillsammans gjorde felet
# obligatoriskt:
#   1. registerraden får aldrig vara tom -- minst en tagg krävs,
#   2. valör får utelämnas på neutrala ord (style_guide tillåter det uttryckligen),
#   3. => formalitetsaxeln måste alltid bära den obligatoriska taggen,
#   4. men varje värde på den axeln var ett MARKERAT register.
# Ett vanligt standardsvenskt ord (marinera, sepia, katedral) hade alltså
# ingen sann tagg att välja, och `formell` var det minst fel-känsliga. Guiden
# lärde till och med ut det genom sitt eget exempel (`formell` för *taverna*).
#
# Kommentaren "omärkt = neutral" fanns här hela tiden, men frånvaro var
# förbjuden -- vokabulären och den obligatoriska regeln sa emot varandra.
# Ett explicit värde löser båda: raden blir ifylld OCH sann.
# Flykt-taggen. Laglig på varje axel, men ALDRIG tyst: validate_register
# rapporterar den särskilt, och `v3_taggkoll.py` kan räkna den.
#
# Varför den finns (Adams beslut 2026-08-10: "tillåt flexibilitet om den inte
# hittar det"): en ÖPPEN vokabulär glider isär över 10 000 kort -- det är mätt,
# och skälet till att listan låstes. Men en LÅST vokabulär som saknar rätt värde
# tvingar fram en lögn, vilket är exakt hur 49 % av decket blev "formell".
# Båda felen är verkliga, så valet står inte mellan dem.
#
# `oklart` är tredje vägen: den är sann (ingen påstår något falskt), den är
# laglig (raden blir ifylld), och den är RÄKNAD. Använder 200 kort `oklart` av
# samma skäl är det bevis för att ett nytt värde behövs -- och då växer
# vokabulären på mätning i stället för gissning. En flykt-tagg som ingen räknar
# är en lucka; en som räknas är ett mätinstrument.
REGISTER_OKLART = "oklart"

# Axel 1 -- STILNIVÅ. `neutral` är det normala fallet, inte ett misslyckande.
REGISTER_FORMALITY = [
    "neutral",          # vanlig standardsvenska -- VANLIGASTE RÄTTA SVARET
    "vardaglig",
    "slang",            # under vardaglig, gatuspråk
    "vulgär",           # svordomar/tabuspråk, grövre än slang
    "barnspråk",        # vovve, nalle
    "dialektal",        # regional variant
    "fackspråklig",     # teknisk stilnivå; VILKET fält anges i REGISTER_DOMAN
    "formell",          # byråkratiskt/officiellt -- INTE "ovanligt" eller "fint"
    "högtidlig",        # ceremoniellt/patetiskt: vigsel, hädanfärd
    "litterär",         # poetiskt/bokspråk, LEVANDE men skriftligt
    "ngt ålderdomlig",  # SAOL:s {ngt åld.} -- daterat men begripligt (pistong)
    "arkaisk",          # UR BRUK
    REGISTER_OKLART,
]

# Axel 2 -- VALÖR. `neutral` skrivs UT (Adams beslut 2026-08-10), inte utelämnas:
# ett tomt fält och ett bedömt fält såg tidigare likadana ut.
REGISTER_VALENS = [
    "neutral",             # ingen känsloladdning -- VANLIGASTE RÄTTA SVARET
    "positiv",
    "ömsint",              # kärleksfullt: älskling, raring
    "skämtsam",
    "ironisk",             # betyder motsatsen
    "eufemistisk",         # mildrar hård verklighet: "gå bort"
    "lätt negativ",
    "negativ",
    "nedsättande",         # om PERSONER
    "starkt nedsättande",  # SO:s egen gradering, t.ex. pöbel
    REGISTER_OKLART,
]

# Axel 3 -- FACKOMRÅDE. NY 2026-08-10. Valfri, oftast tom.
#
# style_guide.md har sedan 2026-08-04 sagt att ämnesdomän är "EN EGEN, separat
# märkning -- blanda inte ihop dem", men den fanns aldrig i koden och användes
# därför aldrig. Den blinda granskningen 2026-08-10 saknade den upprepade
# gånger: `beskärm` är SO-märkt "särsk. bibliskt", `gensaga` "särsk. juridik",
# `granulera` har en medicinsk betydelse, `bleke` en jordbruksbetydelse. Alla
# fyra fick i stället en stilnivå-tagg som inte var sann.
REGISTER_DOMAN = [
    "juridik", "medicin", "biologi", "kemi", "fysik", "matematik", "teknik",
    "IT", "ekonomi", "politik", "militär", "sjöfart", "jordbruk", "geologi",
    "religion", "bibliskt", "filosofi", "psykologi", "lingvistik", "historia",
    "musik", "konst", "litteraturvetenskap", "sport", "matlagning", "jakt",
    REGISTER_OKLART,
]

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

# v3-märkning (beslutat 2026-08-08, Adam: "för alla framtida kort som
# använde 3.0-metoden så taggas det alltid med 3.0"). De gamla
# snabbkoll2-taggarna rörs INTE -- de är historik och beskriver den metod
# som faktiskt användes då.
#
# Taggen sätts BARA när den strikta vägen faktiskt gick igenom: riktig
# sökkoll med loggad källa. Ett kort som körts på den billiga vägen får
# ingen v3-tagg, hur v3-lik processen än kändes. Det är hela poängen --
# 2026-08-08 sattes `sokverifierad` på 177 kort som aldrig sökkollats, och
# en tagg som sätts på granskarens ord är inte värd något.
V3_TAG_PREFIX = "v3_granskad"                  # v3_granskad::YYYY-MM-DD

# Förtur i v3-kön (2026-08-08). Kort med den här taggen plockas FÖRE
# den vanliga due-ordningen av kortbyggare.py, i båda spåren.
#
# En prio-tagg som bara syns i browsern är dekoration -- den måste ändra
# URVALET, annars ligger korten kvar bakom 3 000 andra oavsett hur de är
# märkta. Därför hämtar hamta_pool() prio-korten först och fyller bara på
# med den vanliga poolen om det finns plats kvar.
PRIO_TAG_HOG = "v3_prio::hog"
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
    V3_TAG_PREFIX,                           # skrivet med v3-metoden
    OBEROENDE_TAG_PREFIX,                    # blind andragranskning godkänd
)
