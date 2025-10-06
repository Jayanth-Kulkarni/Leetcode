class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = []
        for stone in stones:
            heapq.heappush(res, -stone)
        while len(res) > 1:
            first, second = -heapq.heappop(res), -heapq.heappop(res)
            if first == second:
                continue
            else:
                heapq.heappush(res, -abs(first-second))
        if res != []:
            return -res[0]
        return 0