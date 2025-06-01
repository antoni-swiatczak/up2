import re
from collections import defaultdict

def count_words_by_letter(text):
    # Usunięcie interpunkcji i zamiana na małe litery
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()

    letter_count = defaultdict(int)

    print(letter_count)

    for word in words:
        if word:  # Sprawdzenie, czy słowo nie jest puste
            letter_count[word[0]] += 1

    # Sortowanie według liczby wystąpień malejąco
    sorted_counts = dict(sorted(letter_count.items(), key=lambda x: x[1], reverse=True))

    return sorted_counts

# Przykładowy tekst
text = """W rozległych połaciach zielonych pól, gdzie wiatr szepce cicho wśród wysokich traw, 
istnieją opowieści przekazywane z pokolenia na pokolenie. Pewnego dnia, gdy słońce górowało na horyzoncie,
młody chłopiec o imieniu Antoni wyruszył na wyprawę w poszukiwaniu tajemniczych ścieżek skrytych w lesie.
Niepewność mieszała się z ekscytacją, lecz odwaga prowadziła go przez gęste zarośla. Spotkał starego mędrca,
który opowiadał historie pełne magii i legend o dawnych czasach. Słowa płynęły niczym melodyjna pieśń,
a każda kolejna fraza układała się w pełną emocji opowieść, przyciągając młodzieńca coraz głębiej w świat fantazji..."""
# Generowanie wyników
result = count_words_by_letter(text)
print(result)
