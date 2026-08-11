"""Rangordnar is:review-korten efter hur bråttom det är att full-v3-kolla dem.

Adams beslut 2026-08-11: "alla kort som jag studerar varje dag även av de som
är is:review ska vara full v3 kollade. kan vi skapa en urgency lista utav de
som är viktigaste att full v3 kolla först?"

VARFÖR EN RANKNING BEHÖVS. Spår B (`kortbyggare.py --spar omgranskning`)
sorterar på `due`. Det är en tidsordning, inte en riskordning: kortet som
råkar förfalla imorgon går före ett kort som Adam har fastnat på nio gånger
och som aldrig sökkollats. Med ~2 670 kort i is:review och 70 kort per pass
tar hela kön ~38 pass -- vilket kort som ligger först avgör alltså hur länge
ett faktiskt fel får stå kvar i det material han pluggar varje dag.

POÄNGEN ÄR EN PRODUKT AV TVÅ SAKER, och båda behövs:

  RISK       hur sannolikt det är att kortet är fel -- avgörs av hur kortet
             blev till (aldrig sökkollat? legacy-format? känt botchat?)
  EXPONERING vad felet kostar -- hur ofta och hur snart Adam ser kortet

Ett aldrig sökkollat kort med 400 dagars intervall är förmodligen fel men
kostar nästan ingenting. Ett kort han fastnat på sex gånger med tre dagars
intervall kostar varje vecka. Bara risk vore fel ranking; bara exponering
vore fel ranking. Därför summeras de.

LAPSES ÄR DEN VIKTIGASTE SIGNALEN och förtjänar en förklaring: ett kort Adam
upprepat misslyckas på tolkas normalt som att HAN inte kan ordet. Men i det
här decket är den andra förklaringen minst lika trolig -- att KORTET är fel,
och att han failar det för att han lärt sig rätt sak och kortet påstår något
annat. De korten kan man inte hitta genom att läsa taggar; de syns bara i
felstatistiken.

  python v3_urgency.py                 # skriv rankad lista
  python v3_urgency.py --tagga 70      # + tagga topp 70 med v3_prio::hog
"""

import argparse
import json
import re
from collections import Counter

import baksida
import config
from ankiconnect import invoke

DECK = f'deck:"{config.DECK_NAME}"'
# is:review UTAN is:learn -- ett kort i ominlärning matchar båda, och de
# hanterades redan av v3_suspend_ofullstandiga.py.
MALGRUPP = f"{DECK} is:review -is:learn"

UTFIL_MD = "v3_urgency.md"
UTFIL_JSON = "v3_urgency.json"

# --- Riskvikter: hur kortet blev till ------------------------------------
# Vikterna är ordinala, inte kalibrerade sannolikheter. De säger "aldrig
# sökkollad är värre än legacy-format", inte "exakt dubbelt så illa".
RISK = [
    ("saknar sökkoll", f"-tag:{config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX}::*", 40),
    ("känt botchad (prio::hog)", f"tag:{config.PRIO_TAG_HOG}", 30),
    ("legacy-format", f"-tag:{config.FORMAT_TAG_V2}", 25),
    ("flerbetydelse ej kollad", f"-tag:{config.FLERBETYDELSE_TAG_PREFIX}::*", 20),
    ("röd flagga", "flag:1", 15),
    ("gul flagga", "flag:2", 8),
    # Nästan alla kort saknar denna -- svag diskriminering, låg vikt. Att ge
    # den hög vikt hade bara adderat en konstant till alla och inte ändrat
    # ordningen alls.
    ("saknar blindgranskning", f"-tag:{config.OBEROENDE_TAG_PREFIX}::*", 5),
]

LAPS_POANG = 7      # per lapse
LAPS_TAK = 35       # 5 lapses räcker för full poäng
DUE_SNART_POANG = 10

# Registerbrist kan inte uttryckas som en Anki-sökning -- den syns först när
# baksidan parsas och valideras. Mäts därför separat och adderas till risken.
# Vikten är hög (2026-08-11): 25 % av de full-v3-taggade korten saknar valör,
# och ett kort med bara halva registret är tvetydigt, inte delvis märkt.
REGISTER_POANG = 35


def exponering(ivl, lapses, snart):
    p = min(lapses * LAPS_POANG, LAPS_TAK)
    if ivl <= 7:
        p += 25
    elif ivl <= 21:
        p += 15
    elif ivl <= 60:
        p += 7
    if snart:
        p += DUE_SNART_POANG
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tagga", type=int, metavar="N",
                    help=f"tagga topp N med {config.PRIO_TAG_HOG}")
    args = ap.parse_args()

    # Redan färdiga kort ska INTE rankas. De har inget arbete kvar, och
    # `--ids-fil` i kortbyggare går förbi POOL_FRAGA -- alltså förbi filtret
    # `-tag:oberoende_verifierad::*` som annars håller dem ute. Utan det här
    # hade de 45 kort som blindverifierades 2026-08-11 kunnat serveras tillbaka
    # i nästa batch och kostat en full omgång för ingenting.
    klara = set(invoke("findCards", query=(
        f"{MALGRUPP} tag:{config.OBEROENDE_TAG_PREFIX}::*")))
    pausade = set(invoke("findCards", query=f"{DECK} tag:v3_pausad::*"))
    # Provisoriskt släppta kort ligger redan i Adams kö och pluggas -- de har
    # en riktig sökkoll och väntar bara på blindgranskning. Adams ordning
    # 2026-08-11: ta de 1 982 SUSPENDERADE först, eftersom de är helt osynliga
    # för honom just nu, och återvänd till de 618 provisoriska efteråt.
    provisoriska = set(invoke("findCards", query=f"{DECK} tag:v3_provisorisk::*"))
    kort = [c for c in invoke("findCards", query=MALGRUPP)
            if c not in klara and c not in pausade and c not in provisoriska]
    print(f"is:review -is:learn: {len(kort)} kort att granska "
          f"({len(klara)} klara, {len(provisoriska)} provisoriska, "
          f"{len(pausade)} pausade — alla undantagna)")

    # Medlemskap via Ankis egen sökning i stället för egen datumräkning:
    # `due` är dagar sedan collection skapades, och att räkna om det själv
    # är ett extra ställe att ha fel på.
    traffar = {}
    for namn, uttryck, vikt in RISK:
        traffar[namn] = set(invoke("findCards", query=f"{MALGRUPP} {uttryck}"))
    snart_set = set(invoke("findCards", query=f"{MALGRUPP} prop:due<=7"))

    info = invoke("cardsInfo", cards=kort)
    noter = invoke("notesInfo", notes=list({c["note"] for c in info}))
    ord_per_not = {}
    register_brist = set()
    for n in noter:
        ra = n["fields"].get(config.FIELD_ORD, {}).get("value", "")
        ord_per_not[n["noteId"]] = re.sub(r"<[^>]+>", "", ra).strip()
        try:
            parsed = baksida.parse(n["fields"].get(config.FIELD_BAKSIDA, {}).get("value", ""))
            if baksida.validate_register(parsed.get("register")):
                register_brist.add(n["noteId"])
        except Exception:
            # Ett kort som inte ens går att parsa är per definition misstänkt.
            register_brist.add(n["noteId"])

    rader = []
    for c in info:
        cid = c["cardId"]
        skal, risk = [], 0
        for namn, _u, vikt in RISK:
            if cid in traffar[namn]:
                risk += vikt
                skal.append(namn)
        if c["note"] in register_brist:
            risk += REGISTER_POANG
            skal.append("ogiltigt register")
        ivl, laps = c["interval"], c["lapses"]
        snart = cid in snart_set
        exp = exponering(ivl, laps, snart)
        rader.append({
            "cardId": cid, "ord": ord_per_not.get(c["note"], "?"),
            "poang": risk + exp, "risk": risk, "exp": exp,
            "ivl": ivl, "lapses": laps, "reps": c["reps"],
            "due_snart": snart, "skal": skal,
        })

    rader.sort(key=lambda r: (-r["poang"], -r["lapses"], r["ivl"]))

    with open(UTFIL_JSON, "w", encoding="utf-8") as f:
        json.dump(rader, f, ensure_ascii=False, indent=1)

    fordelning = Counter()
    for r in rader:
        for s in r["skal"]:
            fordelning[s] += 1

    with open(UTFIL_MD, "w", encoding="utf-8") as f:
        f.write("# Urgency — is:review-kort att full-v3-kolla\n\n")
        f.write(f"{len(rader)} kort. Poäng = RISK (hur kortet blev till) + "
                f"EXPONERING (hur ofta/snart Adam ser det).\n")
        f.write("Genererad av `v3_urgency.py` — skriv inte i den här filen för hand.\n\n")
        f.write("## Hur riskskälen fördelar sig\n\n| Skäl | Kort | Vikt |\n|---|---|---|\n")
        for namn, _u, vikt in RISK:
            f.write(f"| {namn} | {fordelning[namn]} | +{vikt} |\n")
        f.write(f"\n## Topp 200\n\n| # | Ord | Poäng | Risk | Exp | Ivl | Lapses | Skäl |\n")
        f.write("|---|---|---|---|---|---|---|---|\n")
        for i, r in enumerate(rader[:200], 1):
            f.write(f"| {i} | {r['ord']} | **{r['poang']}** | {r['risk']} | {r['exp']} "
                    f"| {r['ivl']}d | {r['lapses']} | {', '.join(r['skal'])} |\n")

    print(f"\nSkrev {UTFIL_MD} och {UTFIL_JSON}")
    print("\nTopp 15:")
    for i, r in enumerate(rader[:15], 1):
        print(f"{i:>3}. {r['ord']:<22} {r['poang']:>4}p  "
              f"(risk {r['risk']}, exp {r['exp']}; ivl {r['ivl']}d, {r['lapses']} lapses)")

    p = [r["poang"] for r in rader]
    print(f"\nPoängspann: {p[0]} (högst) .. {p[-1]} (lägst), median {p[len(p)//2]}")

    if args.tagga:
        topp = rader[:args.tagga]
        invoke("addTags", notes=list({
            c["note"] for c in info if c["cardId"] in {r["cardId"] for r in topp}
        }), tags=config.PRIO_TAG_HOG)
        print(f"\nTaggade topp {args.tagga} med {config.PRIO_TAG_HOG} "
              f"(poäng {topp[-1]['poang']} och uppåt).")


if __name__ == "__main__":
    main()
