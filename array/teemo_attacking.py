from typing import *

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        seconds = 0
        i = 0
        while i < len(timeSeries):
            j = i + 1
            start_time = timeSeries[i]
            end_time = timeSeries[i] + duration - 1
            while j < len(timeSeries):
                if start_time <= timeSeries[j] <= end_time:
                    end_time = timeSeries[j] + duration - 1
                else:
                    break
                j += 1
            seconds += end_time - start_time + 1
            i = j
        return seconds

s = Solution()
print(s.findPoisonedDuration([1, 2], 2))
print(s.findPoisonedDuration([1, 4], 2))
print(s.findPoisonedDuration([1, 4], 3))
print(s.findPoisonedDuration([1], 500))
