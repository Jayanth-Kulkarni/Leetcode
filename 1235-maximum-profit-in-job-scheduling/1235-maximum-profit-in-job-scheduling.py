class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        max_profit = 0
        memo = {}
        def find_max(i):
            if i in memo:
                return memo[i]
            if i >= len(jobs):
                return 0
            # skip to next job
            p_wo_i = find_max(i+1)

            s,e,p = jobs[i]
            
            # find next job with current job
            n_i = bisect.bisect(jobs, (e, -1, -1))
            p_w_i = find_max(n_i)

            max_profit = max(p_wo_i, p + p_w_i)
            memo[i] = max_profit
            return memo[i]

        return find_max(0)