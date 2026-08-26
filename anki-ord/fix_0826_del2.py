# -*- coding: utf-8 -*-
import json

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}

# --- RIKTIGT FIX: tentakel saknade den bildliga betydelsen ---
t = BY["tentakel"]["proposed"]
t["huvudbetydelse"] = ("Smalt, rörligt spröt som djur känner och griper med ; utsträckt gren av "
                       "någon som i hemlighet söker inflytande")
BY["tentakel"]["sokkoll"]["slutsats"] = (
    "SO: smal, lättrörlig, utskjutande kroppsdel, vanligen med känselnerver; äv. bildligt i uttryck "
    "för att någon i hemlighet försöker påverka eller skaffa sig upplysningar (exempel storklubben "
    "har sänt ut sina tentakler). SAOL: känselspröt; fångarm. Rättat 2026-08-26: den bildliga "
    "betydelsen var först utelämnad — den är väl belagd och tas med.")

TILLAT = {
    "anfäktelse": {
        "betydelse_kan_saknas":
            "SO:s fyra poster är två betydelser plus markörerna ibland spec. och numera ofta "
            "skämtsamt. Båda betydelserna — själslig oro eller plåga, och frestelse — finns på kortet.",
        "synonym_saknas_trots_belagg":
            "Frestelse är kortets andra betydelse, inte en synonym till den första. Själslig är "
            "ett adjektiv ur definitionen. Tom lista är rätt svar."},
    "betvingande": {
        "frammande_uppslagsord":
            "Det enda främmande uppslagsordet är betvinga, verbet som particip­formen betvingande "
            "bildas av. Samma ord i annan form, inte ett annat uppslag — ingen risk för fel glosor.",
        "betydelse_kan_saknas":
            "SO:s fem poster tillhör till största delen verbet betvinga (kämpa ner motståndet hos, "
            "hänföra) plus tre markörer. Kortet gäller participet betvingande, som SO redovisar med "
            "en enda betydelse: som bryter ner allt motstånd (exempel hans betvingande personlighet)."},
    "bistå": {
        "betydelse_kan_saknas":
            "SO:s andra post är markören spec. i vissa bibliskt färgade uttryck (vi bör hjälpa och "
            "bistå vår nästa) — samma betydelse i en fast vändning, inte en egen. En betydelse är rätt."},
    "drastisk": {
        "betydelse_kan_saknas":
            "SO:s tredje post är markören äv. bildligt. Båda faktiska betydelserna — kraftigt "
            "verkande och chockerande, burdus — finns på kortet."},
    "folklig": {
        "betydelse_kan_saknas":
            "SO:s två definitioner (som tillhör de breda folklagren; som har att göra med folkets "
            "breda lager) är samma betydelse formulerad två gånger, plus markören äv. om högt "
            "uppsatt person — som kortets exempelmening (patron var riktigt folklig) täcker.",
        "synonym_saknas_trots_belagg":
            "Populär står efter komma i SAOL:s led för vanligt folk, populär och inleder inget eget "
            "led. Dessutom är folklig och populär inte utbytbara: en populär artist behöver inte "
            "vara folklig. Tom lista är rätt svar."},
    "jordbunden": {
        "betydelse_kan_saknas":
            "SO:s tredje post är markören ofta bildligt om person. Båda betydelserna — som inte kan "
            "lyfta från marken, och som inte hänger sig åt fantasier — finns på kortet."},
    "saxa": {
        "betydelse_kan_saknas":
            "SO:s sex poster är tre betydelser plus tre markörer. Kortet har ställa i kors och "
            "klippa ut; SO:s tredje, citera, är inte fristående utan anges av SAOL som klippa ut ur "
            "tidning, ofta i avsikt att citera — vilket är ordagrant kortets andra led."},
    "acklimatisera": {
        "betydelse_kan_saknas":
            "SO:s andra post är markören spec. i fråga om tillvänjning till klimatförhållanden — "
            "samma betydelse med snävare tillämpning. Kortets formulering nytt klimat eller nya "
            "förhållanden täcker båda."},
}

for o, d in TILLAT.items():
    BY[o].setdefault("forgranska_tillat", {}).update(d)

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Tentakel utökad med bildlig betydelse. Motiveringar på %d kort." % len(TILLAT))
