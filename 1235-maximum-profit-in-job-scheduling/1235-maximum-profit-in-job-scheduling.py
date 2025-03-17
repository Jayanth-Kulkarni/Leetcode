class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        memo = {}
        job = sorted(zip(startTime, endTime, profit))
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(job):
                return 0
            
            p_wo_i = dfs(i+1)
            st, et, p = job[i]
            ni = bisect.bisect(job, (et, -1, -1))

            res = max(p + dfs(ni), p_wo_i)
            memo[i] = res

            return memo[i]
        return dfs(0)