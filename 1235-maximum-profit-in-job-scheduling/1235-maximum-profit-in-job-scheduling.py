class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine the job information and sort by start time
        jobs = sorted(zip(startTime, endTime, profit))
        
        # Cache to memoize results for each index
        memo = {}
        
        def find_max_profit(current_job_idx: int) -> int:
            """
            Recursively find the maximum profit from current_job_idx onwards.
            For each job, we either:
            1. Skip the current job
            2. Take the current job and find next non-overlapping job
            """
            # Base case: no more jobs to process
            if current_job_idx == len(jobs):
                return 0
                
            # If we've already calculated this subproblem, return cached result
            if current_job_idx in memo:
                return memo[current_job_idx]
            
            current_start, current_end, current_profit = jobs[current_job_idx]
            
            # Option 1: Skip current job and move to next job
            profit_without_current = find_max_profit(current_job_idx + 1)
            
            # Option 2: Take current job and find next non-overlapping job
            # Use bisect to find the first job that starts after current job ends
            next_available_job = bisect.bisect(jobs, (current_end, -1, -1))
            profit_with_current = current_profit + find_max_profit(next_available_job)
            
            # Take maximum of the two options
            max_profit = max(profit_without_current, profit_with_current)
            
            # Cache the result before returning
            memo[current_job_idx] = max_profit
            return max_profit
        
        return find_max_profit(0)