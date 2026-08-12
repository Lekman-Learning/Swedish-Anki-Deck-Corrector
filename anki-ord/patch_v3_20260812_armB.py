# -*- coding: utf-8 -*-
"""ARM B -- 20 kort UTAN sökkoll (suspenderade is:review, ingen sökverifiering).

Andra halvan av Adams experiment 2026-08-12. Samma frö (20260812), samma
slumpurval, samma behandling — enda skillnaden mot arm A är att dessa kort
aldrig fått en sökkoll. Skilda sessionsfiler hela vägen.

Population: 1 711 (`is:review is:suspended` utan
`flerbetydelse_sokverifierad`, `v3_pausad` eller `v3_underkand`).

## Mekaniska förhandssignalen höll

Riskflaggorna, räknade FÖRE någon läsning: **8 av 20 med hög flagga i arm B
mot 3 av 20 i arm A.** Alla åtta är `dold_betydelse`, alltså precis den lucka
en sökkoll stänger — och det stämmer med vad läsningen sedan visade.

## Vad som faktiskt skiljde

Korten är inte sämre skrivna än arm A. De är v2, de har register, de har
exempelmeningar. Skillnaden ligger i **täckningen mot källan**:

* **`valla`** — kortet hade två betydelser. SO och SAOL har tillsammans sex,
  bland dem "föra omkring (en misstänkt) under bevakning" — den betydelse ordet
  faktiskt möter en svensk i nyhetstexter ("fången vallades på brottsplatsen").
* **`tredskas`** — saknade den juridiska betydelsen "vägra inställa sig inför
  domstol". Det är den som ger *tredskodom*, ordets vanligaste avkomma.
* **`arabesk`**, **`drabbning`**, **`letargi`**, **`pulpet`** — en betydelse var
  som står i SO och inte på kortet.

## Ett rent sakfel och ett grammatikfel

* **`pastörisera`** hade synonymen *sterilisera*. Det är fel på det sätt som
  betyder något: sterilisering dödar allt, pastörisering reducerar bara de
  sjukdomsalstrande bakterierna — därför håller pastöriserad mjölk i veckor
  och inte i år. *Värma* och *behandla* är dessutom så vida att de inte säger
  något alls. Listan är tömd; det finns ingen svensk synonym som inte är en av
  steriliseringsorden.
* **`lucker`** hade exempelmeningen "ur den lucker jorden" — obestämd form i
  bestämd ställning. Rättat till *luckra*.

## Register som inte stämde med orden

`destillera` stod som *vardaglig* (det är en kemisk fackterm), `drabbning`,
`kosa`, `mak` och `marschall` som *litterär* eller *formell* utan stöd, och
`löpsedel` som *vardaglig*. Registret verkar ha satts på känsla snarare än på
märkning — vilket är väntat, eftersom ingen slog upp orden.

## Två hårda flaggor som står kvar med avsikt

`pulpet` får `register_motsager_markning` för märkningen *finl.* SO märker
ordet "vid beskrivning av äldre (och finlandssvenska) förhållanden" — två
saker på en gång, och registerformatet rymmer en stilnivå per betydelse.
Ålderdomligheten är den del som betyder något för Adam; finlandssvenskan står
kvar i sökkollens slutsats i stället.

`valla` får `frammande_uppslagsord` för *valla igen* och *valla in*. Det är
partikelverbsavledningar av valla självt, inte främmande ord — men filtret kan
bara jämföra ortografi, och de två strängarna är inte identiska med `valla`.
"""

import json
import sys
import urllib.parse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FARG = "#3498db"
SVENSKA = "https://svenska.se/api/msearch?ord={}"
SESSION = "sessions/session_2026-08-12_armB-osokkollad.json"


def h(o):
    return f'<font color="{FARG}">{o}</font>'


KORT = {
    "destillera": {
        "hb": "Skilja en vätskas beståndsdelar åt genom förångning och "
              "kondensering",
        "reg": "fackspråklig, neutral, kemi",
        "syn": ["rena", "avskilja", "koncentrera"],
        "ex": f"På bryggeriet lärde hon sig att {h('destillera')} sprit.",
        "skal": "SAOL: 'skilja vätskor åt genom uppvärmning och kondensering'. "
                "Kortet hade bara upphettningen — utan kondenseringen är det "
                "kokning, inte destillation. Registret stod som vardagligt.",
    },
    "arabesk": {
        "hb": "Ornament med stiliserade bladrankor ; utsmyckande element i musik",
        "reg": "formell, neutral, konst ; formell, neutral, musik",
        "grupper": [["bladslinga", "växtornament"], ["utsmyckning", "utsirning"]],
        "ex": f"{h('Arabesker')} var populära i Europa under renässansen.",
        "skal": "SO har underbetydelsen '(stycke med) utsmyckande element', och "
                "SAOL skriver 'äv. bildl.' — den musikaliska arabesken saknades. "
                "'Ornament' som synonym ströks: det är det överordnade begreppet, "
                "arabesken är en av många sorter.",
    },
    "brödtext": {
        "hb": "Den löpande huvudtexten i en artikel",
        "reg": "vardaglig, neutral",
        "syn": ["löpande text"],
        "ex": f"Artikelns {h('brödtext')} gav detaljerna mellan rubrik och bild.",
        "skal": "SO 'längre löpande text i artikel', SAOL 'vanlig text i mots. "
                "till bl.a. rubriktext'. Registret rättat till vardagligt, vilket "
                "är SO:s egen märkning — kortet sa formell.",
    },
    "trikå": {
        "hb": "Elastiskt tyg tillverkat genom maskinstickning ; plagg av sådant tyg",
        "reg": "neutral, neutral",
        "grupper": [["jersey", "maskinstickat tyg"], ["stickat plagg"]],
        "ex": f"Tröjan var sydd i mjuk {h('trikå')} som följde kroppen.",
        "skal": "SO ger tyget, SAOL 'maskinstickad produkt, maskinstickat plagg' "
                "— alltså också plagget. Kortets exempelmening löd 'Ribbad trikå.', "
                "två ord utan predikat.",
    },
    "drabbning": {
        "hb": "Fysisk kraftmätning mellan motståndare ; het debatt",
        "reg": "neutral, neutral",
        "syn": ["strid", "batalj", "kraftmätning"],
        "ex": f"De två arméerna möttes i en blodig {h('drabbning')} utanför "
              f"stadsmurarna.",
        "skal": "SO har underbetydelsen 'het debatt' som kortet saknade. "
                "Registret stod som litterärt trots popularitet 7 262 och ingen "
                "märkning alls.",
    },
    "orgie": {
        "hb": "Vild fest med ohämmade utsvävningar",
        "reg": "neutral, negativ",
        "syn": ["utsvävning", "excess", "frosseri"],
        "ex": f"{h('Orgierna')} i antikens Rom var kända för sin lösaktighet.",
        "skal": "SO 'ohämmade utsvävningar', SAOL 'ohämmad njutning'. "
                "Synonymlistan hade bara 'frosseri', som täcker maten men inte "
                "resten; utsvävning och excess står båda i synonymer.se.",
    },
    "nagla": {
        "hb": "Fästa hårt med spik eller nit",
        "reg": "neutral, neutral",
        "syn": ["spika", "nita"],
        "ex": f"Han {h('naglade')} fast plankorna för att bygga staketet.",
        "skal": "SO 'fästa hårt', Wiktionary 'fästa med nitar eller spikar'. "
                "'Fästa' ensamt ströks som för vitt — man kan fästa med tejp. "
                "Registret stod som vardagligt utan märkning i någon källa.",
    },
    "tredskas": {
        "hb": "Vara motsträvig och streta emot ; vägra inställa sig inför domstol",
        "reg": "ngt ålderdomlig, neutral ; formell, neutral, juridik",
        "syn": ["trilskas", "spjärna emot", "envisas"],
        "ex": f"Barnet {h('tredskades')} och vägrade äta upp gröten.",
        "skal": "SO har underbetydelsen 'vägra att inställa sig inför domstol på "
                "anbefalld tidpunkt' — det är den betydelsen som ger TREDSKODOM, "
                "och den saknades helt. Märkningen 'ngt åld.' saknades i registret.",
    },
    "valla": {
        "hb": "Driva boskap på bete ; föra omkring någon under bevakning ; "
              "stryka glidmedel på skidor ; själva glidmedlet",
        "reg": "neutral, neutral",
        "syn": ["driva", "vakta", "glidmedel"],
        "ex": f"Herden {h('vallade')} sin hjord över de gröna kullarna varje "
              f"morgon.",
        "skal": "Kortet hade två betydelser; SO och SAOL har tillsammans sex. Den "
                "som saknades mest är 'föra omkring (en misstänkt) under "
                "bevakning' — SAOL:s eget exempel är 'fången vallades på "
                "brottsplatsen'. Substantivet (glidmedlet) fanns bara inbakat i en "
                "synonym. 'Skidvalla' duger inte som synonym, den innehåller "
                "uppslagsordet.",
    },
    "mak": {
        "hb": "Långsam, lugn förflyttning",
        "reg": "litterär, neutral",
        "syn": ["utan brådska"],
        "ex": f"Processionen skred framåt i sakta {h('mak')} genom de trånga "
              f"gatorna.",
        "skal": "SO '(långsam) förflyttning'. SAOL har inget annat än frasen 'i "
                "sakta mak', vilket är hela ordets liv i modern svenska. "
                "'Förflyttning' och 'rörelse' ströks som synonymer — de är "
                "definitionen respektive ett vidare begrepp, inte utbytbara ord.",
    },
    "kosa": {
        "hb": "Riktning eller färd man styr mot",
        "reg": "litterär, neutral",
        "syn": ["kurs", "färdväg", "led"],
        "ex": f"Efter en lång dag på jobbet styrde hon äntligen sin {h('kosa')} "
              f"hemåt.",
        "skal": "SO 'färd', SAOL 'riktning, kurs' med exemplet 'styra, ställa "
                "kosan ngnstans'. Kortets huvudbetydelse löd 'Riktning man styr "
                "eller ger sig av' — meningen saknar sitt objekt och går inte att "
                "läsa högt.",
    },
    "letargi": {
        "hb": "Sjukligt, sömnliknande slöhetstillstånd ; djup håglöshet",
        "reg": "formell, neutral, medicin",
        "syn": ["dvala", "håglöshet", "apati"],
        "ex": f"Han föll in i en djup {h('letargi')} efter beskedet.",
        "skal": "SO har underbetydelsen 'håglöshet' vid sidan av det sjukliga "
                "tillståndet — den vardagliga användningen. Kortet hade bara den "
                "medicinska.",
    },
    "marschall": {
        "hb": "Festfackla av en skål med brännbara ämnen",
        "reg": "neutral, neutral",
        "syn": ["festfackla", "bloss"],
        "ex": f"Vad är en kräftskiva utan {h('marschaller')}?",
        "skal": "SO 'festfackla som består av en skål med brännbara ämnen'. "
                "'Fackla' ströks som överordnat begrepp — en fackla behöver "
                "varken skål eller fest. Registret stod som formellt.",
    },
    "pulpet": {
        "hb": "Skrivmöbel med lutande skiva ; skolbänk av äldre typ",
        "reg": "ngt ålderdomlig, neutral",
        "grupper": [["skrivställ"], ["skolbänk"]],
        "ex": f"Hovmästaren stod vid sin {h('pulpet')} i entrén.",
        "skal": "SO har underbetydelsen 'skolbänk' och SAOL har den som egen "
                "betydelse — den saknades. SO märker ordet 'vid beskrivning av "
                "äldre (och finlandssvenska) förhållanden'; märkningen går inte "
                "att uttrycka helt i registerformatet, men ålderdomligheten är "
                "den del som betyder något för Adam.",
    },
    "egalisera": {
        "hb": "Göra jämnt och likformigt",
        "reg": "formell, neutral",
        "syn": ["utjämna", "jämna ut", "släta ut"],
        "ex": f"Kören strävade efter en mjuk och fint {h('egaliserad')} "
              f"tenorstämma.",
        "skal": "SO 'göra jämn eller likformig', SAOL 'göra likformig, utjämna'. "
                "Kortet var i sak riktigt; enda tillägget är 'släta ut' ur "
                "synonymer.se.",
    },
    "löpsedel": {
        "hb": "Affisch som gör reklam för dagens tidning",
        "reg": "neutral, neutral",
        "syn": ["tidningsaffisch"],
        "ex": f"Skandalen syntes på alla kvällstidningarnas {h('löpsedlar')}.",
        "skal": "SO 'affisch som gör reklam för ett tidningsnummer'. Registret "
                "stod som vardagligt utan märkning i någon källa — löpsedel är "
                "fackordet, inte slangen.",
    },
    "harang": {
        "hb": "Yttrande som mest består av fasta fraser utan innehåll",
        "reg": "neutral, lätt negativ",
        "syn": ["svada", "tirad", "ordsvammel"],
        "ex": f"Han drog den vanliga {h('harangen')} om demokrati och "
              f"yttrandefrihet.",
        "skal": "SO: 'yttrande som till stor del utgörs av fasta fraser utan "
                "egentligt innehåll'. Kortets 'långt, innehållslöst tal' missar "
                "att det är just FRASERNA som gör en harang — längden är inte "
                "kriteriet. SAOL 'högtidlig ramsa, ordsvammel'.",
    },
    "pastörisera": {
        "hb": "Hetta upp livsmedel för att oskadliggöra sjukdomsalstrande "
              "bakterier",
        "reg": "neutral, neutral",
        "syn": [],
        "ex": f"All mjölk i butiken är {h('pastöriserad')} innan den förpackas.",
        "skal": "SAKFEL RÄTTAT: synonymen 'sterilisera' är fel på ett sätt som "
                "betyder något — sterilisering dödar ALLA mikroorganismer, "
                "pastörisering oskadliggör bara de sjukdomsalstrande (SO:s egen "
                "formulering). Det är därför pastöriserad mjölk håller veckor och "
                "steriliserad håller år. 'Värma' och 'behandla' är så vida att de "
                "inte säger något. Listan lämnas TOM: varje kandidat i "
                "synonymer.se (göra bakteriefri, sterilbehandla, desinficera) har "
                "samma fel. Exemplet upprepade dessutom definitionen ordagrant.",
    },
    "lucker": {
        "hb": "Löst packad och lätt genomsläpplig, särskilt om jord",
        "reg": "neutral, neutral",
        "syn": ["lös", "porös", "luftig"],
        "ex": f"Ogräset gick lätt att dra upp ur den {h('luckra')} jorden i "
              f"rabatten.",
        "skal": "SO 'löst packad', SAOL 'lös, porös, gles' med exemplet 'lucker "
                "jord'. SO taggar genomsläpplig, luftig och porös som "
                "JFR:cohyponym. GRAMMATIKFEL RÄTTAT: exemplet löd 'den lucker "
                "jorden' — obestämd form i bestämd ställning, ska vara 'luckra'.",
    },
    "bulla upp": {
        "hb": "Duka fram mat i stor och riklig mängd",
        "reg": "vardaglig, neutral",
        "syn": ["bjuda rundhänt", "ställa till kalas"],
        "ex": f"Till kalaset hade mormor {h('bullat upp')} med tårtor, bullar "
              f"och saft.",
        "skal": "SO och SAOL: 'duka fram rikligt'. Kortets synonym 'duka fram "
                "rikligt' var alltså definitionen ordagrant — den lär inte ut "
                "något nytt. Ersatt med synonymer.se:s 'bjuda rundhänt' och "
                "'ställa till kalas'.",
    },
}


def main():
    poster = json.load(open(SESSION, encoding="utf-8"))
    saknar = [p["ord"] for p in poster if p["ord"] not in KORT]
    if saknar:
        sys.exit(f"saknar rättelse för: {', '.join(saknar)}")

    for p in poster:
        o = p["ord"]
        r = KORT[o]
        p["proposed"] = {
            "huvudbetydelse": r["hb"],
            "synonymer": r.get("syn", [s for g in r.get("grupper", []) for s in g]),
            "synonym_groups": r.get("grupper"),
            "exempelmening": r["ex"],
            "register": r["reg"],
            "etymologi": None,
        }
        p["approved"] = True
        p["sokkoll"] = {"kalla": SVENSKA.format(urllib.parse.quote(o)),
                        "slutsats": r["skal"]}
        p.pop("applicerad", None)

    json.dump(poster, open(SESSION, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"fyllde {len(poster)} poster.")


if __name__ == "__main__":
    main()
