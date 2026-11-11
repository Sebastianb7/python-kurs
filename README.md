# Kurs: Python + Git na projekcie Biblioteka

Projekt testowy, w którym uczysz się Pythona i pracy z Gitem. Każda lekcja to osobny branch
z opisem zadań w pliku `README.md`. Wykonujesz zadania, robisz commity, wypychasz branch
i otwierasz Merge Request (MR) / Pull Request (PR) do `main`.

## Wymagania
- Python 3.10 lub nowszy (`python3 --version`)
- Git 2.28 lub nowszy (`git --version`)
- Konto na GitHub lub GitLab
- Edytor kodu (np. VS Code)

## Przygotowanie (zrób raz)
1. Utwórz pusty projekt na GitHub/GitLab (bez README, bez .gitignore).
2. Zaimportuj repozytorium lokalnie:
   ```bash
   git clone <adres-repo-instruktora> python-git-kurs
   cd python-git-kurs
   git remote set-url origin <TWOJ-ADRES-REPO>
   git push --all origin
   git push --tags origin
   ```
3. Sprawdź branche: `git branch -a`

## Kolejność lekcji i tematy

| Nr | Branch | Python | Git |
|----|--------|--------|-----|
| 01 | `01-zmienne-i-typy` | zmienne, typy, `input`, `print` | `status`, `add`, `commit`, `log`, `push` |
| 02 | `02-warunki-i-petle` | `if/elif/else`, `for`, `while` | `diff`, `diff --staged`, dobre commity |
| 03 | `03-funkcje` | `def`, argumenty, `return` | `switch`, `branch`, `branch -d` |
| 04 | `04-kolekcje` | listy, słowniki, zbiory, krotki | `stash`, `restore`, `reset` |
| 05 | `05-klasy-i-obiekty` | klasy, obiekty, `__init__`, metody | `commit --amend`, `show`, `log --graph` |
| 06 | `06-dziedziczenie` | dziedziczenie, polimorfizm | `revert` |
| 07 | `07-wyjatki-i-pliki` | `try/except`, pliki, JSON | `.gitignore`, `rm --cached` |
| 08 | `08-testy-pytest` | `pytest`, asercje, testy jednostkowe | `log --grep`, `blame` |
| 09 | `09-konflikt-a` + `09-konflikt-b` | praca z modułami | **konflikty przy merge**, `merge --abort` |
| 10 | `10-cherry-pick` (+ `10-zrodlo-statystyki`) | moduł statystyk | **cherry-pick** |
| 11 | `11-rest-api` | Flask, REST, JSON, HTTP | **MR/PR**, push `-u`, review |
| 12 | `12-rebase-i-historia` | refaktoryzacja | **rebase -i**, squash, fixup, reflog |
| 13 | `13-release` | wersjonowanie | **tag**, `push --tags`, usuwanie branchy |

## Jak oddawać lekcję
1. `git switch <branch-lekcji>`
2. Wykonaj zadania z `README.md` danego brancha.
3. Commituj małymi krokami z sensownymi komunikatami.
4. `git push -u origin <branch-lekcji>`
5. Otwórz MR/PR do `main` z opisem wykonanych zadań.
6. Po akceptacji instruktora zscal (merge) do `main`.

Uwaga: pliki `README.md` i `POSTEP.md` są zmieniane w wielu branchach. Przy scalaniu
do `main` pojawią się konflikty. To celowe, bo są częścią nauki. Zachowaj zawartość
z obu stron i dopisz swoją linię do `POSTEP.md`.

Ściągawka z komendami Git: `docs/sciagawka-git.md`.
