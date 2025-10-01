class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) > 0:
            min_val = min(self.min[-1], val)
        else:
            min_val = val
        self.min.append(min_val)

    def pop(self) -> None:
        if len(self.min) and len(self.stack) > 0:
            self.stack.pop()
            self.min.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min) > 0:
            return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()