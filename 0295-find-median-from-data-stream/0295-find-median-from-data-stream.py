class MedianFinder:

    def __init__(self):
        self.s, self.l = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.s, -1 * num)
        if self.s and self.l and -1 * self.s[0] > self.l[0]:
            heapq.heappush(self.l, -1 * heapq.heappop(self.s))

        if len(self.s) > len(self.l):
            heapq.heappush(self.l, -1 * heapq.heappop(self.s))
        
        if len(self.l) > len(self.s):
            heapq.heappush(self.s, -1 * heapq.heappop(self.l))

    def findMedian(self) -> float:
        if len(self.s) == len(self.l):
            return (-1 * self.s[0] + self.l[0]) / 2
        elif len(self.s) > len(self.l):
            return -1 * self.s[0]
        else:
            return self.l[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()