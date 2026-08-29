# -*- coding: utf-8 -*-
"""Fyller proposed+sokkoll for de 20 forsta korten i session_2026-08-29_v3-batch3.

Underlag: slaupp_batch3_29aug.txt (SO/SAOL/SAOB via svenska.se, synonymer.se,
Wiktionary, hamtat 2026-08-29).

TRE FYND SOM INTE KOM UR RISKFLAGGORNA:

1. `in suspenso` -- uppslaget gav artikeln for prepositionen `in`
   ("till det inre av nagot | inne | inat"), inte frasen. Samma fel som
   `in infinitum` 2026-08-28. Ordet finns INTE i SO/SAOL. Pausas, skrivs ej.

2. `beting` -- SO har TRE betydelser, kortet hade tva. Den tredje ar
   sjotermen: anordning pa fordack for fastgoring av ankartag.

3. `justera` -- SO har TRE, kortet hade tva. Den tredje ar sportens
   "tillfoga lattare skada" (vard.).

FYRA MOTSATSORD i synonymer.se:s listor, alla uteslutna:
  kurant     -> inkurant, sjuk
  betanklig  -> riskfri, otvivelaktig
  marglos    -> margfull, kraftfull, uttrycksfull
  skiljaktig -> lik, samma
"""
import io, json, sys

FIL = "sessions/session_2026-08-29_v3-batch3.json"
B = '<font color="#3498db">%s</font>'

K = {}

K["kurant"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via https://svenska.se/api/msearch?ord=kurant + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO har TRE betydelser: 'efterfragad och darmed lattsald' | 'som anvands allmant' | 'frisk'. "
                 "Kortet hade tva -- OLD-facit (frisk; gangbar; lattsald) hade ratt och riskflaggan old_har_fler_betydelser stammer. "
                 "SAOL bekraftar bada ytterlaggarna: 'frisk och kry' + 'gangbar'. "
                 "UTESLUTNA ur synonymer.se: 'inkurant' och 'sjuk' -- bada MOTSATSORD, inte synonymer."),
    proposed=dict(
        huvudbetydelse="Lätt att sälja för att många vill ha den ; som är i vanligt bruk just nu ; frisk och pigg igen",
        register="neutral",
        synonymer=["lättsåld", "säljbar", "gängse", "gångbar", "kry", "pigg"],
        synonym_groups=[["lättsåld", "säljbar"], ["gängse", "gångbar"], ["kry", "pigg"]],
        exempelmening="Begagnade elcyklar är en %s vara, medan gamla faxar knappt går att ge bort." % (B % "kurant"),
        etymologi="→ Franska courant 'löpande' — det som är i omlopp och rör sig, alltså går åt.",
    ))

K["cerat"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + Wiktionary (hamtat 2026-08-29, HTTP 200). synonymer.se saknar uppslag.",
        slutsats="SO: 'en vaxhaltig salva som motverkar sprickor pa lapparna'. SAOL: 'en vaxhaltig salva for torra lappar'. "
                 "En betydelse, alla kallor overens. Legacys 'lappglans' ar sakligt fel -- cerat ar en sprickskyddande vaxsalva, "
                 "inte kosmetika. Ingen av de tre kallorna anger nagon synonym; lamnas darfor tom (tom lista ar godkant, beslut 2026-08-12)."),
    proposed=dict(
        huvudbetydelse="Vaxsalva man smörjer på läppar som torkat och spruckit",
        register="neutral",
        synonymer=[],
        synonym_groups=None,
        exempelmening="Efter en vecka i blåsten var läpparna så trasiga att han sov med %s på." % (B % "cerat"),
        etymologi="→ Latin cera 'vax' — salvan är i grunden just vax.",
    ))

K["definition"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO: 'avgransning och bestamning av betydelse'. SAOL: 'angivelse av betydelse'. "
                 "SO:s ovriga poster ar uttrycket 'per definition' (definitionsmassigt) och en underart (genusdefinition) -- "
                 "anvandningsnoter och sammansattningar, inte egna betydelser. En huvudbetydelse. "
                 "UTESLUTNA ur synonymer.se: 'per', 'automatiskt', 'i huvuddrag' -- fragment ur uttrycket 'per definition', inte synonymer till ordet."),
    proposed=dict(
        huvudbetydelse="Att säga precis vad ett ord betyder, så att gränsen mot allt annat blir tydlig",
        register="neutral",
        synonymer=["begreppsbestämning", "precisering"],
        synonym_groups=None,
        exempelmening="De grälade i en timme innan de märkte att de använde olika %s av ordet rättvisa." % (B % "definition"),
        etymologi=None,
    ))

K["knaper"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO: 'inte fullt tillracklig', markt BRUK: vard. SAOL: 'knapp, torftig'. "
                 "Wiktionary listar aven 'torr och hard' (knaprig), men varken SO eller SAOL har den betydelsen for `knaper` -- "
                 "en kalla racker inte, sa den utelamnas. Legacys tva 'betydelser' var samma betydelse i tva omskrivningar."),
    proposed=dict(
        huvudbetydelse="Så lite att det knappt räcker till",
        register="vardaglig",
        synonymer=["knapp", "torftig"],
        synonym_groups=None,
        exempelmening="Studietiden var %s — han räknade kronor för att få mjölken att gå ihop." % (B % "knaper"),
        etymologi=None,
    ))

K["beting"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="🔴 SO har TRE betydelser, kortet hade tva: (1) 'avtalad ersattning for viss, i forvag overenskommen arbetsuppgift', "
                 "(2) 'overenskommen arbetsuppgift som utfors mot avtalad ersattning' -- spec. i skolsammanhang om storre inlasningsuppgifter, "
                 "(3) 'anordning pa fordack av fartyg eller bat for fastgoring av ankartag eller fortojning'. "
                 "Den tredje ar ett eget ord med egen etymologi (lagtyska/nederlandska beting, jfr aldre svenska bette 'tvarbalk') "
                 "och egen belaggsarsrad (1551 mot 1788) -- alltsa en homonym, inte en nyans. Ingen riskflagga fangade den. "
                 "Synonymerna i synonymer.se galler bara betydelse 1-2; sjotermen far tankstreck."),
    proposed=dict(
        huvudbetydelse="Avtalat pris för ett bestämt jobb, inte betalt per timme ; själva uppgiften man tagit på sig till det priset ; kraftig stolpe på ett fartygs framdäck att fästa ankarlinan vid",
        register="neutral ; neutral ; fackspråklig, sjöfart",
        synonymer=["ackord", "entreprenad", "pensum", "—"],
        synonym_groups=[["ackord", "entreprenad"], ["pensum"], ["—"]],
        exempelmening="Grävningen lades ut på %s, så laget fick lika mycket betalt vare sig det tog tre dagar eller sju." % (B % "beting"),
        etymologi=None,
    ))

K["betänklig"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO och SAOL har samma ordalydelse: 'som ger anledning till oro eller kritik'. En betydelse. "
                 "UTESLUTNA ur synonymer.se: 'riskfri' och 'otvivelaktig' -- bada MOTSATSORD. "
                 "'vagad' och 'lattfardig' utesluts ocksa: de beskriver den som handlar, inte det som oroar."),
    proposed=dict(
        huvudbetydelse="Sådant som får en att bli orolig och undra om det verkligen är okej",
        register="neutral",
        synonymer=["oroväckande", "tvivelaktig"],
        synonym_groups=None,
        exempelmening="Siffrorna tog en %s vändning i mars, och styrelsen kallade till extra möte." % (B % "betänklig"),
        etymologi=None,
    ))

K["biennal"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + Wiktionary (hamtat 2026-08-29, HTTP 200). synonymer.se saknar uppslag.",
        slutsats="SO: 'utstallning eller evenemang som anordnas vartannat ar'. SAOL preciserar: 'konstutstallning som aterkommer vartannat ar'. "
                 "SO anger JFR: triennal (vart tredje ar) -- de ska hallas isar. Ingen kalla ger nagon synonym; lamnas tom."),
    proposed=dict(
        huvudbetydelse="Stor konstutställning som hålls vartannat år",
        register="neutral, konst",
        synonymer=[],
        synonym_groups=None,
        exempelmening="Hon ställde ut på %s i Venedig och kom hem med tre nya beställningar." % (B % "biennal"),
        etymologi="→ Latin biennalis 'tvåårig' — bi 'två' + annus 'år'.",
    ))

K["deliciös"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO: 'helt utsokt', markt BRUK: 'nagot hogtidligt'. SAOL: 'fin, utsokt, fortjusande'. "
                 "En betydelse. Registret ar det som skiljer ordet fran 'gott' och maste sta pa kortet."),
    proposed=dict(
        huvudbetydelse="Så gott att det känns lyxigt",
        register="högtidlig",
        synonymer=["utsökt", "läcker"],
        synonym_groups=None,
        exempelmening="Bakverken var %s, och hon åt tre innan hon kom på att räkna." % (B % "deliciös"),
        etymologi="→ Franska délicieux, av latin delicia 'nöje'.",
    ))

K["eminent"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO har TVA betydelser: (1) 'mycket framstaende eller skicklig', (2) 'egentlig och betydelsefull' -- den senare "
                 "bara i fasta uttryck som 'i eminent mening' och 'i eminent grad'. SAOL har bara den forsta. "
                 "Betydelse 2 ar en gradforstarkare utan utbytbar synonym; den far tankstreck."),
    proposed=dict(
        huvudbetydelse="Så skicklig att man sticker ut bland alla andra ; i allra högsta grad, riktigt utpräglat",
        register="neutral",
        synonymer=["framstående", "lysande", "—"],
        synonym_groups=[["framstående", "lysande"], ["—"]],
        exempelmening="Målvakten var %s hela matchen och släppte inte in ett enda skott." % (B % "eminent"),
        etymologi="→ Latin eminere 'höja sig' — den som sticker upp över de andra.",
    ))

K["enväldig"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se (hamtat 2026-08-29, HTTP 200). Wiktionary gav HTTP 429 (rate limit), ej hamtad.",
        slutsats="SO: 'som ensam har all makt att besluta'. SAOL: 'som ensam har all makt'. En betydelse, tva kallor overens. "
                 "SO anger JFR: despotisk, tyrannisk -- de ar narliggande men bar ett vardeomdome som `envaldig` inte gor, "
                 "sa de utesluts som synonymer. 'enradig' och 'oinskrankt' star bada i synonymer.se och ar utbytbara."),
    proposed=dict(
        huvudbetydelse="Som ensam bestämmer allt, utan att behöva fråga någon",
        register="neutral",
        synonymer=["enrådig", "oinskränkt"],
        synonym_groups=None,
        exempelmening="Kungen styrde %s i fyrtio år och kallade aldrig in riksdagen." % (B % "enväldig"),
        etymologi=None,
    ))

K["graciös"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO: 'som karakteriseras av skonhet och latthet i rorelse eller linje'. SAOL: 'behagfull, mjuk i rorelser el. linjer'. "
                 "En betydelse. Bade rorelse och linje ingar -- SO:s exempel tacker bada ('graciös dans', 'skrifttecknens graciösa ornamentik')."),
    proposed=dict(
        huvudbetydelse="Som rör sig vackert och lätt, utan att det ser ansträngt ut",
        register="neutral",
        synonymer=["behagfull", "elegant"],
        synonym_groups=None,
        exempelmening="Hon gick över isen lika %s som om hon aldrig behövt lära sig." % (B % "graciös"),
        etymologi=None,
    ))

K["ihållande"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO: 'som fortgar lange och oavbrutet'. SAOL: 'som aldrig tycks sluta'. En betydelse. "
                 "⚠️ Huvudbetydelsen far INTE innehalla 'haller' -- det ar cirkulart mot uppslagsordet. Skriven med 'fortsatter' i stallet."),
    proposed=dict(
        huvudbetydelse="Som fortsätter länge utan paus eller avbrott",
        register="neutral",
        synonymer=["långvarig", "oavbruten"],
        synonym_groups=None,
        exempelmening="Det %s regnet i augusti gjorde att skörden ruttnade på fälten." % (B % "ihållande"),
        etymologi=None,
    ))

K["justera"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="🔴 SO har TRE betydelser, kortet hade tva: (1) 'stalla in (nagot) i ratt lage', "
                 "(2) 'kontrollera riktigheten hos (motesprotokoll) samt intyga den med sin namnteckning', "
                 "(3) 'tillfoga lattare skada' -- markt vard., SAOL preciserar 'skada t.ex. fotbollsspelare'. "
                 "Den tredje saknades helt och ingen riskflagga fangade den. Registret skiljer sig mellan betydelserna."),
    proposed=dict(
        huvudbetydelse="Ställa in något så att det hamnar i rätt läge ; skriva under ett mötesprotokoll för att intyga att det stämmer ; ge en motståndare en smäll så att han tar skada",
        register="neutral ; fackspråklig, mötesteknik ; vardaglig, sport",
        synonymer=["korrigera", "ställa in", "godkänna", "—"],
        synonym_groups=[["korrigera", "ställa in"], ["godkänna"], ["—"]],
        exempelmening="Protokollet var inte %s än, och därför gällde inga av besluten." % (B % "justerat"),
        etymologi=None,
    ))

K["karg"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO har TVA betydelser: (1) 'kal och ofruktsam' om mark, (2) 'inbunden, avmatt' bildligt om person. "
                 "SAOL: 'ofruktbar; njugg, strav'. Legacys andra betydelse ('snal, besparande') ar en TREDJE nyans som SAOL "
                 "antyder med 'njugg' -- men SO for den under samma bildliga betydelse som 'inbunden'. Tva betydelser skrivs, "
                 "med SO som avgorande. Wiktionarys 'snal, sparsam, njugg' stods av SAOL:s njugg och namns i betydelse 2:s synonymer."),
    proposed=dict(
        huvudbetydelse="Mark där nästan ingenting växer ; person som säger väldigt lite och ger lika lite av sig själv",
        register="neutral",
        synonymer=["ofruktbar", "mager", "ordkarg", "avmätt"],
        synonym_groups=[["ofruktbar", "mager"], ["ordkarg", "avmätt"]],
        exempelmening="Landskapet blev allt %s ju längre norrut de kom, till slut bara sten och mossa." % (B % "kargare"),
        etymologi=None,
    ))

K["märglös"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO: 'som saknar inre kraft och uttrycksfullhet', med MOTSATS:antonym margfull. Wiktionary: 'kraftlos, utan innehall'. "
                 "En betydelse. UTESLUTNA ur synonymer.se: 'margfull', 'kraftfull' och 'uttrycksfull' -- alla tre MOTSATSORD. "
                 "Att synonymer.se blandar in dem gor listan aktivt farlig for just det har ordet."),
    proposed=dict(
        huvudbetydelse="Utan kraft och liv inuti, så att det inte gör något intryck alls",
        register="neutral",
        synonymer=["kraftlös", "slapp"],
        synonym_groups=None,
        exempelmening="Föreställningen var %s — skådespelarna sa rätt repliker men ingen trodde på dem." % (B % "märglös"),
        etymologi="→ Märgen är det mjuka inuti benen; utan den finns ingen inre kraft kvar.",
    ))

K["siesta"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO: '(tid for) vila mitt pa dagen'. SAOL preciserar: 'middagsvila i varma lander'. "
                 "En betydelse. SO:s parentes visar att ordet tacker bade vilan och tidsrummet -- SO:s eget exempel "
                 "'gatorna var tomma under siestan' ar tidsrummet."),
    proposed=dict(
        huvudbetydelse="Vila mitt på dagen när hettan är som värst",
        register="neutral",
        synonymer=["middagsvila", "tupplur"],
        synonym_groups=None,
        exempelmening="Gatorna låg tomma under %s och butikerna öppnade först vid fyra." % (B % "siestan"),
        etymologi="→ Latin sexta hora 'den sjätte timmen' — räknat från soluppgången, alltså mitt på dagen.",
    ))

K["skiljaktig"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO: 'som inte sammanfaller', aven om asikt i forhallande till en annan. SAOL: 'olik, avvikande'. En betydelse. "
                 "UTESLUTNA ur synonymer.se: 'lik' och 'samma' -- bada MOTSATSORD. "
                 "Termen 'skiljaktig mening' (juridik) ar SO:s eget exempel, inte en egen betydelse."),
    proposed=dict(
        huvudbetydelse="Som inte stämmer överens med det andra",
        register="neutral",
        synonymer=["avvikande", "olik"],
        synonym_groups=None,
        exempelmening="En av domarna hade en %s mening och skrev ner sina skäl sist i domen." % (B % "skiljaktig"),
        etymologi=None,
    ))

K["tjäle"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO: '(forekomst av) hard och fast skorpa av jord och is fran markytan och ett stycke nedat'. "
                 "SAOL: 'is (i jorden) i frusen mark'. En betydelse. "
                 "🔴 UTESLUTEN ur synonymer.se: 'permafrost' -- sakligt FEL. Permafrost ar mark som ar frusen aret om i flera ar; "
                 "tjale ar sasongsbunden och gar ur jorden pa varen (SO:s eget exempel: 'annu i slutet av april hade tjalen inte gatt ur jorden'). "
                 "'frost' utesluts ocksa: frost ar rimmen pa ytan, tjale ar det frusna lagret nedat. Inga sakra synonymer kvar -- lamnas tom."),
    proposed=dict(
        huvudbetydelse="Det hårda lagret av frusen jord och is som bildas nedåt i marken under vintern",
        register="neutral",
        synonymer=[],
        synonym_groups=None,
        exempelmening="De kunde inte gräva förrän i maj, eftersom %s satt kvar en halvmeter ner." % (B % "tjälen"),
        etymologi=None,
    ))

K["abstraktion"] = dict(
    sokkoll=dict(
        kalla="SO, SAOL via svenska.se + synonymer.se + Wiktionary (hamtat 2026-08-29, HTTP 200)",
        slutsats="SO: 'det att abstrahera', aven 'om foreteelse som inte kan uppfattas med sinnena'. "
                 "SAOL: 'aven ren tankeskapelse'. Tva betydelser: sjalva handlingen och resultatet av den. "
                 "SO:s eget exempel 'begreppet frihet ar en abstraktion' ar resultatbetydelsen. "
                 "Synonymerna i synonymer.se galler alla resultatbetydelsen; handlingen far tankstreck."),
    proposed=dict(
        huvudbetydelse="Att skala bort detaljerna och bara behålla det som är gemensamt ; en tanke man inte kan se eller ta på",
        register="neutral",
        synonymer=["—", "tankeskapelse"],
        synonym_groups=[["—"], ["tankeskapelse"]],
        exempelmening="Ordet rättvisa är en %s — ingen har någonsin sett den, men alla bråkar om den." % (B % "abstraktion"),
        etymologi=None,
    ))

# --- in suspenso: skrivs INTE ---
PAUSA = {
    "in suspenso": "v3_pausad::inget_uppslagsord_i_so_saol",
}


def main():
    d = json.load(io.open(FIL, encoding="utf-8"))
    skrivna = pausade = 0
    for k in d:
        o = k["ord"]
        if o in PAUSA:
            k["pausad"] = PAUSA[o]
            k["sokkoll"] = dict(
                kalla="svenska.se msearch 2026-08-29",
                slutsats="Uppslaget returnerade artikeln for prepositionen `in` (till det inre av nagot | inne | inat), "
                         "inte frasen `in suspenso`. Varken SO eller SAOL har frasen som uppslagsord. "
                         "Samma fall som `in infinitum` 2026-08-28 och `forborgad` 2026-08-18: flerordslemman "
                         "matchar sina delar och far falska uppslagsordstraffar.")
            k["approved"] = False
            pausade += 1
            continue
        if o in K:
            k["sokkoll"] = K[o]["sokkoll"]
            k["proposed"] = K[o]["proposed"]
            k["approved"] = True
            skrivna += 1
    json.dump(d, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("skrivna :", skrivna)
    print("pausade :", pausade)
    print("kvar    :", sum(1 for k in d if not k.get("proposed") and not k.get("pausad")))


if __name__ == "__main__":
    main()
