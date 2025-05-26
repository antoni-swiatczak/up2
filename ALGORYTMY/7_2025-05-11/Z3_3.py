def thresholding(bitmap, threshold):
    for i in range(len(bitmap)):
        for j in range(len(bitmap[i])):
                if bitmap[i][j] <= threshold:
                    bitmap[i][j] = 0
                else:
                    bitmap[i][j] = 1

bitmap = [
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [8, 1, 1, 8, 8, 1, 1, 1, 2],
    [7, 1, 1, 1, 8, 1, 1, 1, 3],
    [6, 1, 1, 1, 8, 8, 1, 1, 4],
    [5, 1, 1, 8, 8, 8, 1, 1, 5],
    [4, 1, 8, 8, 8, 1, 1, 1, 6],
    [3, 1, 1, 1, 8, 8, 1, 1, 7],
    [2, 1, 1, 1, 1, 8, 8, 8, 8],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]

thresholding(bitmap, 4)

print("\nThresholding:")
for row in bitmap:
    print(row)