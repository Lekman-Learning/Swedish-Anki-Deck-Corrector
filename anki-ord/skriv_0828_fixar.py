# -*- coding: utf-8 -*-
"""Omskrivning av de 5 underkanda korten ur batch 2026-08-28.

Blindgranskaren hade ratt pa alla fem. Kontrollerat mot SO:s och SAOL:s
RASTRUKTUR (huvudbetydelser/underbetydelser i uppslag/*.json), inte mot
slaupp.py:s sammandrag -- det var sammandraget som vilseledde mig pa 'pur',
dar det visade 'ren och oforfalskad | mycket' medan SO i sjalva verket bara
har EN huvudbetydelse for adjektivet.
"""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-28_v3-batch.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
KALLA = ("SO och SAOL via https://svenska.se/api/msearch?ord=%s "
         "(omhamtat 2026-08-28, HTTP 200; radstrukturen last direkt ur "
         "huvudbetydelser/underbetydelser)")
B = '<font color="#3498db">%s</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, grupper=None, tillat=None,
         conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": grupper, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": KALLA % urllib.parse.quote(o),
                    "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("gigolo",
     "Man som mot betalning dansar med kvinnliga gäster på hotell och "
     "restauranger ; man som mot betalning är älskare åt rika kvinnor",
     "neutral, neutral ; neutral, lätt negativ",
     [],
     "Han jobbade som " + B % "gigolo" + " på hotellets danssalong.",
     None,
     "UNDERKAND 2026-08-28, granskaren hade RATT. SO ger tva skilda "
     "betydelser: 'man som mot betalning dansar med kvinnliga gaster' och "
     "'av. om man som mot betalning ar alskare till (rika) kvinnor'. SAOL "
     "bekraftar bada: 'yrkesdansor pa restaurang; man som lever pa rika "
     "kvinnor'. Forsta versionen slog ihop dem med 'eller' ('dansar med "
     "eller ar sallskap at'), vilket enligt regeln alltid ar fel vid skilda "
     "betydelser -- de ska separeras med ' ; '. Dessutom var 'sallskap at' "
     "en eufemism som suddade ut att betydelse tva handlar om ett SEXUELLT "
     "forhallande mot betalning. Bada felen rattade.")

satt("homograf",
     "Ord som stavas precis som ett annat ord men uttalas eller böjs "
     "annorlunda — och oftast betyder något helt annat",
     "fackspråklig, neutral, lingvistik",
     [],
     "Att 'tomten' kan vara både en gubbe och en markbit gör ordet till en "
     + B % "homograf" + ".",
     "→ Grekiska homos 'samma' och graphein 'skriva' — jämför homofon, där "
     "fon betyder ljud.",
     "UNDERKAND 2026-08-28, granskaren hade RATT -- men bara delvis av det "
     "skal som angavs, sa kallorna ar omlasta. SO:s definition ar smal och "
     "namner INTE uttal: 'ord (lemma) som stavas likadant som visst annat'. "
     "SAOL daremot ger i sin exempelparafras 'ord som skrivs pa samma satt "
     "men har olika uttal el. bojning och ofta helt olika betydelse', och "
     "Wiktionary sager 'stavas som ett annat ord, men som uttalas "
     "annorlunda'. Tva av tre kallor stracker alltsa ut kriteriet till "
     "uttal/bojning. Utan det skulle rena homonymer (samma stavning OCH "
     "samma uttal) felaktigt raknas som homografer -- och det ar precis den "
     "gransdragningen HP provar. Tillagt. homofon och homonym ar fortsatt "
     "INTE inskrivna som synonymer: SO listar dem som JFR:cohyponym.")

satt("membran",
     "Tunn, böjlig hinna — i kroppen eller i en apparat, till exempel en "
     "högtalare",
     "neutral, neutral, allmän",
     ["hinna"],
     "Högtalarens " + B % "membran" + " vibrerade så att man kunde se det.",
     None,
     "UNDERKAND 2026-08-28, granskaren hade RATT. SO ger EN betydelse: 'tunn "
     "(elastisk) hinna' -- den tacker bade organiska och tillverkade "
     "membran. SAOL: 'tunn hinna'. Forsta versionen taggade registret med "
     "domanen 'biologi' trots att exempelmeningen ar en hogtalare, alltsa "
     "teknik: domantaggen motsade kortets eget exempel. Rattat till "
     "'allman', som ar den bedomda men fackomradeslosa varden. "
     "Huvudbetydelsen sa ocksa 'som skiljer tva sidor at' -- det star i "
     "ingen kalla och stammer inte pa ett hogtalarmembran. Struket.")

satt("pur",
     "Ren och oblandad — står nästan alltid framför ett känsloord: av pur "
     "glädje, av pur nyfikenhet",
     "neutral, neutral",
     [],
     "De frågade av " + B % "pur" + " nyfikenhet.",
     None,
     "UNDERKAND 2026-08-28, granskaren hade RATT och jag hade fel av ett "
     "skal varr att skriva ut: jag las slaupp.py:s SAMMANDRAG, som visade "
     "'ren och oforfalskad | mycket' och tva olika belaggsartal, och drog "
     "slutsatsen att SO har tva betydelser. Rastrukturen i "
     "uppslag/pur.json visar att SO har EXAKT EN huvudbetydelse for "
     "adjektivet: 'ren och oforfalskad'. SAOL likasa: 'ren, oforfalskad'. "
     "Den andra 'betydelsen' var alltsa ingen betydelse utan en "
     "anvandningsnot om var ordet brukar sta. Kortet ger nu en betydelse "
     "med den noten inbakad. LARDOM: sammandraget slar ihop poster och far "
     "en anvandningsnot att se ut som en egen betydelse -- las "
     "huvudbetydelser/underbetydelser direkt nar antalet betydelser ar det "
     "som star pa spel.")

satt("täcka",
     "Lägga något över en yta så att den döljs ; breda ut sig över hela "
     "ytan ; räcka till för en kostnad ; skydda med militära medel ; vara "
     "på plats och rapportera om något ; i lagsport: hålla noga uppsikt "
     "över en motståndare",
     "neutral, neutral ; neutral, neutral ; neutral, neutral ; "
     "fackspråklig, neutral, militär ; fackspråklig, neutral ; "
     "vardaglig, neutral, sport",
     [],
     "Hon " + B % "täckte" + " bordet med en duk innan gästerna kom.",
     None,
     "UNDERKAND 2026-08-28, granskaren hade RATT -- och det ar deckets "
     "dominerande fel: hela betydelser som saknas. Rastrukturen i "
     "uppslag/tacka.json visar att SO har SEX huvudbetydelser: (1) 'lata "
     "(nastan) hela ytan av (nagot) doljas under eller bakom', (2) 'breda "
     "ut sig over (nastan) hela ytan av', (3) 'ha eller ge (nagot) "
     "tillracklig omfattning for att motsvara', (4) 'skydda med militara "
     "medel', (5) 'vara narvarande vid (nagot) for att skildra', (6) 'halla "
     "(nagon) under sarskild uppsikt' (vardagligt). SAOL:s exempelrad "
     "bekraftar fyra av dem direkt: 'tacka bordet med en duk', 'snon tackte "
     "marken', 'tacka atertaget', 'tacka ett evenemang (om journalist)'. "
     "Forsta versionen hade bara tre och bad om undantag for resten -- "
     "undantaget var inte befogat. Alla sex star nu pa kortet. "
     "⚠️ AVGRANSNING kvarstar: SAOL:s rad 'vacker, natt' hor till "
     "adjektivet TACK, ett annat uppslagsord, och ar fortsatt utelamnad.")

# Det gamla undantaget gallde en version med tre betydelser och ar inte
# langre sant -- ta bort det sa det inte hanger kvar som en tyst ursakt.
BY["täcka"].pop("forgranska_tillat", None)

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Skrev om %d kort." % 5)
