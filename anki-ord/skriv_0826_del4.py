# -*- coding: utf-8 -*-
"""Del 4. Första batchen skriven MED den nya Adam-tal-regeln från början:
inget ord i huvudbetydelsen får självt vara ett uppslagsord i decket, och
lagningen sker som omskrivning till kort fras — aldrig som synonymbyte.
"""
import json, urllib.parse

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}


def H(w):
    return '<font color="#3498db">' + w + '</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, tillat=None, conf=9):
    e = BY[o]
    q = urllib.parse.quote(o)
    e["proposed"] = {"huvudbetydelse": bet, "register": reg, "synonymer": syn,
                     "synonym_groups": None, "exempelmening": ex, "etymologi": ety}
    e["sokkoll"] = {"kalla": "SO och SAOL via https://svenska.se/api/msearch?ord=" + q
                    + " (hämtat 2026-08-26, HTTP 200)", "slutsats": slutsats}
    e["confidence"] = conf
    e["approved"] = True
    if tillat:
        e.setdefault("forgranska_tillat", {}).update(tillat)


satt("changemang",
     "Snabbt och synligt byte, särskilt av scen på en teater",
     "ngt ålderdomlig", ["scenförändring"],
     "Ridån gick ner för ett kort " + H("changemang") + " mellan akterna.", None,
     "SO: snabb synlig förändring; spec. scenväxling; spec. äv. ombyte av galopp i språnget. "
     "Markerat något ålderdomligt. SAOL: scenförändring; ombyte av galoppart — scenförändring "
     "inleder ett eget led och är belagd synonym. Ridsportbetydelsen är för smal för kortet.")

satt("chaussé",
     "Bred landsväg med hårdgjord vägbana",
     "ngt ålderdomlig", [],
     "Alléerna kantade den gamla " + H("chaussén") + " in mot staden.", None,
     "SO: bred landsväg. SAOL: bred väg. Legacys motorväg är fel — en chaussé är en äldre "
     "landsväg, inte en motorväg. Landsväg är definitionens huvudord, inte en utbytbar synonym.",
     {"register_motsager_markning": "Varken SO eller SAOL märker ordet. Registret sätts på eget "
                                    "omdöme: chaussé är i modern svenska ett historiskt ord för "
                                    "äldre vägbyggnad. Ingen ordboksmärkning motsägs."})

satt("demaskera",
     "Ta av någon masken ; avslöja vem eller vad något egentligen är",
     "neutral", ["avslöja"],
     "I slutet av filmen " + H("demaskeras") + " skurkarna.", None,
     "SO: avlägsna maskering från; avslöja, ofta bildligt. SAOL: ta av ngn masken; avslöja, blotta "
     "— avslöja inleder andra ledet och är belagd synonym. Blotta står efter komma och räknas inte.")

satt("determinism",
     "Tanken att allt som händer är bestämt i förväg av det som hänt innan",
     "fackspråklig, filosofi", [],
     "Den hårda " + H("determinismen") + " lämnar inget utrymme för fri vilja.", None,
     "SO: en filosofisk ståndpunkt som hävdar att varje skeende är orsaksbetingat och lagbundet; "
     "ofta mer inskränkt: att allt är förutbestämt och att viljan således inte är fri. "
     "SAOL: uppfattningen att viljan inte är fri. Legacys predestinationslära är ett teologiskt "
     "grannbegrepp, inte en synonym.")

satt("diskurs",
     "Samtal ; det sätt man pratar och tänker om ett ämne inom ett område",
     "fackspråklig, lingvistik", ["samtal"],
     "Tidningarna speglar " + H("diskursen") + " i samhället.", None,
     "SO: samtal; spec. i språkvetenskapliga sammanhang om uppbyggnaden av samtal och texter; "
     "ofta äv. om förhärskande omständigheter eller ideologi. SAOL: sätt att resonera inom ett "
     "visst område, märkt språkv. m.m. Samtal utgör hela SO:s första definition och är belagd.")

satt("doktrin",
     "Fast lära eller uppsättning grundsatser som styr hur man handlar",
     "formell, politik", [],
     "Landets militära " + H("doktrin") + " bygger på avskräckning.", None,
     "SO: system av principer som utgör grundval för handlande eller rättesnöre vid bedömning av "
     "juridiska spörsmål. SAOL: teoretisk el. ensidig lära el. norm, märkt polit., mil. "
     "Lära och norm står inuti SAOL:s enda led utan att inleda det — inte belagda som synonymer.")

satt("encefalografi",
     "Röntgen av hjärnans hålrum med kontrastmedel",
     "fackspråklig, medicin", [],
     "Före datortomografin var " + H("encefalografi") + " en plågsam undersökning.", None,
     "SO: kontraströntgen av hjärnans hålrum. Ingen SAOL-artikel i träffen. Legacys luftskalle är "
     "ett slangartat äldre uttryck utan ordboksbelägg; röntgenundersökning är för brett.")

satt("enrollera",
     "Skriva in någon i en officiell lista över medlemmar eller soldater",
     "formell", [],
     "Vid krigsutbrottet " + H("enrollerades") + " han i infanteriet.", None,
     "SO: skriva in i officiell medlemsförteckning; numera allmännare, ofta med tonvikt på att "
     "vederbörande blir medlem. SAOL: skriva in för militärtjänst, i medlemsförteckning e.d. "
     "Legacys rekrytera och mönstra saknar belägg som egna definitionsled.")

satt("envig",
     "Kamp mellan två — man mot man",
     "ngt ålderdomlig", ["tvekamp"],
     "Finalen blev ett tufft " + H("envig") + " i fem set.", None,
     "SO: strid mellan två personer eller grupper, markerat något ålderdomligt; äv. bildligt "
     "(industrisamhällets envig med naturen). SAOL: tvekamp — utgör hela definitionen och är "
     "belagd synonym. Duell saknar belägg.",
     {"betydelse_kan_saknas": "SO:s extraposter är tre cohyponym-markörer plus äv. bildligt. "
                              "Den enda betydelsen — kamp mellan två — finns på kortet, och "
                              "exempelmeningen visar den bildliga användningen."})

satt("epidermis",
     "Hudens yttersta lager",
     "fackspråklig, medicin", ["överhud"],
     "I fotsulan är " + H("epidermis") + " extra kraftig.", None,
     "SO: överhud; äv. om liknande skikt hos växter. SAOL: överhud; tunt yttre cellskikt hos växt. "
     "Överhud utgör hela SO:s definition och inleder SAOL:s — belagd synonym.")

satt("filolog",
     "Forskare som studerar språk och gamla texter",
     "fackspråklig, lingvistik", ["språkvetare"],
     "En " + H("filolog") + " kan datera en text på stavningen allena.", None,
     "SO: person som yrkesmässigt ägnar sig åt filologi; förr äv. allmännare: språkvetare, lingvist. "
     "Språkvetare inleder det andra definitionsledet och är belagd synonym. Texttolkare saknar belägg.")

satt("foglig",
     "Som lätt går med på vad andra vill, utan att sätta sig på tvären",
     "neutral", [],
     "Regimen ville ha " + H("fogliga") + " och underdåniga medborgare.", None,
     "SO: benägen att anpassa sig; exempel regimen tycktes vilja ha fogliga och underdåniga "
     "medborgare. SAOL har bara en jfr-hänvisning. Medgörlig, lydig och eftergiven saknar belägg "
     "som egna definitionsled — och eftergiven är dessutom självt ett kort i decket.")

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Del 4 skriven: 12 kort. Totalt approved: %d/%d"
      % (sum(1 for e in S if e.get("approved")), len(S)))
