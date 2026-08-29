# -*- coding: utf-8 -*-
"""Satter KATEGORI (`≈≈`) pa de 115 enskilda ord som saknade synonym.

Adams beslut 2026-08-29: "los resten av orden med 2 avrundnings tecken."

VARFOR DET GAR trots att inget uppslag gav ett ord: `≈≈` ar inte ett
pastaende om betydelselikhet, utan KATEGORIN ordet tillhor -- last ur
kortets EGEN, redan granskade definition. `balalajka` sager sjalvt "ryskt
stranginstrument"; att lyfta ut det ordet ar extraktion, inte gissning.

Det ar skillnaden mot `≈`, som ar ett nytt pastaende och darfor kraver
kalla. Matt pa de 115: 63 hade nagon kalltext, men den texten var
DEFINITIONEN igen -- inte ett annat ord. Darfor gick `≈` inte att satta,
medan `≈≈` gor det.

Tre kort loses av kategorin trots att de hade ANDRA problem:
  tertial -- `kvartal` ar FEL (3 mot 4 manader) men "tidsperiod" ar sant
  grav    -- bar subst + adj som tva betydelser, en kategori per betydelse
  polyp   -- havsdjuret och utvaxten far var sin

Idiom (65 st) och ordled (3 st) far INGEN kategori: dar ar hela uttrycket
betydelsebararen, och en kategori sager ingenting om det.
"""
import fyll_synonymer

VAL = {
    "HTML":             "≈≈ märkspråk",
    "absid":            "≈≈ utbyggnad",
    "affix":            "≈≈ orddel",
    "aktuarie":         "≈≈ tjänsteman",
    "amfibiebil":       "≈≈ fordon",
    "anafor":           "≈≈ stilfigur",
    "arbitrage":        "≈≈ handelsmetod",
    "balalajka":        "≈≈ stränginstrument",
    "baryton":          "≈≈ sångröst",
    "benjamin":         "≈≈ yngsting",
    "bidé":             "≈≈ tvättskål",
    "blodvite":         "≈≈ sår",
    "bolare":           "≈≈ äktenskapsbrytare",
    "bossanova":        "≈≈ musikstil",
    "budgetering":      "≈≈ ekonomiplanering",
    "camembert":        "≈≈ dessertost",
    "canasta":          "≈≈ kortspel",
    "cedilj":           "≈≈ diakritiskt tecken",
    "cinnober":         "≈≈ mineral ; ≈≈ färgämne",
    "cirkumflex":       "≈≈ diakritiskt tecken",
    "dental":           "≈≈ tand- ; ≈≈ språkljud",
    "dimorf":           "≈≈ tvåformig",
    "disambiguera":     "≈≈ förtydliga",
    "dräll":            "≈≈ vävnad",
    "drätsel":          "≈≈ finansförvaltning",
    "ekarté":           "≈≈ kortspel",
    "ektomi":           "≈≈ operation",
    "ekumenik":         "≈≈ kyrkosamverkan",
    "enaktare":         "≈≈ teaterpjäs",
    "encefalografi":    "≈≈ hjärnröntgen",
    "endotermisk":      "≈≈ värmeupptagande",
    "epilering":        "≈≈ hårborttagning",
    "eponym":           "≈≈ namnbildning",
    "evidensbaserad":   "≈≈ vetenskapligt grundad",
    "extramural":       "≈≈ extern",
    "fahrenheit":       "≈≈ temperaturenhet",
    "faktori":          "≈≈ handelsstation",
    "fantomsmärta":     "≈≈ smärta",
    "farmaci":          "≈≈ läkemedelslära",
    "ferrit":           "≈≈ järnform ; ≈≈ magnetmaterial",
    "filklove":         "≈≈ skruvstycke",
    "fortis":           "≈≈ konsonant",
    "fotocell":         "≈≈ ljussensor",
    "fördragen":        "≈≈ förhängd",
    "gemination":       "≈≈ ljudfördubbling",
    "genetiker":        "≈≈ ärftlighetsforskare",
    "grafologi":        "≈≈ handstilstydning",
    "grav":             "≈≈ gravplats ; ≈≈ allvarlig",
    "gördla":           "≈≈ omgjorda",
    "halvpension":      "≈≈ hotellavtal",
    "harmynt":          "≈≈ läppspalt",
    "homosocial":       "≈≈ enkönad",
    "imperialistisk":   "≈≈ erövringslysten",
    "implodera":        "≈≈ falla samman",
    "impressionism":    "≈≈ konstriktning",
    "impressionistisk": "≈≈ konstriktnings-",
    "induktion":        "≈≈ slutledningsmetod",
    "jubilera":         "≈≈ högtidlighålla",
    "kainsmärke":       "≈≈ skamfläck",
    "kalejdoskop":      "≈≈ optisk leksak",
    "kantele":          "≈≈ stränginstrument",
    "kastanjett":       "≈≈ slaginstrument",
    "katamaran":        "≈≈ båt",
    "kirurgi":          "≈≈ operationslära",
    "klåfingrig":       "≈≈ närgången",
    "krabb":            "≈≈ gropig",
    "krenelering":      "≈≈ murkrön",
    "kvader":           "≈≈ huggsten",
    "laminat":          "≈≈ skiktmaterial",
    "liljeväxt":        "≈≈ lökväxt",
    "lux":              "≈≈ ljusenhet",
    "långledas":        "≈≈ ledas",
    "mammografi":       "≈≈ bröströntgen",
    "metates":          "≈≈ ljudomkastning",
    "mortel":           "≈≈ stötkärl",
    "måndagsexemplar":  "≈≈ fabrikationsfel",
    "namne":            "≈≈ namnbroder",
    "neonatal":         "≈≈ nyfödd-",
    "nihilism":         "≈≈ livsåskådning",
    "nitlott":          "≈≈ besvikelse",
    "numen":            "≈≈ gudakraft",
    "papeteri":         "≈≈ brevpapper",
    "parnass":          "≈≈ litterär elit",
    "pediatrik":        "≈≈ barnmedicin",
    "polyp":            "≈≈ nässeldjur ; ≈≈ utväxt",
    "pomerans":         "≈≈ bitterapelsin",
    "pomologi":         "≈≈ fruktodlingslära",
    "postmodernism":    "≈≈ konstriktning",
    "postponera":       "≈≈ efterställa",
    "prospektera":      "≈≈ malmleta",
    "pulpa":            "≈≈ tandmärg ; ≈≈ massa",
    "quechua":          "≈≈ indianspråk",
    "redning":          "≈≈ förtjockning",
    "röklin":           "≈≈ mässkjorta",
    "sari":             "≈≈ kvinnoplagg",
    "sinologi":         "≈≈ kinakunskap",
    "sinus":            "≈≈ vinkelfunktion",
    "småskrake":        "≈≈ dykand",
    "sodomi":           "≈≈ könsakt",
    "spinal":           "≈≈ ryggmärgs-",
    "stetoskop":        "≈≈ läkarinstrument",
    "sufflör":          "≈≈ inviskare",
    "swedenborgianism": "≈≈ religiös lära",
    "synaps":           "≈≈ nervkontakt",
    "syndafall":        "≈≈ ursynd",
    "tabulatur":        "≈≈ notskrift",
    "tajga":            "≈≈ barrskog",
    "teach-in":         "≈≈ debattmöte",
    "tertial":          "≈≈ tidsperiod",
    "tilde":            "≈≈ diakritiskt tecken",
    "ymnighetshorn":    "≈≈ överflödssymbol",
    "åmning":           "≈≈ djupgåendeskala",
    "överburen":        "≈≈ försenad födsel",
    "överloppsgärning": "≈≈ överflödig handling",
    "överpröva":        "≈≈ ompröva",
}

if __name__ == "__main__":
    fyll_synonymer.fyll(VAL)
