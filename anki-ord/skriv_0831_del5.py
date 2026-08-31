# -*- coding: utf-8 -*-
"""Batch 2026-08-31. Del 5: kort 32-40, sista omgangen.

SEX AV NIO PAUSAS. Det ar en ovanligt hog andel och den har en enkel
forklaring: batchen ar due-ordnad ur den ogranskade is:new-poolen, och slutet
av den ordningen bestar av kort som en tidigare omgang lade dit UTAN
ordboksunderlag -- HTML, tibia, ipso jure, seriffer, vasstackt och
fornamligen. Ingen av dem har ett uppslagsord i SO eller SAOL.

Att skriva dem anda hade brutit mot regel 3 (ingen betydelse som bara
Wiktionary eller syn.se har) och gjort dem till full v3 pa ett underlag som
inte finns. `seriffer` ar det tydligaste fallet: enda traffen ar syn.se, som
ger "schattering, skuggning" -- alltsa nagot helt annat an typografins
seriffer. Hade den listan behandlats som belagg hade kortet blivit direkt
felaktigt.

Pausade kort ar inte underkanda. De kan tas upp igen mot SAOB, Wikipedia
eller en fackordbok, men da som ett medvetet beslut om kallhierarkin och inte
som en bieffekt av en batchkorning.
"""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-31_v3-batch40.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
B = '<font color="#3498db">%s</font>'


def kallor(o, *extra):
    k = urllib.parse.quote(o)
    return " ".join([
        "https://svenska.se/api/msearch?ord=%s" % k,
        "https://www.synonymer.se/sv-syn/%s" % k,
        "https://sv.wiktionary.org/wiki/%s" % k,
        *extra,
    ])


def satt(o, bet, reg, syn, ex, ety, slutsats, grupper=None, extra=(), conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": grupper, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": kallor(o, *extra), "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True


def pausa(o, skal, slutsats):
    e = BY[o]
    e["proposed"] = None
    e["approved"] = False
    e["note_till_granskare"] = skal
    e["sokkoll"] = {"kalla": kallor(o), "slutsats": slutsats}
    e["v3_pausad"] = skal


# ----------------------------------------------------------------- 32. HTML
pausa("HTML", "inget_uppslagsord_i_so_saol",
      "Noll traffar i SO, SAOL och syn.se. HTML ar en verklig och val "
      "definierad fackterm, men den finns inte i de ordbocker som utgor "
      "valvets kallhierarki, sa varje betydelse jag skrev skulle vila pa min "
      "egen kunskap i stallet for pa ett belagg. Kandidat for en senare "
      "omgang med uttryckligt fackordboksbeslut.")

# -------------------------------------------------------------- 33. blamera
satt("blamera",
     "Skämma ut sig genom något dumt eller oöverlagt ; även skämma ut någon "
     "annan",
     "formell, negativ ; formell, negativ",
     ["skämma ut sig"],
     "Vicepresidenten " + B % "blamerade sig" + " ofta med sina oöverlagda "
     "uttalanden.",
     "av tyskans blamieren, av franskans blâmer 'klandra', ytterst av "
     "grekiskans blasphemein 'smäda'; samma rot som i blasfemi",
     "SO: 'skamma ut sig'. SAOL delar upp i tva: 'skamma ut' och 'skamma ut "
     "sig', alltsa den transitiva och den reflexiva anvandningen. Eftersom "
     "SAOL haller isar dem skrivs bada (regel 1). Synonymen skamma ut sig ar "
     "hela SO:s definition och darmed belagd.",
     grupper=[["skämma ut sig"], []])

# ---------------------------------------------------------- 34. gra eminens
satt("grå eminens",
     "Person som utåt verkar betydelselös men i själva verket har stort "
     "inflytande, ofta utövat i det fördolda",
     "formell, neutral",
     [],
     "På äldre dagar var han utrikesdepartementets " + B % "grå eminens" + ".",
     "översättning av franskans éminence grise, ursprungligen om kapucinmunken "
     "François Leclerc du Tremblay i grå kåpa, kardinal Richelieus förtrogne "
     "rådgivare på 1600-talet",
     "Uppslagsordet i SO ar EMINENS, som haller isar '(titel for) kardinal', "
     "'skenbart betydelselos men i sjalva verket inflytelserik person' och en "
     "vardaglig anvandning om socialdemokrater. Det ar den ANDRA som ar "
     "uttrycket gra eminens, vilket SO:s eget exempel bekraftar: 'pa aldre "
     "dagar var han utrikesdepartementets gra eminens'. Kardinalbetydelsen "
     "hor till eminens ensamt och skrivs inte in har, eftersom kortets "
     "framsida ar hela uttrycket. Inga belagda synonymer.")

# ------------------------------------------------------------ 35. elliptisk
satt("elliptisk",
     "Formad som en ellips, alltså avlångt rund ; i språkvetenskap: förkortad "
     "genom att ett självklart led har utelämnats",
     "fackspråklig, neutral ; fackspråklig, neutral, språkvetenskap",
     [],
     "Planeternas " + B % "elliptiska" + " banor kring solen.",
     "till ellips, av grekiskans elleipsis 'brist, utelämnande', till "
     "elleipein 'lämna kvar'; båda betydelserna går tillbaka på samma bild "
     "av något som saknas",
     "SO haller isar tva: 'formad som en ellips' och 'forkortad till en "
     "ellips', den senare markt sprakvetenskap. Bada skrivs (regel 1), och "
     "domanmarkningen sprakvetenskap har uttryckligt stod i SO. Exemplen "
     "bekraftar bada: 'planeternas elliptiska banor' och 'elliptiska "
     "konstruktioner som foretagsledare mordad'. Inga belagda synonymer: "
     "syn.se:s oval och aggformig star inte i nagon ordboksdefinition, och "
     "oval ar dessutom inte utbytbart -- en ellips ar en bestamd matematisk "
     "kurva, oval ar en vardaglig formbeskrivning.")

# ---------------------------------------------------------- 36. fornamligen
pausa("förnämligen", "inget_uppslagsord_i_so_saol",
      "Noll traffar i SO, SAOL, syn.se och Wiktionary. Ordet ar alderdomligt "
      "och finns sannolikt i SAOB, men ingen av valvets tre huvudkallor har "
      "det. Att skriva 'huvudsakligen, framfor allt' vore att belagga en "
      "betydelse med min egen kunskap.")

# -------------------------------------------------------------- 37. seriffer
pausa("seriffer", "syn_se_ger_fel_ord",
      "Varken SO eller SAOL har seriffer. Enda traffen ar syn.se, som ger "
      "'schattering, skuggning' -- alltsa NAGOT HELT ANNAT an typografins "
      "seriffer, de sma tvarstrecken vid bokstavernas andar. Hade syn.se:s "
      "lista behandlats som belagg hade kortet blivit direkt felaktigt. Det "
      "har ar det tydligaste enskilda exemplet i batchen pa varfor regel 2 "
      "sager att syn.se duger till att HITTA kandidater men aldrig till att "
      "BELAGGA dem.")

# ---------------------------------------------------------------- 38. tibia
pausa("tibia", "inget_uppslagsord_i_so_saol",
      "Noll traffar i SO och SAOL. Wiktionary har ordet men regel 3 forbjuder "
      "en betydelse som bara Wiktionary har. Skenbenet ar en anatomisk "
      "fackterm och kandidat for en senare omgang mot en medicinsk ordbok. "
      "Det gamla kortet listade dessutom fibula som synonym, vilket ar fel: "
      "fibula ar vadbenet, alltsa ett ANNAT ben i underbenet.")

# ------------------------------------------------------------ 39. vasstackt
pausa("vasstäckt", "inget_uppslagsord_i_so_saol",
      "svenska.se svarade men utan definitioner for vasstackt -- ordet finns "
      "inte som eget uppslagsord i vare sig SO eller SAOL, bara delarna vass "
      "och tackt. En sammansattning far inte betydelse genom att bada leden "
      "finns. Det gamla kortet sa dessutom 'tackt med en tat massa av vass "
      "och vegetation ; bevuxen med gras eller annan tat vaxtlighet', vilket "
      "blandar ihop vasstackt tak med vassbevuxen strand.")

# ------------------------------------------------------------- 40. ipso jure
pausa("ipso jure", "inget_uppslagsord_i_so_saol",
      "Noll traffar i samtliga fyra kallor -- den enda posten i batchen med "
      "helt tom hamtning. Latinsk juridisk term som inte finns i nagon "
      "svensk allmanordbok. Kandidat for en senare omgang mot en juridisk "
      "ordbok, om Adam vill ha kvar latinska rattstermer i decket alls.")


json.dump(KORT, io.open(FIL, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
skrivna = sum(1 for k in KORT if k.get("proposed"))
pausade = sum(1 for k in KORT if k.get("v3_pausad"))
print("del 5 klar: %d skrivna, %d pausade, %d utan beslut"
      % (skrivna, pausade, 40 - skrivna - pausade))
