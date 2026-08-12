# -*- coding: utf-8 -*-
"""ARM A -- 20 provisoriskt släppta kort (sökkollade, aldrig blindgranskade).

Halva experimentet som Adam beställde 2026-08-12: *"20 av de sökkollade
provisoriska v3 korten och 20 från de icke sökkollade korten på is:review"*.
Skalar upp 10-mot-10-försöket från 2026-08-11 till 20 mot 20. Armarna hålls i
skilda sessionsfiler hela vägen — slås de ihop går hela mätningen förlorad.

Slumpat urval, frö 20260812, ur populationen 607 (`tag:v3_provisorisk::*`
utan `oberoende_verifierad`, `v3_pausad` eller `v3_underkand`).

## Vad de 20 faktiskt visade

Sökkollen har gjort sitt jobb på **formen**: alla 20 är v2, alla har register,
alla har en exempelmening. Ingen enda hade den sortens uppenbara skräp som
legacy-korten i spår A är fulla av. Mekaniskt syns det redan i riskflaggorna —
3 av 20 med hög flagga här mot 8 av 20 i arm B.

Felen som återstår är av ett annat slag, och de delar en form: **kortet säger
något vidare eller smalare än källan.**

* **`doyen`** — kortet: "person med längst erfarenhet och högst anseende inom
  sitt område". SO: "den till tjänsteåren äldste inom den diplomatiska kåren i
  ett land". Kortet hade generaliserat bort både kåren och tjänsteåren, och
  gjort ordet till en synonym för *nestor* i allmänhet.
* **`assimilera`** — kortet gav "anpassa sig till en större grupp", alltså det
  reflexiva sociala fallet. SO har fyra betydelser och ordet är i grunden
  transitivt: man assimilerar något.
* **`örlogsfartyg`** — "militärt krigsfartyg" tappar det som skiljer ordet från
  *krigsfartyg*: att det tillhör en stats marina stridskrafter.

## Sju kort saknade en betydelse som källan har

`kapsejsa` (bildligt: misslyckas), `impressionistisk` (SO:s underbetydelse
"som utmärks av bristande planering"), `menisk` (SO:s konkavkonvexa lins),
`tradera` (den juridiska traditionen), `normera` ("utgöra norm för"), `preja`
(tränga ett fordon av vägen) och `sätta sig` ("vara nedlåtande" — som till och
med står i kortets EGET OLD-facit).

## Två register som motsäger ordbokens märkning

`gamman` stod som *litterär* fast SO och SAOL båda märker ordet ålderdomligt,
och `leva i sus och dus` som *litterär* fast märkningen är vardagligt. Båda
skulle ha fastnat i `forgranska.py`s `register_motsager_markning`, som inte
fanns när korten skrevs.

## Två exempelmeningar som inte går att läsa högt

* `sätta sig`: "Trött efter promenaden lät hon sig sätta sig på den närmaste
  bänken" — *lät hon sig sätta sig*.
* `nödbedd`: "Han hjälpte till till slut" — *till till*.

Båda är sådant som en sökkoll aldrig kan fånga: källan säger ingenting om
kortets svenska.

## Två hårda flaggor som medvetet står kvar

`gnöl` får `register_motsager_markning` och kommer att göra det oavsett vad
registret säger: SO märker ordet BÅDE *vardagligt* och *provinsiellt*, medan
registerformatet bara rymmer en stilnivå per betydelse. Vardaglig är den mer
användbara av de två för Adams syfte, så den behålls. Regeln har rätt om att
det finns en märkning den inte hittar; den kan bara inte veta att det är
omöjligt att få plats med båda.

`leva i sus och dus` får `frammande_uppslagsord` med 29 grannartiklar, av
samma skäl som fraserna i spår A: svenska.se:s fritextsökning har inget
uppslagsord att matcha mot. Innehållet kommer från synonymer.se, inte från
grannartiklarna.
"""

import json
import sys
import urllib.parse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FARG = "#3498db"
SVENSKA = "https://svenska.se/api/msearch?ord={}"
SESSION = "sessions/session_2026-08-12_armA-provisorisk.json"


def h(o):
    return f'<font color="{FARG}">{o}</font>'


KORT = {
    "kapsejsa": {
        "hb": "Kantra och lägga sig på sidan, om båt ; misslyckas fullständigt",
        "reg": "neutral, neutral, sjöfart ; vardaglig, negativ",
        "grupper": [["kantra", "stjälpa"], ["misslyckas", "haverera"]],
        "ex": f"Båten {h('kapsejsade')} i den kraftiga stormen.",
        "skal": "SO har underbetydelsen 'misslyckas' som kortet saknade, och "
                "SAOL skriver ut 'äv. bildl.'. Registret var 'formell' — "
                "kapsejsa är ett vanligt sjötermsord, inte formellt.",
    },
    "gnöl": {
        "hb": "Ständigt klagande eller gnällande",
        "reg": "vardaglig, lätt negativ",
        "syn": ["klagan", "knot", "tjat"],
        "ex": f"Kollegorna tröttnade på hans ständiga {h('gnöl')} om allt som "
              f"var fel på kontoret.",
        "skal": "SO 'klagande', märkt vardagligt och dialektalt. 'Gnäll' ströks "
                "ur synonymlistan — inte för att det är fel, utan för att det är "
                "så nära ljudlikt att det fungerar som en ledtråd snarare än ett "
                "svar. Knot och tjat står båda i synonymer.se.",
    },
    "menisk": {
        "hb": "Broskskiva som dämpar stötar i en led, som i knäet ; krökt "
              "vätskeyta i ett trångt rör ; konkavkonvex lins",
        "reg": "fackspråklig, neutral, medicin ; fackspråklig, neutral, fysik ; "
               "fackspråklig, neutral, fysik",
        "grupper": [["broskskiva"], ["vätskeyta"], ["konkavkonvex lins"]],
        "ex": f"{h('Menisken')} i knäet kan skadas vid en vridning.",
        "skal": "SO och SAOL har OLIKA andrabetydelser: SO 'konkavkonvex lins', "
                "SAOL 'buktig vätskeyta i trångt rör'. Kortet hade bara SAOL:s. "
                "Unionen är tre betydelser, och synonymer.se märker dem själv "
                "(med.) respektive (fys.).",
    },
    "antecipera": {
        "hb": "Gå händelserna i förväg ; göra något före den bestämda tiden",
        "reg": "formell, neutral",
        "syn": ["föregripa", "förutse"],
        "ex": f"Hans tidiga skisser {h('anteciperar')} hela den moderna "
              f"arkitekturen.",
        "skal": "Kortet skrev de två betydelserna som 'Göra något före bestämd "
                "tid / föregripa' — snedstreck i stället för ' ; ', vilket gör "
                "dem osynliga för registerindragningen och alla svepningar. "
                "Exemplet var dessutom en satsfragment utan predikat.",
    },
    "impressionistisk": {
        "hb": "Som hör till konststilen impressionismen ; som präglas av "
              "bristande planering",
        "reg": "neutral, neutral, konst ; neutral, lätt negativ",
        "syn": [],
        "ex": f"Monet målade {h('impressionistiska')} landskap med snabba "
              f"penseldrag.",
        "skal": "SO har underbetydelsen 'som utmärks av bristande planering' — "
                "den överförda, lätt nedsättande användningen ('en "
                "impressionistisk utredning'). Kortet hade bara konstbetydelsen. "
                "Etymologifältet innehöll en tom sträng i stället för null.",
    },
    "blodfull": {
        "hb": "Livfull och livskraftig",
        "reg": "litterär, positiv",
        "syn": ["livfull", "livskraftig", "mustig"],
        "ex": f"Den {h('blodfulla')} unga hjältinnan drev handlingen framåt.",
        "skal": "SO 'livfull och livskraftig', SAOL 'äv. mustig, fängslande'. "
                "'Kraftfull' saknar stöd i källorna och betyder något annat — "
                "styrka, inte livskraft. Valören är positiv, inte neutral.",
    },
    "frodig": {
        "hb": "Fysiskt väl utvecklad och yppig ; rikt växande och grönskande",
        "reg": "neutral, positiv",
        "syn": ["yppig", "ymnig", "välfödd"],
        "ex": f"Den {h('frodiga')} skogen var full av liv och grönska.",
        "skal": "SO leder med kroppen ('fysiskt väl utvecklad', underbetydelse "
                "'fet och godmodig') och har växtligheten som 'starkt produktiv'. "
                "Kortet hade bara växtbetydelsen. 'Mustig' saknar stöd här — det "
                "hör till blodfull, inte frodig.",
    },
    "tradera": {
        "hb": "Föra vidare muntligt från generation till generation ; juridiskt "
              "överlämna besittningen av något",
        "reg": "formell, neutral",
        "syn": ["vidareföra"],
        "ex": f"Berättelsen {h('traderades')} muntligt genom generationerna.",
        "skal": "SO har en andra betydelse, 'genomföra juridisk tradition av', "
                "som kortet saknade. 'Överföra' och 'förmedla' ströks som för "
                "vida — tradera är alltid över tid och alltid vidare i en kedja. "
                "SAOL:s egen gloss 'vidareföra' behålls.",
    },
    "nödbedd": {
        "hb": "Svår att övertala, ger med sig först efter mycket truggande",
        "reg": "litterär, neutral",
        "syn": ["ovillig", "svårbedd", "trögbedd"],
        "ex": f"Han var {h('nödbedd')} och ställde upp först efter mycket tjat.",
        "skal": "SO 'svår att övertala', SAOL 'som måste trugas'. "
                "'Trögövertalad' finns inte som ord; synonymer.se ger i stället "
                "svårbedd, trögbedd och nödbjuden. Exemplet löd 'Han hjälpte "
                "till till slut' — dubblerat 'till'.",
    },
    "preja": {
        "hb": "Anropa och tvinga ett fartyg att stanna ; tränga ett fordon av "
              "vägen ; ta alltför mycket betalt av någon",
        "reg": "ngt ålderdomlig, neutral, sjöfart ; neutral, neutral ; "
               "vardaglig, negativ",
        "grupper": [["tvinga att stanna"], ["tränga undan"], ["skinna", "pungslå"]],
        "ex": f"Handelsfartyget {h('prejades')} av en jagare i blockadflottan.",
        "skal": "SO har underbetydelsen 'tränga (fordon) av vägen' som kortet "
                "saknade — den moderna användningen. Kortet skrev dessutom "
                "'(vardagligt)' inuti huvudbetydelsen samtidigt som registret sa "
                "samma sak; märkningen hör hemma i registret, inte i texten.",
    },
    "de jure": {
        "hb": "I kraft av lagen, formellt lagligt",
        "reg": "formell, neutral, juridik",
        "syn": ["lagenligt"],
        "ex": f"Regeringen hade {h('de jure')} makten att fatta beslut.",
        "skal": "SO 'i kraft av lagen'. Kortet var i sak riktigt; enda ändringen "
                "är att domänen juridik skrivits ut och att formuleringen följer "
                "SO:s ordval. SO taggar de facto som JFR:cohyponym — motparet är "
                "hela poängen med uttrycket.",
    },
    "örlogsfartyg": {
        "hb": "Krigsfartyg som tillhör en stats marina stridskrafter",
        "reg": "neutral, neutral, militär",
        "syn": ["krigsfartyg"],
        "ex": f"Det svenska {h('örlogsfartyget')} patrullerade Östersjön under "
              f"övningen.",
        "skal": "Kortets 'militärt krigsfartyg' är dels tautologiskt, dels "
                "tappar det det som SO faktiskt säger: tillhörigheten till en "
                "STATS marina stridskrafter. Ett kapat lastfartyg med kanoner är "
                "inget örlogsfartyg. SO taggar hangarfartyg som JFR:hyponym, "
                "alltså ett specialfall — det får inte bli synonym.",
    },
    "doyen": {
        "hb": "Den till tjänsteåren äldste i en kår, särskilt inom diplomatin",
        "reg": "formell, neutral",
        "syn": ["nestor", "ålderspresident"],
        "ex": f"Han var {h('doyen')} i diplomatkåren efter tjugo år i landet.",
        "skal": "RÄTTAT: kortet sa 'person med längst erfarenhet och högst "
                "anseende inom sitt område' — vidare än ordet. SO: 'den till "
                "tjänsteåren äldste inom den diplomatiska kåren i ett land', "
                "SAOL 'ålderspresident i en kår'. Det är tjänsteåren som avgör, "
                "inte anseendet, och 'veteran' ströks av samma skäl.",
    },
    "assimilera": {
        "hb": "Omvandla något till större likhet med omgivningen ; införliva och "
              "ta upp i det egna",
        "reg": "formell, neutral",
        "syn": ["införliva", "sammansmälta"],
        "ex": f"Många invandrare i USA under 1800-talet {h('assimilerades')} "
              f"snabbt.",
        "skal": "RÄTTAT: kortet gav 'anpassa sig till en större grupp', alltså "
                "bara det reflexiva sociala fallet. SO har fyra betydelser och "
                "ordet är i grunden transitivt — man assimilerar NÅGOT. SO taggar "
                "dissimilera som MOTSATS:antonym, vilket visar axeln: likhet mot "
                "olikhet, inte grupptillhörighet.",
    },
    "grogrund": {
        "hb": "Miljö som gynnar att något växer eller uppstår",
        "reg": "neutral, neutral",
        "syn": ["härd", "jordmån"],
        "ex": f"Smutslagret var en utmärkt {h('grogrund')} för bakterier.",
        "skal": "SO 'miljö där något växer bra'. Registret stod som 'litterär' "
                "trots popularitet 12 942 och SAOL:s vardagsnära exempel 'en "
                "grogrund för extremism' — ordet är helt neutralt.",
    },
    "normera": {
        "hb": "Fastställa en norm för något ; utgöra normen för något",
        "reg": "formell, neutral",
        "syn": ["standardisera", "reglera"],
        "ex": f"Den svenska stavningen {h('normerades')} inte förrän på 1800-talet.",
        "skal": "SO har underbetydelsen 'utgöra norm för' vid sidan av "
                "'fastställa norm för' — skillnaden mellan att sätta regeln och "
                "att vara den. Kortet hade bara den första.",
    },
    "leva i sus och dus": {
        "hb": "Leva ett bekymmerslöst liv fullt av fest och lyx",
        "reg": "vardaglig, skämtsam",
        "syn": ["festa", "svira"],
        "ex": f"Han {h('levde i sus och dus')} under hela sin studietid.",
        "skal": "Frasen har inget eget uppslagsord — svenska.se gav 30 "
                "grannartiklar (bus, dusch, dussin …) och noll ortografiträffar, "
                "så synonymer.se är källan: sudda, festa, svira. Kortets 'få "
                "mycket' och 'ha det trevligt' betyder inte detta. Registret "
                "stod som litterärt trots att märkningen är vardagligt.",
    },
    "gamman": {
        "hb": "Glad, festlig stämning",
        "reg": "ngt ålderdomlig, positiv",
        "syn": ["fröjd", "munterhet"],
        "ex": f"I grannlägenheten var det fest och {h('gamman')}.",
        "skal": "SO 'glad stämning', SAOL 'glädje' med exemplet 'fröjd och "
                "gamman'. Registret stod som 'litterär' trots att BÅDA "
                "ordböckerna märker ordet ålderdomligt — ordet lever i praktiken "
                "bara kvar i den frasen.",
    },
    "rya": {
        "hb": "Handvävd matta med lång lugg ; skrika och väsnas högljutt",
        "reg": "neutral, neutral ; vardaglig, neutral",
        "grupper": [["flossamatta", "flossavävnad"], ["skräna", "gasta"]],
        "ex": f"Hon har knutit {h('ryan')} själv på en gammal vävstol.",
        "skal": "Kortet skrev '(dialektalt)' inuti huvudbetydelsen medan "
                "registret sa 'dialektal' — dubbelt, och dessutom fel märkning: "
                "SO och synonymer.se märker verbet vard., inte dialektalt. "
                "'Ryamatta' duger inte som synonym, den innehåller uppslagsordet.",
    },
    "sätta sig": {
        "hb": "Placera sig i sittande ställning ; sjunka ihop, om mark eller "
              "husgrund ; vara nedlåtande mot någon",
        "reg": "neutral, neutral",
        "syn": ["slå sig ner", "sjunka"],
        "ex": f"Trött efter promenaden {h('satte hon sig')} på närmaste bänk.",
        "skal": "SO har tre betydelser; kortet hade två och saknade 'vara "
                "nedlåtande' — som står ordagrant i kortets EGET OLD-facit "
                "('sjunka; vara nedlåtande'). Facit fanns alltså i sessionsfilen "
                "och lästes inte. Exemplet löd 'lät hon sig sätta sig', vilket "
                "inte går att läsa högt.",
    },
}


def main():
    poster = json.load(open(SESSION, encoding="utf-8"))
    saknar = [p["ord"] for p in poster if p["ord"] not in KORT]
    if saknar:
        sys.exit(f"saknar rättelse för: {', '.join(saknar)}")

    for p in poster:
        o = p["ord"]
        r = KORT[o]
        p["proposed"] = {
            "huvudbetydelse": r["hb"],
            "synonymer": r.get("syn", [s for g in r.get("grupper", []) for s in g]),
            "synonym_groups": r.get("grupper"),
            "exempelmening": r["ex"],
            "register": r["reg"],
            "etymologi": None,
        }
        p["approved"] = True
        p["sokkoll"] = {"kalla": SVENSKA.format(urllib.parse.quote(o)),
                        "slutsats": r["skal"]}
        p.pop("applicerad", None)

    json.dump(poster, open(SESSION, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"fyllde {len(poster)} poster.")


if __name__ == "__main__":
    main()
