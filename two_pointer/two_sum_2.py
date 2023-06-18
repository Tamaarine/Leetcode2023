from typing import *
from collections import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        b = len(numbers) - 1
        while f < b:
            if numbers[f] + numbers[b] < target:
                f += 1
            elif numbers[f] + numbers[b] > target:
                b -= 1
            else:
                return f + 1, b + 1

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([2, 3, 4], 6))
print(s.twoSum([-1, 0], -1))