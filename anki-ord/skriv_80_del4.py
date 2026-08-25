# -*- coding: utf-8 -*-
"""80-kortsomgangen 2026-08-25, del 4 (ord 61-80).

Kallor lasta via visa_uppslag.py -- SO:s rastruktur och SAOL ordagrant,
aldrig synonymer.se.

`vadevill` pausas: bara SAOB-lemma, ingen definitionstext i API:t, saknas i
SO och SAOL. Samma skal som glutinos och mockant i batch 6.
"""
import json
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-25_v3-batch2.json"
BLA = '<font color="#3498db">%s</font>'
HOPPA = {"vådevill"}

TILLAT = {
 "kor": {"betydelse_kan_saknas":
   "SO har EN huvudbetydelse for lemmat `kor` (kyrkans altarrum). SAOL:s ovriga "
   "poster ar andra lemman: `kor` som aldre stavning av `kor` (sangkoren) och "
   "pluralen av `ko` (notkreatur). Kortordet ar kyrkorummet."},
 "kvot": {"betydelse_kan_saknas":
   "SO:s rastruktur: TVA huvudbetydelser ('tal som utgor resultatet av division' "
   "och 'andel som ses i proportion till ett helt'). Bada star pa kortet."},
 "ligga i träda": {
   "betydelse_kan_saknas":
   "Uttrycket bygger pa substantivet `trada` ('akermark som tillfalligt ligger "
   "obesadd'). SO:s ovriga lemman ar verbet `ligga` i alla dess betydelser och "
   "verbet `trada` ('forflytta sig med langsamma steg'), som inte hor hit.",
   "frammande_uppslagsord":
   "Uttrycket ar tre ord, sa fuzzy-sokningen traffar `ligga` och `trada` som "
   "egna lemman."},
 "perukstock": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('trastallning for peruker') och EN "
   "underbetydelse ('gammal stofil'). Bada star pa kortet."},
 "progressiv": {"betydelse_kan_saknas":
   "SO har TRE huvudbetydelser ('positiv till forandringar', 'som innebar "
   "progression', 'fortskridande'). Kortet slar ihop de tva sista, som bada "
   "beskriver nagot som vaxer stegvis -- SAOL skriver dem ocksa som ett led: "
   "'jamnt vaxande, gradvis stigande'."},
 "retorisk fråga": {
   "betydelse_kan_saknas":
   "Uttrycket ar sammansatt av `retorisk` och `fraga`, och SO listar bada som "
   "egna lemman med sina fulla betydelseuppsattningar. Uttrycket sjalvt har en "
   "betydelse.",
   "frammande_uppslagsord":
   "Uttrycket ar tva ord, sa fuzzy-sokningen traffar `fraga` som substantiv och "
   "som verb."},
 "överlappa": {"betydelse_kan_saknas":
   "SO:s rastruktur: EN huvudbetydelse ('delvis tacka varandra') med tva "
   "underbetydelser utan egen definition. SAOL:s andra post ('en finess i "
   "fotboll') ar substantivet `overlapp`, inte verbet."},
}

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form, etymologi)
KORT = {
 "kor": ("Den del av en kyrka där huvudaltaret står",
   "fackspråklig, neutral", [],
   "Prästen gick fram till altaret i koret.", "koret",
   "Av latin <i>chorus</i>, av grekiska <i>khoros</i> 'dans, sångargrupp'. Platsen där kyrkokören stod."),

 "kurvatur": ("Bågformighet ; krökt parti av något",
   "fackspråklig, neutral", ["krökning"],
   "Ryggradens naturliga kurvatur syns tydligt på röntgen.", "kurvatur",
   "Av latin <i>curvatura</i> 'krökning', till <i>curvus</i> 'böjd'."),

 "kvader": ("Rätvinklig natursten för byggnadsändamål",
   "fackspråklig, neutral", [],
   "Muren var byggd av huggna kvadrar.", "kvadrar",
   "Av latin <i>quadrus</i> 'fyrkantig', till <i>quattuor</i> 'fyra'."),

 "kvot": ("Tal som utgör resultatet av en division ; andel sedd i proportion till ett helt",
   "neutral, neutral", ["andel"],
   "Kvoten mellan de två talen blev exakt tre.", "Kvoten",
   "Av latin <i>quotus</i> 'hur mångte i ordningen', till <i>quot</i> 'hur många'."),

 "ligga i träda": ("Om åkermark: ligga obesådd en tid för att återhämta sig ; (bildligt) ligga oanvänd",
   "neutral, neutral", [],
   "Halva gården fick ligga i träda den sommaren.", "träda",
   "Till <i>träda</i>, av fornsvenska <i>þræþe</i>. Besläktat med <i>tramp</i> — marken trampades av betande djur."),

 "perukstock": ("Träställning för peruker ; (bildligt) gammal stofil",
   "ngt ålderdomlig, nedsättande", [],
   "Han avfärdade hela styrelsen som en samling perukstockar.", "perukstockar",
   "Till <i>peruk</i> och <i>stock</i>. Den bildliga betydelsen syftar på något livlöst med peruk på."),

 "progressiv": ("Positiv till förändringar och utveckling ; som växer jämnt och stegvis",
   "neutral, neutral", ["framstegsvänlig"],
   "Skatten är progressiv och stiger med inkomsten.", "progressiv",
   "Av latin <i>progressus</i> 'framsteg', till <i>progredi</i> 'gå framåt'."),

 "prospektera": ("Undersöka ett område med avseende på förekomst av naturtillgångar",
   "fackspråklig, neutral", [],
   "Bolaget prospekterade efter koppar i fjällen.", "prospekterade",
   "Av latin <i>prospectare</i> 'blicka ut över', till <i>prospicere</i> 'se framåt'."),

 "protektion": ("Beskydd, ofta genom en inflytelserik gynnare",
   "ngt ålderdomlig, neutral", ["beskydd"],
   "Konstnären levde under grevens protektion.", "protektion",
   "Av latin <i>protectio</i> 'skydd', till <i>protegere</i> 'täcka framför'."),

 "reinkarnation": ("En människas återfödelse efter döden i en annan jordisk kropp",
   "neutral, neutral", [],
   "Läran om reinkarnation är central i hinduismen.", "reinkarnation",
   "Till latin <i>re-</i> 'åter' och <i>incarnatio</i> 'förkroppsligande', av <i>caro</i> 'kött'."),

 "retorisk fråga": ("Fråga som ställs utan att svar väntas, för att göra ett påstående",
   "neutral, neutral", [],
   "Är det verkligen för mycket begärt, frågade han retoriskt.", "retoriskt",
   "Till <i>retorik</i>, av grekiska <i>rhetorike techne</i> 'talarkonst'."),

 "sedeslös": ("Som saknar sexuell moral",
   "ngt ålderdomlig, nedsättande", [],
   "Romanen ansågs sedeslös och förbjöds.", "sedeslös",
   "Till <i>seder</i> och <i>-lös</i>."),

 "skrävel": ("Storordigt skryt",
   "neutral, nedsättande", ["storskryt"],
   "Allt hans prat var tomt skrävel.", "skrävel",
   "Till <i>skrävla</i>, av ljudhärmande ursprung."),

 "teach-in": ("Stor öppen debatt om ett aktuellt problem",
   "neutral, neutral", [],
   "Studenterna ordnade en teach-in om klimatfrågan.", "teach-in",
   "Av engelska <i>teach-in</i>, bildat efter mönster av <i>sit-in</i>."),

 "traktör": ("Person som driver eller förestår en restaurang",
   "ngt ålderdomlig, neutral", ["värdshusvärd", "källarmästare"],
   "Traktören kom själv ut och tog emot gästerna.", "Traktören",
   "Av franska <i>traiteur</i> 'krögare', till <i>traiter</i> 'undfägna, behandla'."),

 "ulster": ("Lång, löst sittande överrock av grovt ylletyg",
   "ngt ålderdomlig, neutral", [],
   "Han svepte om sig ulstern och gick ut i snön.", "ulstern",
   "Efter Ulster på Irland, där tyget tillverkades."),

 "ymnighetshorn": ("Horn som överflödar av frukt och blommor, som bild för riklig förekomst",
   "högtidlig, positiv", [],
   "Hösten öste sina gåvor ur ett ymnighetshorn.", "ymnighetshorn",
   "Översättning av latin <i>cornu copiae</i> 'överflödets horn'."),

 "ögna": ("Snabbt och flyktigt se på eller läsa något",
   "neutral, neutral", [],
   "Hon ögnade igenom rapporten på tåget.", "ögnade",
   "Till <i>öga</i>."),

 "överlappa": ("Delvis täcka varandra ; gå om lott",
   "neutral, neutral", [],
   "De två utredningarna överlappar varandra i flera delar.", "överlappar",
   "Efter engelska <i>overlap</i>, till <i>lap</i> 'vika över'."),
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    skrivna = pausade = 0
    for e in poster:
        o = e["ord"]
        if o in HOPPA:
            pausade += 1
            print("  PAUSAS (ingen ordbokskalla):", o)
            continue
        if o not in KORT:
            continue
        bet, reg, syn, ex, form, etym = KORT[o]
        if form in ex:
            ex = ex.replace(form, BLA % form, 1)
        else:
            print("  VARNING: hittade inte", form, "i:", ex)
        e["proposed"] = {
            "huvudbetydelse": bet, "register": reg, "synonymer": syn,
            "synonym_groups": None, "exempelmening": ex, "etymologi": etym,
        }
        e["approved"] = True
        q = urllib.parse.quote(o)
        e["sokkoll"] = {
            "kalla": (f"SO och SAOL via https://svenska.se/api/msearch?ord={q} "
                      f"samt https://www.synonymer.se/sv-syn/{q} -- hamtade 2026-08-25, "
                      f"sparade i uppslag/{o}.json"),
            "slutsats": ("Betydelser, register och synonymer lasta ur SO:s rastruktur och "
                         "SAOL:s definitionstext via visa_uppslag.py, som inte visar "
                         "synonymer.se. Inget skrivet som inte star i nagon av ordbockerna."),
        }
        if o in TILLAT:
            e["forgranska_tillat"] = TILLAT[o]
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"del 4: skrivna {skrivna}  pausade {pausade}")


if __name__ == "__main__":
    main()
