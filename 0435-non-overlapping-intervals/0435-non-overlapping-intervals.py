class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= result[-1][1]:
                result.append(intervals[i])
        return len(intervals) - len(result)
            