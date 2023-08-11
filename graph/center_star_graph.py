from typing import *

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        center = -1
        for i in range(1, len(edges)):
            prev = edges[i - 1]
            curr = edges[i]
            if prev[0] in curr:
                center = prev[0]
            else:
                center = prev[1]
        return center

s = Solution()
print(s.findCenter([[1,2],[2,3],[4,2]]))
print(s.findCenter([[1,2],[5,1],[1,3],[1,4]]))