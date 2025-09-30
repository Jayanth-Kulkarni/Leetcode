class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memo = {}
        res = set(nums)
        max_count = 0
        def dfs(num):
            if num not in res:
                return 0
            
            if num in memo:
                return memo[num]
            memo[num] = 1 + dfs(num+1)
            return memo[num]
        for num in nums:
            max_count = max(max_count, dfs(num))
        
        return max_count