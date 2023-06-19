import math
from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            mid_val = nums[mid]
            mid_left_val = nums[mid - 1]
            mid_right_val = nums[mid + 1]
            
            # If there is local increase, then we cannot tell
            # what is the smallest. We need to check which half
            # the smallest number is belong in
            if mid_val > mid_left_val and mid_val < mid_right_val:
                left_val = nums[left]
                right_val = nums[right]
                # If this is true, the mid val is greater than both the
                # leftmost and rightmost, then smallest value lies in right half
                if mid_val > left_val and mid_val > right_val:
                    left = mid + 1
                # If this is true, mid is less than both leftmost and rightmost
                # then the smallest value lies in the left half
                elif mid_val < left_val and mid_val < right_val:
                    right = mid - 1
                # This means that the array has not been rotated, left_val is our smallest
                elif mid_val > left_val and mid_val < right_val:
                    return left_val
            # Special case
            elif mid_left_val > mid_val:
                # [7, 0, 1]
                # mid is the smallest
                return mid_val
            # Special case
            elif mid_val > mid_right_val:
                # [6, 7, 0]
                # mid_right is the smallest
                return mid_right_val
            
        return -1

def rotate_array(nums: List[int], k):
    ret = nums.copy()
    for _ in range(k):
        val = ret.pop(0)
        ret.append(val)
    return ret

s = Solution()
arr = [0, 1, 2, 4, 5, 6, 7]
for i in range(0, len(arr)):
    ret = rotate_array(arr, i)
    print(f"The array is {ret}")
    print(f"The min is {s.findMin(ret)}")

arr = [0, 1, 2]
for i in range(0, len(arr)):
    ret = rotate_array(arr, i)
    print(f"The array is {ret}")
    print(f"The min is {s.findMin(ret)}")

arr = [0, 1, 2, 3]
for i in range(0, len(arr)):
    ret = rotate_array(arr, i)
    print(f"The array is {ret}")
    print(f"The min is {s.findMin(ret)}")
