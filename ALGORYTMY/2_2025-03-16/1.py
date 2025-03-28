import random

array100 = [random.randint(0, 100) for _ in range(100)]
array10k = [random.randint(0, 10000) for _ in range(10000)]
array1M = [random.randint(0, 1000000) for _ in range(1000000)]


#O(1)
def get_indicated_element(array, index):
    o1counter = 0
    o1counter = o1counter + 1
    return array[index], o1counter

tmp1 = get_indicated_element(array100, 99)
tmp2 = get_indicated_element(array10k, 99)
tmp3 = get_indicated_element(array1M, 99)
print(f"ELEM: {tmp1[0]} / C: {tmp1[1]}")
print(f"ELEM: {tmp2[0]} / C: {tmp2[1]}")
print(f"ELEM: {tmp3[0]} / C: {tmp3[1]}")

#O(n)
def search_array(array, target):
    oncounter = 0
    for i in range(len(array)):
        oncounter = oncounter + 1
        if array[i] == target:
            return i, oncounter
    return -1, oncounter

tmp1 = search_array(array100, 123)
tmp2 = search_array(array10k, 123)
tmp3 = search_array(array1M, 123)
print(f"POS: {tmp1[0]} / C: {tmp1[1]}")
print(f"POS: {tmp2[0]} / C: {tmp2[1]}")
print(f"POS: {tmp3[0]} / C: {tmp3[1]}")

#O(n^2)
def bubble_sort(arr):
    on2counterif = 0
    on2counterset = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            on2counterif = on2counterif + 1
            if arr[j] > arr[j+1]:
                on2counterset = on2counterset + 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return on2counterif, on2counterset, arr

tmp1 = bubble_sort(array100)
#tmp2 = bubble_sort(array10k)
#tmp3 = bubble_sort(array1M)
print(f"Cif: {tmp1[0]} / Cset: {tmp1[1]}")
#print(tmp1[2])
#print(f"Cif: {tmp2[0]} / Cset: {tmp2[1]}")
#print(f"Cif: {tmp3[0]} / Cset: {tmp3[1]}")

#O(a^n) -> #O(2^n)
def generate_combinations(elements, counter=[0]):
    # counter[0] += 1
    if not elements:
        return [[]], counter
    
    first = elements[0]
    rest_combinations, counter = generate_combinations(elements[1:], counter)
    result = []

    for combo in rest_combinations:
        counter[0] += 1
        result.append(combo)
        result.append([first] + combo)

    return result, counter

array10 = [random.randint(0, 1000000) for _ in range(10)]
combinations, counter = generate_combinations(array10)
print(f"COMBO_C: {counter[0]}")
print(f"COMBO_LEN: {len(combinations)}")