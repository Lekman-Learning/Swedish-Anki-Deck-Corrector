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
import re
import sys

import apply_flerbetydelse as af
import baksida
import config
import sokkoll_verifiering as sv
from ankiconnect import invoke

# Valvet, för raw-websearch/-reserven i sokkoll_verifiering. Transkriptet är
# primärkällan och hittas automatiskt; det här är bara fallback för äldre datum.
VALV_SOKVAG = os.environ.get("STUDY_COACH_VALV", r"c:\Obsidian\Study Coach Ai")

VERIFIERARINSTRUKTION = (
    "BLIND ANDRAGRANSKNING. Du ser ordet, ett facit ur ett fristående deck, och det "
    "färdiga kortet -- avsiktligt INTE hur kortet skrevs, vilka källor som slogs upp "
    "eller vad det stod innan. Döm det på dess egna meriter. SLÅ UPP ORDET SJÄLV i en "
    "riktig ordbok innan du dömer; facit är en andra källa, inte den enda. "
    "Sätt verdikt='godkand' eller 'underkand' + anmarkning för varje post.\n"
    "KONTROLLERA ALLT, i denna ordning:\n"
    "(1) SAKNAS EN HEL BETYDELSE? Det är det vanligaste felet i det här decket, "
    "dominerande i elva granskningsomgångar i rad. Gå igenom ordbokens betydelser en "
    "och en och kryssa av dem mot kortet. Två signaler väger tungt: en synonym som hör "
    "till en betydelse kortet inte nämner, och ett facit med fler betydelser än kortet "
    "(se falt 'facit_signal' -- det är en FRÅGA att avgöra, inte ett konstaterat fel: "
    "facit skiljer ofta synonymer med ';', inte betydelser).\n"
    "(2) Är varje angiven betydelse sakligt korrekt, och leder kortet med den vanligaste?\n"
    "(3) Är betydelserna rätt separerade? ' ; ' mellan GENUINT SKILDA betydelser, "
    "' / ' mellan omformuleringar av SAMMA betydelse. Ordet 'eller' mellan två skilda "
    "betydelser är alltid fel.\n"
    "(4) Är synonymerna faktiskt utbytbara, och är någon cirkulär (innehåller "
    "uppslagsordet eller en böjning av det)? Hör grupperna ihop med rätt betydelse?\n"
    "(5) Illustrerar exempelmeningen rätt betydelse, är den sakligt riktig och "
    "grammatiskt korrekt, och är ordet highlightat?\n"
    "(6) Stämmer registret på BÅDA axlarna -- formalitet och valör?\n"
    "(7) Om kortet har en etymologi: är den sann, OCH gör den betydelsen lättare att "
    "förstå? Trivia som inte hjälper minnet ska bort. Etymologin är valfri -- ett kort "
    "utan den är aldrig ett fel.\n"
    "(8) Går kortet att läsa högt och förstå direkt, utan att slå upp ännu ett ord?\n"
    "Att facit och kortet formulerar sig olika är INTE ett fel -- parafraser är väntade. "
    "Underkänn vid en verklig lucka, ett verkligt sakfel eller ett verkligt formfel."
)

# Loggen som gör oberoendet granskningsbart i efterhand.
#
# Taggen `oberoende_verifierad` säger bara ATT en blind granskning gjorts.
# Den säger inte VEM som gjorde den -- och en tagg som vilar på granskarens
# ord är precis vad `sokverifierad` var innan källspärren: 177 kort bar den
# utan att någon uppslagning skett. Samma medicin här: verdikt() kräver ett
# granskarnamn, vägrar om det är samma som skrev korten, och loggar utfallet.
OBEROENDE_LOGG = "oberoende_granskningar.jsonl"


def _las(sokvag):
    with open(sokvag, encoding="utf-8") as f:
        return json.load(f)


def _skriv(sokvag, data):
    with open(sokvag, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _logga_oberoende(rad):
    sokvag = os.path.join(os.path.dirname(os.path.abspath(__file__)), OBEROENDE_LOGG)
    with open(sokvag, "a", encoding="utf-8") as f:
        f.write(json.dumps(rad, ensure_ascii=False) + "\n")


def _betydelser(text):
    """Antal betydelser i en huvudbetydelse (' ; '-separerad)."""
    return len(baksida.betydelser(text)) or 1


def _facit_betydelser(facit):
    """Grov räkning av betydelser i OLD-facit. OLD skiljer betydelser med ';'
    -- men skiljer OCKSÅ ofta bara synonymer med samma tecken, vilket gav 82
    falsklarm på 116 kandidater 2026-08-07. Siffran är därför en FRÅGA till
    granskaren, aldrig ett konstaterat fel."""
    ren = re.sub(r"<[^>]+>", " ", facit or "")
    delar = [d.strip() for d in ren.split(";") if d.strip()]
    return len(delar)


def _bild(e, p):
    """Bilden, hämtad i tur och ordning ur proposed, postens toppnivå, legacy
    och SIST det kort som faktiskt ligger i Anki.

    Sista ledet tillkom 2026-08-10, efter att tre kort (oknytt, damast, köl)
    förlorat sina bilder i en enda batch. Uppslaget låg på postens toppnivå i
    stället för i `proposed`, och den gamla raden

        p.get("bild_html", (legacy or {}).get("bild_html"))

    tolkade det som "ingen bild" -- alltså RADERA. Det är fel förval: en
    saknad nyckel betyder att ingen uttalat sig om bilden, inte att den ska
    bort. Samma buggklass kostade `faun` sin bild 2026-08-07 och är den enda
    sorten som är osynlig i efterhand, eftersom ett kort utan bild ser precis
    ut som ett kort som aldrig hade någon.

    Vill man verkligen ta bort en bild: skriv `"bild_html": ""` uttryckligen.
    Tom sträng är ett beslut, en saknad nyckel är det inte."""
    for kalla in (p, e, e.get("legacy") or {}):
        if "bild_html" in kalla:
            return kalla["bild_html"]
    try:
        n = invoke("notesInfo", notes=[e["noteId"]])[0]
        return baksida.parse(n["fields"][config.FIELD_BAKSIDA]["value"])["bild_html"]
    except Exception:
        return None


# --------------------------------------------------------------- applicera
def applicera(sokvag, granskare=None):
    poster = _las(sokvag)
    skrivna, hoppade = [], []
    # HÅL 0, tillagt 2026-08-09. Tidigare räckte det att sokkoll-fältet var
    # IFYLLT. Den dagen granskades 141 kort där fältet påstod "svenska.se
    # (SAOL/SO/SAOB) + OLD-facit" på i praktiken alla -- mätt mot loggen hade
    # 11 av 141 en faktisk uppslagning, och spärren släppte igenom allihop.
    # Felet var inte slarv: den som gjorde arbetet skrev också intyget om att
    # arbetet gjorts. Nu måste kalla peka på en hämtning som finns i Claude
    # Codes transkript -- ett vittne granskaren inte kan skriva i.
    bevis = sv.samla_bevis(VALV_SOKVAG)
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
        giltig, motiv = sv.granska_kalla(sok.get("kalla"), bevis)
        if not giltig:
            hoppade.append((e["ord"], f"SÖKKOLL EJ BEVISAD: {motiv}"))
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
                etymologi=p.get("etymologi"),
                bild_html=_bild(e, p),
                mode="sokkoll", escalated=True,
                # kalla= är OBLIGATORISK sedan källspärren 2026-08-08. Utan
                # den kastar apply_card() AssertionError för VARJE kort, och
                # hela dagsbatchen hade tyst hamnat i "hoppade" (hittat
                # 2026-08-08 -- spärren skrevs utan att den här anroparen
                # uppdaterades). Fältet är redan kontrollerat som ifyllt ovan.
                kalla=sok["kalla"],
                ord_=e["ord"], tillat=e.get("tillat", ()),
            )
            e["adamtal_varningar"] = mjuka
            e["applicerad"] = True
            # Vem som SKREV kortet. verdikt() vägrar godkänna av samma namn --
            # det är så "oberoende" blir kontrollerbart i stället för påstått.
            e["skriven_av"] = granskare
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
        facit = e.get("old_facit")
        n_kort, n_facit = _betydelser(p["huvudbetydelse"]), _facit_betydelser(facit)
        ut.append({
            "noteId": e["noteId"],
            "ord": n["fields"][config.FIELD_ORD]["value"],
            "facit": facit,
            # Mekanisk signal, härledd ur facit + färdigt kort -- alltså ur
            # sådant granskaren ändå ser. Läcker ingenting om hur kortet blev
            # till. Samma svepning hittade 34 äkta luckor 2026-08-07.
            "facit_signal": (
                f"facit antyder {n_facit} betydelse(r), kortet har {n_kort} "
                "-- avgör om någon saknas"
                if facit and n_facit > n_kort else None
            ),
            "kort": {
                "huvudbetydelse": p["huvudbetydelse"],
                "register": p["register"],
                "synonymer": p["synonymer"],
                "synonym_groups": p["synonym_groups"],
                "exempelmening": p["exempelmening"],
                "etymologi": p["etymologi"],
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
    # skriven_av ligger UTANFÖR "poster": verdikt() behöver den för att kunna
    # vägra självgranskning, men granskaren ska döma korten, inte författaren.
    _skriv(mal, {
        "instruktion": VERIFIERARINSTRUKTION,
        "skriven_av": next((e.get("skriven_av") for e in poster if e.get("skriven_av")), None),
        "granskare": None,   # fylls av den blinda granskaren, obligatoriskt
        "poster": ut,
    })
    med_signal = sum(1 for u in ut if u["facit_signal"])
    print(f"Skrev {len(ut)} blinda verifieringsposter till {mal}")
    print(f"  varav {med_signal} där facit antyder fler betydelser än kortet har")
    print("Låt en FRISTÅENDE granskare (ny session/agent, som INTE skrev korten)")
    print("fylla i 'granskare' överst plus verdikt/anmarkning per post.")
    print(f"Kör sedan: python kortgranskare.py verdikt {mal}")
    return mal


# ------------------------------------------------------------------ verdikt
def verdikt(paketsokvag, granskare=None):
    data = _las(paketsokvag)
    poster = data["poster"] if isinstance(data, dict) else data
    meta = data if isinstance(data, dict) else {}

    # --- Oberoendespärren ---------------------------------------------
    # Utan den vilar `oberoende_verifierad` på granskarens ord, precis som
    # `sokverifierad` gjorde innan källspärren -- och den taggen satt på 177
    # kort som aldrig sökkollats. En spärr som bara gäller när man råkar
    # tänka på den är ingen spärr.
    gr = granskare or meta.get("granskare")
    if not gr:
        print("AVBRYTER: granskare saknas. Ange vem som gjorde den blinda "
              "granskningen -- fältet 'granskare' i paketfilen eller --granskare. "
              "Taggen oberoende_verifierad får inte sättas anonymt.")
        return
    skrivare = meta.get("skriven_av")
    if skrivare and gr.strip().lower() == skrivare.strip().lower():
        print(f"AVBRYTER: {gr!r} skrev korten och kan inte blindgranska dem.\n"
              "  Hela poängen med steget är att en granskare som kontrollerar sitt\n"
              "  EGET arbete bekräftar sig själv (34 kort med saknad betydelse hittades\n"
              "  2026-08-07 i material som passerat både snabbkoll OCH sökverifiering).\n"
              "  Kör steget i en ny session eller med en separat agent.")
        return

    saknar = [p["ord"] for p in poster if p.get("verdikt") not in ("godkand", "underkand")]
    if saknar:
        print(f"AVBRYTER: {len(saknar)} poster saknar verdikt ({', '.join(saknar[:8])} ...)")
        return
    # Ett underkännande utan motivering går inte att åtgärda, och ett godkännande
    # av ett kort där facit_signal aldrig besvarades är inte en genomförd kontroll.
    obesvarade = [p["ord"] for p in poster
                  if p["verdikt"] == "underkand" and not (p.get("anmarkning") or "").strip()]
    if obesvarade:
        print(f"AVBRYTER: {len(obesvarade)} underkända saknar anmärkning "
              f"({', '.join(obesvarade[:8])}) -- skriv VAD som är fel.")
        return

    godkanda = [p for p in poster if p["verdikt"] == "godkand"]
    underkanda = [p for p in poster if p["verdikt"] == "underkand"]
    idag = __import__("datetime").date.today().isoformat()
    for p in godkanda:
        invoke("addTags", notes=[p["noteId"]],
               tags=f"{config.OBEROENDE_TAG_PREFIX}::{idag}")
        _logga_oberoende({
            "datum": idag, "noteId": p["noteId"], "ord": p["ord"],
            "granskare": gr, "skriven_av": skrivare,
            "verdikt": "godkand", "anmarkning": p.get("anmarkning"),
        })
    for p in underkanda:
        _logga_oberoende({
            "datum": idag, "noteId": p["noteId"], "ord": p["ord"],
            "granskare": gr, "skriven_av": skrivare,
            "verdikt": "underkand", "anmarkning": p.get("anmarkning"),
        })
    print(f"Blind granskare        : {gr}   (kortskrivare: {skrivare or 'okänd'})")
    print(f"Godkända (taggade {config.OBEROENDE_TAG_PREFIX}::{idag}): {len(godkanda)}")
    print(f"UNDERKÄNDA -- rättas och köres om, släpps inte: {len(underkanda)}")
    for p in underkanda:
        print(f"  {p['ord']}: {p.get('anmarkning')}")
    print(f"\nLoggat till {OBEROENDE_LOGG} -- utfallet går att granska i efterhand.")


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
                register=p["register"], ord_=ord_, etymologi=p["etymologi"])
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
    blind = len(invoke("findNotes",
                       query=f'deck:"{config.DECK_NAME}" tag:{config.OBEROENDE_TAG_PREFIX}::*')) if ids else 0
    print(f"Kort i batchen        : {len(poster)}")
    print(f"  granskade+godkända  : {sum(1 for e in poster if e.get('approved'))}")
    print(f"  med sökkoll ifylld  : {sum(1 for e in poster if (e.get('sokkoll') or {}).get('kalla'))}")
    print(f"  applicerade         : {len(ids)}")
    print(f"  släppbara nu        : {len(redo)}")
    print(f"  blockerade          : {len(blockerade)}")
    print(f"blindverifierade i hela decket: {blind}")
    if not blind:
        print("  OBS: 0 -- den blinda andragranskningen har aldrig körts. Inget kort")
        print("  kan släppas förrän den gör det (config.SLAPP_KRAVER_TAGGAR).")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("steg", choices=["applicera", "paket", "verdikt", "slapp", "status"])
    p.add_argument("fil")
    p.add_argument("--torr", action="store_true", help="slapp: visa utan att avsuspendera")
    p.add_argument("--granskare", default=None,
                   help="applicera: vem som SKREV korten. verdikt: vem som "
                        "blindgranskade dem. Måste skilja sig åt.")
    a = p.parse_args()
    if not os.path.exists(a.fil):
        sys.exit(f"Hittar inte {a.fil}")
    {"applicera": lambda: applicera(a.fil, a.granskare), "paket": lambda: paket(a.fil),
     "verdikt": lambda: verdikt(a.fil, a.granskare), "slapp": lambda: slapp(a.fil, a.torr),
     "status": lambda: status(a.fil)}[a.steg]()


if __name__ == "__main__":
    main()
