"""Rödflaggar korten i `tre_kallor_saknas.json` — Adams krav 2026-08-10.

    *"Om du hittar kort där inte detta funkar, så vill jag att du rödmarkerar
    dem. Markera dem i en separat lista, så kan vi gå igenom dem senare för
    att se vad som har gått fel."*

Två nivåer, eftersom de kräver olika åtgärd:

**INGEN källa alls** -> röd flagga OCH suspenderas. Kortet vilar då på
ingenting alls, och att låta det ligga kvar i inlärningskön vore att öva in
något ingen kontrollerat. `degression` och `av hävd` är i det läget.

**En eller två källor** -> röd flagga, men kortet ligger kvar. Innehållet är
belagt, bara inte tre gånger. De flesta av dem är idiom eller fackord som helt
enkelt inte finns i synonymer.se eller Wiktionary — det är ett besked om
KÄLLORNA, inte om kortet.

Skriptet är avsiktligt idempotent: körs det igen tar det bort flaggan från
kort som sedan dess fått sina tre källor. En flagga som ligger kvar efter att
problemet är löst blir brus, och brus lär man sig att ignorera.
"""
import json
import os
import sys

import config
from ankiconnect import invoke

BRISTLISTA = "tre_kallor_saknas.json"


def main():
    if not os.path.exists(BRISTLISTA):
        sys.exit(f"{BRISTLISTA} saknas — kör slaupp.py först.")
    brist = json.load(open(BRISTLISTA, encoding="utf-8"))

    # Poster med alla tre källorna hör inte hemma i bristlistan alls. De
    # uppstår när ett IDIOM belagts via sitt grundord (`av hävd` via `hävd`):
    # slaupp.py kan bara mäta idiomsträngen, som aldrig ger träff, medan
    # belägget i själva verket finns i grundordets artikel. Utan den här
    # raden rödflaggades två korrekt belagda kort 2026-08-10.
    losta = {o: v for o, v in brist.items() if len(v.get("har") or []) >= 3}
    utan_kalla = [o for o, v in brist.items() if not v.get("har")]
    delvis = [o for o, v in brist.items()
              if v.get("har") and o not in losta]

    flaggade, suspenderade, saknade = [], [], []
    for ord_, suspendera in ([(o, True) for o in utan_kalla]
                             + [(o, False) for o in delvis]):
        kort = invoke("findCards",
                      query=f'deck:"{config.DECK_NAME}" '
                            f'"Framsida:{ord_}"')
        if not kort:
            saknade.append(ord_)
            continue
        # newValues tar ett INT, inte en sträng -- AnkiConnect svarar annars
        # "'str' object cannot be interpreted as an integer". Samma anropsform
        # som apply_flerbetydelse.py rad 99.
        invoke("setSpecificValueOfCard", card=kort[0],
               keys=["flags"], newValues=[config.FLAG_ROD], warning_check=True)
        flaggade.append(ord_)
        if suspendera:
            invoke("suspend", cards=kort)
            suspenderade.append(ord_)

    print(f"Rödflaggade {len(flaggade)} kort "
          f"({len(utan_kalla)} utan källa, {len(delvis)} med 1–2 källor)")
    if suspenderade:
        print(f"Suspenderade (ingen källa alls): {', '.join(suspenderade)}")
    if saknade:
        print(f"Hittade inget kort för: {', '.join(saknade)}")

    # Den separata listan Adam bad om, i läsbar form vid sidan av JSON:en.
    with open("tre_kallor_saknas.md", "w", encoding="utf-8") as f:
        f.write("# Kort som saknar en eller flera av de tre källorna\n\n")
        f.write("Skapad automatiskt av `rodflagga_bristlista.py`. Alla kort "
                "nedan är **rödflaggade** i Anki.\n\n")
        f.write("Regeln (Adam 2026-08-10): varje kort ska ha svenska.se, "
                "synonymer.se och Wiktionary. Räcker de inte till görs en "
                "allmän webbsökning. Går det ändå inte — hit.\n\n")
        f.write("## Ingen källa alls — rödflaggade OCH suspenderade\n\n")
        if utan_kalla:
            for o in sorted(utan_kalla):
                f.write(f"- **{o}** — inget uppslag i någon av de tre. "
                        f"Kortet är suspenderat tills en källa hittats.\n")
        else:
            f.write("*(inga)*\n")
        f.write("\n## En eller två källor — rödflaggade, ligger kvar\n\n")
        f.write("| Ord | Har | Saknar |\n|---|---|---|\n")
        alla = {"svenska.se", "synonymer.se", "wiktionary"}
        for o in sorted(delvis):
            har = brist[o]["har"]
            f.write(f"| {o} | {', '.join(har)} | "
                    f"{', '.join(sorted(alla - set(har)))} |\n")
        f.write("\n**Läs så här:** de flesta raderna är idiom eller fackord "
                "som helt enkelt inte finns i synonymer.se eller Wiktionary. "
                "Det säger något om källorna, inte om kortet. Ett kort blir "
                "inte fel av att bara SO har ordet.\n")
    print("Skrev tre_kallor_saknas.md")


if __name__ == "__main__":
    main()
