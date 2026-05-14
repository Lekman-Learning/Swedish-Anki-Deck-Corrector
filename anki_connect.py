import json
import urllib.request
from typing import Any


ANKI_URL = "http://localhost:8765"


def _request(action: str, **params) -> Any:
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request(ANKI_URL, payload)
    resp = json.loads(urllib.request.urlopen(req, timeout=10).read())
    if resp.get("error"):
        raise Exception(f"AnkiConnect: {resp['error']}")
    return resp["result"]


def find_notes(deck_name: str) -> list[int]:
    return _request("findNotes", query=f'deck:"{deck_name}"')


def get_notes_info(note_ids: list[int]) -> list[dict]:
    return _request("notesInfo", notes=note_ids)


def add_tags(note_ids: list[int], tags: str) -> None:
    _request("addTags", notes=note_ids, tags=tags)


def remove_tags(note_ids: list[int], tags: str) -> None:
    _request("removeTags", notes=note_ids, tags=tags)


def get_deck_names() -> list[str]:
    return _request("deckNames")


def update_note_fields(note_id: int, fields: dict) -> None:
    _request("updateNoteFields", note={"id": note_id, "fields": fields})


def create_deck(deck_name: str) -> int:
    return _request("createDeck", deck=deck_name)


def model_names() -> list[str]:
    return _request("modelNames")


def model_field_names(model_name: str) -> list[str]:
    return _request("modelFieldNames", modelName=model_name)


def add_note(deck_name: str, model_name: str, fields: dict, tags: list[str] = None) -> int:
    note = {
        "deckName": deck_name,
        "modelName": model_name,
        "fields": fields,
        "options": {"allowDuplicate": False},
    }
    if tags:
        note["tags"] = tags
    return _request("addNote", note=note)


def ping() -> bool:
    try:
        _request("version")
        return True
    except Exception:
        return False
