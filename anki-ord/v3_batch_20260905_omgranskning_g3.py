# -*- coding: utf-8 -*-
"""Spår B, omgranskning 2026-09-05, grupp 3 (ord 16-24). Sökkoll via slaupp.py."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-05_v3-omgranskning-repetition.json"
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"genie": dict(hb=None, reg=None, grp=None, ex=None,
  sl=("SO: '(skydds)ande', tillägg '<<i antiken symboliserande en mans innersta väsen "
      "och bättre jag>>' [brukl: vanligen något högtidligt] -- matchar kortets 'Skyddsande "
      "som tänktes bära en människas innersta väsen och bättre jag' i sak (generaliserat "
      "från 'en mans' till 'en människas', en rimlig Adam-tal-förenkling som inte ändrar "
      "sakinnehållet). Register 'högtidlig' matchar SO:s egen brukl exakt. En "
      "huvudbetydelse, ingen saknas. SAOL: 'genius' -- matchar kortets synonym direkt "
      "(belagd); 'ande' är SO:s eget huvudord (belagd). Inget att ändra -- kopierat "
      "oförändrat."),
),

"instruktiv": dict(hb=None, reg=None, grp=None, ex=None,
  sl=("SO: 'som tydligt visar fram grundtankarna i visst lärostoff', tillägg 'och "
      "därigenom åstadkommer effektiv inlärning' -- matchar kortets 'Som lär ut något "
      "tydligt' i sak. En huvudbetydelse. SAOL: 'lärorik, upplysande' (komma = samma "
      "betydelse) -- matchar kortets båda synonymer ORDAGRANT, båda belagda. Register "
      "'formell, positiv' rimligt (positiv valör motiverad -- att något är instruktivt är "
      "en komplimang). Inget att ändra -- kopierat oförändrat."),
),

"irrelevant": dict(
  hb=None,
  reg="neutral, neutral",
  grp=None, ex=None,
  sl=("SO: 'som saknar betydelse i sammanhanget' -- matchar kortets 'Som saknar betydelse "
      "för det man talar om' exakt. SAOL: 'betydelselös i sammanhanget, ovidkommande' "
      "(komma = samma betydelse) -- matchar kortets båda synonymer ORDAGRANT, båda "
      "belagda. REGISTERFEL: 'formell' stämmer inte -- 'Det är helt irrelevant' är helt "
      "normalt i vardagssamtal, inget myndighetsspråk över det (samma mönster som "
      "rekrytera/prognos/desertera/utförlig i denna omgranskning). Rättat till "
      "'neutral, neutral'."),
),

"kollaps": dict(hb=None, reg=None, grp=None, ex=None,
  sl=("SO: 'fullständigt och plötsligt sammanbrott', tillägg '<<fysiskt el. psykiskt>>' -- "
      "matchar kortets 'Att något plötsligt faller ihop helt och slutar fungera' exakt. "
      "SAOL:s andra led ('spec. hopfallande av lunga') är en SPECIFIK MEDICINSK "
      "TILLÄMPNING av SAMMA grundbegrepp (något som plötsligt faller ihop) på ett organ, "
      "inte en fristående betydelse -- SO:s egen 'fysiskt el. psykiskt' täcker redan den "
      "kroppsliga sidan utan att behöva bryta ut lungan specifikt (jfr 'gå i clinch' i "
      "grupp 1, samma mönster: en specifik tillämpning av samma idé, inte en ny "
      "betydelse). En huvudbetydelse, matchar kortet. Synonymen 'sammanbrott' är SO/SAOL:s "
      "eget huvudord, belagd. Inget att ändra -- kopierat oförändrat, bild_html bevaras."),
),

"morän": dict(
  hb="Blandning av lera, grus och stora stenar som isen lämnat efter sig",
  reg=None, grp=None, ex=None,
  sl=("SO: 'jordart som består av söndersmulade bergartsfragment', tillägg '<<... med "
      "växlande grovlek, FRÅN BLOCK TILL LERPARTIKLAR>>' -- kortets gamla lydelse "
      "'Blandning av grus och sten' var för smal: källan sträcker sig från lera (finaste "
      "kornstorlek) till stenblock (grövsta), inte bara grus/sten i mitten av spannet. "
      "Bredare hb tillagd så hela kornstorleksspannet syns. SAOL: 'bank av osorterat "
      "bergartsmaterial från glaciär' -- bekräftar 'osorterat' (blandade storlekar), "
      "samma poäng. Register/domän (fackspråklig, geologi) och synonymkategorin "
      "'≈≈ istransporterat material' oförändrade, redan korrekta. bild_html bevaras."),
),

"narr": dict(hb=None, reg=None, grp=None, ex=None,
  sl=("SO: huvudbetydelse 'löjlig (och inbilsk) person' -- BÅDA egenskaperna (löjlig OCH "
      "inbilsk) fångade i kortets 'Löjlig och självgod person' (självgod = rimlig "
      "Adam-tal-synonym för inbilsk). Underbetydelse MED egen definition 'person anställd "
      "vid furstehov för att roa' -- matchar kortets andra betydelse 'anställd skämtare "
      "vid ett hov i äldre tid' exakt. Två sanna betydelser, matchar kortet. SAOL "
      "bekräftar med samma semikolon-uppdelning och ger 'gyckelmakare' ordagrant för "
      "betydelse 2 -- kortets synonym där är belagd. Register (nedsättande om person för "
      "betydelse 1, historia-domän för betydelse 2) stämmer. Inget att ändra -- kopierat "
      "oförändrat, bild_html bevaras."),
),

"profetia": dict(hb=None, reg=None, grp=None, ex=None,
  sl=("SO: '(religiös) förutsägelse' [brukl: ålderdomligt] -- matchar kortets "
      "'Förutsägelse om vad som ska hända, ofta med religiös grund' ('ofta' matchar SO:s "
      "parentetiska '(religiös)', dvs. vanligt men inte tvunget). Underbetydelsen saknar "
      "egen definition (utvidgning), ingen andra betydelse. SAOL:s semikolon "
      "('förkunnelse av gudomligt budskap; förutsägelse') beskriver samma religiösa "
      "förutsägelsekoncept ur två vinklar snarare än två fristående betydelser -- "
      "kortets enda hb täcker båda genom 'religiös grund'. Registret 'ngt ålderdomlig' är "
      "en rimlig mjukning av SO:s råa 'ålderdomligt' (ordet lever fortsatt starkt i "
      "'självuppfyllande profetia'), inte en felmärkning. Synonymen 'förutsägelse' är "
      "SAOL:s eget andra led, belagd. Inget att ändra -- kopierat oförändrat."),
),

"utförlig": dict(
  hb="Tar med även de minsta detaljerna och blir därför ganska lång",
  reg="neutral, neutral",
  grp=None, ex=None,
  sl=("SAOL: 'relativt LÅNG och ingående' -- TVÅ egenskaper (lång OCH ingående/detaljerad), "
      "kortets gamla lydelse 'Som tar med även de små detaljerna' fångade bara "
      "detaljrikedomen, inte längden. SO bekräftar via tillägget 'och DÄRFÖR är relativt "
      "OMFATTANDE' -- samma poäng om längd/omfång. Lagt till 'och blir därför ganska "
      "lång'. REGISTERFEL: 'formell' bytt mot 'neutral' -- 'Ge mig en utförlig "
      "förklaring' är vardagligt normalt, inget myndighetsspråk (samma mönster som "
      "irrelevant/rekrytera/desertera i denna omgranskning). Synonymkategorin "
      "'≈≈ grundlig' oförändrad -- 'lång'/'ingående' bildar EN sammansatt fras i "
      "källorna, inget enskilt ord inleder ett eget led, så kategori-nivån är rätt val "
      "snarare än en obelagd exakt synonym."),
),

"versfot": dict(hb=None, reg=None, grp=None, ex=None,
  sl=("SO: 'grupp av stavelser som utgör minsta rytmiska enhet i (regelbunden) vers', "
      "tillägg '<<vanligen med en betonad och en el. flera obetonade stavelser>>' -- "
      "matchar kortets 'Minsta rytmiska enhet i en vers, en grupp betonade och obetonade "
      "stavelser'. Tillägget beskriver bara det VANLIGA mönstret (inte ett absolut krav -- "
      "versfötter varierar, exempelmeningens egen anapest har två obetonade plus en "
      "betonad), så kortets mer generella formulering är korrekt snarare än för smal. "
      "SAOL:s definition är identisk med SO:s huvudbetydelse. En betydelse, matchar "
      "kortet. Synonymkategorin '≈≈ stavelsegrupp' hämtad ur kortets egen definition. "
      "Exempelmeningen (anapest) stämmer sakligt. Inget att ändra -- kopierat "
      "oförändrat."),
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
