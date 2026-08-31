# -*- coding: utf-8 -*-
"""Batch 2026-08-31. Del 4: kort 23-31.

TVA SAKFEL I DE GAMLA KORTEN som rattas har:

  sober  Det gamla kortet sa "nykter och mattlig, fri fran alkohol". SO:s
         ENDA definition ar "snygg och smakfull", och SAOL har nykterheten
         forst men det estetiska direkt efter. Kortet larde alltsa ut fel
         huvudbetydelse for det vanligaste bruket (sobra farger, sober
         kladsel).
  drive  Det gamla kortet sa "drivkraft, styra, fora ... anvanda kraft eller
         energi". Ingen av ordbockerna har den betydelsen. SO ger satsning,
         golfslag och drive-in.
"""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-31_v3-batch40.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
B = '<font color="#3498db">%s</font>'


def kallor(o, *extra):
    k = urllib.parse.quote(o)
    return " ".join([
        "https://svenska.se/api/msearch?ord=%s" % k,
        "https://www.synonymer.se/sv-syn/%s" % k,
        "https://sv.wiktionary.org/wiki/%s" % k,
        *extra,
    ])


def satt(o, bet, reg, syn, ex, ety, slutsats, grupper=None, extra=(), conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": grupper, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": kallor(o, *extra), "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True


# --------------------------------------------------------- 23. approximativ
satt("approximativ",
     "Ungefärlig, alltså som kan avvika något från det verkliga värdet",
     "formell, neutral",
     ["ungefärlig"],
     "De fick fram ett " + B % "approximativt" + " värde som dög för "
     "ändamålet.",
     "av latinets approximare 'närma sig', till ad 'till' och proximus "
     "'närmast'; samma rot som i proximitet",
     "SO: 'som kan avvika nagot fran det verkliga vardet', med "
     "underbetydelsen 'ungefar' markt SYN:synonym. SAOL: 'ungefarlig'. En "
     "betydelse. Ungefarlig ar belagd pa bada satten regel 2 tillater: SO "
     "SYN:synonym-markerar den OCH den ar hela SAOL:s definition.")

# --------------------------------------------------------------- 24. dandy
satt("dandy",
     "Man som lägger överdrivet mycket omsorg vid kläder och uppträdande",
     "ålderdomlig, negativ",
     ["klädsnobb"],
     "Han klädde sig som en " + B % "dandy" + ", med sidenväst och "
     "promenadkäpp.",
     "av engelskans dandy, känt från 1780-talet i skotsk dialekt; kanske av "
     "smeknamnet Dandy för Andrew",
     "SO: 'man med overdrivet raffinemang i kladsel och upptradande', markt "
     "'nagot alderdomligt'. SAOL: 'kladsnobb'. En betydelse. Kladsnobb ar "
     "hela SAOL:s definition och darmed belagd. syn.se:s spratt, grilljanne "
     "och modelejon saknar ordboksbelagg.")

# --------------------------------------------------------- 25. vara renons
satt("vara renons",
     "Helt sakna något som behövs eller förväntas ; i kortspel: sakna kort "
     "i en viss färg",
     "formell, neutral ; fackspråklig, neutral",
     [],
     "Partiet tycks vara " + B % "renons" + " på goda idéer.",
     "av franskans renoncer 'avstå från', av latinets renuntiare; i kortspel "
     "att avstå från att följa färg",
     "SO haller isar 'som inte ar i besittning' och 'som helt saknar kort i "
     "viss farg'. SAOL likasa: 'alldeles utan' och 'avsaknad av kort i en "
     "farg i kortspel'. Tva betydelser (regel 1). Inga belagda synonymer: "
     "bada definitionerna ar flerordsfraser dar inget enskilt ord ar "
     "utbytbart mot uttrycket.")

# ---------------------------------------------------------------- 26. drive
satt("drive",
     "Särskilt insatt satsning eller kampanj för att öka en verksamhet ; "
     "långt svepande slag i golf eller tennis ; anläggning som kan användas "
     "från bilen, som i drive-in",
     "neutral, neutral ; fackspråklig, neutral ; neutral, neutral",
     ["satsning", "kampanj"],
     "Trafiksäkerhetsverket gjorde en " + B % "drive" + " för att öka "
     "användningen av bilbälten.",
     "av engelskans drive 'driva, köra'; de tre betydelserna är tre skilda "
     "lån in i svenskan, från kampanjspråk, sport respektive bilkultur",
     "SO haller isar tre: 'sarskilt insatt okad verksamhet', 'langt svepande "
     "slag' och 'som kan utnyttjas av bilister utan att de behover ga ur "
     "bilen'. SAOL bekraftar och grupperar om nagot: 'kraftigt, svepande slag "
     "i golf el. tennis; satsning, kampanj' och 'biograf som visar film under "
     "bar himmel'. Tre betydelser (regel 1). Satsning och kampanj inleder "
     "bada sitt led i SAOL och hor till forsta gruppen. DET GAMLA KORTETS "
     "betydelse 'drivkraft, anvanda kraft eller energi' finns inte i nagon "
     "ordbok och stryks -- det var engelskans drive laest rakt av.",
     grupper=[["satsning", "kampanj"], [], []])

# ---------------------------------------------------------------- 27. sober
satt("sober",
     "Måttfull och återhållsam ; snygg och smakfull utan att vara prålig",
     "formell, neutral ; neutral, positiv",
     ["måttfull", "nykter"],
     "Våningen var inredd i " + B % "sobra" + " färger.",
     "av franskans sobre, av latinets sobrius 'nykter'; grundbetydelsen "
     "nykterhet har i svenskan glidit över mot återhållsam smak",
     "SO ger BARA 'snygg och smakfull', med exemplen 'sobra farger', 'en "
     "sober kladsel' och 'vaningens sobra elegans'. SAOL ger 'mattfull, "
     "nykter; vardad, snygg' -- alltsa bada. Tva betydelser skrivs (regel 1). "
     "🔴 DET GAMLA KORTET var missvisande: det sa 'nykter och mattlig, fri "
     "fran alkohol' och lamnade helt bort den estetiska betydelsen, som ar "
     "den enda SO tar upp och den som alla exempel visar. Mattfull och nykter "
     "inleder bada sitt led i SAOL:s forsta halva; vardad och snygg i den "
     "andra, dar snygg dessutom inleder SO:s definition.",
     grupper=[["måttfull", "nykter"], ["vårdad", "snygg", "smakfull"]])

# ----------------------------------------------------------- 28. skocka sig
satt("skocka sig",
     "Samlas tätt ihop i en större och oordnad mängd",
     "neutral, neutral",
     ["samlas"],
     "Publiken " + B % "skockade sig" + " framför scenen.",
     "till skock 'hop, flock', av fornsvenskans skokker; besläktat med "
     "tyskans Schock 'sextiotal'",
     "SO: 'samlas i storre oordnad mangd'. SAOL: 'samlas i grupper'. En "
     "betydelse. Samlas inleder bada definitionerna och ar utbytbart at bada "
     "hallen i sammanhanget, alltsa belagt enligt regel 2. syn.se:s packa "
     "sig och stocka sig saknar ordboksbelagg.")

# --------------------------------------------------------------- 29. te sig
satt("te sig",
     "Framstå eller verka på ett visst sätt för den som ser",
     "formell, neutral",
     ["framstå", "visa sig", "förefalla"],
     "Framtiden " + B % "tedde sig" + " mörk.",
     "till det äldre verbet te 'visa, uppvisa', av fornsvenskans te; "
     "besläktat med tyskans zeigen 'visa'",
     "SO: 'framsta som', med tva underbetydelser markta SYN:synonym. SAOL: "
     "'visa sig, forefalla'. En betydelse. Alla tre synonymerna ar belagda: "
     "framsta inleder SO:s definition, visa sig och forefalla inleder sina "
     "led i SAOL:s.")

# --------------------------------------------------------------- 30. stå sig
satt("stå sig",
     "Behålla sin kvalitet över tid ; alltjämt gälla ; klara sig i "
     "jämförelse med andra, där uttrycket stå sig slätt tvärtom betyder att "
     "klara sig dåligt",
     "neutral, neutral ; neutral, neutral ; neutral, neutral",
     [],
     "Hans teorier " + B % "står sig" + " ännu.",
     "till stå, i den gamla reflexiva användningen 'hålla stånd för egen "
     "räkning'; samma mönster som i ge sig och ta sig",
     "SO haller isar 'behalla sin kvalitet eller beskaffenhet', 'klara sig "
     "daligt', 'alltjamt galla' och 'klara sig'. SAOL: 'bevara sin kvalitet; "
     "fortsatt galla; klara sig'. Tre betydelser skrivs, och SO:s 'klara sig "
     "daligt' aterges dar den hor hemma: den galler bara det fasta uttrycket "
     "STA SIG SLATT, inte sta sig i allmanhet, och att skriva den som en egen "
     "betydelse hade fatt kortet att pasta motsatsen till vad det betyder. "
     "Inga belagda synonymer: alla definitioner ar flerordsfraser.")

# ----------------------------------------------------------------- 31. vina
satt("vina",
     "Susa fram med ett ihållande och genomträngande ljud ; vardagligt om "
     "att dricka vin",
     "neutral, neutral ; vardaglig, neutral",
     ["susa"],
     "Kulorna " + B % "ven" + " omkring dem.",
     "fornsvenska vina, ljudhärmande; verbet om vindrickande är däremot en "
     "sen avledning av substantivet vin",
     "SO haller isar tva: 'susa (fram) med ett ihallande och genomtrangande "
     "ljud' och 'dricka vin', den senare markt vardagligt. SAOL har bara "
     "'dricka vin' (vard.). Tva betydelser (regel 1) -- de ar dessutom skilda "
     "ord med skild harkomst, vilket etymologin skriver ut. Susa inleder "
     "SO:s forsta definition och hor bara till den gruppen.",
     grupper=[["susa"], []])


json.dump(KORT, io.open(FIL, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
skrivna = sum(1 for k in KORT if k.get("proposed"))
pausade = sum(1 for k in KORT if k.get("v3_pausad"))
print("del 4 klar: %d skrivna, %d pausade, %d kvar av 40"
      % (skrivna, pausade, 40 - skrivna - pausade))
