# svenska.se — hur den används, och varför den är värd besväret

Adams fråga 2026-08-09: *"vad behövde du för att kunna använda svenska.se? Finns det
något vi kan ladda ner? Där kan vi få SO- och SAOL-ordböckerna också."*

**Svar: ingenting behöver laddas ner.** Sidan går att läsa med en renderande
webbläsare (Playwright), och den ger SAOL + SO + SAOB **på en och samma sida**.

## Varför WebFetch inte räcker

svenska.se bygger sitt innehåll med JavaScript. WebFetch hämtar HTML:en som den
kommer från servern — där finns bara navigering och ett tomt skal. Sidan *ser* ut
att ha hämtats. Den innehåller inget svar.

Det är precis den sortens tysta misslyckande som gör en obelagd uppgift oskiljbar
från en belagd, och därför är svenska.se **kanalberoende** i
`sokkoll_verifiering.py`: giltig som källa bara när beviset kommer från en
browser-navigering, aldrig från WebFetch. Regeln kontrolleras maskinellt eftersom
transkriptet skiljer på verktygen.

## Receptet

**1. Navigera** (URL:en som hamnar i `kalla`):

```
mcp__playwright__browser_navigate  →  https://svenska.se/tre/?sok=<ord>
```

Sidan omdirigerar själv till `https://svenska.se/?q=<ord>`. Skriv in den URL du
faktiskt navigerade till i `kalla` — spärren jämför mot transkriptet.

**2. Fäll ut och extrahera** med `browser_evaluate`. Klickningen och läsningen måste
ske i **två anrop** — sidan är React-byggd och hinner inte rendera om inom samma
evaluate:

```js
// anrop 1 — fäll ut allt
() => { document.querySelectorAll('button')
          .forEach(b => { if (/VISA MER/i.test(b.textContent)) b.click(); }); }

// anrop 2 — läs ut de tre ordböckerna
() => {
  const ut = {};
  for (const n of ['saol','so','saob']) {
    const h = [...document.querySelectorAll('h3')]
                .find(x => x.textContent.trim().toLowerCase() === n);
    ut[n] = h ? h.parentElement.innerText
                 .replace(/\s*\n\s*/g,' ').replace(/\s{2,}/g,' ').trim() : null;
  }
  return ut;
}
```

Använd **inte** `browser_snapshot` för det här — den ger hela
tillgänglighetsträdet inklusive sidfot och kostade ~2 500 tokens på ett ord.
Extraktionen ovan kostade ~350.

## Vad SO tillför som ingen annan källa ger

Mätt på `gedigen` (575 tecken utfälld):

| Fält på kortet | Vad SO ger |
|---|---|
| Betydelser | Numrerade, moderna, med användningsvillkor |
| Exempelmening | `EXEMPEL: en kanna i gediget silver` — färdiga, idiomatiska |
| Etymologi | `HISTORIK: belagt sedan 1687; av tyska gediegen…` |
| Synonymer | `JFR fullödig, ren 2, solid, äkta 1` — redan avgränsade per betydelse |

**Det är alla fyra fälten i kortformatet, ur en källa.** SAOB ger djupet och
beläggen men är historisk (artikeln om *gedigen* är från 1928); SAOL ger den
kompakta moderna definitionen; SO ger det som faktiskt ska stå på kortet.

Hopfälld visade `gedigen` två betydelser. Utfälld visade den tre — den bildliga
"grundlig, pålitlig" låg dold bakom en VISA MER-knapp. **Fäll alltid ut.**

## Konsekvens för sökkollsregeln

Ett anrop till svenska.se ersätter tre separata hämtningar (SAOB + synonymer.se +
Wiktionary) och ger mer. Men Adams regel står kvar: **tre källor är ett golv, inte
ett tak.** svenska.se räknas som tre ordböcker först när alla tre faktiskt gav ett
svar för ordet — träfflisten skriver ut `N träffar i SAOL, N i SO, N i SAOB`, och
en nolla där ska läsas som en lucka, inte som en bekräftelse.
