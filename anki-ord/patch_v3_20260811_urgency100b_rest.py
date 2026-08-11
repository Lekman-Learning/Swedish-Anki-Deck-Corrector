# -*- coding: utf-8 -*-
"""De 18 kort som `applicera` stoppade i urgency100b — tre skilda fel.

## 1. Flerordsuppslag bröt sökkollens URL (5 kort)

`slå dank`, `alla taggar utåt`, `svara för`, `lända till`, `gå upp i limningen`
hämtades allihop av `slaupp.py` (bevisraderna finns i sessionen), men `kalla`
skrevs med RÅTT MELLANSLAG: `...?ord=slå dank`. `sokkoll_verifiering._URL_RE`
plockar URL:er med `[^\\s...]+` och klippte därför strängen vid mellanslaget —
kortet hänvisade till uppslaget `slå`, som aldrig hämtats, och Hål 0 sa
korrekt "hämtningen gjordes aldrig".

Rättningen är att procentkoda ordet. `_normalisera` kör `unquote` på båda
sidor, så `%20` och mellanslag jämförs som samma sträng — kanonisering, inte
uppmjukning. Kravet på en verklig hämtning är oförändrat.

`gå upp i limningen` byter dessutom källa: svenska.se MISSLYCKADES för det
ordet (idiomet är inte uppslagsord i någon av de tre ordböckerna), medan
synonymer.se gav HTTP 200. Kortet måste hänvisa till den hämtning som faktiskt
lyckades, inte till den som inte gjorde det.

## 2. Exempelmeningen saknade markering (12 kort)

Alla tolv är meningar JAG skrev om i urgency100b — de gamla var fragment
(`Fyllig barm.`), trasig grammatik (`Uppgiften härröra från...`) eller
saknade mellanslag (`Halvkvädnamedgivanden.`). Jag skrev prosan men glömde
`<font color="#3498db">`-märkningen runt ordet, som är en HÅRD Adam-tal-regel.

Värt att notera: spärren tog varenda en. Ett formatfel som hade sluppit in
tyst i det gamla flödet stoppade nu skrivningen.

## 3. puffa: fyra betydelser, två synonymgrupper

Jag utökade `puffa` från två betydelser till fyra (SO har fem) men lät
synonymgrupperna ligga kvar på två. Kortet hade då renderat två betydelser
utan synonymer. Grupperna byggs om till fyra, en per betydelse.
"""

import json
import sys
import urllib.parse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SESSION = "sessions/session_2026-08-11_v3-omgranskning.json"
FARG = "#3498db"


def h(ord_):
    return f'<font color="{FARG}">{ord_}</font>'


# --- 1. Procentkodad kalla för flerordsuppslag ---------------------------
SVENSKA = "https://svenska.se/api/msearch?ord={}"
SYNONYMER = "https://www.synonymer.se/sv-syn/{}"

NY_KALLA = {
    "slå dank": SVENSKA.format(urllib.parse.quote("slå dank")),
    "alla taggar utåt": SVENSKA.format(urllib.parse.quote("alla taggar utåt")),
    "svara för": SVENSKA.format(urllib.parse.quote("svara för")),
    "lända till": SVENSKA.format(urllib.parse.quote("lända till")),
    # Byter källa: svenska.se misslyckades, synonymer.se gav HTTP 200.
    "gå upp i limningen": SYNONYMER.format(urllib.parse.quote("gå upp i limningen")),
}

# --- 2. Exempelmeningar med korrekt markering ---------------------------
EXEMPEL = {
    "toujours": f"Värden var {h('toujours')} och fick alla gäster att känna sig hemma.",
    "barm": f"Hon gömde brevet vid sin {h('barm')} så att ingen skulle hitta det.",
    "förflugen": f"Ett {h('förfluget')} ord på festen ställde till med skandal.",
    "härröra": f"Uppgiften {h('härrör')} från en säker källa inom myndigheten.",
    "flyhänt": f"Översättningen var {h('flyhänt')} men missade textens allvar.",
    "amfora": f"I graven låg en spräckt {h('amfora')} med en bild på Akilles.",
    "pryd": f"Hon var för {h('pryd')} för att ens uttala ordet.",
    "belägenhet": (f"Han hamnade i en svår {h('belägenhet')} när både bilen och "
                   f"telefonen gick sönder."),
    "obscen": (f"Han tyckte att direktörernas {h('obscena')} bonusar var ett hån "
               f"mot de anställda."),
    "prominent": f"Mannen på porträttet kändes igen på sin {h('prominenta')} haka.",
    "halvkväden": (f"Regeringens {h('halvkvädna')} kritik av diktaturen "
                   f"övertygade ingen."),
    "sumpa": f"Han {h('sumpade')} en given målchans i den sista minuten.",
    # Skrevs om i urgency100b (den gamla var grammatiskt trasig) men missades
    # i första omgången här -- samma glömda markering som de tolv ovan.
    "lända till": (f"Den nya lagen {h('lände till')} stora förändringar "
                   f"i samhället."),
}

# --- 3. puffa: en synonymgrupp per betydelse ----------------------------
PUFFA_GRUPPER = [
    ["ryka i stötar", "pysa"],
    ["knuffa", "putta"],
    ["mana på", "pusha"],
    ["göra reklam för", "lyfta fram"],
]


def main():
    poster = json.load(open(SESSION, encoding="utf-8"))
    n_kalla = n_ex = n_grupp = 0

    for p in poster:
        o = p["ord"]
        if o in NY_KALLA:
            p["sokkoll"]["kalla"] = NY_KALLA[o]
            n_kalla += 1
        if o in EXEMPEL:
            p["proposed"]["exempelmening"] = EXEMPEL[o]
            n_ex += 1
        if o == "puffa":
            p["proposed"]["synonym_groups"] = PUFFA_GRUPPER
            p["proposed"]["synonymer"] = [s for g in PUFFA_GRUPPER for s in g]
            n_grupp += 1
        p.pop("applicerad", None)

    json.dump(poster, open(SESSION, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Nya kallor: {n_kalla}. Nya exempelmeningar: {n_ex}. "
          f"Omgjorda synonymgrupper: {n_grupp}.")
    for o, k in NY_KALLA.items():
        print(f"  {o:<20} -> {k}")


if __name__ == "__main__":
    main()
