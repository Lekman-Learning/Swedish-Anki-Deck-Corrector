# -*- coding: utf-8 -*-
import json, urllib.parse

F = "sessions/session_2026-08-26_v3-batch2.json"
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


satt("överhalning",
     "Kraftig krängning hos ett fartyg ; genomgång och reparation av ett fartyg ; hård utskällning",
     "neutral, neutral", [],
     "Skolkarna fick en rejäl " + H("överhalning") + " av rektorn.", None,
     "SO ger tre betydelser: kraftig krängning (skeppet gjorde en överhalning åt babord), översyn "
     "och reparation av fartyg, samt skarp tillrättavisning (skolkarna fick en ordentlig "
     "överhalning av rektorn). SAOL identiskt, med tredje betydelsen som åthutning, utskällning "
     "och ämnesområdet sjö. Alla tre står på kortet.",
     tillat={"synonym_saknas_trots_belagg":
             "SAOL:s led är åthutning, utskällning — åthutning leder ledet och är belagd, men är "
             "svårare än uppslagsordet och bryter mot regeln från 2026-08-26 om att förklaringen "
             "ska ligga en nivå under ordet. Utskällning leder inget eget led och är alltså inte "
             "belagd. Tom lista är rätt svar."})

satt("rygga",
     "Ta ett steg bakåt av rädsla eller olust",
     "neutral, neutral", ["skygga"],
     "De " + H("ryggade") + " tillbaka några steg när de fick se kamphunden.", None,
     "SO (verb): (hastigt) dra sig tillbaka som reaktion på något skrämmande eller otäckt; äv. "
     "känna motvilja eller skräck för något (hon ryggade inför tanken att gå hem ensam mitt i "
     "natten); samt få häst att gå bakåt. SAOL: dra sig tillbaka; om djur: skygga, vika — skygga "
     "leder ledet och är belagd synonym.",
     tillat={"betydelse_kan_saknas":
             "SO har två skilda uppslag på formen. Kortet ger verbet, som är det ordförrådsbärande. "
             "Utelämnade: substantivet rygga (ryggsäck, en genomskinlig kortform av ett ord Adam "
             "redan kan) och ridtermen få häst att gå bakåt, som är fackspråk inom sport."})

satt("behändig",
     "Lätt att använda och lagom liten",
     "neutral, positiv", ["nätt"],
     "Hon läste boken i " + H("behändigt") + " fickformat på tåget.", None,
     "SO: som fungerar väl och med liten ansträngning, om verktyg men äv. om metoder; exempel ett "
     "behändigt redskap, en bok i behändigt fickformat, en behändig lösning på problemet. "
     "SAOL: nätt, praktisk — nätt leder ledet och är belagd. Praktisk står efter komma i samma "
     "led och är alltså inte belagd.")

satt("kooperera",
     "Arbeta tillsammans med någon mot ett gemensamt mål",
     "formell, neutral", ["samarbeta"],
     "Patienten " + H("koopererade") + " väl under hela undersökningen.", None,
     "SO och SAOL identiskt: samarbeta — utgör hela definitionen i båda och är därmed belagd "
     "synonym. SO:s exempel (patienten koopererade väl) är vårdspråk; SAOL märker ordet ekon. "
     "Domänen utelämnas eftersom de två märkningarna pekar åt olika håll.")

satt("reputerlig",
     "Som har gott rykte och är värd att lita på",
     "formell, positiv", [],
     "Banken framstod som ett " + H("reputerligt") + " företag.", None,
     "SO: som har gott anseende; exempel ett reputerligt affärsföretag. SAOL: aktningsvärd, "
     "hedersam.",
     tillat={"synonym_saknas_trots_belagg":
             "SAOL:s led är aktningsvärd, hedersam — aktningsvärd leder ledet och är belagd, men "
             "är minst lika svår som reputerlig. Regeln från 2026-08-26 säger att förklaringen ska "
             "ligga en nivå under ordet. Tom lista är rätt svar."})

satt("bolma",
     "Om rök: strömma ut i tjocka moln ; blossa kraftigt på cigarr eller pipa",
     "neutral, neutral", [],
     "Det " + H("bolmade") + " svart rök från fastigheten på andra sidan gatan.", None,
     "SO: breda ut sig i tjock och stickande form, om rök och dylikt; underbetydelse: blåsa ut "
     "tjock tobaksrök (bolma på en cigarr). SAOL har bara bruksexemplet bolma på en cigarr, utan "
     "egen definition. Båda betydelserna står på kortet.",
     tillat={"register_motsager_markning":
             "SAOL märker uppslaget matlagn., vilket inte stämmer med någon av de två "
             "betydelserna — märkningen tycks höra till ett grannuppslag (bolmört eller "
             "motsvarande). SO sätter ingen märkning alls. Registret följer SO."})

satt("dalta",
     "Behandla någon alltför snällt och skyddande",
     "neutral, lätt negativ", [],
     "Sluta " + H("dalta") + " med ligisterna!", None,
     "SO: behandla (alltför) snällt och beskyddande; exempel sluta dalta med ligisterna. "
     "SAOL: behandla alltför snällt och beskyddande. Definitionerna är i praktiken identiska och "
     "innehåller ingen utbytbar synonym — alltför bär hela valören.",
     tillat={"register_motsager_markning":
             "SAOL märker uppslaget psykol., men definitionen är allmänspråklig och SO sätter "
             "ingen fackmärkning. Ingen domän sätts."})

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 1 skriven: 7 kort. Totalt approved: %d/%d"
      % (sum(1 for e in S if e.get("approved")), len(S)))
