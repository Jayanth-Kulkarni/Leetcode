class MinStack:

    def __init__(self):
        self.queue = []
        self.minval = []

    def push(self, val: int) -> None:
        self.queue.append(val)
        if self.minval == []:
            self.minval.append(val)
        else:
            self.minval.append(min(self.minval[-1], val))

    def pop(self) -> None:
        self.queue.pop()
        self.minval.pop()
        

    def top(self) -> int:
        return self.queue[-1]

    def getMin(self) -> int:
        return self.minval[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()