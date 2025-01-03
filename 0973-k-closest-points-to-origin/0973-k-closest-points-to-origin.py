class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distances.append([math.pow(point[0],2)+math.pow(point[1],2),point])
        
        sorted_distances = sorted(distances, key=lambda x:x[0])[:k]

        return [distance[1] for distance in sorted_distances]