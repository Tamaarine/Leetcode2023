from typing import *
from collections import *

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        counter = defaultdict(int)
        trusted = [False for _ in range(n)]
        
        for pair in trust:
            counter[pair[1]] += 1
            trusted[pair[0] - 1] = True
        for person, count in counter.items():
            if count == n - 1 and not trusted[person - 1]:
                return person
        return -1

s = Solution()
print(s.findJudge(2, [[1, 2]]))
