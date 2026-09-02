# -*- coding: utf-8 -*-
"""Lagger tillbaka de SO-betydelser jag valt bort med en skriven motivering.

VARFOR MOTIVERINGEN VAR FEL STRATEGI. `betydelse_kan_saknas` ar hard just
for att valet ska SKRIVAS, och jag skrev det -- 25 ganger. Men motiveringen
hamnar i `forgranska_tillat`, och `kortgranskare.paket()` tar medvetet inte
med den: paketet ska "lacka ingenting om hur kortet blev till". Foljden ar
att en genomtankt bortvald betydelse ser exakt likadan ut som en forbisedd,
och blindgranskaren underkanner den varje gang.

MATT i omgang 1: 3 av 25 underkanda (12 %), alla tre av precis det skalet --
kriterium, tiara, torsion. Med 23 kort av samma konstruktion i batchen skulle
det bli ungefar nio avslag till over de aterstaende 75, till 1,24 USD per
omgang om 25.

RATT SLUTSATS ar inte att lacka motiveringen till granskaren -- blindheten ar
hela poangen med steget. Det ar att SLUTA valja bort numrerade betydelser.
Granskarens bar ar tydlig och rimlig: star betydelsen som egen numrerad post
i SO eller SAOL hor den hemma pa kortet. Kortformatet rymmer flera betydelser
med ` ; `, sa det kostar ingenting att ta med dem -- och Adam moter dem pa
provet oavsett vad jag tycker om deras fackspraklighet.

UNDANTAGEN som star kvar, och varfor de ar av ett annat slag: kvittens och
vagel ar HOMONYMER -- kvitten ar en buske och vagel en honssittstang, ord som
bara rakat sammanfalla i form. Narrs andra post ar verbet narra. Dar handlar
det inte om en bortvald betydelse utan om ett annat ord i samma artikel, och
det argumentet haller aven for en granskare som inte ser motiveringen.
"""
import io, json, sys
import _hjalp_0902b as HJ

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02b_v3-batch.json"

# ord -> (huvudbetydelse, register, synonymer, grupper)
K = {
 "autokton": (
  "Uppvuxen på samma plats som den finns på nu ; om berggrund: bildad av material från platsen själv",
  "formell, neutral ; fackspråklig, neutral, geologi",
  ["inhemsk", "≈≈ ortsbildad"], [["inhemsk"], ["≈≈ ortsbildad"]]),

 "cyklisk": (
  "Som upprepas regelbundet, moment för moment ; som bildar en sluten ring",
  "formell, neutral ; fackspråklig, neutral, kemi",
  ["kretsformig", "≈≈ ringformad"], [["kretsformig"], ["≈≈ ringformad"]]),

 "eldsjäl": (
  "Person med brinnande engagemang som driver andra framåt ; själva den brinnande iver som driver en sådan person",
  "neutral, positiv ; litterär, positiv",
  ["engagerad person", "≈≈ iver"], [["engagerad person"], ["≈≈ iver"]]),

 "koloss": (
  "Något ovanligt stort och tungt ; något som ser mäktigt ut men är svagt ; mycket stor staty",
  "litterär, neutral ; litterär, neutral ; fackspråklig, neutral, konst",
  ["bjässe", "≈≈ jättestaty"],
  [["bjässe"], ["≈≈ lerfotad jätte"], ["≈≈ jättestaty"]]),

 "kriterium": (
  "Avgörande kännetecken som avgör om något hör till en viss kategori ; travtävling för unghästar",
  "formell, neutral ; fackspråklig, neutral, sport",
  ["kännetecken", "travtävling"], [["kännetecken"], ["travtävling"]]),

 "nexus": (
  "Central koppling som binder samman flera saker ; i grammatik: bandet mellan subjekt och predikat",
  "formell, neutral ; fackspråklig, neutral, lingvistik",
  ["≈≈ knutpunkt", "≈≈ satsband"], [["≈≈ knutpunkt"], ["≈≈ satsband"]]),

 "profetia": (
  "Förutsägelse om vad som ska hända, ofta med religiös grund ; förutsägelse som slår in just för att någon uttalat den",
  "litterär, neutral ; neutral, neutral",
  ["förutsägelse", "förkunnelse", "≈≈ självuppfyllelse"],
  [["förutsägelse", "förkunnelse"], ["≈≈ självuppfyllelse"]]),

 "proviantera": (
  "Skaffa mat och dryck inför en resa ; göra större matinköp",
  "neutral, neutral ; neutral, neutral",
  ["skaffa proviant", "göra (större) matinköp"],
  [["skaffa proviant"], ["göra (större) matinköp"]]),

 "tiara": (
  "Praktfullt huvudsmycke buret vid högtidliga tillfällen ; påvens höga, toppiga huvudbonad",
  "formell, neutral ; fackspråklig, neutral, religion",
  ["diadem", "≈≈ huvudbonad"], [["diadem"], ["≈≈ huvudbonad"]]),

 "korrosion": (
  "Att metall fräts sönder av kemisk påverkan ; att berggrund nöts ned av yttre krafter",
  "fackspråklig, neutral, kemi ; fackspråklig, neutral, geologi",
  ["frätning", "rostning", "≈≈ nednötning"],
  [["frätning", "rostning"], ["≈≈ nednötning"]]),

 "rasera": (
  "Riva ned så att något faller samman ; falla sönder av sig självt över tid",
  "neutral, neutral ; neutral, neutral",
  ["riva", "förstöra", "jämna med marken", "≈≈ förfalla"],
  [["riva", "förstöra", "jämna med marken"], ["≈≈ förfalla"]]),

 "blickfång": (
  "Det som naturligt drar till sig blicken ; det område blicken överskådar",
  "neutral, neutral ; neutral, neutral",
  ["som fångar blicken", "synfält"], [["som fångar blicken"], ["synfält"]]),

 "crescendo": (
  "Musik som gradvis blir starkare ; avsnittet i stycket som ska spelas så",
  "fackspråklig, neutral, musik ; fackspråklig, neutral, musik",
  ["med växande tonstyrka", "≈≈ musikavsnitt"],
  [["med växande tonstyrka"], ["≈≈ musikavsnitt"]]),

 "fission": (
  "Klyvning av en atomkärna ; uppdelning av ett företag i flera delar",
  "fackspråklig, neutral, fysik ; fackspråklig, neutral, ekonomi",
  ["kärnklyvning", "≈≈ bolagsdelning"],
  [["kärnklyvning"], ["≈≈ bolagsdelning"]]),

 "homofon": (
  "Ord som uttalas likadant som ett annat men betyder något annat ; om musik: med en enda melodiförande stämma",
  "fackspråklig, neutral, lingvistik ; fackspråklig, neutral, musik",
  ["≈≈ ord", "≈≈ enstämmig"], [["≈≈ ord"], ["≈≈ enstämmig"]]),

 "lockrop": (
  "Läte som ett djur ger för att locka till sig andra djur ; rop som en boskapsskötare lockar sina djur med",
  "neutral, neutral ; ngt ålderdomlig, neutral",
  ["≈≈ läte", "≈≈ rop"], [["≈≈ läte"], ["≈≈ rop"]]),

 "långrandig": (
  "Tröttsamt utdragen ; randig på längden",
  "neutral, lätt negativ ; neutral, neutral",
  ["långtråkig", "randig på längden"],
  [["långtråkig"], ["randig på längden"]]),

 "statistisk": (
  "Som bygger på insamlade sifferuppgifter och deras analys ; som rör ämnet statistik",
  "formell, neutral, matematik ; formell, neutral, matematik",
  ["≈≈ siffergrundad", "≈≈ ämnesrelaterad"],
  [["≈≈ siffergrundad"], ["≈≈ ämnesrelaterad"]]),

 "trashank": (
  "Person i trasiga kläder ; mycket fattig person",
  "ngt ålderdomlig, nedsättande ; ngt ålderdomlig, nedsättande",
  ["≈≈ trasklädd", "fattig person"], [["≈≈ trasklädd"], ["fattig person"]]),

 "ackumulera": (
  "Samla på hög så att mängden växer över tid",
  "formell, neutral", ["hopa", "samla"], [["hopa", "samla"]]),

 "torsion": (
  "Vridning av ett föremål när dess ändar vrids åt olika håll ; i medicin: att ett organ vridit sig om sin egen axel",
  "fackspråklig, neutral, fysik ; fackspråklig, neutral, medicin",
  ["≈≈ vridning", "≈≈ organvridning"],
  [["≈≈ vridning"], ["≈≈ organvridning"]]),
}

TILL = (" BETYDELSE TILLAGD 2026-09-02 efter blindgranskningens omgång 1. "
        "Kortet bar först bara en betydelse, med en skriven motivering om att "
        "den andra var fackspråk. Motiveringen når aldrig granskaren — "
        "`paket()` utelämnar den avsiktligt, så ett genomtänkt bortval ser "
        "likadant ut som ett förbiseende. Rätt slutsats är att ta med "
        "betydelsen: står den som egen numrerad post i SO hör den hemma på "
        "kortet, och formatet rymmer den.")

poster = json.load(io.open(FIL, encoding="utf-8"))
n, obelagda = 0, []
for e in poster:
    d = K.get(e["ord"])
    if not d:
        continue
    hb, reg, syn, grp = d
    pool = set(HJ.synpool(e["ord"]))
    for s in syn:
        if not s.startswith("≈") and s not in pool:
            obelagda.append((e["ord"], s))
    pr = e["proposed"]
    pr["huvudbetydelse"], pr["register"] = hb, reg
    pr["synonymer"], pr["synonym_groups"] = syn, grp
    # Motiveringen galler inte langre -- betydelsen ar med.
    (e.get("forgranska_tillat") or {}).pop("betydelse_kan_saknas", None)
    e["sokkoll"]["slutsats"] += TILL
    n += 1

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("kort med tillagd betydelse:", n)
print("exakta synonymer utanfor poolen:", obelagda or "inga")
