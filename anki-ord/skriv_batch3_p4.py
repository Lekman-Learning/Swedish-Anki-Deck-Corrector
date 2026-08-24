# -*- coding: utf-8 -*-
"""Skriver proposed+sokkoll for chunk 4 (ord 75-99) av 200-korts v3-batch3."""
import json
import urllib.parse

SOKVAG = "sessions/session_2026-08-20_v3-batch3.json"

def kalla(ord_):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(ord_)

POSTER = {
    "avhandla": dict(
        huvudbetydelse="Behandla eller diskutera ett ämne, till exempel i en text eller ett möte",
        register="formell, neutral",
        synonymer=["handla om"],
        exempelmening='Boken <font color="#3498db">avhandlar</font> Sveriges ekonomiska historia under 1900-talet.',
        slutsats="SO/SAOL/Wiktionary överens: en kärnbetydelse. SAOL:s definitionstext leder andra ledet med 'handla om'.",
    ),
    "bastard": dict(
        huvudbetydelse="En avkomma av två olika djur- eller växtarter ; ett barn fött utanför äktenskapet (åld., nedsättande)",
        register="ngt ålderdomlig, neutral",
        synonymer=["korsningsprodukt"],
        exempelmening='Mulåsnan är en <font color="#3498db">bastard</font> mellan häst och åsna.',
        slutsats="SO/SAOL ger två klart skilda betydelser (art-hybrid; utomäktenskapligt barn). SAOL/BRUK markerar 'ålderdomligt; nedsättande', vilket främst gäller person-betydelsen -- markerat i parentes i huvudbetydelsen. SAOL:s definitionstext leder första ledet med 'korsningsprodukt'.",
    ),
    "bese": dict(
        huvudbetydelse="Titta noga på något för att studera eller inspektera det",
        register="formell, neutral",
        synonymer=["se på"],
        exempelmening='Turisterna kunde <font color="#3498db">bese</font> kyrkans berömda glasmosaik under rundvandringen.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext ÄR frasen 'se på'.",
    ),
    "besittning": dict(
        huvudbetydelse="Att faktiskt ha och kontrollera något, ofta egendom eller makt ; ett landområde som tillhör en annan stat, till exempel en koloni",
        register="fackspråklig, neutral, juridik ; formell, neutral, historia",
        synonym_groups=[["ägande"], ["koloni"]],
        exempelmening='Generalerna satte sig i <font color="#3498db">besittning</font> av makten efter kuppen.',
        slutsats="SO/SAOL ger två klart skilda betydelser (faktiskt förfogande; koloniinnehav). SAOL:s definitionstext leder första ledet med 'ägande' och nämner 'koloni' i andra ledet.",
    ),
    "bleck": dict(
        huvudbetydelse="En tunn plåt av stål eller metall, ofta med ett lager tenn ; blåsinstrumenten av mässing i en orkester (vardagligt)",
        register="neutral, neutral",
        synonymer=[],
        exempelmening='Han bytte ut det rostiga <font color="#3498db">blecket</font> på taket.',
        slutsats="SO/SAOL ger två klart skilda betydelser (tunn förtennad plåt; bleckblåsinstrument samlat). Ingen ordboksbelagd enordssynonym för någondera -- tom lista.",
    ),
    "bryta/dra en lans för någon/något": dict(
        huvudbetydelse="Ta parti för och kämpa för någon eller något, ofta i en debatt",
        register="neutral, neutral",
        synonymer=["stödja", "kämpa för"],
        exempelmening='Hon ville <font color="#3498db">bryta en lans för</font> skolidrotten som en viktig del av folkhälsan.',
        slutsats="Frasen saknar egen träff, men står som exempel under uppslagsordet 'lans' i SO/SAOL, vars andra betydelse definieras just som 'stödja eller kämpa för någon/något' -- grundordslookup (samma metod som 'lägga sordin på'/'kok stryk'). Kalla pekar på grundordet 'lans', inte den fulla frasen, eftersom det är där hämtningen och beläggen faktiskt finns.",
        kalla_ord="lans",
    ),
    "brädslå": dict(
        huvudbetydelse="Klä eller täcka något med bräder",
        register="ngt ålderdomlig, neutral",
        synonymer=["brädbekläda"],
        exempelmening='De <font color="#3498db">brädslog</font> den gamla lagården för att skydda den mot väder och vind.',
        slutsats="SO/synonymer.se överens: en betydelse (endast SO+SAOB, ingen SAOL-artikel, men SO ger tydlig, entydig definition). SO:s definitionstext ÄR ordet 'brädbekläda'. BRUK 'mindre brukligt' -- registret satt till ngt ålderdomlig snarare än helt arkaisk eftersom ordet fortfarande förstås direkt.",
    ),
    "buffé": dict(
        huvudbetydelse="Ett bord med mat och dryck där man själv tar för sig ; ett finare skåp för porslin och bestick",
        register="neutral, neutral",
        synonymer=["skåp"],
        exempelmening='Gästerna serverade sig själva från den stora <font color="#3498db">buffén</font> med varma och kalla rätter.',
        slutsats="SO/SAOL ger två klart skilda betydelser (självserveringsbord; möbel för servisförvaring). SAOL:s definitionstext leder andra ledet med 'skåp'.",
    ),
    "bukfylla": dict(
        huvudbetydelse="Mat som gör en mätt men inte ger mycket näring",
        register="vardaglig, negativ",
        synonymer=[],
        exempelmening='Godis och chips är bara <font color="#3498db">bukfylla</font>, inget som ger dig energi på riktigt.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen ordboksbelagd enordssynonym -- definitionerna är beskrivande fraser. Tom lista.",
    ),
    "dechiffrera": dict(
        huvudbetydelse="Tolka och förstå en hemlig eller svårläst text eller kod",
        register="formell, neutral",
        synonymer=["tolka"],
        exempelmening='Kryptografen lyckades <font color="#3498db">dechiffrera</font> det hemliga meddelandet på några timmar.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'tolka'.",
    ),
    "desperado": dict(
        huvudbetydelse="En hänsynslös och våldsam person som inte drar sig för något",
        register="litterär, negativ",
        synonymer=[],
        exempelmening='Banken rånades av en beväpnad <font color="#3498db">desperado</font> som inte tvekade att hota kunderna.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen ordboksbelagd enordssynonym -- definitionen är en beskrivande fras. Tom lista.",
    ),
    "destinera": dict(
        huvudbetydelse="Bestämma vart något eller någon ska föras eller skickas",
        register="formell, neutral",
        synonymer=[],
        exempelmening='Fartyget var <font color="#3498db">destinerat</font> till London när stormen tvingade det att ändra kurs.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen fristående ordboksbelagd synonym -- SAOL:s definitionstext ('bestämma destinationen för') delar rot med uppslagsordet, för nära för att räknas som en riktig synonym. Tom lista.",
    ),
    "disambiguera": dict(
        huvudbetydelse="Göra något som kan tolkas på flera sätt tydligt och entydigt",
        register="fackspråklig, neutral, lingvistik",
        synonymer=[],
        exempelmening='Programmet försökte <font color="#3498db">disambiguera</font> ordet "bank" utifrån sammanhanget i meningen.',
        slutsats="Endast SAOL har egen artikel (ingen SO/SAOB), men SAOL ger en tydlig, entydig definition och Wiktionary bekräftar samma betydelse -- tillräckligt belagt (SAOL räknas, till skillnad från SAOB-only-fallen). Ingen enordssynonym i definitionstexten -- tom lista.",
    ),
    "disparat": dict(
        huvudbetydelse="Helt olikartad, som inte hör ihop eller går att jämföra",
        register="formell, neutral",
        synonymer=["olikartad"],
        exempelmening='Föredraget hoppade mellan så <font color="#3498db">disparata</font> ämnen att ingen riktigt kunde följa med.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext ÄR ordet 'olikartad'.",
    ),
    "dröna": dict(
        huvudbetydelse="Vara passiv och lat, inte göra något",
        register="vardaglig, lätt negativ",
        synonymer=["söla", "dåsa"],
        exempelmening='Han låg och <font color="#3498db">drönade</font> i soffan hela söndagen i stället för att plugga.',
        slutsats="SO/Wiktionary överens om huvudbetydelsen (SAOL har en andra, dialektal betydelse 'råma utdraget' om djurläte -- så pass olik och sällsynt att den utelämnas). SAOL:s definitionstext leder med 'söla, dåsa'.",
    ),
    "ebenist": dict(
        huvudbetydelse="En skicklig hantverkare som tillverkar fina möbler, förr i tiden",
        register="arkaisk, neutral",
        synonymer=["konstsnickare"],
        exempelmening='<font color="#3498db">Ebenisten</font> Georg Haupt tillverkade praktfulla möbler åt det svenska hovet.',
        slutsats="SO/SAOL överens: en betydelse. BRUK 'historiskt'. SAOL:s definitionstext ÄR ordet 'konstsnickare'.",
    ),
    "elritsa": dict(
        huvudbetydelse="En liten, avlång karpfisk med olivbrun till svartgrön rygg",
        register="fackspråklig, neutral, biologi",
        synonymer=["kvidd"],
        exempelmening='De fångade en hel hink <font color="#3498db">elritsor</font> i den lilla bäcken.',
        slutsats="SO/SAOL överens: en betydelse. SO+ taggar uttryckligen SYN:synonym, som matchar JFR-korsreferensen till 'kvidd' (samma fisk, dialektalt namn).",
    ),
    "emfas": dict(
        huvudbetydelse="Starkt eftertryck eller kraft i hur något sägs",
        register="formell, neutral",
        synonymer=["eftertryck"],
        exempelmening='Hon talade med stor <font color="#3498db">emfas</font> om vikten av mer resurser till vården.',
        slutsats="SO/SAOL/Wiktionary överens: en kärnbetydelse. SAOL:s definitionstext leder med 'eftertryck'.",
    ),
    "enfaldig": dict(
        huvudbetydelse="Dum och okunnig",
        register="neutral, nedsättande",
        synonymer=[],
        exempelmening='Jag kände mig lite <font color="#3498db">enfaldig</font> när jag inte förstod något av den tekniska manualen.',
        slutsats="SO/Wiktionary överens: en kärnbetydelse. BRUK 'nedsättande'. Ingen fristående enordssynonym i definitionstexten (den ÄR definitionen) -- tom lista.",
    ),
    "enhetlig": dict(
        huvudbetydelse="Som ser likadan ut eller fungerar på samma sätt överallt, som en enhet",
        register="neutral, neutral",
        synonymer=["likformig"],
        exempelmening='Företaget ville ha en <font color="#3498db">enhetlig</font> design på alla sina butiker.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder andra ledet med 'likformig'.",
    ),
    "ensartad": dict(
        huvudbetydelse="Som har nästan samma egenskaper eller ser likadan ut överallt",
        register="neutral, neutral",
        synonymer=["likartad"],
        exempelmening='Flygplatser runt om i världen ser ofta <font color="#3498db">ensartade</font> ut, oavsett land.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder andra ledet med 'likartad'.",
    ),
    "entreprenör": dict(
        huvudbetydelse="Ett företag eller en person som åtar sig ett byggprojekt eller uppdrag ; en initiativrik person som startar och driver egna företag",
        register="fackspråklig, neutral ; neutral, positiv",
        synonymer=["initiativrik"],
        exempelmening='Han är en driven <font color="#3498db">entreprenör</font> som redan startat tre företag.',
        slutsats="SO/SAOL ger två klart skilda betydelser (entreprenad-utförare; företagsam person). SAOL:s definitionstext leder andra ledet med 'initiativrik'.",
    ),
    "entydig": dict(
        huvudbetydelse="Som bara kan tolkas eller förstås på ett enda sätt",
        register="neutral, neutral",
        synonymer=[],
        exempelmening='Hennes svar var <font color="#3498db">entydigt</font> -- hon ville definitivt inte gå.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen fristående enordssynonym i definitionstexten -- tom lista.",
    ),
    "epigram": dict(
        huvudbetydelse="En kort, spetsig dikt, ofta med en satirisk poäng",
        register="litterär, neutral, litteraturvetenskap",
        synonymer=[],
        exempelmening='Han skrev ett bitskt <font color="#3498db">epigram</font> om den korrupta politikern.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen enordssynonym -- 'dikt' är en överordnad kategori (epigram är EN typ av dikt), inte utbytbar. Tom lista.",
    ),
    "estrad": dict(
        huvudbetydelse="En upphöjd plattform där man uppträder eller håller tal inför publik",
        register="neutral, neutral",
        synonymer=[],
        exempelmening='Hon klev upp på <font color="#3498db">estraden</font> för att hålla sitt tal.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen enordssynonym i definitionstexten -- tom lista.",
    ),
}

def main():
    data = json.load(open(SOKVAG, encoding="utf-8"))
    by_ord = {c["ord"]: c for c in data}
    saknas = []
    for ord_, spec in POSTER.items():
        c = by_ord.get(ord_)
        if c is None:
            saknas.append(ord_)
            continue
        kalla_ord = spec.get("kalla_ord", ord_)
        c["sokkoll"] = {"kalla": kalla(kalla_ord), "slutsats": spec["slutsats"]}
        c["proposed"] = {
            "huvudbetydelse": spec["huvudbetydelse"],
            "register": spec["register"],
            "synonymer": spec.get("synonymer"),
            "synonym_groups": spec.get("synonym_groups"),
            "exempelmening": spec["exempelmening"],
            "etymologi": spec.get("etymologi"),
        }
        c["approved"] = True
    json.dump(data, open(SOKVAG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(POSTER)} kort. Saknades i sessionsfilen: {saknas}")

if __name__ == "__main__":
    main()
