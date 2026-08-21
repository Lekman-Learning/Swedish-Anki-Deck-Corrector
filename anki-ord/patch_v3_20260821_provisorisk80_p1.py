# -*- coding: utf-8 -*-
"""80-kortsuppdraget, del 1/4 (kort 0-19 av v3_provisorisk_80_riskval.json).

Urval: v3_urgency_provisorisk.py (risk+exponering) kombinerat med en
SO/SAOL-kopieringssignal (select_risky_provisorisk.py, se den filens
docstring och rättelsen där om felaktig källattribution). Poolen är alltså
"provisoriska kort som SANNOLIKT ar fel", inte bara "mest akuta".

Varje ord nedan ar verifierat mot uppslag/<ord>.json (SO+SAOL+SAOB+
synonymer.se+Wiktionary), hamtat av slaupp.py i den har sessionen.
"""
import json
import urllib.parse

SESSION = "sessions/session_2026-08-21_v3-omgranskning.json"


def hl(w):
    return f'<font color="#3498db">{w}</font>'


def kalla(ord_):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(ord_, safe="")


KORT = {
    "oaktat": {
        "hb": "Trots något ; Fastän, även om",
        "syn": ["trots", "fastän"], "grp": [["trots"], ["fastän"]],
        "ex": f'Vi fortsatte mötet {hl("oaktat")} alla protester.',
        "reg": "formell, neutral ; ngt ålderdomlig, neutral",
        "ety": "Efter tyska ungeachtet, besläktat med ordet akta.",
        "skal": "SO ger TVÅ ordklasser: preposition ('2trots', markerad 'något "
                "formellt') och konjunktion ('fastän', markerad 'något "
                "ålderdomligt'). Kortet hade bara konjunktionsbetydelsen och "
                "registret var satt till 'arkaisk' -- SO säger uttryckligen "
                "'något ålderdomligt', inte helt ur bruk. OLD-facit bekräftar "
                "båda användningarna (prep-exempel om gränsvärden, konj-exempel "
                "om att nå fram). Synonymerna är SO:s/SAOL:s egna definitioner.",
    },
    "hövisk": {
        "hb": "Artig, belevad och fint uppträdande, gärna ridderligt ; (om kärlek, förr) byggd på beundran utan sexuell inblandning",
        "syn": ["ärbar", "taktfull", "ridderlig"], "grp": None,
        "ex": f'Han bugade sig {hl("hövisk")} och höll upp dörren åt henne.',
        "reg": "neutral, positiv ; litterär, ömsint",
        "ety": "Fornsvenska hövisker, av lågtyska hövesch, till hov -- efter franska courtois.",
        "skal": "Huvudbetydelsen var SO:s definitionstext ORDAGRANT kopierad "
                "('artig och taktfull på ett förfinat och elegant sätt' = "
                "kortets exakta text) -- Adam-tal-regressionen 2026-08-18. "
                "Omskriven. SO har dessutom en UNDERBETYDELSE kortet saknade: "
                "'hövisk kärlek', en känsloform som betonar tillbedjan och "
                "tonar ned det sexuella, märkt 'särsk. vid beskrivning av "
                "äldre förhållanden'. Tillagd som andra betydelse. Exemplet "
                "var nästan SO:s eget ('en hövisk butler tog emot dem') -- bytt.",
    },
    "tajga": {
        "hb": "Ett stort skogsbälte med nästan bara barrträd, söder om tundran",
        "syn": [], "grp": None,
        "ex": f'{hl("Tajgan")} sträcker sig över stora delar av Sibirien.',
        "reg": "neutral, neutral",
        "ety": "Från ryskans tajga, med samma betydelse.",
        "skal": "SO: 'stort område med uteslutande barrskog'. SAOL preciserar "
                "geografiskt: 'sibiriskt barrskogsområde söder om tundran' -- "
                "den senare precisionen tillagd. Domänen 'formell' i det gamla "
                "registret hade inget stöd (ingen märkning i SO/SAOL) och är "
                "borttagen. Tom synonymlista: 'barrskogsregion' saknar belägg "
                "i SO:s eller SAOL:s egen definitionstext.",
    },
    "kärve": {
        "hb": "Ett hopbundet knippe skördad säd ; även: ett löst knippe av annat, t.ex. gnistor",
        "syn": [], "grp": None,
        "ex": f'Bonden bar {hl("kärven")} över axeln in i logen.',
        "reg": "neutral, neutral",
        "ety": None,
        "skal": "VIKTIGT FYND: SO:s och SAOL:s råa träfflistor för 'kärve' "
                "blandar in en HEL DEL glosor som hör till homografen 'kärv' "
                "(adjektiv: 'sträv, karg, butter') -- klassisk "
                "frammande-uppslagsord-kontaminering för korta ord. Kortets "
                "riktiga innehåll (hopbunden bunt säd) är SO:s förstahandsdef, "
                "nästan ordagrant -- omskrivet nu. SAOL:s äkta andra betydelse "
                "'knippe el. kvast t.ex. av eld [gnistor]' tillagd; "
                "adjektivbetydelserna ('sträv' m.fl.) hör INTE hit och har "
                "uteslutits. Exemplet var SO:s eget ('de satte ut kärvar till "
                "småfåglarna') -- bytt. Tom synonymlista: varken 'halmknippe' "
                "eller 'sädesbunt' är det första ordet i någon SO/SAOL-led.",
    },
    "gepäck": {
        "hb": "Resväskor och annat man har med sig på resan, bagage",
        "syn": ["bagage", "packning"], "grp": None,
        "ex": f'Han packade allt sitt {hl("gepäck")} i en enda gammal resväska.',
        "reg": "vardaglig, neutral",
        "ety": "Från tyska Gepäck, samma betydelse.",
        "skal": "SO märker ordet 'något vardagligt' -- kortets 'arkaisk' var "
                "fel riktning helt och hållet. Rättat. Exemplet låg nästan "
                "ordagrant på SO:s eget ('det var knappt att hon kom på "
                "bussen med allt sitt gepäck') -- bytt. Synonymerna är SO:s "
                "('bagage') och SAOL:s ('packning') egna glosor.",
    },
    "somnambul": {
        "hb": "Sömngångaraktig, som en sömngångare ; en sömngångare",
        "syn": ["sömngångare"], "grp": None,
        "ex": f'Den {hl("somnambula")} patienten hittades stående vid kylskåpet, utan minne av det.',
        "reg": "neutral, neutral",
        "ety": "Franska somnambule, av latinets somnus 'sömn' och ambulare 'vandra'.",
        "skal": "Kortet definierade ordet enbart som substantiv ('Sömngångare') "
                "men det egna exemplet böjer ordet som ADJEKTIV ('den "
                "somnambula patienten') -- en självmotsägelse. SO/SAOL ger "
                "båda ordklasserna ('sömngångaraktig' / 'sömngångare'). "
                "Huvudbetydelsen kompletterad så den täcker exemplet.",
    },
    "harangera": {
        "hb": "Hålla ett hyllande tal till någon ; nämna någon berömmande, utan att nödvändigtvis tala",
        "syn": ["berömma"], "grp": None,
        "ex": f'Han {hl("harangerade")} den avlidne veteranen vid ceremonin.',
        "reg": "neutral, positiv",
        "ety": None,
        "skal": "SO ger TVÅ betydelser: 'hålla (hyllande) tal till' och, "
                "'ofta försvagat', 'omnämna i berömmande ordalag' -- den andra "
                "kräver inget tal alls, bara ett positivt omnämnande. Kortet "
                "hade bara den första. 'hylla'/'prisa' bytta mot 'berömma', "
                "som är SAOL:s egen glosa ('hålla högtidstal till; berömma') "
                "-- de förra är inte ledande ord i någon SO/SAOL-definition.",
    },
    "lux": {
        "hb": "En enhet som mäter hur starkt något är upplyst",
        "syn": [], "grp": None,
        "ex": f'Rummet hade en belysning på 500 {hl("lux")}.',
        "reg": "neutral, neutral",
        "ety": "Latinets lux, som betyder 'ljus'.",
        "skal": "Huvudbetydelsen var SO:s OCH SAOL:s definitionstext "
                "ordagrant ('en måttenhet för belysningsstyrka' i båda) -- "
                "omskriven. En fysikalisk måttenhet har liten "
                "omformuleringsmarginal utan att bli mindre exakt; "
                "domänen 'fackspråklig, fysik' i det gamla registret hade "
                "inget uttryckligt SO/SAOL-stöd och är borttagen till förmån "
                "för neutralt register.",
    },
    "eponym": {
        "hb": "Ett ord som har bildats av ett persons- eller platsnamn",
        "syn": [], "grp": None,
        "ex": f'Ordet \'sandwich\' är ett {hl("eponym")}, uppkallat efter earlen av Sandwich.',
        "reg": "neutral, neutral",
        "ety": None,
        "skal": "SO/SAOL:s definitioner ('ord som bildats på grundval av ett "
                "egennamn') var nästan ordagrant kortets text -- omskriven. "
                "Exemplet var SO:s eget ('exempel på eponymer är volt, watt "
                "och quisling') -- bytt mot ett tydligare, mer konkret "
                "exempel. Tom synonymlista: inga belagda synonymer i SO/SAOL. "
                "Ingen domän satt -- SO/SAOL märker inte ordet fackspråkligt.",
    },
    "encefalit": {
        "hb": "Inflammation i hjärnan",
        "syn": ["hjärninflammation"], "grp": None,
        "ex": f'Epidemisk {hl("encefalit")} är en viral sjukdom som sprids mellan människor.',
        "reg": "fackspråklig, neutral, medicin",
        "ety": "Av grekiskans enkephalos, som betyder 'hjärna'.",
        "skal": "SO/SAOL:s enda glosa är 'hjärninflammation' -- termen har "
                "praktiskt taget ingen omformuleringsmarginal utan att bli "
                "mindre exakt (samma klass som lux/oaktat), löst genom att "
                "dela upp sammansättningen till vanlig svenska. Synonymen är "
                "ordbokens egen enda glosa. Domän 'medicin' säker: ordet är "
                "ett sällsynt facktermer utan popularitetskonflikt.",
    },
    "oval": {
        "hb": "Rund och avlångt formad, som ett ägg ; en figur med den formen",
        "syn": ["äggrund", "avlångt rund"], "grp": None,
        "ex": f'Bordet i matsalen var {hl("ovalt")}.',
        "reg": "neutral, neutral",
        "ety": "Bildat av latinets ovum, som betyder 'ägg'.",
        "skal": "DETTA ÄR forgranska.py:s eget dokumenterade exempelfall: "
                "'oval, popularity_count 9673, märkning [] -- ingen fackterm'. "
                "Kortet hade ändå domänen 'matematik' och en huvudbetydelse "
                "som var SO:s båda definitioner nästan ordagrant. Båda "
                "rättade: domänen borttagen (ordet är ett vanligt vardagsord, "
                "inte en fackterm -- SO/SAOL märker det inte), huvudbetydelsen "
                "omskriven. Synonymerna är SAOL:s egna två ledord.",
    },
    "alltiallo": {
        "hb": "Någon som hjälper till med lite av varje på en arbetsplats",
        "syn": [], "grp": None,
        "ex": f'Anna sköter allt möjligt på kontoret, från kaffe till bokföring -- hon är firmans {hl("alltiallo")}.',
        "reg": "vardaglig, neutral",
        "ety": None,
        "skal": "SO: 'person som utför många skiftande uppgifter', märkt "
                "'vardagligt' -- registret var redan rätt satt, huvudbetydelsen "
                "omskriven för att inte ligga för nära källan. Exemplet var "
                "SO:s eget ORDAGRANT ('han var vaktmästare och alltiallo på "
                "firman') -- bytt. Tom synonymlista: 'faktotum' och "
                "'mångsysslare' står bara i SO:s jfr-lista (syskonord) och "
                "synonymer.se, inte i själva definitionstexten.",
    },
    "väbel": {
        "hb": "En underofficer vars jobb var att hålla ordning bland soldaterna",
        "syn": ["underofficer"], "grp": None,
        "ex": f'{hl("Väbeln")} såg till att soldaterna följde reglementet.',
        "reg": "arkaisk, neutral",
        "ety": "Från tyska Webel/Feldwebel, samma betydelse.",
        "skal": "SO märker ordet 'historiskt', SAOL 'mest i äldre tid' -- "
                "kortets 'formell' saknade helt den tidsmarkeringen. Rättat "
                "till 'arkaisk' (närmast liggande värde i den låsta "
                "registervokabulären -- ingen av vokabulärens termer "
                "innehåller ordstammen 'histor-', ett verkligt vokabulärgap, "
                "se forgranska_tillat-motiveringen). Synonymen är SO:s egen "
                "ledande glosa.",
        "tillat": {"register_motsager_markning":
                   "SO/SAOL märker 'historiskt'/'mest i äldre tid', men den "
                   "låsta registervokabulären (config.REGISTER_FORMALITY) "
                   "har inget värde som delar ordstam med 'historisk' -- "
                   "'arkaisk' (helt ur bruk som levande titel) är närmaste "
                   "sanna beskrivning."},
    },
    "storsint": {
        "hb": "Snäll och frikostig nog att förlåta när någon gjort en illa",
        "syn": ["ädelmodig", "generös"], "grp": None,
        "ex": f'Trots allt hon gått igenom var hon {hl("storsint")} nog att bjuda honom på middag.',
        "reg": "neutral, positiv",
        "ety": None,
        "skal": "Huvudbetydelsen låg nära SAOL:s två glosor plus SO:s klausul "
                "-- omskriven. Exemplet var SO:s eget ORDAGRANT ('brottsoffren "
                "var storsinta nog att acceptera gärningsmannens ursäkt') -- "
                "bytt. Synonymerna är SAOL:s egna två ledord.",
    },
    "struva": {
        "hb": "En kaka som friteras i het olja ; (i Finland) samma sorts kaka, äts kring första maj",
        "syn": [], "grp": None,
        "ex": f'{hl("Struvorna")} serverades varma med kräm och sylt.',
        "reg": "vardaglig, neutral, matlagning",
        "ety": "Fornsvenska struva, av lågtyskans struve 'stel, skrovlig'.",
        "skal": "SAOL ger uttryckligen TVÅ betydelser (allmän svensk och "
                "finlandssvensk, den senare knuten till första maj) -- kortet "
                "hade redan båda, bara nästan ordagrant ur SAOL:s andra "
                "definition. Omskriven för avstånd till källan. Tom "
                "synonymlista: 'klenät' saknar belägg i SO/SAOL:s egen text.",
    },
    "läst": {
        "hb": "En fotformad form som skomakare använder för att göra eller laga skor ; foten på en strumpa",
        "syn": [], "grp": None,
        "ex": f'Skomakaren placerade {hl("lästen")} inuti skon för att behålla formen.',
        "reg": "neutral, neutral",
        "ety": "Fornsvenska läster, besläktat med ordet list, ursprungligen 'spår'.",
        "skal": "VIKTIGT FYND: 'läst' är MINST tre olika homografer i SO/SAOL "
                "-- skoformen, ett gammalt rymdmått/fartygsmått, och verbet "
                "'läsa' (böjningsform). Träfflistan blandar alla tre. Kortets "
                "innehåll (skoformen) är korrekt och hör till den äkta "
                "homografen -- dess egen etymologi nämner uttryckligen "
                "'strumpfot', vilket bekräftar att SO:s andra sens ('fot på "
                "strumpa') hör till SAMMA homograf och är en äkta andra "
                "betydelse, nu tillagd. Rymdmåttet och läsa-betydelserna "
                "hör INTE hit och är uteslutna. Tom synonymlista: "
                "'skoblock' står bara hos synonymer.se.",
    },
    "notarie": {
        "hb": "En juridiskt utbildad tjänsteman, ofta en nyutexaminerad jurist som gör sin tingstjänstgöring",
        "syn": [], "grp": None,
        "ex": f'{hl("Notarien")} attesterade dokumentet vid rätten.',
        "reg": "ngt ålderdomlig, neutral",
        "ety": "Latinets notarius, 'snabbskrivare', till nota 'tecken'.",
        "skal": "SO märker ordet 'något ålderdomligt' -- kortets 'formell' "
                "saknade den markeringen, rättat. SO:s underbetydelse "
                "preciserar att ordet ofta specifikt avser en juris kandidat "
                "som fullgör tingstjänstgöring -- den nyansen (som förklarar "
                "domstolskopplingen bättre än en ren 'vid domstol'-etikett) "
                "är nu inbyggd i huvudbetydelsen. Tom synonymlista: 'jurist' "
                "är inte ledordet i någon SO/SAOL-definition.",
    },
    "skälva": {
        "hb": "Darra och skaka okontrollerat, t.ex. av rädsla eller kyla ; även om saker som skakar, t.ex. ett hus vid en smäll",
        "syn": ["darra", "skaka"], "grp": None,
        "ex": f'Hela kroppen fick henne att {hl("skälva")} av fruktan när hon hörde ljudet i mörkret.',
        "reg": "litterär, neutral",
        "ety": None,
        "skal": "SO:s underbetydelser visar att ordet också används om "
                "ICKE-levande saker som skakar ('huset tycktes skälva när "
                "långtradarna dånade förbi') -- den nyansen saknades och är "
                "tillagd som andra halva av huvudbetydelsen. Synonymerna är "
                "SAOL:s egna två ledord ('darra; skaka'); 'vibrera' "
                "borttagen -- saknar belägg i SO/SAOL:s egen text.",
    },
    "översinnlig": {
        "hb": "Bortom det som går att uppfatta med de fem sinnena ; överjordisk, inte av denna världen",
        "syn": [], "grp": None,
        "ex": f'Många människor söker efter {hl("översinnliga")} erfarenheter genom meditation och andlig praktik.',
        "reg": "litterär, neutral",
        "ety": None,
        "skal": "SO ger TVÅ betydelser ('som inte kan uppfattas med något av "
                "de fem sinnena' OCH, som eget led, 'överjordisk') -- kortet "
                "hade bara den första. Tillagd. Tom synonymlista: varken "
                "'övernaturlig' eller 'andlig' är ledordet i SO:s eller "
                "SAOL:s definitionstext (SO:s andra led ÄR redan 'överjordisk', "
                "nu skrivet direkt i huvudbetydelsen i stället för att "
                "upprepas som synonym).",
    },
    "satyr": {
        "hb": "Bockliknande mansfigur i grekisk mytologi ; (nedsättande) en äldre man med överdrivet stort sexuellt intresse",
        "syn": [], "grp": None,
        "ex": f'Han anklagades för att vara en riktig {hl("satyr")} som ständigt ofredade sina kolleger.',
        "reg": "litterär, neutral ; vardaglig, nedsättande",
        "ety": None,
        "skal": "SO ger en andra, modern bibetydelse: 'någon gång äv. om "
                "(äldre) man med (alltför) stort erotiskt intresse' -- "
                "bekräftad av Wiktionary ('vällusting, liderlig man'). "
                "Tillagd. Exemplet var SO:s eget ORDAGRANT ('en mustig "
                "barockmålning med satyrer och nymfer') -- bytt mot ett som "
                "visar den mer prövningsbara andra betydelsen. Tom "
                "synonymlista: 'faun' står bara i SO:s jfr-lista "
                "(syskonord/cohyponym, inte SYN:synonym) -- faun och satyr "
                "är släkta men inte identiska figurer.",
    },
}


def main():
    data = json.load(open(SESSION, encoding="utf-8"))
    ord_lista = list(KORT.keys())
    n = 0
    for p in data:
        if p["ord"] not in KORT:
            continue
        r = KORT[p["ord"]]
        p["proposed"] = {
            "huvudbetydelse": r["hb"][0].upper() + r["hb"][1:],
            "synonymer": r["syn"],
            "synonym_groups": r.get("grp"),
            "exempelmening": r["ex"],
            "register": r["reg"],
            "etymologi": r.get("ety"),
        }
        p["approved"] = True
        if "tillat" in r:
            p["forgranska_tillat"] = r["tillat"]
        p["sokkoll"] = {"kalla": kalla(p["ord"]), "slutsats": r["skal"]}
        n += 1
    saknas = [o for o in ord_lista if o not in {p["ord"] for p in data}]
    if saknas:
        print("VARNING, hittades inte i sessionsfilen:", saknas)
    json.dump(data, open(SESSION, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Fyllde {n} poster (del 1/4) i {SESSION}.")


if __name__ == "__main__":
    main()
