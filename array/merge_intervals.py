from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals
        
        intervals.sort(key=lambda x : (x[0], x[1]))
        
        res = []
        curr = intervals[0]
        i = 1
        print(intervals)
        while i < len(intervals):
            next = intervals[i]
            
            # [1, 7] and [2, 10]. 7 > 2, the interval overlaps
            # Take the curr[0] and max(right of curr and next)
            if curr[1] >= next[0]:
                curr[1] = max(curr[1], next[1])
            else:
                # They do not overlap. Add it to res as it's own
                # interval. And make next equal to curr
                res.append(curr)
                curr = next
            i += 1
        res.append(curr)
        return res
        

s = Solution()
res = s.merge([[2,6], [1,3], [1, 2], [1,5],[8,10],[15,18]])
print(res)

res = s.merge([[1, 2], [2,3], [3,4],[4,5]])
print(res)

res = s.merge([[1, 100]])
print(res)