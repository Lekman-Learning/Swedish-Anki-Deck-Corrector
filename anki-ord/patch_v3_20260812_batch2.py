# -*- coding: utf-8 -*-
"""20 kort ur spår A (is:new, suspenderade legacy-kort) -> full v3.

Syftet med batchen är att fylla på den färdiga is:new-poolen (455 kort när
körningen startade), så att den inte tar slut mitt i en pluggvecka.

Genomgående defekttyper i de här 20, i fallande ordning:

1. **Uppfunna betydelser** (5 kort). `kuriosa` hade "udda faktauppgifter om ett
   ämne", `salongslejon` "saknar djup eller arbetsvilja", `doning` "något rejält
   eller kraftigt konstruerat", `ponera` "tilldela en egenskap eller status",
   `kätting` en **åkattraktion på nöjesfält**. Ingen av dem finns i någon av de
   tre källorna. Alla strukna.

2. **Saknad betydelse** (3 kort). `generös` saknade SO:s "väl tilltagen" (en
   generös portion), `schakt` saknade SAOL:s "hisstrumma" -- alltså det lodräta
   schaktet genom en byggnad, som är den betydelse de flesta möter i en trappuppgång
   -- och `installation` hade tre betydelser på framsidan men en luddig
   "sätta upp eller ordna något på sin plats" på baksidan.

3. **Sakfel** (1 kort). `gässling` hade "en ung fågel av någon art" som andra
   betydelse. Alla tre källorna säger specifikt gåsunge.

4. **Cirkulära eller dubblerade synonymer** (2 kort). `triumfera` hade `triumf`
   (samma ord, annan ordklass), `med bravur` hade `skickligt` två gånger i samma
   lista.

Två kort vilar på bara två källor (`bondånger`, `avbasning` -- wiktionary saknar
posterna), och `förborgad` är varken i SO eller SAOL som eget uppslagsord: bara
som participform av `förborga`, med SAOB som enda ordbok med posten. Det är
grunden för att registret sattes till `ngt ålderdomlig` -- inte en gissning om
stilnivån, utan en direkt följd av var ordet finns och inte finns.
"""
import json
import sys
import urllib.parse

SESSION = "sessions/session_2026-08-12_v3-batch2.json"
SVENSKA = "https://svenska.se/api/msearch?ord={}"

# Frasen har ingen egen ordbokspost -- uppslaget gjordes på grundordet, och
# källan måste peka dit och inte på framsidan.
K = {"med bravur": "bravur"}

# `förborgad` pausas. Förgranskningen larmade frammande_uppslagsord, och en
# kontroll mot rådatan visade att flaggan har rätt: varken SO eller SAOL har
# formen som eget uppslagsord -- båda ger bara verbet `förborga` ("dölja,
# hemlighålla"), och SAOB är enda ordboken med posten. Betydelsen är inte
# problemet (alla källor pekar åt samma håll), utan att registret då vilar på
# min slutledning om att ordet är ålderdomligt i stället för på en märkning.
# Ett kort vars stilnivå ingen ordbok uttalar sig om hör inte hemma i full v3.
PAUSAS = {"förborgad"}

KORT = {
    "bondånger": {
        "hb": "skamsen ruelse över något man har gjort",
        "syn": ["samvetskval", "självförebråelse", "dåligt samvete"],
        "ex": 'Dagen efter festen kom <font color="#3498db">bondångern</font> över allt han hade sagt.',
        "reg": "ngt ålderdomlig, negativ",
        "skal": "SAOL: 'skamsen ånger', med märkningen 'ngt åld.' som gav stilnivån. "
                "syn.se ger samvetskval, självförebråelse, ruelse. Wiktionary saknar "
                "posten -- kortet vilar på två källor. Ordet 'ånger' undveks i både "
                "huvudbetydelse och synonymlista eftersom det är efterledet i "
                "uppslagsordet.",
    },
    "kuriosa": {
        "hb": "samling märkvärdiga eller egendomliga saker",
        "syn": ["rariteter", "sällsyntheter", "antikviteter"],
        "ex": 'Hyllorna var fulla av <font color="#3498db">kuriosa</font> från farfars resor.',
        "reg": "neutral, neutral",
        "skal": "SAOL: 'samling märkvärdiga el. egendomliga saker'. Kortets andra "
                "betydelse, 'udda intressanta men oviktiga faktauppgifter om ett ämne', "
                "finns inte i någon av de tre källorna och är struken. Synonymerna "
                "kuriositeter/kuriosum utelämnade -- samma ordstam som uppslagsordet.",
    },
    "pandemi": {
        "hb": "epidemi som sprider sig över mycket stora områden",
        "syn": ["farsot"],
        "ex": 'En <font color="#3498db">pandemi</font> stängde skolor över hela världen.',
        "reg": "neutral, neutral, medicin",
        "skal": "SO: 'epidemi som sprider sig över mycket stora områden'. Kortets två "
                "betydelser var samma sak formulerad två gånger -- sammanslagna. "
                "'epidemi' är överordnad term och inte synonym, därför utelämnad; "
                "SAOL:s 'allomfattande farsot' bär i stället farsot.",
    },
    "salongslejon": {
        "hb": "person som tycker om att synas på eleganta tillställningar",
        "syn": ["dandy", "sprätt", "sprätthök"],
        "ex": 'Han rörde sig som ett <font color="#3498db">salongslejon</font> mellan borden på banketten.',
        "reg": "neutral, neutral",
        "skal": "SO: 'person som tycker om att synas på eleganta tillställningar'. "
                "Kortets andra betydelse, 'glänser i ytliga sammanhang men saknar djup "
                "eller arbetsvilja', saknar stöd i alla tre källorna och är struken. "
                "'societetslejon' utelämnat som synonym -- delar efterled med "
                "uppslagsordet.",
    },
    "armera": {
        "hb": "förstärka material genom att foga in ett mer hållfast ämne ; förse med beväpning",
        "syn": ["förstärka", "beväpna", "bestycka"],
        "ex": 'Betongplattan måste <font color="#3498db">armeras</font> med stålnät för att bära lasten.',
        "reg": "neutral, neutral, teknik ; neutral, neutral, militär",
        "skal": "SO ger två betydelser: 'förse med beväpning' och 'förstärka (material) "
                "genom att foga in mera hållfast ämne'. Ordningen följer framsidans "
                "facit ('förstärka material'), som inte ändras.",
    },
    "avbasning": {
        "hb": "lindrigare kroppslig bestraffning ; skarp tillrättavisning",
        "syn": ["smörj", "prygel", "upptuktelse", "tillrättavisning"],
        "ex": 'Han fick en rejäl <font color="#3498db">avbasning</font> av chefen inför hela avdelningen.',
        "reg": "neutral, negativ ; neutral, negativ",
        "skal": "SO: '(lindrigare) kroppslig bestraffning'; SAOL lägger till 'skarp "
                "tillrättavisning', alltså den muntliga betydelsen. Wiktionary saknar "
                "posten -- två källor. Kortets gamla exempelmening ('för att hon var "
                "för uppmärksam') var både inparentesad och ologisk, och är utbytt.",
    },
    "avvakta": {
        "hb": "tills vidare avstå från att handla i väntan på något",
        "syn": ["invänta", "avbida", "förbida"],
        "ex": 'Vi bör <font color="#3498db">avvakta</font> tills provsvaren kommer.',
        "reg": "neutral, neutral",
        "skal": "SO: 'tills vidare avstå från att handla under inväntande av'. "
                "SO markerar bida, dröja och vänta som JFR:cohyponym, inte synonym -- "
                "de är utelämnade och ersatta med syn.se:s invänta, avbida, förbida.",
    },
    "behagsjuk": {
        "hb": "som på ett överdrivet sätt försöker göra sig tilldragande",
        "syn": ["kokett", "flörtig"],
        "ex": 'Hans <font color="#3498db">behagsjuka</font> leende övertygade ingen i rummet.',
        "reg": "neutral, lätt negativ",
        "skal": "SO: 'som på ett överdrivet sätt försöker göra sig tilldragande'. "
                "Kortets två betydelser var två formuleringar av samma sak. 'kokett' "
                "behålls trots SO:s cohyponym-markering, eftersom SAOL definierar hela "
                "ordet som 'kokett, fåfäng'. Valören följer av 'överdrivet'.",
    },
    "doning": {
        "hb": "anordning eller sak av obestämt slag",
        "syn": ["grunka", "pryl"],
        "ex": 'Vad är det för <font color="#3498db">doning</font> du har satt fast på cykeln?',
        "reg": "vardaglig, neutral",
        "skal": "SAOL: 'anordning; grej; don', med märkningen 'något vardagligt; vard.' "
                "som gav stilnivån. Kortets andra betydelse ('något rejält eller "
                "kraftigt konstruerat') saknar stöd och är struken. 'don' utelämnat "
                "som synonym -- det är ordstammen i uppslagsordet.",
    },
    "fackman": {
        "hb": "person med en specialists kompetens på ett visst område",
        "syn": ["specialist"],
        "ex": 'Låt en <font color="#3498db">fackman</font> dra om elen i badrummet.',
        "reg": "neutral, neutral",
        "skal": "SO: 'person med en specialists kompetens på ett visst område', med "
                "specialist märkt SYN:synonym. Kortets 'expert' och 'yrkesutövare' "
                "saknar stöd i källorna och är strukna. Kortets två betydelser var "
                "samma sak.",
    },
    "förborgad": {
        "hb": "dold och okänd",
        "syn": ["undangömd", "latent"],
        "ex": 'Motivet förblev <font color="#3498db">förborgat</font> för utredarna.',
        "reg": "ngt ålderdomlig, neutral",
        "skal": "Varken SO eller SAOL har 'förborgad' som eget uppslagsord -- båda "
                "filtrerar till participformen av verbet 'förborga', och SAOB är enda "
                "ordboken med posten. Det är grunden för 'ngt ålderdomlig'. Betydelsen "
                "kommer från syn.se (dold, hemlig, undangömd, latent) och wiktionary "
                "('fördold och okänd'). Kortets 'Skjuten från uppmärksamhet' var inte "
                "idiomatisk svenska.",
    },
    "generös": {
        "hb": "som gärna delar med sig ; väl tilltagen ; välvillig och tolerant",
        "syn": ["frikostig", "givmild"],
        "ex": 'Hon var <font color="#3498db">generös</font> med både sin tid och sina pengar.',
        "reg": "neutral, positiv ; neutral, positiv ; neutral, positiv",
        "skal": "SO ger tre betydelser: 'som gärna delar med sig', underbetydelserna "
                "'väl tilltagen' och 'välvillig, tolerant'. Kortet saknade helt "
                "'väl tilltagen' -- alltså en generös portion, som inte handlar om en "
                "persons läggning alls. frikostig och givmild är båda märkta "
                "SYN:synonym i SO.",
    },
    "gässling": {
        "hb": "unge av gås",
        "syn": ["gåsunge"],
        "ex": 'En kull <font color="#3498db">gässlingar</font> följde gåsen ner till dammen.',
        "reg": "neutral, neutral, biologi",
        "skal": "SO och SAOL säger båda exakt 'gåsunge', wiktionary 'unge till gås'. "
                "Kortets andra betydelse, 'en ung fågel av någon art', är ett sakfel -- "
                "ordet är artspecifikt och alla tre källorna säger gås.",
    },
    "installation": {
        "hb": "högtidlig insättning i ämbete ; anslutning till ledningsnät ; konstverk där rummets egen plats medvetet ingår som uttrycksmedel",
        "syn": ["insättning i ämbete", "anslutning", "inmontering"],
        "ex": 'Utställningens största <font color="#3498db">installation</font> fyllde hela rummet.',
        "reg": "neutral, neutral ; neutral, neutral, teknik ; neutral, neutral, konst",
        "skal": "SO ger tre betydelser och framsidans facit räknar upp alla tre, men "
                "baksidan hade en luddig 'sätta upp eller ordna något på sin plats' i "
                "stället för anslutningsbetydelsen. Alla tre är nu utskrivna i SO:s "
                "ordning.",
    },
    "kätting": {
        "hb": "grövre kedja avsedd att bära tyngre laster",
        "syn": ["boja", "förtöjning"],
        "ex": 'Lasten säkrades med en <font color="#3498db">kätting</font> av härdat stål.',
        "reg": "neutral, neutral, teknik",
        "skal": "SO: 'grövre kedja som är avsedd att bära tyngre laster'. Kortets tredje "
                "betydelse -- 'en åkattraktion på nöjesfält där man sitter i en gunga' -- "
                "finns inte i någon källa och är struken. Kortets två första betydelser "
                "var samma sak. SAOL:s 'varp till väv' är en vävteknisk specialbetydelse "
                "som inte förs in här, eftersom SO inte har den.",
    },
    "med bravur": {
        "hb": "med stor och påfallande skicklighet",
        "syn": [],
        "ex": 'Hon klarade den svåra uppgiften <font color="#3498db">med bravur</font>.',
        "reg": "neutral, positiv",
        "skal": "Uppslaget gäller substantivet 'bravur' -- frasen har ingen egen "
                "ordbokspost. SO: 'stor och påfallande skicklighet' (SYN: virtuositet); "
                "SAOL: 'överlägsen teknisk skicklighet'. Synonymlistan lämnas tom: "
                "källornas synonym är ett substantiv och passar inte en adverbiell fras. "
                "Kortets gamla lista hade dessutom 'skickligt' två gånger.",
    },
    "nepotism": {
        "hb": "orättvist gynnande av släktingar eller vänner",
        "syn": ["svågerpolitik", "vänskapskorruption", "gunstlingssystem"],
        "ex": 'Att chefen anställde sin egen svåger var ren <font color="#3498db">nepotism</font>.',
        "reg": "neutral, negativ, politik",
        "skal": "SO: 'orättvist gynnande av släktingar eller vänner', med svågerpolitik "
                "märkt SYN:synonym. Kortets två betydelser var samma sak. 'kamaraderi' "
                "utelämnat -- SO markerar det som cohyponym, inte synonym.",
    },
    "ponera": {
        "hb": "förutsätta något som ett faktum",
        "syn": ["förutsätta", "tänka sig", "antaga"],
        "ex": 'Vi kan <font color="#3498db">ponera</font> att priset fördubblas och räkna om kalkylen.',
        "reg": "neutral, neutral",
        "skal": "SO: 'förutsätta som ett faktum'; SAOL: 'anta, förutsätta, tänka sig'. "
                "Kortets andra betydelse, 'tilldela en viss egenskap eller status till "
                "något', saknar stöd och är struken. Exempelmeningens omslutande "
                "parentes borttagen.",
    },
    "schakt": {
        "hb": "fördjupning i marken med mer eller mindre lodräta väggar ; lodrät trumma genom en byggnad, till exempel för hiss",
        "syn": ["gruvhål", "brunn", "trumma"],
        "ex": 'Grävmaskinen öppnade ett djupt <font color="#3498db">schakt</font> för vattenledningen.',
        "reg": "neutral, neutral, teknik ; neutral, neutral, teknik",
        "skal": "SO: 'fördjupning (i marken) med mer eller mindre lodräta väggar'. "
                "SAOL lägger till 'hisstrumma' -- den betydelsen saknades helt på "
                "kortet, trots att det är den de flesta möter i en trappuppgång. "
                "Märkningen 'mest i tekniska sammanhang' gav domänen. Exempelmeningens "
                "omslutande parentes borttagen.",
    },
    "triumfera": {
        "hb": "vinna stor framgång ; jubla segerstolt efter en framgång",
        "syn": ["segra", "jubla"],
        "ex": 'Efter tre förlorade set lyckades hon ändå <font color="#3498db">triumfera</font>.',
        "reg": "neutral, positiv ; neutral, neutral",
        "skal": "SO: 'vinna (stor framgång)' med underbetydelsen 'jubla (segerstolt) "
                "efter att ha vunnit framgång' -- två skilda betydelser, den ena om "
                "utfallet och den andra om beteendet efteråt. Kortets synonym 'triumf' "
                "struken: samma ord i annan ordklass.",
    },
}


def main():
    data = json.load(open(SESSION, encoding="utf-8"))
    poster = data["poster"] if isinstance(data, dict) else data

    kvar = [p for p in poster if p["ord"] not in PAUSAS]
    pausade = [p["ord"] for p in poster if p["ord"] in PAUSAS]

    saknar = [p["ord"] for p in kvar if p["ord"] not in KORT]
    if saknar:
        sys.exit(f"saknar rättelse för: {', '.join(saknar)}")

    for p in kvar:
        o = p["ord"]
        r = KORT[o]
        p["proposed"] = {
            # Versal begynnelsebokstav är husstilen i decket -- kontrollerad mot
            # redan godkända full v3-kort. Görs centralt så den inte kan glömmas
            # på ett enstaka kort och ge en osynlig stilavvikelse.
            "huvudbetydelse": r["hb"][0].upper() + r["hb"][1:],
            "synonymer": r["syn"],
            # Platt lista, inga grupper: synonym_groups valideras bara om det är
            # sanningsvärt, och grupper skulle här bara kunna hamna i otakt med
            # betydelserna utan att tillföra något.
            "synonym_groups": None,
            "exempelmening": r["ex"],
            "register": r["reg"],
            "etymologi": None,
        }
        p["approved"] = True
        p["sokkoll"] = {
            "kalla": SVENSKA.format(urllib.parse.quote(K.get(o, o))),
            "slutsats": r["skal"],
        }
        p.pop("applicerad", None)

    if isinstance(data, dict):
        data["poster"] = kvar
        ut = data
    else:
        ut = kvar
    json.dump(ut, open(SESSION, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"fyllde {len(kvar)} poster.")
    if pausade:
        print(f"UTESLUTNA (pausas separat): {', '.join(pausade)}")


if __name__ == "__main__":
    main()
