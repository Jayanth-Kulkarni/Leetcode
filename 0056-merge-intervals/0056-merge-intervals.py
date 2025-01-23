class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda i: i[0])
        cur = [intervals[0]]
        for interval in intervals:
            last = cur[-1]
            if last[1] >=  interval[0]:
                cur[-1][1] = max(interval[1], last[1])
            else:
                cur.append(interval)
        return cur