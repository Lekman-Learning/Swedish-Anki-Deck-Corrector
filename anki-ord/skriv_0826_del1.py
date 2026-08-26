# -*- coding: utf-8 -*-
import json, urllib.parse

F = "sessions/session_2026-08-26_v3-batch.json"
S = json.load(open(F, encoding="utf-8"))
BY = {e["ord"]: e for e in S}


def H(w):
    return '<font color="#3498db">' + w + '</font>'


def satt(o, bet, reg, syn, ex, ety, slutsats, conf=9):
    e = BY[o]
    q = urllib.parse.quote(o)
    e["proposed"] = {
        "huvudbetydelse": bet,
        "register": reg,
        "synonymer": syn,
        "synonym_groups": None,
        "exempelmening": ex,
        "etymologi": ety,
    }
    e["sokkoll"] = {
        "kalla": "SO och SAOL via https://svenska.se/api/msearch?ord=" + q
                 + " (hämtat 2026-08-26, HTTP 200)",
        "slutsats": slutsats,
    }
    e["confidence"] = conf
    e["approved"] = True


satt("disputation",
     "Mötet där en doktorand offentligt försvarar sin avhandling mot en opponent",
     "formell", [],
     "Hennes " + H("disputation") + " tog tre timmar och opponenten var stenhård.",
     "till disputera, alltså att argumentera",
     "SO: akademisk sammankomst med granskning och försvar av doktorsavhandling. SAOL likalydande. "
     "Legacy hade två snarlika definitioner av samma betydelse — hopslagna. Synonymen doktorsdisputation "
     "struken (cirkulär); försvar och avhandling saknar ordboksbelägg.")

satt("girland",
     "Prydnadsband av blommor eller löv som hänger i mjuka bågar",
     "neutral", [],
     "De hängde en " + H("girland") + " av granris över dörren.", None,
     "SO: yvigt, dekorativt band som kan draperas i mjuka vågor; exempel julgranens girlanger. "
     "SAOL: prydnadsranka av blommor. Festong och slinga saknar ordboksbelägg som synonymer.")

satt("gom",
     "Taket i munnen ; hel tandprotes",
     "neutral", [],
     "Han brände " + H("gommen") + " på den heta pizzan.", None,
     "SO ger TVÅ betydelser: munhålans övre, välvda begränsningsyta samt garnityr av löständer. "
     "SAOL bekräftar båda: tak i munhåla; hel tandprotes. Legacy hade bara den första.")

satt("grav",
     "Grävd hålighet i marken där en död läggs ; allvarlig, med svåra följder",
     "neutral", [],
     "Utredningen fann " + H("grava") + " brister i säkerheten.", None,
     "SO och SAOL ger två skilda ord: substantivet grävd hålighet i marken, och adjektivet som har "
     "eller kan få allvarliga följder (SAOL: svår, allvarlig). OLD-facit sa bara allvarlig, legacy "
     "bara substantivet. Båda krävs.")

satt("gördla",
     "Spänna ett bälte eller band runt något",
     "neutral", [],
     "Munken var " + H("gördlad") + " med ett grovt rep.", None,
     "SO och SAOL identiskt: förse med gördel. SO-exempel: en gördlad rock. Ingen märkning i någon "
     "ordbok, alltså neutral. Legacys förse och omge saknar belägg som synonymer.")

satt("i onåd",
     "Att ha förlorat en överordnads gunst",
     "ngt ålderdomlig", [],
     "Han föll " + H("i onåd") + " hos chefen efter att ha sagt sanningen.", None,
     "SO: onåd = överordnad persons missnöje; exempel råka i onåd, han föll i onåd hos makthavarna. "
     "SAOL: ogunst; exempel falla i onåd. Legacys oråd är ett annat ord — struket.")

satt("inventarium",
     "Förteckning över en verksamhets lösa ägodelar ; person som funnits på en plats så länge "
     "att hen hör till möblemanget",
     "neutral, skämtsam", [],
     "Den gamle vaktmästaren var något av ett " + H("inventarium") + " på teatern.", None,
     "SO ger tre betydelser; de två som bär ordförrådet är förteckningen och den bildliga om en person "
     "(person som verkat mycket länge på en plats, exempel om vaktmästaren). OLD-facit entrotjänare "
     "pekar på just den bildliga — legacy saknade den helt.")

satt("kainsmärke",
     "Synligt tecken på att någon bär skuld för något ont",
     "högtidlig, bibliskt", [],
     "Domen följde honom som ett " + H("kainsmärke") + " resten av livet.",
     "efter Kain, som enligt Bibeln dräpte sin bror",
     "SO: tecken på ondska, märkt ursprungligen bibliskt; etymologi till det bibliska personnamnet Kain. "
     "SAOL: tecken på en persons ondska. Etymologin tas med eftersom ordet blir självförklarande av den.")

satt("karda",
     "Redskap med tänder som reder ut ull före spinning ; reda ut ull med ett sådant redskap",
     "neutral", [],
     "Hon satt och " + H("kardade") + " ullen framför brasan.", None,
     "SO: redskapet, plus verbet luckra upp och reda ut. SAOL bekräftar båda. SO har även betydelsen "
     "hand märkt vardagligt — utelämnad som särbetydelse utanför ordets kärna. Synonymen kardmaskin "
     "struken (cirkulär).")

satt("ketch",
     "Segelbåt med två master, där den bakre är kortare och står en bit in från aktern",
     "fackspråklig, sjöfart", [],
     "De seglade över Atlanten i en gammal " + H("ketch") + ".", None,
     "SO: tvåmastad segelbåt med tämligen hög mesanmast placerad ett stycke in från aktern. "
     "SAOL: en tvåmastad segelbåt. Yawl och galeas är andra båttyper (SO listar dem som cohyponymer, "
     "inte synonymer) — strukna.")

satt("krusig",
     "Full av små vågor eller lockar",
     "neutral", ["smålockig"],
     "En vindpust gjorde vattenytan " + H("krusig") + ".", None,
     "SO: full av små vågor; exempel krusigt hår, en krusig vattenyta, krusig sallat. "
     "SAOL: smålockig; veckig, räfflad — smålockig inleder ledet och är därmed belagd synonym. "
     "Krullig och burrig saknar belägg.")

satt("långledas",
     "Ha väldigt tråkigt under lång tid",
     "ngt ålderdomlig", [],
     "Han satt och " + H("långleddes") + " framför tv:n hela söndagen.", None,
     "SO: ha mycket långtråkigt, märkt något ålderdomligt el. dialektalt; exempel sitta och långledas "
     "framför tv:n. SAOL: ha långtråkigt, märkt prov. Registret följer ordbokens märkning.")

satt("obstruktion",
     "Att medvetet sabotera eller förhala något ; hinder eller tilltäppning",
     "formell", ["hinder"],
     "Oppositionen anklagades för " + H("obstruktion") + " när de begärde votering om varje punkt.", None,
     "SO: medvetet försvårande av utförande, spec. i parlament om förhalning; samt hinder, tilltäppning "
     "(spec. medicin). Hinder inleder ett eget definitionsled och är därmed belagd. SAOL har bara hänvisning.")

satt("solidarisk",
     "Som håller ihop med och ställer upp för andra ; som delar ansvaret lika",
     "neutral", [],
     "De var " + H("solidariska") + " och vägrade utföra de strejkandes jobb.", None,
     "SO ger två betydelser: som känner samhörighet med och är beredd att stödja andra, samt som har "
     "gemensamt och lika ansvar. SAOL: gemensamt ansvarig; som obrottsligt håller på och hjälper ngn.")

satt("talja",
     "Lyftanordning där en lina löper genom två block ; lyfta något med en sådan",
     "fackspråklig, sjöfart", [],
     "De halade upp motorn med en " + H("talja") + ".", None,
     "SO: lyftanordning med två block som en lina löper genom, plus verbet förflytta i höjdled med hjälp "
     "av talja. SAOL bekräftar båda. Synonymen taljblock struken (cirkulär); tackel och blocktyg saknar belägg.")

satt("ympa",
     "Foga in en kvist från en växt i stammen på en annan ; vaccinera",
     "neutral", [],
     "Han " + H("ympade") + " in nya grenar i det gamla äppelträdet.", None,
     "SO: foga samman en växtdel (ymp) med en annan (grundstam), samt vaccinera. SAOL bekräftar båda: "
     "skära in kvist el. knopp från ädlare träd på en stam, samt vaccinera. Synonymen inympa struken (cirkulär).")

json.dump(S, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
klara = sum(1 for e in S if e.get("approved"))
print("Skrev 16 kort. Totalt approved i sessionen: %d/%d" % (klara, len(S)))
