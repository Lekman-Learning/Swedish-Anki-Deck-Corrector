# -*- coding: utf-8 -*-
import json, urllib.parse

PATH = "sessions/session_2026-08-20_v3-batch2.json"

def kalla_url(ord_text):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(ord_text, safe="")

def hl(phrase):
    return f'<font color="#3498db">{phrase}</font>'

fixes = {
"se ut som en fågelholk": dict(
    huvudbetydelse="Se förvirrad och frågande ut, med öppen mun, som om man inte fattar vad som händer",
    register="vardaglig, skämtsam",
    synonymer=None,
    synonym_groups=None,
    exempelmening=f'När läraren förklarat uppgiften för tredje gången utan att det blev klarare, satt han bara och {hl("såg ut som en fågelholk")}.',
    etymologi="Jämförelse med fågelholkens runda ingångshål, format som en öppen, frågande mun.",
    kalla_override="https://sv.wiktionary.org/wiki/som_en_f%C3%A5gelholk",
    slutsats=("OMSKRIVET efter blind underkännande 2026-08-20 (granskare claude-cli-blind): "
              "kortet beskrev 'väldigt förvånad ... som av chock', men både OLD-facit ('se "
              "frågande ut, se ut som om man inte förstått ngt') och granskarens egen kontroll "
              "pekar mot en FÖRVIRRAD/undrande min, inte chock. Omskrivet till att matcha "
              "facit exakt: en frågande, oförstående min, fortfarande med bilden av den öppna "
              "munnen (fågelholkens ingångshål) som Wiktionary "
              "(https://sv.wiktionary.org/wiki/som_en_fågelholk) beskriver som "
              "'(idiomatiskt) mycket förvånad; gapande av förvåning'. Ny exempelmening bytt "
              "från ett chock-scenario (dyr hyra) till ett förvirrings-scenario (fattar inte "
              "trots upprepad förklaring), så exemplet matchar den korrigerade betydelsen. "
              "KONTAMINERING alltjämt konstaterad: direkt svenska.se-sökning på hela frasen "
              "gav bara det generiska 'se ut'-uppslaget, ingen egen SO/SAOL-artikel för "
              "idiomet -- Wiktionary är primärkälla, OLD-facit sekundär bekräftelse."),
),
"koka soppa på en spik": dict(
    huvudbetydelse="Skapa något fullt fungerande av nästan ingenting",
    register="vardaglig, neutral",
    synonymer=None,
    synonym_groups=None,
    exempelmening=f'Med bara lite mjöl och russin lyckades hon {hl("koka soppa på en spik")} och trolla fram en hel kaka.',
    etymologi="Från en folksaga om en luffare som lurade en snål gumma på ingredienser till en soppa.",
    kalla_ord="koka soppa på en spik",
    slutsats=("OMSKRIVET efter blind underkännande 2026-08-20 (granskare claude-cli-blind): "
              "SO ger EN betydelse för just detta idiom -- 'åstadkomma något av (nästan) "
              "ingenting'. Min tidigare andra betydelse ('göra en alldeles för stor sak av "
              "något obetydligt') och synonymen 'göra en höna av en fjäder' hörde i själva "
              "verket till ett HELT ANNAT idiom (SO:s egen artikel för 'göra en höna av en "
              "fjäder', som betyder överdriva något trivialt -- motsatt valör mot 'koka soppa "
              "på en spik', som handlar om resurssnål skaparförmåga). Grundfelet var att en "
              "extern sammanfattning om folksagans ursprung nämnde båda tolkningarna i samma "
              "andetag utan att skilja dem åt ordentligt -- SO, den primära källan, ger bara "
              "den ena. Återgått till en enda betydelse, tagit bort den felaktiga andra "
              "betydelsen och synonymen. Ingen ny synonym satt -- 'göra mycket av lite' "
              "testades men saknar ordagrant stöd i SO/SAOL:s definitionstext "
              "(forgranska.py:s synonym_utan_ordboksbelagg fångade det; tom synonymlista "
              "är godkänt enligt regeln). Register oförändrat sedan förra rättningen: SO:s "
              "'historiskt'-märkning hör till 'spik'-uppslagets andra, orelaterade "
              "betydelser (handeldvapen/guldmynt), inte till detta idiom -- de två "
              "'vardagligt'-märkningarna i samma träff hör till idiomet, vardaglig behålls."),
),
}

d = json.load(open(PATH, encoding="utf-8"))
seen = set()
for entry in d:
    ord_ = entry["ord"]
    c = fixes.get(ord_)
    if c is None:
        continue
    seen.add(ord_)
    kalla = c.get("kalla_override") or kalla_url(c.get("kalla_ord", ""))
    entry["sokkoll"] = {"kalla": kalla, "slutsats": c["slutsats"]}
    entry["proposed"] = {
        "huvudbetydelse": c["huvudbetydelse"],
        "register": c["register"],
        "exempelmening": c["exempelmening"],
        "synonymer": c["synonymer"],
        "synonym_groups": c["synonym_groups"],
    }
    if c["etymologi"]:
        entry["proposed"]["etymologi"] = c["etymologi"]
    entry["approved"] = True
    # Reset stale post-verdikt bookkeeping so applicera re-processes cleanly.
    entry.pop("adamtal_varningar", None)
    entry.pop("exempel_varningar", None)

missing = set(fixes) - seen
if missing:
    raise SystemExit(f"Kort saknades i sessionsfilen: {missing}")

json.dump(d, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("OK, rattade", len(fixes), "kort")
