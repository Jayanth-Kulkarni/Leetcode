class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        output = []
        for a,b in points:
            heapq.heappush(res, [(math.pow(a,2) + math.pow(b,2)), [a,b]])
        while k>0:
            output.append(heapq.heappop(res)[1])
            k-=1
        return output