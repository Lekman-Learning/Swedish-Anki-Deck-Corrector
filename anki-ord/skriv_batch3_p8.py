# -*- coding: utf-8 -*-
"""Skriver proposed+sokkoll for chunk 8 (ord 175-199) av 200-korts v3-batch3."""
import json
import urllib.parse

SOKVAG = "sessions/session_2026-08-20_v3-batch3.json"

def kalla(ord_):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(ord_)

POSTER = {
    "sexism": dict(
        huvudbetydelse="En syn på människor där kön avgör deras värde, ofta så att kvinnor värderas lägre",
        register="formell, negativ",
        synonymer=["könsdiskriminering"],
        exempelmening='Företaget anklagades för <font color="#3498db">sexism</font> efter att bara ha befordrat män.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext innehåller ordet 'könsdiskriminering'.",
    ),
    "singularis": dict(
        huvudbetydelse="Singularform, entalsform av ett ord (motsatsen till plural)",
        register="fackspråklig, neutral, lingvistik",
        synonymer=["singular", "ental"],
        exempelmening='Ordet "katt" står i <font color="#3498db">singularis</font>, medan "katter" är plural.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SO:s och SAOL:s definitionstext ÄR orden 'singular'/'ental'.",
    ),
    "självrådig": dict(
        huvudbetydelse="Som handlar på egen hand utan att fråga eller lyssna på andra",
        register="formell, negativ",
        synonymer=["egenmäktig"],
        exempelmening='Chefen kritiserades för sitt <font color="#3498db">självrådiga</font> beslut att avskeda hela avdelningen utan att rådfråga någon.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext ÄR ordet 'egenmäktig'.",
    ),
    "skillingtryck": dict(
        huvudbetydelse="En enkel, folklig visa med lättbegripligt och ofta sentimentalt innehåll, förr tryckt och spridd som billiga blad",
        register="arkaisk, neutral, litteraturvetenskap",
        synonymer=[],
        exempelmening='På torget sålde man <font color="#3498db">skillingtryck</font> med sorgliga visor om olyckliga kärlekspar.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen fristående enordssynonym i definitionstexten -- tom lista.",
    ),
    "skärskåda": dict(
        huvudbetydelse="Granska noga och kritiskt",
        register="formell, neutral",
        synonymer=["granska"],
        exempelmening='Revisorn <font color="#3498db">skärskådade</font> företagets räkenskaper i detalj.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder andra ledet med 'granska'.",
    ),
    "slapphänt": dict(
        huvudbetydelse="Alltför eftergiven och tillåtande, ger efter för lätt",
        register="neutral, negativ",
        synonymer=[],
        exempelmening='Föräldrarna var <font color="#3498db">slapphänta</font> med reglerna och lät barnen göra vad de ville.',
        slutsats="SO/SAOL hänvisar båda till uppslagsordet 'släpphänt' (variantform) -- Wiktionary bekräftar betydelsen ('som ger efter alltför lätt'). Ingen fristående enordssynonym i SO/SAOL:s egen definitionstext (bara en korshänvisning) -- tom lista.",
    ),
    "snusförnuftig": dict(
        huvudbetydelse="Besvärande klok och belärande på ett krystat sätt, ofta om barn som låter vuxna",
        register="neutral, negativ",
        synonymer=["lillgammal"],
        exempelmening='Den <font color="#3498db">snusförnuftiga</font> sexåringen förklarade högtravande varför godis var dåligt för tänderna.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SO+ taggar uttryckligen SYN:synonym, och SAOL:s definitionstext leder andra ledet med 'lillgammal'.",
    ),
    "sociologi": dict(
        huvudbetydelse="Vetenskapen om hur människor beter sig i grupper och samhällen",
        register="fackspråklig, neutral",
        synonymer=[],
        exempelmening='Hon läste <font color="#3498db">sociologi</font> för att förstå varför människor beter sig som de gör i grupp.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen fristående enordssynonym -- tom lista.",
    ),
    "staga": dict(
        huvudbetydelse="Stötta något, till exempel en mast eller ett tält, med rep eller stag ; ordna upp något (bildligt)",
        register="fackspråklig, neutral, sjöfart",
        synonymer=["stötta"],
        exempelmening='De fick <font color="#3498db">staga</font> upp midsommarstången med extra rep innan blåsten tog fart.',
        slutsats="SO ger huvudbetydelsen plus en bildlig, utvidgad användning ('ordna upp', t.ex. 'staga upp statens finanser'). SAOL:s definitionstext ÄR frasen 'stötta med stag'.",
    ),
    "stundom": dict(
        huvudbetydelse="Ibland, vid vissa tillfällen",
        register="ngt ålderdomlig, neutral",
        synonymer=["ibland"],
        exempelmening='Tonen i debatten blev <font color="#3498db">stundom</font> ganska hätsk.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. BRUK 'ngt åld.'. SAOL:s definitionstext leder med 'ibland'.",
    ),
    "substituera": dict(
        huvudbetydelse="Sätta in eller byta ut något mot något annat",
        register="fackspråklig, neutral",
        synonymer=["ersätta"],
        exempelmening='Fabriken <font color="#3498db">substituerade</font> de skadliga kemikalierna med mindre farliga alternativ.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. BRUK 'särsk. i fackspråk'. SAOL:s definitionstext innehåller ordet 'ersätta'.",
    ),
    "tablå": dict(
        huvudbetydelse="En kortfattad översikt eller sammanställning av fakta ; en underavdelning av en akt i en teaterpjäs",
        register="neutral, neutral",
        synonymer=["översikt"],
        exempelmening='<font color="#3498db">Tablån</font> nedan visar koncernens vinstutveckling de senaste fem åren.',
        slutsats="SO/SAOL ger flera betydelser -- de två vanligaste tas med (faktaöversikt; teateraktsavdelning), den ovanligare 'levande tavla'-betydelsen utelämnas. SAOL:s definitionstext leder första ledet med 'översikt'.",
    ),
    "terrin": dict(
        huvudbetydelse="En större, finare skål för att servera till exempel soppa i",
        register="neutral, neutral, matlagning",
        synonymer=["soppskål"],
        exempelmening='Hon bar in soppan i en vit porslins<font color="#3498db">terrin</font>.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext innehåller ordet 'soppskål'.",
    ),
    "tribun": dict(
        huvudbetydelse="En upphöjd plats för att hålla tal eller uppträda inför publik ; en hög ämbetsman i antikens Rom",
        register="neutral, neutral",
        synonymer=["estrad"],
        exempelmening='Talaren klev upp på <font color="#3498db">tribunen</font> för att adressera folkmassan.',
        slutsats="SO/SAOL ger två klart skilda betydelser (upphöjd talarplats; antik romersk ämbetsman). SAOL:s definitionstext för första ledet innehåller ordet 'estrad'.",
    ),
    "tråna": dict(
        huvudbetydelse="Känna en stark och tärande längtan efter något eller någon",
        register="litterär, neutral",
        synonymer=["längta"],
        exempelmening='Hon <font color="#3498db">trånade</font> efter att få resa hem igen efter månader utomlands.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SO+ taggar uttryckligen SYN:synonym, och SAOL:s definitionstext ÄR frasen 'längta intensivt'.",
    ),
    "tumult": dict(
        huvudbetydelse="Ett bråk eller upplopp med många inblandade ; ett virrvarr eller kaos",
        register="neutral, negativ",
        synonymer=["bråk"],
        exempelmening='Det uppstod <font color="#3498db">tumult</font> i salen när domen lästes upp.',
        slutsats="SO ger två släkta betydelser (folkbråk; allmänt virrvarr) -- samma grundidé, tas med tillsammans. SAOL:s definitionstext leder med 'bråk'.",
    ),
    "tyll": dict(
        huvudbetydelse="Ett mycket tunt och genomskinligt tyg av bomull eller silke",
        register="neutral, neutral",
        synonymer=[],
        exempelmening='Bruden bar en slöja av vit <font color="#3498db">tyll</font>.',
        slutsats="SO/SAOL/Wiktionary överens om huvudbetydelsen (SO:s andra, tekniska betydelse om ett munstycke vid spritsning är mycket smal och utelämnas). Ingen fristående enordssynonym -- tom lista.",
    ),
    "undfallande": dict(
        huvudbetydelse="Som lätt ger efter för andras krav eller önskemål",
        register="formell, negativ",
        synonymer=["eftergiven"],
        exempelmening='Läraren ansågs alltför <font color="#3498db">undfallande</font> mot de stökigaste eleverna.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'eftergiven'.",
    ),
    "uppstudsig": dict(
        huvudbetydelse="Som öppet trotsar eller sätter sig upp mot någon med makt över en",
        register="neutral, negativ",
        synonymer=["ohörsam"],
        exempelmening='Den <font color="#3498db">uppstudsiga</font> eleven vägrade följa lärarens instruktioner.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext avslutar med ordet 'ohörsam'.",
    ),
    "usuell": dict(
        huvudbetydelse="Bruklig, vanlig eller sedvanlig",
        register="formell, neutral",
        synonymer=["bruklig"],
        exempelmening='Det är inte <font color="#3498db">usuellt</font> att gäster kommer utan att ha blivit inbjudna.',
        slutsats="Endast SAOL har egen artikel (ingen SO, men SAOB bekräftar), och Wiktionary bekräftar samma betydelse -- tillräckligt belagt. SAOL:s definitionstext ÄR orden 'bruklig, vanlig'.",
    ),
    "veta hur en slipsten ska dras": dict(
        huvudbetydelse="Veta precis hur man ska göra för att nå ett bra resultat, vara erfaren och skicklig",
        register="vardaglig, positiv",
        synonymer=[],
        exempelmening='Efter tjugo år i branschen vet han verkligen <font color="#3498db">hur en slipsten ska dras</font>.',
        slutsats="Sökträffarna är kraftigt kontaminerade (SAOL-raden visar av misstag artikeln för musikstilen 'ska', helt orelaterat). SO:s egen träfflista innehåller dock frasens exakta betydelse ordagrant: 'veta hur man ska göra för att nå resultat'. Ingen enordssynonym -- tom lista.",
    ),
    "voja sig": dict(
        huvudbetydelse="Klaga eller beklaga sig",
        register="dialektal, negativ",
        synonymer=["beklaga"],
        exempelmening='Han satt och <font color="#3498db">vojade sig</font> över att det regnade hela sommarlovet.',
        slutsats="SO/SAOL/synonymer.se överens: en betydelse (SAOL hänvisar till grundformen 'voja'). SO:s definitionstext ÄR frasen 'beklaga sig'.",
    ),
    "vräka": dict(
        huvudbetydelse="Kasta eller slunga något med kraft ; tvinga någon att flytta från sin bostad",
        register="neutral, negativ",
        synonym_groups=[["kasta"], ["avhysa"]],
        exempelmening='Hyresvärden hotade att <font color="#3498db">vräka</font> familjen om hyran inte betalades i tid.',
        slutsats="SO ger flera betydelser -- de två mest centrala och vardagliga tas med (våldsam kaströrelse; avhysning från bostad), övriga (sälja billigt, ligga utsträckt, komma i stora mängder) utelämnade som mindre framträdande. SO+ taggar uttryckligen SYN:synonym för avhysningsbetydelsen, och SAOL:s definitionstext leder första respektive andra ledet med 'kasta' och 'avhysa'.",
    ),
    "våndas": dict(
        huvudbetydelse="Känna djup ångest eller vånda över något",
        register="litterär, negativ",
        synonymer=["ångest"],
        exempelmening='Hon <font color="#3498db">våndades</font> över vilka ord hon skulle välja i avskedsbrevet.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext innehåller ordet 'ångest' (ordet 'vånda' självt utelämnat som synonym eftersom det delar rot med uppslagsordet).",
    ),
    "öppenhjärtig": dict(
        huvudbetydelse="Som är ärlig och inte döljer sina åsikter eller känslor",
        register="neutral, positiv",
        synonymer=["uppriktig"],
        exempelmening='Hon var <font color="#3498db">öppenhjärtig</font> om svårigheterna hon haft under sjukdomen.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder andra ledet med 'uppriktig'.",
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
