"""Batch 9 — tio FÄRSKA kort ur is:new, aldrig granskade förut.

Skilt från batch 1–8: de korten hade redan gått igenom två granskningar under
dagen. De här tio är orörda, och är därför det bästa måttet på vad v3 med riktig
sökkoll faktiskt hittar på ogranskat material.

Utfall: **7 av 10 ändrade.**

Två strukturella vinster på köpet:
- `civiliserad` var rödflaggad och suspenderad eftersom webbläsaren gav en
  träfflista i stället för artikeln. **API-vägen har inte det problemet** — den
  returnerar artikeln direkt. Kortet är löst och kan avsuspenderas.
- `runda ord` visar idiomregeln i två steg: uttrycket fanns inte på `runda ord`,
  fanns som *hänvisning* under `rund`, och hade sin *definition* under `ord`.
  Slå upp grundordet, och följ hänvisningen vidare.
"""
import json
import os
import urllib.parse

MAL = "sessions/session_2026-08-09_v3-so-batch9.json"
WIKT = "https://sv.wiktionary.org/wiki/{}"
P = {}


def _api(o):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(o)


def lagg(ord_, slutsats, kalla=None, **andr):
    P[ord_] = (kalla or _api(ord_), slutsats, andr)


lagg("besynnerlig",
     "CIRKULÄRT KORT. Definitionen löd 'Egendomlig, märklig' och synonymlistan var "
     "'egendomlig, märklig' — **ordagrant samma sträng**. Kortet lärde inte ut "
     "någonting. SO ger två riktiga betydelser: '**svår att förstå sig på**' och "
     "'**något tokig**' (om person), plus JFR egendomlig, kuriös, mystisk. SAOL: "
     "'konstig, märkvärdig'. Exempel ur SO: 'kattugglans besynnerliga utseende'.",
     huvudbetydelse="Svår att förstå sig på och därför lite underlig ; om person: "
                    "något tokig",
     synonymer=["egendomlig", "kuriös", "märkvärdig"])

lagg("atonal",
     "EN SYNONYM VAR FEL SAK OCH MOTSATSEN SAKNADES. Kortet hade '**tonlös**' — men "
     "tonlös betyder ljudlös eller (i fonetik) obetonad, inte utan tonart. SO ger "
     "JFR **tonal**, motsatsen, som är den enda minnesregel ordet behöver. SO har "
     "också en andra betydelse: '**tondöv**' om person. Exempel: 'tolvtonsmusik är "
     "atonal'.",
     huvudbetydelse="Om musik: obunden till tonart, motsatsen till tonal ; om "
                    "person: tondöv",
     synonymer=["utan tonart", "dissonant"])

lagg("bleke",
     "ANDRA BETYDELSEN SAKNADES OCH DET FANNS ETT STAVFEL. Båda källorna ger två "
     "betydelser: SAOL 'stiltje, stilla vattenyta' OCH '**starkt kalkhaltig vit "
     "jord**'; SO 'vindstilla över spegelblank vattenyta' OCH '**jordart som främst "
     "består av kalkslam**'. Kortet hade bara sjöbetydelsen. Dessutom stod "
     "'**vinstilla**' i synonymlistan — ett d saknades. JFR stiltje bekräftar den "
     "belagda synonymen.",
     huvudbetydelse="Vindstilla med spegelblank vattenyta ; kalkrik vit jordart",
     synonymer=["stiltje", "spegelblankt vatten"])

lagg("daktyloskopi",
     "PÅHITTAD SYNONYM BORTTAGEN. Kortet hade '**daktning**', som inte är ett "
     "svenskt ord — synonymer.se föreslår aktning, taktning, diktning i stället, "
     "alltså ingen träff. SAOL saknar uppslaget helt; SO har det: 'en metod att "
     "identifiera personer med hjälp av fingeravtryck'. Notera att SO säger "
     "**metod**, inte 'lära' som kortet.",
     huvudbetydelse="Metod att identifiera personer med hjälp av fingeravtryck",
     synonymer=["fingeravtrycksanalys"])

lagg("runda ord",
     "REGISTRET VAR FEL, OCH IDIOMET KRÄVDE TVÅ STEG. Uttrycket finns inte på "
     "uppslaget 'runda ord'; det ligger som **hänvisning** under `rund` (belagt "
     "sedan 1967) och har sin **definition** under `ord`: 'vardagliga ord för "
     "sexuella företeelser', med exemplet 'i farsen förekommer en del **svordomar "
     "och** runda ord'. Just det exemplet visar att runda ord INTE är svordomar — de "
     "är den mildare varianten. Kortets register 'vulgär' är därför fel; det ska "
     "vara vardagligt. Kortets synonymer (sexslang, fräckisar) finns i ingen källa.",
     huvudbetydelse="Vardagliga, mildare ord för sexuella saker",
     register="vardaglig",
     synonymer=[])

lagg("civiliserad",
     "RÖDFLAGGNINGEN UPPHÄVD. Kortet suspenderades tidigare i dag eftersom "
     "webbläsaren gav en träfflista (adjektiv + verbformer) i stället för artikeln. "
     "**API-vägen har inte det problemet.** SO ger fyra betydelser: (1) 'präglas av "
     "materiellt och kulturellt välordnat samhällsskick' (2) 'präglas av gott och "
     "hyfsat umgängessätt' (3) 'överföra civilisation till' (4) 'bibringa hyfsat "
     "umgängessätt'. Kortets båda betydelser motsvarar (2) och (1) — i den ordningen, "
     "vilket är rätt för HP. SO:s exempel är lysande: 'han återvände till mer "
     "civiliserade trakter efter några år som polarforskare'.")

lagg("hurtbulle",
     "PRECISERAD UR KÄLLA. SO: '(överdrivet) hurtig och **sportig** person'. "
     "Sportigheten stod inte på kortet men är det som gör bilden konkret. SAOL: "
     "'överdrivet hurtig person'. Kortets 'friskus' och 'käckis' finns i ingen källa "
     "men fångar tonen; de behålls och det noteras.",
     huvudbetydelse="Överdrivet pigg och sportig person")

lagg("håvor",
     "SYNONYM TILLAGD UR KÄLLA. SAOL: 'gåvor, **rikedomar**'. SO: 'gåvor', med de "
     "fasta uttrycken '**Guds håvor**' och '**lyckans håvor**' — ordet används nästan "
     "bara i sådana fraser, vilket är värt att veta. Kortets 'skänker' finns i ingen "
     "källa.",
     synonymer=["gåvor", "rikedomar"])

lagg("ad interim",
     "EJ I SAOL/SO — BELAGT PÅ WIKTIONARY. Uppslaget saknas i båda Akademiens "
     "ordböcker och i synonymer.se. Wiktionary har det: latinskt adverb, "
     "'(temporärt) tills vidare; under en övergångstid', med förkortningen **a.i.** "
     "Kortets definition stämmer ordagrant. **Vilar på en källa**, vilket skrivs ut.",
     kalla=WIKT.format("ad_interim"))

lagg("deadline",
     "BEKRÄFTAT. SO: 'bestämd tidpunkt när något senast måste vara avslutat', JFR "
     "**tidsgräns** — kortets första synonym, belagd. SAOL: 'tidpunkt då ngt måste "
     "vara klart'. SO ger kollokationerna 'hålla en deadline' och 'missa en "
     "deadline'.")


def main():
    # _batch9_bas.json byggs av kortbyggare.bygg_post() direkt mot Anki, eftersom
    # nio av tio kort är FÄRSKA och saknar sessionsdata. Fälten extraheras då av
    # samma kod som resten av pipelinen använder, i stället för att jag tolkar
    # HTML:en på egen hand -- en tolkning som kan bli fel utan att synas.
    kallor = ["sessions/_batch9_bas.json",
              "sessions/session_2026-08-09_v3-omgranskning-nya.json",
              "sessions/session_2026-08-09_v3-dagens-ko.json",
              "sessions/session_2026-08-09_v3-dagens-ko2.json",
              "sessions/session_2026-08-09_v3-inlarning.json"]
    index = {}
    for f in kallor:
        for e in json.load(open(f, encoding="utf-8")):
            index[e["ord"]] = e
    # De flesta av de tio är FÄRSKA kort utan sessionsdata. Bygg poster direkt
    # ur Anki för dem.
    import urllib.request
    import re as _re

    def q(a, p=None):
        r = urllib.request.Request("http://127.0.0.1:8765",
                                   json.dumps({"action": a, "version": 6,
                                               "params": p or {}}).encode())
        return json.loads(urllib.request.urlopen(r).read())["result"]

    ut, saknade = [], []
    for ord_, (kalla, slutsats, andr) in P.items():
        e = index.get(ord_)
        if e is None:
            saknade.append(ord_)
            continue
        e = json.loads(json.dumps(e))
        if not e.get("proposed"):
            e["proposed"] = json.loads(json.dumps(e.get("legacy") or {}))
        e["sokkoll"] = {"kalla": kalla, "slutsats": slutsats}
        e["approved"] = True
        e["applicerad"] = False
        e.pop("skriven_av", None)
        # INDENTERINGSBUGG 2026-08-09: tilldelningen låg en gång UTANFÖR loopen,
        # så bara sista nyckeln i `andr` applicerades. Eftersom `synonymer` råkade
        # stå sist i varje anrop skrevs synonymerna men aldrig huvudbetydelsen
        # eller registret -- korten såg uppdaterade ut och var det till hälften.
        # Hittat genom att läsa tillbaka live-innehållet ur Anki, inte genom att
        # lita på att `applicerad: True` betydde att allt skrivits.
        for f_, v in andr.items():
            e["proposed"][f_] = v
        if "huvudbetydelse" in andr:
            e["proposed"]["synonym_groups"] = None
        e["oforandrad"] = not andr
        ut.append(e)
    os.makedirs("sessions", exist_ok=True)
    json.dump(ut, open(MAL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(ut)} poster -> {MAL}")
    print("SAKNAR sessionsdata (byggs separat):", saknade)


if __name__ == "__main__":
    main()
