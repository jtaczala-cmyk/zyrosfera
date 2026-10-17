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

## Hyperspace v3 — kinowy skok (15.10.2026, Grok)
- PR #9 (grok/hyperspace-v2, samo demo `hyperspace_v2.html`) scalony; v2 jako baza dla etapu w grze.
- Przejście strefy: czarna dziura 0–4.0 s → **nadświetlna 4.0–6.3 s (2.3 s)** → wyjście 6.3–7.6 s (razem 7.6 s, wcześniej 6.7 s).
  - 4.0–4.7 ładowanie: smugi jako punkty, narastający świst, rośnie centralna poświata, lekki shake;
  - 4.7–4.85 szarpnięcie: wszystko cofa się (krótki pullback, FOV 80→64);
  - 4.85–5.9 SLAM: gwałtowne przyspieszenie, punkty rozciągają się w długie linie (długość zależna od prędkości), radial/zoom blur, aberracja chromatyczna na brzegach, tunel świetlny, FOV do 98, głuche uderzenie + ryk;
  - 5.9–6.3 wyjście z nadświetlnej: smugi „zatrzaskują się” z powrotem w punkty, boom, biały błysk → odsłonięcie nowej strefy.
- Smugi: jeden draw call (jeden indeksowany mesh quadów), ruch w vertex shaderze; jasny biało‑niebieski rdzeń + kolorowe halo z palety strefy, zanikający ogon; szerokość ~stała w px (bez znikania sub‑pikselowego). 800 desktop / 450 mobile, ×0.8/0.55/0.4 przy adaptacyjnej jakości 1/2/3.
- Radial blur + CA + błysk: osobny pass tylko podczas etapu; blur w 1/2 rozdz. na mobile / przy jakości ≥2.
- Dźwięk (WebAudio, generowany): świst ładowania, thump przy skoku, ryk, boom przy wyjściu.
- Tap‑to‑skip: w czarnej dziurze jak wcześniej; w nadświetlnej skacze do wyjścia (5.9 s).
- Test headless 390×844 (zamrożony zegar): brak błędów gry, strefa 2 po przejściu; desktop 1280×800: 800 smug, skip OK. Zrzuty `shots/hs2_*.png`, wideo `shots/hs2_transition.mp4` (2.5–8.0 s przejścia).

## 2026-10-17 — Nazwa „Aetheris” + ikona aplikacji (bóstwo)
- Decyzja Jacka: gra nazywa się teraz **Aetheris** we wszystkich wersjach (PL/EN/NO): `<title>`, tytuł w menu, `apple-mobile-web-app-title`, `application-name`, manifest. Fabuła/ekran końcowy już używały „Aetheris”. URL bez zmian: stop60.no/zyrosfera/ (ukryty, noindex).
- Nowa ikona: Strażniczka Aetheris — świetliste bóstwo z aureolą i promieniami, trzymające Serce Równowagi (szklana sfera z cyjanowo-fioletową energią i pierścieniem orbity). Generowana proceduralnie: `tools/make_icon.py` → `icons/icon-1024.png`.
- Pliki: `apple-touch-icon.png` (180), `icons/icon-192.png`, `icons/icon-512.png`, `icons/icon-maskable-192/512.png`, `icons/favicon-32.png`, `favicon.ico`, `manifest.webmanifest` (nowy, display: browser). Linki z `?v=2` (cache-bust; brak service workera w projekcie).
- Podgląd: `shots/icon_deity_preview.png`. Na iPhonie trzeba usunąć stary skrót z ekranu głównego i dodać ponownie.

## 2026-10-17 — Ikona „orb” + animowany splash (Grok)
- Ikona bogini (3eca099) odrzucona przez Jacka → wszystkie ikony z `orb_1` (proceduralna kula energii): `apple-touch-icon.png` 180, `icons/apple-touch-icon-180.png`, `icon-192/512`, `icon-maskable-192/512` (mniejsza kula R=0.29, mieści się w strefie 80%, to samo tło bez szwu), `favicon-32` + `favicon.ico` (16–64, przycięte), `icon-1024`. Generator: `python3 tools/make_orb_icon.py --icons .` (stary `tools/make_icon.py` usunięty). Linki `?v=3` w `index.html` i `manifest.webmanifest`.
- Splash po otwarciu gry (`#splash`, nad menu): animowana kula `media/orb_anim.mp4` (H.264 Main, 400×400, 2 s pętla, bez audio, 58 KB; zapas `orb_anim.webm` VP9 74 KB), `muted playsinline autoplay loop`, poster/fallback `media/orb_poster.jpg` (orb_1, 23 KB). Pod kulą tytuł „Aetheris” i podpowiedź w języku gracza (PL „Dotknij, aby kontynuować” / EN „Tap to continue” / NO „Trykk for å fortsette”). Znika po 2,6 s albo po dotknięciu (fade 0,55 s), potem menu Start bez zmian; po zamknięciu wideo zatrzymane i zwolnione.
- Fallback: wideo jest niewidoczne dopóki nie wyemituje `playing` — jeśli autoplay zablokowany (np. tryb niskiego zużycia energii na iOS) lub plik nie wczyta się, widać statyczną kulę (bez ikony „play”).
- Test headless Chrome 390×844 @3x, UA iPhone iOS 26: PL/EN/NO, auto-zamknięcie i tap, fallback z zablokowanym wideo, Start → prolog → gra. Brak błędów gry w konsoli (lokalnie tylko 404 `/count.js`). Zrzuty: `shots/orb_splash_*.png`, `shots/orb_icons_preview.png`.
- iPhone: stary skrót na ekranie głównym trzeba usunąć i dodać ponownie (Udostępnij → Do ekranu początkowego), żeby pojawiła się nowa ikona.

## 2026-10-17 — Zmiana nazwy: Aetheris → **Aspheris** (Grok)
- Powód: „AETHERIS” już istnieje na Steamie. Sprawdzenie nazwy „Aspheris” (Steam, itch.io, App Store, Google Play, web, ślady znaków towarowych): brak gry ani aplikacji o tej nazwie — tylko niezwiązane użycia (profil użytkownika Steam, nick Discord, domena ENS aspheris.eth).
- Gra nazywa się teraz **Aspheris** we wszystkich językach (PL/EN/NO): `<title>`, `apple-mobile-web-app-title`, `application-name`, manifest `name`/`short_name`, tytuł na splashu i w menu, prolog („stacja Aspheris”), ekran końcowy („Serce bije. Aspheris żyje.” / „The Heart beats. Aspheris lives.” / „Hjertet slår. Aspheris lever.”), GDD.md, README.md. Stacja w fabule też nazywa się Aspheris. Starsze wpisy powyżej zostawione bez zmian jako historia.
- URL bez zmian: stop60.no/zyrosfera/ (ukryty, noindex). Cache-bust ikon/manifestu/postera: `?v=4`.
- Test headless Chrome 390×844 PL/EN/NO: tytuł, splash, menu, prolog OK; brak błędów gry w konsoli (lokalnie tylko 404 `/count.js`). Zrzuty: `shots/aspheris_title.png` (+ `_en`, `_no`, `aspheris_splash.png`, `aspheris_prolog_*.png`).
