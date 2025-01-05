class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Run a for loop, for that item check if newInterval needs to be before or after the item
        # Place the item in that position, in case of overlap -> take the min or first index and max of second index, add it to result and return
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