class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # loop through all the intervals to figure out where to place the new intervals
        # simple case 1. if beginning of new intervals is after the current intervals, insert current 
        # simple case 2. if the end of the new intervals is before start of current intervals, insert new int
        # Case 3. In all other cases reform the new intervals as min(start), max(end)
        # return
        result = []
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        result.append(newInterval)

        return result