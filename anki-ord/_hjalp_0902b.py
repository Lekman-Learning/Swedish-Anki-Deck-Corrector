# -*- coding: utf-8 -*-
"""Delade hjalpare for arbetsbatchen 2026-09-02b.

Finns for att de tre fel som kostade mest i formiddagens batch alla var
MEKANISKA och alltsa gar att stanga i kod i stallet for att komma ihag:

  1. synonymer tagna ur minnet i stallet for ur forgranskas godkanda pool
     -> synpool() ger poolen, och den ar enda kallan kort far valja ur
  2. definitionsartade synonymer ("som bildats ur material fran platsen")
     -> ren() slanger allt med >=4 ord eller " som "
  3. ASCII-translittererad svenska i etymologierna
     -> etym() tar SO:s egen strang ordagrant, sa den kan inte bli fel

Poolen ar dessutom skral i sig: den innehaller SO:s definitionsfragment,
sa "stor" och "ett" dyker upp som "synonymer". Darfor filtreras aven
enordiga fragment som bara ar en avhuggen bit av definitionen bort.
"""
import io, json, os, re, sys
import forgranska as F

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

H = '<font color="#3498db">%s</font>'

# Fragment som SO:s def-parsning lamnar efter sig. De ar inte synonymer.
SKRAP = {
    "som", "det", "en", "ett", "med", "om", "fa", "få", "gora", "göra",
    "lata", "låta", "i", "av", "till", "for", "för", "spec", "bildl",
    "allmannare", "allmännare", "typ", "sarsk", "särsk", "aven", "även",
    "plural", "best", "form", "moment", "drag", "stor", "stort", "liten",
    "svag", "psykiskt", "juridisk", "formell", "vilseledande", "hett",
    "grundlaggande", "grundläggande", "oerhort", "oerhört", "relativt",
    "noggrant", "skriftligt", "fullstandigt", "fullständigt", "lang",
    "sprakl", "språklig", "utmarkande", "utmärkande", "beskyddande",
    "vetenskapligt", "toppig", "kagelformad", "kägelformad", "praktfullt",
    "instruktionsfoljd", "instruktionsföljd", "formforandring",
    "formförändring", "formforandrande", "formförändrande", "period",
    "anordning", "ord", "ljud", "late", "läte", "lara", "läran",
    "vetenskapen", "person", "forbindelse", "förbindelse", "chokladmassa",
    "inflammation", "sittstang", "sittstång", "grupp", "jordart", "bank",
    "punkt", "kvarleva", "gammal", "frukt", "mottagnings", "pasronlika",
    "päronlika", "hog", "hög", "brunsvart", "kortsvansat", "djup",
    "forsjunkande", "försjunkande", "forsjunkenhet", "försjunkenhet",
    "menig", "ohyfsad", "meddelande", "hemlig", "bildande", "uppvuxen",
    "inhemsk_frag", "promenera", "suga", "rymma", "skara", "skära",
    "klyvning", "uppdelning", "notning", "nötning", "metallforstoring",
    "metallförstöring", "ur", "vag", "väg", "mat", "foretielse",
    "foreteelse", "företeelse", "del", "ljus", "omrade", "område",
    "antyda", "mena", "tecken", "tecknet",
}


def ren(kandidater):
    """Slanger definitionsartade och fragmentariska poster.

    >=4 ord eller " som " => det ar en definition, inte en synonym. Regeln
    ar densamma som formiddagens batch fick tillampad i efterhand pa tio
    kort (fiskal, falang, garva ...); har ligger den fore i stallet.
    """
    ut = []
    for s in kandidater:
        s = (s or "").strip()
        if not s or s in ut:
            continue
        if len(s.split()) >= 4 or " som " in s:
            continue
        if s.lower() in SKRAP:
            continue
        ut.append(s)
    return ut


def _u(o):
    f = os.path.join("uppslag", o + ".json")
    return json.load(io.open(f, encoding="utf-8")) if os.path.exists(f) else None


def synpool(o):
    """Exakt de synonymer forgranska godtar, minus skrap och definitioner."""
    u = _u(o)
    if not u:
        return []
    b = F._ordboksbelagg(u, o)
    if not isinstance(b, (set, frozenset, list, tuple)):
        return []
    return ren(sorted(str(x) for x in b))


def etym(o):
    """SO:s egen etymologistrang, ordagrant. Kopieras aldrig for hand."""
    u = _u(o)
    if not u:
        return None
    so = ((u.get("sammandrag") or {}).get("svenska_se") or {}).get("so") or {}
    rader = so.get("etymologi") or []
    return rader[0] if rader else None


def kallor(o):
    """URLerna ur uppslaget, sa de inte kan skrivas fel."""
    u = _u(o)
    return dict((u or {}).get("urler") or {})


def visa(orden):
    for o in orden:
        print("%-22s POOL: %s" % (o, ", ".join(synpool(o)) or "-- TOM --"))
        e = etym(o)
        if e:
            print("%-22s ETYM: %s" % ("", e[:150]))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--fil":
        poster = json.load(io.open(sys.argv[2], encoding="utf-8"))
        visa([e["ord"] for e in poster])
    else:
        visa(sys.argv[1:])
