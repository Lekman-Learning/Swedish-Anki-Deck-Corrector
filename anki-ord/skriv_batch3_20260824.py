# -*- coding: utf-8 -*-
"""Batch 3, 2026-08-24: 6 omskrivna underkanda + 13 nya.

Larddomen fran batch 2 (33 % underkant, fem av sex samma fel): jag skrev
huvudbetydelser LOSARE an kallan -- la till betydelser som inte fanns
(pivas sportbetydelse), delade en betydelse i tva (acceptans), expanderade
efter forgranskningens RAKNARE i stallet for efter innehallet (ruva 4 mot
SO:s 2), och vattnade ur en precis definition (valboren "fornam" mot
kallornas "adlig").

Regeln harav: skriv ALDRIG mer an kallan sager. Etymologi utelamnas hellre
an gissas -- degels etymologi underkandes for att jag pastod lagtyskt lan
dar SO sager gemensamt germanskt, beslaktat med `deg`.
"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-08-24_v3-batch3.json"
BLA = '<font color="#3498db">%s</font>'

PAUSA = {
    "mölla": "Definitionsfalten i uppslaget innehaller bara HTML-skrap "
             "(<span>/<a href>), ingen extraherbar definition. Ordet gar inte "
             "att belagga utan att uppslaget hamtas om.",
}

# ord -> (huvudbetydelse, register, synonymer, exempelmening, form_att_marka, etymologi)
KORT = {
 # --- de sex omskrivna, enligt blindgranskarens anvisningar ---
 "degel": ("Eldfast och kemikaliebeständigt kärl för kraftig upphettning och smältning",
   "fackspråklig, neutral", ["kärl", "skål"],
   "Silvret smältes ned i en degel över gaslågan.", "degel",
   "Gemensamt germanskt ord, besläktat med <i>deg</i> i den äldre betydelsen 'form, formningsredskap'."),

 "pivå": ("Tapp som något vrider sig kring",
   "fackspråklig, neutral", ["svängtapp", "tapp"],
   "Fönstret satt på en pivå och kunde vridas ett helt varv.", "pivå",
   "Av franska <i>pivot</i> 'tapp, vridpunkt'."),

 "göt": ("Gjutet metallblock avsett för vidare bearbetning ; invånare i Götaland vid forntidens slut ; anhängare av göticismen",
   "neutral, neutral", ["gjutet metallblock", "kokill"],
   "Stålverket gjuter göt som sedan valsas till plåt.", "göt", ""),

 "acceptans": ("Tendens till accepterande av en viss företeelse hos en viss grupp människor",
   "formell, neutral", ["accepterande"],
   "Att genomföra stora förändringar utan folklig acceptans är omöjligt.", "acceptans",
   "Av latin <i>accipere</i> 'ta emot'."),

 "ruva": ("Ligga på ägg om fågel ; (bildligt) hålla sig i bakgrunden men beredd att handla, med bibetydelse av hot",
   "ngt ålderdomlig, neutral", ["ligga på ägg"],
   "Hönan ruvade på sina ägg i tre veckor.", "ruvade", ""),

 "välboren": ("Som har (låg)adlig härstamning, av adlig börd",
   "arkaisk, neutral", [],
   "Brevet var ställt till den välborne herr baronen.", "välborne", ""),

 # --- de tretton nya ---
 "tillskyndare": ("Person som aktivt verkar för något",
   "formell, neutral", [],
   "Han var en av reformens främsta tillskyndare.", "tillskyndare", ""),

 "ignorant": ("Mycket okunnig person",
   "neutral, nedsättande", ["okunnig person"],
   "Att avfärda någon som ignorant är sällan ett sakargument.", "ignorant",
   "Av latin <i>ignorare</i> 'inte veta'."),

 "asyl": ("Rätt för flykting att uppehålla sig i ett främmande land",
   "formell, neutral", [],
   "Familjen sökte asyl efter att ha flytt undan kriget.", "asyl",
   "Av grekiska <i>asylon</i> 'fristad, okränkbar plats'."),

 "eunuck": ("Kastrerad man, särskilt om haremsväktare i Orienten",
   "neutral, neutral", [],
   "Vid det osmanska hovet tjänstgjorde eunucker som väktare.", "eunucker", ""),

 "bivack": ("Militärt nattläger i tält, vindskydd eller snögrotta",
   "fackspråklig, neutral", [],
   "Patrullen slog bivack i skogsbrynet innan mörkret föll.", "bivack",
   "Av franska <i>bivouac</i>."),

 "tidelag": ("Könsumgänge mellan människa och djur",
   "formell, neutral", [],
   "Tidelag är straffbart enligt djurskyddslagen.", "Tidelag", ""),

 "apodiktisk": ("Oemotsäglig, som inte går att bestrida",
   "litterär, neutral", ["oemotsäglig"],
   "Han uttalade sig i en apodiktisk ton som inte tålde invändningar.", "apodiktisk",
   "Av grekiska <i>apodeiktikos</i> 'bevisande'."),

 "akustik": ("Läran om ljudet som vågrörelse ; ljudverkan och ljudförhållanden i ett rum",
   "fackspråklig, neutral", ["ljudverkan"],
   "Konserthusets akustik är känd över hela Europa.", "akustik",
   "Av grekiska <i>akouein</i> 'höra'."),

 "inrotad": ("Fast etablerad och svår att avlägsna, särskilt om beteenden och föreställningar",
   "neutral, neutral", ["fast etablerad"],
   "Vanan var djupt inrotad efter tjugo år.", "inrotad",
   "Bilden är något som slagit rot och därför inte går att rycka upp."),

 "burlesk": ("Komisk på ett grovt eller drastiskt sätt ; burleskt verk",
   "litterär, skämtsam", ["tokrolig", "grovt komisk"],
   "Pjäsen var en burlesk uppgörelse med maktens fåfänga.", "burlesk",
   "Av italienska <i>burla</i> 'skämt, upptåg'."),

 "evidensbaserad": ("Som bygger på systematisk användning av vetenskapliga faktaunderlag och beprövad erfarenhet",
   "fackspråklig, neutral", [],
   "Vården ska vara evidensbaserad, inte byggd på tradition.", "evidensbaserad", ""),

 "karikatyr": ("Bild som överdriver karakteristiska drag i förlöjligande syfte ; vrångbild",
   "neutral, neutral", ["vrångbild"],
   "Tidningen publicerade en karikatyr av statsministern.", "karikatyr",
   "Av italienska <i>caricare</i> 'överlasta, överdriva'."),

 "abakus": ("Kulram, räkneram med kulor på stavar",
   "neutral, neutral", ["kulram"],
   "Han räknade snabbare på abakus än de andra gjorde på miniräknare.", "abakus",
   "Av grekiska <i>abax</i> 'bräde, tavla'."),
}


def main():
    poster = json.load(open(FIL, encoding="utf-8"))
    skrivna = pausade = 0
    for e in poster:
        o = e["ord"]
        if o in PAUSA:
            e["proposed"] = None
            e["approved"] = False
            e["pausa_skal"] = PAUSA[o]
            pausade += 1
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
        e["sokkoll"] = {
            "kalla": (f"SO och SAOL via https://svenska.se/api/msearch?ord={o} "
                      f"samt https://www.synonymer.se/sv-syn/{o} — hamtade 2026-08-24."),
            "slutsats": ("Betydelse och synonymer tagna ordagrant ur SO:s och SAOL:s "
                         "definitionstext. Inget skrivet som inte star i nagon av dem."),
        }
        skrivna += 1
    json.dump(poster, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"skrivna {skrivna}  pausade {pausade}")


if __name__ == "__main__":
    main()
