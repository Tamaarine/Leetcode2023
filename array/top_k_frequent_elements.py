from typing import *
from collections import *
import heapq
import random

class Solution:
    # Theortical O(n) run time. However, in practical sense
    # it is slower than just sorting it and finding the answer
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []
        for num, count in c.items():
            heapq.heappush(heap, (count, num))
        while len(heap) > k:
            heapq.heappop(heap)
        return [pair[1] for pair in heap]

class Solution2:
    # So compared to the previous solution. This is just outright beats it in practical runtime
    # because it only has to sort once, no repeatitive operations like heap pushing and heap popping
    # Basically you first count the numbers, into a counter
    # Then you sort the counter based on the SECOND key, which is the number of elements
    # Then you can just read off the sorted counter, the answer is layed out for you
    # The sorted counter basically have the most frequent element in the front, then read k numbers
    # or if you cut off the list early, just return the whole array, but the second key which is the actual number
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        sorted_c = sorted(c.items(), key=lambda x : x[1], reverse=True)[:k]
        return list(map(lambda x : x[0], sorted_c))

s = Solution()
nums = []
for _ in range(100000):
    nums.append(random.randint(0, 10000))

print(s.topKFrequent(nums, 1))
print(s.topKFrequent(nums, 2))
print(s.topKFrequent(nums, 3))
print(s.topKFrequent(nums, 4))
print(s.topKFrequent(nums, 5))
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(s.topKFrequent([1], 1))
# 1115497 function calls (19342 primitive calls) in 0.005 seconds
# 1014767 function calls (13444 primitive calls) in 0.003 seconds