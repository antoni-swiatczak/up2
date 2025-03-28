#a -> C: O(n) / P: O(n)
def move_negatives_to_start(arr):
    negatives = [None] * len(arr)
    positives = [None] * len(arr)
    
    neg_index = 0
    pos_index = 0
    
    for num in arr:
        if num < 0:
            negatives[neg_index] = num
            neg_index += 1
        else:
            positives[pos_index] = num
            pos_index += 1

    negatives = negatives[:neg_index]
    positives = positives[:pos_index]

    return negatives + positives

array = [2, -3, -1, 16, 5, -2, 7, 8]
result = move_negatives_to_start(array)
print(result)

#b -> C: O(n) / P: O(1)
def find_missing_number(arr):
    n = len(array) + 1
    total_sum = (n * (n + 1)) // 2
    actual_sum = 0
    
    for num in arr:
        actual_sum += num

    return total_sum - actual_sum

array = [1, 2, 3, 4, 5, 7, 8]
result = find_missing_number(array)
print(result)

#c -> C: O(n^2) / P: O(n)
def find_duplicates(arr):
    duplicates = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    duplicates = [None] * n
    dup_index = 0

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            is_duplicate = False
            for k in range(dup_index):
                if duplicates[k] == arr[i]:
                    is_duplicate = True
                    break
            if not is_duplicate:
                duplicates[dup_index] = arr[i]
                dup_index += 1

    return duplicates[:dup_index]

array = [7, 4, 2, 4, 5, 6, 2, 7, 7]
result = find_duplicates(array)
print(result)

#d -> C: O(n) / P: O(n)
def reverse_array(arr):
    n = len(arr)
    reversed_arr = [None] * n
    
    for i in range(n):
        reversed_arr[n - i - 1] = arr[i]
    
    return reversed_arr

array = [6, 7, 8, 9, 10]
result = reverse_array(array)
print(result)