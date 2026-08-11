#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kör den blinda andragranskningen automatiskt — v3:s saknade steg.

## Varför filen finns

v3 har fyra steg: `applicera` -> `paket` -> **döm blint** -> `slapp`. Tre av dem
var kommandon. Det tredje var en *instruktion till en människa* ("låt en
fristående granskare fylla i verdikt"), och därför blev det aldrig gjort:
2026-08-10 stod `oberoende_verifierad` på **3 av 10 034 kort**, medan 81
färdigpackade kort låg och väntade på en dom som ingen skulle avge.

Slutsatsen är inte att någon slarvade. **Ett steg som inte går att köra blir
inte kört.** Den här filen gör steget till ett kommando som de andra tre.

## Vad som gör granskningen blind — och vad som INTE gör det

Granskaren startas som en egen `claude`-process. Tre saker måste stämma,
och den andra är den som lättast går sönder utan att synas:

1. **Tomt kontext.** Varje anrop är en ny process utan minne av hur kortet
   skrevs.
2. **Tom arbetskatalog.** Claude Code läser automatiskt in `CLAUDE.md` från
   katalogen den startas i. Körs granskaren i `anki-ord/` får den alltså hela
   metodbeskrivningen, tidigare fynd och konkreta kortexempel gratis — och är
   inte längre blind. Därför skapas en temporär katalog per körning, med
   ENBART paketdata i.
3. **Bara paketets fält.** `paket` utelämnar redan riskflaggor, sökkoll och
   det gamla innehållet.

**Ärlig begränsning:** detta är *nytt kontext, samma modell* — inte en annan
bedömare. Projektets mätning 2026-08-07 gällde självbekräftelse i samma
sittning, och det är den mekanismen som stängs här. En systematisk blind fläck
som modellen delar med sig själv fångas inte. Det är `blint_stickprov.py` mot
OLD-facit som är skyddet mot den, och det ersätter det här steget inte.

## Kostnad, och varför paketen granskas hela

Ett `claude -p`-anrop drar ~25 000 tokens bara i uppstart. Per kort hade 125
kort/dag kostat orimligt; per paket (10–25 kort) fördelas uppstarten. Kör därför
ALDRIG en post i taget.

    python blindgranska.py sessions/<paket>_v3-paket.json
    python blindgranska.py sessions/<paket>_v3-paket.json --torr   # visa prompten
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Granskaren får bara läsa sin egen katalog och slå upp ord. Inga skrivverktyg:
# den ska döma, inte rätta -- och den ska inte kunna nå projektfilerna.
TILLATNA_VERKTYG = ["Read", "WebFetch", "WebSearch"]

GRANSKARE_ID = "claude-cli-blind"

SYSTEMTILLAGG = (
    "Du är en fristående andragranskare av svenska ordkort. Du har medvetet "
    "INTE fått veta hur korten skrevs, vilka källor som slogs upp eller vad "
    "som stod på dem innan. Försök inte ta reda på det. Döm varje kort på dess "
    "egna meriter mot en riktig ordbok. Svara ALLTID med enbart JSON."
)

PROMPT = """Läs filen `paket.json` i din arbetskatalog. Den innehåller {n} svenska \
ordkort under nyckeln "poster".

{instruktion}

ARBETSGÅNG per kort:
- SLÅ UPP ORDET SJÄLVT innan du dömer. Använd WebFetch mot svenska.se:s API:
  https://svenska.se/api/search/so?q=<ordet>&exact_match=true   (SO -- avgör dagens betydelser)
  https://svenska.se/api/search/saol?q=<ordet>&exact_match=true (SAOL)
  Den gamla sid-URL:en /tri/f_so.php fungerar INTE -- sajten är en JS-app och ger tom sida.
- Fältet "facit" är en ANDRA källa, aldrig den enda. "facit_signal" är en FRÅGA
  att avgöra, inte ett konstaterat fel.
- Misslyckas en uppslagning: skriv det uttryckligen i anmärkningen och döm försiktigt.

"godkand" betyder att du själv skulle låta någon lära sig ordet från kortet.

SVARA MED ENBART JSON, ingen text före eller efter, exakt denna form:
[{{"noteId": <int>, "ord": "<ord>", "verdikt": "godkand" eller "underkand", \
"anmarkning": "<konkret motivering på svenska; vid underkänt: vad som är fel och vad det borde vara>"}}]

Alla {n} posterna ska vara med."""


def _claude_binar():
    """Full sökväg till claude.

    På Windows är `claude` tre filer i npm-katalogen (`claude`, `claude.cmd`,
    `claude.ps1`) och ingen av dem är en .exe. `subprocess` utan `shell=True`
    hittar inte .cmd, och MED `shell=True` slås argumentlistan ihop till en
    sträng -- varpå prompten (som innehåller citattecken, radbrytningar och
    JSON-exempel) sönderdelas av skalet. Första försöket gav ett tomt svar och
    en JSONDecodeError som såg ut som ett modellfel men var ett citeringsfel.
    Peka därför ut .cmd-filen explicit och kör utan skal.
    """
    if os.name == "nt":
        for kandidat in (os.path.join(os.environ.get("APPDATA", ""), "npm", "claude.cmd"),
                         shutil.which("claude.cmd"), shutil.which("claude")):
            if kandidat and os.path.exists(kandidat):
                return kandidat
        raise RuntimeError("hittar inte claude.cmd -- npm install -g @anthropic-ai/claude-code")
    binar = shutil.which("claude")
    if not binar:
        raise RuntimeError("hittar inte claude på PATH")
    return binar


def _kor_granskare(poster, instruktion, modell, timeout):
    """Startar en fristående claude-process i en TOM katalog. Se docstring."""
    arbetsrum = tempfile.mkdtemp(prefix="blindgranskning_")
    try:
        # Endast paketdata följer med. Ingen CLAUDE.md, inga projektfiler.
        with open(os.path.join(arbetsrum, "paket.json"), "w",
                  encoding="utf-8") as f:
            json.dump({"poster": poster}, f, ensure_ascii=False, indent=2)

        # Hela instruktionen läggs i en FIL, inte på kommandoraden. På Windows
        # är `claude` en .cmd-wrapper, och kommandoraden kapas vid ~8 000
        # tecken -- prompten med granskningsinstruktionen ligger över det.
        # Symptomet var lömskt: returkod 0, stdout med innehåll, men inte den
        # JSON som --output-format lovar. Varje flagga fungerade var för sig,
        # vilket pekade bort från längden. Kommandoraden hålls nu kort.
        with open(os.path.join(arbetsrum, "instruktion.md"), "w",
                  encoding="utf-8") as f:
            f.write(PROMPT.format(n=len(poster), instruktion=instruktion.strip()))
        prompt = ("Läs `instruktion.md` i din arbetskatalog och följ den exakt. "
                  "Den beskriver en granskningsuppgift och vilket format svaret "
                  "ska ha.")
        cmd = [_claude_binar(), "-p", prompt,
               "--output-format", "json",
               "--allowedTools", *TILLATNA_VERKTYG,
               "--permission-mode", "acceptEdits",
               "--strict-mcp-config",
               "--append-system-prompt", SYSTEMTILLAGG]
        if modell:
            cmd += ["--model", modell]

        r = subprocess.run(cmd, cwd=arbetsrum, capture_output=True,
                           text=True, encoding="utf-8", errors="replace",
                           timeout=timeout)
        if r.returncode != 0 or not (r.stdout or "").strip():
            raise RuntimeError(
                "claude gav inget användbart svar (returkod %s).\n  stderr: %s\n  stdout: %s"
                % (r.returncode, (r.stderr or "")[:500], (r.stdout or "")[:500]))
        return json.loads(r.stdout)
    finally:
        shutil.rmtree(arbetsrum, ignore_errors=True)


def _plocka_json(text):
    """Granskaren ombeds svara med ren JSON men kan lägga text runt."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    m = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", text, re.S)
    if m:
        return json.loads(m.group(1))
    m = re.search(r"(\[\s*\{.*\}\s*\])", text, re.S)
    if m:
        return json.loads(m.group(1))
    raise ValueError("hittade ingen JSON i granskarens svar:\n" + text[:600])


def granska(paketsokvag, modell=None, timeout=2400, torr=False):
    data = json.load(open(paketsokvag, encoding="utf-8"))
    poster = data["poster"]
    kvar = [p for p in poster if not p.get("verdikt")]
    if not kvar:
        print("Alla %d poster har redan verdikt -- inget att göra." % len(poster))
        return 0

    # Skicka BARA de fält granskaren ska se. Att lita på att paketfilen redan
    # är rensad räcker inte: fälten plockas ut explicit här, så ett nytt fält i
    # `paket` inte tyst kan börja läcka in i granskningen.
    blint = [{"noteId": p["noteId"], "ord": p["ord"], "facit": p.get("facit"),
              "facit_signal": p.get("facit_signal"), "kort": p["kort"]}
             for p in kvar]

    print("Blindgranskar %d poster ur %s" % (len(blint), os.path.basename(paketsokvag)))
    if torr:
        print("\n--- vad granskaren far se (forsta posten) ---")
        print(json.dumps(blint[0], ensure_ascii=False, indent=2))
        print("\n--- prompt ---")
        print(PROMPT.format(n=len(blint), instruktion=data.get("instruktion", "")))
        return 0

    svar = _kor_granskare(blint, data.get("instruktion", ""), modell, timeout)
    if svar.get("is_error"):
        print("AVBRYTER: granskaren felade: %s" % svar.get("result"))
        return 1
    domar = {int(d["noteId"]): d for d in _plocka_json(svar["result"])}

    saknas = [p["ord"] for p in kvar if int(p["noteId"]) not in domar]
    if saknas:
        print("AVBRYTER: granskaren dömde inte %d av %d poster (%s).\n"
              "  Ett halvt paket får inte skrivas in -- kör om."
              % (len(saknas), len(kvar), ", ".join(saknas[:8])))
        return 1

    utan_skal = [d["ord"] for d in domar.values()
                 if d.get("verdikt") == "underkand" and not (d.get("anmarkning") or "").strip()]
    if utan_skal:
        print("AVBRYTER: %d underkända saknar anmärkning (%s)."
              % (len(utan_skal), ", ".join(utan_skal[:8])))
        return 1

    # ALLA SPARRAR MASTE LIGGA FORE SKRIVNINGEN. Forsta versionen av
    # uppslagsspärren nedan lag EFTER json.dump och skrev darfor ut
    # "Inget har sparats" -- efter att ha sparat. Ett meddelande som beskriver
    # nagot annat an vad koden gjorde ar samma felklass som resten av projektet
    # jagar; upptackt 2026-08-10 direkt efter att spärren lagts in.
    # Tröskeln var först `turer <= 1` -- byggd för att fånga det uppenbara
    # fallet "svarade utan att röra ett verktyg". Den visade sig för svag
    # 2026-08-11: en körning på 25 kort returnerade **2 turer** och slank
    # igenom. Två turer räcker för att läsa paketfilen och skriva ett svar,
    # alltså i praktiken samma sak som noll uppslagningar.
    #
    # Att domarna var obelagda gick att bevisa, inte bara misstänka: granskaren
    # underkände *lumpen* för "sakfel i etymologin", men etymologin på kortet
    # var ordagrant SO:s egen text ("av tyska Lumpen-, i sammansättn.,
    # 'ynklig'"). En granskare som faktiskt hämtat SO hade sett det. Den
    # resonerade i stället ur eget minne om tyska -- och lät precis lika säker
    # som den granskning som gjort 51 turer.
    #
    # Det är hela poängen med lagret: en obelagd dom SER likadan ut som en
    # belagd. Tröskeln måste därför skala med antalet kort, inte vara ett
    # fast litet tal. Kravet är ungefär en tur per fyra kort, med golv 5 --
    # väl under vad en verklig körning gör (del 1 samma dag: 51 turer på 25
    # kort) men långt över vad ett minnessvar producerar.
    turer = svar.get("num_turns") or 0
    krav = max(5, len(kvar) // 4)
    if turer < krav:
        print("AVBRYTER: granskaren gjorde bara %d turer på %d kort (kräver >= %d).\n"
              "  Så få turer betyder att uppslagningarna aldrig gjordes, och verdikten\n"
              "  vilar då på modellens minne i stället för på SO/SAOL. En obelagd dom\n"
              "  ser exakt likadan ut som en belagd -- därför får den inte skrivas in.\n"
              "  Kontrollera att WebFetch är tillåten och att svenska.se svarar,\n"
              "  och kör om. Inget har sparats." % (turer, len(kvar), krav))
        return 1

    for p in poster:
        d = domar.get(int(p["noteId"]))
        if d:
            p["verdikt"] = d["verdikt"]
            p["anmarkning"] = d.get("anmarkning") or ""
    data["granskare"] = GRANSKARE_ID
    # TURANTALET SPARAS, inte bara skrivs ut. Fram till 2026-08-11 fanns siffran
    # bara i terminalutskriften -- så när en körning visade sig ha dömt 25 kort
    # på 2 turer gick det inte att i efterhand kontrollera om NÅGON tidigare
    # granskning haft samma problem. Domarna loggades, men inte hur väl belagda
    # de var, vilket gör att alla `oberoende_verifierad`-kort ser lika starka ut.
    # Samma lucka som `raw-verktyg/` och `raw-websearch/` finns för att stänga:
    # slutsatsen sparades, mätningen bakom den kastades.
    data["granskning_turer"] = turer
    data["granskning_kostnad_usd"] = svar.get("total_cost_usd")
    data["granskning_turkrav"] = krav
    json.dump(data, open(paketsokvag, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    g = sum(1 for d in domar.values() if d["verdikt"] == "godkand")
    u = len(domar) - g
    kostnad = svar.get("total_cost_usd")
    print("\n%d godkända, %d underkända (%.0f %% underkänt)  --  %d turer%s"
          % (g, u, 100.0 * u / len(domar), turer,
             ", %.2f USD" % kostnad if kostnad else ""))
    for d in domar.values():
        if d["verdikt"] == "underkand":
            print("  UNDERKÄND %-16s %s" % (d["ord"], (d.get("anmarkning") or "")[:150]))
    print("\nSkrivet till %s. Kör nu:\n"
          "  python kortgranskare.py verdikt %s" % (paketsokvag, paketsokvag))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paket", help="sessions/<namn>_v3-paket.json")
    ap.add_argument("--modell", default=None, help="t.ex. claude-opus-5")
    ap.add_argument("--timeout", type=int, default=2400)
    ap.add_argument("--torr", action="store_true",
                    help="visa vad granskaren skulle få se, kör ingenting")
    ap.add_argument("--tillat-api", action="store_true",
                    help="tillåt körning även om en API-nyckel finns i miljön "
                         "(kostar pengar per anrop -- normalt går allt på prenumerationen)")
    a = ap.parse_args()
    if not shutil.which("claude") and os.name != "nt":
        print("AVBRYTER: 'claude' finns inte på PATH. "
              "npm install -g @anthropic-ai/claude-code")
        return 1

    # Prenumerationsspärren (Adams krav 2026-08-10: "hoppas vi enbart använder
    # claude subscription och inte api"). Claude Code väljer API-fakturering om
    # en nyckel finns i miljön, och gör det TYST -- utskriften ser likadan ut,
    # bara `total_cost_usd` blir en riktig kostnad i stället för en omräkning.
    # 125 kort/dag är precis den volym där skillnaden hade märkts på fakturan
    # långt innan den märkts i loggen. Hellre stopp än överraskning.
    for nyckel in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN"):
        if os.environ.get(nyckel):
            print("AVBRYTER: %s är satt, vilket gör att körningen skulle "
                  "faktureras via API i stället för att gå på prenumerationen.\n"
                  "  Ta bort variabeln, eller kör med --tillat-api om det är avsiktligt."
                  % nyckel)
            if not a.tillat_api:
                return 1
    return granska(a.paket, a.modell, a.timeout, a.torr)


if __name__ == "__main__":
    sys.exit(main())
