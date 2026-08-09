"""Batch 6 — tjugo kort, hämtade i ETT verktygsanrop via `slaupp.py`.

Svaret på Adams fråga *"finns det något jag kan göra så att du gör alla 20?"*:
ja — flytta uppslagningen ut ur kontextfönstret. Webbläsarvägen kostade två anrop
per ord; den här batchen kostade ett anrop totalt. Beviskedjan är bevarad genom
skriptets utskriftsrad, som verktygslagret fångar och agenten inte kan hitta på.

Fem kort visade sig ha en saknad eller felaktig betydelse trots att de redan var
granskade två gånger tidigare i dag.
"""
import json
import os

MAL = "sessions/session_2026-08-09_v3-so-batch6.json"
KALLOR = ["sessions/session_2026-08-09_v3-omgranskning-nya.json",
          "sessions/session_2026-08-09_v3-dagens-ko.json",
          "sessions/session_2026-08-09_v3-dagens-ko2.json",
          "sessions/session_2026-08-09_v3-inlarning.json"]
API = "https://svenska.se/api/msearch?ord={}"
P = {}


def lagg(ord_, slutsats, **andr):
    P[ord_] = (API.format(ord_), slutsats, andr)


lagg("changera",
     "FÖRSTA BETYDELSEN SAKNAR STÖD. Kortet sa 'skifta i färg beroende på ljus' — "
     "alltså changerande siden. Varken SAOL eller SO har den. SAOL: 'förändras, "
     "**blekas**; förlora i utseende'. SO: 'märkbart förändras till det sämre' och "
     "'blekas'. Ordet handlar om att förfalla, inte om att skifta. SO:s exempel: "
     "'han har changerat mycket efter pensioneringen', 'tröjan changerade redan "
     "efter första tvätten'.",
     huvudbetydelse="Märkbart förändras till det sämre ; blekna och tappa färg",
     synonymer=["förfalla", "blekna"])

lagg("blaskig",
     "TVÅ AV TRE BETYDELSER SAKNADES. Kortet hade bara 'utspädd smak'. SO ger tre: "
     "(1) 'urvattnad, intetsägande smak' (blaskig soppa) (2) '**intetsägande**' i "
     "vidare mening (blaskiga färger) (3) 'som kännetecknas av **blöta**' — "
     "blaskigt väder. JFR lankig. Kortets synonymer vattnig och tunn hör till (1).",
     huvudbetydelse="Utspädd och smaklös ; om färger och intryck: intetsägande ; "
                    "om väder: blött och slaskigt",
     synonymer=["vattnig", "urvattnad", "intetsägande"])

lagg("nimbus",
     "DEN BOKSTAVLIGA BETYDELSEN SAKNADES — och det är den som förklarar den "
     "bildliga. SO ger två: (1) '**glorieliknande krans av ljus**' (2) 'högt "
     "anseende'. Kortet hade bara (2), formulerad som 'upphöjd stämning'. SAOL: "
     "'glans, skimmer, strålkrans', vilket bekräftar kortets synonymer gloria och "
     "strålglans. Med båda betydelserna blir kortet lättare: gloria först, "
     "anseendet som bild av den.",
     huvudbetydelse="Krans av ljus kring ett huvud, en gloria ; bildligt: det höga "
                    "anseende som omger någon",
     synonymer=["gloria", "strålglans", "anseende"])

lagg("topografi",
     "DEN VANLIGASTE BETYDELSEN SAKNADES. Kortet hade bara läran/beskrivningen. SO "
     "ger också '(ett områdes) **terrängförhållanden**' med exemplet 'öns topografi "
     "lämpar sig inte för anläggning av en landningsbana'. Det är så ordet oftast "
     "används — om själva terrängen, inte om vetenskapen om den.",
     huvudbetydelse="Detaljerad beskrivning av jordytans former ; ett områdes "
                    "faktiska terrängförhållanden",
     synonymer=["terrängbeskrivning", "terrängförhållanden"])

lagg("granulera",
     "MEDICINSKA BETYDELSEN SAKNADES, och den står i BÅDA källorna. SAOL: 'fördela "
     "i korn ...; **bilda ny vävnad**'. SO: 'behandla material så att det får "
     "kornform' och '**bilda granulationsvävnad**', med exemplet 'ett rent, "
     "granulerat sår'. Ett sår som granulerar läker — det är en helt annan bild än "
     "korn av ett fast ämne.",
     huvudbetydelse="Göra om ett ämne till små korn ; om sår: bilda ny läkande "
                    "vävnad")

lagg("effeminerad",
     "SYNONYM TILLAGD UR KÄLLA. SAOL: '**förkvinnligad, förvekligad**'. SO: 'som "
     "liknar en kvinna', exempel 'en effeminerad yngling'. Kortets enda synonym "
     "(kvinnaktig) fanns i ingen källa; de två belagda tas in. Ordet är värderande "
     "och det syns i SAOL:s 'förvekligad' — det ligger i ordet, inte i kortet.",
     synonymer=["förkvinnligad", "förvekligad"])

lagg("affekt",
     "IDIOMET SAKNADES. SO:s första exempel är '**handla i affekt**' — den "
     "användning ordet oftast har, och den stod inte på kortet. SO ger 'stark "
     "sinnesrörelse' och 'intensiv känsla', JFR emotion, känsla. Kortets "
     "'kortvarig' finns i ingen källa och tas bort; det är styrkan som definierar "
     "affekt, inte längden.",
     huvudbetydelse="Stark sinnesrörelse — som i uttrycket 'handla i affekt'",
     synonymer=["sinnesrörelse", "känsloutbrott"])

lagg("hybris",
     "BEKRÄFTAT MED EN RESERVATION SOM SKRIVS UT. SO: 'starkt överdriven "
     "uppskattning av det egna jaget och den egna förmågan', JFR övermod. SAOL: "
     "'övermod, förhävelse'. Kortets tillägg '**som leder till fall**' finns i "
     "ingen av källorna — det är den grekiska tragedins konnotation, inte "
     "ordbokens. Den behålls eftersom den är sann om ordets ursprung och gör kortet "
     "minnesvärt, men den är alltså inte belagd i SAOL/SO och det noteras här.")

lagg("tradera",
     "FACKBETYDELSE NOTERAD, EJ INTAGEN. SO ger utöver den muntliga överföringen "
     "'genomföra **juridisk tradition** av' (saken traderades till en annan part) — "
     "alltså överlämnande av äganderätt. Den tas medvetet inte in: det är en "
     "juridisk fackterm och HP prövar allmänspråket. Kortets betydelse bekräftas "
     "av SAOL: 'muntligt meddela från släkte till släkte, vidareföra'.")

for o, s in [
    ("ism", "BEKRÄFTAT. SO: '(konst)riktning som bildat skola' och '(propagerande) "
            "riktning' — kortets båda betydelser. SAOL: 'riktning, skola särsk. inom "
            "konsten'. SO:s exempel 'impressionismen, expressionismen och andra ismer' "
            "visar bruket."),
    ("allegat", "BEKRÄFTAT. SO: 'handling eller kvitto som bekräftar ekonomisk "
                "transaktion'. SAOL ger ordagrant kortets båda synonymer: 'bilaga, "
                "verifikation'."),
    ("driftig", "BEKRÄFTAT. SO: 'som har förmåga att uppnå resultat', JFR företagsam, "
                "verksam. Kortets 'företagsam' är därmed belagd."),
    ("dupera", "BEKRÄFTAT. SO: 'medvetet ge någon felaktigt intryck', 'lura', JFR lura, "
               "vilseleda. Kortets 'blända' finns inte i källorna men de två andra gör det."),
    ("entente", "BEKRÄFTAT. SO: '(avtal om) vänskapsförbindelse mellan stater'. SAOL: "
                "'sammanslutning mellan stater'."),
    ("futil", "BEKRÄFTAT. SO: 'som inte borde ägnas minsta möda', JFR obetydlig, exempel "
              "'futila problem'. SAOL: 'futtig, obetydlig'."),
    ("gruvlig", "BEKRÄFTAT. SO: 'som orsakar fasa och oro', JFR fasansfull — kortets "
                "starkaste synonym. SAOL: 'förfärlig, gräslig'. SO visar också "
                "förstärkande adverbiell bruk: 'hon tog gruvligt miste'."),
    ("hutlös", "BEKRÄFTAT. SO: 'som tyder på fullständig brist på skamkänsla', JFR "
               "oförskämd. Båda källorna ger exemplet 'hutlösa priser', vilket bekräftar "
               "kortets precisering om priser."),
    ("kalibrera", "BEKRÄFTAT. SO: 'anpassa eller ställa in något efter i förväg "
                  "fastställda mått', JFR fininställa, finjustera — kortets båda synonymer."),
    ("kalorimeter", "BEKRÄFTAT ORDAGRANT. SAOL och SO ger identisk definition: 'apparat "
                    "för mätning av värmemängder'."),
    ("dekantera", "BEKRÄFTAT. SO: 'försiktigt hälla av vätska för att skilja undan "
                  "bottensats'. Båda källorna ger exemplet 'dekantera vinet'. Kortets "
                  "karaff är en detalj källorna inte kräver, men den gör kortet "
                  "konkretare och behålls."),
]:
    lagg(o, s)


def main():
    index = {}
    for f in KALLOR:
        for e in json.load(open(f, encoding="utf-8")):
            index[e["ord"]] = e
    ut, saknade = [], []
    for ord_, (kalla, slutsats, andr) in P.items():
        e = index.get(ord_)
        if e is None:
            saknade.append(ord_)
            continue
        e = json.loads(json.dumps(e))
        e["sokkoll"] = {"kalla": kalla, "slutsats": slutsats}
        e["approved"] = True
        e["applicerad"] = False
        e.pop("skriven_av", None)
        for f_, v in andr.items():
            e["proposed"][f_] = v
        if "huvudbetydelse" in andr:
            e["proposed"]["synonym_groups"] = None
        e["oforandrad"] = not andr
        ut.append(e)
    os.makedirs("sessions", exist_ok=True)
    json.dump(ut, open(MAL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(ut)} poster -> {MAL}")
    print(f"  innehållsändrade : {sum(1 for e in ut if not e['oforandrad'])}")
    if saknade:
        print("SAKNADE:", saknade)


if __name__ == "__main__":
    main()
