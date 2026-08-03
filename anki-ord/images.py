"""Läsa/skriva bilder i Ankis media-mapp via AnkiConnect. Används under Fas 2
för att kritisera befintliga bilder och spara nya (godkända) bilder.
"""

from ankiconnect import invoke


def retrieve_existing(filename):
    """Returnerar base64-data för en bild som redan ligger i Anki-media."""
    return invoke("retrieveMediaFile", filename=filename)


def store_new(filename, base64_data):
    """Sparar en ny bild i Anki-media. Anropas EFTER att Adam godkänt bilden."""
    stored_name = invoke("storeMediaFile", filename=filename, data=base64_data)
    return stored_name


def img_tag(filename):
    return f'<br><br><img src="{filename}" style="max-width:400px; border-radius:4px;">'
