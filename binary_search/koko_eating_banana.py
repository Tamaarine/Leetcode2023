from typing import *
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        min_k = right
        while left <= right:
            mid = (right - left) // 2 + left
            
            total = self.totalEatingTime(piles, mid)
            # Only update min_k if total is within range and min_k > mid
            if min_k > mid and total <= h:
                min_k = mid
            
            if total <= h:
                # Try to increase the time by decreasing k
                right = mid - 1
            else:
                # Try to decrease the time to increase k, because k is too small koko can't finish the bananas
                left = mid + 1
        return min_k
            
    def totalEatingTime(self, piles, k):
        sum = 0
        for pile in piles:
            sum += math.ceil(pile / k)
        return sum

s = Solution()
print(s.minEatingSpeed([3, 6, 7, 11], 10))