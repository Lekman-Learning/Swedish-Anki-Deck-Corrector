# -*- coding: utf-8 -*-
"""Arbetsbatch 2026-09-04, kort 1-12 av 50 (is:review, riskrankade).

Alla synonymer ur HJ.synpool(); dar poolen bara ger definitionsfragment
anvands `≈≈ kategori` ur kortets egen definition, vilket forgranska
undantar fran kallkraven.
"""
import io, json, sys
import _hjalp_0902b as HJ

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIL = "sessions/session_2026-09-04_v3-omgranskning.json"
H = HJ.H

K = {
 "asketisk": (
  "Som avstår från njutningar och lever mycket enkelt",
  "neutral, neutral", ["≈≈ återhållsam", "sparsam"],
  [["≈≈ återhållsam", "sparsam"]],
  "Munkarna levde ett %s liv utan minsta bekvämlighet." % (H % "asketiskt"),
  "SO ger två betydelser men de är samma drag riktat mot olika saker — mot "
  "njutningar (1) och mot uttrycksmedel (2). De hålls ihop i en. Poolen ger "
  "bara 'sparsam', som ensamt är för svagt, så en ≈≈-kategori står först."),

 "vanart": (
  "Dåligt uppförande",
  "ngt ålderdomlig, negativ", ["oart", "osed", "dåligt uppförande"],
  [["oart", "osed", "dåligt uppförande"]],
  "Läraren såg strängt på pojkens %s." % (H % "vanart"),
  "SO märker ordet 'något ålderdomligt' — det står i registret i stället för "
  "att antas neutralt. Alla tre synonymerna finns i poolen."),

 "dimpa": (
  "Falla tungt och plötsligt ; dyka upp oväntat",
  "vardaglig, neutral ; vardaglig, neutral",
  ["falla pladask", "oväntat uppenbara sig"],
  [["falla pladask"], ["oväntat uppenbara sig"]],
  "Tegelpannan %s ner alldeles framför honom." % (H % "damp"),
  "SAOL märker båda betydelserna 'vard.'. Exempelmeningen använder "
  "preteritum 'damp', som är den form Adam faktiskt möter — infinitiven "
  "'dimpa' är sällsynt i bruk."),

 "vörda": (
  "Visa djup respekt för någon eller något",
  "högtidlig, positiv", ["≈≈ högakta"],
  [["≈≈ högakta"]],
  "Vi %s minnet av dem som dog för friheten." % (H % "vördar"),
  "Poolen ger bara 'ha' och 'hysa', alltså avhuggna bitar av SO:s "
  "definition ('ha och visa hög aktning för') och inte synonymer. Därför "
  "≈≈. Registret är högtidligt: ordet hör hemma vid minnesstunder, inte i "
  "vardagstal."),

 "papyross": (
  "Rysk cigarett med långt pappersmunstycke",
  "ngt ålderdomlig, neutral", ["cigarett med pappmunstycke"],
  [["cigarett med pappmunstycke"]],
  "Officeren tände en %s och blåste ut röken genom fönstret." % (H % "papyross"),
  "SO märker 'mest historiskt', vilket ger registret. Etymologin är värd "
  "att ha med: samma ord som papyrus, via ryskans papirosa."),

 "gillra": (
  "Sätta upp en fälla",
  "neutral, neutral", ["sätta upp"],
  [["sätta upp"]],
  "Han %s en fälla för räven vid skogsbrynet." % (H % "gillrade"),
  "SO:s def är bara 'sätta upp', vilket ensamt är för brett — det är "
  "exemplen som visar att det gäller just fällor. Huvudbetydelsen skärps "
  "därför till fällan, som är det enda sammanhang ordet lever i."),

 "iscensätta": (
  "Sätta upp ett verk på scen ; planera och dra igång något",
  "neutral, neutral, konst ; neutral, neutral",
  ["inscenera", "uppföra", "sätta i gång"],
  [["inscenera", "uppföra"], ["sätta i gång"]],
  "Regissören %s Hamlet på Dramaten." % (H % "iscensatte"),
  "Två genuint skilda betydelser: den sceniska och den överförda "
  "('iscensätta en kupp'). Den sceniska står först eftersom den är "
  "grundbetydelsen och exempelmeningen visar den."),

 "pondus": (
  "Naturlig tyngd som gör att andra lyssnar",
  "formell, positiv", ["värdighet", "tyngd"],
  [["värdighet", "tyngd"]],
  "Rektorn var en man med %s." % (H % "pondus"),
  "SO:s andra betydelse ('tyngd, eftertryck') är samma egenskap flyttad "
  "från personen till orden och slås ihop. 'eftertryck' är struket ur "
  "synonymraden — det gäller sättet man säger något på, inte personen."),

 "verst": (
  "Gammalt ryskt längdmått, drygt en kilometer",
  "ngt ålderdomlig, neutral", ["≈≈ längdmått"],
  [["≈≈ längdmått"]],
  "Byn låg tre %s från floden." % (H % "verst"),
  "Poolen ger bara 'drygt 1 km', som är ett mått och inte en synonym. "
  "≈≈-kategorin används i stället. SAOL:s siffra (drygt 1 km) står i "
  "huvudbetydelsen, där den gör nytta."),

 "auktor": (
  "Upphovsman till ett verk",
  "formell, neutral", ["upphovsman", "författare"],
  [["upphovsman", "författare"]],
  "Verkets %s är okänd." % (H % "auktor"),
  "SO:s andra betydelse är den biologiska nomenklaturens — den som först "
  "publicerat ett giltigt vetenskapligt namn. Den är fackterm inom "
  "systematik och tas inte med; kortet ska bära det Adam möter i text."),

 "sätesbjudning": (
  "Förlossning där barnet kommer med rumpan först",
  "fackspråklig, neutral, medicin", ["≈≈ fosterläge"],
  [["≈≈ fosterläge"]],
  "Vid %s kommer barnet med stjärten först i stället för med huvudet." % (H % "sätesbjudning"),
  "Poolen ger 'fosterläge', 'vid', 'då' — bara det första bär innehåll, och "
  "det är en kategori snarare än en synonym, alltså ≈≈. Huvudbetydelsen är "
  "skriven i Adam-tal: SO:s 'passerar bäckenkanalen med sätet före' är "
  "korrekt men obegripligt utan medicinsk vana."),

 "jamb": (
  "Versfot med en obetonad stavelse följd av en betonad",
  "fackspråklig, neutral, litteraturvetenskap", ["≈≈ versfot"],
  [["≈≈ versfot"]],
  "Ordet <i>befäl</i> är en %s: obetonat be-, betonat -fäl." % (H % "jamb"),
  "Poolen ger 'versfot' och 'tvåstavig' — kategori respektive egenskap, "
  "ingen av dem en synonym, därför ≈≈. SO:s eget exempel ('ordet troké är i "
  "sig självt en jamb') är elegant men förvirrande på ett kort, eftersom "
  "det blandar in motsatsbegreppet. 'befäl' visar mönstret rent."),
}

def main():
    d = json.load(io.open(FIL, encoding="utf-8"))
    kort = d["kort"] if isinstance(d, dict) and "kort" in d else d
    n = 0
    for k in kort:
        o = k.get("ord")
        if o not in K:
            continue
        hb, reg, syn, grupper, ex, note = K[o]
        k["proposed"] = {
            "huvudbetydelse": hb,
            "register": reg,
            "synonymer": syn,
            "synonymgrupper": grupper,
            "exempelmening": ex,
            "etymologi": HJ.etym(o),
            "sokkoll": HJ.kallor(o),
        }
        k["note_till_granskare"] = note
        k["approved"] = True
        n += 1
    json.dump(d, io.open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("skrev %d kort till %s" % (n, FIL))
    saknas = [o for o in K if not any(x.get("ord") == o for x in kort)]
    if saknas:
        print("VARNING, fanns inte i sessionsfilen:", saknas)

main()
