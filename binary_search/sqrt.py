from typing import *

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        out = x
        while left <= right:
            mid = (right - left) // 2 + left
            
            res = mid * mid
            if res == x:
                # Perfect square
                return mid
            elif res > x:
                # Too big, reduce it
                right = mid - 1
            else:
                # Too small, keep it as out and increase it
                left = mid + 1
                out = mid
        return out

s = Solution()
for i in range(1, 101):
    print(f"sqrt({i}) = {s.mySqrt(i)}")
