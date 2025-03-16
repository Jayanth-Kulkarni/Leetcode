class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        memo = {}
        def findmax(i):
            if i in memo:
                return memo[i]

            if i == len(jobs):
                return 0 
            
            p_wo_i = findmax(i+1)

            st, et, p = jobs[i]
            ni = bisect.bisect(jobs, (et, -1, -1))

            res = max(p_wo_i, findmax(ni) + p)

            memo[i] = res
            return memo[i]
        return findmax(0)
        