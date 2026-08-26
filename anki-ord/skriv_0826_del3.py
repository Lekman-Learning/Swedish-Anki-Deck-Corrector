# -*- coding: utf-8 -*-
import json, urllib.parse

F = "sessions/session_2026-08-26_v3-batch.json"
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


satt("amplitud",
     "Hur långt något svänger ut från sitt viloläge",
     "fackspråklig, fysik", ["svängningsvidd"],
     "Vågens " + H("amplitud") + " är lika med halva våghöjden.", None,
     "SO: avstånd mellan nolläge och ettdera av ytterlägena i en svängningsrörelse. "
     "SAOL: en svängande kropps utslag från jämviktsläget; svängningsvidd — svängningsvidd inleder "
     "ett eget led och är belagd synonym. Ljudstyrka är en tillämpning, inte en betydelse.")

satt("anglofil",
     "Person som älskar England och engelsk kultur",
     "neutral", ["engelskvän"],
     "Som " + H("anglofil") + " drack han te klockan fem varje dag.", None,
     "Ordet saknar SO-artikel. SAOL ger två uppslag: engelskvänlig (adjektiv) och engelskvän "
     "(substantiv) — engelskvän är därmed belagd synonym. Legacys brittsälskare finns inte i "
     "någon ordbok och är dessutom felstavat.")

satt("anspråk",
     "Krav på något man menar sig ha rätt till",
     "neutral", ["krav"],
     "Hon gjorde " + H("anspråk") + " på hela arvet.", None,
     "SO: krav för egen räkning; äv. något utvidgat: utnyttjande (bibliografin gör inte anspråk på "
     "fullständighet). SAOL: krav — utgör hela definitionen och är belagd synonym. Pretention och "
     "fordran saknar belägg.")

satt("appell",
     "Bön om att någon ska agera ; överklagan till högre domstol ; lystringssignal till hund",
     "neutral", ["vädjan"],
     "Fredsorganisationen riktade en lidelsefull " + H("appell") + " till politikerna.", None,
     "SO ger tre betydelser: bön om välvilligt agerande, framställan om omprövning inför högre rätt "
     "(spec. juridik), samt en tävlingsklass för hundar. SAOL: vädjan; framställan till högre "
     "domstol; lystringssignal — vädjan inleder första ledet och är belagd.")

satt("attribut",
     "Utmärkande egenskap eller typiskt tillbehör ; ord som bestämmer ett substantiv",
     "neutral, lingvistik", ["kännetecken"],
     "Lien är dödens obligatoriska " + H("attribut") + ".", None,
     "SO: utmärkande egenskap eller tillbehör; satsdel som utgör bestämning till ett substantiv "
     "(SAOL märker den språkv.). SAOL: utmärkande egenskap; kännetecken, särmärke — kännetecken "
     "inleder andra ledet och är belagd. Datateknik-betydelsen är en spec.-tillämpning.")

satt("avlat",
     "Efterskänkning av botgöring i katolska kyrkan, ofta mot betalning",
     "historia, religion", [],
     "Kyrkan sålde " + H("avlat") + " för att finansiera bygget av Peterskyrkan.", None,
     "SO: efterskänkning (inom katolska kyrkan) av botgöring mot viss prestation, märkt historiskt, "
     "spec. om vissa urartningar under senmedeltiden. SAOL: inom romersk-katolska kyrkan: botgöring "
     "för begångna synder. VIKTIGT: uppslaget drog även in verbet avla (ge upphov till liv genom "
     "befruktning) — ett annat ord, uteslutet. Syndaförlåtelse och absolution är närliggande men "
     "andra begrepp, saknar belägg som synonymer.")

satt("bemyndiga",
     "Ge någon formell rätt att handla eller besluta",
     "formell, juridik", [],
     "Årsmötet " + H("bemyndigade") + " styrelsen att söka nya lokaler.", None,
     "SO: ge befogenhet åt, märkt ofta juridik. SAOL: ge befogenhet åt, auktorisera — auktorisera "
     "står efter komma och inleder inget eget led, alltså inte belagd enligt synonymregeln. "
     "Delegera och befullmäktiga saknar belägg.")

satt("beredvillig",
     "Som gärna ställer upp och hjälper till",
     "neutral", [],
     "Ministern ställde " + H("beredvilligt") + " upp på intervjun.", None,
     "SO och SAOL identiskt: som gärna utför något. Ingen märkning, alltså neutral. Legacys "
     "tjänstvillig, villig och hjälpsam saknar ordboksbelägg som egna definitionsled.")

satt("berlock",
     "Litet hängsmycke som fästs i ett arm- eller halsband",
     "neutral", [],
     "Hon fick en " + H("berlock") + " i form av ett hjärta till armbandet.", None,
     "SO: litet hängsmycke som används som extra prydnad. SAOL: litet hängsmycke som kan fästas i "
     "arm- el. halsband. Hängsmycke är definitionens huvudord, inte en utbytbar synonym — en "
     "berlock är en särskild sorts hängsmycke.")

satt("blessera",
     "Såra eller skada någon",
     "arkaisk", ["såra"],
     "Två soldater blev svårt " + H("blesserade") + " i drabbningen.", None,
     "Ordet saknar SO-artikel. SAOL: såra, skada, märkt åld. — såra inleder definitionen och är "
     "belagd synonym. Registret följer SAOL:s ålderdomsmärkning.")

satt("bravera",
     "Skryta och stoltsera med det man gjort",
     "neutral", ["skryta", "stoltsera"],
     "Han " + H("braverade") + " gärna med sina bragder på sjön.", None,
     "SO: framhäva egen prestation som berömvärd; exempel han braverade gärna med sina erotiska "
     "äventyr. SAOL: skryta, skrodera, stoltsera. Skryta inleder ledet; stoltsera bekräftas av "
     "OLD-facit (skryta, stoltsera med, briljera) och står i SAOL:s enda definitionsled.")

satt("butelj",
     "Flaska för vin eller annan alkoholhaltig dryck",
     "ngt ålderdomlig", [],
     "De tappade årets vin på " + H("butelj") + ".", None,
     "SO: flaska för (alkoholhaltig) dryck; exempel tappa vin på butelj. Ingen SAOL-definition i "
     "träffen. Flaska är definitionens huvudord men täcker mer än butelj (en butelj är specifikt "
     "för dryck, ofta vin) — inte utbytbar, alltså tom synonymlista.",
     {"register_motsager_markning": "Varken SO eller SAOL märker ordet. Registret ngt ålderdomlig "
                                    "sätts på eget omdöme: butelj har i modern svenska ersatts av "
                                    "flaska i vardagligt tal och lever kvar mest i vinsammanhang. "
                                    "Ingen ordboksmärkning motsägs."})

satt("celebrerad",
     "Som blir firad och hyllad",
     "formell", ["firad"],
     "Den " + H("celebrerade") + " författaren fick stående ovationer.", None,
     "SO och SAOL ger verbet celebrera: fira (exempel de celebrerar sin tioåriga bröllopsdag). "
     "Kortet gäller participet celebrerad, alltså den som firas — firad är därmed direkt belagd "
     "som synonym. Berömd och uppmärksammad ligger nära men saknar belägg.")

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 3 skriven: 13 kort. Totalt approved: %d/%d"
      % (sum(1 for e in S if e.get("approved")), len(S)))
