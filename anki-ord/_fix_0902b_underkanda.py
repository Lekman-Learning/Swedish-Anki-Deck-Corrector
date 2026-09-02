# -*- coding: utf-8 -*-
"""Rattar batch B:s 16 underkanda kort.

MONSTRET i anmarkningarna ar entydigt och gar at tva hall samtidigt:

  9 kort saknade en betydelse SO faktiskt har (chiffer, erovring, psykos,
    vakuum, vagel, feedback, rasera)
  3 kort hade en betydelse SO INTE har, hamtad ur en fast fras eller ur ett
    annat sprak (koloss, profetia, genie)
  4 kort hade en synonym utan belagg eller med fel innebord (algoritm,
    sovel, statistisk, dyig, kvittens)

Det ar samma bar i bada riktningarna: kortet ska aterge ordboken, varken
mindre eller mer. Ett pahittat led ar lika illa som ett saknat -- och tva
av de tre pahittade kom ur MIN egen rattning tidigare i dag, dar jag lade
till "koloss pa lerfotter" och "sjalvuppfyllande profetia" som betydelser.
Overkorrigering ar ocksa ett fel.
"""
import io, json, sys
import _hjalp_0902b as HJ

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-02b_v3-batch.json"
H = HJ.H

K = {
 "chiffer": (
  "Meddelande skrivet så att utomstående inte förstår det ; kunglig namnteckning i form av sammanflätade bokstäver",
  "formell, neutral ; fackspråklig, neutral, historia",
  ["hemlig skrift", "≈≈ monogram"], [["hemlig skrift"], ["≈≈ monogram"]],
  "Kryptologen lyckades forcera det tyska %s efter månader av arbete." % (H % "chiffret"),
  "RÄTTAT efter blindgranskning: monogrambetydelsen saknades helt — det "
  "kungliga namnchiffret på en krona eller ett sigill. Dessutom sade kortet "
  "att chiffer är ett SYSTEM; SO säger meddelandet självt. Båda rättade."),

 "koloss": (
  "Mycket stor staty ; ovanligt stor person eller sak",
  "fackspråklig, neutral, konst ; neutral, neutral",
  ["stor staty", "bjässe"], [["stor staty"], ["bjässe"]],
  "Det var en %s av en man som stod framför oss." % (H % "koloss"),
  "RÄTTAT efter blindgranskning, och felet var mitt eget överdrivna "
  "rättande tidigare samma dag: jag lade in 'något som ser mäktigt ut men "
  "är svagt' som egen betydelse. Den finns bara i den fasta frasen 'koloss "
  "på lerfötter' och är ingen betydelse hos grundordet. Ordningen är också "
  "återställd så SO:s huvudbetydelse står först."),

 "profetia": (
  "Förutsägelse om vad som ska hända, ofta med religiös grund",
  "ngt ålderdomlig, neutral, religion", ["förutsägelse"], [["förutsägelse"]],
  "Enligt legenden hade den gamla kvinnan %s gåva och kunde se in i framtiden." % (H % "profetians"),
  "RÄTTAT efter blindgranskning. Tre fel: (1) 'självuppfyllande profetia' "
  "finns bara som fast fras, inte som betydelse hos ordet — samma "
  "överkorrigering som i koloss; (2) SO märker ordet ålderdomligt, vilket "
  "registret nu speglar; (3) 'förkunnelse' är predikan, inte förutsägelse, "
  "och är struken."),

 "algoritm": (
  "Steg-för-steg-metod för att lösa ett problem",
  "fackspråklig, neutral, IT", ["instruktionsföljd"], [["instruktionsföljd"]],
  "Euklides %s hittar det största gemensamma talet." % (H % "algoritm"),
  "RÄTTAT efter blindgranskning: 'räknemönster' saknar helt belägg i SO och "
  "är dessutom missvisande — en algoritm behöver inte räkna något alls. "
  "Bytt mot poolens 'instruktionsföljd'."),

 "erövring": (
  "Att ta något med våld eller makt ; framsteg som vunnits med möda ; person man vunnit som kärlekspartner",
  "formell, neutral ; litterär, neutral ; vardaglig, lätt negativ",
  ["≈≈ maktövertagande", "≈≈ landvinning", "≈≈ kärlekspartner"],
  [["≈≈ maktövertagande"], ["≈≈ landvinning"], ["≈≈ kärlekspartner"]],
  "Spanjorernas %s av Sydamerika förändrade hela kontinenten." % (H % "erövring"),
  "RÄTTAT efter blindgranskning: två betydelser saknades — den bildliga om "
  "framsteg ('teknikens erövringar') och den vardagliga om ny "
  "kärlekspartner ('hans senaste erövring'). Ingen av dem täcks av "
  "våldsbetydelsen."),

 "psykos": (
  "Psykisk sjukdom där verklighetsuppfattningen förändras och insikten om att man är sjuk saknas ; tillstånd i en grupp där handlandet helt styrs av känslan",
  "fackspråklig, neutral, medicin ; neutral, neutral, psykologi",
  ["≈≈ sjukdomstillstånd", "≈≈ masshysteri"],
  [["≈≈ sjukdomstillstånd"], ["≈≈ masshysteri"]],
  "Han drabbades av en %s efter flera sömnlösa veckor." % (H % "psykos"),
  "RÄTTAT efter blindgranskning: masspsykosen saknades. Den är inte en "
  "individuell sjukdom utan ett grupptillstånd, och täcks därför inte av "
  "kortets första betydelse."),

 "rasera": (
  "Riva ned så att något faller samman ; förstöra något som inte går att ta på, t.ex. någons världsbild",
  "neutral, neutral ; litterär, neutral",
  ["riva", "förstöra", "jämna med marken", "≈≈ omkullkasta"],
  [["riva", "förstöra", "jämna med marken"], ["≈≈ omkullkasta"]],
  "Flera byggnader %s helt vid jordskalvet." % (H % "raserades"),
  "RÄTTAT efter blindgranskning. Min andra betydelse — 'falla sönder av sig "
  "självt' — var sakligt fel: SO definierar rasera genomgående KAUSATIVT, "
  "alltså att någon eller något orsakar raset. Även 'den halvt raserade "
  "bron' förutsätter en verkande kraft. Betydelsen är ersatt med den "
  "bildliga, som faktiskt finns och saknades."),

 "sovel": (
  "Mat man äter till brödet, särskilt det matiga som kött, fisk eller pålägg",
  "ngt ålderdomlig, neutral", ["smörgåspålägg"], [["smörgåspålägg"]],
  "Det var ont om %s till brödet den vintern." % (H % "sovel"),
  "RÄTTAT efter blindgranskning: 'tilltugg' är ett litet mellanmål, ofta "
  "till dryck. Sovel är tvärtom den MATIGA delen av måltiden — proteinet "
  "man äter till brödet. Skillnaden är utskriven i huvudbetydelsen."),

 "vakuum": (
  "Rum helt utan luft ; tomrum där något som borde finnas saknas",
  "fackspråklig, neutral, fysik ; neutral, neutral",
  ["lufttomt rum", "tomrum", "≈≈ tomrum"],
  [["lufttomt rum", "tomrum"], ["≈≈ tomrum"]],
  "Man kan skapa ett %s genom att pumpa ut all luft ur en behållare." % (H % "vakuum"),
  "RÄTTAT efter blindgranskning: den bildliga betydelsen saknades — "
  "maktvakuum, känslomässigt vakuum. Granskaren kallade den 'mycket vanlig "
  "och viktig', och det stämmer: det är i den formen ordet oftast dyker upp "
  "i text."),

 "blickfång": (
  "Det område blicken överskådar ; det som naturligt drar till sig blicken",
  "neutral, neutral ; neutral, neutral",
  ["synfält", "som fångar blicken"], [["synfält"], ["som fångar blicken"]],
  "Den nya fabriken hamnade rakt i grannarnas %s." % (H % "blickfång"),
  "RÄTTAT efter blindgranskning: ordningen var omvänd. Både SO och SAOL "
  "leder med synfältsbetydelsen. Jag hade lagt den sist med motiveringen "
  "att den är ovanligare — men kortets egen exempelmening använder just "
  "den, vilket jag noterade utan att dra slutsatsen."),

 "feedback": (
  "Signal som går tillbaka till sändaren och styr det som händer sedan ; svar på hur någon presterat",
  "fackspråklig, neutral, teknik ; neutral, neutral",
  ["återkoppling för reglering av process", "respons"],
  [["återkoppling för reglering av process"], ["respons"]],
  "Auditiv %s är nödvändig för att barn ska utveckla sitt tal." % (H % "feedback"),
  "RÄTTAT efter blindgranskning: kortet hade bara gensvarsbetydelsen, men "
  "exempelmeningen var SO:s eget exempel på den TEKNISKA — återkopplingen "
  "som styr fortsatt aktivitet. Kortet lärde alltså ut en betydelse och "
  "visade en annan. Båda står nu, med den tekniska först."),

 "genie": (
  "Skyddsande som tänktes bära en människas innersta väsen och bättre jag",
  "högtidlig, neutral", ["ande", "genius"], [["ande", "genius"]],
  "Mozarts skapande %s visade sig redan när han var barn." % (H % "genie"),
  "RÄTTAT efter blindgranskning: exempelmeningen handlade om sagoanden ur "
  "flaskan (jinn/Aladdin), som inte är belagd under 'genie' i vare sig SO "
  "eller SAOL. SO:s ord är den antika skyddsanden som symboliserar en "
  "människas bättre jag — och SO:s eget exempel är 'hans skapande genie'. "
  "Exemplet är bytt till det, registret till högtidlig."),

 "kvittens": (
  "Skriftligt bevis på att en betalning eller leverans tagits emot",
  "formell, neutral, ekonomi", ["≈≈ kvitto"], [["≈≈ kvitto"]],
  "Butiken utfärdade en %s när jag köpte kläderna." % (H % "kvittens"),
  "RÄTTAT efter blindgranskning: 'kvitto' stod som rak synonym, men SO "
  "markerar det som kohyponym och facit skriver själv '(generellare än "
  "kvitto)'. Kvittens är det bredare ordet, kvitto en undertyp. Nu märkt "
  "≈≈, vilket är precis vad den nivån finns till för — annars tränar kortet "
  "in den distraktorfälla HP-ORD straffar."),

 "statistisk": (
  "Som bygger på insamlade sifferuppgifter och deras analys ; som rör ämnet statistik",
  "formell, neutral, matematik ; formell, neutral, matematik",
  ["≈≈ sifferbaserad", "≈≈ ämnesrelaterad"],
  [["≈≈ sifferbaserad"], ["≈≈ ämnesrelaterad"]],
  "Forskarna presenterade sina %s beräkningar i rapporten." % (H % "statistiska"),
  "RÄTTAT efter blindgranskning: 'siffergrundad' och 'ämnesrelaterad' stod "
  "som raka synonymer men finns inte i SO alls. De är nu märkta ≈≈, alltså "
  "kategorier hämtade ur kortets egen definition — vilket är den enda nivå "
  "som får sättas utan ordboksbelägg."),

 "vagel": (
  "Varig svullnad i kanten av ögonlocket ; sittstång för höns",
  "neutral, neutral, medicin ; ngt ålderdomlig, neutral, jordbruk",
  ["inflammation i ögonlocksrand", "sittstång för höns"],
  [["inflammation i ögonlocksrand"], ["sittstång för höns"]],
  "Hon fick en %s i ögat efter förkylningen." % (H % "vagel"),
  "RÄTTAT efter blindgranskning: sittstången saknades. Jag motiverade "
  "bortvalet med att det är ett homonym — vilket det är — men motiveringen "
  "når aldrig granskaren, och båda betydelserna står under samma "
  "uppslagsord i både SO och SAOL. Då hör de hemma på samma kort."),

 "dyig": (
  "Full av dy, alltså löst och ruttnande bottenslam",
  "neutral, neutral", ["≈≈ gyttjig"], [["≈≈ gyttjig"]],
  "Sjöns botten var %s och svår att gå i." % (H % "dyig"),
  "RÄTTAT efter blindgranskning: 'lerig' är sakligt fel. Lera är "
  "mineraljord, dy är organiskt bottenslam — olika ämnen. Facit ger "
  "'gyttjig', som ligger nära, och det står nu som ≈≈ eftersom det saknar "
  "eget ordboksbelägg."),
}


poster = json.load(io.open(FIL, encoding="utf-8"))
n = 0
for e in poster:
    d = K.get(e["ord"])
    if not d:
        continue
    hb, reg, syn, grp, ex, slut = d
    e["proposed"].update({"huvudbetydelse": hb, "register": reg,
                          "synonymer": syn, "synonym_groups": grp,
                          "exempelmening": ex})
    e["sokkoll"]["slutsats"] += " " + slut
    # Gamla motiveringar galler inte langre -- betydelserna ar andrade.
    (e.get("forgranska_tillat") or {}).pop("betydelse_kan_saknas", None)
    n += 1

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("rattade kort:", n, "av 16")
saknas = [o for o in K if not any(e["ord"] == o for e in poster)]
print("hittades inte:", saknas or "inga")
