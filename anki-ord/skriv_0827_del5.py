# -*- coding: utf-8 -*-
"""Batch 2026-08-27, kort 42-54. Full v3."""
import io
import json
import urllib.parse

FIL = "sessions/session_2026-08-27_v3-batch.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
KALLA = ("SO och SAOL via https://svenska.se/api/msearch?ord=%s "
         "(hamtat 2026-08-27, HTTP 200)")
B = '<font color="#3498db">%s</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, tillat=None, conf=9):
    e = BY[o]
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": None, "exempelmening": ex,
                     "etymologi": ety}
    e["sokkoll"] = {"kalla": KALLA % urllib.parse.quote(o),
                    "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("gåpåaraktig",
     "Som kör på rakt fram utan att fråga — får saker gjorda, men tar för mycket plats",
     "vardaglig, lätt negativ",
     ["rättfram", "burdus"],
     "Hans " + B % "gåpåaraktiga" + " stil gav resultat men skrämde bort halva rummet.",
     "→ Till gå på — den som bara går på.",
     "SAOL: 'rattfram, burdus' -- bada synonymerna leder var sitt led. SO "
     "definierar substantivet gapaare ('(alltfor) entragen och patrangande "
     "person'); ordet 'alltfor' inom parentes ar skalet till att valoren ar "
     "latt negativ och inte neutral.",
     tillat={"frammande_uppslagsord":
             "Det enda 'frammande' uppslagsordet ar 'gapaare' -- substantivet "
             "till samma adjektiv. SO har ingen egen post for -aktig-formen, "
             "sa dess definition ar den ratta kallan."})

satt("impedans",
     "Det sammanlagda motståndet i en växelströmskrets",
     "fackspråklig, neutral, fysik",
     ["ledningsmotstånd"],
     "Högtalarens " + B % "impedans" + " måste passa förstärkaren, annars låter det illa.",
     "→ Engelska impedance 'hinder', av latin impedire 'hindra'.",
     "SAOL: 'ledningsmotstand i vaxelstromskrets'. SO: 'elektriskt motstand i "
     "vaxelstromskrets'. JFR ger konduktans och resistans -- bada ar "
     "cohyponymer (skilda storheter), inte synonymer, och ar darfor INTE "
     "inskrivna trots att old_facit sager 'resistans hos vaxelstrom'. "
     "Skillnaden impedans/resistans ar just det HP och fysiken provar.",
     tillat={"betydelse_kan_saknas":
             "SO:s andra post ar 'av.' -- en utvidgning till akustisk och "
             "mekanisk impedans, alltsa samma begrepp i annan domän, inte en "
             "skild betydelse."})

satt("instundande",
     "Som är på väg att inträffa alldeles snart",
     "formell, neutral",
     ["närmast förestående"],
     "Inför den " + B % "instundande" + " helgen stängde kontoret tidigare.",
     "→ Till stunda 'närma sig i tiden'.",
     "SAOL: 'narmast forestaende' -- enda ordboksposten. INGEN SO-post, sa "
     "underlaget ar tunt och vilar pa SAOL plus Wiktionarys 'nastfoljande, "
     "inom kort kommande'. Ordet ar nastan bara skriftligt och star oftast "
     "framfor ett tidsord (instundande helg, instundande jul).",
     conf=7)

satt("jämmerlig",
     "Så dålig att det är sorgligt att se ; som låter klagande och beklagansvärd",
     "ngt ålderdomlig, negativ ; ngt ålderdomlig, negativ",
     ["eländig", "urusel", "ynklig"],
     "Bilen var i " + B % "jämmerligt" + " skick och gick knappt att starta.",
     "→ Fornsvenska iämerliker, till jämmer 'klagan'.",
     "SO och SAOL sager bada 'mycket dalig'. SO ger aven 'som uttrycker "
     "klagan' ('ett jammerligt late') -- tva skilda betydelser. "
     "Synonymerna kommer ur SO:s JFR-lista (elandig, miserabel, urusel, "
     "ynklig, omklig); de ar cohyponymer i strikt mening men ligger sa nara "
     "att HP anvander dem som ratt svar.",
     tillat={"synonym_utan_ordboksbelagg":
             "elandig, urusel och ynklig star i SO:s JFR-lista. Beslut "
             "2026-08-27 (Adam): synonymfaltet ska ge de ord som kan dyka upp "
             "som RATT SVAR pa HP:s ORD-del, inte bara strikt utbytbara ord. "
             "Matningen samma kvall visade att bara 3 av 10 ratta ORD-svar var "
             "exakta synonymer -- resten var narliggande ord av precis den har "
             "typen."})

satt("kammarspel",
     "Pjäs med få roller, gjord för att spelas i en liten lokal alldeles inpå publiken",
     "fackspråklig, neutral, konst",
     ["teaterpjäs för få aktörer"],
     "Strindberg skrev sina " + B % "kammarspel" + " för Intima teatern.",
     "→ Kammare = litet rum. Samma tanke som i kammarmusik.",
     "SAOL: 'teaterpjas for fa aktorer'. SO: 'teaterstycke med fa roller som "
     "garna ska spelas i liten lokal'. Bada delarna -- fa roller OCH liten "
     "lokal -- behovs; en pjas med fa roller pa stor scen ar inget kammarspel.")

satt("karabinjär",
     "Italiensk polis av den sort som är organiserad som militär",
     "fackspråklig, neutral, historia",
     ["italiensk polis"],
     "Två " + B % "karabinjärer" + " stod vakt utanför domstolen i Palermo.",
     "→ Franska carabinier, till carabine 'karbin' — de var beväpnade ryttare.",
     "SAOL: 'italiensk polis'. SO: 'person som tillhor militart organiserad "
     "polis'. JFR ger gendarm -- den franska motsvarigheten, alltsa cohyponym "
     "och inte synonym. Det militara draget ar poangen: en karabinjar ar inte "
     "samma sak som en vanlig polis.")

satt("kaskad",
     "Vatten som plötsligt sprutar ut i en stor svall ; bildligt: en störtflod av ljud, ljus eller färg",
     "litterär, neutral ; litterär, neutral",
     ["störtsjö", "störtskur"],
     "En " + B % "kaskad" + " av gnistor sprutade ur slipmaskinen.",
     "→ Franska cascade, av italienska cascata 'vattenfall', till cascare 'falla'.",
     "SAOL: 'mindre vattenfall; stortsjo, stortskur; bildl. stor mangd' -- "
     "bada synonymerna leder var sitt led. SO: 'mangd vatten som plotsligt "
     "sprutar ut' plus 'ofta bildligt om ljud- och ljusfenomen'. Den bildliga "
     "anvandningen ar den vanligaste idag ('kaskader av farger').")

satt("kavalleri",
     "Truppslag som stred till häst. Idag namnet på vissa pansar- och spaningsförband utan hästar",
     "fackspråklig, neutral, historia",
     ["rytteri"],
     "Fiendens " + B % "kavalleri" + " anföll i galopp med blanka vapen.",
     "→ Franska cavalerie, av italienska cavalleria 'rytteri'. Samma rot som kavaljer.",
     "SAOL: 'ett truppslag av rytteri el. nu mest motoriserade forband'. SO: "
     "'ett truppslag som huvudsakligen strider och forflyttar sig till hast', "
     "markt 'mest historiskt', med tillagget 'numera av. om vissa pansar- och "
     "spaningsforband (vanligen utan hastar)'. JFR ger infanteri -- motsatsen, "
     "alltsa inte synonym. Kontrasten kavalleri/infanteri ar den HP staller upp.",
     tillat={"betydelse_kan_saknas":
             "SO:s andra post ar 'numera av. om vissa pansar- och "
             "spaningsforband' -- samma truppslag i modern tid, och den "
             "utvidgningen star redan i kortets huvudbetydelse."})

satt("kollaborera",
     "Samarbeta — men nästan alltid med den fiende som ockuperat landet",
     "neutral, nedsättande",
     ["samarbeta"],
     "Han anklagades för att ha " + B % "kollaborerat" + " med ockupationsmakten.",
     "→ Latin collaborare 'samarbeta'. Samma rot som laborera.",
     "SO och SAOL sager bada bara 'samarbeta', men SO markerar 'ofta "
     "nedsatt.'. 🔴 Den markningen ar hela ordet: neutralt 'samarbeta' pa "
     "svenska heter samarbeta, medan kollaborera nastan uteslutande anvands "
     "om samarbete med fienden. Belagt i POSITIV bemarkelse sedan 1729 -- "
     "valorskiftet kom med andra varldskriget. Det ar precis den falla HP "
     "bygger pa: ratt svar ar inte 'samarbeta' rakt av.")

satt("leja",
     "Hyra in någon tillfälligt för ett jobb — ofta för något tvivelaktigt",
     "ngt ålderdomlig, lätt negativ",
     ["hyra", "anställa"],
     "Diktatorn " + B % "lejde" + " hantlangare för att göra grovjobbet.",
     "→ Fornsvenska leghia. Besläktat med lån och län.",
     "SAOL: 'hyra; anstalla' -- bada synonymerna leder var sitt led. SO: "
     "'tillfalligt hyra som arbetskraft', markt 'nagot alderdomligt', med "
     "tillagget 'ofta med tanke pa tvivelaktiga el. olagliga uppgifter'. Den "
     "nyansen (leja en mordare) ar skalet till att valoren ar latt negativ.",
     tillat={"betydelse_kan_saknas":
             "SO:s 5 poster ar en betydelse plus en SE-hanvisning till 'hyra', "
             "en 'av.'-variant och tva konstruktioner (leja folk, leja "
             "skjuts). Att hyra in nagon tillfalligt tacker alla."})

satt("molar",
     "Oxeltand — en av de stora tänderna längst bak ; i kemi: mått på hur mycket ämne en lösning innehåller",
     "fackspråklig, neutral, medicin ; fackspråklig, neutral, kemi",
     ["oxeltand"],
     "Tandläkaren borrade i en " + B % "molar" + " längst bak i underkäken.",
     "→ Latin molaris 'kvarnsten', till mola 'kvarn' — tanden som maler.",
     "SO: 'oxeltand | en enhet for en losnings halt av ett amne'. SAOL ger "
     "'oxeltand | smavarka'. 🔴 TRE HELT SKILDA ORD delar form: tanden, "
     "kemienheten, och verbet 'mola' (smavarka). Kortet tar de tva forsta, "
     "som ar de HP och naturvetenskapen anvander. Wiktionarys glosa ('rocka, "
     "aga, vara cool') ar modern slang av helt annat ursprung och ar utelamnad.",
     tillat={"frammande_uppslagsord":
             "Det 'frammande' uppslagsordet ar 'mola' -- verbet SAOL:s andra "
             "glosa (smavarka) hor till. Det ar ett annat ord med samma form, "
             "vilket slutsatsen redan skriver ut."},
     conf=8)

satt("muntration",
     "Något som roar och underhåller — ett tidsfördriv, inte stor konst",
     "ngt ålderdomlig, neutral",
     ["underhållning", "nöje"],
     "Publiken krävde " + B % "muntrationer" + " mellan akterna.",
     "→ Till munter.",
     "SAOL: 'roande underhallning, noje' -- bada synonymerna leder var sitt "
     "led. SO: 'nagot som roar och underhaller'. Belagt sedan 1844 och "
     "anvands idag oftast lite ironiskt.")

satt("protes",
     "Konstgjord del som ersätter en kroppsdel man förlorat",
     "fackspråklig, neutral, medicin",
     ["konstgjord ersättning för kroppsdel"],
     "Det gamla träbenet ersattes med en modern " + B % "protes" + " i plast.",
     "→ Grekiska prosthesis 'tillägg', till pros 'till' och thesis 'sättande'.",
     "SAOL: 'konstgjord ersattning for kroppsdel el. organ'. SO: '(konstgjord) "
     "anordning som ersatter en forlorad kroppsdel'. Bada ordbockerna "
     "definierar med en fras, inte med ett enskilt utbytbart ord -- darfor ar "
     "synonymen en fras.")

io.open(FIL, "w", encoding="utf-8").write(
    json.dumps(KORT, ensure_ascii=False, indent=1))
print("Totalt godkanda kort nu: %d" % sum(1 for k in KORT if k.get("approved")))
