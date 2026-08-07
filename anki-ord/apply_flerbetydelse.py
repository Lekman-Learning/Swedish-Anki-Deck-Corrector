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

import baksida
import config
from ankiconnect import invoke

VALID_MODES = ("snabbkoll2", "sokkoll")


def _today(today):
    return today or datetime.date.today().isoformat()


def _tag_and_flag(note_id, mode, escalated, today):
    if mode not in VALID_MODES:
        raise ValueError(f"okänt läge {mode!r}, förväntade ett av {VALID_MODES}")
    if mode == "sokkoll" and not escalated:
        raise AssertionError(
            f"{note_id}: --mode sokkoll kräver escalated=True för varje kort "
            "(riktig sökkoll ska ha körts på det här kortet innan apply)."
        )

    today = _today(today)
    invoke("addTags", notes=[note_id], tags=f"{config.FLERBETYDELSE_TAG_PREFIX}::{today}")
    invoke("addTags", notes=[note_id], tags=f"{config.FLERBETYDELSE_SNABBKOLL2_TAG_PREFIX}::{today}")
    if mode == "sokkoll" or escalated:
        invoke("addTags", notes=[note_id], tags=f"{config.FLERBETYDELSE_SOKVERIFIERAD_TAG_PREFIX}::{today}")

    card_ids = invoke("findCards", query=f"nid:{note_id}")
    flag = config.FLAG_BLA if (mode == "sokkoll" or escalated) else config.FLAG_GRON
    for c in card_ids:
        invoke("setSpecificValueOfCard", card=c, keys=["flags"], newValues=[flag], warning_check=True)


def apply_card(note_id, huvudbetydelse, synonymer=None, synonym_groups=None,
                exempelmening="", register=None, bild_html=None,
                mode="snabbkoll2", escalated=False, today=None):
    """Bygger v2-baksida och skriver den. Vägrar (ValueError) om
    registret är ogiltigt enligt baksida.validate_register() -- se
    style_guide.md, registret är obligatoriskt, aldrig valfritt."""
    warnings = baksida.validate_register(register)
    if warnings:
        raise ValueError(f"{note_id} ({huvudbetydelse!r}): registret ogiltigt - {warnings}")

    new_baksida = baksida.build(
        huvudbetydelse=huvudbetydelse,
        synonymer=synonymer,
        exempelmening=exempelmening,
        register=register,
        bild_html=bild_html,
        synonym_groups=synonym_groups,
    )
    invoke("updateNoteFields", note={"id": note_id, "fields": {config.FIELD_BAKSIDA: new_baksida}})
    _tag_and_flag(note_id, mode, escalated, today)


def apply_pass(note_id, mode="snabbkoll2", escalated=False, today=None):
    """Taggar/flaggar ett kort UTAN att skriva om Baksida (kortet är
    redan korrekt v2-format och behöver inget innehållsbyte). Läser
    kortets NUVARANDE register direkt från Anki och vägrar (ValueError)
    om det inte är giltigt -- använd apply_card() för att rätta det
    innan apply_pass() kan användas."""
    note_info = invoke("notesInfo", notes=[note_id])
    if not note_info:
        raise ValueError(f"hittade inget kort för noteId {note_id}")
    raw = note_info[0]["fields"][config.FIELD_BAKSIDA]["value"]
    parsed = baksida.parse(raw)
    warnings = baksida.validate_register(parsed["register"])
    if warnings:
        raise ValueError(
            f"{note_id}: nuvarande register ogiltigt - {warnings}. "
            "Kortet är inte redo för apply_pass(), använd apply_card() för att rätta det först."
        )
    _tag_and_flag(note_id, mode, escalated, today)


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
        card_ids = invoke("findCards", query=" OR ".join(f"nid:{n}" for n in ready))
        invoke("unsuspend", cards=card_ids)

    print(f"Avsuspenderade {len(ready)} / {len(note_ids)} kort.")
    if blocked:
        print(f"Kvarlämnade suspenderade ({len(blocked)}), inte redo:")
        for ord_, nid, reason in blocked:
            print(f"  {ord_} ({nid}): {reason}")
    return ready, blocked
