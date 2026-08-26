# -*- coding: utf-8 -*-
import json, urllib.parse

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}


def H(w):
    return '<font color="#3498db">' + w + '</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, tillat=None, conf=9):
    e = BY[o]
    q = urllib.parse.quote(o)
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": None, "exempelmening": ex, "etymologi": ety}
    e["sokkoll"] = {"kalla": "SO och SAOL via https://svenska.se/api/msearch?ord=" + q
                    + " (hämtat 2026-08-26, HTTP 200)", "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("romani",
     "Romernas språk, ett av Sveriges fem nationella minoritetsspråk",
     "neutral, lingvistik", ["romska"],
     "Ordet tjej är lånat från " + H("romani") + ".", None,
     "SO: ett indoariskt språk som talas av romer; exempel romani är ett av Sveriges nationella "
     "minoritetsspråk, tala romani chib. SAOL: romska — belagd synonym. "
     "🔴 OLD-facit sa 'zigenarnas språk'; zigenare är i dag en nedsättande beteckning och SO "
     "använder genomgående romer. Kortet följer ordboken, inte OLD-facit.")

satt("sejdel",
     "Stort, tjockt ölglas med handtag",
     "neutral", [],
     "Han beställde in en stor " + H("sejdel") + " starköl.", None,
     "SO: större, bastant dricksglas med handtag på ena sidan; exempel en immig sejdel skummande "
     "öl. SAOL: ett dryckeskärl för öl med handtag. Legacys ölmugg är OLD-facit men mugg antyder "
     "keramik — SO säger uttryckligen dricksglas.")

satt("skrupler",
     "Tvivel om något är rätt, som hindrar en från att göra det",
     "neutral", [],
     "Han tog pengarna utan minsta " + H("skrupler") + ".", None,
     "SAOL: samvetsbetänkligheter. Ingen SO-artikel i träffen. Samvetsbetänkligheter är SAOL:s "
     "definitionsord men klart svårare än skrupler — kortet skriver ut vad det betyder i stället, "
     "enligt regeln att förklaringen ska ligga en nivå under uppslagsordet. Ordet används nästan "
     "bara i plural och ofta nekande (utan skrupler).",
     tillat={"betydelse_kan_saknas":
             "Ingen SO-artikel finns; SAOL ger en enda definition. Kortet har den."})

satt("skräna",
     "Skrika högt och illa låtande",
     "neutral", ["skrika"],
     H("Skränande") + " supportrar stod tätt på ståplatsläktaren.", None,
     "SO: ge ifrån sig skrän; äv. i fråga om liknande djurläte (skränande måsar). SAOL: skrika, "
     "väsnas — skrika inleder ledet och är belagd synonym. SO:s definition är cirkulär (skräna = "
     "ge ifrån sig skrän), så kortet beskriver ljudet i stället.")

satt("stimulus",
     "Något utifrån som får kroppen att reagera",
     "fackspråklig, psykologi", [],
     "Allt beteende beskrevs i termer av " + H("stimulus") + " och respons.", None,
     "SO: något som framkallar kroppslig reaktion. SAOL: ngt som framkallar kroppslig reaktion, "
     "märkt psykol. Legacys retning är OLD-facit men saknar belägg som definitionsled i någon "
     "av ordböckerna.")

satt("suspendera",
     "Stänga av någon från tjänsten en tid ; tillfälligt sätta en regel ur kraft",
     "formell", [],
     "Två av tjänstemännen " + H("suspenderades") + " efter utredningen.", None,
     "SO: upphäva; spec. stänga av (ämbetsman) från tjänst; exempel de internationella "
     "sanktionerna suspenderades. SAOL: skilja ngn från tjänst för viss tid; uppskjuta; tills "
     "vidare upphäva — samt en kemisk betydelse (slamma upp partiklar) som är för fackspecifik "
     "för ett ordförrådskort.",
     tillat={"betydelse_kan_saknas":
             "SAOL:s andra uppslag (slamma upp partiklar i en vätska) är en kemiterm med eget "
             "fackspråkligt liv, avlägsen från ordets vardagliga användning. De två betydelser "
             "kortet har — avstängning och tillfälligt upphävande — är SO:s båda och täcker "
             "OLD-facit (avstänga; uppskjuta)."})

satt("svastika",
     "Hakkors — en urgammal symbol som nazismen tog över",
     "neutral", ["hakkors"],
     "Symbolen var en " + H("svastika") + " långt före 1900-talet.",
     "av sanskritens svastika, en lyckosymbol",
     "SO och SAOL identiskt: hakkors — utgör hela definitionen och är belagd synonym. SO:s "
     "etymologi: av sanskrit svastika, beteckning på lyckosymbol i form av ett hakkors. "
     "Etymologin tas med eftersom den förklarar varför symbolen finns i äldre kulturer.")

satt("tabulatur",
     "Notskrift med siffror och bokstäver som visar var fingrarna ska sitta",
     "fackspråklig, musik", [],
     "Han lärde sig låten på " + H("tabulatur") + " i stället för noter.", None,
     "SO: notskrift där tonsymbolerna utgörs av bokstäver eller siffror som anger fingrarnas "
     "placering. SAOL: notskrift av bokstäver och siffror. Legacys 'notskrift för gitarrer' är "
     "för snävt — SO knyter inte formen till ett instrument.")

satt("umbärande",
     "Att sakna det man behöver för ett drägligt liv",
     "formell", [],
     "Många dog av " + H("umbäranden") + " och sjukdomar också efter kriget.", None,
     "SO: allvarlig brist på eller försakelse av elementära förutsättningar för ett rimligt liv; "
     "samt verbet umbära: klara sig utan. SAOL: undvara, försaka. Kortet ger substantivet, som är "
     "den form OLD-facit och exemplen visar. Undvara och försaka är belagda men båda svårare än "
     "umbärande — sätts inte som synonymer.",
     tillat={"synonym_saknas_trots_belagg":
             "SAOL:s undvara och försaka är belagda men svårare än uppslagsordet; att sätta dem "
             "skulle bryta mot regeln från 2026-08-26 om att förklaringen ska ligga en nivå under "
             "ordet. Tom lista är rätt svar."})

satt("uppvigla",
     "Egga upp folk till uppror eller motstånd mot makten",
     "neutral", [],
     "Enligt polisen " + H("uppviglade") + " talaren folkmassan.", None,
     "SO: egga upp till motstånd eller uppror mot myndigheter. SAOL: hetsa till motstånd el. "
     "uppror. Legacys 'hetsa en folkmassa' är OLD-facit men missar riktningen — uppvigling sker "
     "mot en makt, inte mot vem som helst.")

satt("vals",
     "Roterande cylinder i en maskin som pressar något ; pardans i tretakt ; lögn",
     "neutral, vardaglig", [],
     "Orkestern spelade en smäktande " + H("vals") + ".", None,
     "SO ger fyra poster: cylindrisk maskindel, en pardans i 3/4-delstakt (äv. om musiken), samt "
     "lögn och ljuga/bluffa, de senare märkta vardagligt. SAOL bekräftar alla tre substantiven. "
     "🔴 De två första är HOMONYMER med olika ursprung (tyska Walze 'rulla' respektive franska "
     "valse) — de står på samma kort eftersom Framsidan är densamma.")

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 9 skriven: 11 kort. Totalt approved: %d/%d"
      % (sum(1 for e in S if e.get("approved")), len(S)))
