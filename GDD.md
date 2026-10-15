# Aetheris — GDD

**Nazwa:** Aetheris  
**Bohater:** Lumen

## Przejście przez czarną dziurę

Po ukończeniu sektora Lumen wlatuje w **czarną dziurę** — portal, który przenosi ją do następnego świata / wymiaru. Samo przejście ma być uczta dla oczu i uszu.

### Jak to działa
1. Gracz zbiera wszystkie fragmenty w sektorze.
2. Pojawia się czarna dziura (horyzont zdarzeń, zakrzywione światło).
3. Lumen wlatuje w nią — sekwencja przejścia (4–6 sekund).
4. Po drugiej stronie jest nowy sektor z inną paletą kolorów i atmosferą.

### Efekty kosmiczne i nieziemskie wrażenia

**Wizualne**
- Przestrzeń zaczyna się zakrzywiać — siatka podłogi rozciąga się w stronę horyzontu.
- Światło z kryształów i sfery rozciąga się w długie, świecące pierścienie (gravitational lensing).
- Filamenty wewnątrz Lumen rozciągają się i zaczynają wirować szybciej.
- Bloom intensywnieje do maksimum, potem na moment gaśnie tuż przed wyjściem.
- Kolory przechodzą płynnie z palety aktualnego sektora w paletę następnego.
- Na brzegach ekranu pojawiają się subtelne zniekształcenia i „przesunięcia” (jakby rzeczywistość się rozrywała).
- Krótkie błyski odległych gwiazd i mgławic w tle, które znikają w horyzoncie.

**Dźwiękowe**
- Niski, narastający drone (sub-bass), który wibruje w słuchawkach / głośniku.
- Wysokie, krystaliczne harmoniczne, które się zlewają i rozciągają.
- Delikatny, niemal niesłyszalny szum „próżni”.
- Tuż przed wyjściem — pół sekundy niemal całkowitej ciszy.
- Po wyjściu — nowy ambient sektora wpada z lekkim echem.

**Odczucie**
- Sfera jest mocno przyciągana do centrum. Gracz może delikatnie korygować, ale nie zatrzymać.
- Lekka wibracja telefonu w trakcie wejścia (jeśli dostępna).
- Krótki moment „bez ciężaru” tuż przed wyjściem.

### Znaczenie fabularne
Czarna dziura to nie tylko portal. To miejsce, gdzie Drift jest najsilniejszy. Każde przejście jest ryzykowne — jeśli Lumen za długo zostaje w horyzoncie, Drift zaczyna ją pochłaniać (wizualne zniekształcenie, spadek prędkości, ciemniejsze kolory).

### Technicznie (dla Stop60)
- Krótka sekwencja shaderowa / post-process (nie pełny cutscene).
- Mocniejszy bloom tylko w trakcie przejścia.
- Zmiana tła, świateł i koloru kryształów po wyjściu.
- Dźwięk generowany proceduralnie lub prosty sample.
- Wydajność: efekt trwa krótko, więc można pozwolić sobie na więcej.

## Pozostałe elementy
Pełna fabuła, dialogi PL/EN/NO i sektory są w PR z gałęzi `grok/gdd-fabuła`. Ten dokument uzupełnia je o mechanikę przejścia.

---
Do akceptacji przez Jacka.
