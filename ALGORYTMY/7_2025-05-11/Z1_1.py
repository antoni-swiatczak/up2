def permutacje(ciag):
    
    # Jeśli ciąg zawiera tylko jeden znak, zwracamy listę z jednym elementem.
    if len(ciag) == 1:
        return ciag

    # Lista do przechowywania permutacji
    wynik = []
    
    # Iterujemy po indeksach i literach w ciągu wejściowym
    for i, litera in enumerate(ciag):
        # Tworzymy nowy ciąg znaków bez aktualnej litery
        pozostale = ""
        for j in range(len(ciag)):
            if j != i:  # Pomijamy literę na pozycji 'i'
                pozostale += ciag[j]

        # Rekurencyjnie generujemy permutacje dla pozostałych znaków
        for p in permutacje(pozostale):
            # Dodajemy aktualną literę na początek każdej permutacji
            wynik.append(litera + p)
    
    # Zwracamy listę wszystkich możliwych permutacji
    return wynik

# Przykładowe użycie funkcji
ciag = "abc"
print(permutacje(ciag))  # Wyświetlenie wszystkich permutacji ciągu "abc"
