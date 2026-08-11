"""Parse/bygg Baksida-fältets HTML-mikroformat (se config.py för formatspec,
"Kortformat v2", beslutat 2026-08-04, korrigerat 2026-08-04 efter Adams
feedback: inga fältetiketter ("Huvudbetydelse:" osv) skrivs ut alls. ENDAST
huvudbetydelsens värde ska vara fet — inget annat. Register ska ha temats
standardfärg (vit i nattläge), inte en hårdkodad grå ton.

Exempel på ett fält:
  <b>vara mycket trött</b><br>
  (vardaglig)<br>
  <br>
  <font color="#3498db">utmattad, dödstrött</font><br>
  <br>
  <i>Han var helt <font color="#3498db">slut</font> efter passet.</i>
  <br><br>Av grekiskans aisthesis, "sinnesintryck".                          (valfri etymologi)
  <br><br><img src="bild.jpg" style="max-width:400px; border-radius:4px;">   (valfritt, sist)

Etymologi (tillagt 2026-08-08 på Adams begäran): valfri rad EFTER
exempelmeningen, med samma `<br><br>`-lucka som mellan de andra blocken,
och FÖRE bilden. Ren text -- ingen fet stil (bara huvudbetydelsen är fet),
ingen egen färg (samma regel som registerraden). Tas bara med när
ursprunget faktiskt gör betydelsen lättare att förstå eller minnas, aldrig
som trivia: kortet ska bli tydligare, inte längre.

Flera betydelser (beslutat 2026-08-05, se style_guide.md "Register per
bibetydelse"): om betydelse 2+ har ETT ANNAT register än betydelse 1,
skrivs BÅDA registren på SAMMA rad, andra registret indraget med &nbsp;
till ungefär under sin betydelses startpunkt i Huvudbetydelse-raden ovanför:
  <b>En våg eller krökning i hår eller ull ; att fjäska och smickra någon underdånigt</b><br>
  (dialektal)                              (vardaglig, negativ)<br>
  <br>
  ...
register-parametern till build() är då " ; "-separerad, en del per
betydelse — build() räknar ut indraget automatiskt utifrån
huvudbetydelsens textlängd (tecken-baserad approximation, inte
pixelperfekt eftersom fetstil inte är monospace).

parse()/build() nedan hanterar detta v2-format. parse_legacy()/build_legacy()
hanterar det gamla formatet (blå synonymrad + <ol><li>-definitioner) och
finns kvar bara för att migrera redan skrivna kort — skriv aldrig nytt
innehåll med dem.
"""

import re

import config

_MAIN_RE = re.compile(
    r"<b>(?P<huvud>.*?)</b>\s*<br>"
    r"(?P<register_block>(?:(?:&nbsp;)*\([^)]*\))*\s*<br>\s*)?"
    r"\s*<br>\s*"
    rf'<font color="{re.escape(config.SYNONYM_COLOR)}">(?P<syn>.*?)</font>\s*<br>'
    r"\s*<br>\s*"
    r"<i>(?P<ex>.*?)</i>",
    re.DOTALL,
)
_REGISTER_LINE_RE = re.compile(r"\(([^)]*)\)")
# Ett eller flera <br> före <img>, inte exakt två: build() skriver alltid
# <br><br>, men äldre/handredigerade kort kan ha ett enda <br> (hittat
# 2026-08-07 på "faun"). Med det gamla, strikta mönstret returnerade
# parse() bild_html=None för sådana kort, och nästa parse->build RADERADE
# bilden tyst -- t.ex. i restore_images_from_old_deck.py eller vilken
# innehållsfix som helst som bygger om kortet.
_IMG_TAIL_RE = re.compile(r"((?:<br>\s*)+<img.*)$", re.DOTALL)
# Fet bokstav är bredare än ett &nbsp;-mellanslag, så en ren teckenräkning
# hamnar för långt till vänster (upptäckt 2026-08-05, Adam: registret för
# betydelse 2 landade mitt i ; -gränsen istället för till höger om den).
# Skala upp offseten för att kompensera — justera denna konstant om
# indraget fortfarande sitter fel.
_REGISTER_INDENT_SCALE = 1.5
# Etymologiraden lagras som ren text men RENDERAS grå med pil (2026-08-10).
# De två mönstren tar av wrappern respektive pilen vid parse, så att
# parse->build är idempotent. Färgen matchas löst (vilken hex som helst) för
# att kort skrivna med en äldre färgkonstant fortfarande ska gå att läsa
# tillbaka i stället för att tolkas som etymologitext med HTML i sig.
_ETY_UNWRAP_RE = re.compile(r'^<font color="#[0-9a-fA-F]{3,6}">(.*)</font>$', re.DOTALL)
_ETY_AVSKALNING_RE = re.compile(r"^\s*(?:→|->|&rarr;)\s*")


def parse(baksida_html):
    match = _MAIN_RE.search(baksida_html)
    if not match:
        return {
            "huvudbetydelse": "",
            "register": None,
            "synonymer": [],
            "exempelmening": "",
            "etymologi": None,
            "bild_html": None,
            "synonym_groups": None,
        }

    huvudbetydelse = match.group("huvud").strip()
    register_lines = [r.strip() for r in _REGISTER_LINE_RE.findall(match.group("register_block") or "")]
    register = " ; ".join(register_lines) if register_lines else None

    raw = match.group("syn")
    synonym_groups = None
    if ";" in raw:
        synonym_groups = [[s.strip() for s in g.split(",")] for g in raw.split(";")]
        synonymer = [s for g in synonym_groups for s in g]
    else:
        synonymer = [s.strip() for s in raw.split(",") if s.strip()]

    exempelmening = match.group("ex").strip()

    img_match = _IMG_TAIL_RE.search(baksida_html)
    bild_html = img_match.group(1).strip() if img_match else None

    # Allt mellan exempelmeningen och bilden (eller slutet) är etymologin.
    # Den läses ur SVANSEN istället för via _MAIN_RE, så att kort utan
    # etymologi -- alltså varje kort skrivet före 2026-08-08 -- parsas
    # exakt som förut och en parse->build-runda inte ändrar dem.
    svans = baksida_html[match.end():]
    img_i_svans = _IMG_TAIL_RE.search(svans)
    if img_i_svans:
        svans = svans[:img_i_svans.start()]
    etymologi = re.sub(r"^(?:\s*<br>\s*)+", "", svans).strip() or None
    if etymologi:
        # Skala av grå-wrappern och pilen så att modellen bär REN TEXT.
        # Utan detta skulle nästa build() kapsla in en redan färgad rad i en
        # ny <font> och skriva ut "→ → ..." -- samma tysta dubblering som
        # bilden drabbades av 2026-08-07. Kort skrivna FÖRE 2026-08-10 saknar
        # wrappern och passerar oförändrade, vilket är avsikten.
        etymologi = _ETY_UNWRAP_RE.sub(r"\1", etymologi).strip()
        etymologi = _ETY_AVSKALNING_RE.sub("", etymologi).strip() or None

    return {
        "huvudbetydelse": huvudbetydelse,
        "register": register,
        "synonymer": synonymer,
        "exempelmening": exempelmening,
        "etymologi": etymologi,
        "bild_html": bild_html,
        "synonym_groups": synonym_groups,
    }


def build(huvudbetydelse, synonymer=None, exempelmening="", register=None, bild_html=None, synonym_groups=None, etymologi=None):
    """register: sträng typ "formell" / "lätt negativ" / "formell, lätt negativ".
    Obligatoriskt i praktiken (style_guide.md, beslutat 2026-08-04) — minst en
    tagg på varje kort, None bara accepteras här på kodnivå för flexibilitet.

    huvudbetydelse-separatorer (ändrat 2026-08-05, se style_guide.md):
    ` ; ` = faktiskt skilda betydelser, ` / ` = omformuleringar av samma
    betydelse. Fritext, kollas inte av denna funktion."""
    if huvudbetydelse:
        huvudbetydelse = huvudbetydelse[0].upper() + huvudbetydelse[1:]
    huvud_html = f"<b>{huvudbetydelse}</b><br>"

    if register:
        reg_parts = [r.strip() for r in register.split(";")]
        if len(reg_parts) > 1:
            # Flera betydelser med olika register (beslutat 2026-08-05, se
            # style_guide.md "Register per bibetydelse"): en rad, varje
            # register indraget till ungefär under SIN betydelses startpunkt
            # i Huvudbetydelse-raden ovanför. Tecken-baserad approximation
            # (fetstil är inte monospace, blir aldrig pixelperfekt) — bra
            # nog för att visuellt koppla ihop rätt register med rätt
            # betydelse.
            meanings = huvudbetydelse.split(" ; ")
            offsets = []
            pos = 0
            for m in meanings:
                offsets.append(pos)
                pos += len(m) + len(" ; ")
            pieces = []
            cursor = 0
            for i, part in enumerate(reg_parts):
                raw_offset = offsets[i] if i < len(offsets) else cursor
                offset = round(raw_offset * _REGISTER_INDENT_SCALE)
                pad = max(1, offset - cursor) if i > 0 else 0
                piece = f"{'&nbsp;' * pad}({part})"
                pieces.append(piece)
                cursor += pad + len(f"({part})")
            register_html = "".join(pieces) + "<br>"
        else:
            register_html = f"({reg_parts[0]})<br>"
    else:
        register_html = ""

    if synonym_groups:
        synonym_text = " ; ".join(", ".join(g) for g in synonym_groups)
    else:
        synonym_text = ", ".join(synonymer or [])
    synonym_html = f'<font color="{config.SYNONYM_COLOR}">{synonym_text}</font><br>'

    example_html = f"<i>{exempelmening}</i>"

    parts = [huvud_html, register_html, "<br>", synonym_html, "<br>", example_html]
    # Samma <br><br>-lucka som mellan de övriga blocken, och alltid FÖRE
    # bilden (Adams krav 2026-08-08). bild_html bär redan sina egna <br>.
    if etymologi:
        # Grå rad med inledande pil (Adams val 2026-08-10, se config.py för
        # varför). Etymologin LAGRAS som ren text -- pilen och färgen läggs på
        # här och plockas av igen i parse(), så att en parse->build-runda ger
        # exakt samma HTML tillbaka och inte kapslar in färgen två gånger.
        ety = _ETY_AVSKALNING_RE.sub("", etymologi.strip()).strip()
        parts.append(f'<br><br><font color="{config.ETYMOLOGI_COLOR}">'
                     f'{config.ETYMOLOGI_PIL} {ety}</font>')
    if bild_html:
        parts.append(bild_html)
    return "".join(parts)


# --- Adam-tal-validering (tillagt 2026-08-07) ---
#
# style_guide.md är prosa som granskaren ska minnas, och lint_adamtal.py
# körs i EFTERHAND. Det är samma lucka som registret hade innan
# apply_flerbetydelse.apply_card() gjorde det till en hård spärr -- och
# registret hamnade fel på 37 av 50 kort just för att kontrollen fanns
# men var frivillig. Reglerna nedan flyttas därför in i SKRIVVÄGEN.
#
# HÅRDA regler blockerar skrivning. De är valda för att de i praktiken
# saknar falsklarm -- uppmätt på hela decket 2026-08-07, se CLAUDE.md
# "Adam-tal-lint": varje kategori nedan gav 0 falsklarm på 3229 kort.
#
# MJUKA regler returneras som varningar och blockerar ALDRIG. De har
# kända legitima undantag: "anafor" MÅSTE ha flera meningar (kortet
# illustrerar stilfiguren genom att upprepa satsinledningen), och
# ordräkning är en dålig proxy för både "fragment" och "ordbokslängd".
# Att göra dem hårda hade tvingat fram sämre kort.

ADAMTAL_HARDA = (
    "tom_exempelmening", "saknar_highlight", "avslutande_skiljetecken_hb",
    "semikolon_utan_mellanslag", "formatering_i_hb", "html_skrap",
    "tom_synonym", "tom_synonymgrupp", "grupper_matchar_ej_betydelser",
    "fler_register_an_betydelser",
)
ADAMTAL_MJUKA = (
    "flera_meningar", "fragment_exempel", "ordbokslangd_hb",
    "cirkular_definition", "cirkular_synonym", "osymmetriska_grupper",
    "etymologi_langd",
)

# Etymologin är valfri och ska bara finnas när ursprunget gör betydelsen
# lättare att FÖRSTÅ. Längd är den enda delen som går att mäta -- om den
# ordet spräcker taket har den nästan alltid glidit över i språkhistorisk
# trivia, vilket är precis vad Adam-tal säger nej till. Mjuk regel: den
# blockerar inte, för enstaka ord kräver en längre förklaring.
ETYMOLOGI_MAX_ORD = 18

_ABBR = ["t.ex.", "bl.a.", "m.fl.", "d.v.s.", "dvs.", "osv.", "m.m.",
         "fr.o.m.", "t.o.m.", "ca.", "kl.", "s.k.", "e.Kr.", "f.Kr."]
_HTML_SKRAP = ("<span", "<div", "<ol", "<li", "&amp;nbsp;", "&quot;", "rgb(52,")


def _strip_html(s):
    if not s:
        return ""
    return re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ").strip()


def betydelser(huvudbetydelse):
    """Delar Huvudbetydelse på den överenskomna ` ; `-separatorn."""
    return [m.strip() for m in re.split(r"\s;\s", huvudbetydelse or "") if m.strip()]


def _rakna_meningar(text):
    for a in _ABBR:
        text = text.replace(a, "@" * len(a))
    return len(re.findall(r"[.!?]+(?=\s|$)", text))


def _stam(word):
    """Grov svensk stam, bara för substrängjämförelser -- inte morfologi."""
    w = (word or "").lower().strip()
    for suf in ("ande", "ende", "arna", "erna", "orna", "aren", "ade", "are",
                "ell", "en", "et", "er", "or", "ar", "an", "a", "s"):
        if len(w) - len(suf) >= 4 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def validate_adamtal(huvudbetydelse, synonymer=None, synonym_groups=None,
                     exempelmening="", register=None, ord_=None, tillat=(),
                     etymologi=None):
    """Kontrollerar det i style_guide.md som går att avgöra mekaniskt.

    Returnerar (fel, varningar) -- två listor med "regel: förklaring".
    `fel` ska blockera skrivning, `varningar` ska visas men aldrig blockera.

    `tillat` är en lista med regelnamn som medvetet får brytas (t.ex.
    `tillat=["flera_meningar"]` för anafor-kortet). Använd den hellre än
    att göra en regel mjuk -- undantaget syns då i sessionsfilen.
    """
    fel, varn = [], []

    def lagg(regel, text):
        if regel in tillat:
            return
        (fel if regel in ADAMTAL_HARDA else varn).append(f"{regel}: {text}")

    hb = (huvudbetydelse or "").strip()
    ms = betydelser(hb)
    ex_raw = exempelmening or ""
    ex = _strip_html(ex_raw)
    syns = synonymer or []

    # --- Huvudbetydelse ---
    if hb.rstrip().endswith((".", ",")) and not hb.rstrip().endswith("..."):
        lagg("avslutande_skiljetecken_hb", f"Huvudbetydelse slutar med skiljetecken: ...{hb[-30:]!r}")
    if "<b>" in hb or "<font" in hb or "<i>" in hb:
        lagg("formatering_i_hb", "Huvudbetydelse ska vara ren text, ingen HTML")
    if ";" in hb and not re.search(r"\s;\s", hb):
        lagg("semikolon_utan_mellanslag",
             "använd ' ; ' med mellanslag mellan skilda betydelser -- "
             "ett bart ';' är osynligt för register-indragningen och alla svepningar")
    for m in ms:
        if len(m.split()) > 12:
            lagg("ordbokslangd_hb", f"{len(m.split())} ord i en betydelse -- korta ner: {m[:50]!r}")
    if ord_ and " " not in ord_.strip():
        st = _stam(ord_)
        if len(st) >= 4 and re.search(rf"\w*{re.escape(st)}\w*", hb.lower()):
            lagg("cirkular_definition", f"{ord_!r} tycks förklaras med sig självt")

    # --- Exempelmening ---
    if not ex:
        lagg("tom_exempelmening", "exempelmening saknas")
    else:
        if config.SYNONYM_COLOR not in ex_raw:
            lagg("saknar_highlight",
                 f'ordet måste märkas <font color="{config.SYNONYM_COLOR}">...</font> -- inte valfritt')
        n = _rakna_meningar(ex)
        if n > 1:
            lagg("flera_meningar", f"{n} meningar -- en per kort (tillat=['flera_meningar'] om motiverat)")
        if len(ex.split()) < 4:
            lagg("fragment_exempel", f"mycket kort, kontrollera att det är en hel mening: {ex!r}")

    # --- Synonymer ---
    for s in syns:
        if not (s or "").strip():
            lagg("tom_synonym", "tom sträng i synonymlistan")
        elif ord_ and " " not in ord_.strip():
            st = _stam(ord_)
            if len(st) >= 4 and st in s.lower().replace(" ", ""):
                lagg("cirkular_synonym", f"{s!r} innehåller uppslagsordet -- avslöjar svaret")
    if synonym_groups:
        if any(not [x for x in g if (x or "").strip()] for g in synonym_groups):
            lagg("tom_synonymgrupp", "tom grupp ger ett '; '-artefakt på kortet")
        if len(synonym_groups) != len(ms):
            lagg("grupper_matchar_ej_betydelser",
                 f"{len(synonym_groups)} synonymgrupper mot {len(ms)} betydelser")
        storlekar = [len([x for x in g if (x or "").strip()]) for g in synonym_groups]
        if storlekar and max(storlekar) - min(storlekar) >= 2:
            lagg("osymmetriska_grupper", f"gruppstorlekar {storlekar} -- sikta symmetriskt")

    # --- Register ---
    if register:
        nreg = len([r for r in register.split(";") if r.strip()])
        if nreg > len(ms):
            lagg("fler_register_an_betydelser", f"{nreg} register mot {len(ms)} betydelser")

    # --- Etymologi (valfri, tillagd 2026-08-08) ---
    ety_raw = etymologi or ""
    ety = _strip_html(ety_raw)
    if ety and len(ety.split()) > ETYMOLOGI_MAX_ORD:
        lagg("etymologi_langd",
             f"{len(ety.split())} ord -- etymologin ska förklara betydelsen, "
             f"inte berätta ordets historia: {ety[:60]!r}")

    # --- Kvarglömd HTML var som helst ---
    hittad = [j for j in _HTML_SKRAP if j in ex_raw or j in hb or j in ety_raw]
    if hittad:
        lagg("html_skrap", "kvarglömd HTML: " + ", ".join(repr(j) for j in hittad))

    return fel, varn


def validate_register(register):
    """Returnerar lista med varningssträngar (tom = ok). Kollar mot den låsta
    vokabulären i config.py — kraschar inte, bara ett granskningshjälpmedel.
    Register är obligatoriskt och båda axlarna (formalitet+valör) krävs,
    beslutat 2026-08-04 (skärpt från "minst en av dem").

    Stöder flera betydelser (beslutat 2026-08-05): register kan innehålla
    ` ; `-separerade delar, en per betydelse som har ETT EGET register
    (bara betydelser 2+ vars register skiljer sig behöver anges, se
    style_guide.md "Register per bibetydelse") — varje del valideras var
    för sig mot samma vokabulär/max-en-per-axel-regel."""
    if not register:
        return ['register saknas helt — obligatoriskt, se style_guide.md']

    warnings = []
    for part in register.split(";"):
        part = part.strip()
        tags = [t.strip() for t in part.split(",")]

        # Axeltilldelning kan INTE göras på medlemskap ensamt sedan 2026-08-10,
        # eftersom `neutral` och `oklart` medvetet finns på flera axlar. Första
        # versionen räknade dem mot varje axel de förekom i och larmade därför
        # på `neutral, neutral` (marinera) -- det korrekta svaret för ett
        # vanligt ord utan laddning. Regeln nedan är i stället:
        #
        #   entydig tagg  -> sin egen axel
        #   tvetydig tagg -> första ÄNNU LEDIGA axeln, i ordningen
        #                    stilnivå -> valör -> domän
        #
        # Det gör valideringen ordningstolerant: "neutral, starkt nedsättande"
        # och "formell, neutral, juridik" tilldelas båda rätt utan att skribenten
        # behöver minnas en fältordning.
        AXLAR = [("stilnivå", config.REGISTER_FORMALITY),
                 ("valör", config.REGISTER_VALENS),
                 ("domän", config.REGISTER_DOMAN)]
        kand = set().union(*(set(v) for _, v in AXLAR))
        warnings += [
            f'okänd register-tagg "{tag}", inte i config.REGISTER_FORMALITY/'
            f'REGISTER_VALENS/REGISTER_DOMAN'
            for tag in tags if tag not in kand
        ]

        upptagen = {}
        tvetydiga = []
        for t in tags:
            traffar = [namn for namn, v in AXLAR if t in v]
            if len(traffar) == 1:
                axel = traffar[0]
                if axel in upptagen:
                    warnings.append(
                        f'flera {axel}-taggar i "{part}", max en per axel')
                upptagen[axel] = t
            elif len(traffar) > 1:
                tvetydiga.append(t)
        for t in tvetydiga:
            ledig = next((namn for namn, _ in AXLAR if namn not in upptagen), None)
            if ledig is None:
                warnings.append(
                    f'"{t}" i "{part}" får ingen ledig axel — alla tre är tagna')
            else:
                upptagen[ledig] = t

        # KRAVET PÅ BÅDA AXLARNA (implementerat 2026-08-11).
        #
        # Docstringen ovan har sedan 2026-08-04 sagt att stilnivå OCH valör
        # båda krävs ("skärpt från 'minst en av dem'"). Koden kontrollerade
        # det aldrig. Följden mättes 2026-08-11 på 70 repetitionskort: 17 hade
        # fel eller ofullständigt register, och `arkaisk` ensamt, `negativ`
        # ensamt och till och med `juridik` ensamt passerade valideringen utan
        # en enda varning -- det sista alltså ett kort med enbart fackområde
        # och inget register alls.
        #
        # Varför det spelar roll: axlarna svarar på olika frågor. Stilnivå
        # säger VAR ordet hör hemma (vardagligt/formellt/ålderdomligt), valör
        # säger hur det LÅTER (neutralt/nedsättande/ömsint). Ett ord med bara
        # den ena är inte "delvis märkt" utan tvetydigt: `negativ` utan
        # stilnivå lämnar öppet om ordet är slang eller kanslisvenska, och
        # `arkaisk` utan valör om det är hånfullt eller sakligt.
        #
        # Domän är avsiktligt INTE obligatorisk -- den är tom för de flesta ord
        # (se config.REGISTER_DOMAN, "Valfri, oftast tom").
        for axel in ("stilnivå", "valör"):
            if axel not in upptagen:
                warnings.append(
                    f'"{part}" saknar {axel}-tagg — både stilnivå och valör '
                    f'krävs på varje betydelse (config.REGISTER_'
                    f'{"FORMALITY" if axel == "stilnivå" else "VALENS"}). '
                    f'"neutral" är ett giltigt och ofta rätt svar.')

        # Flykt-taggen är LAGLIG men aldrig tyst. Prefixet OKLART: gör den
        # greppbar, så "hur ofta räckte inte vokabulären?" är en körbar fråga
        # och inte en känsla. Se config.REGISTER_OKLART för resonemanget.
        if config.REGISTER_OKLART in tags:
            warnings.append(
                f'OKLART: "{part}" använder flykt-taggen — lagligt, men räkna '
                'dem: återkommer samma skäl behövs ett nytt värde i vokabulären')
    return warnings


# --- Legacy (format t.o.m. 2026-08-04, används bara av migrate_format.py) ---

_LEGACY_SYNONYM_RE = re.compile(
    rf'<font color="{re.escape(config.SYNONYM_COLOR)}">(.*?)</font>\s*<br>\s*<br>',
    re.DOTALL,
)
_LEGACY_LIST_RE = re.compile(r"<ol>\s*(.*?)\s*</ol>", re.DOTALL)
_LEGACY_LI_RE = re.compile(r"<li>(.*?)</li>", re.DOTALL)
_LEGACY_EXAMPLE_RE = re.compile(r"<i>(.*?)</i>", re.DOTALL)


def parse_legacy(baksida_html):
    synonym_match = _LEGACY_SYNONYM_RE.search(baksida_html)
    synonym_groups = None
    if synonym_match:
        raw = synonym_match.group(1)
        if ";" in raw:
            synonym_groups = [[s.strip() for s in g.split(",")] for g in raw.split(";")]
            synonymer = [s for g in synonym_groups for s in g]
        else:
            synonymer = [s.strip() for s in raw.split(",")]
    else:
        synonymer = []

    list_match = _LEGACY_LIST_RE.search(baksida_html)
    definitioner = [li.strip() for li in _LEGACY_LI_RE.findall(list_match.group(1))] if list_match else []

    example_match = _LEGACY_EXAMPLE_RE.search(baksida_html)
    exempelmening = example_match.group(1).strip() if example_match else ""

    img_match = _IMG_TAIL_RE.search(baksida_html)
    bild_html = img_match.group(1).strip() if img_match else None

    return {
        "synonymer": synonymer,
        "definitioner": definitioner,
        "exempelmening": exempelmening,
        "etymologi": None,  # finns aldrig i legacy-formatet, men håller formen lika
        "bild_html": bild_html,
        "synonym_groups": synonym_groups,
    }
