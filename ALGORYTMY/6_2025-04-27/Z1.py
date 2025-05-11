# 1. Prosta funkcja haszująca (suma ASCII modulo rozmiar tablicy)
def simple_hash(s, size):
    return sum(ord(char) for char in s) % size

# 2. Funkcja haszująca Hornera (metoda iteracyjnego mnożenia przez bazę)
def horner_hash(s, base=31, size=100):
    hash_value = 0
    for char in s:
        hash_value = hash_value * base + ord(char)
    return hash_value % size

# 3. Funkcja haszująca FNV-1a (szybka i dobrze rozpraszająca)
def fnv1a_hash(s, size=100):
    FNV_OFFSET = 0x811c9dc5
    FNV_PRIME = 0x01000193

    hash_value = FNV_OFFSET
    for char in s:
        hash_value ^= ord(char)
        hash_value *= FNV_PRIME
        hash_value &= 0xFFFFFFFF  # Ograniczenie do 32 bitów
    return hash_value % size

# Testowanie funkcji na przykładowej liście stringów
test_strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
                "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya",
                "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla"]

size = 50  # Rozmiar HashMap

# Generowanie wartości hash dla każdej funkcji
results = {s: (simple_hash(s, size), horner_hash(s, size=size), fnv1a_hash(s, size)) for s in test_strings}

# Wyświetlenie wyników w formie tabeli
print(f"\n{'String':<15}{'Simple Hash':<12}{'Horner Hash':<12}{'FNV-1a Hash':<12}")
print("-" * 50)
for s, (h1, h2, h3) in results.items():
    print(f"{s:<15}{h1:<12}{h2:<12}{h3:<12}")