# -*- coding: utf-8 -*-
"""Batch 2026-08-31, 40 is:new-kort. Del 1: kort 1-6.

Reglerna, oforandrade sedan 2026-08-29:

1. SLA ALDRIG IHOP tva betydelser som SO eller SAOL haller isar.
   Underbetydelser (SO:s "ub:") far daremot folja med sin huvudbetydelse --
   de ar inte egna betydelser.
2. Synonym bara om ordet ar utbytbart AT BADA HALLEN och antingen ar
   SYN:synonym-markerat i SO eller INLEDER ett led i SO:s/SAOL:s definition.
   syn.se ar kandidatlista, aldrig belagg.
3. Ingen betydelse som bara Wiktionary eller syn.se har.
4. Facit styrs av definitionen, aldrig av etymologin eller en synonym.
5. Etymologifaltet renderas pa kortet: full svenska med a/a/o.
   Bara sokkoll-slutsatsen ar intern och far vara ASCII.
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


# ---------------------------------------------------------------- 1. molla
satt("mölla",
     "Kvarn, särskilt väderkvarn eller vattenkvarn ; numera även om ett "
     "vindkraftverk",
     "dialektal, neutral",
     ["kvarn", "väderkvarn", "vattenkvarn"],
     "Den gamla " + B % "möllan" + " vid åkanten maler fortfarande mjöl.",
     "till fornsvenskans mylna, av latinets molina 'kvarn'; samma ord som "
     "danskans og norskans mølle",
     "SO ger definitionen 'kvarn' med markningen dialektalt, och "
     "underbetydelsen 'numera av. om liknande (storre) anordning som omvandlar "
     "vindkraft till elenergi'. Det ar en UB, inte en egen betydelse, sa den "
     "foljer med i samma grupp. SAOL 'vader- el. vattenkvarn' (prov.) belagger "
     "vaderkvarn och vattenkvarn som ledinledande, och SO belagger kvarn.")

# ---------------------------------------------------------------- 2. docent
satt("docent",
     "Person som har avlagt doktorsexamen och därutöver visat så goda "
     "vetenskapliga meriter att hen fått titeln",
     "formell, neutral, utbildning",
     [],
     "Efter tio år som forskare utnämndes hon till " + B % "docent" + " i "
     "molekylärbiologi.",
     "av latinets docens 'undervisande', av docere 'undervisa, lära ut'; "
     "besläktat med doktor och doktrin",
     "SO: '(titel for) person som har avlagt doktorsexamen och darutover "
     "visat goda vetenskapliga kvalifikationer'. SAOL: 'universitetslarare "
     "med hog forskningskompetens'. En betydelse. INGEN synonym skrivs: "
     "syn.se foreslar universitetslarare, lektor och forskare, men ingen av "
     "dem ar utbytbar at bada hallen -- varje docent ar forskare, men langt "
     "ifran varje forskare ar docent. Tom synonymlista ar godkant.")

# -------------------------------------------------------------- 3. schveifa
pausa("schveifa",
      "inget_uppslagsord_i_so_saol",
      "Varken SO eller SAOL har schveifa som uppslagsord. Enda traffen ar "
      "syn.se, som ger '(tekn.), hamra ut' -- och syn.se ar kandidatlista, "
      "aldrig belagg (regel 2 och 3). Kortet kan inte bli full v3 utan att "
      "hela betydelsen vilar pa en icke-ordbokskalla. Pausat, inte underkant: "
      "ordet finns sannolikt i SAOB under en annan stavning (schvejfa/svejfa) "
      "och kan tas upp igen nar den kontrollerats.")

# ---------------------------------------------------------------- 4. propa
satt("propå",
     "Preliminärt förslag som läggs fram för att prövas",
     "formell, neutral",
     ["förslag"],
     "Styrelsen sa nej till varje " + B % "propå" + " om att sälja fastigheten.",
     "av franskans propos 'förslag, yttrande', av latinets proponere "
     "'lägga fram'; jämför proposition och förespråka",
     "SO: '(preliminart) forslag'. SAOL: 'forslag'. En betydelse. Synonymen "
     "forslag inleder bada ordbockernas definition och ar utbytbar at bada "
     "hallen, alltsa belagd enligt regel 2. syn.se:s ovriga forslag (invit, "
     "pastotning, framstot, propos) star inte i nagon ordboksdefinition och "
     "skrivs darfor inte in.")

# ------------------------------------------------------------------ 5. stor
satt("stör",
     "Tillspetsad stång av trä som slås ner i marken ; typ av stor strålfenig "
     "fisk med broskskelett och utdraget nosparti",
     "neutral, neutral ; neutral, neutral, biologi",
     ["stång", "trädstam"],
     "Bönderna slog ner en " + B % "stör" + " vid varje tomatplanta.",
     "fornsvenska stör 'påle, stång'; fisknamnet kommer av lågtyskans stör, "
     "besläktat med tyskans Stör",
     "SO haller isar tva substantivbetydelser: 'stang av tra' och 'typ av "
     "(stor) stralfenig fisk som har broskartat skelett och utdraget "
     "nosparti'. De skrivs som tva betydelser, inte en (regel 1). SO:s ovriga "
     "traffar ('avbryta nagon i vila', 'oroa, irritera', 'forsvara "
     "radiokommunikation') tillhor verbet stora och ar en annan homograf -- "
     "de hor inte till det har substantivkortet. Synonymer: stang inleder "
     "SO:s definition, tradstam inleder SAOL:s 'tillspetsad mindre "
     "tradstam'. Fisken har ingen belagd synonym.",
     grupper=[["stång", "trädstam"], []])

# ---------------------------------------------------------------- 6. stigma
satt("stigma",
     "Sårmärke som anses likna dem Jesus fick vid korsfästelsen ; synligt "
     "tecken på psykisk sjukdom ; negativt socialt kännetecken som gör att "
     "omgivningen ser ner på någon",
     "formell, neutral, religion ; fackspråklig, neutral, medicin ; "
     "neutral, negativ, samhälle",
     ["sårmärke"],
     "Psykisk ohälsa bär fortfarande ett " + B % "stigma" + " som gör att "
     "många drar sig för att söka hjälp.",
     "av grekiskans stigma 'stickmärke, brännmärke', av stizein 'sticka, "
     "märka'; slavar och brottslingar brändes med ett märke i antikens "
     "Grekland",
     "SO haller isar tre betydelser: 'sar som anses likna dem som Jesus fick "
     "vid korsfastelsen', '(synligt) tecken pa psykisk sjukdom' och 'negativt "
     "socialt kannetecken'. Alla tre skrivs ut (regel 1). Synonymen sarmarke "
     "inleder SAOL:s definition 'sarmarke liknande Jesu sar' och hor till "
     "forsta betydelsen. SAOL:s 'vanarande kannetecken' ar modifierat och "
     "belagger darfor inte kannetecken ensamt (samma provning som falide "
     "farsot for pandemi).",
     grupper=[["sårmärke"], [], []])


json.dump(KORT, io.open(FIL, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
skrivna = sum(1 for k in KORT if k.get("proposed"))
pausade = sum(1 for k in KORT if k.get("v3_pausad"))
print("del 1 klar: %d skrivna, %d pausade, %d kvar av 40"
      % (skrivna, pausade, 40 - skrivna - pausade))
