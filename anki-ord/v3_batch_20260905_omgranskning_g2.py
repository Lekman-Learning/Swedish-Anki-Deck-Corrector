# -*- coding: utf-8 -*-
"""Spår B, omgranskning 2026-09-05, grupp 2 (ord 8-15). Sökkoll via slaupp.py."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-05_v3-omgranskning-repetition.json"
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"rekrytera": dict(
  hb="Söka upp och välja ut folk till ett jobb, ett uppdrag eller liknande",
  reg="neutral, neutral",
  grp=None,
  ex=None,
  sl=("SO: 'locka (lämpliga personer) till ledig tjänst ELLER DYLIKT' -- 'eller dylikt' "
      "breddar ordet bortom bara anställning (t.ex. värvning till en rörelse, förening, "
      "militär). Kortets gamla lydelse 'till en tjänst' var för smalt jämfört med källan. "
      "SAOL bekräftar bredden: 'skaffa nya medlemmar el. personal; nyanställa' -- två "
      "närliggande formuleringar (medlemmar ELLER personal), inte två skilda betydelser -- "
      "samma kärnhandling (få folk att gå med/ta plats). Bredare hb tillagd. REGISTERFEL: "
      "'formell' stämmer inte, inget SO/SAOL-brukl markerar ordet och 'vi behöver "
      "rekrytera fler till laget' är helt vardagligt -- rättat till neutral. Synonymen "
      "'nyanställa' är SAOL:s eget andra led, belagd, oförändrad."),
),

"statistisk": dict(
  hb=None,
  reg="fackspråklig, neutral, matematik ; fackspråklig, neutral, matematik",
  grp=None, ex=None,
  sl=("SO: huvudbetydelse 'som utförs eller erhålls enligt statistikens metoder' plus "
      "underbetydelse MED egen definition 'som har att göra med statistik' -- två sanna "
      "betydelser, exakt de kortet redan har ('Som bygger på insamlade sifferuppgifter och "
      "deras analys ; som rör ämnet statistik'). REGISTERFEL: 'formell' bytt mot "
      "'fackspråklig' på båda -- ordet är en teknisk/akademisk stilnivå kopplad till ett "
      "specifikt fält (matematik/statistik), inte byråkratspråk, samma mönster som "
      "'nexus' betydelse 2 och 'endotermisk' i denna omgång. Synonymkategorierna "
      "'≈≈ sifferbaserad' och '≈≈ statistikrelaterad' är rimliga komprimeringar av "
      "kortets egna två definitioner, oförändrade."),
),

"a och o": dict(
  hb=None,
  reg="neutral, neutral",
  grp=None, ex=None,
  sl=("SO/SAOL saknar 'a och o' som eget uppslagsord -- samtliga träffar (30 per källa) "
      "är rena bokstavsartiklar (a, o, A-lag, o-ring ...), ingen relevant. Ordboken "
      "'pausas' dock INTE eftersom Wiktionary har en riktig artikel: 'det viktigaste; det "
      "essentiella' -- matchar kortets 'Det viktigaste och mest avgörande' nästan "
      "ordagrant. synonymer.se:s REDAKTIONELLA lista (inte användarbidrag) ger dessutom "
      "'början och slutet, det viktigaste, det väsentliga, alfa, och, omega' -- 'det "
      "viktigaste' är alltså dubbelt belagt (Wiktionary + syn.se redaktionellt). "
      "REGISTERFEL: 'litterär' stämmer inte -- uttrycket används flitigt i vardaglig och "
      "affärsprosa ('Kundnöjdheten är a och o'), inget bokspråkligt över det. Rättat till "
      "'neutral, neutral'."),
),

"ackumulera": dict(hb=None, reg=None, grp=None, ex=None,
  sl=("SO: 'samla till sig och lagra' -- matchar kortets 'Samla på hög så att mängden "
      "växer över tid' exakt, en betydelse (underbetydelsen 'sammanlagd' är bara "
      "particip-/adjektivformen av samma grundbegrepp, inte en ny betydelse). SAOL: "
      "'samla, hopa' (komma = samma betydelse) -- kortets synonymer 'hopa' och 'samla' är "
      "SAOL:s egna två ord, belagda. Register 'formell' rimligt (inget brukl motsäger, "
      "ordet har en teknisk/skriftspråklig ton utan att vara byråkratiskt). Etymologin "
      "(accumulare/cumulus) stämmer. Inget att ändra -- kopierat oförändrat."),
),

"crescendo": dict(hb=None, reg=None, grp=None, ex=None,
  sl=("SO ger TVÅ lemman: crescendo (adverb) 'med växande tonstyrka' och crescendo "
      "(substantiv) 'del av musikstycke som ska framföras med växande tonstyrka' -- "
      "kortets två betydelser matchar exakt ('Musik som gradvis blir starkare ; avsnittet "
      "i stycket som ska spelas så'). SAOL bekräftar med brukl 'mus.' -- matchar kortets "
      "domän 'musik' på båda. Synonymen 'med växande tonstyrka' är SAOL:s exakta "
      "ordalydelse, belagd; '≈≈ musikavsnitt' är en rimlig komprimering av betydelse 2. "
      "Exempelmeningen visar betydelse 1 (dirigentens rop), som står först -- rätt. Inget "
      "att ändra -- kopierat oförändrat."),
),

"deja vu": dict(
  hb=None,
  reg="vardaglig, neutral, psykologi",
  grp=[["≈≈ igenkänningskänsla"]],
  ex=None,
  sl=("SAOL: 'känsla av att man tidigare har upplevt samma sak' [brukl: psykol.] -- "
      "matchar kortets 'Känsla av att ha upplevt något förut' exakt. Domän 'psykologi' "
      "tillagd, SAOL:s egen bruklighetsmärkning saknades i registret. SAKFEL I SYNONYMEN: "
      "'déjà vu' var bara samma ord med franska diakriter -- inte en oberoende synonym "
      "utan en stavningsvariant av uppslagsordet självt (den mekaniska "
      "cirkulär-synonym-kontrollen missar detta eftersom den hoppar över "
      "flerordsuttryck). Ersatt med '≈≈ igenkänningskänsla', hämtad ur kortets egen "
      "definition, eftersom varken SO, SAOL eller syn.se ger ett fristående svenskt "
      "ersättningsord."),
),

"desertera": dict(
  hb="Smita från sin plats i militären mitt under ett krig",
  reg="neutral, negativ, militär",
  grp=None, ex=None,
  sl=("SO: 'rymma från stridande förband UNDER KRIG' -- specifikt under krigstid, inte "
      "militärtjänst i allmänhet (fredstida frånvaro utan lov är en annan sak). Kortets "
      "gamla 'Rymma från militärtjänst' var för brett. SAOL: 'rymma från krigstjänst' -- "
      "matchar old_facit ord för ord. Skärpt till att inkludera krigsnyansen. "
      "REGISTERFEL: 'formell' bytt mot 'neutral' -- domänen 'militär' bär redan "
      "fackkopplingen, och meningen 'Han deserterade från armén' är vanlig "
      "berättarprosa, inte myndighetsspråk. Synonymen 'rymma från krigstjänst' är SAOL:s "
      "exakta ordalydelse, oförändrad."),
),

"endotermisk": dict(hb=None, reg=None, grp=None, ex=None,
  sl=("SO: 'som sker under upptagning av värme'. SAOL: 'som sker under upptagande av "
      "värme' -- samma betydelse, en huvudbetydelse i båda. Kortets 'tar upp värme från "
      "omgivningen och gör det kallare' lägger till den vetenskapligt sanna konsekvensen "
      "(upptagen värme kyler omgivningen) för att göra begreppet konkret -- ändrar inte "
      "betydelsen, bara illustrerar den (jfr style_guide.md 'konkret före abstrakt'). "
      "Domän 'kemi' rimlig (ordet hör hemma i kemiundervisning, matchar exempelmeningens "
      "ammoniumklorid-lösning, ett klassiskt skolexempel). Synonymkategorin "
      "'≈≈ värmeupptagande' är hämtad ur kortets egen definition. Inget att ändra -- "
      "kopierat oförändrat."),
),
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    f = FIX.get(e["ord"])
    if not f:
        continue
    leg = e["legacy"] or {}
    hb = f["hb"] if f["hb"] is not None else leg.get("huvudbetydelse")
    reg = f["reg"] if f["reg"] is not None else leg.get("register")
    ex = f["ex"] if f["ex"] is not None else leg.get("exempelmening")
    if f["grp"] is not None:
        grp = f["grp"]
        syn = [s for g in grp for s in g]
    else:
        grp = leg.get("synonym_groups")
        syn = leg.get("synonymer")
    e["proposed"] = {
        "huvudbetydelse": hb,
        "register": reg,
        "synonymer": syn,
        "synonym_groups": grp,
        "exempelmening": ex,
        "etymologi": leg.get("etymologi"),
        "bild_html": leg.get("bild_html"),
    }
    e["sokkoll"] = {"kalla": U(e["ord"]), "slutsats": f["sl"]}
    e["approved"] = True
    n += 1

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("uppdaterade", n, "poster")
