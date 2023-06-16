from typing import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking rows
        dict = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue
                if val not in dict:
                    dict[val] = 1
                else:
                    return False
            dict.clear()
        # Column order check
        for j in range(len(board[0])):
            for i in range(len(board)):
                val = board[i][j]
                if val == ".":
                    continue
                if val not in dict:
                    dict[val] = 1
                else:
                    return False
            dict.clear()
        # Square check
        for i in range(3):
            for j in range(3):
                if not self.checkSquare(board, i, j, dict):
                    return False
                dict.clear()
        return True
                
    def checkSquare(self, board, i, j, dict):
        for x in range(i * 3, i * 3 + 3):
            for y in range(j * 3, j * 3 + 3):
                val = board[x][y]
                if val == ".":
                    continue
                if val not in dict:
                    dict[val] = 1
                else:
                    return False
        return True
        
s = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board1 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = [[".",".",".",".","5",".",".","1","."],
          [".","4",".","3",".",".",".",".","."],
          [".",".",".",".",".","3",".",".","1"],
          ["8",".",".",".",".",".",".","2","."],
          [".",".","2",".","7",".",".",".","."],
          [".","1","5",".",".",".",".",".","."],
          [".",".",".",".",".","2",".",".","."],
          [".","2",".","9",".",".",".",".","."],
          [".",".","4",".",".",".",".",".","."]]
print(s.isValidSudoku(board))
print(s.isValidSudoku(board1))
