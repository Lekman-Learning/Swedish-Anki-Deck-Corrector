# -*- coding: utf-8 -*-
"""Sorterar en batch INNAN den skrivs: enkla kort forst, svara undan.

Adams regel 2026-09-02: "kort som inte gar att full v3-kora snabbt och enkelt
markeras med full v3 senare-tagg, sa hinner vi skriva de enklare korten forst."

VARFOR SORTERINGEN GORS FORE FORSTA FORSOKET, inte efter:
En omskrivning ar inte gratis. Ett underkant kort maste ratttas OCH granskas om,
och blindgranskningen kostar ~1,15 USD per 25 poster -- alltsa ungefar lika
mycket som att skriva kortet fran borjan. Att upptacka svarigheten efter
granskningen betalar man alltsa for tva ganger.

MATNINGEN som ger tumregeln (131 kort, batchen 2026-09-02):

    Grupp                Kort   Underkanda   Andel
    ingen SO-artikel        4        2        50 %
    1-2 SO-betydelser      75        6         8 %
    3-4 SO-betydelser      36        5        14 %
    5+ SO-betydelser       16        7        44 %

Antalet SO-betydelser ar alltsa den enda variabel som separerar -- 5+ ar
5,5 gangar sa riskabelt som 1-2. Kontrollprovet: FA KALLOR predicerar INTE
svarighet (14 kort med under 3 kallor, 0 underkanda), sa "lite underlag" ar
fel signal att sortera pa. Rakningen ar dessutom gratis: samma tal som
_pool.py redan skriver ut, ur forgranskas egna funktioner.

TVA VAGAR IN I TAGGEN:
  screena  -- fore skrivandet, pa matt betydelseantal (billigt, det har ar
              poangen med verktyget)
  tagga    -- efterat, for kort som fastnade anda: underkanda i
              blindgranskningen, eller blockerade av `slapp`

Bada skriver skalet till v3_senare.jsonl. En tagg utan skal ar en atervandsgrand
-- den dag korten ska betas av maste det ga att se VARFOR de lades undan, annars
borjar arbetet om fran noll.

Taggen andrar URVALET (kortbyggare.hamta_pool utesluter den, `--senare` hamtar
bara den). En tagg som bara syns i browsern hade inte lost nagonting: korten
hade legat kvar pa sina platser i due-ordningen och blockerat precis de luckor
de skulle lamna.
"""
import argparse, datetime, io, json, os, sys

import config
import forgranska as F
from ankiconnect import invoke

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

LOGG = "v3_senare.jsonl"
GRANS_BETYDELSER = 5          # 5+ SO-betydelser => 44 % underkanda, se docstring


def betydelseantal(o):
    """(antal, finns_uppslag). Samma rakning som _pool.py skriver ut."""
    f = os.path.join("uppslag", o + ".json")
    if not os.path.exists(f):
        return 0, False
    u = json.load(io.open(f, encoding="utf-8"))
    return len(F._so(u, "def")) + len(F._riktiga_underbetydelser(u)), True


def bedom(o):
    """-> (skjut_upp, skal). Enda stallet regeln finns uttryckt.

    FLERORDSUTTRYCK skjuts upp utan att raknas alls. svenska.se:s msearch har
    inga uppslagsord for fraser: den matchar de INGAENDE ORDEN och returnerar
    ett svar som ser fullt normalt ut. Mott 2026-09-02: `dra pa munnen` fick
    SO:s artiklar for "dra till med" och "sele" (remtyg pa hast) med tre
    definitioner och en etymologi, och `uppslagsordstraffar` sa 2 -- allt
    sag ut som en lyckad hamtning. Foljden ar varre an en tom traff, for
    `_ordboksbelagg` bygger da synonympoolen ur fel ord: for `dra pa munnen`
    blev de godtagna synonymerna "ackordeon, drakskepp, handklaver, mane,
    pjas, skadespel". Ett kort skrivet mot den poolen underkanns garanterat.
    For enstaka ord fangas samma fel -- da skriver uppslaget "INGEN
    UPPSLAGSORDSTRAFF" -- men for fraser gor det inte det.

    Regeln ar medvetet trubbig: den skjuter upp aven fraser vars ovriga
    kallor duger (`dra pa munnen` finns bade i synonymer.se och Wiktionary).
    Skalet ar att det ar forgranskas SO/SAOL-baserade pool som avgor om
    kortet gar igenom, och den ar forgiftad oavsett vad ovriga kallor sager.
    Fraser ska darfor skrivas medvetet, mot en kalla som faktiskt har dem.

    NOLL betydelser rakas hit tillsammans med "ingen fil", inte till de latta.
    Forsta skarpa korningen 2026-09-02 slappte igenom tio ord -- vitkrage,
    carpe diem, escargot, enigma m.fl. -- som hade en uppslagsfil men vars
    innehall var `kallor_med_innehall: []` och `verifieringsgrund: SAKNAS`.
    Regeln lat dem passera som latta eftersom 0 < 5. Bevislaget ar dock
    identiskt med att artikeln saknas helt: det finns ingenting att skriva
    kortet UR, och da hjalper det inte att antalet ar lagt. Ett tomt uppslag
    ser bara ut som ett enkelt ord.
    """
    if " " in o.strip():
        return True, ("flerordsuttryck -- SO:s msearch loser upp frasen i sina "
                      "enskilda ord och rapporterar det som TRAFF, sa "
                      "betydelseantalet galler ett annat ord")
    n, finns = betydelseantal(o)
    if not finns:
        return True, "ingen SO-artikel i uppslag/ (50 % underkanda i matningen)"
    if n == 0:
        return True, ("uppslag finns men 0 SO-betydelser -- inget att skriva ur "
                      "(samma bevislage som ingen artikel alls)")
    if n >= GRANS_BETYDELSER:
        return True, "%d SO-betydelser (5+ => 44 %% underkanda i matningen)" % n
    return False, "%d SO-betydelser" % n


def _noter(ord_):
    """ord -> noteIds, via EXAKT faltmatchning pa config.FIELD_ORD.

    `Framsida:chikan` ger 1 traff, `chikan` som fritext ger 2 -- den andra ar
    ett kort dar ordet nampns i baksidan. En tagg som satts pa fel not ar
    varre an ingen tagg alls, sa faltet anges alltid.
    """
    ut = {}
    for o in ord_:
        esc = o.replace('"', '\\"')
        ut[o] = invoke("findNotes", query='deck:"%s" "%s:%s"'
                       % (config.DECK_NAME, config.FIELD_ORD, esc))
    return ut


def _logga(rader):
    with io.open(LOGG, "a", encoding="utf-8") as fh:
        for r in rader:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


def _tagga(par, kalla, torr):
    """par: [(ord, skal)]. Satter taggen och loggar skalet."""
    nidmap = _noter([o for o, _ in par])
    dag = datetime.date.today().isoformat()
    lagg, rader, saknas = [], [], []
    for o, skal in par:
        nids = nidmap.get(o) or []
        if not nids:
            saknas.append(o)
            continue
        lagg += nids
        rader.append({"ord": o, "noteIds": nids, "skal": skal,
                      "kalla": kalla, "datum": dag})
    if torr:
        print("TORRKORNING -- inget skrivet till Anki.")
    elif lagg:
        invoke("addTags", notes=lagg, tags=config.PRIO_TAG_SENARE)
        _logga(rader)
    for r in rader:
        print("  %-24s %s" % (r["ord"], r["skal"]))
    if saknas:
        print("  HITTADES INTE i decket: " + ", ".join(saknas))
    print("Taggade %d ord (%d noter) med %s"
          % (len(rader), len(lagg), config.PRIO_TAG_SENARE))
    return rader


def cmd_screena(a):
    """Delar en ordlista i tva hogar. Skriver den enkla halvan till fil."""
    if a.fil:
        poster = json.load(io.open(a.fil, encoding="utf-8"))
        orden = [e["ord"] if isinstance(e, dict) else e for e in poster]
    else:
        orden = a.ord
    enkla, svara = [], []
    for o in orden:
        skjut, skal = bedom(o)
        (svara if skjut else enkla).append((o, skal))

    print("== SKJUTS UPP (%d av %d) ==" % (len(svara), len(orden)))
    if svara:
        _tagga(svara, "screening fore skrivning", a.torr)
    print("\n== SKRIVS NU (%d) ==" % len(enkla))
    for o, skal in enkla:
        print("  %-24s %s" % (o, skal))
    if a.ut:
        json.dump([{"ord": o} for o, _ in enkla],
                  io.open(a.ut, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("\nSkrev de %d enkla till %s" % (len(enkla), a.ut))


def cmd_tagga(a):
    """Efterat: kort som fastnade anda. Skalet ar obligatoriskt."""
    _tagga([(o, a.skal) for o in a.ord], a.kalla, a.torr)


def cmd_lista(a):
    nids = invoke("findNotes", query='deck:"%s" tag:%s'
                  % (config.DECK_NAME, config.PRIO_TAG_SENARE))
    print("%d noter bar %s" % (len(nids), config.PRIO_TAG_SENARE))
    if not os.path.exists(LOGG):
        print("(%s saknas -- ingen skalhistorik)" % LOGG)
        return
    for rad in io.open(LOGG, encoding="utf-8"):
        d = json.loads(rad)
        print("  %s  %-22s %-28s %s"
              % (d["datum"], d["ord"], d["kalla"], d["skal"]))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--torr", action="store_true", help="visa, skriv inget")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("screena", help="dela en lista i enkla och svara")
    s.add_argument("ord", nargs="*")
    s.add_argument("--fil", help="json med [{'ord': ...}] eller ['ord', ...]")
    s.add_argument("--ut", help="skriv de enkla orden hit")
    s.set_defaults(func=cmd_screena)

    t = sub.add_parser("tagga", help="skjut upp namngivna ord i efterhand")
    t.add_argument("ord", nargs="+")
    t.add_argument("--skal", required=True)
    t.add_argument("--kalla", default="manuell")
    t.set_defaults(func=cmd_tagga)

    l = sub.add_parser("lista", help="vad ligger undanlagt, och varfor")
    l.set_defaults(func=cmd_lista)

    a = p.parse_args()
    a.func(a)
