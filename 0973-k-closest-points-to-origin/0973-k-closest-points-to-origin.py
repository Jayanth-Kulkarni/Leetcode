class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[i[0]**2 + i[1]**2, i] for i in points]
        heapq.heapify(distances)
        res = []
        while k:
            res.append(heapq.heappop(distances)[1])
            k -= 1
        return res