"""
betydelseordning.py -- letar kort dar HUVUDBETYDELSEN sannolikt ar fel vald.

Bakgrund. Adam hittade 2026-09-06 tva kort som var fullt v3-granskade och anda
ledde med fel betydelse:

    tråckla   bet.1 "Sy provisoriskt med långa stygn", men exempelmeningen var
              "Han tråcklade sig fram genom folkmassan" -- alltsa bet.4.
    fortuna   bet.1 tivolispelet, bet.2 "lycka eller öde". Etymologin sager
              "namn på lycko- och ödesgudinna" och beskriver alltsa bet.2.
              En avledd, daterad specialbetydelse stod fore originalet.

Regeln som foll ut: ORD ar ett LASPROV. Huvudbetydelsen ska vara den betydelse
ordet bar i SKRIFT -- inte ordbokens ordning, och inte en konkret
specialbetydelse som hunnit bli mer kand i tal.

Skriptet implementerar samma tva indicier som forgranska.py regel 7, men mot
decket i stallet for mot en byggsession:

    A. etymologin beskriver en SENARE betydelse battre an den forsta
    B. exempelmeningen demonstrerar en SENARE betydelse

🔴 Bada ar INDICIER. Skriptet domer inte -- det pekar ut kort for granskning.
   Kor med --tagga for att markera dem, aldrig for att andra dem automatiskt.

🔴 RATTAT 2026-09-06, samma dag. En flagga far ALDRIG resolveras med ett
   resonemang -- den kraver `slaupp.py <ord>` och en last SO/SAOL-artikel.

   Beviset ar fortuna sjalvt, kortet som gav upphov till indicium A. Jag
   flyttade "lycka eller ode" till forstaplats med argumentet att etymologin
   ("till latin Fortu'na, namn pa lycko- och odesgudinna") beskrev den
   betydelsen. Uppslagningen samma dag visade:

       SAOL: "ett spel med kulor..."          -- ENDA betydelsen
       SO  : "ett spel med en metallkula..."  -- ENDA betydelsen, jfr flipperspel

   Etymologin i SO forklarar var ORDET kommer ifran. Den ar inte en
   betydelsedefinition. Indicium A pekar alltsa pa en FRAGA, inte pa ett svar
   -- och den som resolverar fragan utan att sla upp ordet gor exakt det
   felslut som indiciet finns for att fanga.

   Kortet beholl lycka forst, men pa ett annat skal: Adam moter aldrig spelet
   i en text. SO:s ordning och lasexponeringen pekar at olika hall har, och
   det finns inget facit som avgor -- darfor bar kortet bada, med SO:s egen
   jfr-hanvisning (flipperspel) som synonym sa spelbetydelsen anda ar
   igenkannbar.

    python betydelseordning.py                # rapport
    python betydelseordning.py --tagga        # satt betydelseordning_granska
    python betydelseordning.py --alla         # aven suspenderade
"""

import argparse
import html
import json
import re
import sys
import urllib.request

DECK = '"deck:Humanities::Languages::Svenska 10 000"'
BLOCK = re.compile(r"<\s*(br|/?div|/?p|/?li)[^>]*>", re.I)
INLINE = re.compile(r"<[^>]+>")

_ETY_STOPP = {
    "till", "av", "med", "samma", "betydelse", "betydelsen", "ovisst", "ursprung",
    "latin", "latinska", "grekiska", "tyska", "lagtyska", "lågtyska", "franska",
    "engelska", "fornsvenska", "fornnordiska", "nederländska", "italienska",
    "ord", "ordet", "eller", "och", "som", "det", "den", "ett", "besläktat",
    "bildning", "egentligen", "urspr", "ursprungligen", "avledning",
    "sannolikt", "trolig", "troligen", "efter", "genom", "sedan", "även",
}

# Fras-betydelser: "Tråckla sig: ..." -- kollokationen som exemplet kan avsloja.
_FRAS = re.compile(r"([A-Za-zÅÄÖåäö]+)\s+"
                   r"((?:sig|om|av|på|till|ut|upp|ihop|fram|undan|bort|efter|ur|i)"
                   r"(?:\s+\w+)?)\s*:")


def anki(action, **params):
    data = json.dumps({"action": action, "version": 6, "params": params}).encode()
    svar = json.loads(urllib.request.urlopen(
        urllib.request.Request("http://127.0.0.1:8765", data), timeout=300).read())
    if svar.get("error"):
        sys.exit("AnkiConnect: %s" % svar["error"])
    return svar.get("result")


def text(h):
    return html.unescape(INLINE.sub("", BLOCK.sub("\n", h or "")))


def stam(w):
    for a in ("andet", "ingen", "arna", "erna", "orna", "ande", "else", "het",
              "ning", "are", "ade", "ar", "en", "et", "or", "an", "a", "e"):
        if len(w) > len(a) + 3 and w.endswith(a):
            return w[:-len(a)]
    return w


def innehallsord(s):
    return {stam(w)[:5] for w in re.findall(r"[a-zåäöéèü]{4,}", (s or "").lower())
            if w not in _ETY_STOPP}


def dela(bak):
    """Plockar ut betydelser, exempelmening och etymologi ur baksidans text."""
    rader = [r.strip() for r in bak.split("\n") if r.strip()]
    numrerade = [(int(m.group(1)), m.group(2).strip())
                 for r in rader for m in [re.match(r"^(\d)\.\s*(.+)$", r)] if m]
    if numrerade:
        bet = [t for _, t in sorted(numrerade)]
    else:
        # Oumrerat format: betydelserna star pa forsta raden, separerade med " ; ".
        forsta = rader[0] if rader else ""
        bet = [x.strip() for x in re.split(r"\s;\s", forsta) if x.strip()]
    ety = next((r for r in rader if r.startswith("→")), "")
    # Pa onumrerade kort ar rad 1 sjalva betydelseraden. Den maste uteslutas
    # explicit: bara dess DELAR ligger i `bet`, sa `r not in bet` slapper
    # igenom hela raden och den blir felaktigt tagen for exempelmening.
    forbjudna = set(bet) | ({rader[0]} if rader and not numrerade else set())
    ex = next((r for r in rader
               if len(r) > 25 and not re.match(r"^\d\.", r) and "≈" not in r
               and not r.startswith("→") and not r.startswith("(")
               and r not in forbjudna), "")
    return bet, ex, ety


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tagga", action="store_true")
    ap.add_argument("--alla", action="store_true",
                    help="ta med suspenderade kort (default: bara levande)")
    a = ap.parse_args()

    q = DECK if a.alla else DECK + " -is:suspended"
    noter = anki("notesInfo", notes=anki("findNotes", query=q))
    print("Granskar %d kort...\n" % len(noter), file=sys.stderr)

    ety_flagg, ex_flagg = [], []
    flerbet = 0
    for n in noter:
        ordet = text(n["fields"]["Framsida"]["value"]).strip()
        bak = text(n["fields"].get("Baksida", {}).get("value", ""))
        bet, ex, ety = dela(bak)
        if len(bet) < 2:
            continue
        flerbet += 1

        karna = innehallsord(ety)
        if karna:
            tack = [len(karna & innehallsord(b)) for b in bet]
            if tack[0] == 0 and max(tack[1:]) >= 2:
                i = tack.index(max(tack[1:]))
                ety_flagg.append((n["noteId"], ordet, i + 1, bet[0][:40],
                                  bet[i][:40], ety[:52]))

        exl = ex.lower()
        if exl:
            for i, b in enumerate(bet):
                if i == 0:
                    continue
                m = _FRAS.match(b.strip())
                if not m:
                    continue
                rot = m.group(1).lower()[:max(4, len(m.group(1)) - 2)]
                if rot in exl and all(d in exl for d in m.group(2).lower().split()):
                    ex_flagg.append((n["noteId"], ordet, i + 1,
                                     bet[0][:40], b[:40], ex[:52]))
                    break

    print("# Betydelseordning — granskning\n")
    print("| | Antal |")
    print("|---|---|")
    print("| Kort granskade | %d |" % len(noter))
    print("| Med flera betydelser | %d |" % flerbet)
    print("| 🔴 Etymologin pekar på en senare betydelse | **%d** |" % len(ety_flagg))
    print("| 🔴 Exemplet visar en senare betydelse | **%d** |" % len(ex_flagg))

    if ety_flagg:
        print("\n## A. Etymologin beskriver en senare betydelse\n")
        print("| Ord | Bet.1 | Etymologin pekar på | Etymologi |")
        print("|---|---|---|---|")
        for _, o, i, b1, bi, e in ety_flagg:
            print("| **%s** | %s | **%d.** %s | %s |" % (o, b1, i, bi, e))

    if ex_flagg:
        print("\n## B. Exempelmeningen visar en senare betydelse\n")
        print("| Ord | Bet.1 | Exemplet visar | Exempel |")
        print("|---|---|---|---|")
        for _, o, i, b1, bi, e in ex_flagg:
            print("| **%s** | %s | **%d.** %s | %s |" % (o, b1, i, bi, e))

    if not ety_flagg and not ex_flagg:
        print("\n🟢 Inga kort flaggade.")

    print("\n⚠️ **Bägge kontrollerna är indicier.** En etymologi som beskriver "
          "betydelse 2 kan vara helt korrekt om betydelse 1 är den gängse i "
          "dag — *preludium*, *kartell* och *traktat* leder rätt trots samma "
          "form. Läs kortet innan du ändrar.")

    if a.tagga:
        ids = list({x[0] for x in ety_flagg + ex_flagg})
        for i in range(0, len(ids), 400):
            anki("addTags", notes=ids[i:i + 400], tags="betydelseordning_granska")
        print("\nTaggade %d kort med betydelseordning_granska" % len(ids),
              file=sys.stderr)


if __name__ == "__main__":
    main()
