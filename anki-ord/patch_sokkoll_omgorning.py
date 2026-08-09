"""Bygger en sessionsfil med de kort som fått en RIKTIG sökkoll 2026-08-09 (kväll).

Varje `kalla` innehåller de URL:er som faktiskt hämtades. Hål 0-spärren i
`applicera` slår upp dem i Claude Codes transkript och vägrar skriva kortet om
hämtningen inte finns där. Det är hela poängen: fältet går inte längre att fylla
i på förtroende.
"""
import json
import os

SAOB = "https://www.saob.se/artikel/?seek={}"
SYN = "https://www.synonymer.se/sv-syn/{}"
WIKT = "https://sv.wiktionary.org/wiki/{}"

KALLOR = ["sessions/session_2026-08-09_v3-omgranskning-nya.json",
          "sessions/session_2026-08-09_v3-dagens-ko.json",
          "sessions/session_2026-08-09_v3-dagens-ko2.json",
          "sessions/session_2026-08-09_v3-inlarning.json"]

MAL = "sessions/session_2026-08-09_v3-sokkoll-omgorning.json"


def k(ord_, saob=True, syn=True, wikt=False):
    """URL-sträng för kalla. Bara källor som FAKTISKT hämtades får listas."""
    u = []
    if saob:
        u.append(SAOB.format(ord_))
    if syn:
        u.append(SYN.format(ord_))
    if wikt:
        u.append(WIKT.format(ord_))
    return " + ".join(u)


# (ord, kalla, slutsats, ändringar i proposed)
# Ändringar som None = kortet står kvar oförändrat, bara sökkollen tillkommer.
P = {}


def lagg(ord_, kalla, slutsats, **andringar):
    P[ord_] = (kalla, slutsats, andringar)


# --- Grupp A: de åtta "ordet finns inte"-påståendena --------------------------
lagg("hävdatecknare", k("h%C3%A4vdaforskare") + " + " + k("hävdatecknare", saob=False),
     "RÄTTAD MOTIVERING. Jag påstod 2026-08-09 att 'hävdaforskare' inte är ett ord. "
     "Det är fel: SAOB har det ('person som forskar i hävderna; historieforskare, "
     "historiker', belägg 1813). Borttagningen står ändå kvar, men av rätt skäl: en "
     "FORSKARE forskar i hävderna, en TECKNARE skriver ned dem -- inte utbytbara. "
     "Facits 'historieskrivare' saknades och lades till.")

lagg("dalt", k("bortsk%C3%A4mmande") + " + " + k("dalt", saob=False),
     "RÄTTAD MOTIVERING. Jag påstod att 'bortskämmande' inte är ett ord. SAOB har "
     "formen -- men enbart som korshänvisning ('BORTSKÄMMANDE, sbst., se bortskämma, "
     "v.'), utan egen betydelse, och varken synonymer.se eller Wiktionary känner den. "
     "Som synonym till dalt är den alltså inte brukbar. Rätt handling, falskt skäl.")

lagg("uppslag", k("bok%C3%B6ppning"),
     "'boköppning' kontrollerat och saknas i båda källorna (SAOB föreslår bomöppning/"
     "bokning, synonymer.se broöppning/botövning). Borttagningen belagd.")
lagg("girig", k("habeg%C3%A4rlig"),
     "'habegärlig' kontrollerat och saknas i båda källorna. Ersättningen 'sniken' står "
     "kvar. Borttagningen belagd.")
lagg("signera", k("initialera"),
     "'initialera' kontrollerat och saknas i båda källorna (SAOB föreslår instillera/"
     "installera/inhalera). Borttagningen belagd.")
lagg("sepia", k("brunton"),
     "'brunton' kontrollerat och saknas i båda källorna. Tom synonymlista står kvar.")
lagg("slapstick", k("misskastning"),
     "'misskastning' kontrollerat och saknas i båda källorna. Omskrivningen av "
     "exempelmeningen belagd.")
lagg("vernissage", k("%C3%B6ppningsvisning"),
     "'öppningsvisning' kontrollerat och saknas i båda källorna. Borttagningen belagd.")

# --- Grupp B: innehållsändrade kort, nu belagda -------------------------------
lagg("beprövad", k("bepr%C3%B6vad"),
     "SAOB ger bara korshänvisning (bepröfvad, se bepröfva). synonymer.se: 'som "
     "prövats och visat sig bra' -- tillförlitlig, pålitlig, erfaren, van, härdad. "
     "TVÅ FEL RÄTTADE: 'prövad' är cirkulärt (be-PRÖVAD), och 'etablerad' finns inte "
     "i någon källa. Borttagningen av 'bevisad' bekräftad -- ingen källa har det.",
     synonymer=["tillförlitlig", "pålitlig", "härdad"])

lagg("bilateral", k("bilateral"),
     "SAOB ger tre betydelser: (1) tvåsidig/symmetrisk i fackspråk, (2) ömsesidigt "
     "förpliktande i juridik, (3) fonetiskt om ljud på båda sidor av tungan. Den "
     "medicinska/dubbelsidiga betydelsen som lades till bekräftas av (1). "
     "Borttagningen av 'parvis' bekräftad -- finns i ingen källa. Kortet saknade "
     "synonymer helt; tvåsidig/ömsesidig är belagda hos synonymer.se. Betydelse (3) "
     "utelämnad medvetet -- för specialiserad för HP.",
     synonymer=["tvåsidig", "ömsesidig"])

lagg("blindskrift", k("blindskrift", wikt=True),
     "MISSLYCKAD SAOB-HÄMTNING: ?seek=blindskrift landade på grundordet BLIND (13 "
     "betydelser), inte sammansättningen -- räknas inte som belägg. synonymer.se och "
     "Wiktionary bär i stället, båda ger punktskrift och brailleskrift. 'braille' "
     "ändrat till den belagda formen 'brailleskrift'.",
     synonymer=["punktskrift", "brailleskrift"])

lagg("depreciera", k("depreciera"),
     "LÖSER CIRKULARITETEN. Kortet definierade ordet som 'sjunka i värde' och gav "
     "'falla i värde' som synonym -- samma sak omskriven. SAOB: om valuta/mynt sjunka "
     "i värde under det nominella. synonymer.se ger belagda, icke-cirkulära "
     "synonymer: devalvera, nedvärdera, nedskriva. Motsats: appreciera.",
     synonymer=["devalvera", "nedvärdera", "skriva ned"])

lagg("fonetik", k("fonetik"),
     "SAOB: (1) äldre, verslärans rimavsnitt (Almqvist 1840) (2) läran om språkljuden. "
     "Borttagningen av 'språkvetenskap' bekräftad -- det är hela fältet, inte grenen. "
     "synonymer.se listar 'fonologi' som synonym; det tas MEDVETET INTE in, fonologi "
     "är en angränsande disciplin (ljudsystem) och inte samma sak som fonetik "
     "(ljudens fysik). Ett exempel på att synonymer.se inte får kopieras rakt av.")

lagg("förhala", k("f%C3%B6rhala", wikt=True),
     "MISSLYCKAD SAOB-HÄMTNING: ?seek=förhala gav en träfflista, inte artikeln. "
     "synonymer.se OCH Wiktionary ger båda TVÅ betydelser, och kortet hade bara en: "
     "sjötermen 'förflytta ett fartyg kortare sträckor med hjälp av linor' saknades. "
     "Det är dessutom ordets ursprung (lågtyska/nederländska verhalen).",
     huvudbetydelse="Medvetet dra ut på tiden för att skjuta upp något ; "
                    "sjöterm: förflytta ett fartyg korta sträckor med hjälp av linor")

lagg("glyptotek", k("glyptotek"),
     "SAOB: museum med skulptursamling. synonymer.se: skulpturmuseum, skulptursamling. "
     "Enbetydelseord, kortet stämmer mot båda källorna. Ingen ändring.")

lagg("konstitutiv", k("konstitutiv"),
     "SAKNAD BETYDELSE. SAOB ger två: (1) konstitutionell, som rör författning "
     "(2) grundläggande/väsentlig. Kortet hade bara (2). synonymer.se listar "
     "'författnings-' bland synonymerna, vilket bekräftar (1).",
     huvudbetydelse="Som utgör en nödvändig, grundläggande beståndsdel ; "
                    "som rör en författning eller grundlag",
     synonymer=["grundläggande", "väsentlig", "bestämmande"])

lagg("korus", k("korus"),
     "LÖSER CIRKULARITETEN. Kortet gav 'kör' som synonym till 'flera röster som "
     "ljuder samtidigt' -- definitionen omskriven. SAOB: (1) sångkör (2) körsång/"
     "körklang (4) 'i korus' = samtidigt och enstämmigt. synonymer.se ger samklang, "
     "enstämmigt, samfällt, unisont -- 'samstämmighet' fanns i ingen källa och ersätts "
     "med de belagda formerna.",
     synonymer=["kör", "samklang", "unisont"])

lagg("lägga sordin på", k("sordin"),
     "SAOB (sordin): (1) dämpare på musikinstrument (2) bildligt dämpad framställning; "
     "uttrycket 'lägga sordin på' belagt i båda källorna. 'hämma' fanns i ingen källa "
     "och tas bort -- det betyder hindra, inte dämpa.",
     synonymer=["dämpa", "tona ned"])

lagg("putslustig", k("putslustig"),
     "SAOB ger fyra betydelser, alla varianter av skämtsamt/smått komiskt. "
     "synonymer.se: 'narraktigt lustig; smårolig på ett löjligt sätt' -- skojig, "
     "tokrolig och smårolig är alla belagda. Definitionen sa 'löjligt eller gulligt'; "
     "'gulligt' finns i ingen källa och är dessutom fel valör -- ordet är nedsättande.",
     huvudbetydelse="Lustig på ett lite löjligt, narraktigt sätt")

lagg("schattera", k("schattera"),
     "SAOB ger fem betydelser (måleri, textil, färgnyans, blindtryck, typografi). "
     "Kortets definition motsvarar (1) och synonymerna skugga/nyansera är belagda hos "
     "synonymer.se, som också ger 'förtona'. Stavningsrättelsen schattar -> schatterar "
     "bekräftad av böjningen i källan.",
     synonymer=["skugga", "nyansera", "förtona"])

lagg("sondera", k("sondera"),
     "SAKNAD BETYDELSE. SAOB ger fem, varav den bokstavliga (undersöka med sond) är "
     "grunden för alla de bildliga -- synonymer.se inleder sin egen förklaring med "
     "'undersöka med sond'. Kortet hade bara den bildliga. Dessutom: 'känna sig för' "
     "fanns inte i källan, men 'höra sig för' gör det.",
     huvudbetydelse="Försiktigt undersöka hur något ligger till ; "
                    "undersöka något med en sond",
     synonymer=["undersöka", "höra sig för", "utforska"])

lagg("vedervåga", k("vederv%C3%A5ga", wikt=True),
     "MISSLYCKAD SAOB-HÄMTNING: ?seek=vedervåga landade på prefixartikeln VEDER-, "
     "inte på ordet -- räknas inte som belägg. synonymer.se: sätta på spel, ta risken "
     "av, riskera, våga sig på. Wiktionary: äventyra. 'våga' var cirkulärt "
     "(veder-VÅGA) och ersätts med den belagda formen 'våga sig på' plus 'äventyra'.",
     synonymer=["sätta på spel", "våga sig på", "äventyra"])

lagg("yuppie", k("yuppie", saob=False, wikt=True),
     "SAOB UTELÄMNAD MED AVSIKT: ordet är belagt i svenskan först 1985 (Wiktionary) "
     "och ligger utanför SAOB:s täckning för bokstaven -- att söka hade gett ett "
     "meningslöst nej. synonymer.se: 'ung, akademiskt utbildad yrkesutövare i storstad "
     "med goda inkomster' -- finanslejon, nyrik, uppkomling, parveny, ung penningmakare. "
     "'karriärist', 'statusjägare' och 'dyra vanor' fanns i ingen källa.",
     huvudbetydelse="Ung, välbetald storstadsyrkesutövare med akademisk utbildning",
     synonymer=["finanslejon", "nyrik", "uppkomling"])

lagg("bonitet", k("bonitet", wikt=True),
     "KORTET HADE RÄTT -- OCH DET SYNTES FÖRST I TREDJE KÄLLAN. SAOB ger bara "
     "'(god) kvalitet; godhetsgrad', främst skogsbruk. synonymer.se likaså (värde, "
     "avkastningsförmåga). Betydelsen 'kreditvärdighet' bekräftas ENBART av Wiktionary. "
     "Hade jag stannat vid två källor hade jag tagit bort en korrekt betydelse. "
     "Cirkulariteten löses av de belagda synonymerna.",
     synonymer=["avkastningsförmåga", "godhetsgrad"])

lagg("urmodig", k("urmodig"),
     "LÖSER CIRKULARITETEN OCH GER EN ANVÄNDNINGSREGEL KORTET SAKNADE. Kortet hade "
     "definitionen ordagrant som synonymlista. synonymer.se anger uttryckligen: "
     "'Sedan långliga tider kommen ur bruk. KUNNA ENDAST SÄGAS OM SAK.' -- ordet får "
     "alltså aldrig användas om personer, vilket är precis den sortens begränsning HP "
     "prövar. SAOB understryker tidsaspekten ('sedan länge ur modet'). Belagda "
     "synonymer utan överlapp med definitionen: förlegad, obsolet, ålderdomlig.",
     huvudbetydelse="Sedan länge ur bruk och därmed löjligt gammaldags (endast om saker, "
                    "aldrig om personer)",
     synonymer=["förlegad", "obsolet", "ålderdomlig"])

lagg("ekvivalent", k("ekvivalent"),
     "SAKNAD BETYDELSE PLUS CIRKULARITET. SAOB delar upp i adjektiv (likvärdig; kemi; "
     "fysik) OCH substantiv ('fullgod ersättning', 'den viktmängd varmed ett ämne kan "
     "ersätta ett annat'). Kortet hade bara adjektivet. synonymer.se bekräftar båda "
     "ordklasserna. 'likvärdig/motsvarande' var definitionen omskriven; jämgod och "
     "jämförlig är belagda och inte cirkulära.",
     huvudbetydelse="Som har samma värde eller verkan som något annat ; "
                    "en fullgod ersättning eller motsvarighet",
     synonymer=["jämgod", "jämförlig", "likvärdig"])

lagg("ingenium", k("ingenium"),
     "SAKNAD BETYDELSE. SAOB ger två: (1) medfödd begåvning och förstånd (2) den "
     "begåvade PERSONEN -- ett snille. Kortet hade bara (1), men bar ändå 'snille' "
     "som synonym, vilket hör till (2). Det är därför kortet såg cirkulärt ut: "
     "synonymen tillhörde en betydelse som inte stod skriven. synonymer.se bekräftar "
     "med begåvning, snille, intellekt, geni.",
     huvudbetydelse="Medfödd skarpsinnighet och begåvning ; en person med sådan "
                    "begåvning, ett snille",
     synonymer=["begåvning", "snille", "intellekt"])

lagg("adoratör", k("adorat%C3%B6r"),
     "SAOB: 'tillbedjare; särskilt en kvinnas beundrare eller älskare' (1893, ur "
     "franskans adorateur). synonymer.se ger dyrkare utöver kortets två. Kortet är "
     "fortfarande delvis cirkulärt, och det är svårt att undvika: ordet ÄR ett "
     "ovanligare ord för beundrare. Där bär i stället registret (litterärt/ålderdomligt) "
     "och exempelmeningen inlärningen -- inte synonymlistan.",
     synonymer=["beundrare", "tillbedjare", "dyrkare"])


def main():
    index = {}
    for f in KALLOR:
        for e in json.load(open(f, encoding="utf-8")):
            index[e["ord"]] = e

    ut, saknade = [], []
    for ord_, (kalla, slutsats, andringar) in P.items():
        e = index.get(ord_)
        if e is None:
            saknade.append(ord_)
            continue
        e = json.loads(json.dumps(e))       # djupkopia
        e["sokkoll"] = {"kalla": kalla, "slutsats": slutsats}
        e["approved"] = True
        e["applicerad"] = False
        e.pop("skriven_av", None)
        for falt, varde in andringar.items():
            e["proposed"][falt] = varde
        e["oforandrad"] = not andringar
        ut.append(e)

    os.makedirs("sessions", exist_ok=True)
    json.dump(ut, open(MAL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(ut)} poster till {MAL}")
    print(f"  innehållsändrade: {sum(1 for e in ut if not e['oforandrad'])}")
    print(f"  enbart ny sökkoll: {sum(1 for e in ut if e['oforandrad'])}")
    if saknade:
        print("SAKNADE (fanns inte i sessionsfilerna):", saknade)


if __name__ == "__main__":
    main()
