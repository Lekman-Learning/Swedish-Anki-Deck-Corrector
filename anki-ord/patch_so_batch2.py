"""Batch 2 av sökkollen — tio kort mot svenska.se (SAOL + SO).

Första batchen som körts med den nya kanalen från början i stället för att
rättas i efterhand. Källhierarkin från kvällen gäller: SO/SAOL avgör vilka
betydelser som lever, SAOB bara djup och etymologi.

En fjärde fälla i svenska.se upptäcktes här: sidan visar en **träfflista** även
när ordet matchar flera uppslag (`civiliserad` gav "adj." + "(civilisera) verb").
Då krävs ett extra klick för att nå artikeln. Kortet lämnas därför obelagt och
rödflaggas enligt Adams regel, i stället för att skrivas på en halv hämtning.
"""
import json
import os

MAL = "sessions/session_2026-08-09_v3-so-batch2.json"
KALLOR = ["sessions/session_2026-08-09_v3-omgranskning-nya.json",
          "sessions/session_2026-08-09_v3-dagens-ko.json",
          "sessions/session_2026-08-09_v3-dagens-ko2.json",
          "sessions/session_2026-08-09_v3-inlarning.json"]
SV = "https://svenska.se/tre/?sok={}"
P = {}


def lagg(ord_, sok, slutsats, **andr):
    P[ord_] = (SV.format(sok), slutsats, andr)


lagg("repressalie", "repressalie",
     "TVÅ TILLÄGG FRÅN SO. (1) Ordet används **nästan enbart i plural** -- SAOL "
     "'mest i pl.', SO '(nästan enbart plur.)'. Det stod inte på kortet, och det är "
     "just den sortens bruksregel HP prövar. (2) SO märker betydelsen (militär) och "
     "ger JFR vedergällning, som bekräftar kortets starkaste synonym. 'motåtgärd' och "
     "'straffåtgärd' finns i ingen källa och byts mot belagda former.",
     huvudbetydelse="Hämndaktion som svar på en oförrätt, oftast militär och nästan "
                    "alltid i plural: repressalier",
     synonymer=["vedergällning", "hämndaktion"])

lagg("sufflett", "sufflett",
     "TVÅ SAKFEL. Kortet sa 'tyg- ELLER LÄDERtak på ett FORDON'. SAOL: 'nedfällbart "
     "tak på bil el. barnvagn'. SO: 'upp- och nedfällbart skyddstak på bil el. "
     "barnvagn; **vanligen av tyg**'. Läder nämns inte av någon källa, och "
     "**barnvagn** saknades helt -- det är inte bara fordon. SO ger JFR hardtop, "
     "vilket är den upplysande kontrasten: sufflett är den mjuka varianten.",
     huvudbetydelse="Upp- och nedfällbart skyddstak av tyg, på bil eller barnvagn",
     synonymer=["fällbart tak", "kapell"])

lagg("terapeutisk", "terapeutisk",
     "SAKNAD BETYDELSE. SO ger två: (1) 'som har att göra med terapi' (terapeutisk "
     "rådgivning, terapeutisk behandling) (2) spec. 'som har botande eller lindrande "
     "verkan' (samtalet verkade terapeutiskt på henne). Kortet hade bara (2). "
     "SAOL bekräftar synonymerna: sjukdomsbehandlande, läkande.",
     huvudbetydelse="Som har att göra med terapi ; som har botande eller lindrande "
                    "verkan",
     synonymer=["läkande", "behandlande"])

lagg("prelat", "prelat",
     "TRE FYND. (1) Ordet är en **hederstitel**, inte bara 'högt uppsatt' -- SAOL "
     "'en hederstitel för katolsk präst', SO '(hederstitel för) förtjänt katolsk "
     "präst'. (2) Andra betydelsen saknades: 'äv. om präst i allmänhet, ofta med "
     "tonvikt på värdighet'. (3) SO märker ⟨ibland något ironiskt⟩ -- en valör "
     "kortet inte hade. 'biskop' och 'kyrkofurste' finns i ingen källa; en prelat "
     "behöver inte vara biskop.",
     huvudbetydelse="Hederstitel för en förtjänt katolsk präst ; allmännare om en "
                    "präst, med tonvikt på värdigheten",
     register="formell, ironisk")

lagg("fördärvlig", "fördärvlig",
     "BEKRÄFTAT. SO: 'som medför stor skada eller olycka', KONSTRUKTION 'fördärvlig "
     "(för NÅGON)', exempel 'spritens fördärvliga inverkan'. SAOL: "
     "'fördärvbringande'. Kortets definition stämmer och är inte längre cirkulär "
     "(den tidigare löd 'som leder till fördärv'). Konstruktionen med *för* är värd "
     "att synas i exempelmeningen.")

lagg("högfärdig", "högfärdig",
     "SYNONYMFEL. SO ger JFR högdragen, högmodig, nedlåtande, uppblåst; SAOL ger "
     "mallig, nedlåtande. Av kortets tre synonymer är **bara 'uppblåst' belagd** -- "
     "'inbilsk' och 'dryg' finns i ingen källa. Dessutom preciserar SO att "
     "överlägsenheten särskilt gäller **social status**, vilket skiljer högfärdig "
     "från inbilsk (som handlar om självbild).",
     huvudbetydelse="Uppträder som förmer än andra, särskilt i fråga om social status",
     synonymer=["högdragen", "högmodig", "uppblåst"])

lagg("variabel", "variabel",
     "ADJEKTIVET BEKRÄFTAT. Både SAOL och SO numrerar uppslaget **1variabel** "
     "(substantiv), vilket betyder att det finns ett 2variabel -- adjektivet. "
     "Tillägget jag gjorde i morse var alltså rätt, och det syns i själva "
     "numreringen. SO:s definition av substantivet: 'storhet som kan anta olika "
     "(tal)värden ingående i matematiska funktioner', JFR **konstant** -- motsatsen "
     "är den bästa minnesregeln och saknades på kortet.",
     synonymer=["föränderlig", "växlande"])

lagg("tabernakel", "tabernakel",
     "TREDJE BETYDELSEN SAKNAS FORTFARANDE. Kortet har nattvardsskåpet och "
     "ökenvandringens tält. Både SAOL och SO ger dessutom **frikyrklig "
     "gudstjänstlokal / frikyrkokapell**. SO numrerar sin första betydelse '1', "
     "alltså finns fler uppslag. Ordningen bör också ändras: SAOL leder med "
     "tälthelgedomen, kortet med skåpet.",
     huvudbetydelse="Israeliternas flyttbara tälthelgedom under ökenvandringen ; "
                    "skåp i en kyrka där nattvardsbrödet förvaras ; frikyrkligt kapell")

lagg("fadd", "fadd",
     "DEFINITIONEN VAR FEL I SAK. Kortet sa 'utan smak'. SO: 'som har **ointressant "
     "(och ofta oangenäm)** smak el. bismak' -- en fadd smak är alltså inte frånvarande "
     "utan tråkig och lite obehaglig. SAOL ger de belagda synonymerna **jolmig** och "
     "smaklös, som kortet saknade helt. Den bildliga användningen bekräftas av SO:s "
     "exempel 'pjäsen lämnar en fadd eftersmak'.",
     huvudbetydelse="Har en tråkig och ofta lite obehaglig smak ; bildligt: "
                    "intetsägande och andefattig",
     synonymer=["jolmig", "smaklös", "intetsägande"])


def main():
    index = {}
    for f in KALLOR:
        for e in json.load(open(f, encoding="utf-8")):
            index[e["ord"]] = e
    ut = []
    for ord_, (kalla, slutsats, andr) in P.items():
        e = json.loads(json.dumps(index[ord_]))
        e["sokkoll"] = {"kalla": kalla, "slutsats": slutsats}
        e["approved"] = True
        e["applicerad"] = False
        e.pop("skriven_av", None)
        for f_, v in andr.items():
            e["proposed"][f_] = v
        e["oforandrad"] = not andr
        ut.append(e)
    os.makedirs("sessions", exist_ok=True)
    json.dump(ut, open(MAL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(ut)} poster -> {MAL}")
    print(f"  innehållsändrade : {sum(1 for e in ut if not e['oforandrad'])}")


if __name__ == "__main__":
    main()
