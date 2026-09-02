# -*- coding: utf-8 -*-
"""Rattar batch A (kort 0-17) mot forgranskas FAKTISKA synonymregel.

Felet: synonymerna togs fran synonymer.se. Den kallan raknas INTE som
ordboksbelagg -- bara SO:s SYN-falt och SO/SAOL:s definitionstext gor det.
13 av 18 kort fick synonym_utan_ordboksbelagg. Tom synonymlista ar godkant
och ar normalfallet (69 % av korten), sa dar ingen belagd synonym finns
lamnas listan tom i stallet for att fyllas med nagot som later rimligt.

Poolen per ord las ut med _pool.py, som anropar forgranskas egna funktioner
i stallet for att aterimplementera regeln.
"""
import io, json, sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02_v3-batch.json"

# ord -> (synonymer, synonym_groups)
SYN = {
 "absolvera":   (["fullborda", "avsluta", "ge syndaförlåtelse"],
                 [["fullborda", "avsluta"], ["ge syndaförlåtelse"]]),
 "sanslös":     ([], None),
 "bylsig":      ([], None),
 "coupe":       (["efterrätt", "glassefterrätt"], None),
 "digna":       (["sjunka samman", "svikta"], None),
 "endokrin":    (["inresekretorisk", "insöndrande"], None),
 "essens":      ([], None),
 "expenser":    (["omkostnader", "utlägg", "små utgifter"], None),
 "fiskal":      (["fiskalisk", "jurist som genomgår domarutbildning"], None),
 "habil":       (["duglig", "kompetent", "skicklig"], None),
 "hypotetisk":  ([], None),
 "kont":        (["enkel ryggsäck", "korg"], None),
 "lisma":       (["fjäska", "ställa sig in"], None),
 "periferisk":  (["perifer"], None),
 "sakral":      (["religiös", "högtidlig"], None),
 "saltomortal": (["frivolt", "halsbrytande luftsprång"], None),
 "serum":       ([], None),
 "spisa":       (["äta", "lyssna på", "avvisa", "avfärda"], None),
}

# hypotetisk far en andra betydelse i stallet for en motivering: SO:s def 2 ar
# en akta huvudbetydelse, inte brus.
NY_HB = {
 "hypotetisk": "Som bygger enbart på ett antagande och inte på något känt "
               "faktum ; som gäller bara om vissa förutsättningar uppfylls",
}

TILLAT = {
 "absolvera": {"betydelse_kan_saknas":
   "SO raknar 4, men de tva underbetydelserna ar 'spec. om att avlagga examen' "
   "och 'spec. av.' -- den forsta ar en tillampning av fullborda och ryms i "
   "kortets forsta betydelse, den andra ar en tom markor utan definition. "
   "Kortets tva betydelser (fullborda / ge syndaforlatelse) motsvarar SO:s tva "
   "riktiga def."},
 "sanslös": {"betydelse_kan_saknas":
   "SO:s fjarde post ar underbetydelsen 'av. allmant (ofta positivt) "
   "forstarkande', vilket ar en anvandning av kortets tredje betydelse "
   "('fullkomligt meningslos' -> 'sanslost bra'), inte en fjarde betydelse. "
   "De tre huvudbetydelserna star pa kortet."},
 "coupe": {"betydelse_kan_saknas":
   "SO:s tva extra poster ar 'best. form' och 'plural' -- rena grammatiska "
   "etiketter, inte betydelser. Ordet har en betydelse."},
 "digna": {"betydelse_kan_saknas":
   "SO har en def plus tva bildliga utvidgningar; kortet tar bada de "
   "sarskiljbara ('sjunka ihop under borda' och overflodsbetydelsen). Den "
   "tredje posten ar 'av. bildligt' utan egen definition."},
 "essens": {
  "betydelse_kan_saknas":
   "SO:s 7 poster ar fororenade av lemmat ESS: 'spelkort med hogsta varde' och "
   "'ha en overraskning i beredskap' tillhor ess, inte essens. Detsamma galler "
   "SAOL-raderna om 'tonen e sankt' och 'det hogsta kortet i en farg'. Essens "
   "egna betydelser ar tva, och bada star pa kortet.",
  "frammande_uppslagsord":
   "Det frammande uppslagsordet ar 'ess'. Samtliga glosor och betydelser fran "
   "ess ar aktivt uteslutna ur kortet -- se sokkollens slutsats."},
 "habil": {"betydelse_kan_saknas":
   "SO:s andra post ar underbetydelsen 'av. om handling och dylikt', dvs. samma "
   "betydelse tillampad pa en handling i stallet for en person. Kortets "
   "huvudbetydelse ar formulerad sa att den tacker bada."},
 "hypotetisk": {"betydelse_kan_saknas":
   "SO:s tredje post ar markoren 'spec.' utan egen definition. Kortet bar bada "
   "SO:s riktiga huvudbetydelser."},
 "sakral": {"betydelse_kan_saknas":
   "SO:s andra post ar 'MOTSATS:antonym', en relationsmarkor och inte en "
   "betydelse. Ordet har en betydelse."},
 "saltomortal": {"betydelse_kan_saknas":
   "SO:s andra post ar 'av. bildligt, sarsk. om aventyrligt resonemang' -- en "
   "bildlig anvandning av samma hopp, inte en andra betydelse. Utelamnas "
   "medvetet: kortet ska lara ut grundbetydelsen."},
 "serum": {"betydelse_kan_saknas":
   "SO raknar 4: tva def plus underbetydelserna 'el.' (tom markor) och 'sarsk. "
   "om blodvatska befriad fran blodkroppar, anv. vid medicinsk behandling'. "
   "Den sista ar lakemedelsbetydelsen, som star som kortets andra betydelse "
   "med stod av SAOL:s egen huvudbetydelse. Kortets tre betydelser tacker "
   "alltsa SO:s fyra poster."},
 "spisa": {"betydelse_kan_saknas":
   "SO:s fjarde post ar 'av. bildligt' utan egen definition. Kortets tre "
   "betydelser motsvarar SO:s tre def och SAOL:s tre huvudbetydelser."},
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = s = t = 0
for e in poster:
    o = e["ord"]
    if o in SYN:
        syn, grp = SYN[o]
        e["proposed"]["synonymer"] = syn
        e["proposed"]["synonym_groups"] = grp
        s += 1
    if o in NY_HB:
        e["proposed"]["huvudbetydelse"] = NY_HB[o]
        n += 1
    if o in TILLAT:
        e.setdefault("forgranska_tillat", {}).update(TILLAT[o])
        t += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("synonymer rattade: %d | huvudbetydelser: %d | motiveringar: %d" % (s, n, t))
tomma = [o for o, (sy, _) in SYN.items() if not sy]
print("tom synonymlista (godkant, normalfallet): %s" % ", ".join(tomma))
