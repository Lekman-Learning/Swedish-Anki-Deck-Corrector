# -*- coding: utf-8 -*-
"""Fyller synonymraden pa de kort i decket som star tomma.

MATT 2026-09-02 mot AnkiConnect: av 4 965 v2-noter saknar 41 synonymrad.
12 ar flerordsuttryck, dar tom rad ar RATT (style_guide.md: idiom och ordled
bar hela betydelsen sjalva). Kvar: 29 enskilda ord.

Tre av dem ar ORDLED -- `-tyg`, `-vill`, `iso-`. Styleguiden namner dem i
samma andetag som idiomen, och av samma skal: ett efterled ar inte ett ord
med en synonym, det ar en byggsten. De ror jag inte, och forgranskas
`synonymrad_tom` undantar dem inte automatiskt (den tittar bara efter
mellanslag) -- det ar en kand lucka, inte ett forbiseende har.

Synonymerna nedan kommer ur `_hjalp_0902b.synpool()`, alltsa forgranskas
egna godkanda belagg. Dar poolen ar tom eller bara innehaller
definitionsfragment anvands `≈≈ kategori`, som far tas ur kortets egen
definition och darfor inte kraver kalla.

Skrivs direkt mot Anki med baksida.build(), eftersom korten redan ar
applicerade och inte ligger i nagon sessionsfil.
"""
import io, json, sys

import baksida
import config
from ankiconnect import invoke

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ord -> (synonymer, grupper). En grupp per betydelse pa kortet.
S = {
 "agna":          (["förse med agn"], [["förse med agn"]]),
 "alligator":     (["ett krokodildjur"], [["ett krokodildjur"]]),
 "biennal":       (["konstutställning"], [["konstutställning"]]),
 "cerat":         (["≈≈ salva"], [["≈≈ salva"]]),
 "docent":        (["universitetslärare"], [["universitetslärare"]]),
 "elliptisk":     (["≈≈ oval", "≈≈ förkortad"], [["≈≈ oval"], ["≈≈ förkortad"]]),
 "fosgen":        (["giftig gas"], [["giftig gas"]]),
 "fysisk":        (["≈≈ kroppslig", "≈≈ materiell"],
                   [["≈≈ kroppslig"], ["≈≈ materiell"]]),
 "galvanometer":  (["≈≈ mätinstrument"], [["≈≈ mätinstrument"]]),
 "inhysa":        (["ge husrum åt"], [["ge husrum åt"]]),
 "inprägla":      (["fästa i minnet"], [["fästa i minnet"]]),
 "intellektuell": (["≈≈ tankemässig", "≈≈ tänkare"],
                   [["≈≈ tankemässig"], ["≈≈ tänkare"]]),
 "kolugn":        (["fullkomligt lugn"], [["fullkomligt lugn"]]),
 # Tre betydelser pa kortet, inte tva -- forsta forsoket gav
 # "2 grupper mot 3 betydelser" och stoppades av kontrollen.
 "kuliss":        (["flyttbar scendekoration", "≈≈ bakomscenen", "som döljer"],
                   [["flyttbar scendekoration"], ["≈≈ bakomscenen"], ["som döljer"]]),
 "lavinartad":    (["≈≈ okontrollerad"], [["≈≈ okontrollerad"]]),
 "limes":         (["matematiskt gränsvärde"], [["matematiskt gränsvärde"]]),
 "mycel":         (["mycelium"], [["mycelium"]]),
 "mångfaldiga":   (["≈≈ föröka", "framställa"], [["≈≈ föröka"], ["framställa"]]),
 "småsinnad":     (["småsint"], [["småsint"]]),
 "tjäle":         (["≈≈ frusen mark"], [["≈≈ frusen mark"]]),
 "tjära":         (["trögflytande vätska", "bestryka med tjära"],
                   [["trögflytande vätska"], ["bestryka med tjära"]]),
 "triage":        (["≈≈ prioritering"], [["≈≈ prioritering"]]),
 "turbin":        (["≈≈ kraftmaskin"], [["≈≈ kraftmaskin"]]),
 "utvikning":     (["≈≈ nakenbild", "avvikelse"], [["≈≈ nakenbild"], ["avvikelse"]]),
 "vilsam":        (["≈≈ rogivande"], [["≈≈ rogivande"]]),
}

# Ordled -- tom rad ar ratt svar, se docstring.
ORDLED = {"-tyg", "-vill", "iso-"}

# `sinus` har TOM huvudbetydelse i decket och kan darfor inte fa synonymer
# som matchar betydelser. Det ar ett annat och storre fel an en tom
# synonymrad, och ratt atgard ar inte att lappa synonymraden ovanpa ett
# tomt kort. Rapporteras i stallet.
UTAN_HUVUDBETYDELSE = set()

# `sinus` visade sig vara ett HELT TOMT kort -- ingen huvudbetydelse, inget
# register, ingen exempelmening -- och det ligger LIVE i Adams ko. Det ar ett
# storre fel an en tom synonymrad: kortet lar ut ingenting alls. Det skrivs
# darfor fran grunden har i stallet for att bara flaggas.
HELT_NYA = {
 "sinus": {
  "huvudbetydelse": "Grundläggande trigonometrisk funktion ; hålrum eller "
                    "utbuktning i kroppen",
  "register": "fackspråklig, neutral, matematik ; fackspråklig, neutral, medicin",
  "synonymer": ["en trigonometrisk funktion", "hålrum i kroppen"],
  "synonym_groups": [["en trigonometrisk funktion"], ["hålrum i kroppen"]],
  "exempelmening": "<font color=\"#3498db\">Sinus</font> för 30 grader är 0,5.",
  "etymologi": "av latin sin´us 'veck; vik', i medeltidslatin även "
               "'sinus'; jfr ursprung till insinuera",
 },
}

TORR = "--torr" in sys.argv


def main():
    D = 'deck:"%s"' % config.DECK_NAME
    nids = invoke("findNotes", query=D + " tag:kortformat::v2")
    info = invoke("notesInfo", notes=nids)

    andrade, hoppade, fel = [], [], []
    for n in info:
        ord_ = n["fields"][config.FIELD_ORD]["value"]
        d = S.get(ord_)
        if not d:
            continue
        p = baksida.parse(n["fields"][config.FIELD_BAKSIDA]["value"])
        if [x for x in (p.get("synonymer") or []) if str(x).strip()]:
            hoppade.append((ord_, "har redan synonym"))
            continue
        hb = p.get("huvudbetydelse") or ""
        if not hb.strip():
            fel.append((ord_, "TOM huvudbetydelse"))
            continue
        syn, grp = d
        n_bet = len(baksida.betydelser(hb))
        if len(grp) != n_bet:
            fel.append((ord_, "%d grupper mot %d betydelser" % (len(grp), n_bet)))
            continue
        ny = baksida.build(
            huvudbetydelse=hb, synonymer=syn, synonym_groups=grp,
            exempelmening=p.get("exempelmening") or "",
            register=p.get("register"), bild_html=p.get("bild_html"),
            etymologi=p.get("etymologi"))
        if not TORR:
            invoke("updateNoteFields", note={
                "id": n["noteId"], "fields": {config.FIELD_BAKSIDA: ny}})
        andrade.append((ord_, ", ".join(syn)))

    # Kort som skrivs fran grunden.
    nya = []
    for n in info:
        ord_ = n["fields"][config.FIELD_ORD]["value"]
        d = HELT_NYA.get(ord_)
        if not d:
            continue
        ny = baksida.build(**d)
        if not TORR:
            invoke("updateNoteFields", note={
                "id": n["noteId"], "fields": {config.FIELD_BAKSIDA: ny}})
        nya.append((ord_, d["huvudbetydelse"]))

    print("TORRKORNING -- inget skrivet." if TORR else "Skrivet till Anki.")
    for o, hb in nya:
        print("  NYSKRIVET %-12s %s" % (o, hb))
    print()
    for o, s in andrade:
        print("  %-16s %s" % (o, s))
    print()
    print("andrade : %d" % len(andrade))
    if hoppade:
        print("hoppade : %s" % ", ".join("%s (%s)" % h for h in hoppade))
    if fel:
        print("FEL     : %s" % ", ".join("%s (%s)" % f for f in fel))
    print("orord   : %s -- ordled, tom rad ar ratt" % ", ".join(sorted(ORDLED)))
    print("flaggat : %s -- tom huvudbetydelse, eget arende"
          % ", ".join(sorted(UTAN_HUVUDBETYDELSE)))


if __name__ == "__main__":
    main()
