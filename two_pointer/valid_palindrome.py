from typing import *
from collections import *
import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        table = s.maketrans({ch: "" for ch in string.punctuation + " "})
        s = s.translate(table)
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                return False
        
        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
