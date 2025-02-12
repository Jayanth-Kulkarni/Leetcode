class MinStack:

    def __init__(self):
        self.l = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if self.min_stack == []:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.l.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()