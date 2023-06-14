from typing import *
from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_i in range(len(nums)):
            for index_j in range(index_i + 1, len(nums)):
                if target - nums[index_i] == nums[index_j]:
                    return [index_i, index_j]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = Counter(nums)
        for index in range(len(nums)):
            c[nums[index]] -= 1
            needed = target - nums[index]
            if needed in c and c[needed] > 0:
                if needed == nums[index]:
                    return [index, nums.index(needed, index + 1)]
                return [index, nums.index(needed)]
            c[nums[index]] += 1
                
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Much more elegant solution is just to look forward.
        # Keep an running empty dictionary. If the element
        # is part of the sum, don't worry you will be able to catch
        # it at the second number. Just put it in and then rememebr the index
        # Then in the for loop, just search for the needed, that's it.
        # No need to keep all of them in it at once
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [i, dict[target - num]]
            dict[num] = i

                

s = Solution3()
print(s.twoSum([1, 2, 3, 4, 5, 6, 7, 8], 10))
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
