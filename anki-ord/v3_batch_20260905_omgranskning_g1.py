# -*- coding: utf-8 -*-
"""Spår B, omgranskning 2026-09-05, grupp 1 (ord 0-7). Sökkoll via slaupp.py."""
import io, json, urllib.parse
FIL = "sessions/session_2026-09-05_v3-omgranskning-repetition.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: "https://svenska.se/api/msearch?ord=%s" % urllib.parse.quote(o)

FIX = {
"gå i clinch": dict(
  hb=None,  # oförändrad
  reg=None,
  grp=[["närkamp", "≈≈ konflikt"]],
  ex=None,
  sl=("SAOL: 'gå i clinch med' -> parafras 'gå i närkamp med' -- matchar old_facit "
      "('gå i närkamp') exakt. SO: huvudbetydelse 'ömsesidig fastlåsning av armar under "
      "boxningsmatch' plus en utvidgning utan egen definition ('äv. bildligt i uttryck för "
      "intellektuell (när)kamp, konfrontation eller dylikt') -- SAMMA grundbegrepp i två "
      "register, inte en andra betydelse, så kortets enda huvudbetydelse 'Hamna i öppen "
      "konflikt eller närkamp med någon' är korrekt oförändrad. FEL HITTAT: synonymerna "
      "'slagsmål' och 'strid' höll inte i en andra naturlig mening ('Politikerna gick i "
      "clinch under debatten' -> 'hade ett slagsmål' ändrar till bokstavligt fysiskt våld, "
      "fel -- SO:s egen bildliga underbetydelse handlar om ORDVÄXLING/konfrontation, inte "
      "fysisk kamp). Behöll 'närkamp' (SAOL:s egen parafras, starkt belagd) och la till "
      "'≈≈ konflikt', hämtad ur kortets egen huvudbetydelse."),
),

"tungsinne": dict(
  hb="Tung sorgsenhet och nedstämdhet som ofta är ett drag i personligheten",
  reg=None,
  grp=[["svårmod", "dysterhet", "≈ melankoli"]],
  ex=None,
  sl=("SO: '(benägenhet till) svårmod och nedstämdhet' med definitionstillägg 'ofta som "
      "ett karaktärsdrag' -- kortets gamla lydelse 'Djup nedstämdhet som sitter i länge' "
      "tappade BÅDA 'svårmod' (tyngden/sorgsenheten) och tillägget om att det ofta är ett "
      "personlighetsdrag, inte bara ett tillfälligt tillstånd. Skrivet om för att ta med "
      "båda. En huvudbetydelse i SO, en i SAOL ('dysterhet, melankoli', komma = samma "
      "betydelse) -- ingen betydelse saknas. Synonymer: 'svårmod' och 'dysterhet' inleder "
      "vardera sitt led i SO/SAOL:s definitionstext (belagda). 'melankoli' nedgraderat till "
      "'≈' eftersom SO uttryckligen taggar det JFR:cohyponym (jämför-med, inte synonym) "
      "trots att SAOL nämner det i sin definition."),
),

"kamouflage": dict(
  hb="Maskering som gör att något inte upptäcks ; Något som döljer den verkliga avsikten bakom en handling",
  reg="neutral, neutral, militär ; neutral, neutral",
  grp=[["skyddsförklädnad"], ["täckmantel"]],
  ex=None,  # oförändrad, visar betydelse 1 (som står först) -- rätt enligt regeln
  sl=("DOLD BETYDELSE HITTAD: legacy hade 'täckmantel' listat som SYNONYM till den "
      "bokstavliga maskeringsbetydelsen -- men SAOL:s definition är 'vilseledande "
      "maskering el. skyddsmålning, skyddsförklädnad; täckmantel', och SEMIKOLONET skiljer "
      "TVÅ betydelser (bokstavlig maskering / bildlig 'täckmantel för en avsikt'), inte en "
      "synonym till den första. SO bekräftar med en utvidgning utan egen definition för det "
      "bildliga bruket. Delat i två betydelser: (1) SO:s huvudbetydelse '(täckande) "
      "anordning som ska ge skydd mot upptäckt' [brukl: särsk. militärväsen] -> domän "
      "militär tillagd, (2) SAOL:s 'täckmantel'. Synonymer omfördelade per betydelse: "
      "'skyddsförklädnad' (SAOL, betydelse 1) och 'täckmantel' (SAOL, betydelse 2). "
      "Exempelmeningen visar redan betydelse 1 (soldat i skogen), som står först -- rätt "
      "enligt regeln, ingen ändring där. bild_html bevaras."),
),

"kontemplation": dict(
  hb=None, reg=None, grp=None, ex=None,
  sl=("SO: 'försjunkenhet i djupa tankar' -- matchar kortets 'Att sjunka in i djupa, stilla "
      "tankar' exakt, en huvudbetydelse, ingen saknas. SAOL: 'djup begrundan, försjunkande "
      "i betraktelser' (komma = samma betydelse) -- kortets synonym 'djup begrundan' är "
      "SAOL:s eget första led, starkt belagd. Register 'formell' är en rimlig bedömning "
      "(inget SO/SAOL-brukl motsäger det, ordet hör hemma i skriftspråk/filosofisk/religiös "
      "kontext snarare än vardagssvenska). Etymologin (templum/betraktande) stämmer mot "
      "latinets contemplari. Inget att ändra -- kopierat oförändrat."),
),

"nexus": dict(
  hb=None, reg=None, grp=None, ex=None,
  sl=("SO: huvudbetydelse 'förbindelse' plus en underbetydelse MED EGEN definition "
      "'språklig förbindelse mellan två begrepp som förutsätter varandra' -- en riktig "
      "andra betydelse, redan korrekt uppdelad på kortet ('Central koppling som binder "
      "samman flera saker ; bandet mellan satsens subjekt och predikat'). SAOL bekräftar "
      "den språkvetenskapliga betydelsen med brukl 'språkv.' -- matchar kortets domän "
      "'lingvistik' på betydelse 2. Synonymkategorierna '≈≈ knutpunkt' och '≈≈ satsband' är "
      "rimliga komprimeringar av kortets egna två definitioner. Inget att ändra -- kopierat "
      "oförändrat."),
),

"prognos": dict(
  hb="En förutsägelse om framtiden, byggd på fakta man redan vet",
  reg="neutral, neutral",
  grp=None,
  ex=None,
  sl=("SO: 'förutsägelse om kommande utveckling eller förlopp', definitionstillägg "
      "'vanligen grundad på iakttagbara fakta'. SAOL: 'vetenskapligt grundad förutsägelse'. "
      "Kortets gamla lydelse ('Förutsägelse om hur något kommer att utveckla sig') tappade "
      "just den distinktionen mot en ren gissning (jfr old_facit 'gissad framtidsbild', som "
      "SO:s eget tillägg motsäger -- prognosen ska vara faktabaserad, inte en slump-gissning; "
      "OLD hade fel nyans här). Lagt till 'byggd på fakta man redan vet'. REGISTERFEL "
      "HITTAT: 'formell' stämmer inte -- inget SO/SAOL-brukl markerar ordet, och testet "
      "('Vad är prognosen för vädret imorgon?' i ett sms) är helt normalt, inte "
      "myndighetsspråk. Rättat till 'neutral, neutral'. Synonymen 'förutsägelse' är SO:s "
      "eget första ord i definitionen, belagd."),
),

"prövning": dict(
  hb="En psykiskt tung situation man tvingas ta sig igenom ; Juridisk behandling och bedömning av ett ärende ; Tentamen",
  reg="neutral, negativ ; formell, neutral, juridik ; neutral, neutral",
  grp=[["psykisk påfrestning"], ["≈≈ rättsprocess"], ["tentamen"]],
  ex=None,  # oförändrad, visar betydelse 1 (först) -- rätt
  sl=("SO ger TRE separata huvudbetydelser: 'psykisk påfrestning', 'juridisk behandling "
      "och bedömning', 'tentamen' -- kortet hade redan alla tre men med två fel. (1) HÅRT "
      "FORMATFEL: synonym_groups hade bara 2 grupper mot 3 betydelser "
      "(grupper_matchar_ej_betydelser) -- lagt till en tredje grupp '≈≈ rättsprocess', "
      "hämtad ur kortets egen 'juridisk behandling'-definition. (2) HALV DEFINITION: "
      "betydelse 1 saknade 'psykisk' (SO: 'psykisk påfrestning', inte påfrestning i "
      "allmänhet) och betydelse 2 saknade 'bedömning' (SO: 'behandling OCH bedömning', två "
      "led, kortet hade bara 'behandling'). Båda kompletterade. (3) REGISTERFEL: valören på "
      "betydelse 1 stod som 'neutral' trots att en påfrestning/prövning är känslomässigt "
      "belastad -- rättat till 'negativ'. Exempelmeningen visar redan betydelse 1 (först), "
      "rätt enligt regeln, oförändrad. bild_html bevaras."),
),

"psykos": dict(
  hb=None, reg=None, grp=None, ex=None,
  sl=("SO: huvudbetydelse 'psykiskt sjukdomstillstånd med förändrad verklighetsuppfattning "
      "och bristande sjukdomsinsikt' [definitionstillägg: orsakad av bl.a. traumatisk "
      "händelse, sjukdom eller droger -- etiologi, ändrar inte SJÄLVA definitionen till "
      "skillnad från t.ex. afficiera, så en kort Adam-tal-definition utan orsaksledet är "
      "fortfarande sann och komplett] plus en underbetydelse 'äv. försvagat om tillstånd "
      "(hos en grupp människor) där handlandet styrs enbart av känslan' (morfex: "
      "masspsykos) -- kortets andra betydelse 'tillstånd i en grupp där handlandet helt "
      "styrs av känslan' matchar nästan ordagrant. SAOL har bara EN definition ('svår "
      "psykisk störning med t.ex. förvirring och hallucinationer'), ingen semikolon -- "
      "ingen tredje betydelse saknas. Synonymkategorierna '≈≈ sjukdomstillstånd' och "
      "'≈≈ masshysteri' är rimliga komprimeringar av kortets egna två definitioner. "
      "Register (fackspråklig/medicin resp. neutral/psykologi) matchar SAOL:s ämnesområde "
      "och SO:s grupp-nyans. Inget att ändra -- kopierat oförändrat."),
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
