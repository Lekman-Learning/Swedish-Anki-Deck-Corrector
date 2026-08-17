# Återuppta: batch30 full v3 (is:new, staged 2026-08-17)

Adam bad om 30 is:new-kort till full v3 eftersom nya-kön bara har **75**
full-v3-kort kvar. Uppslagningen är klar och bevisad. **Kvar: skriva korten.**

## Kontrollerna han bad om — båda rena

**"Har du glömt unsuspenda kort med full v3?"** Nej.
`python v3_invariant.py --torr` ger:

```
Full v3, ej undantagna : 959
  fel flagga (ej blå)  : 0
  suspenderade         : 0
Undantagna (underkända/pausade, ska förbli röda+spärrade): 9
```

De 4 full-v3-kort som ÄR suspenderade (`gourmand`, `hugfästa`, `uppknäppt`,
`ocker`) bär alla `v3_underkand` med **senare datum** än verifieringen — de
underkändes efter att ha verifierats och ska vara spärrade.

De 5 som bär `v3_underkand` men är aktiva (`märgfull`, `apoplexi`, `förvärva`,
`beskärm`, `alla taggar utåt`) har tvärtom **verifieringsdatum senare än
underkännandet** — rättade och omverifierade. Korrekt aktiva.

> ⚠️ **Svaghet upptäckt i `v3_invariant.py`:** undantagslogiken tittar bara på
> om taggen `v3_underkand` *finns*, inte på dess datum. Den kan därför inte
> skilja "underkänd och aldrig fixad" från "underkänd, fixad, omverifierad".
> Just nu är det ofarligt, men skriptet skulle tiga även om ett av de fem
> faktiskt vore trasigt. Värt att datumjämföra.

## Klart

| | |
|---|---|
| Batchfil | `sessions/session_2026-08-17_v3-batch.json` — 30 kort |
| Uppslagning | **90 hämtningar**, `SVENSKA_SE_HAMTAD ... HTTP 200` för alla 30 i transkript + `raw-verktyg/` → **källspärren bevisad** |
| Trekällstäckning | 24 av 30 fullständiga; 6 ofullständiga (alla har svenska.se) |
| Omkörningssvep | `förlikas` fick Wiktionary 429 → omkörd → HTTP 200 |
| Underlag | `underlag_batch30.txt` (298 rader) |
| Ordlista | `batch30_ord.json` |

### 2 kort pausade före skrivning

Båda gav `uppslagsordstraffar: ["saob"]` — SAOL 0 träffar, SO saknas. Samma
läge som `förborgad` 2026-08-12. Taggade `v3_pausad::inget_uppslagsord_i_so_saol`
och suspenderade:

- **ordig** — SAOL `didYouMean: oredig`
- **reglementarisk** — SAOL `didYouMean: reglementering`

`probat` såg först likadan ut men **SAOL har det**: *"beprövad och därvid
befunnen god"*, märkt `åld.` — går vidare.

**Kvar att skriva: 28 kort.**

## 🔴 Det största fyndet: `autopsi` har fel huvudbetydelse

Nuvarande kort ger bara obduktionsbetydelsen. Ordböckerna säger tvärtom:

| Källa | Betydelse 1 | Betydelse 2 |
|---|---|---|
| SO | **iakttagelse som man gjort med egna ögon** | obduktion *(mindre brukligt)* |
| SAOL | **iakttagelse med egna ögon, självsyn** | obduktion |

**Kortets enda betydelse är alltså ordboks andra, och den är märkt mindre
brukligt.** Självsynsbetydelsen saknas helt. Det är inte en nyansjustering utan
ett omvänt kort.

## Riskflaggor i batchen

```
7  old_delar_inget_ordforrad
3  tom_exempelmening
2  old_delar_inget_ordforrad + tom_exempelmening
2  dubblettdefinition
1  old_delar_inget_ordforrad + cirkular_synonym + tom_exempelmening
1  old_delar_inget_ordforrad + cirkular_synonym
```

Andra kort med känd problembild ur underlaget:

- **drive** — kortet beskriver verbet *driva*; SO/SAOL har substantivet
  (golfslag, kampanj, drive-in). Helt fel ordklass.
- **lagra** — `cirkular_synonym` (*upplagra*), tom exempelmening, och SO har
  fyra betydelser där kortet har två.
- **symbios** — saknar den bildliga betydelsen som SO och SAOL båda tar upp.
- **konservator** — kortet missar SO:s särskilda betydelse *uppstoppare av
  döda djur*, som FACIT också har.

## Kör detta härnäst

```
cd anki-ord
# 1. skriv de 28 korten i sessions/session_2026-08-17_v3-batch.json
#    underlag: underlag_batch30.txt
python forgranska.py sessions/session_2026-08-17_v3-batch.json
python kortgranskare.py applicera sessions/session_2026-08-17_v3-batch.json
python kortgranskare.py paket    sessions/session_2026-08-17_v3-batch.json
python blindgranska.py sessions/session_2026-08-17_v3-batch_v3-paket.json --antal 25
python blindgranska.py sessions/session_2026-08-17_v3-batch_v3-paket.json --antal 25   # resten
python kortgranskare.py verdikt sessions/session_2026-08-17_v3-batch_v3-paket.json
python kortgranskare.py slapp   sessions/session_2026-08-17_v3-batch.json   # BATCHfilen
```

## Fortfarande öppet sedan 2026-08-17

- **batch50** (is:review) ligger kvar staged i `ATERUPPTA_batch50.md`. Anki är
  igång nu, så den är inte längre blockerad.
- **njugg, inbunden, förlägga** — underkända med färdig diagnos, ligger kvar i
  Adams kö.
- **ryd** — `traffar=saob`, samma pausfråga som ordig/reglementarisk ovan.
