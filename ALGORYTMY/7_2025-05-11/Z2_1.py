def flood_fill_dfs(bitmap, x, y, old_color, new_color):
    # sprawdznie granic
    if x < 0 or y < 0 or x >= len(bitmap) or y >= len(bitmap[0]) or bitmap[x][y] != old_color:
        return None

    # zmiana koloru
    bitmap[x][y] = new_color

    # wywolania dla sasiadujacych pixeli (up, dn, r, l)
    flood_fill_dfs(bitmap, x + 1, y, old_color, new_color)
    flood_fill_dfs(bitmap, x - 1, y, old_color, new_color)
    flood_fill_dfs(bitmap, x, y + 1, old_color, new_color)
    flood_fill_dfs(bitmap, x, y - 1, old_color, new_color)

def apply_flood_fill_dfs(bitmap, start, new_color):
    x, y = start
    old_color = bitmap[x][y]
    if old_color != new_color:
        flood_fill_dfs(bitmap, x, y, old_color, new_color)

# Przykład użycia
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
selected_pixel = (4, 4)
new_value = 2

apply_flood_fill_dfs(bitmap, selected_pixel, new_value)

print("DFS Result:")
for row in bitmap:
    print(row)
