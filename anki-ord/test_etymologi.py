# -*- coding: utf-8 -*-
"""Verifierar etymologiraden (Adams krav 2026-08-08).

Det som MÅSTE hålla:
  1. build->parse ger tillbaka etymologin, med och utan bild.
  2. Etymologin hamnar EFTER exempelmeningen och FÖRE bilden, med samma
     <br><br>-lucka som mellan de övriga blocken.
  3. Kort UTAN etymologi parsas exakt som förut -- annars hade tillägget
     tyst ändrat innehållet på 3200+ befintliga kort vid nästa omskrivning.
  4. En parse->build-runda över hela det riktiga decket är identisk.

Punkt 3 och 4 är den viktiga delen. Samma buggklass (parse tappar ett
fält -> nästa build raderar det) kostade "faun" sin bild 2026-08-07.
"""
import re

import baksida
import config
from ankiconnect import invoke

B = '<font color="#3498db">%s</font>'
ETY = "Av grekiskans aisthesis, ”sinnesintryck”."
# Etymologin LAGRAS som ren text men RENDERAS grå med pil (2026-08-10, Adams
# val). Testet kontrollerar därför två saker som är lätta att blanda ihop:
# att modellen bär ren text, och att HTML:en bär wrappern.
ETY_HTML = f'<font color="{config.ETYMOLOGI_COLOR}">{config.ETYMOLOGI_PIL} {ETY}</font>'
BILD = '<br><br><img src="x.jpg" style="max-width:400px; border-radius:4px;">'


def _bygg(**extra):
    return baksida.build(
        huvudbetydelse="Läran om det sköna",
        register="formell",
        synonymer=["skönhetslära", "konstfilosofi"],
        exempelmening=f"Hans {B % 'estetik'} genomsyrade hela utställningen.",
        **extra,
    )


def main():
    fel = []

    # 1+2 -- etymologi utan bild
    html = _bygg(etymologi=ETY)
    p = baksida.parse(html)
    if p["etymologi"] != ETY:
        fel.append(f"1. etymologi kom inte tillbaka: {p['etymologi']!r}")
    if not re.search(r"</i><br><br>" + re.escape(ETY_HTML) + r"$", html):
        fel.append(f"2. fel placering/lucka: ...{html[-90:]!r}")

    # 1+2 -- etymologi MED bild: etymologin före bilden, båda intakta
    html_b = _bygg(etymologi=ETY, bild_html=BILD)
    p_b = baksida.parse(html_b)
    if p_b["etymologi"] != ETY:
        fel.append(f"1b. etymologi tappad när bild finns: {p_b['etymologi']!r}")
    if p_b["bild_html"] != BILD:
        fel.append(f"1c. bild tappad när etymologi finns: {p_b['bild_html']!r}")
    if html_b.index(ETY) > html_b.index("<img"):
        fel.append("2b. etymologin hamnade EFTER bilden")

    # 3 -- kort utan etymologi ska vara oförändrade
    utan = _bygg()
    if baksida.parse(utan)["etymologi"] is not None:
        fel.append("3. kort utan etymologi fick ett värde")
    if baksida.build(**{k: v for k, v in baksida.parse(utan).items()
                        if k != "etymologi"}) != utan:
        fel.append("3b. gammal anropsform (utan etymologi) ger inte samma HTML")

    # Mjuk längdregel varnar men blockerar aldrig
    _, mjuka = baksida.validate_adamtal(
        huvudbetydelse="Läran om det sköna", synonymer=["skönhetslära"],
        exempelmening=f"Hans {B % 'estetik'} var slående.", register="formell",
        etymologi=" ".join(["ord"] * (baksida.ETYMOLOGI_MAX_ORD + 1)))
    if not any(m.startswith("etymologi_langd") for m in mjuka):
        fel.append("4a. lång etymologi gav ingen varning")
    hard, _ = baksida.validate_adamtal(
        huvudbetydelse="Läran om det sköna", synonymer=["skönhetslära"],
        exempelmening=f"Hans {B % 'estetik'} var slående.", register="formell",
        etymologi=" ".join(["ord"] * 50))
    if hard:
        fel.append(f"4b. längdregeln blockerade -- ska vara mjuk: {hard}")

    # 4 -- hela decket, parse->build identisk
    ids = invoke("findNotes", query=f'deck:"{config.DECK_NAME}" tag:{config.FORMAT_TAG_V2}')
    info = []
    for i in range(0, len(ids), 500):
        info.extend(invoke("notesInfo", notes=ids[i:i + 500]))
    avvikande, migreras, ety_kort = [], [], 0
    for n in info:
        raw = n["fields"][config.FIELD_BAKSIDA]["value"]
        p = baksida.parse(raw)
        if not p["huvudbetydelse"]:
            continue
        if p["etymologi"]:
            ety_kort += 1
        om = baksida.build(**{k: v for k, v in p.items() if k != "definitioner"})
        if om == raw:
            continue
        # Kort skrivna FÖRE 2026-08-10 har etymologin som omarkerad text. De
        # SKA ändras av en omskrivning -- det är stilbytet, inte en bugg. Men
        # skillnaden måste vara exakt den, och ingenting annat: om något mer
        # skiljer är det den gamla farliga buggklassen (parse tappar ett fält,
        # build raderar det tyst) och då ska testet falla.
        ord_ = n["fields"][config.FIELD_ORD]["value"]
        if p["etymologi"] and om.replace(
                f'<font color="{config.ETYMOLOGI_COLOR}">'
                f'{config.ETYMOLOGI_PIL} {p["etymologi"]}</font>',
                p["etymologi"]) == raw:
            migreras.append(ord_)
        else:
            avvikande.append(ord_)
    print(f"Deckkontroll: {len(info)} kort, {len(avvikande)} avvikande, "
          f"{ety_kort} med etymologi, {len(migreras)} migreras till grå pilrad")
    if migreras:
        print(f"  migreras vid nästa omskrivning: {migreras[:10]}")
    if avvikande:
        fel.append(f"5. parse->build ändrade {len(avvikande)} kort: {avvikande[:10]}")

    if fel:
        print("\nMISSLYCKADES:")
        for f in fel:
            print(f"  {f}")
    else:
        print("Alla kontroller OK.")


if __name__ == "__main__":
    main()
