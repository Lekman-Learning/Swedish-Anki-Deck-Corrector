"""Batch 8 — de sista 21 korten. Därmed är alla 130 sökkollade.

Fyra av dem visade samma mönster som återkommit hela dagen: **den upplysning som
gör ordet lätt att minnas stod i källan och saknades på kortet.** huldras farliga
lockelse, frottés uppsugningsförmåga, bruttos motsats netto, bödelns skarprättare.
Ett kort kan vara korrekt och ändå inte lära ut något — det var lärdomen från
`trolsk` i morse, och den håller.
"""
import json
import os
import urllib.parse

MAL = "sessions/session_2026-08-09_v3-so-batch8.json"
KALLOR = ["sessions/session_2026-08-09_v3-omgranskning-nya.json",
          "sessions/session_2026-08-09_v3-dagens-ko.json",
          "sessions/session_2026-08-09_v3-dagens-ko2.json",
          "sessions/session_2026-08-09_v3-inlarning.json"]
SAOB = "https://www.saob.se/artikel/?seek={}"
P = {}


def _api(o):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(o)


def lagg(ord_, slutsats, kalla=None, **andr):
    P[ord_] = (kalla or _api(ord_), slutsats, andr)


lagg("huldra",
     "DET SOM GÖR HULDRAN FARLIG SAKNADES. Kortet sa bara 'kvinnligt skogsväsen i "
     "nordisk folktro'. SO: 'mytologiskt kvinnligt (skogs)väsen med förmåga att "
     "utöva **farlig lockelse**' — förförelsen är hela poängen med väsendet, och "
     "OLD-facit sa det också ('förförisk skogskvinna'). SAOL ger 'skogsfru, "
     "skogsrå', JFR skogsrå i SO.",
     huvudbetydelse="Kvinnligt skogsväsen i nordisk folktro som lockar män i "
                    "fördärvet",
     synonymer=["skogsrå", "skogsfru"])

lagg("frotté",
     "ORDETS POÄNG SAKNADES. Kortet sa 'mjukt, öglat bomullstyg'. SAOL förklarar "
     "VARFÖR öglorna finns: 'tyg med små öglor vilket ger **god "
     "uppsugningsförmåga**'. Det är därför handdukar är av frotté. SO: 'poröst "
     "bomullstyg med öglelugg'. Kortets 'handduksväv' finns i ingen källa men "
     "beskriver rätt sak; den ersätts av den belagda termen öglelugg.",
     huvudbetydelse="Poröst bomullstyg med små öglor som suger upp vatten bra",
     synonymer=["öglelugg", "handduksfrotté"])

lagg("brutto",
     "MOTSATSEN OCH EN BETYDELSE SAKNADES. Båda källorna ger JFR **netto** — den "
     "enklaste minnesregeln för ordet, och den stod inte på kortet. SAOL ger "
     "dessutom viktbetydelsen: 'med **förpackning medräknad**' (paketet vägde 5 kg "
     "brutto). Kortet hade bara pengabetydelsen. SO skiljer också på adverbet "
     "('före vederbörliga avdrag') och substantivet ('behållning före avdrag').",
     huvudbetydelse="Före avdrag, motsatsen till netto ; om vikt: med förpackningen "
                    "inräknad",
     synonymer=["totalt", "före avdrag"])

lagg("bödel",
     "RÄTT SYNONYM SAKNADES OCH EN BETYDELSE MED. SO ger JFR **skarprättare** — det "
     "svenska fackordet — medan kortets 'avrättningsman' finns i ingen källa. SO ger "
     "också en bildlig betydelse kortet saknade: '**makthavare som kränker "
     "elementära mänskliga rättigheter**'. SAOL bekräftar båda ('mest i äldre tid ...; "
     "äv. bildl.').",
     huvudbetydelse="Person som yrkesmässigt verkställer dödsdomar ; bildligt om en "
                    "makthavare som grovt kränker mänskliga rättigheter",
     synonymer=["skarprättare"])

lagg("exkludera",
     "TVÅ BETYDELSER OCH EN MOTSATS. SO skiljer '**tvångsmässigt avlägsna**' (han "
     "exkluderades ur partiet) från 'inte ta med' — att uteslutas ur en förening och "
     "att utelämnas ur en lista är olika saker. SO ger också JFR **inkludera**, "
     "motsatsen, som är den bästa minnesregeln. Kortets 'bortse från' finns i ingen "
     "källa.",
     huvudbetydelse="Utesluta någon ur en gemenskap ; inte ta med något — motsatsen "
                    "till inkludera",
     synonymer=["utesluta", "utestänga"])

lagg("mikrofiche",
     "SYNONYMEN VAR FEL SAK. Kortet hade 'mikrofilm'. SO ger JFR **mikrokort** och "
     "definitionen '(genomskinligt) **kort** med mycket stor mängd information i form "
     "av kraftigt förminskade tecken'. SAOL: 'stycke genomskinlig film'. En "
     "mikrofiche är alltså ett ARK, en mikrofilm är en rulle — det är just den "
     "förväxlingen ett prov skulle fråga om.",
     huvudbetydelse="Genomskinligt kort med kraftigt förminskad text — ett ark, inte "
                    "en rulle",
     synonymer=["mikrokort"])

lagg("katakomb",
     "CIRKULARITET LÖST MED KÄLLANS EGEN DETALJ. Kortet definierade ordet som "
     "'underjordisk gravgång' och gav 'gravgång' som synonym. SO ger det som saknades: "
     "'underjordisk begravningsplats som består av långa gångar med **uthuggna "
     "gravkammare i väggarna**'. Det är detaljen som gör bilden tydlig. Exempel i "
     "båda källorna: katakomberna i Rom.",
     huvudbetydelse="Underjordisk begravningsplats med långa gångar och gravkammare "
                    "uthuggna i väggarna",
     synonymer=["gravvalv"])

lagg("imperium",
     "BILDLIGA BRUKET SAKNADES. SAOL noterar '**ofta bildl.**' med exemplet "
     "'industriimperium' — ett medieimperium har inga underkuvade stater. SO ger den "
     "bokstavliga: '(geografiskt vidsträckt) stormaktsvälde med ett antal "
     "**underkuvade** stater', JFR välde. Underkuvandet är det som skiljer ett "
     "imperium från ett stort land.",
     huvudbetydelse="Stormaktsvälde som härskar över underkuvade stater ; bildligt om "
                    "ett stort företagsvälde",
     synonymer=["välde", "rike"])

lagg("vidlyftig",
     "VÄRDERINGEN SAKNADES. Kortet sa 'mycket bred och utdragen' — neutralt. Båda "
     "källorna har **alltför**: SAOL '**alltför** omfattande; utsvävande', SO "
     "'(alltför) omfattande'. Ordet är alltså kritiskt, inte beskrivande. SO:s "
     "exempel visar spännvidden: vidlyftiga affärer, vidlyftiga spekulationer, "
     "vidlyftiga gester, en vidlyftig monografi.",
     huvudbetydelse="Alltför omfattande och utdragen ; om levnadssätt: utsvävande",
     synonymer=["omfångsrik", "utsvävande"])

lagg("cypress",
     "KÄLLAN GER EN BILD KORTET SAKNADE. Kortet sa 'smalt, koniskt barrträd' — inget "
     "av de orden står i källorna. SO: 'ständigt grönt träd med **platta, fjällika "
     "barr och klotrunda kottar**', och exemplet 'karaktärsträd i Medelhavsländerna, "
     "ofta planterad på **kyrkogårdar**'. Medelhavet och kyrkogården är det som gör "
     "ordet minnesvärt.",
     huvudbetydelse="Ständigt grönt träd med fjällika barr, typiskt för Medelhavets "
                    "kyrkogårdar")

lagg("rutt",
     "PRECISERAD. SO: '**fastlagd** färdväg' — en rutt är planerad, inte vilken väg "
     "som helst man råkar ta. Kortet sa 'väg eller bana man färdas'. SAOL: 'resväg'. "
     "SO:s exempel visar bruket: staka ut en rutt, trafikera en rutt.",
     huvudbetydelse="Fastlagd färdväg som man planerat att följa",
     synonymer=["färdväg", "resväg"])

lagg("dispasch",
     "SYNONYMEN BYTT MOT KÄLLANS ORD. SAOL och SO ger båda exakt ett ord: "
     "'**haveriutredning**' — vilket också är OLD-facits glosa. Kortets "
     "'sjöskadeutredning' finns i ingen källa. Kortets längre förklaring "
     "(kostnadsfördelning efter sjöskada) är riktig och behålls, men synonymen ska "
     "vara den belagda.",
     synonymer=["haveriutredning"])

lagg("monstruös",
     "ANDRA BETYDELSEN PRECISERAD. Kortet sa 'mycket stor'. SO säger "
     "'**orimlig**' — en monstruös summa är oförsvarlig, inte bara stor. SAOL "
     "bekräftar kortets synonymer: 'vidunderlig; oformlig; ohygglig'.",
     huvudbetydelse="Oformlig och skrämmande ; om något omfattande: orimlig")

lagg("goodwill",
     "BEKRÄFTAT, MED EN NOTERING. SAOL: 'gott anseende som t.ex. företag åtnjuter'. "
     "SO: 'gott rykte eller anseende', JFR **badwill** — motsatsen, som är en bra "
     "minnesregel. Kortets andra betydelse (det bokföringsmässiga övervärdet) står "
     "INTE i vare sig SAOL eller SO. Den är korrekt som redovisningsterm men är "
     "alltså obelagd i de här källorna, och det noteras hellre än döljs.")

lagg("degression",
     "EJ I SAOL/SO — BELAGT I SAOB. Uppslaget saknas i båda de moderna ordböckerna "
     "och synonymer.se gav 'du kanske menade digression/depression/regression'. SAOB "
     "har det: 'nedåtgående, (fortsatt) tillbakagång l. avtagande l. minskning', och "
     "särskilt om beskattning: en **sjunkande skattesats**, motsatsen till progressiv "
     "skatt. Kortet stämmer alltså exakt, skatteexemplet inkluderat — men det vilar "
     "på EN källa, vilket skrivs ut.",
     kalla=SAOB.format("degression"))

for o, s in [
    ("försigkommen", "BEKRÄFTAT ORDAGRANT. SAOL: 'väl utvecklad för sin ålder, "
                     "avancerad'. SO: 'väl utvecklad för sin ålder', med exemplet 'redan "
                     "vid fyra års ålder kunde han läsa'. Kortets synonymer brådmogen och "
                     "lillgammal står inte i källorna men OLD-facit ger brådmogen."),
    ("imperialism", "BEKRÄFTAT. SO: 'utrikespolitik som är inriktad på behärskning av "
                    "områden **långt utanför** de egna gränserna', JFR kolonialism — "
                    "kortets första synonym. Avståndet är en del av definitionen och "
                    "skiljer imperialism från vanlig gränsexpansion."),
    ("extraordinär", "BEKRÄFTAT. SO: 'som går **mycket** utöver det vanliga', JFR "
                     "ovanlig. SAOL: 'ovanlig, utomordentlig'. Kortets definition är i "
                     "praktiken SO:s."),
    ("katedral", "BEKRÄFTAT — OCH KORTET ÄR BÄTTRE ÄN KÄLLAN. Båda ordböckerna säger bara "
                 "'domkyrka'. Kortets 'biskopens huvudkyrka i ett stift' förklarar vad en "
                 "domkyrka ÄR, vilket en synonymlista inte gör. Behålls."),
    ("nota bene", "BEKRÄFTAT ORDAGRANT. SAOL och SO ger identiskt 'märk väl'. SO:s exempel "
                  "visar den ironiska användningen: 'det är inte svårt att hålla nere "
                  "inflationen, nota bene om man ignorerar arbetslösheten'."),
    ("pistong", "BEKRÄFTAT. SAOL: 'kolv i cylinder'. SO: 'kolv'. Kortets synonym är "
                "ordagrant SO:s definition."),
]:
    lagg(o, s)


def main():
    index = {}
    for f in KALLOR:
        for e in json.load(open(f, encoding="utf-8")):
            index[e["ord"]] = e
    ut, saknade = [], []
    for ord_, (kalla, slutsats, andr) in P.items():
        e = index.get(ord_)
        if e is None:
            saknade.append(ord_)
            continue
        e = json.loads(json.dumps(e))
        e["sokkoll"] = {"kalla": kalla, "slutsats": slutsats}
        e["approved"] = True
        e["applicerad"] = False
        e.pop("skriven_av", None)
        for f_, v in andr.items():
            e["proposed"][f_] = v
        if "huvudbetydelse" in andr:
            e["proposed"]["synonym_groups"] = None
        e["oforandrad"] = not andr
        ut.append(e)
    os.makedirs("sessions", exist_ok=True)
    json.dump(ut, open(MAL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Skrev {len(ut)} poster -> {MAL}")
    print(f"  innehållsändrade : {sum(1 for e in ut if not e['oforandrad'])}")
    if saknade:
        print("SAKNADE:", saknade)


if __name__ == "__main__":
    main()
