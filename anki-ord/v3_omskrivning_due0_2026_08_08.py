# -*- coding: utf-8 -*-
"""v3-omskrivning av gröna kort med prop:due=0 (schemalagda 2026-08-08).

Samma väg som föregående batch: apply_card() så att validate_register()
och validate_adamtal() körs. mode="sokkoll", escalated=True -- varje kort
har jämförts mot Svenska OLD där facit finns, annars dubbelkollat.

oberoende_verifierad sätts INTE: samma agent skriver och granskar.
"""
import sys

import apply_flerbetydelse as af
from ankiconnect import invoke
import config

B = '<font color="#3498db">%s</font>'

KORT = [
    # --- verkliga fel ---
    ("förära", "Ge bort som hedersgåva", "litterär",
     ["skänka", "tilldela", "överlämna"],
     f"Kungen {B % 'förärade'} honom en medalj för hans insats."),          # syftningsfel: "sin" -> "hans"

    ("paralysera", "Göra oförmögen att röra sig", "formell",
     ["förlama", "lamslå"],
     f"Olyckan {B % 'paralyserade'} hans vänstra arm."),                    # pleonasm: "olyckliga olyckan"

    ("ovarium", "Äggstock, den honliga könskörteln", "formell",
     ["äggstock"],
     f"Ett {B % 'ovarium'} frisätter ägg under menstruationscykeln."),      # var för snävt: "kvinnans"

    ("svara för", "Ha ansvaret för något / Utgöra en viss andel", "formell",
     ["ansvara för", "stå för", "utgöra"],
     f"Exporten {B % 'svarar för'} en tredjedel av företagets omsättning."),  # saknad betydelse

    # --- helt cirkulära ---
    ("respiration", "Kroppens gasutbyte — syre in, koldioxid ut", "formell",
     ["andning", "andhämtning"],
     f"Patientens {B % 'respiration'} övervakades under operationen."),

    # --- svaga eller felaktiga synonymer ---
    ("utgrunda", "Genom eftertanke komma fram till något svårt", "litterär",
     ["klura ut", "lista ut", "räkna ut"],
     f"Han satt länge och försökte {B % 'utgrunda'} gåtans lösning."),      # "genomskåda" var fel betydelse

    ("ortopedi", "Medicinsk specialitet för skelett, muskler och leder", "formell",
     ["rörelseorganens medicin"],
     f"Hon opererades av en kirurg specialiserad på {B % 'ortopedi'}."),    # "skelettlära" var för snävt

    ("syntax", "Läran om hur ord fogas samman till satser", "formell",
     ["satslära"],
     f"{B % 'Syntaxen'} reglerar hur orden ordnas i en mening."),           # "grammatik" var för brett

    # --- delvis cirkulära, Adam-tal ---
    ("aseptisk", "Fri från sjukdomsalstrande mikroorganismer", "formell",
     ["steril", "bakteriefri"],
     f"Operationssalen hölls helt {B % 'aseptisk'}."),

    ("kronologi", "Ordningen som händelser inträffar i", "formell",
     ["tidsföljd", "tidsordning"],
     f"{B % 'Kronologin'} kastas om i berättelsen genom flera tillbakablickar."),

    ("residuum", "Det som blir kvar efter en process", "formell",
     ["rest", "återstod", "kvarleva"],
     f"Materialet löstes upp fullständigt utan {B % 'residuum'}."),

    ("pigment", "Ämne som ger färg åt vävnad eller material", "formell",
     ["färgämne", "färgkropp"],
     f"Han tillsatte lite {B % 'pigment'} för en varmare ton."),

    ("surmulen", "Tystlåtet missnöjd och tvär", "vardaglig",
     ["tjurig", "vresig", "butter"],
     f"Trots att solen sken var han {B % 'surmulen'} över att behöva städa."),

    ("lapidarisk", "Knapp i formen men träffsäker", "litterär",
     ["kortfattad", "koncis", "fåordig"],
     f"Den {B % 'lapidariska'} stilen i de isländska sagorna imponerade på forskarna."),

    ("näpsa", "Ge någon en skarp tillsägelse", "litterär",
     ["tillrättavisa", "banna", "tukta"],
     f"Statsrådet {B % 'näpste'} journalisterna för deras påstridiga frågor."),
]


def main():
    ok, fel = [], []
    for ord_, huvud, reg, syn, ex in KORT:
        try:
            nids = invoke("findNotes",
                          query=f'deck:"{config.DECK_NAME}" "Framsida:{ord_}"')
            if not nids:
                fel.append((ord_, "hittade ingen not"))
                continue
            anm = af.apply_card(nids[0], huvudbetydelse=huvud, synonymer=syn,
                                exempelmening=ex, register=reg,
                                mode="sokkoll", escalated=True, ord_=ord_)
            ok.append((ord_, anm))
        except Exception as e:
            fel.append((ord_, f"{type(e).__name__}: {e}"))

    print(f"=== SKRIVNA: {len(ok)} ===")
    for o, anm in ok:
        print(f"  {o}" + (f"   [anm: {anm}]" if anm else ""))
    print(f"=== FEL: {len(fel)} ===")
    for o, m in fel:
        print(f"  {o}: {m}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
