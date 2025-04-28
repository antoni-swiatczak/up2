import random

def insertion_sort(array):
    comparisons = 0
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            comparisons += 1
        array[j + 1] = key
        comparisons += 1
    return comparisons

def merge(array, left, mid, right):
    comparisons = 0
    left_part = array[left:mid + 1]
    right_part = array[mid + 1:right + 1]
    
    i = 0
    j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1
        k += 1
        comparisons += 1

    while i < len(left_part):
        array[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        array[k] = right_part[j]
        j += 1
        k += 1

    return comparisons

def merge_sort(array, left, right, run_size):
    comparisons = 0
    if right - left + 1 <= run_size:
        comparisons += insertion_sort(array[left:right + 1])
    else:
        mid = (left + right) // 2
        comparisons += merge_sort(array, left, mid, run_size)
        comparisons += merge_sort(array, mid + 1, right, run_size)
        comparisons += merge(array, left, mid, right)
    return comparisons

def hybrid_sort(array, run_size):
    total_comparisons = merge_sort(array, 0, len(array) - 1, run_size)
    return total_comparisons

def run_tests():
    # Funkcja pomocnicza do generowania różnych przypadków testowych
    def generate_test_cases(size):
        sorted_array = list(range(1, size + 1))  # Posortowana rosnąco
        partially_sorted = sorted_array[:int(size * 0.7)] + random.sample(sorted_array[int(size * 0.7):], size - int(size * 0.7))
        random_array = random.sample(sorted_array, size)  # Losowa
        reversed_array = sorted_array[::-1]  # Odwrotnie posortowana
        return [
            ("Sorted", sorted_array),
            ("Partially Sorted", partially_sorted),
            ("Random", random_array),
            ("Reversed", reversed_array)
        ]

    # Rozmiary runów do przetestowania
    run_sizes = [16, 32, 64]
    # Rozmiary tablic do przetestowania
    array_sizes = [10, 100, 1000]

    # Wyniki testów
    results = []

    for size in array_sizes:
        print(f"\n--- Array Size: {size} ---")
        test_cases = generate_test_cases(size)
        
        for case_name, array in test_cases:
            for run_size in run_sizes:
                array_copy = array[:]
                comparisons = hybrid_sort(array_copy, run_size)
                results.append((size, case_name, run_size, comparisons))
                print(f"Case: {case_name}, Run Size: {run_size}, Comparisons: {comparisons}")

    return results

# Uruchomienie testów
test_results = run_tests()