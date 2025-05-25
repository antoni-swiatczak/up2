def solve_maze(maze, pos, end, path, visited):
    # obecna pozycja
    x, y = pos
    
    # warunek koncowy (cel)
    if pos == end:
        path.append(pos)
        return True
    
    # granice i przeszkody labiryntu
    if (x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] == 1 or pos in visited):
        return False
    
    # oznaczenie obecnej pozycji (odwiedzony + krok)
    visited.append(pos)
    path.append(pos)
    
    # badanie mozliwego ruchu (r, dn, l, up)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in moves:
        if solve_maze(maze, (x + dx, y + dy), end, path, visited):
            return True
    
    # cofanie sie jak slepy zaulek
    path.pop()
    return False

def find_path(maze, start, end):
    path = []
    visited = []
    if solve_maze(maze, start, end, path, visited):
        return path
    return None # nie znaleziono rozwiazania

# przyklad uzycia
maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 1]
]
start = (5, 0)
end = (0, 0)

path = find_path(maze, start, end)
print("Found path:", path)
