# -*- coding: utf-8 -*-
"""Skriver proposed+sokkoll for chunk 1 (ord 0-24) av 200-korts v3-batch3."""
import json

SOKVAG = "sessions/session_2026-08-20_v3-batch3.json"

def kalla(ord_):
    return f"https://svenska.se/api/msearch?ord={ord_}"

POSTER = {
    "disponera": dict(
        huvudbetydelse="Bestämma fritt över något ; planera och lägga upp något i rätt ordning ; göra mer mottaglig för något (t.ex. en sjukdom)",
        register="neutral, neutral",
        synonym_groups=[["förfoga över", "bestämma över"], ["planera", "arrangera"], []],
        exempelmening='Han <font color="#3498db">disponerar</font> fritt över lägenheten medan ägaren är utomlands.',
        slutsats="SO ger fyra släkta betydelser (förfoga/bestämma över; ordna/organisera; göra mottaglig; leda till). Kortet slår ihop de tre mest relevanta -- 'leda till' är för nära 'göra mottaglig' för att vara en egen fjärde betydelse på ett Adam-tal-kort. Ingen ordboksbelagd synonym för mottaglighets-betydelsen (predisponera är samma ord, inte en synonym) -- tom grupp, style_guide tillåter det.",
    ),
    "sättning": dict(
        huvudbetydelse="Vilka instrument ett musikstycke är skrivet för ; att marken sjunker ihop under ett hus ; hur text ordnas och sätts för tryckning",
        register="fackspråklig, neutral, musik",
        synonym_groups=[["instrumentbesättning", "besättning"], ["hopsjunkning", "sänkning"], ["typsättning"]],
        exempelmening='Stycket är skrivet för en ovanlig <font color="#3498db">sättning</font> med bara stråkar och slagverk.',
        slutsats="SO ger tre klart skilda betydelser (musik/besättning, byggnadsteknik/marksjunkning, tryckeri/typsättning). SAOL bekräftar med 'arrangemang; besättning'. Alla tre tas med, register satt för förstabetydelsen (musik).",
    ),
    "akvarell": dict(
        huvudbetydelse="En målning gjord med vattenfärg som inte täcker helt",
        register="neutral, neutral, konst",
        synonym_groups=[["vattenfärgsmålning"]],
        exempelmening='Hon målade en <font color="#3498db">akvarell</font> av havet i mjuka blåtoner.',
        etymologi="Av italienska acquerello, till latinets aqua, ”vatten”.",
        slutsats="SO/SAOL/Wiktionary överens: en betydelse, målning med icke-täckande vattenfärg. Etymologin tas med eftersom den förklarar VARFÖR färgen kallas så (vatten-basen), inte bara trivia.",
    ),
    "arbitrage": dict(
        huvudbetydelse="Att köpa och sälja samma sak på olika marknader för att tjäna på prisskillnaden",
        register="fackspråklig, neutral, ekonomi",
        synonym_groups=[[]],
        exempelmening='Banken tjänade pengar på <font color="#3498db">arbitrage</font> mellan börserna i Tokyo och New York.',
        slutsats="SO/SAOL: en betydelse, handel med valutor/varor för att utnyttja kursskillnader. synonymer.se:s enda kandidat ('valutahandel') är en underkategori, inte en utbytbar synonym -- tom lista, style_guide tillåter det.",
    ),
    "blasfemisk": dict(
        huvudbetydelse="Som hånar eller förolämpar något heligt",
        register="neutral, negativ",
        synonym_groups=[["hädisk"]],
        exempelmening='Hans <font color="#3498db">blasfemiska</font> skämt om helgonet chockade publiken.',
        slutsats="SO taggar 'hädisk' SYN:synonym -- belagd. En huvudbetydelse (SO:s andra nyans 'starkt provocerande' är samma sak försvagat, inte en egen betydelse).",
    ),
    "bong": dict(
        huvudbetydelse="Ett kvitto eller en lapp du löser in mot varor, pengar eller en beställning ; en vattenpipa, särskilt för cannabis (slang)",
        register="neutral, neutral",
        synonym_groups=[["kvitto", "talong"], []],
        exempelmening='Kom ihåg att spara <font color="#3498db">bongen</font> om du vill byta varan.',
        slutsats="SO/SAOL ger kontrollmärke/kvitto-betydelsen. Wiktionary lägger till en genuint skild slangbetydelse (vattenpipa för cannabis) som saknas i SO/SAOL men är verifierad -- tas med som andra betydelse.",
    ),
    "brodd": dict(
        huvudbetydelse="En liten metallpigg under skon som ger fäste på hal is ; ett nyss uppkommet skott av säd eller gräs",
        register="neutral, neutral",
        synonym_groups=[["pigg", "dubb"], ["grodd", "skott"]],
        exempelmening='Han satte <font color="#3498db">broddar</font> under skorna innan promenaden på den isiga vägen.',
        slutsats="SO ger tre nära besläktade betydelser, varav två (nyss uppkommen säd / typ av gräs) är samma grundidé (ett tidigt skott) -- slås ihop till en för att undvika en konstlad tredje betydelse. Pigg/dubb-betydelsen är klart skild och behålls separat.",
    ),
    "bövel": dict(
        huvudbetydelse="Djävulen (används som ett gammaldags kraftuttryck)",
        register="vardaglig, lätt negativ",
        synonym_groups=[["djävul", "satan"]],
        exempelmening='För <font color="#3498db">bövelen</font>, ställ dig i givakt när jag pratar med dig!',
        slutsats="SO/SAOL: en betydelse, djävul, i kraftuttryck. SO/SAOL ger BÅDA 'vardagligt' och 'något ålderdomligt' -- kortet väljer vardaglig eftersom uttrycket fortfarande används, med lätt negativ valör (svordom-karaktär).",
    ),
    "charter": dict(
        huvudbetydelse="En paketresa där flyg, hotell och transport är förbokat och ingår i priset",
        register="neutral, neutral",
        synonym_groups=[["paketresa"]],
        exempelmening='De bokade en <font color="#3498db">charter</font> till Mallorca över sommaren.',
        slutsats="SO/SAOL: charterflyg/uthyrning för turistgrupp -- en betydelse i vardagsspråk. synonymer.se:s Användarbidrag 'paketresa' är den vardagligaste, äkta synonymen.",
    ),
    "dakapo": dict(
        huvudbetydelse="En gång till, från början igen (används ofta om musik)",
        register="neutral, neutral, musik",
        synonym_groups=[["en gång till", "om igen"]],
        exempelmening='Publiken ropade <font color="#3498db">dakapo</font> efter den sista låten på konserten.',
        etymologi="Italienska da capo, bokstavligen ”från huvudet”.",
        slutsats="Ordet saknar egen SO/SAOL-artikel men har full SAOB-täckning plus Wiktionary ('ännu en gång, omtagning') och en tydlig, konsekvent synonymer.se-lista -- tillräckligt belagt trots SAOB-only-status.",
    ),
    "dental": dict(
        huvudbetydelse="Som har med tänderna att göra ; ett språkljud som bildas med tungan mot tänderna (t.ex. d och t)",
        register="fackspråklig, neutral, medicin",
        synonym_groups=[[], ["tandljud"]],
        exempelmening='Tandläkaren rekommenderade ett <font color="#3498db">dentalt</font> implantat efter att tanden gått sönder.',
        slutsats="SO/SAOL ger två klart skilda betydelser: allmän tand-relaterad, och den specifika lingvistiska (tandljud/konsonant som d, t, n). Båda tas med.",
    ),
    "dråp": dict(
        huvudbetydelse="Att döda någon utan att det var planerat i förväg (skiljer sig från mord)",
        register="fackspråklig, neutral, juridik",
        synonym_groups=[[]],
        exempelmening='Mannen dömdes till åtta års fängelse för <font color="#3498db">dråp</font>.',
        slutsats="SO: en betydelse, oöverlagt dödande, jämförs uttryckligen med mord (JFR). synonymer.se:s kandidater (mord, homicidium) är juridiskt SKILDA brott, inte utbytbara -- tom synonymlista, style_guide tillåter det.",
    ),
    "epikuré": dict(
        huvudbetydelse="En person som lever för njutning och goda upplevelser",
        register="litterär, neutral",
        synonym_groups=[["njutningsmänniska", "levnadskonstnär"]],
        exempelmening='Som sann <font color="#3498db">epikuré</font> lät han aldrig en god måltid gå obemärkt förbi.',
        etymologi="Efter den grekiske filosofen Epikuros.",
        slutsats="SO ger två släkta betydelser (njutningsmänniska / anhängare av epikurismen som filosofi) -- slås ihop, eftersom den filosofiska betydelsen är en smalare specialfall av samma grundidé och en egen rad skulle bli ordboksprosa.",
    ),
    "expo": dict(
        huvudbetydelse="En utställning, ofta inom handel eller kultur",
        register="neutral, neutral",
        synonym_groups=[["utställning", "mässa"]],
        exempelmening='Företaget visade sin nya produkt på en <font color="#3498db">expo</font> i Stockholm.',
        slutsats="SO/SAOL: en betydelse, förkortning av exposition/utställning.",
    ),
    "extramural": dict(
        huvudbetydelse="Som sker utanför en institution, till exempel utanför universitetet",
        register="formell, neutral",
        synonym_groups=[[]],
        exempelmening='Kursen erbjöd <font color="#3498db">extramural</font> undervisning, där eleverna fick lära sig genom praktik i samhället.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Inga ordboksbelagda synonymer hittade -- tom lista.",
    ),
    "faktori": dict(
        huvudbetydelse="En handelsstation som ett företag hade i ett annat land förr, med lager för varor",
        register="arkaisk, neutral",
        synonym_groups=[[]],
        exempelmening='Kompaniet byggde ett <font color="#3498db">faktori</font> vid kusten för att lagra kryddorna innan skeppen kom.',
        slutsats="SAOL markerar ordet 'åld.' (arkaisk). Wiktionary bekräftar samma betydelse (fabrikskomplex/filial i koloni). Inga ordboksbelagda synonymer.",
    ),
    "farmaci": dict(
        huvudbetydelse="Vetenskapen om hur läkemedel görs och verkar",
        register="fackspråklig, neutral, medicin",
        synonym_groups=[[]],
        exempelmening='Hon läser <font color="#3498db">farmaci</font> på universitetet för att bli apotekare.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse, läran om läkemedel.",
    ),
    "flexibel": dict(
        huvudbetydelse="Som lätt kan anpassas efter det som behövs",
        register="neutral, neutral",
        synonym_groups=[["anpassningsbar", "smidig"]],
        exempelmening='Han har en <font color="#3498db">flexibel</font> arbetstid och kan jobba hemifrån när han vill.',
        slutsats="SO ger två släkta betydelser (om saker/system, och om personer) -- samma grundidé, slås ihop till en för att undvika konstlad uppdelning.",
    ),
    "gage": dict(
        huvudbetydelse="Lönen en artist får för ett uppträdande",
        register="neutral, neutral, musik",
        synonym_groups=[["arvode", "lön"]],
        exempelmening='Bandet fick ett <font color="#3498db">gage</font> på 15 000 kronor för konserten.',
        slutsats="SO/SAOL överens: en betydelse, ersättning för tillfälligt (artist-)arbete.",
    ),
    "gans": dict(
        huvudbetydelse="Ett smalt, dekorativt band av till exempel guld- eller silvertråd, sytt på möbler eller kläder",
        register="arkaisk, neutral",
        synonym_groups=[["garneringssnöre", "kantband"]],
        exempelmening='Fåtöljens kant var klädd med en fin <font color="#3498db">gans</font> i guldtråd.',
        slutsats="SO/SAOL överens (belagt sedan 1830, sällsynt hantverksord i dagligt bruk -- arkaisk). Wiktionary kunde inte hämtas (HTTP 429), men SO+SAOL+synonymer.se ger full täckning på egen hand.",
    ),
    "genombruten": dict(
        huvudbetydelse="Försedd med hål som tillsammans bildar ett mönster",
        register="fackspråklig, neutral, konst",
        synonym_groups=[["perforerad", "nätmönstrad"]],
        exempelmening='Porslinet hade ett vackert <font color="#3498db">genombrutet</font> mönster längs kanten.',
        slutsats="SO/SAOL överens: en betydelse, om tryck/hantverk med hålmönster.",
    ),
    "grip": dict(
        huvudbetydelse="Ett sagodjur med kropp som ett lejon och huvud och vingar som en örn",
        register="litterär, neutral",
        synonym_groups=[["fabeldjur", "sagodjur"]],
        exempelmening='På vapenskölden syntes en gyllene <font color="#3498db">grip</font> mot blå botten.',
        slutsats="SO:s träff blandar in flera artiklar (bl.a. verbet 'gripa') under samma sökning -- kortet begränsas medvetet till den entydiga, SAOL-bekräftade huvudbetydelsen (heraldiskt fabeldjur) för att undvika att felaktigt lägga till verbbetydelser som hör till ett annat uppslagsord.",
    ),
    "happening": dict(
        huvudbetydelse="Ett oplanerat konstevenemang där publiken ofta är med och skeendet är oväntat",
        register="neutral, neutral, konst",
        synonym_groups=[["spontanföreställning"]],
        exempelmening='Konstnären sågade sönder ett piano mitt under <font color="#3498db">happeningen</font>, till publikens förvåning.',
        slutsats="SO/SAOL överens: en betydelse, teaterliknande improviserad konstform.",
    ),
    "i andanom": dict(
        huvudbetydelse="I sina tankar, för sitt inre öga",
        register="ngt ålderdomlig, neutral",
        synonym_groups=[[]],
        exempelmening='Hon såg <font color="#3498db">i andanom</font> hur huset skulle se ut när det var färdigrenoverat.',
        slutsats="SO ger frasen 'för sitt inre'. SO:s andra träff ('nionde bokstaven') är sökkontaminering -- gäller bokstaven 'i', inte frasen 'i andanom', och utelämnas. SAOL bekräftar 'ursprungligen bibliskt' -- registret satt till ngt ålderdomlig.",
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
        c["sokkoll"] = {
            "kalla": kalla(ord_),
            "slutsats": spec["slutsats"],
        }
        c["proposed"] = {
            "huvudbetydelse": spec["huvudbetydelse"],
            "register": spec["register"],
            "synonymer": None,
            "synonym_groups": spec["synonym_groups"],
            "exempelmening": spec["exempelmening"],
            "etymologi": spec.get("etymologi"),
        }
        c["approved"] = True
    json.dump(data, open(SOKVAG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(POSTER)} kort. Saknades i sessionsfilen: {saknas}")

if __name__ == "__main__":
    main()
