# -*- coding: utf-8 -*-
"""V3-omgranskning av 50 is:review-kort, urgency-rankade (2026-08-11).

Sökkoll körd i transkriptet samma session (`slaupp_batch50.txt`): 50 ord,
samtliga med uppslagsordsträff utom `ytong`, som pausats separat.

RATTELSER: de kort där källorna säger något annat än kortet. Var och en har
en motivering som pekar på VILKEN källa och VAD den säger -- inte "SO säger
så", utan den formulering skillnaden hänger på.

OFORANDRADE: resten. De jämfördes mot SO/SAOL/synonymer.se och stämde. De
skrivs ändå om via apply_card(), eftersom v3-taggen ska betyda "sökkollad i
den här sessionen" -- ett kort som hoppas över ser annars ut som ett kort
ingen tittat på.
"""

import json
import sys

import apply_flerbetydelse
import config
from ankiconnect import invoke

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SESSION = "sessions/session_2026-08-11_v3-omgranskning-repetition2.json"
KALLA = "https://svenska.se/api/msearch?ord={}"

# ord -> {falt att ANDRA} + "_skal"
RATTELSER = {
    "förskingra": {
        "huvudbetydelse": "Olovligen förbruka egendom man anförtrotts ; slösa bort",
        "synonymer": ["försnilla", "undansnilla", "förslösa"],
        "_skal": "SO: 'utnyttja (och förslösa) EGENDOM som man förfogar över men som "
                 "tillhör någon annan' -- kortet sa 'pengar'. SO har dessutom en andra "
                 "betydelse 'slösa bort' som saknades helt.",
    },
    "författning": {
        "huvudbetydelse": "Samling rättsliga bestämmelser om hur ett land styrs ; "
                          "enskild lag eller förordning",
        "synonymer": ["grundlag", "konstitution", "förordning", "lagbestämmelse"],
        "_skal": "SO ger fyra betydelser; kortet hade bara den första. Den andra -- "
                 "'enskild lag, förordning eller annan rättslig föreskrift' -- är den "
                 "vardagliga juridiska. OLD-facit sa 'lagbestämmelse', alltså hade det "
                 "gamla facit rätt och kortet fel.",
    },
    "löje": {
        "huvudbetydelse": "Dämpad munterhet som uttrycker ringaktning",
        "synonymer": ["ringaktande munterhet", "spe", "hån"],
        "_skal": "SO: 'DÄMPAD munterhet som uttrycker ringaktning'. Kortet sa 'förakt "
                 "uttryckt genom skratt' -- löje är just inte högljutt skratt.",
    },
    "mynna": {
        "huvudbetydelse": "Leda fram till och öppna sig ; resultera i",
        "synonymer": ["rinna ut", "utmynna", "resultera"],
        "_skal": "SAOL har 'resultera' och SO 'föra' som egna betydelser. Den bildliga "
                 "användningen (mynna ut i) är den vanligaste och saknades.",
    },
    "beständig": {
        "huvudbetydelse": "Som bibehåller sina egenskaper trots påfrestningar ; ständig",
        "synonymer": ["varaktig", "bestående", "oavbruten"],
        "_skal": "SO ger 'ständig' som egen betydelse (beständig oro). Kortet hade bara "
                 "hållbarhetsbetydelsen.",
    },
    "löga": {
        "huvudbetydelse": "Tvätta ; bada",
        "synonymer": ["tvätta", "bada", "tvaga"],
        "_skal": "SO: 'tvätta | bada' -- två betydelser, kortet hade en.",
    },
    "ohägn": {
        "huvudbetydelse": "Lättare besvär ; skada eller åverkan",
        "synonymer": ["förtret", "obehag", "åverkan"],
        "_skal": "SAOL: 'skada; förtret'. Skadebetydelsen saknades och stöds av "
                 "etymologin ('skadat eller nedfallet stängsel').",
    },
    "särk": {
        "huvudbetydelse": "Underplagg för överkroppen, buret närmast kroppen",
        "_skal": "SO: 'typ av (kvinno)underplagg för ÖVERKROPPEN'. Kortet sa 'fotsitt', "
                 "alltså fel plagglängd.",
    },
    "jenka": {
        "huvudbetydelse": "Finsk dans med ett steg framåt, ett bakåt och tre framåt ; "
                          "musiken till dansen",
        "synonymer": ["finsk sällskapsdans", "dansmusik"],
        "_skal": "SO beskriver stegen exakt; kortet sa bara 'hopprörelser framåt och "
                 "bakåt'. SAOL har dessutom musiken som egen betydelse.",
    },
    "gräfta": {
        "huvudbetydelse": "Hacka jord med flåhacka",
        "synonymer": ["hacka", "flåhacka"],
        "_skal": "Kortet definierade ett SUBSTANTIV ('äldre verktyg') men "
                 "exempelmeningen använde ordet som VERB ('gräfta upp jorden') -- "
                 "kortet motsade sig självt. SAOL ger 'flåhacka'.",
    },
    "släntra": {
        "huvudbetydelse": "Gå nonchalant och till synes utan mål",
        "synonymer": ["strosa", "driva", "flanera"],
        "_skal": "SO: 'gå NONCHALANT och till synes utan mål'. Kortet sa 'gå långsamt "
                 "utan brådska' -- betoningen ligger på likgiltigheten, inte farten.",
    },
    "ragu": {
        "huvudbetydelse": "Stuvning på kött i småbitar ; äv. på fisk",
        "synonymer": ["köttstuvning", "gryta", "frikassé"],
        "_skal": "SO: 'typ av köttstuvning', SO+ 'äv. om vissa fiskstuvningar'. Kortet "
                 "la till grönsaker och kryddor som ingen källa nämner, och missade fisk.",
    },
    "sammandrag": {
        "huvudbetydelse": "Förkortad framställning som framhäver det viktiga ; "
                          "turnering där lag möts på samma plats",
        "synonymer": ["resumé", "referat", "kortversion"],
        "_skal": "SAOL har en andra betydelse: 'en spelform inom t.ex. fotboll'.",
    },
    "eluvial": {
        "huvudbetydelse": "Som utsatts för urlakning, utfällning eller vittring på platsen",
        "_skal": "SO: 'urlakning, utfällning ELLER vittring'. Kortet nämnde bara vittring.",
    },
    "anskri": {
        "huvudbetydelse": "Plötsligt, häftigt skrik",
        "_skal": "SO: 'häftigt skrik', SAOL 'plötsligt skri'. Kortet la till 'av rädsla "
                 "eller förskräckelse', vilket ingen källa begränsar det till.",
    },
}


def main():
    poster = json.load(open(SESSION, encoding="utf-8"))
    skrivna, hoppade, fel = 0, 0, []

    for p in poster:
        ord_ = p["ord"]
        L = p["legacy"]
        r = RATTELSER.get(ord_, {})
        try:
            apply_flerbetydelse.apply_card(
                note_id=p["noteId"],
                huvudbetydelse=r.get("huvudbetydelse", L.get("huvudbetydelse")),
                synonymer=r.get("synonymer", L.get("synonymer")),
                synonym_groups=r.get("synonym_groups", L.get("synonym_groups")),
                exempelmening=r.get("exempelmening", L.get("exempelmening") or ""),
                register=r.get("register", L.get("register")),
                bild_html=L.get("bild_html"),
                etymologi=r.get("etymologi", L.get("etymologi")),
                ord_=ord_,
                mode="sokkoll",
                escalated=True,
                kalla=KALLA.format(ord_),
            )
            skrivna += 1
            if r:
                print(f"  RATTAT   {ord_}")
            else:
                hoppade += 1
        except Exception as e:
            fel.append((ord_, str(e)[:140]))
            print(f"  FEL      {ord_}: {str(e)[:140]}")

    print(f"\nSkrivna: {skrivna}/{len(poster)}  "
          f"(rattade: {skrivna - hoppade}, oforandrade: {hoppade})")
    if fel:
        print(f"MISSLYCKADE: {len(fel)}")
        for o, e in fel:
            print(f"  {o}: {e}")


if __name__ == "__main__":
    main()
