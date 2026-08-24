# -*- coding: utf-8 -*-
import json, urllib.parse

PATH = "sessions/session_2026-08-20_v3-batch2.json"
GRANSKARE = "claude-batch11-skrivare"

def kalla_url(ord_text):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(ord_text, safe="")

def hl(phrase):
    return f'<font color="#3498db">{phrase}</font>'

cards = {
"över stock och sten": dict(
    huvudbetydelse="Genom besvärlig, ojämn terräng — ta sig fram oavsett hur marken ser ut",
    register="neutral, neutral",
    synonymer=None,
    synonym_groups=None,
    exempelmening=f'Vandrarna tog sig {hl("över stock och sten")} för att hinna fram till stugan innan mörkret föll.',
    etymologi=None,
    kalla_ord="stock",
    slutsats=("Den exakta frasen gav 0 träffar i SAOL/SO/SAOB (kontrollerat separat). SO:s "
              "artikel för uppslagsordet 'stock' listar däremot frasen ordagrant som exempel "
              "under sub-betydelsen 'över svårframkomlig mark' (jfr 'de gick på en slingrig "
              "skogsstig som bar över stock och sten'). Bekräftat oberoende via extern sökning "
              "(ordlista.se/synonymer.se): betyder att ta sig fram genom besvärlig terräng "
              "oavsett hinder i vägen. Ingen egen SO/SAOL-artikel för själva idiomet, men väl "
              "belagt under grundordet -- samma mönster som tidigare kontaminationsfall löstes "
              "på (sticka av/sticka av mot)."),
),
"komma som lök på laxen": dict(
    huvudbetydelse="Komma som en extra påfrestning ovanpå ett problem som redan finns",
    register="vardaglig, lätt negativ",
    synonymer=None,
    synonym_groups=None,
    exempelmening=f'Bilen gick sönder samma dag han blev av med jobbet — det kom verkligen {hl("som lök på laxen")}.',
    etymologi=None,
    kalla_ord="komma som lök på laxen",
    slutsats=("SO ger frasen ordagrant under uppslagsordet 'lök', definition '(komma) som "
              "försvårande omständighet', exempel 'de var redan försenade, och punkteringen "
              "kom som lök på laxen', märkt 'vardagligt' -- registret satt till vardaglig "
              "därefter (forgranska.py:s register_motsager_markning fångade detta, rättat). "
              "Detta är snävare än legacy-kortets 'något som inte behövs eller är välkommet' "
              "-- den riktiga innebörden är specifikt en YTTERLIGARE motgång ovanpå en redan "
              "dålig situation, inte vilket ovälkommet inslag som helst. Omskrivet för att "
              "matcha SO:s faktiska definition. (forgranska.py:s frammande_uppslagsord-varning "
              "kontrollerad och avfärdad -- kontamination från lök-uppslagets övriga, "
              "orelaterade betydelser (grönsaken, svettfläck, soldatgrupp).)"),
),
"se ut som en fågelholk": dict(
    huvudbetydelse="Se väldigt förvånad och mållös ut, med munnen öppen som av chock",
    register="vardaglig, skämtsam",
    synonymer=None,
    synonym_groups=None,
    exempelmening=f'När hon fick se prislappen på lägenheten {hl("såg hon ut som en fågelholk")}.',
    etymologi="Jämförelse med fågelholkens runda ingångshål, format som en öppen mun.",
    kalla_ord=None,
    kalla_override="https://sv.wiktionary.org/wiki/som_en_f%C3%A5gelholk",
    slutsats=("KONTAMINERING konstaterad: direkt svenska.se-sökning på 'se ut som en fågelholk' "
              "matchade bara det generiska 'se ut'-uppslaget (exempel om bombnedslag, ingen "
              "koppling till fågelholk) -- ingen egen SO/SAOL-artikel för idiomet. Wiktionary "
              "(https://sv.wiktionary.org/wiki/som_en_fågelholk, hämtad med WebFetch denna "
              "session) ger en dedikerad idiomdefinition: '(idiomatiskt) mycket förvånad; "
              "gapande av förvåning'. OLD-facit bekräftar oberoende: 'se frågande ut, se ut "
              "som om man inte förstått ngt' -- samma bild av ett mållöst, gapande "
              "ansiktsuttryck. Legacy-kortets nuvarande innehåll (fågelholk som konkret objekt, "
              "'ha en form som liknar en fågelholk') är helt fel -- ordet är ett rent idiom om "
              "ansiktsuttryck, inte en bokstavlig jämförelse av form."),
),
"envar blir salig på sin tro/fason": dict(
    huvudbetydelse="Var och en blir lycklig på sitt eget sätt — utifrån sin egen tro eller sina egna val",
    register="litterär, neutral",
    synonymer=None,
    synonym_groups=None,
    exempelmening=f'Han älskade fotboll och hon teater, men {hl("envar blir salig på sin tro")}.',
    etymologi=None,
    kalla_ord="envar blir salig på sin tro",
    slutsats=("SO ger uttrycket ordagrant under artikeln 'salig' (betydelsen 'mycket lycklig "
              "och upprymd'), och listar BÅDA framsidans varianter som egna exempel: 'envar "
              "blir salig på sin tro' och 'envar blir salig på sin fason'. Bekräftar OLD-facit "
              "ordagrant ('var o en blir lycklig på sitt sätt, med egna val'). Legacy-kortets "
              "två 'betydelser' var samma tanke uttryckt två gånger -- konsoliderat till en."),
),
"koka soppa på en spik": dict(
    huvudbetydelse="Skapa något fullt fungerande av nästan ingenting ; Göra en alldeles för stor sak av något obetydligt",
    register="vardaglig, neutral",
    synonymer=None,
    synonym_groups=[["göra mycket av lite"], ["göra en höna av en fjäder"]],
    exempelmening=f'Med bara lite mjöl och russin lyckades hon {hl("koka soppa på en spik")} och trolla fram en hel kaka.',
    etymologi="Från en folksaga om en luffare som lurade en snål gumma på ingredienser till en soppa.",
    kalla_ord="koka soppa på en spik",
    slutsats=("SO ger frasen ordagrant, definition 'åstadkomma något av (nästan) ingenting', "
              "exempel 'som krönikör är hon van att koka soppa på en spik'. En extern sökning "
              "om uttryckets ursprung (folksagan om en luffare som lurar en snål gumma på "
              "ingredienser genom att låtsas koka soppa på bara en spik) bekräftar ATT "
              "uttrycket även har en andra, negativ användning: 'att uppförstora något som "
              "inte har tillräcklig substans i sig' -- matchar OLD-facits andra rad 'göra en "
              "höna av en fjäder'. Kortet fick därför två betydelser i stället för legacy-"
              "kortets tre snarlika omskrivningar av samma tanke. OBS: 'göra en höna av en "
              "fjäder' är annars ett eget idiom i decket (granskat 2026-08-18) -- här används "
              "det bara som synonym för spik-uttryckets bibetydelse, inte som huvudbetydelse. "
              "forgranska.py:s register_motsager_markning ('historiskt') kontrollerad: den "
              "märkningen hör till 'spik'-uppslagets andra, orelaterade betydelser (ett "
              "historiskt handeldvapen resp. en guldmyntstyp) -- de två 'vardagligt'-"
              "märkningarna i samma träff hör till just den här idiomatiska användningen, så "
              "vardaglig behålls."),
),
"kola vippen": dict(
    huvudbetydelse="Dö",
    register="vardaglig, skämtsam",
    synonymer=None,
    synonym_groups=None,
    exempelmening=f'Farbror Nisse {hl("kolade vippen")} förra vintern, 87 år gammal.',
    etymologi="Av finska kuolla, 'dö'.",
    kalla_ord="kola vippen",
    slutsats=("SO ger 'avlida' med märkningen 'vardagligt', synonymer.se ger 'dö', SO:s egen "
              "etymologi anger finska 'kuolla' ('dö'). Matchar OLD-facit exakt ('dö'). "
              "Legacy-kortets nuvarande innehåll (en tropisk frukt som växer på 'kolaträdet') "
              "är helt fabricerat -- inget stöd i någon källa. Helt omskrivet kort."),
),
"komma upp sig i smöret": dict(
    huvudbetydelse="Bli rik och få det mycket bättre ekonomiskt",
    register="vardaglig, positiv",
    synonymer=None,
    synonym_groups=None,
    exempelmening=f'Efter att företaget börsnoterades {hl("kom han verkligen upp sig i smöret")}.',
    etymologi=None,
    kalla_ord="komma upp sig i smöret",
    slutsats=("SO:s artikel för 'smör' ger sub-betydelsen 'få det ekonomiskt mycket bra' "
              "(fritextträffen var delvis brusig -- flera orelaterade smör-idiom i samma svar "
              "-- men just den definitionen matchar). Wiktionary bekräftar oberoende: 'få det "
              "bättre (vanligtvis ekonomiskt eller karriärsmässigt)'. Matchar OLD-facit exakt "
              "('få gott om pengar, bli framgångsrik'). Legacy-kortets engelska rad ('Achieve "
              "success and prosperity') borttagen och ersatt med korrekt svenska. Ingen synonym "
              "satt -- 'bli rik' testades men varken SO:s SYN-taggning eller definitionstexten "
              "leder med det ordet (forgranska.py:s synonym_utan_ordboksbelagg fångade det, "
              "struken enligt regeln -- tom synonymlista är godkänt)."),
),
"ligga i stöpsleven": dict(
    huvudbetydelse="Vara under omprövning eller omarbetning — inte bestämt än",
    register="neutral, neutral",
    synonymer=None,
    synonym_groups=None,
    exempelmening=f'Frågan om en ny skolbyggnad {hl("ligger fortfarande i stöpsleven")}.',
    etymologi="En stöpslev smälter metall — det som ligger i den är fortfarande formbart, inte färdigt.",
    kalla_ord="ligga i stöpsleven",
    slutsats=("SO/Wiktionary: 'vara under omarbetning, råka ut för förändring, omprövning "
              "eller är eller kommer under diskussion'. Extern sökning bekräftar etymologin: "
              "stöpslev = smältslev för bly/tenn, användes bl.a. i folkliga spådomar. "
              "Konsoliderade legacy-kortets två nästan identiska definitioner till en. Ingen "
              "synonym satt -- 'oavgjord' (synonymer.se, redaktionell) testades men saknar "
              "stöd i SO/SAOL:s egen text (forgranska.py:s synonym_utan_ordboksbelagg fångade "
              "det -- regeln kräver SO/SAOL, inte synonymer.se ensamt, struken)."),
),
"sätta någon på pottkanten": dict(
    huvudbetydelse="Försätta någon i en pinsam eller besvärlig situation, ofta utan förvarning",
    register="vardaglig, lätt negativ",
    synonymer=None,
    synonym_groups=None,
    exempelmening=f'Hon hoppade av uppdraget i sista sekunden och {hl("satte hela gruppen på pottkanten")}.',
    etymologi=None,
    kalla_ord="sätta någon på pottkanten",
    slutsats=("SO ger frasen ordagrant, definition 'bringa någon i förlägenhet', exempel om en "
              "ordförandekandidat som hoppar av och sätter föreningen i en besvärlig sits. "
              "Matchar legacy-kortets huvudsakliga innebörd. Konsoliderade legacy-kortets två "
              "nästan identiska definitioner till en."),
),
"titta/se i månen efter något": dict(
    huvudbetydelse="Leta efter något helt förgäves, utan att någonsin hitta det",
    register="neutral, lätt negativ",
    synonymer=None,
    synonym_groups=None,
    exempelmening=f'Om du väntar dig en ursäkt av honom kan du {hl("titta i månen efter den")}.',
    etymologi=None,
    kalla_ord="se i månen efter något",
    slutsats=("Direkt sökning på 'titta i månen efter något' gav bara generiska "
              "'titta'/'se'-uppslag (kontaminering, samma mönster som tidigare flerordsfraser). "
              "Sökning på synonymformen 'se i månen efter något' gav SO:s faktiska "
              "idiomdefinition: 'se förgäves efter något' -- matchar OLD-facit exakt "
              "('se förgäves efter ngt')."),
),
"vända på kuttingen": dict(
    huvudbetydelse="Se på något ur ett helt nytt, motsatt perspektiv",
    register="vardaglig, neutral",
    synonymer=None,
    synonym_groups=None,
    exempelmening=f'Skolan valde att {hl("vända på kuttingen")} och byggde om nästan alla klassrum till grupprum.',
    etymologi="En kutting var en liten tunna — man vände den upp och ner för att se om något fanns kvar.",
    kalla_ord="vända på kuttingen",
    slutsats=("SO ger frasen ordagrant, definition 'anlägga ett motsatt perspektiv', exempel "
              "om en skola som byggde om klassrum till grupprum. Bekräftat av "
              "Wiktionary/synonymer.se ('se på ett nytt sätt') och en extern källa "
              "(Språkrådet/Språktidningen) om etymologin: kutting = liten tunna för "
              "sprit/fisk, vändes upp och ner för att se om något fanns kvar i botten. SO:s "
              "'dialektalt'-märkning kontrollerad: hör till ordet 'kutting' som sådant (en "
              "regional benämning på en liten tunna), inte till idiomets eget bruk -- frasen "
              "används i rikstäckande medier (Språktidningen m.fl.), så vardaglig behålls "
              "snarare än dialektal. Ingen synonym satt -- 'se på ett nytt sätt' testades men "
              "saknar stöd i SO/SAOL:s egen definitionstext (forgranska.py:s "
              "synonym_utan_ordboksbelagg fångade det, struken)."),
),
}

d = json.load(open(PATH, encoding="utf-8"))
seen = set()
for entry in d:
    ord_ = entry["ord"]
    c = cards.get(ord_)
    if c is None:
        raise SystemExit(f"SAKNAS kort for: {ord_!r}")
    seen.add(ord_)
    kalla = c.get("kalla_override") or kalla_url(c["kalla_ord"])
    entry["sokkoll"] = {"kalla": kalla, "slutsats": c["slutsats"]}
    entry["proposed"] = {
        "huvudbetydelse": c["huvudbetydelse"],
        "register": c["register"],
        "exempelmening": c["exempelmening"],
        "synonymer": c["synonymer"],
        "synonym_groups": c["synonym_groups"],
    }
    if c["etymologi"]:
        entry["proposed"]["etymologi"] = c["etymologi"]
    entry["approved"] = True

missing = set(cards) - seen
if missing:
    raise SystemExit(f"Kort i cards-dicten som inte fanns i sessionsfilen: {missing}")

json.dump(d, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("OK, skrev", len(d), "kort")
