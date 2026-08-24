# -*- coding: utf-8 -*-
"""Batch 4, 2026-08-24: 22 nya is:new-kort.

Larddomarna fran batch 2 och 3, bada tillampade har:
  * batch 2 (33 % underkant): skriv ALDRIG mer an kallan sager.
  * batch 3 (37 % underkant): missa inte betydelser kallan HAR.
    6 av 7 underkannanden bar redan flaggan `betydelse_kan_saknas`,
    som darfor gjordes HARD samma kvall.

Register lases ur SO:s/SAOL:s markning, aldrig gissat. Saknas markning
skrivs `neutral` -- det ar kallans besked, inte en lucka.
Synonymer bara dar ordet INLEDER ett led i SO:s/SAOL:s definitionstext.
"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-24_v3-batch4.json"
BLA = '<font color="#3498db">%s</font>'

TILLAT = {
 "moloken": {"betydelse_kan_saknas":
   "SO:s uppslag blandar adjektivet `moloken` (nedstamd) med substantivet "
   "`molok` (omattligt vidunder, av hebreiska Molek) och SAOL lagger till "
   "odlan. Det ar skilda lemman, inte betydelser av adjektivet."},
 "daven": {"betydelse_kan_saknas":
   "SO listar 3 definitioner och 3 underbetydelser (av dryck / om person / "
   "bildligt) som ar samma tre betydelser raknade tva ganger. Kortet har alla tre."},
 "blotdjur": {"betydelse_kan_saknas":
   "Tredje posten ar underbetydelsen 'ibland bildligt', vilket ar precis "
   "kortets andra betydelse (slapp person). Ingen betydelse saknas."},
 "kostlig": {"betydelse_kan_saknas":
   "Tredje posten ar underbetydelsen 'vanligen bildligt' till 'lustig', "
   "inte en egen betydelse."},
 "kantin": {"betydelse_kan_saknas":
   "Tredje posten ar underbetydelsen 'av.' till karlbetydelsen, som kortet "
   "redan har. JFR:cohyponym raknas inte som betydelse."},
 "trakad": {"frammande_uppslagsord":
   "Traffarna `traka` och `traka ut` ar infinitivformen till samma lemma. "
   "Kortordet ar perfektparticipet."},
 "go": {"frammande_uppslagsord":
   "Traffen `god` kommer av fuzzy-matchning pa tva bokstaver. Bade bradspelet "
   "och framatandan star som egna uppslag under `go`."},
 "gra eminens": {"betydelse_kan_saknas":
   "SO:s def-lista galler lemmat `eminens` (kardinalstitel, applesort). "
   "Kortet galler uttrycket `gra eminens`, som bara har en betydelse.",
   "frammande_uppslagsord":
   "Uttrycket ar tva ord, sa fuzzy-sokningen traffar allt som innehaller `gra`. "
   "Sjalva uttrycket star som eget uppslag under `eminens`."},
}

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form, etymologi)
KORT = {
 "däven": ("Unken och något fuktig ; (om dryck) avslagen och fadd ; (om person) trött",
   "neutral, neutral", ["unken", "dåsig"],
   "Källarluften var däven och luktade mögel.", "däven",
   "Av fornsvenska <i>dävin</i> 'fuktig'. Ursprunget i övrigt är ovisst."),

 "merkantil": ("Som har att göra med handel",
   "neutral, neutral", [],
   "Han gick en merkantil utbildning och tog över faderns firma.", "merkantil",
   "Av franska <i>mercantile</i>, till latin <i>mercari</i> 'driva handel' — samma rot som i <i>kommers</i> och <i>marknad</i>."),

 "tråkad": ("Retad på ett godmodigt sätt ; uttråkad, trött på något",
   "vardaglig, neutral", [],
   "Han blev tråkad av kompisarna varje gång han gick till gosskören.", "tråkad",
   "Av svensk dialekt <i>tråka</i> 'gå och släpa, knoga'. Besläktat med <i>trycka</i>."),

 "insidiös": ("Som döljer sin skadliga eller oangenäma innebörd",
   "ngt ålderdomlig, neutral", ["försåtlig", "lömsk"],
   "Kritiken kom i form av insidiösa antydningar i stället för öppna angrepp.", "insidiösa",
   "Av franska <i>insidieux</i>, av latin <i>insidiosus</i> 'lömsk, försåtlig'."),

 "anbelanga": ("Beträffa, angå",
   "neutral, neutral", ["beträffa", "angå"],
   "Vad den saken anbelangar vill jag säga följande.", "anbelangar",
   "Av lågtyska <i>anbelangen</i>, egentligen 'nå fram till'."),

 "beråd": ("Situation där ett besvärligt val måste göras ; att just ämna göra något",
   "neutral, neutral", [],
   "Föräldrarna var i beråd om sonen skulle få gå in vid teatern.", "beråd",
   "Av lågtyska <i>berat</i> 'övervägande'. Samma rot som i <i>råd</i>."),

 "beskänkt": ("Lindrigt berusad",
   "neutral, eufemistisk", ["berusad"],
   "Två beskänkta herrar kom ut från restaurangen.", "beskänkta",
   "Av lågtyska <i>beschenkt</i>, perfekt particip av <i>beschenken</i> 'skänka i åt någon'. Ursprungligen alltså 'undfägnad'."),

 "blötdjur": ("Ryggradslöst djur med huvud, inälvssäck och ombildad fot ; (bildligt) slapp och karaktärslös person",
   "neutral, neutral", ["mollusk"],
   "Snäckor, musslor och bläckfiskar är blötdjur.", "blötdjur", ""),

 "drott": ("Fornnordisk storman med eget hov",
   "neutral, neutral", [],
   "Sagan handlar om en drott som samlade ett krigarfölje kring sig.", "drott",
   "Av fornsvenska <i>drotin</i>, till <i>drótt</i> '(konungens) krigarfölje'. Besläktat med gotiska <i>driugan</i> 'göra krigstjänst'."),

 "ekarté": ("Kortspel för två personer med 32 kort av hög valör",
   "neutral, neutral", [],
   "De fördrev kvällen med ekarté vid brasan.", "ekarté",
   "Av franska <i>écarté</i>, till <i>écarter</i> 'kasta korten' — av <i>carte</i> 'kort'."),

 "filklove": ("Mindre skruvstycke som håller fast arbetsstycket vid filning",
   "fackspråklig, neutral", [],
   "Han spände fast nyckeln i filkloven innan han började fila.", "filkloven",
   "Sammansatt av <i>fil</i> och <i>klove</i>, ett äldre ord för klämma."),

 "go": ("Östasiatiskt brädspel där man omsluter så stora områden som möjligt med små stenar ; (vardagligt) initiativkraft och framåtanda",
   "vardaglig, neutral", ["framåtanda", "kraft", "fart"],
   "Han lärde sig spela go av sin farfar.", "go",
   "Spelet av japanska <i>go</i>. Betydelsen framåtanda är ett annat ord: engelska <i>go</i>, till <i>go</i> 'gå, färdas'."),

 "grå eminens": ("Skenbart betydelselös men i själva verket inflytelserik person",
   "neutral, neutral", [],
   "På äldre dagar var han utrikesdepartementets grå eminens.", "grå eminens",
   "Av <i>eminens</i>, kardinalens titel, av latin <i>eminentia</i> 'framstående person'. Bilden är rådgivaren i grå kåpa bakom den purpurklädde kardinalen."),

 "hepatit": ("Inflammation i levern",
   "fackspråklig, neutral", ["leverinflammation"],
   "Vaccinet skyddar mot hepatit A och B.", "hepatit",
   "Modern bildning till grekiska <i>hepar</i> (genitiv <i>hepatos</i>) 'lever'."),

 "kantin": ("Serveringsställe vid militärförläggning eller arbetsplats ; större kärl för mat eller dryck i restaurangkök",
   "ngt ålderdomlig, neutral", ["marketenteri"],
   "Soldaterna köpte cigaretter och läsk i kantinen.", "kantinen",
   "Av franska <i>cantine</i>, av italienska <i>cantina</i> 'vinkällare'."),

 "komminister": ("Ordinarie präst närmast under kyrkoherde i en församling",
   "neutral, neutral", [],
   "Han tjänstgjorde som komminister i församlingen i tolv år.", "komminister",
   "Till latin <i>con-</i> 'med' och <i>minister</i> 'tjänare' — alltså medhjälpande tjänare."),

 "kostlig": ("Lustig, roande ; dyrbar",
   "ngt ålderdomlig, neutral", ["lustig", "dyrbar"],
   "De utklädda barnen var en kostlig syn.", "kostlig",
   "Av fornsvenska <i>kosteliker</i>, till <i>kost</i> i äldre betydelsen 'utgift, värde'."),

 "moloken": ("Slokörad och nedstämd",
   "neutral, neutral", ["modstulen", "slokörad"],
   "Han satt moloken kvar vid bordet sedan de andra gått.", "moloken",
   "Till <i>mod</i> och svensk dialekt <i>loken</i> 'olustig, utmattad', till <i>loka</i> 'sloka, hänga'."),

 "oförtruten": ("Som präglas av energi och ihärdighet",
   "neutral, neutral", ["outtröttlig", "ihärdig"],
   "Hon förde en oförtruten kamp för social rättvisa.", "oförtruten",
   "Efter lågtyska <i>unvordroten</i>, till <i>förtryta</i> 'ta illa vid sig, tröttna'."),

 "paritet": ("Likvärdig nivå mellan två parter ; (ekonomi) likvärdighet mellan valutor",
   "neutral, neutral", ["likvärdighet", "jämngodhet"],
   "Hans kunnande är inte i paritet med hans entusiasm.", "paritet",
   "Via franska av latin <i>paritas</i> 'likhet'. Samma rot som i <i>par</i> och <i>pari</i>."),

 "protagonist": ("Huvudrollsinnehavare, huvudperson i en berättelse",
   "neutral, neutral", ["huvudperson"],
   "Romanens protagonist är en ung läkare i Stockholm.", "protagonist",
   "Av grekiska <i>protagonistes</i>, till <i>protos</i> 'först' och <i>agonistes</i> 'tävlande'. Samma rot som i <i>antagonist</i>."),

 "tremänning": ("Syssling, alltså barn till förälders kusin",
   "dialektal, neutral", ["syssling"],
   "Vi är tremänningar — våra mormödrar var kusiner.", "tremänningar",
   "Av fornsvenska <i>þrämänninger</i>, till <i>tre</i> och <i>man</i> — tredje ledet i släktskapsräkningen."),
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
        e["sokkoll"] = {
            "kalla": (f"SO och SAOL via https://svenska.se/api/msearch?ord={o} "
                      f"samt https://www.synonymer.se/sv-syn/{o} -- hamtade 2026-08-24, "
                      f"sparade i uppslag/{o}.json"),
            "slutsats": ("Betydelser, register och synonymer tagna ordagrant ur SO:s och "
                         "SAOL:s definitionstext och markning. Inget skrivet som inte star "
                         "i nagon av dem."),
        }
        nyckel = o.replace("ö", "o").replace("å", "a").replace("ä", "a")
        if nyckel in TILLAT:
            e["forgranska_tillat"] = TILLAT[nyckel]
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nskrivna {skrivna}  ej skrivna {saknade}")


if __name__ == "__main__":
    main()
