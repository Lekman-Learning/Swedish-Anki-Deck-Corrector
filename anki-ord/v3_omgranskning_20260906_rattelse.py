# -*- coding: utf-8 -*-
"""Rattar de 50 harda forgranskningsanmarkningarna i 2026-09-06-batchen.

ORSAKEN, for protokollet: jag tog synonymerna ur synonymer.se:s redaktionella
lista i stallet for ur SO/SAOL. Det ar EXAKT det dokumenterade felet fran
batch 6 (2026-08-25, se visa_uppslag.py:s huvudkommentar) -- tio
`synonym_utan_ordboksbelagg` av samma skal. Har blev det 29. Alla synonymer ar
nu omprovade mot RASTRUKTUREN (visa_uppslag.py), inte mot sammandraget och
aldrig mot synonymer.se: det som star kvar omarkerat finns ordagrant i SO:s
SYN-tagg eller i SO/SAOL:s definitionstext, resten ar nedgraderat till
`≈≈ kategori` ur kortets egen definition.

Utover det: tre kort har fatt fler betydelser (belagga 4->5, agrar 2->4) eller
rattat register (grand), och nio verifierade falsklarm har fatt
`forgranska_tillat` med skriven motivering.
"""
import io, json

FIL = "sessions/session_2026-09-06_v3-omgranskning.json"

# ---------------------------------------------------------------- synonymer
# Endast omarkerade poster nedan ar ordboksbelagda. Kallan star i kommentaren.
GRP = {
 "ömma för":     [["≈≈ känna medlidande"]],                  # SO: 'hysa medkänsla' -- ingen enordssynonym
 "lovvärd":      [["berömvärd"]],                            # SO SYN
 "mondän":       [["elegant", "fin"]],                       # SAOL: 'fin, elegant, av värld'
 "krösus":       [["≈≈ rik person"]],                        # SO/SAOL: 'mycket rik person' -- ingen synonym
 "vidtaga":      [["≈≈ genomföra en åtgärd"], ["≈≈ ta vid"]],
 "asketisk":     [["≈≈ avhållsam"], ["≈≈ sparsam i stilen"]],
 "lake":         [["saltlake"], ["≈≈ torskfisk"]],           # SAOL: '... konservering, saltlake'
 "vidja":        [["≈≈ kvist"]],
 "åtbörd":       [["gest"]],                                 # SAOL: 'gest'
 "oför":         [["vanför"]],                               # SO: 'vanför'
 "gå med håven": [["≈≈ samla in pengar"], ["≈≈ fiska efter beröm"]],
 "agn":          [["skärmfjäll", "blomfjäll"], ["bete"]],    # SAOL: 'blom- el. skärmfjäll ...' / 'bete vid fiske'
 "förfara":      [["gå till väga"]],                         # SO: 'gå till väga'
 "förevändning": [["≈≈ påhittat skäl"]],
 "pracka":       [["truga på", "lura på"], ["≈≈ andfågel"]], # SAOL: 'truga på, lura på'
 "cession":      [["≈≈ fordringsöverlåtelse"], ["≈≈ landavträdelse"], ["konkurs"]],  # SO under: 'konkurs'
 "genever":      [["≈≈ brännvin"]],
 "korollarium":  [["följdsats"]],                            # SAOL: 'följdsats'
 "pagod":        [["≈≈ tempelbyggnad"]],
 "exstirpera":   [["operera bort"]],                         # SAOL: 'operera bort svulst'
 "gensträvig":   [["motsträvig"]],                           # SO och SAOL: 'motsträvig'
 "mola":         [["småvärka"]],                             # SO: 'ihållande småvärka', SAOL: 'småvärka'
 "obetingad":    [["≈≈ medfödd"], ["oinskränkt", "förbehållslös"]],  # SO under: 'absolut, oinskränkt'; SAOL
 "strimmig":     [["≈≈ randig"]],
 "svängtapp":    [["pivå"]],                                 # SO SYN
 "hedendom":     [["≈≈ flergudadyrkan"], ["ateism"]],        # SO under: 'ateism'
 "libretto":     [["≈≈ operatext"]],
 "avpassa":      [["≈≈ anpassa"]],
}

# ---------------------------------------------- omskrivna huvudbetydelser m.m.
HB = {
 # 'elegant' flyttat fran definitionen till synonymraden -- det ar SAOL:s ord
 # och far darfor vara synonym, men da far det inte sta i definitionen ocksa.
 "mondän": "Förnämt stilfull, med prägel av den stora världen",
 # 'kvist' flyttat till synonymraden av samma skal; SAOL sager 'böjlig gren'.
 "vidja": "Lång och böjlig gren, ofta av vide, som man kan fläta med",
 # SO:s parentes '<<vanligen med flera utspringande takfall>>' tillagd.
 "pagod": "Östasiatiskt tempel byggt som ett fristående torn, oftast med flera "
          "utskjutande takfall",
 # 4 -> 5 betydelser: SO:s 'gora fast' (sjofartsordet) tillagd, och ordningen
 # foljer nu SO:s egen.
 "belägga": "Täcka en yta med ett lager ; ta upp platsen i något så att den är "
            "upptagen ; genom beslut förena med en påföljd, till exempel skatt "
            "eller förbud ; göra fast ett tåg om en knap ; visa med fakta att "
            "något stämmer",
 # 2 -> 4 betydelser: SO har tva adjektivled och tva substantivled, alla med
 # egen definitionstext.
 "agrar": "Som har att göra med jordbruk ; dominerad av jordbruk ; person som "
          "driver jordbrukets intressen i politiken ; jordbrukare",
}

REG = {
 # SO markerar partikelbetydelsen 'mindre brukligt' -- det var
 # register_motsager_markning.
 "grand": "mindre brukligt, neutral ; neutral, neutral, historia",
 "belägga": "neutral, neutral ; neutral, neutral ; fackspråklig, neutral, juridik ; "
            "fackspråklig, neutral, sjöfart ; neutral, neutral",
 "agrar": "neutral, neutral, lantbruk ; neutral, neutral, lantbruk ; "
          "neutral, neutral, politik ; neutral, neutral, lantbruk",
}

GRP.update({
 "belägga": [["≈≈ täcka med lager"], ["≈≈ uppta"], ["belasta"], ["≈≈ göra fast"],
             ["bevisa"]],                                    # SAOL: 'belasta' / 'bevisa'
 "agrar": [["jordbruks-"], ["≈≈ jordbruksdominerad"],
           ["förespråkare för jordbruksintressen"], ["jordbrukare"]],
})

# ------------------------------------------------------- verifierade falsklarm
T = {
 "ömma för": {
  "frammande_uppslagsord":
    "Flerordsuttryck. svenska.se:s fritextsokning pa 'omma for' matchar delordet "
    "'for' -- preposition, konjunktion OCH substantiv, tillsammans ett av "
    "svenskans mest polysema ord med 14 egna definitioner i rastrukturen -- och "
    "drar in 25 orelaterade lemman (amma, emma, finger, far, fol ...). Grundordet "
    "har en egen, ren SO-artikel: SO-LEMMA omma (verb), kontrollerad via "
    "visa_uppslag.py. Samma dokumenterade monster som 'ga i clinch' och "
    "'karringen mot strommen' (CLAUDE.md 2026-08-19).",
  "betydelse_kan_saknas":
    "Rakningen kommer fran det kontaminerade sammandraget (se ovan) och raknar "
    "prepositionen 'for':s betydelser som om de vore uppslagsordets. RASTRUKTUREN "
    "visar att SO-LEMMA omma (verb) har exakt TVA definitioner: 'valla omhet' "
    "<<om kroppsdel>> och 'hysa medkansla' <<med nagon el. nagot; vanligen med "
    "bibetydelse av att ge konkret stod>>. Kortets uppslagsord ar inte 'omma' "
    "utan 'OMMA FOR', och prepositionen for ar just det som valjer den andra "
    "betydelsen -- 'foten ommar' (betydelse 1) kan aldrig konstrueras med for. "
    "En betydelse ar alltsa ratt for detta uppslagsord. SO:s '<<vanligen med "
    "bibetydelse av att ge konkret stod>>' ar dessutom kallan till kortets 'och "
    "vilja skydda'.",
 },
 "vidtaga": {
  "frammande_uppslagsord":
    "Det doljda lemmat ar 'vidta' -- inte ett frammande ord utan samma verb i "
    "sin kortare, numera vanligare form (SAOL:s eget exempel skriver ut bada: "
    "'milsvida skogar VIDTAR el. TAR VID norr om byn'). Rastrukturen visar "
    "SO-LEMMA vidtaga utan egen definitionstext, med innehallet under vidta. "
    "Kortets uppslagsord ar den langa formen, som ar den Adam har i decket; "
    "betydelserna ar hamtade fran den korta och galler bada.",
 },
 "asketisk": {
  "betydelse_kan_saknas":
    "Rastrukturen: SO-LEMMA asketisk har EN definition ('som helt avstar fran "
    "njutningar') och TVA underbetydelser, varav den forsta ar markt '(ingen "
    "egen definition -- utvidgning)' och den andra har egen text ('mycket "
    "sparsam <<med uttrycksmedel eller dylikt>>'). En utvidgning utan egen "
    "definition ar ingen betydelse (samma regel som 'flirta'-fallet 2026-08-25). "
    "Alltsa tva sanna betydelser -- exakt vad kortet har.",
 },
 "endiv": {
  "frammande_uppslagsord":
    "Det doljda lemmat ar 'endive', den engelska/franska formen av samma ord, "
    "inte ett annat ord. Ingen glosa pa kortet kommer darifran: hela "
    "huvudbetydelsen ar hamtad ur SO:s svenska artikel ('en besk, sprod, avlang "
    "salladsliknande gronsak').",
 },
 "grand": {
  "frammande_uppslagsord":
    "De sju doljda lemmana ar sammansattningar med grand som forsta led -- grand "
    "prix, grand slam, grand danois, grand mal, grand old man, grand tour. Alla "
    "ar egna uppslagsord med egna artiklar, inte betydelser hos 'grand'. Ingen "
    "glosa pa kortet kommer fran dem.",
  "betydelse_kan_saknas":
    "Rastrukturen visar TVA SO-lemman: 'grand' (substantiv) med definitionen "
    "'liten partikel' och ett andra 'grand' (substantiv) utan egen "
    "definitionstext. SAOL:s tredje led, 'namn pa vissa stora tavlingar', ar "
    "inte en tredje betydelse hos grand utan SAOL:s samlade hanvisning till just "
    "de sammansattningar som doljts som frammande lemman ovan (grand prix, grand "
    "slam). Kortets tva betydelser -- partikeln och den spanska adelstiteln, den "
    "senare belagd i OLD-facit ('manlig spansk hogadel') -- ar de tva som hor "
    "till uppslagsordet sjalvt.",
 },
 "snaskig": {
  "betydelse_kan_saknas":
    "Rastrukturen: SO-LEMMA snaskig har EN definition ('solig och kladdig') och "
    "EN underbetydelse med egen text ('som innebar otillborligt rotande i "
    "manniskors intima liv'). Det ar tva betydelser, vilket ar precis vad kortet "
    "har. Sammandragets tredje post ar SAOL:s 'smutsig; snuskig', alltsa samma "
    "forsta betydelse i en annan ordboks formulering -- inte en ny betydelse.",
 },
 "gå med håven": {
  "frammande_uppslagsord":
    "Flerordsuttryck. Fritextsokningen matchar 'ga', svenskans mest polysema "
    "verb (rastrukturen visar 20-talet definitioner: forflytta sig, ha sin "
    "utstrackning, utveckla sig, fortlopande fungera ...), och drar in 29 "
    "orelaterade lemman (Herre Gud, avstand, bro, dag, gata ...). Innehallet pa "
    "kortet kommer uteslutande fran SO:s artikel for HAV, dar bada de "
    "idiomatiska betydelserna star. Samma monster som 'ga i clinch' "
    "(CLAUDE.md 2026-08-19).",
  "betydelse_kan_saknas":
    "Rakningen galler verbet 'ga', inte frasen (se ovan). SO:s artikel for hav "
    "ger tva idiomatiska betydelser for 'ga med haven': 'forsoka fa bidrag' och "
    "'forsoka locka fram vanligt omdome om sig sjalv'. Kortet har bada -- den "
    "forsta var den som saknades i legacy och ar hela skalet till att kortet "
    "skrivits om.",
 },
 "agn": {
  "betydelse_kan_saknas":
    "Rastrukturen visar TVA SO-lemman, ett per betydelse: 'skarm- och blomfjall "
    "(kring frukt) hos sad, som skiljs bort vid troskning' (med EN underbetydelse "
    "markt '(ingen egen definition -- utvidgning)', alltsa ingen egen betydelse) "
    "och 'atbart lockbete (pa krok) vid fiske'. Tva sanna betydelser, vilket ar "
    "vad kortet har. SAOL bekraftar samma tvadelning.",
 },
 "dager": {
  "betydelse_kan_saknas":
    "SO-LEMMA dager har EN definition ('(naturligt) ljus som inte utgors av "
    "direkt solstralning') och TRE underbetydelser, ALLA markta '(ingen egen "
    "definition -- utvidgning)' i rastrukturen -- de raknas darfor inte som "
    "betydelser. Kortets tre rader kommer i stallet fran SAOL, vars led ar "
    "semikolonseparerade och alltsa ar riktiga betydelser: 'dagsljus; belysning; "
    "ljuseffekt'. Kortet ligger med tre betydelser alltsa OVER det rastrukturen "
    "kraver, inte under; flaggan raknar sammandragets utplattade lista.",
 },
 "mola": {
  "betydelse_kan_saknas":
    "SO-LEMMA mola har EN definition ('ihallande smavarka') och EN underbetydelse "
    "markt '(ingen egen definition -- utvidgning)' -- det ar den bildliga "
    "anvandningen (SO:s syntex 'en molande kansla av tomhet'), som saknar egen "
    "definitionstext och darfor inte ar en andra betydelse. SAOL har ocksa bara "
    "ett led ('smavarka'). En betydelse ar ratt.",
 },
}

poster = json.load(io.open(FIL, encoding="utf-8"))
ng = nh = nr = nt = 0
for e in poster:
    o = e["ord"]
    pr = e.get("proposed")
    if not pr:
        continue
    if o in GRP:
        pr["synonym_groups"] = GRP[o]
        pr["synonymer"] = [s for g in GRP[o] for s in g]
        ng += 1
    if o in HB:
        pr["huvudbetydelse"] = HB[o]
        nh += 1
    if o in REG:
        pr["register"] = REG[o]
        nr += 1
    if o in T:
        e["forgranska_tillat"] = T[o]
        nt += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("synonymgrupper: %d, huvudbetydelser: %d, register: %d, tillat: %d"
      % (ng, nh, nr, nt))
