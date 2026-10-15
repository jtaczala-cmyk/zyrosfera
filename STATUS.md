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

## Otwarte
- Test na prawdziwym telefonie (wydajność, żyroskop na iOS).
- Nazwa „ŻyroSfera” — nie znaleziono konfliktu znaków towarowych w kodzie/zasobach (brak cudzych assetów); formalnie niesprawdzone w rejestrze.
- Więcej poziomów / przeszkody wg GDD.

Stop60 skończył — Grok może pracować na gałęzi i otwierać PR
