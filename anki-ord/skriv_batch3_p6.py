# -*- coding: utf-8 -*-
"""Skriver proposed+sokkoll for chunk 6 (ord 125-149) av 200-korts v3-batch3."""
import json
import urllib.parse

SOKVAG = "sessions/session_2026-08-20_v3-batch3.json"

def kalla(ord_):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(ord_)

POSTER = {
    "harakiri": dict(
        huvudbetydelse="Rituellt japanskt självmord genom uppristning av magen ; ett vettlöst handlande som leder till katastrof (bildligt)",
        register="högtidlig, neutral",
        synonymer=[],
        exempelmening='Han kallade sitt beslut att satsa hela sparkontot på en enda aktie för ekonomisk <font color="#3498db">harakiri</font>.',
        slutsats="SO/SAOL/Wiktionary överens om huvudbetydelsen, SO lägger till en bildlig, allmännare betydelse. Ingen enordssynonym i definitionstexten -- tom lista.",
    ),
    "hjärtnupen": dict(
        huvudbetydelse="Som lätt blir rörd eller känslosam",
        register="neutral, neutral",
        synonymer=["lättrörd"],
        exempelmening='Mormor blev alltid <font color="#3498db">hjärtnupen</font> när barnbarnen sjöng för henne.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SO+ taggar uttryckligen SYN:synonym, och SAOL:s definitionstext ÄR ordet 'lättrörd'.",
    ),
    "idiosynkrasi": dict(
        huvudbetydelse="En stark motvilja eller överkänslighet mot något ; en personlig egenhet eller ett särdrag",
        register="fackspråklig, neutral, medicin ; formell, neutral",
        synonymer=["överkänslighet", "avsky"],
        exempelmening='Han utvecklade med åren en stark <font color="#3498db">idiosynkrasi</font> mot fisk.',
        slutsats="SO ger två klart skilda betydelser (motvilja/överkänslighet; personlig egenhet). SAOL:s definitionstext leder med 'överkänslighet' och nämner 'avsky' i samma led.",
    ),
    "illumination": dict(
        huvudbetydelse="Festlig belysning, till exempel av en byggnad eller plats ; utsmyckning av en handskrift med färglagda bilder och initialer",
        register="neutral, positiv",
        synonymer=["illustration"],
        exempelmening='Slottet badade i <font color="#3498db">illumination</font> under jubileumsfirandet.',
        slutsats="SO ger tre nära betydelser (festlig upplysning; färgläggning; illustration) -- de två senare är samma grundidé (handskriftsutsmyckning), slås ihop. SO:s definitionstext ÄR ordet 'illustration' för den betydelsen.",
    ),
    "impressario": dict(
        huvudbetydelse="En person som ordnar uppträdanden och turnéer åt artister",
        register="fackspråklig, neutral, konst",
        synonymer=[],
        exempelmening='Sångerskans <font color="#3498db">impressario</font> bokade in konserter i hela Europa.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen fristående enordssynonym i definitionstexten -- tom lista.",
    ),
    "indisponerad": dict(
        huvudbetydelse="Tillfälligt i dålig form eller lätt sjuk",
        register="formell, negativ",
        synonymer=[],
        exempelmening='Frun var <font color="#3498db">indisponerad</font> och kunde inte komma till middagen.',
        slutsats="SO/SAOL överens: en kärnbetydelse (SO:s tredje nyans 'som inte har lust' är en försvagad variant av samma idé, utelämnad). Ingen fristående enordssynonym -- SAOL:s definitionstext är korta fraser, inte enskilda utbytbara ord. Tom lista.",
    ),
    "induktion": dict(
        huvudbetydelse="En tankemetod där man drar allmänna slutsatser utifrån enskilda iakttagelser ; alstring av elektrisk spänning genom ett förändrat magnetfält",
        register="fackspråklig, neutral, filosofi ; fackspråklig, neutral, fysik",
        synonymer=[],
        exempelmening='Genom <font color="#3498db">induktion</font> drog forskaren en allmän slutsats utifrån de enskilda observationerna.',
        slutsats="SO ger två helt orelaterade betydelser (logisk slutledningsmetod; fysikaliskt fenomen) -- äkta homonym, bekräftat av SO:s egen MOTSATS-notering (mot deduktion) för den första. Ingen enordssynonym i definitionstexten -- tom lista.",
    ),
    "kamrer": dict(
        huvudbetydelse="En tjänsteman med ansvar för ekonomisk förvaltning och bokföring",
        register="formell, neutral",
        synonymer=[],
        exempelmening='<font color="#3498db">Kamreraren</font> gick igenom företagets räkenskaper varje kvartal.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen fristående enordssynonym -- tom lista.",
    ),
    "karott": dict(
        huvudbetydelse="Ett skålformigt fat för att lägga upp mat på ; en liten, trubbig morot",
        register="neutral, neutral",
        synonymer=["serveringskärl"],
        exempelmening='Hon ställde fram sallad i en stor <font color="#3498db">karott</font> mitt på bordet.',
        slutsats="SO/SAOL ger två helt orelaterade betydelser (serveringsfat; morotssort) -- äkta homonym med olika ursprung. SAOL:s definitionstext för första ledet innehåller ordet 'serveringskärl'.",
    ),
    "kartell": dict(
        huvudbetydelse="En sammanslutning mellan självständiga företag som samarbetar för att begränsa konkurrensen ; ett samarbete mellan politiska partier, till exempel vid val",
        register="fackspråklig, neutral, ekonomi ; formell, neutral, politik",
        synonymer=[],
        exempelmening='Byggföretagens likartade anbud väckte misstankar om en hemlig <font color="#3498db">kartell</font>.',
        slutsats="SO/SAOL ger två släkta betydelser (företagssamverkan; partisamverkan). Ingen fristående enordssynonym -- tom lista.",
    ),
    "katarakt": dict(
        huvudbetydelse="Ett stort vattenfall som störtar utför en brant klippa ; grå starr, en ögonsjukdom",
        register="neutral, neutral",
        synonymer=["gråstarr"],
        exempelmening='Turisterna beundrade de mäktiga <font color="#3498db">katarakterna</font> i Nilen.',
        slutsats="SO/SAOL ger två helt orelaterade betydelser (vattenfall; ögonsjukdom) -- äkta homonym. SAOL:s definitionstext för andra ledet ÄR ordet 'gråstarr'.",
    ),
    "kleresi": dict(
        huvudbetydelse="Prästerskapet, särskilt inom den katolska kyrkan",
        register="ngt ålderdomlig, neutral, religion",
        synonymer=["prästerskap"],
        exempelmening='<font color="#3498db">Kleresiet</font> hade stort inflytande över det medeltida samhället.',
        slutsats="SO/SAOL överens: en betydelse. BRUK 'något ålderdomligt'. SAOL:s definitionstext leder med 'prästerskap'.",
    ),
    "kohort": dict(
        huvudbetydelse="En truppavdelning som var en del av en romersk legion, förr i tiden ; en grupp människor med gemensamma kännetecken, till exempel i en studie",
        register="arkaisk, neutral, historia",
        synonym_groups=[["truppavdelning"], ["grupp"]],
        exempelmening='Forskarna följde en <font color="#3498db">kohort</font> av 500 patienter under tio år.',
        slutsats="SO/SAOL ger två klart skilda betydelser (antik truppenhet; modern grupp med gemensamma drag, t.ex. inom medicin/sociologi). SAOL:s definitionstext leder båda leden med 'truppavdelning' respektive 'grupp'.",
    ),
    "kollektion": dict(
        huvudbetydelse="En samling värdefulla föremål ; en uppsättning nya kläder som visas upp, till exempel på en modevisning",
        register="neutral, neutral",
        synonymer=["samling"],
        exempelmening='Modehuset visade sin nya <font color="#3498db">kollektion</font> på catwalken i Paris.',
        slutsats="SO ger huvudbetydelsen plus en specialtillämpning på modevisningskläder -- bägge tas med då den senare är den vanligaste i dagligt bruk. SO:s definitionstext ÄR ordet 'samling'.",
    ),
    "konform": dict(
        huvudbetydelse="Som stämmer överens i formen",
        register="fackspråklig, neutral, matematik",
        synonymer=["likformig"],
        exempelmening='En <font color="#3498db">konform</font> avbildning bevarar vinklarna mellan kurvor.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'likformig'.",
    ),
    "kreera": dict(
        huvudbetydelse="Skapa något nytt ; framföra en roll för första gången ; utnämna någon till en titel",
        register="ngt ålderdomlig, neutral",
        synonymer=["skapa", "utnämna"],
        exempelmening='Skådespelerskan fick <font color="#3498db">kreera</font> huvudrollen i den nya pjäsen.',
        slutsats="SO ger tre klart skilda betydelser (skapa; framföra en roll första gången; utnämna). BRUK 'formellt; något ålderdomligt'. SAOL:s definitionstext leder första och tredje ledet med 'skapa' respektive 'utnämna'.",
    ),
    "kronvittne": dict(
        huvudbetydelse="En brottsling som vittnar mot sina medbrottslingar mot löfte om lindrigare straff",
        register="fackspråklig, neutral, juridik",
        synonymer=[],
        exempelmening='Åklagaren erbjöd honom att bli <font color="#3498db">kronvittne</font> i utbyte mot ett kortare straff.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse (SAOL:s definitionstext identisk med SO:s). Ingen fristående enordssynonym -- tom lista.",
    ),
    "kryptera": dict(
        huvudbetydelse="Göra ett meddelande eller information oläslig för andra genom en hemlig kod",
        register="fackspråklig, neutral, IT",
        synonymer=[],
        exempelmening='Företaget <font color="#3498db">krypterar</font> all sin e-post för att skydda känslig information.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Ingen fristående enordssynonym -- tom lista.",
    ),
    "kvacksalvare": dict(
        huvudbetydelse="En person som utger sig för att vara läkare eller kunnig inom medicin utan att egentligen vara det",
        register="vardaglig, nedsättande",
        synonymer=["kvackare"],
        exempelmening='Byns <font color="#3498db">kvacksalvare</font> sålde mirakelmedicin som inte botade någonting.',
        slutsats="SO/synonymer.se överens: en betydelse. BRUK 'vardagligt, nedsättande'. SO:s definitionstext ÄR ordet 'kvackare'.",
    ),
    "kverulera": dict(
        huvudbetydelse="Klaga och gnälla ihärdigt, ofta över småsaker",
        register="ngt ålderdomlig, negativ",
        synonymer=["klaga"],
        exempelmening='Grannen <font color="#3498db">kverulerade</font> ständigt över de höga skatterna.',
        slutsats="SO/SAOL överens: en betydelse. BRUK 'något ålderdomligt'. SAOL:s definitionstext innehåller ordet 'klaga'.",
    ),
    "latta": dict(
        huvudbetydelse="En tunn ribba av trä eller liknande material",
        register="fackspråklig, neutral, sjöfart",
        synonymer=["träribba"],
        exempelmening='Han bytte ut en trasig <font color="#3498db">latta</font> i det stora seglet.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext ÄR frasen 'tunn träribba'.",
    ),
    "libell": dict(
        huvudbetydelse="En liten bubbla i vätska som visar om något är rakt eller i våg, till exempel i ett vattenpass ; en smädeskrift (ålderdomligt)",
        register="fackspråklig, neutral, teknik",
        synonymer=[],
        exempelmening='Han la <font color="#3498db">libellen</font> mot bordsskivan för att kontrollera att den var helt plan.',
        slutsats="SO:s egen definitionstext täcker bara mätverktygsbetydelsen. Wiktionary bekräftar en andra, ålderdomlig betydelse (smädesskrift/flygskrift), som synonymer.se:s lista också speglar -- tas med som andra betydelse men utan synonym eftersom den saknar stöd i SO/SAOL:s egen definitionstext. Ingen enordssynonym för mätverktygsbetydelsen heller -- tom lista.",
    ),
    "liknöjd": dict(
        huvudbetydelse="Helt ointresserad och likgiltig",
        register="neutral, negativ",
        synonymer=["likgiltig"],
        exempelmening='"Det spelar ingen roll", sa han <font color="#3498db">liknöjt</font> och ryckte på axlarna.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SAOL:s definitionstext leder med 'likgiltig'.",
    ),
    "luxation": dict(
        huvudbetydelse="En ledskada där ledytorna glidit isär, en urledvridning",
        register="fackspråklig, neutral, medicin",
        synonymer=["urledvridning"],
        exempelmening='Han fick en <font color="#3498db">luxation</font> i axelleden efter fallet från cykeln.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. SO+ taggar uttryckligen SYN:synonym, och SAOL:s definitionstext ÄR ordet 'urledvridning'.",
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
