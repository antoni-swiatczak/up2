def blur_Gausa(bitmap, weights):
    for i in range(len(bitmap)):
        for j in range(len(bitmap[i])):
            counter = 0
            tmp_val = 0
            if i > 0 and j > 0:
                counter += weights[0][0]
                tmp_val += bitmap[i-1][j-1] * weights[0][0]
            if i > 0:
                counter += weights[0][1]
                tmp_val += bitmap[i-1][j] * weights[0][1]
            if i > 0 and j < len(bitmap[i-1])-1:
                counter += weights[0][2]
                tmp_val += bitmap[i-1][j+1] * weights[0][2]
            if j > 0:
                counter += weights[1][0]
                tmp_val += bitmap[i][j-1] * weights[1][0]
            if True:
                counter += weights[1][1]
                tmp_val += bitmap[i][j] * weights[1][1]
            if j < len(bitmap[i])-1:
                counter += weights[1][2]
                tmp_val += bitmap[i][j+1] * weights[1][2]
            if i < len(bitmap)-1 and j > 0:
                counter += weights[2][0]
                tmp_val += bitmap[i+1][j-1] * weights[2][0]
            if i < len(bitmap)-1:
                counter += weights[2][1]
                tmp_val += bitmap[i+1][j] * weights[2][1]
            if i < len(bitmap)-1 and j < len(bitmap[i+1])-1:
                counter += weights[2][2]
                tmp_val += bitmap[i+1][j+1] * weights[2][2]
            if counter != 0:
                bitmap[i][j] = round(tmp_val / counter, 1)

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

weights = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

blur_Gausa(bitmap, weights)

print("\nBlur Gausa:")
for row in bitmap:
    print(row)