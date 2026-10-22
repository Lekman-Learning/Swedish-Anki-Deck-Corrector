"""Rätta synonymerna efter forgranska 2026-10-22: bara SO SYN / SO-SAOL-definitionstext eller ≈≈ kategori.

synonymer.se ensamt räcker inte som belägg (projektets regel). Betydelseflaggorna
som bara räknar 'äv.'/'spec.'-underbetydelser bedöms och noteras i slutsatsen.
"""
import json

FIL = "sessions/session_2026-10-22_v3-omgranskning-repetition-mognad.json"

GRP = {
    "pamflett": [["nidskrift"]],
    "respons": [["reaktion"], ["gensvar"]],
    "aktuell": [["≈≈ brännande"], ["≈≈ närvarande i medvetandet"], ["≈≈ planerad"]],
    "croissant": [["≈≈ bakverk"]],
    "dividera": [["dela"], ["diskutera"]],
    "evolution": [["utveckling"]],
    "exotisk": [["från fjärran land"], ["främmande", "sällsam", "ovanlig"]],
    "insinuation": [["≈≈ antydan"]],
    "optimal": [["bästa möjliga"], ["≈≈ störst möjlig"]],
    "passionerad": [["lidelsefull"]],
    "platonsk": [["platonisk"], ["≈≈ osinnlig"], ["passionsfri", "sval"]],
    "prestanda": [["prestationsförmåga"], ["åligganden"]],
    "saldo": [["≈≈ behållning"]],
    "sexualitet": [["≈≈ könsdrift"]],
    "absorbera": [["suga upp", "uppta"], ["tillgodogöra sig"], ["≈≈ fånga"]],
    "anstucken": [["påverkad"]],
    "avträda": [["lämna ifrån sig"], ["avlägsna sig"]],
    "centrera": [["placera i centrum"], ["inrikta"]],
    "dassig": [["dålig", "trist"]],
    "eruption": [["vulkaniskt utbrott"], ["≈≈ framväxt"], ["≈≈ utbrott"]],
    "eufori": [["lyckokänsla", "förhöjt stämningsläge"]],
    "kleptomani": [["≈≈ tvångsbeteende"]],
    "kompromiss": [["medelväg"], ["≈≈ avtal"]],
    "kondensera": [["förtäta"], ["tränga ihop"]],
    "kreatur": [["boskap"], ["varelse"], ["lydigt redskap", "hantlangare"]],
    "lurvig": [["luden", "rufsig"], ["lätt berusad"], ["≈≈ dansa"]],
    "mollusk": [["blötdjur"], ["≈≈ vårta"], ["≈≈ mes"]],
    "multipel": [["mångfaldig"], ["≈≈ produkt"]],
    "naturalisera": [["≈≈ ge medborgarskap"], ["göra inhemsk"]],
    "pedagogisk": [["undervisande"], ["skickligt undervisande"]],
    "repressiv": [["undertryckande", "hämmande"]],
    "schablon": [["mall"], ["slentrian"], ["≈≈ beräkningsgrund"]],
    "sporadiskt": [["då och då"], ["här och där"]],
    "sympati": [["tillgivenhet"], ["välvillig förståelse", "gillande"]],
    "tyfon": [["virvelstorm", "cyklon"], ["siren"]],
}
HB = {
    "flott": ("Elegant och påkostad, ibland också frikostig ; smält djurfett som man steker i ; om båt: som flyter utan att röra botten",
              "neutral, neutral, allmän ; neutral, neutral, matlagning ; fackspråklig, neutral, sjöfart"),
}
NOT = ("Förgranskningen 22/10: synonymer utan belägg i SO SYN eller SO/SAOL-definitionstext ersatta med belagda "
       "eller ≈≈ kategori ur kortets egen HB. Betydelseflaggor som räknar 'äv.'/'spec.'/'ibland bildligt' "
       "bedömda som underbruk av befintlig betydelse, inte saknade betydelser.")


def main():
    d = json.load(open(FIL, encoding="utf-8"))
    for e in d:
        p = e["proposed"]
        if e["ord"] in HB:
            p["huvudbetydelse"], p["register"] = HB[e["ord"]]
        if e["ord"] in GRP:
            g = GRP[e["ord"]]
            assert len(g) == len(p["huvudbetydelse"].split(" ; ")), e["ord"]
            p["synonym_groups"] = g if len(g) > 1 else None
            p["synonymer"] = [s for x in g for s in x]
            e["sokkoll"]["slutsats"] += " " + NOT
    json.dump(d, open(FIL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("rättade", len(GRP) + len(HB))


if __name__ == "__main__":
    main()
