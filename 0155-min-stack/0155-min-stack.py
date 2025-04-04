class MinStack:

    def __init__(self):
        self.l = []
        self.min = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if self.min == []:
            self.min.append(val)
        else:
            min_val = min(self.min[-1], val)
            self.min.append(min_val)

    def pop(self) -> None:
        self.l.pop()
        self.min.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()