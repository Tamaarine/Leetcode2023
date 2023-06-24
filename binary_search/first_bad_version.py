# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version >= 2:
        return True
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        lastBadVersion = n
        while left <= right:
            mid = (right - left) // 2 + left
            if isBadVersion(mid):
                # Search in the left, this version is bad
                right = mid - 1
                lastBadVersion = mid
            else:
                # Search in the right, this version is good
                left = mid + 1
        return lastBadVersion

s = Solution()
print(s.firstBadVersion(3))