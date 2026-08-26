# -*- coding: utf-8 -*-
import json

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}

# --- RIKTIGT FIX: synonymspärren har rätt, firad saknar belägg ---
BY["celebrerad"]["proposed"]["synonymer"] = []
BY["celebrerad"]["sokkoll"]["slutsats"] += (
    " RÄTTAT 2026-08-26: firad ströks efter att synonymspärren slog till. SAOL ger infinitiven "
    "fira, inte participet firad — belägget räcker inte, och tom synonymlista är godkänt.")

TILLAT = {
    "tentakel": {"betydelse_kan_saknas":
        "SO:s tredje post är markören el., inte en egen betydelse. Båda betydelserna — spröt hos "
        "djur och den bildliga om utsträckt inflytande — finns på kortet sedan rättelsen."},
    "adagio": {"synonym_saknas_trots_belagg":
        "Långsamt är SAOL:s definitionsord och musikstycke är kortets andra betydelse. Ingen av "
        "dem är utbytbar mot adagio, som är en fackterm. Tom lista är rätt svar."},
    "anglofil": {"frammande_uppslagsord":
        "De två främmande uppslagen är förleden anglo- och efterleden -fil, alltså ordets egna "
        "beståndsdelar som SAOL redovisar separat. Inga andra ord — ingen risk för fel glosor."},
    "anspråk": {"betydelse_kan_saknas":
        "SO:s tre poster är två definitioner plus markören äv. något utvidgat. Den andra "
        "(utnyttjande, exempel gör inte anspråk på fullständighet) är samma grundbetydelse — "
        "att hävda rätt till något — i överförd användning, vilket kortets krav på något man "
        "menar sig ha rätt till täcker."},
    "appell": {"betydelse_kan_saknas":
        "SO:s fjärde post är markören spec. juridik till domstolsbetydelsen. Alla tre faktiska "
        "betydelserna finns på kortet, i samma ordning som SAOL: vädjan; framställan till högre "
        "domstol; lystringssignal."},
    "attribut": {"betydelse_kan_saknas":
        "SO:s fyra poster är tre definitioner plus en markör. Kortet har de två som bär "
        "ordförrådet: utmärkande egenskap/tillbehör och den grammatiska. Den tredje (föränderlig "
        "egenskap inom datateknik) är samma begrepp som den första, tillämpat i ett fackområde."},
    "avlat": {
        "frammande_uppslagsord":
            "Det främmande uppslaget är avla — ett helt annat ord (ge upphov till liv genom "
            "befruktning) som fuzzy-matchningen drog in. Det är uttryckligen uteslutet ur kortet, "
            "vilket också står i sökkollen. Inga glosor kommer därifrån.",
        "betydelse_kan_saknas":
            "SO:s tre poster är avlats enda betydelse, plus markören spec. om vissa urartningar "
            "under senmedeltiden, plus verbet avlas betydelse — som hör till det andra uppslaget "
            "(se ovan) och inte ska med. En betydelse är rätt."},
    "butelj": {"synonym_saknas_trots_belagg":
        "Flaska är definitionens huvudord men vidare än butelj: varje butelj är en flaska, inte "
        "tvärtom. Inte utbytbar. Tom lista är rätt svar."},
    "celebrerad": {"frammande_uppslagsord":
        "Det främmande uppslaget är celebrera, verbet som participet celebrerad bildas av. "
        "Samma ord i annan form, inte ett annat uppslag."},
}

for o, d in TILLAT.items():
    BY[o].setdefault("forgranska_tillat", {}).update(d)

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Celebrerads synonym struken. Motiveringar på %d kort." % len(TILLAT))
