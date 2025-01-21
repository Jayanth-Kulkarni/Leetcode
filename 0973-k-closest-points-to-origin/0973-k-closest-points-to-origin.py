class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[math.pow(point[0], 2) + math.pow(point[1], 2), point] for point in points]
        heapq.heapify(distances)
        result = []
        while k > 0:
            result.append(heapq.heappop(distances)[1])
            k -= 1
        return result