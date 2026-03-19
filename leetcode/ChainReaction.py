def init():
    grid = [[3, 1, 2, 1], [1, 1, 1, 4], [3, 1, 2, 2], [3, 3, 3, 4]]
    rows = len(grid)
    columns = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited_graph = [[False] * columns for _ in range(rows)]

    def is_eligible(i, j):
        cell_value = grid[i][j]
        count = 0
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == cell_value:
                count += 1
        return count >= 2

    def mark_explosion(i, j, vg):
        cell_value = grid[i][j]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == cell_value:
                vg[nr][nc] = True

    for r in range(rows):
        for c in range(columns):
            if is_eligible(r, c):
                mark_explosion(r, c, visited_graph)
                visited_graph[r][c] = True
    return visited_graph


print(init())
