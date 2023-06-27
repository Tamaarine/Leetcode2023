from typing import *

# Too slow
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = []
        for i, temp in enumerate(temperatures):
            if i > 0 and temp == temperatures[i - 1]:
                if out[-1] == 0:
                    out.append(0)
                else:
                    out.append(out[-1] - 1)
                continue
            
            j = i + 1
            days = 1 # assume that it takes one day to get warmer
            while j < len(temperatures) and temp >= temperatures[j]:
                j += 1
                days += 1
            if j == len(temperatures):
                out.append(0)
            else:
                out.append(days)
        return out

# A much better solution that will only pop when look for the temperature
# when it can, compared to solution 1 which it will search through rest of the
# list regardless. This solution will stop early for [47, 47, 47] case
class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the output array which is all 0 at first
        res = [0] * len(temperatures)
        # Stack will be used to keep track of the temperature you trying to find
        # a warmer temperature for, it has the temperature along with the index 
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                # This means that the temperatures inside the stack
                # have a warmer temperature to compare
                popped = stack.pop()
                res[popped[1]] = i - popped[1]
            # Add it on top of the stack to look for a better temperature
            stack.append((temp, i))
        # If no better temperature found, it will be 0 anyway
        return res
        

s = Solution2()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(s.dailyTemperatures([30,40,50,60]))
print(s.dailyTemperatures([30,60,90]))
print(s.dailyTemperatures([1]))
print(s.dailyTemperatures([1, 0, 2]))
print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
print(s.dailyTemperatures([47, 47, 47]))