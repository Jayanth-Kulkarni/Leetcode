class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [0 for i in range(n+1)]
        nums[0] = 1
        nums[1] = 1
        for i in range(2, len(nums)):
            nums[i] = nums[i-1] + nums[i-2]
        return nums[n]