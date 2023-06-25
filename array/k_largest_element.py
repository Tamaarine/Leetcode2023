from typing import *
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # Runs in O(n)
        
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))