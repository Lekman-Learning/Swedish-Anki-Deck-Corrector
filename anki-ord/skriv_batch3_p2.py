# -*- coding: utf-8 -*-
"""Skriver proposed+sokkoll for chunk 2 (ord 25-49) av 200-korts v3-batch3."""
import json
import urllib.parse

SOKVAG = "sessions/session_2026-08-20_v3-batch3.json"

def kalla(ord_):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(ord_)

POSTER = {
    "inbringande": dict(
        huvudbetydelse="Som ger bra ekonomisk vinst",
        register="neutral, positiv",
        synonymer=["lönande", "vinstgivande"],
        exempelmening='De startade en <font color="#3498db">inbringande</font> verksamhet som snart gav stor vinst.',
        slutsats="SO/SAOL överens: en betydelse (lönande). SO+ noterar SYN:synonym för 'lönande' -- belagd.",
    ),
    "jetong": dict(
        huvudbetydelse="En myntliknande bricka som används i stället för pengar, till exempel vid spel",
        register="neutral, neutral",
        synonymer=["spelmark", "pollett"],
        exempelmening='Hon satsade en <font color="#3498db">jetong</font> på roulettens nummer 14.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse.",
    ),
    "lathund": dict(
        huvudbetydelse="En lat person ; en kort sammanställning som gör det lätt att komma ihåg eller slå upp något",
        register="vardaglig, negativ ; vardaglig, neutral",
        synonym_groups=[["latmask", "slöfock"], ["handbok", "manual"]],
        exempelmening='Hon tog fram sin <font color="#3498db">lathund</font> för att komma ihåg alla kortkommandon.',
        slutsats="SO/SAOL ger uttryckligen två skilda betydelser (lat person; minneshjälpmedel). Första är nedsättande om person, andra neutral -- olika register per betydelse.",
    ),
    "martyr": dict(
        huvudbetydelse="En person som lider eller dör för sin övertygelse",
        register="neutral, neutral",
        synonymer=["blodsvittne"],
        exempelmening='De tidiga kristna <font color="#3498db">martyrerna</font> vägrade avsäga sig sin tro trots hoten.',
        slutsats="SO/SAOL/Wiktionary överens: en kärnbetydelse. SO:s 'ofta ironiskt'-notering gäller den vardagliga överdrivna användningen ('spela martyr'), inte en egen betydelse.",
    ),
    "mortel": dict(
        huvudbetydelse="Ett kärl som man krossar och maler kryddor eller andra ämnen i med en stöt",
        register="neutral, neutral, matlagning",
        synonymer=[],
        exempelmening='Hon krossade kardemummakärnorna i en <font color="#3498db">mortel</font> innan hon bakade.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse. Inga ordboksbelagda synonymer -- 'mortelstöt' är verktyget i kärlet, inte en synonym för kärlet.",
    ),
    "polyp": dict(
        huvudbetydelse="Ett smådjur i havet som sitter fast och har tentakler ; en utväxt på en slemhinna, t.ex. i näsan",
        register="fackspråklig, neutral, biologi",
        synonym_groups=[[], ["svulst"]],
        exempelmening='Läkaren opererade bort <font color="#3498db">polyperna</font> i pojkens näsa så att han kunde andas bättre.',
        slutsats="SO/SAOL överens: två klart skilda betydelser (nässeldjur-individ; medicinsk utväxt).",
    ),
    "rimma": dict(
        huvudbetydelse="Ha samma slutljud som ett annat ord, eller skriva sådan vers ; stämma överens, passa ihop ; salta in lätt (t.ex. kött eller fisk) för att bevara det",
        register="neutral, neutral",
        synonym_groups=[["bilda rim"], ["stämma överens", "passa"], []],
        exempelmening='Kan du <font color="#3498db">rimma</font> på ordet "själv"?',
        slutsats="SO ger tre genuint skilda betydelser (rim/vers; överensstämma; saltkonservering) -- SAOL bekräftar alla tre ('utgöra rim; bildl. passa; rimsalta'). Ingen ordboksbelagd synonym för saltbetydelsen -- tom grupp.",
    ),
    "scripta": dict(
        huvudbetydelse="En person som sköter praktiska detaljer och för anteckningar under en film- eller tv-inspelning",
        register="fackspråklig, neutral, konst",
        synonymer=["inspelningssekreterare"],
        exempelmening='<font color="#3498db">Scriptan</font> antecknade exakt var varje skådespelare stod i scenen.',
        slutsats="SO/SAOL överens: en betydelse.",
    ),
    "sond": dict(
        huvudbetydelse="Ett tunt, rör- eller stavformat instrument som läkare för in i kroppen för att undersöka eller mäta ; en tunn slang för att mata någon som inte kan äta själv ; en apparat som skickas upp för att mäta högt upp i luften eller i rymden",
        register="fackspråklig, neutral, medicin",
        synonym_groups=[[], [], ["rymdsond"]],
        exempelmening='Läkaren förde in en <font color="#3498db">sond</font> genom näsan för att undersöka magsäcken.',
        slutsats="SO/SAOL ger tre klart skilda betydelser (kirurgiskt instrument; matningsslang; atmosfär/rymdmätare). Alla tre tas med.",
    ),
    "underblåsa": dict(
        huvudbetydelse="Ge dolt stöd åt något, ofta något skadligt, och på så sätt göra det värre",
        register="formell, negativ",
        synonymer=["ge näring åt", "uppmuntra"],
        exempelmening='Grannländerna misstänktes <font color="#3498db">underblåsa</font> konflikten genom vapenleveranser.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse, dolt/indirekt stöd åt något negativt.",
    ),
    "underrätta": dict(
        huvudbetydelse="Informera någon officiellt om något",
        register="formell, neutral",
        synonymer=["informera", "meddela"],
        exempelmening='Polisen <font color="#3498db">underrättade</font> föräldrarna om olyckan samma kväll.',
        slutsats="SO ger två nära besläktade betydelser (informera någon; skaffa sig information/'underrätta sig') -- samma grundhandling sett från två håll, slås ihop.",
    ),
    "usurpera": dict(
        huvudbetydelse="Olagligt eller med våld ta makten eller rätten till något",
        register="formell, negativ",
        synonymer=["bemäktiga sig", "inkräkta"],
        exempelmening='Generalen <font color="#3498db">usurperade</font> makten genom en blodig militärkupp.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse.",
    ),
    "aladåb": dict(
        huvudbetydelse="En kall maträtt med bitar av kött, fisk eller grönsaker i gelé",
        register="neutral, neutral, matlagning",
        synonymer=["aspic", "sylta"],
        exempelmening='Till julbordet serverade de <font color="#3498db">aladåb</font> på grisfötter.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse.",
    ),
    "artificiell": dict(
        huvudbetydelse="Konstgjord, inte äkta eller naturlig",
        register="formell, neutral",
        synonymer=["konstgjord", "syntetisk"],
        exempelmening='Sötningsmedlet i läsken är helt <font color="#3498db">artificiellt</font>, inte utvunnet ur socker.',
        slutsats="SO ger en kärnbetydelse (konstgjord) plus en smalare tillämpning på AI/tänkande ('artificiell intelligens') -- samma grundbetydelse, slås ihop för att undvika konstlad uppdelning.",
    ),
    "artrit": dict(
        huvudbetydelse="En inflammation i lederna",
        register="fackspråklig, neutral, medicin",
        synonymer=["ledinflammation"],
        exempelmening='Hennes <font color="#3498db">artrit</font> gjorde det svårt att böja fingrarna på morgonen.',
        slutsats="SO/SAOL överens: en betydelse.",
    ),
    "avfatta": dict(
        huvudbetydelse="Skriva och formulera något i skrift, till exempel ett officiellt dokument",
        register="formell, neutral",
        synonymer=["formulera", "utforma"],
        exempelmening='Juristen fick i uppdrag att <font color="#3498db">avfatta</font> avtalet på både svenska och engelska.',
        slutsats="SO/SAOL överens: en betydelse.",
    ),
    "avhållen": dict(
        huvudbetydelse="Mycket omtyckt ; en anordning som minskar belastningen när man firar ner något tungt",
        register="neutral, positiv ; fackspråklig, neutral",
        synonym_groups=[["omtyckt", "populär"], []],
        exempelmening='Läraren var mycket <font color="#3498db">avhållen</font> bland eleverna.',
        slutsats="SO/SAOL ger uttryckligen två helt orelaterade betydelser (omtyckt; firningsanordning) -- äkta homonym, inte bara nyanser. Ingen ordboksbelagd synonym för den tekniska betydelsen.",
    ),
    "behjärtad": dict(
        huvudbetydelse="Modig och helhjärtat engagerad, om en insats eller handling",
        register="ngt ålderdomlig, positiv",
        synonymer=["modig", "oförskräckt"],
        exempelmening='Räddningsmannen gjorde en <font color="#3498db">behjärtad</font> insats när han sprang in i det brinnande huset.',
        slutsats="SO/SAOL överens: en betydelse. SAOL markerar 'något ålderdomligt'.",
    ),
    "duplicera": dict(
        huvudbetydelse="Göra en eller flera exakta kopior av något",
        register="neutral, neutral",
        synonymer=["kopiera", "mångfaldiga"],
        exempelmening='Han glömde att <font color="#3498db">duplicera</font> filen innan han redigerade originalet.',
        slutsats="SO/SAOL överens: en betydelse (framställa kopior/dubblera är samma sak sett från två håll).",
    ),
    "griljera": dict(
        huvudbetydelse="Snabbt bryna eller steka något som redan är kokt eller stekt, till exempel i ugn",
        register="fackspråklig, neutral, matlagning",
        synonymer=["bryna", "halstra"],
        exempelmening='Hon <font color="#3498db">griljerade</font> julskinkan i ugnen tills ytan blev gyllenbrun.',
        slutsats="SO/SAOL/Wiktionary överens: en betydelse.",
    ),
    "illuster": dict(
        huvudbetydelse="Mycket berömd och framstående, ofta sagt lite ironiskt",
        register="litterär, ironisk",
        synonymer=["berömd", "framstående"],
        exempelmening='Han hamnade i det mest <font color="#3498db">illustra</font> sällskapet på polisstationens häkte.',
        slutsats="SO/SAOL överens: en betydelse. SO noterar uttryckligen 'ofta ironiskt' -- valör satt till ironisk snarare än neutral/positiv för att fånga den vanliga användningen.",
    ),
    "konvention": dict(
        huvudbetydelse="En oskriven regel som de flesta följer utan att tänka på det ; en formell överenskommelse mellan länder eller andra parter",
        register="neutral, neutral ; formell, neutral, juridik",
        synonym_groups=[["sedvänja", "vedertagen sed"], ["fördrag", "pakt"]],
        exempelmening='Att skaka hand vid en presentation är en <font color="#3498db">konvention</font> i många kulturer.',
        slutsats="SO/SAOL ger två klart skilda betydelser (oskriven social regel; formellt fördrag mellan stater).",
    ),
    "kredit": dict(
        huvudbetydelse="Möjligheten att köpa något och betala senare ; högersidan i en bokföring, motsatsen till debet",
        register="neutral, neutral ; fackspråklig, neutral, ekonomi",
        synonym_groups=[["lån", "betalningsanstånd"], ["tillgodohavande"]],
        exempelmening='De köpte de nya möblerna på <font color="#3498db">kredit</font> och betalade av dem under ett år.',
        slutsats="SO ger tre nyanser, varav de två första (betalningsanstånd; förtroende som ger köpmöjlighet) är samma grundidé -- slås ihop. Den tredje (bokföringsterm, motsats till debet) är genuint skild och behålls separat.",
    ),
    "kulör": dict(
        huvudbetydelse="En färgton eller nyans ; en brun vätska som används för att färga mat och dryck, till exempel öl eller sås",
        register="neutral, neutral ; fackspråklig, neutral, matlagning",
        synonym_groups=[["färgton", "nyans"], []],
        exempelmening='Tyget fanns i flera olika <font color="#3498db">kulörer</font>, från ljusblått till mörkrött.',
        slutsats="SO ger tre nyanser (färgton; hudfärg; färgningsvätska för mat/dryck). Hudfärg-betydelsen är samma grundbegrepp som färgton, slås ihop. Färgningsvätska-betydelsen är en genuint skild, konkret betydelse och behålls separat.",
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
