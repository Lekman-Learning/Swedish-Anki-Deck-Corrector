# -*- coding: utf-8 -*-
"""Batch 2: 35 kort. Lardomar fran batch30 tillampade i forvag --
bojd form inne i fargtaggen, synonymer BARA ur SO/SAOL:s definitionstext,
' ; ' med mellanslag, alla SO-betydelser med, register mot markningen."""
import json

F = 'sessions/session_2026-08-17_v3-batch2.json'
C = '<font color="#3498db">%s</font>'
PAUSA = {"i ur och skur", "till lags", "åtra sig"}

K = {
"andlös": ("Som har sinnena på helspänn ; som präglas av stark koncentration", [],
 "Publiken satt " + (C % "andlös") + " genom hela slutscenen.",
 "neutral, neutral, allmän", "till ande och -lös"),

"dräktig": ("Som bär foster, om djur ; ibland bildligt full eller överfylld", [],
 "Veterinären konstaterade att tiken var " + (C % "dräktig") + " med fem valpar.",
 "fackspråklig, neutral, biologi", "till dräkt i äldre betydelsen 'börda'"),

"förläggare": ("Person som driver bokförlag ; äv. person som lämnar kapital eller lån för drivande av rörelse", [],
 "Hennes " + (C % "förläggare") + " ville korta manuset med hundra sidor.",
 "neutral, neutral, allmän", "till förlägga i betydelsen 'bekosta utgivning'"),

"herdedikt": ("Dikt om herdars och herdinnors liv på landsbygden, i äldre litteratur", [],
 "Samlingen innehöll flera " + (C % "herdedikter") + " från sextonhundratalet.",
 "ngt ålderdomlig, neutral, litteraturvetenskap", "till herde och dikt"),

"konsensus": ("Enighet eller vilja till enighet mellan parter som har olika intressen",
 ["enighet", "samstämmighet"],
 "Efter timmar av förhandling nåddes äntligen " + (C % "konsensus") + " i frågan.",
 "neutral, neutral, allmän", "av latinets consensus 'samstämmighet'"),

"mastodont": ("Utdött elefantdjur med betar i både under- och överkäken ; vanligen bildligt om väldig företeelse",
 ["koloss", "bjässe"],
 "Det nya sjukhuset blev en " + (C % "mastodont") + " som slukade hela budgeten.",
 "neutral, neutral, allmän", "av grekiska mastós 'bröstvårta' och odoús 'tand'"),

"nyttja": ("Tillgodogöra sig ; använda eller bruka", ["använda", "bruka", "begagna"],
 "Föreningen får " + (C % "nyttja") + " lokalen två kvällar i veckan.",
 "ngt ålderdomlig, neutral, allmän", "till nytta"),

"nära": ("Som befinner sig på kort avstånd i rum eller tid ; äv. bildligt om personligt och kärleksfullt förhållande ; äv. i substantivisk användning om anhöriga ; äv. i betydelsen nästan", [],
 "De bor " + (C % "nära") + " varandra men träffas nästan aldrig.",
 "neutral, neutral, allmän", "fornsvenska nær"),

"basker": ("Mjuk, låg mössa utan skärm ; äv. om person från Baskien", [],
 "Han bar alltid en svart " + (C % "basker") + " lite på sned.",
 "neutral, neutral, allmän", "efter Baskien, där mössan har sitt ursprung"),

"bergtagen": ("Som på ett övernaturligt sätt lockats in i ett berg ; ofta bildligt fascinerad och fängslad",
 ["fascinerad", "fängslad"],
 "Hon satt " + (C % "bergtagen") + " genom hela konserten.",
 "neutral, neutral, allmän", "till berg och taga"),

"frekvens": ("Antal förekomster per tidsenhet eller inom ett visst material ; äv. antal svängningar per sekund hos en vågrörelse", [],
 "Radion var inställd på fel " + (C % "frekvens") + " och gav bara brus.",
 "neutral, neutral, allmän", "av latinets frequentia 'talrikhet'"),

"oavvänd": ("Oavbruten, om blick eller uppmärksamhet", ["oavbruten"],
 "Barnet betraktade tricket med " + (C % "oavvänd") + " blick.",
 "litterär, neutral, allmän", "till o- och avvända"),

"oväld": ("Rättvisa och opartiskhet", ["rättvisa", "opartiskhet"],
 "Domaren berömdes för sin " + (C % "oväld") + " i en mycket laddad rättegång.",
 "ngt ålderdomlig, neutral, allmän", "till o- och väld 'partiskhet'"),

"stint": ("Med orörlig blick ; äv. om något välfyllt så att sidorna buktar ut", [],
 "Katten stirrade " + (C % "stint") + " på fågeln utanför fönstret.",
 "neutral, neutral, allmän", "till fornsvenska stinter 'styv, spänd'"),

"bossanova": ("Brasiliansk populärmusik utvecklad ur samban ; ofta äv. om ett enskilt musikstycke av denna typ", [],
 "Bandet avslutade kvällen med en långsam " + (C % "bossanova") + ".",
 "neutral, neutral, musik", "av portugisiska bossa nova 'ny stil'"),

"boulevard": ("Lång och bred, ofta trädplanterad gata i större stad", [],
 "De promenerade längs " + (C % "boulevarden") + " ända ner till hamnen.",
 "neutral, neutral, allmän", "av franska boulevard, ursprungligen 'bastion'"),

"dräll": ("Enklare damastliknande linnevävnad med geometriskt mönster ; äv. vardagligt om att planlöst förflytta sig hit och dit eller förekomma i stor och oordnad mängd", [],
 "Dukarna var vävda i " + (C % "dräll") + " med ett stramt geometriskt mönster.",
 "neutral, neutral, allmän ; vardaglig, neutral, allmän", "av lågtyska drell"),

"exkursion": ("Utfärd eller utflykt i studiesyfte", ["utflykt", "utfärd"],
 "Klassen åkte på " + (C % "exkursion") + " till kalkbrottet för att samla fossil.",
 "neutral, neutral, allmän", "av latinets excursio 'utflykt'"),

"förflackas": ("Göras ytligare och förlora sitt djup", [],
 "Debatten " + (C % "förflackades") + " när alla började tävla i slagord.",
 "neutral, lätt negativ, allmän", "till flack 'platt, grund'"),

"gimmick": ("Lustig specialitet eller finess som ska väcka uppmärksamhet ; äv. reklamtrick", [],
 "Appens enda " + (C % "gimmick") + " var att den kunde härma din röst.",
 "vardaglig, lätt negativ, allmän", "av engelska gimmick"),

"inpass": ("Snabbt inskjuten replik", [],
 "Hans torra " + (C % "inpass") + " fick hela rummet att skratta.",
 "neutral, neutral, allmän", "till inpassa 'skjuta in'"),

"jakaranda": ("Hårt och tungt brunviolett ädelträslag med mörk ådring ; äv. om det brasilianska träd som ger virket", [],
 "Gitarrens botten och sarger var byggda i " + (C % "jakaranda") + ".",
 "neutral, neutral, allmän", "av tupí-guaraní jacarandá"),

"jubilera": ("Fira jubileum", [],
 "Föreningen " + (C % "jubilerar") + " nästa år och fyller hundra.",
 "neutral, neutral, allmän", "till jubileum, av latinets jubilaeus"),

"kommunion": ("Utdelning eller mottagande av nattvarden ; äv. om föreningen med Kristus i nattvarden",
 ["nattvardsgång", "gudsgemenskap"],
 "Efter predikan följde " + (C % "kommunionen") + " vid altaret.",
 "fackspråklig, neutral, religion", "av latinets communio 'gemenskap'"),

"korrespondera": ("Brevväxla ; äv. överensstämma eller motsvara",
 ["brevväxla", "överensstämma", "motsvara"],
 "De två " + (C % "korresponderade") + " i trettio år utan att någonsin träffas.",
 "neutral, neutral, allmän", "av latinets correspondere 'svara varandra'"),

"materialisera": ("Ge konkret gestalt åt något ; äv. själv få konkret gestalt", ["förkroppsliga"],
 "Planerna " + (C % "materialiserades") + " aldrig till något verkligt bygge.",
 "neutral, neutral, allmän", "till material, av latinets materia"),

"misskreditera": ("Ge dåligt anseende ; bringa i vanrykte", ["diskreditera"],
 "Hela kampanjen gick ut på att " + (C % "misskreditera") + " motståndaren.",
 "neutral, negativ, allmän", "till miss- och kreditera"),

"multilateral": ("Som innefattar fler än två parter", [],
 "Avtalet var " + (C % "multilateralt") + " och band samman tolv länder.",
 "formell, neutral, politik", "till multi- 'många' och lateral 'sido-'"),

"numen": ("Verkan av en högre, utommänsklig kraft ; äv. om övernaturligt väsen som ännu inte fått någon exakt tolkning",
 ["naturgudomlighet"],
 "Platsen sades bära på ett " + (C % "numen") + " som ingen vågade störa.",
 "fackspråklig, neutral, religion", "av latinets numen 'gudomlig vilja'"),

"saklöst": ("Utan egentliga konsekvenser ; särskilt i juridiska sammanhang utan rättslig påföljd", [],
 "Stycket kan " + (C % "saklöst") + " strykas utan att texten förlorar något.",
 "formell, neutral, juridik", "till sak i juridisk betydelse och -löst"),

"silo": ("Högt, cylinderformat magasin för till exempel spannmål ; äv. om underjordisk anläggning där raketer förvaras", ["magasin"],
 "Spannmålet blåstes upp i " + (C % "silon") + " direkt från lastbilen.",
 "neutral, neutral, allmän", "av spanska silo 'sädesgrop'"),

"sinka": ("Fördröja eller uppehålla ; äv. foga ihop trasigt porslin med klammer eller brädor med tappar",
 ["fördröja", "uppehålla"],
 "Ett långt godståg " + (C % "sinkade") + " hela morgontrafiken.",
 "neutral, neutral, allmän", "till sink 'tapp, urtag'"),

"skrivelse": ("Skriftlig hänvändelse av formell karaktär, ofta till eller från en myndighet", [],
 "Föreningen skickade in en " + (C % "skrivelse") + " till kommunen om bullret.",
 "formell, neutral, allmän", "till skriva"),

"upprinnelse": ("Ursprung eller början till något", ["ursprung", "början", "källa", "orsak"],
 "Bråkets " + (C % "upprinnelse") + " var en gammal gränstvist mellan byarna.",
 "neutral, neutral, allmän", "till upprinna 'ha sin början'"),

"zygot": ("Cell som bildats genom sammansmältning av en hanlig och en honlig könscell",
 ["befruktad äggcell"],
 "Ur den befruktade " + (C % "zygoten") + " utvecklas så småningom hela embryot.",
 "fackspråklig, neutral, biologi", "av grekiska zygōtós 'sammanfogad'"),
}

d = json.load(open(F, encoding='utf-8'))
poster = d['poster'] if isinstance(d, dict) else d
n = 0
for p in poster:
    w = p['ord']
    if w in PAUSA or w not in K:
        continue
    hb, syn, ex, reg, ety = K[w]
    p['proposed'] = {"huvudbetydelse": hb, "synonymer": syn, "synonym_groups": None,
                     "exempelmening": ex, "register": reg, "etymologi": ety}
    p['approved'] = True
    n += 1
json.dump(d, open(F, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('skrev proposed pa %d kort' % n)
