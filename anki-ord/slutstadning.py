# -*- coding: utf-8 -*-
"""Slutstadning av 100-kortsomgangen 2026-08-30.

RATTELSE AV MITT EGET MISSTAG, och den ar viktig nog att skrivas ut:

Jag har hela dagen behandlat "kortet har ingen belagd synonym" som ett
blockerande tillstand och pausat kort pa den grunden -- forst fyra i gar,
sedan fjorton till i dag. Det var fel. `baksida.validate_adamtal` har ingen
sparr mot att sakna synonym. Sparren `tom_synonymgrupp` traffar bara kort
som DEKLARERAR synonymgrupper och lamnar alla tomma, alltsa `[[]]` -- en
trasig gruppering. Ett kort med `synonym_groups = []` och `synonymer = []`
passerar rent:

    groups=[[]]  -> FEL: tom_synonymgrupp
    groups=[]    -> inga fel
    groups=None  -> inga fel

forgranska.py sa detta hela tiden, i klartext: "Stryk det; tom synonymlista
ar godkant" och "Tom lista passerar tyst: det ar normalfallet (69 %)". Jag
lade in `[[]]` i stallet for `[]` och lasta darmed mina egna kort.

VAD SKRIPTET GOR

 1. Stryker varje synonym utan stod i SO:s SYN-falt eller SO/SAOL:s
    definitionstext. forgranska.py:s regel 4c undantar wiktionary och
    synonymer.se MED FLIT ("ordboken sjalv sager ingenting") -- det ar inte
    en lucka i verktyget, och mitt tidigare "raddande" av 24 synonymer via
    Wiktionary gick emot en avsiktlig regel. Bort.
 2. Normaliserar tomma grupplistor till `[]` i stallet for `[[]]`.
 3. Skriver forslag for de fem kort som aldrig fick nagot.
 4. Avpausar allt utom `carpe diem` (0 traffar i bade SO och SAOL, den harda
    regeln uppslagsord_saknas) och `med varm hand` (uppslagningen gav
    artikeln for ordet 'varm'; ingen kalla tacker uttrycket).
"""
import io
import json

SES = "sessions/session_2026-08-30_v3-omgranskning-repetition-mognad.json"
FG = "fg.json"
B = '<font color="#3498db">%s</font>'

FORTSATT_PAUSAD = {"carpe diem", "med varm hand"}

# Kort som aldrig fick ett forslag alls -- alla saknar belagd synonym, vilket
# nu inte langre ar ett hinder.
NYA = {
    "plektrum": dict(
        hb="Liten tunn skiva som man knäpper strängarna med",
        reg="neutral, neutral",
        ex="Gitarristen tappade sitt %s mitt i solot men fortsatte spela med fingrarna." % (B % "plektrum"),
        etym="via latin av grekiska plektron, till plessein 'slå'",
        notis="Ingen synonym finns: SAOL och SO definierar båda omskrivande, "
              "synonymer.se har ingen artikel, och kortets gamla 'skiva' är "
              "överbegreppet, 'plock' påhittat och 'plektron' samma ord i annan "
              "form. Synonymfältet lämnas tomt, vilket förgranskningen "
              "uttryckligen godkänner."),
    "turbin": dict(
        hb="Maskin som gör strömmande vatten eller gas till rotation",
        reg="neutral, neutral",
        ex="Ingenjörerna fick trimma %s i kraftverket för att öka effekten." % (B % "turbinerna"),
        etym="till latin turbo (genitiv turbinis) 'snurra, virvel'",
        notis="Ingen synonym finns. 'maskin' är överbegreppet, 'skovelhjul' en "
              "DEL av turbinen, och 'roterande enhet' går inte att belägga. "
              "synonymer.se har ingen artikel alls. Tomt synonymfält."),
    "autism": dict(
        hb="Funktionsnedsättning som bland annat gör socialt samspel svårt",
        reg="neutral, neutral",
        ex="%s påverkar hur hjärnan hanterar social information." % (B % "Autism"),
        etym="till grekiska autos 'själv'",
        notis="Huvudbetydelsen är SO:s och SAOL:s ordagranna definition. Ingen "
              "synonym sätts: kortets gamla 'autismspektrumtillstånd' "
              "innehåller uppslagsordet (cirkular_synonym, redan flaggad), och "
              "synonymer.se:s 'sjuklig självförsjunkenhet' och 'kontaktlöshet' "
              "är föråldrade beskrivningar som motsäger ordböckernas egen "
              "definition. Ett tomt fält är bättre än ett felaktigt."),
    "feromon": dict(
        hb="Doftämne som djur av samma art skickar signaler med",
        reg="neutral, neutral",
        ex="Honan sänder ut ett %s som lockar till sig hannarna." % (B % "feromon"),
        etym="till grekiska pherein 'bära' och -mon i hormon",
        notis="Ingen synonym finns: alla tre källorna definierar omskrivande "
              "('doftämne som överförs mellan individer av samma art') och "
              "synonymer.se har ingen artikel. 'doftämne' är definitionens "
              "överbegrepp; kortets gamla 'luktsignal' finns i ingen källa."),
}

AVPAUSNING = (
    " AVPAUSAT 2026-08-30: pausningen byggde på mitt eget fel. Jag skrev "
    "synonym_groups som [[]] i stället för [], vilket tripper sparren "
    "tom_synonymgrupp -- den träffar trasig GRUPPERING, inte frånvaro av "
    "synonym. forgranska.py sa hela tiden att tom synonymlista är godkänd och "
    "att den är normalfallet i 69 % av korten.")


def main():
    d = json.load(io.open(SES, encoding="utf-8"))
    fg = json.load(io.open(FG, encoding="utf-8"))

    obelagda = {}
    for p in fg:
        for a in p["fel"]:
            if a["regel"] == "synonym_utan_ordboksbelagg":
                namn = a["detalj"].split(" -- ")[0]
                obelagda.setdefault(p["ord"], set()).update(
                    s.strip() for s in namn.split(","))

    n_strukna = n_norm = n_nya = n_avp = 0
    for p in d:
        o = p["ord"]

        if o in NYA:
            f = NYA[o]
            p["proposed"] = {
                "huvudbetydelse": f["hb"], "register": f["reg"],
                "synonym_groups": [], "synonymer": [],
                "exempelmening": f["ex"], "etymologi": f["etym"],
            }
            p["sokkoll"]["slutsats"] = (
                p["sokkoll"]["slutsats"].split(" PAUSAT")[0] + " " + f["notis"])
            n_nya += 1

        v = p.get("proposed")
        if not v:
            continue

        if o in obelagda:
            nya_g = []
            for g in (v.get("synonym_groups") or []):
                kvar = [s for s in g if s not in obelagda[o]]
                n_strukna += len(g) - len(kvar)
                nya_g.append(kvar)
            v["synonym_groups"] = nya_g
            v["synonymer"] = [s for g in nya_g for s in g]

        if v.get("synonym_groups") and not any(v["synonym_groups"]):
            v["synonym_groups"] = []
            v["synonymer"] = []
            n_norm += 1

        if p.get("pausad") and o not in FORTSATT_PAUSAD:
            p["pausad"] = False
            p["approved"] = True
            p.pop("paus_tagg", None)
            p["sokkoll"]["slutsats"] += AVPAUSNING
            n_avp += 1

    json.dump(d, io.open(SES, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("strukna obelagda synonymer : %d" % n_strukna)
    print("grupplistor normaliserade  : %d" % n_norm)
    print("nyskrivna forslag          : %d" % n_nya)
    print("avpausade                  : %d" % n_avp)
    print("approved                   : %d" % sum(1 for p in d if p.get("approved")))
    print("pausade                    : %s" % [p["ord"] for p in d if p.get("pausad")])
    utan = [p["ord"] for p in d if p.get("proposed") and not p["proposed"]["synonymer"]]
    print("kort utan synonym (tillatet): %d" % len(utan))


main()
