# -*- coding: utf-8 -*-
"""Rättar de två kort blindgranskaren underkände 2026-08-26 (batch 2)."""
import json

F = "sessions/session_2026-08-26_v3-batch2.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}


def H(w):
    return '<font color="#3498db">' + w + '</font>'


# --- rygga -----------------------------------------------------------------
# Granskaren har rätt: ridbetydelsen är TRANSITIV (rygga hästen) och alltså en
# egen betydelse, inte samma handling sedd utifrån. OLD-facit pekar dessutom
# rakt på den med 'backa'. Min motivering (fackspråk inom sport) höll inte.
p = BY["rygga"]["proposed"]
p["huvudbetydelse"] = ("Ta ett steg bakåt av rädsla eller olust ; få en häst att gå bakåt")
BY["rygga"]["sokkoll"]["slutsats"] += (
    " 🔴 RÄTTAT efter blindgranskning: ridbetydelsen (rygga hästen) lades till. Den är "
    "TRANSITIV — man ryggar något — och därmed en egen betydelse, inte samma rörelse sedd "
    "utifrån. OLD-facit pekar på den med backa. Min första motivering (fackspråk inom sport, "
    "kan utelämnas) höll inte.")
BY["rygga"]["forgranska_tillat"]["betydelse_kan_saknas"] = (
    "SO har två skilda uppslag på formen. Kortet ger verbets båda betydelser: den "
    "intransitiva (dra sig tillbaka, inklusive underbetydelsen känna motvilja för något) och "
    "den transitiva (få häst att gå bakåt). Utelämnat: substantivet rygga = ryggsäck, en "
    "vardaglig kortform av ett ord Adam redan kan.")

# --- perpendikel -----------------------------------------------------------
# Granskaren har rätt på den viktigare punkten: lodlinje är INTE utbytbar mot
# normal. En lodlinje är lodrät av tyngdkraften; en perpendikel kan stå
# vinkelrätt i vilken riktning som helst. Synonymen stryks och de två konkreta
# betydelserna skrivs ut.
p = BY["perpendikel"]["proposed"]
p["huvudbetydelse"] = ("Linje som möter en annan linje i rät vinkel ; lodrätt hängande "
                       "snöre med vikt, som visar lodlinjen ; pendeln i ett golvur")
p["synonymer"] = []
p["exempelmening"] = ("Han drog en " + H("perpendikel") + " från punkten ned till linjen.")
BY["perpendikel"]["sokkoll"]["slutsats"] = (
    "SO: linje som är vinkelrät mot en viss annan linje; underbetydelse: sänklod. "
    "SAOL: lodlinje; normal; pendel i ur, märkt mat. — tre led åtskilda med semikolon, "
    "alltså tre skilda betydelser. "
    "🔴 RÄTTAT efter blindgranskning, på granskarens starkare argument: lodlinje är INTE "
    "utbytbar mot normal. En lodlinje är lodrät därför att tyngdkraften gör den lodrät; en "
    "perpendikel kan stå vinkelrätt mot vad som helst i vilken riktning som helst. "
    "Synonymen stryks därför helt, och de två konkreta betydelserna (sänklodet och urpendeln) "
    "skrivs ut som egna led i stället för att motiveras bort. Min första motivering — att de "
    "vore instrumentnamn för samma geometriska princip — var en efterhandskonstruktion.")
BY["perpendikel"].pop("forgranska_tillat", None)

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 4: rygga och perpendikel omskrivna.")
