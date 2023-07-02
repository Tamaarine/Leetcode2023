from typing import *

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for position, speed in pairs:
            stack.append((target - position) / speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # This means that a faster car is going to catch up to the car that's in front of it
                # thus being a fleet
                # For example. A car at d=0, traveling s=4, with target of 12, will take 3 seconds to reach destination
                # A car at d=2, traveling at s=1, will take 10 seconds to reach destination
                # But because second car is in front of it it will become a fleet
                # Stack will be
                # 3
                # 10
                # So you will want to pop the 3 off
                stack.pop()
        return len(stack)

        
s = Solution()
print(s.carFleet(20, [10, 8, 3, 5, 1], [1, 2, 3, 4, 5]))
print(s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
