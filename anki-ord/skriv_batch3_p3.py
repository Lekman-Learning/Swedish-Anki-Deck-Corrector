# -*- coding: utf-8 -*-
"""Skriver proposed+sokkoll for chunk 3 (ord 50-74) av 200-korts v3-batch3."""
import json
import urllib.parse

SOKVAG = "sessions/session_2026-08-20_v3-batch3.json"

def kalla(ord_):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(ord_)

POSTER = {
    "kurir": dict(
        huvudbetydelse="En snabb budbärare som för viktiga meddelanden, ofta mellan en regering och dess ambassader",
        register="ngt ålderdomlig, neutral",
        synonymer=["ilbud"],
        exempelmening='Kungen skickade en <font color="#3498db">kurir</font> med det brådskande budet till slottet.',
        slutsats="SO ger två släkta betydelser (allmän snabb budbärare; diplomatisk budbärare) -- slås ihop till en, eftersom den andra bara är en specialtillämpning av samma grundidé. SAOL:s definitionstext leder med 'ilbud' -- belagd synonym.",
    ),
    "lavemang": dict(
        huvudbetydelse="En sköljning av tarmen med vätska genom ändtarmen",
        register="fackspråklig, neutral, medicin",
        synonymer=["tarmsköljning"],
        exempelmening='Patienten fick ett <font color="#3498db">lavemang</font> inför undersökningen.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext ÄR ordet 'tarmsköljning' -- belagd synonym.",
    ),
    "målerisk": dict(
        huvudbetydelse="Vacker på ett sätt som gör att man vill måla eller fotografera det",
        register="litterär, positiv",
        synonymer=["pittoresk", "tjusande"],
        exempelmening='De vandrade genom den <font color="#3498db">måleriska</font> gamla stadsdelen med smala gränder och färgglada hus.',
        slutsats="SO ger 'pittoresk' som en egen, fristående alternativ definitionsformulering -- starkt belagd. SAOL:s definitionstext leder med 'tjusande' -- också belagd. Den tredje SO-betydelsen (om själva målarkonsten) är en klart annan användning men ovanlig -- utelämnad för att hålla kortet fokuserat på huvudbruket.",
    ),
    "primitiv": dict(
        huvudbetydelse="Som ligger på en mycket enkel eller outvecklad nivå",
        register="neutral, lätt negativ",
        synonymer=["outvecklad", "enkel"],
        exempelmening='Flyktinglägret bestod av <font color="#3498db">primitiva</font> tält utan rinnande vatten.',
        slutsats="SO:s två betydelser (låg utvecklingsnivå; ytterst enkel/torftig) är samma grundidé, slås ihop. SAOL:s definitionstext ('ursprunglig; outvecklad; enkel') ger tre leder -- 'outvecklad' och 'enkel' använda som belagda synonymer.",
    ),
    "reducera": dict(
        huvudbetydelse="Göra mindre eller minska något",
        register="neutral, neutral",
        synonymer=["minska"],
        exempelmening='Företaget lyckades <font color="#3498db">reducera</font> tillverkningstiden med en tredjedel.',
        slutsats="SO:s andra betydelse (göra mål i bollspel för att minska underläge) är en smal sportspecifik tillämpning av samma grundidé -- utelämnad till förmån för kärnbetydelsen. SAOL:s definitionstext leder med 'minska'.",
    ),
    "seans": dict(
        huvudbetydelse="En sluten sammankomst där man försöker komma i kontakt med andar",
        register="neutral, neutral",
        synonymer=[],
        exempelmening='Mediumet ledde en <font color="#3498db">seans</font> för att kontakta den avlidna kvinnans ande.',
        slutsats="SO/SAOL/Wiktionary överens om huvudbetydelsen. SAOL:s andra, sällsynta betydelse ('sittning för målare') utelämnad -- för ovanlig för att motivera en egen rad. Ingen ordboksbelagd synonym hittades i definitionstexten -- tom lista.",
    ),
    "skrå": dict(
        huvudbetydelse="En sammanslutning av alla hantverkare inom ett visst yrke, förr i tiden ; sned eller lutande",
        register="arkaisk, neutral ; neutral, neutral",
        synonym_groups=[["yrkeskår"], ["sned"]],
        exempelmening='Skomakargesällerna fick vänta länge innan de vann inträde i <font color="#3498db">skrået</font>.',
        slutsats="SO/SAOL bekräftar två helt orelaterade betydelser (hantverksförening; sned/lutande) -- äkta homonym. SAOL:s definitionstext leder med 'yrkeskår' respektive 'sned'.",
    ),
    "snöplig": dict(
        huvudbetydelse="Som gör en besviken och lite förnedrad, sämre än väntat",
        register="neutral, negativ",
        synonymer=["försmädlig"],
        exempelmening='Laget förlorade på ett <font color="#3498db">snöpligt</font> självmål i sista minuten.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'försmädlig'.",
    ),
    "svepande": dict(
        huvudbetydelse="Allmänt hållen och inte särskilt detaljerad, om till exempel ett uttalande ; röra sig snabbt i en vid rörelse",
        register="neutral, neutral",
        synonym_groups=[[], ["stryka"]],
        exempelmening='Talaren gav bara en <font color="#3498db">svepande</font> beskrivning av planerna, utan några konkreta detaljer.',
        slutsats="SO ger flera betydelser -- två tas med (vag/allmänt hållen; snabb vid rörelse), de mer facktekniska (linda in lik, minsvepning) utelämnade som mindre relevanta. SAOL:s definitionstext leder andra ledet med 'stryka'. Ingen belagd synonym för den vaga/allmänt hållna betydelsen -- tom grupp.",
    ),
    "teatralisk": dict(
        huvudbetydelse="Överdrivet dramatisk och konstlad, som på en teaterscen",
        register="neutral, negativ",
        synonymer=["högtravande"],
        exempelmening='Hans <font color="#3498db">teatraliska</font> gester fick publiken att skratta.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'högtravande'.",
    ),
    "unilateral": dict(
        huvudbetydelse="Som bara gäller eller beslutas av en part, inte flera tillsammans",
        register="formell, neutral, politik",
        synonymer=["ensidig"],
        exempelmening='Landet genomförde en <font color="#3498db">unilateral</font> nedrustning utan att vänta på motparten.',
        slutsats="SO/SAOL överens: en betydelse. SAOL:s definitionstext ÄR ordet 'ensidig'.",
    ),
    "vederstygglig": dict(
        huvudbetydelse="Ytterst motbjudande och äcklig",
        register="ngt ålderdomlig, negativ",
        synonymer=["avskyvärd"],
        exempelmening='Slagfältet efter striden var en <font color="#3498db">vederstygglig</font> syn.',
        slutsats="SO/SAOL överens: en betydelse. SAOL:s definitionstext leder med 'avskyvärd'.",
    ),
    "verkställa": dict(
        huvudbetydelse="Genomföra eller utföra något som bestämts, till exempel ett beslut",
        register="formell, neutral, juridik",
        synonymer=["utföra"],
        exempelmening='Kommunen fick i uppdrag att <font color="#3498db">verkställa</font> regeringens nya beslut.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'utföra'.",
    ),
    "adrenalin": dict(
        huvudbetydelse="Ett hormon i kroppen som gör en piggare och skärper reaktionerna, särskilt vid stress eller fara",
        register="fackspråklig, neutral, medicin",
        synonymer=[],
        exempelmening='<font color="#3498db">Adrenalinet</font> pumpade genom kroppen när han stod högst upp på berget.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen ordboksbelagd enordssynonym -- definitionerna är beskrivande fraser, inte utbytbara ord. Tom lista.",
    ),
    "agglomerat": dict(
        huvudbetydelse="En bergart gjord av grova, kantiga vulkanbitar som klumpat ihop sig med finare material",
        register="fackspråklig, neutral, geologi",
        synonymer=["hopgyttring"],
        exempelmening='Berget bestod av ett <font color="#3498db">agglomerat</font> format av ett gammalt vulkanutbrott.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext ÄR ordet 'hopgyttring'.",
    ),
    "agrikultur": dict(
        huvudbetydelse="Jordbruk",
        register="formell, neutral",
        synonymer=["åkerbruk", "jordbruk"],
        exempelmening='Landets ekonomi byggde till stor del på <font color="#3498db">agrikultur</font>.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext ('åkerbruk, jordbruk') ger båda orden i samma led.",
    ),
    "aktuarie": dict(
        huvudbetydelse="En tjänsteman som gör statistiska beräkningar, till exempel åt ett försäkringsbolag",
        register="fackspråklig, neutral, ekonomi",
        synonymer=[],
        exempelmening='<font color="#3498db">Aktuarien</font> räknade ut hur stor risken var att så många skulle bli sjuka samtidigt.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen ordboksbelagd enordssynonym -- definitionerna är beskrivande fraser. Tom lista.",
    ),
    "alumn": dict(
        huvudbetydelse="En tidigare elev eller student vid en skola eller ett universitet",
        register="högtidlig, neutral",
        synonymer=[],
        exempelmening='Skolan bjöd in alla sina <font color="#3498db">alumner</font> till 50-årsjubileet.',
        slutsats="SO ger två släkta betydelser (lärjunge/skyddsling; f.d. elev/student) -- SO noterar 'numera särsk.' den senare, som är den moderna huvudanvändningen och den enda som tas med. SAOL markerar 'något högtidligt'. Ingen enordssynonym i definitionstexten -- tom lista.",
    ),
    "amfiteater": dict(
        huvudbetydelse="En utomhusscen omgiven av bänkar som stiger i trappsteg runt om",
        register="neutral, neutral",
        synonymer=[],
        exempelmening='Gladiatorerna kämpade inför tiotusentals åskådare i den antika <font color="#3498db">amfiteatern</font>.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen enordssynonym i definitionstexten -- tom lista.",
    ),
    "antagonism": dict(
        huvudbetydelse="Ett tillstånd av fiendskap eller stark motsättning mellan parter",
        register="formell, negativ",
        synonymer=["motsättning"],
        exempelmening='Det rådde djup <font color="#3498db">antagonism</font> mellan de två folkgrupperna efter kriget.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'motsättning'.",
    ),
    "antagonistisk": dict(
        huvudbetydelse="Som befinner sig i konflikt eller motsättning med något annat",
        register="formell, negativ",
        synonymer=[],
        exempelmening='De två maktblocken hade en långvarigt <font color="#3498db">antagonistisk</font> relation.',
        slutsats="SO ger huvudbetydelsen plus en medicinsk specialanvändning (t.ex. antagonistiska muskler) -- den senare utelämnad som för smal. Ingen enordssynonym i SO:s definitionstext (beskrivande fras) -- tom lista.",
    ),
    "artefakt": dict(
        huvudbetydelse="Ett föremål som är gjort av en människa, ofta ett arkeologiskt fynd",
        register="fackspråklig, neutral",
        synonymer=["konstprodukt"],
        exempelmening='Arkeologerna hittade flera <font color="#3498db">artefakter</font> av keramik vid utgrävningen.',
        slutsats="SO/SAOL överens: en betydelse. SAOL:s definitionstext leder med 'konstprodukt'.",
    ),
    "audiens": dict(
        huvudbetydelse="Tillstånd att få besöka en högt uppsatt person, till exempel en kung eller påve",
        register="formell, neutral",
        synonymer=["mottagning"],
        exempelmening='Han fick <font color="#3498db">audiens</font> hos påven under sin resa till Rom.',
        slutsats="SO/SAOL överens: en betydelse. SAOL:s definitionstext lägger till 'mottagning' i samma led -- belagd synonym.",
    ),
    "auktoritativ": dict(
        huvudbetydelse="Som man kan lita på för att den kommer från stor kunskap eller makt",
        register="formell, positiv",
        synonymer=["vederhäftig"],
        exempelmening='Rapporten räknades som en <font color="#3498db">auktoritativ</font> källa eftersom den var nära knuten till regeringen.',
        slutsats="SO/SAOL överens: en betydelse. SAOL:s definitionstext leder med 'vederhäftig'.",
    ),
    "autokrat": dict(
        huvudbetydelse="En härskare som har all makt själv, utan att dela den med någon",
        register="formell, negativ",
        synonymer=["självhärskare"],
        exempelmening='Landet styrdes i decennier av en <font color="#3498db">autokrat</font> som inte tillät någon opposition.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext ÄR ordet 'självhärskare'.",
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
        c["sokkoll"] = {"kalla": kalla(ord_), "slutsats": spec["slutsats"]}
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
