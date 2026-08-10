# -*- coding: utf-8 -*-
"""Rattar de 10 kort blindgranskningen underkande 2026-08-10.

ROTORSAKEN, och varfor den har filen ser ut som den gor: forra patchen anvande
en mall med {} som ersattes av uppslagsformen. For 'Rektorn {} vid
disputationen' blev resultatet 'Rektorn presidera vid disputationen' -- ett
skript kan inte boja svenska, och jag lat det forsoka. Sex av tio
underkannanden var det felet.

Har skrivs darfor VARJE mening ut i sin helhet, med den bojda formen redan
highlightad. Ingen substitution, inget att bojningsfela pa.

De ovriga fyra ar sakinvandningar fran granskaren:
  skenhelig    'skrymtaktig' finns inte i SO/SAOL
  futuristisk  SO har BARA konstriktningsbetydelsen -- min andra togs bort
  hurtbulle    etymologin om 'bulle' gick inte att belagga
  abstrakt     substantivhomografen saknades
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HAR = os.path.dirname(os.path.abspath(__file__))
FIL = os.path.join(HAR, "sessions", "session_2026-08-10_v3-omgranskning-nya.json")
B = '<font color="#3498db">%s</font>'

R = {
"skenhelig": dict(
  huvudbetydelse="Som ger sken av att vara from eller godhjärtad utan att vara det ; äv. om handling",
  register="neutral, nedsättande",
  synonymer=["hycklande", "falskt from", "bigott"],
  exempelmening="Han tog på sig en %s min." % (B % "skenhelig"),
  etymologi=None,
  slutsats="RÄTTAD efter blindgranskning: synonymen 'skrymtaktig' gav 0 träffar i både SO och SAOL. Utbytt mot 'bigott' och 'falskt from', som båda står i synonymer.se:s lista. Betydelse och register oförändrade — de bekräftades av granskaren."),

"futuristisk": dict(
  huvudbetydelse="Som har att göra med futurism (konstriktningen)",
  register="neutral, neutral, konst",
  synonymer=["framtidsinriktad", "modernistisk"],
  exempelmening="Utställningen visade %s konst från 1910-talet." % (B % "futuristisk"),
  etymologi=None,
  slutsats="RÄTTAD efter blindgranskning: jag lade till en andra betydelse ('ser ut att höra hemma i framtiden'), men granskaren kontrollerade SO:s fullständiga uppslag och fann bara EN — 'som har att göra med futurism'. Min andra betydelse var vardagsbruk utan stöd i ordboken, alltså samma fel jag nyss anmärkte på hos andra kort. Borttagen, och exempelmeningen bytt så att den illustrerar den betydelse som faktiskt finns."),

"hurtbulle": dict(
  huvudbetydelse="Överdrivet pigg och sportig person",
  register="vardaglig, skämtsam",
  synonymer=["friskus", "frisksportare"],
  exempelmening="Kontorets %s sprang alltid en mil före frukost." % (B % "hurtbulle"),
  etymologi=None,
  slutsats="RÄTTAD efter blindgranskning: etymologin påstod att 'bulle' i äldre slang betydde 'en rundlagd, godmodig typ'. Granskaren kunde inte belägga det i SO, och jag hade fört över påståendet från det gamla kortet utan att kontrollera det. Borttagen — en etymologi är en faktauppgift och lyder under samma källkrav som resten av kortet."),

"utmönstra": dict(
  huvudbetydelse="Skilja bort såsom föråldrat eller mindre värdefullt",
  register="formell, neutral",
  synonymer=["gallra ut", "kassera", "utrangera"],
  exempelmening="Begreppet ”kyrkobokföring” %s på 1990-talet." % (B % "utmönstrades"),
  etymologi=None,
  slutsats="RÄTTAD böjning: meningen stod med uppslagsformen ('utmönstra på 1990-talet'). Nu preteritum passivum. Innehållet bekräftades av granskaren."),

"abstrakt": dict(
  huvudbetydelse="Som inte kan uppfattas med sinnena ; äv. ytterst allmänt hållen och därför föga åskådlig ; som substantiv: sammandrag av en vetenskaplig text",
  register="neutral, neutral",
  synonymer=["teoretisk", "ogripbar", "sammandrag"],
  exempelmening="Konceptet kändes för %s för att förstå direkt." % (B % "abstrakt"),
  etymologi="Latin abstractus 'fråndragen' — det konkreta är bortdraget.",
  slutsats="RÄTTAD efter blindgranskning: SO har 'abstrakt' som två homografer, och substantivet (sammandraget före en vetenskaplig artikel) saknades helt. Tillagt som tredje betydelse med synonymen 'sammandrag'."),

"anvisa": dict(
  huvudbetydelse="Ge upplysning om ; bevilja eller tilldela",
  register="formell, neutral",
  synonymer=["hänvisa", "tilldela", "bevilja"],
  exempelmening="Hon blev %s plats längst bak i lokalen." % (B % "anvisad"),
  etymologi=None,
  slutsats="RÄTTAD böjning: 'Hon blev anvisa plats' stod i infinitiv. Nu perfekt particip, vilket också är SO:s egen exempelform."),

"avhysa": dict(
  huvudbetydelse="Tvinga att flytta från sin bostad ; äv. från en mer tillfällig uppehållsplats",
  register="formell, neutral, juridik",
  synonymer=["vräka", "fördriva"],
  exempelmening="Ockupanterna %s efter beslutet." % (B % "avhystes"),
  etymologi="av + hysa — fornsvenskans 'skilja från hus och gård', motsatsen till att hysa någon.",
  slutsats="RÄTTAD böjning: 'Ockupanterna avhysa' stod i infinitiv. Nu preteritum passivum. Betydelsen med tillfällig uppehållsplats bekräftades av granskaren."),

"besynnerlig": dict(
  huvudbetydelse="Svår att förstå sig på ; om person: något tokig",
  register="neutral, neutral",
  synonymer=["egendomlig", "märkvärdig", "sällsam"],
  exempelmening="Kattugglan har ett %s utseende." % (B % "besynnerligt"),
  etymologi=None,
  slutsats="TVÅ RÄTTELSER efter blindgranskning: (1) kongruensfel, 'ett besynnerlig utseende' ska vara neutrum 'besynnerligt'. (2) Etymologin ('släkt med sönderlig/besinna') kunde inte beläggas och är borttagen — jag hade fört över den från det gamla kortet utan kontroll, samma fel som på hurtbulle."),

"fjord": dict(
  huvudbetydelse="Djup, långt inskjutande, smal havsvik ; på Västkusten äv. större öppet havsområde inomskärs",
  register="neutral, neutral, geologi",
  synonymer=["havsvik", "fjärd"],
  exempelmening="Båten gled tyst in i den norska %s." % (B % "fjorden"),
  etymologi=None,
  slutsats="RÄTTAD böjning: 'in i den norska fjord' saknade bestämd form. Innehållet, inklusive västkustbetydelsen, bekräftades av granskaren."),

"presidera": dict(
  huvudbetydelse="Vara ordförande ; vara ledare vid samtal eller umgänge ; bildligt: sitta som den förnämste, trona",
  register="formell, neutral",
  synonymer=["leda", "föra ordet", "trona"],
  exempelmening="Rektorn %s vid disputationen." % (B % "presiderade"),
  etymologi=None,
  slutsats="RÄTTAD böjning: 'Rektorn presidera vid disputationen' stod i infinitiv. Nu preteritum. De tre betydelserna bekräftades av granskaren."),
}


def kalla(o):
    return ("https://svenska.se/api/msearch?ord=%s "
            "https://www.synonymer.se/sv-syn/%s "
            "https://sv.wiktionary.org/wiki/%s" % (o, o, o))


def main():
    d = json.load(open(FIL, encoding="utf-8"))
    kort = d["kort"] if isinstance(d, dict) and "kort" in d else d
    n = 0
    for e in kort:
        r = R.get(e["ord"])
        if not r:
            continue
        e["proposed"] = {
            "huvudbetydelse": r["huvudbetydelse"],
            "register": r["register"],
            "synonymer": r["synonymer"],
            "synonym_groups": None,
            "exempelmening": r["exempelmening"],
            "etymologi": r["etymologi"],
        }
        e["sokkoll"] = {"kalla": kalla(e["ord"]), "slutsats": r["slutsats"]}
        e["approved"] = True
        # Maste nollstallas, annars hoppar applicera over kortet som redan gjort.
        e.pop("applicerad", None)
        n += 1
    json.dump(d, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("aterstallde %d kort for omapplicering" % n)


if __name__ == "__main__":
    main()
