from typing import *
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "*/+-":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = 0
                if token == "+":
                    res = num1 + num2
                elif token == "-":
                    res = num1 - num2
                elif token == "*":
                    res = num1 * num2
                elif token == "/":
                    math.trunc(num1 / num2)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]

s = Solution()
print(s.evalRPN(
    ['20', '36', '-', '4', '/', '-4', '/']
))