from datetime import datetime, timedelta
import random

def zapisz_wizyte(odwiedziny, wspolrzedne, czas=None):
    if czas is None:
        czas = datetime.now()
    odwiedziny[wspolrzedne] = czas

lokalizacje = [
    (52.41, 16.93),
    (52.40, 16.90),
    (52.42, 16.91),
    (52.39, 16.92),
    (52.38, 16.94),
    (52.43, 16.95),
    (52.44, 16.92),
    (52.37, 16.90),
    (52.36, 16.91),
    (52.35, 16.93)
]

odwiedziny = {}

# Ustawienie początkowego czasu dla symulacji
aktualny_czas = datetime.now()

# Symulacja wywołania funkcji 25 razy
for i in range(25):
    # Wybieramy losowo jedną z 10 lokalizacji
    wsp = random.choice(lokalizacje)
    zapisz_wizyte(odwiedziny, wsp, aktualny_czas)
    
    # Co 5 wywołań dodajemy jeden dzień, w pozostałych losowo 8 lub 12 godzin
    if (i + 1) % 5 == 0:
        aktualny_czas += timedelta(days=1)
    else:
        aktualny_czas += timedelta(hours=random.choice([8, 12]))

# Przeszukiwanie słownika: wypisujemy lokalizacje, w których czas wizyty przypada na zadany dzień.
# Przykładowo, jako zapytany dzień wybieramy dzień poprzedni względem aktualnego czasu po symulacji.
query_date = (aktualny_czas - timedelta(days=1)).date()

print(f"Lokalizacje odwiedzone w dniu {query_date}:")
for coords, timestamp in odwiedziny.items():
    if timestamp.date() == query_date:
        print(f"Lokalizacja: {coords} - Czas wizyty: {timestamp}")

# Złożoność obliczeniowa wyszukiwania po wartościach hashmapy:
print("\nZłożoność obliczeniowa wyszukiwania po wartościach hashmapy:")
print("O(n) - w najgorszym przypadku musimy przejrzeć wszystkie pary klucz-wartość, aby znaleźć te spełniające dany warunek.")
