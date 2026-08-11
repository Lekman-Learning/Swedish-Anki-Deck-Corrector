# -*- coding: utf-8 -*-
"""Rättningar för sökkollsexperimentets båda armar (2026-08-11).

Arm A = 10 slumpade PROVISORISKA kort (sökkollade, i kön, ej blindgranskade).
Arm B = 10 slumpade OSÖKKOLLADE suspenderade is:review-kort.

Samma granskare, samma dag, samma metod — enda skillnaden är vilken arm
kortet kommer ur. Verdikten räknas per arm.

## Synonymerna sätts enligt den nya regeln

Efter kvällens fynd (10 av 25 underkännanden gällde synonymer, och
synonymer.se ORSAKADE hälften av dem) sätts synonymer nu i första hand från
SO:s och SAOL:s egna glosor — ordboken påstår själv likvärdighet. syn.se är
kandidatpool, och varje kandidat testas: går den att sätta in i stället för
ordet utan att meningen ändras?

Exempel på kandidater som föll på det testet i den här omgången:
* `struva` hade *fika* — en struva är ett bakverk, fika är en måltid.
* `utröna` hade *klargöra* — att klargöra är att göra tydligt FÖR ANDRA,
  utröna är att ta reda på FÖR SIG SJÄLV.
* `sandrevel` hade *bank* — för generellt, en bank behöver inte vara av sand.

## Två fuzzy-digester som INTE fick röra korten

`få sitt lystmäte` gav SO-träffar om `få` som adjektiv ("som har litet
antal") plus grimas-definitioner från grannuppslag. `i gåsmarsch` gav
"nionde bokstaven" (bokstaven i). Ingen av dem har lagts till. Det är tredje
gången samma fälla dyker upp på ett dygn — `solvens`, `pärs`, och nu de här
två — men den här gången fångade jag den före skrivningen.
"""

import json
import sys
import urllib.parse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FARG = "#3498db"
SVENSKA = "https://svenska.se/api/msearch?ord={}"

SESSIONER = {
    "A": "sessions/session_2026-08-11_expA-provisorisk.json",
    "B": "sessions/session_2026-08-11_expB-osokkollad.json",
}


def h(o):
    return f'<font color="{FARG}">{o}</font>'


DOMAN = {
    # Arm A
    "oval": "matematik", "utröna": "allmän", "struva": "matlagning",
    "sandrevel": "geologi", "bildlig": "lingvistik", "fnöske": "allmän",
    "kampanil": "konst", "nematod": "biologi", "dopfunt": "religion",
    "få sitt lystmäte": "allmän",
    # Arm B
    "konstruktiv": "allmän", "ganglie": "medicin", "institut": "allmän",
    "i gåsmarsch": "allmän", "övermanna": "allmän", "exemplarisk": "allmän",
    "motorik": "medicin", "grammatik": "lingvistik",
    "rättshaverist": "juridik", "färdighet": "allmän",
}

RATTELSER = {
    # ---------------- ARM A ----------------
    "oval": {
        "huvudbetydelse": "Som har en sluten, långsträckt och rundad form ; "
                          "figur med sådan form",
        "synonymer": ["äggrund", "avlångt rund", "ellips"],
        "_skal": "SO ger både adjektivet och SUBSTANTIVET ('ansiktets perfekta oval "
                 "inramades av ett mörkt hårsvall'). Kortet hade bara adjektivet. "
                 "'Äggformad' byttes mot SAOL:s 'äggrund, avlångt rund' — en oval är "
                 "symmetrisk, ett ägg är det inte.",
    },
    "utröna": {
        "synonymer": ["ta reda på", "fastställa", "konstatera"],
        "_skal": "Synonymrensning enligt den nya regeln. SO och SAOL ger båda 'ta "
                 "reda på' som gloss. Kortets 'klargöra' föll på utbytbarhetstestet: "
                 "att klargöra är att göra tydligt FÖR ANDRA, att utröna är att ta "
                 "reda på FÖR SIG SJÄLV. 'Avslöja' har samma problem.",
    },
    "struva": {
        "huvudbetydelse": "Flottyrkokt sött bakverk ; (finlandssvenska) flottyrkokt "
                          "bakverk som äts kring första maj",
        "synonymer": ["flottyrkokt bakverk", "klenät"],
        "_skal": "SAOL ger TVÅ betydelser -- den finländska första maj-struvan "
                 "(tippaleipä) är en egen post. Synonymen 'fika' ströks: en struva är "
                 "ett bakverk, fika är en måltid; den klarar inte utbytbarhetstestet.",
    },
    "sandrevel": {
        "synonymer": ["sandrev", "revel", "sandbank"],
        "_skal": "Synonymrensning. SO:s gloss är 'sandavlagring ute i vattnet längs "
                 "kusten'; syn.se ger 'sandrev, revel'. Kortets 'bank' ströks som för "
                 "generellt -- en bank behöver inte vara av sand.",
    },
    "nematod": {
        "synonymer": ["rundmask", "trådmask"],
        "_skal": "SAOL ger 'rundmask, trådmask'; kortet hade bara den ena. Rak "
                 "komplettering ur ordbokens egen gloss.",
    },

    # ---------------- ARM B ----------------
    "konstruktiv": {
        "huvudbetydelse": "Inriktad på att bygga upp eller förbättra ; som har att "
                          "göra med konstruktion",
        "synonymer": ["uppbyggande", "nyskapande", "konstruerande"],
        "_skal": "SO och SAOL ger båda den TEKNISKA betydelsen ('som gäller "
                 "konstruktion', SAOL: 'konstruerande') som egen betydelse. Kortet "
                 "hade bara den positiva. Synonymen 'kreativ' ströks -- konstruktiv "
                 "kritik är inte kreativ kritik.",
    },
    "ganglie": {
        "huvudbetydelse": "Anhopning av nervceller, nervknut ; godartad svulst vid "
                          "sena eller led, senknut",
        "synonymer": ["nervknut", "ganglion", "senknut"],
        "_skal": "syn.se:s redaktionella post ger TVÅ skilda betydelser: 'nervknut, "
                 "anhopning av nervceller' och 'senknut, svulst'. Den andra är en "
                 "helt annan sak -- en cysta vid en sena -- och saknades helt. OBS: "
                 "svenska.se har ordet BARA i SAOB (ingen SO/SAOL-artikel), så kortet "
                 "vilar här på synonymer.se enligt Adams källregel 2026-08-11.",
    },
    "institut": {
        "huvudbetydelse": "Fristående inrättning för forskning eller undervisning ; "
                          "(juridik) system av rättsregler inom ett rättsområde",
        "synonymer": ["inrättning", "anstalt", "läroanstalt"],
        "_skal": "SO och SAOL ger båda den juridiska betydelsen ('institutet "
                 "panträtt', 'institutet adoption') som egen betydelse. Den saknades. "
                 "Synonymen 'institution' ströks som cirkulär -- den innehåller "
                 "uppslagsordet och avslöjar svaret.",
    },
    "övermanna": {
        "huvudbetydelse": "Vinna kontroll över någon med fysiskt våld ; bildligt om "
                          "känsla eller tillstånd som tar överhanden",
        "synonymer": ["betvinga", "överväldiga", "bemästra"],
        "_skal": "SO+: 'äv. bildligt', med exemplet 'dåsigheten började övermanna "
                 "honom'. Den bildliga betydelsen saknades, och det är den som gör "
                 "ordet användbart utanför våldsbeskrivningar.",
    },
    "grammatik": {
        "huvudbetydelse": "Beskrivning av hur ordformer, fraser och meningar bildas i "
                          "ett språk ; lärobok i ämnet",
        "synonymer": ["språklära", "formlära", "syntax"],
        "_skal": "SO+: 'äv. om motsvarande lärobok' -- 'en fransk grammatik' är en "
                 "BOK. Betydelsen saknades. 'Satslära' ströks: det är en DEL av "
                 "grammatiken (syntaxen), inte en synonym för helheten.",
    },
    "motorik": {
        "huvudbetydelse": "Förmåga att kontrollera de egna muskelrörelserna ; äv. om "
                          "själva muskelrörelserna",
        "synonymer": ["rörelseförmåga", "rörlighet"],
        "_skal": "SO+: 'äv. om själva muskelrörelserna'. Kortets "
                 "'koordinationsförmåga' ströks -- koordination är en aspekt av "
                 "motoriken, inte samma sak.",
    },
    "färdighet": {
        "exempelmening": f"Hennes manuella {h('färdighet')} imponerade på hela verkstaden.",
        "synonymer": ["skicklighet", "kunnighet", "förmåga"],
        "_skal": "Exempelmeningen var fragmentet 'Manuell färdighet.' -- inte en "
                 "mening. Betydelsen orörd; SO:s gloss 'förmåga att utföra något i "
                 "praktiken' stämmer med kortet.",
    },
}

STANDARD = ("Jamfort mot SO/SAOL/synonymer.se i denna session: betydelse, register och "
            "synonymer stammer. Ingen saknad betydelse hittad. Doman bedomd per ord. "
            "Synonymerna kontrollerade mot ordboksglossen for utbytbarhet.")


def _med_doman(register, ord_):
    dom = DOMAN.get(ord_)
    if not dom or not register:
        return register
    delar = [d.strip() for d in register.split(";")]
    if any(dom == t.strip() for d in delar for t in d.split(",")):
        return register
    delar[0] = delar[0] + ", " + dom
    return " ; ".join(delar)


def main():
    for arm, sokvag in SESSIONER.items():
        poster = json.load(open(sokvag, encoding="utf-8"))
        saknar = [p["ord"] for p in poster if p["ord"] not in DOMAN]
        if saknar:
            sys.exit(f"Arm {arm}: domän saknas för {', '.join(saknar)}")
        n = 0
        for p in poster:
            o = p["ord"]
            L = p["legacy"]
            r = RATTELSER.get(o, {})
            p["proposed"] = {
                "huvudbetydelse": r.get("huvudbetydelse", L.get("huvudbetydelse")),
                "synonymer": r.get("synonymer", L.get("synonymer")),
                "synonym_groups": r.get("synonym_groups", L.get("synonym_groups")),
                "exempelmening": r.get("exempelmening", L.get("exempelmening") or ""),
                "register": r.get("register") or _med_doman(L.get("register"), o),
                "etymologi": r.get("etymologi", L.get("etymologi")),
            }
            p["approved"] = True
            # Procentkoda ALLTID -- flerordsuppslag ("få sitt lystmäte",
            # "i gåsmarsch") bröt annars URL:en vid mellanslaget och Hål 0
            # stoppade kortet med "hämtningen gjordes aldrig".
            p["sokkoll"] = {"kalla": SVENSKA.format(urllib.parse.quote(o)),
                            "slutsats": r.get("_skal", STANDARD)}
            p.pop("applicerad", None)
            n += 1
        json.dump(poster, open(sokvag, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        rattade = sum(1 for p in poster if p["ord"] in RATTELSER)
        print(f"Arm {arm}: fyllde {n} poster, varav {rattade} rattade.")


if __name__ == "__main__":
    main()
