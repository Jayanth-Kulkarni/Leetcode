class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[math.pow(point[0],2) + math.pow(point[1],2), point] for point in points]
        heapq.heapify(distances)
        res = []
        while k>0:
            dist, point = heapq.heappop(distances)
            res.append(point)
            k-=1
        return res