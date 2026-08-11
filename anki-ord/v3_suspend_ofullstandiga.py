"""Suspenderar varje kort i is:new och is:relearn som INTE har full v3.

Adams beslut 2026-08-11: "suspenda alla kort som inte är full v3 kollade på
is:new eller is:relearn. Däremot de som är is:review kan du lämna, de får vi
kämpa med en annan dag."

Skillnaden mot suspend_unreviewed_new.py (2026-08-05) är vilken ribba som
gäller: det skriptet krävde bara kortformat::v2. Här är ribban hela
config.SLAPP_KRAVER_TAGGAR -- alla fem taggarna som kortgranskare.slapp()
kräver för att ett kort ska få avsuspenderas. Ribban läses från config, den
skrivs inte av här: annars kan de två definitionerna glida isär och det här
skriptet börjar tyst släppa igenom kort som slapp() skulle stoppa.

VARFÖR is:review lämnas: de korten pluggar Adam redan. Att suspendera dem
skulle radera pågående inlärningsintervall -- ett vunnet minne kastas bort
för att kortets granskningsstatus är okänd. is:new och is:relearn kostar
ingenting att hålla tillbaka; ett kort som aldrig visats har inget att tappa.

Suspend är persistent (till skillnad från Ankis "bury") och reversibelt.
apply_updates.py avsuspenderar automatiskt när ett kort granskats färdigt.
Säkert att köra om.

Kör med --torr för att bara mäta utan att röra något.
"""

import sys

import config
from ankiconnect import invoke

DECK = f'deck:"{config.DECK_NAME}"'

# Sökuttryck per krav i SLAPP_KRAVER_TAGGAR. Taggarna är hierarkiska
# (prefix::YYYY-MM-DD) utom kortformat::v2 som är exakt -- därför wildcard
# på prefixen och exakt match på formattaggen.
KRAV = [
    (config.FORMAT_TAG_V2, f"tag:{config.FORMAT_TAG_V2}"),
    (config.FLERBETYDELSE_TAG_PREFIX, f"tag:{config.FLERBETYDELSE_TAG_PREFIX}::*"),
    (config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX,
     f"tag:{config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX}::*"),
    (config.V3_TAG_PREFIX, f"tag:{config.V3_TAG_PREFIX}::*"),
    (config.OBEROENDE_TAG_PREFIX, f"tag:{config.OBEROENDE_TAG_PREFIX}::*"),
]


def hitta(query):
    return set(invoke("findCards", query=query))


def main():
    torr = "--torr" in sys.argv
    # Adams beslut 2026-08-11 (utvidgat samma dag): "Jag vill att vi suspendar
    # allt som inte är full v3." Ursprungsbeslutet undantog is:review för att
    # inte kasta pågående inlärningsintervall. Undantaget är nu upphävt --
    # suspend BEHÅLLER intervallet (till skillnad från forgetCards), så ett
    # avsuspenderat kort återtar sin plats i schemat. Priset är alltså att kön
    # tystnar tills korten granskats, inte att repetitionshistoriken går förlorad.
    allt = "--allt" in sys.argv

    # Spärr: om ribban i config utökas men KRAV inte följer med, skulle
    # skriptet tyst mäta mot en lägre ribba än slapp() kräver.
    if len(KRAV) != len(config.SLAPP_KRAVER_TAGGAR):
        sys.exit(
            f"AVBRYTER: config.SLAPP_KRAVER_TAGGAR har "
            f"{len(config.SLAPP_KRAVER_TAGGAR)} krav, det här skriptet känner "
            f"till {len(KRAV)}. Uppdatera KRAV innan du kör."
        )

    if not torr:
        print("Synkar Anki före...")
        invoke("sync")

    # Anki har ingen "is:relearn". Ett kort i ominlärning matchar is:learn OCH
    # is:review samtidigt -- alltså överlappar Adams "ta is:relearn" och "lämna
    # is:review" i Ankis egen syntax. Löses så här: relearn = is:learn is:review,
    # och review-som-lämnas = is:review -is:learn (äkta repetitionskort).
    nya = hitta(f"{DECK} is:new")
    relearn = hitta(f"{DECK} is:learn is:review")
    review = hitta(f"{DECK} is:review -is:learn")
    # Kort i FÖRSTA inlärningen är varken is:new eller relearn -- de nämndes
    # inte i beslutet, så de rörs inte. Mäts bara så luckan syns.
    forstainlarning = hitta(f"{DECK} is:learn -is:review")
    malgrupp = (nya | relearn | review | forstainlarning) if allt else (nya | relearn)

    print(f"\n{'':<38}{'kort':>7}")
    print(f"{'is:new':<38}{len(nya):>7}")
    print(f"{'relearn (is:learn is:review)':<38}{len(relearn):>7}")
    print(f"{'review (is:review -is:learn)':<38}{len(review):>7}"
          f"{'  INGÅR' if allt else '  rörs ej'}")
    print(f"{'första inlärning (is:learn -is:review)':<38}{len(forstainlarning):>7}"
          f"{'  INGÅR' if allt else '  rörs ej'}")
    print(f"{'  = MÅLGRUPP':<38}{len(malgrupp):>7}")

    # Full v3 = har samtliga fem taggar.
    full_v3 = malgrupp.copy()
    print("\nHur målgruppen faller på varje krav:")
    for namn, uttryck in KRAV:
        har = hitta(f"{DECK} {uttryck}")
        saknar = malgrupp - har
        full_v3 &= har
        print(f"  saknar {namn:<40}{len(saknar):>6}")

    redan_susp = hitta(f"{DECK} is:suspended")

    # PROVISORISKT SLÄPPTA (Adams beslut 2026-08-11, samma kväll som
    # suspenderingen). 618 kort som HAR en riktig sökkoll men ännu inte
    # blindgranskats släpptes medvetet tillbaka i kön, eftersom kostnaden för
    # att glömma 2 600 inlärda ord är säker medan risken att ett sökkollat kort
    # är fel är låg.
    #
    # De är alltså inte full v3 och ska inte påstås vara det -- men de får
    # heller inte spärras igen av en rutinkörning. Utan det här undantaget hade
    # nästa `--allt` tyst rivit upp beslutet, och utdatan hade sett ut som en
    # vanlig städning.
    provisoriska = hitta(f"{DECK} tag:v3_provisorisk::*")
    kandidater = malgrupp - full_v3 - provisoriska
    att_suspendera = kandidater - redan_susp
    if provisoriska:
        print(f"\n{'Provisoriskt släppta (undantas)':<44}{len(provisoriska):>6}")

    print(f"\n{'Full v3 i målgruppen (lämnas aktiva)':<44}{len(full_v3):>6}")
    print(f"{'Ofullständiga':<44}{len(kandidater):>6}")
    print(f"{'  varav redan suspenderade':<44}{len(kandidater & redan_susp):>6}")
    print(f"{'  ATT SUSPENDERA NU':<44}{len(att_suspendera):>6}")

    if torr:
        print("\n--torr: inget ändrat.")
        return

    if not att_suspendera:
        print("\nInget att göra -- allt ofullständigt är redan suspenderat.")
    else:
        invoke("suspend", cards=sorted(att_suspendera))

        # Verifiera mot Anki i stället för att lita på att anropet lyckades.
        kvar = (malgrupp - full_v3) - hitta(f"{DECK} is:suspended")
        if kvar:
            sys.exit(f"VARNING: {len(kvar)} ofullständiga kort är fortfarande aktiva.")
        print(f"\nKlart: {len(att_suspendera)} kort suspenderade, 0 ofullständiga kvar aktiva.")

    print(f"Aktiv nya-kö efter körningen   : "
          f"{len(hitta(f'{DECK} is:new -is:suspended'))} kort (alla full v3).")
    print(f"Aktiv repetitionskö efter      : "
          f"{len(hitta(f'{DECK} is:review -is:learn -is:suspended'))} kort.")
    if not allt:
        print(f"is:review orört                : {len(review)} kort.")

    print("\nSynkar Anki efter...")
    invoke("sync")
    print("Klart.")


if __name__ == "__main__":
    main()
