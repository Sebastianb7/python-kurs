# Lekcja 01: zmienne i typy danych

# TODO 1: utwórz zmienne: tytul, autor, rok_wydania, cena, dostepna

# TODO 2: wypisz każdą zmienną w osobnej linii (print)

# TODO 3: wypisz typ każdej zmiennej (type)

# TODO 4: pobierz tytuł przez input() i wypisz "Dodano: <tytuł>"

if __name__ == "__main__":
    tytul = "lalka"
    autor = "Bolesław Prus"
    rok_wydania = 1890
    cena = 40.99
    dostepna = True
    
    print(tytul)
    print(autor)
    print(rok_wydania)
    print(cena)
    print(dostepna, "\n")
    
    print(type(tytul))
    print(type(autor))
    print(type(rok_wydania))
    print(type(cena))
    print(type(dostepna), "\n")
    
    tytul = input("Dodaj tytuł: ")
    print(f"Dodano: {tytul}")
    
