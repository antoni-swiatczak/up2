def zwykly_blur(bitmap):
    for i in range(len(bitmap)):
        for j in range(len(bitmap[i])):
            counter = 0
            tmp_val = 0
            if i > 0 and j > 0:
                counter += 1
                tmp_val += bitmap[i-1][j-1]
            if i > 0:
                counter += 1
                tmp_val += bitmap[i-1][j]
            if i > 0 and j < len(bitmap[i-1])-1:
                counter += 1
                tmp_val += bitmap[i-1][j+1]
            if j > 0:
                counter += 1
                tmp_val += bitmap[i][j-1]
            if True:
                counter += 1
                tmp_val += bitmap[i][j]
            if j < len(bitmap[i])-1:
                counter += 1
                tmp_val += bitmap[i][j+1]
            if i < len(bitmap)-1 and j > 0:
                counter += 1
                tmp_val += bitmap[i+1][j-1]
            if i < len(bitmap)-1:
                counter += 1
                tmp_val += bitmap[i+1][j]
            if i < len(bitmap)-1 and j < len(bitmap[i+1])-1:
                counter += 1
                tmp_val += bitmap[i+1][j+1]
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

zwykly_blur(bitmap)

print("\nZwykly blur:")
for row in bitmap:
    print(row)