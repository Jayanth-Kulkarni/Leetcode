class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = defaultdict(int)
        res = set(nums)
        max_count = 0
        def dfs(num):
            if num not in res:
                return 0
            if num in map:
                return map[num]
            count = 1+ dfs(num+1)
            map[num] = count
            return count
        for num in nums:
            max_count = max(max_count, dfs(num))
        return max_count