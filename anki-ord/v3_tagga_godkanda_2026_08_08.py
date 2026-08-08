# -*- coding: utf-8 -*-
"""Registrerar sökkollen på de kort som klarade v3-granskningen utan omskrivning.

Innehållet rörs inte -- bara tagg och flagga sätts, så inga innehållsspärrar
kringgås (de skyddar skrivning av fält, och här skrivs inga fält).
"""
from ankiconnect import invoke
import config

D = f'deck:"{config.DECK_NAME}"'

GODKANDA = [
    "troppa av", "försummelse", "redare", "räfst", "hygrometer", "uppehälle",
    "skälmaktig", "båk", "byke", "kanalje", "drabbning", "teologi",
    "konvulsion", "crème-de-la-crème", "kollrig", "gynekolog", "hängiven",
    "jorda", "ackumulation", "enhällig", "ganglie", "uppsluppen",
]


def main():
    nids, cids, miss = [], [], []
    for o in GODKANDA:
        n = invoke("findNotes", query=f'{D} "Framsida:{o}"')
        if not n:
            miss.append(o)
            continue
        nids.append(n[0])
        cids += invoke("findCards", query=f'{D} "Framsida:{o}"')

    print(f"hittade: {len(nids)} av {len(GODKANDA)}")
    if miss:
        print("SAKNAS:", ", ".join(miss))

    invoke("addTags", notes=nids, tags="flerbetydelse_sokverifierad::2026-08-08")
    for c in cids:
        invoke("setSpecificValueOfCard", card=c, keys=["flags"],
               newValues=[4], warning_check=True)

    for lbl, q in [
        ("prop:due=0 totalt", f"{D} prop:due=0"),
        ("  varav gron", f"{D} prop:due=0 flag:3"),
        ("  varav bla", f"{D} prop:due=0 flag:4"),
        ("sokverifierad::2026-08-08", f"{D} tag:flerbetydelse_sokverifierad::2026-08-08"),
    ]:
        print(f"{lbl}: {len(invoke('findCards', query=q))}")


if __name__ == "__main__":
    main()
