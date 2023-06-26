from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the list so that we can skip out the duplicates
        nums.sort()
        out = []
        
        for i, v in enumerate(nums):
            # Duplicated element, answer was already found
            if i > 0 and v == nums[i]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                result = nums[l] + nums[r] + v
                if result > 0:
                    r -= 1
                elif result < 0:
                    l += 1
                else:
                    out.append([v, nums[l], nums[r]])
                    
                    # We found an triplet of answer
                    l += 1
                    
                    # Whether we decrement r here does not matter, because if the answer is going to be large
                    # it will be handle by result > 0, we only need to handle decrementing on the left side
                    
                    # We will increment the left side s long as there is duplicates
                    # no need to handle duplicates on the right side because of result > 0
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return out
            
            

s = Solution()
print(s.threeSum([0, 1, -1, 2, -2]))
print(s.threeSum([-1,0,1,2,-1,-4])) # -4, -1, -1, 0, 1, 2