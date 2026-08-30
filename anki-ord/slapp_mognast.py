# -*- coding: utf-8 -*-
"""Avsuspenderar de N mognaste suspenderade REPETITIONSKORTEN.

Adams begaran 2026-08-30: "avsuspendera de 328 is:review korten utifran
maturitet nu". 328 = deckens dagstak for repetitioner (330) minus de tva han
redan gjort.

URVALET ar begransat till kort med BLA FLAGGA (full v3). Det ar inte en
inskrankning jag hittat pa -- det ar Adams egen regel fran 2026-08-11
("jag vill att vi suspendar allt som inte ar full v3"). Att slappa
ogranskade kort for att fylla en dagskvot hade brutit mot den.

MATT INNAN KORNING (2026-08-30):
    suspenderade repetitionskort          2 270
      varav bla (full v3)                   591   <- poolen
      varav oberoende_verifierade             8   <- 0 av dem mogna
    aktiva repetitionskort i skuld        1 166

De 591 ar ett INVARIANTBROTT i sig: `v3_invariant.py` sager att ett fullt
v3-kort ska vara blaflaggat OCH avsuspenderat. De har varit v3-skrivna men
aldrig slappta. Att slappa dem lagar alltsa ett fel, det skapar inte ett.

VARNING som maste sagas hogt: att avsuspendera racker INTE for att korten
ska dyka upp idag. De gar in i en skuld pa 1 166 forfallna, och deckens
dagstak ar 330. Vilka av dem Adam faktiskt far se styrs av deckens
`reviewOrder`, som star pa 10 och som jag inte har verifierat innebörden av.
Ska mognast komma forst maste den sattas till "Descending intervals" i
Deck options -> Display Order -> Review sort order.
"""
import argparse
import json

import config
from ankiconnect import invoke


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--antal", type=int, default=328)
    p.add_argument("--kor", action="store_true",
                   help="utan denna flagga gors bara en torrkorning")
    a = p.parse_args()

    fraga = ('deck:"%s" is:review is:suspended flag:4' % config.DECK_NAME)
    ids = invoke("findCards", query=fraga)
    print("pool (bla + suspenderade + is:review): %d" % len(ids))
    if not ids:
        return

    info = invoke("cardsInfo", cards=ids)

    # De sex kort blindgranskaren underkande i dag halls UTE. De ar
    # v3-skrivna och blaflaggade, sa de kommer med i poolen -- men jag har
    # redan fatt veta att de ar fel (betydelser saknas). Att slappa ett kort
    # man vet ar felaktigt for att fylla en dagskvot ar samre an att lata
    # platsen sta tom.
    underkanda = invoke("findNotes",
                        query='deck:"%s" (adjutant OR atrofi OR banal OR '
                              'fysisk OR "förankra" OR geografi) '
                              'tag:v3_granskad::2026-08-30' % config.DECK_NAME)
    fore = len(info)
    info = [c for c in info if c["note"] not in set(underkanda)]
    print("uteslutna (blindunderkanda i dag): %d" % (fore - len(info)))

    info.sort(key=lambda c: -c["interval"])
    valda = info[:a.antal]
    ivl = [c["interval"] for c in valda]
    print("valda: %d   intervall %d .. %d dagar" % (len(valda), max(ivl), min(ivl)))
    band = [("ivl>=90", 90, 10 ** 6), ("21-89", 21, 90),
            ("14-20", 14, 21), ("<14", 0, 14)]
    for lab, lo, hi in band:
        print("   %-8s %4d" % (lab, sum(1 for i in ivl if lo <= i < hi)))

    idag = sum(1 for c in valda
               if c["note"] in _dagens())
    print("varav ur dagens 100-kortsomgang: %d" % idag)

    if not a.kor:
        print("\n(torrkorning -- kor med --kor for att avsuspendera)")
        return

    invoke("unsuspend", cards=[c["cardId"] for c in valda])
    kvar = invoke("findCards", query=fraga)
    print("\navsuspenderade : %d" % len(valda))
    print("kvar i poolen  : %d" % len(kvar))
    for lab, f in [("due review aktiva", "is:due is:review -is:suspended"),
                   ("aktiva review totalt", "is:review -is:suspended")]:
        n = len(invoke("findCards",
                       query='deck:"%s" %s' % (config.DECK_NAME, f)))
        print("%-22s %5d" % (lab, n))


def _dagens():
    import io
    import os
    sv = os.path.join("sessions",
                      "session_2026-08-30_v3-omgranskning-repetition-mognad.json")
    if not os.path.exists(sv):
        return set()
    d = json.load(io.open(sv, encoding="utf-8"))
    return {p["noteId"] for p in d if p.get("approved")}


main()
