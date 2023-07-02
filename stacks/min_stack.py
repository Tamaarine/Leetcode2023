class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            if popped == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]

s = MinStack()
s.push(2)
s.push(2)
print(s.top())
print(s.getMin())
s.pop()
print(s.top())
s.pop()
print(s.top())
