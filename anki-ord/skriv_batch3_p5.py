# -*- coding: utf-8 -*-
"""Skriver proposed+sokkoll for chunk 5 (ord 100-124) av 200-korts v3-batch3."""
import json
import urllib.parse

SOKVAG = "sessions/session_2026-08-20_v3-batch3.json"

def kalla(ord_):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(ord_)

POSTER = {
    "excentriker": dict(
        huvudbetydelse="En person med udda och ovanliga vanor eller åsikter",
        register="neutral, neutral",
        synonymer=[],
        exempelmening='Morbrodern var en <font color="#3498db">excentriker</font> som samlade på gamla gevär.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SO:s definitionstext ('excentrisk person') delar rot med uppslagsordet -- ingen fristående synonym. Tom lista.",
    ),
    "extrovert": dict(
        huvudbetydelse="Utåtriktad och öppen till sin läggning, tycker om att vara med andra människor",
        register="neutral, neutral, psykologi",
        synonymer=["utåtvänd"],
        exempelmening='Hon är väldigt <font color="#3498db">extrovert</font> och trivs bäst i stora sällskap.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'utåtvänd'.",
    ),
    "firmament": dict(
        huvudbetydelse="Himlavalvet, himlen som man ser stjärnorna på",
        register="högtidlig, neutral",
        synonymer=["himlavalv"],
        exempelmening='Inga stjärnor syntes ännu på <font color="#3498db">firmamentet</font> den klara sommarkvällen.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. BRUK 'något högtidligt'. SAOL:s definitionstext ÄR ordet 'himlavalv'.",
    ),
    "flagrant": dict(
        huvudbetydelse="Så uppenbar och påtaglig att den inte går att bortförklara, om något klandervärt",
        register="formell, negativ",
        synonymer=["uppenbar"],
        exempelmening='Domaren kallade det ett <font color="#3498db">flagrant</font> brott mot reglerna.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'uppenbar'.",
    ),
    "florstunn": dict(
        huvudbetydelse="Mycket tunn och genomskinlig, som en tunn slöja",
        register="litterär, neutral",
        synonymer=[],
        exempelmening='Bruden bar en <font color="#3498db">florstunn</font> vit klänning som fladdrade i vinden.',
        slutsats="Ordet är en sammansättning (SO/SAOL: hänvisar till komponenterna 'flor', ett slags tunt tyg/slöja, och 'tunn') utan egen fristående definitionstext -- bekräftat i rådata (compound_target). Betydelsen härleds direkt ur sammansättningen. Ingen enordssynonym i definitionstexten (bara synonymer.se-kandidater finns, inte facit) -- tom lista.",
    ),
    "foton": dict(
        huvudbetydelse="Den minsta enheten av elektromagnetisk strålning, en ljuspartikel ; ett fotografi (vardagligt, kortform)",
        register="fackspråklig, neutral, fysik ; vardaglig, neutral",
        synonym_groups=[["ljuspartikel"], ["fotografi"]],
        exempelmening='En <font color="#3498db">foton</font> är energi utan massa som rör sig med ljusets hastighet.',
        slutsats="SO/SAOL ger två klart skilda betydelser (fysikalisk ljuspartikel; vardaglig kortform för fotografi). SAOL:s definitionstext leder första ledet med 'ljuspartikel' och avslutar andra ledet med 'fotografi'.",
    ),
    "frekvent": dict(
        huvudbetydelse="Som förekommer ofta",
        register="formell, neutral",
        synonymer=["ofta förekommande"],
        exempelmening='Ordet har blivit allt mer <font color="#3498db">frekvent</font> i vardagssvenskan.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext ÄR frasen 'ofta förekommande'.",
    ),
    "friktion": dict(
        huvudbetydelse="Motstånd mellan två ytor som gnids mot varandra ; slitningar eller konflikter mellan människor som samarbetar",
        register="fackspråklig, neutral, fysik ; neutral, negativ",
        synonymer=["gnidning"],
        exempelmening='Det uppstod en del <font color="#3498db">friktion</font> mellan de nya kollegorna under det första året.',
        slutsats="SO/SAOL ger två klart skilda betydelser (fysikaliskt motstånd; social konflikt) -- SAOL:s egen definitionstext bekräftar båda ('motstånd i kontaktyta ...; slitningar vid samarbete'). SAOL:s definitionstext leder första ledet med 'gnidning'.",
    ),
    "fähus": dict(
        huvudbetydelse="En ladugård, en byggnad där man förr höll boskap",
        register="ngt ålderdomlig, neutral",
        synonymer=["ladugård"],
        exempelmening='Bönderna drev korna till <font color="#3498db">fähuset</font> varje kväll.',
        slutsats="SO/Wiktionary överens: en betydelse. BRUK 'något ålderdomligt'. SO:s definitionstext ÄR ordet 'ladugård'.",
    ),
    "förbistra": dict(
        huvudbetydelse="Göra något förvirrande eller obegripligt",
        register="formell, neutral",
        synonymer=["förvirra"],
        exempelmening='Alla de motsägande instruktionerna bara <font color="#3498db">förbistrade</font> nybörjarna ännu mer.',
        slutsats="Endast SAOL har egen artikel (ingen SO, men SAOB bekräftar samma ord), och SAOL ger en tydlig, entydig definition -- tillräckligt belagt. SAOL:s definitionstext leder andra ledet med 'förvirra'.",
    ),
    "företrädesvis": dict(
        huvudbetydelse="Huvudsakligen eller helst",
        register="formell, neutral",
        synonymer=["huvudsakligen", "helst"],
        exempelmening='Kursen vänder sig <font color="#3498db">företrädesvis</font> till nybörjare, även om alla är välkomna.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SO:s definitionstext ÄR orden 'huvudsakligen' och 'helst' (två alternativa enordsformuleringar).",
    ),
    "förtjänt": dict(
        huvudbetydelse="Som har gjort sig värd något, till exempel beröm eller belöning",
        register="formell, positiv",
        synonymer=["värd"],
        exempelmening='Hon fick ett pris för sin <font color="#3498db">förtjänta</font> insats inom forskningen.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SO:s definitionstext ÄR ordet 'värd' (en av två alternativa enordsformuleringar).",
    ),
    "förtälja": dict(
        huvudbetydelse="Berätta",
        register="ngt ålderdomlig, neutral",
        synonymer=[],
        exempelmening='Mer än så <font color="#3498db">förtäljer</font> inte historien om vad som hände den natten.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SO/SAOL:s definitionstext ÄR ordet 'berätta', redan huvudbetydelsen -- ingen ytterligare synonym att lägga till. Tom lista.",
    ),
    "förvillelse": dict(
        huvudbetydelse="En felaktig och klandervärd uppfattning eller övertygelse man förletts in i",
        register="formell, negativ",
        synonymer=[],
        exempelmening='I sin ungdom drabbades han av den nazistiska <font color="#3498db">förvillelsen</font>.',
        slutsats="SO/Wiktionary överens: en betydelse. Ingen fristående enordssynonym i SO:s definitionstext (en beskrivande fras) -- tom lista.",
    ),
    "gassig": dict(
        huvudbetydelse="Mycket varmt på grund av starkt solsken",
        register="vardaglig, neutral",
        synonymer=[],
        exempelmening='Det var redan <font color="#3498db">gassigt</font> ute när de vaknade på morgonen.',
        slutsats="SO/synonymer.se överens: en betydelse. Ingen fristående enordssynonym i SO:s definitionstext -- tom lista.",
    ),
    "giga": dict(
        huvudbetydelse="Ett medeltida stråkinstrument, en sorts fiol ; en miljard (slang, särskilt om pengar)",
        register="arkaisk, neutral",
        synonym_groups=[["fiol"], []],
        exempelmening='Musikern spelade på en <font color="#3498db">giga</font> under medeltidsmarknaden.',
        slutsats="SO ger två helt orelaterade betydelser (medeltida stråkinstrument; miljard, modern slangbildning till 'giga-') -- äkta homonym. SAOL:s definitionstext för instrumentbetydelsen ÄR ordet 'fiol'. Ingen ordboksbelagd synonym för miljard-betydelsen -- tom grupp.",
    ),
    "girigbuk": dict(
        huvudbetydelse="En girig person",
        register="neutral, nedsättande",
        synonymer=[],
        exempelmening='Han var en sådan <font color="#3498db">girigbuk</font> att han aldrig bjöd på något.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. BRUK 'nedsättande'. Ingen fristående enordssynonym utöver definitionens eget adjektiv -- tom lista.",
    ),
    "god man": dict(
        huvudbetydelse="En person som utses av domstol för att sköta ekonomi eller andra angelägenheter åt någon som inte klarar det själv",
        register="formell, neutral, juridik",
        synonymer=[],
        exempelmening='Den äldre mannen fick en <font color="#3498db">god man</font> som skötte hans räkningar och kontakter med myndigheter.',
        slutsats="Sökträffarna för frasen 'god man' är kraftigt kontaminerade av andra artiklar (gods, gård, embankment m.m. -- fritextsökningen matchar de enskilda orden 'god' och 'man' brett). Den juridiska betydelsen bekräftas i stället av Wiktionarys precisa definition ('fysisk person som utses av allmän domstol för att utföra ett visst uppdrag') plus SO:s egen EX-mening som visar bruket. Ingen enordssynonym tas med eftersom source-listan för denna specifika betydelse inte går att skilja ut ur SO/SAOL:s kontaminerade träfflista -- tom lista, säkrast så.",
    ),
    "göra avkall på": dict(
        huvudbetydelse="Sänka sina krav eller kvalitet inom något, gå med på ett sämre alternativ",
        register="neutral, neutral",
        synonymer=[],
        exempelmening='Företaget vägrade <font color="#3498db">göra avkall på</font> kvaliteten trots de höga kostnaderna.',
        slutsats="Sökträffarna är kraftigt kontaminerade (frasen 'göra avkall på' hör till uppslagsordet 'avkall', men fritextsökningen drar in orelaterade artiklar för 'göra'/'man' m.m.). Betydelsen bekräftas av SO:s egen EX-mening ('hon ville inte ge avkall på kvaliteten'), som direkt visar bruket. Ingen enordssynonym tas med -- tom lista, säkrast så givet kontamineringen.",
    ),
    "görlig": dict(
        huvudbetydelse="Möjlig att genomföra eller göra",
        register="formell, neutral",
        synonymer=["möjlig"],
        exempelmening='Han lovade att hålla kontakten så ofta det var <font color="#3498db">görligt</font>.',
        slutsats="SO/SAOL överens: en betydelse. Båda definitionstexterna ('möjlig att genomföra'/'möjlig att åstadkomma') leder med 'möjlig'.",
    ),
    "halogen": dict(
        huvudbetydelse="En typ av grundämne, till exempel fluor, klor, brom och jod, vars föreningar med metaller bildar salter",
        register="fackspråklig, neutral, kemi",
        synonymer=["saltbildare"],
        exempelmening='Klor är en <font color="#3498db">halogen</font> som används för att rena vatten.',
        slutsats="SO/synonymer.se överens: en betydelse. SO+ taggar uttryckligen SYN:synonym, matchande JFR-korsreferensen 'saltbildare'.",
    ),
    "handtryckning": dict(
        huvudbetydelse="Ett handslag, att skaka hand ; en mindre muta (bildligt)",
        register="ngt ålderdomlig, neutral",
        synonymer=["muta"],
        exempelmening='Han kände att hon svarade på hans <font color="#3498db">handtryckning</font> med ett leende.',
        slutsats="SO ger två klart skilda betydelser (bokstavligt handslag; bildligt om muta). BRUK 'något ålderdomligt'. SO:s definitionstext för andra ledet ÄR ordet 'muta'.",
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
