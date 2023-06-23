from typing import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Search through the rows first
        left = 0
        right = len(matrix) - 1
        
        while left <= right:
            mid = (right - left) // 2 + left
            row_left_val = matrix[mid][0]
            row_right_val = matrix[mid][-1]
            
            if row_left_val <= target <= row_right_val:
                # The value is within this row, binary search it
                left = 0
                right = len(matrix[0]) - 1
                while left <= right:
                    row_mid = (right - left) // 2 + left
                    mid_val = matrix[mid][row_mid]
                    if mid_val == target:
                        return True
                    elif mid_val < target:
                        left = row_mid + 1
                    else:
                        right = row_mid - 1
                return False
            elif target > row_right_val:
                left = mid + 1
            else:
                right = mid - 1
        return False

s = Solution()
mat1 = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
print(s.searchMatrix(mat1, 3))
print(s.searchMatrix(mat1, 60))
print(s.searchMatrix(mat1, 5))
print(s.searchMatrix(mat1, 50))
print(s.searchMatrix(mat1, 13))
