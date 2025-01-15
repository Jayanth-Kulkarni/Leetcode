class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            # if new interval is before the current interval, insert new interval to result
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            # if new interval is after the current interval, insert current interval to result
            elif newInterval[0] >  intervals[i][1]:
                result.append(intervals[i])
            # else create a new interval by resizing the window
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        # append the newInterval to result
        result.append(newInterval)
    
        return result
