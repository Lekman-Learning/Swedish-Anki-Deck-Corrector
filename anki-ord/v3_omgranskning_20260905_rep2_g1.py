# -*- coding: utf-8 -*-
"""Spar B (omgranskning), session_2026-09-05_v3-omgranskning-repetition2.json.
Grupp 1, ord 1-8 (algoritm .. totem). Sokkoll via slaupp.py --tyst (kord separat,
bevisraderna star i sessionens eget transkript)."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-05_v3-omgranskning-repetition2.json"
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"algoritm": dict(
  unchanged=False,
  hb="Steg-för-steg-metod för att lösa ett matematiskt problem, till exempel i ett datorprogram",
  reg="fackspråklig, neutral, IT",
  grp=[["instruktionsföljd"]],
  ex='Euklides <font color="#3498db">algoritm</font> hittar den största gemensamma delaren till två tal.',
  etym="via engelska av medeltidslatin algorismus med samma betydelse; till namnet på den arabiske "
       "matematikern al-Chwarizmi (800-talet)",
  sl="SO: 'instruktionsföljd för lösning av problem' med definitionstillägget 'av (mer el. mindre) "
     "matematiskt slag', bruklighetskommentar 'matematik, informationsteknik m.m.' -- legacys 'ett "
     "problem' utan denna kvalificering var för brett, tillägget nu med. SAOL: 'modell för uträkning, "
     "räknemönster' (komma, samma betydelse, inget nytt led). 'instruktionsföljd' inleder SO:s led "
     "ordagrant -- belagd, oförändrad. Exempelmeningen var redan korrigerad (delaren, inte 'talet') och "
     "matchar SO:s syntex 'Euklides algoritm för att finna minsta gemensamma nämnare' i sak (SGD). "
     "Etymologin matchar SO:s historiskaUppgifter ordagrant, oförändrad."),

"basse": dict(
  hb="En vanlig soldat utan grad ; en ohyfsad, grov man eller pojke",
  reg="ngt ålderdomlig, nedsättande",
  grp=[["menig värnpliktig"], ["≈≈ ohyfsad person"]],
  ex='Ivan var en gång en <font color="#3498db">basse</font> i den svenska armén.',
  etym="jfr fornsvenska basse 'vildgalt'; svensk dialekt även 'stor oxe; grovt vuxen karl'; jfr "
       "ursprung till bjässe",
  sl="SAKNAD BETYDELSE. SO: huvudbetydelse 'menig värnpliktig' [ålderdomligt el. nedsättande] MEN har "
     "en underbetydelse med EGEN definitionstext (typ 'ursprungligen'): 'ohyfsad man eller pojke' -- "
     "en riktig andra betydelse, inte en utvidgning utan innehåll. OLD-facit bekräftar direkt: "
     "'rekryt, tölp' -- tölp = ohyfsad/burdus man, exakt den saknade betydelsen. Etymologin (redan på "
     "kortet, oförändrad) styrker det ytterligare: 'stor oxe; grovt vuxen karl' är samma bild som "
     "'ohyfsad man'. 'menig värnpliktig' inleder SAOL:s led ordagrant (belagd). Ingen enskild "
     "dictionary-synonym för andra betydelsen, kategori satt ur kortets egen definition (≈≈, ingen "
     "källa krävs). Exempelmeningen visar bara första betydelsen -- korrekt, det är den vanligaste."),

"desinficera": dict(
  hb="Rengöra så att smittämnen oskadliggörs",
  reg="neutral, neutral, medicin",
  grp=[["desinfektera", "rena"]],
  ex='Sjuksköterskan skyndade sig att <font color="#3498db">desinficera</font> såret innan hon lade '
     'om det.',
  etym="till desinfektion",
  sl="SO: 'oskadliggöra smittämnen i', inget definitionstillägg, en betydelse -- matchar legacy exakt. "
     "'desinfektera' är SO:s eget SYN:synonym-taggade korshänvisning (fullt utbytbart, belagd). 'rena' "
     "inleder SAOL:s led ('rena från smittämnen el. ohyra', 'el.' skiljer inte betydelser). REGISTER "
     "ÄNDRAT: SO ger ingen bruklighetskommentar alls för ordet (varken formellt eller vardagligt) -- "
     "'formell' var en gissning, sannolikt kvarleva från innan 'neutral' fanns som alternativ "
     "(style_guide.md, 2026-08-10: 49% av decket felaktigt 'formell' av samma skäl). Ordet är "
     "vardagligt vanligt (handsprit, sårvård) utan byråkratisk klang -- neutral + domän medicin. "
     "Etymologi matchar SO ordagrant, oförändrad."),

"homofon": dict(
  hb="Ord som låter likadant som ett annat men stavas annorlunda och oftast betyder något annat ; "
     "om musik: har bara en ton i taget som bär melodin, med resten som stöd",
  reg="fackspråklig, neutral, lingvistik ; fackspråklig, neutral, musik",
  grp=[["≈≈ ord"], ["≈≈ musikstil"]],
  ex='Orden "själ", "skäl" och "stjäl" är <font color="#3498db">homofoner</font>.',
  etym="av grekiska homo- 'lika' och foné 'ljud' -- alltså 'lika ljudande'",
  sl="SO substantiv: 'ord (lemma) som uttalas likadant som visst annat ord' MED definitionstillägg "
     "'men har annan stavning och (vanligen) betydelse' -- legacy hade bara 'betyder något annat', "
     "saknade 'annan stavning' som är den egenskap som skiljer homofon från homograf/homonym (SO:s "
     "egna JFR-hänvisningar till just dessa två ord bekräftar att stavningsskillnaden är poängen). "
     "Tillagt. SO adjektiv (musik): 'som har en enda melodiförande stämma' med tillägget 'medan "
     "övriga stämmor bildar ett ackordiskt ackompanjemang' -- alltså FLERA stämmor totalt, en bär "
     "melodin. Legacys kategori '≈≈ enstämmig' är sakligt missvisande (enstämmig = en enda stämma "
     "TOTALT, inget ackompanjemang) -- bytt mot '≈≈ musikstil' (homofoni är en av flera texturtyper i "
     "musik, jfr SO:s egen JFR till 'polyfon'). SAOL bekräftar samma tvådelning. ETYMOLOGI ÄNDRAD: "
     "legacy hade 'se ursprung till 2homofon 1' -- en olöst SO-intern korsreferens, inte text. Löst "
     "till den faktiska SO-etymologin på adjektivposten: 'till homo- och grekiska foné läggs' -- ger "
     "'lika ljudande', vilket hjälper minnet. Exempelmening (själ/skäl/stjäl) matchar SO:s egen syntex "
     "ordagrant, oförändrad."),

"kiropraktor": dict(
  unchanged=True,
  hb="Behandlare som arbetar med ryggrad och leder med händerna",
  reg="neutral, neutral, medicin",
  grp=[["≈≈ terapeut"]],
  ex='En <font color="#3498db">kiropraktor</font> behandlade hennes ryggsmärtor.',
  etym="av engelska chiropractor med samma betydelse",
  sl="SO: 'person som yrkesmässigt utövar kiropraktik', en betydelse, inget definitionstillägg. SAOL: "
     "'utövare av kiropraktik', samma. Kortets konkreta omskrivning (ryggrad, leder, händer) är sakligt "
     "korrekt (det ÄR vad kiropraktik innebär) och bättre Adam-tal än ordbokens cirkulära "
     "'kiropraktik-utövare'. '≈≈ terapeut' är en sann, rimlig kategori (kiropraktor är en typ av "
     "behandlare/terapeut) -- inget krav på källa för ≈≈. Ingen ändring behövs."),

"kvissla": dict(
  unchanged=True,
  hb="Liten finne i huden",
  reg="vardaglig, neutral",
  grp=[["blemma", "finne"]],
  ex='Han fick en irriterande <font color="#3498db">kvissla</font> i pannan precis innan '
     'skolfotograferingen.',
  etym="bildn. till fornsvenska kvisa 'blemma; böld'",
  bild_html_unchanged=True,
  sl="SO: 'liten finne', exakt matchning, en betydelse. SAOL: 'finne, blemma' (komma, samma "
     "betydelse med två ord) -- båda inleder var sitt komma-led i SAOL, fullt belagda, oförändrade. "
     "OLD-facit 'hudakne' är bara en bredare parafras, inget motsägande. Etymologi matchar. bild_html "
     "BEVARAD oförändrad. Ingen ändring behövs."),

"rasera": dict(
  hb="Riva ned eller låta falla sönder, så att något rasar helt samman ; förstöra något som inte går "
     "att ta på, t.ex. någons världsbild",
  reg="neutral, neutral",
  grp=[["riva", "förstöra", "jämna med marken"], ["≈≈ förstöra"]],
  ex='Flera byggnader <font color="#3498db">raserades</font> helt vid jordskalvet.',
  etym="av tyska rasieren 'rasera; raka'; till latin rådere 'skrapa'; jfr ursprung till radera",
  sl="SO huvudbetydelse: 'få (något) att rasa', med en underbetydelse (typ 'äv. i fråga om mer passiv "
     "inverkan under längre tid') som HAR egen definitionstext: 'få att falla sönder' (t.ex. 'den "
     "halvt raserade gamla bron' -- förfall över tid, inte bara aktiv nedrivning). Legacys 'Riva ned' "
     "fångade bara den aktiva sidan -- breddat till att även täcka passivt förfall. En andra "
     "underbetydelse (typ 'äv. bildligt') saknar egen definitionstext men har syntex om att rasera "
     "någons världsbild -- redan korrekt fångad som betydelse 2 på kortet, oförändrad. REGISTER "
     "ÄNDRAT: SO ger ingen bruklighetskommentar ('litterär' eller annat) på den bildliga "
     "underbetydelsen -- 'litterär' var en ogrundad gissning (den bildliga användningen, t.ex. i "
     "nyhetstext, är vardaglig/neutral snarare än bokspråklig). Enat till en registerrad. Synonymer "
     "'riva'/'förstöra'/'jämna med marken' inleder var sitt SAOL-led ('riva ner, jämna med marken, "
     "förstöra' -- komma skiljer omformuleringar), oförändrade. Betydelse 2:s kategori bytt från "
     "'≈≈ omkullkasta' (inte ur kortets egen text) till '≈≈ förstöra' (ordagrant ur definitionen). "
     "Etymologi matchar SO, oförändrad."),

"totem": dict(
  hb="Ett djur, en växt eller naturföreteelse som en grupp känner sig mystiskt förbunden med och ser "
     "som sin beskyddare",
  reg="fackspråklig, neutral, religion",
  grp=[["≈≈ beskyddare"]],
  ex='Örnen var stammens <font color="#3498db">totem</font>, en symbol för styrka.',
  etym="av engelska totem med samma betydelse; ur nordamerikanskt indianspråk",
  sl="SO: '(natur)företeelse som viss grupp människor känner en mystisk samhörighet med' med "
     "definitionstillägget 'och bl.a. uppfattar som beskyddare och dylikt; i vissa kulturer' -- "
     "legacys 'Djur eller föremål' var SMALARE än SO:s '(natur)företeelse' (utesluter t.ex. växter/"
     "naturkrafter) och saknade 'beskyddare'-nyansen ur tillägget. Breddat + tillägget infogat. SAOL "
     "('avbildning av djur el. växt ... skyddsande') bekräftar beskyddar-rollen från en annan vinkel. "
     "Kategori bytt från '≈≈ symbol' till '≈≈ beskyddare' för att matcha kortets egen (nu bredare) "
     "definition ordagrant. Exempelmening (örnen, stammens totem) matchar den vanligaste "
     "djur-varianten, oförändrad. Etymologi matchar SO, oförändrad."),
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    f = FIX.get(e["ord"])
    if not f:
        continue
    e["proposed"] = {
        "huvudbetydelse": f["hb"], "register": f["reg"],
        "synonymer": [s for g in f["grp"] for s in g],
        "synonym_groups": f["grp"], "exempelmening": f["ex"],
    }
    if f.get("etym"):
        e["proposed"]["etymologi"] = f["etym"]
    bild = (e.get("legacy") or {}).get("bild_html")
    if bild:
        e["proposed"]["bild_html"] = bild
    e["sokkoll"] = {"kalla": U(e["ord"]), "slutsats": f["sl"]}
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("godkande %d kort" % n)
