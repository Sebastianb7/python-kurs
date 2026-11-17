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
1. Przełącz się na branch lekcji: `git switch 01-zmienne-i-typy`
2. Sprawdź stan: `git status`
3. Edytuj `lekcje/01_zmienne.py` i wykonaj zadania poniżej.
4. Dodaj zmiany do stage: `git add lekcje/01_zmienne.py POSTEP.md`
5. Zrób commit: `git commit -m "feat(lekcja-01): zmienne i typy danych"`
6. Zobacz historię: `git log --oneline`
7. Wypchnij branch: `git push -u origin 01-zmienne-i-typy`
8. Na GitHubie otwórz Pull Request (PR) z brancha `01-zmienne-i-typy` do `main`.

## Zadania
1. Utwórz zmienne: `tytul` (str), `autor` (str), `rok_wydania` (int), `cena` (float), `dostepna` (bool).
2. Wypisz każdą zmienną w osobnej linii przez `print`.
3. Wypisz typ każdej zmiennej przez `type()`.
4. Pobierz od użytkownika tytuł przez `input()` i wypisz komunikat `Dodano: <tytuł>`.
5. Dopisz na końcu `POSTEP.md` linię: `- [x] 01 Zmienne i typy`.

## Kryteria ukończenia
- Plik `lekcje/01_zmienne.py` uruchamia się bez błędu: `python lekcje/01_zmienne.py`.
- Commit ma czytelny komunikat.
- Pull Request do `main` jest otwarty.