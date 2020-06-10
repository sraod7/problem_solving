def numIslands(grid) -> int:
    islands = 0
    if not grid:
        return islands

    def _dfs(gd, r, c):

        if r < 0 or c < 0 or r >= len(gd) or c >= len(gd[0]) or gd[r][c] == 0:
            return

        gd[r][c] = 0

        _dfs(gd, r + 1, c)
        _dfs(gd, r - 1, c)
        _dfs(gd, r, c - 1)
        _dfs(gd, r, c + 1)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                _dfs(grid, row, col)
                islands = islands + 1

    return islands


a = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(numIslands(a))
