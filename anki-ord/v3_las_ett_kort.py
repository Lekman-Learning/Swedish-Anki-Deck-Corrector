# -*- coding: utf-8 -*-
"""Läser ett kort + facit ur OLD för v3-granskning. Argument: uppslagsordet."""
import re
import sys

from ankiconnect import invoke
import config


def strip(h):
    h = re.sub(r"<br\s*/?>", " ~ ", h)
    h = re.sub(r"<[^>]+>", "", h).replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", h).strip()


def main():
    ord_ = sys.argv[1]
    nids = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" "Framsida:{ord_}"')
    if not nids:
        print("HITTADE INGEN NOT")
        return
    n = invoke("notesInfo", notes=nids)[0]
    print("FRAMSIDA:", strip(n["fields"]["Framsida"]["value"]))
    print("BAKSIDA :", strip(n["fields"]["Baksida"]["value"]))
    print("TAGGAR  :", ", ".join(n["tags"]))
    cids = invoke("findCards", query=f'deck:"{config.DECK_NAME}" "Framsida:{ord_}"')
    ci = invoke("cardsInfo", cards=cids)
    print("FLAGGA  :", [c["flags"] for c in ci], " KO:", [c["queue"] for c in ci])

    o = invoke("findNotes",
               query=f'deck:"Humanities::Languages::Svenska OLD" "Framsida:{ord_}"')
    if o:
        print("FACIT   :", strip(invoke("notesInfo", notes=[o[0]])[0]["fields"]["Baksida"]["value"]))
    else:
        print("FACIT   : INGET FACIT")


if __name__ == "__main__":
    main()
