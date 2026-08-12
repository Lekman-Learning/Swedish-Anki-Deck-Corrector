# -*- coding: utf-8 -*-
"""Rättningar för 30 is:new-kort (2026-08-12, andra omgången).

**25 av de 30 är gårdagens underkända kort.** De är suspenderade `is:new` utan
full v3, alltså exakt `kortbyggare.py`s urvalskriterium — de kommer tillbaka av
sig själva tills de blir rätt. Det är en bättre batch än 30 slumpade, för nu
finns granskarens exakta motivering att rätta mot i stället för min gissning.

Fem är nya: `agglomerera`, `antibiotika`, `autonom`, `infiltration`, `pläd`.

## Det återkommande felet, nu med ett namn

`affix` underkändes för att *förstavelse* och *ändelse* är **hyponymer** —
underordnade specialfall, inte utbytbara synonymer. Samma fel finns i ett av
de nya korten: `antibiotika` hade *penicillin*, som är ETT SLAGS antibiotikum.

Det är samma familj som `härk`/*rentjur* (hyperonym — en rentjur behöver inte
vara kastrerad), `kardinal`/*kardinalbiskop* (en av tre rangklasser) och
`hedonism`/*lyckofilosofi* (SO skiljer uttryckligen hedonism från eudemonism).

**Testet som fångar alla fyra:** en synonym får varken vara snävare eller
vidare än ordet. Om den ena kan vara sann när den andra är falsk är det ingen
synonym.

## Varför den automatiska relationskontrollen INTE kunde göra jobbet

SO taggar faktiskt varje korshänvisning: `JFR:hyponym`, `JFR:cohyponym`,
`MOTSATS:antonym`. Jag byggde en regel på det och **backtestade bort den**:

* `JFR:cohyponym` (1204 förekomster) är för löst använt — regeln underkände
  `girig`/*snål*, `grossist`/*grosshandlare* och `bleke`/*stiltje*, där ordet
  ifråga är SAOL:s EGEN gloss. 27 träffar, 7 relevanta.
* `JFR:hyponym` (23 förekomster) är precis men matchar inte — SO länkar till
  *prefix*, medan kortet skriver *förstavelse*. Noll träffar.

Slutsatsen är att taggarna duger som **underlag för mitt omdöme**, inte som
spärr. `forgranska.py` behåller därför bara de tre precisa taggarna som
skyddsnät, och `JFR:cohyponym` som ren information.

## Vad granskaren fångade utöver synonymerna

* **`depression`** — exemplet sa att Döda havet når 392 m under havsytan.
  Det är runt 422 m idag, och sjunker. Sakfel som suttit i kortet hela tiden.
* **`accession`** — kortet ledde med den betydelse SO märker *mindre brukligt*
  (traktatanslutning) och lade den vanliga (tillskott till en samling) sist.
* **`aristokratisk`** — "utmärker ELLER hör till" satte *eller* mellan två
  skilda betydelser. Där ska ` ; ` stå.
* **`komma för`** — exemplet saknade hjälpverb: "att han sett" ska vara
  "att han hade sett".
* **`övlig`** — registret säger *ironisk*, men exemplet var helt sakligt.
* **`förmäla`** — registerleden satt omkastade mot betydelserna.
* **`oratorium`** och **`stilisera`** — betydelser jag lade till som SO inte
  har. Bönsalen är oratoriums ETYMOLOGI, inte en levande betydelse.
* **`entente`** — etymologin sa "inte ett bindande förbund", synonymlistan sa
  *statsförbund*. Kortet motsade sig självt.

## Framsidor som inte rättas här

`loafer` (SO har bara `loafers`) står kvar — framsidan är Adams beslut, och
`loafers` finns inte som kort så det blir ett rent namnbyte. `antibiotika`
lämnas som det är: SAOL:s uppslagsord är `antibiotikum`, men `antibiotika` är
den form som faktiskt används, precis som `pellets`.
"""

import json
import sys
import urllib.parse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FARG = "#3498db"
SVENSKA = "https://svenska.se/api/msearch?ord={}"
SESSION = "sessions/session_2026-08-12_v3-omgranskning-nya.json"


def h(o):
    return f'<font color="{FARG}">{o}</font>'


DOMAN = {
    "agglomerera": "teknik", "depreciera": "ekonomi", "entente": "politik",
    "kalibrera": "teknik", "sint": "allmän", "accession": "allmän",
    "brikett": "teknik", "depression": "allmän", "kardinal": "religion",
    "konstruktivism": "konst", "näver": "allmän", "oratorium": "musik",
    "receptarie": "medicin", "övlig": "allmän", "affix": "lingvistik",
    "antibiotika": "medicin", "aristokratisk": "historia", "autonom": "politik",
    "curare": "medicin", "förmäla": "allmän", "hedonism": "filosofi",
    "härk": "biologi", "infiltration": "allmän", "komma för": "allmän",
    "loafer": "allmän", "manisk": "psykologi", "pläd": "allmän",
    "runda ord": "allmän", "snuthäck": "allmän", "stilisera": "konst",
}

RATTELSER = {
    # ---------- Synonymen var snävare eller vidare än ordet ----------
    "affix": {
        "synonymer": [],
        "_skal": "SO taggar infix/prefix/suffix som JFR:hyponym — underordnade "
                 "specialfall. Kortets 'förstavelse' (=prefix) och 'ändelse' "
                 "(=suffix) är alltså snävare än affix, som även rymmer infix. "
                 "Affix har ingen svensk synonym; listan lämnas TOM enligt Adams "
                 "beslut 2026-08-12 att hellre lämna tomt än hitta på.",
    },
    "antibiotika": {
        "synonymer": ["bakteriedödande medel"],
        "_skal": "'Penicillin' ströks — det är ETT SLAGS antibiotikum, alltså en "
                 "hyponym, exakt samma fel som affix/förstavelse. Notera att "
                 "SAOL:s uppslagsord är singularformen 'antibiotikum'; "
                 "'antibiotika' behålls som framsida eftersom det är den form som "
                 "faktiskt används.",
    },
    "hedonism": {
        "synonymer": ["njutningslära", "njutningsevangelium"],
        "_skal": "'Lyckofilosofi' ströks. SO skiljer uttryckligen hedonism "
                 "(njutning som mål) från EUDEMONISM (lycka och välbefinnande som "
                 "mål) — närliggande riktningar, inte samma.",
    },
    "härk": {
        "synonymer": ["renoxe", "kastrerad rentjur"],
        "_skal": "'Rentjur' ströks: en rentjur är en normalt intakt hanren. "
                 "Kastreringen är hela poängen med ordet, så synonymen var vidare "
                 "än uppslagsordet. OLD-facits 'renoxe' fångar nyansen.",
    },
    "kardinal": {
        "synonymer": ["prelat", "fältsparv", "grundläggande", "väsentlig"],
        "synonym_groups": [["prelat"], ["fältsparv"],
                           ["grundläggande", "väsentlig"]],
        "_skal": "'Kardinalbiskop' ströks — det är en av TRE rangklasser "
                 "(kardinalbiskop/kardinalpräst/kardinaldiakon), alltså en "
                 "hyponym, inte en synonym till titeln i allmänhet.",
    },
    "receptarie": {
        "synonymer": ["farmaceut"],
        "_skal": "'Apotekare med kandidatexamen' är en självmotsägelse: apotekare "
                 "kräver 5-årig masterexamen, receptarie är en egen kortare "
                 "yrkesexamen på kandidatnivå. Två legalt reglerade titlar som "
                 "inte går att slå ihop. 'Farmaceut' är det överordnade ordet som "
                 "täcker båda och står i syn.se.",
    },
    "snuthäck": {
        "synonymer": ["polisbil", "polisstation"],
        "synonym_groups": [["polisbil"], ["polisstation"]],
        "_skal": "'Polispiket' ströks: SO ger piket som 'polis- eller truppstyrka "
                 "i beredskap' — alltså MÄNNISKOR, inte ett fordon. Inte utbytbart "
                 "mot en polisbil.",
    },
    "kalibrera": {
        "synonymer": ["fininställa", "finjustera", "justera"],
        "_skal": "'Nollställa' ströks — att nollställa är att sätta instrumentet "
                 "till noll, medan kalibrering är att jämföra mot en känd referens "
                 "i flera punkter över skalan. SO:s egna näraliggande ord är "
                 "'fininställa' och 'finjustera'.",
    },
    "näver": {
        "synonymer": ["björkbark"],
        "_skal": "'Björknäver' innehåller uppslagsordet och avslöjar svaret. "
                 "Regeln cirkular_synonym är hård sedan 2026-08-12.",
    },
    "brikett": {
        "synonymer": ["sammanpressat stycke"],
        "_skal": "Både 'fyrkantig bit' och 'kolbit' var fel: briketter är ofta "
                 "runda eller cylindriska (grillbriketter), och materialet kan "
                 "enligt både SO och SAOL vara pulver ELLER fiber — torv, sågspån, "
                 "inte bara kol.",
    },
    "entente": {
        "synonymer": ["samförstånd", "vänskapsförbindelse"],
        "_skal": "'Statsförbund' ströks. Kortet motsade sig självt: etymologin "
                 "slår fast att en entente INTE är ett bindande förbund, medan "
                 "synonymen påstod precis en förbundsbildning.",
    },

    # ---------- Saknade eller felordnade betydelser ----------
    "depreciera": {
        "huvudbetydelse": "Minska värdet av något, skriva ned en valutas värde ; "
                          "i vidare bemärkelse: sjunka i värde",
        "synonymer": ["skriva ned", "devalvera", "sjunka i värde"],
        "synonym_groups": [["skriva ned", "devalvera"], ["sjunka i värde"]],
        "exempelmening": f"Riksbanken lät kronan {h('depreciera')} för att stärka "
                         f"exporten.",
        "_skal": "SO:s och SAOL:s grundbetydelse är TRANSITIV — någon deprecierar "
                 "något. Kortet ledde med den intransitiva vidare användningen, "
                 "som SO märker 'används ibland äv. i vidare bem.'. OLD-facit "
                 "('skriva ned') pekar åt samma håll.",
    },
    "sint": {
        "huvudbetydelse": "Arg, ilsken ; sinnad, i sammansättningar som lättsint "
                          "och hårdsint",
        "synonymer": ["vred", "ilsken", "sinnad"],
        "synonym_groups": [["vred", "ilsken"], ["sinnad"]],
        "register": "dialektal, neutral",
        "_skal": "SAOL har en andra betydelse kortet saknade: 'sinnad', den som "
                 "lever i lättsint, hårdsint, fastsint. Registret behålls "
                 "dialektalt — SO:s märkning är 'mindre brukligt; prov.'",
    },
    "autonom": {
        "huvudbetydelse": "Som har hög grad av oberoende och styr sig själv ; om "
                          "fordon: som kan framföras utan förare ; om person eller "
                          "grupp: starkt samhällskritisk",
        "synonymer": ["självständig", "självstyrande", "självkörande",
                      "starkt kritisk inställning till samhället"],
        "synonym_groups": [["självständig", "självstyrande"], ["självkörande"],
                           ["starkt kritisk inställning till samhället"]],
        "_skal": "SO har en fjärde betydelse kortet saknade: 'som uttrycker en "
                 "starkt kritisk inställning till samhället' — de autonoma. "
                 "Kortet hade bara oberoende och självkörande.",
    },
    "accession": {
        "huvudbetydelse": "Tillskott eller nyförvärv till en befintlig samling, "
                          "t.ex. ett bibliotek eller museum ; en stats anslutning "
                          "till ett redan existerande fördrag",
        "synonymer": ["nyförvärv", "tillskott", "anslutning"],
        "synonym_groups": [["nyförvärv", "tillskott"], ["anslutning"]],
        "exempelmening": f"Bibliotekets {h('accession')} under året uppgick till "
                         f"drygt tvåtusen band.",
        "register": "ngt ålderdomlig, neutral",
        "_skal": "Ordningen vändes. SO märker traktatbetydelsen 'mindre brukligt' "
                 "medan samlingsbetydelsen är standard — kortet ledde med den "
                 "ovanliga och gav den dessutom det enda exemplet.",
    },
    "aristokratisk": {
        "huvudbetydelse": "Som utmärker aristokratin, med förnämt och lite "
                          "överlägset sätt ; som har att göra med aristokrati",
        "synonymer": ["högdragen", "adlig"],
        "synonym_groups": [["högdragen"], ["adlig"]],
        "_skal": "Kortet skrev 'utmärker ELLER hör till aristokratin'. 'Eller' får "
                 "aldrig stå mellan två skilda betydelser — SO håller isär dem, "
                 "och separatorn ska vara ' ; '.",
    },
    "curare": {
        "huvudbetydelse": "Muskelförlamande pilgift ur sydamerikanska växter ; "
                          "muskelavslappnande medel som används vid kirurgi",
        "synonymer": ["pilgift", "muskelförlamande medel"],
        "synonym_groups": [["pilgift"], ["muskelförlamande medel"]],
        "_skal": "SO lyfter uttryckligen fram BÅDA användningarna. Kortet hade "
                 "bara pilgiftet, trots att registret redan sa 'medicin'.",
    },
    "förmäla": {
        "huvudbetydelse": "Meddela eller omtala ; gifta bort någon ; om företeelser: "
                          "förekomma tillsammans, förenas",
        "synonymer": ["omtala", "förtälja", "gifta bort", "förena"],
        "synonym_groups": [["omtala", "förtälja"], ["gifta bort"], ["förena"]],
        "register": "formell, neutral ; ngt ålderdomlig, neutral ; litterär, neutral",
        "_skal": "Två fel. SO har en tredje, bildlig användning kortet saknade "
                 "('hos NN förmäler sig folklighet med akademisk lärdom'). Och "
                 "registerleden satt omkastade: SO märker meddela-betydelsen "
                 "FORMELL och gifta bort-betydelsen ÅLDERDOMLIG, kortet hade "
                 "tvärtom.",
    },
    "konstruktivism": {
        "register": "fackspråklig, neutral, konst",
        "exempelmening": f"Tatlins torn är {h('konstruktivismens')} mest kända "
                         f"verk — stål och glas i stället för marmor.",
        "_skal": "Exemplet illustrerade bara den andra betydelsen, inte "
                 "konstriktningen kortet leder med, och förenklade den dessutom "
                 "fel: 'vi är alla sociala varelser' är inte samma påstående som "
                 "'verkligheten är socialt konstruerad'. Nytt exempel för "
                 "huvudbetydelsen. Domänen flyttad från filosofi till konst av "
                 "samma skäl.",
    },
    "infiltration": {
        "huvudbetydelse": "Omärkligt eller gradvis inträngande av främmande element "
                          "i en organisation eller organism ; vattnets nedträngande "
                          "i marken",
        "synonymer": ["innästling", "inträngning", "nedträngning"],
        "synonym_groups": [["innästling", "inträngning"], ["nedträngning"]],
        "_skal": "SO:s underbetydelse 'vattnets nedträngande i marken' är en egen "
                 "betydelse, inte en aspekt av den första. Kortet slog ihop dem i "
                 "en mening, vilket dolde att exemplet handlade om den andra.",
    },
    "pläd": {
        "huvudbetydelse": "Mindre, lättare filt som används utan lakan, särskilt "
                          "vid vila dagtid ; rutig yllesjal av skotskt slag",
        "synonymer": ["filt", "resfilt", "yllesjal"],
        "synonym_groups": [["filt", "resfilt"], ["yllesjal"]],
        "_skal": "Wiktionary och syn.se ger båda den rutiga sjalen — ordets "
                 "ursprungliga betydelse, från engelskans plaid. Kortet hade bara "
                 "filten.",
    },

    # ---------- Betydelser jag lagt till utan täckning ----------
    "oratorium": {
        "huvudbetydelse": "Stort dramatiskt musikverk för kör, solister och "
                          "orkester, oftast över religiöst ämne",
        "synonymer": ["sakralt musikverk", "körverk för solister"],
        "synonym_groups": None,
        "exempelmening": f"Haydns {h('oratorium')} Skapelsen framfördes av kör, "
                         f"solister och orkester i domkyrkan.",
        "_skal": "Bönsalen ströks. Både SO och SAOL ger bara EN nutida betydelse. "
                 "'Oratorium' som bönsal är ordets medeltidslatinska ETYMOLOGI "
                 "(till orare 'bedja'), inte en levande svensk betydelse — och "
                 "etymologin står redan i sitt eget fält.",
    },
    "stilisera": {
        "huvudbetydelse": "Förenkla en avbildning så att det typiska framhävs",
        "synonymer": ["förenkla", "schematisera", "renodla"],
        "_skal": "Den klandrande betydelsen ('göra schablonmässig') ströks — SO "
                 "har bara en huvudbetydelse med en NEUTRAL bildlig "
                 "underbetydelse ('bokens stiliserade persongalleri'), utan "
                 "nedsättande ton.",
    },

    # ---------- Exempelmeningar och register ----------
    "depression": {
        "exempelmening": f"Döda havets {h('depression')} ligger drygt 420 meter "
                         f"under havsytan och sjunker för varje år.",
        "_skal": "Sakfel i den gamla exempelmeningen: 392 meter är en föråldrad "
                 "siffra, nivån ligger idag omkring 422 meter under havsytan och "
                 "fortsätter sjunka. Betydelserna i övrigt täcker SO:s tre "
                 "korrekt.",
    },
    "komma för": {
        "exempelmening": f"Det {h('kom för')} honom att han hade sett mannen "
                         f"förut, men han kunde inte placera ansiktet.",
        "_skal": "Grammatiskt fel i exemplet: 'att han sett mannen' saknar "
                 "hjälpverbet. Ska vara 'att han hade sett'.",
    },
    "övlig": {
        "exempelmening": f"Han kom med sina {h('övliga')} undanflykter om att "
                         f"tåget varit försenat.",
        "register": "ngt ålderdomlig, ironisk",
        "_skal": "Registret säger 'ironisk' — SO:s märkning är 'ofta något "
                 "ironiskt; något ålderdomligt' — men det gamla exemplet ("
                 "handskakning efter avtal) var helt sakligt och visade inte "
                 "tonen. Nytt exempel som gör ironin hörbar.",
    },
    "manisk": {
        "register": "neutral, neutral, psykologi",
        "_skal": "'Ngt ålderdomlig' var mitt fel från i natt. SO ger ingen "
                 "bruklighetsmarkering alls — manisk är fullt aktuellt både "
                 "kliniskt och vardagligt (manisk episod, manisk-depressiv).",
    },
    "runda ord": {
        "huvudbetydelse": "Vardagliga, raka och burdusa ord för sexuella saker",
        "synonymer": ["fula ord", "ord med sexuell anspelning"],
        "_skal": "Kortet sa 'mildare ord', alltså förskönande omskrivningar. Det "
                 "motsades av kortets egen synonym 'fula ord' och av OLD-facit. "
                 "Runda ord är raka, inte förmildrande.",
    },
}

STANDARD = ("Omgranskning efter blindgranskarens anmarkning 2026-08-12, mot "
            "SO/SAOL/synonymer.se/wiktionary med ortografifiltrerat underlag. "
            "Synonymerna provade mot utbytbarhet: varken snavare eller vidare "
            "an uppslagsordet.")


def _med_doman(register, ord_):
    dom = DOMAN.get(ord_)
    if not dom or not register:
        return register
    delar = [d.strip() for d in register.split(";")]
    if any(dom == t.strip() for d in delar for t in d.split(",")):
        return register
    delar[0] = delar[0] + ", " + dom
    return " ; ".join(delar)


def main():
    poster = json.load(open(SESSION, encoding="utf-8"))
    saknar = [p["ord"] for p in poster if p["ord"] not in DOMAN]
    if saknar:
        sys.exit(f"domän saknas för {', '.join(saknar)}")
    for p in poster:
        o = p["ord"]
        L = p["legacy"]
        r = RATTELSER.get(o, {})
        p["proposed"] = {
            "huvudbetydelse": r.get("huvudbetydelse", L.get("huvudbetydelse")),
            "synonymer": r.get("synonymer", L.get("synonymer")),
            "synonym_groups": r.get("synonym_groups", L.get("synonym_groups")),
            "exempelmening": r.get("exempelmening", L.get("exempelmening") or ""),
            "register": r.get("register") or _med_doman(L.get("register"), o),
            "etymologi": r.get("etymologi", L.get("etymologi")),
        }
        p["approved"] = True
        p["sokkoll"] = {"kalla": SVENSKA.format(urllib.parse.quote(o)),
                        "slutsats": r.get("_skal", STANDARD)}
        p.pop("applicerad", None)
    json.dump(poster, open(SESSION, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"fyllde {len(poster)} poster, varav {len(RATTELSER)} rattade.")


if __name__ == "__main__":
    main()
