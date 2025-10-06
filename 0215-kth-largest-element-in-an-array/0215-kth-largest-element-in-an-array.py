class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for num in nums:
            heapq.heappush(res, -num)
        while k > 1:
            heapq.heappop(res)
            k -= 1
        return -heapq.heappop(res)