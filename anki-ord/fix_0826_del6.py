# -*- coding: utf-8 -*-
import json

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}

# --- svarighetskoll: omskrivning, inte synonymbyte ---
BY["försåt"]["proposed"]["huvudbetydelse"] = \
    "Att gömma sig och vänta på rätt tillfälle att överfalla någon"
BY["gillestuga"]["proposed"]["huvudbetydelse"] = \
    "Sällskapsrum i källaren, ofta med trä och mysig inredning"

# --- register: SO marker linberedningen 'mest historiskt' ---
BY["häckla"]["proposed"]["register"] = "neutral, historia"

TILLAT = {
    "fossil": {"betydelse_kan_saknas":
        "SO:s fyra poster är tre definitioner plus en markör. De två första — adjektivet (som "
        "utgör förmultnad rest) och substantivet (bevarad rest) — är samma sak i olika ordklass "
        "och står som kortets första led. Den bildliga om otidsenlig person är kortets andra led."},
    "försåt": {"betydelse_kan_saknas":
        "SO:s tre poster är en definition (dold förberedelse för överfall), markören äv. konkret "
        "med betydelsen bakhåll, plus en cohyponym-markör. Bakhåll och dold förberedelse är samma "
        "sak sedd abstrakt respektive konkret — kortets formulering täcker båda."},
    "gnatig": {"betydelse_kan_saknas":
        "SO:s andra post är markören äv. om handling och dylikt (hennes gnatiga ton) — samma "
        "egenskap överförd från person till yttrande, inte en skild betydelse."},
    "häckla": {
        "betydelse_kan_saknas":
            "SO:s sju poster är fem betydelser plus två markörer. Kortet har de två som bär "
            "ordförrådet: linberedningen (ordets ursprung, mest historiskt) och den bildliga om "
            "att angripa någon verbalt. SO:s tredje (hånfullt kritisera) är en gradskillnad mot "
            "den andra, inte en egen betydelse. De två redskapsbetydelserna — häcklan för lin och "
            "ett fiskredskap — är konkreta föremål med samma namn; att lägga in dem skulle göra "
            "kortet till en uppräkning i stället för en förklaring.",
        "synonym_saknas_trots_belagg":
            "SAOL:s nagelfara är belagd men SVÅRARE än häckla — att sätta den skulle förklara "
            "svårt med svårt, vilket är precis den regel som skärptes 2026-08-26. Kritisera står "
            "efter komma och inleder inget eget led. Övriga kandidater är definitionsverb. "
            "Tom lista är rätt svar."},
    "högrest": {"betydelse_kan_saknas":
        "SO:s andra post är markören äv. om djur med stor utsträckning i höjdled — samma egenskap "
        "överförd från människa till djur. Kortets formulering nämner ingen art och täcker båda; "
        "exempelmeningen är SO:s egen om gasellen."},
}

for o, d in TILLAT.items():
    BY[o].setdefault("forgranska_tillat", {}).update(d)

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("2 omskrivna, häcklas register rättat, motiveringar på %d kort." % len(TILLAT))
