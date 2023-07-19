from typing import *
from collections import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        
        min_num = min(nums)
        max_num = max(nums)
        c = [0] * (max_num - min_num + 1)
        
        for num in nums:
            c[num - min_num] += 1
        
        j = 0 # Used for writing over nums
        for index in range(len(c)):
            while c[index] > 0:
                nums[j] = index + min_num
                j += 1
                c[index] -= 1

s = Solution()
org = [0, 1, 1, 2, 1, 1, 3]
s.sortColors(org)
print(org)

org = [0]
s.sortColors(org)
print(org)

org = []
s.sortColors(org)
print(org)