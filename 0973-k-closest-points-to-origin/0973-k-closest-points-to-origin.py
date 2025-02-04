class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [[math.pow(x,2) + math.pow(y,2),[x,y]] for x, y in points]
        heapq.heapify(dist)
        res = []
        while k > 0:
            val = heapq.heappop(dist)
            res.append(val[1])
            k -= 1
        return res