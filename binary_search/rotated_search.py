from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (right - left) // 2 + left
            mid_val = nums[mid]
            left_val = nums[left]
            right_val = nums[right]
            
            if mid_val == target:
                return mid
            elif left_val <= mid_val <= right_val:
                # Proceed with a normal binary search
                if target > mid_val:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # Need to determine which side the target is in
                if mid_val < left_val and mid_val < right_val:
                    # Strictly increasing on the right side
                    if mid_val <= target <= right_val:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    # Strictly increasing on the left side
                    if left_val <= target <= mid_val:
                        right = mid - 1
                    else:
                        left = mid + 1
        
        # Not found
        return -1

def rotate_array(nums: List[int], k):
    ret = nums.copy()
    for _ in range(k):
        val = ret.pop(0)
        ret.append(val)
    return ret

s = Solution()
arr = [0, 1, 2, 4, 5, 6, 7]
target = 8
for i in range(len(arr)):
    ret = rotate_array(arr, i)
    print(ret)
    print(f"Searching for {target}")
    print(s.search(ret, target))
