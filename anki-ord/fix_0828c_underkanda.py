# -*- coding: utf-8 -*-
"""Rattar de 9 underkanda korten ur v3-batch100.

Blindgranskningen delade sig i tre lika stora hogar om tre kort var:

  FOR BRETT   anlopa, autograf, eklatera -- betydelser tillagda ur en svag
              kalla (Wiktionary) eller vidgade utover vad SO/SAOL bar.
  FOR SMALT   harnesk, ax, yttring -- betydelser som STAR i ordbockerna men
              som slogs ihop eller hoppades over.
  SYNONYM     bemarkt, singular, spe -- ord hamtade ur SAOL:s definitionstext
              som visade sig vara forklaringar, inte utbytbara ord.

Den tredje hogen ar den viktigaste. Regeln som skarptes 2026-08-28 -- "bara
ord ur SO:s eller SAOL:s definitionstext, eller markta SYN:synonym, far bli
synonymer" -- rackte inte. En ordboksglosa ar ofta en FORKLARING: SAOL
glossar bemarkt med 'framstaende', men man kan vara framstaende utan att
vara bemarkt. Samma sak med singular/saregen och spe/gyckel. Skarpningen:
ett ord ur definitionstexten duger bara om det ar utbytbart at BADA hallen.
"""
import io
import json

FIL = "sessions/session_2026-08-28_v3-batch100.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}


def ratta(ord_, bet=None, reg=None, syn=None, not_=None, conf=None):
    e = BY[ord_]
    p = e["proposed"]
    if bet is not None:
        p["huvudbetydelse"] = bet
    if reg is not None:
        p["register"] = reg
    if syn is not None:
        p["synonymer"] = syn
    if conf is not None:
        e["confidence"] = conf
    if not_:
        e["sokkoll"]["slutsats"] += " " + not_
    assert len(p["huvudbetydelse"].split(" ; ")) == \
        len(p["register"].split(" ; ")), ord_


# ---------------------------------------------------------- FOR SMALT
ratta("harnesk",
      bet="Den del av en rustning som skyddar bröstet och överkroppen ; i "
          "uttrycket ”gå i harnesk mot”: bli stridslysten och helt "
          "avvisande mot något ; i vävning: mekanismen som lyfter trådarna i "
          "en vävstol ; i geologin: en blankslipad yta i berget där två "
          "block glidit mot varandra",
      reg="arkaisk, neutral, historia ; neutral, neutral, allmän ; "
          "fackspråklig, neutral, allmän ; fackspråklig, neutral, geologi",
      not_="RATTAT efter blindgranskning: SAOL ger TRE betydelser -- "
           "rustningsdelen, den geologiska glidytan OCH 'draginrattning for "
           "solv', den vavtekniska. Den tredje saknades helt och ar nu "
           "tillagd, utskriven som 'mekanismen som lyfter tradarna i en "
           "vavstol' eftersom 'solv' ar lika svart som uppslagsordet. "
           "Granskaren ville dessutom STRYKA idiomet 'ga i harnesk mot' med "
           "motiveringen att det bara ar ett uttryck byggt pa "
           "rustningsbetydelsen. Det ar behallet: SO listar det som en egen "
           "underbetydelse med egen exempelmening, och det ar i praktiken "
           "den enda anvandning ordet har i dag. Kortet har darfor fyra "
           "betydelser, inte tre.")

ratta("ax",
      bet="Toppen på ett sädesstrå, där kornen sitter tätt samlade ; hos "
          "växter i allmänhet: en blomsamling där blommorna sitter utan "
          "skaft direkt på en lång stjälk ; den utskjutande delen av en "
          "nyckel som griper in i låset ; vardagligt: acceleration hos ett "
          "fordon",
      reg="neutral, neutral, allmän ; fackspråklig, neutral, biologi ; "
          "neutral, neutral, teknik ; vardaglig, neutral, allmän",
      not_="RATTAT efter blindgranskning: jag slog medvetet ihop SO:s "
           "botaniska definition ('blomstallning med oskaftade blommor pa "
           "lang huvudaxel') med sadesaxet och skrev ut att jag gjorde det. "
           "Granskaren underkande hopslagningen, och har ratt: ett ax hos "
           "groblad eller orkideer ar ingen sad, sa den allmanna botaniska "
           "betydelsen ar vidare an sadesaxet och inte samma sak. Den ar nu "
           "en egen betydelse.")

ratta("yttring",
      bet="Ett uttalande där någon uttryckligen förklarar sin vilja eller "
          "åsikt ; något som visar sig utåt och avslöjar vad som pågår under "
          "ytan ; inom medicinen: ett symtom",
      reg="neutral, neutral, allmän ; neutral, neutral, allmän ; "
          "fackspråklig, neutral, medicin",
      not_="RATTAT efter blindgranskning: samma fel som pa ax -- jag slog "
           "ihop SO:s 'tillkannagivande' med 'uttryck for bakomliggande "
           "tillstand' och kallade dem samma sak i olika styrka. De ar "
           "motsatser i riktning: en viljeyttring ar AKTIV och avsiktlig, en "
           "yttring av rasism ar ett INDIREKT tecken som rojer nagot den som "
           "visar det kanske inte ville visa. Bada ar nu med. Paketet "
           "flaggade dessutom kortet med facit_signal (facit antydde fler "
           "betydelser an kortet hade) -- den flaggan pekade ratt och jag "
           "gick forbi den.")

# ---------------------------------------------------------- FOR BRETT
ratta("anlöpa",
      bet="Om fartyg: gå in i en hamn och lägga till för ett kortare "
          "uppehåll",
      reg="fackspråklig, neutral, sjöfart",
      conf=9,
      not_="RATTAT efter blindgranskning: metallbetydelsen ('morkna eller fa "
           "en hinna pa ytan') ar STRUKEN. Jag tog den ur Wiktionary och "
           "markte kortet conf=7 for att den bara hade en kalla -- men "
           "granskaren pekar ut varfor den kallan ar opalitlig just har: "
           "tyskans anlaufen har BADA betydelserna, svenskans anlopa bara "
           "sjofartsbetydelsen, och Wiktionary-artikeln ser ut att ha arvt "
           "den tyska. Att markera ett tveksamt pastaende med lag "
           "confidence ar inte samma sak som att lata bli att skriva det.")

ratta("autograf",
      bet="Namnteckning som en känd person skrivit för hand åt en beundrare",
      reg="neutral, neutral, allmän",
      not_="RATTAT efter blindgranskning: den andra betydelsen ('ocksa om "
           "annat som nagon skrivit med egen hand') ar STRUKEN. Den kom fran "
           "Wiktionary ensam; bade SO och SAOL ger bara namnteckningen. "
           "Samma fel som pa anlopa, i samma batch: en betydelse som bara "
           "Wiktionary har ar en hypotes, inte ett belagg.")

ratta("eklatera",
      bet="Offentligt berätta att man har förlovat sig",
      syn=[],
      not_="RATTAT efter blindgranskning: facit ar avsmalnat. SO:s "
           "definition ar visserligen bara 'tillkannage', utan begransning, "
           "men SAOL sager uttryckligen 'offentliggora forlovning', och det "
           "ar den enda anvandning ordet faktiskt har. Min formulering "
           "'nagot som varit privat, framfor allt en forlovning' antydde en "
           "bredare anvandning som inget belagg stoder. Synonymerna "
           "(tillkannage, offentliggora) ar ocksa strukna: de ar bredare an "
           "eklatera och alltsa inte utbytbara.")

# ---------------------------------------------------------- SYNONYMFELET
ratta("bemärkt",
      syn=[],
      not_="RATTAT efter blindgranskning -- OCH DET HAR AR BATCHENS "
           "VIKTIGASTE FEL. Synonymerna framstaende och uppmarksammad togs "
           "ur SAOL:s definitionstext, alltsa enligt den regel jag skarpte "
           "sa sent som igar ('bara definitionstext eller SYN:synonym "
           "duger'). Granskarens invandning ar semantisk och traffar mitt i: "
           "framstaende betyder duktig, bemarkt betyder kand -- MAN KAN VARA "
           "FRAMSTAENDE UTAN ATT VARA BEMARKT. En ordboksglosa ar ofta en "
           "forklaring, inte ett utbytbart ord. Regeln maste alltsa skarpas "
           "ett steg till: ett ord ur definitionstexten duger bara om det ar "
           "utbytbart at BADA hallen.")

ratta("singulär",
      bet="Ensam i sitt slag: något som bara inträffat en enda gång och "
          "saknar motstycke",
      syn=[],
      not_="RATTAT efter blindgranskning: synonymen saregen ar STRUKEN, och "
           "huvudbetydelsen ar stramad. Sareget betyder 'avvikande, "
           "egenartat' -- det handlar om ett paffallande DRAG, medan "
           "singulart handlar om att vara ensam i sitt slag. Nagot kan vara "
           "sareget utan att vara singulart. Mitt tillagg 'inte liknar nagot "
           "annat' tanjde dessutom definitionen at saregenhallet for att "
           "motivera synonymen -- alltsa lat jag synonymen styra facit i "
           "stallet for tvartom. Samma glosfel som pa bemarkt.")

ratta("spe",
      syn=["hån"],
      not_="RATTAT efter blindgranskning: synonymen gyckel ar STRUKEN, han "
           "ar kvar. Gyckel ar skamt och retande och kan vara godmodigt; spe "
           "innebar alltid forakt. Granskaren noterar att det ar precis den "
           "sortens narsynonym HP-provet bygger sina distraktorer av. Tredje "
           "fallet av samma glosfel i samma batch (se bemarkt).")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False,
          indent=1)
print("rattade 9 underkanda kort")
