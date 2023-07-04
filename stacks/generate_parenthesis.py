from typing import *

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ret = []
        
        def backtrack(left, right):
            if left == right == n:
                ret.append("".join(stack))
                return
            
            if left < n:
                stack.append("(")
                backtrack(left + 1, right)
                stack.pop()
            if right < left:
                # Only close if there are more than enough left. Otherwise, do not close!
                stack.append(")")
                backtrack(left, right + 1)
                stack.pop()
        backtrack(0, 0)
        return ret
        
        
s = Solution()
print(s.generateParenthesis(3))
