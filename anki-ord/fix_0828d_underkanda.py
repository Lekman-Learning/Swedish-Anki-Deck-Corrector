# -*- coding: utf-8 -*-
"""Rattar underkanda kort ur v3-batch5 (del1)."""
import io
import json

FIL = "sessions/session_2026-08-28_v3-batch5.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}


def ratta(o, bet, reg, syn=None, not_=None):
    e = BY[o]
    p = e["proposed"]
    p["huvudbetydelse"] = bet
    p["register"] = reg
    if syn is not None:
        p["synonymer"] = syn
    if not_:
        e["sokkoll"]["slutsats"] += " " + not_
    assert len(bet.split(" ; ")) == len(reg.split(" ; ")), o


ratta("krum",
      "Om kropp eller rygg: krökt framåt av ålder, sjukdom eller tungt "
      "arbete ; också om växter: krokvuxen ; som substantiv: själva kröken "
      "— \"med ryggen i krum\"",
      "neutral, neutral, allmän ; neutral, neutral, biologi ; neutral, "
      "neutral, allmän",
      not_="RATTAT efter blindgranskning, TVA fel i ett kort. (1) Min "
           "formulering 'krokig i formen' var for bred -- SO:s samtliga "
           "exempel pa adjektivet ar kroppsliga (krumma ben, en krum kropp, "
           "ryggen krum), sa 'en krum pinne' hade blivit inlart som "
           "godkant. Facit ar nu forankrat i kroppen. (2) Samtidigt hade "
           "jag SLAGIT IHOP bort SO:s underbetydelse 'av. om vaxt' (SO:s "
           "eget exempel: 'krumma trad'), som nu ar en egen betydelse. "
           "Kortet var alltsa for brett och for smalt pa en gang. NOT: "
           "granskaren skrev att ordet ar avgransat till kropp -- det ar en "
           "overdrift at andra hallet, for SO:s aldsta belagg (1560) galler "
           "ett oxhorn och vaxtbetydelsen ar uttrycklig. Facit foljer SO, "
           "inte granskarens skarpning.")

ratta("subtil",
      "Så fin att den knappt märks — man måste vara uppmärksam för att "
      "uppfatta den ; om ett resonemang eller ett sätt att uttrycka sig: "
      "förfinat och skarpsinnigt, med antydningar i stället för raka besked",
      "neutral, neutral, allmän ; neutral, neutral, allmän",
      not_="RATTAT efter blindgranskning, TVA fel. (1) Ordet 'forsiktig' ar "
           "STRUKET ur facit -- det stod i ingen kalla. Subtil handlar om "
           "finhet och forfining, inte om forsiktighet, och den inlasningen "
           "hade lart in fel nyans. (2) Jag skrev uttryckligen i den forsta "
           "sokkollen att jag UTELAMNADE SAOL:s 'sofistikerad, spetsfundig' "
           "med motiveringen att den anvandningen ar sallsynt i svenskan. "
           "Det var fel: SO:s egen exempelmening ar just den ('han talar "
           "inte sa oppet utan mera subtilt med antydningar'), och latinets "
           "subtilis ges av SO sjalv som 'fin; harfin; SKARPSINNIG'. "
           "Betydelsen ar nu med. Tredje gangen samma dag som jag skar bort "
           "en betydelse och skrev ut att jag gjorde det -- att dokumentera "
           "en hopslagning gor den inte riktig.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("rattade 2 kort")

# ---- del2 ----
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}

ratta("notabel",
      "Värd att lägga märke till — tillräckligt ovanlig för att nämnas ; om "
      "en person: framstående och av hög samhällsställning",
      "formell, neutral, allmän ; formell, positiv, allmän",
      not_="RATTAT efter blindgranskning: personbetydelsen saknades helt. "
           "SAOL:s definition ar 'marklig; bemarkt, fornam' -- jag las "
           "andra halvan som glosor att INTE ta som synonymer (vilket var "
           "ratt) men drog fel slutsats av det och strok betydelsen ocksa. "
           "Att ett ord inte duger som synonym betyder inte att betydelsen "
           "det pekar pa saknas. Jfr slaktordet notabilitet 'framstaende "
           "person' och uttrycket 'notabla gaster'.")

ratta("tabelras",
      "Fullständig förödelse: att allt jämnas med marken och ingenting "
      "lämnas kvar",
      "ngt ålderdomlig, negativ, allmän",
      not_="RATTAT efter blindgranskning: bade facit och valensen var for "
           "mjuka. SO sager 'total forstorelse' och SAOL 'fullstandig "
           "forodelse' -- jag skrev 'allt sopas bort och man borjar om fran "
           "noll', vilket gor ordet till en nystart, och satte valensen "
           "till neutral. Felet kom av att jag lat ETYMOLOGIN styra facit: "
           "latinets tabula rasa (den utplanade vaxtavlan) bar mycket riktigt "
           "en nystart, men det svenska ordet har inte foljt med dit. Samma "
           "sorts overtolkning som pa singular i foregaende batch, dar jag "
           "lat synonymen styra facit. NOT: granskaren skriver att SAOL "
           "taggar ordet 'mil.' -- den markningen syns INTE i uppslaget, "
           "som ger 'mindre brukligt' och 'ald.'. Nagon militar doman ar "
           "darfor inte inskriven.")
BY["tabelras"]["proposed"]["exempelmening"] = (
    "Efter branden var det " + '<font color="#3498db">%s</font>' % "tabelras"
    + " i hela kvarteret.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("rattade 2 kort till (notabel, tabelras)")
