from typing import *

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existed = {}
        for n in nums:
            if n in existed:
                return True
            else:
                existed[n] = 1
        return False

# This is a brilliant fucking solution.
# We can just use the built-in set datatype to check
# whether or not there are duplicates.
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)        

s = Solution2()
assert s.containsDuplicate([1, 2, 1, 5]) == True
assert s.containsDuplicate([1, 2, 5]) == False
assert s.containsDuplicate([1]) == False
assert s.containsDuplicate([]) == False
