class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        distances = [[math.pow(point[0], 2) + math.pow(point[1], 2), point] for point in points]
        heapq.heapify(distances)
        while k > 0:
            distance, point =  heapq.heappop(distances)
            result.append(point)
            k -= 1
        return result