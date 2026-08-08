"""Delad apply-/tagg-/flagg-/avsuspenderingslogik för flerbetydelse-
granskning (2026-08-07), gemensam för både --mode snabbkoll2 (eskalera
bara vid avvikelse) och --mode sokkoll (riktig sökkoll på varje kort).

Skapades efter att 37 av 50 kort i en testbatch samma dag visade sig
sakna giltigt register trots att baksida.validate_register() redan
fanns -- registerkontrollen görs här till en HÅRD SPÄRR i apply_card()
istället för ett manuellt steg som kan glömmas bort mitt i en stor
batch. apply_batch_unsuspend() gör samma dubbelkontroll direkt mot
Anki innan avsuspendering, eftersom det var precis det steget som
missades i samma testbatch.
"""

import datetime
import json
import os

import baksida
import config
from ankiconnect import invoke

VALID_MODES = ("snabbkoll2", "sokkoll")

# Max antal nid:-led per findCards-fråga, se apply_batch_unsuspend().
NID_QUERY_CHUNK = 500


def _today(today):
    return today or datetime.date.today().isoformat()


def _logga_kalla(note_id, ord_, kalla, today):
    """Skriver ner vilken källa som faktiskt slogs upp, en rad per kort.

    Taggen `flerbetydelse_sokverifierad` säger BARA att en sökkoll gjorts.
    Den säger inte vad som slogs upp, och går därför inte att granska i
    efterhand. Den här filen gör den granskningsbar."""
    rad = {"datum": today, "noteId": note_id, "ord": ord_, "kalla": kalla}
    sokvag = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "sokkoll_kallor.jsonl")
    with open(sokvag, "a", encoding="utf-8") as f:
        f.write(json.dumps(rad, ensure_ascii=False) + "\n")


def _tag_and_flag(note_id, mode, escalated, today, has_old_match=None,
                  kalla=None, ord_=None):
    if mode not in VALID_MODES:
        raise ValueError(f"okänt läge {mode!r}, förväntade ett av {VALID_MODES}")
    if mode == "sokkoll" and not escalated:
        raise AssertionError(
            f"{note_id}: --mode sokkoll kräver escalated=True för varje kort "
            "(riktig sökkoll ska ha körts på det här kortet innan apply)."
        )
    # Flaggregeln nedan har tre utfall, inte två (style_guide.md, "Nytt
    # flagg-system för flerbetydelse-genomgången"). Utan detta krav gick
    # kort UTAN OLD-matchning tyst ut som Gröna, dvs de såg ut att vara
    # jämförda mot ett facit som aldrig fanns (9 kort hittade så
    # 2026-08-07). Kräv därför ett uttryckligt svar istället för en
    # default som kan bli fel.
    escalate = mode == "sokkoll" or escalated
    if not escalate and has_old_match is None:
        raise AssertionError(
            f"{note_id}: has_old_match måste anges för icke-eskalerade kort — "
            "OLD-matchning ger Grön, avsaknad av OLD-matchning ger Gul."
        )
    # Spärr tillkommen 2026-08-08. Bakgrund: 177 kort taggades
    # `flerbetydelse_sokverifierad` efter att bara ha jämförts mot OLD-decket
    # och granskarens egen kunskap. Ingen uppslagning gjordes. Taggen tog
    # granskarens ord för att en sökkoll skett -- samma sorts oskyddat
    # påstående som Adam-tal var innan validate_adamtal() flyttades in i
    # skrivvägen. Kräv därför ett bevis, inte ett intyg.
    if escalate and not kalla:
        raise AssertionError(
            f"{note_id}: sökkoll kräver kalla=... — en URL eller källhänvisning "
            "för det som faktiskt slogs upp. Utan källa sätts ingen "
            "sokverifierad-tagg. Gjordes ingen uppslagning är läget snabbkoll2: "
            "kör med mode='snabbkoll2', escalated=False och has_old_match=True/False."
        )

    today = _today(today)
    invoke("addTags", notes=[note_id], tags=f"{config.FLERBETYDELSE_TAG_PREFIX}::{today}")
    invoke("addTags", notes=[note_id], tags=f"{config.FLERBETYDELSE_SNABBKOLL2_TAG_PREFIX}::{today}")
    if escalate:
        invoke("addTags", notes=[note_id], tags=f"{config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX}::{today}")
        _logga_kalla(note_id, ord_, kalla, today)

    card_ids = invoke("findCards", query=f"nid:{note_id}")
    if escalate:
        flag = config.FLAG_BLA
    else:
        flag = config.FLAG_GRON if has_old_match else config.FLAG_GUL
    for c in card_ids:
        invoke("setSpecificValueOfCard", card=c, keys=["flags"], newValues=[flag], warning_check=True)


def apply_card(note_id, huvudbetydelse, synonymer=None, synonym_groups=None,
                exempelmening="", register=None, bild_html=None,
                mode="snabbkoll2", escalated=False, today=None,
                has_old_match=None, ord_=None, tillat=(), kalla=None):
    """Bygger v2-baksida och skriver den.

    Vägrar (ValueError) skriva ett kort som bryter mot
      * baksida.validate_register()  -- registret är obligatoriskt
      * baksida.validate_adamtal()   -- de HÅRDA Adam-tal-reglerna

    Adam-tal-spärren tillkom 2026-08-07 av samma skäl som register-
    spärren: reglerna fanns i style_guide.md men bara som prosa granskaren
    skulle minnas, och kontrollerades i efterhand av lint_adamtal.py. Ett
    kort som skrivs FEL och upptäcks en vecka senare har Adam redan
    pluggat in. Mjuka anmärkningar returneras istället för att blockera.

    has_old_match: krävs för icke-eskalerade kort, styr Grön/Gul-flaggan.
    ord_:          uppslagsordet, för cirkularitetskontrollerna. Hämtas
                   från Anki om det inte skickas med.
    tillat:        regelnamn som medvetet får brytas, t.ex.
                   tillat=["flera_meningar"] för anafor-kortet.

    Returnerar listan med mjuka anmärkningar (tom = kortet är rent).
    """
    warnings = baksida.validate_register(register)
    if warnings:
        raise ValueError(f"{note_id} ({huvudbetydelse!r}): registret ogiltigt - {warnings}")

    if ord_ is None:
        info = invoke("notesInfo", notes=[note_id])
        ord_ = info[0]["fields"][config.FIELD_ORD]["value"] if info else None

    fel, mjuka = baksida.validate_adamtal(
        huvudbetydelse=huvudbetydelse,
        synonymer=synonymer,
        synonym_groups=synonym_groups,
        exempelmening=exempelmening,
        register=register,
        ord_=ord_,
        tillat=tillat,
    )
    if fel:
        raise ValueError(
            f"{note_id} ({ord_!r}): bryter mot Adam-tal (style_guide.md) - "
            + "; ".join(fel)
            + ". Rätta kortet, eller skicka tillat=[...] om undantaget är motiverat."
        )

    new_baksida = baksida.build(
        huvudbetydelse=huvudbetydelse,
        synonymer=synonymer,
        exempelmening=exempelmening,
        register=register,
        bild_html=bild_html,
        synonym_groups=synonym_groups,
    )
    invoke("updateNoteFields", note={"id": note_id, "fields": {config.FIELD_BAKSIDA: new_baksida}})
    # Kortet ÄR nu v2 -- utan denna tagg blir det osynligt för varje
    # `tag:kortformat::v2`-fråga i projektet (snabbkoll2.py,
    # build_all_v2_snabbkoll_queue.py, find_old_slash_separator.py,
    # find_eller_separator.py, restore_images_from_old_deck.py ...).
    # 26 kort hade hamnat i det hålet innan detta upptäcktes 2026-08-07:
    # de var v2 till innehållet, avsuspenderade och i Adams kö, men syntes
    # inte i någon uppföljande kontroll.
    invoke("addTags", notes=[note_id], tags=config.FORMAT_TAG_V2)
    _tag_and_flag(note_id, mode, escalated, today, has_old_match, kalla, ord_)
    return mjuka


def apply_pass(note_id, mode="snabbkoll2", escalated=False, today=None,
               has_old_match=None, tillat=(), kalla=None):
    """Taggar/flaggar ett kort UTAN att skriva om Baksida (kortet är
    redan korrekt v2-format och behöver inget innehållsbyte). Läser
    kortets NUVARANDE register direkt från Anki och vägrar (ValueError)
    om det inte är giltigt -- använd apply_card() för att rätta det
    innan apply_pass() kan användas."""
    note_info = invoke("notesInfo", notes=[note_id])
    if not note_info:
        raise ValueError(f"hittade inget kort för noteId {note_id}")
    raw = note_info[0]["fields"][config.FIELD_BAKSIDA]["value"]
    ord_ = note_info[0]["fields"][config.FIELD_ORD]["value"]
    parsed = baksida.parse(raw)
    warnings = baksida.validate_register(parsed["register"])
    if warnings:
        raise ValueError(
            f"{note_id}: nuvarande register ogiltigt - {warnings}. "
            "Kortet är inte redo för apply_pass(), använd apply_card() för att rätta det först."
        )
    # apply_pass() betyder "kortet är redan rätt och behöver ingen
    # innehållsändring" -- då måste det också klara Adam-tal, annars är
    # påståendet falskt och kortet godkänns med ett formfel kvar.
    fel, mjuka = baksida.validate_adamtal(
        huvudbetydelse=parsed["huvudbetydelse"],
        synonymer=parsed["synonymer"],
        synonym_groups=parsed["synonym_groups"],
        exempelmening=parsed["exempelmening"],
        register=parsed["register"],
        ord_=ord_,
        tillat=tillat,
    )
    if fel:
        raise ValueError(
            f"{note_id} ({ord_!r}): kortet bryter mot Adam-tal - " + "; ".join(fel)
            + ". Använd apply_card() för att rätta det istället för apply_pass()."
        )
    _tag_and_flag(note_id, mode, escalated, today, has_old_match, kalla, ord_)
    return mjuka


def apply_batch_unsuspend(note_ids):
    """Avsuspenderar bara kort som (a) redan är taggade
    flerbetydelse_granskad och (b) har ett giltigt register just nu i
    Anki -- dubbelkontroll direkt mot livedata, inte mot vad som en
    gång skickades in till apply_card(). Kort som inte klarar kontrollen
    lämnas suspenderade och listas separat."""
    notes_info = invoke("notesInfo", notes=note_ids)
    ready, blocked = [], []
    for n in notes_info:
        tags = n.get("tags", [])
        has_granskad = any(t.startswith(f"{config.FLERBETYDELSE_TAG_PREFIX}::") for t in tags)
        raw = n["fields"][config.FIELD_BAKSIDA]["value"]
        parsed = baksida.parse(raw)
        register_ok = not baksida.validate_register(parsed["register"])
        ord_ = n["fields"][config.FIELD_ORD]["value"]
        if has_granskad and register_ok:
            ready.append(n["noteId"])
        else:
            reason = []
            if not has_granskad:
                reason.append("ej taggad flerbetydelse_granskad")
            if not register_ok:
                reason.append("ogiltigt/saknat register")
            blocked.append((ord_, n["noteId"], ", ".join(reason)))

    if ready:
        # Anki/SQLite spränger uttrycksträdet vid ~1000 OR-led ("Expression
        # tree is too large (maximum depth 1000)"), så en enda OR-kedja över
        # hela batchen kraschar precis när verktyget används som det är tänkt
        # -- CLAUDE.md:s nästa steg är uttryckligen `--batch-size 100+`.
        # Verifierat 2026-08-07: 2356 nid:-led ger exakt det felet.
        card_ids = []
        for i in range(0, len(ready), NID_QUERY_CHUNK):
            chunk = ready[i:i + NID_QUERY_CHUNK]
            card_ids.extend(invoke("findCards", query=" OR ".join(f"nid:{n}" for n in chunk)))
        invoke("unsuspend", cards=card_ids)

    print(f"Avsuspenderade {len(ready)} / {len(note_ids)} kort.")
    if blocked:
        print(f"Kvarlämnade suspenderade ({len(blocked)}), inte redo:")
        for ord_, nid, reason in blocked:
            print(f"  {ord_} ({nid}): {reason}")
    return ready, blocked
