class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        memo = {}

        def recurse(id):
            if id == len(jobs):
                return 0
            if id in memo:
                return memo[id]

            cur_st, cur_et, cur_p = jobs[id]
            p_wo_id = recurse(id+1)

            next_id = bisect.bisect(jobs, (cur_et, -1, -1))
            p_w_id = cur_p + recurse(next_id)

            memo[id] = max(p_wo_id, p_w_id)

            return memo[id]
        
        return recurse(0)