"""SO/SAOL-kontroll av tio redan rättade kort — och fyra rättelser av MINA fel.

Adam bad 2026-08-09 om en omkontroll av tio redan rättade kort mot den nya
svenska.se-kanalen (SAOL + SO). Utfallet är den viktigaste metodlärdomen hittills:

**SAOB:s extrabetydelser är ofta ålderdomliga och har medvetet strukits i SAOL/SO.**
Jag hade lagt till två sådana samma kväll -- `konstitutiv` (författningsbetydelsen)
och `ingenium` (personbetydelsen). Ingen av dem finns i vare sig SAOL eller SO.
SAOB:s artiklar är från 1900-talets början; SAOL och SO är från 2026. När de går
isär om vad ett ord BETYDER I DAG är det inte SAOB som ska vinna.

Kortet ska pluggas mot HP-provet, som prövar modern svenska. Alltså: SAOB för djup,
belägg och etymologi -- SAOL/SO för vilka betydelser som fortfarande gäller.
"""
import json
import os

MAL = "sessions/session_2026-08-09_v3-so-kontroll.json"
KALLOR = ["sessions/session_2026-08-09_v3-sokkoll-omgorning.json",
          "sessions/session_2026-08-09_v3-sokkoll-de-sju.json"]
SV = "https://svenska.se/tre/?sok={}"

P = {}


def lagg(ord_, extra_kalla, slutsats, **andr):
    P[ord_] = (extra_kalla, slutsats, andr)


lagg("konstitutiv", SV.format("konstitutiv"),
     "JAG HADE FEL, RÄTTAT. Jag lade samma kväll till betydelsen 'som rör en "
     "författning eller grundlag' på grundval av SAOB (artikel från 1900-talet) och "
     "synonymer.se:s närliggande ord 'författnings-'. SAOL 2026 ger endast "
     "'grundläggande, väsentlig'. SO 2026 ger endast 'grundläggande', märkt "
     "⟨något formellt⟩, med exemplet 'kvickhet var en konstitutiv del av hans "
     "personlighet'. Ingen modern ordbok har författningsbetydelsen -- den tas bort. "
     "Registret skärps till 'formell' enligt SO:s egen märkning.",
     huvudbetydelse="Som utgör en nödvändig, grundläggande beståndsdel",
     synonymer=["grundläggande", "väsentlig", "bestämmande"])

lagg("ingenium", SV.format("ingenium"),
     "JAG HADE FEL, RÄTTAT. Jag lade till betydelsen 'en person med sådan begåvning, "
     "ett snille' med SAOB som stöd. SAOL 2026: 'förstånd, begåvning'. SO 2026: "
     "'(skapande) begåvning', märkt ⟨något högtidligt⟩, exempel 'hennes skapande "
     "ingenium'. Ingen av dem har personbetydelsen -- den tas bort. Det betyder att "
     "kortets ursprungliga cirkularitet delvis kommer tillbaka; den löses i stället "
     "av SO:s precisering SKAPANDE begåvning, som skiljer ordet från 'begåvning' i "
     "allmänhet. Register ändrat från litterär till högtidlig enligt SO.",
     huvudbetydelse="Medfödd skapande begåvning",
     synonymer=["begåvning", "snille", "fallenhet"])

lagg("korus", SV.format("korus"),
     "SAKFEL HITTAT AV SO/SAOL. Kortet sa 'flera röster ELLER INSTRUMENT'. SAOL: "
     "'samtidigt tal av flera röster'. SO: 'samtidigt ljudande av flera röster', "
     "JFR kör. Ingen av dem nämner instrument -- ordet gäller röster. Dessutom "
     "saknade kortet ordets vanligaste användning: SAOL ger uttrycket 'i korus = "
     "enstämmigt, alla på en gång', och SO:s exempel är 'alla barnen svarade i "
     "korus'. Ordet är oböjligt neutrum (ett korus).",
     huvudbetydelse="Flera röster som ljuder samtidigt ; i korus: enstämmigt, alla "
                    "på en gång",
     synonymer=["kör", "samklang", "unisont"])

lagg("girig", SV.format("girig"),
     "REGISTERFEL HITTAT AV SO/SAOL. Båda märker ordet ⟨nedsättande⟩; kortet hade "
     "'vardaglig, negativ'. Nedsättande är en starkare och mer precis valör, och den "
     "står uttryckligen i två oberoende ordböcker. Betydelsen jag lade till samma "
     "kväll ('som häftigt åtrår något för stunden') BEKRÄFTAS av SO:s eget exempel "
     "'hon tog girigt för sig av tårtan'. SAOL tillägger att ordet i sammansättningar "
     "även betyder ivrig (vetgirig, äregirig). JFR gniden, lysten, närig, sniken, snål.",
     register="nedsättande")


def main():
    index = {}
    for f in KALLOR:
        for e in json.load(open(f, encoding="utf-8")):
            index[e["ord"]] = e
    ut = []
    for ord_, (extra, slutsats, andr) in P.items():
        e = json.loads(json.dumps(index[ord_]))
        e["sokkoll"] = {"kalla": e["sokkoll"]["kalla"] + " + " + extra,
                        "slutsats": slutsats}
        e["approved"] = True
        e["applicerad"] = False
        e.pop("skriven_av", None)
        for f_, v in andr.items():
            e["proposed"][f_] = v
        e["oforandrad"] = False
        ut.append(e)
    os.makedirs("sessions", exist_ok=True)
    json.dump(ut, open(MAL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(ut)} poster -> {MAL}")


if __name__ == "__main__":
    main()
