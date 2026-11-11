# Lekcja 01: Zmienne i typy danych

## Cel
Poznasz zmienne, podstawowe typy (`str`, `int`, `float`, `bool`) i wypisywanie danych.
Poznasz też podstawowe polecenia Git: `status`, `add`, `commit`, `log`, `push`.

## Python
- Zmienna: `tytul = "Lalka"`
- Typy: `str`, `int`, `float`, `bool`; sprawdzanie: `type(zmienna)`
- `print()` i f-stringi: `print(f"Książka: {tytul}")`
- `input()` pobiera tekst od użytkownika

## Git
1. Sprawdź stan: `git status`
2. Edytuj `lekcje/01_zmienne.py` (zrób zadania poniżej)
3. Dodaj do stage: `git add lekcje/01_zmienne.py`
4. Zrób commit: `git commit -m "feat(lekcja-01): zmienne i typy danych"`
5. Zobacz historię: `git log --oneline`
6. Wypchnij: `git push -u origin 01-zmienne-i-typy`
7. Otwórz MR/PR do `main`.

## Zadania
1. Utwórz zmienne: `tytul` (str), `autor` (str), `rok_wydania` (int), `cena` (float), `dostepna` (bool).
2. Wypisz każdą zmienną w osobnej linii przez `print`.
3. Wypisz typ każdej zmiennej przez `type()`.
4. Pobierz od użytkownika tytuł przez `input()` i wypisz komunikat `Dodano: <tytuł>`.
5. Dopisz linię do `POSTEP.md`: `- [x] 01 Zmienne i typy`.
6. Dopisz na końcu `README.md` główny (w `main`) podsumowanie — przy merge pojawi się konflikt, rozwiąż go.

## Kryteria ukończenia
- Plik `lekcje/01_zmienne.py` uruchamia się bez błędu: `python lekcje/01_zmienne.py`
- Commit ma czytelny komunikat, MR jest otwarty.
