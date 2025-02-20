class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        memo = {}

        def find_max_profit(job_id):
            if job_id == len(jobs):
                return 0
            
            if job_id in memo:
                return memo[job_id]

            # get cur job details
            cur_st, cur_et, cur_p = jobs[job_id]
            
            # option 1: skip the current job
            profit_without_current = find_max_profit(job_id + 1)
            
            # option 2: find the next available job and find max profit
            next_job_id = bisect.bisect(jobs, (cur_et, -1, -1))
            profit_with_current = cur_p + find_max_profit(next_job_id)
            
            # calculate max profit
            max_profit = max(profit_with_current, profit_without_current)
            memo[job_id] = max_profit

            return max_profit
        
        return find_max_profit(0)
