from typing import *

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        
        while stack:
            if stack[-1] == popped[i]:
                stack.pop()
            else:
                return False
        
        return True
    
s = Solution()
print(s.validateStackSequences([1, 7, 10], [10, 1, 7]))
print(s.validateStackSequences([1, 7, 10], [1, 7, 10]))
print(s.validateStackSequences([1, 7, 10], [7, 1, 10]))
print(s.validateStackSequences([1, 7, 10], [7, 10, 1]))