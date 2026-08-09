"""Batch 3 — femton kort mot svenska.se (SAOL + SO).

Adam 2026-08-09: *"Adam-tal är viktigt, men det viktigaste är att innehållet
stämmer och att det går att förstå relativt väl."* Definitionerna här är därför
medvetet kortare än i batch 2 — samma källkrav, färre ord.

Tumregel som användes: skriv den mening du skulle sagt till någon som frågar vad
ordet betyder. Inte ordbokens formulering, men inte heller mer innehåll än den har.
"""
import json
import os

MAL = "sessions/session_2026-08-09_v3-so-batch3.json"
KALLOR = ["sessions/session_2026-08-09_v3-omgranskning-nya.json",
          "sessions/session_2026-08-09_v3-dagens-ko.json",
          "sessions/session_2026-08-09_v3-dagens-ko2.json",
          "sessions/session_2026-08-09_v3-inlarning.json"]
SV = "https://svenska.se/tre/?sok={}"
P = {}


def lagg(ord_, sok, slutsats, **andr):
    P[ord_] = (SV.format(sok), slutsats, andr)


lagg("grossist", "grossist",
     "TVÅ FEL. (1) Kortet sa 'företag'. SAOL och SO säger båda **person**: "
     "'grosshandlare' respektive 'person som bedriver grosshandel'. (2) Den bästa "
     "synonymen, **grosshandlare**, saknades helt medan den obelagda "
     "'mellanledshandlare' stod kvar. SO ger dessutom MOTSATS detaljhandlare — "
     "motsatsen är den enklaste minnesregeln och den togs in.",
     huvudbetydelse="Person som köper in stora partier och säljer vidare till "
                    "butiker — motsatsen till en detaljhandlare",
     synonymer=["grosshandlare", "partihandlare"])

lagg("överreklamerad", "överreklamerad",
     "DEFINITIONEN HANDLADE OM FEL SAK. Kortet sa 'har fått mer uppmärksamhet än "
     "den förtjänar' — alltså om mängden uppmärksamhet. SO: 'framställd som bättre "
     "än den/det är'. Det handlar om hur något **beskrivs**, inte hur mycket. "
     "SO:s andra exempel visar skillnaden tydligt: 'utsikten var inte "
     "överreklamerad'. Ordet finns bara i SAOL och SO, inte i SAOB.",
     huvudbetydelse="Beskriven som bättre än den faktiskt är")

lagg("skrymma", "skrymma",
     "BRUKSREGEL SAKNADES, OCH EN DETALJ VAR PÅHITTAD. SO: '(nästan enbart presens "
     "particip)' — ordet används i praktiken bara som **skrymmande**. Det stod inte "
     "på kortet. Dessutom sa kortet 'i förhållande till sin vikt'; ingen källa säger "
     "det, båda säger '(onödigt) stort utrymme'. Exempel ur SO: skrymmande gods, "
     "skrymmande möbler.",
     huvudbetydelse="Ta upp onödigt mycket plats — används nästan bara som "
                    "skrymmande",
     synonymer=["ta stor plats", "vara otymplig"])

lagg("avbörda sig", "avbörda",
     "ANDRA BETYDELSEN SAKNAR STÖD. Kortet hade 'berätta om något tungt för att "
     "slippa bära det ensam'. Varken SAOL eller SO har den. SAOL: 'göra sig fri "
     "från'. SO: 'göra fri från', ofta reflexivt och ofta abstrakt, med exemplet "
     "'han försökte avbörda sig ansvaret'. Betydelsen är alltså att göra sig av med "
     "något — ansvar, skuld, en börda — inte att anförtro sig.",
     huvudbetydelse="Göra sig fri från något tungt, oftast ett ansvar",
     synonymer=["lämna ifrån sig", "göra sig fri från"])

lagg("anblick", "anblick",
     "EN SYNONYM VAR FEL. Kortet hade 'skymt', men en skymt är en flyktig glimt — "
     "en anblick är hela synintrycket. SO: 'synintryck vid betraktande av visst "
     "föremål', JFR **syn, åsyn** (kortets två andra synonymer, båda belagda). "
     "SO:s exempel är bra och konkret: 'blotta anblicken av smörgåsbordet satte "
     "igång salivkörtlarna'.",
     huvudbetydelse="Det man ser när man tittar på något",
     synonymer=["åsyn", "syn"])

lagg("eolisk", "eolisk",
     "REGISTER OCH DEFINITION JUSTERADE. SO: ⟨i vetenskapliga sammanhang el. "
     "högtidligt⟩ 'som har att göra med vinden', exempel 'eoliska avlagringar'. "
     "Kortet sa snävare 'orsakad eller formad av vinden'; källan är bredare. "
     "Synonymerna 'vindburen' och 'vindskapad' finns i ingen källa och tas bort — "
     "ordet är en fackterm utan vardaglig synonym, och då ska listan vara tom.",
     huvudbetydelse="Som har med vinden att göra — fackord, mest i geologi",
     synonymer=[],
     register="formell")

lagg("ornera", "ornera",
     "BRUKSREGEL TILLAGD. SO: '(vanligen perfekt particip) ornamentera', exempel "
     "'vackert ornerade bårder'. Ordet möter man alltså nästan alltid som "
     "**ornerad**. SAOL bekräftar kortets synonymer pryda och utsmycka; 'dekorera' "
     "finns inte i någon av källorna men är samma innebörd — den behålls eftersom "
     "den gör kortet begripligare, och det noteras här i stället för att döljas.",
     huvudbetydelse="Smycka ut något med mönster — möter man mest som ornerad",
     synonymer=["utsmycka", "pryda"])

lagg("djäkne", "djäkne",
     "REGISTER SKÄRPT. SAOL märker ordet ⟨åld.⟩ och SO ⟨endast vid beskrivning av "
     "äldre förhållanden⟩ — starkare än kortets tidigare märkning. SO preciserar "
     "också: 'elev i äldre typ av läroverk, s.k. lärdomsskola; särsk. i dess högre "
     "klasser'. Alltså inte vilken skolpojke som helst.",
     huvudbetydelse="Elev i en gammaldags lärdomsskola, särskilt i de högre "
                    "klasserna",
     register="arkaisk")

lagg("prelat_dummy", "prelat", "ej använd")   # borttagen, gjord i batch 2
del P["prelat_dummy"]

lagg("försonlig", "försonlig",
     "BEKRÄFTAT UTAN ÄNDRING. SO: 'beredd att ge efter för att åter uppnå ett "
     "vänskapligt förhållande', KONSTRUKTION 'försonlig (mot NÅGON)'. Kortets "
     "definition säger samma sak med enklare ord. Konstruktionen med *mot* är värd "
     "att synas i exempelmeningen.")

lagg("oktett", "oktett",
     "BEKRÄFTAT UTAN ÄNDRING. Båda betydelserna på kortet står i båda källorna: "
     "SAOL 'musikstycke för åtta instrument; grupp om åtta musiker', SO "
     "'musikaliskt verk för åtta instrument' + 'äv. musik- eller sånggrupp med åtta "
     "medlemmar'.")

lagg("salongsfähig", "salongsfähig",
     "SYNONYM BEKRÄFTAD. SO ger uttryckligen JFR **rumsren** — den synonym jag "
     "tidigare var osäker på. SO ger också en försvagad andra användning: 'i fråga "
     "om beteende eller framtoning som inte avviker från vad som är lämpligt', "
     "alltså inte bara om finrum.")

lagg("uttrycklig", "uttrycklig",
     "BEKRÄFTAT. SO: 'tydlig och bestämd och ofta språkligt uttryckt'. Kortets tre "
     "synonymer (uttalad, tydlig, bestämd) täcks alla av den formuleringen. "
     "Grammatikrättelsen uttalat → uttalad från i morse står kvar.")

lagg("affektiv", "affektiv",
     "SYNONYMER BEKRÄFTADE, FACKBETYDELSE NOTERAD. SO ger JFR känsloladdad, "
     "känslomässig — exakt kortets två synonymer. SO har dessutom en medicinsk "
     "specialbetydelse ('affektiv störning'). Den tas INTE in på kortet: den är en "
     "fackterm inom psykiatri och HP prövar allmänspråket. Noteras här så att nästa "
     "granskare ser att den är bortvald med avsikt, inte missad.")

lagg("borsjtj", "borsjtj",
     "BEKRÄFTAT. SAOL och SO säger båda 'en kraftig rödbetssoppa', och SO:s exempel "
     "'borsjtj serveras ofta med sur grädde' bekräftar kortets gräddfil. Ingen källa "
     "säger 'från Östeuropa' — det är korrekt bakgrund men står inte i ordböckerna, "
     "och det skrivs ut här hellre än att låtsas vara belagt.")

lagg("medaljong", "medaljong",
     "TRE BETYDELSER BEKRÄFTADE. SO numrerar sin första och ger inom den: "
     "'medaljliknande hängsmycke som innehåller miniatyrporträtt', 'äv. om "
     "förvaringskapsel för annat minne', 'äv. (mindre) målning eller relief i oval "
     "eller rund form'. Kortets hängsmycke och runda infattning är alltså båda "
     "belagda. Köttbiten ligger i ett senare numrerat uppslag.")


def main():
    index = {}
    for f in KALLOR:
        for e in json.load(open(f, encoding="utf-8")):
            index[e["ord"]] = e
    ut, saknade = [], []
    for ord_, (kalla, slutsats, andr) in P.items():
        e = index.get(ord_)
        if e is None:
            saknade.append(ord_)
            continue
        e = json.loads(json.dumps(e))
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
    print(f"  enbart ny sökkoll: {sum(1 for e in ut if e['oforandrad'])}")
    if saknade:
        print("SAKNADE:", saknade)


if __name__ == "__main__":
    main()
