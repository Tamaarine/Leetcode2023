from typing import *

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image, visited, i, j):
            nonlocal n, m, color
            
            # Mark it as visited
            visited[i][j] = 1
            
            for row, col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row = i + row
                new_col = j + col
                
                if 0 <= new_row < n and 0 <= new_col < m:
                    if visited[new_row][new_col] == 0 and image[new_row][new_col] == image[i][j]:
                        # It hasn't been visited and is the same color
                        # We visit it first, then mark it as target
                        dfs(image, visited, new_row, new_col)
                        image[new_row][new_col] = color
            # Then after the neighbnors has been converted we convert ourselves
            image[i][j] = color
        
        n = len(image)
        m = len(image[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        
        # Start the dfs at the source
        dfs(image, visited, sr, sc)
        return image

s = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
print(s.floodFill(image, 1, 1, 2))

image = [[0,0,0],[0,0,0]]
print(s.floodFill(image, 0, 0, 3))