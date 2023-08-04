from typing import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, visited, i, j):
            # Mark it as visited
            visited[i][j] = 1
            row_combo = [-1, 1, 0, 0]
            col_combo = [0, 0, 1, -1]

            for row, col in zip(row_combo, col_combo):
                new_row = i + row
                new_col = j + col

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    if visited[new_row][new_col] == 0 and grid[new_row][new_col] == "1":
                        dfs(grid, visited, new_row, new_col)

        n = len(grid)
        m = len(grid[0])

        visited = [[0 for _ in range(m)] for _ in range(n)]

        islands = 0

        for row in range(n):
            for col in range(m):
                if visited[row][col] == 0 and grid[row][col] == "1":
                    islands += 1
                    dfs(grid, visited, row, col)
        return islands


def printA(a):
    print("[")
    for row in a:
        print(row)
    print("]")


s = Solution()
print(s.numIslands([["0", "1", "1", "1"], ["1", "1", "0", "0"]]))
print(
    s.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
print(
    s.numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
