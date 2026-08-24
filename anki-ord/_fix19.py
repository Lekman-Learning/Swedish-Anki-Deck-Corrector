# -*- coding: utf-8 -*-
"""Rattar de 19 korten som underkandes i blindgranskningen av
session_2026-08-20_v3-paket3-klara.json. Skriver in nya proposed-falt i
sessions/session_2026-08-20_v3-batch3.json (samma fil som ursprungligen
byggde alla 200 korten via kortbyggare/applicera), sa att kortgranskare.py
applicera kan koras om for just dessa noteIds.

Kalla for varje ord: https://svenska.se/api/msearch?ord=<ord>, hamtad via
slaupp.py i den har sessionen (SVENSKA_SE_HAMTAD-bevisraderna star i
transkriptet -- se sokkoll_verifiering.py). Fullstandiga SO/SAOL/SAOB-svar
sparade i uppslag/<ord>.json.
"""
import json
import urllib.parse

PATH = "sessions/session_2026-08-20_v3-batch3.json"


def hl(word):
    return f'<font color="#3498db">{word}</font>'


def kalla(ord_):
    return "https://svenska.se/api/msearch?ord=" + urllib.parse.quote(ord_, safe="")


FIXES = {
    1780080621182: dict(  # epikuré
        huvudbetydelse="En person som lever för njutning och goda upplevelser",
        register="litterär, neutral",
        synonymer=["njutningsmänniska"],
        synonym_groups=None,
        exempelmening='Som sann {} lät han aldrig en god måltid gå obemärkt förbi.'.format(hl("epikuré")),
        etymologi="Efter den grekiske filosofen Epikuros.",
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21 (claude-cli-blind), OMSKRIVET efter "
            "riktig sokkoll mot svenska.se. SAOL:s enda synonym for epikure ar "
            "'njutningsmanniska' (star sist i SAOL:s ledade definition 'anhangare av ... "
            "Epikuros filosofi ...; njutningsmanniska'). 'levnadskonstnar' finns bara i "
            "synonymer.se:s lista (kandidater, ej facit) och ar inte en sann synonym "
            "-- en levnadskonstnar ar skicklig pa att LEVA (gott/sparsamt/konstfullt), "
            "inte specifikt en njutningsmanniska. Tagen bort, 'njutningsmanniska' behallen "
            "(ordagrant SAOL-belagd)."
        ),
    ),
    1780080621139: dict(  # usurpera
        huvudbetydelse="Egenmäktigt ta sig makten eller rätten till något",
        register="formell, negativ",
        synonymer=[],
        synonym_groups=None,
        exempelmening='Generalen {} makten genom en blodig militärkupp.'.format(hl("usurperade")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. SO:s "
            "definition ar 'egenmaktigt ta sig ratten till' (aven med avseende pa "
            "egendom) -- inget krav pa vald eller olaglighet, bara att man tar sig "
            "ratten utan att ha den. Tog bort 'olagligt eller med vald' ur "
            "huvudbetydelsen. Exempelmeningen (kupp-scenario) ar fortfarande en "
            "giltig INSTANS av usurpation, bara inte den enda formen -- oforandrad. "
            "Register 'formell' matchar SO:s bruk-markering 'formellt'."
        ),
    ),
    1780080621270: dict(  # avhållen
        huvudbetydelse="Mycket omtyckt",
        register="neutral, positiv",
        synonymer=["omtyckt"],
        synonym_groups=None,
        exempelmening='Läraren var mycket {} bland eleverna.'.format(hl("avhållen")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. "
            "Verifierat i ravdata: SO/SAOL:s adjektiv 'avhallen' (bojning 'avhallet "
            "avhallna') har BARA betydelsen 'omtyckt'. Anordningen som minskar "
            "belastning vid firning hor till ett HELT ANNAT uppslagsord, "
            "substantivet 'avhall' (ordled 'av|hall', bojning 'avhallet; pl. avhall') "
            "-- de rakade bara dela sokresultat. Den felaktigt hopblandade andra "
            "betydelsen borttagen helt, kortet har nu en betydelse."
        ),
    ),
    1780080621055: dict(  # griljera
        huvudbetydelse="Snabbt bryna eller steka något panerat som redan är kokt eller stekt, till exempel i ugn",
        register="fackspråklig, neutral, matlagning",
        synonymer=["bryna"],
        synonym_groups=None,
        exempelmening='Hon {} julskinkan i ugnen tills ytan blev gyllenbrun.'.format(hl("griljerade")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. SO:s "
            "definition ar 'hastigt bereda (ett PANERAT, forut kokt eller stekt "
            "fodoamne) i ugn eller panna'. Paneringen (t.ex. med senap+strobrod) ar "
            "det som gor tekniken till just griljering och skiljer den fran vanlig "
            "bryning/gratinering -- lades till i huvudbetydelsen. Synonymen 'bryna' "
            "star som eget led i SAOL:s definition ('steka hastigt, bryna'), behallen."
        ),
    ),
    1780080621101: dict(  # primitiv
        huvudbetydelse=(
            "Enkel och outvecklad, oftast menat nedsättande ; ursprunglig och "
            "oförfinad, utan negativ värdering, till exempel om konst"
        ),
        register="neutral, lätt negativ",
        synonymer=["outvecklad", "enkel"],
        synonym_groups=None,
        exempelmening='Flyktinglägret bestod av {} tält utan rinnande vatten.'.format(hl("primitiva")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. SO "
            "listar en egen underbetydelse 'ibland med bibetydelse av "
            "ursprunglighet eller dylikt (med neutral el. positiv vardeladdning)', "
            "exemplet 'primitiv konst' -- skild fran huvudlasningen 'star pa lag "
            "utvecklingsniva'/'ytterst enkel och torftig' som kortet redan hade. "
            "Lade till nyansen som en andra betydelse. Registret star kvar som "
            "ETT tag (galler ledande/vanligaste betydelsen enligt style_guide.md, "
            "inte fler register an betydelser)."
        ),
    ),
    1780080621235: dict(  # svepande
        huvudbetydelse="Allmänt hållen och ofta missvisande eller orättvis, om till exempel ett uttalande",
        register="neutral, lätt negativ",
        synonymer=[],
        synonym_groups=None,
        exempelmening='Talaren gav bara en {} beskrivning av planerna, utan några konkreta detaljer.'.format(hl("svepande")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. "
            "Verifierat i ravdata: SO:s och SAOL:s ADJEKTIV 'svepande' (ordklass "
            "adjektiv) har BARA en betydelse, 'allmant hallen (och darfor ofta "
            "missvisande el. orattvis)'. 'Rora sig snabbt i en vid rorelse' hor "
            "till en HELT ANNAN post, VERBET 'svepa' (ordklass verb, skild "
            "SO/SAOL-artikel) -- inte en betydelse av adjektivet. Den pahittade "
            "rorelsebetydelsen borttagen. Aven registret rattat: 'vardaglig' "
            "kom fran verbets SAOL-bruk ('vardagligt'), inte adjektivets -- "
            "adjektivets egen SO-post saknar bruksmarkning (= neutral stilniva); "
            "valoren 'latt negativ' matchar SO:s egen 'ofta missvisande el. "
            "orattvis'."
        ),
    ),
    1780080621128: dict(  # alumn
        huvudbetydelse=(
            "En tidigare elev eller student vid en skola eller ett universitet ; "
            "en lärjunge eller skyddsling"
        ),
        register="högtidlig, neutral",
        synonymer=[],
        synonym_groups=None,
        exempelmening='Skolan bjöd in alla sina {} till 50-årsjubileet.'.format(hl("alumner")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. SO:s "
            "huvudbetydelse for alumn ar bredare, 'larjunge eller skyddsling' -- "
            "'tidigare elev eller student' star som en UNDERbetydelse markerad "
            "'numera sarsk.' (dagens vanligaste anvandning). Lade till den bredare "
            "grundbetydelsen som en andra betydelse, med den moderna "
            "studentbetydelsen forst eftersom SAOL bara ger den och SO:s egen "
            "markering sager att den ar dagens sarskilda/vanligaste anvandning."
        ),
    ),
    1780080621047: dict(  # antagonistisk
        huvudbetydelse=(
            "Som befinner sig i konflikt eller motsättning med något annat ; "
            "som verkar på motsatt sätt, till exempel om muskler eller läkemedel"
        ),
        register="formell, negativ",
        synonymer=[],
        synonym_groups=None,
        exempelmening='De två maktblocken hade en långvarigt {} relation.'.format(hl("antagonistisk")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. SO "
            "listar en andra, skild betydelse: 'som verkar pa motsatt satt (om "
            "muskel, lakemedel m.m.)', markerad 'spec. i medicinska sammanhang' -- "
            "en vanlig farmakologisk/fysiologisk term om motverkande (inte "
            "nodvandigtvis fientliga) krafter. Lade till som andra betydelse."
        ),
    ),
    1780080621154: dict(  # bastard
        huvudbetydelse=(
            "En avkomma av två olika djur- eller växtarter ; ett barn fött "
            "utanför äktenskapet"
        ),
        register="neutral, neutral ; ngt ålderdomlig, nedsättande",
        synonymer=["korsningsprodukt"],
        synonym_groups=None,
        exempelmening='Mulåsnan är en {} mellan häst och åsna.'.format(hl("bastard")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. "
            "SAOL bekraftar tva betydelser med OLIKA register: 'korsningsprodukt "
            "mellan tva vaxt- el. djurarter' (helt neutralt, ostamplat -- fortfarande "
            "i bruk inom biologi/avel) och 'utomaktenskapligt barn' (SAOL: 'ald., "
            "nedsatt.'). Kortet hade ETT gemensamt register for bada, vilket felaktigt "
            "stamplade hybrid-betydelsen som ålderdomlig/nedsattande. Registret delat "
            "per betydelse. Den inline-parentesen '(ald., neds.)' i sjalva "
            "huvudbetydelsen togs bort eftersom informationen nu star i "
            "registerfaltet istallet (dubblering)."
        ),
    ),
    1780080621051: dict(  # dröna
        huvudbetydelse="Vara passiv och lat, inte göra något",
        register="vardaglig, lätt negativ",
        synonymer=["söla", "vara lat"],
        synonym_groups=None,
        exempelmening='Han låg och {} i soffan hela söndagen i stället för att plugga.'.format(hl("drönade")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21 for synonymerna 'sola'/'dasa'. "
            "SAKKOLLAT MOT RAVDATA: granskarens anmarkning stammer inte fullt ut -- "
            "SAOL:s FAKTISKA definition av droma AR ordagrant 'sola, dasa, vara "
            "lat' (tre samordnade led, exakt samma monster som style_guide.md:s "
            "eget triumfera-exempel dar varje ord i en kommaseparerad "
            "SAOL/SO-definition raknas som belagd synonym). 'sola' och 'dasa' ar "
            "alltsa INTE obelagda. Andrade anda 'dasa' (halvsovande, fel nyans "
            "for 'passiv/lat') mot SAOL:s tredje led 'vara lat' -- battre matchning "
            "mot SO:s egna karndefinition 'fora en passiv tillvaro', fortfarande "
            "SAOL-ordagrant belagd. 'sola' behallen oforandrad."
        ),
    ),
    1780080621085: dict(  # entreprenör
        huvudbetydelse=(
            "Ett företag eller en person som åtar sig ett byggprojekt eller "
            "uppdrag ; en initiativrik person som startar och driver egna företag"
        ),
        register="fackspråklig, neutral ; neutral, positiv",
        synonymer=["företagare"],
        synonym_groups=None,
        exempelmening='Han är en driven {} som redan startat tre företag.'.format(hl("entreprenör")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. SO:s "
            "andra betydelse ar 'initiativkraftig och uppfinningsrik EGEN "
            "FORETAGARE' -- 'foretagare' ar sjalva karnsubstantivet i SO:s egen "
            "definition. Bytte ut 'initiativrik' (ett adjektiv, inte utbytbart "
            "mot substantivet entreprenor -- man kan inte saga 'en driven "
            "initiativrik') mot 'foretagare'."
        ),
    ),
    1780080621151: dict(  # foton
        huvudbetydelse="Den minsta enheten av elektromagnetisk strålning, en ljuspartikel",
        register="fackspråklig, neutral, fysik",
        synonymer=["ljuspartikel"],
        synonym_groups=None,
        exempelmening='En {} är energi utan massa som rör sig med ljusets hastighet.'.format(hl("foton")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. "
            "Verifierat i ravdata: 'foton' som EGET uppslagsord (SAOL id 21727, "
            "SO l_nr 154421, bojning 'fotonen fotoner') har BARA betydelsen "
            "ljuspartikel. 'fotografisk bild, fotografi' ar definitionen for ett "
            "HELT ANNAT uppslagsord, 'foto' (SAOL id 21668) -- vars OBESTAMD FORM "
            "PLURAL rakar vara 'foton' (bojningstabellen visar det svart pa vitt). "
            "'Foton' ar alltsa aldrig ett sjalvstandigt ord for ett enskilt "
            "fotografi, bara plural av 'foto'. Den pahittade andra betydelsen "
            "borttagen helt."
        ),
    ),
    1780080621142: dict(  # friktion
        huvudbetydelse=(
            "Motstånd mellan två ytor som gnids mot varandra ; slitningar eller "
            "konflikter mellan människor som samarbetar"
        ),
        register="fackspråklig, neutral, fysik ; neutral, negativ",
        synonymer=["gnidning"],
        synonym_groups=None,
        exempelmening='Det uppstod en del {} mellan de nya kollegorna under det första året.'.format(hl("friktion")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21 for synonymen 'gnidning'. "
            "SAKKOLLAT MOT RAVDATA, granskarens anmarkning ar FEL: SAOL:s "
            "FAKTISKA definition av friktion ar ordagrant 'gnidning; motstand i "
            "kontaktyta mellan kroppar vid gnidning el. forskjutning; slitningar "
            "vid samarbete' -- tre semikolon-atskilda led, dar 'gnidning' HELT "
            "ENSAMT inleder det forsta ledet. Exakt samma monster som "
            "style_guide.md:s eget triumfera-exempel ('segra; jubla ...', bada "
            "orden inleder sina led = belagda synonymer). 'gnidning' ar alltsa "
            "en SAOL-belagd synonym, inte en pahittad -- INGEN ANDRING gjord av "
            "kortets innehall, bara dokumenterat att den tidigare underkanningen "
            "var felaktig (samma monster som tidigare visade sig med 'schakt' och "
            "'brodtext', se CLAUDE.md 2026-08-12)."
        ),
    ),
    1780080621141: dict(  # förtjänt
        huvudbetydelse=(
            "Som har gjort sig värd något, till exempel beröm eller belöning ; "
            "väl meriterad genom långvarigt arbete"
        ),
        register="formell, positiv",
        synonymer=["värd", "väl meriterad"],
        synonym_groups=None,
        exempelmening='Efter allt hårt arbete var segern verkligen {}.'.format(hl("förtjänt")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. "
            "Verifierat: SO har TVA huvudbetydelser -- (1) '¹vard' (t.ex. 'gjort "
            "sig fortjant av en uppmuntran') och (2) 'val meriterad genom "
            "langvarigt arbete' (t.ex. 'en fortjant forskare'). Kortet hade bara "
            "(1). Lade till (2). Bytte ocksa exempelmeningen -- den gamla "
            "('fick ett pris for sin fortjanta insats') var tvetydig mellan "
            "bada betydelserna och matchade varken renodlat; den nya "
            "illustrerar entydigt betydelse (1), 'vard/formatd'."
        ),
    ),
    1780080621167: dict(  # giga
        huvudbetydelse="Ett medeltida stråkinstrument, en sorts fiol",
        register="arkaisk, neutral",
        synonymer=["fiol"],
        synonym_groups=None,
        exempelmening='Musikern spelade på en {} under medeltidsmarknaden.'.format(hl("giga")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. "
            "Verifierat i ravdata: SO/SAOL:s tredje homograf 'giga' = 'miljard "
            "(i vissa mattangivelser)' saknar helt bojningstabell (bunden form) "
            "och anvands ENDAST som FORLED i sammansattningar (gigabyte, "
            "gigaton, gigawatt) -- aldrig som ett fristaende ord for 'en "
            "miljard, sarskilt om pengar'. Det pastadda slangbruket om pengar "
            "gick inte att belagga nagonstans. Den pahittade andra betydelsen "
            "borttagen helt, kortet har nu en betydelse (instrumentet, SAOL-bruk "
            "'ald.')."
        ),
    ),
    1780080621050: dict(  # kamrer
        huvudbetydelse="En tjänsteman med ansvar för ekonomisk förvaltning och bokföring",
        register="formell, neutral",
        synonymer=[],
        synonym_groups=None,
        exempelmening='{} gick igenom företagets räkenskaper varje kvartal.'.format(hl("Kamrern")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21 for formfel. Verifierat: "
            "SO:s bojningsuppgift ar 'kamrern av. kamreren, plural kamrerer' -- "
            "'kamrerare' finns INTE i SO eller SAOL. Exempelmeningens "
            "'Kamreraren' rattat till 'Kamrern' (SO:s forsta/vanligaste "
            "bestamda form)."
        ),
    ),
    1780080621217: dict(  # kohort
        huvudbetydelse=(
            "En truppavdelning som var en del av en romersk legion, förr i "
            "tiden ; en grupp människor med gemensamma kännetecken, till "
            "exempel i en studie"
        ),
        register="arkaisk, neutral, historia ; fackspråklig, neutral, medicin",
        synonymer=["truppavdelning", "grupp"],
        synonym_groups=[["truppavdelning"], ["grupp"]],
        exempelmening='Forskarna följde en {} av 500 patienter under tio år.'.format(hl("kohort")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21 for registerfel. Verifierat: "
            "SO markerar betydelse 1 (romersk truppavdelning) 'historiskt' men "
            "betydelse 2 (t.ex. kohortstudie) 'sarsk. medicin och sociologi' -- "
            "en LEVANDE, aktivt anvand facktermin, inte ålderdomlig. Registret "
            "delat per betydelse (samma monster som induktion/kartell). Domanen "
            "'medicin' anvand for betydelse 2 -- 'sociologi' finns inte i "
            "projektets lasta REGISTER_DOMAN-vokabular, 'medicin' ar narmaste "
            "godkanda tagg och tacker sjalva HP-relevanta anvandningen "
            "(kohortstudie)."
        ),
    ),
    1780080621175: dict(  # libell
        huvudbetydelse=(
            "Ett litet instrument (rör) med en vätskebubbla som används för "
            "att avgöra om något är rakt eller i våg ; en smädeskrift "
            "(ålderdomligt)"
        ),
        register="fackspråklig, neutral, teknik",
        synonymer=[],
        synonym_groups=None,
        exempelmening='Han la {} mot bordsskivan för att kontrollera att den var helt plan.'.format(hl("libellen")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. "
            "SO:s definition ar 'matverktyg for bestamning av lutning och "
            "vinklar, anv. i vagar och vattenpass' -- INTE 'en liten bubbla i "
            "vatska' (kortets egen exempelmening, 'la libellen mot "
            "bordsskivan', motsagde redan den gamla definitionen: man lagger "
            "ett INSTRUMENT mot en yta, inte en bubbla). Huvudbetydelsen "
            "rattad till instrumentet enligt granskarens foreslagna formulering. "
            "Andra betydelsen ('smadeskrift') gick inte att belagga i SO/SAOL "
            "(0 traffar dar) men SAOB har tva egna homografer for 'libell' "
            "(homograf 1 och 2) och Wiktionary bekraftar 'flygskrift, "
            "smadesskrift' som en skild, aldre betydelse -- behallen men "
            "markerad tydligt ålderdomlig eftersom den bara star i historiska "
            "kallor."
        ),
    ),
    1780080621081: dict(  # marig
        huvudbetydelse=(
            "Tovig och förkrympt (mindre bruklig, till exempel om hår eller "
            "växtlighet) ; som orsakar svårigheter, besvärlig"
        ),
        register="ngt ålderdomlig, neutral",
        synonymer=["besvärlig"],
        synonym_groups=None,
        exempelmening='Den sista uppgiften på provet var riktigt {}.'.format(hl("marig")),
        etymologi=None,
        slutsats=(
            "UNDERKAND av blind granskare 2026-08-21, OMSKRIVET efter sokkoll. "
            "SO ger tva betydelser: (1) 'tovig och forkrympt' (markerad "
            "'mindre brukligt', belagt sedan 1752) och (2) 'som orsakar "
            "svarigheter eller fortretligheter' (vardagligt, belagt 1911). "
            "Kortet hade bara (2). Lade till (1) forst, i kronologisk/SO-ordning. "
            "Register andrat till att galla ledande (nu forsta) betydelsen: "
            "'ngt alderdomlig' matchar SO:s 'mindre brukligt' battre an det "
            "tidigare 'vardaglig', som bara stammer for betydelse (2)."
        ),
    ),
}


def main():
    d = json.load(open(PATH, encoding="utf-8"))
    by_id = {e["noteId"]: e for e in d}
    missing = set(FIXES) - set(by_id)
    if missing:
        raise SystemExit(f"Saknade noteIds: {missing}")

    for note_id, fix in FIXES.items():
        e = by_id[note_id]
        e["sokkoll"] = {"kalla": kalla(e["ord"]), "slutsats": fix["slutsats"]}
        e["proposed"] = {
            "huvudbetydelse": fix["huvudbetydelse"],
            "register": fix["register"],
            "synonymer": fix["synonymer"],
            "synonym_groups": fix["synonym_groups"],
            "exempelmening": fix["exempelmening"],
        }
        if fix.get("etymologi"):
            e["proposed"]["etymologi"] = fix["etymologi"]
        e["approved"] = True
        # Reset stale post-applicera bookkeeping so applicera reprocesses cleanly.
        e["applicerad"] = False
        e.pop("adamtal_varningar", None)
        e.pop("exempel_varningar", None)
        e.pop("skriven_av", None)

    json.dump(d, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("OK, rattade", len(FIXES), "kort i", PATH)


if __name__ == "__main__":
    main()
