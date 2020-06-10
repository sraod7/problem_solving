from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    old = image[sr][sc]
    new = newColor
    row, col = len(image), len(image[0])

    def dfs_helper(i, j):
        if i >= row or i < 0 or j >= col or j < 0:
            return
        if image[i][j] != old or image[i][j] == new:
            return

        image[i][j] = new
        dfs_helper(i + 1, j)
        dfs_helper(i - 1, j)
        dfs_helper(i, j + 1)
        dfs_helper(i, j - 1)

    dfs_helper(sr, sc)

    return image

def floodFill2(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    r, c = len(image), len(image[0])
    color = image[sr][sc]

    def dfs(i, j):
        if i < 0 or i >= r or j < 0 or j >= c:
            return
        if image[i][j] == newColor or image[i][j] != color:
            return
        image[i][j] = newColor
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    dfs(sr, sc)
    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
