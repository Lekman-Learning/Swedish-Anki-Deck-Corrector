"""Kortgranskare v3.0 -- skriver, blindverifierar och släpper dagsbatchen.

Fyra steg, i ordning. Inget steg går att hoppa över, för varje steg
kontrollerar mekaniskt att det föregående faktiskt är gjort:

    python kortgranskare.py applicera sessions/session_<dat>_v3-batch.json
    python kortgranskare.py paket     sessions/session_<dat>_v3-batch.json
    (en FRISTÅENDE granskare fyller i verdikt i paketfilen)
    python kortgranskare.py verdikt   sessions/session_<dat>_v3-paket.json
    python kortgranskare.py slapp     sessions/session_<dat>_v3-batch.json

## Varför "paket" är ett eget steg

Det här är hela poängen med v3. En granskare som kontrollerar sitt EGET
arbete i samma sittning bekräftar sig själv -- style_guide.md noterade
risken redan om snabbkoll 2.0 ("samma granskare ... i samma sittning"),
och den visade sig befogad: 2026-08-07 hittades 34 kort med en saknad
betydelse i material som passerat BÅDE snabbkoll OCH sökverifiering.

`paket` skriver därför en fil som innehåller ENDAST uppslagsordet,
OLD-facit och det färdiga kortet. Den innehåller medvetet INTE
riskflaggorna, sökkollsanteckningarna, det gamla innehållet eller något
annat som avslöjar hur kortet blev till. En granskare som läser paketet
kan bara döma kortet på dess egna meriter mot en källa -- vilket är det
enda som gör verifieringen värd något.

## Släppspärren

`slapp` avsuspenderar bara kort som har alla taggar i
config.SLAPP_KRAVER_TAGGAR OCH klarar register + Adam-tal kontrollerat
mot LIVE-innehållet i Anki, inte mot vad som en gång skickades in.
Det är skillnaden mot tidigare: "granskat" var ett påstående i en logg,
nu är det ett villkor maskinen vägrar släppa igenom utan.
"""

import argparse
import json
import os
import sys

import apply_flerbetydelse as af
import baksida
import config
from ankiconnect import invoke

VERIFIERARINSTRUKTION = (
    "BLIND ANDRAGRANSKNING. Du ser ordet, ett facit ur ett fristående deck, och det "
    "färdiga kortet -- avsiktligt INTE hur kortet skrevs. Döm det på dess egna meriter. "
    "Sätt verdikt='godkand' eller 'underkand' + anmarkning för varje post. Kontrollera: "
    "(1) Är huvudbetydelsen sakligt korrekt? (2) SAKNAS EN HEL BETYDELSE? -- det är det "
    "vanligaste felet i det här decket, dominerande i åtta granskningsomgångar i rad; "
    "kolla särskilt om någon synonym hör till en betydelse som inte nämns. (3) Passar "
    "synonymerna den angivna betydelsen, och är någon cirkulär? (4) Illustrerar "
    "exempelmeningen rätt betydelse, och är den sakligt riktig? (5) Stämmer registret? "
    "Att facit och kortet formulerar sig olika är INTE ett fel -- parafraser är väntade. "
    "Underkänn bara vid ett verkligt sakfel eller en verklig lucka."
)


def _las(sokvag):
    with open(sokvag, encoding="utf-8") as f:
        return json.load(f)


def _skriv(sokvag, data):
    with open(sokvag, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# --------------------------------------------------------------- applicera
def applicera(sokvag):
    poster = _las(sokvag)
    skrivna, hoppade = [], []
    for e in poster:
        if not e.get("approved") or not e.get("proposed"):
            hoppade.append((e["ord"], "ej granskad/godkänd än"))
            continue
        # Sökkollen är obligatorisk i v3 och kontrolleras här -- ett tomt
        # fält betyder att steget inte gjordes, oavsett vad loggen säger.
        sok = e.get("sokkoll") or {}
        if not (sok.get("kalla") and sok.get("slutsats")):
            hoppade.append((e["ord"], "sokkoll saknas (kalla+slutsats krävs)"))
            continue
        p = e["proposed"]
        try:
            # Varje kort har fått en riktig sökkoll -> eskalerat -> Blå.
            # has_old_match behövs inte på den vägen.
            mjuka = af.apply_card(
                note_id=e["noteId"],
                huvudbetydelse=p["huvudbetydelse"],
                synonymer=p.get("synonymer"),
                synonym_groups=p.get("synonym_groups"),
                exempelmening=p.get("exempelmening", ""),
                register=p.get("register"),
                bild_html=p.get("bild_html", (e.get("legacy") or {}).get("bild_html")),
                mode="sokkoll", escalated=True,
                ord_=e["ord"], tillat=e.get("tillat", ()),
            )
            e["adamtal_varningar"] = mjuka
            e["applicerad"] = True
            skrivna.append(e["ord"])
        except Exception as exc:
            hoppade.append((e["ord"], str(exc)[:120]))
    _skriv(sokvag, poster)
    print(f"Skrivna: {len(skrivna)}   Hoppade över: {len(hoppade)}")
    for o, r in hoppade[:25]:
        print(f"  SKIP {o}: {r}")
    return skrivna, hoppade


# -------------------------------------------------------------------- paket
def paket(sokvag):
    """Blind verifieringsfil. Tar med ENDAST ord, facit och färdigt kort."""
    poster = [e for e in _las(sokvag) if e.get("applicerad")]
    if not poster:
        print("Inga applicerade kort -- kör 'applicera' först.")
        return None
    ut = []
    for e in poster:
        n = invoke("notesInfo", notes=[e["noteId"]])[0]
        p = baksida.parse(n["fields"][config.FIELD_BAKSIDA]["value"])
        ut.append({
            "noteId": e["noteId"],
            "ord": n["fields"][config.FIELD_ORD]["value"],
            "facit": e.get("old_facit"),
            "kort": {
                "huvudbetydelse": p["huvudbetydelse"],
                "register": p["register"],
                "synonymer": p["synonymer"],
                "synonym_groups": p["synonym_groups"],
                "exempelmening": p["exempelmening"],
            },
            "verdikt": None,
            "anmarkning": None,
        })
    # Målnamnet MÅSTE skilja sig från indatafilen. Utan den här kontrollen
    # blev målet identiskt med källan för varje fil som inte råkade heta
    # "_v3-batch" -- och paketet hade då skrivit över den granskade
    # sessionsfilen med all sökkoll i (hittat vid egengranskning 2026-08-07).
    stam = os.path.splitext(sokvag)[0]
    mal = None
    for kalla in ("_v3-batch", "_v3-omgranskning"):
        if kalla in stam:
            mal = f"{stam.replace(kalla, '_v3-paket')}.json"
            break
    if mal is None:
        mal = f"{stam}_v3-paket.json"
    if os.path.abspath(mal) == os.path.abspath(sokvag):  # bältet och hängslena
        raise RuntimeError(f"vägrar skriva paketet över indatafilen {sokvag}")
    _skriv(mal, {"instruktion": VERIFIERARINSTRUKTION, "poster": ut})
    print(f"Skrev {len(ut)} blinda verifieringsposter till {mal}")
    print("Låt en FRISTÅENDE granskare fylla i verdikt/anmarkning, kör sedan 'verdikt'.")
    return mal


# ------------------------------------------------------------------ verdikt
def verdikt(paketsokvag):
    data = _las(paketsokvag)
    poster = data["poster"] if isinstance(data, dict) else data
    saknar = [p["ord"] for p in poster if p.get("verdikt") not in ("godkand", "underkand")]
    if saknar:
        print(f"AVBRYTER: {len(saknar)} poster saknar verdikt ({', '.join(saknar[:8])} ...)")
        return
    godkanda = [p for p in poster if p["verdikt"] == "godkand"]
    underkanda = [p for p in poster if p["verdikt"] == "underkand"]
    idag = __import__("datetime").date.today().isoformat()
    for p in godkanda:
        invoke("addTags", notes=[p["noteId"]],
               tags=f"{config.OBEROENDE_TAG_PREFIX}::{idag}")
    print(f"Godkända (taggade {config.OBEROENDE_TAG_PREFIX}::{idag}): {len(godkanda)}")
    print(f"UNDERKÄNDA -- rättas och köres om, släpps inte: {len(underkanda)}")
    for p in underkanda:
        print(f"  {p['ord']}: {p.get('anmarkning')}")


# -------------------------------------------------------------------- slapp
def kontrollera_slappbar(note_ids):
    """Kontrollerar taggar OCH live-innehåll. Returnerar (redo, blockerade)."""
    info = []
    for i in range(0, len(note_ids), 500):
        info.extend(invoke("notesInfo", notes=note_ids[i:i + 500]))
    redo, blockerade = [], []
    for n in info:
        ord_ = n["fields"][config.FIELD_ORD]["value"]
        taggar = n.get("tags", [])
        skal = []
        for krav in config.SLAPP_KRAVER_TAGGAR:
            if not any(t == krav or t.startswith(f"{krav}::") for t in taggar):
                skal.append(f"saknar {krav}")
        p = baksida.parse(n["fields"][config.FIELD_BAKSIDA]["value"])
        if not p["huvudbetydelse"]:
            skal.append("ej v2-format")
        else:
            skal += baksida.validate_register(p["register"])
            fel, _ = baksida.validate_adamtal(
                huvudbetydelse=p["huvudbetydelse"], synonymer=p["synonymer"],
                synonym_groups=p["synonym_groups"], exempelmening=p["exempelmening"],
                register=p["register"], ord_=ord_)
            skal += fel
        (redo if not skal else blockerade).append(
            n["noteId"] if not skal else (ord_, n["noteId"], "; ".join(skal))
        )
    return redo, blockerade


def slapp(sokvag, torr=False):
    poster = _las(sokvag)
    ids = [e["noteId"] for e in poster if e.get("applicerad")]
    if not ids:
        print("Inga applicerade kort i filen.")
        return
    # Spår B-kort ligger redan i Adams kö. Avsuspendering är då en no-op,
    # men rapporten får inte påstå att de "släpptes in" -- det som händer
    # är att de blir godkända, inte att de blir synliga.
    omgranskning = any(e.get("redan_i_kon") for e in poster)
    redo, blockerade = kontrollera_slappbar(ids)
    etikett = "Godkända" if omgranskning else "Redo att släppas"
    print(f"{etikett:<17}: {len(redo)} av {len(ids)}")
    print(f"Blockerade       : {len(blockerade)}")
    for o, _, skal in blockerade[:25]:
        print(f"  {'EJ GODKÄNT' if omgranskning else 'HÅLLS KVAR'} {o}: {skal}")
    if omgranskning and blockerade:
        print("\n  VARNING: dessa kort ligger REDAN i Adams kö och pluggas nu, "
              "trots att de inte klarar kontrollen. Rätta dem, suspendera dem "
              "manuellt, eller acceptera medvetet.")
    if torr:
        print("\n(torrkörning -- ingenting ändrades)")
        return
    if redo and not omgranskning:
        kort = []
        for i in range(0, len(redo), af.NID_QUERY_CHUNK):
            bit = redo[i:i + af.NID_QUERY_CHUNK]
            kort.extend(invoke("findCards", query=" OR ".join(f"nid:{n}" for n in bit)))
        invoke("unsuspend", cards=kort)
        print(f"\nAvsuspenderade {len(redo)} kort -- dessa är nu i Adams kö.")
    elif omgranskning:
        print(f"\n{len(redo)} omgranskade kort är nu blindverifierade "
              f"(låg redan i kön, inget avsuspenderades).")


# ------------------------------------------------------------------- status
def status(sokvag):
    poster = _las(sokvag)
    ids = [e["noteId"] for e in poster if e.get("applicerad")]
    redo, blockerade = kontrollera_slappbar(ids) if ids else ([], [])
    print(f"Kort i batchen        : {len(poster)}")
    print(f"  granskade+godkända  : {sum(1 for e in poster if e.get('approved'))}")
    print(f"  med sökkoll ifylld  : {sum(1 for e in poster if (e.get('sokkoll') or {}).get('kalla'))}")
    print(f"  applicerade         : {len(ids)}")
    print(f"  släppbara nu        : {len(redo)}")
    print(f"  blockerade          : {len(blockerade)}")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("steg", choices=["applicera", "paket", "verdikt", "slapp", "status"])
    p.add_argument("fil")
    p.add_argument("--torr", action="store_true", help="slapp: visa utan att avsuspendera")
    a = p.parse_args()
    if not os.path.exists(a.fil):
        sys.exit(f"Hittar inte {a.fil}")
    {"applicera": lambda: applicera(a.fil), "paket": lambda: paket(a.fil),
     "verdikt": lambda: verdikt(a.fil), "slapp": lambda: slapp(a.fil, a.torr),
     "status": lambda: status(a.fil)}[a.steg]()


if __name__ == "__main__":
    main()
