from typing import *
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # Runs in O(n)
        
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # This is done by using counting sort
        min_num = min(nums)
        max_num = max(nums)
        
        count_arr = [0] * (max_num - min_num + 1)
        for num in nums:
            count_arr[num - min_num] += 1
        for i in range(len(count_arr) - 1, -1, -1):
            if k <= count_arr[i]:
                return i + min_num
            else:
                k -= count_arr[i]

s = Solution2()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))