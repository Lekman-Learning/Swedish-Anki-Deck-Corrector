# -*- coding: utf-8 -*-
"""Synonymbatch 03 -- 51 kort.

MOTSATSORD i synonymer.se-listorna som kontrollerats och uteslutits har:
"rak" (krum), "fralst" (fortappad), "tom/svulten" (stinn), "haglosnhet"
(patos), "divergent" (konvergent), "heterogen" (homogen), "overdriva" och
"forstora" (bagatellisera). Sajten blandar sektionerna, sa listan far aldrig
kopieras rakt av.

subtil och tabelras ar tva kort som UNDERKANDES i blindgranskningen 28/8 --
subtil for en opastad utvidgning, tabelras for att jag lat etymologin styra
facit. Synonymerna har ar valda mot kortens NUVARANDE, rattade betydelse.
"""
import fyll_synonymer

VAL = {
    # --- akta synonymer ---
    "pult":             "dirigentpall ; notställ",
    "hätta":            "luva, huva",
    "överläggning":     "rådslag, samråd",
    "konklav":          "kardinalmöte",
    "principal":        "arbetsgivare, husbonde",
    "varseblivning":    "perception, förnimmelse",
    "ranson":           "tilldelning, portion",
    "krås":             "innanmäte, inälvor",
    "krum":             "krokig, kutryggig",
    "tuktig":           "sedesam, ärbar",
    "förtappad":        "fördömd, förkastad",
    "notabel":          "anmärkningsvärd, bemärkt",
    "tabelras":         "total förödelse, fullständig ödeläggelse",
    "stinn":            "proppfull, välfylld",
    "patos":            "lidelse, glöd",
    "kätte":            "bås, spilta",
    "yrka":             "begära, fordra",
    "blåställ":         "overall, överdragskläder",
    "lomma":            "lufsa, larva",
    "kväde":            "skaldestycke, drapa",
    "konvergent":       "sammanlöpande",
    "suggerera":        "intala, inge",
    "distorsion":       "stukning ; förvrängning",
    "degeneration":     "urartning, förfall",
    "ävlan":            "strävan, iver",
    "frondera":         "opponera, revoltera",
    "allenarådande":    "enväldig, allenahärskande",
    "entlediga":        "avskeda, friställa",
    "subtil":           "hårfin, knappt märkbar",
    "extravagant":      "överdådig, slösaktig",
    "sejour":           "vistelse, uppehåll",
    "deklassera":       "degradera, nedvärdera",
    "eklog":            "herdedikt, idyll",
    "homogen":          "enhetlig, likformig",
    "bagatellisera":    "förringa, vifta bort",
    "gondol":           "venetiansk roddbåt ; ballongkorg",

    # --- narmaste ord, inte utbyte ---
    "gastkramning":     "≈ fasa",
    "frikadell":        "≈ kokt köttbulle",
    "koloratur":        "≈ fioritur",
    "fotogenisk":       "≈ kameravänlig",
    "hälare":           "≈ tjuvgodsköpare",

    # --- ingen synonym i nagon av de tre kallorna ---
    "halvpension":      None,   # hotellterm, eget namn
    "åmning":           None,   # sjofartsterm
    "jade":             None,   # mineralnamn
    "sponta":           None,   # snickeriterm
    "etyd":             None,   # musikterm
    "implodera":        None,   # bara anvandarbidrag ("sprangas inat")
    "nihilism":         None,   # "anarki/anomi" ar naraliggande LAROR, inte utbyten
    "måndagsexemplar":  None,
    "mangold":          None,   # vaxtnamn
    "katamaran":        None,   # batttyp, eget namn
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
