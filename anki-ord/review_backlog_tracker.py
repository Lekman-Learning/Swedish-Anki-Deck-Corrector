"""Räknar ut hur många is:review-kort som ska köras IDAG för att beta av en
eftersläpning (overdue-hög) fram till ett satt måldatum -- den "lata"
varianten: du behöver aldrig komma ihåg var i planen du är eller räkna om
för hand. Kör scriptet, gör det tal det säger, glöm bort det till nästa gång.

Hur den lata delen funkar: FÖRSTA körningen sätter ett måldatum (idag + N
dagar) och sparar det i `backlog_mal.json`. Varje körning DÄREFTER läser
det sparade måldatumet och räknar ut dagens tal utifrån två live-fakta:
  1. Hur många is:review-kort som faktiskt är förfallna just nu (inte vad
     planen TRODDE skulle vara kvar).
  2. Hur många dagar som faktiskt är kvar till måldatumet.

Gjorde du färre kort än riktvärdet en dag: fler kort är förfallna imorgon,
färre dagar är kvar -> dagens tal höjs automatiskt för att fortfarande
hinna. Gjorde du fler: färre kort är förfallna, dagens tal sänks
automatiskt. Du rättar aldrig planen själv -- den rättar sig själv, för att
den aldrig litar på något annat än vad Anki faktiskt säger just nu.

Körs: python review_backlog_tracker.py                 (läser sparat mål,
                                                          eller frågar om ett nytt om inget finns)
      python review_backlog_tracker.py --dagar 14       (sätter/ersätter mål: idag + 14 dagar)
      python review_backlog_tracker.py --rensa          (glömmer sparat mål utan att sätta nytt)
      python review_backlog_tracker.py --deck NAMN      (annat deck än standard)
"""

import argparse
import datetime
import json
import math
import os

import config
from ankiconnect import invoke

STATE_FIL = os.path.join(os.path.dirname(__file__), "backlog_mal.json")


def hamta_eftersläpning(deck):
    """is:review-kort som är förfallna t.o.m. idag (prop:due<=0), ej
    suspenderade -- det ÄR eftersläpningen just nu, oavsett vad en gammal
    plan trodde."""
    query = f'deck:"{deck}" is:review -is:suspended prop:due<=0'
    return len(invoke("findCards", query=query))


def hamta_naturligt_forfall(deck, dag):
    """Ungefär hur många is:review-kort som förfaller om `dag` dagar om
    inget görs utöver det redan schemalagda. Approximation -- kort som
    körs och lyckas idag får nytt intervall och dyker inte upp exakt här
    längre. Bara till för överblick, inte en exakt siffra."""
    query = f'deck:"{deck}" is:review -is:suspended prop:due={dag}'
    return len(invoke("findCards", query=query))


def läs_state():
    if not os.path.exists(STATE_FIL):
        return None
    with open(STATE_FIL, "r", encoding="utf-8") as f:
        return json.load(f)


def skriv_state(state):
    with open(STATE_FIL, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def sätt_nytt_mål(deck, dagar, eftersläpning_nu):
    idag = datetime.date.today()
    mål = idag + datetime.timedelta(days=dagar)
    state = {
        "deck": deck,
        "start_datum": idag.isoformat(),
        "mål_datum": mål.isoformat(),
        "start_eftersläpning": eftersläpning_nu,
    }
    skriv_state(state)
    return state


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--dagar", type=int, default=None,
        help="Sätt/ersätt målet: beta av dagens eftersläpning över N dagar från idag",
    )
    parser.add_argument("--rensa", action="store_true", help="Glöm sparat mål utan att sätta ett nytt")
    parser.add_argument("--deck", default=config.DECK_NAME, help=f"Deck-namn (default: {config.DECK_NAME!r})")
    args = parser.parse_args()

    if args.rensa:
        if os.path.exists(STATE_FIL):
            os.remove(STATE_FIL)
            print("Sparat mål borttaget. Kör med --dagar N för att sätta ett nytt.")
        else:
            print("Inget sparat mål fanns.")
        return

    eftersläpning = hamta_eftersläpning(args.deck)
    print(f"Deck: {args.deck}")
    print(f"Eftersläpning just nu (is:review, förfallet t.o.m. idag): {eftersläpning} kort\n")

    state = läs_state()

    if args.dagar is not None:
        state = sätt_nytt_mål(args.deck, args.dagar, eftersläpning)
        print(f"Nytt mål satt: beta av {eftersläpning} kort till {state['mål_datum']} ({args.dagar} dagar).\n")
    elif state is None:
        print("Inget sparat mål ännu. Kör med --dagar N för att sätta ett (t.ex. --dagar 14).")
        return

    idag = datetime.date.today()
    mål_datum = datetime.date.fromisoformat(state["mål_datum"])
    dagar_kvar = (mål_datum - idag).days

    if eftersläpning == 0:
        print("Eftersläpningen är avbetad. 🎉")
        if os.path.exists(STATE_FIL):
            os.remove(STATE_FIL)
            print("Sparat mål borttaget -- sätt ett nytt med --dagar N nästa gång du vill jaga ikapp något.")
        return

    if dagar_kvar <= 0:
        print(f"🔴 Måldatumet ({state['mål_datum']}) har passerat och {eftersläpning} kort återstår.")
        print("Antingen kör allihopa idag, eller sätt ett nytt mål: --dagar N.")
        idag_tal = eftersläpning
    else:
        idag_tal = math.ceil(eftersläpning / dagar_kvar)

    # Är du före eller efter takt jämfört med planen? Linjär approximation
    # (ignorerar naturligt tillskott) -- bara till för överblick.
    start_datum = datetime.date.fromisoformat(state["start_datum"])
    total_dagar = max((mål_datum - start_datum).days, 1)
    förflutna_dagar = (idag - start_datum).days
    andel_tid_förbi = min(förflutna_dagar / total_dagar, 1.0)
    förväntad_kvar = round(state["start_eftersläpning"] * (1 - andel_tid_förbi))
    diff = eftersläpning - förväntad_kvar
    if diff > 5:
        takt_text = f"⚠️ {diff} kort EFTER takt jämfört med en jämn plan från start"
    elif diff < -5:
        takt_text = f"✅ {-diff} kort FÖRE takt jämfört med en jämn plan från start"
    else:
        takt_text = "på ungefär rätt takt"

    print(f"Mål: {state['mål_datum']} ({dagar_kvar} dagar kvar) -- {takt_text}\n")
    print(f"IDAG: kör {idag_tal} is:review-kort")
    print(f"  ({eftersläpning} kort / {max(dagar_kvar, 1)} dagar kvar, avrundat uppåt)\n")

    horisont = min(dagar_kvar, 14) if dagar_kvar > 0 else 0
    if horisont > 1:
        print(f"Ungefärlig {horisont}-dagars projektion (riktlinje -- kör scriptet igen imorgon för det riktiga talet):")
        print(f"  {'Dag':<12}{'Beta av-andel':<16}{'+ naturligt förfall':<22}{'~ Totalt'}")
        kvar = eftersläpning
        for dag in range(0, horisont):
            dagar_kvar_då = dagar_kvar - dag
            beta_av = min(math.ceil(kvar / max(dagar_kvar_då, 1)), kvar)
            kvar -= beta_av
            naturligt = hamta_naturligt_forfall(args.deck, dag) if dag > 0 else 0
            totalt = beta_av + naturligt
            etikett = "Idag" if dag == 0 else f"+{dag} dagar"
            print(f"  {etikett:<12}{beta_av:<16}{naturligt:<22}{totalt}")


if __name__ == "__main__":
    main()
