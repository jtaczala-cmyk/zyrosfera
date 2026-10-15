# Status — ŻyroSfera (stop60)

**URL:** https://stop60.no/zyrosfera/ (GitHub Pages z main / root; domena niestandardowa konta → stop60.no). Ukryta: `noindex,nofollow`, brak linku na stronie głównej i w sitemap.

## Zrobione
- Włączone GitHub Pages.
- Three.js r128 + postprocessing zvendorowane lokalnie w `vendor/` (wcześniej brakowało `ShaderPass.js` → gra się wywalała po Start).
- Naprawione odwrócone sterowanie w pionie (palec w górę = kula w głąb).
- Grafika: świecące animowane włókna wewnątrz półprzezroczystej kuli, fioletowe kryształy z własnym światłem, mocniejszy bloom (połowa rozdzielczości dla wydajności).
- Feedback przy zbieraniu: „+1”, cząsteczki, dźwięk, wibracja, błysk bloom; ekran wygranej z czasem.
- Opcjonalny żyroskop (przycisk, iOS requestPermission, kalibracja, martwa strefa); dotyk domyślny.
- GoatCounter (`/count.js`, respektuje skipgc).
- Test: headless Chromium, emulacja telefonu 390×844 — 7/7 kryształów, brak błędów konsoli. Zrzuty w `shots/`.

## Overhaul grafiki (15.10.2026, Grok)
- Feedback Jacka (iPhone): „nudne, prymitywne, brak koloru” → pełny lifting wizualny.
- 3 strefy z własną paletą (Neon Laguna / Zachód Lawy / Toksyczna Dżungla): gradientowe niebo (shader), kolorowa mgła, neonowa siatka i pierścienie; po 7 fragmentach przejście do następnej strefy.
- Kolorowe fasetowane kryształy z poświatą i iskrami, tęczowy ślad za kulą, wybuch cząsteczek + fala + wstrząs kamery przy zbieraniu.
- Menu: gradientowe tło, tęczowy animowany tytuł, pulsujący przycisk; HUD w stylu mobilnym.
- Wydajność: usunięte światła punktowe kryształów, pule cząsteczek, bloom w 1/2 rozdz., bez MSAA. Żyroskop/dotyk bez zmian, noindex bez zmian.

## Grafika premium + fabuła (15.10.2026, Grok — gałąź grok/graphics-story)
- Z PR grok/better-graphics przeniesione techniki (PR nie scalony: oparty na starym main, cofałby 3 strefy, żyroskop, GoatCounter i nazwę ŻyroSfera):
  - kula gracza: MeshPhysicalMaterial z transmission 0.92 + clearcoat (jedyny obiekt z transmission), kolor/emisja wg strefy;
  - ACES Filmic tone mapping, bloom w pełnej rozdzielczości (wyższy próg, mniej przepaleń);
  - kinowe światło: ciepły key (DirectionalLight) + dwa kolorowe rim-lighty wg palety strefy, hemisphere w kolorach strefy;
  - głębsza mgła FogExp2 w kolorze strefy, lustrzana metaliczna podłoga;
  - mniej agresywnych neonów: siatka 0.16, pierścienie 0.3, ślad w kolorach strefy zamiast tęczy, mniejsze drobiny; kryształy jako szlachetne kamienie (MeshStandard, metal/roughness).
  - Odrzucone z PR: nazwa Aetheris, usunięcie stref/żyroskopu/GoatCounter, PointLight na każdym krysztale (za drogie na iPhone), antialias MSAA.
- Wydajność: pixel ratio max 1.75; adaptacyjna jakość — gdy średnio <45 FPS przez ~120 klatek: PR 1.35, potem PR 1.0 + bloom w 1/2 rozdz.
- Fabuła z GDD (gałąź grok/gdd-fabuła): ekran prologu (Lumen, Drift, stacja Aetheris), karta misji przed każdą strefą, wydarzenie przy 3. fragmencie (nagranie załogi / „Drift się zbliża” / rośliny), „Fragment odzyskany” przy 7., ekran końcowy „Serce bije. Aetheris żyje.” Języki PL (domyślny) / EN / NO — przyciski w menu, zapamiętywane w localStorage.
- Nazwa gry i URL bez zmian: ŻyroSfera, stop60.no/zyrosfera; „Aetheris” występuje tylko jako nazwa stacji w fabule.
- Integracja z portalem czarnej dziury (main): karta misji pokazuje się po zakończeniu przejścia BH; endBH przywraca nowe wartości kuli (opacity 1, halo 0.25); adaptacja jakości wstrzymana w trakcie BH.
- Test headless 390×844: brak błędów gry w konsoli (tylko 404 /count.js lokalnie). Zrzuty: shots/gs_*.png.
- **Test na iPhonie 15 Pro: oczekuje na Jacka** (FPS, czy adaptacja nie obniża jakości bez potrzeby, transmission na kuli).

## Otwarte
- Test na prawdziwym telefonie (wydajność, żyroskop na iOS).
- Nazwa „ŻyroSfera” — nie znaleziono konfliktu znaków towarowych w kodzie/zasobach (brak cudzych assetów); formalnie niesprawdzone w rejestrze.
- Więcej poziomów / przeszkody wg GDD.

Stop60 skończył — Grok może pracować na gałęzi i otwierać PR

## Czarna dziura — przejście między strefami (15.10.2026, dla Groka)
- Zaimplementowane wg `BLACK_HOLE_EFFECT.md` w `index.html` (`startBH/updateBH`): 5,5 s po zebraniu 7/7 w strefie 1→2 i 2→3 (po strefie 3 nadal ekran wygranej).
- 0–0,8 s pojawienie się (czarny dysk + niebiesko-biały pierścień akrecyjny, siatka zaczyna się zakrzywiać w lej); 0,8–2,5 Lumen wciągana, włókna rozciągają się i wirują szybciej, łuki światła (lensing), bloom 0,9→2,8; 2,5–3,8 maks. zniekształcenie (shader pełnoekranowy: wir/soczewka + aberracja chromatyczna i falowanie na brzegach), paleta przechodzi do następnej strefy, puls jasności; 3,8–4,2 cisza, prawie czarno, widać tylko włókna, bloom 0,35; 4,2–5,5 nowa strefa się rozjaśnia, kryształy wyrastają, bloom wraca do 0,9.
- Dźwięk WebAudio: narastający drone sub-bass, wysokie krystaliczne tony z odstrojeniem, cichy szum próżni, 0,4 s ciszy, wejście akordu nowej strefy z pogłosem (Convolver).
- Bez dodatkowych systemów cząsteczek; ShaderPass włączany tylko na czas przejścia; jeśli FPS spadnie w trakcie, bloom tymczasowo w 1/4 rozdz. Tap w trakcie (1–3,8 s) = pomiń do wyjścia.
- Uwaga: GDD w PR #2 zmienia nazwę na „Aetheris/Lumen” — w grze nazwa/URL ŻyroSfera bez zmian (decyzja Jacka).
- Zrzuty: `shots/live_bh_*.png`.

## 2026-10-15 — Mobile optimizations (MOBILE_OPTIMIZATIONS.md, PR #6)
- Implemented: mobile profile (`MOB` = dpr>2 or coarse pointer): bloom at half-res by default on dpr>2; trail 16 sprites (was 26); sparkles pool 150 (was 300); player sphere 32×24 segments (was 48×32).
- Adaptive quality: new level 3 (after 1.35 → 1.0+half bloom) hides the trail and limits ambient motes to 200.
- Already present / skipped: pixel ratio cap 1.75, levels 1–2, black hole quarter-res bloom fallback, flat-shaded crystals; lights already at 2 PointLights (no per-crystal lights exist). Skipped "full-res bloom during short effects" (reallocating render targets mid-effect causes stutter on iOS).
- Verified headless 390×844 @3x: no game console errors (only 404 for /count.js + favicon on the local server, both exist only on stop60.no root).

## 2026-10-15 — Hyperspace zone transition (note for Grok)
- PR #8 (grok/hyperspace-tunnel, demo `hyperspace.html`) merged as-is.
- index.html: black-hole transition extended 5.5 s → 6.7 s: 0–0.8 portal opens · 0.8–2.5 orb pulled in · 2.5–3.8 max distortion + palette shift · 3.8–4.0 silent black beat · **4.0–5.4 hyperspace** (streaks in next zone's palette `cr[0]`,`cr[1]`,`top`; accelerate to max in 0.4 s, FOV 74→104, bloom ↑, white flash at end, WebAudio whoosh) · 5.4–6.7 exit into new zone (FOV 104→56).
- Streaks: one `THREE.LineSegments` + ShaderMaterial (additive, GPU-animated, no per-frame buffer upload), lazily created on first transition, visible only in the hyperspace phase. Count 560 desktop / 320 mobile, 260/180 when adaptive quality lvl≥2.
- Tap-to-skip unchanged (jumps to 3.8 s, hyperspace still plays). Fix: zone switch is now guaranteed even if a frame hitch jumps past the exit phase.
- Headless 390×844 check: no console errors (only local 404 for GoatCounter count.js). Shots: shots/hs_*.png.
