# -*- coding: utf-8 -*-
"""Omkörning av de 10 kort som blindgranskaren underkände 2026-08-12 (kväll).

Plockar posterna ur de tre sessionsfilerna, rättar dem enligt granskarens
motivering och skriver EN gemensam omkörningssession. Armtillhörigheten är
redan mätt i första passet — omkörningen påverkar inte den siffran.

## Nio av tio underkännanden var berättigade

Åtta av dem är samma fel: **en betydelse som källan har och kortet inte har.**

* `nativ` — SO:s underbetydelse *medfödd* ("nativ språkkänsla"). Den stod i
  underlaget jag läste och jag valde bort den.
* `eventuell` — SO skiljer "kanske kommer att inträffa" från "kanske redan
  finns" (*eventuella fel*). Kortet hade bara framtidsfallet.
* `frodig` — SO:s tredje underbetydelse "starkt produktiv" (*en frodig
  fantasi*).
* `sätta sig` — *sätta sig i respekt*, alltså hävda sin auktoritet. Kortet hade
  tre av fyra.
* `apostel` — **för snävt, inte för brett.** Kortet sa "en av Jesu tolv
  lärjungar". SAOL:s eget exempel är *aposteln Paulus*, som inte var en av de
  tolv. Ordet täcker efterföljare i vidare mening (Ansgar, Nordens apostel).
* `dagsedel` och `preja` — registret. Båda orden bär märkningen *ålderdomligt*,
  och på `preja` sitter den bara på EN av tre betydelser (att ta för mycket
  betalt), inte på sjötermen. Kortet hade satt den på fel betydelse.
* `destillera` — exempelmeningen sa att hon lärde sig destillera sprit "på
  bryggeriet". Ett bryggeri jäser öl; sprit destilleras på destilleri. Sakfel i
  exemplet, inte i betydelsen.
* `bulla upp` — synonymen *ställa till kalas*. Man kan bulla upp utan kalas och
  ha kalas utan att bulla upp.

## Den tionde: granskaren hade fel, och det går att bevisa

`brödtext` underkändes för registret *vardaglig*, med motiveringen "SAOL har
ingen vard.-markering för ordet, det är en neutral fackterm". Det stämmer om
SAOL. Men SO:s post för `brödtext` har fältet

    "bruklighetskommentar": "vardagligt"

på sin enda huvudbetydelse. Registret följer alltså SO ordagrant, och det var
dessutom `forgranska.py`s `register_motsager_markning` som krävde ändringen
från *formell* i första passet. Kortet skickas tillbaka OFÖRÄNDRAT, med
fältnamnet utskrivet i sökkollen så att nästa granskare kan slå upp det själv i
stället för att göra samma antagande.

Det här är första gången i projektet en blindgranskares underkännande visar sig
vara felaktigt på ett kontrollerbart sätt. Det är värt att notera för vad det
säger om granskningens felmarginal åt BÅDA hållen — hittills har bara
falska godkännanden diskuterats.
"""

import json
import os
import sys
import urllib.parse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FARG = "#3498db"
SVENSKA = "https://svenska.se/api/msearch?ord={}"
KALLOR = [
    "sessions/session_2026-08-12_v3-batch.json",
    "sessions/session_2026-08-12_armA-provisorisk.json",
    "sessions/session_2026-08-12_armB-osokkollad.json",
]
UT = "sessions/session_2026-08-12_omkorning.json"


def h(o):
    return f'<font color="{FARG}">{o}</font>'


KORT = {
    "nativ": {
        "hb": "Som finns färdig i naturen ; medfödd och inneboende ; om metall: "
              "gedigen och ren",
        "reg": "fackspråklig, neutral",
        "grupper": [["naturlig"], ["medfödd"], ["gedigen"]],
        "ex": f"Guld förekommer {h('nativt')} i naturen och behöver inte "
              f"framställas.",
        "skal": "TILLAGD BETYDELSE: SO har underbetydelsen 'medfödd' vid sidan av "
                "'som förekommer färdig i naturen' — den används om egenskaper "
                "(nativ språkkänsla, nativ begåvning) och stod även i kortets "
                "OLD-facit ('naturlig, medfödd; gedigen, ren'). Facit hade alltså "
                "alla tre betydelserna från början.",
    },
    "dagsedel": {
        "hb": "Kraftig örfil",
        "reg": "ngt ålderdomlig, neutral",
        "syn": ["örfil", "snyting", "hurring"],
        "ex": f"Han delade ut en {h('dagsedel')} mitt framför kamerorna.",
        "skal": "REGISTER RÄTTAT: SO märker ordet både 'vardagligt' och 'något "
                "ålderdomligt', SAOL 'åld.'. Registerformatet rymmer en stilnivå "
                "per betydelse, och ålderdomligheten är den som faktiskt "
                "informerar — att ordet är vardagligt gissar man ändå, att det är "
                "daterat gör man inte.",
    },
    "eventuell": {
        "hb": "Som kanske kommer att inträffa ; som kanske redan finns",
        "reg": "neutral, neutral",
        "syn": ["möjlig"],
        "ex": f"Ta med paraply för {h('eventuellt')} regn på vägen hem.",
        "skal": "TILLAGD BETYDELSE: SO har både 'som kanske kommer att inträffa' "
                "och underbetydelsen 'som kanske existerar'; SAOL skriver "
                "'möjligen inträffande el. förekommande'. Skillnaden syns i "
                "'eventuella fel i texten' — felen finns redan eller inte alls, "
                "de ska inte inträffa.",
    },
    "apostel": {
        "hb": "Efterföljare till Jesus som spred kristendomen ; ivrig förkunnare "
              "av en lära eller rörelse",
        "reg": "neutral, neutral, religion ; neutral, neutral",
        "grupper": [["Jesu sändebud"], ["förkunnare", "missionär"]],
        "ex": f"Han blev en {h('apostel')} för den nya kostläran och predikade "
              f"den överallt.",
        "skal": "RÄTTAT — FÖR SNÄVT: kortet sa 'en av Jesu tolv lärjungar'. "
                "SAOL:s gloss är 'efterföljare till Jesus som medverkade till att "
                "sprida kristendomen', och dess EGET exempel är 'aposteln "
                "Paulus' — Paulus tillhörde inte de tolv. Ordet används dessutom "
                "om senare missionärer (Ansgar, Nordens apostel).",
    },
    "frodig": {
        "hb": "Fysiskt väl utvecklad och yppig ; rikt växande och grönskande ; "
              "starkt produktiv, om fantasi och bildspråk",
        "reg": "neutral, positiv",
        "syn": ["yppig", "ymnig", "välfödd"],
        "ex": f"Den {h('frodiga')} skogen var full av liv och grönska.",
        "skal": "TILLAGD BETYDELSE: SO:s huvudbetydelse har tre underbetydelser "
                "— om växt, om person ('fet och godmodig') och om abstrakta "
                "företeelser ('starkt produktiv'). Den sista, 'en frodig "
                "fantasi', saknades.",
    },
    "sätta sig": {
        "hb": "Placera sig i sittande ställning ; sjunka ihop, om mark eller "
              "husgrund ; vara nedlåtande mot någon ; hävda sin auktoritet",
        "reg": "neutral, neutral",
        "syn": ["slå sig ner", "sjunka"],
        "ex": f"Trött efter promenaden {h('satte hon sig')} på närmaste bänk.",
        "skal": "TILLAGD BETYDELSE: SO har två skilda bildliga underbetydelser "
                "till 'sitta ned' — 'vara nedlåtande' (som kortet hade) och "
                "'sätta sig i respekt', alltså hävda sin auktoritet. "
                "Facit_signal sa 4 mot 3 och hade rätt.",
    },
    "preja": {
        "hb": "Anropa och tvinga ett fartyg att stanna ; tränga ett fordon av "
              "vägen ; ta alltför mycket betalt av någon",
        "reg": "neutral, neutral, sjöfart ; neutral, neutral ; ngt ålderdomlig, "
               "negativ",
        "grupper": [["tvinga att stanna"], ["tränga undan"], ["skinna", "pungslå"]],
        "ex": f"Handelsfartyget {h('prejades')} av en jagare i blockadflottan.",
        "skal": "REGISTER FLYTTAT: både SO och SAOL märker BARA betydelsen 'ta "
                "(alltför) mycket betalt' som ålderdomlig — sjötermen är fullt "
                "levande. Kortet hade satt märkningen på den första betydelsen. "
                "Ett register per betydelse finns just för att kunna skilja dem åt.",
    },
    "destillera": {
        "hb": "Skilja en vätskas beståndsdelar åt genom förångning och "
              "kondensering",
        "reg": "fackspråklig, neutral, kemi",
        "syn": ["rena", "avskilja"],
        "ex": f"På destilleriet lärde hon sig att {h('destillera')} whisky.",
        "skal": "SAKFEL I EXEMPLET RÄTTAT: exemplet utspelade sig 'på bryggeriet'. "
                "Ett bryggeri jäser öl; sprit destilleras på ett destilleri. "
                "'Koncentrera' ströks ur synonymlistan — kärnan är att skilja åt "
                "och rena, koncentrationen är en följd.",
    },
    "bulla upp": {
        "hb": "Duka fram mat i stor och riklig mängd",
        "reg": "vardaglig, neutral",
        "syn": ["bjuda rundhänt"],
        "ex": f"Till kalaset hade mormor {h('bullat upp')} med tårtor, bullar "
              f"och saft.",
        "skal": "SYNONYM STRUKEN: 'ställa till kalas' är att anordna en fest, "
                "'bulla upp' är att duka fram rikligt — man kan göra det ena utan "
                "det andra. Kvar står 'bjuda rundhänt' ur synonymer.se, som är "
                "utbytbart.",
    },
    "brödtext": {
        "hb": "Den löpande huvudtexten i en artikel",
        "reg": "vardaglig, neutral",
        "syn": ["löpande text"],
        "ex": f"Artikelns {h('brödtext')} gav detaljerna mellan rubrik och bild.",
        "skal": "OFÖRÄNDRAT — föregående underkännande vilade på ett fel. "
                "Granskaren skrev att ordet saknar vardaglighetsmärkning och är "
                "en neutral fackterm. Det stämmer för SAOL, men SO:s post "
                "(l_nr 127085) har fältet \"bruklighetskommentar\": \"vardagligt\" "
                "på sin enda huvudbetydelse — slå upp det innan verdikt. "
                "Registret följer alltså SO ordagrant, och det var "
                "forgranska.py:s register_motsager_markning som krävde bytet från "
                "'formell' i första passet.",
    },
}


def main():
    hittade = {}
    for k in KALLOR:
        for p in json.load(open(k, encoding="utf-8")):
            if p["ord"] in KORT:
                hittade[p["ord"]] = p
    saknar = set(KORT) - set(hittade)
    if saknar:
        sys.exit(f"hittade inte i sessionsfilerna: {', '.join(sorted(saknar))}")

    poster = []
    for o, r in KORT.items():
        p = hittade[o]
        p["proposed"] = {
            "huvudbetydelse": r["hb"],
            "synonymer": r.get("syn", [s for g in r.get("grupper", []) for s in g]),
            "synonym_groups": r.get("grupper"),
            "exempelmening": r["ex"],
            "register": r["reg"],
            "etymologi": None,
        }
        p["approved"] = True
        p["sokkoll"] = {"kalla": SVENSKA.format(urllib.parse.quote(o)),
                        "slutsats": r["skal"]}
        p.pop("applicerad", None)
        poster.append(p)

    os.makedirs(os.path.dirname(UT), exist_ok=True)
    json.dump(poster, open(UT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"skrev {len(poster)} omkörningsposter till {UT}")


if __name__ == "__main__":
    main()
