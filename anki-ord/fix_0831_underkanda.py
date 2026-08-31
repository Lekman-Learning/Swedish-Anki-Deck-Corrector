# -*- coding: utf-8 -*-
"""De tre underkannandena ur blindgranskningen 2026-08-31, rattade.

Alla tre hade granskaren ratt i, och alla tre ar samma sorts fel som
2026-08-28-batchen kostade tjugo underkannanden pa: jag laste ordbokens
struktur slarvigt.

  uppsyn     Jag skrev utseende som synonym till ansiktsuttryck. SO:s
             korsreferens for betydelse 1 pekar mot syn 5 = 'ansikte'.
             Utseende ar en persons stadigvarande yttre, inte ett tillfalligt
             uttryck -- "road uppsyn" gar inte att byta mot "road utseende".
             Nastan-synonym, alltsa inte synonym.

  deviation  Jag ledde med kompassavvikelsen. SO leder med
             'riktningsandring av ljusstrale genom brytning' -- optiken ar
             HUVUDbetydelsen och kompassen ar underbetydelsen. Jag hade
             plockat exemplet och lamnat definitionen, vilket ar exakt det
             regel 4 forbjuder: facit styrs av definitionen, aldrig av ett
             exempel.

  drive      Jag skrev drive-in som en tredje betydelse av drive. Det ar ett
             EGET uppslagsord (l_nr 137978, klassat som forled) med egen
             definition. Att en sammansattning finns gor inte dess betydelse
             till en betydelse hos forledet. Etymologins pastaende om "tre
             skilda lan" foll med samma fel.
"""
import io
import json

FIL = "sessions/session_2026-08-31_v3-batch40.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}
B = '<font color="#3498db">%s</font>'

# ------------------------------------------------------------------ uppsyn
p = BY["uppsyn"]["proposed"]
p["synonymer"] = ["min"]
p["synonym_groups"] = [["min"], ["uppsikt"]]

# --------------------------------------------------------------- deviation
p = BY["deviation"]["proposed"]
p["huvudbetydelse"] = ("Riktningsändring av en ljusstråle när den bryts ; även "
                       "avvikelse i allmänhet, särskilt det fel en kompassnål "
                       "får av järnet i ett fartyg")
p["register"] = "fackspråklig, neutral, fysik ; fackspråklig, neutral"
p["synonymer"] = ["riktningsändring"]
p["synonym_groups"] = [["riktningsändring"], ["avvikelse"]]
p["etymologi"] = ("av latinets deviatio 'avvikelse', till de 'bort från' och "
                  "via 'väg'; samma rot som i trivial, ordagrant 'trevägs'")

# ------------------------------------------------------------------- drive
p = BY["drive"]["proposed"]
p["huvudbetydelse"] = ("Särskilt insatt satsning eller kampanj för att öka en "
                       "verksamhet ; långt slag med bred rörelse i golf eller "
                       "tennis")
p["register"] = "neutral, neutral ; fackspråklig, neutral, sport"
p["synonymer"] = ["satsning", "kampanj"]
p["synonym_groups"] = [["satsning", "kampanj"], []]
p["etymologi"] = ("av engelskans drive 'driva, köra'; kampanjbetydelsen och "
                  "sportslaget är två skilda lån in i svenskan")

for o, txt in (
    ("uppsyn", "UNDERKAND i blindgranskningen och rattad: utseende struket. "
               "SO:s korsreferens for betydelse 1 pekar mot syn 5 = 'ansikte', "
               "och utseende ar en persons stadigvarande yttre snarare an ett "
               "tillfalligt uttryck. 'Road uppsyn' gar inte att byta mot 'road "
               "utseende'. Min star kvar, belagt av SAOL."),
    ("deviation", "UNDERKAND i blindgranskningen och rattad. Jag ledde med "
                  "kompassavvikelsen, men SO leder med 'riktningsandring av "
                  "ljusstrale genom brytning' -- optiken ar huvudbetydelsen "
                  "och kompassen underbetydelsen. Jag hade tagit exemplet och "
                  "lamnat definitionen, vilket regel 4 uttryckligen forbjuder. "
                  "Bada star nu, i ordbokens egen ordning."),
    ("drive", "UNDERKAND i blindgranskningen och rattad: tredje betydelsen "
              "struken. Drive-in ar ett EGET uppslagsord (l_nr 137978, "
              "klassat som forled), inte en betydelse hos drive. Att en "
              "sammansattning finns gor inte dess betydelse till forledets. "
              "Etymologin sa 'tre skilda lan' och sager nu tva."),
):
    BY[o]["sokkoll"]["slutsats"] += " " + txt

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("rattade uppsyn, deviation, drive")
