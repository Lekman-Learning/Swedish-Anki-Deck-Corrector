# Återuppta: batch50 full v3 (staged 2026-08-17 kväll)

Adam bad om 50 provisoriska is:review-kort till full v3 och stängde sedan
Anki. Uppslagningen är gjord och bevisad; resten väntar på att Anki startas.

## Klart

- `batch50.json` — 50 kort, valda ur `v3_urgency_provisorisk.json` (topp 50 av 503)
- **Uppslagningen körd**: 150 hämtningar, `SVENSKA_SE_HAMTAD <ord> HTTP 200`
  för alla 50 ligger i transkriptet och `raw-verktyg/` → **källspärren är bevisad**
- `uppslag/*.json` — full rådata per ord
- 43 av 50 har trekällstäckning; 7 saknar en källa (alla har svenska.se)

## Kör detta när Anki är igång

```
cd anki-ord
python v3_urgency_provisorisk.py            # RÄKNA OM -- listan gjordes före
                                            # dagens 47 fick oberoende_verifierad
python kortbyggare.py --spar batch50 --antal 50
# därefter: skriv om korten, sedan
python forgranska.py sessions/<fil>
python kortgranskare.py applicera sessions/<fil>
python kortgranskare.py paket sessions/<fil>
python blindgranska.py sessions/<fil>_v3-paket.json --antal 25   # x2
python kortgranskare.py verdikt sessions/<fil>_v3-paket.json
python kortgranskare.py slapp sessions/<fil>                     # BATCHfilen
```

## Tre kort har redan färdig diagnos

Underkända i dagens blindgranskning, ligger kvar i Adams kö, högst prio:

- **njugg** — kortet delar felaktigt upp ordet i två betydelser. SO har EN
  numrerad betydelse ("(onödigt) snål och knusslig"), SAOL en sammanhållen
  ("snål; knapp"). Slå ihop.
- **inbunden** — rätt antal betydelser (två), fel ordning. SO har
  "försedd med pärmar" som betydelse 1; kortet leder med personlighets-
  betydelsen. Vänd.
- **förlägga** — saknar SO:s huvudbetydelse (1) "tilldela utrymme att vistas
  i" (*bataljonen är förlagd i baracker*). Kortets exempelmening är hämtad ur
  betydelse (6), tidsbetydelsen, men kopplad till en vag definition.

## En flagga att kolla först

**`ryd`** gav `traffar=saob` — ordet finns varken i SO eller SAOL, bara i SAOB.
Samma läge som `förborgad` 2026-08-12, som pausades med
`v3_pausad::inget_uppslagsord_i_so_saol`. Avgör om `ryd` ska pausas innan det
skrivs.
