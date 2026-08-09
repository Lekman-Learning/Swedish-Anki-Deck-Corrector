"""Batch 4 — inlärningskön (is:learn), tio kort mot svenska.se.

Adam bad om att börja med korten i inlärningskön eftersom de är de han möter
först. Mätning innan start: **17 kort i is:learn, noll av dem sökkollade.**

Adams precisering av Adam-tal 2026-08-09: *"inte specifikt att definitionen ska
vara kortare, men den ska vara mer koncis och enklare att förstå för mig."*
Skillnaden är verklig — batch 3 kortade, den här försöker i stället skriva så att
meningen går att förstå vid första läsningen. Ibland betyder det fler ord, inte färre.

Träfflistefällan gick att lösa. `förslagen` gav samma disambigueringslista som
`civiliserad` (adjektiv + två substantivformer), men ett klick på "förslagen adj."
i sidan når artikeln. `civiliserad` behöver alltså inte förbli rödflaggad — den kan
plockas upp igen med samma metod.
"""
import json
import os

MAL = "sessions/session_2026-08-09_v3-so-batch4.json"
KALLOR = ["sessions/session_2026-08-09_v3-omgranskning-nya.json",
          "sessions/session_2026-08-09_v3-dagens-ko.json",
          "sessions/session_2026-08-09_v3-dagens-ko2.json",
          "sessions/session_2026-08-09_v3-inlarning.json"]
SV = "https://svenska.se/tre/?sok={}"
P = {}


def lagg(ord_, sok, slutsats, **andr):
    P[ord_] = (SV.format(sok), slutsats, andr)


lagg("fascikel", "fascikel",
     "DEFINITIONEN VAR EN ANNAN BETYDELSE. Kortet sa 'del av ett verk som ges ut i "
     "omgångar' — den bibliografiska betydelsen. Varken SAOL eller SO har den. "
     "SAOL: 'bunt skrifter; häfte'. SO: ⟨mindre brukligt⟩ 'bunt papper', JFR häfte, "
     "med exemplet 'handlingarna ligger i faskiklar, sorterade ämnesvis'. Ordet "
     "betyder alltså en **bunt**. Båda källorna stavar dessutom uppslaget "
     "**faskikel** i första hand.",
     huvudbetydelse="En bunt papper eller skrifter som hör ihop",
     synonymer=["häfte", "pappersbunt"])

lagg("fisförnäm", "fisförnäm",
     "DEN ENDA BELAGDA SYNONYMEN SAKNADES. SAOL och SO ger båda exakt ett ord: "
     "**struntförnäm**. Kortets tre synonymer (snobbig, högfärdig, fjantig) finns i "
     "ingen av källorna. SO märker ordet ⟨vardagligt⟩ och ger exemplet 'de "
     "fisförnäma kusinerna från Kalifornien', som fångar tonen bättre än kortets "
     "abstrakta formulering.",
     huvudbetydelse="Spelar förnäm på ett sätt som bara blir löjligt",
     synonymer=["struntförnäm"])

lagg("oväldig", "oväldig",
     "EN SYNONYM VAR FEL SAK. Kortet hade 'omutlig' — men omutlig betyder att inte "
     "gå att muta, oväldig betyder att inte ta parti. SO: ⟨något högtidligt⟩ "
     "'rättvis', JFR objektiv, opartisk. Kortets övriga två synonymer är alltså "
     "belagda, den tredje byts ut. Exempel ur SO: 'en oväldig domare'.",
     huvudbetydelse="Dömer rättvist utan att ta parti för någon sida",
     synonymer=["opartisk", "objektiv", "rättvis"])

lagg("pöbel", "pöbel",
     "REGISTRET VAR FÖR SVAGT. SO märker ordet ⟨**starkt** nedsättande⟩ och SAOL "
     "⟨nedsätt.⟩ — kortet hade ingen sådan markering. SO:s definition är också "
     "skarpare än kortets: 'föraktade personer ur de lägsta samhällsklasserna med "
     "tonvikt på (förment) brist på moral'. Ordet **säger något om den som använder "
     "det**. JFR mobb, plebs, slödder; 'pack' finns i ingen källa.",
     huvudbetydelse="Föraktfullt om folk ur samhällets lägsta skikt ; en folkhop "
                    "som ställer till upplopp",
     synonymer=["mobb", "slödder"],
     register="nedsättande")

lagg("käck", "käck",
     "TOM SYNONYMLISTA FYLLD MED BELAGDA ORD. SO ger JFR **frimodig, hurtig, kavat** "
     "och definitionen 'som handlar oförskräckt och med glatt humör' — vilket "
     "bekräftar att kortets båda betydelser (glad/rask och obekymrat modig) hör ihop "
     "i en enda. SAOL: 'pigg, frimodig; trevlig'. Facits 'modig' från i morse "
     "stämmer alltså, men modet är av det glada slaget, inte det tappra.",
     huvudbetydelse="Glad och oförskräckt på samma gång — tar sig an saker med gott "
                    "humör",
     synonymer=["frimodig", "hurtig", "kavat"])

lagg("gensaga", "gensaga",
     "FACKMARKERING SAKNADES. SO: ⟨**särskilt juridik**⟩ 'svar som bestämt uttrycker "
     "avvikande ståndpunkt', JFR invändning, protest, reservation. Kortets tre "
     "synonymer är alltså nästan helt belagda ('motsägelse' finns inte, "
     "'reservation' gör det). Att ordet hör hemma i juridiskt språk är den upplysning "
     "som skiljer det från vanlig 'invändning'.",
     huvudbetydelse="Formellt bestridande av ett påstående, särskilt i juridiska "
                    "sammanhang",
     synonymer=["invändning", "protest", "reservation"])

lagg("beveka", "beveka",
     "PRECISERAD. SO: 'ändra eller mildra inställning hos någon genom **vädjan till "
     "känslor**'. SAOL: 'vädja till och övertala'. Kortets två betydelser (påverka "
     "genom vädjan / mildra någons ovilja) är alltså EN betydelse i källorna — det "
     "är samma sak sedd från två håll. Slås ihop, vilket också gör kortet enklare. "
     "Facits exempel från i morse (Orfeus bevekte underjordens härskare med sin sång) "
     "illustrerar precis känslovädjan.",
     huvudbetydelse="Få någon att mjukna genom att vädja till känslorna",
     synonymer=["blidka", "övertala"])

lagg("förvärva", "förvärva",
     "FORMATFELET BEKRÄFTAT LÖST. Kortet hade tidigare betydelserna åtskilda med "
     "' / ' i stället för ' ; ' och lästes därför aldrig som två. SO bekräftar att "
     "det ÄR två: 'bli ägare till något, t.ex. genom köp; ofta med avseende på "
     "ägodelar **men äv. abstraktare**', med exemplen 'förvärva byggnaden' och "
     "'**förvärva kunskaper**'. Båda betydelserna på kortet är alltså belagda i en "
     "och samma källa.")

lagg("rabalder", "rabalder",
     "PRECISERAD. Kortet sa 'högljutt tumult'. SO: 'allmän diskussion eller gräl med "
     "upprörda känslor, ibland övergående i handgemäng', JFR uppståndelse. Ordet "
     "börjar alltså i ett **gräl**, inte i oväsen — handgemänget är undantaget, inte "
     "regeln. SAOL bekräftar kortets synonymer: oväsen, bråk, uppståndelse.",
     huvudbetydelse="Högljutt gräl som drar till sig uppmärksamhet")

lagg("förslagen", "förslagen",
     "TRÄFFLISTEFÄLLAN LÖST MED KLICK. ?sok=förslagen gav en disambigueringslista "
     "(adjektivet plus två böjningsformer av substantivet 'förslag') — samma fälla "
     "som stoppade `civiliserad`. Ett klick på 'förslagen adj.' i sidan når "
     "artikeln: SAOL ger '**slug, listig**'. Kortets 'listig' är därmed belagd och "
     "'bakslug' ligger nära; 'illmarig' står kvar men är inte belagd här. "
     "Konsekvens: `civiliserad` behöver inte förbli rödflaggad.")


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
        # Grupper som inte längre matchar antalet betydelser stoppas av
        # Adam-tal-spärren (hände avbörda sig i batch 3). Nollställ dem när
        # huvudbetydelsen skrivits om, så får synonymer-fältet gälla.
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
