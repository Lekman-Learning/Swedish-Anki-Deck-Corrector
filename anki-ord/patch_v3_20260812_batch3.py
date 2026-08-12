# -*- coding: utf-8 -*-
"""20 legacy-kort ur spår A (is:new) -> full v3.

**Första batchen skriven under den nya synonymspärren.** Alla synonymer nedan
är ordboksbelagda: antingen taggade `SYN:synonym` av SO, eller ledande ord i
SO:s/SAOL:s egen definition. Ingen kommer från syn.se.

Utfallet av regeln, som är själva poängen med batchen: **8 av 20 kort får tom
synonymlista** -- fiffel, hydrokultur, kanvas, bokslut, lagbunden, lektor,
metates och undra (den sista har en, `fråga sig`). Det är ungefär den andel
mätningen förutsade (69 % av alla uppslag saknar belägg helt) och är avsiktligt:
ett kort utan synonymer är godkänt, ett kort med en nästan-synonym är det inte.

Där ordboken faktiskt levererar blir synonymerna i gengäld starka:
`skolexempel` -> `typexempel` är SO:s egen SYN:synonym-taggning, och
`påpasslig` -> `alert, vaken` respektive `föresats` -> `ambition, mål` står
ordagrant i SAOL:s definition.

**Två avgränsningar värda att skriva ut:**

* `blodfattig` får bara den bildliga betydelsen. Den medicinska ("som lider av
  blodbrist") finns bara i wiktionary -- varken SO eller SAOL har den, och
  enligt källhierarkin avgör de två dagens betydelser.
* `hydrokultur` och `metates` vilar på två källor vardera (syn.se saknar den
  ena, wiktionary den andra).

`gemen` är batchens svåraste kort: SO har fem poster, från "elak på ett simpelt
sätt" till typografins gemena bokstav. Kortet tar de tre som faktiskt möts i
text och lämnar "i gemen" (= i allmänhet) därhän, eftersom den formen hör till
uttrycket snarare än till ordet.
"""
import json
import sys
import urllib.parse

SESSION = "sessions/session_2026-08-12_v3-batch3.json"
SVENSKA = "https://svenska.se/api/msearch?ord={}"

K = {}
PAUSAS = set()

KORT = {
    "blodfattig": {
        "hb": "som tycks sakna kraft och liv ; intetsägande och färglös",
        "syn": ["blek", "ointressant"],
        "ex": 'Texten var <font color="#3498db">blodfattig</font> och lämnade ingen bild kvar hos läsaren.',
        "reg": "neutral, lätt negativ ; neutral, negativ",
        "skal": "SO: 'som tycks sakna kraft och liv' med underbetydelsen "
                "'intetsägande, färglös'. Synonymerna är SAOL:s egen definition "
                "('äv. blek, ointressant'). Den medicinska betydelsen 'som lider av "
                "blodbrist' finns bara i wiktionary och tas inte in -- varken SO eller "
                "SAOL har den, och de avgör dagens betydelser.",
    },
    "fiffel": {
        "hb": "verksamhet som är på gränsen till olaglig",
        "syn": [],
        "ex": 'Revisorn upptäckte omfattande <font color="#3498db">fiffel</font> med reseräkningarna.',
        "reg": "vardaglig, negativ",
        "skal": "SO: 'verksamhet som är på gränsen till olaglig' med märkningen 'vardagligt' (SAOL: 'vard.'), som gav stilnivån. SAOL har posten utan "
                "definitionstext. Tom synonymlista: varken SO eller SAOL pekar ut något "
                "utbytbart ord, och framsidans 'smussel' är facit, inte en källa.",
    },
    "hydrokultur": {
        "hb": "odling av växter i näringsberikat vatten",
        "syn": [],
        "ex": 'Basilikan växte i <font color="#3498db">hydrokultur</font> utan en enda kruka jord.',
        "reg": "neutral, neutral",
        "skal": "SO: 'odling i (näringsberikat) vatten'; SAOL: 'odling av växter i "
                "vatten'. Tom synonymlista med flit: SO:s vattenbruk och vätskekultur är "
                "båda taggade JFR:cohyponym, alltså syskonord och inte synonymer. "
                "Wiktionary saknar posten -- två källor.",
    },
    "kanvas": {
        "hb": "grovt, styvt tyg av bomull eller hampa",
        "syn": [],
        "ex": 'Seglen var av <font color="#3498db">kanvas</font> och tålde saltvattnet i åratal.',
        "reg": "neutral, neutral",
        "skal": "SO: 'grovt, vanligen oblekt styvt tyg av bomull eller hampa'; SAOL: "
                "'ett kraftigt tyg'. Ingen av ordböckerna ger ett utbytbart ord -- bara "
                "beskrivande fraser, som hör hemma i huvudbetydelsen och inte i "
                "synonymlistan.",
    },
    "libertin": {
        "hb": "person som ohämmat ägnar sig åt njutningar",
        "syn": ["vällusting"],
        "ex": 'Han levde som en <font color="#3498db">libertin</font> och struntade i alla förmaningar.',
        "reg": "neutral, negativ",
        "skal": "SO: 'person som ohämmat ägnar sig åt (erotiska) njutningar'. "
                "SAOL:s hela definition är ordet 'vällusting', vilket är starkast "
                "möjliga belägg för synonymen. Valören följer av 'ohämmat' och av att "
                "SAOL väljer just vällusting.",
    },
    "skolexempel": {
        "hb": "särskilt tydligt och karakteristiskt exempel",
        "syn": ["typexempel"],
        "ex": 'Fallet är ett <font color="#3498db">skolexempel</font> på hur en utredning inte ska gå till.',
        "reg": "neutral, neutral",
        "skal": "SO: 'särskilt tydligt och karakteristiskt exempel', med typexempel "
                "taggat SYN:synonym -- ordbokens starkaste synonymmarkering. "
                "'skolboksexempel' utelämnat: SO taggar det JFR:jämför, inte synonym. "
                "Wiktionary saknar posten -- två källor.",
    },
    "gemen": {
        "hb": "elak på ett simpelt sätt ; vanlig och folklig ; liten bokstav i boktryck, till skillnad från versal",
        "syn": ["elak", "vanlig", "folklig"],
        "ex": 'Att sprida ryktet vidare var ett <font color="#3498db">gement</font> tilltag.',
        "reg": "neutral, negativ ; ngt ålderdomlig, neutral ; neutral, neutral",
        "skal": "SO har fem poster för ordet. Kortet tar de tre som faktiskt möts i "
                "text: 'elak på ett simpelt sätt', 'vanlig' och den typografiska "
                "gemenen. Betydelsen 'allmänhet' lämnas därhän -- den finns bara i "
                "uttrycket 'i gemen' och hör till frasen, inte till ordet. Alla tre "
                "synonymerna står i SAOL:s definitioner ('elak'; 'folklig; vanlig'). "
                "SO:s infam, lumpen, nedrig och perfid är taggade JFR:cohyponym och "
                "utelämnade.",
    },
    "blazer": {
        "hb": "kavaj som inte ingår i en kostym",
        "syn": ["udda kavaj"],
        "ex": 'Han bar en marinblå <font color="#3498db">blazer</font> till ljusa byxor.',
        "reg": "neutral, neutral",
        "skal": "SO: 'kavaj som inte ingår i kostym'; SAOL:s hela definition är 'udda "
                "kavaj', vilket belägger synonymen. 'jackett' utelämnat -- SO taggar "
                "det JFR:cohyponym. Wiktionary saknar posten -- två källor.",
    },
    "bokslut": {
        "hb": "sammanställning av bokföringen vid slutet av en redovisningsperiod",
        "syn": [],
        "ex": 'Företagets <font color="#3498db">bokslut</font> visade vinst för första gången.',
        "reg": "neutral, neutral, ekonomi",
        "skal": "SO: 'sammanställning av bokföring vid slutet av en redovisningsperiod'. "
                "Ingen ordbok ger ett utbytbart ord. Framsidans 'ekonomisk "
                "årsredovisning' är dessutom inte riktigt samma sak -- en årsredovisning "
                "är en offentlig handling som bygger PÅ bokslutet.",
    },
    "föresats": {
        "hb": "bestämd avsikt att lyckas med något",
        "syn": ["ambition", "mål"],
        "ex": 'Hans <font color="#3498db">föresats</font> att sluta röka höll i tre veckor.',
        "reg": "neutral, neutral",
        "skal": "SO: 'bestämd avsikt att lyckas med något'. SAOL:s hela definition är "
                "'ambition, mål' -- två belagda synonymer.",
    },
    "klausul": {
        "hb": "tilläggsbestämmelse eller förbehåll i ett avtal",
        "syn": ["förbehåll", "särbestämmelse", "tillägg"],
        "ex": 'Avtalet innehöll en <font color="#3498db">klausul</font> om uppsägning med tre månaders varsel.',
        "reg": "neutral, neutral, juridik",
        "skal": "SO: 'tilläggsbestämmelse eller förbehåll'; SAOL: 'förbehåll; tillägg; "
                "särbestämmelse' -- alla tre synonymerna inleder sina egna led i SAOL:s "
                "definition och är därmed belagda.",
    },
    "lagbunden": {
        "hb": "som regleras av lagar ; som följer ett regelbundet och förutsägbart mönster",
        "syn": [],
        "ex": 'Tidvattnet är <font color="#3498db">lagbundet</font> och går att räkna ut på förhand.',
        "reg": "neutral, neutral ; neutral, neutral",
        "skal": "SO ger två skilda betydelser: 'som regleras av lagar' (samhällets "
                "lagar) och 'som följer ett regelbundet, förutsägbart mönster' "
                "(naturlagar). Skillnaden är hela poängen med ordet och framsidans "
                "'reglerad och bestämd' fångar bara den första. Ingen belagd synonym.",
    },
    "lektor": {
        "hb": "titel för person med högre lärartjänst vid gymnasieskola eller högskola",
        "syn": [],
        "ex": 'Hon utnämndes till <font color="#3498db">lektor</font> i matematik vid högskolan.',
        "reg": "neutral, neutral",
        "skal": "SO: '(titel för) person med högre lärartjänst'; SAOL preciserar "
                "'vid gymnasieskola el. högskola'. 'adjunkt' utelämnat -- SO taggar det "
                "JFR:cohyponym, alltså en annan lärartitel och inte samma sak.",
    },
    "metates": {
        "hb": "omkastning av språkljud i ett ord",
        "syn": [],
        "ex": 'Namnformerna Andre och Anders skiljs åt av en <font color="#3498db">metates</font>.',
        "reg": "fackspråklig, neutral, lingvistik",
        "skal": "SO: 'omkastning av språkljud'; SAOL: 'omkastning av ljud'. "
                "Exempelmeningen använder framsidans eget exempelpar (Andre/Anders), "
                "där d och r byter plats. Wiktionarys kemibetydelse ('byte av "
                "bindningar mellan två molekyler') tas inte in -- varken SO eller SAOL "
                "har den. syn.se saknar posten -- två källor.",
    },
    "ombonad": {
        "hb": "hemtrevlig och bekväm",
        "syn": ["trivsam", "välordnad"],
        "ex": 'Stugan var liten men <font color="#3498db">ombonad</font>, med filtar och brasa.',
        "reg": "neutral, positiv",
        "skal": "SO: 'hemtrevlig och bekväm'; SAOL: 'välordnad, trivsam' -- båda "
                "synonymerna inleder sina led och är belagda.",
    },
    "pli": {
        "hb": "stramt och disciplinerat uppträdande",
        "syn": ["god hållning"],
        "ex": 'Sergeanten satte <font color="#3498db">pli</font> på rekryterna redan första veckan.',
        "reg": "neutral, neutral",
        "skal": "SO: 'stramt, disciplinerat uppträdande'; SAOL: 'disciplinerat skick, "
                "god hållning' -- den senare halvan är ett eget led och belägger "
                "synonymen.",
    },
    "påpasslig": {
        "hb": "som reagerar och handlar vid rätt tillfälle",
        "syn": ["alert", "vaken"],
        "ex": 'En <font color="#3498db">påpasslig</font> granne ringde brandkåren innan elden spred sig.',
        "reg": "neutral, positiv",
        "skal": "SO: 'som reagerar och handlar vid rätt tillfälle'. SAOL:s hela "
                "definition är 'alert, vaken'. Notera att SO samtidigt taggar 'alert' "
                "JFR:cohyponym -- men SAOL använder ordet som definition, vilket väger "
                "tyngre än en jämförelsehänvisning.",
    },
    "sensation": {
        "hb": "oväntad och uppseendeväckande händelse ; upplevelse som härrör från sinnesintryck",
        "syn": ["uppseendeväckande händelse", "sinnesintryck"],
        "ex": 'Fyndet blev en <font color="#3498db">sensation</font> i hela forskarvärlden.',
        "reg": "neutral, neutral ; neutral, neutral, psykologi",
        "skal": "SO ger två skilda betydelser, och SAOL samma två: "
                "'uppseendeväckande händelse el. företeelse' och 'sinnesintryck'. "
                "Den andra är den som brukar falla bort -- den är ren fackterm i "
                "psykologisk mening och syns sällan i vanlig text. 'skräll' utelämnat, "
                "SO taggar det JFR:cohyponym.",
    },
    "spritta": {
        "hb": "plötsligt rycka till i kroppen",
        "syn": ["rycka till", "hoppa till"],
        "ex": 'Hon <font color="#3498db">spritter</font> till varje gång dörren slår igen.',
        "reg": "neutral, neutral",
        "skal": "SO: 'plötsligt rycka till (i kroppen)'; SAOL: 'rycka till, hoppa till' "
                "-- båda synonymerna inleder sina led. SO taggar 'rycka' ensamt som "
                "JFR:cohyponym, men den fasta förbindelsen 'rycka till' är SAOL:s egen "
                "definition och alltså något annat än det enkla verbet.",
    },
    "undra": {
        "hb": "vara intresserad av att få veta ; tvivla på",
        "syn": ["fråga sig"],
        "ex": 'Jag <font color="#3498db">undrar</font> om tåget kommer i tid.',
        "reg": "neutral, neutral ; neutral, neutral",
        "skal": "SO ger två betydelser: 'vara intresserad av att få veta' (med "
                "'fråga sig' taggat SYN:synonym) och 'tvivla på'. SAOL har samma två. "
                "Framsidans facit är bara 'tvivla på', alltså den mindre vanliga av "
                "de två -- båda står nu på kortet.",
    },
}


def main():
    data = json.load(open(SESSION, encoding="utf-8"))
    poster = data["poster"] if isinstance(data, dict) else data

    kvar = [p for p in poster if p["ord"] not in PAUSAS]
    pausade = [p["ord"] for p in poster if p["ord"] in PAUSAS]

    saknar = [p["ord"] for p in kvar if p["ord"] not in KORT]
    if saknar:
        sys.exit(f"saknar rättelse för: {', '.join(saknar)}")

    for p in kvar:
        o = p["ord"]
        r = KORT[o]
        p["proposed"] = {
            "huvudbetydelse": r["hb"][0].upper() + r["hb"][1:],
            "synonymer": r["syn"],
            "synonym_groups": None,
            "exempelmening": r["ex"],
            "register": r["reg"],
            "etymologi": None,
        }
        p["approved"] = True
        p["sokkoll"] = {
            "kalla": SVENSKA.format(urllib.parse.quote(K.get(o, o))),
            "slutsats": r["skal"],
        }
        p.pop("applicerad", None)

    if isinstance(data, dict):
        data["poster"] = kvar
        ut = data
    else:
        ut = kvar
    json.dump(ut, open(SESSION, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    tomma = sum(1 for p in kvar if not p["proposed"]["synonymer"])
    print(f"fyllde {len(kvar)} poster -- {tomma} med tom synonymlista.")
    if pausade:
        print(f"UTESLUTNA (pausas separat): {', '.join(pausade)}")


if __name__ == "__main__":
    main()
