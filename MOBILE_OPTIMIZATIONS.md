# Mobile Optimizations — PR #7

## Cel
Utrzymać płynną grę na iPhonie (szczególnie starszych) bez dużej utraty jakości wizualnej.

## Aktualny stan
Gra ma już adaptive quality (obniża pixel ratio i bloom przy niskim FPS). To dobry fundament.

## Proponowane optymalizacje

### 1. Bloom
- Domyślnie połowa rozdzielczości na urządzeniach z `devicePixelRatio > 2`.
- Pełna rozdzielczość tylko podczas krótkich efektów (zbieranie, czarna dziura).

### 2. Cząsteczki
- Ograniczyć trail do 12–16 sprite’ów na słabszych urządzeniach.
- Sparkles: max 150 aktywnych jednocześnie.

### 3. Geometria
- Sfera gracza: 32 segmenty zamiast 48 na mobile.
- Kryształy: flat shading już jest — OK.

### 4. Światła
- Na mobile ograniczyć do 2 PointLight + 1 DirectionalLight.
- Wyłączyć dodatkowe światła kryształów jeśli FPS < 50.

### 5. Adaptive Quality (już jest)
- Zachować obecną logikę.
- Dodać trzeci poziom: wyłączyć trail i zmniejszyć motes do 200.

### 6. Black Hole
- Podczas przejścia tymczasowo obniżyć rozdzielczość bloomu.
- Nie dodawać nowych systemów cząsteczek.

## Priorytet
1. Bloom resolution (największy zysk)
2. Trail length
3. Adaptive quality rozszerzenie

## Test
Po wdrożeniu: test na iPhonie (Safari). Docelowo stabilne 50+ FPS w normalnej grze.
