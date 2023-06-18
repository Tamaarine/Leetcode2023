from collections import *
from typing import *

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        c = Counter(nums)
        
        max_length = 1
        for num in nums:
            if num - 1 in c:
                continue
            length = 1
            num = num + 1
            while num in c:
                length += 1
                num += 1
            max_length = length if length > max_length else max_length
        return max_length

class Solution2:
    # Damn even though there is a constraint of O(n) run time, it is still faster
    # if you sort lmao. Just have to keep an eye on the edge cases where
    # if the condition last through the entire array
    # just have to put an additional check at the end.
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # Sort the array even though it must run in o(n)
        nums = sorted(nums)
        
        max_length = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                length += 1
            elif nums[i - 1] == nums[i]:
                continue
            else:
                max_length = length if length > max_length else max_length
                length = 1
        
        max_length = length if length > max_length else max_length
        return max_length
    
s = Solution2()
print(s.longestConsecutive([100, 1, 3, 2, 4]))
print(s.longestConsecutive([100, 1, 101, 102, 2, 3, 4, 5]))
print(s.longestConsecutive([100]))
print(s.longestConsecutive([]))
print(s.longestConsecutive([5, 4, 3, 2, 1]))
print(s.longestConsecutive([1, 1, 2]))
