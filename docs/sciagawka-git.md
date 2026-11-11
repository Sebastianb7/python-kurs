# Ściągawka Git

## Podstawy
| Cel | Komenda |
|-----|---------|
| Status repozytorium | `git status` |
| Dodaj wszystko do commita | `git add -A` |
| Dodaj wybrany plik | `git add plik.py` |
| Commit | `git commit -m "feat: opis"` |
| Historia | `git log --oneline --graph --all` |
| Różnice (niezastage'owane) | `git diff` |
| Różnice (zastage'owane) | `git diff --staged` |
| Pokaż commit | `git show <hash>` |

## Branche
| Cel | Komenda |
|-----|---------|
| Lista branchy lokalnych | `git branch` |
| Lista wszystkich | `git branch -a` |
| Nowy branch | `git switch -c nazwa` |
| Przełącz się | `git switch nazwa` |
| Usuń lokalny (bezpiecznie) | `git branch -d nazwa` |
| Usuń lokalny (wymuszenie) | `git branch -D nazwa` |
| Usuń zdalny | `git push origin --delete nazwa` |
| Wypchnij nowy branch | `git push -u origin nazwa` |

## Scalanie i konflikty
| Cel | Komenda |
|-----|---------|
| Scal branch | `git merge nazwa` |
| Przerwij merge | `git merge --abort` |
| Po rozwiązaniu konfliktu | `git add plik && git commit` |

Znaczniki konfliktu w pliku:
```
<<<<<<< HEAD
twoja wersja
=======
wersja z drugiego brancha
>>>>>>> nazwa-brancha
```

## Cherry-pick
| Cel | Komenda |
|-----|---------|
| Przenieś jeden commit | `git cherry-pick <hash>` |
| Przerwij | `git cherry-pick --abort` |
| Kontynuuj po konflikcie | `git cherry-pick --continue` |

## Cofanie zmian
| Cel | Komenda |
|-----|---------|
| Cofnij zmiany w pliku | `git restore plik.py` |
| Usuń z staging | `git restore --staged plik.py` |
| Popraw ostatni commit | `git commit --amend` |
| Cofnij commit bezpiecznie | `git revert <hash>` |
| Przesuń branch wstecz | `git reset --soft/--mixed/--hard HEAD~1` |
| Tymczasowy schowek | `git stash` / `git stash pop` |
| Odzyskiwanie | `git reflog` |

## Historia i przepisywanie
| Cel | Komenda |
|-----|---------|
| Rebase na main | `git rebase main` |
| Interaktywny rebase | `git rebase -i HEAD~3` |
| Szukaj w commitach | `git log --grep="tekst"` |
| Kto zmienił linię | `git blame plik.py` |

## Tagi
| Cel | Komenda |
|-----|---------|
| Tag adnotowany | `git tag -a v1.0.0 -m "opis"` |
| Wypchnij tagi | `git push origin --tags` |

## Ignorowanie
Plik `.gitignore` wyklucza pliki z repozytorium. Pliki już śledzone usuwasz z gita tak:
`git rm --cached plik`.
