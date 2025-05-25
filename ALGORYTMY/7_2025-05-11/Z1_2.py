def zapis_binarny(n):
    if n > 1:
        zapis_binarny(n // 2)
    print(n % 2, end="")

liczba = 23
zapis_binarny(liczba)
