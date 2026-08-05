"""Thin wrapper runt AnkiConnect HTTP API (https://foosoft.net/projects/anki-connect/)."""

import json
import urllib.request

ANKICONNECT_URL = "http://127.0.0.1:8765"


class AnkiConnectError(RuntimeError):
    pass


def invoke(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    request = urllib.request.Request(ANKICONNECT_URL, payload)
    try:
        response = urllib.request.urlopen(request, timeout=60)
    except Exception as exc:
        raise AnkiConnectError(
            f"Kunde inte nå AnkiConnect på {ANKICONNECT_URL}. Är Anki öppen med AnkiConnect-pluginet installerat?"
        ) from exc

    body = json.loads(response.read().decode("utf-8"))
    if len(body) != 2:
        raise AnkiConnectError("Oväntat svar från AnkiConnect (fel antal fält).")
    if body.get("error") is not None:
        raise AnkiConnectError(body["error"])

    result = body["result"]
    # Vissa actions (t.ex. setSpecificValueOfCard) rapporterar fel per post som
    # [bool, felmeddelande] istället för via top-level "error" — utan denna
    # koll ser ett internt misslyckande ut som lyckad invoke().
    if isinstance(result, list) and result and all(
        isinstance(item, list) and len(item) == 2 and isinstance(item[0], bool)
        for item in result
    ):
        failures = [msg for ok, msg in result if not ok]
        if failures:
            raise AnkiConnectError(f"{action} misslyckades för en eller flera poster: {failures}")

    return result
