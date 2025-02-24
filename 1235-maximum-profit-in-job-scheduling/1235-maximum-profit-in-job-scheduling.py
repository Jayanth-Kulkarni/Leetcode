class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        memo = {}
        def find_max(i):
            if i in memo:
                return memo[i]
            if i == len(jobs):
                return 0
            
            # skip this job
            p_wo_i = find_max(i+1)

            st,et,p = jobs[i]
            ni = bisect.bisect(jobs,(et, -1, -1))
            p_w_i = find_max(ni)

            res = max(p_w_i+p, p_wo_i)

            memo[i] = res
            return res
        return find_max(0)