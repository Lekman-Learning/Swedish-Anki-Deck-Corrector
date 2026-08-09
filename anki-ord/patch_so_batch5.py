"""Batch 5 — resten av inlärningskön. Efter den här är alla 17 sökkollade.

Metodregel som föll ut ur `bära sig`, och som gäller alla idiom:
**slå upp GRUNDORDET, inte frasen.** `synonymer.se/sv-syn/bära sig` gav
"inget resultat"; `synonymer.se/sv-syn/bära` listade uttrycket med båda dess
betydelser. Wiktionary gav 404 på frasen. svenska.se visade "bära sig" och
"bära sig åt" i sin lista men lämnade ut texten.

Det är den konkreta formen av Adams observation att svenska.se bara tar enstaka
uppslagsord — och av hans instruktion att söka vidare när tre källor inte räcker.
Här krävdes fyra försök innan uttrycket var belagt.
"""
import json
import os

MAL = "sessions/session_2026-08-09_v3-so-batch5.json"
KALLOR = ["sessions/session_2026-08-09_v3-omgranskning-nya.json",
          "sessions/session_2026-08-09_v3-dagens-ko.json",
          "sessions/session_2026-08-09_v3-dagens-ko2.json",
          "sessions/session_2026-08-09_v3-inlarning.json"]
SV = "https://svenska.se/tre/?sok={}"
SYN = "https://www.synonymer.se/sv-syn/{}"
P = {}


def lagg(ord_, kalla, slutsats, **andr):
    P[ord_] = (kalla, slutsats, andr)


lagg("brokad", SV.format("brokad"),
     "TVÅ FEL. (1) 'jacquardvävt' finns i ingen källa och är dessutom ett ord som "
     "gör kortet svårare än det behöver vara. SAOL: 'sidentyg med guld- el. "
     "silvertrådar'. SO: 'tjockt, mönstrat sidentyg ofta med inslag el. botten av "
     "guld- el. silvertråd'. (2) **Silver saknades** — kortet nämnde bara guld. "
     "Den upplysande kontrasten är [[damast]]: damast är enfärgad och får sitt "
     "mönster ur väven, brokad är mönstrad med metalltråd.",
     huvudbetydelse="Tjockt, mönstrat sidentyg med inslag av guld- eller silvertråd",
     synonymer=["guldtyg", "silvertyg"])

lagg("beskärm", SV.format("beskärm"),
     "REGISTRET VAR FÖR TRUBBIGT. Kortet sa 'arkaisk'. Båda källorna är mer "
     "precisa: SAOL ⟨bibl.⟩ och SO ⟨särskilt bibliskt⟩ — ordet är inte bara gammalt, "
     "det hör hemma i bibelspråk. SO:s exempel visar det: 'under den Allsmäktiges "
     "beskärm'. Konstruktionen är nästan alltid 'i/under NÅGONS beskärm'. Kortets "
     "synonymer värn och beskydd täcks av SO:s 'skydd och värn'; 'hägn' står kvar "
     "obelagt men är samma bildvärld.",
     huvudbetydelse="Någons skydd och värn över en annan — nästan alltid i uttrycket "
                    "'under någons beskärm'",
     register="arkaisk")

lagg("damast", SV.format("damast"),
     "PRECISERAD. Kortet sa att mönstret syns 'genom vävens glans'. SO säger "
     "'enfärgad vävnad med **rik reliefmönstring**' — mönstret sitter i ytan som "
     "relief, glansen är följden. SAOL: 'ett enfärgat mönstervävt tyg'. Att tyget är "
     "**enfärgat** är den avgörande upplysningen och den fanns redan på kortet; den "
     "skiljer damast från [[brokad]], som är mönstrad med guld- eller silvertråd.",
     huvudbetydelse="Enfärgat tyg där mönstret vävs in som relief och syns i glansen")

lagg("bära sig", SYN.format("bära"),
     "IDIOM — BELAGT FÖRST PÅ FJÄRDE FÖRSÖKET, OCH KORTET HADE RÄTT. "
     "svenska.se listade 'bära sig' men lämnade ut texten; "
     "synonymer.se/sv-syn/bära sig gav 'inget resultat'; Wiktionary gav 404. "
     "Men **synonymer.se på GRUNDORDET** (/sv-syn/bära) listar uttrycket med båda "
     "betydelserna: (1) 'slumpa sig, hända sig' (2) 'gå bra, löna sig', med "
     "relaterade uttryck löna sig, ge vinst, betala sig. Kortets båda betydelser och "
     "båda synonymer är därmed belagda, ordagrant. "
     "**Regel för idiom: slå upp grundordet, inte frasen.**")

lagg("vråk", SV.format("vråk"),
     "KORTET VAR REDAN RÄTT — OCH DET ÄR VÄRT ATT NOTERA. Båda betydelserna står i "
     "SAOL: '1 en fågel 2 isränna, råk'. SO beskriver fågeln: 'grovt byggd rovfågel "
     "med breda vingar och bred, något rundad stjärt', med sammansättningarna "
     "bivråk, fjällvråk, ormvråk. Kortet hade båda och behövde ingen ändring. "
     "KVARSTÅENDE PROBLEM som INTE är språkligt: kortets bild är hotlänkad till "
     "upload.wikimedia.org i stället för att ligga i collection.media. Den syns så "
     "länge datorn har nät och Anki tillåter extern laddning — annars inte.")

lagg("bjugg", SV.format("bjugg"),
     "BEKRÄFTAT UTAN ÄNDRING. SAOL: ⟨åld.⟩ 'sädesslaget korn'. SO: ⟨ålderdomligt⟩ "
     "'(sädesslaget) korn'. Kortets definition, synonym och arkaiska register "
     "stämmer med båda källorna. Ordet finns även i SAOB, alltså tre träffar.")

lagg("förvissning", SV.format("förvissning"),
     "BEKRÄFTAT, MED EN BRUKSREGEL TILLAGD I MOTIVERINGEN. SO: '(vanligen i vissa "
     "uttryck) personlig, djupgående övertygelse', konstruktion 'i förvissning om "
     "NÅGOT'. SAOL: 'visshet, fast övertygelse' — kortets båda synonymer ordagrant. "
     "Kortets exempelmening ('i den fasta förvissningen att...') använder just den "
     "konstruktion SO pekar ut, så kortet lär redan ut rätt sak.")


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
        print("SAKNADE i sessionsfilerna:", saknade)


if __name__ == "__main__":
    main()
