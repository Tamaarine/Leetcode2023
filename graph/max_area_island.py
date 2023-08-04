from typing import *


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, visited, i, j):
            visited[i][j] = 1

            area = 1
            row_combo = [-1, 1, 0, 0]
            col_combo = [0, 0, 1, -1]

            for row, col in zip(row_combo, col_combo):
                new_row = i + row
                new_col = j + col

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    if visited[new_row][new_col] == 0 and grid[new_row][new_col] == 1:
                        area += dfs(grid, visited, new_row, new_col)
            return area

        max_area = 0

        n = len(grid)
        m = len(grid[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]

        for row in range(n):
            for col in range(m):
                if visited[row][col] == 0 and grid[row][col] == 1:
                    # If the starting land hasn't been visited yet and it is an island
                    ret_area = dfs(grid, visited, row, col)
                    max_area = max(ret_area, max_area)
        return max_area


s = Solution()
grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
print(s.maxAreaOfIsland(grid))

grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
print(s.maxAreaOfIsland(grid))
