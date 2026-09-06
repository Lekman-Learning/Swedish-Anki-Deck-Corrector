# -*- coding: utf-8 -*-
"""De tva sista harda anmarkningarna, var och en provad mot rastrukturen.

belagga: flaggan har RATT. SO:s femte definition ('ange fakta som stoder') bar
en underbetydelse med EGEN definitionstext, 'pavisa forekomst av' -- alltsa en
sjatte sann betydelse, sprakvetenskapens 'ordet ar belagt fran 1600-talet'.
Tillagd; ingen motivering skriven, felet var mitt.

brosta: flaggan har FEL, och det gar att visa. Rastrukturen ger tre betydelser,
kortet har tre.
"""
import io, json

FIL = "sessions/session_2026-09-06_v3-omgranskning.json"

poster = json.load(io.open(FIL, encoding="utf-8"))
for e in poster:
    pr = e.get("proposed")
    if not pr:
        continue

    if e["ord"] == "belägga":
        pr["huvudbetydelse"] = (
            "Täcka en yta med ett lager ; ta upp platsen i något så att den är "
            "upptagen ; genom beslut förena med en påföljd, till exempel skatt "
            "eller förbud ; göra fast ett tåg om en knap ; visa med fakta att "
            "något stämmer ; visa att ett ord har funnits i språket vid en viss tid")
        pr["register"] = (
            "neutral, neutral ; neutral, neutral ; fackspråklig, neutral, juridik ; "
            "fackspråklig, neutral, sjöfart ; neutral, neutral ; "
            "fackspråklig, neutral, språkvetenskap")
        pr["synonym_groups"] = [["≈≈ täcka med lager"], ["≈≈ uppta"], ["belasta"],
                                ["≈≈ göra fast"], ["bevisa"], ["≈≈ påvisa förekomst"]]
        pr["synonymer"] = [s for g in pr["synonym_groups"] for s in g]
        pr["exempelmening"] = ('Ordet är <font color="#3498db">belagt</font> i svenska '
                               'texter ända från 1500-talet.')
        e["sokkoll"]["slutsats"] += (
            " TILLAGG EFTER FORGRANSKNING: forgranskningen flaggade att kortet hade "
            "for fa betydelser, och den hade ratt. SO:s femte definition ('ange fakta "
            "som stoder') bar en underbetydelse med EGEN definitionstext -- 'pavisa "
            "forekomst av' -- och en underbetydelse med egen text ar en sann betydelse "
            "enligt projektets regel. Det ar sprakvetenskapens anvandning: 'ordet ar "
            "belagt fran 1600-talet', alltsa inte att bevisa ett pastaende utan att "
            "visa att en form funnits. Tillagd som betydelse 6, med doman "
            "sprakvetenskap. Aven 'gora fast' (SO:s fjarde, sjofartsordet: belagga en "
            "trosse om en knap) ar med sedan forsta rattelsen. Kortet foljer nu SO:s "
            "egen ordning rakt igenom. EXEMPELMENING BYTT till den nya betydelse 6 -- "
            "'sjukhuset var belagt' visade betydelse 2, som redan var val forsedd, och "
            "belaggs-betydelsen ar den enda som ar helt osynlig for den som bara kan "
            "'tacka' och 'bevisa'.")

    if e["ord"] == "brösta":
        e["forgranska_tillat"] = {"betydelse_kan_saknas": (
            "Rastrukturen (visa_uppslag.py) visar EN SO-definition -- SO-LEMMA brosta "
            "(substantiv): 'del av seldon som forbinder sulky med hast' -- plus tva "
            "doljda fuzzy-lemman som inte ar ord i uppslaget. SAOL ger tre "
            "semikolonseparerade led, alltsa tre betydelser: 'en del av ett seldon', "
            "'avlossa en salva' och 'krama sig, stoltsera'. Kortets tre betydelser ar "
            "exakt dessa tre, i den ordning som satter den vanligaste forst. "
            "Sammandragets rakning pa fem kommer av att det plattar ut SO:s "
            "kanonartikel ('koppla loss kanoner for att forsatta dem i eldstallning' "
            "och 'framfora') till egna poster -- bada ar historiska respektive "
            "sportsliga specialfall av SAOL:s 'avlossa en salva', som redan star pa "
            "kortet som betydelse 3. Ingen betydelse saknas.")}

json.dump(poster, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("klart")
