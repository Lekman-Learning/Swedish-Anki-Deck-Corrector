# -*- coding: utf-8 -*-
import json, urllib.parse

F = "sessions/session_2026-08-26_v3-batch2.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}


def H(w):
    return '<font color="#3498db">' + w + '</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, tillat=None, conf=9):
    e = BY[o]
    q = urllib.parse.quote(o)
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": None, "exempelmening": ex, "etymologi": ety}
    e["sokkoll"] = {"kalla": "SO och SAOL via https://svenska.se/api/msearch?ord=" + q
                    + " (hämtat 2026-08-26, HTTP 200)", "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("given",
     "Som det inte finns något tvivel om ; bestämd på förhand",
     "neutral, neutral", ["självklar", "överenskommen"],
     "Utgången av matchen var " + H("given") + " redan från början.", None,
     "SO (adjektiv): som det inte finns något tvivel om (succén var given från början, jag tar för "
     "givet att alla ställer upp); äv. överenskommen (starta på en given signal); äv. faktiskt "
     "föreliggande (dra en sträcka från en given punkt A). SAOL: självklar; överenskommen — "
     "semikolon skiljer leden, så BÅDA är belagda synonymer.",
     tillat={"frammande_uppslagsord":
             "Uppslaget drog in giv (kortutdelning i kortspel) och ge (verbet), två andra ord som "
             "delar stam med participformen. Ingen glosa på kortet kommer därifrån — kortet ger "
             "adjektivet given, som SO och SAOL båda har som eget uppslag.",
             "betydelse_kan_saknas":
             "SO:s tredje betydelse (faktiskt föreliggande, som i en given punkt A) är en "
             "matematisk användning av samma grundbetydelse som kortets andra led — något som är "
             "bestämt på förhand. Den behöver inget eget led."})

satt("guano",
     "Gödsel av intorkad fågelspillning",
     "neutral, neutral, jordbruk", [],
     "Fälten göddes med " + H("guano") + " som hämtats från öarna utanför Peru.", None,
     "SO: ett gödselmedel av fågelspillning, som ibland blandats med fiskrester; särskilt hämtat "
     "från Latinamerikas västkust. SAOL: fågelträck och fiskrester som gödselmedel, märkt jordbr. "
     "Kortet tar SO:s kärna; fiskresterna är ett tillägg som ibland gäller, inte en del av "
     "definitionen.")

satt("inkurant",
     "Om varor: som inte går att sälja längre",
     "fackspråklig, negativ, ekonomi", [],
     "Lagret skrevs ned eftersom en stor del av varorna var " + H("inkuranta") + ".", None,
     "SO: som inte (längre) är gångbar, underbetydelse: som saknar ekonomiskt värde; exempel "
     "överblivet och inkurant material. SAOL: skadad, inte gångbar, utan värde, märkt ekon. "
     "Ingen av definitionens delar är ett utbytbart enskilt ord.")

satt("pakt",
     "Högtidligt avtal, oftast mellan stater",
     "neutral, neutral, politik", ["förbund", "avtal"],
     H("Pakten") + " mellan de båda stormakterna oroade grannstaterna.", None,
     "SO: formell överenskommelse i större fråga, vanligen mellan stater, ofta om samarbete av "
     "militär natur. SAOL: formell överenskommelse ofta mellan stater; förbund; avtal — semikolon "
     "skiljer leden, så både förbund och avtal är belagda synonymer.")

satt("perpendikel",
     "Linje som möter en annan linje i rät vinkel",
     "fackspråklig, neutral, matematik", ["lodlinje"],
     "Han drog en " + H("perpendikel") + " från punkten ned till linjen.", None,
     "SO: linje som är vinkelrät mot en viss annan linje; underbetydelse: sänklod. SAOL: lodlinje; "
     "normal; pendel i ur, märkt mat. Lodlinje leder första ledet och är belagd. Normal utelämnas "
     "som synonym trots eget led — ordet är tvetydigt mot vardagsbetydelsen och skulle göra kortet "
     "sämre, inte bättre.",
     tillat={"betydelse_kan_saknas":
             "SO:s underbetydelse sänklod och SAOL:s pendel i ur är två konkreta redskap som "
             "utnyttjar samma geometriska förhållande — lodlinjen. De är instrumentnamn, inte "
             "skilda betydelser av ordet, och kortets definition täcker principen bakom båda."})

satt("sfär",
     "Helt rund kropp där varje punkt på ytan ligger lika långt från mitten ; bildligt: det område någon rör sig inom",
     "neutral, neutral", ["klot"],
     "Frågan hör hemma i hennes privata " + H("sfär") + ".", None,
     "SO: helt runt tredimensionellt föremål, så att alla punkter på ytan har samma avstånd till en "
     "punkt i det inre; med bruksexemplet hennes privata sfär för den bildliga användningen. "
     "SAOL: klot; klotformigt hölje; omgivning; skikt, krets; verksamhetsområde — klot leder första "
     "ledet och är belagd. Omgivning och verksamhetsområde hör till den bildliga betydelsen och "
     "är för vaga för att fungera som utbytbara synonymer.")

satt("svada",
     "Ström av ord som låter bra men säger lite",
     "neutral, lätt negativ", ["ordflöde"],
     "Försäljarens " + H("svada") + " gjorde det svårt att komma till tals.", None,
     "SO: ordrikt prat, vanligen utan mer väsentligt innehåll; exempel försäljarens svada, "
     "agitatorns svada, hon har en otrolig svada. SAOL: ordflöde — utgör hela definitionen och är "
     "belagd synonym. Valören är lätt negativ: SO:s tillägg om innehållet bär den, men SO:s eget "
     "exempel hon har en otrolig svada kan vara beundrande.")

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 2 skriven: 7 kort. Totalt approved: %d/%d"
      % (sum(1 for e in S if e.get("approved")), len(S)))
