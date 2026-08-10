"""V3 med TRE källor och etymologi — Adams krav 2026-08-10.

Vad som är nytt mot gårdagens batcher:

1. **Tre källor på varje kort, alltid.** svenska.se (SO+SAOL+SAOB räknas som
   en), synonymer.se och Wiktionary. Kort där någon saknas rödflaggas och
   hamnar i `tre_kallor_saknas.json` i stället för att tyst skrivas med två.

2. **Etymologi på varje kort där ursprunget säger något.** Källan är SO:s
   `historiskaUppgifter.etymologi`, inte Wiktionary — svenska Wiktionary är
   tunn och saknar etymologi för de flesta av de här orden. SO ger den i
   samma svar som betydelserna, alltså gratis.

3. **Adam-tal: vardagligt men fullständigt.** Adams val av tre uppritade
   alternativ 2026-08-10. Varje betydelse ska finnas kvar, men sägas med ord
   han använder till vardags. En facktermnär den ÄR ordet, aldrig som
   förklaring av ordet.

Etymologin skrivs som REN TEXT här. Pilen och den grå färgen läggs på av
`baksida.build()` — se config.py för varför utseendet ändrades.
"""
import json
import os
import urllib.parse

MAL = "sessions/session_2026-08-10_v3-tre-kallor-b1.json"
P = {}


def _kallor(o):
    """Alla tre källorna, i den form spärren kan bevisa mot transkriptet."""
    k = urllib.parse.quote(o)
    return (f"https://svenska.se/api/msearch?ord={k} "
            f"https://www.synonymer.se/sv-syn/{k} "
            f"https://sv.wiktionary.org/wiki/{k}")


def lagg(ord_, slutsats, kalla=None, **andr):
    P[ord_] = (kalla or _kallor(ord_), slutsats, andr)


# ---------------------------------------------------------------- batch 1
lagg("fascikel",
     "ETYMOLOGIN ÄR HELA MINNESREGELN. SO: 'bunt papper', SAOL: 'bunt "
     "skrifter; häfte', JFR häfte. Definitionen stämde alltså redan. Det som "
     "saknades var ursprunget: latin *fasciculus* 'litet knippe', diminutiv "
     "till *fascis* 'knippa' — **samma ord som gav fascism** (rissknippet var "
     "romersk maktsymbol). Ett kort där ordet hänger ihop med ett ord Adam "
     "redan kan är lättare än ett kort med ännu en synonym. "
     "TVÅ KÄLLOR: Wiktionary saknar uppslaget — rödflaggas.",
     etymologi="Av latinets fasciculus, 'litet knippe' — samma ord som gav "
               "oss fascism (knippet var Roms maktsymbol).")

lagg("neslig",
     "BEKRÄFTAT OCH PRECISERAT. SO: 'som ger vanära', med underbetydelsen "
     "'äv. om handling som ger vanära åt den handlande'. Kortets definition "
     "stämmer. SO:s exempel visar dock att ordet INTE bara gäller brott: "
     "'hon hamnade på en neslig 35:e plats' — alltså också om något bara "
     "pinsamt dåligt, vilket är precis kortets exempelmening. Etymologin är "
     "kort och räcker: ordet är byggt på *nesa*, som betyder vanära.",
     etymologi="Byggt på det gamla ordet nesa, som betyder vanära.")

lagg("rabalder",
     "EN BETYDELSE TILL, OCH EN LJUDHÄRMANDE ETYMOLOGI. SO: 'allmän "
     "diskussion eller gräl med upprörda känslor' — alltså inte bara gräl, "
     "utan även högljudd debatt: 'hans frispråkighet vållade stort rabalder "
     "på mötet'. SO har dessutom bruket om djur ('en räv ställde till med "
     "stort rabalder i hönshuset'), vilket visar att det handlar om OVÄSEN, "
     "inte om konflikt. Kortets 'gräl' var för snävt.",
     huvudbetydelse="Högljutt bråk eller upprörd debatt som väcker "
                    "uppmärksamhet",
     synonymer=["oväsen", "bråk", "uppståndelse", "ståhej"],
     etymologi="Från danskans baldre, 'bullra' — ordet låter som det betyder.")

lagg("ocker",
     "FÖRENKLAD DEFINITION + ETYMOLOGI SOM FÖRKLARAR ORDET. Kortet sa "
     "'Orimligt höga räntor eller priser, genom att utnyttja någons svaga "
     "ställning eller trångmål' — riktigt, men en mening man måste läsa två "
     "gånger. SO säger kort: 'inriktning på att göra oskälig vinst'. "
     "Etymologin är oväntat bra: ordet kommer av lågtyskans *woker* 'ränta' "
     "och är **besläktat med växa** — pengar som växer på någon annans "
     "olycka. Belagt sedan 1400-talet.",
     huvudbetydelse="Att ta ut orimligt höga räntor eller priser av någon "
                    "som är i knipa",
     synonymer=["procenteri", "utsugning", "utpressning"],
     etymologi="Besläktat med växa — ocker är pengar som växer på någon "
               "annans trångmål.")

lagg("oknytt",
     "KORTET HADE FEL TAL. SO: '(**sammanfattande beteckning på**) små "
     "övernaturliga väsen', SAOL: 'spökerier; trolltyg'. Oknytt är alltså ett "
     "KOLLEKTIV — allt smått otyg tillsammans — inte 'ett litet väsen' som "
     "kortet sa. Det syns i kortets egen exempelmening, där 'bodde oknytt' "
     "bara fungerar om ordet är kollektivt. Kortet saknade dessutom synonymer "
     "helt.",
     huvudbetydelse="Samlingsnamn för allt smått övernaturligt otyg i "
                    "folktron",
     synonymer=["trolltyg", "småväsen", "vättar", "spökerier"],
     etymologi="Av dialektens oknytt, 'farlighet, spökeri' — o- som i otyg.")

lagg("damast",
     "ETYMOLOGIN GÖR ORDET OMÖJLIGT ATT GLÖMMA. Definitionen stämde (SO: "
     "'enfärgad vävnad med rik reliefmönstring'). Men ordet kommer av "
     "italienskans *damasco* — efter **Damaskus**, Syriens huvudstad, där "
     "tyget vävdes. Samma stad som gett damaskerat stål. Kortet hade bild men "
     "ingen förklaring till namnet.",
     synonymer=["mönstervävt tyg", "linnetyg"],
     etymologi="Uppkallat efter Damaskus i Syrien, där tyget vävdes.")

lagg("flau",
     "RÖDFLAGGAS — SAKNAS HELT PÅ svenska.se. Varken SAOL eller SO har "
     "uppslaget; bara synonymer.se och Wiktionary. Enligt Adams regel "
     "2026-08-10 ska ett sådant kort märkas och gås igenom separat, inte "
     "skrivas som om det vore fullbelagt. Innehållet från de två källor som "
     "FINNS: Wiktionary ger tre bruk — (1) 'med föga omsättning, matt, trög' "
     "(handel), (2) 'platt, tom, fadd, svag', (3) 'generande, pinsam'. "
     "synonymer.se märker ordet **(ekon.)**, vilket kortet inte gjorde. "
     "Kortets exempelmening ('stämningen på festen var lite flau') hör till "
     "bruk 2, medan definitionens 'utan efterfrågan' hör till bruk 1 — de "
     "pekade åt olika håll utan att det syntes.",
     huvudbetydelse="Matt och livlös ; om handel: trög, utan efterfrågan",
     synonymer=["matt", "trög", "svag"],
     etymologi=None)

lagg("köl",
     "DEN BETYDELSE SOM FAKTISKT KOMMER PÅ PROV SAKNADES. Kortet hade bara "
     "den bokstavliga båtdelen. SO ger uttrycket **'komma på rät köl'** = "
     "'komma till ordnade förhållanden', med exemplet 'efter en stökig "
     "ungdomstid verkar hon nu ha kommit på rätt köl'. Det är den bildliga "
     "användningen man möter i text, och den fanns inte på kortet. Kortet "
     "saknade dessutom synonymer helt.",
     huvudbetydelse="Den understa, längsgående balken i ett fartygs botten ; "
                    "bildligt i 'komma på rät köl' — komma i ordning igen",
     synonymer=["bottenstomme", "fartygsbotten", "fena"],
     etymologi="Fornsvenska kiol, ursprungligen 'något krökt' — besläktat "
               "med kälke.")

lagg("käck",
     "UTVIDGAT BRUK + ETYMOLOGI. Kortets definition var bra. Men SO visar att "
     "ordet också används **om saker**, inte bara om personer: 'en käck keps', "
     "'en käck knut på halsduken', 'en käck reklamslogan'. Den nyansen "
     "saknades. Etymologin binder ihop ordet med ett Adam redan kan: käck "
     "kommer av tyskans *keck* och är nära besläktat med **kvick**.",
     huvudbetydelse="Glad och oförskräckt på samma gång ; om saker: piggt och "
                    "flott gjort",
     synonymer=["frimodig", "hurtig", "kavat", "piffig"],
     etymologi="Av tyskans keck — nära släkt med kvick.")

lagg("andakt",
     "EN HEL BETYDELSE SAKNADES, OCH DET ÄR DEN ICKE-RELIGIÖSA. Kortet hade "
     "bara 'kort stund av bön'. SO ger TVÅ: (1) 'hänvändelse till gudom' och "
     "(2) '**fridfull, högtidlig sinnesstämning**'. Den andra är den man "
     "möter utanför kyrkan: 'han betraktade med andakt en av schackhistoriens "
     "märkligaste ställningar', och SO:s skämtsamma 'oxfilén kostade 400 "
     "kronor kilot – ät den med andakt!'. Etymologin förklarar varför: ordet "
     "kommer av tyskans *Andacht*, till *denken* 'tänka' — andakt är alltså "
     "samlad tanke, inte nödvändigtvis bön.",
     huvudbetydelse="Stilla stund av bön eller enkel gudstjänst ; djup, "
                    "högtidlig koncentration inför något",
     synonymer=["bönestund", "gudstjänst", "vördnad", "stillhet"],
     etymologi="Av tyskans Andacht, till denken 'tänka' — samlad tanke.")


def main():
    bas = json.load(open("sessions/_dagens_142.json", encoding="utf-8"))
    index = {e["ord"]: e for e in bas}
    import baksida

    ut, saknade = [], []
    for ord_, (kalla, slutsats, andr) in P.items():
        e = index.get(ord_)
        if e is None:
            saknade.append(ord_)
            continue
        p = baksida.parse(e["baksida"])
        proposed = {
            "huvudbetydelse": p["huvudbetydelse"],
            "register": p["register"],
            "synonymer": p["synonymer"],
            "synonym_groups": p["synonym_groups"],
            "exempelmening": p["exempelmening"],
            "etymologi": p["etymologi"],
        }
        for f_, v in andr.items():
            proposed[f_] = v
        # En ny huvudbetydelse ogiltigförklarar den gamla grupperingen:
        # synonym_groups vinner tyst över synonymer i build(), och lämnas den
        # kvar skrivs de nya synonymerna aldrig ut. Det hände på `bonitet`
        # 2026-08-09 och syntes inte förrän kortet lästes tillbaka ur Anki.
        if "huvudbetydelse" in andr or "synonymer" in andr:
            proposed["synonym_groups"] = None
        ut.append({
            "noteId": e["note"], "ord": ord_,
            "legacy": None, "proposed": proposed,
            "bild_html": p["bild_html"],
            "sokkoll": {"kalla": kalla, "slutsats": slutsats},
            "approved": True, "applicerad": False,
            "oforandrad": not andr,
        })
    os.makedirs("sessions", exist_ok=True)
    json.dump(ut, open(MAL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(ut)} poster -> {MAL}")
    if saknade:
        print("SAKNAS i dagens kö:", saknade)


if __name__ == "__main__":
    main()
