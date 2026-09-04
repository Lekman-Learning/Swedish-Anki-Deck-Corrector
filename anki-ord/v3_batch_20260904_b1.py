# -*- coding: utf-8 -*-
"""Spår A batch 2026-09-04, del 1 (13 ord, 12 skrivna + filiströs pausad).
Sökkoll via slaupp.py — bevisrader SVENSKA_SE_HAMTAD i transkriptet."""
import io, json
FIL = "sessions/session_2026-09-04_v3-batch.json"
B = lambda o: '<font color="#3498db">%s</font>' % o
U = lambda o: f"https://svenska.se/api/msearch?ord={o}"

FIX = {
"sprätta": dict(
  hb="Krafsa så att smått yr omkring ; fara iväg med fart ; stoltsera och visa upp sig ; skära upp något med kniv",
  reg="neutral",
  grp=[["krafsa","riva"],["skvätta","stänka"],["kråma sig","göra sig till"],["öppna","skära upp"]],
  ex="Han %s upp kuvertet med en smörkniv." % B("sprättade"),
  sl="SO ger fyra betydelser över två lemman: 'krafsa så att små partiklar far omkring', "
     "'fara iväg med fart', 'visa upp sig på ett övermodigt sätt', 'skära upp'. SAOL "
     "bekräftar alla fyra. Kortet hade två. OLD-facit hade rätt hela tiden: "
     "'krafsa; fara iväg; stoltsera; skära upp'."),

"bastion": dict(
  hb="Utskjutande hörn på en fästningsmur, byggt för att skjuta längs muren",
  reg="neutral, historia",
  syn=["skans","bålverk","fästningsverk"],
  ex="Kanonerna stod uppställda i den södra %s." % B("bastionen"),
  sl="SO: 'utskjutande vinkel på fästningsvall på äldre befästningar, ofta förhöjd, avsedd "
     "för flankeld' [mest historiskt]. En betydelse. Kortets andra 'definition' var samma "
     "sak omskriven, inte en egen betydelse — struken."),

"buffert": dict(
  hb="Stötdämpare i änden på en järnvägsvagn ; något som mildrar en yttre påfrestning",
  reg="neutral",
  grp=[["stötdämpare","stötfångare"],["skyddsmarginal","reserv"]],
  ex="Sparkontot är hans %s om något går sönder." % B("buffert"),
  sl="SO: 'fjädrande anordning på ände av järnvägsfordon' med underbetydelsen 'företeelse "
     "som mildrar effekten av ogynnsam yttre påverkan'. SAOL: 'stötdämpare på järnvägsvagn; "
     "äv. bildl.' Kortets 'reservförråd' var en för snäv variant av den bildliga betydelsen. "
     "Cirkulärflaggan åtgärdad: 'stötfångare' behållen bara i den bokstavliga gruppen."),

"butter": dict(
  hb="Tvär och ovänlig i sättet",
  reg="neutral, lätt negativ",
  syn=["vresig","sur","trumpen"],
  ex="Han svarade %s utan att titta upp." % B("buttert"),
  sl="SO: 'som (ofta) visar sig tvär och ovänlig'. SAOL: 'sur, vresig'. En betydelse — "
     "kortets två definitioner sa samma sak två gånger."),

"edikt": dict(
  hb="Påbud från en härskare, utfärdat uppifrån utan diskussion",
  reg="formell, historia",
  syn=["påbud","förordning","kungörelse"],
  ex="Kungen utfärdade ett %s om att alla vapen skulle lämnas in." % B("edikt"),
  sl="SO: 'påbud som utfärdas av hög makthavare' [mest vid beskrivning av äldre utländska "
     "förhållanden]. SAOL: 'påbud el. kungörelse från makthavare'. En betydelse."),

"famna": dict(
  hb="Sluta armarna om någon ; rymma och täcka in ett helt område",
  reg="neutral, litterär",
  grp=[["krama","omsluta"],["omfatta","spänna över"]],
  ex="Boken %s hela efterkrigstiden på trehundra sidor." % B("famnar"),
  sl="SO: 'omsluta med armarna' plus underbetydelsen '(lyckas) behandla i ett sammanhang'. "
     "SAOL: 'ta i famn; omsluta'. Kortet hade bara kramen. Cirkulärflaggan åtgärdad: "
     "'omfamna' struken som synonym till famna."),

"fariseism": dict(
  hb="Att spela moralisk och from utåt men inte vara det",
  reg="formell, negativ",
  syn=["hyckleri","skenhelighet"],
  ex="Talet om solidaritet var ren %s." % B("fariseism"),
  ety="efter fariséerna i Nya testamentet, kända för yttre regelfromhet",
  sl="SO: 'hycklande och självgod inställning'. En betydelse. Etymologin tillagd — den gör "
     "ordet självförklarande."),

"fiffla": dict(
  hb="Smussla och fuska med pengar eller regler i det lilla",
  reg="vardaglig, negativ",
  syn=["mygla","smussla","fuska"],
  ex="Han hade %s med kvittona i flera år." % B("fifflat"),
  sl="SO: 'ägna sig åt fiffel' [vardagligt] — cirkulärt, så definitionen är skriven ur "
     "SAOL: 'smussla, begå oegentligheter' [vard.]. En betydelse. Kortets 'manipulera' "
     "struken: för brett och inte utbytbart."),

"funtad": dict(
  hb="Skruvad på ett visst sätt i huvudet, som en person är av naturen",
  reg="vardaglig",
  syn=["beskaffad","danad"],
  ex="Hur är man %s om man tycker det där är kul?" % B("funtad"),
  sl="SO: 'som har vissa grundläggande (psykiska) egenskaper' [något vardagligt]. SAOL: "
     "'beskaffad'. En betydelse. Nästan alltid i frågan 'hur är han funtad'."),

"hurts": dict(
  hb="Litet lådskåp som står under eller intill skrivbordet",
  reg="neutral",
  syn=["sidoskåp","underskåp"],
  ex="Pennorna ligger i översta lådan i %s." % B("hurtsen"),
  sl="SO: 'sidoskåp i anslutning till skrivbord, vanligen fäst på bordsskivans undersida'. "
     "SAOL: 'underskåp till skrivbord'. En betydelse."),

"hysa": dict(
  hb="Ge någon tak över huvudet ; bära på en känsla inom sig",
  reg="neutral",
  grp=[["härbärgera","inkvartera"],["känna","bära på","nära"]],
  ex="Hon %s fortfarande ett agg mot honom." % B("hyser"),
  sl="SO ger TVÅ: 'ha boende hos sig' och 'ha en bestående känsla av'. SAOL likaså "
     "('ge husrum åt; innesluta, rymma' / 'ha, känna'). Kortet klämde ihop båda i en enda "
     "mening — de är skilda betydelser och separeras nu."),

"hägna": dict(
  hb="Sätta stängsel runt något ; skydda och värna det som är ens eget",
  reg="neutral, ngt ålderdomlig",
  grp=[["inhägna","stängsla"],["värna","skydda"]],
  ex="Föreningen vill %s om de sista strandängarna." % B("hägna"),
  sl="SO: 'omge (med något) för att avgränsa'. SAOL lägger till den bildliga: 'uppföra el. "
     "utgöra stängsel kring; skydda, värna'. Kortet hade bara stängslet, trots att "
     "OLD-facit sa 'beskydda'. Delat i två."),
}

poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    f = FIX.get(e["ord"])
    if not f:
        continue
    prop = {"huvudbetydelse": f["hb"], "register": f["reg"],
            "synonymer": f.get("syn") or [s for g in f["grp"] for s in g],
            "synonym_groups": f.get("grp"), "exempelmening": f["ex"]}
    if f.get("ety"):
        prop["etymologi"] = f["ety"]
    if (e["legacy"] or {}).get("bild_html"):
        prop["bild_html"] = e["legacy"]["bild_html"]
    e["proposed"] = prop
    e["sokkoll"] = {"kalla": U(e["ord"]), "slutsats": f["sl"]}
    e["approved"] = True
    n += 1
json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"godkände {n} kort")
