# -*- coding: utf-8 -*-
"""Delar ett v3-paket i mindre delar inför blindgranskningen.

VARFÖR DELNINGEN BEHÖVS. Ett paket på 50 kort får granskaren att spara
kontext: den slår upp de första orden ordentligt och börjar sedan svara ur
minnet på resten. Det syns inte i utdata -- domarna ser likadana ut -- men
turantalet avslöjar det. Delar på 25 har hållit sig runt 34-51 turer, alltså
1,4-2 turer per kort, vilket är vad en verklig uppslagning kostar.

Delningen är alltså inte en teknisk begränsning (paketet ryms i kontexten)
utan en kvalitetsspärr. `blindgranska.py` har golvet `max(5, n // 4)`, men
ett golv fångar bara det grova fallet; små paket förebygger problemet.

Verdikten ligger kvar i deldelarna, och `kortgranskare.py verdikt` körs en
gång per del. Ursprungsfilen rörs inte -- den är kvar som facit på vad
batchen bestod av.
"""
import argparse
import json
import os


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paket", help="sessions/<namn>_v3-paket.json")
    ap.add_argument("--storlek", type=int, default=25,
                    help="kort per del (standard 25)")
    args = ap.parse_args()

    with open(args.paket, encoding="utf-8") as f:
        data = json.load(f)

    poster = data["poster"]
    redan = [p for p in poster if p.get("verdikt")]
    if redan:
        print("VARNING: %d av %d poster har redan verdikt -- de följer med in i\n"
              "  delarna och blir granskade igen." % (len(redan), len(poster)))

    bas, ext = os.path.splitext(args.paket)
    delar = [poster[i:i + args.storlek]
             for i in range(0, len(poster), args.storlek)]
    # Kontrollen görs för ALLA delar innan någon skrivs. En kontroll inne i
    # skrivloopen hade lämnat del1 överskriven när del2 stoppade körningen --
    # halvvägs är sämre än inte alls när det som står på spel är domar.
    for n in range(1, len(delar) + 1):
        ut = "%s-del%d%s" % (bas, n, ext)
        # Delnamnen härleds ur moderpaketets namn, och två batchar samma dag
        # kan mycket väl heta samma sak -- det hände 2026-08-11, då den här
        # delningen tyst skrev över 50 färdiggranskade verdikt (de gick att
        # hämta ur git, men bara för att de råkade vara committade). En delfil
        # med verdikt är resultatet av en betald granskningskörning; den får
        # inte försvinna för att ett filnamn krockade.
        if not os.path.exists(ut):
            continue
        with open(ut, encoding="utf-8") as f:
            gammal = json.load(f)
        dömda = sum(1 for p in gammal.get("poster", []) if p.get("verdikt"))
        if dömda:
            print("AVBRYTER: %s finns redan och har %d domar.\n"
                  "  Byt namn på moderpaketet eller flytta undan den gamla\n"
                  "  delen först. Inget har skrivits." % (ut, dömda))
            return 1

    for n, grupp in enumerate(delar, 1):
        d = dict(data)
        d["poster"] = grupp
        # Turantalet hör till den granskning som faktiskt körs på DEN HÄR
        # delen. Att ärva moderpaketets siffra vore att påstå ett underlag
        # som inte finns.
        for nyckel in ("granskare", "granskning_turer",
                       "granskning_kostnad_usd", "granskning_turkrav"):
            d.pop(nyckel, None)
        ut = "%s-del%d%s" % (bas, n, ext)
        with open(ut, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print("%s  %d kort" % (ut, len(grupp)))

    print("\nKör nu, en del i taget:")
    for n in range(1, len(delar) + 1):
        print("  python blindgranska.py %s-del%d%s" % (bas, n, ext))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
