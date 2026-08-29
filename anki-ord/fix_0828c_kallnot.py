# -*- coding: utf-8 -*-
"""Rattar tre sokkoll-slutsatser efter omkorning av slaupp.py med --tyst.

Omkorningen gav mer information an den forsta: UPPSLAGSORD-raden visar att
tva av orden FINNS som uppslagsord i SAOL respektive SAOB, aven om ingen
definitionstext gick att extrahera. Att skriva 'ordet saknas i SAOL' nar
uppslagsordet finns dar ar ett starkare pastaende an underlaget bar.
"""
import io
import json

FIL = "sessions/session_2026-08-28_v3-batch100.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}

BY["gastkramning"]["sokkoll"]["slutsats"] = (
    "SVAGT BELAGD: uppslagsordet FINNS i SAOL (UPPSLAGSORD-raden ger "
    "traffar=saol), men ingen definitionstext gick att hamta darifran -- "
    "sannolikt for att SAOL listar ordet som avledning under gastkrama "
    "utan egen forklaring. SO har ingen artikel. Den enda kalla som ger en "
    "faktisk BETYDELSE ar alltsa Wiktionary, som listar bada: folktrons "
    "sjukdomssymtom efter en natt utomhus, och den moderna 'hallas i "
    "skrackfylld spanning'. Facit vilar pa en enda betydelsegivande kalla "
    "och ar markt darefter. I dag ar adjektivet gastkramande betydligt "
    "vanligare an substantivet.")

BY["misskundsam"]["sokkoll"]["slutsats"] = (
    "SVAGT BELAGD: uppslagsordet finns i SAOB (UPPSLAGSORD-raden ger "
    "traffar=saob), men uppslagningsskriptet extraherar ingen "
    "definitionstext ur SAOB for nagot ord i den har batchen, sa den "
    "artikeln ar inte last. Varken SO eller SAOL har nagon artikel. Enda "
    "kalla med en faktisk betydelse ar Wiktionary: 'barmhartig; medlidsam' "
    "-- darav synonymen. Att ordet saknas i bade SO och SAOL, som bada "
    "beskriver NUTIDA svenska, medan det finns i SAOB, som ar historisk, "
    "ar sjalva grunden for registret arkaisk. Det ar en slutsats av var "
    "ordet star respektive inte star, inte en markning nagon kalla gett.")

BY["reda pengar"]["sokkoll"]["slutsats"] = (
    "MISSLYCKAD UPPSLAGNING, BEKRAFTAD TVA GANGER: svenska.se:s sokning "
    "klarar inte flerordsuttryck och returnerade fel artikel bada "
    "gangerna -- forst REDAKTION ('grupp av personer som staller samman "
    "text- och bildmaterial'), vid omkorningen REGN ('nederbord i form av "
    "vattendroppar'). Att de tva traffarna inte ens ar samma ord visar att "
    "det ar en systematisk begransning i sokningen, inte en engangsmiss. "
    "Tva saker overlever bada forsoken och ar det enda som anvants: SO:s "
    "exempellista innehaller frasen 'i reda pengar', sa uttrycket ar "
    "belagt, och etymologin 'fornsvenska redha, av lagtyska rede' hor till "
    "ratt ord (reda, inte redaktion eller regn). Sjalva BETYDELSEN kommer "
    "darfor fran Wiktionary ensam: 'kontanter'. Registret ar satt till "
    "neutralt -- den alderdomlighetsmarkning som syntes i traffarna "
    "tillhorde de FELAKTIGA uppslagsorden och far inte overforas hit.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("rattade 3 sokkoll-slutsatser")
