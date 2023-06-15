from typing import *
from collections import *

class Solution:
    # You got the idea right. However, it is very inefficient
    # consider that you have essentially three loops going
    # You are gathering up the sums in it's own array.
    # But you do not need to!
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums
        left_prod = []
        right_prod = []
        for i, val in enumerate(nums):
            if i == 0:
                left_prod.append(val)
            else:
                left_prod.append(left_prod[-1] * val)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_prod.append(nums[i])
            else:
                right_prod.insert(0, right_prod[0] * nums[i])
        out = [left_prod[i - 1] * right_prod[i + 1] for i in range(1, len(nums) - 1)]
        out.insert(0, right_prod[1])
        out.append(left_prod[-2])
        return out

class Solution2:
    # Instead what we can do is that we can just keep a
    # prefix product and postfix product variable
    # Keep that running product going, and then multiply it
    # to the output array which is just initially 1
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums) # Output array initially all 1, prefix and postfix product will multiply it
        
        # Multiply with every number except last one
        # We are gathering left product now right now
        # For every element
        prefix = 1
        for i in range(len(nums) - 1):
            # Multiply the prefix with the current element
            prefix *= nums[i]
            # Assign it to the element after. It doesn't belong in the current index!
            # In addition, multiply to the existing one. The left one
            # really don't need to multiply but is good to do it anyway
            out[i + 1] = prefix * out[i + 1]
        postfix = 1
        for i in range(len(nums) - 1, 0, -1):
            # For right product, we go from the last element to the first
            # not including the first.
            postfix *= nums[i]
            # Again we assign it to the element after the current one
            out[i - 1] = postfix * out[i - 1]
        return out
            
s = Solution2()
print(s.productExceptSelf([1, 2, 3, 4]))
print(s.productExceptSelf([1]))
print(s.productExceptSelf([]))
