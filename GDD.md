# Aetheris — GDD

**Nazwa:** Aetheris  
**Bohater:** Lumen

## Przejście przez czarną dziurę

Po ukończeniu sektora Lumen wlatuje w **czarną dziurę** — portal, który przenosi ją do następnego świata / wymiaru.

### Jak to działa
1. Gracz zbiera wszystkie fragmenty w sektorze.
2. Pojawia się czarna dziura (horyzont zdarzeń, zakrzywione światło).
3. Lumen wlatuje w nią — krótka sekwencja przejścia (3–5 sekund).
4. Po drugiej stronie jest nowy sektor z inną paletą kolorów i atmosferą.

### Uczta dla oczu i uszu
- **Wizualnie:** zakrzywienie przestrzeni, światło rozciągnięte w pierścienie, filamenty sfery rozciągają się, bloom intensywnieje, kolory przechodzą z jednej palety w drugą.
- **Dźwiękowo:** niski, narastający drone + wysokie harmoniczne, które się zlewają. Krótki impuls ciszy tuż przed wyjściem. Po wyjściu — nowy ambient sektora.
- **Sterowanie:** w trakcie przejścia sfera jest przyciągana do centrum. Gracz może delikatnie korygować, ale nie zatrzymać.

### Znaczenie fabularne
Czarna dziura to nie tylko portal. To miejsce, gdzie Drift jest najsilniejszy. Każde przejście jest ryzykowne — jeśli Lumen za długo zostaje w horyzoncie, Drift zaczyna ją pochłaniać (wizualne zniekształcenie, spadek prędkości).

### Technicznie (dla Stop60)
- Krótka animacja / shader przejścia (nie pełny cutscene).
- Zmiana tła, świateł i koloru kryształów po wyjściu.
- Dźwięk generowany lub prosty sample (bez ciężkich assetów).
- Wydajność: bloom może być mocniejszy tylko w trakcie przejścia.

## Pozostałe elementy
Pełna fabuła, dialogi PL/EN/NO i sektory są w PR z gałęzi `grok/gdd-fabuła`. Ten dokument uzupełnia je o mechanikę przejścia.

---
Do akceptacji przez Jacka.
