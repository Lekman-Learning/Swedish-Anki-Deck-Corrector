"""De sju kort där jag slog upp fel ord.

På uppslag, girig, signera, sepia, slapstick och vernissage slog jag upp den
BORTTAGNA synonymen (boköppning, habegärlig, initialera, brunton, misskastning,
öppningsvisning) och aldrig uppslagsordet självt. På "lägga sordin på" slog jag upp
`sordin`. Kortets egna innehåll stod alltså fortfarande utan källa.

Adams regel 2026-08-09: två eller tre källor räcker, men noll är oacceptabelt --
och tre är ett MINIMUM, inte ett tak: hittar jag inte svaret ska jag söka vidare.

Regel som lades till samtidigt: **SAOB och svenska.se tar bara enstaka uppslagsord.**
Idiom och flerordsuttryck går aldrig att belägga där -- de ska sökas på synonymer.se,
Wiktionary och fri webbsökning. `lägga sordin på` är fallet som visade det.
"""
import json
import os

MAL = "sessions/session_2026-08-09_v3-sokkoll-de-sju.json"
KALLOR = ["sessions/session_2026-08-09_v3-omgranskning-nya.json",
          "sessions/session_2026-08-09_v3-dagens-ko.json",
          "sessions/session_2026-08-09_v3-dagens-ko2.json",
          "sessions/session_2026-08-09_v3-inlarning.json"]

S = "https://www.saob.se/artikel/?seek={}"
Y = "https://www.synonymer.se/sv-syn/{}"
W = "https://sv.wiktionary.org/wiki/{}"

P = {}


def lagg(ord_, kalla, slutsats, **andr):
    P[ord_] = (kalla, slutsats, andr)


lagg("uppslag",
     " + ".join([S.format("uppslagsord"), Y.format("uppslag"), W.format("uppslag")]),
     "TRE KÄLLOR PÅ ORDET SJÄLVT (tidigare slogs bara den borttagna synonymen "
     "'boköppning' upp). MISSLYCKAD DIREKTHÄMTNING: ?seek=uppslag gav en träfflista "
     "med två artiklar vars id inte går att konstruera; ?seek=uppslagsord bär i "
     "stället och bekräftar sammansättningsledet. synonymer.se: (1) idé, tanke, "
     "impuls, plan, förslag, utkast (2) byxuppslag (3) två motstående sidor i en bok. "
     "Wiktionary: boksidorna, uppslagsordet i ett uppslagsverk, samt idé -- den "
     "sistnämnda MÄRKT SOM SAKNANDE KÄLLA hos Wiktionary, men den är primär hos "
     "synonymer.se och är dessutom OLD-facits egen glosa. Kortets två betydelser står "
     "därmed belagda.")

lagg("girig",
     " + ".join([S.format("girig"), Y.format("girig"), W.format("girig")]),
     "SAKNAD BETYDELSE, hittad först när ordet självt slogs upp. Wiktionary ger två: "
     "(1) överdrivet begär efter pengar och ägodelar (2) **'som häftigt åstundar'** -- "
     "exemplet är att dricka girigt efter en ökenmarsch, alltså utan koppling till "
     "pengar. SAOB har samma uppdelning plus en ålderdomlig om växter som växer "
     "ymnigt. Kortets tre synonymer (snål, vinningslysten, sniken) är alla belagda hos "
     "synonymer.se, som också ger närig, penningkär, gnidig.",
     huvudbetydelse="Vill hänsynslöst ha mer, särskilt pengar ; som häftigt åtrår "
                    "något för stunden")

lagg("signera",
     " + ".join([S.format("signera"), Y.format("signera"), W.format("signera")]),
     "TRE KÄLLOR PÅ ORDET SJÄLVT. SAOB ger fyra betydelser, varav tre är "
     "ålderdomliga (ringa in en lektion, dra lott, känneteckna) och medvetet "
     "utelämnas. synonymer.se: underteckna, underskriva, påteckna, attestera, skriva "
     "under. Wiktionary: 'förse med signatur'. Kortets båda synonymer belagda i alla "
     "tre. Grammatikrättelsen skriv under -> skriva under står kvar.",
     synonymer=["skriva under", "underteckna", "attestera"])

lagg("sepia",
     " + ".join([S.format("sepia"), Y.format("sepia"), W.format("sepia")]),
     "STÖRSTA FYNDET AV DE SJU. Kortet sa bara 'brunaktig färgton, som på gamla foton' "
     "-- den härledda fotografiska betydelsen. INGEN av de tre källorna leder med den. "
     "SAOB: (1) bläckfisken Sepia officinalis (2) brunt pigment ur bläckfiskens "
     "bläcksäck (3) sepiaskalet. Wiktionary: mörkbrunt färgämne från bläckfiskar, samt "
     "djuret. synonymer.se: bläcket från bläckfisk, och pigmentet gjort av det. "
     "Kortet saknade alltså både ursprunget och djurbetydelsen. Färgtonen behålls "
     "först eftersom den är den betydelse HP prövar, men den står inte längre ensam.",
     huvudbetydelse="Mörkbrunt färgämne ur bläckfiskens bläck, och den brunaktiga "
                    "färgton det ger ; själva bläckfisken",
     synonymer=["bläckfiskbläck", "sepiabrunt"])

lagg("slapstick",
     " + ".join([S.format("slapstick"), Y.format("slapstick"), W.format("slapstick")]),
     "MITT ANTAGANDE VAR FEL: jag utgick från att ordet var för modernt för SAOB och "
     "hade struntat i att söka. SAOB HAR det -- 'burlesk situationskomik o. ofta "
     "våldsamt tempo', ur amerikansk engelska slap + stick (rekvisitan: två "
     "träpinnar som slås ihop för ljudeffekt). synonymer.se: '(stum)filmfars i högt "
     "tempo' -- fars, buskis, burdus humor, dårfars. OLD-facits 'en sorts filmfars' "
     "stämmer alltså ordagrant med synonymer.se. 'fysisk komedi' fanns i ingen källa "
     "och ersätts med belagda buskis och dårfars.",
     synonymer=["fars", "buskis", "dårfars"])

lagg("vernissage",
     " + ".join([S.format("vernissage"), Y.format("vernissage"), W.format("vernissage")]),
     "FELAKTIG SYNONYM HITTAD. Kortet hade 'förhandsvisning', som finns i ingen källa "
     "och dessutom är missvisande: SAOB säger 'högtidligt öppnande och invigning av "
     "en konstutställning med inbjudna gäster och förfriskningar', och Wiktionary "
     "'öppnandet OCH första dagen'. En vernissage är alltså själva öppningen, inte en "
     "visning före den. synonymer.se ger utställningsöppnande, konstpremiär, "
     "premiärvisning. Wiktionary ger invigning, och motsatsen finissage.",
     synonymer=["invigning", "konstpremiär", "premiärvisning"])

lagg("lägga sordin på",
     " + ".join([S.format("sordin"), Y.format("sordin"), W.format("sordin")]),
     "IDIOM -- OCH DÄRMED ETT FALL SAOB INTE KAN AVGÖRA. Adam påpekade 2026-08-09 att "
     "SAOB och svenska.se bara tar enstaka uppslagsord; flerordsuttryck går inte att "
     "slå upp där. `sv.wiktionary.org/wiki/lägga_sordin_på` gav 404. Uttrycket är i "
     "stället belagt via grundordet i två källor: Wiktionary listar 'lägga sordin' "
     "uttryckligen under den bildliga betydelsen ('dämpning av något slag, "
     "tillbakahållande'), och synonymer.se förklarar det som 'stämningen dras ner av "
     "något'. SAOB bekräftar grundordets två betydelser (dämpare på instrument; "
     "bildligt dämpad framställning). Borttagningen av 'hämma' står kvar -- hindra är "
     "inte dämpa.")


def main():
    index = {}
    for f in KALLOR:
        for e in json.load(open(f, encoding="utf-8")):
            index[e["ord"]] = e
    ut = []
    for ord_, (kalla, slutsats, andr) in P.items():
        e = json.loads(json.dumps(index[ord_]))
        e["sokkoll"] = {"kalla": kalla, "slutsats": slutsats}
        e["approved"] = True
        e["applicerad"] = False
        e.pop("skriven_av", None)
        for f_, v in andr.items():
            e["proposed"][f_] = v
        e["oforandrad"] = not andr
        ut.append(e)
    os.makedirs("sessions", exist_ok=True)
    json.dump(ut, open(MAL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(ut)} poster -> {MAL}")
    print(f"  innehållsändrade : {sum(1 for e in ut if not e['oforandrad'])}")
    print(f"  enbart ny sökkoll: {sum(1 for e in ut if e['oforandrad'])}")


if __name__ == "__main__":
    main()
