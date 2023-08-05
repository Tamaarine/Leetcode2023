from typing import *


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(board, visited, i, j):
            visited[i][j] = 1

            # Because there is no adjacent ships we don't have to worry about
            # the case where two ships are next to each other

            # Discover down
            if (
                0 <= i + 1 < len(board)
                and visited[i + 1][j] == 0
                and board[i + 1][j] == "X"
            ):
                dfs(board, visited, i + 1, j)
            # Discover right
            elif (
                0 <= j + 1 < len(board[0])
                and visited[i][j + 1] == 0
                and board[i][j + 1] == "X"
            ):
                dfs(board, visited, i, j + 1)

        n = len(board)
        m = len(board[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]

        ships = 0
        for row in range(n):
            for col in range(m):
                if visited[row][col] == 0 and board[row][col] == "X":
                    # Find the rest of the part of the ship
                    ships += 1
                    dfs(board, visited, row, col)
        return ships


s = Solution()
board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
print(s.countBattleships(board))

board = [["."]]
print(s.countBattleships(board))