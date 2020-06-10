from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    current_area = []
    max_area = 0
    area = 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return
        if grid[i][j] == 0:
            return
        grid[i][j] = 0
        current_area.append(1)
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                dfs(row, col, )
                max_area = max(max_area, sum(current_area))
                current_area = []

    return max_area

print(maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))