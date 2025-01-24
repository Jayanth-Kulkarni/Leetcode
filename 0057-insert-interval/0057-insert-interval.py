class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for idx, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                return result + intervals[idx:]
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        result.append(newInterval)
    
        return result
