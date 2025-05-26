from collections import deque

def flood_fill_bfs(bitmap, start, new_color):
    x, y = start
    old_color = bitmap[x][y]
    
    if old_color == new_color:
        return None
    
    queue = deque([(x, y)])
    
    while queue:
        cx, cy = queue.popleft()
        
        if cx < 0 or cy < 0 or cx >= len(bitmap) or cy >= len(bitmap[0]) or bitmap[cx][cy] != old_color:
            continue
        
        bitmap[cx][cy] = new_color
        
        # dodanie sąsiadujących pikseli do kolejki (up, dn, r, l)
        queue.append((cx + 1, cy))
        queue.append((cx - 1, cy))
        queue.append((cx, cy + 1))
        queue.append((cx, cy - 1))

# przykład użycia
bitmap_bfs = [
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

flood_fill_bfs(bitmap_bfs, selected_pixel, new_value)

print("\nBFS Result:")
for row in bitmap_bfs:
    print(row)
