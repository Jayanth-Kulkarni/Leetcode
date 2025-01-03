class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[math.pow(point[0],2) + math.pow(point[1],2),point] for point in points]
        heapq.heapify(distances)
        res = []
        while k > 0:
            d, a =  heapq.heappop(distances)
            res.append(a)
            k -=1
        return res