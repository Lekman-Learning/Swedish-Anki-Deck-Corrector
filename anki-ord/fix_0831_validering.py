# -*- coding: utf-8 -*-
"""Sista rattelserna innan applicering, batch 2026-08-31.

Fyra feltyper, alla fangade av baksida.validate_adamtal och kortgranskarens
registerkontroll:

1. BART SEMIKOLON i forsavida och inhysa. Ett ';' utan mellanslag ar
   osynligt for register-indragningen -- kortet hade renderats med fel
   betydelseuppdelning. Bytt mot komma, som ar vad meningarna faktiskt
   behovde.
2. OGILTIGA REGISTERVARDEN. 'alderdomlig' finns inte i
   config.REGISTER_FORMALITY, dar formen heter 'ngt alderdomlig'.
   'sprakvetenskap' heter 'lingvistik' i REGISTER_DOMAN. Och
   'finlandssvensk', som jag satte for uppbad tidigare i dag for att blidka
   forgranskningens markningskontroll, finns inte alls -- dialektal ar
   narmaste giltiga varde. Markningen finl. star kvar i klartext i sjalva
   betydelsen, dar Adam faktiskt laser den.
3. FOR LANG HUVUDBETYDELSE i uppbad, 17 ord i en betydelse.
4. FOR LANG ETYMOLOGI i elliptisk, 22 ord. Etymologin ska forklara
   betydelsen, inte beratta ordets historia.
"""
import io
import json

FIL = "sessions/session_2026-08-31_v3-batch40.json"
KORT = json.load(io.open(FIL, encoding="utf-8"))
BY = {k["ord"]: k for k in KORT}


def satt(ord_, **falt):
    for k, v in falt.items():
        BY[ord_]["proposed"][k] = v


# 1. bart semikolon
satt("försåvida", huvudbetydelse="Under förutsättning att, alltså om det är "
                                 "så att")
satt("inhysa", huvudbetydelse="Ge tillfällig bostad åt någon, även om att "
                              "förvara föremål någonstans")

# 2. ogiltiga registervarden
satt("dandy", register="ngt ålderdomlig, negativ")
satt("dagtinga", register="högtidlig, negativ ; ngt ålderdomlig, neutral")
satt("elliptisk", register="fackspråklig, neutral ; fackspråklig, neutral, "
                           "lingvistik")
satt("uppbåd", register="neutral, neutral ; dialektal, neutral")

# 3. for lang huvudbetydelse
satt("uppbåd", huvudbetydelse="Stor grupp personer som kallats samman för ett "
                              "särskilt syfte ; i finlandssvenska: mönstring "
                              "till militärtjänst")

# 4. for lang etymologi
satt("elliptisk", etymologi="till ellips, av grekiskans elleipsis "
                            "'utelämnande'; båda betydelserna handlar om "
                            "något som saknas")

for o in ("försåvida", "inhysa", "dandy", "dagtinga", "elliptisk", "uppbåd"):
    BY[o]["sokkoll"]["slutsats"] += (
        " RATTAT fore applicering: se fix_0831_validering.py for vilken av de "
        "fyra feltyperna det gallde. Ingen betydelse har andrats, bara form "
        "och registervarden.")

json.dump(KORT, io.open(FIL, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("rattade 6 kort")
