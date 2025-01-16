class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = [[math.pow(point[0], 2) + math.pow(point[1], 2), point] for point in points]
        heapq.heapify(res)
        result = []
        while k > 0:
            distance, point = heapq.heappop(res)
            result.append(point)    
            k -= 1
        return result