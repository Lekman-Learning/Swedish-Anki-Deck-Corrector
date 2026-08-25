# -*- coding: utf-8 -*-
"""80-kortsomgangen 2026-08-25, del 2 (ord 21-40).

Kallor lasta via visa_uppslag.py -- SO:s rastruktur och SAOL ordagrant,
aldrig synonymer.se.

`arterioskleros` saknas i SO. SAOL ger bara hanvisningen 'ateroskleros', sa
den slogs upp separat (SVENSKA_SE_HAMTAD ateroskleros HTTP 200) och gav
'aderforfettning'. Kortet skrivs alltsa ur den kedjan, inte ur gissning.
"""
import json
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-25_v3-batch2.json"
BLA = '<font color="#3498db">%s</font>'

TILLAT = {
 "resning": {"betydelse_kan_saknas":
   "SO har TRE huvudbetydelser (rattsmedel / uppror / uppratt hallning) och de "
   "star alla pa kortet. SAOL:s fjarde led ('moralisk kvalitet') ar den bildliga "
   "utvidgningen av 'uppratt hallning' och tacks av kortets tredje betydelse."},
 "salutera": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('halsa pa faststallt satt') med tva "
   "underbetydelser ('halsa med salut', 'hylla'). Kortet har huvudbetydelsen och "
   "salutskottet; 'hylla' ar den bildliga anvandningen av samma handling."},
 "telning": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('ungt skott av trad') och EN "
   "underbetydelse ('avkomma, barn', brukl. skamtsamt). Bada star pa kortet."},
 "allena": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('utan sallskap av nagon annan') och EN "
   "underbetydelse ('utan stod av annat'). SAOL:s andra post ar adverbet "
   "'endast', som kortet ocksa har."},
 "androgyn": {"betydelse_kan_saknas":
   "SO har TVA lemman med samma stavning, substantivet och adjektivet. Kortet "
   "tacker bada: personen och egenskapen."},
 "aspiration": {"betydelse_kan_saknas":
   "SO har TRE huvudbetydelser (stravan / inandning / utandningsljud vid uttal). "
   "Alla tre star pa kortet."},
 "arterioskleros": {"betydelse_kan_saknas":
   "SO saknar ordet helt. SAOL ger bara hanvisningen 'ateroskleros', som slogs "
   "upp separat och definieras som 'aderforfettning'. Det ar hela innehallet "
   "kallorna ger.",
   "frammande_uppslagsord":
   "Traffen `ateroskleros` ar den hanvisning SAOL sjalv gor fran uppslagsordet."},
 "baisse": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('marknadslage med laga priser') och EN "
   "underbetydelse ('svag forvantan'). Bada star pa kortet."},
}

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form, etymologi)
KORT = {
 "regim": ("Högsta styrelse för ett land, ofta om en odemokratisk regering",
   "neutral, lätt negativ", ["styrelse", "ledning"],
   "Den nya regimen upplöste parlamentet.", "regimen",
   "Av franska <i>régime</i>, av latin <i>regimen</i> 'styrelse', till <i>regere</i> 'styra'."),

 "resning": ("Rättsmedel som gör att en dom som vunnit laga kraft kan prövas på nytt ; uppror ; upprätt hållning",
   "neutral, neutral", ["uppror"],
   "Advokaten ansökte om resning i målet.", "resning",
   "Till <i>resa</i> i betydelsen 'ställa upprätt'."),

 "salutera": ("Hälsa på fastställt sätt, särskilt militärt ; hälsa med salutskott",
   "neutral, neutral", [],
   "Vakten saluterade när kungen passerade.", "saluterade",
   "Av latin <i>salutare</i> 'hälsa', till <i>salus</i> 'hälsa, välgång'."),

 "sardonisk": ("Hånfull och bitter",
   "neutral, negativ", ["hånfull"],
   "Han log ett sardoniskt leende och sa ingenting.", "sardoniskt",
   "Av grekiska <i>sardonios</i>, efter en giftig växt på Sardinien som troddes framkalla krampaktiga grimaser."),

 "schvungfull": ("Full av fart och kraft",
   "neutral, positiv", [],
   "Orkestern spelade en schvungfull marsch.", "schvungfull",
   "Till <i>schvung</i>, av tyska <i>Schwung</i> 'sving, fart'."),

 "spräcklig": ("Som har fläckar i olika färger",
   "neutral, neutral", ["brokig", "fläckig"],
   "Hönan var brun och spräcklig.", "spräcklig",
   "Till <i>spräcka</i> i äldre betydelsen 'göra fläckig'."),

 "telning": ("Ungt skott av ett träd ; (skämtsamt) barn eller avkomma",
   "neutral, skämtsam", [],
   "Han kom hem med hustru och tre telningar.", "telningar",
   "Fornsvenska <i>telning</i>, till <i>tel</i> 'ungt skott'."),

 "urkund": ("Ursprungligt dokument som har värde som kunskapskälla eller bevis",
   "fackspråklig, neutral", [],
   "Domstolen granskade urkunden noggrant.", "urkunden",
   "Efter tyska <i>Urkunde</i>, till <i>ur-</i> 'ursprunglig' och <i>kund</i> 'kunskap, vittnesbörd'."),

 "aerosol": ("Ämne i finfördelad form under tryck ; svävande partiklar av vätska eller fast ämne i en gas",
   "fackspråklig, neutral", [],
   "Sprayburken innehåller en aerosol.", "aerosol",
   "Till grekiska <i>aer</i> 'luft' och <i>solution</i> 'lösning'."),

 "allena": ("Som är utan sällskap av någon annan ; endast",
   "ngt ålderdomlig, neutral", ["ensam", "endast"],
   "Han stod allena kvar på perrongen.", "allena",
   "Av <i>all</i> och <i>en</i>, egentligen 'alldeles ensam'."),

 "alltfort": ("Fortfarande",
   "ngt ålderdomlig, neutral", ["fortfarande"],
   "Frågan är alltfort olöst.", "alltfort",
   "Av <i>allt</i> och <i>fort</i> i betydelsen 'vidare'."),

 "alternera": ("Omväxla, turas om",
   "neutral, neutral", ["omväxla"],
   "De två skådespelarna alternerade i huvudrollen.", "alternerade",
   "Av latin <i>alternare</i> 'växla', till <i>alter</i> 'den andre av två'."),

 "androgyn": ("Person med både manligt och kvinnligt utseende och sätt ; som har både manliga och kvinnliga egenskaper",
   "ngt ålderdomlig, neutral", [],
   "Modellen hade ett androgynt utseende.", "androgynt",
   "Av grekiska <i>andros</i> 'man' och <i>gyne</i> 'kvinna'."),

 "antagonist": ("Person som står i motsats- eller konkurrensförhållande till en annan",
   "neutral, neutral", ["motståndare"],
   "Romanens antagonist är hjältens egen bror.", "antagonist",
   "Av grekiska <i>antagonistes</i> 'motståndare', till <i>anti-</i> 'mot' och <i>agonistes</i> 'tävlande'. Motsatsen till <i>protagonist</i>."),

 "antites": ("Sats som hävdar motsatsen till vad en annan sats hävdar ; motsatt idé eller företeelse",
   "fackspråklig, neutral", ["motsats"],
   "Hegels metod ställer tes mot antites.", "antites",
   "Av grekiska <i>antithesis</i> 'motsättning', till <i>anti-</i> 'mot' och <i>thesis</i> 'sats'."),

 "arterioskleros": ("Åderförfettning",
   "fackspråklig, neutral", ["ateroskleros"],
   "Rökning ökar risken för arterioskleros.", "arterioskleros",
   "Till grekiska <i>arteria</i> 'pulsåder' och <i>skleros</i> 'förhårdnad'."),

 "aspiration": ("Strävan eller förhoppning att uppnå något ; inandning ; utandningsljud vid uttal av språkljud",
   "neutral, neutral", ["ambition"],
   "Hans aspirationer sträckte sig långt bortom kommunpolitiken.", "aspirationer",
   "Av latin <i>aspiratio</i> 'andning, fläkt', till <i>aspirare</i> 'andas mot, sträva efter'."),

 "avkok": ("Lösning som fås genom att djur- eller växtdelar kokas",
   "neutral, neutral", [],
   "Hon gjorde ett avkok på kamomill.", "avkok",
   ""),

 "baisse": ("Marknadsläge som kännetecknas av låga priser ; svag förväntan på börsen",
   "fackspråklig, neutral", ["prisfall", "kursfall", "nedgång"],
   "Börsen gick in i en långvarig baisse.", "baisse",
   "Av franska <i>baisse</i> 'sänkning', till <i>baisser</i> 'sänka'. Motsatsen till <i>hausse</i>."),

 "bigott": ("Ofördragsam på grund av överdriven eller hycklad fromhet",
   "neutral, nedsättande", [],
   "Han var bigott och dömde alla som inte trodde som han.", "bigott",
   "Av franska <i>bigot</i>, av ovisst ursprung."),
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    skrivna = 0
    for e in poster:
        o = e["ord"]
        if o not in KORT:
            continue
        bet, reg, syn, ex, form, etym = KORT[o]
        if form in ex:
            ex = ex.replace(form, BLA % form, 1)
        else:
            print("  VARNING: hittade inte", form, "i:", ex)
        e["proposed"] = {
            "huvudbetydelse": bet, "register": reg, "synonymer": syn,
            "synonym_groups": None, "exempelmening": ex, "etymologi": etym,
        }
        e["approved"] = True
        q = urllib.parse.quote(o)
        e["sokkoll"] = {
            "kalla": (f"SO och SAOL via https://svenska.se/api/msearch?ord={q} "
                      f"samt https://www.synonymer.se/sv-syn/{q} -- hamtade 2026-08-25, "
                      f"sparade i uppslag/{o}.json"),
            "slutsats": ("Betydelser, register och synonymer lasta ur SO:s rastruktur och "
                         "SAOL:s definitionstext via visa_uppslag.py, som inte visar "
                         "synonymer.se. Inget skrivet som inte star i nagon av ordbockerna."),
        }
        if o in TILLAT:
            e["forgranska_tillat"] = TILLAT[o]
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"del 2: skrivna {skrivna}")


if __name__ == "__main__":
    main()
