class MedianFinder:

    def __init__(self):
        self.large, self.small = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, (-1 * num))

        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))


        if len(self.small) > len(self.large):
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))


        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))


    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-1 * self.small[0] + self.large[0])/2

        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        else:
            return self.large[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()