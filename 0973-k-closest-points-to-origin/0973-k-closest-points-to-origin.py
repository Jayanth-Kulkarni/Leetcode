class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for point in points:
            distance.append([math.pow(point[0],2)+math.pow(point[1],2),point])
        sorted_list= sorted(distance, key=lambda x: x[0])
        res = []
        for i in range(k):
            res.append(sorted_list[i][1])
        return res