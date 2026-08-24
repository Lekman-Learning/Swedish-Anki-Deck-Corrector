# -*- coding: utf-8 -*-
"""Skriver proposed+sokkoll for chunk 7 (ord 150-174) av 200-korts v3-batch3."""
import json
import urllib.parse

SOKVAG = "sessions/session_2026-08-20_v3-batch3.json"

def kalla(ord_):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(ord_)

POSTER = {
    "lösöre": dict(
        huvudbetydelse="Lös egendom, det vill säga ägodelar som inte är pengar eller värdepapper",
        register="formell, neutral, juridik",
        synonymer=[],
        exempelmening='Vid bouppteckningen räknades allt <font color="#3498db">lösöre</font> i lägenheten, från möbler till husgeråd.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. BRUK 'särsk. i juridiska sammanhang'. Ingen fristående enordssynonym utöver det redan i huvudbetydelsen -- tom lista.",
    ),
    "manifestera": dict(
        huvudbetydelse="Visa tydligt eller ge tydligt uttryck åt något",
        register="formell, neutral",
        synonymer=[],
        exempelmening='Hennes glädje <font color="#3498db">manifesterade</font> sig i ett stort leende.',
        slutsats="SO ger tre nära besläktade betydelser (ge uttryck åt; visa tydligt; visa sig) -- samma grundidé ur olika vinklar, slås ihop. Ingen fristående enordssynonym -- tom lista.",
    ),
    "marig": dict(
        huvudbetydelse="Besvärlig eller krånglig",
        register="vardaglig, negativ",
        synonymer=["besvärlig"],
        exempelmening='Den sista uppgiften på provet var riktigt <font color="#3498db">marig</font>.',
        slutsats="SO ger huvudbetydelsen ('som orsakar svårigheter') plus en bokstavlig äldre betydelse ('tovig och förkrympt') -- den senare utelämnad som ovanlig i dag. SAOL:s definitionstext ÄR ordet 'besvärlig'.",
    ),
    "nalkas": dict(
        huvudbetydelse="Närma sig, ofta långsamt",
        register="ngt ålderdomlig, neutral",
        synonymer=[],
        exempelmening='Julen <font color="#3498db">nalkades</font> och staden fylldes av ljus.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. BRUK 'något högtidligt/ngt åld.'. Ingen fristående enordssynonym -- tom lista.",
    ),
    "nidbild": dict(
        huvudbetydelse="En elak och överdrivet negativ bild eller beskrivning av någon",
        register="formell, negativ",
        synonymer=[],
        exempelmening='Tidningens <font color="#3498db">nidbild</font> av politikern var långt ifrån rättvis.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen fristående enordssynonym -- tom lista.",
    ),
    "nyans": dict(
        huvudbetydelse="En liten skillnad eller skiftning, till exempel i färg eller betydelse",
        register="neutral, neutral",
        synonymer=["färgskiftning"],
        exempelmening='Väggen var målad i en varm <font color="#3498db">nyans</font> av gult.',
        slutsats="SO ger flera nära nyanser (färgskiftning; fin skillnad; något litet) -- samma grundidé, slås ihop. SAOL:s definitionstext leder första ledet med 'färgskiftning'.",
    ),
    "nämndeman": dict(
        huvudbetydelse="En person utan juridisk utbildning som dömer tillsammans med en domare i domstol",
        register="fackspråklig, neutral, juridik",
        synonymer=["lekmannadomare"],
        exempelmening='Rätten bestod av en domare och tre <font color="#3498db">nämndemän</font>.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'lekmannadomare'.",
    ),
    "oavlåtligt": dict(
        huvudbetydelse="Ständigt och utan uppehåll",
        register="formell, neutral",
        synonymer=["oupphörlig"],
        exempelmening='Hans <font color="#3498db">oavlåtliga</font> stirrande gjorde henne obekväm.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse (uppslagsformen 'oavlåtlig' -- adverbet böjs regelbundet). SAOL:s definitionstext leder med 'oupphörlig'.",
    ),
    "oförmärkt": dict(
        huvudbetydelse="Utan att någon lägger märke till det",
        register="formell, neutral",
        synonymer=["omärklig"],
        exempelmening='Tjuven tog sig <font color="#3498db">oförmärkt</font> in i lokalerna mitt på dagen.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'omärklig'.",
    ),
    "olat": dict(
        huvudbetydelse="En dålig vana",
        register="vardaglig, negativ",
        synonymer=["osed"],
        exempelmening='Att bita på naglarna var en av hans värsta <font color="#3498db">olater</font>.',
        slutsats="SO/SAOL/Wiktionary överens om huvudbetydelsen (SAOL:s barnramse-betydelse är en helt annan, ovanlig sidobetydelse, utelämnad). SAOL:s definitionstext leder med 'osed'.",
    ),
    "orangeri": dict(
        huvudbetydelse="Ett uppvärmt växthus, ursprungligen till för att odla apelsinträd",
        register="neutral, neutral",
        synonymer=["växthus"],
        exempelmening='Slottsträdgården hade ett vackert <font color="#3498db">orangeri</font> fullt av citrusträd.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'växthus'.",
    ),
    "panegyrisk": dict(
        huvudbetydelse="Som berömmer något helt okritiskt och överdrivet",
        register="litterär, negativ",
        synonymer=["lovprisande"],
        exempelmening='Historikerns <font color="#3498db">panegyriska</font> skildring av kungen ifrågasattes senare av forskare.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext ('överdrivet lovprisande') innehåller ordet 'lovprisande'.",
    ),
    "parnass": dict(
        huvudbetydelse="Det absoluta toppskiktet inom litteraturen, dit bara de främsta författarna når",
        register="högtidlig, neutral, litteraturvetenskap",
        synonymer=[],
        etymologi="Efter berget Parnassos i Grekland, helgat åt diktkonstens gudinnor.",
        exempelmening='Han räknades snart till den svenska <font color="#3498db">parnassen</font> efter sin första diktsamling.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. BRUK 'högtidligt; ibland ironiskt'. Ingen fristående enordssynonym -- tom lista.",
    ),
    "paroxysm": dict(
        huvudbetydelse="Ett häftigt anfall, till exempel av sjukdom eller starka känslor",
        register="fackspråklig, neutral, medicin",
        synonymer=[],
        exempelmening='Han skakades av en <font color="#3498db">paroxysm</font> av hostattacker.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen fristående enordssynonym -- tom lista.",
    ),
    "passé": dict(
        huvudbetydelse="Föråldrad, inte längre modern eller aktuell",
        register="formell, negativ",
        synonymer=["föråldrad"],
        exempelmening='Många tycker att den gamla ekonomiska politiken är <font color="#3498db">passé</font>.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SO+ taggar uttryckligen SYN:synonym, och SAOL:s definitionstext leder med 'föråldrad'.",
    ),
    "pediatrik": dict(
        huvudbetydelse="Läran om barnsjukdomar och hur de behandlas",
        register="fackspråklig, neutral, medicin",
        synonymer=[],
        exempelmening='Hon specialiserade sig inom <font color="#3498db">pediatrik</font> för att kunna arbeta med sjuka barn.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen fristående enordssynonym -- tom lista.",
    ),
    "pejling": dict(
        huvudbetydelse="Att mäta riktningen till ett föremål, till exempel med kompass eller radio",
        register="fackspråklig, neutral, sjöfart",
        synonymer=["bäring"],
        exempelmening='Fartyget gjorde en <font color="#3498db">pejling</font> för att avgöra var kusten låg.',
        slutsats="SO/synonymer.se överens om huvudbetydelsen (SAOL:s licens-tv-notering är en historisk, mycket smal specialanvändning, utelämnad). SO:s definitionstext avslutar andra ledet med ordet 'bäring'.",
    ),
    "piktur": dict(
        huvudbetydelse="Handstil",
        register="ngt ålderdomlig, neutral, litterär",
        synonymer=[],
        exempelmening='Läraren kunde knappt tyda elevens svårlästa <font color="#3498db">piktur</font>.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SO/SAOL:s definitionstext ÄR ordet 'handstil', redan huvudbetydelsen -- ingen ytterligare synonym. Tom lista.",
    ),
    "precedens": dict(
        huvudbetydelse="Företräde, att något går före något annat",
        register="formell, neutral",
        synonymer=[],
        exempelmening='Den äldre lagen hade <font color="#3498db">precedens</font> framför den nya tolkningen.',
        slutsats="Endast SO har egen artikel (ingen SAOL, men SAOB bekräftar). SO:s definitionstext ÄR ordet 'företräde', redan huvudbetydelsen -- ingen ytterligare fristående synonym. Tom lista.",
    ),
    "processa med": dict(
        huvudbetydelse="Föra en rättegång mot någon, stämma någon inför domstol",
        register="formell, neutral, juridik",
        synonymer=[],
        exempelmening='Företaget valde att <font color="#3498db">processa med</font> sin tidigare leverantör om den uteblivna betalningen.',
        slutsats="Sökträffarna för 'processa' är brett kontaminerade (tekniska/datateknik-betydelser blandas in), men SO/SAOL:s första betydelse ('driva en rättegång') matchar exakt frasen 'processa med' och SO:s egen EX-mening bekräftar bruket ('hon processade med förlaget om upphovsrätten'). Ingen enordssynonym i definitionstexten -- tom lista.",
    ),
    "pulpa": dict(
        huvudbetydelse="Mjuk, blodkärlsrik vävnad inuti ett organ, till exempel inuti en tand ; foder gjort av rester från potatisstärkelsetillverkning",
        register="fackspråklig, neutral, medicin",
        synonymer=[],
        exempelmening='Tandläkaren förklarade att infektionen hade nått tandens <font color="#3498db">pulpa</font>.',
        slutsats="SO/SAOL ger två klart skilda betydelser (mjuk kroppsvävnad; potatisfoder). Ingen enordssynonym i definitionstexten -- tom lista.",
    ),
    "på basis av": dict(
        huvudbetydelse="Utifrån något, med något som grund eller underlag",
        register="formell, neutral",
        synonymer=["grundval"],
        exempelmening='Beslutet fattades <font color="#3498db">på basis av</font> de senaste forskningsrönen.',
        slutsats="Sökträffarna för frasen är kontaminerade (matchar andra artiklar för 'bas' brett), men SAOL:s egen definitionstext för uppslagsordet 'bas' är just 'grundval', som är den ord frasen bygger på -- använt som belagd synonym.",
    ),
    "reseffekter": dict(
        huvudbetydelse="Bagage, det man tar med sig på en resa",
        register="formell, neutral",
        synonymer=["bagage"],
        exempelmening='Han glömde sina <font color="#3498db">reseffekter</font> i taxin på väg till flygplatsen.',
        slutsats="SO/SAOL överens: en betydelse. BRUK 'formellt'. SO/SAOL:s definitionstext ÄR ordet 'bagage'.",
    ),
    "resår": dict(
        huvudbetydelse="En elastisk del i kanten av ett klädesplagg ; en spiralfjäder i en möbel, till exempel en soffa",
        register="neutral, neutral",
        synonymer=["spiralfjäder"],
        exempelmening='Byxlinningen hade en bred <font color="#3498db">resår</font> för extra komfort.',
        slutsats="SO/SAOL ger två klart skilda betydelser (elastisk kantdel i kläder; spiralfjäder i möbler). SAOL:s definitionstext leder andra ledet med 'spiralfjäder'.",
    ),
    "sammankomst": dict(
        huvudbetydelse="Ett organiserat möte",
        register="formell, neutral",
        synonymer=["möte"],
        exempelmening='Föreningens årliga <font color="#3498db">sammankomst</font> hölls i stadshuset.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext ÄR ordet 'möte'.",
    ),
}

def main():
    data = json.load(open(SOKVAG, encoding="utf-8"))
    by_ord = {c["ord"]: c for c in data}
    saknas = []
    for ord_, spec in POSTER.items():
        c = by_ord.get(ord_)
        if c is None:
            saknas.append(ord_)
            continue
        c["sokkoll"] = {"kalla": kalla(ord_), "slutsats": spec["slutsats"]}
        c["proposed"] = {
            "huvudbetydelse": spec["huvudbetydelse"],
            "register": spec["register"],
            "synonymer": spec.get("synonymer"),
            "synonym_groups": spec.get("synonym_groups"),
            "exempelmening": spec["exempelmening"],
            "etymologi": spec.get("etymologi"),
        }
        c["approved"] = True
    json.dump(data, open(SOKVAG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(POSTER)} kort. Saknades i sessionsfilen: {saknas}")

if __name__ == "__main__":
    main()
