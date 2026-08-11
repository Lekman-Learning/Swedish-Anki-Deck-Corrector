"""Kortbyggare v3.0 -- bygger dagsbatchen som ska skrivas om till v2.

Ersätter snabbkoll2_blanya_v2.py för det dagliga flödet från 2026-08-08:
125 kort/dag ur den suspenderade legacy-poolen (6 805 kort vid start,
~54 dagar). snabbkoll2_blanya_v2.py finns kvar för engångskörningar.

Vad den här filen gör: samlar ALLT granskaren behöver för ett kort på
ett ställe, så att inget steg kan glömmas bort mitt i en batch om 125.
Den skriver aldrig till Anki.

Per kort i sessionsfilen:
  legacy        -- nuvarande innehåll (parse_legacy)
  old_facit     -- uppslag i Svenska OLD-decket, projektets andra källa
  riskflaggor   -- mekaniska signaler, se riskflaggor.py
  adamtal_krav  -- de hårda reglerna kortet MÅSTE klara för att skrivas
  sokkoll       -- tomt fält som granskaren fyller med källa + slutsats
  proposed      -- tomt fält för det omskrivna kortet

Ordningen i kön är inte godtycklig: kort med `hog`-riskflagga läggs
FÖRST. Vid 125 kort/dag är uppmärksamheten som skarpast i början, och
"saknad hel betydelse" -- det dominerande felmönstret i åtta omgångar i
rad -- är exakt det som kräver skärpa.

Körning:
    python kortbyggare.py                    # 125 kort (config.DAGSBATCH_STORLEK)
    python kortbyggare.py --antal 25         # mindre sats
    python kortbyggare.py --dump             # skriv även en läsbar .txt
    python kortbyggare.py --spar omgranskning --ko nya --antal 50
"""

import argparse
import datetime
import json
import os
import re

import baksida
import config
import riskflaggor
from ankiconnect import invoke
from queue_lib import fetch_cards_sorted_by_due
from snabbkoll2 import build_old_lookup

ALLVAR_ORDNING = {"hog": 0, "medel": 1, "lag": 2, None: 3}

_ADAMTAL = (
    "Skriv i Adam-tal: vardagliga ord, kort nog att läsas högt och förstås direkt, "
    "aldrig ordboksprosa, aldrig ordet i sin egen definition, förklara inte svårt "
    "med svårt, konkret före abstrakt, bevara humor. EN exempelmening med ordet i "
    "blått. Bara utbytbara synonymer, aldrig cirkulära. Skilda betydelser separeras "
    "med ' ; ' och synonymerna grupperas i samma ordning. ETYMOLOGI (valfri, från "
    "2026-08-08): lägg till 'etymologi' i proposed BARA när ursprunget gör betydelsen "
    "lättare att förstå eller minnas -- t.ex. när ordet blir självförklarande av det "
    "('rangera' av ty. rangieren, 'ordna i rad'). Aldrig som språkhistorisk trivia, "
    "aldrig bara för att ursprunget är känt. Max ~18 ord, ren text, hellre utelämnad "
    "än utfyllnad. De flesta kort ska INTE ha någon."
)

GRANSKARINSTRUKTION = {
    "nya": (
        "V3 SPÅR A (nytt kort, suspenderat) -- ETT KORT ÄR INTE KLART FÖRRÄN ALLA "
        "FYRA STEGEN ÄR GJORDA: (1) Jämför mot old_facit. (2) Gör en RIKTIG sökkoll "
        "och skriv källa + slutsats i fältet 'sokkoll' -- tomt fält = kortet skrivs "
        f"inte. (3) {_ADAMTAL} (4) Läs riskflaggorna -- 'hog' betyder att kortet "
        "statistiskt sannolikt saknar en HEL betydelse, det vanligaste felet i decket."
    ),
    "omgranskning": (
        "V3 SPÅR B (kort som REDAN ligger i Adams kö och som han pluggar just nu). "
        "Det här kortet skrevs under den gamla processen och har aldrig blindverifierats. "
        "Ett fel här gör skada varje dag, till skillnad från de suspenderade korten. "
        "(1) Jämför mot old_facit. (2) RIKTIG sökkoll, fyll i 'sokkoll'. "
        "(3) Bedöm om kortet behöver ändras -- är det redan korrekt och i Adam-tal, "
        "kopiera nuvarande innehåll oförändrat till 'proposed' och notera det i "
        f"sokkoll-slutsatsen. Om det behöver ändras: {_ADAMTAL} "
        "(4) BEVARA bild_html oförändrat om kortet har en bild. "
        "(5) Riskflaggan 'hog' betyder sannolikt saknad betydelse -- det felet fanns "
        "på 34 kort i just den här poolen så sent som 2026-08-07."
    ),
}

POOL_FRAGA = {
    # Spår A: suspenderade legacy-kort som ska skrivas om och släppas in.
    "nya": (
        f'deck:"{config.DECK_NAME}" is:suspended -tag:{config.FORMAT_TAG_V2} '
        f'-tag:{config.DAGSBATCH_TAG_PREFIX}::*'
    ),
    # Spår B: v2-kort som skrivits under den gamla processen och aldrig
    # blindverifierats.
    #
    # `-is:suspended` STOD HÄR till 2026-08-11 och byggde på att spår B:s kort
    # per definition låg i Adams aktiva kö. Det upphörde att gälla samma dag:
    # när allt som inte är full v3 suspenderades blev villkoret sant för noll
    # kort, och poolen tömdes tyst. `test_prio_urval.py` fångade det
    # ("omgranskning hämtade 0 kort") -- utan testet hade dagsbatchen bara
    # blivit tom utan att någon förstod varför.
    #
    # Suspenderat är numera normaltillståndet för ett ogranskat kort, inte ett
    # undantag. Det som ska hållas UTE ur poolen är i stället kort som pausats
    # för att de inte går att sökkolla (se v3_pausa.py) -- de kostar arbete
    # varje gång de plockas och blir aldrig klara.
    # `-tag:v3_dagsbatch::*` STOD HÄR till 2026-08-11 och exkluderade varje kort
    # som NÅGONSIN varit i en batch. Taggen finns för att slippa dra samma kort
    # två gånger samma dag -- men eftersom den aldrig tas bort behandlades
    # "påbörjad" som "klar". Mätt när felet hittades: 460 kort hade varit i en
    # batch, **97 av dem blev aldrig verifierade** (78 underkända plus
    # avhoppade), och ingen av dem kunde plockas igen. Ett underkänt kort är
    # per definition trasigt och ska tillbaka i kön FÖRST, inte försvinna ur
    # den.
    #
    # Rätt villkor är alltså "redan klar" (oberoende_verifierad), plus dagens
    # egen batch så att en pågående omgång inte dubbelhämtas.
    "omgranskning": (
        f'deck:"{config.DECK_NAME}" tag:{config.FORMAT_TAG_V2} '
        f'-tag:{config.OBEROENDE_TAG_PREFIX}::* '
        f'-tag:{config.DAGSBATCH_TAG_PREFIX}::{datetime.date.today().isoformat()} '
        f'-tag:v3_pausad::*'
    ),
}


# Kösegment. Due-sortering ensam räcker inte: repetitionskort har ett
# schemalagt datum som due, nya kort har en köposition, och de talen ligger
# i helt olika intervall. I praktiken sorterar repetitionskorten alltid
# först, vilket 2026-08-09 gav en batch på 20 kort där ALLA var repetition
# och noll var nya -- trots att det var de nya korten som skulle skyddas.
# Filtret måste därför läggas på FÖRE sorteringen, inte efter.
KO_FILTER = {
    "nya": " is:new",
    "repetition": " -is:new",
    "bada": "",
}


def hamta_pool(antal, spar, ko="bada"):
    """Prio-märkta kort först, därefter due-ordning (= Adams egen ordning).

    Förturen måste ligga i URVALET, inte bara i sorteringen av det som
    råkade hämtas: med 3 000+ kort i spår B hade ett prio-kort längre bak i
    due-ordningen aldrig kommit med i dagens 25, hur högt det än var märkt.

    `ko` läggs på BASFRÅGAN, inte bara på restposten -- annars hade
    prio-hämtningen dragit in repetitionskort även vid `--ko nya` och ätit
    upp platserna innan de nya korten ens övervägdes.
    """
    bas = POOL_FRAGA[spar] + KO_FILTER[ko]
    prio = fetch_cards_sorted_by_due(f"{bas} tag:{config.PRIO_TAG_HOG}", antal)
    kvar = antal - len(prio)
    if kvar <= 0:
        return prio
    return prio + fetch_cards_sorted_by_due(f"{bas} -tag:{config.PRIO_TAG_HOG}", kvar)


def hamta_ids(kort_ids):
    """Hämtar exakt de angivna korten, i angiven ordning.

    Finns för att prio-taggen bara kan uttrycka "viktig", inte "hur viktig":
    hamta_pool() sorterar prio-korten inbördes på `due`, så en rankad lista
    (v3_urgency.py) skulle tappa sin ordning och -- när fler kort är
    prio-märkta än batchen rymmer -- tappa poster ur toppen godtyckligt.

    Kastar om något ID saknas i stället för att tyst leverera en kortare
    batch: en batch som tyst krymper ser ut som en klar batch.
    """
    cards = invoke("cardsInfo", cards=list(kort_ids))
    hittade = {c["cardId"]: c for c in cards if c.get("cardId")}
    saknas = [i for i in kort_ids if i not in hittade]
    if saknas:
        raise SystemExit(f"AVBRYTER: {len(saknas)} kort-ID saknas i Anki: {saknas[:5]}")
    return [hittade[i] for i in kort_ids]


def bygg_post(card, old_lookup, spar, prio_nids=frozenset()):
    falt = {n: v["value"] for n, v in card["fields"].items()}
    ord_ = falt.get(config.FIELD_ORD, "")
    raw = falt.get(config.FIELD_BAKSIDA, "")

    parsed = baksida.parse(raw)
    ar_v2 = bool(parsed["huvudbetydelse"])
    # Nyckeln heter "legacy" i båda spåren: den håller kortets NUVARANDE
    # innehåll före omskrivning, oavsett om det är gammalt <ol><li>-format
    # (spår A) eller redan v2 (spår B). kortgranskare läser samma nyckel.
    legacy = parsed if ar_v2 else baksida.parse_legacy(raw)
    old = old_lookup.get(ord_.strip().lower())
    flaggor = riskflaggor.berakna(ord_, legacy, old)

    return {
        "noteId": card["note"],
        "ord": ord_,
        "spar": spar,
        "prio": card["note"] in prio_nids,
        "redan_i_kon": spar == "omgranskning",
        "nuvarande_format": "v2" if ar_v2 else "legacy",
        "legacy": legacy,
        "old_facit": old,
        "har_old_facit": bool(old),
        "riskflaggor": [
            {"flagga": f, "allvar": a, "forklaring": t} for f, a, t in flaggor
        ],
        "hogsta_allvar": riskflaggor.hogsta_allvar(flaggor),
        "adamtal_krav": list(baksida.ADAMTAL_HARDA),
        # --- fylls av granskaren ---
        "sokkoll": None,          # {"kalla": "...", "slutsats": "..."} -- OBLIGATORISKT
        "proposed": None,         # {"huvudbetydelse","register","synonymer","synonym_groups","exempelmening","etymologi"?}
        "approved": False,
        "note_till_granskare": GRANSKARINSTRUKTION[spar],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--spar", choices=["nya", "omgranskning"], default="nya",
                   help="nya = suspenderade legacy-kort (125/dag). "
                        "omgranskning = v2-kort som redan ligger i Adams kö (25/dag).")
    p.add_argument("--antal", type=int, default=None,
                   help="default: 125 för 'nya', 25 för 'omgranskning'")
    p.add_argument("--ko", choices=["nya", "repetition", "bada"], default="bada",
                   help="kösegment INOM spåret. 'nya' = kort Adam introduceras "
                        "för (is:new), 'repetition' = kort han redan sett. "
                        "Utan detta sorterar repetitionskorten alltid först och "
                        "de nya korten kommer aldrig med.")
    p.add_argument("--dump", action="store_true", help="skriv även en läsbar .txt")
    p.add_argument("--ids-fil", metavar="FIL",
                   help="JSON-lista från v3_urgency.py: ta exakt dessa kort, i "
                        "listans ordning, i stället för poolurvalet.")
    p.add_argument("--antal-ur-fil", type=int, metavar="N",
                   help="med --ids-fil: ta bara de N översta.")
    args = p.parse_args()

    antal = args.antal if args.antal is not None else (
        config.DAGSBATCH_STORLEK if args.spar == "nya" else config.OMGRANSKNING_STORLEK)

    if args.spar == "nya" and args.ko != "bada":
        # Spår A är per definition suspenderat och därmed varken nytt eller
        # förfallet i Ankis mening -- filtret skulle tysta bort hela poolen.
        p.error("--ko gäller bara --spar omgranskning (spår A är suspenderat)")

    if args.ids_fil:
        with open(args.ids_fil, encoding="utf-8") as f:
            rankade = json.load(f)
        if args.antal_ur_fil:
            rankade = rankade[:args.antal_ur_fil]
        # Pausade kort måste filtreras HÄR också. --ids-fil går förbi
        # POOL_FRAGA, så `-tag:v3_pausad::*` i pool-frågan skyddar den inte:
        # 2026-08-11 kom `ytong` med i en 50-kortsbatch trots att det pausats
        # samma dag, och kostade en sökkoll som redan var känd som omöjlig.
        pausade = set(invoke("findCards",
                             query=f'deck:"{config.DECK_NAME}" tag:v3_pausad::*'))
        fore = len(rankade)
        rankade = [r for r in rankade if r["cardId"] not in pausade]
        if len(rankade) < fore:
            print(f"Hoppade {fore - len(rankade)} pausade kort (v3_pausad).")
        cards = hamta_ids([r["cardId"] for r in rankade])
        print(f"Läste {len(cards)} kort ur {args.ids_fil} "
              f"(poäng {rankade[0]['poang']} ned till {rankade[-1]['poang']}).")
    else:
        cards = hamta_pool(antal, args.spar, args.ko)
    if not cards:
        print(f"Poolen för spår '{args.spar}' (kö: {args.ko}) är tom.")
        return

    old_lookup = build_old_lookup()
    prio_nids = frozenset(invoke("findNotes",
                                 query=f'deck:"{config.DECK_NAME}" tag:{config.PRIO_TAG_HOG}'))
    poster = [bygg_post(c, old_lookup, args.spar, prio_nids) for c in cards]
    # Prio före risk: ett prio-märkt kort är märkt för att NÅGON vet något om
    # det som riskflaggorna inte kan se (t.ex. "detta kort skrevs om utan
    # sökkoll"). Riskprioriterat, inte slumpmässigt, i övrigt: syftet är att
    # LAGA fel så fort som möjligt. Det gör urvalet snedvridet -- räkna aldrig
    # felfrekvens på det, den blir för hög. Mätningen kommer från
    # blint_stickprov.py, som drar slumpmässigt just därför.
    # Med --ids-fil ÄR ordningen resultatet (urgency-rankningen). Att sortera
    # om den här hade tyst kastat bort hela poängen med att skicka in en lista.
    if not args.ids_fil:
        poster.sort(key=lambda e: (not e["prio"], ALLVAR_ORDNING[e["hogsta_allvar"]], e["ord"]))

    idag = datetime.date.today().isoformat()
    katalog = os.path.join(os.path.dirname(__file__), "sessions")
    os.makedirs(katalog, exist_ok=True)
    stam = "v3-batch" if args.spar == "nya" else "v3-omgranskning"
    if args.ko != "bada":
        stam += f"-{args.ko}"
    sokvag = os.path.join(katalog, f"session_{idag}_{stam}.json")
    n = 2
    while os.path.exists(sokvag):
        sokvag = os.path.join(katalog, f"session_{idag}_{stam}{n}.json")
        n += 1
    with open(sokvag, "w", encoding="utf-8") as f:
        json.dump(poster, f, ensure_ascii=False, indent=2)

    # Markera korten som uttagna så nästa körning inte tar samma igen.
    # ETT anrop för hela batchen, inte 125 stycken: ett avbrott mitt i en
    # kort-för-kort-loop hade lämnat halva batchen otaggad, och nästa
    # körning hade då plockat upp samma kort igen och dubblerat arbetet.
    invoke("addTags", notes=[e["noteId"] for e in poster],
           tags=f"{config.DAGSBATCH_TAG_PREFIX}::{idag}")

    if args.dump:
        rader = []
        for i, e in enumerate(poster):
            defs = e["legacy"].get("definitioner") or [e["legacy"].get("huvudbetydelse", "")]
            rensa = lambda s: re.sub(r"<[^>]+>", "", s or "").strip()
            rader.append(
                f"[{i}] {e['ord']}  <{e['hogsta_allvar'] or 'ren'}>\n"
                f"     NU  : {' | '.join(rensa(d) for d in defs)}\n"
                f"     SYN : {e['legacy'].get('synonymer')}\n"
                f"     OLD : {rensa(e['old_facit'])[:110]}\n"
                f"     RISK: {riskflaggor.sammanfatta([(r['flagga'], r['allvar'], '') for r in e['riskflaggor']])}"
            )
        with open(f"{os.path.splitext(sokvag)[0]}_dump.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(rader))

    antal_hog = sum(1 for e in poster if e["hogsta_allvar"] == "hog")
    antal_prio = sum(1 for e in poster if e["prio"])
    utan_old = sum(1 for e in poster if not e["har_old_facit"])
    bas_kvar = POOL_FRAGA[args.spar] + KO_FILTER[args.ko]
    kvar = len(invoke("findNotes", query=bas_kvar))
    prio_kvar = len(invoke("findNotes",
                           query=f"{bas_kvar} tag:{config.PRIO_TAG_HOG}"))
    print(f"Skrev {len(poster)} kort ({args.spar}, kö: {args.ko}) till {sokvag}")
    print(f"  prio (ligger först)        : {antal_prio}   (kvar i poolen: {prio_kvar})")
    print(f"  hög risk (läs dessa först) : {antal_hog}")
    print(f"  utan OLD-facit             : {utan_old}")
    print(f"  kvar i poolen efter denna  : {kvar}")
    if args.spar == "omgranskning":
        print("  OBS: dessa kort ligger REDAN i Adams kö -- de pluggas medan de granskas.")


if __name__ == "__main__":
    main()
