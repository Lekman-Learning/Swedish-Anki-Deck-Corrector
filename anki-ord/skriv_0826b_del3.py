# -*- coding: utf-8 -*-
"""Rättar de 11 hårda anmärkningarna från förgranskningen."""
import json

F = "sessions/session_2026-08-26_v3-batch2.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}


def tillat(o, **kv):
    BY[o].setdefault("forgranska_tillat", {}).update(kv)


# --- reputerlig: ordboken har rätt, registret ändras ---------------------
BY["reputerlig"]["proposed"]["register"] = "ngt ålderdomlig, positiv"
BY["reputerlig"]["sokkoll"]["slutsats"] += (
    " 🔴 REGISTER RÄTTAT efter förgranskning: SO märker ordet något ålderdomligt. "
    "Kortet sa först formell — ordboken går före min egen känsla för ordet.")

# --- pakt: domänen saknar stöd i SO, stryks ------------------------------
BY["pakt"]["proposed"]["register"] = "neutral, neutral"
BY["pakt"]["sokkoll"]["slutsats"] += (
    " Domänen politik stryks: SO sätter ingen fackmärkning och ordet är vanligt "
    "(popularitet 8556). SAOL:s mil. gäller den militära underanvändningen, inte ordet.")

# --- rygga: märkningen tillhör substantivet, inte verbet -----------------
tillat("rygga", register_motsager_markning=(
    "Märkningen vardagligt/vard. sitter på SO:s och SAOL:s SUBSTANTIV-uppslag rygga = "
    "ryggsäck, en vardaglig kortform. Verbet rygga (dra sig tillbaka) är omärkt i båda "
    "ordböckerna. Kortet ger verbet, så neutral är rätt register."))

# --- kooperera: 'mindre brukligt' är frekvens, inte stilnivå -------------
tillat("kooperera", register_motsager_markning=(
    "SO:s markering är mindre brukligt — ett påstående om hur ofta ordet används, inte "
    "om vilken stilnivå det har. Valvets stilnivåaxel har ingen sådan etikett. Ordet lever "
    "i vård- och ekonomispråk (SO:s eget exempel: patienten koopererade väl), vilket är "
    "grunden för formell. Ingen stilmärkning motsägs."))

# --- betydelse_kan_saknas: bruksuppgifter räknas som betydelser ----------
tillat("överhalning", betydelse_kan_saknas=(
    "SO:s sex poster är tre betydelser plus tre tillägg: underbetydelsen det att tappa "
    "balansen (han gjorde en överhalning framåt) är samma krängning applicerad på en "
    "människa, och två bruksuppgifter. Alla tre SJÄLVSTÄNDIGA betydelser står på kortet."))

tillat("behändig", betydelse_kan_saknas=(
    "SO:s andra post är bruksuppgiften om verktyg etc. men äv. om metoder och dylikt — "
    "den säger var ordet används, inte vad det betyder. Kortet har SO:s enda definition."))

tillat("bolma", betydelse_kan_saknas=(
    "SO:s tredje post är bruksuppgiften om rök och dylikt, som talar om vad subjektet "
    "brukar vara. Den står inbakad i kortets första led (Om rök:). De två faktiska "
    "betydelserna — röken som väller ut och rökaren som blåser ut den — finns båda."))

tillat("inkurant", betydelse_kan_saknas=(
    "SO:s tre poster är en definition (som inte längre är gångbar), en underbetydelse "
    "(som saknar ekonomiskt värde) och en bruksuppgift. Underbetydelsen är följden av "
    "huvudbetydelsen, inte en skild betydelse: en vara som inte går att sälja saknar "
    "därmed värde. Kortet täcker båda i en formulering."))

tillat("pakt", betydelse_kan_saknas=(
    "SO:s andra post är bruksuppgiften vanligen mellan stater; ofta om samarbete av "
    "militär natur — den preciserar vilka som ingår pakter, inte vad ordet betyder. "
    "Den står inbakad i kortets oftast mellan stater."))

tillat("sfär", betydelse_kan_saknas=(
    "SO:s tre poster är definitionen, en lång bruksuppgift om ytans form kontra det inre, "
    "och idiomet hennes privata sfär. Kortet har den geometriska betydelsen och den "
    "bildliga — alltså båda de betydelsebärande, med bruksuppgiften utelämnad."))

tillat("svada", betydelse_kan_saknas=(
    "SO:s andra post är bruksuppgiften vanligen utan mer väsentligt innehåll. Den är inte "
    "en andra betydelse utan valören i den första, och den står inbakad i kortets men "
    "säger lite."))

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 3: 11 anmärkningar hanterade.")
