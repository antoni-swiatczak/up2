def permutacje(ciag):
    
    if len(ciag) == 1:
        return [ciag]

    wynik = []
    
    for i, litera in enumerate(ciag):
        pozostale = ""
        for j in range(len(ciag)):
            if j != i:
                pozostale += ciag[j]

        for p in permutacje(pozostale):
            wynik.append(litera + p)
    
    return wynik

ciag = "abc"
print(permutacje(ciag))