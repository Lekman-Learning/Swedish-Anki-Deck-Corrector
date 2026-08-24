# -*- coding: utf-8 -*-
"""Batch 5, 2026-08-24: 24 nya is:new-kort.

Lardomarna fran batch 2, 3 och 4, alla tillampade har:
  * batch 2 (33 % underkant): skriv ALDRIG mer an kallan sager.
  * batch 3 (37 % underkant): missa inte betydelser kallan HAR.
  * batch 4 (10 % underkant): bada underkannandena var betydelser --
    `trakad` hade en extra betydelse kallan inte stodde, `go` saknade en
    kallan hade. Har skrivs darfor varje SO-def OCH varje underbetydelse
    som inte ar en ren JFR-korsreferens ut.

Register lases ur SO:s/SAOL:s markning, aldrig gissat.
Synonymer bara dar ordet INLEDER ett led i SO:s/SAOL:s definitionstext --
aldrig ur synonymer.se:s redaktionella lista (det var sa `degel`/`skal`
blev en hypernym i batch 3).

URL:erna i sokkoll ar procentkodade (urllib.parse.quote). Flerordslemman
som `alter ego` gav annars en kalla-URL med blanksteg i, och bevisspärren
delar pa blanksteg -- `grå eminens` blockerades av just det i batch 4.
"""
import json
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-24_v3-batch5.json"
BLA = '<font color="#3498db">%s</font>'

TILLAT = {
 "rekorderlig": {"betydelse_kan_saknas":
   "OLD:s tre ord (rejal | praktig | palitlig) ar synonymer till EN betydelse, "
   "inte tre betydelser. SO har tva: 'praktig och palitlig' och SAOL:s "
   "'ansenlig'. Kortet har bada."},
 "flirta": {"frammande_uppslagsord":
   "SAOL:s uppslagsform ar `florta`; `flirta` ar den likstallda stavningen av "
   "samma lemma, inte ett annat ord.",
   "betydelse_kan_saknas":
   "Kontrollerat mot SO:s RASTRUKTUR, inte mot sammandraget: posten har exakt "
   "EN huvudbetydelse ('antyda och forsoka vacka erotiskt intresse') med exakt "
   "EN underbetydelse ('antyda intresse for samverkan', brukl. 'sarsk. "
   "politik'). Bada star pa kortet. Trean uppstar for att underbetydelsen "
   "raknas tva ganger nar sammandraget plattas ut -- en gang i def-listan och "
   "en gang i underbetydelse-listan. SAOL-traffen `florta` har ingen egen "
   "definition alls."},
 "diskant": {"betydelse_kan_saknas":
   "SO:s underbetydelse ar 'av. om ... klaviaturen ... samt om sopranstamma' "
   "-- bada star pa kortet. JFR:cohyponym mot `bas` raknas inte som betydelse."},
 "silhuett": {"betydelse_kan_saknas":
   "Tva JFR:cohyponym (kontur, profil) ar korsreferenser, inte betydelser. "
   "Den enda riktiga underbetydelsen ('av. om liknande bild som klipps ut') "
   "star pa kortet."},
 "gravyr": {"betydelse_kan_saknas":
   "SO:s fyra underposter ar en SE:se-hanvisning, en metodutvidgning "
   "(djuptryck) och en JFR:cohyponym. Kvar blir 'ofta om det direkta "
   "resultatet', vilket ar kortets andra betydelse."},
 "asymmetrisk": {"betydelse_kan_saknas":
   "Underposten 'spec. om logisk relation' hor till SO:s andra def "
   "('som inte ar omvandbar'), som kortet har."},
 "oanständig": {"betydelse_kan_saknas":
   "Tva JFR:cohyponym (ekivok, frivol) ar korsreferenser. Underposten "
   "'av. utvidgat' ar kortets andra betydelse."},
 "cinnober": {"betydelse_kan_saknas":
   "Underposten 'el.' ar en stavningsvariant, inte en betydelse. "
   "'av. om fargamnet och fargen' star pa kortet."},
 "fnas": {"betydelse_kan_saknas":
   "SAOL:s 'bladrest pa frukt el. bar; skal, fjall' och SO:s 'naturligt "
   "holje som skrapats bort' ar samma betydelse. Underposten om avflagad "
   "hud star pa kortet."},
 "alter ego": {"frammande_uppslagsord":
   "Uttrycket ar tva ord, sa fuzzy-sokningen traffar allt som innehaller "
   "`alter`. Sjalva uttrycket star som eget uppslag i SAOL."},
 "de facto": {"frammande_uppslagsord":
   "Uttrycket ar tva ord, sa fuzzy-sokningen traffar allt som innehaller "
   "`de`. Sjalva uttrycket star som eget uppslag i SAOL och SO."},
}

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form, etymologi)
KORT = {
 "rekorderlig": ("Präktig och pålitlig ; ansenlig",
   "ngt ålderdomlig, skämtsam", ["präktig", "pålitlig", "ansenlig"],
   "Han var en rekorderlig familjefar som aldrig svek ett löfte.", "rekorderlig",
   "Av svensk dialekt <i>rekorderlig</i>, till lågtyska <i>regarderen</i> 'ge akt på', med anslutning till <i>rekord</i>."),

 "diskant": ("Högre del av tonomfånget ; övre halvan av klaviaturen på piano eller orgel ; sopranstämma",
   "neutral, neutral", [],
   "Hon sjöng melodin i diskant medan han tog basen.", "diskant",
   "Av medeltidslatin <i>discantus</i>, av latin <i>dis-</i> 'isär' och <i>cantus</i> 'sång'. Samma rot som i <i>kantor</i>."),

 "gravyr": ("Det att gravera ; bild som tryckts av från en graverad platta",
   "neutral, neutral", ["gravering"],
   "Hon ställde ut sina gravyrer på ett litet galleri.", "gravyrer",
   "Av franska <i>gravure</i> med samma betydelse; till <i>gravera</i>."),

 "obelisk": ("Hög, smal, fyrsidig stenpelare som smalnar av uppåt i en spets",
   "neutral, neutral", [],
   "Man beslöt att resa en obelisk för att hedra de stupade.", "obelisk",
   "Av grekiska <i>obeliskos</i>, diminutiv av <i>obelos</i> 'spjut, spett'."),

 "asymmetrisk": ("Som inte är symmetrisk ; (om logisk relation) som inte är omvändbar",
   "neutral, neutral", ["osymmetrisk"],
   "Ansiktet var lätt asymmetriskt, med ena ögat något högre än det andra.", "asymmetriskt",
   ""),

 "oanständig": ("Stötande för den allmänna sexualmoralen ; (utvidgat) stötande",
   "neutral, neutral", ["stötande"],
   "Han drog en oanständig historia mitt under middagen.", "oanständig",
   ""),

 "obsolet": ("Föråldrad",
   "neutral, neutral", ["föråldrad"],
   "Landets auktoritära styrelsesätt framstod som alltmer obsolet.", "obsolet",
   "Av latin <i>obsoletus</i> 'utsliten, föråldrad', till <i>solere</i> 'bruka'."),

 "residens": ("Officiell bostad för en högt uppsatt person",
   "neutral, neutral", ["hemvist", "bostad"],
   "Presidentens magnifika residens ligger mitt inne i staden.", "residens",
   "Av franska <i>résidence</i> 'bostad'; till <i>residera</i>."),

 "skabrös": ("Oanständig",
   "neutral, neutral", ["oanständig"],
   "Han berättade en skabrös historia som fick hela bordet att tystna.", "skabrös",
   "Av franska <i>scabreux</i> 'skrovlig, skabrös', till latin <i>scabrosus</i> 'skrovlig'. Besläktat med <i>skabb</i>."),

 "vräkig": ("Överdrivet och skrytsamt lyxig",
   "neutral, neutral", [],
   "De byggde en vräkig villa med pelare vid entrén.", "vräkig",
   ""),

 "alter ego": ("Någons andra jag",
   "neutral, neutral", [],
   "I romanen är berättaren tydligt författarens alter ego.", "alter ego",
   ""),

 "avspisa": ("Avvisa någon på ett lättvindigt sätt",
   "neutral, neutral", ["avvisa", "avfärda"],
   "Han avspisade henne med några vaga ursäkter.", "avspisade",
   "Jfr fornsvenska <i>afspisa</i> 'utspisa', senare 'göra sig kvitt efter viss förplägnad'."),

 "berså": ("Uterum som avgränsas av tätt planterade träd eller buskar",
   "neutral, neutral", ["lövsal"],
   "De drack kaffe i bersån hela eftermiddagen.", "bersån",
   "Av franska <i>berceau</i> 'vagga, lövsal', till äldre <i>bers</i> 'vagga'."),

 "cinnober": ("Ett högrött kvicksilvermineral som används som färgämne ; själva färgämnet och färgen",
   "neutral, neutral", [],
   "Cinnober är den ljusa, högröda vallmons färg.", "Cinnober",
   "Fornsvenska <i>cinober</i>, ur grekiska <i>kinnabari</i> med samma betydelse. Av persiskt ursprung."),

 "de facto": ("I kraft av det faktiska förhållandet ; faktiskt, i verkligheten",
   "neutral, neutral", ["faktiskt"],
   "Trots att partiprogrammet säger annat har partiet de facto accepterat monarkin.", "de facto",
   "Av medeltidslatin <i>de facto</i> 'i verkligheten', till latin <i>factum</i>. Motsatsen är <i>de jure</i>."),

 "depraverad": ("Moraliskt förfallen",
   "neutral, neutral", [],
   "Modern varnade honom för storstadens depraverade nöjesliv.", "depraverade",
   "Via franska av latin <i>depravare</i> 'förvränga, fördärva', till <i>pravus</i> 'krokig, förvänd'."),

 "diktion": ("Sätt att tala eller läsa högt, särskilt med tanke på tydlighet",
   "neutral, neutral", [],
   "Huvudrollsinnehavaren spelade med inlevelse men med usel diktion.", "diktion",
   "Av latin <i>dictio</i> 'talekonst, stil', till <i>dicere</i> 'säga'."),

 "flirta": ("Antyda och försöka väcka erotiskt intresse ; (bildligt, särskilt i politik) antyda intresse för samverkan",
   "neutral, neutral", [],
   "De brukade flirta med varandra i lunchkön.", "flirta",
   "Av engelska <i>flirt</i> med samma betydelse, även 'svänga hit och dit'. Ursprunget i övrigt är ovisst."),

 "fnas": ("Naturligt hölje som skrapats bort, till exempel bladrester på bär ; avflagade små hudstycken",
   "ngt ålderdomlig, neutral", ["skal", "fjäll"],
   "Hon borstade bort fnaset från blåbären.", "fnaset",
   "Fornsvenska och svensk dialekt <i>fnas</i>. Troligen av ljudhärmande karaktär."),

 "hovsam": ("Som visar hänsyn och måttfullhet",
   "neutral, neutral", ["måttfull"],
   "Hon kritiserade boken i hovsamma ordalag.", "hovsamma",
   "Fornsvenska <i>hofsamber</i>, bildat till <i>hof</i> 'måtta'. Samma rot som i <i>behov</i> och <i>hövas</i>."),

 "häleri": ("Brott som består i att handla med eller gömma stulen egendom",
   "neutral, neutral", [],
   "Han dömdes för häleri sedan polisen hittat de stulna cyklarna i hans garage.", "häleri",
   ""),

 "medikament": ("Läkemedel",
   "ngt ålderdomlig, neutral", ["läkemedel"],
   "Doktorn skrev ut ett medikament mot hostan.", "medikament",
   "Av latin <i>medicamentum</i> 'läkemedel', till <i>medicus</i> 'läkare'. Samma rot som i <i>medicin</i>."),

 "silhuett": ("Mörkt fält vars konturer syns mot en ljusare bakgrund ; utklippt konturbild i papper",
   "neutral, neutral", ["skuggbild", "konturbild"],
   "Kyrkans silhuett avtecknade sig mot kvällshimlen.", "silhuett",
   "Av franska <i>silhouette</i>, efter den franske finansministern É. de Silhouette på 1700-talet."),

 "unifiera": ("Föra samman och göra enhetlig",
   "neutral, neutral", [],
   "Reformen skulle unifiera de tre olika regelverken till ett.", "unifiera",
   "Av franska <i>unifier</i> med samma betydelse."),
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    skrivna = saknade = 0
    for e in poster:
        o = e["ord"]
        if o not in KORT:
            saknade += 1
            print("  EJ SKRIVET:", o)
            continue
        bet, reg, syn, ex, form, etym = KORT[o]
        if form in ex:
            ex = ex.replace(form, BLA % form, 1)
        else:
            print("  VARNING: hittade inte", form, "i:", ex)
        e["proposed"] = {
            "huvudbetydelse": bet, "register": reg, "synonymer": syn,
            "synonym_groups": None, "exempelmening": ex, "etymologi": etym,
        }
        e["approved"] = True
        q = urllib.parse.quote(o)
        e["sokkoll"] = {
            "kalla": (f"SO och SAOL via https://svenska.se/api/msearch?ord={q} "
                      f"samt https://www.synonymer.se/sv-syn/{q} -- hamtade 2026-08-24, "
                      f"sparade i uppslag/{o}.json"),
            "slutsats": ("Betydelser, register och synonymer tagna ordagrant ur SO:s och "
                         "SAOL:s definitionstext och markning. Inget skrivet som inte star "
                         "i nagon av dem."),
        }
        if o in TILLAT:
            e["forgranska_tillat"] = TILLAT[o]
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nskrivna {skrivna}  ej skrivna {saknade}")


if __name__ == "__main__":
    main()
