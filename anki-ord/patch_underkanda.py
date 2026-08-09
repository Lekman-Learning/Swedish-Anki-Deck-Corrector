"""De två kort som den blinda granskaren UNDERKÄNDE 2026-08-09.

Detta är första gången underkännanden från ett oberoende `verdikt` rättas — och
båda visade sig vara verkliga fel som jag själv hade infört samma dag.

Lärdomen är skarpare än bara "två kort blev bättre":

**På `vedervåga` hade granskaren rätt om FELET men fel om ÅTGÄRDEN.** Den hävdade
att synonymen "våga sig på" inte var belagd. SAOL har den ordagrant: "sätta på
spel; våga sig på". Granskaren nådde aldrig svenska.se (JS-renderad via WebFetch)
och dömde på SAOB 1933 + synonymer.se. Men dess *observation* var riktig: sätt in
synonymen i kortets egen exempelmening och den blir ogrammatisk. Slutsatsen blir
alltså den motsatta av den föreslagna — synonymen ska INTE strykas, **betydelsen
den hör till ska läggas till**.

Det är ett argument för att ge nästa blinda granskare tillgång till `slaupp.py`.
En granskare utan den bästa källan blir sämre än nödvändigt, och kan råka döma
rätt sak av fel skäl.
"""
import json
import os
import urllib.parse

MAL = "sessions/session_2026-08-09_v3-underkanda.json"
P = {}


def _api(o):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(o)


def lagg(ord_, slutsats, **andr):
    P[ord_] = (_api(ord_), slutsats, andr)


lagg("vedervåga",
     "UNDERKÄND AV BLIND GRANSKARE — RÄTTAD, MEN ÅT ANDRA HÅLLET ÄN FÖRESLAGET. "
     "Granskaren påpekade att 'våga sig på' inte går att sätta in i kortets egen "
     "exempelmening ('Ingen ville *våga sig på* sitt liv') och föreslog att stryka "
     "den. **SAOL har den dock ordagrant: 'sätta på spel; våga sig på'** — "
     "granskaren nådde aldrig svenska.se och dömde på SAOB 1933. Observationen var "
     "ändå riktig: synonymen hör till ett ANDRA bruk som kortet saknade. Rätt "
     "åtgärd är därför att lägga till den betydelsen, inte att ta bort synonymen. "
     "SO saknar uppslaget helt.",
     huvudbetydelse="Riskera något värdefullt ; våga sig på något farligt",
     synonymer=["sätta på spel", "äventyra", "våga sig på"])

lagg("revy",
     "UNDERKÄND AV BLIND GRANSKARE — TVÅ FEL BEKRÄFTADE OCH ETT TREDJE UPPTÄCKT. "
     "(1) Registret: granskaren hade rätt att 'vardaglig' är fel. Ingen källa "
     "märker ordet som vardagligt; det är den etablerade genrebeteckningen. "
     "Skärpt argument från granskaren: en enda registeretikett kan inte täcka både "
     "den levande genrebeteckningen och den ålderdomliga mönstringsbetydelsen. "
     "(2) Synonymen 'spex' är inte belagd — SO ger JFR **kabaré, varieté**. Spex är "
     "dessutom specifikt studentamatörteater, alltså inte utbytbart. "
     "(3) EN TREDJE BETYDELSE som varken kortet, jag eller granskaren hade: SO ger "
     "'**förbimarsch av trupp**' och SAOL 'mönstring' — den militära paraden är "
     "ursprunget till uttrycket 'passera revy'. SO:s tre betydelser: föreställning "
     "med blandad underhållning ; översiktlig artikel ; förbimarsch av trupp.",
     huvudbetydelse="Scenföreställning med blandad, aktuell underhållning ; "
                    "översikt eller artikel ; militär förbimarsch — som i "
                    "'passera revy'",
     register="formell",
     synonymer=["kabaré", "varieté"])


def main():
    kallor = ["sessions/session_2026-08-09_v3-so-batch2.json",
              "sessions/session_2026-08-09_v3-sokkoll-omgorning.json",
              "sessions/session_2026-08-09_v3-dagens-ko.json",
              "sessions/session_2026-08-09_v3-dagens-ko2.json",
              "sessions/session_2026-08-09_v3-omgranskning-nya.json",
              "sessions/session_2026-08-09_v3-inlarning.json"]
    index = {}
    for f in kallor:
        if not os.path.exists(f):
            continue
        for e in json.load(open(f, encoding="utf-8")):
            index.setdefault(e["ord"], e)
    ut = []
    for ord_, (kalla, slutsats, andr) in P.items():
        e = json.loads(json.dumps(index[ord_]))
        if not e.get("proposed"):
            e["proposed"] = json.loads(json.dumps(e.get("legacy") or {}))
        e["sokkoll"] = {"kalla": kalla, "slutsats": slutsats}
        e["approved"] = True
        e["applicerad"] = False
        e.pop("skriven_av", None)
        for f_, v in andr.items():
            e["proposed"][f_] = v
        if "huvudbetydelse" in andr:
            e["proposed"]["synonym_groups"] = None
        e["oforandrad"] = False
        ut.append(e)
    json.dump(ut, open(MAL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(ut)} poster -> {MAL}")


if __name__ == "__main__":
    main()
